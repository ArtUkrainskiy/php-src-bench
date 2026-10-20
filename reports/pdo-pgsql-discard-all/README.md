# pdo_pgsql: `DISCARD ALL` at the end of every request with persistent connections

Commit [`19deb91002a`](https://github.com/php/php-src/commit/19deb91002a53958893903aa3315e30e3285e614) ([#20572](https://github.com/php/php-src/pull/20572); in PHP-8.6 since 8.6.0alpha1, up to 8.6.0RC3, and in master) makes pdo_pgsql run `DISCARD ALL` when a persistent PDO object is freed. Under PHP-FPM that is the end of every request. `DISCARD ALL` is [equivalent to](https://www.postgresql.org/docs/17/sql-discard.html) `CLOSE ALL; SET SESSION AUTHORIZATION DEFAULT; RESET ALL; DEALLOCATE ALL; UNLISTEN *; SELECT pg_advisory_unlock_all(); DISCARD PLANS; DISCARD TEMP; DISCARD SEQUENCES;`. Behind PgBouncer in transaction pooling, `DISCARD ALL` and `DEALLOCATE ALL` also [clear the prepared statements PgBouncer tracks for the client](https://www.pgbouncer.org/config.html#max_prepared_statements) (tracking is on by default since PgBouncer 1.24), so every request prepares its statements on PostgreSQL again.

This report measures the commit on PHP-FPM, directly against PostgreSQL and through PgBouncer, and a narrower reset that keeps prepared statements.

## Builds

All three are PHP 8.5.11 built with the same script and flags; only `ext/pdo_pgsql/pgsql_driver.c` differs:
- **8.5.11:** as released.
- **DISCARD ALL:** [discard-all-backport.patch](discard-all-backport.patch), the `pgsql_driver.c` part of `19deb91002a` applied to 8.5.11 (it applies with an offset of 7 lines; the code of the commit is unchanged).
- **keep statements:** [discard-keep-statements.patch](discard-keep-statements.patch), the same function sending `DISCARD ALL` without `DEALLOCATE ALL` and `DISCARD PLANS`, in one `PQexec`:
  `CLOSE ALL; SET SESSION AUTHORIZATION DEFAULT; RESET ALL; UNLISTEN *; SELECT pg_advisory_unlock_all(); DISCARD TEMP; DISCARD SEQUENCES`.

## Setup

- **Harness:** [web-request-cost](https://github.com/ArtUkrainskiy/web-request-cost/tree/afd7ea6ee4f2f10069bd029e0c29a705c034861c) at `afd7ea6`, stack `fpm`: nginx 1.30.5 and PHP-FPM (`pm = static`, 32 children, persistent PDO, native prepares — pdo_pgsql's default), a JSON API with four SQL statements per request ([spec](https://github.com/ArtUkrainskiy/web-request-cost/blob/afd7ea6ee4f2f10069bd029e0c29a705c034861c/spec/spec.md)). PHP builds by `harness/stack/build-php.sh` (flags of the official Docker image), the variant selected with the harness' `PHP_BUILD`.
- **Database:** PostgreSQL 17.11 in Docker; through PgBouncer 1.25.1 (`VIA_BOUNCER=1`): `pool_mode = transaction`, 4 processes, 24 server connections, `max_prepared_statements = 200`. libpq 18.6.
- **Load:** wrk2, 2000 req/s over 48 connections (`c` = 50 in the records: 4 wrk threads × 12); every run first checks the responses against the reference hash.
- **Machine:** AMD Ryzen 9 5950X, Ubuntu 26.04, kernel 7.0, governor `performance`, GCC 15.2; stack on 4 cores / 8 threads, PostgreSQL and the load generator on other cores.
- **Metric:** cgroup CPU time per request of the stack's containers (nginx, PHP-FPM and PgBouncer) and of PostgreSQL, over the 20 s measurement window after 15 s of warm-up.
- **Passes:** 5; 8.5.11 and the variant alternate within each pass, in reverse order on even passes ([scripts/run-variant.sh](scripts/run-variant.sh)). A change is the median of the per-pass ratios variant / 8.5.11, with their range ([scripts/pair.py](scripts/pair.py)).

## Results

CPU per request, medians of 5 passes (ms); the change in brackets, with the range of the per-pass ratios:

| path | build | stack | PostgreSQL | total | p99 |
|---|---|---:|---:|---:|---:|
| direct | 8.5.11 | 0.498 | 1.453 | 1.952 | 6.2 ms |
| direct | DISCARD ALL | 0.525 | 1.504 | 2.030 (+3.8%, +1.2…+7.0%) | 6.4 ms |
| PgBouncer | 8.5.11 | 0.947 | 0.687 | 1.632 | 4.2 ms |
| PgBouncer | DISCARD ALL | 1.002 | 1.492 | 2.493 (+52.1%, +50.5…+53.5%) | 6.8 ms |
| direct | 8.5.11 | 0.505 | 1.466 | 1.969 | 6.3 ms |
| direct | keep statements | 0.532 | 1.530 | 2.065 (+4.1%, +3.3…+7.9%) | 6.4 ms |
| PgBouncer | 8.5.11 | 0.963 | 0.695 | 1.659 | 4.2 ms |
| PgBouncer | keep statements | 1.012 | 0.737 | 1.749 (+5.9%, +3.3…+7.8%) | 4.4 ms |

Each pair of rows is one series ([data/](data)). "total" is the median of the per-run sums, so it can differ from the sum of the two column medians by up to 0.003 ms. Behind PgBouncer, `DISCARD ALL` more than doubles PostgreSQL's CPU per request (0.687 → 1.492 ms, +117%): about what PostgreSQL spends without PgBouncer, where every statement is prepared on every request. Directly against PostgreSQL, and behind PgBouncer with the narrower reset, the cost is the extra round trip and the reset itself, 4–6%.

No request failed in any run; the non-2xx responses (369–373 per run) are the 1% of requests with an unknown token that the load contains by design. Two variant runs directly against PostgreSQL completed about 1% fewer requests in the 20 s window (39,432 and 39,441 instead of about 39,923: DISCARD ALL pass 4, keep statements pass 2); the metric is per request.

## What each reset clears

[scripts/session-reset-check.php](scripts/session-reset-check.php) changes the session on a persistent connection, frees the PDO object and creates it again on the same connection (the same backend in every run); the outputs are in [data/session-check/](data/session-check):

| after the PDO object is freed | 8.5.11 | DISCARD ALL | keep statements |
|---|---|---|---|
| setting reset (tested with `application_name`) | no | yes | yes |
| temporary table dropped | no | yes | yes |
| advisory lock released | no | yes | yes |
| `LISTEN` removed | no | yes | yes |
| SQL-level `PREPARE` by the application removed | no | yes | no |

Through PgBouncer, the rows above are the same for all three builds. The list of server statements there shows PgBouncer's own statements (`PGBOUNCER_n`), which PgBouncer keeps after its clients close theirs; the application's `reset_check_sql` is gone only with `DISCARD ALL`. Directly against PostgreSQL, the statement of the `PDOStatement` from the first use is closed when the object is destroyed, in all three builds. The narrower reset also leaves out `DISCARD PLANS`, so cached plans of the remaining prepared statements are kept.

## Not tested

- PHP-8.6 or master themselves (only the backport to 8.5.11), other PostgreSQL and PgBouncer versions, session pooling in PgBouncer.
- Worker runtimes (FrankenPHP, RoadRunner) with persistent connections.
- `SET SESSION AUTHORIZATION DEFAULT` and `RESET ALL` with roles or settings set by the application in more detail than `application_name`.
