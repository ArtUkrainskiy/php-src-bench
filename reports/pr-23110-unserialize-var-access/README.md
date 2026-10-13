# unserialize(): O(1) back-reference lookup (php-src PR #23110)

Review material for [php/php-src#23110](https://github.com/php/php-src/pull/23110) by kamil-tekiela, "Optimize serialize". PR head [`15438e3c5d2`](https://github.com/php/php-src/pull/23110/commits/15438e3c5d2300cf35878580a70419057d4702cc), merged without conflicts onto master [`c65321c70f7`](https://github.com/php/php-src/commit/c65321c70f7); nothing had to be changed to build it. Measured and checked on 14 October 2026.

`unserialize()` keeps every value that a later `R:`/`r:` may refer to in chunks of 1,018 slots (`var_entries`), linked in a list. `var_access()` walked that list, one chunk per 1,018 ids, to find the value behind a reference. The PR keeps an array of pointers to the chunks (`chunk_list`, grown by doubling from 4) and computes the chunk and the slot from the id. Only `unserialize()` changes; `serialize()` is untouched.

## Summary

- **References to late values get faster:** 14–31% fewer cycles on payloads with many `r:`/`R:` to values beyond the first 1,018, on all four compilers. The old list walk is a chain of dependent loads, so cycles drop more than instructions (2–9% fewer).
- **Payloads without such references:** cycles −2 … +4% against master, while master against master in the same series spans −1 … +3%: no measurable change.
- **GCC executes more instructions for every unserialized value**, with or without references: 4.12–4.13 per value on 6,200 ints, 3.79 (GCC 13) and 0.85 (GCC 14) on 50,000 strings, 0.2–1.0% of the call; clang 0.15–0.16. The branch in `var_push()` that adds a chunk, taken once per 1,018 values, grows with the PR, and `var_push()` is inlined into `php_var_unserialize_internal()`, which grows by 543 bytes (GCC 13) and 683 (GCC 14). Moving the body of that branch into a non-inlined function ([`cold-variant.diff`](cold-variant.diff)) brings GCC to 0.05–0.07 instructions per value, as much as master against master differs (0.07), and back to master's size, with similar gains on reference-heavy payloads (11–30% fewer cycles against 14–31%). [Details](#gcc-and-the-inlined-chunk-branch).
- **Output** is the same as master with all four compilers and under ASan/UBSan, on 1,429 boundary payloads and 3,000 random ones; the check catches six deliberate mutations.
- **The PR's test** reaches the overflow chunks, but its comments name ids the payloads do not contain, and it does not reach the growth of `chunk_list` beyond 4 chunks. [Details](#the-prs-test).
- **Not measured:** AMD, ZTS builds, payloads from real applications.

## Results

Change in CPU cycles per call with the PR, relative to master (negative = fewer cycles, faster). Intel i7-13700H, one column per compiler, median of five alternating runs; the second column is master's cost for scale:

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 |
|---|--:|--:|--:|--:|--:|
| array of 10 scalars (no references) | 1,482 | +1% | +3% | +1% | +3% |
| session-like array, ~0.5 KB (no references) | 4,766 | 0% | +3% | +3% | +2% |
| 1,000 ints (no references) | 111,975 | +2% | 0% | −1% | +2% |
| 6,200 ints (no references) | 715,794 | +4% | 0% | −2% | +3% |
| 50,000 strings (no references) | 8,466,801 | −1% | +3% | +3% | 0% |
| 5,000 objects (no references) | 9,111,635 | −2% | +3% | 0% | 0% |
| 5,000 objects sharing 50 objects (`r:` to early ids) | 9,606,840 | −1% | +2% | +1% | −1% |
| 20,000 objects, each refers to the previous one (`r:`) | 58,467,095 | −29% | −28% | −31% | −31% |
| 20,000 objects, each refers to a random earlier one (`r:`) | 76,164,644 | −15% | −14% | −15% | −16% |
| 6,200 ints + 100,000 `R:` to random ones | 19,276,613 | −17% | −15% | −16% | −14% |

With spread and instructions: [full table](#full-table).

## GCC and the inlined chunk branch

| build | instructions per unserialized value, change to master (6,200 ints) | size of `php_var_unserialize_internal()`, bytes (master → build) |
|---|--:|--:|
| PR, GCC 13.3 | +4.12 | 8,818 → 9,361 |
| PR, GCC 14.2 | +4.13 | 8,774 → 9,457 |
| PR, clang 18.1 | +0.15 | 6,300 → 6,435 |
| PR, clang 20.1 | +0.16 | 6,344 → 6,468 |
| variant, GCC 13.3 | +0.05 | 8,818 → 8,812 |
| variant, GCC 14.2 | +0.07 | 8,774 → 8,778 |
| variant, clang 18.1 | +0.16 | 6,300 → 6,294 |
| variant, clang 20.1 | +0.04 | 6,344 → 6,336 |
| master against master, GCC 13.3 | +0.07 | — |

[`cold-variant.diff`](cold-variant.diff) moves the body of `if (var_hash->used_slots == VAR_ENTRIES_MAX)` in `var_push()` (new chunk, link, append to `chunk_list`) into `var_push_new_chunk()`, marked `zend_never_inline`, and marks the condition `UNEXPECTED`. Output identical to master. Change in cycles relative to master with the variant:

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | instructions |
|---|--:|--:|--:|--:|--:|--:|
| array of 10 scalars (no references) | 1,460 | −1% (−2 … 0) | +4% (+3 … +5) | 0% (−1 … +1) | +7% (+6 … +7) | 0% |
| session-like array, ~0.5 KB (no references) | 4,903 | 0% (−3 … +5) | +3% (+1 … +3) | +5% (+4 … +6) | +2% (0 … +3) | 0% |
| 1,000 ints (no references) | 113,339 | +4% (+3 … +4) | +3% (+2 … +4) | −3% (−4 … −1) | +1% (+1 … +2) | 0% |
| 6,200 ints (no references) | 719,100 | +3% (+3 … +4) | +5% (+2 … +8) | −4% (−5 … −3) | +4% (+2 … +10) | 0% |
| 50,000 strings (no references) | 8,387,990 | +2% (+2 … +27) | +4% (+3 … +5) | +4% (+2 … +9) | −4% (−7 … −3) | −1% … 0% |
| 5,000 objects (no references) | 9,065,240 | −1% (−3 … +4) | +1% (0 … +4) | +1% (−3 … +3) | +2% (−1 … +4) | 0% |
| 5,000 objects sharing 50 objects (`r:` to early ids) | 9,686,771 | 0% (−2 … +1) | 0% (−1 … +5) | 0% (−1 … +2) | −2% (−3 … +3) | 0% |
| 20,000 objects, each refers to the previous one (`r:`) | 58,925,116 | −28% (−29 … −22) | −29% (−29 … −28) | −30% (−31 … −29) | −30% (−32 … −29) | −9% … −7% |
| 20,000 objects, each refers to a random earlier one (`r:`) | 76,062,606 | −13% (−15 … −9) | −14% (−18 … −8) | −14% (−15 … −13) | −15% (−16 … −13) | −5% … −3% |
| 6,200 ints + 100,000 `R:` to random ones | 19,142,070 | −13% (−14 … −12) | −11% (−20 … −10) | −21% (−23 … −10) | −16% (−17 … −15) | −4% … −3% |

The cycles of payloads without references move by −4 … +7% with the variant and −2 … +4% with the PR, around the −1 … +3% of the master-against-master control: the instructions the variant removes are not visible in cycles on this machine.

## Correctness

- [`difftest.php`](difftest.php) prints one SHA-256 per section over `serialize()` of every result (which keeps the reference structure) or `false` plus the warning:
  - `R:` to every id within ±3 of each of the first nine chunk boundaries (1,018 to 9,162), to −1, 0, 1, 2, 3 and around the end of the payload, and to `PHP_INT_MAX`, in arrays of 1 to 9,200 values (801 payloads);
  - `R:` to every id of a 5,200-element array, ascending and descending;
  - `r:` and `R:` into objects and their properties around the boundaries (624 payloads);
  - `R:` from one nested array into another that spans three chunks, and `unserialize()` called from `__unserialize()` inside a large payload;
  - 3,000 random payloads of up to 12,000 values (ints, strings, objects, nested arrays, `R:`/`r:` to earlier ids; about one in ten with one invalid id: 278 of 3,000 are rejected), seed 7.
- Identical output ([`difftest-master.txt`](difftest-master.txt)) on master, the PR and the variant with all four compilers, and on the PR built with `--enable-debug --enable-address-sanitizer --enable-undefined-sanitizer` (clang 18.1, `USE_ZEND_ALLOC=0`, nothing on stderr): [`difftest-builds.txt`](difftest-builds.txt).
- [`mutate.py`](mutate.py) applies six mutations to the PR's `var_access()` and `var_push()` one at a time (off by one in the chunk index, in the slot, in both bounds checks, last base slot sent to the overflow path, a chunk not recorded); each one changes the output or crashes: [`mutate-output.txt`](mutate-output.txt).
- `ext/standard/tests/serialize` under ASan: 172 passed, 0 failed, 6 skipped.

## The PR's test

`unserialize_var_access_chunk_boundary.phpt` says its references point at ids 0, 1018 and 1019 and at object 1050. The ids in the payloads it builds are different: `serialize()` emits `R:2;`, `R:1020;`, `R:1021;` and `r:2102;` (ids count from 1, the outer array takes id 1, and each object and its property take one id each). The references still land in the base chunk, the first overflow chunk and the second one, so the test exercises the new code, but not at the places the comments describe. `chunk_list` starts with room for 4 chunks and is grown when the fifth overflow chunk is created, at id 5,091 (serialized); the test stays below that, while `difftest.php` goes past it.

## Method

- Machine: Intel i7-13700H, P-core CPU 2, governor `powersave`, turbo on, kernel 7.0.0-34. Compilers GCC 13.3.0, GCC 14.2.0, clang 18.1.3, clang 20.1.2.
- Builds: `bench build`, CLI only (`--disable-all`), with the compiler and linker flags of the official Docker image plus `-g`: `BENCH_CFLAGS='-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64'`, `LDFLAGS='-Wl,-O1 -pie'`, `--enable-werror`.
- Metric: CPU cycles and instructions per call from `perf stat`, N calls minus the same process with 0 calls, divided by N ([`pairs-run.sh`](pairs-run.sh), cases in [`cases.php`](cases.php)). Five runs per case, master and the build alternating; the value is the median over runs of the build's cycles divided by the median of master's runs, written as a change in percent.
- Payloads are built with `serialize()`, which the PR does not change. Small ones come from a pool of 64 different payloads (fixed seed).
- Control: master against master in the same series, −1 … +3% over the ten cases.
- Raw data: [`intel-docker-20261014.txt`](intel-docker-20261014.txt) (groups `g13` … `c20` for the PR, `g13c` … `c20c` for the variant, `aa` for the control). Tables: [`speedup-table.py`](speedup-table.py) with [`rows.txt`](rows.txt).

## Full table

Change in CPU cycles per call with the PR relative to master (negative = fewer cycles, faster), median of five runs, in brackets the lowest and the highest run; last column: change in instructions, lowest and highest over the four compilers.

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | instructions |
|---|--:|--:|--:|--:|--:|--:|
| array of 10 scalars (no references) | 1,482 | +1% (−4 … +52) | +3% (+3 … +5) | +1% (0 … +7) | +3% (+2 … +7) | 0% … +1% |
| session-like array, ~0.5 KB (no references) | 4,766 | 0% (−1 … +1) | +3% (+2 … +5) | +3% (+3 … +8) | +2% (+2 … +4) | 0% … +1% |
| 1,000 ints (no references) | 111,975 | +2% (+2 … +6) | 0% (0 … 0) | −1% (−2 … +1) | +2% (+2 … +2) | 0% … +1% |
| 6,200 ints (no references) | 715,794 | +4% (+4 … +4) | 0% (0 … +1) | −2% (−2 … −2) | +3% (+2 … +3) | 0% … +1% |
| 50,000 strings (no references) | 8,466,801 | −1% (−2 … +1) | +3% (+2 … +17) | +3% (+2 … +6) | 0% (−1 … +4) | 0% … +1% |
| 5,000 objects (no references) | 9,111,635 | −2% (−4 … +4) | +3% (+1 … +4) | 0% (0 … +1) | 0% (−1 … +1) | 0% |
| 5,000 objects sharing 50 objects (`r:` to early ids) | 9,606,840 | −1% (−3 … +3) | +2% (−1 … +5) | +1% (0 … +2) | −1% (−2 … 0) | 0% |
| 20,000 objects, each refers to the previous one (`r:`) | 58,467,095 | −29% (−30 … −26) | −28% (−31 … −28) | −31% (−32 … −29) | −31% (−32 … −30) | −9% … −6% |
| 20,000 objects, each refers to a random earlier one (`r:`) | 76,164,644 | −15% (−16 … −13) | −14% (−15 … −13) | −15% (−17 … −14) | −16% (−18 … +1) | −5% … −3% |
| 6,200 ints + 100,000 `R:` to random ones | 19,276,613 | −17% (−18 … −14) | −15% (−17 … −2) | −16% (−18 … −15) | −14% (−16 … −4) | −4% … −2% |

## Reproduce

From the root of php-src-bench, with `PHP_SRC` pointing at a php-src clone:

```sh
git -C $PHP_SRC fetch origin master pull/23110/head:pr23110
W=$PWD/../php-src-pr23110
git -C $PHP_SRC worktree add "$W" origin/master && git -C "$W" merge pr23110   # the numbers here: master c65321c70f7 instead of origin/master
F='-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64'
for cc in "cc g13" "gcc-14 g14" "clang c18" "clang-20 c20"; do set -- $cc
  CC=$1 BENCH_CFLAGS="$F" LDFLAGS='-Wl,-O1 -pie' BENCH_CONFIGURE_EXTRA=--enable-werror ./bench build unser-$2-base origin/master
  CC=$1 BENCH_CFLAGS="$F" LDFLAGS='-Wl,-O1 -pie' BENCH_CONFIGURE_EXTRA=--enable-werror PHP_SRC="$W" ./bench build unser-$2-pr .
done
cd reports/pr-23110-unserialize-var-access
B=${BENCH_BUILDS:-../../../php-builds}
for b in g13-base g13-pr; do $B/unser-$b/sapi/cli/php -n difftest.php 3000 7 | diff - difftest-master.txt && echo "$b ok"; done
BENCH_BUILDS=$B PREFIX=unser- CPU=2 PASSES=5 ./pairs-run.sh out.txt g13:g13-base:g13-pr g14:g14-base:g14-pr c18:c18-base:c18-pr c20:c20-base:c20-pr aa:g13-base:g13-base
mapfile -t ROWS < rows.txt
./speedup-table.py --full out.txt 'g13:GCC 13.3,g14:GCC 14.2,c18:clang 18.1,c20:clang 20.1' "${ROWS[@]}"
```
