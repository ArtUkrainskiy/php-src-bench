> Diagnostic alignment-profile measurements. Current publication results use the Docker flags: see [README.md](README.md).

# Inline UTF-8 decoding (php-src PR #24283)

Remeasured on 31 October 2026 against master `97335aa86f7`, which includes #24145. The candidate is the original PR `f3311658349` with the requested rename to `php_next_utf8_char_fast()`. The [candidate patch](candidate-20261031.patch) contains exactly the sources measured on top of that master. The PR commit is `df2b554e0b4`; its merge with master has the same tree as the measured snapshot.

`get_next_char()` is now always inlined into the exported `php_next_utf8_char()`. Callers in other translation units still make an out-of-line call. The new header helper decodes valid ASCII and two-, three- and four-byte UTF-8 at the call site. Invalid or truncated input falls back to the unchanged exported function. The exported API and its error handling are preserved.

## Results

Negative = fewer cycles (faster). Each percentage is the median of the paired PR/master ratios. The baseline cycle count is for GCC 13.3. No benchmark inputs or measurement scripts were changed.

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | GCC 15.2 (AMD) | clang 21.1 (AMD) |
|---|--:|--:|--:|--:|--:|--:|--:|
| Cyrillic, 4 KiB | 42,458 | −32% | −37% | −16% | −23% | −22% | −21% |
| Cyrillic, unescaped Unicode, 4 KiB | 56,035 | −20% | −27% | −28% | −25% | −15% | −30% |
| CJK, 4 KiB | 24,068 | −18% | −11% | −19% | −18% | −14% | −18% |
| CJK, unescaped Unicode, 4 KiB | 25,217 | −11% | −11% | −14% | −14% | −10% | −22% |
| Emoji, 4 KiB | 25,646 | −11% | −5% | −10% | −7% | −8% | −12% |
| Emoji, unescaped Unicode, 4 KiB | 19,134 | −16% | −14% | −18% | −11% | −19% | −20% |
| French, 4 KiB | 25,191 | −5% | −4% | −15% | −14% | −14% | −15% |
| ASCII with random-position e acute, 4 KiB | 24,310 | −3% | +1% | −2% | −9% | −5% | −6% |
| ASCII with periodic e acute, unescaped Unicode, 4 KiB | 21,650 | −2% | +33% | +3% | −6% | −5% | −8% |
| ASCII, 16 bytes | 143 | 0% | +1% | +4% | 0% | 0% | +3% |
| ASCII, 4 KiB | 8,630 | 0% | −4% | +3% | 0% | +5% | 0% |
| ASCII, 64 KiB | 138,416 | −1% | +3% | +1% | 0% | +5% | 0% |
| HTML, 4 KiB | 28,281 | +10% | −2% | 0% | +1% | +4% | 0% |
| URLs, 4 KiB | 31,931 | 0% | +2% | +3% | +1% | −2% | −1% |
| Quotes only, 4 KiB | 25,321 | +2% | +1% | 0% | 0% | +12% | −2% |
| A newline every 40 bytes, 4 KiB | 16,260 | +1% | −20% | +6% | 0% | +7% | 0% |
| 1,000 arrays of 10 fields | 966,495 | +2% | −1% | 0% | 0% | −2% | −1% |
| 1,000 objects of 10 properties | 941,047 | 0% | +2% | +2% | +2% | −2% | −1% |

## Summary

- Cyrillic, 4 KiB: −37% to −16% cycles and −17% to −14% instructions across the six builds.
- CJK, 4 KiB: −19% to −11% cycles and −14% to −10% instructions across the six builds.
- Emoji, 4 KiB: −12% to −5% cycles and −9% to −7% instructions across the six builds.

The full table contains [all 26 cases, instructions and the min–max range across passes](table-full-20261031.md). Individual pass ranges can be wider than the median change; retain the range when assessing small differences. Changes comparable to the A/A controls are not resolved by this series and should not be treated as established gains or regressions.

Observed cycle increases above 2% in this series:

- GCC 14.2, ASCII with periodic e acute, unescaped Unicode, 4 KiB: +33% cycles.
- GCC 15.2 (AMD), Quotes only, 4 KiB: +12% cycles.
- GCC 13.3, HTML, 4 KiB: +10% cycles.
- GCC 15.2 (AMD), A newline every 40 bytes, 4 KiB: +7% cycles.
- clang 18.1, A newline every 40 bytes, 4 KiB: +6% cycles.
- GCC 15.2 (AMD), ASCII, 64 KiB: +5% cycles.
- GCC 15.2 (AMD), ASCII, 4 KiB: +5% cycles.
- GCC 15.2 (AMD), A quote every 8 bytes, 4 KiB: +4% cycles.
- GCC 15.2 (AMD), HTML, 4 KiB: +4% cycles.
- clang 18.1, ASCII, 16 bytes: +4% cycles.
- GCC 14.2, ASCII, 64 KiB: +3% cycles.
- clang 18.1, URLs, 4 KiB: +3% cycles.
- GCC 13.3, ASCII with random-position e acute, unescaped Unicode, 4 KiB: +3% cycles.
- clang 18.1, ASCII, 4 KiB: +3% cycles.
- clang 18.1, ASCII with periodic e acute, unescaped Unicode, 4 KiB: +3% cycles.
- clang 21.1 (AMD), ASCII, 16 bytes: +3% cycles.
- GCC 15.2 (AMD), ASCII, 256 bytes: +2% cycles.
- clang 20.1, 1,000 objects of 10 properties: +2% cycles.
- GCC 13.3, 1,000 arrays of 10 fields: +2% cycles.
- GCC 14.2, URLs, 4 KiB: +2% cycles.

## Method

- Intel Core i7-13700H, CPU 2: GCC 13.3, GCC 14.2, clang 18.1 and clang 20.1; five alternating passes per case.
- AMD Ryzen 9 5950X, CPU 15: GCC 15.2 and clang 21.1; fifteen alternating passes per case. The selected CPU and its SMT sibling were idle before the series.
- Release builds with `--enable-werror --with-libxml --enable-xml`. The original report's flags were retained: `-O2 -g -falign-functions=64 -falign-loops=32`, the existing `align` profile. These are measurements with explicit alignment, rather than the Docker build profile.
- The existing [pairs-run.sh](pairs-run.sh) measures `perf stat` cycles and instructions for N calls minus zero calls, divided by N, and alternates the build order. Inputs come from the unchanged [cases.php](cases.php).
- A/A controls before and after the series cover ASCII, Cyrillic, emoji and 1,000 arrays. The largest absolute median deviation was 2.82%. [Control tables](controls-20261031.md) include the complete pass ranges.
- [Raw runs](cycles-20261031.txt) and [build metadata](metadata-20261031.json) accompany the generated tables. Tables were generated with the existing `speedup-table.py`, using paired ratios for both dates.

## ASCII regression on GCC 15

The 4 KiB and 64 KiB ASCII rows take about 5% more cycles at effectively unchanged instruction counts. A separate five-repeat `perf stat` diagnostic on the same 4 KiB input confirmed this direction. Its [base counters](ascii-gcc15-perf-base-gcc15.txt) and [candidate counters](ascii-gcc15-perf-head-gcc15.txt) show that the branch-miss increase is too small to account for the cycle difference.

Both versions place `php_json_escape_string()` and the scan-loop entry at the same addresses. Register allocation and instruction encodings inside the scan loop differ. The function grows from `0x12f2` to `0x1530` bytes, moving the following JSON functions by `0x240` bytes. These facts do not establish the exact microarchitectural cause. The regression is retained in the results; no source or flag changes were made to remove it.

## What changed after #24145

The exported decoder's lower cost reduces the instruction saving available to this PR. The effect on cycles varies by compiler and input. [The AMD comparison](comparison-amd-20261031.md) recalculates the 13 October and current raw series using the same paired statistic. The two masters differ by other commits too, so this is not an isolated before/after experiment for #24145.

The original measurements, implementation history and broader checks are preserved in the [13 October report](README-20261013.md). Its numbers refer to the older master and must not be used as current results.

## Correctness

The existing `pairs.php`, `triples.php`, `quads.php`, `positions.php`, `keys.php` and `udecode.php` produced identical output for master and the candidate on all six builds. The existing random generator also matched: 200,000 inputs with seed 1 per Intel compiler and 400,000 per AMD compiler, including values, keys, escaping flags and error statuses.

`ext/json`, `ext/xml` and `ext/standard/tests/strings` were run with the renamed candidate on GCC 13, clang 20 and GCC 15. This rerun does not claim a fresh sanitizer, aarch64, 32-bit or MSVC check. The identifier change was the only change to the decoder; measurements use rebuilt renamed binaries on every compiler.

## Reproduce

From the php-src-bench root, with php-src next to it, build both source trees with identical options. The source patch applies to master `97335aa86f7` and includes the rename:

```sh
export BENCH_CONFIGURE_EXTRA="--enable-werror --with-libxml --enable-xml"
./bench build --profile align --cc gcc,gcc-14,clang,clang-20 json-base 97335aa86f7
candidate_src="$(mktemp -d)"
git -C ../php-src worktree add --detach "$candidate_src" 97335aa86f7
git -C "$candidate_src" apply "$PWD/reports/json-encode-utf8-inline/candidate-20261031.patch"
PHP_SRC="$candidate_src" ./bench build --profile align --cc gcc,gcc-14,clang,clang-20 json-head .
```

On AMD, use `--cc gcc,clang` with the same source trees and options. The packaged runner only replaces the original machine-specific default build path with a relative one. Every measured run set `BENCH_BUILDS` explicitly, so this packaging change does not alter the executed measurements. Both runner hashes are recorded in the metadata, and the measured original is preserved with the private raw artifacts.

The unchanged runner expects build names prefixed with `json-`:

```sh
CPU=2 PASSES=5 ./pairs-run.sh cycles.txt gcc13:base-gcc13:head-gcc13 gcc14:base-gcc14:head-gcc14 clang18:base-clang18:head-clang18 clang20:base-clang20:head-clang20
CPU=15 PASSES=15 ./pairs-run.sh cycles-amd.txt gcc15:base-gcc15:head-gcc15 clang21:base-clang21:head-clang21
```

Run the same cases with the base binary in both roles for the A/A controls. The four control cases and raw control files are linked above. The original decoder-comparison generator remains an artifact of the older helper name in the archived report.
