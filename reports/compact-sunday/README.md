# Compact Sunday shift tables

This report benchmarks the compact-Sunday candidate
[`8d7babbc364`](https://github.com/ArtUkrainskiy/php-src/commit/8d7babbc364ffcf28dac9777ce807edc9adbb534)
([branch](https://github.com/ArtUkrainskiy/php-src/tree/strpos-compact-sunday-pr), [patch](change.patch))
against stock PHP [`cf1b5771a76`](https://github.com/php/php-src/commit/cf1b5771a76a81b455a8677446daf9c46e1781be).
Both are PHP 8.7.0-dev builds. These are fresh measurements; no adaptive-PR
percentages are reused.

The shared substring matcher behind `strpos()`, `str_contains()`, `explode()`
and string replacement uses a smaller shift table for 9–31-byte needles when
at least 1024 bytes remain from the current search position. A needle is the
searched substring; its length is measured in bytes, including for UTF-8 text.
The candidate reduces the shift table from 1024 to 256 bytes on these platforms,
keeping the Sunday search algorithm. The inline helper and the wide-table algorithm for longer needles
remain. Dispatch and generated-code placement also change; those costs are included.

## Main observations

AMD Ryzen 9 5950X, one complete PHP operation per reported cost. These are not
request-wide speedups, and no traffic-weighted average is assumed. Negative means
less elapsed time. Moderation searches a list of 12 phrases in generated ordinary
text with no banned phrases present. Rendering replaces order-card placeholders
such as `{{order.id}}`; it does not run a complete template engine.

Each binary/case gets at least three seconds warmup and ten approximately
one-second samples. There is one paired round. Counters come from a separate
five-pass series. Six release compiler builds pass the string tests; full PHP
and extracted C checks also pass with ASan/UBSan. Details and limits follow.

| Operation | GCC 15 elapsed change | Clang 21 elapsed change |
|---|--:|--:|
| Clean moderation posts, nine languages | -10.18% … -4.93% | -11.84% … -5.19% |
| Template rendering, 4 KiB | -15.91% | -14.42% |
| Count template slots, 4 KiB | -16.52% | -15.53% |
| 31-byte early match, corrected fixture | -12.30% | -10.92% |

The quick AMD screen reproduces useful gains without the adaptive engine. Small
changes remain uncertain. A/A compares an identical binary against itself:
GCC is +2.32% before and +1.37% after the main series; Clang is −0.30% before
and +0.24% after. The tables retain noisy rows and use interpretation floors of
2.32% on GCC and 2.00% on Clang. Changes inside the floor are labelled near A/A.
One paired round with ten samples is descriptive; the samples share one process.

Possible losses remain visible. The two 32-byte early controls show +3.86% and
+2.99% elapsed on GCC, versus +0.48% and −1.50% on Clang. These small results are
not a proof that every regression is eliminated; timing and separate cycles also
differ on some controls. The unmodified delimiter/parser paths receive no new
search algorithm, but their measured variation is retained.

Intel wall time is **not usable in this run**: A/A of the identical binary reached
about −50% and +93%. Both interrupted attempts are [preserved](data/excluded-intel.tar.gz).
Intel counters are diagnostic only; no Intel elapsed gain or absence of the old
Clang regressions is claimed. Quiet Intel confirmation remains necessary.

- [All elapsed values, deltas, sizes and quality](time.md).
- [Build and reproduce, or regenerate from archived data](#method-and-reproduction).
- [Absolute cycles and instructions for timed inputs](counters.md).
- [Five-pass counter matrices on six compilers, with A/A](cycles.md).
- [Long-scan profiles](profiles.md), [original profile logs](data/profiles.tar.gz).
- [Unrounded metrics](metrics.json), [raw-record hashes](manifest.json),
  [lossless native series and logs](data/native.tar.gz).

Long-scan cycle gains can occur with less than 0.5% change in retired instructions.
The profiles confirm lower cycles but do not establish a single cause. These
results include table-access code generation and placement effects; they are not
attributed entirely to shift-table initialization or to fewer instructions.

## Inputs and route attribution

The unchanged owned product corpus supplies posts, long threads, delimiters, HTTP
and order-card templates. The [case glossary](../substr-adaptive-search/README.md#reading-the-case-names)
explains the language tags, clean/early/late states and data contents. Exact byte
sizes accompany the elapsed rows. [Suite](suite.php), [corrected early fixture](early31-suite.php).
Moving the suite into this directory changes only its relative `require` path.
The numeric checker restores that path before checking the recorded source hash.

All nine languages have post and thread counter cases. AMD elapsed selects all
nine clean posts, the English/Chinese thread controls, rendering and counting
`{{order.id}}` slots, the two 4 KiB delimiters `||`/`::`, HTTP parsing with a 64 KiB
body, and three routing controls. The original screen has 19 timed inputs per
compiler; the additional true 31-byte early fixture brings it to 20.

A naming mistake in the original screen is retained explicitly: the input named
`boundary/31/early` actually contains a 32-byte needle. It is displayed as
`boundary/32/early-text`, and all original data remain in the archive. Only that
missing 31-byte control was added separately. The corrected fixture computes its
needle using `substr(..., 0, 31)` and checks the byte length. The A/A controls also
used the original 32-byte operand; their identity comparison remains valid.

## Correctness

All six matched release compilers pass 699 string PHPT, with 62 skipped and zero
failures/warnings. The full PHP Clang 21 debug build with ASan/UBSan and
`USE_ZEND_ALLOC=0` passes 680, with 81 skipped and zero failures/warnings. The one
new PHPT checks 300 inputs: byte lengths around 31/32, NUL/high bytes, default
shifts, last-position matches and repeated searches crossing to a short remainder.

The exact candidate and stock matching code are compared with libc `memmem` in
an extracted C verifier. GCC and Clang ASan/UBSan each pass 20,000 seeded random
inputs and 135,460 guarded configurations, including existing inline-path
controls. Two purposeful faults—too-large default shift and omitted last valid
position—are detected. These are shared corpora, not independent input sets.
[Validation data](data/c-validation.json), [verification sources](verify/README.md).
The [captured C drivers and logs](data/c-verification.tar.gz) and
[PHP test logs and sanitizer metadata](data/php-validation.tar.gz) retain the
original validation protocol.

Native ARM, Windows and 32-bit builds have not been run. The production change
adds no architecture-specific guards or instructions. It preserves the Sunday
algorithm's worst-case behavior; pathological-search hardening is a separate topic.

## Method and reproduction

Measured on 31 October 2026 using matched release `docker` profiles. AMD uses GCC
15.2 and Clang 21.1, CPU 15 (SMT sibling 31), performance governor, turbo on. The
core is not exclusively isolated. Intel counter diagnostics use GCC 13/14 and
Clang 18/20, CPU 2, with the observed busy-host/power-state limitations above.
System affinity and power settings were not changed.

Per timed case and binary: one warmup of at least three seconds, followed by ten
approximately one-second batches, ten seconds total target measurement. Calibration,
input preparation and result checking are outside timing; median empty-loop cost
is subtracted. Each pair uses separate PHP processes. The native one-round
significance verdict is intentionally not promoted to a reliable speedup claim.
Cycles and instructions come from a separate five-pass, 50 ms-target series with
alternating A/B and same-row A/A. They are not simultaneous with the elapsed series.

Build stock and compact from the pinned commits with the same compilers and
`bench build` default profile. Do not use an IDE debug build for performance.
For the measured compiler pair, from the **php-src-bench repository root**
([repository setup](../../README.md#quick-start)):

```sh
export PHP_SRC=/path/to/php-src
export BENCH_BUILDS=/path/to/compact-builds
export BENCH_PHP=/path/to/an/existing/php
BENCH_ROOT=$PWD
COMPACT_DATA=$PWD/results/compact-sunday-reproduction
mkdir -p "$COMPACT_DATA"
read -r -p 'Benchmark CPU number: ' COMPACT_CPU
read -r -p 'Orchestrator CPU number: ' COMPACT_ORCHESTRATOR
COMPACT_BASE=cf1b5771a76a81b455a8677446daf9c46e1781be
COMPACT_HEAD=8d7babbc364ffcf28dac9777ce807edc9adbb534
python3 corpus/substr-product/generate.py --owned-only --php-src "$PHP_SRC"
./bench build --slim --cc gcc-15,clang-21 compact-base "$COMPACT_BASE"
./bench build --slim --cc gcc-15,clang-21 compact-head "$COMPACT_HEAD"
export BENCH_PHP="$BENCH_BUILDS/compact-base-gcc15/sapi/cli/php"
python3 reports/compact-sunday/measure.py --bench-root "$PWD" \
  --builds "$BENCH_BUILDS" --out "$COMPACT_DATA/amd" --lane amd \
  --cpu "$COMPACT_CPU" --orchestrator "$COMPACT_ORCHESTRATOR"
```

Choose two appropriate CPU numbers at the prompts. Use an empty output directory.
The two compiler builds require minutes each. The main timing screen targets
about 20 minutes before calibration and counter work. It prints per-case progress.
The source candidate must exist in the php-src repository, either fetched from
the branch or recreated using the linked patch. A recreated commit has a different
ID: update the measurement driver's pinned candidate ID before using it.

The driver’s `amd` lane selects GCC 15/Clang 21 build names and case coverage;
it does not automatically identify a CPU model. Install those compilers to repeat
this exact matrix. Other compiler versions require adapting its build-name list.
The [measurement driver](measure.py) accepts build/output paths and CPU numbers;
the measured build prefixes are `compact-base` and `compact-head`. Its AMD lane
runs the 19-case quick screen. `--counters-only` supports diagnostic-only hosts.
Do not reuse Intel wall measurements while its A/A is invalid.
The separately added 31-byte fixture is [early31-suite.php](early31-suite.php).
Run it after the main screen, with the same builds:

```sh
mkdir -p "$COMPACT_DATA/early31"
export BENCH_RESULTS="$COMPACT_DATA/early31"
for cc in gcc15 clang21; do
  taskset -c "$COMPACT_ORCHESTRATOR" ./bench run \
    reports/compact-sunday/early31-suite.php \
    --a "compact-base-$cc" --b "compact-head-$cc" --cpu "$COMPACT_CPU" \
    --rounds 1 --samples 10 --target-ms 1000 --warmup-ms 3000 --wait-idle 120 \
    > "$COMPACT_DATA/early31/$cc.log" 2>&1
done
taskset -c "$COMPACT_ORCHESTRATOR" ./bench compare \
  reports/compact-sunday/early31-suite.php \
  gcc15=compact-base-gcc15:compact-head-gcc15 \
  clang21=compact-base-clang21:compact-head-clang21 \
  --cpu "$COMPACT_CPU" --passes 5 --target-ms 50 --wait-idle 120 \
  --out "$COMPACT_DATA/early31/cycles.json"
```

This produces the AMD screen plus the corrected early fixture. The separate
Intel counter matrix needs the four corresponding compiler builds and the
`intel --counters-only` lane. It is not evidence for Intel elapsed performance.
Use `bench show` and `bench table` to inspect fresh runs.

To regenerate this exact published document from its archive without measuring,
choose another empty directory. This requires any PHP 8.0+ binary for the tool:


```sh
BENCH_ROOT=$PWD
COMPACT_DATA=$PWD/results/compact-sunday-archived
mkdir -p "$COMPACT_DATA"
tar -xzf reports/compact-sunday/data/native.tar.gz -C "$COMPACT_DATA"
python3 reports/compact-sunday/build-report.py \
  --data "$COMPACT_DATA" --out reports/compact-sunday \
  --bench-root "$BENCH_ROOT" --php "$BENCH_PHP"
python3 reports/compact-sunday/check.py
./bench report check reports/compact-sunday
```

Machine paths in display-only counter metadata are normalized; raw native JSON
and logs remain unchanged in the archive. Both the source revisions and all
input/output hashes are checked. The source branch is a candidate for a small PR;
these quick measurements do not substitute for upstream CI or quiet Intel timing.

## Previous adaptive experiment

The previous adaptive corpus was not literally all below 32 bytes: seven unique
Russian/Hindi phrases are 36–55 bytes. Capturing the actual operands across its
233 cases found 42 long searches in 12 cases. Instrumenting the original 8c6759
matcher confirmed 14 Sunday-adaptive entries, but **zero pair, gram4 or Two-Way
entries**. Thus it did not demonstrate ordinary-product gains from those advanced
stages. [Route summary](data/corpus-route-summary.json),
[captured operands and route log](data/corpus-audit.tar.gz), [capture source](verify/corpus-audit.php).

