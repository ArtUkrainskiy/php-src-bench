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

In the initial shift state a byte below 0x80 is a complete character in every multibyte charset
a locale can use — UTF-8, EUC-*, Shift_JIS, GBK, GB18030 and Big5 all have their lead bytes at
0x80 and above — so `php_mblen()` returns 1 for such a byte without calling `mbrlen()`.

## Numbers

Release build, `mblen-bench.php`, best of 5, ns per row or per call. Data from `gen-data.php`
(20,000 rows; "plain" 10 unquoted fields, "quoted" 10 fields with ~30% enclosed, "wide" 50 fields).

| | master | patched |
|---|---|---|
| `fgetcsv()` plain | 4,196 | 449 |
| `fgetcsv()` quoted | 2,561 | 325 |
| `fgetcsv()` wide | 20,664 | 1,968 |
| `str_getcsv()` plain | 4,093 | 408 |
| `str_getcsv()` wide | 20,513 | 1,854 |
| `escapeshellarg()` 24-byte path | 311 | 33 |
| `escapeshellarg()` 128 bytes | 1,512 | 77 |
| `escapeshellarg()` 26 bytes of UTF-8 Cyrillic | 233 | 149 |
| `basename()` | 19 | 19 |

`basename()` has its own ASCII path when the locale is `C` and is not affected.

## State between calls

`php_mblen()` starts every call from the initial shift state, as glibc's `mblen()` did for NTS
builds; the `mbstate_t` in the basic globals and the `php_mb_reset()` calls are gone, and ZTS
builds behave like NTS.

## Verification

`mbfuzz.php` runs every `php_mblen()` user (`str_getcsv` with three dialects, `fgetcsv`,
`escapeshellarg`, `escapeshellcmd`, `basename`, `pathinfo`) over 5,000 random strings mixing lead
bytes, lead + ASCII-special trail bytes, lone high bytes and ASCII specials, and prints the hex
of every result. Output is compared between master NTS, patched NTS and patched ZTS builds in 19 glibc
locales: `C`, `C.UTF-8`, `en_US.UTF-8`, `ja_JP.SJIS`, `zh_CN.GBK`, `ja_JP.EUC-JP`, `zh_TW.BIG5`,
`zh_CN.GB18030`, `zh_TW.EUC-TW`, `ko_KR.EUC-KR`, `zh_HK.BIG5-HKSCS`, `yi_US.CP1255`,
`ja_JP.EUC-JISX0213`, `ja_JP.SHIFT_JISX0213`, `ta_IN.TSCII`, `en_US.IBM1047`, `vi_VN.TCVN`,
`vi_VN.CP1258`, `en_US.EBCDIC-US`. Identical in the first sixteen. In TCVN5712-1 and CP1258
glibc's decoder buffers an ASCII letter to merge it with a following tone mark into one
precomposed character; the patch counts the letter on its own, which changes where
`escapeshellcmd()` looks for metacharacters in such input. EBCDIC-US is not ASCII-compatible and undefined bytes below
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
