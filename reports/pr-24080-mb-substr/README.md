# mb_substr() fast path for strings known to be valid UTF-8 (php-src PR #24080)

Review material for [php/php-src#24080](https://github.com/php/php-src/pull/24080) by kamil-tekiela, "ext/mbstring: Optimize valid UTF-8 in mb_substr()". PR head [`b218ba6b8d2`](https://github.com/php/php-src/pull/24080/commits/b218ba6b8d25c0e3e44e5ec693a0edffff7d8ff6), merged onto master [`1c9242e7fec`](https://github.com/php/php-src/commit/1c9242e7fec) without conflicts. Measured and checked on 16 October 2026.

For a string that carries the valid-UTF-8 flag (`IS_STR_VALID_UTF8`), the PR has `mb_get_substr()` find the start and the end of the slice by counting non-continuation bytes, 256 bytes at a time with `mb_fast_strlen_utf8()`, and copy the bytes, instead of decoding the string to code points and encoding them again. `offset_to_pointer_utf8()`, which `mb_strpos()` and its variants use to find the offset, gets the same chunked count for flagged strings.

## Summary

- **Correctness issue: the UTF-8-Mobile encodings.** The new path is taken for every encoding that `php_mb_is_no_encoding_utf8()` accepts, which includes `UTF-8-Mobile#DOCOMO`, `#KDDI-A`, `#KDDI-B` and `#SOFTBANK`. For those, master decodes and encodes again, which turns for example U+00AE (`c2 ae`) into the carrier's code point (`ee 9c b6` for DOCOMO). With the PR, the result depends on whether the string was checked before: the same call returns `ee9cb6` and then `c2ae` once a negative offset (which counts the length and sets the flag) or `mb_check_encoding()` has run on the string ([`repro.php`](repro.php), [`repro-output.txt`](repro-output.txt)). Limiting the path to `enc == &mbfl_encoding_utf8` ([`fix.diff`](fix.diff)) makes the output the same as master in every case below.
- **Speed, strings with the flag:** 23–57% fewer cycles for the first 10 characters of a 31–49-byte title, 34–87% for 20 characters from the middle of 1 KB of text, 90–98% for 64 KB; `mb_strpos()` with an offset in the middle 38–43% (1 KB) and 83–85% (64 KB).
- **Speed, strings without the flag:** −4 … +2%, master against master in the same series −1 … +2%.
- **Differential test:** UTF-8 and other encodings give the same output as master on all four compilers and under ASan/UBSan; every UTF-8-Mobile difference comes from the issue above.
- **Tests:** `ext/mbstring/tests` pass with the PR, so they do not catch the UTF-8-Mobile issue; of seven other deliberate mutations they also miss two in the chunk loop and one in the reverse search (which the differential test misses too). One short test catches the UTF-8-Mobile issue and the two chunk-loop mutations ([below](#tests)).
- **Not checked:** AMD, 32-bit builds, the fix variant's speed (its UTF-8 path is the PR's code; only the condition differs), mbregex (configured out, 88 of 427 tests skipped).

## Results

Change in CPU cycles per call with the PR, relative to master (negative = fewer cycles, faster). Intel i7-13700H, flags of the official Docker image, one column per compiler, median of five alternating runs; the second column is master's cost for scale. "Checked" strings went through `mb_check_encoding($s, 'UTF-8')` once before the loop, as after `preg_match()` with `/u`; the last two rows did not:

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 |
|---|--:|--:|--:|--:|--:|
| `mb_substr($s, 0, 10)`, 31-byte English title | 200 | −34% | −23% | −35% | −44% |
| `mb_substr($s, 0, 10)`, 49-byte Russian title | 277 | −39% | −40% | −57% | −57% |
| `mb_substr($s, $half, 20)`, English text, 1 KB | 1,373 | −82% | −80% | −87% | −87% |
| `mb_substr($s, $half, 20)`, Russian text, 1 KB | 1,725 | −44% | −46% | −70% | −72% |
| `mb_substr($s, $half, 20)`, Chinese text, 1 KB | 2,833 | −38% | −34% | −50% | −56% |
| `mb_substr($s, $half, 20)`, text with emoji, 1 KB | 1,989 | −51% | −47% | −67% | −68% |
| `mb_substr($s, -20)`, Russian text, 1 KB | 2,767 | −63% | −63% | −77% | −78% |
| `mb_substr($s, 0, $half)`, Russian text, 1 KB | 2,818 | −69% | −65% | −81% | −82% |
| `mb_strpos($s, $needle, $half)`, Russian text, 1 KB | 6,369 | −38% | −39% | −38% | −43% |
| `mb_substr($s, $half, 20)`, English text, 64 KB | 63,477 | −91% | −90% | −95% | −95% |
| `mb_substr($s, $half, 20)`, Russian text, 64 KB | 166,045 | −96% | −96% | −98% | −98% |
| `mb_substr($s, -20)`, Russian text, 64 KB | 395,800 | −96% | −95% | −98% | −97% |
| `mb_strpos($s, $needle, $half)`, Russian text, 64 KB | 238,180 | −83% | −83% | −84% | −85% |
| `mb_substr($s, $half, 20)`, Russian text, 1 KB, not checked | 1,741 | +1% | +1% | −1% | +1% |
| `mb_substr($s, 0, 10)`, 49-byte Russian title, not checked | 268 | −4% | +2% | −1% | +1% |

`$half` is half the length in characters, `$needle` 6 characters near the end. A negative offset makes `mb_substr()` count the length first, which checks the string and sets the flag, so `mb_substr($s, -20)` takes the new path whether or not the string was checked before.

Full table, with the range over the five passes and the change in instructions:

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | instructions |
|---|--:|--:|--:|--:|--:|--:|
| `mb_substr($s, 0, 10)`, 31-byte English title | 200 | −34% (−37 … −33) | −23% (−23 … +7) | −35% (−56 … −24) | −44% (−49 … −39) | −43% … −38% |
| `mb_substr($s, 0, 10)`, 49-byte Russian title | 277 | −39% (−40 … −38) | −40% (−43 … −38) | −57% (−60 … −53) | −57% (−58 … −26) | −61% … −57% |
| `mb_substr($s, $half, 20)`, English text, 1 KB | 1,373 | −82% (−83 … −81) | −80% (−82 … −79) | −87% (−88 … −82) | −87% (−88 … −86) | −88% … −85% |
| `mb_substr($s, $half, 20)`, Russian text, 1 KB | 1,725 | −44% (−45 … −43) | −46% (−47 … −44) | −70% (−71 … −70) | −72% (−74 … −71) | −74% … −69% |
| `mb_substr($s, $half, 20)`, Chinese text, 1 KB | 2,833 | −38% (−38 … −35) | −34% (−36 … −31) | −50% (−51 … −49) | −56% (−56 … −55) | −71% … −59% |
| `mb_substr($s, $half, 20)`, text with emoji, 1 KB | 1,989 | −51% (−51 … −50) | −47% (−48 … −47) | −67% (−69 … −66) | −68% (−69 … −67) | −70% … −63% |
| `mb_substr($s, -20)`, Russian text, 1 KB | 2,767 | −63% (−66 … −62) | −63% (−63 … −61) | −77% (−78 … −76) | −78% (−79 … −78) | −80% … −76% |
| `mb_substr($s, 0, $half)`, Russian text, 1 KB | 2,818 | −69% (−70 … −68) | −65% (−66 … −64) | −81% (−82 … −80) | −82% (−83 … −80) | −84% … −81% |
| `mb_strpos($s, $needle, $half)`, Russian text, 1 KB | 6,369 | −38% (−39 … −38) | −39% (−40 … −37) | −38% (−39 … −38) | −43% (−43 … −42) | −5% … +5% |
| `mb_substr($s, $half, 20)`, English text, 64 KB | 63,477 | −91% (−93 … −90) | −90% (−92 … −88) | −95% (−96 … −89) | −95% (−95 … −94) | −95% … −92% |
| `mb_substr($s, $half, 20)`, Russian text, 64 KB | 166,045 | −96% (−96 … −95) | −96% (−96 … −95) | −98% (−98 … −98) | −98% (−98 … −97) | −95% … −93% |
| `mb_substr($s, -20)`, Russian text, 64 KB | 395,800 | −96% (−96 … −96) | −95% (−96 … −94) | −98% (−98 … −96) | −97% (−99 … −96) | −92% … −89% |
| `mb_strpos($s, $needle, $half)`, Russian text, 64 KB | 238,180 | −83% (−85 … −83) | −83% (−84 … −83) | −84% (−85 … −83) | −85% (−85 … −84) | −57% … −49% |
| `mb_substr($s, $half, 20)`, Russian text, 1 KB, not checked | 1,741 | +1% (−1 … +2) | +1% (−1 … +1) | −1% (−2 … 0) | +1% (−2 … +2) | 0% |
| `mb_substr($s, 0, 10)`, 49-byte Russian title, not checked | 268 | −4% (−5 … −3) | +2% (+1 … +2) | −1% (−2 … +2) | +1% (0 … +2) | +1% |

Master against master, GCC 13.3, at the start and at the end of the series: medians −1 … +2% on every row.

## The UTF-8-Mobile encodings

`php_mb_is_no_encoding_utf8()` is true for `UTF-8` and the four `UTF-8-Mobile` variants. The variants are byte-for-byte UTF-8, but their decoders and encoders map some code points to the carriers' private-use emoji. Since [`ec348a12d11`](https://github.com/php/php-src/commit/ec348a12d11) (PHP 8.3.2, "Character indices used by mb_strpos and mb_substr have same meaning, even on invalid strings"), `mb_substr()` decodes and encodes again for all of them, so on master `mb_substr("a®b", 1, 1, 'UTF-8-Mobile#DOCOMO')` is `ee9cb6`, flag or not. Before that commit `mb_substr()` used the encoding's `mblen_table` and copied bytes, which gave `c2ae` (the PHP 8.2 and 8.3.0–8.3.1 output that the author's fuzzer found and youkidearitai bisected to that commit in the PR discussion).

With the PR, a flagged string takes the copying path for the variants too:

```php
$s = str_repeat("a\u{AE}b", 2);
var_dump(bin2hex(mb_substr($s, 1, 1, 'UTF-8-Mobile#DOCOMO')));
mb_substr($s, -1, null, 'UTF-8-Mobile#DOCOMO'); // counts the length, which marks $s as valid UTF-8
var_dump(bin2hex(mb_substr($s, 1, 1, 'UTF-8-Mobile#DOCOMO')));
```

Master and the fix print `"ee9cb6"` twice; the PR prints `"ee9cb6"` and then `"c2ae"`.

Over the differential test below, 64–73% of the UTF-8-Mobile lines differ from master with the PR, flagged or not: unflagged lines differ through calls that count the length first and so set the flag (a negative offset or length in `mb_substr()`, a non-zero start in `mb_strimwidth()`). With the condition `enc == &mbfl_encoding_utf8` none do.

On master the mbstring functions already disagree for these encodings: `mb_str_split()` and `mb_strcut()` return the input bytes, `mb_substr()`, `mb_strstr()` and `mb_convert_encoding()` encode again ([`mobile-consistency.php`](mobile-consistency.php), all four variants, [`mobile-consistency-master.txt`](mobile-consistency-master.txt)). Which of the two is right for the variants is a separate question; this PR changes `mb_substr()` only for flagged strings, which makes its output depend on earlier calls.

## Differential test

[`difftest.php`](difftest.php) generates strings from 1-, 2-, 3- and 4-byte characters, including the carriers' private-use ranges, `®`, `©`, flags, keycaps, combining marks and 10% invalid strings (stray continuation bytes, truncated and overlong sequences, surrogates), from empty to about 3,000 characters, many of them 255–257, 511–513, 768 or 1,024–1,025 characters long (around multiples of the 256-byte chunk), and calls the functions that go through `mb_get_substr()` or `mb_find_strpos()` on the string: `mb_substr()` with 6 offsets × 13 lengths, `mb_strpos()`, `mb_strrpos()`, `mb_stripos()`, `mb_strripos()`, `mb_strimwidth()`, `mb_strstr()`, `mb_strrchr()`, `mb_stristr()`, `mb_strrichr()`, `mb_ucfirst()`, `mb_lcfirst()`, `mb_trim()`, `mb_ltrim()`, `mb_rtrim()`, `mb_strlen()` (`mb_str_pad()` is called too, but it takes the new path only for the pad string, which here is a literal and never flagged). Each call gets a fresh copy of the string, unflagged and flagged, in UTF-8 and the four UTF-8-Mobile encodings; `mb_strpos()`, `mb_stripos()`, `mb_strrpos()` and `mb_substr()` also run on the string converted to SJIS, UTF-16LE, ISO-8859-1 and EUC-JP. One line per case and encoding holds the md5 of all results.

| builds | cases | UTF-8, other encodings | UTF-8-Mobile |
|---|--:|---|---|
| PR, GCC 13.3, seeds 1 and 2 | 40,000 | same as master | 65–72% of lines differ |
| PR, GCC 14.2, clang 18.1, clang 20.1, seed 3 | 10,000 each | same as master | 64–73% of lines differ |
| PR, clang 18.1 ASan/UBSan (`USE_ZEND_ALLOC=0`), seed 4 | 3,000 | same as master, no reports | 66–73% of lines differ |
| fix, GCC 13.3, seeds 1 and 2 | 40,000 | same as master | same as master |
| fix, clang 18.1 ASan/UBSan, seed 4 | 3,000 | same as master, no reports | same as master |

Counts per encoding: [`dt-summary.txt`](dt-summary.txt). Master gives the same output with all four compilers (seed 3). The ASan builds are compared with master built with GCC 13.3.

## Code

- `mb_get_substr()`, the condition `php_mb_is_no_encoding_utf8(enc->no_encoding)` (`mbstring.c:2205` at the PR head): `enc == &mbfl_encoding_utf8` keeps the UTF-8-Mobile variants on the decoding path. `mb_get_strlen()` and `mb_find_strpos()` can keep `php_mb_is_no_encoding_utf8()`: they count characters or compare bytes and do not change them, and the differential test shows no difference there.
- `GC_ADD_FLAGS(result, IS_STR_VALID_UTF8)` on the result means a slice of a checked string stays checked, so chained `mb_substr()` calls keep the fast path.
- The chunk loop subtracts at most 256 per chunk and runs only while `offset > 256`, so the offset never goes below zero; a chunk may end inside a character, and the byte loop after it skips the continuation bytes. Reading this, I found no problem with the `offset == 0 ? end : NULL` return, the `len < end - start` shortcut or the `zend_string_init_fast()` result for 0 and 1 bytes (interned, not flagged).
- Strings without the flag and with non-negative offsets still decode. Checking them with `mb_check_str_encoding()` first would be a pass over the whole string even when only the first characters are needed; I did not measure that.

## Tests

`ext/mbstring/tests` (339 passed, 88 skipped without mbregex, [`tests-mbstring-pr.txt`](tests-mbstring-pr.txt)) pass with the PR. [`mutate.py`](mutate.py) applies eight mutations to the fixed variant, one at a time ([`mutate-output.txt`](mutate-output.txt)):

| mutation | difftest | `ext/mbstring/tests` |
|---|---|---|
| UTF-8-Mobile variants take the fast path (the PR as it is) | caught | missed |
| unflagged strings take the fast path | caught | caught (2) |
| chunk loop runs while `offset > 0` | caught | missed |
| chunk step 255 bytes instead of 256 | caught | missed |
| only ASCII bytes counted as characters | caught | caught (5) |
| offset past the end returns the end | caught | caught (1) |
| result one character short | caught | caught (5) |
| reverse search with a negative offset uses the fast path for unflagged strings | missed | missed |

The last one changes the end of the `mb_strrpos()` search range only for invalid strings with a negative offset; the differential test does not catch it, and I did not look for an input where the result changes.

[`mb_substr_valid_utf8.phpt`](mb_substr_valid_utf8.phpt) compares flagged and unflagged strings around 256-byte chunks and checks the UTF-8-Mobile result before and after the flag; it fails with the PR and passes on master and with the fix, and it catches the three mutations the existing tests miss ([`mutate-proposed-output.txt`](mutate-proposed-output.txt)).

## Reproduce

From the repository root, with a php-src checkout that has master `1c9242e7fec`, the PR merged onto it and the fix on top (`git fetch origin pull/24080/head`, merge, apply [`fix.diff`](fix.diff)):

```
cd reports/pr-24080-mb-substr
PHP_SRC=<php-src> ./build.sh gcc g13 base 1c9242e7fec          # and pr, fix; gcc-14 g14, clang c18, clang-20 c20
PHP_SRC=<php-src> ./build.sh clang c18 asan <pr commit> asan     # and fixasan
BENCH_BUILDS=<builds> ./difftest-run.sh
BENCH_BUILDS=<builds> CPU=2 PASSES=5 ./pairs-run.sh out.txt aa:g13-base:g13-base g13:g13-base:g13-pr g14:g14-base:g14-pr c18:c18-base:c18-pr c20:c20-base:c20-pr aa2:g13-base:g13-base
mapfile -t R < rows.txt; python3 speedup-table.py out.txt 'g13:GCC 13.3,g14:GCC 14.2,c18:clang 18.1,c20:clang 20.1' "${R[@]}"
```

The series in this report is [`intel-docker-20261016.txt`](intel-docker-20261016.txt) (lines: group, side, case, cycles, instructions per call).
