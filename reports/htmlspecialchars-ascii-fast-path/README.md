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
- One machine, one compiler: GCC 13.3 on an Intel i7-13700H (x86-64). On a second machine
  (GCC 15.2, a virtual Haswell core, wall time only) the same comparison gave English 2.5–2.8×,
  HTML 1.8–2.0×, Russian 1.3×, cp1251 1.3–1.6× faster, with no row slower.

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
