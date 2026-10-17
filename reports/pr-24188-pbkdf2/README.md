# hash_pbkdf2() with precomputed HMAC states (php-src PR 24188)

Review material for [php/php-src#24188](https://github.com/php/php-src/pull/24188) by Sjord, "ext/hash: improve PBKDF2 performance", head [`5db5b7adbaf`](https://github.com/php/php-src/pull/24188/commits/5db5b7adbaf29eaf03e58815011fd7d7fc76d1d5), which targets PHP-8.2. It was merged onto PHP-8.2 [`03e959375b1`](https://github.com/php/php-src/commit/03e959375b1) without conflicts (locally as `845ec37f7b5`, the B side of the tables) and measured against it on 16 October 2026 (UTC) on an Intel i7-13700H (CPU 2, a performance core).

Each HMAC round of `hash_pbkdf2()` used to start from a fresh hash state and absorb the key block (`K ⊕ ipad` or `K ⊕ opad`) before the data. The PR computes the two states after those key blocks once, before the loop, and copies them at the start of every round, so each iteration hashes two blocks fewer. The output does not change.

PHP-8.2 does not build with `--enable-werror` on these compilers (bundled PCRE2 and `ext/json/json_encoder.c` with GCC 13.3 and 14.2, `Zend/Optimizer/zend_ssa.c` with clang 18.1 and 20.1; [`werror-check.txt`](werror-check.txt)), so both sides were built with the flags of the official Docker image but without `-Werror`.

## Summary

- **Speed:** with 1000 iterations 43–53% fewer cycles (whirlpool 35%), with 10 iterations 36–46% (whirlpool 32%), on all four compilers. With 1 iteration 0–5% more cycles: the precomputation costs as much as the one round it replaces, plus two allocations and copies.
- **Correctness:** output identical to PHP-8.2 for all 44 HMAC algorithms on 3,000 random passwords and salts on four compilers and 1,000 under ASan/UBSan; `ext/hash/tests` pass (70 passed, 7 skipped); the differential test and `ext/hash/tests` both catch all 6 deliberate mistakes in the new code.
- **Code:** one suggestion: the two precomputed states are derived from the password like `K1`/`K2`, which are wiped with `ZEND_SECURE_ZERO()` before `efree()`; the states are not. The change of `php_hash_copy()`'s signature in PHP-8.2 is a question for the maintainers.
- **Not checked:** AMD, master (the PR targets PHP-8.2), 32-bit builds.

## Results

Change in CPU cycles per call relative to PHP-8.2 (negative = fewer cycles, faster); median over the passes of the PR against PHP-8.2 in the same pass. The password and the salt are fixed (28 and 16 bytes): their content does not change the cost, the algorithm and the number of iterations do.

The machine was not quiet (powersave governor, CPU 2 13% busy, see the warnings): the medians and the A/A control are stable (0 to −1% on every row), single passes of some rows are not, which the ranges of the full table show.

<!-- bench-table compare.json --labels labels.txt --base-name PHP-8.2 --header -->
Machine: 13th Gen Intel(R) Core(TM) i7-13700H, CPU 2, kernel 7.0.0-34-generic.
Group gcc13: A = pr24188-base-gcc13 (03e959375b1 GCC 13.3, profile docker), B = pr24188-head-gcc13 (845ec37f7b5 GCC 13.3, profile docker).
Group gcc14: A = pr24188-base-gcc14 (03e959375b1 GCC 14.2, profile docker), B = pr24188-head-gcc14 (845ec37f7b5 GCC 14.2, profile docker).
Group clang18: A = pr24188-base-clang18 (03e959375b1 clang 18.1, profile docker), B = pr24188-head-clang18 (845ec37f7b5 clang 18.1, profile docker).
Group clang20: A = pr24188-base-clang20 (03e959375b1 clang 20.1, profile docker), B = pr24188-head-clang20 (845ec37f7b5 clang 20.1, profile docker).
5 alternating passes per case, user-space cycles per call (perf stat, minus the empty loop), A against A at the start and the end.
Machine: CPU governor is 'powersave': frequency scaling adds noise (sudo ./bench tune on).
Machine: turbo boost is on: thermal and frequency drift between rounds (sudo ./bench tune on).
Machine: load average is 1.9: other programs are competing for the CPU.
Machine: CPU 2 is 13% busy with other processes: timings will be noisy (try --cpu 8).
negative = fewer cycles (faster)

| call | PHP-8.2, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 |
|---|--:|--:|--:|--:|--:|
| `hash_pbkdf2('md5', …, 1)`, 1 iteration | 1,845 | +5% | +4% | +2% | +4% |
| `hash_pbkdf2('sha1', …, 1)`, 1 iteration | 2,097 | +5% | +4% | +3% | +4% |
| `hash_pbkdf2('sha256', …, 1)`, 1 iteration | 4,158 | +2% | +2% | 0% ~ | +1% |
| `hash_pbkdf2('sha512', …, 1)`, 1 iteration | 5,534 | +3% | +1% | +1% | +2% |
| `hash_pbkdf2('sha3-256', …, 1)`, 1 iteration | 6,378 | 0% ~ | +2% | +1% | +1% |
| `hash_pbkdf2('whirlpool', …, 1)`, 1 iteration | 6,695 | +1% | +2% | +4% | +2% |
| `hash_pbkdf2('md5', …, 10)`, 10 iterations | 13,626 | −36% | −36% | −38% | −38% |
| `hash_pbkdf2('sha1', …, 10)`, 10 iterations | 15,386 | −38% | −39% | −39% | −39% |
| `hash_pbkdf2('sha256', …, 10)`, 10 iterations | 35,783 | −42% | −42% | −45% | −44% |
| `hash_pbkdf2('sha512', …, 10)`, 10 iterations | 49,303 | −41% | −41% | −42% | −44% |
| `hash_pbkdf2('sha3-256', …, 10)`, 10 iterations | 55,227 | −45% | −45% | −46% | −45% |
| `hash_pbkdf2('whirlpool', …, 10)`, 10 iterations | 71,337 | −32% | −32% | −32% | −32% |
| `hash_pbkdf2('md5', …, 1000)`, 1000 iterations | 1,298,394 | −43% | −43% | −44% | −44% |
| `hash_pbkdf2('sha1', …, 1000)`, 1000 iterations | 1,424,314 | −43% | −46% | −46% | −45% |
| `hash_pbkdf2('sha256', …, 1000)`, 1000 iterations | 3,504,329 | −48% | −48% | −51% | −49% |
| `hash_pbkdf2('sha512', …, 1000)`, 1000 iterations | 4,865,934 | −47% | −47% | −48% | −49% |
| `hash_pbkdf2('sha3-256', …, 1000)`, 1000 iterations | 5,422,488 | −51% | −52% | −53% | −52% |
| `hash_pbkdf2('whirlpool', …, 1000)`, 1000 iterations | 7,168,768 | −35% | −35% | −35% | −35% |

Control: PHP-8.2 against itself.

| call | PHP-8.2, CPU cycles per call (GCC 13.3) | A/A start | A/A end |
|---|--:|--:|--:|
| `hash_pbkdf2('md5', …, 1)`, 1 iteration | 1,841 | 0% | 0% |
| `hash_pbkdf2('sha1', …, 1)`, 1 iteration | 2,092 | 0% | 0% |
| `hash_pbkdf2('sha256', …, 1)`, 1 iteration | 4,185 | −1% | 0% |
| `hash_pbkdf2('sha512', …, 1)`, 1 iteration | 5,531 | 0% | 0% |
| `hash_pbkdf2('sha3-256', …, 1)`, 1 iteration | 6,383 | 0% | 0% |
| `hash_pbkdf2('whirlpool', …, 1)`, 1 iteration | 6,710 | 0% | 0% |
| `hash_pbkdf2('md5', …, 10)`, 10 iterations | 13,675 | 0% | 0% |
| `hash_pbkdf2('sha1', …, 10)`, 10 iterations | 15,445 | 0% | 0% |
| `hash_pbkdf2('sha256', …, 10)`, 10 iterations | 35,963 | 0% | 0% |
| `hash_pbkdf2('sha512', …, 10)`, 10 iterations | 49,471 | −1% | 0% |
| `hash_pbkdf2('sha3-256', …, 10)`, 10 iterations | 55,290 | 0% | 0% |
| `hash_pbkdf2('whirlpool', …, 10)`, 10 iterations | 71,218 | 0% | 0% |
| `hash_pbkdf2('md5', …, 1000)`, 1000 iterations | 1,298,784 | 0% | 0% |
| `hash_pbkdf2('sha1', …, 1000)`, 1000 iterations | 1,430,315 | 0% | 0% |
| `hash_pbkdf2('sha256', …, 1000)`, 1000 iterations | 3,511,195 | 0% | 0% |
| `hash_pbkdf2('sha512', …, 1000)`, 1000 iterations | 4,862,373 | 0% | 0% |
| `hash_pbkdf2('sha3-256', …, 1000)`, 1000 iterations | 5,433,750 | 0% | 0% |
| `hash_pbkdf2('whirlpool', …, 1000)`, 1000 iterations | 7,210,028 | −1% | 0% |

~: the change is not larger than the A/A control of the same row: not evidence of a difference.
<!-- /bench-table -->

Full table, with the range over the passes and the change in instructions:

<!-- bench-table compare.json --labels labels.txt --base-name PHP-8.2 --full -->
| call | PHP-8.2, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | instructions |
|---|--:|--:|--:|--:|--:|--:|
| `hash_pbkdf2('md5', …, 1)`, 1 iteration | 1,845 | +5% (+4 … +5) | +4% (0 … +7) | +2% (+2 … +3) | +4% (+3 … +4) | +6% |
| `hash_pbkdf2('sha1', …, 1)`, 1 iteration | 2,097 | +5% (+5 … +5) | +4% (−17 … +19) | +3% (+1 … +7) | +4% (+4 … +5) | +3% |
| `hash_pbkdf2('sha256', …, 1)`, 1 iteration | 4,158 | +2% (+1 … +2) | +2% (+1 … +29) | 0% (−1 … +3) ~ | +1% (−3 … +1) | +1% … +2% |
| `hash_pbkdf2('sha512', …, 1)`, 1 iteration | 5,534 | +3% (0 … +3) | +1% (−14 … +2) | +1% (+1 … +4) | +2% (+1 … +19) | +1% |
| `hash_pbkdf2('sha3-256', …, 1)`, 1 iteration | 6,378 | 0% (0 … +1) ~ | +2% (−1 … +2) | +1% (−3 … +1) | +1% (−15 … +2) | +1% |
| `hash_pbkdf2('whirlpool', …, 1)`, 1 iteration | 6,695 | +1% (0 … +1) | +2% (+1 … +2) | +4% (−1 … +5) | +2% (−2 … +4) | +1% |
| `hash_pbkdf2('md5', …, 10)`, 10 iterations | 13,626 | −36% (−36 … −36) | −36% (−36 … −35) | −38% (−38 … −38) | −38% (−38 … −38) | −36% … −32% |
| `hash_pbkdf2('sha1', …, 10)`, 10 iterations | 15,386 | −38% (−39 … −37) | −39% (−39 … −38) | −39% (−39 … −39) | −39% (−39 … −38) | −40% … −39% |
| `hash_pbkdf2('sha256', …, 10)`, 10 iterations | 35,783 | −42% (−42 … −41) | −42% (−43 … −42) | −45% (−45 … −45) | −44% (−44 … −44) | −43% … −42% |
| `hash_pbkdf2('sha512', …, 10)`, 10 iterations | 49,303 | −41% (−53 … −32) | −41% (−41 … −41) | −42% (−42 … −31) | −44% (−44 … −44) | −43% … −41% |
| `hash_pbkdf2('sha3-256', …, 10)`, 10 iterations | 55,227 | −45% (−70 … +2) | −45% (−45 … −45) | −46% (−46 … −45) | −45% (−46 … −44) | −44% … −43% |
| `hash_pbkdf2('whirlpool', …, 10)`, 10 iterations | 71,337 | −32% (−32 … −31) | −32% (−33 … −28) | −32% (−32 … −31) | −32% (−32 … −31) | −32% |
| `hash_pbkdf2('md5', …, 1000)`, 1000 iterations | 1,298,394 | −43% (−43 … −42) | −43% (−43 … −42) | −44% (−46 … −44) | −44% (−44 … −44) | −43% … −39% |
| `hash_pbkdf2('sha1', …, 1000)`, 1000 iterations | 1,424,314 | −43% (−44 … −43) | −46% (−46 … −45) | −46% (−55 … −45) | −45% (−45 … −44) | −46% … −45% |
| `hash_pbkdf2('sha256', …, 1000)`, 1000 iterations | 3,504,329 | −48% (−55 … −47) | −48% (−49 … −47) | −51% (−51 … −50) | −49% (−50 … −49) | −48% … −47% |
| `hash_pbkdf2('sha512', …, 1000)`, 1000 iterations | 4,865,934 | −47% (−58 … −46) | −47% (−47 … −47) | −48% (−48 … −42) | −49% (−49 … −49) | −48% … −47% |
| `hash_pbkdf2('sha3-256', …, 1000)`, 1000 iterations | 5,422,488 | −51% (−55 … −45) | −52% (−54 … −52) | −53% (−54 … −52) | −52% (−52 … −52) | −49% … −48% |
| `hash_pbkdf2('whirlpool', …, 1000)`, 1000 iterations | 7,168,768 | −35% (−38 … +6) | −35% (−36 … −35) | −35% (−35 … −35) | −35% (−35 … −35) | −35% |

Control: PHP-8.2 against itself.

| call | PHP-8.2, CPU cycles per call (GCC 13.3) | A/A start | A/A end |
|---|--:|--:|--:|
| `hash_pbkdf2('md5', …, 1)`, 1 iteration | 1,841 | 0% (0 … 0) | 0% (0 … 0) |
| `hash_pbkdf2('sha1', …, 1)`, 1 iteration | 2,092 | 0% (0 … +1) | 0% (0 … +1) |
| `hash_pbkdf2('sha256', …, 1)`, 1 iteration | 4,185 | −1% (−1 … 0) | 0% (0 … 0) |
| `hash_pbkdf2('sha512', …, 1)`, 1 iteration | 5,531 | 0% (−1 … +2) | 0% (−1 … +2) |
| `hash_pbkdf2('sha3-256', …, 1)`, 1 iteration | 6,383 | 0% (0 … +37) | 0% (−5 … +8) |
| `hash_pbkdf2('whirlpool', …, 1)`, 1 iteration | 6,710 | 0% (−2 … 0) | 0% (−1 … +1) |
| `hash_pbkdf2('md5', …, 10)`, 10 iterations | 13,675 | 0% (−1 … +2) | 0% (0 … 0) |
| `hash_pbkdf2('sha1', …, 10)`, 10 iterations | 15,445 | 0% (0 … +1) | 0% (0 … 0) |
| `hash_pbkdf2('sha256', …, 10)`, 10 iterations | 35,963 | 0% (−6 … 0) | 0% (−1 … 0) |
| `hash_pbkdf2('sha512', …, 10)`, 10 iterations | 49,471 | −1% (−4 … +4) | 0% (0 … 0) |
| `hash_pbkdf2('sha3-256', …, 10)`, 10 iterations | 55,290 | 0% (0 … +6) | 0% (0 … 0) |
| `hash_pbkdf2('whirlpool', …, 10)`, 10 iterations | 71,218 | 0% (0 … 0) | 0% (−9 … +1) |
| `hash_pbkdf2('md5', …, 1000)`, 1000 iterations | 1,298,784 | 0% (0 … +1) | 0% (0 … +10) |
| `hash_pbkdf2('sha1', …, 1000)`, 1000 iterations | 1,430,315 | 0% (−1 … 0) | 0% (−1 … 0) |
| `hash_pbkdf2('sha256', …, 1000)`, 1000 iterations | 3,511,195 | 0% (0 … 0) | 0% (0 … +1) |
| `hash_pbkdf2('sha512', …, 1000)`, 1000 iterations | 4,862,373 | 0% (−1 … +1) | 0% (0 … +1) |
| `hash_pbkdf2('sha3-256', …, 1000)`, 1000 iterations | 5,433,750 | 0% (−2 … +1) | 0% (0 … +4) |
| `hash_pbkdf2('whirlpool', …, 1000)`, 1000 iterations | 7,210,028 | −1% (−3 … 0) | 0% (−51 … 0) |

~: the change is not larger than the A/A control of the same row: not evidence of a difference.
<!-- /bench-table -->

## Code

- **Equivalence.** A round was `init(NULL)`, `update(K ⊕ pad)`, `update(data)`, `final`; it is now `copy(state after init(NULL) and update(K ⊕ pad))`, `update(data)`, `final`, which gives the same bytes for any of these hash functions. The `$options` argument goes into `hash_init(context, args)` before the key preparation, and `php_hash_hmac_prep_key()` initialises again with `NULL` for long keys, so the options reach no round; the rounds used `hash_init(context, NULL)` before and after the change (options matter only for murmur and xxhash, which `hash_pbkdf2()` rejects).
- **Copies.** `hash_pbkdf2()` accepts only algorithms with `is_crypto`; all of them use `php_hash_copy()`, a `memcpy()` of the context.
- **Where the gain comes from.** A round hashes the key block and then the data, a digest plus padding. For sha256, sha512 and sha3-256 the digest and its padding fit one block: two compressions per round become one, about half of the work (47–53% fewer cycles with 1000 iterations). A whirlpool digest fills a whole 64-byte block and its padding takes another: three become two (35%). md5 compressions are cheap, so `init`/`final`/copy weigh more (43–44%). The instruction counts move by similar amounts (`--full` table).
- **Secrets in memory.** `K1`, `K2` and the salt buffer are wiped with `ZEND_SECURE_ZERO()` before `efree()`; `inner_context` and `outer_context` hold the hash states after absorbing `K1` and `K2`, which is as good as the key for computing the HMAC, and are freed without wiping. Suggested: `ZEND_SECURE_ZERO(inner_context, ops->context_size)` and the same for `outer_context` before their `efree()`. (`digest` and `temp`, which hold derived output, were not wiped before the PR either.)
- **API in a stable branch.** The PR adds `const` to the source context of `php_hash_copy()` and of the `php_hash_copy_func_t` typedef, both exported. The algorithms in php-src use `php_hash_copy()` (changed together with the typedef) or cast their own copy functions, so they are not affected; an extension outside php-src that assigns a copy function with the old signature without a cast gets an incompatible-pointer-types diagnostic, an error by default with GCC 14 and with clang (18.1 and 20.1 tried; GCC 13.3 warns). The optimisation does not need the `const`.

## Tests

- **Differential test** ([`difftest-s1.txt`](difftest-s1.txt), [`difftest-asan-s2.txt`](difftest-asan-s2.txt)): `difftests/code.php` with random bytes as passwords and salts, up to 300 bytes, half of the lengths on or next to the block sizes 64, 72, 104, 128, 136 and 144; four calls over all 44 algorithms of `hash_hmac_algos()`: 1 iteration; 3 iterations, empty salt, 200 hex characters (several output blocks); random salt, raw output; password as salt, 5 iterations, 100 raw bytes. PHP-8.2 built with GCC 13.3 against the PR built with GCC 13.3, GCC 14.2, clang 18.1 and clang 20.1: 3,000 inputs (seed 1), identical. Against a debug build with AddressSanitizer and UndefinedBehaviorSanitizer: 1,000 inputs (seed 2), identical, no reports.
- **php-src tests** ([`tests-ext-hash-base.txt`](tests-ext-hash-base.txt), [`tests-ext-hash-head.txt`](tests-ext-hash-head.txt)): `ext/hash/tests` on PHP-8.2 and on the PR, 70 passed and 7 skipped on both (six need mhash, one openssl).
- **Mutations** ([`mutations.php`](mutations.php), [`mutate.md`](mutate.md)): six mistakes in the new code, one at a time: a round started from a fresh state instead of the copy; the inner state built from the opad block; the outer state without its key block; the inner round run from the outer state, in the first block and in the iterations; the outer round left out of the iterations. The differential test (1,000 inputs, seed 3) and `ext/hash/tests` each catch all six, so the existing tests cover the change and the PR needs no new test.

## Reproduce

From the root of [php-src-bench](https://github.com/ArtUkrainskiy/php-src-bench), with php-src next to it:

```
./bench pr 24188 --base 03e959375b1 --slim --profile docker --no-werror --cc gcc,gcc-14,clang,clang-20   # head 5db5b7adbaf
./bench compare reports/pr-24188-pbkdf2/suite.php gcc13=pr24188-base-gcc13:pr24188-head-gcc13 gcc14=pr24188-base-gcc14:pr24188-head-gcc14 clang18=pr24188-base-clang18:pr24188-head-clang18 clang20=pr24188-base-clang20:pr24188-head-clang20
./bench table results/<date>-compare-suite.json --labels reports/pr-24188-pbkdf2/labels.txt --base-name PHP-8.2 --full
```

The series in this report: [`compare.json`](compare.json); `bench table compare.json` renders it.
