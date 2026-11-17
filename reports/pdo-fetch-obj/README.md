# PDO::FETCH_OBJ rows built as a properties table

The change is on branch [`pdo-fetch-obj`](https://github.com/ArtUkrainskiy/php-src/tree/pdo-fetch-obj) of ArtUkrainskiy/php-src, also as a patch: [`pdo-fetch-obj.patch`](pdo-fetch-obj.patch). Measured and checked on 16 November 2026 on an AMD Ryzen 9 5950X with GCC 15.2 and clang 21.1.

`PDO::FETCH_OBJ` returns each row as a `stdClass` object. It's the default fetch mode of Laravel's database layer ([`Connection::$fetchMode`](https://github.com/laravel/framework/blob/12.x/src/Illuminate/Database/Connection.php)), so query builder results and Eloquent models go through it. On master, `query()` + `fetchAll(PDO::FETCH_OBJ)` of 100 rows takes 18–21% more CPU cycles in the PHP process than the same call with `FETCH_ASSOC` from SQLite. From MySQL 8.4 it's 27–32% more ([table](#results)).

The change makes `FETCH_OBJ` build the row the way `FETCH_ASSOC` builds its array, then wrap it in an object. Code that fetches with `FETCH_OBJ` gets it without any change or setting.

## Summary

- **10 or 30 columns:** 12–19% fewer CPU cycles than master per call of 100 rows, on SQLite and MySQL, through `query()`, native prepared statements and `fetch()` in a loop. With 10 columns a row takes 1,273–1,286 fewer instructions. `FETCH_OBJ | FETCH_GROUP`: 11% fewer cycles. For MySQL the percentages count only the PHP process: no server, no kernel, no wait.
- **1 or 3 columns:** 4–7% fewer cycles, except 1 column on clang: 0%, within the control.
- **Gap to `FETCH_ASSOC`:** with 10 or 30 columns, `FETCH_OBJ` now takes 2–7% more cycles than `FETCH_ASSOC`, down from 19–33%.
- **Costs:** a row with a repeated column name can take more memory, 928 bytes instead of 608 with 9 columns. `FETCH_ASSOC` and `FETCH_CLASS` move by 3% or less in cycles ([Trade-offs](#trade-offs)). Other rows take the same memory as on master.
- **Correctness:** the same output as master on GCC, clang and ASan + UBSan, from SQLite and MySQL. The php-src PDO tests pass ([Correctness checks](#correctness-checks)).
- **Not checked:** Intel, other compilers, PostgreSQL, a full application ([Not tested](#not-tested)).

## What changes and why it is faster

Before: `do_fetch()` in `ext/pdo/pdo_stmt.c` creates an empty `stdClass` and writes each column with `zend_update_property_ex()`. Each write goes through the generic property handler `zend_std_write_property()`, with its checks and a lookup. The properties table starts with 8 entries and rehashes at the 9th and 17th column.

After: `do_fetch()` collects the row into a hash table sized for the column count, with `zend_hash_update()` per column. With `FETCH_GROUP` or `FETCH_UNIQUE` the first column is the group key, so the table is one entry smaller. Then `object_and_properties_init()` makes the `stdClass` around that table.

Why the result is the same: the property handler also stores a column of a `stdClass` under its name as a string key, and a repeated name overwrites the value in place. `zend_hash_update()` does the same. `FETCH_ASSOC` uses `zend_symtable_update()`, which would turn the name `"0"` into the integer key `0`. The handler rejects names that start with `"\0"`, so rows with such a name keep the old path.

Instructions counted with callgrind, GCC 15.2, `query()` + `fetchAll()` of 100 rows × 10 columns from SQLite ([`profile.php`](profile.php), [`data/callgrind.txt`](data/callgrind.txt)):

| instructions | master, `FETCH_OBJ` | change, `FETCH_OBJ` | change, `FETCH_ASSOC` |
|---|--:|--:|--:|
| per row, whole process | 9,828 | 8,555 | 8,231 |
| writing one column, with the functions it calls | 194 | 61 | 61 |
| `zend_hash_rehash` per row | 147 | not called | not called |

## Trade-offs

- **Repeated column names:** the table is sized for all columns, but a repeated name keeps one entry. When the column count passes a power of two and the name count doesn't, the table is twice as large as on master. 9 columns with 8 names: 928 bytes per row instead of 608 ([`data/memory.txt`](data/memory.txt)). `SELECT *` over a join with a shared `id` column can do that.
- **1 column:** a row takes 41–44 fewer instructions than on master. On clang that doesn't show in cycles.
- **Other modes:** `FETCH_ASSOC` and `FETCH_CLASS` take up to 3 more instructions per row, from the extra check after the loop. Their cycles move by −3% to +2%, which I read as code placement.
- **Names starting with `"\0"`:** these rows take the old path, at the old cost plus the check.
- **`fetchObject()` and `FETCH_CLASS` into `stdClass`** still use the old path.

## Results

Change in CPU cycles per call against master (negative = fewer cycles, faster). The range over the passes, the change in instructions and the master-against-master control are in [`FULL-TABLES.md`](FULL-TABLES.md).

<!-- bench-table series.json --labels labels.txt --no-control -->
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

~: within noise, the change is no larger than the difference between master and master on the same row.
<!-- /bench-table -->

How much slower `FETCH_OBJ` is than `FETCH_ASSOC` on the same rows, in the same build: extra CPU cycles per call, in percent of the `FETCH_ASSOC` call ([`gap.py`](gap.py), [`data/gap.txt`](data/gap.txt)). From 10 columns up the change brings `FETCH_OBJ` within 2–7% of `FETCH_ASSOC`.

| rows | GCC 15.2, before → after | clang 21.1, before → after |
|---|--:|--:|
| SQLite, 1 column | +21% → +15% | +19% → +21% |
| SQLite, 3 columns | +18% → +14% | +18% → +8% |
| SQLite, 10 columns | +19% → +6% | +20% → +5% |
| SQLite, 30 columns | +20% → +3% | +20% → +2% |
| MySQL 8.4, 10 columns, `query()` | +27% → +6% | +32% → +6% |
| MySQL 8.4, 10 columns, native prepares | +29% → +7% | +33% → +7% |

The two calls are measured at different moments, so these numbers are noisier than the table above. On master the same cell differs by up to 1.3 points between measurements.

Memory held per row after `fetchAll()` of 100 rows, SQLite, GCC 15.2 ([`memory.php`](memory.php), [`data/memory.txt`](data/memory.txt)):

| `FETCH_OBJ` rows | master | change |
|---|--:|--:|
| 1, 3, 10, 30 columns | 442, 497, 928, 1,960 | same |
| 9 columns, `FETCH_GROUP` (8 properties, group arrays included) | 824 | 824 |
| 9 columns, one name twice (8 properties) | 608 | 928 |

## Correctness checks

- **Same output as master:** [`difftest.php`](difftest.php) prints everything a script can see in `FETCH_OBJ` rows, from `var_dump()` to `serialize()`. Inputs: duplicate, numeric, empty and non-ASCII column names, `FETCH_GROUP` and `FETCH_UNIQUE`, emulated and native prepares, rows changed after the fetch. Master and the change print the same on GCC, clang and ASan + UBSan, from SQLite and MySQL ([`data/difftest-md5.txt`](data/difftest-md5.txt)).
- **php-src tests** of `ext/pdo`, `ext/pdo_sqlite` and `ext/pdo_mysql`: 0 failed on GCC and on ASan + UBSan ([`tests.sh`](tests.sh), [`data/`](data/)). A new test, `pdo_sqlite_fetch_obj_column_names.phpt`, covers the column names above and passes on master too.
- **valgrind:** 0 errors, no leaks ([`data/valgrind.txt`](data/valgrind.txt)).
- **Do the checks catch bugs?** I put three bugs into the change ([`mutants.sh`](mutants.sh), [`data/mutants.txt`](data/mutants.txt)). Numeric names turned into integer keys and a repeated name keeping the first value are both caught. A broken check for `"\0"` isn't: neither driver returns such a name.

## Not tested

- Intel CPUs and other compilers.
- PostgreSQL and the other drivers.
- Column names that start with `"\0"`.
- Single-row queries such as `find()` and `first()`, opcache and JIT.
- A full application, such as a Laravel request.

## Machine and method

- AMD Ryzen 9 5950X, kernel 7.0.0-42, governor `performance`, turbo on. Measured on CPU 15, on the second CCD. CPU 15 and its sibling 31 were idle at the start. The load average was 9.9 from builds that had just finished on other cores. A desktop application was running. MySQL 8.4.11 ran in Docker on CPUs 0–7 ([`data/environment.txt`](data/environment.txt), also the SQLite version).
- GCC 15.2 and clang 21.1, builds by `bench build --slim --profile docker`: the flags of the official Docker image (`-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64`, link `-Wl,-O1 -pie`), `--enable-werror`, with `--enable-pdo --with-pdo-sqlite --with-pdo-mysql`. The harness runs `php -n` (no opcache) and disables the cycle collector during the loop.
- The number is user-space CPU cycles of the PHP process per call (`perf stat`, minus an empty loop). For MySQL it excludes the server, the kernel's socket work and the wait. A call is `query()` + `fetchAll()`, `query()` + 101 × `fetch()`, or `execute()` + `fetchAll()` of a statement prepared once with `ATTR_EMULATE_PREPARES = false`, 100 rows each ([`suite.php`](suite.php)). Tables of 1, 3, 10 and 30 columns: `id`, then text, float and integer columns in turn.
- `bench compare`: 15 alternating passes per case and compiler. Each pass runs master and the change back to back. A cell is the median of those per-pass changes. The A/A control runs master against itself, on GCC 15.2 only, at the start and at the end. Its medians are at most 1% from zero on every row. A `~` marks a change no larger than the A/A median of its row. The clang column uses the GCC control.

## Reproduce

Steps, about 55 minutes on a 16-core machine: [`REPRODUCE.md`](REPRODUCE.md). The series in this report: [`series.json`](series.json).
