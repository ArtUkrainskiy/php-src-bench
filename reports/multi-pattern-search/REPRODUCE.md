# Reproduce the literal search and replacement measurements

Use a separate checkout to preserve the published capture: the final import step
replaces this report’s captured data with your measurements.

Use Linux with Python 3.11 or newer, Bash, Git, GCC 15.2, Clang 21.1, `taskset`, `perf`, and
normal php-src build prerequisites (autoconf, bison, re2c, make, pkg-config).
The measured Clang patch version was 21.1.8. Other compiler/CPU versions produce
new experiments, not identical binary hashes. No package installation or kernel
setting changes are performed by the driver.

Start in this report directory. These commands create fresh ignored source/build
locations. The public repository's `bench build` generates `.bench-build.json`;
a plain external PHP build without that metadata is not accepted by the driver.
The `docker` profile selects the release flags described above and configures
`--disable-all --disable-cgi --disable-phpdbg --enable-cli --enable-werror`.
Do not use `--slim`: the standalone extension needs the build headers.

```sh
set -euo pipefail
mkdir -p .local
export PHP_SRC="$PWD/.local/php-src"
export BENCH_BUILDS="$PWD/.local/builds"
GCC=gcc-15
CLANG=clang-21
git clone --filter=blob:none --no-checkout https://github.com/ArtUkrainskiy/php-src.git "$PHP_SRC"
../../bench build --profile docker --cc "$GCC,$CLANG" runtime 758c9ac5492848a54f9fd88fac2a54d5e6108c05
mkdir -p .local/extension
git -C "$PHP_SRC" archive 287aaab7fb729d3a8e91c6fd35224c4359c343e3 ext/strmatch | tar -x -C .local/extension
export STRMATCH_SOURCE="$PWD/.local/extension/ext/strmatch"
export STRMATCH_REVISION=287aaab7fb729d3a8e91c6fd35224c4359c343e3
```

The clone/build can take several minutes, depending on the machine. Successful
builds print `ok:` and leave full trees at `$BENCH_BUILDS/runtime-gcc15` and
`$BENCH_BUILDS/runtime-clang21`. Each has `sapi/cli/php`, headers and its actual
`.bench-build.json`. Adjust the two compiler executable names above if your
installation uses different names for the same versions.

Choose an idle logical CPU and keep its SMT sibling idle. The driver requires
readable `topology/thread_siblings_list` and `cpufreq/scaling_governor` below that
CPU's sysfs directory. Even smoke tests need working user-space hardware counters.
The preflight must exit successfully and print supported counts for all events.

```sh
read -r -p 'Idle logical CPU number: ' BENCH_CPU
export BENCH_CPU
SIBLINGS_FILE="/sys/devices/system/cpu/cpu$BENCH_CPU/topology/thread_siblings_list"
cat "$SIBLINGS_FILE"
# The frozen main driver accepts comma-separated single CPU IDs only.
if grep -q -- '-' "$SIBLINGS_FILE"; then
  echo 'This driver requires sibling IDs without ranges; choose a supported CPU/machine.' >&2
  exit 1
fi
test -r "/sys/devices/system/cpu/cpu$BENCH_CPU/cpufreq/scaling_governor"
perf stat -e cycles:u,instructions:u,context-switches,cpu-migrations -- taskset -c "$BENCH_CPU" true
python3 render.py --check
python3 ../../corpus/multi-pattern-product/generate.py --check
python3 ../../corpus/multi-pattern-scaling/generate.py --check
export RUN_ROOT="$(mktemp -d "$PWD/.local/run.XXXXXX")"
```

Run compilers and corpora sequentially. Smoke is a small timed check and must end
with `MUTATION CAUGHT` and `SMOKE PASS`. The full run verifies every case before
timing; progress and failures go to its log. Each full command must end with
`COMPLETE` (92 rows for product, 158 for size). Here full runs took about 11 and
16 minutes per compiler respectively; durations are machine-dependent.

```sh
for specification in "gcc15:$GCC" "clang21:$CLANG"; do
  tag="${specification%%:*}"
  cc="${specification#*:}"
  export PHP_BUILD="$BENCH_BUILDS/runtime-$tag"
  export SMOKE_OUTPUT="$RUN_ROOT/smoke-$tag"
  python3 measure.py smoke --php-build "$PHP_BUILD" --source "$STRMATCH_SOURCE" \
    --source-revision "$STRMATCH_REVISION" --cc "$cc" --cpu "$BENCH_CPU" \
    --filter moderation.en.clean --output "$SMOKE_OUTPUT"
  "$PHP_BUILD/sapi/cli/php" -n -d "extension=$SMOKE_OUTPUT/strmatch.so" \
    ../../corpus/multi-pattern-product/verify.php
  "$PHP_BUILD/sapi/cli/php" -n -d "extension=$SMOKE_OUTPUT/strmatch.so" \
    ../../corpus/multi-pattern-product/verify.php --corpus ../../corpus/multi-pattern-scaling
  for corpus in product size; do
    if [ "$corpus" = product ]; then
      CORPUS_DIR=../../corpus/multi-pattern-product
    else
      CORPUS_DIR=../../corpus/multi-pattern-scaling
    fi
    python3 measure.py run --php-build "$PHP_BUILD" --source "$STRMATCH_SOURCE" \
      --source-revision "$STRMATCH_REVISION" --cc "$cc" --cpu "$BENCH_CPU" \
      --corpus "$CORPUS_DIR" --output "$RUN_ROOT/data-$corpus-$tag" \
      > "$RUN_ROOT/$corpus-$tag.log" 2>&1
  done
done
```

An interrupted or failed series is not a complete result. Keep its logs and start
that series in a new directory. Output directories containing `results.json` are
rejected before compiling or replacing their module. To repeat all four runs,
create another `RUN_ROOT`; to clean a completed local reproduction, remove only
that chosen run directory. No scripts remove other builds or results.

To generate tables from your new measurements, all four output directories above
must be complete. The following replaces this report's captured data with your
new series; use a separate checkout if you want to preserve the published capture.

```sh
python3 capture.py "$RUN_ROOT"
# Continue with additional measurements below before rendering the final report.
```

Import must print `CAPTURE PASS 4 complete series`, then rendering must pass.
The importer checks hashes, exact rows, output aggregates and every corrected
counter against raw N/zero outputs. Public JSON contains the raw elapsed samples;
the audit records the original raw-output comparisons. Binaries and the complete
per-process run directories are not bundled with the report.

## Additional measurements

Keep the same `RUN_ROOT`, source, CPU and builds. Choose the SMT sibling shown
by `thread_siblings_list` (excluding the selected CPU). The driver checks sibling
activity and stops if it exceeds 5%. Set the paths explicitly; no machine-specific
build names are required.

```sh
export PHP_BUILD_GCC15="$BENCH_BUILDS/runtime-gcc15"
export PHP_BUILD_CLANG21="$BENCH_BUILDS/runtime-clang21"
read -r -p 'SMT sibling logical CPU number: ' BENCH_SIBLING
export BENCH_SIBLING
python3 supplements/prepare.py
python3 supplements/measure.py --validate
python3 supplements/measure.py > "$RUN_ROOT/supplements.log" 2>&1
```

Preparation takes seconds and must print
`BATCH N1/N2, MUTATION, CONSTRUCTION N1 PASS`. It copies four immutable PHP helpers
into the fresh run and refuses to overwrite them. The main four series must all
be complete. The supplemental driver takes roughly 20 minutes here, depending
on the CPU. It runs sequential order confirmations, memory, constructors, estimates
and direct batches for both compilers. Success prints `SUPPLEMENTS COMPLETE`;
`post-status.json` gives current progress. A failure writes `failure-post.json`.
Do not accept partial files. Preserve a failed run and repeat in a new directory;
main results may be copied unchanged into it before `prepare.py`.

```sh
python3 supplements/capture.py "$RUN_ROOT"
python3 render.py
python3 render.py --check
```

Expect `SUPPLEMENT CAPTURE PASS ... raw outputs verified` and successful rendering
checks for operation, memory, preparation, payback and confirmation tables.
The raw-output count can differ on another machine because the adaptive batch
point selection can choose different points. The importer currently expects the
published case matrix and exactly the configured 15 passes, not reduced smoke data.

The supplemental PHP helpers match recorded hashes. The portable Python controller
adapts environment/path configuration and omits the original asynchronous wait;
it is not claimed to have the original private controller's hash. Main and
supplemental importers verify raw outputs before exporting path placeholders.
For memory-only repetition, use the separate commands in [Memory](MEMORY.md)
instead of running the supplemental memory series twice.

The optional figure uses Matplotlib in a separate plotting environment:

```sh
python3 -m venv "$RUN_ROOT/plot-venv"
"$RUN_ROOT/plot-venv/bin/pip" install matplotlib==3.11.2
"$RUN_ROOT/plot-venv/bin/python" memory/plot.py
```

Plotting is not a measurement dependency. The published SVG was regenerated from
the same measured bytes. No build, process or kernel configuration is removed by
these commands; remove only your chosen `.local` run/build directories when done.


## Fixed-length and pure-construction series

The short README tables use this additional series. Keep the PHP builds, source revision and CPU selected above. Work from this report directory; the following can repeat only the new summary while leaving the other published captures intact. New runs take roughly 10–15 minutes here, excluding builds.

```sh
set -euo pipefail
python3 ../../corpus/multi-pattern-length/generate.py --check
export LENGTH_RUN_ROOT="$(mktemp -d "$PWD/.local/length.XXXXXX")"
read -r -p 'SMT sibling logical CPU number: ' BENCH_SIBLING
export BENCH_SIBLING
for specification in "gcc15:$GCC" "clang21:$CLANG"; do
  tag="${specification%%:*}"
  cc="${specification#*:}"
  python3 length/measure.py smoke --php-build "$BENCH_BUILDS/runtime-$tag" \
    --source "$STRMATCH_SOURCE" --source-revision "$STRMATCH_REVISION" \
    --cc "$cc" --cpu "$BENCH_CPU" --filter length.any.absent.128 \
    --passes 1 --sample .01 --warmup .001 --output "$LENGTH_RUN_ROOT/smoke-$tag"
done
python3 length/additional.py smoke --run-root "$LENGTH_RUN_ROOT" \
  --gcc-build "$BENCH_BUILDS/runtime-gcc15" --cpu "$BENCH_CPU" --sibling "$BENCH_SIBLING"
```

Each main smoke must print `MUTATION CAUGHT` and `SMOKE PASS`. The additional smoke must print `ADDITIONAL SMOKE N1/N2, THREE RESULT MUTATIONS AND BATCH MUTATION PASS`. It checks constructor memory/time intervals, corrupted bool/list/string results and batched calls. All helpers are hashed before the full supplementary run. Use a fresh directory after a failed smoke; existing raw output is refused.

```sh
for specification in "gcc15:$GCC" "clang21:$CLANG"; do
  tag="${specification%%:*}"
  cc="${specification#*:}"
  python3 length/measure.py run --php-build "$BENCH_BUILDS/runtime-$tag" \
    --source "$STRMATCH_SOURCE" --source-revision "$STRMATCH_REVISION" \
    --cc "$cc" --cpu "$BENCH_CPU" --output "$LENGTH_RUN_ROOT/data-length-$tag" \
    > "$LENGTH_RUN_ROOT/length-$tag.log" 2>&1
done
python3 length/additional.py run --run-root "$LENGTH_RUN_ROOT" \
  --gcc-build "$BENCH_BUILDS/runtime-gcc15" --clang-build "$BENCH_BUILDS/runtime-clang21" \
  --cpu "$BENCH_CPU" --sibling "$BENCH_SIBLING" > "$LENGTH_RUN_ROOT/additional.log" 2>&1
python3 length/capture.py "$LENGTH_RUN_ROOT"
python3 render.py
python3 render.py --check
```

Main logs must end with `COMPLETE 24 rows`; the supplemental log with `ADDITIONAL COMPLETE`. The importer accepts only complete records and the supplementary completion marker. It verifies raw stdout, repeated-call aggregates, exact inputs and binary/harness identity, and recalculates counters from raw N/zero records. Expect `LENGTH CAPTURE PASS 720 corrected counters` and successful render checks. Direct batch counts can differ on another machine because model-selected points change.

The importer updates `data/length-*`, `data/build-cost-*` and `data/additional-aa-*`; rendering updates the README, LENGTH, BUILD-MEMORY and LENGTH-PAYBACK tables. The original application and dictionary-size measurements retain their own binary hashes and scopes. Full fresh repetitions of those older tables require the earlier commands too. Raw results and configuration files stay in your chosen LENGTH_RUN_ROOT. No command removes them.

## Fixed 4 KiB matrix

This separate series measures the same saved 4 KiB strings against 8–512-key dictionaries and the four match-position states. It leaves earlier captures unchanged. Use the same source revision and release builds selected above; no php-src rebuild is needed. Expect roughly 6–10 minutes on the recorded machine, excluding builds.

From this report directory:

```sh
set -euo pipefail
python3 ../../corpus/multi-pattern-4k/generate.py --check
export GRID_RUN_ROOT="$(mktemp -d "$PWD/.local/grid.XXXXXX")"
for mode in smoke run; do
  python3 length/grid.py "$mode" --run-root "$GRID_RUN_ROOT" \
    --gcc-build "$BENCH_BUILDS/runtime-gcc15" \
    --clang-build "$BENCH_BUILDS/runtime-clang21" \
    --gcc "$GCC" --clang "$CLANG" --source "$STRMATCH_SOURCE" \
    --cpu "$BENCH_CPU" --sibling "$BENCH_SIBLING" \
    > "$GRID_RUN_ROOT/$mode.log" 2>&1
done
python3 length/grid_capture.py "$GRID_RUN_ROOT"
python3 render.py
python3 render.py --check
```

Smoke checks N=1/N=2 batches, compares outputs with the saved independent oracles, and catches deliberately corrupted boolean/string results. It must finish with `GRID SMOKE COMPLETE`. The full coordinator must finish with `GRID RUN COMPLETE`, with `GRID_COMPLETE` containing `PASS`. Each `run-<compiler>.log` must finish with `COMPLETE 18 rows`. Progress is in `status.json` and the logs; failures create `failure.json`. Never accept a partial run. Preserve failed directories and repeat using a fresh GRID_RUN_ROOT.

The main series uses the frozen `length/measure.py` and `length/harness.php`, with the new corpus passed explicitly. Direct one-shot times use the same frozen batch recipe as the input-length series. Each compiler gets prepared A/A controls before/after the main series and one-shot Matcher/Replacer A/A controls before/after the batches; full A/A paired medians must stay within 2%. The driver stops on an SMT sibling busy above 5%.

The importer must print `GRID CAPTURE PASS 540 corrected counters; 80 one-shot raw outputs`. It checks exact ordered input dictionaries and texts, stdout, consumption aggregates, protocol, helper/binary identity and raw N-minus-zero perf corrections. It writes `data/grid-*`; rendering updates the README position/size blocks and FIXED-4K.md. All 15 samples and five corrected counter passes are retained in the exported JSON; raw configs/stdout/perf files remain in GRID_RUN_ROOT. Nothing is deleted by these commands.
