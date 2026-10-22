# pdo_pgsql integer columns without strtoll() (php-src PR #24385)

Review material for [php/php-src#24385](https://github.com/php/php-src/pull/24385) by brainexe, "ext/pdo_pgsql: Parse integer columns inline". PR head [`3e479d70ffa`](https://github.com/php/php-src/pull/24385/commits/3e479d70ffa1d21d59273caafed0af13b4c6d404), merged onto master [`c242f17cf4b`](https://github.com/php/php-src/commit/c242f17cf4b) without conflicts. Measured and checked on 22 October 2026 on an Intel i7-13700H, PostgreSQL 17 in Docker on the same machine.

`pgsql_stmt_get_col()` converts `int2`, `int4` and (on 64-bit builds) `int8` columns with `ZEND_HANDLE_NUMERIC_STR()`, the parser of numeric array keys, and keeps `ZEND_ATOL()` (`atoll()`, which is `strtoll()` in glibc) for anything it rejects. The report measures `execute()` plus `fetchAll()` of 10,000 rows from a prepared statement and compares every fetched value with master. The numbers are user-space CPU cycles of the PHP process: they include libpq reading the result and PDO building the arrays, not the time of the PostgreSQL server. Wall time was not measured. The builds of the PR are named after `a8dc310c5cc`, the PR head merged onto `c242f17cf4b` by `bench pr`; that merge commit is not on GitHub.

## Summary

- **Integer columns:** 9–15% fewer cycles for 4 `int2` or `int4` columns, 12–20% for 4 short `int8` (1–6 digits), 14–26% for 4 `int8` of 15–19 digits, on all four compilers. Instructions: 13–23% fewer.
- **Mixed and text columns:** 2 integer + 9 text columns take 0–5% fewer cycles, 3% fewer instructions. 4 text columns: no difference from master (0% instructions, cycles within the master-against-master control).
- **Same output as master:** every `int2` value, `int4` and `int8` around every power of ten and at their limits, 300,000 random `int8`, NULLs, with native and with emulated prepares: identical with GCC 13.3 and clang 20.1. A deliberate off-by-one for 19-character values is caught.
- **Tests:** `ext/pdo` and `ext/pdo_pgsql` give the same result on master and on the PR (214 passed, 1 expected fail, 0 failed). The new test passes on master too, as it should: it pins the limits.
- **Not checked:** AMD, 32-bit builds, ASan/UBSan, wall time.

## Results

Change in CPU cycles per call relative to A (negative = fewer cycles, faster); median over the passes of B against A of the same pass.

<!-- bench-table series.json --labels labels.txt --header -->
Machine: 13th Gen Intel(R) Core(TM) i7-13700H, CPU 2, kernel 7.0.0-38-generic.
Group gcc13: A = pr24385-base-gcc13 (c242f17cf4b GCC 13.3, profile docker), B = pr24385-head-gcc13 (a8dc310c5cc GCC 13.3, profile docker).
Group gcc14: A = pr24385-base-gcc14 (c242f17cf4b GCC 14.2, profile docker), B = pr24385-head-gcc14 (a8dc310c5cc GCC 14.2, profile docker).
Group clang18: A = pr24385-base-clang18 (c242f17cf4b clang 18.1, profile docker), B = pr24385-head-clang18 (a8dc310c5cc clang 18.1, profile docker).
Group clang20: A = pr24385-base-clang20 (c242f17cf4b clang 20.1, profile docker), B = pr24385-head-clang20 (a8dc310c5cc clang 20.1, profile docker).
5 alternating passes per case, user-space cycles per call (perf stat, minus the empty loop), A against A at the start and the end.
Machine: CPU governor is 'powersave': frequency scaling adds noise (sudo ./bench tune on).
Machine: turbo boost is on: thermal and frequency drift between rounds (sudo ./bench tune on).
Machine: load average is 4.5: other programs are competing for the CPU.
Machine: CPU 2 is 36% busy with other processes: timings will be noisy (wait for it to finish).
negative = fewer cycles (faster)

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 |
|---|--:|--:|--:|--:|--:|
| `execute()` + `fetchAll(PDO::FETCH_NUM)`, 10,000 rows × 4 `int2` | 7,430,183 | −11% | −10% | −12% | −12% |
| same, 4 `int4` of 1–3 digits | 5,971,762 | −11% | −12% | −12% | −13% |
| same, 4 `int4` over the full range | 8,352,227 | −13% | −10% | −15% | −13% |
| same, 4 `int8` of 1–6 digits (id, counters) | 6,039,232 | −14% | −12% | −15% | −20% |
| same, 4 `int8` of 15–19 digits | 9,271,294 | −14% | −19% | −23% | −26% |
| same, 2 `int4` + 9 `text` | 15,962,277 | −1% ~ | −4% | −5% | −2% |
| same, 4 `text` (no integers) | 6,233,117 | −1% ~ | +1% ~ | −2% ~ | +2% ~ |
| same with `fetchAll(PDO::FETCH_ASSOC)`, 4 `int4` over the full range | 8,644,055 | −9% | −12% | −12% | −12% |
| same with `fetchAll(PDO::FETCH_ASSOC)`, 2 `int4` + 9 `text` | 17,128,523 | −1% ~ | 0% ~ | −4% | 0% ~ |

Control: master against itself.

| call | master, CPU cycles per call (GCC 13.3) | A/A start | A/A end |
|---|--:|--:|--:|
| `execute()` + `fetchAll(PDO::FETCH_NUM)`, 10,000 rows × 4 `int2` | 7,994,588 | −4% | −1% |
| same, 4 `int4` of 1–3 digits | 6,079,467 | +3% | +1% |
| same, 4 `int4` over the full range | 8,219,474 | +2% | +1% |
| same, 4 `int8` of 1–6 digits (id, counters) | 6,047,442 | +1% | +1% |
| same, 4 `int8` of 15–19 digits | 9,282,520 | +1% | −1% |
| same, 2 `int4` + 9 `text` | 16,414,312 | 0% | +2% |
| same, 4 `text` (no integers) | 6,359,720 | +2% | −4% |
| same with `fetchAll(PDO::FETCH_ASSOC)`, 4 `int4` over the full range | 9,072,293 | 0% | 0% |
| same with `fetchAll(PDO::FETCH_ASSOC)`, 2 `int4` + 9 `text` | 17,749,719 | +2% | 0% |

~: the change is not larger than the A/A control of the same row: not evidence of a difference.
<!-- /bench-table -->

Other programs loaded the machine during the series (CPU 2 was 36% busy with them), so the ranges over the passes are wide. The change in instructions, which that load does not affect, backs every integer row. Full table, with the range over the passes and the change in instructions:

<!-- bench-table series.json --labels labels.txt --full -->
| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | instructions |
|---|--:|--:|--:|--:|--:|--:|
| `execute()` + `fetchAll(PDO::FETCH_NUM)`, 10,000 rows × 4 `int2` | 7,430,183 | −11% (−13 … −3) | −10% (−14 … −9) | −12% (−16 … −9) | −12% (−13 … −9) | −14% … −13% |
| same, 4 `int4` of 1–3 digits | 5,971,762 | −11% (−13 … −9) | −12% (−14 … −8) | −12% (−16 … −5) | −13% (−13 … −11) | −13% |
| same, 4 `int4` over the full range | 8,352,227 | −13% (−16 … −9) | −10% (−19 … −10) | −15% (−20 … −12) | −13% (−14 … −11) | −18% … −16% |
| same, 4 `int8` of 1–6 digits (id, counters) | 6,039,232 | −14% (−15 … −7) | −12% (−14 … −10) | −15% (−24 … +8) | −20% (−26 … −14) | −14% … −13% |
| same, 4 `int8` of 15–19 digits | 9,271,294 | −14% (−18 … −13) | −19% (−23 … −15) | −23% (−27 … −22) | −26% (−38 … −18) | −23% … −19% |
| same, 2 `int4` + 9 `text` | 15,962,277 | −1% (−4 … +3) ~ | −4% (−6 … +2) | −5% (−8 … −4) | −2% (−4 … +1) | −3% |
| same, 4 `text` (no integers) | 6,233,117 | −1% (−3 … +3) ~ | +1% (−1 … +63) ~ | −2% (−5 … +10) ~ | +2% (0 … +5) ~ | 0% |
| same with `fetchAll(PDO::FETCH_ASSOC)`, 4 `int4` over the full range | 8,644,055 | −9% (−11 … −7) | −12% (−19 … −6) | −12% (−17 … −7) | −12% (−15 … −10) | −17% … −15% |
| same with `fetchAll(PDO::FETCH_ASSOC)`, 2 `int4` + 9 `text` | 17,128,523 | −1% (−3 … +2) ~ | 0% (−12 … +9) ~ | −4% (−5 … −2) | 0% (−2 … +4) ~ | −3% |

Control: master against itself.

| call | master, CPU cycles per call (GCC 13.3) | A/A start | A/A end |
|---|--:|--:|--:|
| `execute()` + `fetchAll(PDO::FETCH_NUM)`, 10,000 rows × 4 `int2` | 7,994,588 | −4% (−13 … +8) | −1% (−3 … +7) |
| same, 4 `int4` of 1–3 digits | 6,079,467 | +3% (0 … +19) | +1% (−2 … +22) |
| same, 4 `int4` over the full range | 8,219,474 | +2% (−1 … +4) | +1% (−1 … +8) |
| same, 4 `int8` of 1–6 digits (id, counters) | 6,047,442 | +1% (−13 … +1) | +1% (−1 … +3) |
| same, 4 `int8` of 15–19 digits | 9,282,520 | +1% (−1 … +6) | −1% (−2 … 0) |
| same, 2 `int4` + 9 `text` | 16,414,312 | 0% (−2 … +2) | +2% (−4 … +5) |
| same, 4 `text` (no integers) | 6,359,720 | +2% (−6 … +17) | −4% (−9 … +1) |
| same with `fetchAll(PDO::FETCH_ASSOC)`, 4 `int4` over the full range | 9,072,293 | 0% (−4 … +1) | 0% (−2 … +1) |
| same with `fetchAll(PDO::FETCH_ASSOC)`, 2 `int4` + 9 `text` | 17,749,719 | +2% (−8 … +5) | 0% (−2 … +3) |

~: the change is not larger than the A/A control of the same row: not evidence of a difference.
<!-- /bench-table -->

## Code

PostgreSQL's text output for `int2`, `int4` and `int8` is an optional minus sign and digits without leading zeros. `_zend_handle_numeric_str_ex()` ([`Zend/zend_hash.c`](https://github.com/php/php-src/blob/c242f17cf4b/Zend/zend_hash.c#L3477-L3514)) accepts exactly that within the `zend_long` range: it rejects leading zeros, `-0` and values that do not fit, and returns `PHP_INT_MIN` correctly (it compares `idx - 1` against `ZEND_LONG_MAX` before negating). Everything it rejects goes to `ZEND_ATOL()` as before, so the result cannot differ from master; for PostgreSQL's own output that fallback is never taken.

The helper is an out-of-line `ZEND_API` call; the PR description says a hand-written loop was about 3 points faster, which I did not measure. The earlier review comment about "reinventing the wheel" was on a version before the force-push of 17 October; the current version reuses the existing parser.

On 32-bit builds the `int2` and `int4` branch changes too, and the helper has its own overflow check for `SIZEOF_ZEND_LONG == 4`. The new test is skipped there, but php-src's 32-bit CI job has no PostgreSQL service, so pdo_pgsql tests do not run on 32-bit in CI anyway. 32-bit was not checked here.

## Tests

[`difftest.php`](difftest.php) prints a SHA-256 over every fetched value with its type for 9 queries, once with native and once with emulated prepares: all 65,536 `int2` values, `int4` and `int8` at ±(10^k − 2 … 10^k + 2) for every k and at their limits, 200,000 random `int8` of up to 19 digits, 100,000 small `int8`, the `int2` and `int4` benchmark tables and NULLs ([`difftest-output.txt`](difftest-output.txt)). The output of master and the PR is identical with GCC 13.3 and with clang 20.1 ([`difftest-builds.txt`](difftest-builds.txt)). A build with `+ (len == 19)` added to the converted value ([`mutation.diff`](mutation.diff)), an error for 19-character values only, changes the hashes of three queries (int8 around powers of ten, int8 limits, int8 random) in both modes ([`difftest-mutation.txt`](difftest-mutation.txt)). [`difftest-builds.txt`](difftest-builds.txt) lists each build with the first 16 hex digits of the SHA-256 of its output.

`ext/pdo/tests` and `ext/pdo_pgsql/tests` with the GCC 13.3 builds, the PR's test files: 214 passed, 142 skipped, 1 expected fail (`pdo_022`), 0 failed, the same on master and on the PR ([`tests-head-gcc13.txt`](tests-head-gcc13.txt), [`tests-base-gcc13.txt`](tests-base-gcc13.txt)). Not run under ASan/UBSan.

## Reproduce

Needs Linux with perf access to hardware counters (`./bench doctor`), `libpq-dev` (the runs used libpq 16.15, `pkg-config --modversion libpq`), Docker, git 2.38 or newer, and php-src cloned from github.com/php/php-src next to php-src-bench, fetched after 22 October 2026. From the root of [php-src-bench](https://github.com/ArtUkrainskiy/php-src-bench):

```
# PostgreSQL 17 (the runs: 17.11) on cores other than the one bench measures on
docker run -d --name pr24385-pg --cpuset-cpus 12-15 -e POSTGRES_PASSWORD=bench -p 127.0.0.1:55432:5432 postgres:17
docker exec -i pr24385-pg psql -v ON_ERROR_STOP=1 -U postgres < reports/pr-24385-pdo-pgsql-int/pgsql.sql

# builds of master and of the PR merged onto it; the output must say PR 24385 head 3e479d70ffa
BENCH_CONFIGURE_EXTRA='--enable-pdo --with-pdo-pgsql' ./bench pr 24385 --base c242f17cf4b --slim --profile docker --cc gcc,gcc-14,clang,clang-20

# cycles; the build names carry your compiler versions (./bench builds)
./bench compare reports/pr-24385-pdo-pgsql-int/pgsql.php gcc13=pr24385-base-gcc13:pr24385-head-gcc13 gcc14=pr24385-base-gcc14:pr24385-head-gcc14 clang18=pr24385-base-clang18:pr24385-head-clang18 clang20=pr24385-base-clang20:pr24385-head-clang20 --out results/pr24385-pgsql.json
./bench table results/pr24385-pgsql.json --labels reports/pr-24385-pdo-pgsql-int/labels.txt --full

# the differential check: base and head of each compiler must print the same
for b in pr24385-base-gcc13 pr24385-head-gcc13; do ../php-builds/$b/sapi/cli/php -n reports/pr-24385-pdo-pgsql-int/difftest.php > results/difftest-$b.txt; done
diff results/difftest-pr24385-base-gcc13.txt results/difftest-pr24385-head-gcc13.txt
```

With other compilers or versions the build names differ, and with another CPU or machine load the cycles per call differ; the percentages are what compares. `difftest-output.txt` matches only with the tables of `pgsql.sql` and PostgreSQL 15 or newer, whose `random()` sequence for a seed the runs used. The tests ran from the PR's php-src tree with `PDO_PGSQL_TEST_DSN='pgsql:host=127.0.0.1 port=55432 dbname=postgres user=postgres password=bench' <build>/sapi/cli/php -n run-tests.php -j8 -p <build>/sapi/cli/php ext/pdo/tests ext/pdo_pgsql/tests`; the skip count depends on the libpq version.

The series in this report is [`series.json`](series.json); it was recorded from a copy of [`pgsql.php`](pgsql.php) at another path with the same content. `./bench table reports/pr-24385-pdo-pgsql-int/series.json --labels reports/pr-24385-pdo-pgsql-int/labels.txt --full` prints the tables above. Afterwards: `./bench gc --yes 'pr24385-*'` and `docker rm -f pr24385-pg`.
