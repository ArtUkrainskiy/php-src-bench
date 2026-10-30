# Reproducing the final substring-search report

Run these commands from the benchmark repository root. A PHP 8.0+ CLI, Python 3,
GCC/Clang, Linux perf access and the existing benchmark build prerequisites are required.
Set `BENCH_PHP` if the default PHP is unavailable. Regenerating documents does not run
benchmarks or require the original machine's directories.

## Regenerate and check the published tables

```sh
d=reports/substr-adaptive-search
python3 "$d/scripts/build_report.py"
python3 "$d/scripts/build_report.py" --check
python3 "$d/scripts/audit.py"
./bench report check "$d"
```

The generator reads the published raw JSON, uses the native `result_rows()` statistics
for elapsed time, and invokes `bench table --full` for the compiler cycle matrices.
It verifies matched release builds, input/output equality, completed series and the
binary fingerprints connecting the cycle and elapsed series. It writes the English report and shared tables. The public report has no dependency on internal drafts or archived experiments.

`data/report-manifest.json` records SHA-256 of every source series read by this
generator. `data/metrics.tsv` contains all selected rows, absolute elapsed costs,
absolute cycles where measured, absolute instruction counts, all deltas, spread,
source filenames and sample windows. The raw initial runs are retained alongside all
repeats. No measurement is overwritten by the table generator.

The [layout](LAYOUT.md) lists the role and provenance of every active directory. Earlier exploratory exporters and unpublished variants are outside this report.

## Build the measured source trees

Use separate build directories; the user's working checkout does not need a branch
switch. Replace compiler commands with the exact installed versions shown in the raw
build metadata. Each compiler must have its own matched base/candidate pair.

```sh
./bench doctor
BASE=ef99f4248f1450c39fb86fd7fd6f24c49b8d11eb
# PHP_SRC: a php-src repository containing BASE and the pinned corpus source commit.
# CANDIDATE_TREE: a new path for the candidate worktree.
git -C "$PHP_SRC" worktree add --detach "$CANDIDATE_TREE" "$BASE"
git -C "$CANDIDATE_TREE" apply "$PWD/reports/substr-adaptive-search/change.patch"
git -C "$CANDIDATE_TREE" add Zend/zend_operators.c ext/standard/tests/strings/str_search_*.phpt
git -C "$CANDIDATE_TREE" -c user.name='Benchmark reproduction' \
    -c user.email='benchmark@example.invalid' commit -m 'Apply frozen substring-search candidate'
CANDIDATE_COMMIT=$(git -C "$CANDIDATE_TREE" rev-parse HEAD)

./bench build --profile docker --cc gcc-15,clang-21 base "$BASE"
./bench build --profile docker --cc gcc-15,clang-21 product-guard "$CANDIDATE_COMMIT"
```

The new commit hash can differ from the original candidate due to author/date metadata;
the included patch reproduces the source change. The series in this report names the
original real commit `ca89fb5fb96399ed730cacb12d948025f83c4e6e`. The driver checks those
recorded commit hashes by default. When rebuilding from the patch, pass
`--candidate-commit "$CANDIDATE_COMMIT"` and retain its recorded source fingerprints.
This does not change the measured case expressions or timing.

On the Intel machine use `gcc-13,gcc-14,clang-18,clang-20` instead. Do not add alignment
flags: aligned builds in the historical files are diagnostics, not the final result.

## Generate and verify the corpus

```sh
python3 corpus/substr-product/generate.py --php-src "$PHP_SRC" --owned-only
"$BENCH_PHP" -n corpus/substr-product/verify.php
```

The owned fixtures are deterministic. C-source inputs are pinned to
`9d94059ce881d010d91c0ccaa05ee7e987513e3e:ext/standard/string.c`, independently of the
runtime base. Omit `--owned-only` for the full corpus; that mode requires the three
`corpus/real/*.txt` snapshots. Exact byte
hashes of the measured public-document snapshots are in `data/corpus-manifest.json`; downloading
current pages with `corpus/real/fetch.sh` does not promise identical historical bytes.
Those document rows are supplementary. The primary 76 cases need only the owned
fixtures; do not silently substitute new snapshots and call them the same corpus.

## Repeat the native compiler cycle matrix

`data/primary-filter.txt` selects the unchanged 76-case primary set. The native runner
chooses a suitable measurement CPU by default. Use `bench check` and explicit `--cpu`
if needed; keep its SMT sibling and other workloads idle.

```sh
d=reports/substr-adaptive-search
./bench check
./bench compare "$d/suite.php" \
    gcc15=base-gcc15:product-guard-gcc15 \
    clang21=base-clang21:product-guard-clang21 \
    --filter "$(cat "$d/data/primary-filter.txt")" --passes 5 --target-ms 50 \
    --wait-idle 600 --out results/substr-final-amd-cycles.json
./bench table results/substr-final-amd-cycles.json --full

# Intel, with the four corresponding build pairs already built:
./bench compare "$d/suite.php" \
    gcc13=base-gcc13:product-guard-gcc13 gcc14=base-gcc14:product-guard-gcc14 \
    clang18=base-clang18:product-guard-clang18 clang20=base-clang20:product-guard-clang20 \
    --filter "$(cat "$d/data/primary-filter.txt")" --passes 3 --target-ms 50 \
    --wait-idle 600 --out results/substr-final-intel-cycles.json
./bench table results/substr-final-intel-cycles.json --full
```

The report's final AMD source is
[`cycles-reference.json`](data/amd/cycles-reference.json);
the fresh quiet Intel source is
[`control-cycles.json`](data/intel/control-cycles.json).
These are complete native `bench compare` series, including A/A and every pass.

## Repeat the warmed one-second series

The published [`scripts/reproduce.py`](scripts/reproduce.py) is the measurement driver
with portable input locations. It invokes the unchanged native `bench run` for one
case at a time, alternates GCC/Clang after each case, and aggregates without dropping
any cases. Before measuring it verifies input SHA-256 and case expressions against
the frozen report manifest. It also runs the six-case same-binary A/A pilot at 50 ms and 1000 ms. Set
`MEASURE_CPU` and `CONTROL_CPU` from the local machine's CPU topology and `bench check`;
set `BENCH_BUILDS` to the directory holding the four recorded builds.

```sh
python3 reports/substr-adaptive-search/scripts/reproduce.py \
    --bench-root "$PWD" --builds "$BENCH_BUILDS" \
    --out results/substr-final-seconds-owned \
    --candidate-commit "$CANDIDATE_COMMIT" \
    --cpu "$MEASURE_CPU" --orchestrator-cpu "$CONTROL_CPU" --primary-only
```

Use `--full` instead of `--primary-only` to repeat all 233 cases when the exact public
snapshots are available. Full mode checks that all 233 inputs/cases exist. Use a new
output directory for a new experiment: the driver resumes matching completed files.

A direct native command for one case is:

```sh
./bench run reports/substr-adaptive-search/suite.php \
    --a base-gcc15 --b product-guard-gcc15 \
    --filter '^render-template/4k @ ' --rounds 4 --samples 1 \
    --target-ms 1000 --warmup-ms 1000 --perf --wait-idle 300
```

The final one-second series has one case per PHP process. An earlier full suite used
one process for all filtered cases within a round; reproducing that grouping is a
different experiment. A large input with an early match may inspect only its prefix.

## Repeat the quiet Intel elapsed series

```sh
./bench run reports/substr-adaptive-search/suite.php \
    --a base-gcc13 --b product-guard-gcc13 \
    --rounds 4 --samples 7 --target-ms 10 --perf --wait-idle 600
```

Repeat for every Intel compiler pair. The original focus and quality selections are
recorded in the [quiet Intel policy and data](README.md#machine-and-method).
Its published main rows use quality recheck, then preselected focus, then original
full-run data; all original rows remain in the complete appendix. Recheck with
`--target-ms 50` and the recorded selection, rather than selecting by a desirable sign.

## Confirmations, profiling and correctness

The final AMD confirmation [policy](data/amd/final-confirmation/policy.json)
and [23-case selection](data/amd/final-confirmation/selection.json)
are fixed. Each selected case has one same-setting A/B repeat. Originally usable slower
cases also get stock-versus-stock and candidate-versus-candidate A/A. `bench why` uses
five passes for the recorded unchanged-instruction slower rows. All 47 native runs
and eight profile logs are published beside that policy; no repeated search for a
favourable answer is part of it.

```sh
./bench why reports/substr-adaptive-search/suite.php \
    base-gcc15 product-guard-gcc15 --filter '^parse-http/body64k @ ' --passes 5

# Native boundary/stress series, independently of everyday cases:
./bench compare reports/substr-adaptive-search/boundary-suite.php \
    gcc15=base-gcc15:product-guard-gcc15 clang21=base-clang21:product-guard-clang21 --target-ms 25
./bench compare reports/substr-adaptive-search/adversarial-suite.php \
    gcc15=base-gcc15:product-guard-gcc15 clang21=base-clang21:product-guard-clang21

BENCH_PHP="$BENCH_BUILDS/product-guard-gcc15/sapi/cli/php" tests/run.sh
```

Run the affected PHP tests from each candidate build worktree:

```sh
cd "$BENCH_BUILDS/product-guard-gcc15"
sapi/cli/php run-tests.php -q -j8 -p "$PWD/sapi/cli/php" ext/standard/tests/strings
```

The broader release/debug-ZTS PHPT summaries, exact extracted source hashes, sanitizer
results and mutation checks are in [validation.json](data/validation.json). Follow
[verify/README.md](verify/README.md) to repeat the guard-page, random-input, sanitizer
and work-budget checks. Native ARM/32-bit testing was not performed here.
