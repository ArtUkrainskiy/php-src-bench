# Reproduce the date_format() report

About 70 minutes on a 16-core machine, plus about 35 minutes for the optional step 7. Run all steps in one shell. Needs:
- git, Python 3, `taskset`, GCC and clang;
- the build tools of php-src: on Debian or Ubuntu `sudo apt install build-essential autoconf bison re2c pkg-config clang linux-tools-$(uname -r)`, on Fedora `sudo dnf install gcc make autoconf bison re2c pkgconf clang perf`. The builds use `--disable-all`, so no library headers are needed;
- `perf` with access to hardware counters (`kernel.perf_event_paranoid` ≤ 2);
- about 15 GB free disk: `bench build` wants 10 GB free before each build.

`./bench doctor` lists what the machine has and lacks.

1. Sources (a few minutes):

   ```
   git clone https://github.com/ArtUkrainskiy/php-src-bench.git
   git clone --filter=blob:none https://github.com/php/php-src.git
   git -C php-src fetch https://github.com/ArtUkrainskiy/php-src.git +date-format-lazy-offset:date-format-lazy-offset
   ```

   If the branch has moved, build the measured code from the patch instead: `git -C php-src checkout -q -b date-format-lazy-offset-report 5ddcc3591fb && git -C php-src -c user.name=repro -c user.email=repro@localhost am "$PWD/php-src-bench/reports/date-format-lazy-offset/date-format-lazy-offset.patch"`, and use `date-format-lazy-offset-report` for `date-format-lazy-offset` below.

2. Builds (about 3 minutes each on 16 cores, `ok: …/sapi/cli/php` at the end). `bench build` takes the sources from `../php-src`. Start here on a rerun. These are full builds, not `--slim`: steps 4 and 6 run php-src tests in them. The default profile is `docker` with `--enable-werror`. If your compiler stops on a warning outside this change, add `--no-werror` and say so. `bench build --cc` names a build after the compiler's major version, so `G` and `C` pick up yours. With builds of two GCC or clang versions in `../php-builds`, set `G` and `C` by hand.

   ```
   cd php-src-bench
   R=reports/date-format-lazy-offset
   P=../php-builds
   ./bench build --cc gcc,clang dfo-base 5ddcc3591fb
   ./bench build --cc gcc,clang dfo-chg date-format-lazy-offset
   CC=gcc ./bench build --profile asan dfo-base-asan 5ddcc3591fb
   CC=gcc ./bench build --profile asan dfo-chg-asan date-format-lazy-offset
   CC=gcc BENCH_CONFIGURE_EXTRA=--enable-zts ./bench build dfo-chg-zts date-format-lazy-offset
   G=$(cd $P && ls -d dfo-base-gcc* | sed 's/dfo-base-//'); C=$(cd $P && ls -d dfo-base-clang* | sed 's/dfo-base-//'); echo $G $C
   $P/dfo-chg-zts/sapi/cli/php -v | head -1     # ends with "(cli) (built: …) (ZTS)"
   ```

   The series files of this report call these builds `k14-base-*` (master) and `k14off-*` (the change). The measured commit differs from the branch only in `NEWS`, `UPGRADING` and the new test: the branch has no `NEWS` entry.

3. Output comparison (about a minute). Every line must say `reference` or `same`, and the last line `exit 0`. Expected: `difftest-chars.php` `557f4136519883344edbc0edbbf557ab`, 969 lines; `difftest-random.php` `0be9298e6b81ff1bebbf5646e96acecc`, 51242 lines ([`data/difftest.txt`](data/difftest.txt)). The time zone database comes with php-src, so other machines should get the same hashes.

   ```
   $R/difftest.sh $P/dfo-base-$G/sapi/cli/php $P/dfo-base-$C/sapi/cli/php $P/dfo-chg-$G/sapi/cli/php $P/dfo-chg-$C/sapi/cli/php $P/dfo-chg-zts/sapi/cli/php
   USE_ZEND_ALLOC=0 $R/difftest.sh $P/dfo-base-$G/sapi/cli/php $P/dfo-base-asan/sapi/cli/php $P/dfo-chg-asan/sapi/cli/php
   ```

4. php-src tests of ext/date (about a minute per build, 5 with ASan). The new test is only in the change's tree: copy it into the GCC master build to run it on master too.

   ```
   cp $P/dfo-chg-$G/ext/date/tests/date_format_escaped_timezone_chars.phpt $P/dfo-base-$G/ext/date/tests/
   $R/tests.sh $P/dfo-base-$G $P/dfo-base-$C $P/dfo-base-asan $P/dfo-chg-$G $P/dfo-chg-$C $P/dfo-chg-asan $P/dfo-chg-zts
   ```

   Expected ([`data/tests.txt`](data/tests.txt)): 0 failed, except `ExtendDateTime.phpt` on both ASan builds. 729 passed on the release builds with the new test, 728 on the clang master build without it, 18 skipped everywhere. ASan: 727 and 728 passed, 1 failed.

5. The series (about 10 minutes) on an idle core. The first `bench table` prints the table of the README, the second the main table of `FULL-TABLES.md`:

   ```
   CPU=$(( $(nproc) - 1 ))     # an idle core; check with ./bench check --cpu $CPU
   O=$PWD/results/date-format-lazy-offset; mkdir -p $O     # results/ is not tracked by git
   ./bench compare $R/date.php $G=dfo-base-$G:dfo-chg-$G $C=dfo-base-$C:dfo-chg-$C --passes 15 --cpu $CPU --out $O/series.json
   ./bench table $O/series.json --labels $R/labels.txt --no-control
   ./bench table $O/series.json --full
   ./bench compare $R/date-extra.php $G=dfo-base-$G:dfo-chg-$G $C=dfo-base-$C:dfo-chg-$C $C-aa=dfo-base-$C:dfo-base-$C --passes 15 --cpu $CPU --out $O/extra.json
   ./bench table $O/extra.json --labels $R/extra-labels.txt --no-control
   ```

   The second series (about 10 minutes) prints the table of "More paths"; its last column is clang master against itself.

   On a hybrid Intel CPU the last cores are E-cores: pick a P-core instead, one with the highest `MAXMHZ` in `lscpu --extended`, not CPU 0 or its sibling. For a quick try add `--passes 1 --filter "Madrid"`, and run `bench table` without `--labels` then. One pass swings by up to 10% on this machine, so it shows the large rows only.

6. Do the checks catch mistakes (about 3 minutes, 10 with ASan)? `mutants.sh` edits `ext/date/php_date.c` inside the build, rebuilds it and restores it at the end. Run it after the series, since it rebuilds the binary the series measures:

   ```
   $R/mutants.sh $P/dfo-chg-$G $P/dfo-base-$G/sapi/cli/php
   USE_ZEND_ALLOC=0 $R/mutants.sh $P/dfo-chg-asan $P/dfo-base-$G/sapi/cli/php
   ```

   Expected: the tables of [`data/mutants-release.txt`](data/mutants-release.txt) and [`data/mutants-asan.txt`](data/mutants-asan.txt).

7. Optional: the aligned builds and the code placement data (about 35 minutes). The aligned builds use the flags of the main series plus `-falign-functions=64 -falign-loops=32`. The `perf record` lines print the profile of [`data/placement-clang.md`](data/placement-clang.md):

   ```
   export BENCH_CFLAGS='-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -falign-functions=64 -falign-loops=32'
   ./bench build --slim --profile docker --cc gcc,clang dfo-base-al 5ddcc3591fb
   ./bench build --slim --profile docker --cc gcc,clang dfo-chg-al date-format-lazy-offset
   unset BENCH_CFLAGS
   ./bench compare $R/date.php $G=dfo-base-al-$G:dfo-chg-al-$G $C=dfo-base-al-$C:dfo-chg-al-$C --passes 15 --cpu $CPU \
     --filter "\((.c.|.Y-m-d.TH:i:sP.|.D, d M Y H:i:s O.|.T.|DATE_ATOM)\)|format\(.Y.\) @ (UTC|Europe)" --out $O/align.json
   ./bench table $O/align.json --full
   ./bench compare $R/date-extra.php $G=dfo-base-al-$G:dfo-chg-al-$G $C=dfo-base-al-$C:dfo-chg-al-$C $C-aa=dfo-base-al-$C:dfo-base-al-$C --passes 15 --cpu $CPU \
     --filter "gmdate|format|date\(" --out $O/extra-align.json
   ./bench table $O/extra-align.json --full
   ./bench why $R/date.php dfo-base-$C dfo-chg-$C --filter "format\(.c.\) @ offset" \
     --functions date_format,ap_php_slprintf,ap_php_conv_10,php_conv_fp,_emalloc,timelib_time_offset_ctor --passes 7 --cpu $CPU
   for v in base chg; do
     taskset -c $CPU perf record -q -o $O/$v.data -e cycles:u $P/dfo-$v-$C/sapi/cli/php -n \
       -r '$d = new DateTimeImmutable("2026-11-18T12:34:56.123456+05:30"); for ($i = 0; $i < 3000000; $i++) { $d->format("c"); }'
     perf report -q -i $O/$v.data --sort symbol --percent-limit 3 | head
   done
   ```

8. Clean up: `rm -rf "$O"; git -C ../php-src checkout -q master; git -C ../php-src branch -D date-format-lazy-offset date-format-lazy-offset-report 2>/dev/null; ./bench gc --yes 'dfo-*'`.

The published tables are rendered from [`series.json`](series.json), [`align-series.json`](align-series.json), [`extra-series.json`](extra-series.json), [`extra-align-series.json`](extra-align-series.json) and [`earlier-series.json`](earlier-series.json) with `bench table`. [`date.php`](date.php) got clearer comments after the series ran; its cases are the same. Back to the [report](README.md).
