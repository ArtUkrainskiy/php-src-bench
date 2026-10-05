# Instructions for AI agents

php-src-bench measures whether a change to php-src made a C function faster and kept its output the
same. You will either *use* it to evaluate a php-src change, or *change* the tool itself. Read the
part that applies. `README.md` has the user-facing overview, `docs/methodology.md` explains why the
rules below exist.

## Using php-src-bench to evaluate a php-src change

### Procedure

1. Build the reference and the candidate. `.` snapshots the php-src working tree without touching
   it; a build of the same name is incremental.

   ```sh
   ./bench build base master
   ./bench build dev .
   ```

2. Pick the suite (`./bench suites`), or write one (`docs/suites.md`) when no suite calls the
   function you changed. Include short inputs, inputs of 64 KB or more, the worst case of the new
   code and the neighbouring code paths you did not intend to change.

3. Iterate with a filter and `--quick`. Quick runs give no verdict (`?`), only a direction.

   ```sh
   ./bench run htmlspecialchars --a base --b dev --filter 'en-|ru-' --quick --perf --no-save
   ```

4. Measure for real: the whole suite, default rounds, with instruction counts.

   ```sh
   ./bench run htmlspecialchars --a base --b dev --perf --wait-idle 600
   ```

5. Check the output on generated inputs, and under sanitizers if the change touches buffers or
   pointer arithmetic (`docs/suites.md`, "Differential tests").

   ```sh
   ./bench difftest html-encode base dev --count 20000
   ```

6. Run the relevant php-src tests with the built binary, from the build's worktree:

   ```sh
   cd ../php-builds/dev && sapi/cli/php run-tests.php -q -j8 -p "$PWD/sapi/cli/php" ext/standard/tests/strings
   ```

### Rules

- **Never benchmark a debug build.** A php-src tree used for development is often configured with
  `--enable-debug`. Measure builds made by `bench build`, never `php-src/sapi/cli/php` directly.
  A result with a debug side has `DEBUG` in its header and a line starting with `!`; treat that
  run as void. Any other `!` line (different compiler, configure options or CFLAGS) voids it too.
- **Rebuild after every edit, then re-measure.** Do not carry numbers over from an earlier
  version of the patch: in a large function an equivalent rewrite can change the generated code
  by several percent. The one exception is an edit that provably leaves the machine code alone
  (a rename, a comment): show it with identical `objdump -d` output of the function, and say so.
- **Read the warnings.** A spread (`±`) above 5%, load on the pinned core or a running compiler
  mean the wall times of that run are not usable. Wait and run again (`--wait-idle`), or rely on
  instruction counts, which load does not affect.
- **Two metrics, both reported.** Wall time is what users feel; instruction counts are what
  php-src CI measures and what stays stable. When they disagree, report the disagreement and find
  out why (`perf stat -e branch-misses`, `objdump -d`) instead of quoting the nicer one.
- **`layout?` is not a result.** It marks a wall-time difference with unchanged instruction
  counts: the amount of work is the same, so something else changed (code placement, cache or
  branch behaviour). Find out which before reporting the row, in either direction.
- **A disturbed round means run again.** When the runner says that a round is more than 10%
  slower than another round of the same build, the marks and ratios of those cases are shaky.
- **`≠out` stops everything.** Outputs of A and B differ. Find out why before looking at timings.
- **Short inputs flatter branchy code.** A 1 KB input repeated in a loop is memorized by the
  branch predictor. Do not conclude anything about a byte loop from inputs under 64 KB alone.
- **Look for regressions on purpose.** For every fast path, measure the inputs that miss it. A
  result table where every row improved has usually not tested the slow side.
- **Do not edit files under `../php-builds/`.** They are build outputs; change php-src and rebuild.
- **Do not change the user's php-src checkout to run a benchmark.** `bench build` needs no branch
  switch, stash or commit there.

### Reporting

- Give ranges per kind of input ("English text 1.7–2.5× faster"), not one headline number, and
  always list the rows that got slower or did not change.
- State what the comparison is: the two commits, the suite, whether the machine was quiet.
- Say how the output was verified: which generator, how many inputs, which test directories.
- A number that was estimated rather than measured must be labelled as an estimate.
- For a pull request, `./bench show <result.json> --md` gives the table; the full table of a run
  worth citing goes to `reports/` (see `reports/README.md`).

## Changing php-src-bench itself

### Layout

| Path | Role |
|---|---|
| `bench` | entry point: dispatches to the scripts in `lib/` |
| `lib/runner.php` | orchestrator: `run`, `show`, `check`, `builds`, `suites` |
| `lib/harness.php` | runs inside the PHP binary under test: loads a suite, times its cases |
| `lib/process.php`, `environment.php`, `stats.php`, `render.php`, `console.php` | parts of the orchestrator |
| `lib/Corpus.php` | builds inputs from `corpus/` |
| `lib/build.sh`, `tune.sh`, `difftest.sh` | `bench build`, `bench tune`, `bench difftest` |
| `lib/difftest.php` | what every generator in `difftests/` shares |
| `suites/` | benchmark suites |
| `difftests/` | generators for differential tests |
| `corpus/` | generated text (committed), `generate.py`; `corpus/real/` downloaded documents (not committed) |
| `tests/` | self-tests: `tests/run.sh` |
| `results/` | saved runs, not committed |
| `reports/` | published results, committed |

### Constraints

- **PHP 8.0 syntax, no extensions.** `lib/*.php`, suites and generators run on whatever PHP is
  measured, built with `--disable-all`: no mbstring, ctype, posix; no enums, readonly properties,
  first-class callable syntax or other features newer than 8.0.
- **No dependencies.** No Composer, no PHP or Python packages. Bash, PHP and coreutils only.
- **Results stay comparable.** Do not change the generated corpus, `Corpus::` output or the way a
  case is timed without saying so in the commit message: published numbers depend on them.
  `tests/run.sh` pins hashes of generated inputs to catch accidental changes.
- **Rendering is tested against files.** If you change the table on purpose, run
  `tests/run.sh --update` and review the diff of `tests/expected/`.
- **The result JSON has a version** (`format`). Old files must keep rendering with `bench show`.
- **No machine-specific paths or CPU numbers** in code, suites or docs. CPU choice comes from
  `/sys`, locations from `PHP_SRC` and `BENCH_BUILDS`.
- **Style.** PHP: 4 spaces, plain functions (the two classes, `Corpus` and `DifftestRng`, are
  what suites and generators call), `declare(strict_types=1)` in the orchestrator files, a comment
  where the reason is not obvious from the code, named constants for thresholds. Bash: tabs,
  `set -euo pipefail`.
- **Data shapes.** Results and sides are plain arrays; their keys are described once, at the top
  of `lib/runner.php`. Keep that description true.

### Before you finish

```sh
tests/run.sh
```

It needs any PHP 8.0+ (a build, `BENCH_PHP`, or `php` in `PATH`). Do not commit `results/`,
`corpus/real/*.txt` or anything from `../php-builds/`.
