# pdo_pgsql: `DISCARD ALL` when a PDO object on a persistent connection is freed

Commit [`19deb91002a`](https://github.com/php/php-src/commit/19deb91002a53958893903aa3315e30e3285e614) ([#20572](https://github.com/php/php-src/pull/20572); in PHP-8.6 since 8.6.0alpha1, up to 8.6.0RC3, and in master) adds a `persistent_shutdown` callback to pdo_pgsql that runs `DISCARD ALL`. PDO calls it from the free handler of the PDO object (`pdo_dbh_free_storage`, [ext/pdo/pdo_dbh.c](https://github.com/php/php-src/blob/19deb91002a53958893903aa3315e30e3285e614/ext/pdo/pdo_dbh.c)) when the object uses a persistent connection. Under PHP-FPM, a PDO object is freed no later than request shutdown, so every request that creates a PDO object on a persistent connection resets the session, at the latest at the end of the request.

`DISCARD ALL` is [equivalent to](https://www.postgresql.org/docs/17/sql-discard.html) `CLOSE ALL; SET SESSION AUTHORIZATION DEFAULT; RESET ALL; DEALLOCATE ALL; UNLISTEN *; SELECT pg_advisory_unlock_all(); DISCARD PLANS; DISCARD TEMP; DISCARD SEQUENCES;`. PgBouncer in transaction pooling, with `max_prepared_statements` > 0 (200 by default since PgBouncer 1.24), tracks the protocol-level prepared statements of each client (prepared with the Parse message, as libpq does for pdo_pgsql's native prepares) and keeps them prepared on its server connections across transactions. [`DISCARD ALL` and `DEALLOCATE ALL` clear the statements it tracks for the client](https://www.pgbouncer.org/config.html#max_prepared_statements). SQL-level `PREPARE` is not tracked; it is passed to PostgreSQL as is.

This report measures the commit on PHP-FPM, directly against PostgreSQL and through PgBouncer, and two narrower resets.

## Builds

Four builds of PHP 8.5.11 with the same script and flags; they differ only in `ext/pdo_pgsql/pgsql_driver.c`:
- **8.5.11:** as released.
- **DISCARD ALL:** [discard-all-backport.patch](discard-all-backport.patch), the `pgsql_driver.c` part of `19deb91002a` applied to 8.5.11 (it applies with an offset of 7 lines; the code of the commit is unchanged).
- **keep statements:** [discard-keep-statements.patch](discard-keep-statements.patch), a modified reset callback that omits `DEALLOCATE ALL` and `DISCARD PLANS` from `DISCARD ALL`, preserving both prepared statements and their cached plans. The remaining reset commands run in a single `PQexec` call:
  `CLOSE ALL; SET SESSION AUTHORIZATION DEFAULT; RESET ALL; UNLISTEN *; SELECT pg_advisory_unlock_all(); DISCARD TEMP; DISCARD SEQUENCES`.
- **keep statements, drop plans:** [discard-keep-statements-drop-plans.patch](discard-keep-statements-drop-plans.patch), the same callback with `DISCARD PLANS` added: prepared statements are preserved, their cached plans are dropped.

## Setup

- **Harness:** [web-request-cost](https://github.com/ArtUkrainskiy/web-request-cost/tree/afd7ea6ee4f2f10069bd029e0c29a705c034861c) at `afd7ea6`, stack `fpm`: nginx 1.30.5 and PHP-FPM (`pm = static`, 32 children, persistent PDO, native prepares — pdo_pgsql's default), a JSON API with four SQL statements per request ([spec](https://github.com/ArtUkrainskiy/web-request-cost/blob/afd7ea6ee4f2f10069bd029e0c29a705c034861c/spec/spec.md)). PHP builds by `harness/stack/build-php.sh` (flags of the official Docker image), the variant selected with the harness' `PHP_BUILD`.
- **Database:** PostgreSQL 17.11 in Docker; through PgBouncer 1.25.1 (`VIA_BOUNCER=1`): `pool_mode = transaction`, 4 processes, 24 server connections, `max_prepared_statements = 200`. libpq 18.6.
- **Load:** wrk2, 2000 req/s. The records store `c` = 50; wrk2 opens 48 connections, 12 per thread on 4 threads ([wrk.c:123](https://github.com/giltene/wrk2/blob/44a94c17d8e6a0bac8559b53da76848e430cb7a7/src/wrk.c#L123) divides the connections by the threads). Every run first checks the responses against the reference hash.
- **Machine:** AMD Ryzen 9 5950X, Ubuntu 26.04, kernel 7.0, governor `performance`, GCC 15.2; stack on 4 cores / 8 threads, PostgreSQL and the load generator on other cores.
- **Metric:** cgroup CPU time per completed request of the stack's containers (nginx, PHP-FPM and PgBouncer) and of PostgreSQL, over the 20 s measurement window after 15 s of warm-up.
- **Passes:** 5; 8.5.11 and the variant alternate within each pass, in reverse order on even passes ([scripts/run-variant.sh](scripts/run-variant.sh)). Each variant is compared only with the 8.5.11 runs of its own series: a change is the median of the per-pass ratios variant / 8.5.11, and the range is the smallest and largest of these ratios, not a confidence interval ([scripts/pair.py](scripts/pair.py)).

## Results

CPU per request, medians of 5 passes (ms); the change in brackets, with the range of the per-pass ratios. Each pair of rows is one series ([data/](data)); "total" is the median of the per-run sums, so it can differ from the sum of the two column medians by up to 0.003 ms.

| path | build | stack | PostgreSQL | total | p99 |
|---|---|---:|---:|---:|---:|
| PgBouncer | 8.5.11 | 0.947 | 0.687 | 1.632 | 4.2 ms |
| PgBouncer | DISCARD ALL | 1.002 | 1.492 | 2.493 (+52.1%, +50.5…+53.5%) | 6.8 ms |
| PgBouncer | 8.5.11 | 0.961 | 0.689 | 1.652 | 4.2 ms |
| PgBouncer | keep statements, drop plans | 1.021 | 1.040 | 2.061 (+24.6%, +22.3…+27.2%) | 4.7 ms |
| PgBouncer | 8.5.11 | 0.963 | 0.695 | 1.659 | 4.2 ms |
| PgBouncer | keep statements | 1.012 | 0.737 | 1.749 (+5.9%, +3.3…+7.8%) | 4.4 ms |
| direct | 8.5.11 | 0.498 | 1.453 | 1.952 | 6.2 ms |
| direct | DISCARD ALL | 0.525 | 1.504 | 2.030 (+3.8%, +1.2…+7.0%) | 6.4 ms |
| direct | 8.5.11 | 0.505 | 1.465 | 1.970 | 6.3 ms |
| direct | keep statements, drop plans | 0.525 | 1.519 | 2.046 (+3.9%, +3.4…+4.2%) | 6.3 ms |
| direct | 8.5.11 | 0.505 | 1.466 | 1.969 | 6.3 ms |
| direct | keep statements | 0.532 | 1.530 | 2.065 (+4.1%, +3.3…+7.9%) | 6.4 ms |

Behind PgBouncer, `DISCARD ALL` raises PostgreSQL's CPU per request by 117% (0.687 → 1.492 ms), close to the level of direct connections (1.453 ms), where pdo_pgsql prepares every statement on every request. Keeping the prepared statements but dropping their plans leaves about half of the regression (+24.6%, PostgreSQL +51%); keeping both leaves +5.9%. The series have their own baselines, so these differences describe the variants, not an exact split of PostgreSQL's CPU between the two mechanisms. Directly against PostgreSQL the three resets cost about the same, 3.8–4.1%: there, prepared statements do not outlive a request anyway. This remaining overhead is consistent with the additional round trip and the reset itself.

No request failed in any run; the non-2xx responses (369–373 per run) are the 1% of requests with an unknown token that the workload intentionally includes. Two variant runs directly against PostgreSQL completed about 1% fewer requests in the 20 s window (39,432 and 39,441 instead of about 39,923: DISCARD ALL pass 4, keep statements pass 2), and they are the largest changes of their series (+7.0% and +7.9%). Without them the medians are +3.1% (DISCARD ALL) and +3.9% (keep statements).

## Prepares on PostgreSQL

This is a separate diagnostic run, not the configuration of the CPU benchmark: it shows the mechanism, it does not profile the runs above. To count the prepares directly, PgBouncer ran as one process with admin access (`admin_users`; [data/bouncer-counts/](data/bouncer-counts), [scripts/bouncer-counts.py](scripts/bouncer-counts.py)): `SHOW STATS` of the database before and after 2000 requests sent by 8 concurrent clients (1978 answered 200, 22 answered 401 in each build).

| build | Parse from clients | Parse on PostgreSQL | Parse on PostgreSQL / HTTP request | Bind | transactions |
|---|---:|---:|---:|---:|---:|
| 8.5.11 | 7,934 | 55 | 0.03 | 7,934 | 23,802 |
| DISCARD ALL | 7,934 | 6,649 | 3.32 | 7,934 | 25,802 |
| keep statements | 7,934 | 55 | 0.03 | 7,934 | 25,802 |
| keep statements, drop plans | 7,934 | 55 | 0.03 | 7,934 | 25,802 |

With `DISCARD ALL`, Parse operations on PostgreSQL increase from 55 to 6,649 (84% of the 7,934 Parse messages from the clients), for the same number of client Parse messages. Both narrower resets keep the baseline's 55. The 2000 extra transactions with every reset are the resets, one per request.

## What each reset clears

[scripts/session-reset-check.php](scripts/session-reset-check.php) is a smoke test of one sequence on one connection, not a proof of isolation under concurrent load. It modifies the session state through a persistent PDO connection, frees the PDO object (the same `persistent_shutdown` path as at the end of an FPM request) and creates a PDO object again on the same persistent connection; it checks that the second use runs on the same backend. The advisory lock is checked from a second, non-persistent connection; when that connection runs on the same backend, the script prints "not applicable", since a backend can take its own session-level advisory lock again. Outputs: [data/session-check/](data/session-check).

Directly against PostgreSQL (the second connection on another backend in every build):

| after the PDO object is freed | 8.5.11 | DISCARD ALL | keep statements, drop plans | keep statements |
|---|---|---|---|---|
| setting reset (tested with `application_name`) | no | yes | yes | yes |
| temporary table dropped | no | yes | yes | yes |
| advisory lock released | no | yes | yes | yes |
| `LISTEN` removed | no | yes | yes | yes |
| SQL-level `PREPARE` by the application removed | no | yes | no | no |

Through PgBouncer, the setting, temporary table and `LISTEN` rows are the same. The advisory-lock result is conclusive only when PgBouncer gives the second connection another backend, which varies between runs: in the published outputs it did for 8.5.11 (not released) and both narrower resets (released), and not for DISCARD ALL (not applicable). The server-side statement list there includes PgBouncer's own statements (`PGBOUNCER_n`), which PgBouncer keeps after its clients close theirs.

The statement lists are collected after the checks, which prepare statements of their own (`pdo_stmt_00000008` directly against PostgreSQL); the statement of the `PDOStatement` used before the PDO object was freed is closed when that object is destroyed, in all four builds.

## Conclusion

In the tested PHP-FPM workload, `DISCARD ALL` at the end of each request increased the total CPU per request by 3.8% with direct PostgreSQL connections and by 52.1% behind PgBouncer in transaction pooling. Most of the PgBouncer regression is on the PostgreSQL side. PgBouncer's counters confirm repeated server-side preparation as one source of it; the variant with `DISCARD PLANS` shows that losing the cached plans also accounts for a substantial part (+24.6% with the statements kept). A reset that keeps prepared statements and their plans reduced the measured overhead behind PgBouncer to 5.9% and passed the session-state smoke tests described above.

These results show the cost of `DISCARD ALL` in this configuration. They do not show that the narrower reset is a drop-in replacement: it keeps session-level prepared statements and cached plans, including SQL-level `PREPARE` by the application, and its security and compatibility implications across requests — particularly when session roles, search paths or database schemas change — have not been evaluated. It also runs several commands in one `PQexec`, which PostgreSQL executes as [one implicit transaction](https://www.postgresql.org/docs/17/protocol-flow.html#PROTOCOL-FLOW-MULTI-STATEMENT): if one command fails, the following ones do not run and the transactional effects of the earlier ones are rolled back; like the commit, the callback ignores the result, so nothing reports it.

## Not tested

- PHP-8.6 or master themselves (only the backport to 8.5.11), other PostgreSQL and PgBouncer versions, session pooling in PgBouncer.
- Worker runtimes (FrankenPHP, RoadRunner) with persistent connections.
- Roles (`SET ROLE`, `SET SESSION AUTHORIZATION`), `search_path` and schema changes between requests with the narrower resets.
- Other SQL workloads and plan-cache behaviour (`plan_cache_mode = auto` here): the cost of `DISCARD PLANS` depends on how expensive the plans of the workload's statements are.
