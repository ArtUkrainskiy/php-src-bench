# array_diff() of ints through a bitset (php-src PR #22648)

Review material for [php/php-src#22648](https://github.com/php/php-src/pull/22648) by mehmetcansahin, "Optimize array_diff() for long values". PR head [`b5a4a7fe851`](https://github.com/php/php-src/pull/22648/commits/b5a4a7fe8516c90bcc7457602cad98cd47dae138), merged onto master [`c65321c70f7`](https://github.com/php/php-src/commit/c65321c70f7) (conflict in `UPGRADING` only). Measured and checked on 14 October 2026.

On master, `array_diff()` turns every value of the exclusion arrays into a string and puts it in a hash table, then looks up the string of every value of the first array. The PR adds a path for ints only: when every value of every array is an int (references to ints included) and the exclusion values span less than 8 bits per exclusion element, it marks them in a bitset and tests the first array against it. Anything else returns to the existing code.

## Summary

- **Ints that fit: 71–88% fewer cycles** (10 to 200,000 values, one or three exclusion arrays), on all four compilers. The description's example takes 7.9–8.2× fewer cycles, as the description reports (about 8×).
- **Fallbacks cost little:** when the PR scans the arrays and then falls back (a far value, a string at the end of an array, sparse ints), 0 … +4% cycles and +1 … +5% instructions on 1,000 values; with strings it gives up at the first value, +1 … +7% on 10 strings (8–50 cycles on a 657–711-cycle call) and −2 … +2% on 1,000. The control (master against master) is −1 … +1%.
- **No correctness issue found:** the result, its keys, references and refcounts are the same as master on 200,000 random calls (37% of them on the new path) and on targeted cases, on all four compilers and under ASan/UBSan; the check catches six deliberate mutations.
- **Test gap:** the PR's test only reaches bitsets of up to 4 bits, never more than one 64-bit word; elsewhere in the test suite `ext/random/tests/03_randomizer/methods/pickArrayKeys.phpt` builds one, indirectly (500 bits). The differential test here goes up to 8,004 bits.
- **Not measured:** AMD; memory use (the bitset needs at most one byte per exclusion element, rounded up to whole 8-byte words; the old path a string hash table).

## Results

Change in CPU cycles per call with the PR, relative to master (negative = fewer cycles, faster). Intel i7-13700H, one column per compiler, median of five alternating runs; the second column is master's cost for scale:

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 |
|---|--:|--:|--:|--:|--:|
| `range(0, 200000)` minus `range(100000, 300000)` (the description's example) | 50,869,022 | −88% | −88% | −87% | −88% |
| 10 ints minus 10 ints (values 1–30) | 1,563 | −75% | −74% | −71% | −73% |
| 100 ints minus 100 ints (values 1–300) | 19,536 | −82% | −82% | −82% | −83% |
| 1,000 ints minus 1,000 ints (values 1–3,000) | 239,935 | −86% | −85% | −86% | −87% |
| 1,000 ints minus three arrays of 300 ints | 225,205 | −85% | −85% | −86% | −86% |
| 1,000 ints minus 1,000 ints, values up to 10⁹ (falls back) | 243,475 | 0% | +1% | +1% | +2% |
| 1,000 ints minus 999 dense ints and one far value (falls back after the scan) | 240,022 | +2% | +3% | +3% | +4% |
| 1,000 ints minus 999 ints and one string (falls back after the scan) | 240,918 | 0% | +4% | +3% | +3% |
| 999 ints and one string minus 1,000 ints (falls back after the scan) | 241,631 | 0% | +2% | +1% | 0% |
| 1,000 strings minus 1,000 strings (falls back at once) | 75,019 | 0% | +2% | 0% | −2% |
| 10 strings minus 10 strings (falls back at once) | 657 | +1% | +3% | +7% | +1% |

## Correctness

- [`difftest.php`](difftest.php) records every result with `debug_zval_dump()` (values, keys, refcounts, reference flags), plus warnings and exceptions:
  - exclusion spans of 8 × count − 2 to 8 × count + 1 for 2–1,000 exclusion values, around 64-bit word boundaries, with values just below, inside and above the range (88);
  - `PHP_INT_MIN`/`PHP_INT_MAX`, negative ranges and spans that would overflow (14);
  - string keys, references and duplicates in the first array, references in the exclusions, an exclusion array passed by reference (4);
  - int-like strings, floats, bools, null, objects with `__toString()` and nested arrays mixed with ints (32); empty and one-element arrays, a single argument (6);
  - 200,000 random calls (seed 7): one to three exclusion arrays of up to 400 values, half of them dense enough for the bitset, with string keys, references and occasional non-int values; 73,022 of them (37%) take the new path, counted with an instrumented build ([`path-count.txt`](path-count.txt)).
- Identical output ([`difftest-master.txt`](difftest-master.txt)) on master and the PR with all four compilers, and on the PR built with `--enable-debug --enable-address-sanitizer --enable-undefined-sanitizer` (clang 18.1, `USE_ZEND_ALLOC=0`, nothing on stderr): [`difftest-builds.txt`](difftest-builds.txt).
- [`mutate.py`](mutate.py) applies six mutations to the PR (no out-of-range check, the minimum never updated, no addref on copied values, string keys dropped, the first array's types not checked, references not dereferenced when copying); each one changes the output or crashes: [`mutate-output.txt`](mutate-output.txt).
- `ext/standard/tests/array` under ASan: 816 passed, 0 failed, 17 skipped ([`asan-tests.txt`](asan-tests.txt)).

## Method

- Machine: Intel i7-13700H, P-core CPU 2, governor `powersave`, turbo on, kernel 7.0.0-34. Compilers GCC 13.3.0, GCC 14.2.0, clang 18.1.3, clang 20.1.2.
- Builds: `bench build`, CLI only (`--disable-all`), with the compiler and linker flags of the official Docker image plus `-g`: `BENCH_CFLAGS='-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64'`, `LDFLAGS='-Wl,-O1 -pie'`, `--enable-werror`. The PR merged onto `c65321c70f7` as `64e4aede086` (`UPGRADING` from master).
- Metric: CPU cycles and instructions per call from `perf stat`, N calls minus the same process with 0 calls, divided by N ([`pairs-run.sh`](pairs-run.sh), cases in [`cases.php`](cases.php)). Five runs per case, master and the PR alternating; the value is the median over runs of the PR's cycles divided by the median of master's runs, written as a change in percent. Small inputs come from a pool of 64 or 16 random argument sets (fixed seed).
- Control: master against master in the same series, −1 … +1% over the eleven cases.
- Raw data: [`intel-docker-20261014.txt`](intel-docker-20261014.txt) (how it was run: [`runs.txt`](runs.txt)). Tables: [`speedup-table.py`](speedup-table.py) with [`rows.txt`](rows.txt).

## Full table

Change in CPU cycles per call relative to master (negative = fewer cycles, faster), median of five runs, in brackets the lowest and the highest run; last column: change in instructions, lowest and highest over the four compilers.

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | instructions |
|---|--:|--:|--:|--:|--:|--:|
| `range(0, 200000)` minus `range(100000, 300000)` (the description's example) | 50,869,022 | −88% (−88 … −87) | −88% (−88 … −87) | −87% (−88 … −80) | −88% (−88 … −87) | −87% … −86% |
| 10 ints minus 10 ints (values 1–30) | 1,563 | −75% (−75 … −74) | −74% (−75 … −73) | −71% (−72 … −70) | −73% (−74 … −72) | −68% … −65% |
| 100 ints minus 100 ints (values 1–300) | 19,536 | −82% (−82 … −80) | −82% (−83 … −81) | −82% (−83 … −82) | −83% (−84 … −82) | −81% … −80% |
| 1,000 ints minus 1,000 ints (values 1–3,000) | 239,935 | −86% (−87 … −85) | −85% (−86 … −84) | −86% (−87 … −86) | −87% (−87 … −86) | −83% … −82% |
| 1,000 ints minus three arrays of 300 ints | 225,205 | −85% (−86 … −85) | −85% (−85 … −85) | −86% (−86 … −85) | −86% (−87 … −85) | −83% … −81% |
| 1,000 ints minus 1,000 ints, values up to 10⁹ (falls back) | 243,475 | 0% (0 … +2) | +1% (+1 … +2) | +1% (−1 … +2) | +2% (+1 … +2) | +1% |
| 1,000 ints minus 999 dense ints and one far value (falls back after the scan) | 240,022 | +2% (+1 … +2) | +3% (+1 … +5) | +3% (+2 … +4) | +4% (+4 … +5) | +4% … +5% |
| 1,000 ints minus 999 ints and one string (falls back after the scan) | 240,918 | 0% (0 … +1) | +4% (+2 … +4) | +3% (+2 … +12) | +3% (+3 … +3) | +5% |
| 999 ints and one string minus 1,000 ints (falls back after the scan) | 241,631 | 0% (−2 … 0) | +2% (0 … +5) | +1% (0 … +1) | 0% (0 … +1) | +1% … +2% |
| 1,000 strings minus 1,000 strings (falls back at once) | 75,019 | 0% (−1 … 0) | +2% (+1 … +5) | 0% (0 … +1) | −2% (−3 … −2) | 0% |
| 10 strings minus 10 strings (falls back at once) | 657 | +1% (+1 … +2) | +3% (+2 … +4) | +7% (+5 … +8) | +1% (0 … +2) | +1% … +2% |
