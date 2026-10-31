# Inline UTF-8 decoding (php-src PR #24283)

Docker-profile measurements against master `97335aa86f7`, including #24145, and PR head `df2b554e0b4`. The [source patch](candidate-20261031.patch) is unchanged from the preceding run; only the build profile changed. All six compiler pairs were rebuilt and checked with the official Docker-image flags.

`get_next_char()` is already always inlined into the exported `php_next_utf8_char()`. The header helper `php_next_utf8_char_fast()` avoids the exported call for valid UTF-8. Invalid or truncated input falls back to the unchanged exported function, preserving its error handling and ABI.

## Results

Negative = fewer cycles (faster). The baseline cycle column is for GCC 13.3. Unescaped Unicode rows use `JSON_UNESCAPED_UNICODE`.

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | GCC 15.2 (AMD) | clang 21.1 (AMD) |
|---|--:|--:|--:|--:|--:|--:|--:|
| Cyrillic, 4 KiB | 35,063 | −19% | −28% | +12% | −22% | −22% | −14% |
| Cyrillic, unescaped Unicode, 4 KiB | 56,511 | −15% | −29% | −21% | −25% | −17% | −22% |
| CJK, 4 KiB | 22,791 | −7% | −11% | −20% | −19% | −24% | −21% |
| CJK, unescaped Unicode, 4 KiB | 25,056 | −11% | −11% | −13% | −15% | −18% | −20% |
| Emoji, 4 KiB | 25,041 | −10% | −9% | −14% | −9% | −7% | −11% |
| Emoji, unescaped Unicode, 4 KiB | 18,933 | −17% | −16% | −14% | −14% | −22% | −18% |
| French, 4 KiB | 24,467 | −4% | −3% | −1% | −17% | −15% | −8% |
| ASCII with random-position e acute, 4 KiB | 23,056 | −5% | −7% | −3% | −10% | −5% | −4% |
| ASCII with periodic e acute, unescaped Unicode, 4 KiB | 21,786 | −17% | +24% | −6% | −4% | −6% | −3% |
| ASCII, 16 bytes | 135 | +7% | −4% | 0% | +1% | +1% | +1% |
| ASCII, 4 KiB | 8,114 | +6% | 0% | 0% | 0% | +6% | +1% |
| ASCII, 64 KiB | 134,588 | +3% | 0% | 0% | 0% | +5% | 0% |
| HTML, 4 KiB | 28,450 | +5% | −1% | −1% | 0% | +4% | 0% |
| URLs, 4 KiB | 30,128 | +8% | +1% | −1% | 0% | −1% | −1% |
| Quotes only, 4 KiB | 25,683 | 0% | 0% | −1% | +1% | +12% | 0% |
| A newline every 40 bytes, 4 KiB | 22,313 | −33% | −21% | 0% | 0% | +7% | 0% |
| 1,000 arrays of 10 fields | 888,668 | +16% | −6% | +3% | −4% | −1% | 0% |
| 1,000 objects of 10 properties | 832,933 | +13% | +2% | +1% | +4% | 0% | 0% |

- Cyrillic, 4 KiB: −28% to +12% cycles across the six builds.
- CJK, 4 KiB: −24% to −7% cycles across the six builds.
- Emoji, 4 KiB: −14% to −7% cycles across the six builds.

[All 26 cases, instruction changes and pass ranges](table-full-docker-20261031.md), [raw runs](cycles-docker-20261031.txt), [A/A controls](controls-docker-20261031.md), [build metadata](metadata-docker-20261031.json).

Observed cycle increases above 2% in this series, including differences that may be within the control noise:

- GCC 14.2, ASCII with periodic e acute, unescaped Unicode, 4 KiB: +24% cycles.
- GCC 13.3, 1,000 arrays of 10 fields: +16% cycles.
- GCC 13.3, 1,000 objects of 10 properties: +13% cycles.
- GCC 13.3, An array of 100 distinct keys: +12% cycles.
- clang 18.1, Cyrillic, 4 KiB: +12% cycles.
- GCC 15.2 (AMD), Quotes only, 4 KiB: +12% cycles.
- GCC 13.3, URLs, 4 KiB: +8% cycles.
- GCC 15.2 (AMD), A newline every 40 bytes, 4 KiB: +7% cycles.
- GCC 13.3, ASCII, 16 bytes: +7% cycles.
- GCC 15.2 (AMD), ASCII, 4 KiB: +6% cycles.
- GCC 15.2 (AMD), ASCII, 256 bytes: +6% cycles.
- GCC 13.3, ASCII, 4 KiB: +6% cycles.
- GCC 13.3, HTML, 4 KiB: +5% cycles.
- GCC 15.2 (AMD), ASCII, 64 KiB: +5% cycles.
- GCC 13.3, ASCII, 256 bytes: +5% cycles.
- GCC 15.2 (AMD), HTML, 4 KiB: +4% cycles.
- clang 20.1, 1,000 objects of 10 properties: +4% cycles.
- clang 21.1 (AMD), ASCII, 256 bytes: +4% cycles.
- clang 18.1, 1,000 arrays of 10 fields: +3% cycles.
- clang 18.1, An array of 100 distinct keys: +3% cycles.
- GCC 15.2 (AMD), A quote every 8 bytes, 4 KiB: +3% cycles.
- GCC 13.3, ASCII, 64 KiB: +3% cycles.
- clang 18.1, A quote every 8 bytes, 4 KiB: +2% cycles.
- clang 20.1, ASCII, 256 bytes: +2% cycles.

No cycle difference at unchanged instruction counts is attributed to an algorithmic improvement here. Those rows need code-placement or microarchitectural analysis before a stronger conclusion.

## Method

Release builds with the official PHP Docker-image CFLAGS plus `-g` for profiling, using the existing `docker` profile and `--enable-werror`:

```text
CFLAGS=-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64
LDFLAGS=-Wl,-O1 -pie
```

The flags were checked against the [official Dockerfile](https://github.com/docker-library/php/blob/master/8.5/trixie/cli/Dockerfile). Every build's metadata was checked, and every executable was checked for ELF PIE. No explicit `-falign-*` options were used.

Intel Core i7-13700H, CPU 2: GCC 13.3, GCC 14.2, clang 18.1 and clang 20.1, five alternating passes. AMD Ryzen 9 5950X, CPU 15: GCC 15.2 and clang 21.1, fifteen alternating passes. The original 26 inputs and measurement runner were reused unchanged.

`perf stat` cycles and instructions for N calls minus zero calls, divided by N. Percentages are medians of paired PR/master ratios. A/A controls before and after cover ASCII, Cyrillic, emoji and 1,000 arrays. Maximum absolute A/A median deviation: Intel 1.31%, AMD 0.23%. Individual passes can be noisier; the full table retains their min–max ranges. Changes comparable to these controls are not resolved by this series.

## Correctness

The existing `pairs.php`, `triples.php`, `quads.php`, `positions.php`, `keys.php` and `udecode.php` matched master on all six fresh Docker-profile builds. The existing fuzzer also matched for values, keys, escaping flags and error statuses: 200,000 inputs with seed 1 per Intel compiler and 400,000 per AMD compiler.

`ext/json`, `ext/xml` and `ext/standard/tests/strings` passed with the Docker-profile GCC 13, clang 20 and GCC 15 candidates. No fresh sanitizer, aarch64, 32-bit or MSVC check is claimed.

## Previous measurements

The [31 October alignment-profile figures](README-align-20261031.md) are retained as diagnostics. The [13 October report](README-20261013.md) is historical too. Neither supplies the current publication numbers. Their compiler flags differ from this report, so cross-date cycle differences do not isolate #24145.

## Reproduce

From php-src-bench, with php-src next to it:

```sh
export BENCH_CONFIGURE_EXTRA="--with-libxml --enable-xml"
./bench build --profile docker --cc gcc,gcc-14,clang,clang-20 json-base 97335aa86f7
candidate_src="$(mktemp -d)"
git -C ../php-src worktree add --detach "$candidate_src" 97335aa86f7
git -C "$candidate_src" apply "$PWD/reports/json-encode-utf8-inline/candidate-20261031.patch"
PHP_SRC="$candidate_src" ./bench build --profile docker --cc gcc,gcc-14,clang,clang-20 json-head .
```

On AMD use `--cc gcc,clang` with the same sources and profile. Then run the existing [pairs-run.sh](pairs-run.sh) with the same [cases.php](cases.php):

```sh
CPU=2 PASSES=5 ./pairs-run.sh cycles.txt gcc13:base-gcc13:head-gcc13 gcc14:base-gcc14:head-gcc14 clang18:base-clang18:head-clang18 clang20:base-clang20:head-clang20
CPU=15 PASSES=15 ./pairs-run.sh cycles-amd.txt gcc15:base-gcc15:head-gcc15 clang21:base-clang21:head-clang21
```

For controls, use the base binary in both roles on `ascii-4k`, `cyrillic-4k`, `emoji-4k` and `api-1000-records`. Every measured run set `BENCH_BUILDS` explicitly; the packaged runner's relative default build path does not affect these runs. Tables were generated from the raw data with the existing `speedup-table.py`.
