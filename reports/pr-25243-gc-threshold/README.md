# GC threshold that follows the live graph (php-src PR #25243)

Review material for [php/php-src#25243](https://github.com/php/php-src/pull/25243) by kamil-tekiela, "Fix GH-9993: Bad performance with hard-coded GC_THRESHOLD_* values". PR head [`af71b8e0f66`](https://github.com/php/php-src/pull/25243/commits/af71b8e0f66), merged onto master [`4f3d9508be9`](https://github.com/php/php-src/commit/4f3d9508be9) without conflicts. Measured on 13 November 2026. The PR is open; nothing here is merged.

By default the cycle collector (GC) runs when 10,000 possible roots have piled up. Each run walks everything reachable from those roots, including objects that are still alive. With a large live graph, every run walks the whole graph again. That is [GH-9993](https://github.com/php/php-src/issues/9993): test suites that keep big object graphs alive got about two times slower in PHP 8.1.10. The PR counts the nodes a run walked. It then raises the threshold to at least (walked − collected) / 8, so the next run waits until enough new roots pay for that walk. The threshold goes back to normal at the start of each request.

## Summary

- **Large live graph:** with 1 million live objects the script takes 85% less time than on master (17.2 s → 2.6 s). With 200,000 live objects it takes 38% less, with 160,000 23% less. GCC 15.2 and Clang 21.1 agree within 3 points.
- **Small or no live graph:** no change in the threshold. Up to 80,000 live objects it stays at 10,001. Scripts with 70,000–80,000 live objects take 2–4% longer with the same threshold and the same number of GC runs. On GCC that is mostly the new counter: 1.7–1.8% more instructions. On Clang instructions are equal and cycles grow 3.4%, which is code placement.
- **Peak memory with destructors grows up to 6.7%.** In two of the three destructor scripts peak RSS grows 6.6–6.7%, in the third 0.3%. When garbage has a `__destruct()` method, the GC runs a second pass, and the PR adds the nodes of both passes. The threshold ends up twice as high as intended (54,547 instead of 25,001 with 200,000 live objects). A script that fits into `memory_limit=168M` on master hits the limit on the PR in 5 of 5 runs.
- **One-line fix:** resetting the counter before the second pass ([`reset.diff`](reset.diff)) gives the same peak memory as master and no fatal error. The destructor cases stay 11–35% faster than master.
- **Real test suites:** doctrine/orm's PHPUnit suite (3,696 tests, GC is 9% of its time) runs 1.2% faster on GCC and the same on Clang. Symfony Demo's tests spend 1% in the GC and show no change. PHPStan and Composer turn the GC off themselves with `gc_disable()`.
- **Correctness:** no issues found. `Zend`, `ext/standard` and `ext/spl` tests pass under ASan/UBSan, and so do the PR's test workload and the doctrine/orm suite. The PR's new test fails on master and passes with the PR.

## Results

Change in wall time with the PR, relative to master (negative = faster). Median of 5 rounds; the build order alternates every round. Peak RSS is the process maximum (`VmHWM`), so it includes the GC root buffer, which `memory_get_peak_usage()` does not see.

| case in the data | what it does | master, s (GCC) | GCC 15.2 | Clang 21.1 | peak RSS, master | peak RSS change |
|---|---|--:|--:|--:|--:|--:|
| `live1m` | `synth.php`: 1M live objects; 2M iterations, each makes a 2-object garbage cycle and touches a live object | 17.158 | −85% | −85% | 141 MiB | 0% |
| `live200k` | `synth.php`: same with 200k live objects and 500k iterations (the PR's test) | 0.334 | −38% | −39% | 50 MiB | 0% |
| `pairs 160000 0` | `mem.php`: 160k live objects, 200k iterations of the same loop | 0.126 | −23% | −23% | 48 MiB | 0% |
| `pairs 80000 0` | 80k live objects, same | 0.086 | +2.3% | +3.2% | 37 MiB | 0% |
| `pairs 70000 0` | 70k live objects, same | 0.079 | +2.5% | +3.6% | 36 MiB | 0% |
| `nolive` | `synth.php`: no live objects, 2M garbage cycles | 0.252 | +0.4% | +0.8% | 26 MiB | 0% |
| `pairs 1000000 16` | `mem.php`: 1M live objects, each garbage cycle holds 16 KiB | 1.284 | −3% | −3% | 1,006 MiB | 0% |
| `dtor 1000000 0` | `mem.php`: 1M live objects, garbage with `__destruct()` | 0.848 | −34% | −33% | 159 MiB | **+6.6%** |
| `dtor 200000 0` | `mem.php`: 200k live objects, garbage with `__destruct()` | 0.291 | −52% | −54% | 54 MiB | +0.3% |
| `dtor 200000 4` | `mem.php`: 200k live objects, garbage with `__destruct()` and 4 KiB | 0.489 | −27% | −29% | 184 MiB | **+6.7%** |
| `dtor 200000 4`, `168M` | same with `memory_limit=168M` | ok 5 of 5 | fails 5 of 5 | fails 5 of 5 | | |
| `orm` | doctrine/orm PHPUnit suite | 5.127 | −1% | 0% | 197 MiB | −1% |

The PR with the one-line fix, same workloads, GCC 15.2, a separate series ([`reset-summary.md`](data/reset-summary.md)):

| case in the data | PR | PR + fix | peak RSS, PR | peak RSS, PR + fix |
|---|--:|--:|--:|--:|
| `dtor 1000000 0` | −34% | −11% | +6.6% | 0% |
| `dtor 200000 4` | −26% | −18% | +6.6% | 0% |
| `dtor 200000 4`, `168M` | fails 5 of 5 | ok 5 of 5 | | |
| `live1m` | −85% | −85% | 0% | 0% |
| `pairs 80000 0` | +2.3% | +5.8% | 0% | 0% |

At 70,000 and 80,000 live objects the fix executes the same instructions as the PR, 1.7–1.8% more than master. In this series it takes 3.6–4.7% more cycles than master, against 2.2–2.5% for the PR. No second pass happens there, so the extra line never runs. The difference is code placement.

Full tables with the spread of the five rounds and cycles: [`series-summary.md`](data/series-summary.md) (master and PR, both compilers), [`reset-summary.md`](data/reset-summary.md) and [`reset-series-pr-summary.md`](data/reset-series-pr-summary.md) (fix series). Raw runs: [`series-20261113.csv`](data/series-20261113.csv), [`reset-20261113.csv`](data/reset-20261113.csv).

## Why the destructor case uses more memory

`zend_gc_collect_cycles()` sets `GC_G(visited)` to 0 once, before `rerun_gc:`. When the first pass finds garbage with destructors, it calls them and jumps back to `rerun_gc`. The second pass walks the live graph again. `gc_adjust_threshold()` then sees both passes in `visited`, so the threshold becomes (2 × live) / 8 instead of live / 8. Garbage waits about twice as long between runs, and the peak grows. The PR description reports up to +43% peak memory for a ratio of 4; with destructors, the PR's ratio of 8 behaves like 4.

The fix sets `GC_G(visited) = 0` before `goto rerun_gc`, so the threshold follows the last pass.

## Real workloads

GH-9993 has no public reproducer. These are the workloads I could run:

| workload | GC share of time on master | change with the PR |
|---|--:|---|
| doctrine/orm [`678c053`](https://github.com/doctrine/orm/commit/678c05360da70ba1d399e755f10930aa8f4c2c89) PHPUnit, SQLite | 9% | −1.2% (GCC), −0.1% (Clang), 5 rounds |
| symfony/demo [`f42980c`](https://github.com/symfony/demo/commit/f42980c690b4bf335fa41bbafdb075bb67b719c2) PHPUnit, 53 tests | 1% | 0%, 3 runs after a warm-up run ([`symfony-demo-20261113.txt`](data/symfony-demo-20261113.txt)) |
| doctrine/dbal [`b281545`](https://github.com/doctrine/dbal/commit/b2815456989aa41964ee66d7ab47b7885264acf3) PHPUnit, SQLite | 1% | not compared |
| PHPStan on doctrine/dbal | GC off: `bin/phpstan` calls `gc_disable()` | — |
| Composer 2.11.2 `install` | GC off while installing: `Installer.php` calls `gc_disable()` | — |

## The generational GC draft (#19709)

The PR thread suggests comparing with [#19709](https://github.com/php/php-src/pull/19709) (head `3e57c1eb150`, run with `FULL_GC_FREQ=10`). On the same builds it crashes. ASan reports a heap-use-after-free: a partial run frees a live object, and the next read of the live array touches freed memory. It reproduces every time with the 200,000-object workload above (`php synth.php live200k`). On the debug ASan build the doctrine/orm suite stops at an assertion in `gc_fetch_unused()`, and without ASan it ends with SIGSEGV. I did not compare its timings.

## Machine and method

- AMD Ryzen 9 5950X, Ubuntu 26.04, kernel 7.0, governor `performance` (checked after the series). One process at a time, pinned to CPU 15. I ran nothing else on the machine during the series.
- GCC 15.2 and Clang 21.1. Flags of the official Docker image: `-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64`, `-Wl,-O1 -pie`. NTS CLI with the extensions the test suites need.
- Wall time comes from the script's own timer (`hrtime()`); cycles and instructions from `perf stat`; peak RSS from `/usr/bin/time`.
- Each number in the Results tables is the median over 5 rounds of PR / master in the same round. The order of builds alternates every round.

## Output verification

- `run-tests.php --asan` for `Zend`, `ext/standard` and `ext/spl` on the PR with ASan/UBSan: 9,906 passed, 754 skipped. One test, `proc_open_multiplex.phpt`, failed under `-j28` load and passes 3 of 3 times alone.
- Under ASan with `USE_ZEND_ALLOC=0`: `synth.php live200k` and the doctrine/orm suite are clean.
- The PR's `Zend/tests/gc/gh9993.phpt` fails on master and passes with the PR.

## Not tested

ZTS builds, Intel, 32-bit and opcache/JIT. FPM with many requests per worker: the root buffer is persistent and never shrinks. The author's own worst-case script, which is not public. My closest case, 100,000 live objects with garbage rings of 100,000 objects, was 2% slower in a quick check of 3 runs.

## Reproduce

All commands run in this directory. Builds and the ORM checkout go into `builds/` and `orm/` next to `series.sh`.

1. **Builds** (about 3 minutes each on 32 threads). [`build.sh`](build.sh) clones php-src, checks out master `4f3d9508be9231940b946a618e8bda24fbbfbb1b`, merges the PR head `af71b8e0f66fce3ed9b03da0143c67397c12b9d5`, applies [`reset.diff`](reset.diff) for the fix, and builds with the flags above:
   ```
   for cc in gcc15 clang21; do ./build.sh master $cc; ./build.sh 25243 $cc; done
   ./build.sh reset gcc15
   ```
2. **doctrine/orm** for the `orm` rows, with the lock file from this run ([`orm-composer.lock`](orm-composer.lock)):
   ```
   git clone https://github.com/doctrine/orm.git orm && git -C orm checkout 678c05360da70ba1d399e755f10930aa8f4c2c89
   cp orm-composer.lock orm/composer.lock
   builds/gc-master-gcc15/sapi/cli/php composer.phar install -d orm --ignore-platform-reqs
   ```
   I used Composer 2.11.2.
3. **Machine setup.** `perf stat` must count cycles: `sudo sysctl kernel.perf_event_paranoid=-1` (my setting). Install `/usr/bin/time` (package `time`). Pick an idle core with `CPU=` (default 15). On hybrid Intel CPUs set `EVENTS=cpu_core/cycles/,cpu_core/instructions/`.
4. **Main series**, master against the PR, about 8 minutes (5 rounds × 2 compilers × 45 s; `live1m` alone takes 17 s on master):
   ```
   OUT=data/series-new.csv N=5 CCS="gcc15 clang21" ./series.sh
   python3 analyze.py data/series-new.csv 25243
   ```
5. **Fix series**, about 2.5 minutes:
   ```
   OUT=data/reset-new.csv N=5 CCS=gcc15 BUILDS="master 25243 reset" ORM=0 \
     CASES_OVERRIDE='"mem.php dtor 200000 0" "mem.php dtor 1000000 0" "mem.php dtor 200000 4" "mem.php pairs 70000 0" "mem.php pairs 80000 0" "synth.php nolive" "synth.php live200k" "synth.php live1m"' ./series.sh
   python3 analyze.py data/reset-new.csv reset
   python3 analyze.py data/reset-new.csv 25243
   ```

**Check that it worked.** Thresholds and GC run counts don't depend on the machine. `live200k` should show `10001/25001`. `dtor 200000 0` should show `10001/54547` for the PR and `10001/25001` for the fix. The `168M` row of `dtor 200000 4` should show fatal `0/5`.

The `memory_limit` of 168M sits between the PHP peaks of `dtor 200000 4` on master (162 MiB) and with the PR (174 MiB), as printed in `php_peak_mib`. With other extensions the peaks move; set `LIMIT=` between them.

`series.sh` stops if `OUT` exists, a build is missing, or perf can't count cycles. It deletes its temporary files.

Not scripted here: the Symfony Demo and doctrine/dbal runs, the PHPStan and Composer checks, the ASan builds and tests, and the #19709 runs. They are one-off checks with the same builds.

Scripts: [`build.sh`](build.sh), [`mem.php`](mem.php) (live graph plus garbage cycles, with or without payload and destructors), [`synth.php`](synth.php) (the PR's test workload and larger variants), [`gcstat.php`](gcstat.php) (prints `gc_status()` at shutdown, used with `auto_prepend_file`), [`series.sh`](series.sh), [`analyze.py`](analyze.py).
