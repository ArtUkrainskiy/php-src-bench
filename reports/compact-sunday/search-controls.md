# Search-shape controls

Full PHP CLI builds: compact `8d7babbc364` versus master `cf1b5771a76`.
AMD Ryzen 9 5950X, CPU 15, performance governor, turbo on; the core is not reserved.
All inputs are 4096 bytes. Times are microseconds per complete PHP operation,
with empty-loop subtraction. All changes are relative to master; negative is lower cost.

The main elapsed matrix has 21 inputs per compiler; a separate GCC 15 check
adds a 64-byte repeated-prefix search and same-input A/A. The counter matrix
has 58 inputs. Ordinary absent, early, late and
repeated-prefix searches use needles of 9, 16 and 31 bytes. Early-match controls
also use 32, 64 and 256 bytes. `substr_count()` and `str_replace()` repeat searches
for 9/16/31-byte needles. These repeated fixtures contain 86/75/58 matches.

All four single-search shapes use `strpos()`. The ordinary ASCII filler contains order/payment/delivery messages. Early matches
start at zero; late matches end at the input boundary. Repeated-prefix inputs are
`a` repeated 4096 times, searched for `a` repeated `m-1` times followed by `b`.

Each elapsed comparison has one paired round: at least 3 seconds warmup and ten
approximately one-second samples per build. The two measurement batches each
have before/after identical-binary A/A on the 16-byte repeated-prefix input.
The additional 64-byte check has its own same-input A/A. Counters are a separate
five-pass series, with Clang 21 identical-binary controls before and after.
Small movements are descriptive; they do not establish a statistical speedup.
Cycle deltas are the median of five paired compact/master ratios; instruction
deltas compare median counts.

The <32 cutoff limits the optimization to short tokens; it is not the byte-table
capacity limit. All shifts fit in a byte up to needle length 254. These
measurements do not establish that 32 is an optimal cutoff.

## Clang 21.1

Largest observed elapsed A/A: 1.36%.

| Search | Needle B | master µs | compact µs | Time Δ | Cycles Δ | Instr. Δ |
|---|--:|--:|--:|--:|--:|--:|
| Absent in ordinary text | 9 | 1.0755 | 0.9570 | -11.02% | -11.06% | -0.53% |
| Match at offset 0 | 9 | 0.0181 | 0.0119 | -34.24% | -41.24% | -13.17% |
| Match at the last position | 9 | 1.0798 | 0.9570 | -11.37% | -10.93% | -0.53% |
| Repeated prefix, no match | 9 | 7.6186 | 7.2358 | -5.02% | -4.49% | -0.03% |
| Absent in ordinary text | 16 | 0.5951 | 0.5334 | -10.37% | -11.08% | -0.98% |
| Match at offset 0 | 16 | 0.0215 | 0.0160 | -25.50% | -25.54% | -11.05% |
| Match at the last position | 16 | 0.6044 | 0.5375 | -11.06% | -10.40% | -0.96% |
| Repeated prefix, no match | 16 | 10.0987 | 10.4297 | +3.28% | -3.11% | -0.02% |
| Absent in ordinary text | 31 | 0.4920 | 0.4442 | -9.73% | -9.87% | -1.22% |
| Match at offset 0 | 31 | 0.0291 | 0.0217 | -25.43% | -23.23% | -7.81% |
| Match at the last position | 31 | 0.5019 | 0.4550 | -9.34% | -10.51% | -1.16% |
| Repeated prefix, no match | 31 | 17.3782 | 16.6855 | -3.99% | -2.58% | -0.01% |
| Match at offset 0 | 32 | 0.0296 | 0.0294 | -0.69% | +0.75% | +2.98% |
| Match at offset 0 | 64 | 0.0422 | 0.0430 | +1.93% | +1.70% | +2.83% |
| Match at offset 0 | 256 | 0.1218 | 0.1245 | +2.23% | -0.90% | +2.65% |
| substr_count, repeated matches | 9 | 1.5646 | 1.2428 | -20.57% | -23.77% | -12.71% |
| str_replace, repeated matches | 9 | 3.4361 | 2.6877 | -21.78% | -22.48% | -11.48% |
| substr_count, repeated matches | 16 | 1.4035 | 1.1777 | -16.09% | -17.04% | -11.55% |
| str_replace, repeated matches | 16 | 2.9807 | 2.5821 | -13.37% | -17.30% | -10.53% |
| substr_count, repeated matches | 31 | 1.2931 | 1.1395 | -11.88% | -12.69% | -8.29% |
| str_replace, repeated matches | 31 | 2.7379 | 2.6019 | -4.97% | -6.28% | -7.78% |

## GCC 15.2

Largest observed elapsed A/A: 2.10%.

| Search | Needle B | master µs | compact µs | Time Δ | Cycles Δ | Instr. Δ |
|---|--:|--:|--:|--:|--:|--:|
| Absent in ordinary text | 9 | 1.1551 | 1.0530 | -8.83% | -10.78% | -1.68% |
| Match at offset 0 | 9 | 0.0225 | 0.0158 | -29.84% | -32.46% | -31.71% |
| Match at the last position | 9 | 1.1635 | 1.0493 | -9.81% | -9.26% | -1.66% |
| Repeated prefix, no match | 9 | 6.2265 | 6.1249 | -1.63% | -2.50% | -0.11% |
| Absent in ordinary text | 16 | 0.6428 | 0.5833 | -9.26% | -8.99% | -3.04% |
| Match at offset 0 | 16 | 0.0252 | 0.0187 | -25.83% | -28.20% | -26.38% |
| Match at the last position | 16 | 0.6470 | 0.5881 | -9.10% | -9.48% | -2.98% |
| Repeated prefix, no match | 16 | 8.1452 | 8.2980 | +1.87% | -0.26% | -0.07% |
| Absent in ordinary text | 31 | 0.5401 | 0.4869 | -9.85% | -9.87% | -3.70% |
| Match at offset 0 | 31 | 0.0330 | 0.0267 | -19.22% | -21.99% | -19.40% |
| Match at the last position | 31 | 0.5483 | 0.4974 | -9.30% | -10.01% | -3.54% |
| Repeated prefix, no match | 31 | 15.3771 | 15.8188 | +2.87% | +1.17% | -0.04% |
| Match at offset 0 | 32 | 0.0335 | 0.0337 | +0.49% | +0.48% | +0.67% |
| Match at offset 0 | 64 | 0.0492 | 0.0493 | +0.33% | -0.14% | +0.43% |
| Match at offset 0 | 256 | 0.1501 | 0.1502 | +0.07% | -0.08% | +0.14% |
| substr_count, repeated matches | 9 | 1.6778 | 1.2511 | -25.43% | -27.14% | -31.86% |
| str_replace, repeated matches | 9 | 3.6052 | 2.7012 | -25.08% | -26.39% | -29.68% |
| substr_count, repeated matches | 16 | 1.3591 | 0.9888 | -27.25% | -25.83% | -28.05% |
| str_replace, repeated matches | 16 | 2.9713 | 2.2637 | -23.81% | -21.14% | -26.33% |
| substr_count, repeated matches | 31 | 1.4600 | 1.2879 | -11.79% | -9.92% | -20.75% |
| str_replace, repeated matches | 31 | 3.2657 | 2.7529 | -15.70% | -13.64% | -19.86% |

## Synthetic repeated-prefix regression

A separate elapsed check follows the 58-case counter sweep. It uses `strpos(str_repeat("a", 4096), str_repeat("a", 63) . "b")`, returning `false`.

| Compiler | Needle B | master µs | compact µs | Time Δ | Cycles Δ | Instr. Δ |
|---|--:|--:|--:|--:|--:|--:|
| GCC 15.2 | 64 | 30.7851 | 40.2358 | +30.70% | +30.94% | +0.00% |

Same-input identical-binary A/A: +0.00%. This needle uses the existing wide table; the byte table is not involved. A separate three-pass `bench why` run records about 1 versus 2019 branch misses per call, with nearly unchanged instruction counts. The loop addresses differ. The precise placement mechanism has not been isolated.

This input is deliberately constructed to produce repeated long partial matches. The patch retains Sunday’s existing quadratic worst case. Keep this regression separate from the ordinary-text results when assessing the trade-off.

## Elapsed A/A

All main-batch A/A rows use the 16-byte repeated prefix; amd-wide-check uses 64 bytes.

| Batch | Compiler | Position | First µs | Second µs | Time Δ |
|---|---|---|--:|--:|--:|
| amd-primary | clang21 | after | 10.7378 | 10.6956 | -0.39% |
| amd-primary | gcc15 | after | 8.0939 | 8.0389 | -0.68% |
| amd-primary | clang21 | before | 10.8906 | 10.7420 | -1.36% |
| amd-primary | gcc15 | before | 8.1024 | 8.0990 | -0.04% |
| amd-matrix | clang21 | after | 10.8668 | 10.7851 | -0.75% |
| amd-matrix | gcc15 | after | 8.0243 | 8.0737 | +0.62% |
| amd-matrix | clang21 | before | 10.8285 | 10.8410 | +0.12% |
| amd-matrix | gcc15 | before | 8.0621 | 8.2314 | +2.10% |
| amd-wide-check | gcc15 | after | 30.8248 | 30.8256 | +0.00% |

## Coverage and correctness

The counter matrix covers four search shapes at byte lengths 8, 9, 16, 24, 31,
32, 33, 48, 64, 128, 254, 255 and 256, plus six repeated-operation cases: 58 in
total. All 58 return independent Python-computed expected values in both compiler
pairs and the full PHP ASan/UBSan build. Source commits and executable hashes are
checked before measurement. There are no Intel elapsed results in this dataset.

## Generated code

In the captured Clang 21 PHP binaries the inner candidate-comparison loop is
byte-identical: 19 bytes, six instructions. Table preparation, shift loads, stack
frame sizes and code addresses differ. The identical inner loop does not establish
a unique cause for small timing movements or predict other compiler versions.

[All 58 counter cases and ranges](search-counters.md) · [Unrounded values](search-metrics.json) · [Native data and measurement scripts](data/search-controls.tar.gz) · [Exact inputs and expectations](search-cases.json) · [Suite](search-suite.php) · [Raw hashes](search-manifest.json) · [Clang 21 disassembly](search-codegen.json).

To rerun an individual case, use `bench run search-suite.php` with matched master/compact builds, the case filter, `--rounds 1 --samples 10 --target-ms 1000 --warmup-ms 3000`. Run one case at a time. Use `bench compare` with `--passes 5 --target-ms 50` for counters. CPU and build-directory selection follow [the reproduction instructions](reproduce.md).
