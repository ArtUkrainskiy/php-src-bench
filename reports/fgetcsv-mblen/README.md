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

When the locale uses ASCII characters as singletons — `CG(ascii_compatible_locale)`, the flag
`php_basename()` already relies on: C, single-byte and UTF-8 locales — a byte below 0x80 is one
character and `php_mblen()` returns 1 for it without calling `mbrlen()`. That is read once per
string, in `php_mb_reset()`. Other locales — CJK, ISO-2022 where a libc offers it — keep going
through `mbrlen()` with the state held across the string, as ZTS builds always did. A decoder
that flushes a buffered character without consuming input (glibc's BIG5-HKSCS, CP1255,
JIS X 0213 and TSCII return 0 for a non-NUL byte there) is decoded again from the initial
state, since every caller reads a 0 as end of input.

## Numbers

Release build, `mblen-bench.php`, best of 5, ns per row or per call. Data from `gen-data.php`
(20,000 rows; "plain" 10 unquoted fields, "quoted" 10 fields with ~30% enclosed, "wide" 50 fields).

| | master | patched |
|---|---|---|
| `fgetcsv()` plain | 4,217 | 515 |
| `fgetcsv()` quoted | 2,558 | 354 |
| `fgetcsv()` wide | 20,775 | 2,241 |
| `str_getcsv()` plain | 4,131 | 458 |
| `str_getcsv()` wide | 20,583 | 2,068 |
| `escapeshellarg()` 24-byte path | 310 | 48 |
| `escapeshellarg()` 128 bytes | 1,573 | 115 |
| `escapeshellarg()` 128 bytes, `ja_JP.SJIS` (old path) | 1,400 | 1,368 |
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
`vi_VN.CP1258`, `en_US.EBCDIC-US`. Identical in the first sixteen. glibc's TCVN5712-1 and CP1258
decoders buffer an ASCII letter to merge it with a following tone mark, so master counted `a|`
as one character and `escapeshellcmd()` copied the `|` through: CP1258 is single-byte, so the
letter is now counted on its own and the `|` escaped (2,544 of the ~6,500 inputs); TCVN is
two-byte, so it keeps the slow path with the state held across the string, as ZTS did (230
inputs). EBCDIC-US is not ASCII-compatible and undefined bytes below
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
