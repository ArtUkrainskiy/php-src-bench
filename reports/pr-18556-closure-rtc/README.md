# Shared run-time cache for closures under opcache (php-src PR #18556, GH-10782)

Review material for [php/php-src#18556](https://github.com/php/php-src/pull/18556) by arnaud-lb (branch [`gh10782`](https://github.com/arnaud-lb/php-src/tree/gh10782)), which fixes [GH-10782](https://github.com/php/php-src/issues/10782). The PR no longer merges into master, so I ported it by hand ([`pr18556.diff`](pr18556.diff)). Master has changed the signature of `zend_create_closure_ex()` since then, and that's the only difference.

With opcache, every closure created inside a class method starts with an empty run-time cache. Laravel creates a few hundred such closures per request, and observer extensions such as OpenTelemetry set up their per-function state again for each one. The PR lets these closures share one cache.

## Summary

- **The bug is real on a framework.** On Laravel `/`, 260 of the 288 closures created per request get a fresh cache on master. With the PR it's 4. On `/users` it's 694 of 723 → 4.
- **Observers.** In a Laravel worker loop with OpenTelemetry, observer initializations drop from 187 to 4.3 per HTTP request, and the loop takes 1.3% fewer cycles than master. On normal requests the drop is small (1,556 → 1,486 on `/`), because every function is initialized again on each request anyway. Extensions don't need changes.
- **Elsewhere the PR is slower than master.** 9 of the 12 results take 0.4–1.5% more cycles: GCC +0.5% to +1.5%, clang +0.4% to +0.5%, GCC with OpenTelemetry +1.0% to +1.2%. Instructions go down by 0.1–1.0% in every row.
- **The extra cycles come from code placement.** With GCC the PR moves all code linked after `zend_closures.c` by 128 bytes. The *placement build*, master plus a never-called function that makes the same move, costs 0.5–1.6% on its own. Master against itself stays within 0.2%. Against the placement build the PR is −0.8% to +0.6%, and the sign differs between the two series I ran. I tried moving the allocation into a cold function: it halves the move, but it's still +0.2% to +1.1% against master.
- **Correctness:** the PR's observer test fails on master with opcache and passes with the PR. Other test results are the same as master, also under ASan/UBSan. One code issue: arithmetic on `void *`, which MSVC most likely rejects. Not tested: ZTS, JIT, Windows, Intel, PHP-FPM ([full list](#not-tested)).
- **Side finding:** loading OpenTelemetry costs 8–18% of cycles here. A 3-line change in OpenTelemetry saves up to 4.9% ([OpenTelemetry](#opentelemetry)).

## What changes

`zend_create_closure_ex()` reuses the declaration's run-time cache only if the closure's scope equals `func->common.scope`. Without opcache, the first creation stores the scope there and later creations share the cache. With opcache, the declaration is immutable and its scope stays NULL, while `ZEND_DECLARE_LAMBDA_FUNCTION` passes the method's class. So each creation `emalloc()`s a private, zeroed cache. The observer API keeps each function's observer handlers in that cache, so it calls the observer extensions' init again for each new closure object on its first call.

The PR stores the scope in an extra slot in front of the shared cache and compares against it. A different scope still gets a private cache.

## Results

Change in CPU cycles per request, PR against master (negative = fewer cycles). Main series, median of 10 alternating passes, 8 for the worker. Master against itself: −0.04% to +0.18% at the median, single passes −0.9% to +1.5%.

| page | master, cycles per request (GCC) | GCC 15.2 | clang 21.1 | GCC, OpenTelemetry loaded |
|---|--:|--:|--:|--:|
| Laravel `/` (Blade welcome page) | 8.5 M | +0.5% | +0.5% | +1.2% |
| Laravel `/users` (100 Eloquent models as JSON) | 57.7 M | +1.3% | −0.6% | +1.0% |
| Symfony Demo `/en/blog/` | 29.8 M | +1.5% | +0.4% | +1.1% |
| Laravel worker loop, per HTTP request | 27.4 M | +0.7% | −0.6% | −1.3% |

Instructions: −0.1% to −0.5%, with OpenTelemetry −0.3% to −1.0%.

Memory ([`data/memory.txt`](data/memory.txt)): peak request memory is 8–10 KB lower on `/users` and Symfony Demo and 50 KB higher on Laravel `/`. The PR puts the shared caches into the compiler arena, which grows in 64 KB blocks. On `/` it fills the first block sooner, so the second one is allocated before the page copies its 70 KB output buffer, not after. Memory in use at the end of the request is 5–9 KB lower on all three pages. Memory taken from the system and the worker loop's memory don't change.

Counts per request, from callgrind ([`data/callgrind-counts.txt`](data/callgrind-counts.txt)):

| | before | PR |
|---|--:|--:|
| Laravel `/`: closures created / with a fresh cache (master) | 288 / 260 | 288 / 4 |
| Laravel `/users`: closures created / with a fresh cache (master) | 723 / 694 | 723 / 4 |
| Laravel `/`: observer initializations (placement build, OpenTelemetry) | 1,556 | 1,486 |
| Laravel `/users`: observer initializations (placement build, OpenTelemetry) | 2,070 | 1,805 |
| worker loop: observer initializations per HTTP request (placement build, OpenTelemetry) | 187 | 4.3 |

Observer counts are from the placement build, which runs the same code as master. The 4 fresh caches left with the PR are 3 closures that laravel/serializable-closure rebuilds through its `laravel-serializable-closure://` stream wrapper and binds back to their scope. The fourth is Composer's autoloader initializer, which `Closure::bind()` binds to another class ([`data/fresh-caches-pr.txt`](data/fresh-caches-pr.txt)).

## Code placement

The PR adds 112 bytes of code to `zend_closures.c` with GCC (48 with clang), and everything linked after it moves by 128 bytes (48 with clang), `execute_ex` included. The *placement build* is master plus a never-called function in that file that makes the same move ([`placement-gcc15.diff`](placement-gcc15.diff), [`placement-clang21.diff`](placement-clang21.diff)). Its `execute_ex` and `zend_hash_find` have the same addresses as in the PR build ([`data/nm.txt`](data/nm.txt)). The *cold* build is the PR with the cache allocation moved into a `ZEND_COLD` function ([`pr18556-cold.diff`](pr18556-cold.diff)). It moves `execute_ex` by 64 bytes.

GCC, change in cycles per request, main series:

| page | master → placement | placement → PR | master → PR | master → cold | placement → PR, earlier series |
|---|--:|--:|--:|--:|--:|
| Laravel `/` | +0.5% | +0.5% | +0.5% | +0.5% | −0.8% |
| Laravel `/users` | +1.6% | −0.2% | +1.3% | +0.2% | −0.4% |
| Symfony Demo | +1.0% | +0.6% | +1.5% | +1.1% | −0.3% |

On `/users` and Symfony Demo that is well above master against itself. Master → placement changes instructions by less than 0.01%. Placement → PR and master → cold change them by −0.1% to −0.5%.

L1 instruction-cache misses per request on Symfony Demo: 84 thousand on master, 90 thousand on the placement build, 92 thousand with the PR ([`data/l1i-3way.txt`](data/l1i-3way.txt)). An earlier run showed 109 thousand for the PR and didn't repeat ([`data/l1i-master-pr-run1.txt`](data/l1i-master-pr-run1.txt)).

## Review notes

1. `zend_arena_alloc(...) + extra_slot_size` adds to a `void *`. That's a GNU extension, and I think MSVC rejects it (not tried). Alternative: `(void **) zend_arena_alloc(&CG(arena), func->op_array.cache_size + extra_slot_size) + 1`.
2. The branch conflicts with master: `zend_create_closure_ex()` now takes `zend_object *this_ptr` and `uint32_t flags`.
3. The new code reads `ptr[-1]`, so only `zend_create_closure_ex()` may set a closure declaration's run-time cache. I checked the other writers (`init_func_run_time_cache()`, JIT helpers, `Closure::call()`): none of them gets the declaration.
4. One scope slot is enough here. A cache per scope would only help the 4 closures per request bound to another class.

## OpenTelemetry

[opentelemetry-php-instrumentation](https://github.com/open-telemetry/opentelemetry-php-instrumentation) with default settings, plus 20 empty hooks ([`otel-hooks.php`](otel-hooks.php)) on classes that the Laravel, Symfony and PDO auto-instrumentation packages hook. Earlier series:

| | Laravel `/` | Laravel `/users` | Symfony Demo |
|---|--:|--:|--:|
| loading OpenTelemetry, cycles | +18.3% | +7.8% | +8.8% |
| skipping its `WithSpan` lookup when attribute hooks are off, cycles | −4.9% | −0.9% | −1.8% |

On every observer initialization of a named function the extension looks for a `WithSpan` attribute on the function and its interface methods. It uses the result only when `opentelemetry.attr_hooks_enabled` or `opentelemetry.display_warnings` is on, and both are off by default. [`otel-lazy-withspan.diff`](otel-lazy-withspan.diff) skips the lookup in that case.

## Full tables

From [`summary.py`](summary.py). Each row compares B against A in the same pass: median of the per-pass ratios (min…max). A is the first build in the name; `otel-cost`: A is the placement build, B the same with OpenTelemetry; `otel-lazy`: A with OpenTelemetry, B with the lazy patch.

Main series ([`data/main/`](data/main/)):

| row | A, cycles per request | cycles | instructions |
|---|--:|--:|--:|
| `gcc-master-pr-lar-home` | 8,546,252 | +0.50% (−1.64…+1.43) | −0.49% |
| `gcc-master-pr-lar-users` | 57,732,136 | +1.25% (+0.39…+2.66) | −0.12% |
| `gcc-master-pr-sf-list` | 29,799,492 | +1.48% (+1.09…+1.78) | −0.11% |
| `clang-master-pr-lar-home` | 8,469,800 | +0.50% (−0.44…+1.12) | −0.48% |
| `clang-master-pr-lar-users` | 56,970,038 | −0.60% (−1.21…−0.15) | −0.11% |
| `clang-master-pr-sf-list` | 29,648,050 | +0.43% (−0.66…+0.74) | −0.10% |
| `otel-master-pr-lar-home` | 9,934,859 | +1.18% (+0.26…+5.25) | −1.01% |
| `otel-master-pr-lar-users` | 61,803,152 | +0.99% (+0.46…+1.81) | −0.46% |
| `otel-master-pr-sf-list` | 32,446,348 | +1.08% (+0.64…+1.90) | −0.34% |
| `worker-master-pr` | 27,352,938 | +0.70% (−0.14…+2.85) | −0.14% |
| `worker-otel-master-pr` | 29,211,105 | −1.28% (−3.38…+0.17) | −0.59% |
| `worker-clang-master-pr` | 26,806,322 | −0.64% (−2.73…+0.12) | −0.14% |
| `gcc-master-placement-lar-home` | 8,501,494 | +0.46% (−2.12…+1.43) | +0.00% |
| `gcc-master-placement-lar-users` | 57,570,252 | +1.58% (+0.40…+2.43) | +0.00% |
| `gcc-master-placement-sf-list` | 29,790,415 | +1.01% (+0.43…+1.45) | +0.00% |
| `gcc-placement-pr-lar-home` | 8,514,549 | +0.46% (−0.74…+0.71) | −0.48% |
| `gcc-placement-pr-lar-users` | 58,414,503 | −0.18% (−0.70…+0.96) | −0.12% |
| `gcc-placement-pr-sf-list` | 30,046,194 | +0.63% (+0.01…+0.98) | −0.11% |
| `gcc-master-cold-lar-home` | 8,459,892 | +0.51% (−0.52…+1.13) | −0.47% |
| `gcc-master-cold-lar-users` | 57,613,915 | +0.21% (−0.96…+1.42) | −0.12% |
| `gcc-master-cold-sf-list` | 29,798,574 | +1.07% (+0.46…+1.28) | −0.11% |
| `gcc-master-master-lar-home` | 8,469,107 | −0.04% (−0.66…+1.54) | +0.00% |
| `gcc-master-master-lar-users` | 57,605,246 | +0.18% (−0.73…+1.08) | +0.00% |
| `gcc-master-master-sf-list` | 29,809,517 | +0.04% (−0.87…+0.33) | +0.00% |
| `worker-master-master` | 27,319,236 | +0.10% (−0.42…+0.98) | +0.00% |

Earlier series ([`data/earlier/`](data/earlier/)):

| row | A, cycles per request | cycles | instructions |
|---|--:|--:|--:|
| `gcc-master-pr-lar-home` | 8,465,565 | +0.13% (−0.59…+0.86) | −0.49% |
| `gcc-master-pr-lar-users` | 57,693,469 | +0.74% (−0.05…+1.60) | −0.12% |
| `gcc-master-pr-sf-list` | 29,782,278 | +0.97% (+0.52…+2.02) | −0.11% |
| `gcc-master-placement-sf-list` | 29,840,189 | +0.77% (+0.22…+1.68) | +0.00% |
| `gcc-placement-pr-lar-home` | 8,545,169 | −0.82% (−1.59…−0.04) | −0.49% |
| `gcc-placement-pr-lar-users` | 58,283,130 | −0.45% (−0.83…+0.86) | −0.12% |
| `gcc-placement-pr-sf-list` | 30,100,946 | −0.27% (−0.71…+0.56) | −0.11% |
| `clang-placement-pr-lar-home` | 8,453,196 | −0.18% (−0.73…+0.13) | −0.48% |
| `clang-placement-pr-lar-users` | 56,275,513 | +0.00% (−0.77…+0.98) | −0.12% |
| `clang-placement-pr-sf-list` | 29,570,153 | −0.57% (−0.86…+0.41) | −0.10% |
| `otel-placement-pr-lar-home` | 10,044,923 | −0.81% (−1.80…+0.03) | −1.01% |
| `otel-placement-pr-lar-users` | 62,725,911 | −0.87% (−1.56…−0.11) | −0.46% |
| `otel-placement-pr-sf-list` | 32,708,856 | −0.19% (−0.79…+0.42) | −0.35% |
| `worker-placement-pr` | 27,329,531 | −0.94% (−2.52…+1.26) | −0.14% |
| `worker-otel-placement-pr` | 29,001,521 | −1.45% (−1.88…−0.33) | −0.59% |
| `worker-otel-lazy-placement-pr` | 28,853,325 | −0.60% (−1.46…+0.08) | −0.44% |
| `otel-cost-lar-home` | 8,534,108 | +18.29% (+15.88…+19.37) | +26.45% |
| `otel-cost-lar-users` | 58,255,494 | +7.79% (+5.08…+8.91) | +10.83% |
| `otel-cost-sf-list` | 30,129,650 | +8.82% (+7.99…+10.90) | +11.25% |
| `otel-lazy-lar-home` | 10,071,618 | −4.90% (−5.63…−4.05) | −4.87% |
| `otel-lazy-lar-users` | 62,681,371 | −0.88% (−2.89…+0.25) | −0.77% |
| `otel-lazy-sf-list` | 32,754,866 | −1.78% (−2.19…−1.01) | −1.20% |

## Machine and method

- AMD Ryzen 9 5950X, Ubuntu 26.04, governor `performance`, measured processes pinned to CPU 9. GCC 15.2 and clang 21.1 with the official Docker image flags, NTS ([`build.sh`](build.sh)).
- Pages: `php-cgi -T` ([`cgi.sh`](cgi.sh)) runs the full request startup and shutdown for each request. opcache on without timestamp checks, JIT off. [`ab-cgi.sh`](ab-cgi.sh) divides `perf stat` cycles of the whole process by the number of measured requests. Startup and the warm-up requests are in the numerator, the same on both sides, so absolute cycles per request are at least 5–8% high.
- Worker loop: [`worker.php`](worker.php) boots Laravel once and serves `/`, `/users` and `/users?page=2` in turn through the HTTP kernel. [`ab-worker.sh`](ab-worker.sh) takes (1,000 requests − 200 requests) / 800, so the boot cancels out.
- Each pass runs both builds once, and the order alternates between passes (A B, B A, …). Each table or column compares rows of one series, the one it names.
- Counts: callgrind, [`count.sh`](count.sh) and [`count-worker.sh`](count-worker.sh). A fresh cache is an `_emalloc()` call under `zend_create_closure_ex()`.
- Applications ([`apps.sh`](apps.sh)): Laravel 13 skeleton with a fixed lock file, SQLite, production mode with caches. Symfony Demo at a fixed commit, prod mode. Any code that creates closures in class methods under opcache takes the same path.

## Output verification

- `run-tests.php` with opcache off and on ([`data/tests.txt`](data/tests.txt)): `Zend/tests`, `ext/opcache/tests`, `ext/reflection/tests` and `ext/zend_test/tests` on release builds; `ext/zend_test/tests` and `Zend/tests/closures` with zend_test loaded; the four directories with zend_test loaded on ASan/UBSan debug builds. The PR fails the same tests as master, except the PR's `observer_closure_04.phpt`: it fails on master with opcache and passes with the PR. No ASan or UBSan reports. The cold build, four directories with zend_test loaded, fails the same tests as the PR.
- The three pages return the same body on master, placement and PR builds ([`data/output-hashes.txt`](data/output-hashes.txt)).

## Not tested

ZTS, JIT, preload, `opcache.file_cache_only`, Windows/MSVC, Intel, PHP-FPM and Octane servers, other observer extensions.

## Reproduce

In this directory, about 2 hours in total. Quick check: step 1 for master and PR, step 2, step 6.

1. **Builds**, about 5 minutes each:
   ```
   for b in master placement pr cold; do ./build.sh $b gcc15; done
   for b in master placement pr; do ./build.sh $b clang21; done
   ./build.sh master gcc15 asan; ./build.sh pr gcc15 asan    # tests only
   ```
   Placement and PR builds of one compiler must print the same `execute_ex` address. If not, change the `.skip` count in `placement-<cc>.diff` by the difference, `rm -rf builds/placement-<cc>` and build it again.
2. **Applications**, needs network and Composer:
   ```
   ./apps.sh builds/master-gcc15/sapi/cli/php composer.phar
   ```
   Symfony Demo's `asset-map:compile` needs `api.iconify.design`. It timed out on my recheck, so the Symfony part of `apps.sh` is checked only on the original setup.
3. **OpenTelemetry:** `./otel.sh builds/placement-gcc15; ./otel.sh builds/placement-gcc15 lazy`
4. **Machine:** `sudo sysctl kernel.perf_event_paranoid=-1`, an idle core with an idle SMT sibling.
5. **Series**, about 35 minutes: `CPU=9 ./series.sh data-new` (all groups), then `python3 summary.py data-new`. Compare percentages, not cycles: with GCC 15.2 and clang 21.1 instructions should change by the same amount, cycles depend on the CPU.
6. **Counts**, a few minutes each:
   ```
   ./count.sh builds/master-gcc15/sapi/cgi/php-cgi $PWD/apps/laravel/public / cg/master-home
   ./count.sh builds/pr-gcc15/sapi/cgi/php-cgi $PWD/apps/laravel/public / cg/pr-home
   ```
   Expected: 288 calls of `zend_create_closure_ex`, 260 `_emalloc` under it on master, 4 with the PR. For observer counts add `-d extension=$PWD/builds/placement-gcc15/opentelemetry.so -d auto_prepend_file=$PWD/otel-hooks.php`; for the worker loop use `count-worker.sh`.
7. **Tests**, for each build `b` and `oc` 0 and 1:
   ```
   (cd builds/$b && TEST_PHP_EXECUTABLE=sapi/cli/php sapi/cli/php run-tests.php -q -j20 \
     -d extension=$PWD/zend_test.so -d opcache.enable_cli=$oc -d opcache.file_update_protection=0 \
     Zend/tests ext/opcache/tests ext/reflection/tests ext/zend_test/tests)
   ```
   Add `--asan` and `USE_ZEND_ALLOC=0` for the asan builds. This loads zend_test for all four directories; my release runs of master and PR didn't (see `data/tests.txt`).
