# Reproduce the compact-Sunday measurements

Measured on 31 October 2026 using matched release `docker` profiles. AMD uses GCC
15.2 and Clang 21.1, CPU 15 (SMT sibling 31), performance governor, turbo on. The
core was not reserved for the benchmark. Intel counter diagnostics use GCC 13/14 and
Clang 18/20, CPU 2, with [invalid elapsed A/A controls](README.md#results).
Benchmark processes were pinned to the recorded CPUs. Governor, turbo and system
core-isolation settings were not modified for these runs.

Report elapsed tables use microseconds per complete PHP operation. Native
elapsed JSON and `bench run` output use nanoseconds per operation.

Per timed case and binary: one warmup of at least three seconds, followed by ten
approximately one-second batches, ten seconds total target measurement. Calibration,
input preparation and result checking are outside timing; median empty-loop cost
is subtracted. Each case and build uses one PHP process for all ten samples.
Cycles and instructions come from a separate five-pass, 50 ms-target series with
alternating A/B and same-row A/A. They are not simultaneous with the elapsed series.

Build master and compact from the pinned commits with the same compilers and
`bench build` default profile. Do not use an IDE debug build for performance.
The main driver measures 19 inputs; the displayed 31-byte row requires the
second command block below. For the measured compiler pair, start from the **php-src-bench repository root**
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
Four release binaries are built: master and compact with each compiler.
Each build takes minutes. The main timing run targets
about 20 minutes before calibration and counter work. It prints per-case progress.
The source candidate must exist in the php-src repository, either fetched from
the branch or recreated using the linked patch. A recreated commit has a different
ID: update the measurement driver's pinned candidate ID before using it.

The driver’s `amd` lane selects GCC 15/Clang 21 build names and case coverage;
it does not automatically identify a CPU model. Install those compilers to repeat
this exact matrix. Other compiler versions require adapting its build-name list.
The [measurement driver](measure.py) accepts build/output paths and CPU numbers;
the measured build prefixes are `compact-base` and `compact-head`. Its AMD lane
runs the 19-case timing set. `--counters-only` supports diagnostic-only hosts.
Do not reuse Intel wall measurements while its A/A is invalid.
The 31-byte control is [early31-suite.php](early31-suite.php).
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

This produces the AMD timing set plus the 31-byte control. The separate
Intel counter matrix needs the four corresponding compiler builds and the
`--lane intel --counters-only` options. It is not evidence for Intel elapsed performance.
Use `bench show` and `bench table` to inspect fresh runs.

To regenerate this exact published document from its archive without measuring,
choose another empty directory. This requires any PHP 8.0+ binary for the tool:


```sh
BENCH_ROOT=$PWD
COMPACT_DATA=$PWD/results/compact-sunday-archived
mkdir -p "$COMPACT_DATA"
tar -xzf reports/compact-sunday/data/native.tar.gz -C "$COMPACT_DATA"
COMPACT_SEARCH=$PWD/results/compact-sunday-search-archived
mkdir -p "$COMPACT_SEARCH"
tar -xzf reports/compact-sunday/data/search-controls.tar.gz -C "$COMPACT_SEARCH"
python3 "$COMPACT_SEARCH/summarize.py" \
  --data "$COMPACT_SEARCH" --out reports/compact-sunday
python3 reports/compact-sunday/build-report.py \
  --data "$COMPACT_DATA" --out reports/compact-sunday \
  --bench-root "$BENCH_ROOT" --php "$BENCH_PHP"
python3 reports/compact-sunday/check.py
./bench report check reports/compact-sunday
```

Machine paths in display-only counter metadata are normalized; raw native JSON
and logs remain unchanged in the archive. Both the source revisions and all
input/output hashes are checked. The source branch is a candidate for a small PR;
these preliminary measurements do not substitute for upstream CI or quiet Intel timing.


## Repeat a search-shape control

The additional matrix is independent of the product cases. Use the matched
master/compact builds and environment above. From the repository root, this
repeats the constructed 64-byte absent search and its same-input A/A on GCC 15:

```sh
export BENCH_RESULTS="$COMPACT_DATA/search-runs"
for COMPACT_OTHER in compact-head-gcc15 compact-base-gcc15; do
  taskset -c "$COMPACT_ORCHESTRATOR" ./bench run \
    reports/compact-sunday/search-suite.php \
    --a compact-base-gcc15 --b "$COMPACT_OTHER" --cpu "$COMPACT_CPU" \
    --filter '^strpos/prefix/64 @ prefix-4096$' \
    --rounds 1 --samples 10 --target-ms 1000 --warmup-ms 3000 --wait-idle 120
done
```

Each paired run targets at least 26 seconds plus calibration and idle checks.
The first compares the two versions; the second compares the identical master
binary. Expected output is `false` in both versions. `bench run` writes native
JSON to the selected results directory. Replace the case filter to test another
row. The [suite](search-suite.php) and [case definitions](search-cases.json)
contain the exact inputs, byte lengths and expected results.

The full additional counter matrix can be repeated separately:

```sh
./bench compare reports/compact-sunday/search-suite.php \
  clang21=compact-base-clang21:compact-head-clang21 \
  gcc15=compact-base-gcc15:compact-head-gcc15 \
  --cpu "$COMPACT_CPU" --passes 5 --target-ms 50 --wait-idle 120 \
  --out "$COMPACT_DATA/search-cycles.json"
```

It has 58 cases and 2320 count records, including Clang identical-binary
controls. This can take several minutes beyond the measurement targets.
The scripts captured in the search-controls archive record the exact ordering
of the published elapsed batches and the later targeted 64-byte check.
