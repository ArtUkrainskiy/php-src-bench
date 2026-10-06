# A fast path for ASCII in htmlspecialchars()

php-src change: [`0e4d8e73a21`](https://github.com/ArtUkrainskiy/php-src/commit/0e4d8e73a21742064828f0ea098e2d3011b7d666)
"ext/standard: Add a fast path for ASCII in htmlspecialchars()", compared with its parent on
master, [`100e8f353ea`](https://github.com/php/php-src/commit/100e8f353ea8ef841339ba4c74a0966a7eea5157).

The change, in the loop of `php_escape_html_entities_ex()`:

- ASCII bytes no longer go through `get_next_char()`;
- runs of ASCII other than `& " ' < >` are copied in a loop of their own (`htmlspecialchars()`
  without `ENT_DISALLOWED`);
- `get_next_char()` is always inlined, which also gives `php_next_utf8_char()`, used by
  `json_encode()`, a copy without the charset switch.

## Summary

| | time | instructions |
|---|---|---|
| `htmlspecialchars()`, 8–40 byte strings | 1.4–1.75× faster | 1.4–3.4× fewer |
| `htmlspecialchars()`, English text | 1.7–2.5× faster | 4.5–6.5× fewer |
| `htmlspecialchars()`, Markdown, JS | 2.8× faster | 5.4–6.4× fewer |
| `htmlspecialchars()`, HTML | 1.8× faster | 3.4–3.7× fewer |
| `htmlspecialchars()`, Russian (UTF-8) | 1.2–1.5× faster | 1.3× fewer |
| `htmlspecialchars()`, Chinese (UTF-8), Shift_JIS, Big5 | 1.2× faster | 1.2× fewer |
| `htmlspecialchars()`, only `&` or `"` | 1.2–1.4× faster | 1.15–1.4× fewer |
| `htmlspecialchars()`, cp1251 Cyrillic | 1 KB: same to 1.02× slower; 64 KB: 1.08× faster | 1.35× fewer |
| `htmlentities()` | 1.3–1.4× faster | 1.2–1.3× fewer |
| `json_encode()`, Russian and Chinese text | 1.06–1.13× faster | 1.1× fewer |
| empty string; `json_encode()` of ASCII; `json_decode()` | same | same |

Two things to know when reading it:

- For long text, quote the 64 KB rows (English 1.7×), not the 1 KB ones (2.5×). A 1 KB input
  that is repeated in a loop gets memorized by the branch predictor, which flatters the new code
  and, in the cp1251 row, the old one: that row has 1.35× fewer instructions and was 1–2% slower
  in two of three runs, while 64 KB of the same text is 1.08× faster. See "Traps" in
  [the methodology notes](../../docs/methodology.md).
- The tables below are from an Intel i7-13700H with GCC 13.3. The same comparison on an AMD
  Ryzen 9 5950X with GCC 15.2 is in the section "A second machine": the instruction ratios are
  the same within a few percent, the gains in time are larger (English 2.7–3.8×, HTML 2.5–2.9×),
  and the cp1251 row is 1.3–1.7× faster there. On a third one (GCC 15.2, a virtual Haswell
  core, wall time only) English was 2.5–2.8× and HTML 1.8–2.0× faster, with no row slower.

## How it was measured

A laptop in normal use: governor powersave, turbo on, on battery, load average below 2, run
with `--wait-idle 600`. Samples scatter by less than 2.5% in every row except the empty string
(4.6%). The runner flagged one row of each suite as having a disturbed round
(`htmlspecialchars @ ru-title-30` and `json_encode @ en-1k`); in both, time and instruction
counts agree. Three earlier runs of the same comparison on mains power differ from this one by
1–2% per row.

What the case names call is in [suites/htmlspecialchars.php](../../suites/htmlspecialchars.php)
and [suites/json.php](../../suites/json.php); for example `htmlspecialchars cp1251` is
`htmlspecialchars($s, ENT_QUOTES | ENT_SUBSTITUTE, 'cp1251')`. The number in an input name is
its nominal size, the `bytes` column is exact.

## htmlspecialchars suite

A: base — PHP 8.6.0-dev, 100e8f353ea ext/uri: Preserve empty query and fragment in URL builders  
B: ascii-fast-path — PHP 8.6.0-dev, 0e4d8e73a21 ext/standard: Add a fast path for ASCII in htmlspecialchars()  
CPU 2 (13th Gen Intel(R) Core(TM) i7-13700H), governor powersave, turbo on, kernel 7.0.0-34-generic  
4 rounds × 7 samples × 10 ms, cc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0, configure --disable-all --disable-cgi --disable-phpdbg --enable-cli, CFLAGS -O2 -g -falign-functions=64 -falign-loops=32, 2026-10-05T21:18+00:00  

| case | bytes | A ns/op | ± | B ns/op | ± | B vs A | A instr/op | B instr/op | instr B vs A |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| htmlspecialchars @ empty | 0 | 6.6 | 4.6% | 6.4 | 3.0% | 1.03× faster ~ | 120 | 120 | 1.00× |
| htmlspecialchars @ word-8 | 8 | 53.0 | 1.5% | 32.8 | 0.8% | 1.62× faster ✅ | 937 | 564 | 1.66× fewer |
| htmlspecialchars @ name-16 | 16 | 76.5 | 1.9% | 46.2 | 0.5% | 1.66× faster ✅ | 1428 | 637 | 2.24× fewer |
| htmlspecialchars @ title-40 | 40 | 152.0 | 1.3% | 86.6 | 0.4% | 1.75× faster ✅ | 2910 | 856 | 3.40× fewer |
| htmlspecialchars @ title-amp-40 | 40 | 175.7 | 2.4% | 104.4 | 0.6% | 1.68× faster ✅ | 3025 | 1329 | 2.28× fewer |
| htmlspecialchars @ ru-title-30 | 30 | 134.5 | 1.7% | 94.0 | 0.5% | 1.43× faster ✅ | 2076 | 1446 | 1.44× fewer |
| htmlspecialchars @ en-64 | 86 | 297.7 | 0.6% | 162.4 | 0.3% | 1.83× faster ✅ | 5635 | 1257 | 4.48× fewer |
| htmlspecialchars @ en-256 | 314 | 1090 | 0.6% | 538.3 | 0.2% | 2.02× faster ✅ | 19307 | 3231 | 5.98× fewer |
| htmlspecialchars @ en-1k | 1042 | 4317 | 0.7% | 1754 | 0.2% | 2.46× faster ✅ | 63146 | 10027 | 6.30× fewer |
| htmlspecialchars @ en-64k | 65583 | 321682 | 0.4% | 186046 | 0.5% | 1.73× faster ✅ | 3946273 | 611834 | 6.45× fewer |
| htmlspecialchars @ html-1k | 1076 | 4047 | 1.5% | 2193 | 0.8% | 1.85× faster ✅ | 67580 | 19322 | 3.50× fewer |
| htmlspecialchars @ html-page-4k | 4096 | 15277 | 1.4% | 8210 | 0.3% | 1.86× faster ✅ | 254920 | 69106 | 3.69× fewer |
| htmlspecialchars @ html-wiki-64k | 65536 | 289303 | 0.7% | 159883 | 0.4% | 1.81× faster ✅ | 4046899 | 1176236 | 3.44× fewer |
| htmlspecialchars @ md-4k | 4096 | 19045 | 0.3% | 6913 | 0.4% | 2.75× faster ✅ | 247527 | 38706 | 6.39× fewer |
| htmlspecialchars @ js-4k | 4096 | 20136 | 0.4% | 7135 | 0.3% | 2.82× faster ✅ | 251931 | 43581 | 5.78× fewer |
| htmlspecialchars @ js-min-4k | 4096 | 20113 | 0.9% | 7109 | 0.3% | 2.83× faster ✅ | 248711 | 45768 | 5.43× fewer |
| htmlspecialchars @ amp-1k | 1024 | 2402 | 0.3% | 1722 | 0.5% | 1.39× faster ✅ | 49264 | 35105 | 1.40× fewer |
| htmlspecialchars @ quot-1k | 1024 | 4451 | 0.5% | 3733 | 0.7% | 1.19× faster ✅ | 89846 | 77793 | 1.15× fewer |
| htmlspecialchars @ ru-1k | 1030 | 3812 | 0.9% | 2544 | 1.1% | 1.50× faster ✅ | 52357 | 40614 | 1.29× fewer |
| htmlspecialchars @ ru-64k | 65537 | 272911 | 1.4% | 226537 | 0.5% | 1.20× faster ✅ | 3306655 | 2555836 | 1.29× fewer |
| htmlspecialchars @ zh-1k | 1046 | 1970 | 0.5% | 1689 | 0.3% | 1.17× faster ✅ | 39103 | 33150 | 1.18× fewer |
| htmlspecialchars @ zh-64k | 65577 | 120665 | 0.4% | 102448 | 0.4% | 1.18× faster ✅ | 2420120 | 2047976 | 1.18× fewer |
| htmlspecialchars @ emoji-1k | 1071 | 3286 | 0.5% | 1709 | 0.5% | 1.92× faster ✅ | 52979 | 20062 | 2.64× fewer |
| htmlspecialchars !double_encode @ html-1k | 1076 | 4046 | 0.7% | 2196 | 0.5% | 1.84× faster ✅ | 67885 | 19622 | 3.46× fewer |
| htmlspecialchars !double_encode @ entities-1k | 1080 | 3432 | 1.0% | 2043 | 0.8% | 1.68× faster ✅ | 61105 | 22326 | 2.74× fewer |
| htmlspecialchars !double_encode @ amp-1k | 1024 | 2943 | 0.8% | 2306 | 0.6% | 1.28× faster ✅ | 67769 | 52588 | 1.29× fewer |
| htmlspecialchars ENT_DISALLOWED @ en-1k | 1042 | 6005 | 0.6% | 3786 | 0.7% | 1.59× faster ✅ | 74652 | 54402 | 1.37× fewer |
| htmlspecialchars ENT_DISALLOWED @ html-1k | 1076 | 5672 | 0.7% | 3448 | 0.8% | 1.65× faster ✅ | 78367 | 57643 | 1.36× fewer |
| htmlspecialchars cp1251 @ en-1k | 1042 | 3418 | 0.6% | 1780 | 0.4% | 1.92× faster ✅ | 61418 | 10385 | 5.91× fewer |
| htmlspecialchars cp1251 @ cp1251-1k | 1056 | 3391 | 1.7% | 3437 | 1.6% | 1.01× slower ~ | 62075 | 46134 | 1.35× fewer |
| htmlspecialchars cp1251 @ cp1251-64k | 65572 | 330637 | 0.7% | 305777 | 0.3% | 1.08× faster ✅ | 3808083 | 2809908 | 1.36× fewer |
| htmlspecialchars Shift_JIS @ sjis-1k | 1034 | 2529 | 0.7% | 2131 | 0.3% | 1.19× faster ✅ | 50541 | 41594 | 1.22× fewer |
| htmlspecialchars BIG5 @ big5-1k | 1061 | 3138 | 0.6% | 2653 | 1.9% | 1.18× faster ✅ | 50182 | 41969 | 1.20× fewer |
| htmlentities @ title-40 | 40 | 170.6 | 0.5% | 131.7 | 0.6% | 1.30× faster ✅ | 3767 | 2964 | 1.27× fewer |
| htmlentities @ en-1k | 1042 | 3586 | 1.1% | 2577 | 0.3% | 1.39× faster ✅ | 85974 | 65156 | 1.32× fewer |
| htmlentities @ html-1k | 1076 | 4863 | 1.4% | 3806 | 0.8% | 1.28× faster ✅ | 89812 | 68683 | 1.31× fewer |
| htmlentities @ ru-1k | 1030 | 4550 | 1.0% | 3539 | 0.6% | 1.29× faster ✅ | 65113 | 55339 | 1.18× fewer |

<sub>ns/op: median time of one evaluation, loop overhead subtracted; ±: spread of the samples (1.4826·MAD/median); B vs A: A time / B time; ✅/❌: every round of B was faster/slower than every round of A, by at least 1%; ~: rounds overlap, no clear difference; instr/op: instructions per evaluation</sub>

## json suite

Same builds and settings.

| case | bytes | A ns/op | ± | B ns/op | ± | B vs A | A instr/op | B instr/op | instr B vs A |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| json_encode @ en-1k | 1042 | 1863 | 4.4% | 1914 | 1.2% | 1.03× slower ~ | 15043 | 15043 | 1.00× |
| json_encode @ en-64k | 65583 | 114177 | 6.3% | 114684 | 3.2% | 1.00× ~ | 901299 | 901309 | 1.00× |
| json_encode @ html-1k | 1076 | 2057 | 2.4% | 2077 | 1.2% | 1.01× slower ~ | 19722 | 19722 | 1.00× |
| json_encode @ ru-1k | 1030 | 2625 | 0.8% | 2326 | 1.8% | 1.13× faster ✅ | 56579 | 50265 | 1.13× fewer |
| json_encode @ ru-64k | 65537 | 255890 | 0.5% | 242116 | 0.5% | 1.06× faster ✅ | 3553499 | 3153739 | 1.13× fewer |
| json_encode @ zh-1k | 1046 | 1919 | 0.5% | 1739 | 0.4% | 1.10× faster ✅ | 43934 | 39146 | 1.12× fewer |
| json_encode @ zh-64k | 65577 | 119309 | 0.4% | 108144 | 0.5% | 1.10× faster ✅ | 2709538 | 2409108 | 1.12× fewer |
| json_encode @ emoji-1k | 1071 | 1829 | 0.2% | 1807 | 0.3% | 1.01× faster ✅ | 30513 | 28928 | 1.05× fewer |
| json_encode UNESCAPED_UNICODE @ ru-1k | 1030 | 3803 | 0.4% | 3556 | 1.0% | 1.07× faster ✅ | 60317 | 54003 | 1.12× fewer |
| json_encode UNESCAPED_UNICODE @ ru-64k | 65537 | 304572 | 0.6% | 286944 | 0.5% | 1.06× faster ✅ | 3777962 | 3378202 | 1.12× fewer |
| json_encode UNESCAPED_UNICODE @ zh-1k | 1046 | 2166 | 0.5% | 1924 | 0.3% | 1.13× faster ✅ | 46800 | 42012 | 1.11× fewer |
| json_encode UNESCAPED_UNICODE @ zh-64k | 65577 | 131852 | 0.3% | 117001 | 0.5% | 1.13× faster ✅ | 2878894 | 2578474 | 1.12× fewer |
| json_encode UNESCAPED_UNICODE @ emoji-1k | 1071 | 1806 | 0.4% | 1746 | 0.4% | 1.03× faster ✅ | 27757 | 26172 | 1.06× fewer |
| json_decode @ json-en-64k | 67475 | 204356 | 0.8% | 204116 | 0.6% | 1.00× ~ | 1540678 | 1540681 | 1.00× |
| json_decode @ json-ru-64k | 180808 | 618530 | 0.6% | 614726 | 0.6% | 1.01× faster ~ | 6118041 | 6118040 | 1.00× |
| json_decode @ json-ru-raw-64k | 66592 | 137760 | 0.2% | 138475 | 0.2% | 1.01× slower ~ | 1245313 | 1245307 | 1.00× |

<sub>ns/op: median time of one evaluation, loop overhead subtracted; ±: spread of the samples (1.4826·MAD/median); B vs A: A time / B time; ✅/❌: every round of B was faster/slower than every round of A, by at least 1%; ~: rounds overlap, no clear difference; instr/op: instructions per evaluation</sub>

## A second machine

AMD Ryzen 9 5950X, GCC 15.2, htmlspecialchars suite, same commits and settings. The machine was
in use during the run (load average 3.2): the runner reported 11 cases with a disturbed round and
6 with a spread above 5%, so read the times as approximate; instruction counts are not affected.
The `empty` row shows what `layout?` is for: 112 instructions in both builds, one nanosecond
apart.

```
A: base — PHP 8.6.0-dev, 100e8f353ea ext/uri: Preserve empty query and fragment in URL builders
B: ascii-fast-path — PHP 8.6.0-dev, 0e4d8e73a21 ext/standard: Add a fast path for ASCII in htmlspecialchars()
CPU 1 (AMD Ryzen 9 5950X 16-Core Processor), governor powersave, turbo on, kernel 7.0.0-34-generic
4 rounds × 7 samples × 10 ms, cc (Ubuntu 15.2.0-16ubuntu1) 15.2.0, configure --disable-all --disable-cgi --disable-phpdbg --enable-cli, CFLAGS -O2 -g -falign-functions=64 -falign-loops=32, 2026-10-05T21:53+00:00

case                                           bytes  A ns/op      ±  B ns/op     ±                  B vs A  A instr/op  B instr/op  instr B vs A
htmlspecialchars @ empty                           0      6.4   6.2%      5.4  1.4%  1.19× faster ✓ layout?         112         112         1.00×
htmlspecialchars @ word-8                          8     41.5   0.6%     27.9  0.2%          1.49× faster ✓         916         555   1.65× fewer
htmlspecialchars @ name-16                        16     64.8   0.7%     34.4  0.3%          1.88× faster ✓        1410         630   2.24× fewer
htmlspecialchars @ title-40                       40    135.5   0.4%     54.2  0.2%          2.50× faster ✓        2902         855   3.39× fewer
htmlspecialchars @ title-amp-40                   40    147.8   0.3%     71.7  0.5%          2.06× faster ✓        3009        1311   2.30× fewer
htmlspecialchars @ ru-title-30                    30    103.6   0.3%     73.0  0.6%          1.42× faster ✓        2062        1434   1.44× fewer
htmlspecialchars @ en-64                          86    269.0   0.5%     99.2  0.5%          2.71× faster ✓        5631        1278   4.41× fewer
htmlspecialchars @ en-256                        314    968.7   1.5%    316.4  0.2%          3.06× faster ✓       19355        3345   5.79× fewer
htmlspecialchars @ en-1k                        1042     3751   0.4%     1010  0.5%          3.71× faster ✓       63347       10410   6.09× fewer
htmlspecialchars @ en-64k                      65583   250744   0.3%    65231  0.5%          3.84× faster ✓     3959850      636290   6.22× fewer
htmlspecialchars @ html-1k                      1076     4042   3.9%     1417  2.6%          2.85× faster ✓       67596       19698   3.43× fewer
htmlspecialchars @ html-page-4k                 4096    13612   1.8%     5081  2.1%          2.68× faster ✓      255009       71349   3.57× fewer
htmlspecialchars @ html-wiki-64k               65536   242254   0.4%    97694  0.7%          2.48× faster ✓     4047634     1209208   3.35× fewer
htmlspecialchars @ md-4k                        4096    15534   0.5%     4165  0.3%          3.73× faster ✓      248435       40537   6.13× fewer
htmlspecialchars @ js-4k                        4096    16204   1.7%     3997  0.4%          4.05× faster ✓      253119       44900   5.64× fewer
htmlspecialchars @ js-min-4k                    4096    15056   2.6%     3795  0.5%          3.97× faster ✓      249369       49194   5.07× fewer
htmlspecialchars @ amp-1k                       1024     2858   0.3%     2214  0.8%          1.29× faster ✓       48146       41160   1.17× fewer
htmlspecialchars @ quot-1k                      1024     5259   0.3%     5193  1.0%          1.01× faster ~       88746       81816   1.08× fewer
htmlspecialchars @ ru-1k                        1030     3210   2.3%     2784  6.1%          1.15× faster ✓       52463       40728   1.29× fewer
htmlspecialchars @ ru-64k                      65537   214921   0.8%   175920  2.0%          1.22× faster ✓     3315040     2562834   1.29× fewer
htmlspecialchars @ zh-1k                        1046     2107   0.7%     1774  5.8%          1.19× faster ✓       39443       33415   1.18× fewer
htmlspecialchars @ zh-64k                      65577   129543   0.8%   105778  1.3%          1.22× faster ✓     2442756     2065817   1.18× fewer
htmlspecialchars @ emoji-1k                     1071     2812   0.5%     1158  0.9%          2.43× faster ✓       53108       19977   2.66× fewer
htmlspecialchars !double_encode @ html-1k       1076     3994   2.6%     1422  2.0%          2.81× faster ✓       67900       20001   3.39× fewer
htmlspecialchars !double_encode @ entities-1k   1080     3450  10.2%     1282  0.7%          2.69× faster ✓       61083       22317   2.74× fewer
htmlspecialchars !double_encode @ amp-1k        1024     3315   0.4%     2648  0.5%          1.25× faster ✓       65600       58613   1.12× fewer
htmlspecialchars ENT_DISALLOWED @ en-1k         1042     4294   0.5%     3540  0.2%          1.21× faster ✓       72315       56685   1.28× fewer
htmlspecialchars ENT_DISALLOWED @ html-1k       1076     4443   0.9%     3501  1.2%          1.27× faster ✓       75957       59709   1.27× fewer
htmlspecialchars cp1251 @ en-1k                 1042     3755   8.6%     1023  0.3%          3.67× faster ✓       61625       10773   5.72× fewer
htmlspecialchars cp1251 @ cp1251-1k             1056     2903   3.2%     1711  0.4%          1.70× faster ✓       62291       41411   1.50× fewer
htmlspecialchars cp1251 @ cp1251-64k           65572   246149   0.4%   188197  0.3%          1.31× faster ✓     3823019     2518727   1.52× fewer
htmlspecialchars Shift_JIS @ sjis-1k            1034     3076   0.8%     2693  0.5%          1.14× faster ✓       50548       42509   1.19× fewer
htmlspecialchars BIG5 @ big5-1k                 1061     2864   0.6%     2957  0.8%          1.03× slower ~       50194       42606   1.18× fewer
htmlentities @ title-40                           40    178.8   0.6%    142.0  0.7%          1.26× faster ✓        3782        3062   1.24× fewer
htmlentities @ en-1k                            1042     3969   0.4%     3072  0.3%          1.29× faster ✓       86982       68244   1.27× fewer
htmlentities @ html-1k                          1076     4605   1.2%     3598  0.5%          1.28× faster ✓       90609       71529   1.27× fewer
htmlentities @ ru-1k                            1030     3622   3.9%     3024  8.1%          1.20× faster ✓       65668       54348   1.21× fewer
```

The json suite on the same machine: the same 1.1× fewer instructions for non-ASCII text, a
smaller gain in time than on the Intel machine.

```
case                                       bytes  A ns/op      ±  B ns/op     ±          B vs A  A instr/op  B instr/op  instr B vs A
json_encode @ en-1k                         1042    789.0   1.9%    792.7  0.8%         1.00× ~       15019       15019         1.00×
json_encode @ en-64k                       65583    52395   0.6%    52229  0.3%         1.00× ~      901393      901395         1.00×
json_encode @ html-1k                       1076    961.3  10.2%    987.8  2.3%  1.03× slower ~       19764       19764         1.00×
json_encode @ ru-1k                         1030     2401   1.8%     2322  5.1%  1.03× faster ~       55922       50059   1.12× fewer
json_encode @ ru-64k                       65537   198323   0.3%   189805  0.3%  1.04× faster ✓     3496508     3125315   1.12× fewer
json_encode @ zh-1k                         1046     1823   0.5%     1690  0.5%  1.08× faster ✓       43767       38979   1.12× fewer
json_encode @ zh-64k                       65577   112746   0.4%   103837  0.1%  1.09× faster ✓     2688143     2387714   1.13× fewer
json_encode @ emoji-1k                      1071     1221   0.3%     1202  0.6%  1.02× faster ~       29687       28276   1.05× fewer
json_encode UNESCAPED_UNICODE @ ru-1k       1030     3384   4.0%     3370  2.9%         1.00× ~       59839       53976   1.11× fewer
json_encode UNESCAPED_UNICODE @ ru-64k     65537   238910   1.3%   232536  1.3%  1.03× faster ~     3749368     3378167   1.11× fewer
json_encode UNESCAPED_UNICODE @ zh-1k       1046     2254   1.3%     2164  0.5%  1.04× faster ~       46773       41985   1.11× fewer
json_encode UNESCAPED_UNICODE @ zh-64k     65577   138969   2.8%   131897  0.4%  1.05× faster ~     2878871     2578437   1.12× fewer
json_encode UNESCAPED_UNICODE @ emoji-1k    1071     1346   0.7%     1347  0.4%         1.00× ~       27557       26146   1.05× fewer
json_decode @ json-en-64k                  67475   123299   0.5%   123410  0.5%         1.00× ~     1540342     1540340         1.00×
json_decode @ json-ru-64k                 180808   429209   0.6%   427015  0.6%  1.01× faster ~     6054537     6054540         1.00×
json_decode @ json-ru-raw-64k              66592    84333   0.3%    84368  0.6%         1.00× ~     1245274     1245278         1.00×
```

## Output

- `bench difftest html-encode base ascii-fast-path --seed 11 --count 20000`: identical output of
  `htmlspecialchars()` and `htmlentities()` on 20000 generated inputs, each with 13 flag sets,
  14 charsets and both values of `double_encode`.
- The same generator on a build of this commit with AddressSanitizer and
  UndefinedBehaviorSanitizer (`USE_ZEND_ALLOC=0`, 1500 inputs): clean.
- `ext/standard/tests/strings` and `ext/json/tests`: 782 passed, 0 failed, 63 skipped.

## Symfony Demo

Measured the way php-src CI does (`benchmark/benchmark.php`: php-cgi under callgrind, 50
requests), on a build with the CI set of extensions. Instructions per request:

| | master | with the change | |
|---|--:|--:|--:|
| whole request | 39,480,760 | 39,136,421 | −344,339 (−0.87%) |
| whole request, tracing JIT | 33,990,773 | 33,646,442 | −344,331 (−1.01%) |
| `htmlspecialchars()`, 207 calls | 474,203 | 148,784 | −325,419 |
| `htmlentities()`, 14 calls | 53,260 | 41,616 | −11,644 |
| `escape_html()` in `main/main.c`, 2 calls | 9,184 | 1,891 | −7,293 |
| everything else | | | +17 |

A call of `htmlspecialchars()` goes from 2,291 to 719 instructions on average. The three rows of
escaping entry points add up to −344,356, so the rest of the request changed by 17 instructions,
which is what two runs of the unchanged build differ by (the page prints the time). The
responses are byte-identical apart from those timestamps.

These runs were made on revision `b3da9261ed9` of the patch. It differs from `0e4d8e73a21` only
in the names of one function and one variable and in two comments, and `html.c` of both compiles
to the same machine code (identical `objdump -dr` output), which is why the numbers are quoted
for the final commit.

## Reproduce

```sh
git -C ../php-src fetch https://github.com/ArtUkrainskiy/php-src htmlspecialchars-plain-runs
./bench build base 100e8f353ea8ef841339ba4c74a0966a7eea5157
./bench build ascii-fast-path 0e4d8e73a21742064828f0ea098e2d3011b7d666
corpus/real/fetch.sh
./bench run htmlspecialchars --a base --b ascii-fast-path --perf --wait-idle 600
./bench run json --a base --b ascii-fast-path --perf --wait-idle 600
./bench difftest html-encode base ascii-fast-path --seed 11 --count 20000
```

Raw results: [htmlspecialchars.json](htmlspecialchars.json), [json.json](json.json)
(`./bench show <file> [--md]` renders them). The inputs `html-page-4k` and `html-wiki-64k` come
from live web pages and will differ slightly on another machine.
