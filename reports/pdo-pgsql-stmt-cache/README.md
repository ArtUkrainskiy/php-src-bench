# pdo_pgsql: a per-connection cache of prepared statements, measured on Drupal 11.4

A prototype patch for PHP 8.5.11: [stmt-cache-8.5.11.patch](stmt-cache-8.5.11.patch), 4 files of ext/pdo_pgsql, about 220 added lines. It is not part of any PHP release and has not been proposed to php-src yet. Measured on 21 October 2026. The measured patch has one known bug in an error path, fixed after the runs ([Details for review](#the-change)); master was not measured.

## Summary

With native prepared statements (pdo_pgsql's default), 8.5.11 prepares each statement on the server, executes it, and closes it when the `PDOStatement` object is freed. That is three round trips to the database for a query that runs once. The patch keeps the prepared statements of a connection and reuses them, by SQL text, from any later `PDOStatement`, as PgJDBC does with [`prepareThreshold`](https://jdbc.postgresql.org/documentation/server-prepare/). The cache lives as long as the connection: with persistent connections it carries over from request to request, without them it lasts one request.

All numbers are total CPU per URL: nginx, PHP-FPM, PostgreSQL and, where used, PgBouncer. "Directly" means PHP connects to PostgreSQL itself; "through PgBouncer" means it connects through PgBouncer 1.25.1 in transaction pooling, with `max_prepared_statements = 200`.
- **The patch, native prepares, persistent connections:** −15.2% directly, −13.4% through PgBouncer, against 8.5.11 in the same mode. PostgreSQL's CPU drops by 40.3% and 18.0%. The prepare and close round trips are gone: PostgreSQL, which counts each prepare and each execute as a transaction, counts 122 per URL instead of 241.
- **The patch, native prepares, no persistent connections:** −9.6% directly, −10.7% through PgBouncer, against 8.5.11 in the same mode (a second series). The cache lasts one request, and still PostgreSQL counts 129.5 transactions per URL instead of 242.1.
- **Against emulated prepares** (PDO puts the parameters into the SQL text; the mode with the lowest CPU without the patch here), both persistent: PostgreSQL uses 20.0% less CPU directly and 15.4% less through PgBouncer. Total CPU drops by 2.9% and 1.8%, because most of it is PHP-FPM running Drupal: with emulated prepares, PostgreSQL is 22% and 18% of the total.
  - Costs: PHP-FPM uses 2.0% more CPU directly. Through PgBouncer, PgBouncer uses 6.4% more CPU and the median latency is 2.8% higher. PgBouncer was busy 76–89% of one CPU thread, so its latency includes queueing.
  - Without persistent connections, against emulated prepares also without them, the total CPU is 1.3% higher directly and 0.3% higher through PgBouncer (0.7% and 0.9% in the second series). Through PgBouncer, PgBouncer's CPU is 3.9% higher and the median latency 3.3% higher (3.5% and 2.5% in the second series).
- **Emulated prepares never reach the patched code:** applications that use them, such as Drupal by default, are not affected.
- **Noise:** the same binary measured twice differs by −0.2% directly and −0.1% through PgBouncer, and by −0.3% and −0.4% in the second series. In single passes the difference ranges from −1.3% to +1.4%.

## Why Drupal

Drupal is the test bench, not the subject. The patch changes pdo_pgsql for any PHP code that uses native prepares. Nothing in it is specific to Drupal, and no other application or framework was measured.

Drupal was chosen because it is a large open-source application with real business logic on PostgreSQL, rather than a synthetic loop of queries. It is also a hard case for a statement cache:
- it builds many distinct SQL texts: dynamic filters and sorts, and `LIMIT`/`OFFSET` written into the text;
- its own PostgreSQL driver turns native prepares off, with the comment "most of Drupal's prepared queries are not re-used" ([Connection.php](https://github.com/drupal/drupal/blob/11.4.10/core/modules/pgsql/src/Driver/Database/pgsql/Connection.php)).

The URLs here were chosen for SQL variety. With persistent connections the cache still served almost every statement: through PgBouncer, PHP sent 1.05 prepares per URL with the patch, against 123 without it.

The workload is 8 logged-in editors in a closed loop against 8 PHP-FPM workers, with no page cache.

## Terms

- **Native prepares:** PostgreSQL receives the SQL with placeholders and the parameters separately. This is pdo_pgsql's default.
- **Emulated prepares** (`PDO::ATTR_EMULATE_PREPARES => TRUE`; Drupal's default): PDO puts the parameters into the SQL text and sends one query.
- **Persistent connection** (`PDO::ATTR_PERSISTENT`): a PHP-FPM worker keeps its database connection open between requests.
- **Round trip:** one exchange of messages between PHP and the database, from the request to the answer.
- **Named statement:** prepared on the server under a name. Executing it again skips parsing.
- **Unnamed statement:** parsed, bound and executed in one round trip. The server keeps it only until the next unnamed statement.
- **A/A control:** the 8.5.11 binary measured as two variants under two names. Their difference is the noise of the setup.

## The change

**Without the patch:** with native prepares, 8.5.11 gives every `PDOStatement` its own named statement. It is prepared at the first `execute()` and closed when the object is freed.

**With the patch:**
- Each connection keeps a table of the statements it executed, keyed by the SQL text and the parameter types.
- For its first 4 executions on the connection, a statement runs as an unnamed statement (`PQexecParams`).
- At the 5th execution it is prepared under a name. From then on, every `PDOStatement` with the same text executes it by name (`PQexecPrepared`): one round trip, no parsing.
- When the table is full, the least recently used entry is dropped. If that entry was prepared, its statement is closed on the server.
- Emulated prepares, `Pdo\Pgsql::ATTR_DISABLE_PREPARES` and scrollable cursors do not use the table.

**Two new INI settings,** read when a connection opens:
- `pdo_pgsql.prepare_threshold`: the execution at which a statement is prepared. Default 5; 0 restores the behaviour of 8.5.11.
- `pdo_pgsql.statement_cache_size`: entries per connection. Default 64; 0 (with a threshold above 0) runs every statement unnamed.

**Behaviour that applications can see:**
- **Schema changes.** A cached statement whose result columns change makes PostgreSQL return SQLSTATE 0A000, for example `SELECT *` after `ALTER TABLE … ADD COLUMN`.
  - Outside a transaction the patch closes the statement and retries the query unnamed.
  - Inside a transaction the error goes to the application, because PostgreSQL has already aborted the transaction. Without the patch, a new `PDOStatement` would prepare the query again.
  - A statement that no longer exists (26000, for example after `DEALLOCATE ALL`) is handled the same way.
- **Persistent connections** also carry session state from one request to the next. That is a property of persistent connections, not of the patch, but against emulated prepares the patch pays off only with them.

**Details for review:**
- The name is `pdo_s_` plus 192 bits of the SHA-256 of the key, so the same text gets the same name on every connection. A prepare that fails with 42P05 ("prepared statement already exists") counts as prepared; inside a transaction that failure also aborts the transaction.
- Inside an aborted transaction nothing is closed. A prepared entry is then not evicted, and only the statement that needed the space runs without the table.
- **Known bug in this patch.** After 0A000 inside a transaction, the measured patch does not close the server statement. In later transactions the statement keeps failing until it runs once outside a transaction, which closes it. The application gets 0A000, or 25P02 when the new prepare finds the old name and aborts the transaction. It was fixed after the runs. The fix is not in this directory and was not measured. The runs contain no such error: no Drupal log entry of severity warning or worse.
- **Why 8.5.11:** the prototype was written against the release that the measured stack builds. Master was not measured.

## Results

Medians of 5 passes; CPU is in ms per URL. Running `python3 scripts/table.py data/<file>.jsonl` from this directory prints the tables of each data file.

### Directly against PostgreSQL

| build | PDO mode | total CPU | PHP-FPM | PostgreSQL | p50 | p99 | PostgreSQL transactions per URL |
|---|---|---:|---:|---:|---:|---:|---:|
| 8.5.11 | emulated | 105.7 | 71.7 | 33.4 | 84 ms | 188 ms | 122.2 |
| 8.5.11 | emulated, persistent | 86.3 | 66.2 | 19.3 | 71 ms | 175 ms | 121.0 |
| 8.5.11 | native, persistent | 98.7 | 71.9 | 26.0 | 80 ms | 185 ms | 241.1 |
| 8.5.11, A/A copy | native, persistent | 98.5 | 71.6 | 26.0 | 80 ms | 187 ms | 240.6 |
| 8.5.11 + cache | native, persistent | **83.8** | 67.6 | **15.5** | 68 ms | 171 ms | 122.1 |
| 8.5.11 + cache | native | 107.0 | 72.9 | 33.5 | 85 ms | 189 ms | 129.2 |

A change is the median, over the five passes, of the ratio of the two variants in the same pass. Negative means less CPU or lower latency.

| comparison | total CPU | PHP-FPM | PostgreSQL | p50 |
|---|---:|---:|---:|---:|
| A/A: the same binary twice | −0.2% | −0.4% | −0.1% | 0.0% |
| native + patch against native, both persistent | **−15.2%** | −6.3% | −40.3% | −15.2% |
| native + patch against emulated, both persistent | −2.9% | +2.0% | −20.0% | −2.9% |
| native + patch against emulated, neither persistent | +1.3% | +1.3% | +0.2% | +1.2% |
| native + patch, persistent, against emulated, not | −20.8% | −5.6% | −53.6% | −19.3% |
| no patch: emulated, persistent against not | −18.1% | −7.1% | −42.0% | −15.3% |

### Through PgBouncer

| build | PDO mode | total CPU | PHP-FPM | PostgreSQL | PgBouncer | p50 | p99 |
|---|---|---:|---:|---:|---:|---:|---:|
| 8.5.11 | emulated | 110.7 | 73.7 | 19.2 | 17.1 | 120 ms | 242 ms |
| 8.5.11 | emulated, persistent | 106.5 | 71.7 | 19.2 | 14.9 | 106 ms | 223 ms |
| 8.5.11 | native, persistent | 120.8 | 77.3 | 19.8 | 23.0 | 153 ms | 313 ms |
| 8.5.11, A/A copy | native, persistent | 120.3 | 77.3 | 19.6 | 22.9 | 152 ms | 312 ms |
| 8.5.11 + cache | native, persistent | **104.6** | 71.8 | **16.2** | 15.9 | 109 ms | 227 ms |
| 8.5.11 + cache | native | 111.2 | 73.9 | 18.7 | 17.7 | 123 ms | 245 ms |

PgBouncer's counters per URL (`SHOW STATS`: client transactions, `total_client_parse_count`, `total_server_parse_count`):

| build | PDO mode | client transactions | prepares sent by PHP | prepares sent to PostgreSQL |
|---|---|---:|---:|---:|
| 8.5.11 | emulated | 121.01 | 0.00 | 0.00 |
| 8.5.11 | emulated, persistent | 121.03 | 0.00 | 0.00 |
| 8.5.11 | native, persistent | 360.93 | 123.11 | 2.05 |
| 8.5.11, A/A copy | native, persistent | 360.39 | 122.93 | 2.08 |
| 8.5.11 + cache | native, persistent | 123.19 | 1.05 | 0.04 |
| 8.5.11 + cache | native | 128.02 | 7.16 | 0.01 |

| comparison | total CPU | PHP-FPM | PostgreSQL | PgBouncer | p50 |
|---|---:|---:|---:|---:|---:|
| A/A: the same binary twice | −0.1% | +0.1% | −1.0% | −0.2% | −0.7% |
| native + patch against native, both persistent | **−13.4%** | −6.9% | −18.0% | −31.0% | −28.3% |
| native + patch against emulated, both persistent | −1.8% | +0.2% | −15.4% | +6.4% | +2.8% |
| native + patch against emulated, neither persistent | +0.3% | 0.0% | −1.9% | +3.9% | +3.3% |
| native + patch, persistent, against emulated, not | −5.5% | −2.8% | −15.4% | −7.0% | −9.2% |
| no patch: emulated, persistent against not | −3.8% | −2.5% | 0.0% | −12.8% | −11.7% |

The minimum and maximum of the five per-pass ratios for each cell are in the [full tables](#full-tables).

### Without persistent connections: the second series

A second series of 5 passes measured the modes without persistent connections: 8.5.11 emulated, 8.5.11 native twice (its own A/A control) and the patch native. It ran on the same day, after the first series, with the scripts of this directory. Its numbers are not mixed into the tables above.

Directly against PostgreSQL:

| build | PDO mode | total CPU | PHP-FPM | PostgreSQL | p50 | p99 | PostgreSQL transactions per URL |
|---|---|---:|---:|---:|---:|---:|---:|
| 8.5.11 | emulated | 106.2 | 71.7 | 33.7 | 84 ms | 189 ms | 122.2 |
| 8.5.11 | native | 118.4 | 76.8 | 40.6 | 94 ms | 201 ms | 242.1 |
| 8.5.11, A/A copy | native | 118.2 | 76.7 | 40.7 | 94 ms | 201 ms | 242.2 |
| 8.5.11 + cache | native | 106.8 | 72.4 | 33.6 | 86 ms | 189 ms | 129.5 |

| comparison | total CPU | PHP-FPM | PostgreSQL | p50 |
|---|---:|---:|---:|---:|
| A/A: the same binary twice | −0.3% | −0.4% | −0.1% | 0.0% |
| native + patch against native, neither persistent | **−9.6%** | −5.7% | −17.2% | −8.5% |
| native + patch against emulated, neither persistent | +0.7% | +0.8% | −0.1% | +1.2% |

Through PgBouncer:

| build | PDO mode | total CPU | PHP-FPM | PostgreSQL | PgBouncer | p50 | p99 |
|---|---|---:|---:|---:|---:|---:|---:|
| 8.5.11 | emulated | 110.9 | 73.8 | 19.2 | 17.2 | 121 ms | 244 ms |
| 8.5.11 | native | 125.5 | 80.0 | 19.7 | 25.0 | 167 ms | 337 ms |
| 8.5.11, A/A copy | native | 125.5 | 79.6 | 20.0 | 24.9 | 167 ms | 340 ms |
| 8.5.11 + cache | native | 111.9 | 74.6 | 18.8 | 17.8 | 124 ms | 247 ms |

| build | PDO mode | client transactions | prepares sent by PHP | prepares sent to PostgreSQL |
|---|---|---:|---:|---:|
| 8.5.11 | emulated | 121.10 | 0.00 | 0.00 |
| 8.5.11 | native | 360.94 | 123.11 | 2.05 |
| 8.5.11, A/A copy | native | 360.35 | 122.91 | 2.07 |
| 8.5.11 + cache | native | 128.08 | 7.17 | 0.01 |

| comparison | total CPU | PHP-FPM | PostgreSQL | PgBouncer | p50 |
|---|---:|---:|---:|---:|---:|
| A/A: the same binary twice | −0.4% | −0.7% | 0.0% | −0.1% | +0.6% |
| native + patch against native, neither persistent | **−10.7%** | −6.7% | −4.6% | −28.6% | −25.9% |
| native + patch against emulated, neither persistent | +0.9% | +0.7% | −2.2% | +3.5% | +2.5% |

### What the numbers show

- **Round trips.** Without the patch, PostgreSQL counts the prepare and the execute of each native statement as transactions: 241 per URL directly, against 121–122 with emulation or with the patch. It does not count the close. PgBouncer counts all three exchanges: 360.9 client transactions per URL, against 121.0 with emulation and 123.2 with the patch.
- **Prepares.** Through PgBouncer, PHP sends 123.1 prepares per URL without the patch and 1.05 with it. PgBouncer keeps the prepared statements of its server connections (`max_prepared_statements = 200`), so it sends PostgreSQL only 2.05 and 0.04 per URL.
- **Without persistent connections,** the patch prepares only the statements that run 5 times within one request: 7.2 per URL through PgBouncer. Directly, they show as 129.2 PostgreSQL transactions per URL, against 122.2 with emulation.
  - Every other statement runs unnamed in one round trip, where 8.5.11 with native prepares needs three. In the second series that is 129.5 PostgreSQL transactions per URL against 242.1 directly, and 128.1 PgBouncer client transactions against 360.9.
- **CPU causes were not profiled.** PostgreSQL's CPU is 20.0% lower with the patch than with emulation directly, and 15.4% lower through PgBouncer. Through PgBouncer, 8.5.11 with native prepares also executes named statements on PostgreSQL, yet its PostgreSQL CPU (19.8 ms) stays close to emulation's (19.2 ms), so naming alone does not explain the drop. The 2.0% more CPU of PHP-FPM against emulation was not profiled either.
- **PgBouncer** runs as one process and was busy 76–89% of one CPU thread during a run. Latencies are therefore not comparable between the two paths.
- **Noise.** In the A/A control, the total CPU of single passes differs by at most 1.4%. One exception is PostgreSQL's CPU through PgBouncer: with 8.5.11 and native prepares it varies between passes from 19.3 to 21.4 ms (A/A −6.7%…+7.8% in the first series, −4.9%…+6.5% in the second). In the other variants it varies by at most 4.1%.

## Method

- **Site.** Drupal 11.4.10, installed with the image `drupal:11-php8.4-apache`, which is used only for the installation ([scripts/setup.sh](scripts/setup.sh)).
  - The standard profile, plus the core recipes for articles, pages, tags, comments and content search.
  - 3,000 nodes with up to 5 comments each, 200 terms and 121 users, 20 of them editors. The content comes from devel_generate, which is not seeded. The site is described in [data/site.txt](data/site.txt).
  - Caches are cleared and `automated_cron` is uninstalled. Then the database is saved as the template that every run starts from.
- **PHP.** 8.5.11, built by [build.sh](scripts/build.sh) with the extension set and compiler flags of web-request-cost's [build-php.sh](https://github.com/ArtUkrainskiy/web-request-cost/blob/afd7ea6/harness/stack/build-php.sh), plus `--enable-gd --with-freetype` (Drupal needs an image toolkit).
  - The flags are those of the official php Docker image: `-fstack-protector-strong -fpic -fpie -O2 -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64`, linked with `-Wl,-O1 -pie`.
  - GCC 15.2, libpq 18.6.
- **Stack.**
  - nginx 1.30.5 and PHP-FPM with `pm = static` and 8 children ([scripts/drupal-run.sh](scripts/drupal-run.sh)).
  - PostgreSQL 17.11 with default settings. Besides the built-in `plpgsql`, its only extension is `pg_trgm`, which Drupal installs.
  - Through PgBouncer: PgBouncer 1.25.1, one process, transaction pooling, pool size 8, `max_prepared_statements = 200`.
- **PDO modes.** They are set in the environment of the FPM pool and applied as `pdo` options of Drupal's connection ([scripts/settings-bench.php](scripts/settings-bench.php)): `emulated`, `emulated-persistent`, `native` and `native-persistent`.
- **Load.** JMeter 5.6.3 runs 8 logged-in editors in a closed loop ([scripts/editors.jmx](scripts/editors.jmx)).
  - Every run requests the same 2,000 URLs ([scripts/make-urls.py](scripts/make-urls.py), seed 42):
    - 30% the content overview with random filters, sorts and pages;
    - 15% nodes and 10% node edit forms;
    - 10% term pages and 10% search with random words;
    - 10% deep pages of the front page;
    - 5% user pages, 5% the front page and 5% the plain content overview.
  - Every 20th step, an editor posts a comment: 95–98 per run.
  - Before each run the database is restored from the template, and 200 other URLs (seed 7) warm the site up.
- **Machine.** AMD Ryzen 9 5950X (16 cores, 32 threads), Ubuntu 26.04, governor `performance`, boost on.
  - Each group of containers runs on whole cores ([scripts/cpus.sh](scripts/cpus.sh)): nginx, PHP-FPM and PgBouncer on 4 cores, PostgreSQL on 4 others, JMeter on 2.
  - The other CPUs were 1.8–2.9% busy during the runs.
- **Metric.** The CPU time of the containers' cgroups over the measured part of a run, divided by the 2,000 URLs.
  - Total CPU is nginx + PHP-FPM + PostgreSQL (+ PgBouncer). nginx takes 0.7–0.8 ms and is not shown separately.
  - The work also includes 8 logins and the comments.
  - Latency is the p50 and p99 of the 2,000 page requests.
- **Series.** 5 passes. Each pass runs every variant once: in the order of `VARIANTS` in odd passes, in reverse order in even passes ([scripts/drupal-series.sh](scripts/drupal-series.sh)).
  - The first series: 6 variants, the tables of the first two sections of Results.
  - The second series: the 4 variants without persistent connections, with its own A/A control.
  - A change is the median of the five per-pass ratios. The full tables give their minimum and maximum, which is not a confidence interval.
- **Checks recorded with every run** ([scripts/record.py](scripts/record.py)): HTTP status codes, new entries of Drupal's log (`watchdog`) by severity, the counters above, and the busy time of the other CPUs.
  - The database counters are read after 11 s without load, outside the measured part, because PostgreSQL publishes the statistics of an idle backend every 10 s.
  - In all 100 runs of both series every response was 200, and no `watchdog` entry was of severity warning or worse.

## Reproduce

The scripts here are the scripts of the runs, cleaned up afterwards. [Data](#data) lists the changes and how they were checked.

**Host:**
- Ubuntu 26.04 on x86-64 (the runs). `build.sh` builds the runtime image for the host's Ubuntu release. Other releases from 24.04 on were not tested.
- Docker without `sudo`: `sudo usermod -aG docker $USER`, then log in again. cgroup v2 with the systemd cgroup driver: `docker info -f '{{.CgroupDriver}}'` prints `systemd`.
- Port 127.0.0.1:58090 free.
- About 2 GB of disk for the sources, builds and the site, plus about 3 GB of Docker images.
- Packages:
  ```
  sudo apt install build-essential autoconf bison re2c pkg-config libxml2-dev libsqlite3-dev libssl-dev \
    zlib1g-dev libcurl4-openssl-dev libonig-dev libpq-dev libreadline-dev libargon2-dev libsodium-dev \
    libpng-dev libfreetype-dev git curl patch xz-utils python3
  ```
- **CPUs: 10 whole cores.** The setup needs 4 cores for the stack, 4 for PostgreSQL and 2 for JMeter. It was not tried with fewer.
  - The defaults in [scripts/cpus.sh](scripts/cpus.sh) are for the 5950X, where CPU n and n+16 are the two threads of one core.
  - On another machine, `lscpu -e` shows which CPUs share a core (column CORE). On Intel the two threads of a core are usually adjacent numbers. Leave out E-cores.
  - Change the three lists in `cpus.sh` before `setup.sh`. `setup.sh`, the series and `record.py` all read them from there.
- **CPU frequency.** `drupal-run.sh` refuses to run unless the CPU frequency settings are those of the runs: governor `performance`, energy_performance_preference `performance`, and boost on.
  - Its check reads files of the amd-pstate driver.
  - With intel_pstate, set the same with `echo performance | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor /sys/devices/system/cpu/cpu*/cpufreq/energy_performance_preference` and `echo 0 | sudo tee /sys/devices/system/cpu/intel_pstate/no_turbo`.
  - Then put `SKIP_GOVERNOR_CHECK=1` in front of the series commands.

**Steps.** Start in an empty directory. The first commands put three things side by side: php-src-bench, web-request-cost and the PHP tarball. All later commands run in `scripts/`, and all files are written there.
```
git clone https://github.com/ArtUkrainskiy/php-src-bench
git clone https://github.com/ArtUkrainskiy/web-request-cost && git -C web-request-cost checkout afd7ea6
curl -fLO https://www.php.net/distributions/php-8.5.11.tar.xz
echo 'd9be75c08e8c316f4c8f4194d8fbe1750a15f6a6d9d4e3fe72082abeeb800360  php-8.5.11.tar.xz' | sha256sum -c
cd php-src-bench/reports/pdo-pgsql-stmt-cache/scripts
WRC=../../../../web-request-cost PHP_TARBALL=../../../../php-8.5.11.tar.xz ./build.sh
./setup.sh
VARIANTS="base:native-persistent v3:native-persistent" PASSES=1 ./drupal-series.sh smoke.jsonl
VARIANTS="base:emulated base:emulated-persistent base:native-persistent base2:native-persistent v3:native-persistent v3:native" PASSES=5 ./drupal-series.sh direct.jsonl
BOUNCER=1 VARIANTS="base:emulated base:emulated-persistent base:native-persistent base2:native-persistent v3:native-persistent v3:native" PASSES=5 ./drupal-series.sh pgbouncer.jsonl
python3 table.py direct.jsonl; python3 table.py pgbouncer.jsonl
VARIANTS="base:emulated base:native base2:native v3:native" PASSES=5 ./drupal-series.sh no-persistent-direct.jsonl
BOUNCER=1 VARIANTS="base:emulated base:native base2:native v3:native" PASSES=5 ./drupal-series.sh no-persistent-pgbouncer.jsonl
```

1. **`build.sh`** builds `build-base` and `build-v3` (about a minute each on 32 threads) and the runtime images. It ends with:
   ```
   build-base: 8fd3b974b20a0b0f, pdo_pgsql.prepare_threshold=false pdo_pgsql.statement_cache_size=false
   build-v3: 23ef3bd3856f47c4, pdo_pgsql.prepare_threshold='5' pdo_pgsql.statement_cache_size='64'
   ```
   The hashes match only with the same compiler and packages. The INI values must match: `false` means that 8.5.11 has no such setting.
2. **`setup.sh`** takes about 15 minutes, and composer needs network access.
   - It leaves the container `drupal-bench-pg` running. The series need it; after a reboot, run `docker start drupal-bench-pg`.
   - Its `site.txt` should show the node, term and user counts of [data/site.txt](data/site.txt). The generated text, the comments and `nids.csv` differ, because devel_generate is not seeded.
3. **The smoke run** takes about 2 minutes. Each run prints the start of its JSON line, with `"codes": {"200": …}`.
   - A series stops at the first run that fails.
   - The logs of a run are in `runs/<label>/`: `fpm.log`, `php-error.log` and the JMeter logs.
4. **The series** take about 32 and 40 minutes for the first, 22 and 28 for the second: one run every 60–95 s.
5. **`table.py`** prints the tables of this report from your data. On another machine the absolute numbers differ, so compare the changes with your own A/A row.

**To clean up:** run `docker rm -f drupal-bench-pg drupal-bench-web; docker network rm drupal-bench`. Then remove `src`, `build-*`, `build-php-gd.sh`, `app`, `runs` and the generated `.csv`, `.txt` and `.jsonl` files in `scripts/`.

## Data

- **`data/direct.jsonl`, `data/pgbouncer.jsonl`:** the first series, one record per run. The fields are described at the top of [scripts/record.py](scripts/record.py); the builds there are named `base` (8.5.11), `base2` (the A/A copy) and `v3` (8.5.11 + cache). The runs started on 21 October 2026, between 01:44 and 02:55 UTC.
- **`data/no-persistent-direct.jsonl`, `data/no-persistent-pgbouncer.jsonl`:** the second series, the same fields. The runs started on 21 October 2026, between 05:38 and 06:28 UTC, with the same binaries.
- **`data/site.txt`:** the versions and row counts of the site that the runs started from.
- **The FPM binaries of the runs** (field `php_fpm_sha256`): `base` and `base2` `8fd3b974b20a0b0f…`, `v3` `23ef3bd3856f47c4…`. [stmt-cache-8.5.11.patch](stmt-cache-8.5.11.patch) applied to the php-8.5.11 tarball gives exactly the source tree of build `v3`.
- **The URL lists:** `make-urls.py 2000 42` gives sha256 `cb5a8e58001f3291…` and `make-urls.py 200 7` gives `99978edf132e1689…`, the same as in the runs.
- **Scripts changed after the first series.** The second series ran with the scripts of this directory. None of these changes alters what a run measures:
  - the CPU lists moved into `cpus.sh`, with the same defaults;
  - the nginx and JMeter images are pinned by the digests of the images used;
  - the runtime image is built for the host's Ubuntu release, which was 26.04 in the runs;
  - the governor check can be skipped;
  - the `build-base2` link is made by `drupal-run.sh` instead of `drupal-series.sh`;
  - `drupal-series.sh` stops at a failed run;
  - `setup.sh` refuses to run over an existing site and waits for PostgreSQL over TCP;
  - the default port of `editors.jmx` (the runs passed the port explicitly);
  - waits written with `sleep` instead of `read -t`, of the same length; lint fixes and comments;
  - `build.sh` and `table.py` were rewritten after the runs.

  `record.py` recomputes all 30 PgBouncer records of the first series identically from the raw files of the runs, and `make-urls.py` gives the same lists. `drupal-series.sh`, `drupal-run.sh` and `record.py` ran end to end in the second series; `build.sh` and `setup.sh` were not run again after these changes.

## Full tables

The change with the minimum and maximum of the five per-pass ratios. The first series, directly:

| comparison | total CPU | PHP-FPM | PostgreSQL | p50 |
|---|---:|---:|---:|---:|
| A/A: the same binary twice | −0.2% (−0.8…+1.4) | −0.4% (−1.0…+1.8) | −0.1% (−0.4…+0.4) | 0.0% (−1.2…+1.3) |
| native + patch against native, both persistent | −15.2% (−15.6…−14.4) | −6.3% (−7.2…−5.2) | −40.3% (−40.7…−39.4) | −15.2% (−16.2…−12.5) |
| native + patch against emulated, both persistent | −2.9% (−4.2…−1.7) | +2.0% (−0.2…+3.3) | −20.0% (−20.4…−18.4) | −2.9% (−6.9…−2.8) |
| native + patch against emulated, neither persistent | +1.3% (−0.4…+2.7) | +1.3% (−0.6…+3.9) | +0.2% (0.0…+1.4) | +1.2% (−1.2…+3.6) |
| native + patch, persistent, against emulated, not | −20.8% (−21.4…−20.4) | −5.6% (−7.2…−4.9) | −53.6% (−53.8…−52.6) | −19.3% (−21.2…−16.7) |
| no patch: emulated, persistent against not | −18.1% (−19.1…−17.8) | −7.1% (−8.3…−7.1) | −42.0% (−42.6…−41.5) | −15.3% (−17.6…−14.3) |

Through PgBouncer:

| comparison | total CPU | PHP-FPM | PostgreSQL | PgBouncer | p50 |
|---|---:|---:|---:|---:|---:|
| A/A: the same binary twice | −0.1% (−1.3…+1.2) | +0.1% (−0.2…+0.6) | −1.0% (−6.7…+7.8) | −0.2% (−1.0…+0.2) | −0.7% (−1.3…0.0) |
| native + patch against native, both persistent | −13.4% (−14.2…−12.8) | −6.9% (−7.3…−5.9) | −18.0% (−24.1…−17.2) | −31.0% (−31.3…−30.4) | −28.3% (−30.1…−27.6) |
| native + patch against emulated, both persistent | −1.8% (−1.9…−1.1) | +0.2% (−0.4…+0.9) | −15.4% (−15.7…−14.4) | +6.4% (+5.6…+7.6) | +2.8% (+0.9…+3.8) |
| native + patch against emulated, neither persistent | +0.3% (0.0…+1.4) | 0.0% (−0.4…+1.5) | −1.9% (−3.1…+0.1) | +3.9% (+3.5…+4.9) | +3.3% (+1.7…+4.2) |
| native + patch, persistent, against emulated, not | −5.5% (−6.0…−4.8) | −2.8% (−3.1…−1.6) | −15.4% (−15.7…−15.1) | −7.0% (−7.8…−6.6) | −9.2% (−10.1…−8.3) |
| no patch: emulated, persistent against not | −3.8% (−4.2…−3.4) | −2.5% (−3.3…−2.4) | 0.0% (−0.8…+0.5) | −12.8% (−13.1…−12.2) | −11.7% (−12.4…−10.0) |

The second series, directly:

| comparison | total CPU | PHP-FPM | PostgreSQL | p50 |
|---|---:|---:|---:|---:|
| A/A: the same binary twice | −0.3% (−0.6…+0.8) | −0.4% (−0.4…+0.9) | −0.1% (−1.2…+0.7) | 0.0% (−1.1…+1.1) |
| native + patch against native, neither persistent | −9.6% (−10.1…−9.3) | −5.7% (−6.1…−5.3) | −17.2% (−18.1…−16.4) | −8.5% (−9.7…−7.5) |
| native + patch against emulated, neither persistent | +0.7% (+0.2…+1.1) | +0.8% (+0.4…+1.8) | −0.1% (−1.0…+1.9) | +1.2% (0.0…+4.8) |

Through PgBouncer:

| comparison | total CPU | PHP-FPM | PostgreSQL | PgBouncer | p50 |
|---|---:|---:|---:|---:|---:|
| A/A: the same binary twice | −0.4% (−0.9…+0.5) | −0.7% (−0.8…+0.3) | 0.0% (−4.9…+6.5) | −0.1% (−0.3…+0.4) | +0.6% (−1.2…+0.6) |
| native + patch against native, neither persistent | −10.7% (−12.0…−10.2) | −6.7% (−7.6…−5.9) | −4.6% (−13.0…−1.7) | −28.6% (−29.4…−28.5) | −25.9% (−26.3…−24.7) |
| native + patch against emulated, neither persistent | +0.9% (−0.3…+1.9) | +0.7% (−0.4…+2.6) | −2.2% (−3.1…+0.9) | +3.5% (+2.1…+3.9) | +2.5% (+1.6…+3.3) |

## Not tested

- **Workload:**
  - other applications and frameworks, other Drupal versions and sites;
  - anonymous traffic with a page cache;
  - more than 64 frequently used statements per connection, where the table evicts statements that are still in use;
  - other numbers of FPM children and clients.
- **Settings:** other values of `prepare_threshold` and `statement_cache_size`; session pooling in PgBouncer and other values of `max_prepared_statements`.
- **Correctness:**
  - schema changes while the application runs;
  - the response bodies of the PDO modes against each other (the runs checked status codes and Drupal's log);
  - the session state that persistent connections carry between requests.
- **Code:** the prototype on master (only this port to 8.5.11). The patch has no tests of its own.
- **Not measured:**
  - the memory that cached statements hold in PostgreSQL backends and in PHP;
  - profiles of PostgreSQL and PHP;
  - the effect of code layout on the cache build. The A/A control is one binary, so it does not cover the layout of a second build.
