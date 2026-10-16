# mb_substr() fast path for strings known to be valid UTF-8 (php-src PR #24080)

Review material for [php/php-src#24080](https://github.com/php/php-src/pull/24080) by kamil-tekiela, "ext/mbstring: Optimize valid UTF-8 in mb_substr()". Measured and checked on 16 October 2026 on master [`1c9242e7fec`](https://github.com/php/php-src/commit/1c9242e7fec).

- The first version, head [`b218ba6b8d2`](https://github.com/php/php-src/pull/24080/commits/b218ba6b8d25c0e3e44e5ec693a0edffff7d8ff6), took the new path for the UTF-8-Mobile encodings too ([below](#the-utf-8-mobile-encodings)).
- The current head, [`6d9250e8b74`](https://github.com/php/php-src/pull/24080/commits/6d9250e8b747cb785b54d3799b8c5a93f76598e6) "Restrict optimization to only UTF-8", limits it to UTF-8. Merged onto `1c9242e7fec` it gives the same tree as the first version plus [`fix.diff`](fix.diff), which is what the differential test and the mutations below call "the fix". The speed tables are for the current head.

For a string that carries the valid-UTF-8 flag (`IS_STR_VALID_UTF8`), the PR has `mb_get_substr()` find the start and the end of the slice by counting non-continuation bytes, 256 bytes at a time with `mb_fast_strlen_utf8()`, and copy the bytes, instead of decoding the string to code points and encoding them again. `offset_to_pointer_utf8()`, which `mb_strpos()` and its variants use to find the offset, gets the same chunked count for flagged strings.

## Summary

- **Correctness: fixed in the current head.** The first version took the new path for every encoding that `php_mb_is_no_encoding_utf8()` accepts, including `UTF-8-Mobile#DOCOMO`, `#KDDI-A`, `#KDDI-B` and `#SOFTBANK`, so their output depended on whether the string had been checked before. The current head takes it only for `UTF-8`; its output is the same as master's in every case below.
- **Speed, strings with the valid-UTF-8 flag**, the same calls in nine languages: 21–68% fewer cycles for the first 10 characters of a title, 90–98% for 20 characters from the middle of 64 KB. From the middle of 1 KB it depends on the bytes per character: 81–87% in English, 32–76% in Spanish, Russian, Arabic, Korean and with emoji, 28–56% in Chinese and Japanese, 10–43% in Hindi.
- **Speed, strings without the flag:** −1 … +4% on all four compilers, with 6–18 more instructions per call. Master against master in the same series: −2 … +3%.
- **Differential test:** UTF-8 and other encodings give the same output as master with the first version on all four compilers and under ASan/UBSan, and with the fix on GCC 13.3 and under ASan/UBSan; the UTF-8-Mobile differences of the first version are gone with the fix.
- **Tests:** the PR adds none, and `ext/mbstring/tests` pass with the first version, so they do not catch the UTF-8-Mobile issue; of seven other deliberate mutations they also miss two in the chunk loop and one in the reverse search (which the differential test misses too). One short test catches the UTF-8-Mobile issue and the two chunk-loop mutations ([below](#tests)).
- **Not checked:** AMD, 32-bit builds, mbregex (configured out; 80 of the 88 skipped tests of 427), the 7 tests that need the CGI binary and 1 that needs iconv.

## Results

Change in CPU cycles per call with the current head, relative to master (negative = fewer cycles, faster). Intel i7-13700H, flags of the official Docker image, one column per compiler, median of five alternating runs; the second column is master's cost for scale.

The PR only changes strings that carry PHP's internal valid-UTF-8 flag. A string gets it when a function has checked the whole string: `mb_check_encoding($s, 'UTF-8')`, `mb_strlen()`, `preg_match()`/`preg_match_all()` with `/u` from offset 0, or `mb_substr()` with a negative offset or length (it counts the length first). The rows below run on a string that went through `mb_check_encoding()` once before the loop, except the three rows marked "without the flag", which show the unchanged path.

Each language gets the same three calls on generated text (`corpus/` in this repository); B/char is the bytes per character of that input. The other call shapes run on English. `$half` is half the length in characters, `$needle` 6 characters near the end.

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 |
|---|--:|--:|--:|--:|--:|
| `mb_substr($s, 0, 10)`, English (1.00 B/char), 31-byte title | 200 | −33% | −21% | −46% | −47% |
| `mb_substr($s, $half, 20)`, English (1.00 B/char), 1 KB | 1,366 | −82% | −81% | −87% | −87% |
| `mb_substr($s, $half, 20)`, English (1.00 B/char), 64 KB | 63,324 | −92% | −90% | −95% | −95% |
| `mb_substr($s, 0, 10)`, Spanish (1.00 B/char), 37-byte title | 210 | −37% | −25% | −47% | −50% |
| `mb_substr($s, $half, 20)`, Spanish (1.04 B/char), 1 KB | 1,620 | −63% | −57% | −76% | −71% |
| `mb_substr($s, $half, 20)`, Spanish (1.03 B/char), 64 KB | 89,136 | −94% | −92% | −97% | −97% |
| `mb_substr($s, 0, 10)`, Russian (1.81 B/char), 49-byte title | 275 | −37% | −40% | −58% | −56% |
| `mb_substr($s, $half, 20)`, Russian (1.78 B/char), 1 KB | 1,720 | −44% | −44% | −70% | −72% |
| `mb_substr($s, $half, 20)`, Russian (1.77 B/char), 64 KB | 165,015 | −96% | −96% | −98% | −98% |
| `mb_substr($s, 0, 10)`, Arabic (1.75 B/char), 56-byte title | 302 | −45% | −45% | −60% | −60% |
| `mb_substr($s, $half, 20)`, Arabic (1.74 B/char), 1 KB | 1,868 | −43% | −42% | −70% | −68% |
| `mb_substr($s, $half, 20)`, Arabic (1.76 B/char), 64 KB | 158,923 | −96% | −96% | −98% | −98% |
| `mb_substr($s, 0, 10)`, Hindi (2.61 B/char), 94-byte title | 475 | −60% | −60% | −67% | −68% |
| `mb_substr($s, $half, 20)`, Hindi (2.54 B/char), 1 KB | 2,191 | −18% | −10% | −43% | −43% |
| `mb_substr($s, $half, 20)`, Hindi (2.54 B/char), 64 KB | 180,592 | −96% | −95% | −98% | −97% |
| `mb_substr($s, 0, 10)`, Chinese (3.00 B/char), 54-byte title | 389 | −46% | −46% | −58% | −58% |
| `mb_substr($s, $half, 20)`, Chinese (2.89 B/char), 1 KB | 2,830 | −47% | −34% | −51% | −56% |
| `mb_substr($s, $half, 20)`, Chinese (2.89 B/char), 64 KB | 119,904 | −94% | −93% | −96% | −97% |
| `mb_substr($s, 0, 10)`, Japanese (3.00 B/char), 63-byte title | 406 | −49% | −48% | −61% | −61% |
| `mb_substr($s, $half, 20)`, Japanese (2.91 B/char), 1 KB | 2,749 | −48% | −28% | −50% | −56% |
| `mb_substr($s, $half, 20)`, Japanese (2.88 B/char), 64 KB | 122,395 | −95% | −93% | −97% | −97% |
| `mb_substr($s, 0, 10)`, Korean (2.33 B/char), 49-byte title | 355 | −47% | −49% | −58% | −57% |
| `mb_substr($s, $half, 20)`, Korean (2.24 B/char), 1 KB | 3,023 | −41% | −32% | −62% | −57% |
| `mb_substr($s, $half, 20)`, Korean (2.25 B/char), 64 KB | 143,645 | −95% | −96% | −98% | −97% |
| `mb_substr($s, 0, 10)`, English with emoji (1.30 B/char), 26-byte title | 176 | −24% | −26% | −42% | −40% |
| `mb_substr($s, $half, 20)`, English with emoji (1.39 B/char), 1 KB | 1,982 | −50% | −46% | −68% | −68% |
| `mb_substr($s, $half, 20)`, English with emoji (1.43 B/char), 64 KB | 149,380 | −96% | −96% | −98% | −98% |
| `mb_substr($s, -20)`, English (1.00 B/char), 1 KB | 2,310 | −66% | −62% | −70% | −67% |
| `mb_substr($s, 0, $half)`, English (1.00 B/char), 1 KB | 2,079 | −89% | −88% | −92% | −92% |
| `mb_strpos($s, $needle, $half)`, English (1.00 B/char), 1 KB | 6,290 | −91% | −90% | −92% | −92% |
| `mb_substr($s, -20)`, English (1.00 B/char), 64 KB | 134,526 | −87% | −84% | −91% | −91% |
| `mb_strpos($s, $needle, $half)`, English (1.00 B/char), 64 KB | 385,906 | −93% | −93% | −94% | −94% |
| `mb_substr($s, 0, 10)`, English (1.00 B/char), 31-byte title, without the flag | 199 | +4% | +3% | 0% | +1% |
| `mb_substr($s, $half, 20)`, English (1.00 B/char), 1 KB, without the flag | 1,363 | −1% | +1% | 0% | −1% |
| `mb_substr($s, $half, 20)`, Chinese (2.89 B/char), 1 KB, without the flag | 2,841 | 0% | +1% | 0% | 0% |

Master against master (GCC 13.3) at the start and at the end of the series: medians −2 … +3% on every row ([`aa.md`](aa.md)).

The gain from the middle of 1 KB falls with the bytes per character: master decodes and encodes every character up to the offset, the PR counts bytes. In Hindi, Chinese, Japanese and Korean the middle of 1 KB is 181–241 characters, not more than the 256 at which the PR's chunk loop starts, so it is counted byte by byte ([below](#code)).

Without the flag the PR adds the flag check: 6–18 more instructions per call, and 3–4% more cycles for the 31-byte title with both GCC versions. With the first version, GCC 13.3 showed 3–25% fewer cycles on these rows, from code placement in that build ([`placement-g13.txt`](placement-g13.txt)); with the current head, the two 1 KB rows take the same cycles, branch misses and front-end stalls per call as master, within 2% ([`placement-g13-head.txt`](placement-g13-head.txt), [`placement-run.sh`](placement-run.sh)).

Full table, with the range over the five passes and the change in instructions:

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | instructions |
|---|--:|--:|--:|--:|--:|--:|
| `mb_substr($s, 0, 10)`, English (1.00 B/char), 31-byte title | 200 | −33% (−35 … −32) | −21% (−25 … −19) | −46% (−49 … −46) | −47% (−51 … −44) | −43% … −38% |
| `mb_substr($s, $half, 20)`, English (1.00 B/char), 1 KB | 1,366 | −82% (−82 … −82) | −81% (−82 … −81) | −87% (−87 … −86) | −87% (−87 … −87) | −88% … −85% |
| `mb_substr($s, $half, 20)`, English (1.00 B/char), 64 KB | 63,324 | −92% (−92 … −92) | −90% (−90 … −89) | −95% (−96 … −88) | −95% (−95 … −93) | −95% … −92% |
| `mb_substr($s, 0, 10)`, Spanish (1.00 B/char), 37-byte title | 210 | −37% (−37 … −35) | −25% (−26 … −25) | −47% (−48 … −46) | −50% (−50 … −50) | −47% … −42% |
| `mb_substr($s, $half, 20)`, Spanish (1.04 B/char), 1 KB | 1,620 | −63% (−63 … −61) | −57% (−57 … −56) | −76% (−76 … −75) | −71% (−71 … −70) | −66% … −58% |
| `mb_substr($s, $half, 20)`, Spanish (1.03 B/char), 64 KB | 89,136 | −94% (−94 … −92) | −92% (−93 … −91) | −97% (−97 … −97) | −97% (−97 … −97) | −94% … −92% |
| `mb_substr($s, 0, 10)`, Russian (1.81 B/char), 49-byte title | 275 | −37% (−39 … −37) | −40% (−41 … −38) | −58% (−59 … −57) | −56% (−56 … −52) | −61% … −57% |
| `mb_substr($s, $half, 20)`, Russian (1.78 B/char), 1 KB | 1,720 | −44% (−45 … −43) | −44% (−45 … −44) | −70% (−71 … −68) | −72% (−73 … −72) | −74% … −69% |
| `mb_substr($s, $half, 20)`, Russian (1.77 B/char), 64 KB | 165,015 | −96% (−97 … −95) | −96% (−96 … −95) | −98% (−99 … −98) | −98% (−98 … −98) | −95% … −93% |
| `mb_substr($s, 0, 10)`, Arabic (1.75 B/char), 56-byte title | 302 | −45% (−45 … −44) | −45% (−46 … −44) | −60% (−61 … −59) | −60% (−60 … −58) | −63% … −59% |
| `mb_substr($s, $half, 20)`, Arabic (1.74 B/char), 1 KB | 1,868 | −43% (−44 … −42) | −42% (−42 … −41) | −70% (−71 … −69) | −68% (−69 … −68) | −72% … −66% |
| `mb_substr($s, $half, 20)`, Arabic (1.76 B/char), 64 KB | 158,923 | −96% (−97 … −96) | −96% (−97 … −95) | −98% (−99 … −98) | −98% (−98 … −98) | −95% … −93% |
| `mb_substr($s, 0, 10)`, Hindi (2.61 B/char), 94-byte title | 475 | −60% (−60 … −59) | −60% (−61 … −59) | −67% (−68 … −65) | −68% (−69 … −68) | −76% … −71% |
| `mb_substr($s, $half, 20)`, Hindi (2.54 B/char), 1 KB | 2,191 | −18% (−18 … −13) | −10% (−11 … −8) | −43% (−43 … −43) | −43% (−43 … −41) | −66% … −54% |
| `mb_substr($s, $half, 20)`, Hindi (2.54 B/char), 64 KB | 180,592 | −96% (−97 … −96) | −95% (−96 … −95) | −98% (−100 … −98) | −97% (−98 … −97) | −96% … −93% |
| `mb_substr($s, 0, 10)`, Chinese (3.00 B/char), 54-byte title | 389 | −46% (−47 … −45) | −46% (−47 … −46) | −58% (−58 … −56) | −58% (−59 … −58) | −68% … −61% |
| `mb_substr($s, $half, 20)`, Chinese (2.89 B/char), 1 KB | 2,830 | −47% (−49 … −47) | −34% (−35 … −32) | −51% (−51 … −50) | −56% (−56 … −55) | −71% … −59% |
| `mb_substr($s, $half, 20)`, Chinese (2.89 B/char), 64 KB | 119,904 | −94% (−96 … −94) | −93% (−93 … −92) | −96% (−97 … −96) | −97% (−97 … −96) | −96% … −93% |
| `mb_substr($s, 0, 10)`, Japanese (3.00 B/char), 63-byte title | 406 | −49% (−50 … −48) | −48% (−49 … −46) | −61% (−62 … −60) | −61% (−62 … −61) | −71% … −64% |
| `mb_substr($s, $half, 20)`, Japanese (2.91 B/char), 1 KB | 2,749 | −48% (−49 … −47) | −28% (−29 … −28) | −50% (−51 … −48) | −56% (−56 … −56) | −71% … −59% |
| `mb_substr($s, $half, 20)`, Japanese (2.88 B/char), 64 KB | 122,395 | −95% (−95 … −94) | −93% (−94 … −92) | −97% (−97 … −96) | −97% (−97 … −96) | −96% … −93% |
| `mb_substr($s, 0, 10)`, Korean (2.33 B/char), 49-byte title | 355 | −47% (−48 … −46) | −49% (−49 … −47) | −58% (−59 … −55) | −57% (−58 … −57) | −66% … −60% |
| `mb_substr($s, $half, 20)`, Korean (2.24 B/char), 1 KB | 3,023 | −41% (−42 … −31) | −32% (−35 … −30) | −62% (−62 … −62) | −57% (−58 … −56) | −72% … −61% |
| `mb_substr($s, $half, 20)`, Korean (2.25 B/char), 64 KB | 143,645 | −95% (−96 … −94) | −96% (−97 … −94) | −98% (−98 … −97) | −97% (−98 … −97) | −96% … −93% |
| `mb_substr($s, 0, 10)`, English with emoji (1.30 B/char), 26-byte title | 176 | −24% (−26 … −24) | −26% (−27 … −25) | −42% (−43 … −42) | −40% (−42 … −40) | −41% … −37% |
| `mb_substr($s, $half, 20)`, English with emoji (1.39 B/char), 1 KB | 1,982 | −50% (−51 … −49) | −46% (−47 … −46) | −68% (−68 … −66) | −68% (−69 … −68) | −70% … −63% |
| `mb_substr($s, $half, 20)`, English with emoji (1.43 B/char), 64 KB | 149,380 | −96% (−96 … −95) | −96% (−97 … −95) | −98% (−100 … −97) | −98% (−100 … −98) | −95% … −92% |
| `mb_substr($s, -20)`, English (1.00 B/char), 1 KB | 2,310 | −66% (−67 … −65) | −62% (−62 … −60) | −70% (−71 … −70) | −67% (−68 … −67) | −73% … −67% |
| `mb_substr($s, 0, $half)`, English (1.00 B/char), 1 KB | 2,079 | −89% (−90 … −88) | −88% (−89 … −88) | −92% (−92 … −91) | −92% (−93 … −91) | −93% … −91% |
| `mb_strpos($s, $needle, $half)`, English (1.00 B/char), 1 KB | 6,290 | −91% (−92 … −91) | −90% (−91 … −89) | −92% (−92 … −91) | −92% (−92 … −92) | −64% … −57% |
| `mb_substr($s, -20)`, English (1.00 B/char), 64 KB | 134,526 | −87% (−87 … −86) | −84% (−85 … −83) | −91% (−92 … −90) | −91% (−92 … −90) | −91% … −87% |
| `mb_strpos($s, $needle, $half)`, English (1.00 B/char), 64 KB | 385,906 | −93% (−94 … −93) | −93% (−93 … −92) | −94% (−95 … −94) | −94% (−97 … −93) | −73% … −67% |
| `mb_substr($s, 0, 10)`, English (1.00 B/char), 31-byte title, without the flag | 199 | +4% (+3 … +5) | +3% (+3 … +4) | 0% (0 … +3) | +1% (+1 … +3) | +1% … +2% |
| `mb_substr($s, $half, 20)`, English (1.00 B/char), 1 KB, without the flag | 1,363 | −1% (−2 … +1) | +1% (0 … +2) | 0% (−1 … 0) | −1% (−2 … +2) | 0% |
| `mb_substr($s, $half, 20)`, Chinese (2.89 B/char), 1 KB, without the flag | 2,841 | 0% (−1 … +2) | +1% (0 … +3) | 0% (0 … 0) | 0% (−1 … +3) | 0% |

## The UTF-8-Mobile encodings

This section is about the first version, `b218ba6b8d2`; the current head contains the condition suggested here.

`php_mb_is_no_encoding_utf8()` is true for `UTF-8` and the four `UTF-8-Mobile` variants. The variants are byte-for-byte UTF-8, but their decoders and encoders map some code points to the carriers' private-use emoji. Since [`ec348a12d11`](https://github.com/php/php-src/commit/ec348a12d11) (PHP 8.3.2, "Character indices used by mb_strpos and mb_substr have same meaning, even on invalid strings"), `mb_substr()` decodes and encodes again for all of them, so on master `mb_substr("a®b", 1, 1, 'UTF-8-Mobile#DOCOMO')` is `ee9cb6`, flag or not. Before that commit `mb_substr()` used the encoding's `mblen_table` and copied bytes, which gave `c2ae` (the PHP 8.2 and 8.3.0–8.3.1 output that the author's fuzzer found and youkidearitai bisected to that commit in the PR discussion).

With the first version, a flagged string took the copying path for the variants too:

```php
$s = str_repeat("a\u{AE}b", 2);
var_dump(bin2hex(mb_substr($s, 1, 1, 'UTF-8-Mobile#DOCOMO')));
mb_substr($s, -1, null, 'UTF-8-Mobile#DOCOMO'); // counts the length, which marks $s as valid UTF-8
var_dump(bin2hex(mb_substr($s, 1, 1, 'UTF-8-Mobile#DOCOMO')));
```

Master and the fix print `"ee9cb6"` twice; the first version prints `"ee9cb6"` and then `"c2ae"` ([`repro.php`](repro.php), [`repro-output.txt`](repro-output.txt)).

Over the differential test below, 64–73% of the UTF-8-Mobile lines differ from master with the first version, flagged or not: unflagged lines differ through calls that count the length first and so set the flag (a negative offset or length in `mb_substr()`, a non-zero start in `mb_strimwidth()`). With the condition `enc == &mbfl_encoding_utf8` none do.

On master the mbstring functions already disagree for these encodings: `mb_str_split()` and `mb_strcut()` return the input bytes, `mb_substr()`, `mb_strstr()` and `mb_convert_encoding()` encode again ([`mobile-consistency.php`](mobile-consistency.php), all four variants, [`mobile-consistency-master.txt`](mobile-consistency-master.txt)). Which of the two is right for the variants is a separate question.

## Differential test

[`difftest.php`](difftest.php) generates strings from 1-, 2-, 3- and 4-byte characters, including the carriers' private-use ranges, `®`, `©`, flags, keycaps, combining marks and 10% invalid strings (stray continuation bytes, truncated and overlong sequences, surrogates), from empty to about 3,000 characters, many of them 255–257, 511–513, 768 or 1,024–1,025 characters long (around multiples of the 256-byte chunk), and calls the functions that go through `mb_get_substr()` or `mb_find_strpos()` on the string: `mb_substr()` with 6 offsets × 13 lengths, `mb_strpos()`, `mb_strrpos()`, `mb_stripos()`, `mb_strripos()`, `mb_strimwidth()`, `mb_strstr()`, `mb_strrchr()`, `mb_stristr()`, `mb_strrichr()`, `mb_ucfirst()`, `mb_lcfirst()`, `mb_trim()`, `mb_ltrim()`, `mb_rtrim()`, `mb_strlen()` (`mb_str_pad()` is called too, but it takes the new path only for the pad string, which here is a literal and never flagged). Each call gets a fresh copy of the string, unflagged and flagged, in UTF-8 and the four UTF-8-Mobile encodings; `mb_strpos()`, `mb_stripos()`, `mb_strrpos()` and `mb_substr()` also run on the string converted to SJIS, UTF-16LE, ISO-8859-1 and EUC-JP. One line per case and encoding holds the md5 of all results.

| builds | cases | UTF-8, other encodings | UTF-8-Mobile |
|---|--:|---|---|
| first version, GCC 13.3, seeds 1 and 2 | 40,000 | same as master | 65–72% of lines differ |
| first version, GCC 14.2, clang 18.1, clang 20.1, seed 3 | 10,000 each | same as master | 64–73% of lines differ |
| first version, clang 18.1 ASan/UBSan (`USE_ZEND_ALLOC=0`), seed 4 | 3,000 | same as master, no reports | 66–73% of lines differ |
| fix (= current head), GCC 13.3, seeds 1 and 2 | 40,000 | same as master | same as master |
| fix (= current head), clang 18.1 ASan/UBSan, seed 4 | 3,000 | same as master, no reports | same as master |

Counts per encoding: [`dt-summary.txt`](dt-summary.txt). Master gives the same output with all four compilers (seed 3). The ASan builds are compared with master built with GCC 13.3.

## Code

- `mb_get_substr()` now checks `enc == &mbfl_encoding_utf8`, which keeps the UTF-8-Mobile variants on the decoding path. `mb_get_strlen()` and `mb_find_strpos()` keep `php_mb_is_no_encoding_utf8()`: they count characters or compare bytes and do not change them, and the differential test shows no difference there.
- `GC_ADD_FLAGS(result, IS_STR_VALID_UTF8)` on the result means a slice of a checked string stays checked, so chained `mb_substr()` calls keep the fast path.
- The chunk loop subtracts at most 256 per chunk and runs only while `offset > 256`, so the offset never goes below zero; a chunk may end inside a character, and the byte loop after it skips the continuation bytes. Reading this, I found no problem with the `offset == 0 ? end : NULL` return, the `len < end - start` shortcut or the `zend_string_init_fast()` result for 0 and 1 bytes (interned, not flagged).
- Strings without the flag and with non-negative offsets still decode. Checking them with `mb_check_str_encoding()` first would be a pass over the whole string even when only the first characters are needed; I did not measure that.
- The chunk loop starts only while more than 256 characters remain to skip, because a 256-byte chunk can hold up to 256 characters. A chunk of pure 2- to 4-byte text holds 64–128 characters (87–149 in the texts here), so offsets of up to 256 characters (the middle of 1 KB in Hindi, Chinese, Japanese, Korean) go through the byte loop. I measured two ways to use the chunks there, both on top of the fix, output identical to master (GCC 13.3 seed 1, clang 18.1 seed 3). Each slows down other rows, so I do not suggest either for this PR:

  1. Count each chunk first and skip it while it holds no more characters than the offset ([`chunk-variant.diff`](chunk-variant.diff)): 1 KB from the middle 30–77% faster than the PR in every language except English, but English 1 KB slower: 25–52% from the middle (after two chunks 9 characters remain, and the third chunk is counted and thrown away), 22–43% for the first half, 7–10% for `mb_strpos()`, and up to 20% for `mb_substr($s, -20)`.
  2. The same, but only while the offset is at least 64 ([`chunk64-variant.diff`](chunk64-variant.diff)): English 1 KB from the middle is then within 2% of the PR with GCC 14.2, but 11–23% slower with GCC 13.3 and clang; with clang 18.1 and 20.1 every `mb_substr()` row on 64 KB is 12–64% slower than the PR, `mb_substr($s, -20)` on 1 KB up to 29% slower, and with GCC 13.3 the English, Spanish and emoji titles 8–9% slower.

  The variants were measured against the first version; its UTF-8 path is the same as the current head's, only the encoding condition differs. Change in CPU cycles per call relative to the PR (not to master), variant 1 ([`intel-docker-20261016-chunk.txt`](intel-docker-20261016-chunk.txt)):

  | call | PR, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 |
  |---|--:|--:|--:|--:|--:|
  | `mb_substr($s, 0, 10)`, English (1.00 B/char), 31-byte title | 132 | −2% | +2% | +2% | −2% |
  | `mb_substr($s, $half, 20)`, English (1.00 B/char), 1 KB | 234 | +35% | +52% | +27% | +25% |
  | `mb_substr($s, $half, 20)`, English (1.00 B/char), 64 KB | 5,199 | 0% | −1% | +3% | 0% |
  | `mb_substr($s, 0, 10)`, Spanish (1.00 B/char), 37-byte title | 130 | −2% | +2% | +1% | −2% |
  | `mb_substr($s, $half, 20)`, Spanish (1.04 B/char), 1 KB | 594 | −44% | −30% | −54% | −62% |
  | `mb_substr($s, $half, 20)`, Spanish (1.03 B/char), 64 KB | 5,577 | −1% | +2% | +5% | +5% |
  | `mb_substr($s, 0, 10)`, Russian (1.81 B/char), 49-byte title | 167 | −5% | −3% | +1% | −7% |
  | `mb_substr($s, $half, 20)`, Russian (1.78 B/char), 1 KB | 970 | −63% | −55% | −62% | −59% |
  | `mb_substr($s, $half, 20)`, Russian (1.77 B/char), 64 KB | 5,996 | −13% | −11% | −12% | −10% |
  | `mb_substr($s, 0, 10)`, Arabic (1.75 B/char), 56-byte title | 166 | −5% | −3% | −2% | −7% |
  | `mb_substr($s, $half, 20)`, Arabic (1.74 B/char), 1 KB | 1,052 | −62% | −53% | −60% | −56% |
  | `mb_substr($s, $half, 20)`, Arabic (1.76 B/char), 64 KB | 6,013 | −13% | −10% | −12% | −12% |
  | `mb_substr($s, 0, 10)`, Hindi (2.61 B/char), 94-byte title | 190 | −6% | −4% | −1% | −2% |
  | `mb_substr($s, $half, 20)`, Hindi (2.54 B/char), 1 KB | 1,839 | −77% | −72% | −75% | −72% |
  | `mb_substr($s, $half, 20)`, Hindi (2.54 B/char), 64 KB | 6,691 | −21% | −20% | −24% | −21% |
  | `mb_substr($s, 0, 10)`, Chinese (3.00 B/char), 54-byte title | 197 | +1% | −9% | 0% | +1% |
  | `mb_substr($s, $half, 20)`, Chinese (2.89 B/char), 1 KB | 1,811 | −75% | −69% | −74% | −74% |
  | `mb_substr($s, $half, 20)`, Chinese (2.89 B/char), 64 KB | 6,799 | −22% | −18% | −21% | −20% |
  | `mb_substr($s, 0, 10)`, Japanese (3.00 B/char), 63-byte title | 200 | 0% | −9% | +1% | +1% |
  | `mb_substr($s, $half, 20)`, Japanese (2.91 B/char), 1 KB | 1,719 | −74% | −66% | −73% | −73% |
  | `mb_substr($s, $half, 20)`, Japanese (2.88 B/char), 64 KB | 6,699 | −21% | −18% | −21% | −19% |
  | `mb_substr($s, 0, 10)`, Korean (2.33 B/char), 49-byte title | 182 | −5% | −5% | −2% | +1% |
  | `mb_substr($s, $half, 20)`, Korean (2.24 B/char), 1 KB | 1,760 | −76% | −72% | −74% | −72% |
  | `mb_substr($s, $half, 20)`, Korean (2.25 B/char), 64 KB | 6,699 | −21% | −20% | −24% | −21% |
  | `mb_substr($s, 0, 10)`, English with emoji (1.30 B/char), 26-byte title | 130 | −1% | +2% | +2% | −3% |
  | `mb_substr($s, $half, 20)`, English with emoji (1.39 B/char), 1 KB | 973 | −61% | −47% | −63% | −57% |
  | `mb_substr($s, $half, 20)`, English with emoji (1.43 B/char), 64 KB | 5,813 | −10% | −6% | −10% | −12% |
  | `mb_substr($s, -20)`, English (1.00 B/char), 1 KB | 788 | +5% | +20% | +10% | −5% |
  | `mb_substr($s, 0, $half)`, English (1.00 B/char), 1 KB | 221 | +32% | +43% | +22% | +24% |
  | `mb_strpos($s, $needle, $half)`, English (1.00 B/char), 1 KB | 577 | +7% | +10% | +10% | +9% |
  | `mb_substr($s, -20)`, English (1.00 B/char), 64 KB | 17,632 | 0% | +1% | −6% | −4% |
  | `mb_strpos($s, $needle, $half)`, English (1.00 B/char), 64 KB | 24,101 | 0% | 0% | +12% | −2% |

  Variant 2 ([`intel-docker-20261016-chunk64.txt`](intel-docker-20261016-chunk64.txt)):

  | call | PR, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 |
  |---|--:|--:|--:|--:|--:|
  | `mb_substr($s, 0, 10)`, English (1.00 B/char), 31-byte title | 132 | +9% | −2% | +2% | −2% |
  | `mb_substr($s, $half, 20)`, English (1.00 B/char), 1 KB | 237 | +11% | −2% | +23% | +19% |
  | `mb_substr($s, $half, 20)`, English (1.00 B/char), 64 KB | 5,204 | +1% | −1% | +64% | +49% |
  | `mb_substr($s, 0, 10)`, Spanish (1.00 B/char), 37-byte title | 130 | +9% | −3% | +2% | −1% |
  | `mb_substr($s, $half, 20)`, Spanish (1.04 B/char), 1 KB | 595 | −52% | −53% | −54% | −66% |
  | `mb_substr($s, $half, 20)`, Spanish (1.03 B/char), 64 KB | 5,566 | +3% | +1% | +63% | +43% |
  | `mb_substr($s, 0, 10)`, Russian (1.81 B/char), 49-byte title | 168 | −1% | +1% | −1% | +3% |
  | `mb_substr($s, $half, 20)`, Russian (1.78 B/char), 1 KB | 972 | −68% | −67% | −64% | −63% |
  | `mb_substr($s, $half, 20)`, Russian (1.77 B/char), 64 KB | 6,042 | −13% | −10% | +40% | +32% |
  | `mb_substr($s, 0, 10)`, Arabic (1.75 B/char), 56-byte title | 166 | −2% | −1% | −5% | −2% |
  | `mb_substr($s, $half, 20)`, Arabic (1.74 B/char), 1 KB | 1,056 | −66% | −63% | −59% | −62% |
  | `mb_substr($s, $half, 20)`, Arabic (1.76 B/char), 64 KB | 6,031 | −12% | −9% | +39% | +29% |
  | `mb_substr($s, 0, 10)`, Hindi (2.61 B/char), 94-byte title | 190 | −2% | 0% | −2% | 0% |
  | `mb_substr($s, $half, 20)`, Hindi (2.54 B/char), 1 KB | 1,839 | −80% | −77% | −76% | −77% |
  | `mb_substr($s, $half, 20)`, Hindi (2.54 B/char), 64 KB | 6,702 | −21% | −17% | +21% | +12% |
  | `mb_substr($s, 0, 10)`, Chinese (3.00 B/char), 54-byte title | 196 | −4% | +1% | +1% | −1% |
  | `mb_substr($s, $half, 20)`, Chinese (2.89 B/char), 1 KB | 1,754 | −79% | −74% | −75% | −78% |
  | `mb_substr($s, $half, 20)`, Chinese (2.89 B/char), 64 KB | 6,809 | −22% | −20% | +25% | +13% |
  | `mb_substr($s, 0, 10)`, Japanese (3.00 B/char), 63-byte title | 197 | −4% | +1% | 0% | −1% |
  | `mb_substr($s, $half, 20)`, Japanese (2.91 B/char), 1 KB | 1,709 | −78% | −72% | −73% | −77% |
  | `mb_substr($s, $half, 20)`, Japanese (2.88 B/char), 64 KB | 6,810 | −22% | −17% | +27% | +19% |
  | `mb_substr($s, 0, 10)`, Korean (2.33 B/char), 49-byte title | 181 | −3% | +1% | −2% | −2% |
  | `mb_substr($s, $half, 20)`, Korean (2.24 B/char), 1 KB | 1,754 | −78% | −76% | −74% | −76% |
  | `mb_substr($s, $half, 20)`, Korean (2.25 B/char), 64 KB | 6,889 | −24% | −19% | +21% | +14% |
  | `mb_substr($s, 0, 10)`, English with emoji (1.30 B/char), 26-byte title | 131 | +8% | −3% | +2% | −2% |
  | `mb_substr($s, $half, 20)`, English with emoji (1.39 B/char), 1 KB | 973 | −64% | −61% | −62% | −64% |
  | `mb_substr($s, $half, 20)`, English with emoji (1.43 B/char), 64 KB | 5,963 | −11% | −9% | +43% | +27% |
  | `mb_substr($s, -20)`, English (1.00 B/char), 1 KB | 794 | +20% | +5% | +29% | 0% |
  | `mb_substr($s, 0, $half)`, English (1.00 B/char), 1 KB | 221 | +3% | 0% | +16% | +1% |
  | `mb_strpos($s, $needle, $half)`, English (1.00 B/char), 1 KB | 578 | +2% | 0% | +5% | +4% |
  | `mb_substr($s, -20)`, English (1.00 B/char), 64 KB | 17,665 | +1% | 0% | +25% | +26% |
  | `mb_strpos($s, $needle, $half)`, English (1.00 B/char), 64 KB | 23,915 | +2% | 0% | +12% | −1% |

## Tests

The PR adds no tests. `ext/mbstring/tests` (427 tests: 339 passed, 88 skipped, 80 of them for mbregex, [`tests-mbstring-pr.txt`](tests-mbstring-pr.txt)) pass with the first version. [`mutate.py`](mutate.py) applies eight mutations to the fix, one at a time ([`mutate-output.txt`](mutate-output.txt)):

| mutation | difftest | `ext/mbstring/tests` |
|---|---|---|
| UTF-8-Mobile variants take the fast path (the first version) | caught | missed |
| unflagged strings take the fast path | caught | caught (2) |
| chunk loop runs while `offset > 0` | caught | missed |
| chunk step 255 bytes instead of 256 | caught | missed |
| only ASCII bytes counted as characters | caught | caught (5) |
| offset past the end returns the end | caught | caught (1) |
| result one character short | caught | caught (5) |
| reverse search with a negative offset uses the fast path for unflagged strings | missed | missed |

The last one changes the end of the `mb_strrpos()` search range only for invalid strings with a negative offset; the differential test does not catch it, and I did not look for an input where the result changes.

The same eight mutations with the tool's own `bench mutate` (added after the review), on a full GCC 13.3 build of the fix, with `difftests/code.php` on 11 calls and `ext/mbstring/tests` as the checks ([`mutations.php`](mutations.php)), give the same verdicts: the differential test catches seven, the tests the same four with the same numbers of failing tests ([`mutate-bench.md`](mutate-bench.md)).

[`mb_substr_valid_utf8.phpt`](mb_substr_valid_utf8.phpt) compares flagged and unflagged strings around 256-byte chunks and checks the UTF-8-Mobile result before and after the flag; it fails with the first version and passes on master and with the current head ([`proposed-test-builds.txt`](proposed-test-builds.txt)), and it catches the three mutations the existing tests miss ([`mutate-proposed-output.txt`](mutate-proposed-output.txt)).

## Reproduce

From the repository root, with a php-src checkout that has master `1c9242e7fec`, the first version merged onto it and the fix on top (`git fetch origin pull/24080/head`, merge `b218ba6b8d2`, apply [`fix.diff`](fix.diff); or merge the current head `6d9250e8b74`, which gives the same tree as the fix):

```
cd reports/pr-24080-mb-substr
PHP_SRC=<php-src> ./build.sh gcc g13 base 1c9242e7fec          # and pr, fix; gcc-14 g14, clang c18, clang-20 c20
PHP_SRC=<php-src> ./build.sh clang c18 asan <pr commit> asan     # and fixasan
BENCH_BUILDS=<builds> ./difftest-run.sh
BENCH_BUILDS=<builds> CPU=2 PASSES=5 ./pairs-run.sh out.txt aa:g13-base:g13-base g13:g13-base:g13-fix g14:g14-base:g14-fix c18:c18-base:c18-fix c20:c20-base:c20-fix aa2:g13-base:g13-base
mapfile -t R < rows.txt; python3 speedup-table.py out.txt 'g13:GCC 13.3,g14:GCC 14.2,c18:clang 18.1,c20:clang 20.1' "${R[@]}"
BENCH_BUILDS=<builds> CPU=2 ./placement-run.sh placement.txt g13-base g13-fix
# variants: build them as chunk / chunk64 (fix + chunk-variant.diff / chunk64-variant.diff), then
CASES="$(php cases.php list | tr ' ' '\n' | grep -v plain)"
BENCH_BUILDS=<builds> CPU=2 PASSES=5 CASES="$CASES" ./pairs-run.sh chunk.txt g13:g13-pr:g13-chunk g14:g14-pr:g14-chunk c18:c18-pr:c18-chunk c20:c20-pr:c20-chunk
BENCH_BUILDS=<builds> CPU=2 PASSES=5 CASES="$CASES" ./pairs-run.sh chunk64.txt g13:g13-pr:g13-chunk64 g14:g14-pr:g14-chunk64 c18:c18-pr:c18-chunk64 c20:c20-pr:c20-chunk64
```

The same measurement with the tool's own commands, without the scripts above (added after the review; same machine, 16 October 2026, on battery with a load average of 5.9 at the start): [`suite.php`](suite.php) marks each copy of the input as valid UTF-8 with `setup`, and

```
BENCH_CONFIGURE_EXTRA="--enable-mbstring --disable-mbregex" ./bench build --slim --cc gcc,gcc-14,clang,clang-20 mbc-base 1c9242e7fec
BENCH_CONFIGURE_EXTRA="--enable-mbstring --disable-mbregex" ./bench build --slim --cc gcc,gcc-14,clang,clang-20 mbc-head <head merged onto 1c9242e7fec>
./bench compare reports/pr-24080-mb-substr/suite.php gcc13=mbc-base-gcc13:mbc-head-gcc13 gcc14=mbc-base-gcc14:mbc-head-gcc14 \
    clang18=mbc-base-clang18:mbc-head-clang18 clang20=mbc-base-clang20:mbc-head-clang20
./bench table <series> --labels reports/pr-24080-mb-substr/labels-compare.txt --header
```

gave [`compare-head.json`](compare-head.json) in 193 seconds. Its cells are within 5 percentage points of the table above (the largest difference: the Russian title with GCC 13.3, −42% against −37%), computed per pass and with the empty loop subtracted instead of zero calls.

The series in this report: [`intel-docker-20261016-head.txt`](intel-docker-20261016-head.txt) (master against the current head), [`intel-docker-20261016-langs.txt`](intel-docker-20261016-langs.txt) (master against the first version, same calls), [`intel-docker-20261016-chunk.txt`](intel-docker-20261016-chunk.txt) and [`intel-docker-20261016-chunk64.txt`](intel-docker-20261016-chunk64.txt) (the first version against the variants); lines: group, side, case, cycles, instructions per call.
