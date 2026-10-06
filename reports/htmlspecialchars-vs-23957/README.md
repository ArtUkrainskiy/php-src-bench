# htmlspecialchars(): php-src #23957 and #24145 together

Two open php-src pull requests speed up `htmlspecialchars()` in different places:

- [#23957](https://github.com/php/php-src/pull/23957) (nicolas-grekas) scans the input with SIMD
  and returns it unchanged when nothing needs encoding; otherwise the scanned prefix is copied and
  the old byte-at-a-time loop encodes the rest.
- [#24145](https://github.com/php/php-src/pull/24145) (this repository's author) keeps the loop
  but copies runs of plain ASCII inside it and inlines the decoder.

This report measures #23957 against its base, and #24145 rebased on top of #23957 against #23957
alone. The rebased commit is
[`1b9965d106a`](https://github.com/ArtUkrainskiy/php-src/commit/1b9965d106a) on branch
[`hsc-runs-on-ng`](https://github.com/ArtUkrainskiy/php-src/commits/hsc-runs-on-ng): #23957's
`384fbd6447a` plus #24145's change, +32/-2 lines on top, two trivial conflicts.

## Summary

| input | #23957 vs its base | #23957 + #24145 vs #23957 |
|---|--:|--:|
| 40-byte title, nothing to encode | 7.3x faster | same |
| 256 B English, nothing to encode | 34x faster | same |
| 1 KB cp1251 Cyrillic | 32x faster | same |
| 1 KB Russian / Chinese UTF-8 | 1.4x faster / 1.1x slower | same |
| 40-byte title with `&` and quotes | same | 1.8x faster |
| 1 KB English with an apostrophe | 3.3x faster | 2.1x faster |
| 64 KB English | same | 1.8x faster |
| 1 KB HTML / 64 KB Wikipedia HTML | 1.05x / 1.03x slower | 2.0x / 1.9x faster |
| 4 KB Markdown / JS | same | 2.8x faster |
| `ENT_DISALLOWED`, Shift_JIS, Big5 | same | 1.2-1.6x faster |
| `htmlentities()` | 1.0-1.2x faster | another 1.0-1.2x |

Symfony Demo (`benchmark/benchmark.php` from php-src, callgrind, JIT off, instructions per
request): base 39,415,756; #23957 39,050,852 (-0.93%); #23957 + #24145 38,998,576 (-1.06%).
`zif_htmlspecialchars()` inclusive per request: 526,303 -> 177,814 -> 81,405.

Output of the combined build is identical to the base on 20,000 random inputs
(`bench difftest html-encode ng-base ng-combo`: 13 flag sets, 14 charsets, both functions, both
values of `double_encode`).

One thing #23957 may want to look at: on Chinese UTF-8 text with nothing to encode it halves the
instructions (39,097 -> 19,860 per 1 KB) but is 11-13% slower in wall time here, on 1 KB and 64 KB
alike; the per-character `html_skip_utf8_char()` in the scan loop is the likely place.

## How it was measured

i7-13700H, GCC 13.3, builds with the php-src CI extension set, CFLAGS `-O2 -g -falign-functions=64
-falign-loops=32`; `bench run htmlspecialchars --a <A> --b <B> --perf`. Builds: `ng-base` =
`03bf9cdcac9` (the merge base of #23957), `ng-hsc` = `384fbd6447a` (#23957), `ng-combo` =
`1b9965d106a`. The second run had three rows with a disturbed round (marked in the output);
instruction counts are not affected by that.

## #23957 vs its base

A: ng-base — PHP 8.7.0-dev, 03bf9cdcac9 Merge branch 'PHP-8.6'  
B: ng-hsc — PHP 8.7.0-dev, 384fbd6447a ext/standard: Return the input of htmlspecialchars() when nothing needs encoding  
CPU 2 (13th Gen Intel(R) Core(TM) i7-13700H), governor powersave, turbo on, kernel 7.0.0-34-generic  
4 rounds × 7 samples × 10 ms, cc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0, configure --disable-all --disable-cgi --disable-phpdbg --enable-cli --enable-cgi --with-valgrind --enable-mbstring --enable-sockets --with-mysqli --enable-mysqlnd --enable-pdo --with-pdo-sqlite --with-sqlite3 --with-openssl --with-gmp --enable-ctype --with-iconv --enable-session --enable-tokenizer --with-libxml --enable-dom --enable-xml --enable-simplexml --enable-xmlreader --enable-xmlwriter --enable-filter --enable-posix --enable-phar --enable-fileinfo, CFLAGS -O2 -g -falign-functions=64 -falign-loops=32, 2026-10-06T11:56+00:00  

| case | bytes | A ns/op | ± | B ns/op | ± | B vs A | A instr/op | B instr/op | instr B vs A |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| htmlspecialchars @ empty | 0 | 6.1 | 2.4% | 6.2 | 4.4% | 1.02× slower ~ | 120 | 120 | 1.00× |
| htmlspecialchars @ word-8 | 8 | 53.7 | 1.1% | 23.5 | 2.3% | 2.28× faster ✅ | 933 | 359 | 2.60× fewer |
| htmlspecialchars @ name-16 | 16 | 77.3 | 2.8% | 18.9 | 1.8% | 4.08× faster ✅ | 1424 | 337 | 4.23× fewer |
| htmlspecialchars @ title-40 | 40 | 150.9 | 1.3% | 20.8 | 4.2% | 7.27× faster ✅ | 2906 | 377 | 7.71× fewer |
| htmlspecialchars @ title-amp-40 | 40 | 176.4 | 1.6% | 176.2 | 1.4% | 1.00× ~ | 3021 | 2820 | 1.07× fewer |
| htmlspecialchars @ ru-title-30 | 30 | 133.1 | 1.8% | 52.9 | 0.6% | 2.51× faster ✅ | 2072 | 736 | 2.82× fewer |
| htmlspecialchars @ en-64 | 86 | 300.2 | 1.1% | 21.8 | 2.0% | 13.8× faster ✅ | 5629 | 451 | 12.5× fewer |
| htmlspecialchars @ en-256 | 314 | 1083 | 1.2% | 32.1 | 2.1% | 33.8× faster ✅ | 19303 | 731 | 26.4× fewer |
| htmlspecialchars @ en-1k | 1042 | 4407 | 0.8% | 1327 | 0.9% | 3.32× faster ✅ | 63140 | 21118 | 2.99× fewer |
| htmlspecialchars @ en-64k | 65583 | 322762 | 0.6% | 323156 | 0.9% | 1.00× ~ | 3946298 | 3839297 | 1.03× fewer |
| htmlspecialchars @ html-1k | 1076 | 4085 | 0.9% | 4303 | 1.1% | 1.05× slower ❌ | 67576 | 66485 | 1.02× fewer |
| htmlspecialchars @ html-page-4k | 4096 | 15332 | 0.6% | 15999 | 1.1% | 1.04× slower ❌ | 254922 | 250565 | 1.02× fewer |
| htmlspecialchars @ html-wiki-64k | 65536 | 290273 | 0.6% | 299848 | 0.8% | 1.03× slower ❌ | 4046915 | 3976619 | 1.02× fewer |
| htmlspecialchars @ md-4k | 4096 | 19169 | 0.7% | 19316 | 1.7% | 1.01× slower ~ | 247524 | 241184 | 1.03× fewer |
| htmlspecialchars @ js-4k | 4096 | 20470 | 0.7% | 19077 | 1.4% | 1.07× faster ✅ | 251928 | 232965 | 1.08× fewer |
| htmlspecialchars @ js-min-4k | 4096 | 20153 | 1.1% | 19829 | 1.5% | 1.02× faster ✅ | 248712 | 238552 | 1.04× fewer |
| htmlspecialchars @ amp-1k | 1024 | 2417 | 0.6% | 2382 | 0.4% | 1.01× faster ✅ | 49232 | 48339 | 1.02× fewer |
| htmlspecialchars @ quot-1k | 1024 | 4477 | 1.4% | 4378 | 1.3% | 1.02× faster ~ | 89816 | 87915 | 1.02× fewer |
| htmlspecialchars @ ru-1k | 1030 | 3786 | 0.9% | 2696 | 0.7% | 1.40× faster ✅ | 52351 | 17958 | 2.92× fewer |
| htmlspecialchars @ ru-64k | 65537 | 273338 | 2.0% | 170571 | 0.6% | 1.60× faster ✅ | 3306655 | 1114003 | 2.97× fewer |
| htmlspecialchars @ zh-1k | 1046 | 1981 | 0.8% | 2193 | 0.5% | 1.11× slower ❌ | 39097 | 19860 | 1.97× fewer |
| htmlspecialchars @ zh-64k | 65577 | 121836 | 0.8% | 137589 | 0.6% | 1.13× slower ❌ | 2420126 | 1223536 | 1.98× fewer |
| htmlspecialchars @ emoji-1k | 1071 | 3307 | 1.1% | 730.3 | 0.7% | 4.53× faster ✅ | 52975 | 7322 | 7.24× fewer |
| htmlspecialchars !double_encode @ html-1k | 1076 | 4095 | 1.1% | 4374 | 0.7% | 1.07× slower ❌ | 67882 | 66791 | 1.02× fewer |
| htmlspecialchars !double_encode @ entities-1k | 1080 | 3421 | 0.8% | 3553 | 1.7% | 1.04× slower ❌ | 61084 | 58902 | 1.04× fewer |
| htmlspecialchars !double_encode @ amp-1k | 1024 | 2958 | 1.1% | 3050 | 0.4% | 1.03× slower ❌ | 67739 | 66847 | 1.01× fewer |
| htmlspecialchars ENT_DISALLOWED @ en-1k | 1042 | 6065 | 1.2% | 6036 | 1.1% | 1.00× ~ | 74648 | 73633 | 1.01× fewer |
| htmlspecialchars ENT_DISALLOWED @ html-1k | 1076 | 5684 | 0.5% | 5816 | 1.1% | 1.02× slower ❌ | 78364 | 77223 | 1.01× fewer |
| htmlspecialchars cp1251 @ en-1k | 1042 | 3569 | 2.3% | 1194 | 1.0% | 2.99× faster ✅ | 61414 | 20814 | 2.95× fewer |
| htmlspecialchars cp1251 @ cp1251-1k | 1056 | 3379 | 1.1% | 104.8 | 1.0% | 32.2× faster ✅ | 62070 | 2007 | 30.9× fewer |
| htmlspecialchars cp1251 @ cp1251-64k | 65572 | 335620 | 1.1% | 3692 | 0.9% | 90.9× faster ✅ | 3808035 | 82668 | 46.1× fewer |
| htmlspecialchars Shift_JIS @ sjis-1k | 1034 | 2558 | 1.1% | 2557 | 0.9% | 1.00× ~ | 50537 | 50087 | 1.01× fewer |
| htmlspecialchars BIG5 @ big5-1k | 1061 | 3213 | 0.7% | 3069 | 1.4% | 1.05× faster ✅ | 50179 | 49712 | 1.01× fewer |
| htmlentities @ title-40 | 40 | 170.7 | 0.8% | 167.2 | 0.4% | 1.02× faster ✅ | 3761 | 3740 | 1.01× fewer |
| htmlentities @ en-1k | 1042 | 3631 | 1.1% | 3524 | 0.7% | 1.03× faster ✅ | 85968 | 84943 | 1.01× fewer |
| htmlentities @ html-1k | 1076 | 4886 | 1.7% | 4696 | 1.0% | 1.04× faster ✅ | 89806 | 88656 | 1.01× fewer |
| htmlentities @ ru-1k | 1030 | 4611 | 0.7% | 3931 | 0.9% | 1.17× faster ✅ | 65107 | 64550 | 1.01× fewer |

<sub>ns/op: median time of one evaluation, loop overhead subtracted; ±: spread of the samples (1.4826·MAD/median); B vs A: A time / B time; ✅/❌: every round of B was faster/slower than every round of A, by at least 1%; ~: rounds overlap, no clear difference; instr/op: instructions per evaluation</sub>

## #23957 + #24145 vs #23957

A: ng-hsc — PHP 8.7.0-dev, 384fbd6447a ext/standard: Return the input of htmlspecialchars() when nothing needs encoding  
B: ng-combo — PHP 8.7.0-dev, 1b9965d106a ext/standard: Add a fast path for ASCII in htmlspecialchars()  
CPU 2 (13th Gen Intel(R) Core(TM) i7-13700H), governor powersave, turbo on, kernel 7.0.0-34-generic  
4 rounds × 7 samples × 10 ms, cc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0, configure --disable-all --disable-cgi --disable-phpdbg --enable-cli --enable-cgi --with-valgrind --enable-mbstring --enable-sockets --with-mysqli --enable-mysqlnd --enable-pdo --with-pdo-sqlite --with-sqlite3 --with-openssl --with-gmp --enable-ctype --with-iconv --enable-session --enable-tokenizer --with-libxml --enable-dom --enable-xml --enable-simplexml --enable-xmlreader --enable-xmlwriter --enable-filter --enable-posix --enable-phar --enable-fileinfo, CFLAGS -O2 -g -falign-functions=64 -falign-loops=32, 2026-10-06T13:09+00:00  

| case | bytes | A ns/op | ± | B ns/op | ± | B vs A | A instr/op | B instr/op | instr B vs A |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| htmlspecialchars @ empty | 0 | 6.3 | 6.9% | 5.9 | 3.7% | 1.06× faster ~ | 120 | 120 | 1.00× |
| htmlspecialchars @ word-8 | 8 | 23.5 | 2.3% | 22.8 | 2.4% | 1.03× faster ~ | 359 | 359 | 1.00× |
| htmlspecialchars @ name-16 | 16 | 18.9 | 2.4% | 18.5 | 2.3% | 1.02× faster ~ | 337 | 337 | 1.00× |
| htmlspecialchars @ title-40 | 40 | 21.0 | 2.0% | 20.3 | 2.0% | 1.04× faster ~ | 377 | 377 | 1.00× |
| htmlspecialchars @ title-amp-40 | 40 | 179.3 | 2.7% | 100.3 | 0.8% | 1.79× faster ✅ | 2820 | 1345 | 2.10× fewer |
| htmlspecialchars @ ru-title-30 | 30 | 52.7 | 0.7% | 52.9 | 0.6% | 1.00× ~ | 736 | 736 | 1.00× |
| htmlspecialchars @ en-64 | 86 | 22.0 | 2.6% | 21.4 | 1.4% | 1.02× faster ✅ layout? | 451 | 451 | 1.00× |
| htmlspecialchars @ en-256 | 314 | 31.4 | 2.4% | 31.0 | 1.4% | 1.01× faster ~ | 731 | 731 | 1.00× |
| htmlspecialchars @ en-1k | 1042 | 1325 | 1.6% | 628.8 | 0.5% | 2.11× faster ✅ | 21118 | 4876 | 4.33× fewer |
| htmlspecialchars @ en-64k | 65583 | 326877 | 4.0% | 181946 | 0.7% | 1.80× faster ✅ | 3839270 | 607537 | 6.32× fewer |
| htmlspecialchars @ html-1k | 1076 | 4299 | 1.0% | 2196 | 1.0% | 1.96× faster ✅ | 66485 | 19575 | 3.40× fewer |
| htmlspecialchars @ html-page-4k | 4096 | 16066 | 0.6% | 8218 | 0.5% | 1.95× faster ✅ | 250566 | 69806 | 3.59× fewer |
| htmlspecialchars @ html-wiki-64k | 65536 | 299156 | 0.8% | 161387 | 0.9% | 1.85× faster ✅ | 3976592 | 1187869 | 3.35× fewer |
| htmlspecialchars @ md-4k | 4096 | 19278 | 0.8% | 6887 | 0.6% | 2.80× faster ✅ | 241183 | 38487 | 6.27× fewer |
| htmlspecialchars @ js-4k | 4096 | 19106 | 1.0% | 6726 | 0.5% | 2.84× faster ✅ | 232964 | 41768 | 5.58× fewer |
| htmlspecialchars @ js-min-4k | 4096 | 19865 | 1.3% | 6973 | 0.8% | 2.85× faster ✅ | 238550 | 45261 | 5.27× fewer |
| htmlspecialchars @ amp-1k | 1024 | 2374 | 0.6% | 1706 | 0.6% | 1.39× faster ✅ | 48339 | 36123 | 1.34× fewer |
| htmlspecialchars @ quot-1k | 1024 | 4339 | 0.4% | 3780 | 0.8% | 1.15× faster ✅ | 87915 | 77771 | 1.13× fewer |
| htmlspecialchars @ ru-1k | 1030 | 2697 | 0.4% | 2696 | 0.2% | 1.00× ~ | 17958 | 17958 | 1.00× |
| htmlspecialchars @ ru-64k | 65537 | 170335 | 0.3% | 170195 | 0.4% | 1.00× ~ | 1113987 | 1113997 | 1.00× |
| htmlspecialchars @ zh-1k | 1046 | 2186 | 0.1% | 2187 | 0.1% | 1.00× ~ | 19860 | 19860 | 1.00× |
| htmlspecialchars @ zh-64k | 65577 | 137174 | 0.3% | 137096 | 0.1% | 1.00× ~ | 1223539 | 1223536 | 1.00× |
| htmlspecialchars @ emoji-1k | 1071 | 727.2 | 0.4% | 725.2 | 0.1% | 1.00× ~ | 7322 | 7322 | 1.00× |
| htmlspecialchars !double_encode @ html-1k | 1076 | 4334 | 0.8% | 2204 | 0.8% | 1.97× faster ✅ | 66791 | 19875 | 3.36× fewer |
| htmlspecialchars !double_encode @ entities-1k | 1080 | 3577 | 1.9% | 2018 | 0.4% | 1.77× faster ✅ | 58901 | 22129 | 2.66× fewer |
| htmlspecialchars !double_encode @ amp-1k | 1024 | 3037 | 0.5% | 2461 | 0.9% | 1.23× faster ✅ | 66846 | 53606 | 1.25× fewer |
| htmlspecialchars ENT_DISALLOWED @ en-1k | 1042 | 6040 | 1.7% | 3999 | 0.9% | 1.51× faster ✅ | 73633 | 58699 | 1.25× fewer |
| htmlspecialchars ENT_DISALLOWED @ html-1k | 1076 | 5783 | 0.9% | 3687 | 1.4% | 1.57× faster ✅ | 77222 | 61784 | 1.25× fewer |
| htmlspecialchars cp1251 @ en-1k | 1042 | 1191 | 2.0% | 649.7 | 0.4% | 1.83× faster ✅ | 20814 | 5232 | 3.98× fewer |
| htmlspecialchars cp1251 @ cp1251-1k | 1056 | 104.7 | 0.7% | 103.9 | 0.6% | 1.01× faster ~ | 2007 | 2007 | 1.00× |
| htmlspecialchars cp1251 @ cp1251-64k | 65572 | 3672 | 0.2% | 3675 | 0.3% | 1.00× ~ | 82668 | 82667 | 1.00× |
| htmlspecialchars Shift_JIS @ sjis-1k | 1034 | 2552 | 0.7% | 2136 | 0.5% | 1.19× faster ✅ | 50087 | 42723 | 1.17× fewer |
| htmlspecialchars BIG5 @ big5-1k | 1061 | 3061 | 1.0% | 2587 | 0.5% | 1.18× faster ✅ | 49712 | 43130 | 1.15× fewer |
| htmlentities @ title-40 | 40 | 167.3 | 0.6% | 142.4 | 0.4% | 1.18× faster ✅ | 3740 | 3219 | 1.16× fewer |
| htmlentities @ en-1k | 1042 | 3505 | 0.8% | 2859 | 0.3% | 1.23× faster ✅ | 84943 | 71390 | 1.19× fewer |
| htmlentities @ html-1k | 1076 | 4694 | 0.7% | 4167 | 0.8% | 1.13× faster ✅ | 88656 | 74502 | 1.19× fewer |
| htmlentities @ ru-1k | 1030 | 3921 | 1.0% | 3841 | 0.9% | 1.02× faster ✅ | 64550 | 58825 | 1.10× fewer |

<sub>ns/op: median time of one evaluation, loop overhead subtracted; ±: spread of the samples (1.4826·MAD/median); B vs A: A time / B time; ✅/❌: every round of B was faster/slower than every round of A, by at least 1%; ~: rounds overlap, no clear difference; instr/op: instructions per evaluation; layout?: the time changed, the instruction count did not; the amount of work does not explain it (code placement? cache or branch behaviour?)</sub>
