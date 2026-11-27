# Reproduce the grapheme_ascii_check() report

About 80 minutes on a 16-core machine, 32 of them the series. Run all steps in one shell. Needs:
- git, Python 3, `taskset`, PHP 8 on the `PATH` (it runs the `bench` tool), GCC and clang with their C++ compilers (`g++`, `clang++`);
- the build tools of php-src and the ICU headers:
  - Ubuntu: `sudo apt install build-essential autoconf bison re2c pkg-config clang libicu-dev php-cli linux-tools-$(uname -r)`;
  - Debian: the same with `linux-perf` instead of `linux-tools-$(uname -r)`;
  - Fedora: `sudo dnf install gcc gcc-c++ make autoconf bison re2c pkgconf clang libicu-devel php-cli perf`;
- `perf` with access to hardware counters: `kernel.perf_event_paranoid` ≤ 2 (`sudo sysctl kernel.perf_event_paranoid=2`; Debian defaults to 3). Most VMs and containers have no counters;
- about 16 GB free disk: `bench build` wants 10 GB free before each build;
- about 10 GB of free memory for step 6.

The report was measured with GCC 15.2, clang 21.1 and ICU 78.2. Other versions build the same code, but the numbers differ. If a warning stops a release build, add `--no-werror` to it and say so.

1. Sources (a few minutes):

   ```
   git clone https://github.com/ArtUkrainskiy/php-src-bench.git
   git clone --filter=blob:none https://github.com/php/php-src.git
   git -C php-src fetch https://github.com/ArtUkrainskiy/php-src.git +grapheme-ascii-check-words:grapheme-ascii-check-words
   BASE=abab936a39594561990b002055944fc31abd7cb6
   CHG=grapheme-ascii-check-words
   git -C php-src diff $BASE $CHG | diff - <(sed -n '/^diff/,/^-- $/p' php-src-bench/reports/grapheme-ascii-check/grapheme-ascii-check.patch | sed '$d') && echo "the branch is the measured code"
   cd php-src-bench
   ./bench doctor
   ```

   If the branch has moved, build the measured code from the patch instead: `git -C ../php-src checkout -q -b grapheme-ascii-check-report $BASE && git -C ../php-src -c user.name=repro -c user.email=repro@example.invalid am "$PWD/reports/grapheme-ascii-check/grapheme-ascii-check.patch" && CHG=grapheme-ascii-check-report`.

2. Builds (2–3 minutes each on 16 cores, `ok: …/sapi/cli/php` at the end). `bench build` takes the sources from `../php-src`. These are full builds, not `--slim`: steps 4 and 7 run php-src tests in them. The default profile is `docker` with `--enable-werror`.

   ext/intl is C++. The Docker image passes its flags in `CPPFLAGS`, so its C++ gets `-O2`; the commands below do the same. Without it master builds the C++ of ext/intl without `-O2` (GH-25688), and master looks slower than it is. `bench build --cc` doesn't set `CXX`, so each compiler gets its own command. `bench build` doesn't notice a change of `CXX` or `CXXFLAGS` alone: keep these build names for these settings.

   ```
   R=reports/grapheme-ascii-check
   P=../php-builds
   F='-fstack-protector-strong -fpic -fpie -O2 -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64'
   export BENCH_CONFIGURE_EXTRA=--enable-intl
   for v in base:$BASE chg:$CHG; do
     CC=gcc CXX=g++ CPPFLAGS="$F" CXXFLAGS=-g ./bench build gac-${v%%:*}-gcc ${v#*:} &&
     CC=clang CXX=clang++ CPPFLAGS="$F" CXXFLAGS=-g ./bench build gac-${v%%:*}-clang ${v#*:} &&
     CC=gcc CXX=g++ ./bench build --profile asan gac-${v%%:*}-asan ${v#*:} || break
   done
   CC=gcc CXX=g++ CPPFLAGS="$F" CXXFLAGS=-g BENCH_CONFIGURE_EXTRA='--enable-intl --enable-zts' ./bench build gac-chg-zts $CHG
   unset BENCH_CONFIGURE_EXTRA
   grep -E '^(CXX|CPPFLAGS) =' $P/gac-base-gcc/Makefile $P/gac-base-clang/Makefile     # CXX = g++ / clang++, CPPFLAGS has -O2
   $P/gac-chg-zts/sapi/cli/php -v | head -1     # ends with "(ZTS)"
   ```

   The data files of this report call these builds `k10-base-*` (master) and `k10-*` (the change); `k10` is only a name prefix. [`data/builds.txt`](data/builds.txt) lists the commit and the SHA-1 of each binary. The head of the branch builds the measured binaries.

3. Output comparison (about 7 minutes, most of it ASan). Every line must say `reference` or `same`, and the last line `exit 0`. On ICU 78.2 the second column is `426b042197afb453b63c735dd383f8a5` and the third `10` ([`data/difftest.txt`](data/difftest.txt)). Another ICU version can split non-ASCII text differently and print another MD5; master and the change must still agree.

   ```
   $R/difftest.sh $P/gac-base-gcc/sapi/cli/php $P/gac-base-clang/sapi/cli/php $P/gac-chg-gcc/sapi/cli/php $P/gac-chg-clang/sapi/cli/php $P/gac-chg-zts/sapi/cli/php
   USE_ZEND_ALLOC=0 $R/difftest.sh $P/gac-base-gcc/sapi/cli/php $P/gac-base-asan/sapi/cli/php $P/gac-chg-asan/sapi/cli/php
   ```

4. php-src tests of ext/intl (about a minute per build, 5 with ASan):

   ```
   $R/tests.sh $P/gac-base-gcc $P/gac-base-clang $P/gac-base-asan $P/gac-chg-gcc $P/gac-chg-clang $P/gac-chg-asan $P/gac-chg-zts
   mkdir -p /tmp/gac && cp $P/gac-chg-gcc/ext/intl/tests/grapheme_ascii_check_positions.phpt /tmp/gac/
   for b in gac-base-gcc gac-base-clang; do echo "== $b: the new test"; (cd $P/$b && TEST_PHP_EXECUTABLE=sapi/cli/php sapi/cli/php -n run-tests.php -q -n --no-color /tmp/gac | grep -E '^Tests (passed|failed)'); done
   ```

   Expected on ICU 78.2 ([`data/tests.txt`](data/tests.txt), [`data/new-test-on-master.txt`](data/new-test-on-master.txt)): 0 failed on the release builds, 548 passed with the change and 547 on master (the new test is in the change's tree only), 51 skipped. Both ASan builds fail the same seven `oom_*.phpt` tests, in varying order. Another ICU version changes the passed and skipped counts; the failures must be the same on master and the change. The new test passes on master.

5. The series (about 32 minutes) on an idle core. The first `bench table` prints the table of the README, the second the main table of [`FULL-TABLES.md`](FULL-TABLES.md). The group names are only labels; these are the ones of the published series:

   ```
   CPU=15     # an idle core, not CPU 0 or its sibling; check with ./bench check --cpu $CPU
   O=$PWD/results/grapheme-ascii-check; mkdir -p $O     # results/ is not tracked by git
   ./bench compare $R/grapheme.php gcc15=gac-base-gcc:gac-chg-gcc clang21=gac-base-clang:gac-chg-clang clang21-aa=gac-base-clang:gac-base-clang \
     --passes 15 --cpu $CPU --out $O/series.json
   ./bench table $O/series.json --labels $R/labels.txt --no-control
   ./bench table $O/series.json --full --header
   ```

   On a hybrid Intel CPU pick a P-core, one with the highest `MAXMHZ` in `lscpu --extended`. For a quick try add `--passes 1 --filter "ASCII (5|64) B"` and run `bench table` without `--labels`. One pass of a short-string row swings by 10% or more on this machine, so it shows the large rows only.

6. Strings over 2 GiB (about a minute, about 9 GB of memory per run). [`large-string.php`](large-string.php) calls the eight functions on 2³¹ + 8 bytes. Expected: the text of [`data/large-string.txt`](data/large-string.txt) and `exit 0` for both. Master and the change differ only in the `grapheme_strlen()` and `grapheme_strstr()` lines.

   ```
   for b in base:master chg:change; do echo "== ${b#*:}"; $P/gac-${b%%:*}-gcc/sapi/cli/php -n -d memory_limit=-1 $R/large-string.php; echo "exit $?"; done
   ```

7. Do the checks catch mistakes (about 4 minutes)? `mutants.sh` edits `ext/intl/grapheme/grapheme_util.cpp` inside the build, rebuilds it and restores it from git at the end. Run it after the series, since it rebuilds the binary the series measures:

   ```
   $R/mutants.sh $P/gac-chg-gcc $P/gac-base-gcc/sapi/cli/php
   WITHOUT_NEW_TEST=1 $R/mutants.sh $P/gac-chg-gcc $P/gac-base-gcc/sapi/cli/php
   ```

   Expected: the tables of [`data/mutants.txt`](data/mutants.txt) and [`data/mutants-without-new-test.txt`](data/mutants-without-new-test.txt).

8. Clean up: `rm -rf results/grapheme-ascii-check /tmp/gac; git -C ../php-src checkout -q master; git -C ../php-src branch -D grapheme-ascii-check-words grapheme-ascii-check-report 2>/dev/null; ./bench gc --yes 'gac-*'`.

The published tables are rendered with `./bench table $R/series.json --labels $R/labels.txt --no-control` (README), `./bench table $R/series.json --full --header`, and `./bench table` with `--full` on [`memchr-series.json`](memchr-series.json) and [`inword-series.json`](inword-series.json) (FULL-TABLES). Back to the [report](README.md).
