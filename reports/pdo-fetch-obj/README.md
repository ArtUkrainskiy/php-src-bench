# PDO::FETCH_OBJ rows built as a properties table

Status: prototype, not a php-src PR yet, so no PHP release has it. The change is commit `5b322ca1e8e` on branch [`pdo-fetch-obj`](https://github.com/ArtUkrainskiy/php-src/tree/pdo-fetch-obj) of ArtUkrainskiy/php-src. It's one commit on top of php-src master [`48e34bf6348`](https://github.com/php/php-src/commit/48e34bf6348b0e9c5818218aeb06f8121cde3e24). The same commit as a patch: [`pdo-fetch-obj.patch`](pdo-fetch-obj.patch). Measured and checked on 16 November 2026 on an AMD Ryzen 9 5950X with GCC 15.2 and clang 21.1.

`PDO::FETCH_OBJ` returns each row as a `stdClass` object. It's the default fetch mode of Laravel's database layer ([`Connection::$fetchMode`](https://github.com/laravel/framework/blob/12.x/src/Illuminate/Database/Connection.php)), so query builder results and Eloquent models go through it. On master, `query()` + `fetchAll(PDO::FETCH_OBJ)` of 100 rows takes 18–21% more CPU cycles in the PHP process than the same call with `FETCH_ASSOC` from SQLite. From MySQL 8.4 it's 27–32% more ([table](#results)).

The change makes `FETCH_OBJ` build the row the way `FETCH_ASSOC` builds its array, then wrap it in an object. Once merged, code that fetches with `FETCH_OBJ` gets it without any change or setting. The report measures the change against master and checks that scripts see the same rows as on master.

## Summary

- **`FETCH_OBJ` with 10 or 30 columns:** 12–19% fewer CPU cycles than master per call of 100 rows, on GCC 15.2 and clang 21.1. Measured on SQLite with 10 and 30 columns, on MySQL with 10 columns through `query()` and through native prepared statements, and with `fetch()` in a loop. Without `FETCH_GROUP`, with 10 columns, every driver and call saves 1,273–1,286 instructions and 291–442 cycles per row. For MySQL the percentages count only the PHP process: no server, no kernel, no wait. `FETCH_OBJ | FETCH_GROUP` with 10 columns: 11% fewer cycles.
- **`FETCH_OBJ` with 1 or 3 columns:** 2–7% fewer instructions. Cycles: 4–7% fewer, except 1 column on clang, which is within the control. With 1 column on GCC the cycles drop more than the instructions (−7% against −2%). I think part of that is code placement. On the same build, `FETCH_ASSOC` with 1 column also takes 3% fewer cycles, and its source isn't changed.
- **Other modes:** the change doesn't touch the code of `FETCH_ASSOC` and `FETCH_CLASS`, but they run through the same `do_fetch()`. They take at most 3 more instructions per row, less than 0.2%. Their cycles move by 3% or less (see [Trade-offs](#trade-offs)).
- **Gap to `FETCH_ASSOC`:** with 10 or 30 columns, `FETCH_OBJ` now takes 2–7% more cycles than `FETCH_ASSOC`, down from 19–33%. With 1 or 3 columns it's 8–21%, down from 18–21%.
- **Same rows as master:** master and the change print the same output on GCC 15.2, clang 21.1 and an ASan + UBSan build, from SQLite and MySQL. The inputs include duplicate, numeric, empty and non-ASCII column names, `FETCH_GROUP`, `FETCH_UNIQUE` and rows changed after the fetch ([Correctness checks](#correctness-checks)).
- **Memory:** the same bytes per row as master, also with `FETCH_GROUP`. A row with a repeated column name can take more: 928 bytes instead of 608 with 9 columns and 8 names (see [Trade-offs](#trade-offs)).
- **Checks:** I put three bugs into the change on purpose, to see whether the checks catch them. They catch two. The third is in the path for names that start with `"\0"`, which neither driver returns. The php-src tests of `ext/pdo`, `ext/pdo_sqlite` and `ext/pdo_mysql` pass, plus a new one.
- **Not checked:** Intel, other compilers, PostgreSQL, a full application (see [Not tested](#not-tested)).

## What changes and why it is faster

Before: `do_fetch()` in `ext/pdo/pdo_stmt.c` creates an empty `stdClass` and writes each column with `zend_update_property_ex()`. Every write goes through the generic property handler `zend_std_write_property()`. For `stdClass` it checks that the class declares no properties, checks the name for a leading `"\0"`, looks the name up in the object's properties table, then inserts it. The table is created at the first write with room for 8 entries. It grows and rehashes at the 9th column, and again at the 17th.

After: `do_fetch()` collects the row into a hash table sized for the column count, with `zend_hash_update()` per column. With `FETCH_GROUP` or `FETCH_UNIQUE` the first column is the group key, so the table is one entry smaller. Then `do_fetch()` creates the `stdClass` around that table with `object_and_properties_init()`. Without a group key, `FETCH_ASSOC` builds its array the same way, but with `zend_symtable_update()`.

Why the result is the same: for a `stdClass`, `zend_std_write_property()` stores a column as a dynamic property, keyed by the name as a string. `zend_hash_update()` does the same. `zend_symtable_update()` would turn the name `"0"` into the integer key `0`, which is why `FETCH_OBJ` doesn't use it. On the old and the new path, a later column with the same name overwrites the value and keeps the first one's position. The one name the property handler rejects is a name that starts with `"\0"`, the prefix PHP uses for private and protected property names. It throws "Cannot access property starting with "\0"". The change checks the column names on each row and keeps the old path when any name starts with `"\0"`.

Instructions counted with callgrind, GCC 15.2, `query()` + `fetchAll()` of 100 rows × 10 columns from SQLite ([`profile.php`](profile.php), [`data/callgrind.txt`](data/callgrind.txt)). The cost of `query()` is divided over the 100 rows.

| instructions | master, `FETCH_OBJ` | change, `FETCH_OBJ` | change, `FETCH_ASSOC` |
|---|--:|--:|--:|
| per row, whole process | 9,828 | 8,555 | 8,231 |
| writing one column, with the functions it calls | 194 (`zend_update_property_ex`) | 61 (`zend_hash_update`) | 61 (`zend_hash_update`) |
| `zend_hash_rehash` when the table grows, per row | 147 | not called | not called |

`FETCH_OBJ` on the change takes 324 instructions per row more than `FETCH_ASSOC`. 201 of them are in `do_fetch()`, of which 138 are `object_and_properties_init()`. The other 123 are spent when the rows are freed.

## Trade-offs

- **1 column:** the change adds the name check and creates the object after the loop. Even so, a row takes 41–44 fewer instructions than on master. On clang that doesn't show in cycles: 0%, within the control. The name check runs on every row. I didn't measure it on its own.
- **Repeated column names:** the table is sized for all columns, but a repeated name keeps one entry. When the column count passes a power of two and the name count doesn't, the table is twice as large as on master. 9 columns with 8 names: 928 bytes per row instead of 608 ([`data/memory.txt`](data/memory.txt)). `SELECT *` over a join with a shared `id` column can do that. The number of names isn't known before the row is built, so the change doesn't size for it.
- **Other modes:** `FETCH_ASSOC` and `FETCH_CLASS` take up to 3 more instructions per row, from the extra check after the loop in `do_fetch()`. Their cycles move by −3% to +2%. The same rows moved differently with the earlier commit of this change, built from the same source except the `FETCH_GROUP` sizing: `FETCH_CLASS` on clang was +3% there and is −1% here, at the same instructions ([`data/series-3561fa5f896.json`](data/series-3561fa5f896.json)). I read that as code placement, since `do_fetch()` grew and moved what follows it. On this commit `bench why` shows the same cycles and instructions for that row ([`data/why-class-clang21.txt`](data/why-class-clang21.txt)). I didn't prove the cause.
- **Names starting with `"\0"`:** these rows take the old path, at the old cost plus the check.
- **`fetchObject()` and `FETCH_CLASS` into `stdClass`** still use the old path. They go through the class branch of `do_fetch()`, which can run a constructor and writes declared properties.

## Machine and method

- AMD Ryzen 9 5950X, kernel 7.0.0-42, governor `performance`, turbo on. Measured on CPU 15, on the second CCD. CPU 15 and its sibling 31 were idle at the start. The load average was 9.9 because builds had just finished on other cores. A desktop application was running. MySQL 8.4.11 ran in Docker on CPUs 0–7 ([`data/environment.txt`](data/environment.txt), also the SQLite version).
- The measured builds were made from commit `5741d870de3`. The published commit `5b322ca1e8e` only adds the measured numbers to its message: both have the tree `67e1e07d03f`.
- GCC 15.2 and clang 21.1, builds by `bench build --slim --profile docker`: the flags of the official Docker image (`-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64`, link `-Wl,-O1 -pie`), `--enable-werror`, with `--enable-pdo --with-pdo-sqlite --with-pdo-mysql`. The harness runs `php -n` (no opcache) and disables the cycle collector during the loop.
- The number is user-space CPU cycles of the PHP process per call (`perf stat`, minus an empty loop). For MySQL it excludes the server, the kernel's socket work and the wait. A call is `query()` + `fetchAll()`, `query()` + 101 × `fetch()`, or `execute()` + `fetchAll()` of a statement prepared once with `ATTR_EMULATE_PREPARES = false`, 100 rows each ([`suite.php`](suite.php)). Tables of 1, 3, 10 and 30 columns: `id`, then text, float and integer columns in turn.
- `bench compare`: 15 alternating passes per case and compiler. Each pass runs master and the change back to back. A cell is the median of those per-pass changes. The A/A control runs master against itself, on GCC 15.2 only, at the start and at the end. Its medians are at most 1% from zero on every row. Single A/A passes reach −34% (one outlier, `fetch()` in a loop) and +15% (`FETCH_OBJ` with 1 column). A `~` marks a change no larger than the A/A median of its row. The clang column uses the GCC control.

## Results

Change in CPU cycles per call against master (negative = fewer cycles, faster).

<!-- bench-table series.json --labels labels.txt --header -->
Machine: AMD Ryzen 9 5950X 16-Core Processor, CPU 15, kernel 7.0.0-42-generic.
Group gcc15: A = pdoobj-base-gcc15 (48e34bf6348 GCC 15.2, profile docker), B = pdoobj-fix-gcc15 (5741d870de3 GCC 15.2, profile docker).
Group clang21: A = pdoobj-base-clang21 (48e34bf6348 clang 21.1, profile docker), B = pdoobj-fix-clang21 (5741d870de3 clang 21.1, profile docker).
15 alternating passes per case, user-space cycles per call (perf stat, minus the empty loop), A against A at the start and the end.
Machine: turbo boost is on: thermal and frequency drift between rounds (sudo ./bench tune on).
Machine: load average is 9.9: other programs are competing for the CPU.
negative = fewer cycles (faster)

| call | master, CPU cycles per call (GCC 15.2) | GCC 15.2 | clang 21.1 |
|---|--:|--:|--:|
| `query()` + `fetchAll(PDO::FETCH_OBJ)`, SQLite, 100 rows × 1 column | 59,800 | −7% | 0% ~ |
| same, 3 columns | 119,979 | −4% | −7% |
| same, 10 columns | 304,032 | −12% | −13% |
| same, 30 columns | 841,453 | −14% | −14% |
| same, MySQL 8.4, 10 columns | 199,072 | −16% | −19% |
| `query()` + `fetchAll(PDO::FETCH_OBJ \| PDO::FETCH_GROUP)`, SQLite, 100 rows × 10 columns | 321,583 | −11% | −11% |
| `query()` + `fetch(PDO::FETCH_OBJ)` in a loop, SQLite, 100 rows × 10 columns | 313,346 | −12% | −14% |
| control, code not touched: `fetchAll(PDO::FETCH_ASSOC)`, SQLite, 1 column | 49,580 | −3% | −2% |
| control, code not touched: same, 3 columns | 101,743 | −1% | +2% |
| control, code not touched: same, 10 columns | 254,914 | 0% | 0% ~ |
| control, code not touched: same, 30 columns | 703,745 | 0% | 0% ~ |
| control, code not touched: same, MySQL 8.4, 10 columns | 157,031 | −1% ~ | +1% |
| control, code not touched: `fetchAll(PDO::FETCH_CLASS)`, SQLite, 10 columns | 292,877 | +1% | −1% |
| control, code not touched: same, MySQL 8.4, 10 columns | 184,829 | +1% | 0% ~ |
| `execute()` + `fetchAll(PDO::FETCH_OBJ)` of a prepared statement, MySQL 8.4, native prepares, 10 columns | 178,149 | −16% | −19% |
| control, code not touched: same with `fetchAll(PDO::FETCH_ASSOC)` | 138,391 | 0% ~ | 0% ~ |

Control: master against itself.

| call | master, CPU cycles per call (GCC 15.2) | A/A start | A/A end |
|---|--:|--:|--:|
| `query()` + `fetchAll(PDO::FETCH_OBJ)`, SQLite, 100 rows × 1 column | 60,052 | 0% | 0% |
| same, 3 columns | 119,987 | 0% | 0% |
| same, 10 columns | 304,253 | 0% | 0% |
| same, 30 columns | 837,213 | 0% | +1% |
| same, MySQL 8.4, 10 columns | 196,408 | +1% | −1% |
| `query()` + `fetchAll(PDO::FETCH_OBJ \| PDO::FETCH_GROUP)`, SQLite, 100 rows × 10 columns | 319,995 | 0% | 0% |
| `query()` + `fetch(PDO::FETCH_OBJ)` in a loop, SQLite, 100 rows × 10 columns | 313,795 | 0% | +1% |
| control, code not touched: `fetchAll(PDO::FETCH_ASSOC)`, SQLite, 1 column | 49,362 | 0% | 0% |
| control, code not touched: same, 3 columns | 101,357 | 0% | 0% |
| control, code not touched: same, 10 columns | 254,037 | 0% | 0% |
| control, code not touched: same, 30 columns | 701,896 | 0% | 0% |
| control, code not touched: same, MySQL 8.4, 10 columns | 155,549 | +1% | 0% |
| control, code not touched: `fetchAll(PDO::FETCH_CLASS)`, SQLite, 10 columns | 293,233 | 0% | 0% |
| control, code not touched: same, MySQL 8.4, 10 columns | 184,859 | 0% | −1% |
| `execute()` + `fetchAll(PDO::FETCH_OBJ)` of a prepared statement, MySQL 8.4, native prepares, 10 columns | 177,389 | 0% | −1% |
| control, code not touched: same with `fetchAll(PDO::FETCH_ASSOC)` | 137,482 | 0% | −1% |

~: the change is not larger than the A/A control of the same row: not evidence of a difference.
<!-- /bench-table -->

Full table, with the range over the passes and the change in instructions on both compilers:

<!-- bench-table series.json --labels labels.txt --full -->
| call | master, CPU cycles per call (GCC 15.2) | GCC 15.2 | clang 21.1 | instructions |
|---|--:|--:|--:|--:|
| `query()` + `fetchAll(PDO::FETCH_OBJ)`, SQLite, 100 rows × 1 column | 59,800 | −7% (−10 … +7) | 0% (−7 … +2) ~ | −2% |
| same, 3 columns | 119,979 | −4% (−6 … −1) | −7% (−9 … −4) | −7% |
| same, 10 columns | 304,032 | −12% (−13 … −10) | −13% (−18 … −11) | −13% |
| same, 30 columns | 841,453 | −14% (−16 … −12) | −14% (−17 … −11) | −14% |
| same, MySQL 8.4, 10 columns | 199,072 | −16% (−18 … −13) | −19% (−22 … −18) | −18% |
| `query()` + `fetchAll(PDO::FETCH_OBJ \| PDO::FETCH_GROUP)`, SQLite, 100 rows × 10 columns | 321,583 | −11% (−12 … −9) | −11% (−12 … −9) | −11% |
| `query()` + `fetch(PDO::FETCH_OBJ)` in a loop, SQLite, 100 rows × 10 columns | 313,346 | −12% (−13 … −11) | −14% (−17 … −10) | −13% |
| control, code not touched: `fetchAll(PDO::FETCH_ASSOC)`, SQLite, 1 column | 49,580 | −3% (−4 … 0) | −2% (−4 … 0) | 0% |
| control, code not touched: same, 3 columns | 101,743 | −1% (−1 … +2) | +2% (0 … +4) | 0% |
| control, code not touched: same, 10 columns | 254,914 | 0% (−1 … +1) | 0% (−16 … +2) ~ | 0% |
| control, code not touched: same, 30 columns | 703,745 | 0% (−2 … +1) | 0% (−2 … +2) ~ | 0% |
| control, code not touched: same, MySQL 8.4, 10 columns | 157,031 | −1% (−3 … +4) ~ | +1% (−4 … +4) | 0% |
| control, code not touched: `fetchAll(PDO::FETCH_CLASS)`, SQLite, 10 columns | 292,877 | +1% (0 … +12) | −1% (−2 … +2) | 0% |
| control, code not touched: same, MySQL 8.4, 10 columns | 184,829 | +1% (−3 … +5) | 0% (−2 … +7) ~ | 0% |
| `execute()` + `fetchAll(PDO::FETCH_OBJ)` of a prepared statement, MySQL 8.4, native prepares, 10 columns | 178,149 | −16% (−18 … −15) | −19% (−22 … −15) | −20% |
| control, code not touched: same with `fetchAll(PDO::FETCH_ASSOC)` | 138,391 | 0% (−3 … +3) ~ | 0% (−2 … +5) ~ | 0% |

Control: master against itself.

| call | master, CPU cycles per call (GCC 15.2) | A/A start | A/A end |
|---|--:|--:|--:|
| `query()` + `fetchAll(PDO::FETCH_OBJ)`, SQLite, 100 rows × 1 column | 60,052 | 0% (−1 … +15) | 0% (−2 … +2) |
| same, 3 columns | 119,987 | 0% (−2 … +2) | 0% (−14 … +3) |
| same, 10 columns | 304,253 | 0% (−12 … +3) | 0% (−2 … +2) |
| same, 30 columns | 837,213 | 0% (−8 … +1) | +1% (−2 … +2) |
| same, MySQL 8.4, 10 columns | 196,408 | +1% (−2 … +3) | −1% (−2 … +3) |
| `query()` + `fetchAll(PDO::FETCH_OBJ \| PDO::FETCH_GROUP)`, SQLite, 100 rows × 10 columns | 319,995 | 0% (−2 … +4) | 0% (−2 … +9) |
| `query()` + `fetch(PDO::FETCH_OBJ)` in a loop, SQLite, 100 rows × 10 columns | 313,795 | 0% (−1 … +2) | +1% (−34 … +2) |
| control, code not touched: `fetchAll(PDO::FETCH_ASSOC)`, SQLite, 1 column | 49,362 | 0% (−3 … +3) | 0% (−3 … +3) |
| control, code not touched: same, 3 columns | 101,357 | 0% (−2 … +3) | 0% (−1 … +5) |
| control, code not touched: same, 10 columns | 254,037 | 0% (−2 … +2) | 0% (−5 … +2) |
| control, code not touched: same, 30 columns | 701,896 | 0% (−3 … +3) | 0% (−1 … +2) |
| control, code not touched: same, MySQL 8.4, 10 columns | 155,549 | +1% (−2 … +2) | 0% (−1 … +4) |
| control, code not touched: `fetchAll(PDO::FETCH_CLASS)`, SQLite, 10 columns | 293,233 | 0% (−1 … +2) | 0% (−2 … +3) |
| control, code not touched: same, MySQL 8.4, 10 columns | 184,859 | 0% (−2 … +4) | −1% (−13 … +3) |
| `execute()` + `fetchAll(PDO::FETCH_OBJ)` of a prepared statement, MySQL 8.4, native prepares, 10 columns | 177,389 | 0% (−2 … +2) | −1% (−2 … +2) |
| control, code not touched: same with `fetchAll(PDO::FETCH_ASSOC)` | 137,482 | 0% (−3 … +2) | −1% (−3 … +2) |

~: the change is not larger than the A/A control of the same row: not evidence of a difference.
<!-- /bench-table -->

How many more cycles `FETCH_OBJ` takes than `FETCH_ASSOC` for the same rows in the same build, from the median cycles per call ([`gap.py`](gap.py), [`data/gap.txt`](data/gap.txt)). The two cases run at different moments of the series. On master the five samples of the series vary by up to 1.3 points.

| table | master, GCC 15.2 | change, GCC 15.2 | master, clang 21.1 | change, clang 21.1 |
|---|--:|--:|--:|--:|
| SQLite, 1 column | +21% | +15% | +19% | +21% |
| SQLite, 3 columns | +18% | +14% | +18% | +8% |
| SQLite, 10 columns | +19% | +6% | +20% | +5% |
| SQLite, 30 columns | +20% | +3% | +20% | +2% |
| MySQL 8.4, 10 columns, `query()` | +27% | +6% | +32% | +6% |
| MySQL 8.4, 10 columns, native prepares | +29% | +7% | +33% | +7% |

Memory held per row after `fetchAll()` of 100 rows, SQLite, GCC 15.2 ([`memory.php`](memory.php), [`data/memory.txt`](data/memory.txt)). The earlier commit `3561fa5f896` sized the table for all columns also with `FETCH_GROUP`:

| `FETCH_OBJ` rows | master | change | earlier commit |
|---|--:|--:|--:|
| 1, 3, 10, 30 columns | 442, 497, 928, 1,960 | same | same |
| 9 columns, `FETCH_GROUP` (8 properties, group arrays included) | 824 | 824 | 1,144 |
| 9 columns, one name twice (8 properties) | 608 | 928 | 928 |

## Correctness checks

- [`difftest.php`](difftest.php) prints everything a script can see in `FETCH_OBJ` rows: `var_dump`, `(array)` cast, `get_object_vars()`, `json_encode()`, `foreach` keys, `serialize()`. Inputs:
  - duplicate column names (`SELECT id AS a, name AS a`);
  - numeric names `"0"`, `"1"`, `"01"`, `"-1"`, `"9223372036854775808"`;
  - an empty name, SQLite only. MySQL replaces an empty alias with a generated name;
  - Cyrillic, CJK and emoji names and values, names with spaces, 41 columns, a query without rows;
  - `fetch()`, `fetchObject()`, `fetchAll()`, `FETCH_OBJ | FETCH_GROUP`, `FETCH_OBJ | FETCH_UNIQUE`, `ATTR_CASE`, `foreach` over a statement, `ATTR_DEFAULT_FETCH_MODE`;
  - MySQL with emulated and native prepares, buffered and unbuffered;
  - rows changed after the fetch: a property written, added, removed, a `clone`.

  [`difftest.sh`](difftest.sh) runs it with every build. The output is identical for master and change on GCC 15.2, clang 21.1 and ASan + UBSan (GCC, debug), from SQLite and from MySQL: [`data/difftest-md5.txt`](data/difftest-md5.txt), outputs in [`data/difftest/`](data/difftest/).
- **Bugs put in on purpose (mutations)** ([`mutants.sh`](mutants.sh), [`data/mutants.txt`](data/mutants.txt)). Each one is applied to the change, built, and checked with `difftest.php` on SQLite and with the new php-src test:
  - [`data/mutation-1.diff`](data/mutation-1.diff), `zend_symtable_update()` instead of `zend_hash_update()`: numeric names turn into integer keys. 25 output lines differ, the test fails.
  - [`data/mutation-2.diff`](data/mutation-2.diff), `zend_hash_add()`: a repeated column name keeps the first value. 12 output lines differ, the test fails.
  - [`data/mutation-3.diff`](data/mutation-3.diff), the check for `"\0"` never matches: not caught. SQLite and MySQL can't return such a name, so the fallback path isn't run by any check.
- **New php-src test** `ext/pdo_sqlite/tests/pdo_sqlite_fetch_obj_column_names.phpt`: duplicate, numeric and empty names, writes after the fetch, `FETCH_GROUP`. It passes on master and on the change ([`data/new-test.txt`](data/new-test.txt)), so it pins the behaviour.
- **php-src tests** ([`tests.sh`](tests.sh)): `ext/pdo_sqlite` + `ext/pdo_mysql`, then the generic `ext/pdo` tests against SQLite and against MySQL. 0 failed on every build. Master, from the master tree: 512 passed in `ext/pdo_sqlite` and `ext/pdo_mysql`, 131 in `ext/pdo` on SQLite, 134 in `ext/pdo` on MySQL ([`data/tests-master-gcc15.txt`](data/tests-master-gcc15.txt)). The change, from the branch tree with the new test: 513, 131 and 134, on GCC 15.2 and on ASan + UBSan ([`data/tests-change-gcc15.txt`](data/tests-change-gcc15.txt), [`data/tests-change-asan.txt`](data/tests-change-asan.txt)).
- **valgrind** memcheck on `difftest.php` with SQLite and with MySQL, `USE_ZEND_ALLOC=0`, GCC 15.2: 0 errors and all heap blocks freed, master and change ([`data/valgrind.txt`](data/valgrind.txt)).

## Not tested

- Intel CPUs and other compilers (GCC 13/14, clang 18/20). Only AMD Zen 3 with GCC 15.2 and clang 21.1.
- PostgreSQL, Oracle, Firebird, ODBC. The change is in the driver-independent `do_fetch()`. The column names come from the driver.
- A column name that starts with `"\0"`: the fallback path wasn't run (mutation 3).
- The cause of +3% for `FETCH_CLASS` on clang 21.1 with the earlier commit `3561fa5f896`.
- Single-row queries such as `find()` and `first()`, where `query()` takes a larger share of the call. Also more than 100 rows per call, long values, opcache and JIT, RSS.
- The cycles of the other fetch modes that go through `do_fetch()`: `FETCH_BOTH` (the PDO default), `FETCH_NUM`, `FETCH_NAMED`, `FETCH_COLUMN`, `FETCH_FUNC`. Their output is covered by the php-src tests.
- A full application (a Laravel request, Eloquent hydration) and wall time.
- 32-bit builds, ZTS builds.

## Reproduce

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
   git -C php-src log -1 --format=%H pdo-fetch-obj    # expected: 5b322ca1e8e01ae0b05944b7f261db9077bb2436
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

6. The series (about 8 minutes) on `$CPU`. The first command prints the short table of this report, the second the full one:

   ```
   ./bench compare $R/suite.php $G=pdoobj-base-$G:pdoobj-chg-$G $C=pdoobj-base-$C:pdoobj-chg-$C --passes 15 --cpu $CPU --out $O/series.json
   ./bench table $O/series.json --labels $R/labels.txt --header
   ./bench table $O/series.json --labels $R/labels.txt --full
   python3 $R/gap.py $O/series.json
   ```

   For a quick try add `--passes 1 --filter 10cols`. Without `PDO_MYSQL_DSN`, or with `--filter`, some cases are missing: run `bench table` without `--labels` then.

7. Optional: the cause analysis and the rest of `data/` (about 15 minutes):

   ```
   ./bench why $R/suite.php pdoobj-base-$C pdoobj-chg-$C --filter 'CLASS @ sqlite' --passes 15 --cpu $CPU \
     --functions do_fetch,fetch_value,zend_update_property_ex,zend_std_write_property
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

The series in this report: [`series.json`](series.json); `bench table series.json --labels labels.txt` renders it.
