# Review follow-up: route coverage and isolated variants

The [main product report](../README.md) remains the measurement of
`ca89fb5fb96399ed730cacb12d948025f83c4e6e` against stock
`ef99f4248f1450c39fb86fd7fd6f24c49b8d11eb`. This supplement addresses review
questions about real SIMD coverage, the value of the gram4 stage, and the scalar
route. Experimental variants are separate from the PR implementation.

## Results

A/B directions are stated in each row. Positive deltas mean B is slower. Times are microseconds per complete PHP `strpos()` operation.

| Case / A → B | GCC A | GCC B | Δ time | Clang A | Clang B | Δ time |
|---|--:|--:|--:|--:|--:|--:|
| 9-byte miss: stock → ca89 | 3.8264 | 3.4415 | -10.06% | 3.5199 | 3.1623 | -10.16% |
| 16-byte early: stock → ca89 | 0.0266 | 0.0209 | -21.34% | 0.0250 | 0.0174 | -30.45% |
| 32-byte early: stock → ca89 | 0.0402 | 0.0423 | +5.19% | 0.0388 | 0.0393 | +1.30% |
| 32-byte early, repeat | 0.0401 | 0.0421 | +5.01% | 0.0386 | 0.0391 | +1.33% |
| Selective gram: ca89 → no gram4 | 3.4371 | 2.5461 | -25.92% | 3.4753 | 2.4778 | -28.70% |
| Changing density: ca89 → no gram4 | 15.6866 | 10.1882 | -35.05% | 16.3126 | 10.3551 | -36.52% |
| Periodic ASCII: ca89 → no gram4 | 12.2889 | 31.3527 | +155.13% | 12.7708 | 34.0430 | +166.57% |
| Periodic DNA: ca89 → no gram4 | 12.2599 | 43.6577 | +256.10% | 12.5136 | 43.2905 | +245.95% |

The gram stage has a measurable benefit on the two periodic-needle inputs:
ca89 is **2.55–3.56 times faster** than the no-gram4 alternative there. It is not
universally beneficial: removing it saves about 26–29% on the selective `a` × 31
+ `b` miss and 35–37% on the changing-density input. Neither variant wins all
constructed workloads. These are implementation comparisons, not application-wide gains.

The 32-byte early-match loss is real on GCC: the independent repeat is **+5.00%**,
about **+2.0 ns** per call; instructions rise from about 810 to 837 (+3.33%). Clang
is about +1.3%, with overlapping rounds and an Unclear native verdict. The small
absolute cost does not erase the regression.

The six ordinary controls span −0.97% to +1.59% for no-gram4 versus ca89, and
−1.92% to +2.27% for scalar versus ca89. A/A median deltas stay within ±1.75%.
Four of the 113 elapsed rows are flagged as disturbed, including one A/A; they
remain marked Noise in the full tables. There were no idle-wait timeouts.
The prior main-report regressions, including the Intel Clang losses around 4–5%,
are unchanged. There is no universal “under 3%” claim.

The PR retains the ca89 algorithm; the follow-up commit changes tests and comments.
No ablation variant was adopted. The measurements establish a specific value for
gram4 and also show its costs. The full tables retain every original and repeat:

- [Elapsed time, cycle/instruction deltas, spread and quality](time.md).
- [Absolute cycles and instructions](counters.md).
- [Native compiler matrices and same-row cycle A/A controls](cycles.md).
- [Unrounded metrics](metrics.json), [source hashes](manifest.json),
  [binary provenance](binary-provenance.json), [lossless native series and logs](native.tar.gz).

## Source and test corrections

The branch adds
[`8c6759c6826`](https://github.com/ArtUkrainskiy/php-src/commit/8c6759c6826e59aeaf14db2696c503f5334f81ad)
([patch](review-tests.patch)). Its C changes remove folding comments; the remaining
C token sequence matches ca89. The PHPT descriptions no longer attribute short
binary inputs or three-byte needles to adaptive SIMD paths.

The adaptive PHPT now checks 703 inputs, including 160 new inputs whose paths are
independently audited. Eight needle lengths cover pair-relative positions 15, 16,
17 and all 15 starts in a partial final block. Other inputs exercise a selective
gram, a dense sample, later density changes, and the remembered-prefix branch of
periodic Two-Way. The old needle containing a unique `q` did not establish that
last property.

[Route auditing](audit.py) extracts the matcher from the supplied PHP source;
instrumentation is confined to a generated standalone copy. GCC and sanitized
Clang confirm the first 160 PHPT inputs plus the two extra periodic measurement
inputs: [GCC evidence](audit-gcc.json), [Clang ASan/UBSan evidence](audit-clang-asan.json).
Both an omitted pair mask bit and an omitted scalar tail are detected.

[Machine-code comparison](machine-code.json) found identical addresses, sizes and
bytes for all seven emitted matcher functions on both GCC 15 and Clang 21, and
for `php_explode`. Clang `zif_strpos` differs in the address of an error string in
a cold branch; its size, position and valid-input path remain the same. This is
not a claim that complete binaries are identical. Original ca89 measurements
retain their original source and binary identities.

## Correctness checks

| PHP build | String PHPT | Passed | Skipped | Failed | Warned |
|---|--:|--:|--:|--:|--:|
| 8c6759, GCC 15 release | 765 | 703 | 62 | 0 | 0 |
| 8c6759, Clang 21 release | 765 | 703 | 62 | 0 | 0 |
| 8c6759, Clang 21 debug + ASan/UBSan | 765 | 684 | 81 | 0 | 0 |

The full PHP sanitizer run uses `USE_ZEND_ALLOC=0`; extra skips include tests
requiring Zend MM. Each of the four experimental release binaries also passes
all five `str_search_*.phpt` files. See the [summary](php-validation-summary.json) and [build/test logs](php-validation-logs.tar.gz).

Before measurement, exact matcher extraction for control, no-gram4 and scalar
was tested under ASan/UBSan with GCC and Clang. **Each of the six runs** checks
100,000 random inputs and 135,460 guarded configurations, with a shared seed and
boundary set. The complete matcher and available stage entry points agree with
`memmem`: [validation evidence](variant-validation.json). These counts describe
repeated validation of the same corpus, not six independent corpora.

External exhaustive-test counts quoted during review are not included in our
own validation totals; the external harness was not supplied.

## Measured variants and inputs

| Name | Source | Change from ca89 |
|---|---|---|
| Stock | `ef99f4248f14` | Original matcher |
| ca89 | `ca89fb5fb963` | PR algorithm used in the main report |
| No gram4 | `fa81a3379208` | Both pair-budget exits pass the same suffix directly to Two-Way; gram4 is removed: [patch](no-gram4.patch) |
| Scalar | `db4d3f65c692` | Only the three new matcher SSE2 guards are disabled: [patch](scalar.patch) |

Scalar keeps other PHP SIMD paths enabled. It measures the fallback on the same
x86-64 CPU; it does not simulate MSVC, AArch64 or their code generation. Native
ARM64, Windows and 32-bit runs remain outside this evidence.

Everyday inputs and expressions come from the unchanged owned product corpus.
The new route fixtures are deliberately constructed algorithmic stress cases,
not an assumed distribution of application traffic.

| Route group | Haystack / needle | Search and purpose |
|---|---|---|
| `short9/16/31` | About 14 KiB ordinary ASCII text; a 9/16/31-byte prefix of `product-token-in-request-metadata` | Absent or inserted at offset 7; compact Sunday setup and early success |
| `long/ordinary-miss`, `long/early` | Ordinary ASCII text; `a` × 31 + `b` | Cheap mismatches or early success; account for adaptive-dispatch overhead |
| `pair/ascii`, `pair/dna`, `pair/binary` | 16 KiB of one byte; 32-byte needle ending in a distinct absent byte | Trigger Sunday handoff; selective pair over different byte alphabets |
| `gram/selective` | 16 KiB: `a` × 64, `c`, then `ab`; needle `a` × 31 + `b` | Dense false pairs, zero gram sample hits; absent and late success |
| `gram/dense` | Same prefix, then `aaab` | Gram sample rejected; cost of preparing an unhelpful stage |
| `gram/changing` | 64 KiB, initially `ab`, then `aaab` after byte 8192 | Sample initially selective, then gram budget forces Two-Way |
| `twoway/periodic-memory` | 64 KiB of `bb` + (`ab` × 15); needle `ab` × 16 | Dense filters, periodic Two-Way with remembered work |
| `threshold/8191/8192` | Repeated `a`; needle `a` × 31 + `b` | The haystack threshold for adaptive accounting |
| `gram-periodic/ascii` | 64 KiB, costly nonmatching prefix, then `abac`; needle `ab` × 16 | Dense pairs, selective gram and a short Two-Way period |
| `gram-periodic/dna` | 64 KiB, costly nonmatching prefix, then `ACGA`; needle `ACGT` × 8 | Dense C/G pairs, absent four-byte motif |

The two extra periodic inputs were added **after** the initial `a` × 31 + `b`
against `ab` pilot favoured no-gram4. That pilot is retained. The extension tests
a distinct periodic-needle hypothesis; it is not a replacement for an unfavourable
input. [Main supplementary suite](suite.php), [periodic extension](gram-periodic-suite.php).

## Method and reproduction

All new measurements use the AMD Ryzen 9 5950X, CPU 15, GCC 15.2 and Clang 21.1,
matched release docker profiles. The stock and ca89 binary hashes match the
original product series. The orchestrator uses CPU 14. Builds and
correctness tests finish before timing. Governor is performance; turbo is on.
Elapsed timing uses four alternating rounds, one approximately one-second sample
per side after at least one second of warmup. Each selected pair runs separately.
The native tool subtracts median empty-loop overhead. Instructions are from that
series; cycles come from a separate three-pass `bench compare` series. They must
not be combined into exact simultaneous IPC.

The full main corpus is not rerun. The supplementary universe is 38 cases:
18 product controls, 18 route cases and the two periodic extensions. New elapsed
measurements cover 26 distinct case identities: all route cases and six product
controls. The remaining product cases receive cycle/instruction diagnostics;
their full ca89-versus-stock elapsed evidence remains in the main report.

The six timed product controls are EN clean/early banlists, `explode('::')`,
`substr_count('::')`, `str_replace('::')` and template rendering. No-gram4 elapsed
pairs cover the five main gram/Two-Way cases plus these controls. Scalar elapsed
pairs cover the ten main pair/gram/Two-Way/threshold cases plus the controls.
Stock-versus-ca89 covers all 18 main route cases. Both compilers measure all
three comparisons on the periodic extension. A/A precedes and follows the main
series. Unclear and disturbed results remain visible. A single independent repeat of
`long/early` on each compiler was selected after the GCC original exceeded +3%;
[the finite policy](confirmation-policy.json) preserves both originals and repeats.

Use the [main build/corpus instructions](../REPRODUCE.md), including the owned-only
corpus option. For experimental sources, create clean worktrees at ca89, apply
the respective patch, commit it locally, then build with the same profile:

```sh
PHP_SRC="$SOURCE_NOGRAM" ./bench build --slim --cc gcc-15,clang-21 review-no-gram4 HEAD
PHP_SRC="$SOURCE_SCALAR" ./bench build --slim --cc gcc-15,clang-21 review-scalar HEAD
python3 reports/substr-adaptive-search/review/reproduce.py \
  --bench-root "$BENCH_ROOT" --builds "$BENCH_BUILDS" --out "$REVIEW_OUT" \
  --cpu 15 --orchestrator-cpu 14 \
  --control-commit "$CANDIDATE_COMMIT" \
  --nogram-commit "$NOGRAM_COMMIT" --scalar-commit "$SCALAR_COMMIT"
```

The driver expects existing `base-{gcc15,clang21}` and
`product-guard-{gcc15,clang21}` builds, as in the main report. Use the commits
recorded in your build metadata for the commit arguments. A locally recreated
control commit may differ from ca89 in identity; pass its actual commit explicitly.
Run the same command with `--smoke` first, then `--extra` and `--confirm` after
the main series.
Output directories can be resumed; existing binary fingerprints must match.

For route auditing against the follow-up source:

```sh
python3 reports/substr-adaptive-search/review/audit.py \
  --source "$PHP_SOURCE" --cc clang --sanitize --out "$AUDIT_OUT"
```

The generated audit C files are temporary instrumentation, not production source.
No new platform dispatch or algorithm change is part of the test/comment fix.

To regenerate this supplement from the published archive (no measurements):

```sh
mkdir -p "$REVIEW_DATA"
tar -xzf reports/substr-adaptive-search/review/native.tar.gz -C "$REVIEW_DATA"
python3 reports/substr-adaptive-search/review/render.py \
  --bench-root "$BENCH_ROOT" --php "$BENCH_PHP" --data "$REVIEW_DATA" \
  --out reports/substr-adaptive-search/review
python3 reports/substr-adaptive-search/review/check.py
```

The independent check verifies 113 elapsed pairs, 26 timed input identities,
empty-loop subtraction, paired source/output identities, unchanged original
control binaries, and the separate cycle arithmetic. The native cycle matrices
also participate in `bench report check` through their generated table blocks.
The supplement does not replace upstream CI or native ARM/Windows validation.

Machine paths in display-only counter warnings and route-audit source labels are
normalized. The native archive retains the original counter JSON and logs; numeric
fields are unchanged and checked independently.
