# Reproduce the literal search and replacement measurements

Use a separate checkout to preserve the published capture: the final import step
replaces this report’s captured data with your measurements.

Use Linux with Python 3, Bash, Git, GCC 15.2, Clang 21.1, `taskset`, `perf`, and
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
git -C "$PHP_SRC" archive 5025a32fdfb7c7c4c383fa33165d0ea3e91452a8 ext/strmatch | tar -x -C .local/extension
export STRMATCH_SOURCE="$PWD/.local/extension/ext/strmatch"
export STRMATCH_REVISION=5025a32fdfb7c7c4c383fa33165d0ea3e91452a8
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
cat "/sys/devices/system/cpu/cpu$BENCH_CPU/topology/thread_siblings_list"
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
python3 render.py
python3 render.py --check
```

Import must print `CAPTURE PASS 4 complete series`, then rendering must pass.
The importer checks hashes, exact rows, output aggregates and every corrected
counter against raw N/zero outputs. Public JSON contains the raw elapsed samples;
the audit records the original raw-output comparisons. Binaries and the complete
per-process run directories are not bundled with the report.

The [recorded measurement driver](data/measured-driver.py) preserves the exact
source hash used for the published series. The current driver moves only the
existing-output guard ahead of compilation, preventing accidental overwrites.
Timed PHP recipes, arguments and sampling protocol are unchanged. The importer
recognizes both recorded and current hashes; the published observations remain
byte-for-byte unchanged. Table generation and artifact import are not timed.
