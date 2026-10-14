# array_shift(): one memmove() for hole-free packed arrays (php-src PR #23517)

Review material for [php/php-src#23517](https://github.com/php/php-src/pull/23517) by mehmetcansahin, "PHP array_shift(): Optimize tail move on hole-free packed arrays". PR head [`7268e324050`](https://github.com/php/php-src/pull/23517/commits/7268e324050c71f3250d0f8c3a835ab61131527f), merged onto master [`c65321c70f7`](https://github.com/php/php-src/commit/c65321c70f7) (conflicts in `NEWS` and `UPGRADING` only). Measured and checked on 14 October 2026.

After removing the first element of a packed array, `array_shift()` on master moves every remaining element down one slot in a loop that tests each slot for `IS_UNDEF`. The PR reads `HT_IS_WITHOUT_HOLES()` before the removal; when the array had no holes and no iterator is active, it moves the tail with one `memmove()` (a direct copy for a one-element tail). Arrays with holes, with active iterators, and hash arrays keep the old paths.

## Summary

- **Faster wherever the tail is long:** a queue of 100–10,000 elements (shift one, append one) takes 66–84% fewer cycles, draining a copy of 100–10,000 ints 57–83% fewer (2.3–6.0× faster; the description reports 2.7–4.3×), one shift of a fresh copy of 1,000 ints 45–49% fewer, on all four compilers.
- **No cost elsewhere:** two elements −4 … −1%; an array with a hole and a hash array, which keep the old paths, −6 … +2% with instructions within 0.1%, next to −3 … +2% for master against master.
- **No correctness issue found:** return values, the resulting arrays with their references, and the lifetime and destructor order of objects in the tail are the same as master on 500,000 random operation sequences and targeted cases, on all four compilers and under ASan/UBSan; the check catches four of five deliberate mutations, the fifth (not clearing the vacated last slot) changes nothing observable.
- **Not measured:** AMD; ZTS builds.

## Results

Change in CPU cycles per operation with the PR, relative to master (negative = fewer cycles, faster). Intel i7-13700H, one column per compiler, median of five alternating runs; the second column is master's cost for scale:

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 |
|---|--:|--:|--:|--:|--:|
| `array_shift()` of a fresh copy of `[0, 1]` | 121 | −1% | −4% | −3% | −3% |
| queue of 10: shift one, append one | 103 | −15% | −21% | −8% | −15% |
| queue of 100: shift one, append one | 467 | −70% | −69% | −66% | −70% |
| queue of 1,000: shift one, append one | 3,557 | −82% | −83% | −82% | −84% |
| queue of 10,000: shift one, append one | 35,702 | −73% | −73% | −72% | −75% |
| drain a copy of 100 ints with `while ($a) array_shift($a)` | 27,458 | −62% | −63% | −57% | −62% |
| drain a copy of 1,000 ints | 1,832,745 | −81% | −81% | −81% | −83% |
| drain a copy of 10,000 ints | 181,201,571 | −74% | −74% | −74% | −76% |
| one shift of a fresh copy of 1,000 ints | 6,073 | −48% | −49% | −45% | −46% |
| one shift of a fresh copy of 1,000 ints with a hole (old path) | 6,646 | +2% | +1% | −1% | −6% |
| one shift of a fresh copy of 100 string keys (hash, old path) | 1,394 | 0% | 0% | −1% | 0% |

A queue of 10,000 gains less than a queue of 1,000 (−75 … −72% against −84 … −82%) while executing 92–93% fewer instructions (1,000: 90–91% fewer). Moving 160 KB per shift makes copy and cache bandwidth the likely limit; these counters alone do not prove it.

## Correctness

- [`difftest.php`](difftest.php) hashes return values, array states (`serialize()` keeps references; keys separately) and the order of destructor calls:
  - draining packed arrays of every size from 0 to 40, with an append and a pop after every shift (41);
  - one or two holes at every position of arrays of 1–12 elements, then three shifts with appends, with the array state after every step: the old path, then the fast path once the array is compact again (156);
  - references to one variable and objects with destructors in the tail (the shifted element itself is an int), with a copy-on-write copy of the array kept: values, references and destructor order (8);
  - `array_shift()` inside `foreach` by value and by reference (8); a self-referencing array and nested arrays (2);
  - 500,000 random sequences of shifts, unsets, appends, appended references, shifts of copies, string keys (turning the array into a hash) and `array_unshift()`, on arrays starting at 0 to 300 elements, seed 7: every return value and the final array state.
- Identical output ([`difftest-master.txt`](difftest-master.txt)) on master and the PR with all four compilers, and on the PR built with `--enable-debug --enable-address-sanitizer --enable-undefined-sanitizer` (clang 18.1, `USE_ZEND_ALLOC=0`, nothing on stderr): [`difftest-builds.txt`](difftest-builds.txt).
- [`mutate.py`](mutate.py) applies five mutations to the PR: the fast path also for arrays with holes, one slot too many, the two-element case copying the wrong slot, a wrong `nNextFreeElement` — each changes the output or crashes — and not clearing the vacated last slot, which changes nothing: that slot lies beyond `nNumUsed`, and I found no code that reads it before overwriting it. [`mutate-output.txt`](mutate-output.txt).
- `ext/standard/tests/array` and `Zend/tests/foreach` under ASan: 876 passed, 0 failed, 17 skipped ([`asan-tests.txt`](asan-tests.txt)).

## Method

- Machine: Intel i7-13700H, P-core CPU 2, governor `powersave`, turbo on, kernel 7.0.0-34. Compilers GCC 13.3.0, GCC 14.2.0, clang 18.1.3, clang 20.1.2.
- Builds: `bench build`, CLI only (`--disable-all`), with the compiler and linker flags of the official Docker image plus `-g`: `BENCH_CFLAGS='-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64'`, `LDFLAGS='-Wl,-O1 -pie'`, `--enable-werror`. The PR merged onto `c65321c70f7` as `657902a1b11`; in that merge `NEWS` and `UPGRADING` kept the conflict markers, which does not affect the build.
- Metric: CPU cycles and instructions per operation from `perf stat`, N operations minus the same process with 0, divided by N ([`pairs-run.sh`](pairs-run.sh), cases in [`cases.php`](cases.php)). An operation is one loop body: one queue step, one whole drain of a copy, or one shift of a fresh copy (the copy is part of the cost, as in the PR's own benchmark). Five runs per case, master and the PR alternating; the value is the median over runs of the PR's cycles divided by the median of master's runs, written as a change in percent.
- Control: master against master in the same series, −3 … +2% over the eleven cases.
- Raw data: [`intel-docker-20261014.txt`](intel-docker-20261014.txt) (how it was run: [`runs.txt`](runs.txt)). Tables: [`speedup-table.py`](speedup-table.py) with [`rows.txt`](rows.txt).

## Full table

Change in CPU cycles per operation relative to master (negative = fewer cycles, faster), median of five runs, in brackets the lowest and the highest run; last column: change in instructions, lowest and highest over the four compilers.

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | instructions |
|---|--:|--:|--:|--:|--:|--:|
| `array_shift()` of a fresh copy of `[0, 1]` | 121 | −1% (−2 … +2) | −4% (−6 … −3) | −3% (−6 … −3) | −3% (−7 … −2) | −2% |
| queue of 10: shift one, append one | 103 | −15% (−16 … −14) | −21% (−21 … −21) | −8% (−9 … −7) | −15% (−15 … −9) | −27% … −23% |
| queue of 100: shift one, append one | 467 | −70% (−70 … −70) | −69% (−69 … −69) | −66% (−67 … −65) | −70% (−70 … −69) | −77% … −74% |
| queue of 1,000: shift one, append one | 3,557 | −82% (−83 … −82) | −83% (−84 … −79) | −82% (−82 … −82) | −84% (−84 … −83) | −91% … −90% |
| queue of 10,000: shift one, append one | 35,702 | −73% (−74 … −72) | −73% (−73 … −72) | −72% (−72 … −72) | −75% (−75 … −74) | −93% … −92% |
| drain a copy of 100 ints with `while ($a) array_shift($a)` | 27,458 | −62% (−63 … −58) | −63% (−63 … −62) | −57% (−57 … −56) | −62% (−62 … −61) | −69% … −65% |
| drain a copy of 1,000 ints | 1,832,745 | −81% (−82 … −81) | −81% (−82 … −73) | −81% (−81 … −80) | −83% (−85 … −81) | −90% … −89% |
| drain a copy of 10,000 ints | 181,201,571 | −74% (−74 … −74) | −74% (−74 … −74) | −74% (−74 … −73) | −76% (−76 … −76) | −93% … −92% |
| one shift of a fresh copy of 1,000 ints | 6,073 | −48% (−48 … −47) | −49% (−49 … −48) | −45% (−45 … −44) | −46% (−46 … −44) | −54% … −49% |
| one shift of a fresh copy of 1,000 ints with a hole (old path) | 6,646 | +2% (0 … +6) | +1% (−1 … +4) | −1% (−2 … 0) | −6% (−7 … −5) | 0% |
| one shift of a fresh copy of 100 string keys (hash, old path) | 1,394 | 0% (−3 … +1) | 0% (0 … +1) | −1% (−1 … −1) | 0% (−1 … +2) | 0% |
