# Reproduce the measurements

[Report](README.md). Commands below run from the **php-src-bench repository root**.
They build release CLIs and measure PHP operations using frozen corpus inputs,
without running the corpus generator. No container is required. The `docker` profile refers to compiler flags.

## Choose a route

To inspect or regenerate saved numbers, no compiler, CPU selection or perf
access is needed. From an existing php-src-bench checkout, run:

```sh
python3 reports/compact-sunday/tools/render.py
./bench report update reports/compact-sunday/tables
python3 reports/compact-sunday/tools/render.py --check
./bench report check reports/compact-sunday
```

Expect completion in seconds and unchanged tables. Python 3.9+ and PHP 8.0+
are required. To conduct a new experiment, follow the stages below: prerequisites,
matching core builds, validation, tiny smoke, full core measurement, then optional
shared-module builds and extension measurements. Keep the new results separate
from the captured data in this report.

## Prerequisites and local settings

Use Linux x86-64 with hardware `perf stat` access, Python 3.9+, PHP 8.0+ to run the
orchestrator, Git, rsync, and the normal php-src build dependencies, including
bison/re2c/autoconf. Extension measurements also require ICU and Oniguruma
headers/libraries and complete C++ toolchains. Every selected Clang must be able
to locate working C++ standard-library headers. Package versions of the captures
are recorded in [metadata](data/metadata.json); other toolchains produce a new
experiment, not byte-identical binaries.

Use Bash with failure handling. Starting from an empty parent directory:

```sh
set -euo pipefail
git clone https://github.com/ArtUkrainskiy/php-src-bench.git
git clone https://github.com/ArtUkrainskiy/php-src.git
cd php-src-bench
```

Put all machine choices in one local file, for example
`results/compact-sunday.env`, and source it before the remaining steps:

```sh
export PHP_SRC="$(cd ../php-src && pwd)"
export BENCH_BUILDS="$(pwd)/../php-builds"
export CPU=                       # choose an idle physical core using bench doctor
export CC_LIST=gcc,gcc-14,clang,clang-20
export BUILD_SUFFIXES=gcc13,gcc14,clang18,clang20
export FIRST_SUFFIX=gcc13
export BUILD_JOBS=8               # module builds only; core bench build uses nproc
export MODULE_ROOT="$(pwd)/results/compact-sunday-modules"
export EXT_RUNNER="$(pwd)/results/compact-sunday-extension-runner"
```

Adapt compiler commands and suffixes to the available versions. On the AMD
capture the commands were `gcc,clang` and suffixes `gcc15,clang21`.
Do not use a busy SMT sibling. No OS isolation or governor change is required
by these commands. Empty `CPU` is intentional; select it for the current machine.

```sh
. results/compact-sunday.env
./bench doctor
: "${CPU:?Set CPU in results/compact-sunday.env}"
python3 reports/compact-sunday/tools/check.py
```

Doctor and structural validation should finish in seconds. Validation prints
205 cases across 20 suites, with no timings. A missing dependency or hash
mismatch must be resolved before continuing.

## Build and verify core binaries

Read the exact measured base and the matching candidate tree from metadata:

```sh
MASTER_REF=$(python3 -c 'import json; print(json.load(open("reports/compact-sunday/data/metadata.json"))["measured_tree"]["master"])')
CANDIDATE_REF=$(python3 -c 'import json; print(json.load(open("reports/compact-sunday/data/metadata.json"))["measured_tree"]["branch_candidate"])')
git -C "$PHP_SRC" fetch origin strpos-compact-sunday-pr
./bench build --slim --cc "$CC_LIST" master "$MASTER_REF"
./bench build --slim --cc "$CC_LIST" compact "$CANDIDATE_REF"
export BENCH_PHP="$BENCH_BUILDS/master-$FIRST_SUFFIX/sapi/cli/php"
```

The build command prints the actual registered names. Check them with
`./bench builds`, then adjust `BUILD_SUFFIXES` if needed. Expect minutes per
compiler, potentially longer on another machine. Both sides must be release,
non-ZTS builds with matching options; inspect their `.bench-build.json` files.
Captured binary hashes identify the original executables; newly built binaries
on another machine are not expected to have those hashes.

```sh
for suffix in $(printf '%s' "$BUILD_SUFFIXES" | tr ',' ' '); do
  for side in master compact; do
    "$BENCH_BUILDS/$side-$suffix/sapi/cli/php" -n \
      reports/compact-sunday/tools/validate.php reports/compact-sunday/corpus core
  done
done
```

Expected: `checked 163 core cases; all outputs match independent expectations`
for each binary. This includes the four untimed alias checks. Runtime validation
takes seconds and fails at the first wrong output or unavailable required API.

## Small smoke, then full core run

```sh
python3 reports/compact-sunday/tools/measure.py \
  --out results/compact-sunday-smoke --cpu "$CPU" --compilers "$FIRST_SUFFIX" --smoke
```

Smoke uses one case per compiler with one tiny elapsed pair and one native
counter pass; it should finish in seconds if the core is idle. It is only a
runner check, not performance evidence. Inspect its logs and `complete` marker.

```sh
python3 reports/compact-sunday/tools/measure.py \
  --out results/compact-sunday-core --cpu "$CPU" --compilers "$BUILD_SUFFIXES"
```

The driver measures **one case per process**, not a whole suite in one process.
It runs 159 core/control cases per compiler, A/A brackets, then native per-suite
counter series. All cases get five paired rounds with 500 ms warmup and five
~200 ms samples per side/process; counter passes target 50 ms. It prints every
job and retains native JSON and logs in the selected output directory.
The four-compiler core elapsed cohort took about 4.3 hours in this capture;
counters, builds, replications and idle waits add time.

## Shared extensions without relocating the core executable

The captures loaded matching shared mbstring/intl modules into the original
CLI binaries; the core executables were not rebuilt with static extensions.
Static extension builds can change code layout and are a different experiment.
Build module-only worktrees from the same base. Complete C++ development
packages for each compiler are required; no package is installed by these steps.

```sh
mkdir -p "$MODULE_ROOT"
for suffix in $(printf '%s' "$BUILD_SUFFIXES" | tr ',' ' '); do
  cc=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["cc_command"])' \
    "$BENCH_BUILDS/master-$suffix/.bench-build.json")
  case "$cc" in
    *gcc*) cxx=$(printf '%s' "$cc" | sed 's/gcc/g++/') ;;
    *clang*) cxx=$(printf '%s' "$cc" | sed 's/clang/clang++/') ;;
    *) exit 1 ;;
  esac
  module_dir="$MODULE_ROOT/$suffix"
  git -C "$PHP_SRC" worktree add --detach "$module_dir" "$MASTER_REF"
  (
    cd "$module_dir"
    ./buildconf --force
    flags='-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64'
    CC="$cc" CXX="$cxx" CFLAGS="$flags" CXXFLAGS="$flags" LDFLAGS='-Wl,-O1' \
      ./configure --disable-all --disable-cgi --disable-phpdbg --enable-cli \
      --enable-werror --enable-mbstring=shared --enable-intl=shared
    make -j "$BUILD_JOBS" build-modules
  )
done
```

Expect several minutes per compiler and two `.so` files in each worktree's
`modules` directory. The original Intel Clang module builds explicitly selected
the GCC 13 C++ header directory; exact module flags are in metadata. If Clang
cannot find standard headers, fix its toolchain selection before measurement.
Do not change the core CFLAGS to compensate. Build on other cores or finish
all compilation before timing.

Prepare a mapping and a **private** extension-enabled orchestration copy:

```sh
python3 - <<'PY'
import json, os
from pathlib import Path
mapping = {}
for suffix in os.environ['BUILD_SUFFIXES'].split(','):
    module_dir = str((Path(os.environ['MODULE_ROOT']) / suffix / 'modules').resolve())
    for side in ['master', 'compact']:
        binary = Path(os.environ['BENCH_BUILDS']) / (side + '-' + suffix) / 'sapi/cli/php'
        mapping[str(binary.resolve())] = module_dir
Path('results/compact-sunday-modules-map.json').write_text(json.dumps(mapping, indent=2) + '\n')
PY
python3 reports/compact-sunday/tools/extension-runner.py \
  --bench-root . --out "$EXT_RUNNER" --map results/compact-sunday-modules-map.json
for suffix in $(printf '%s' "$BUILD_SUFFIXES" | tr ',' ' '); do
  for side in master compact; do
    "$BENCH_BUILDS/$side-$suffix/sapi/cli/php" -n \
      -d "extension_dir=$MODULE_ROOT/$suffix/modules" \
      -d extension=mbstring.so -d extension=intl.so \
      reports/compact-sunday/tools/validate.php reports/compact-sunday/corpus all
  done
done
```

Expected: 205 successful cases per binary. The startup adapter changes only the
private runner's command line; it does not alter `lib/harness.php` or measured
binaries. Use this runner only for extension suites.

```sh
python3 reports/compact-sunday/tools/measure.py --family extensions \
  --out results/compact-sunday-extension-smoke --cpu "$CPU" \
  --compilers "$FIRST_SUFFIX" --bench "$EXT_RUNNER/bench" --smoke
python3 reports/compact-sunday/tools/measure.py --family extensions \
  --out results/compact-sunday-extensions --cpu "$CPU" \
  --compilers "$BUILD_SUFFIXES" --bench "$EXT_RUNNER/bench"
```

The extension elapsed cohort took about 1.2 hours for four compilers, plus
counters and waits. Streams in these suites are memory streams, not external I/O.

## Additional two-argument diagnostic

The separate [prefix-default-offset suite](suites/prefix-default-offset.php)
contains the exact 4096-byte input and 64-byte needle used in the two additional
AMD comparisons. It is outside the 205-case frozen corpus; its hash is in
metadata. Run it separately with the core runner:

```sh
./bench run reports/compact-sunday/suites/prefix-default-offset.php \
  --a "master-$FIRST_SUFFIX" --b "compact-$FIRST_SUFFIX" --cpu "$CPU" \
  --rounds 5 --samples 5 --target-ms 200 --warmup-ms 500 --wait-idle 120
```

## Inspect, repeat and regenerate

A failed command stops the series and retains its artifacts. Output mismatches
must be investigated before looking at speed. A run with an expired idle wait
is retained but not accepted as quiet. Do not delete an inconvenient observation
or rerun only the slower side. Inspect the log and repeat the entire paired case
in a fresh output directory. The captured replication rule was process spread
>10%, sample MAD >5%, A/A median outside ±2%, or product median regression >3%.
For a flagged case, use `bench run` with the same five-pair settings and exact
`--filter` in a new `BENCH_RESULTS` directory; keep both cohorts and their dates.

Reinvoking `measure.py` with the same plan resumes fully saved jobs. A failed
job whose raw record was retained requires inspection; the tool refuses to
silently overwrite it. Use a fresh directory for a new series. It never builds
or switches the user's source checkout.

Regenerate the **published captured tables**, without running a benchmark:

```sh
python3 reports/compact-sunday/tools/render.py
./bench report update reports/compact-sunday/tables
python3 reports/compact-sunday/tools/render.py --check
./bench report check reports/compact-sunday
./bench table reports/compact-sunday/data/counters/amd-search.json --full --compact-header
```

These commands should finish in seconds and leave the checked-in tables
unchanged. For a new experiment, retain its output separately; the captured
JSON here should not be replaced with unrelated machine or source versions.
`tools/export.py --help` lists the original capture layout used for the exported
observations. The portable `measure.py` writes a different layout; retain its
results as a new experiment rather than importing them into these captures.

For cleanup, retain the JSON/log output first, remove only the private runner
you created, and use `git worktree remove` on the module worktrees listed by
`git -C "$PHP_SRC" worktree list`. Use `bench gc` after reviewing its build list.
No cleanup command is run automatically.
