# Reproduce the PDO::FETCH_OBJ report

About 55 minutes on a 16-core machine, plus 15 for the optional step 7. Run all steps in one shell, from `php-src-bench/` after step 1. On a rerun, start at step 2. Needs:
- git, Docker without sudo, Python 3, `taskset`;
- `perf` with access to hardware counters (`kernel.perf_event_paranoid` ≤ 2);
- the build tools of php-src, the SQLite and zlib headers (`libsqlite3-dev zlib1g-dev`, on Fedora `sqlite-devel zlib-devel`), GCC and clang;
- at least 10 GB free disk (`bench build` checks it before each build);
- valgrind for the optional step 7;
- port 53306 free.

1. Sources (a few minutes):

   ```
   git clone https://github.com/ArtUkrainskiy/php-src-bench.git
   git clone --filter=blob:none https://github.com/php/php-src.git
   git -C php-src fetch https://github.com/ArtUkrainskiy/php-src.git pdo-fetch-obj:pdo-fetch-obj
   cd php-src-bench
   R=reports/pdo-fetch-obj
   ```

   If the branch has moved, build the measured code from the patch instead: `git -C php-src checkout -q -b pdo-fetch-obj-report 48e34bf6348 && git -C php-src -c user.name=repro -c user.email=repro@localhost am "$PWD/php-src-bench/reports/pdo-fetch-obj/pdo-fetch-obj.patch"`, and use `pdo-fetch-obj-report` for `pdo-fetch-obj` below.

2. Builds (about 3 minutes each, `ok: …/sapi/cli/php` at the end). The default profile is `docker` with `--enable-werror`. If your compiler stops on a warning outside this change, add `--no-werror` and say so. `bench build --cc` names a build after the compiler's major version, so `G` and `C` pick up yours:

   ```
   export BENCH_CONFIGURE_EXTRA='--enable-pdo --with-pdo-sqlite --with-pdo-mysql'
   ./bench build --slim --cc gcc,clang pdoobj-base 48e34bf6348
   ./bench build --slim --cc gcc,clang pdoobj-chg pdo-fetch-obj
   CC=gcc ./bench build --profile asan pdoobj-base-asan 48e34bf6348
   CC=gcc ./bench build --profile asan pdoobj-chg-asan pdo-fetch-obj
   P=../php-builds
   G=$(cd $P && ls -d pdoobj-base-gcc* | sed 's/pdoobj-base-//'); C=$(cd $P && ls -d pdoobj-base-clang* | sed 's/pdoobj-base-//'); echo $G $C
   $P/pdoobj-base-$G/sapi/cli/php -n -m | grep -i pdo    # PDO, pdo_mysql, pdo_sqlite
   ```

3. MySQL 8.4.11 on 127.0.0.1:53306, kept off the core you measure on (under a minute). The builds have no OpenSSL, so the root user gets `mysql_native_password`:

   ```
   CPU=15     # the core for the series: an idle one, on a hybrid Intel CPU a P-core; check with ./bench check --cpu $CPU
   docker run -d --name pdoobj-mysql --cpuset-cpus 0-7 -p 127.0.0.1:53306:3306 -e MYSQL_ROOT_PASSWORD=bench -e MYSQL_DATABASE=bench \
     mysql@sha256:24989179f58856db763f418010c1169fecc944e3ec1ea7e921572d83eb070f70 --mysql-native-password=ON
   timeout 120 bash -c 'until docker exec pdoobj-mysql mysqladmin -h127.0.0.1 -uroot -pbench ping >/dev/null 2>&1; do sleep 2; done' || docker logs pdoobj-mysql
   docker exec pdoobj-mysql mysql -uroot -pbench -e "ALTER USER root@'%' IDENTIFIED WITH mysql_native_password BY 'bench'"
   export PDO_MYSQL_DSN='mysql:host=127.0.0.1;port=53306;dbname=bench'
   $P/pdoobj-base-$G/sapi/cli/php -n -r 'new PDO(getenv("PDO_MYSQL_DSN"), "root", "bench"); echo "mysql ok\n";'
   ```

   `--cpuset-cpus 0-7` keeps the server away from `$CPU` and its sibling: change it if your `$CPU` is in 0–7.

4. Output comparison (under a minute). Within SQLite and within MySQL every hash must be the same. Expected: SQLite `4d7c75c4af927041c61d301f8b18adbc`, MySQL `baf4723484f0afc163d6b6d60529e69a`. Equal hashes that differ from these mean another SQLite or MySQL version: compare with `$R/data/difftest/`.

   ```
   O=$PWD/results/pdo-fetch-obj; mkdir -p $O     # results/ is not tracked by git
   $R/difftest.sh $O/difftest $P/pdoobj-{base,chg}-$G/sapi/cli/php $P/pdoobj-{base,chg}-$C/sapi/cli/php \
     $P/pdoobj-{base,chg}-asan/sapi/cli/php
   ```

5. php-src tests (about 3 minutes per build, 10 with ASan). The tree must be at the tested commit:

   ```
   git -C ../php-src checkout -q 48e34bf6348
   $R/tests.sh ../php-src $P/pdoobj-base-$G/sapi/cli/php $O/tests-master.txt
   git -C ../php-src checkout -q pdo-fetch-obj
   $R/tests.sh ../php-src $P/pdoobj-chg-$G/sapi/cli/php $O/tests-change.txt
   $R/tests.sh ../php-src $P/pdoobj-chg-asan/sapi/cli/php $O/tests-change-asan.txt --asan
   ```

   Expected: 0 failed. The change has exactly one more passed test than master in the first run, the new test. Here: 512 / 131 / 134 passed on master and 513 / 131 / 134 on the change, with 22 / 5 / 2 skipped. The counts depend on the SQLite and MySQL versions. Many more skipped tests in the MySQL runs mean the server wasn't reachable.

6. The series (about 8 minutes) on `$CPU`. The first `bench table` prints the table of the README, the second the tables of `FULL-TABLES.md`:

   ```
   ./bench compare $R/suite.php $G=pdoobj-base-$G:pdoobj-chg-$G $C=pdoobj-base-$C:pdoobj-chg-$C --passes 15 --cpu $CPU --out $O/series.json
   ./bench table $O/series.json --labels $R/labels.txt --no-control
   ./bench table $O/series.json --labels $R/labels.txt --full
   python3 $R/gap.py $O/series.json
   ```

   For a quick try add `--passes 1 --filter 10cols`. Without `PDO_MYSQL_DSN`, or with `--filter`, some cases are missing: run `bench table` without `--labels` then.

7. Optional: the rest of `data/` (about 15 minutes):

   ```
   for v in base chg; do echo "## pdoobj-$v-$G"; $P/pdoobj-$v-$G/sapi/cli/php -n $R/memory.php; done
   for v in base chg; do
     USE_ZEND_ALLOC=0 valgrind --leak-check=full $P/pdoobj-$v-$G/sapi/cli/php -n $R/difftest.php > /dev/null
     USE_ZEND_ALLOC=0 valgrind --leak-check=full $P/pdoobj-$v-$G/sapi/cli/php -n $R/difftest.php "$PDO_MYSQL_DSN" root bench > /dev/null
     for m in obj assoc; do for n in 0 100; do
       valgrind --tool=callgrind --callgrind-out-file=$O/cg-$v-$m-$n.out $P/pdoobj-$v-$G/sapi/cli/php -n $R/profile.php $n $m
     done; done
   done
   callgrind_annotate --inclusive=yes $O/cg-chg-obj-100.out | head -40
   $R/mutants.sh ../php-src pdo-fetch-obj $O/difftest/pdoobj-base-$G-sqlite.txt $O
   ```

   valgrind prints its summary on stderr: expected "0 errors" and "All heap blocks were freed". Instructions per row = (PROGRAM TOTALS at N=100 − at N=0) / 100 calls / 100 rows. `mutants.sh` should print the three lines of [`data/mutants.txt`](data/mutants.txt).

8. Clean up: `docker rm -fv pdoobj-mysql; rm -rf "$O"; git -C ../php-src checkout -q master; git -C ../php-src worktree prune; git -C ../php-src branch -D pdo-fetch-obj; ./bench gc --yes 'pdoobj-*'`.

The published tables are rendered from [`series.json`](series.json) with `bench table series.json --labels labels.txt`. Back to the [report](README.md).
