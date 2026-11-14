# PDO::FETCH_OBJ rows built as a properties table

Status: prototype, not a php-src PR yet. The change is commit `3561fa5f896` on branch [`pdo-fetch-obj`](https://github.com/ArtUkrainskiy/php-src/tree/pdo-fetch-obj) of ArtUkrainskiy/php-src, one commit on master [`48e34bf6348`](https://github.com/php/php-src/commit/48e34bf6348b0e9c5818218aeb06f8121cde3e24). The same commit as a patch: [`pdo-fetch-obj.patch`](pdo-fetch-obj.patch). Measured and checked on 14 November 2026 on an AMD Ryzen 9 5950X with GCC 15.2 and clang 21.1.

`PDO::FETCH_OBJ` returns each row as a `stdClass` object. It's the default fetch mode of Laravel's database layer ([`Connection::$fetchMode`](https://github.com/laravel/framework/blob/12.x/src/Illuminate/Database/Connection.php)), so query builder results and Eloquent models go through it. On master, `query()` + `fetchAll(PDO::FETCH_OBJ)` of 100 rows takes 18–22% more CPU cycles than the same call with `FETCH_ASSOC` from SQLite, and 25–33% more from MySQL 8.4. The change makes `FETCH_OBJ` build the row the way `FETCH_ASSOC` builds its array, then wrap it in an object. The report measures that against master and compares every observable property of the rows with master.

## Summary

- **`FETCH_OBJ` with 10 or 30 columns:** 12–19% fewer CPU cycles than master, on GCC 15.2 and clang 21.1. That's SQLite with 10 and 30 columns, MySQL with 10 columns through `query()` and through native prepared statements, and `fetch()` in a loop. Instructions: 13–20% fewer, 1,275–1,288 per row with 10 columns on every driver and call.
- **`FETCH_OBJ` with 1 or 3 columns:** 2–7% fewer instructions. Cycles: 3–8% fewer. With 1 column on GCC the cycles drop more than the instructions explain (−8% against −2%): part of that row is code placement.
- **Unchanged modes:** `FETCH_ASSOC` and `FETCH_CLASS` don't change. Their instructions are within 0.2% of master and their cycles within 3%, except `FETCH_CLASS` on clang 21.1: +3% cycles with the same instructions. I didn't find the cause (see [Trade-offs](#trade-offs)).
- **What's left:** with 10 or 30 columns, `FETCH_OBJ` now takes 3–7% more cycles than `FETCH_ASSOC`, down from 19–33%. With 1 or 3 columns it's 9–18%, down from 18–21%.
- **Same output as master:** rows with duplicate, numeric, empty and non-ASCII column names, `FETCH_GROUP`, `FETCH_UNIQUE`, `ATTR_CASE`, `foreach` over a statement, MySQL buffered, unbuffered and native prepares, rows changed after the fetch. Identical on GCC, clang and ASan + UBSan, master and change. Two deliberate mistakes in the change are caught. A third one, in the fallback for names that start with `"\0"`, isn't, because neither driver returns such names. The php-src tests of `ext/pdo`, `ext/pdo_sqlite` and `ext/pdo_mysql` pass, plus a new one. Memory per row is the same as master.
- **Not checked:** Intel, other compilers, PostgreSQL, a full application (see [Not tested](#not-tested)).

## What changes and why it is faster

Before: `do_fetch()` in `ext/pdo/pdo_stmt.c` creates an empty `stdClass` and writes each column with `zend_update_property_ex()`. Every write goes through the generic property handler `zend_std_write_property()`. For `stdClass` it checks that the class declares no properties, checks the name for a leading `"\0"`, looks the name up in the object's properties table, then inserts it. The table is created at the first write with room for 8 entries. It grows and rehashes at the 9th column, and again at the 17th.

After: `do_fetch()` collects the row into a hash table sized for the column count, with `zend_hash_update()` per column. Then it creates the `stdClass` around that table with `object_and_properties_init()`. `FETCH_ASSOC` builds its array the same way, with `zend_symtable_update()` instead of `zend_hash_update()`.

Why the result is the same: for a `stdClass`, `zend_std_write_property()` stores a column as a dynamic property, keyed by the name as a string. `zend_hash_update()` does the same, while `zend_symtable_update()` would turn the name `"0"` into the integer key `0`. A later column with the same name replaces the value at the position of the first, in both. The one name the property handler rejects is a name that starts with `"\0"`, the prefix PHP uses for private and protected property names. It throws "Cannot access property starting with "\0"". The change checks the column names on each row and keeps the old path when any name starts with `"\0"`.

callgrind, GCC 15.2, `query()` + `fetchAll()` of 100 rows × 10 columns from SQLite ([`profile.php`](profile.php), [`data/callgrind.txt`](data/callgrind.txt); `query()` is included, spread over the 100 rows):

| instructions | master, `FETCH_OBJ` | change, `FETCH_OBJ` | change, `FETCH_ASSOC` |
|---|--:|--:|--:|
| per row, whole process | 9,828 | 8,553 | 8,231 |
| writing one column, inclusive | 194 (`zend_update_property_ex`) | 61 (`zend_hash_update`) | 61 (`zend_hash_update`) |
| of that, growing the properties table, per row | 147 | 0 | 0 |

`FETCH_OBJ` on the change takes 322 instructions per row more than `FETCH_ASSOC`. 199 of them are in `do_fetch()`, of which 138 are `object_and_properties_init()`. The other 123 are spent when the rows are freed.

## Trade-offs

- **1 column:** the change adds the check of the names and creates the object after the loop. That's still 43–46 fewer instructions per row than master. The check costs a few instructions per column on every row: I didn't measure it on its own.
- **`FETCH_CLASS` on clang 21.1:** +3% cycles (+1 … +4% over the passes), the same instructions. This path isn't changed, but `do_fetch()` is 144 bytes longer, so its own code and the functions after it moved. `bench why` with 15 passes ([`data/why-class-clang21.txt`](data/why-class-clang21.txt)): cycles +4%, instructions 0%, branch misses −2%, L1 instruction cache misses −12%. None of these counters explains the extra cycles. The same row on GCC 15.2 shows no change beyond the control, with MySQL on clang 21.1 it's +1%.
- **Names starting with `"\0"`:** these rows take the old path, at the old cost plus the check.
- **`fetchObject()` and `FETCH_CLASS` into `stdClass`** still use the old path. They go through the class branch of `do_fetch()`, which can run a constructor and writes declared properties.

## Machine and method

- AMD Ryzen 9 5950X, kernel 7.0.0-42, governor `performance`, turbo on. Measured on CPU 15, on the second CCD. CPU 15 and its sibling 31 were idle at the start. The load average was 7.6 because builds had just finished on other cores. A desktop application was running. MySQL 8.4.11 ran in Docker on CPUs 0–7 ([`data/environment.txt`](data/environment.txt), also the SQLite version).
- GCC 15.2 and clang 21.1, builds by `bench build --slim --profile docker`: the flags of the official Docker image (`-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64`, link `-Wl,-O1 -pie`), `--enable-werror`, with `--enable-pdo --with-pdo-sqlite --with-pdo-mysql`. The harness runs `php -n`: no opcache.
- The number is user-space CPU cycles of the PHP process per call (`perf stat`, minus an empty loop). For MySQL it excludes the server, the kernel's socket work and the wait. A call is `query()` + `fetchAll()`, `query()` + 101 × `fetch()`, or `execute()` + `fetchAll()` of a statement prepared once with `ATTR_EMULATE_PREPARES = false`, 100 rows each ([`suite.php`](suite.php)). Tables of 1, 3, 10 and 30 columns: `id`, then text, float and integer columns in turn.
- `bench compare`: 15 alternating passes per case and compiler. The change in a cell is the median over the passes of the change against master of the same pass. The A/A control (master against itself) runs on GCC 15.2 only, at the start and at the end. Its medians are at most 1% from zero on every row. Single passes reach −12% and +102%. The `~` marks in the clang column use the GCC control.

## Results

Change in CPU cycles per call relative to master (negative = fewer cycles, faster); median over the passes of the change against master of the same pass.

<!-- bench-table series.json --labels labels.txt --header -->
Machine: AMD Ryzen 9 5950X 16-Core Processor, CPU 15, kernel 7.0.0-42-generic.
Group gcc15: A = pdoobj-base-gcc15 (48e34bf6348 GCC 15.2, profile docker), B = pdoobj-chg-gcc15 (3561fa5f896 GCC 15.2, profile docker).
Group clang21: A = pdoobj-base-clang21 (48e34bf6348 clang 21.1, profile docker), B = pdoobj-chg-clang21 (3561fa5f896 clang 21.1, profile docker).
15 alternating passes per case, user-space cycles per call (perf stat, minus the empty loop), A against A at the start and the end.
Machine: turbo boost is on: thermal and frequency drift between rounds (sudo ./bench tune on).
Machine: load average is 7.6: other programs are competing for the CPU.
negative = fewer cycles (faster)

| call | master, CPU cycles per call (GCC 15.2) | GCC 15.2 | clang 21.1 |
|---|--:|--:|--:|
| `query()` + `fetchAll(PDO::FETCH_OBJ)`, SQLite, 100 rows × 1 column | 60,320 | −8% | −3% |
| same, 3 columns | 120,469 | −3% | −7% |
| same, 10 columns | 305,902 | −12% | −13% |
| same, 30 columns | 838,411 | −14% | −15% |
| same, MySQL 8.4, 10 columns | 198,276 | −15% | −19% |
| `fetch(PDO::FETCH_OBJ)` in a loop, SQLite, 100 rows × 10 columns | 312,516 | −12% | −14% |
| control, unchanged: `fetchAll(PDO::FETCH_ASSOC)`, SQLite, 1 column | 49,662 | −3% | −1% |
| control, unchanged: same, 3 columns | 101,544 | 0% ~ | 0% |
| control, unchanged: same, 10 columns | 254,416 | 0% | 0% |
| control, unchanged: same, 30 columns | 706,880 | −1% | −1% |
| control, unchanged: same, MySQL 8.4, 10 columns | 159,131 | −2% | 0% ~ |
| control, unchanged: `fetchAll(PDO::FETCH_CLASS)`, SQLite, 10 columns | 296,144 | 0% ~ | +3% layout? |
| control, unchanged: same, MySQL 8.4, 10 columns | 186,262 | 0% ~ | +1% |
| `prepare()` + `execute()` + `fetchAll(PDO::FETCH_OBJ)`, MySQL 8.4, native prepares, 10 columns | 178,657 | −17% | −19% |
| control, unchanged: same with `fetchAll(PDO::FETCH_ASSOC)` | 138,549 | 0% ~ | −1% |

Control: master against itself.

| call | master, CPU cycles per call (GCC 15.2) | A/A start | A/A end |
|---|--:|--:|--:|
| `query()` + `fetchAll(PDO::FETCH_OBJ)`, SQLite, 100 rows × 1 column | 60,186 | 0% | 0% |
| same, 3 columns | 120,490 | 0% | 0% |
| same, 10 columns | 304,548 | 0% | 0% |
| same, 30 columns | 837,772 | 0% | +1% |
| same, MySQL 8.4, 10 columns | 197,560 | 0% | 0% |
| `fetch(PDO::FETCH_OBJ)` in a loop, SQLite, 100 rows × 10 columns | 315,638 | 0% | 0% |
| control, unchanged: `fetchAll(PDO::FETCH_ASSOC)`, SQLite, 1 column | 49,758 | −1% | 0% |
| control, unchanged: same, 3 columns | 102,306 | 0% | 0% |
| control, unchanged: same, 10 columns | 253,636 | 0% | 0% |
| control, unchanged: same, 30 columns | 702,902 | 0% | 0% |
| control, unchanged: same, MySQL 8.4, 10 columns | 156,022 | +1% | 0% |
| control, unchanged: `fetchAll(PDO::FETCH_CLASS)`, SQLite, 10 columns | 295,565 | 0% | 0% |
| control, unchanged: same, MySQL 8.4, 10 columns | 184,751 | 0% | +1% |
| `prepare()` + `execute()` + `fetchAll(PDO::FETCH_OBJ)`, MySQL 8.4, native prepares, 10 columns | 177,398 | −1% | 0% |
| control, unchanged: same with `fetchAll(PDO::FETCH_ASSOC)` | 137,254 | 0% | −1% |

~: the change is not larger than the A/A control of the same row: not evidence of a difference.

layout?: in every pass the cycles changed in the same direction, by 3% or more in the median, the instructions by less than 0.5%: the work is the same, so look for the cause (code placement, branch prediction) with `bench why` before reporting the row.
<!-- /bench-table -->

Full table, with the range over the passes and the change in instructions:

<!-- bench-table series.json --labels labels.txt --full -->
| call | master, CPU cycles per call (GCC 15.2) | GCC 15.2 | clang 21.1 | instructions |
|---|--:|--:|--:|--:|
| `query()` + `fetchAll(PDO::FETCH_OBJ)`, SQLite, 100 rows × 1 column | 60,320 | −8% (−10 … +32) | −3% (−11 … +1) | −2% |
| same, 3 columns | 120,469 | −3% (−6 … +2) | −7% (−8 … −3) | −7% |
| same, 10 columns | 305,902 | −12% (−14 … −11) | −13% (−14 … −11) | −13% |
| same, 30 columns | 838,411 | −14% (−15 … −12) | −15% (−16 … −13) | −14% |
| same, MySQL 8.4, 10 columns | 198,276 | −15% (−19 … −13) | −19% (−21 … −18) | −18% |
| `fetch(PDO::FETCH_OBJ)` in a loop, SQLite, 100 rows × 10 columns | 312,516 | −12% (−14 … −10) | −14% (−15 … −13) | −13% |
| control, unchanged: `fetchAll(PDO::FETCH_ASSOC)`, SQLite, 1 column | 49,662 | −3% (−5 … −1) | −1% (−4 … +2) | 0% |
| control, unchanged: same, 3 columns | 101,544 | 0% (−2 … +2) ~ | 0% (−13 … +8) | 0% |
| control, unchanged: same, 10 columns | 254,416 | 0% (−2 … +2) | 0% (−1 … 0) | 0% |
| control, unchanged: same, 30 columns | 706,880 | −1% (−4 … +1) | −1% (−3 … +9) | 0% |
| control, unchanged: same, MySQL 8.4, 10 columns | 159,131 | −2% (−6 … +9) | 0% (−2 … +3) ~ | 0% |
| control, unchanged: `fetchAll(PDO::FETCH_CLASS)`, SQLite, 10 columns | 296,144 | 0% (−2 … +1) ~ | +3% (+1 … +4) layout? | 0% |
| control, unchanged: same, MySQL 8.4, 10 columns | 186,262 | 0% (−2 … +6) ~ | +1% (−1 … +6) | 0% |
| `prepare()` + `execute()` + `fetchAll(PDO::FETCH_OBJ)`, MySQL 8.4, native prepares, 10 columns | 178,657 | −17% (−19 … −14) | −19% (−21 … −15) | −20% |
| control, unchanged: same with `fetchAll(PDO::FETCH_ASSOC)` | 138,549 | 0% (−2 … +5) ~ | −1% (−2 … +1) | 0% |

Control: master against itself.

| call | master, CPU cycles per call (GCC 15.2) | A/A start | A/A end |
|---|--:|--:|--:|
| `query()` + `fetchAll(PDO::FETCH_OBJ)`, SQLite, 100 rows × 1 column | 60,186 | 0% (−2 … +2) | 0% (−3 … +3) |
| same, 3 columns | 120,490 | 0% (−2 … +2) | 0% (−2 … +2) |
| same, 10 columns | 304,548 | 0% (−2 … +2) | 0% (−2 … +1) |
| same, 30 columns | 837,772 | 0% (−2 … +2) | +1% (−4 … +3) |
| same, MySQL 8.4, 10 columns | 197,560 | 0% (−3 … +5) | 0% (−12 … +2) |
| `fetch(PDO::FETCH_OBJ)` in a loop, SQLite, 100 rows × 10 columns | 315,638 | 0% (−2 … +1) | 0% (−2 … +2) |
| control, unchanged: `fetchAll(PDO::FETCH_ASSOC)`, SQLite, 1 column | 49,758 | −1% (−7 … +1) | 0% (−4 … +2) |
| control, unchanged: same, 3 columns | 102,306 | 0% (−3 … +4) | 0% (−2 … +2) |
| control, unchanged: same, 10 columns | 253,636 | 0% (−2 … +2) | 0% (−3 … +5) |
| control, unchanged: same, 30 columns | 702,902 | 0% (−1 … +102) | 0% (−2 … +2) |
| control, unchanged: same, MySQL 8.4, 10 columns | 156,022 | +1% (−3 … +3) | 0% (−1 … +2) |
| control, unchanged: `fetchAll(PDO::FETCH_CLASS)`, SQLite, 10 columns | 295,565 | 0% (−2 … +2) | 0% (−2 … +2) |
| control, unchanged: same, MySQL 8.4, 10 columns | 184,751 | 0% (−3 … +2) | +1% (−2 … +5) |
| `prepare()` + `execute()` + `fetchAll(PDO::FETCH_OBJ)`, MySQL 8.4, native prepares, 10 columns | 177,398 | −1% (−4 … +3) | 0% (−3 … +5) |
| control, unchanged: same with `fetchAll(PDO::FETCH_ASSOC)` | 137,254 | 0% (−2 … +2) | −1% (−4 … +3) |

~: the change is not larger than the A/A control of the same row: not evidence of a difference.

layout?: in every pass the cycles changed in the same direction, by 3% or more in the median, the instructions by less than 0.5%: the work is the same, so look for the cause (code placement, branch prediction) with `bench why` before reporting the row.
<!-- /bench-table -->

`FETCH_OBJ` against `FETCH_ASSOC` of the same rows in the same build: the ratio of the median cycles per call ([`gap.py`](gap.py), [`data/gap.txt`](data/gap.txt)):

| table | master, GCC 15.2 | change, GCC 15.2 | master, clang 21.1 | change, clang 21.1 |
|---|--:|--:|--:|--:|
| SQLite, 1 column | +21% | +16% | +19% | +18% |
| SQLite, 3 columns | +19% | +14% | +18% | +9% |
| SQLite, 10 columns | +20% | +6% | +22% | +6% |
| SQLite, 30 columns | +19% | +3% | +20% | +3% |
| MySQL 8.4, 10 columns, `query()` | +25% | +7% | +33% | +7% |
| MySQL 8.4, 10 columns, native prepares | +29% | +7% | +31% | +7% |

Memory held per row after `fetchAll(PDO::FETCH_OBJ)` ([`memory.php`](memory.php), [`data/memory.txt`](data/memory.txt), GCC 15.2): 442 bytes with 1 column, 497 with 3, 928 with 10, 1,960 with 30, master and change alike.

## Output verification

- [`difftest.php`](difftest.php) prints everything a script can see in `FETCH_OBJ` rows: `var_dump`, `(array)` cast, `get_object_vars()`, `json_encode()`, `foreach` keys, `serialize()`. Inputs:
  - duplicate column names (`SELECT id AS a, name AS a`);
  - numeric names `"0"`, `"1"`, `"01"`, `"-1"`, `"9223372036854775808"`;
  - an empty name (SQLite only: MySQL replaces an empty alias with a generated name);
  - Cyrillic, CJK and emoji names and values, names with spaces, 41 columns, a query without rows;
  - `fetch()`, `fetchObject()`, `fetchAll()`, `FETCH_OBJ | FETCH_GROUP`, `FETCH_OBJ | FETCH_UNIQUE`, `ATTR_CASE`, `foreach` over a statement, `ATTR_DEFAULT_FETCH_MODE`;
  - MySQL with emulated and native prepares, buffered and unbuffered;
  - rows changed after the fetch: a property written, added, removed, a `clone`.

  [`difftest.sh`](difftest.sh) runs it with every build. The output is identical for master and change on GCC 15.2, clang 21.1 and ASan + UBSan (GCC, debug), from SQLite and from MySQL: [`data/difftest-md5.txt`](data/difftest-md5.txt), outputs in [`data/difftest/`](data/difftest/).
- **Mutations** ([`mutants.sh`](mutants.sh), [`data/mutants.txt`](data/mutants.txt)). Each one is applied to the change, built, and checked with `difftest.php` on SQLite and with the new php-src test:
  - [`data/mutation-1.diff`](data/mutation-1.diff), `zend_symtable_update()` instead of `zend_hash_update()`: numeric names turn into integer keys. 25 output lines differ, the test fails.
  - [`data/mutation-2.diff`](data/mutation-2.diff), `zend_hash_add()`: a repeated column name keeps the first value. 12 output lines differ, the test fails.
  - [`data/mutation-3.diff`](data/mutation-3.diff), the check for `"\0"` never matches: not caught. SQLite and MySQL can't return such a name, so the fallback path isn't run by any check.
- **New php-src test** `ext/pdo_sqlite/tests/pdo_sqlite_fetch_obj_column_names.phpt`: duplicate, numeric and empty names, writes after the fetch, `FETCH_GROUP`. It passes on master too: it pins the behaviour.
- **php-src tests** ([`tests.sh`](tests.sh)): `ext/pdo_sqlite` + `ext/pdo_mysql`, then the generic `ext/pdo` tests against SQLite and against MySQL. 0 failed on every build. Master, from the master tree: 512 + 131 + 134 passed ([`data/tests-master-gcc15.txt`](data/tests-master-gcc15.txt)). Change, from the branch tree with the new test: 513 + 131 + 134 passed, on GCC 15.2 and on ASan + UBSan ([`data/tests-change-gcc15.txt`](data/tests-change-gcc15.txt), [`data/tests-change-asan.txt`](data/tests-change-asan.txt)).
- **valgrind** memcheck on `difftest.php` with SQLite and with MySQL, `USE_ZEND_ALLOC=0`, GCC 15.2: 0 errors and all heap blocks freed, master and change ([`data/valgrind.txt`](data/valgrind.txt)).

## Not tested

- Intel CPUs and other compilers (GCC 13/14, clang 18/20). Only AMD Zen 3 with GCC 15.2 and clang 21.1.
- PostgreSQL, Oracle, Firebird, ODBC. The change is in the driver-independent `do_fetch()`. The column names come from the driver.
- A column name that starts with `"\0"`: the fallback path wasn't run (mutation 3).
- The cause of +3% for `FETCH_CLASS` on clang 21.1.
- opcache and JIT, long values, more than 100 rows per call, RSS.
- A full application (a Laravel request, Eloquent hydration) and wall time.
- 32-bit builds, ZTS builds.

## Reproduce

About 45 minutes on a 16-core machine. Run all steps in one shell, from `php-src-bench/` after step 1. Needs:
- git, Docker without sudo, Python 3, `taskset`;
- `perf` with access to hardware counters (`kernel.perf_event_paranoid` ≤ 2);
- the build tools of php-src, `libsqlite3-dev`, GCC and clang, 10 GB free per build;
- valgrind for the optional step 7;
- port 53306 free.

1. Sources (a few minutes):

   ```
   git clone https://github.com/ArtUkrainskiy/php-src-bench.git
   git clone --filter=blob:none https://github.com/php/php-src.git
   git -C php-src fetch https://github.com/ArtUkrainskiy/php-src.git pdo-fetch-obj:pdo-fetch-obj
   git -C php-src log -1 --format=%H pdo-fetch-obj    # 3561fa5f896…; if the branch moved: git -C php-src am <this patch> on 48e34bf6348
   cd php-src-bench
   R=reports/pdo-fetch-obj
   ```

2. Builds (about 3 minutes each, `ok: …/sapi/cli/php` at the end). `bench build --cc` names a build after the compiler's major version, so set `G` and `C` to yours:

   ```
   export BENCH_CONFIGURE_EXTRA='--enable-pdo --with-pdo-sqlite --with-pdo-mysql'
   ./bench build --slim --cc gcc,clang pdoobj-base 48e34bf6348
   ./bench build --slim --cc gcc,clang pdoobj-chg pdo-fetch-obj
   CC=gcc ./bench build --profile asan pdoobj-base-asan 48e34bf6348
   CC=gcc ./bench build --profile asan pdoobj-chg-asan pdo-fetch-obj
   ls ../php-builds                         # e.g. pdoobj-base-gcc15 pdoobj-chg-clang21
   G=gcc15 C=clang21 P=../php-builds
   $P/pdoobj-base-$G/sapi/cli/php -n -m | grep -i pdo    # PDO, pdo_mysql, pdo_sqlite
   ```

3. MySQL 8.4.11 on 127.0.0.1:53306 (under a minute). The builds have no OpenSSL, so the root user gets `mysql_native_password`:

   ```
   docker run -d --name pdoobj-mysql -p 127.0.0.1:53306:3306 -e MYSQL_ROOT_PASSWORD=bench -e MYSQL_DATABASE=bench \
     mysql@sha256:24989179f58856db763f418010c1169fecc944e3ec1ea7e921572d83eb070f70 --mysql-native-password=ON
   until docker exec pdoobj-mysql mysqladmin -h127.0.0.1 -uroot -pbench ping >/dev/null 2>&1; do sleep 2; done
   docker exec pdoobj-mysql mysql -uroot -pbench -e "ALTER USER root@'%' IDENTIFIED WITH mysql_native_password BY 'bench'"
   export PDO_MYSQL_DSN='mysql:host=127.0.0.1;port=53306;dbname=bench'
   ```

4. Output comparison (under a minute). Within SQLite and within MySQL every hash must be the same. Expected: SQLite `4d7c75c4af927041c61d301f8b18adbc`, MySQL `baf4723484f0afc163d6b6d60529e69a`. Equal hashes that differ from these mean another SQLite or MySQL version: compare with `$R/data/difftest/`.

   ```
   O=$(mktemp -d)
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

   Expected: 0 failed, and 512 / 131 / 134 passed on master, 513 / 131 / 134 on the change.

6. The series (about 8 minutes). Pick an idle core for `--cpu` (`./bench check --cpu N`; on a hybrid Intel CPU, a P-core):

   ```
   ./bench compare $R/suite.php $G=pdoobj-base-$G:pdoobj-chg-$G $C=pdoobj-base-$C:pdoobj-chg-$C --passes 15 --cpu 15 --out $O/series.json
   ./bench table $O/series.json --labels $R/labels.txt --full
   python3 $R/gap.py $O/series.json
   ```

   For a quick try add `--passes 1 --filter 10cols`. Without `PDO_MYSQL_DSN`, or with `--filter`, some cases are missing: run `bench table` without `--labels` then.

7. Optional: the cause analysis and the rest of `data/` (about 15 minutes):

   ```
   ./bench why $R/suite.php pdoobj-base-$C pdoobj-chg-$C --filter 'CLASS @ sqlite' --passes 15 --cpu 15 \
     --functions do_fetch,fetch_value,zend_update_property_ex,zend_std_write_property
   $P/pdoobj-base-$G/sapi/cli/php -n $R/memory.php; $P/pdoobj-chg-$G/sapi/cli/php -n $R/memory.php
   for v in base chg; do
     USE_ZEND_ALLOC=0 valgrind --leak-check=full $P/pdoobj-$v-$G/sapi/cli/php -n $R/difftest.php > /dev/null
     USE_ZEND_ALLOC=0 valgrind --leak-check=full $P/pdoobj-$v-$G/sapi/cli/php -n $R/difftest.php "$PDO_MYSQL_DSN" root bench > /dev/null
     for n in 0 100; do valgrind --tool=callgrind --callgrind-out-file=$O/cg-$v-$n.out $P/pdoobj-$v-$G/sapi/cli/php -n $R/profile.php $n obj; done
   done
   callgrind_annotate --inclusive=yes $O/cg-chg-100.out | head -40
   $R/mutants.sh ../php-src pdo-fetch-obj $O/difftest/pdoobj-base-$G-sqlite.txt
   ```

8. Clean up: `docker rm -fv pdoobj-mysql; rm -rf "$O"; git -C ../php-src checkout master; ./bench gc --yes 'pdoobj-*'`.

The series in this report: [`series.json`](series.json); `bench table series.json --labels labels.txt` renders it.
