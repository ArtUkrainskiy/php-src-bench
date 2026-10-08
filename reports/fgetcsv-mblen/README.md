# php_mblen(): skip mbrlen() for ASCII bytes

`fgetcsv()`, `str_getcsv()`, `escapeshellarg()` and `escapeshellcmd()` walk their input with
`php_mblen()`, one call per byte. On glibc that is `mblen()`/`mbrlen()` → `mbrtowc` → gconv.
Callgrind on a `fgetcsv()` loop over 20,000 rows of 10 ASCII fields, master `1d397fcd57f`,
release build:

| function | share of instructions |
|---|---|
| `mbrtowc` + `__gconv_transform_utf8_internal` + `mblen` | 83% |
| `php_fgetcsv_lookup_trailing_spaces` | 5% |
| `php_fgetcsv` | 3% |

Every charset a libc can use for `LC_CTYPE` is ASCII-compatible, so in an encoding without shift
states a byte below 0x80 is one character and `php_mblen()` returns 1 for it without calling
`mbrlen()`. Whether the encoding has shift states is read once per string, in `php_mb_reset()`,
with `mblen(NULL, 0)` (C99 7.20.7.1); glibc reports 1 for BIG5-HKSCS, CP1255, EUC/SHIFT_JISX0213,
TCVN5712-1, CP1258 and TSCII (decoders that buffer output), 0 for everything else. State-dependent
encodings keep going through `mbrlen()` with the state held across the string, as ZTS builds
always did, and a decoder that flushes a buffered character without consuming input is retried
from the initial state, since every caller reads a 0 as end of input.

## Numbers

Release build, `mblen-bench.php`, best of 5, ns per row or per call. Data from `gen-data.php`
(20,000 rows; "plain" 10 unquoted fields, "quoted" 10 fields with ~30% enclosed, "wide" 50 fields).

| | master | patched |
|---|---|---|
| `fgetcsv()` plain | 4,222 | 483 |
| `fgetcsv()` quoted | 2,557 | 348 |
| `fgetcsv()` wide | 20,753 | 2,142 |
| `str_getcsv()` plain | 4,094 | 445 |
| `str_getcsv()` wide | 20,508 | 2,040 |
| `escapeshellarg()` 24-byte path | 311 | 49 |
| `escapeshellarg()` 128 bytes | 1,573 | 114 |
| `escapeshellarg()` 26 bytes of UTF-8 Cyrillic | 234 | 160 |
| `basename()` | 19 | 19 |

`basename()` has its own ASCII path when the locale is `C` and is not affected.

## State between calls

NTS builds used glibc's `mblen()`, which starts from the initial state on every call; ZTS and
Windows builds used `mbrlen()` with `BG(mblen_state)`. Both now use `BG(mblen_state)`, reset by
`php_mb_reset()` at the start of every string in every caller (`escapeshellarg()`/
`escapeshellcmd()` did not reset it before) and after an invalid sequence.

## Verification

`mbfuzz.php` runs every `php_mblen()` user (`str_getcsv` with three dialects, `fgetcsv`,
`escapeshellarg`, `escapeshellcmd`, `basename`, `pathinfo`) over 5,000 random strings mixing lead
bytes, lead + ASCII-special trail bytes, lone high bytes and ASCII specials, and prints the hex
of every result. Output is compared between master NTS, patched NTS and patched ZTS builds in 19 glibc
locales: `C`, `C.UTF-8`, `en_US.UTF-8`, `ja_JP.SJIS`, `zh_CN.GBK`, `ja_JP.EUC-JP`, `zh_TW.BIG5`,
`zh_CN.GB18030`, `zh_TW.EUC-TW`, `ko_KR.EUC-KR`, `zh_HK.BIG5-HKSCS`, `yi_US.CP1255`,
`ja_JP.EUC-JISX0213`, `ja_JP.SHIFT_JISX0213`, `ta_IN.TSCII`, `en_US.IBM1047`, `vi_VN.TCVN`,
`vi_VN.CP1258`, `en_US.EBCDIC-US`. Identical in the first sixteen. TCVN5712-1 and CP1258 are
state-dependent in glibc (an ASCII letter is buffered to merge with a following tone mark);
master NTS decoded them with a fresh state per character and ZTS with the state kept, the patch
keeps it on both, so 230 and 508 of the ~6,500 inputs (a letter directly before a metacharacter)
now give the ZTS result on NTS. EBCDIC-US is not ASCII-compatible and undefined bytes below
0x80 were invalid before; nothing runs PHP in it. The locales are built without root:

```
mkdir locales
localedef -f SHIFT_JIS -i ja_JP locales/ja_JP.SJIS
localedef -f GBK       -i zh_CN locales/zh_CN.GBK
localedef -f EUC-JP    -i ja_JP locales/ja_JP.EUC-JP
localedef -f BIG5      -i zh_TW locales/zh_TW.BIG5
LOCPATH=$PWD/locales php -n mbfuzz.php ja_JP.SJIS 5000 > sjis.master.txt   # per build, then cmp
```

About 4,900 of the 5,000 lines differ between the SJIS and C runs of the same build, so the
inputs do exercise the locale-dependent paths.

## Files

- `mblen-bench.php` — the timings above; expects `data/` from `gen-data.php <dir>`
- `mbfuzz.php <locale> [n]` — the differential run
