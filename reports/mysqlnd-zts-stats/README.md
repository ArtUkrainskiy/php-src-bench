# mysqlnd: relaxed atomics instead of a mutex for statistics in ZTS builds

In ZTS builds, every mysqlnd statistics update locks a mutex. The global statistics (`mysqlnd_global_stats`) are one object for the whole process, so all threads take the same mutex on every counted packet and row; the statistics are collected by default (`mysqlnd.collect_statistics=1`). [mysqlnd-stats-atomic.patch](mysqlnd-stats-atomic.patch) makes the counters `atomic_uint_least64_t` under ZTS, updated with `atomic_fetch_add_explicit(..., memory_order_relaxed)` and read with `atomic_load_explicit`, and removes the mutex. NTS builds are unchanged.

- Base: php-src master [`b7256eee301`](https://github.com/php/php-src/commit/b7256eee3018928d265830e5f523dcc848dea2b6) (18 October 2026).
- Change: the patch on top of it, commit `a43cc05effb` (php/php-src#24448). It adds to `757907bb42f` only the `atomic_init()` of every counter in `mysqlnd_stats_init()` under ZTS, which runs once per statistics object, when it is created; the measurements, the counts and the objdump comparisons below ran on the tree of `757907bb42f`, the tests and the C/C++ test also on `a43cc05effb`. Earlier commits of the tree of `757907bb42f`, which differ only in the commit message, are `354bc4f4ce3`, on which the tests, the `--enable-werror` builds and the counts ran, and `f5b26235f2d`, after which the measured build is named `php-atomic-f5b2623`. The tests and the exact counts were run on `354bc4f4ce3` and, earlier, on `dc7779b2ae5`: the same C code without the `UPGRADING.INTERNALS` entry, with the C++ declarations in `Zend/zend_portability.h` instead of `ext/mysqlnd/mysqlnd_structs.h`, and with one more comment line in `mysqlnd_driver.c`.

The same measurement on a full JSON API, with PHP 8.5.11 and a prototype of the change, is in [web-request-cost](https://github.com/ArtUkrainskiy/web-request-cost/tree/ba122ac9e4feae2d883d4a815720cd4d264b32cd/results/2026-10-mysqlnd).

## Setup

- **Machine:** AMD Ryzen 9 5950X (two CCDs of 8 cores, each with its own L3), Ubuntu 26.04, kernel 7.0, governor `performance`, GCC 15.2.
- **Builds:** PHP ZTS embed with the flags of the official Docker image (`-O2 -fstack-protector-strong -fpic -fpie`, [scripts/build.sh](scripts/build.sh)), FrankenPHP 1.13.1 built against it, worker mode, 16 PHP threads, run natively.
- **FrankenPHP and master:** FrankenPHP 1.13.1 does not build against master as is. It uses `zend_atomic_bool`, removed in [#23927](https://github.com/php/php-src/pull/23927), and initialises the `terminate_process` SAPI member, removed in [#23524](https://github.com/php/php-src/pull/23524). `build.sh` replaces `zend_atomic_bool` and its load and store calls with `atomic_bool`, `atomic_store` and `atomic_load` and drops the initializer line, the same for both builds.
- **Database and load:** MySQL 8.4.11 in Docker, `wrk -t4 -c50`.
- **Workload:** [repro/](repro), one prepared `SELECT` of 20 rows of a 1000-row table per request. PDO runs with emulated prepares (text protocol, PDO's default) or with `PDO::ATTR_EMULATE_PREPARES => false` (binary protocol).
- **Metrics:** per request for the FrankenPHP process (all threads), over 20 s per pass:
  - CPU time: user + system from `/proc/<pid>/stat`;
  - cycles and instructions: `perf stat -p`, user and kernel.
- **Passes:** the four variants (master and patch, statistics on and off) alternate within each pass, in reverse order on even passes ([scripts/measure.sh](scripts/measure.sh)).
- **Aggregation:** median of the passes; a change is the median of the per-pass ratios, with their range ([scripts/aggregate.py](scripts/aggregate.py)).

## Results

### Where the threads run

Text protocol. FrankenPHP's 16 threads on 4 or 8 cores (with their SMT siblings), on one CCD or split evenly over both. The cost of statistics is statistics on against statistics off of the same build:

| FrankenPHP cores | passes | master, on | master, off | cost on master | patch, on | cost with the patch |
|---|---:|---:|---:|---:|---:|---:|
| 4, one CCD | 15 | 0.3029 ms | 0.2705 ms | +12.1% | 0.2722 ms | +0.6% |
| 4, two on each CCD | 10 | 0.3553 ms | 0.2897 ms | +22.7% | 0.2934 ms | +1.4% |
| 8, one CCD | 10 | 0.3810 ms | 0.2714 ms | +40.8% | 0.2739 ms | +0.8% |
| 8, four on each CCD | 10 | 0.5274 ms | 0.2747 ms | +90.9% | 0.2781 ms | +1.0% |

The cost on master grows with both factors:
- **More cores:** more threads hold or wait for the mutex at the same time.
- **The split over CCDs:** at the same number of cores, it roughly doubles the cost (+12% → +23% on 4 cores, +41% → +91% on 8).

On 8 cores split over both CCDs, throughput drops from 28,855 to 21,450 req/s.

Cycles and instructions behind the cost on master:

| FrankenPHP cores | cycles | instructions |
|---|---:|---:|
| 4, one CCD | +12.4% | +11.9% |
| 4, two on each CCD | +22.9% | +14.5% |
| 8, one CCD | +41.7% | +21.7% |
| 8, four on each CCD | +90.6% | +31.9% |

The instructions grow with contention too, as they include the kernel's `futex` path. The cycles grow faster than the instructions, which is consistent with threads waiting for the mutex's cache line; that was not traced separately.

With the patch, the cost is 0.6–1.4% in the median in every placement. Two kinds of updates remain:
- the additions on the global counters, which all threads share;
- about 350 uncontended `lock add` per request on the per-connection counters, which only the thread that owns the connection touches.

The per-pass ratios of patch on to patch off range from about −10% to +14% because of the two states described below. The medians are what is stable.

Placements, as CPU lists:

| FrankenPHP | MySQL | `wrk` |
|---|---|---|
| 4 cores, one CCD: 8–11, 24–27 | 0–5, 16–21 | 6–7, 22–23 |
| 4 cores, two on each CCD: 6–9, 22–25 | 0–5, 16–21 | 12–13, 28–29 |
| 8 cores, one CCD: 8–15, 24–31 | 0–5, 16–21 | 6–7, 22–23 |
| 8 cores, four on each CCD: 4–11, 20–27 | 0–3, 16–19 | 12–15, 28–31 |

### Both protocols, one CCD

| protocol | passes | statistics | master | patch | change |
|---|---:|---|---:|---:|---:|
| text | 15 | on (default) | 0.3029 ms, 1.30 M cycles | 0.2722 ms, 1.17 M cycles | −10% (−18% to −3.5%) |
| | | off | 0.2705 ms, 1.16 M cycles | 0.2703 ms, 1.16 M cycles | 0% |
| binary | 5 | on (default) | 0.3712 ms, 1.58 M cycles | 0.3292 ms, 1.39 M cycles | −11% (−19% to −11%) |
| | | off | 0.3271 ms, 1.39 M cycles | 0.3027 ms, 1.27 M cycles | −7% (−9% to +9%)¹ |

Cost of statistics with the binary protocol: +13.9% on master, +1.4% with the patch.

¹ With statistics off both builds run the same code. In the 5 binary passes the patch was in the faster state in 3 passes and master in 1, which moves the medians apart. With 10 and 15 passes the two builds are within 0.3% of each other with statistics off.

### Two states

Most variants of both builds fall into one of two states from pass to pass. For example, with statistics off on 4 cores of one CCD, a pass takes about 1.05 M or 1.16 M cycles and 658 k or 722–723 k instructions per request. Master with statistics on is the exception: it stays in one state in all 5 binary passes and in 14 of the 15 text passes on one CCD. The instructions differ between the states, so it is not only the clock frequency. The cause is not known. This is why the per-pass ranges are wide while the medians over 5–15 passes are stable.

Raw output in [data/](data):
- [series-a-one-ccd-text.txt](data/series-a-one-ccd-text.txt);
- [series-b-two-ccds-text.txt](data/series-b-two-ccds-text.txt) (8 cores, four on each CCD);
- [series-c-one-ccd-binary.txt](data/series-c-one-ccd-binary.txt);
- [series-d-four-cores-two-ccds-text.txt](data/series-d-four-cores-two-ccds-text.txt);
- [series-e-eight-cores-one-ccd-text.txt](data/series-e-eight-cores-one-ccd-text.txt).

## How many locks

[repro/count-locks.sh](repro/count-locks.sh) runs the official image `dunglas/frankenphp:1.13-php8.5.11` ([repro/Dockerfile](repro/Dockerfile)), so PHP 8.5.11, not the master builds above. It uses 16 PHP threads, statistics on and off, two passes of 10 s. bpftrace counts a uprobe on `pthread_mutex_lock` in the FrankenPHP process and the `futex` syscall tracepoint ([data/locks.txt](data/locks.txt), raw maps in [data/locks-raw/](data/locks-raw)).

- **Statistics on:** 722.74 and 722.78 `pthread_mutex_lock` calls per request in the two passes. In the first pass, 371.38 per request are on one mutex shared by all threads (the global statistics) and 351.36 on 16 others, one per thread (the connection statistics).
- **`collect_statistics=0`:** no `pthread_mutex_lock` calls.
- **`futex`:** the address with the most `futex` calls is the shared mutex, 34–38 calls per request. None of the 16 per-thread mutexes is among the 20 addresses with the most `futex` calls.
- **Tracing overhead:** tracing slows the server to about 4,400 req/s from about 22,000. The `futex` counts show where the contention is, not how much of it there is without tracing.

## Correctness

- **Exact counts under concurrency.** [scripts/counts.sh](scripts/counts.sh) sends exactly 50,000 requests, 50 at a time, to FrankenPHP with 16 threads and statistics on. It compares `mysqli_get_client_stats()` before and after ([data/counts.txt](data/counts.txt)). These builds have ext/mysqli for that function; the requests use PDO.

  | build | `com_query` | `rows_fetched_from_server_normal` |
  |---|---:|---:|
  | master | 50,000 | 1,000,000 |
  | the patch (`354bc4f4ce3`'s tree) | 50,000 | 1,000,000 |
  | [racy-mutant.patch](racy-mutant.patch): `atomic_store(atomic_load() + value)` | 49,460 | 997,554 |

  The racy variant loses about 1% of the updates, so the check can see lost updates. An earlier run on `dc7779b2ae5` gave the same exact counts, and 49,515 and 997,782 for the racy variant ([data/counts-dc7779b.txt](data/counts-dc7779b.txt)).
- **Tests.** `ext/mysqlnd`, `ext/mysqli` and `ext/pdo_mysql` ran on ZTS debug builds against MySQL 8.4.11 ([scripts/run-tests.sh](scripts/run-tests.sh), [data/tests.txt](data/tests.txt)): 796 tests, 28 skipped.
  - Master, `354bc4f4ce3` and `a43cc05effb`: 763 passed, 4 expected to fail, 1 failed ([data/tests-a43cc05.txt](data/tests-a43cc05.txt) for the last).
  - The failure on both is `pdo_mysql___construct.phpt`, because of the local DSN setup.
  - `--with-openssl` is needed for `caching_sha2_password`.
- **`--enable-werror` builds.** `354bc4f4ce3`: GCC 13.3 and clang 18.1, ZTS and NTS; `a43cc05effb`: GCC 13.3 and clang 18.1, ZTS (its addition is ZTS-only) ([data/](data), `werror-*.log`).
- **NTS is unchanged.** [scripts/nts-objdump.sh](scripts/nts-objdump.sh) compares the 455 functions whose debug information points into `ext/mysqlnd/`, with addresses normalized. NTS master and the patch: 0 differing lines (GCC 13.3, Docker flags). The same script on NTS master against the ZTS patch build finds 5,049 differing lines ([data/nts-objdump.txt](data/nts-objdump.txt)).
- **Hot function.** `php_mysqlnd_rowp_read_text_protocol` has 4 `tsrm_mutex_lock` calls on master and 4 `lock`-prefixed instructions and no calls with the patch ([data/hot-function-objdump.txt](data/hot-function-objdump.txt)).
- **C++.** [scripts/cxx-test.cpp](scripts/cxx-test.cpp) includes `php.h`, `mysqlnd.h` and `mysqlnd_statistics.h` and uses `MYSQLND_INC_STATISTIC`, `MYSQLND_INC_STATISTIC_W_VALUE2`, `MYSQLND_DEC_STATISTIC` and `MYSQLND_INC_GLOBAL_STATISTIC`. Under ZTS it compiles with g++ 13 and clang++ 18 and 20 in C++11, C++17 and C++20, and emits only `lock`-prefixed additions ([data/cxx-test.txt](data/cxx-test.txt)). The command, in a configured and built ZTS tree `<tree>` of the patch:

  ```sh
  g++ -std=c++17 -O2 -DZTS -I<tree> -I<tree>/main -I<tree>/Zend -I<tree>/TSRM -I<tree>/ext -c cxx-test.cpp && objdump -d cxx-test.o | grep 'lock '
  # clang++ needs a C++ standard library it can find, here GCC 13's: --gcc-install-dir=/usr/lib/gcc/x86_64-linux-gnu/13
  ```

  mysql_xdevapi itself was not built against the patch.
- **C and C++ share the struct.** [scripts/xlang-c.c](scripts/xlang-c.c) and [scripts/xlang-cxx.cpp](scripts/xlang-cxx.cpp), with the headers of `a43cc05effb` under ZTS: C and C++ see the same `sizeof(struct st_mysqlnd_stats)`, `offsetof(values)` and element size and alignment (all 8); counters allocated and initialized in C, updated with `MYSQLND_STATS_UPDATE_VALUE()` from 8 C++ threads 1,000,000 times each and read back in C are exact (8,000,000 and 24,000,000). GCC 13.3, clang 18.1 and 20.1, C++11, C++17 and C++20, 9 of 9 ([data/xlang-layout.txt](data/xlang-layout.txt)). With the C++ update made a non-atomic load and store, C reads 6,290,537 instead of 8,000,000. Built like the C++ test above: `gcc -std=c11 -O2 -DZTS <includes> -c xlang-c.c`, `g++ -std=c++17 -O2 -DZTS <includes> -c xlang-cxx.cpp`, linked with `g++ ... -pthread`.
- clang++ warns `'counted_by' attribute ignored` on `values[]` when a C++ file includes `mysqlnd_structs.h`; it does so on master as well.

## Not tested

- Windows: x86 ZTS, and MSVC compiling the header as C++ (a flexible array of `std::atomic`).
- 32-bit Linux builds of PHP. A standalone C11 file with the same type compiles with `gcc -m32` and `clang -m32` to inline `lock cmpxchg8b` without libatomic.
- Targets without lock-free 64-bit atomics (32-bit ARM, MIPS, PowerPC) may need libatomic.
- ARM64, more than one socket, other ZTS servers (Apache with a threaded MPM, ext/parallel), TSan.

## Run it again

```sh
SRC=/path/to/php-src                     # a clone with b7256eee301
cd scripts
git -C $SRC archive --prefix=php-master-b7256ee/ b7256eee301 | gzip > php-master-b7256ee.tar.gz
git -C $SRC worktree add /tmp/atomic b7256eee301 && git -C /tmp/atomic am "$PWD/../mysqlnd-stats-atomic.patch"
git -C /tmp/atomic archive --prefix=php-atomic-f5b2623/ HEAD | gzip > php-atomic-f5b2623.tar.gz
git -C /tmp/atomic apply "$PWD/../racy-mutant.patch"
(cd /tmp && tar czf "$OLDPWD/php-mutant-racy.tar.gz" --transform 's|^atomic|php-mutant-racy|' --exclude=.git atomic)
export FRANKENPHP_SRC=/path/to/frankenphp-1.13.1   # the release's source tree
for b in php-master-b7256ee php-atomic-f5b2623 php-mutant-racy; do
	./build.sh $b; EXTRA_CONFIGURE=--with-mysqli ./build.sh $b mysqli
done
docker build -t mysqlnd-zts-repro ../repro
PASSES=15 TAG=A ./measure.sh
APP_CPUS=4-11,20-27 LOAD_CPUS=12-15,28-31 DB_CPUS=0-3,16-19 PASSES=10 TAG=B ./measure.sh
PREPARES=native PASSES=5 TAG=C ./measure.sh
APP_CPUS=6-9,22-25 LOAD_CPUS=12-13,28-29 PASSES=10 TAG=D ./measure.sh
APP_CPUS=8-15,24-31 PASSES=10 TAG=E ./measure.sh
python3 aggregate.py results-*.txt
./counts.sh php-master-b7256ee-mysqli php-atomic-f5b2623-mysqli php-mutant-racy-mysqli
cd ../repro && sudo ./count-locks.sh
```

`run-tests.sh` expects MySQL 8.4 on 127.0.0.1:53306 with user root, password `bench` and a database `test`, for example `docker run -d -p 127.0.0.1:53306:3306 -e MYSQL_ROOT_PASSWORD=bench -e MYSQL_DATABASE=test mysql:8.4.11`.
