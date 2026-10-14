# array_diff() of ints through a bitset (php-src PR #22648)

Review material for [php/php-src#22648](https://github.com/php/php-src/pull/22648) by mehmetcansahin, "Optimize array_diff() for long values". PR head [`b5a4a7fe851`](https://github.com/php/php-src/pull/22648/commits/b5a4a7fe8516c90bcc7457602cad98cd47dae138), merged onto master [`c65321c70f7`](https://github.com/php/php-src/commit/c65321c70f7) (conflict in `UPGRADING` only). Measured and checked on 14 October 2026.

On master, `array_diff()` turns every value of the exclusion arrays into a string and puts it in a hash table, then looks up the string of every value of the first array. The PR adds a path for ints only: when every value of every array is an int (references to ints included) and the exclusion values span less than 8 bits per exclusion element, it marks them in a bitset and tests the first array against it. Anything else returns to the existing code.

## Summary

- **Ints that fit: 71–88% fewer cycles** (10 to 200,000 values, one or three exclusion arrays), on all four compilers. The description's example takes 7.9–8.2× fewer cycles, as the description reports (about 8×).
- **Fallbacks cost little:** when the PR scans the arrays and then falls back (a far value, a string at the end of an array, sparse ints), 0 … +4% cycles and +1 … +5% instructions on 1,000 values; with strings it gives up at the first value, +1 … +7% on 10 strings (8–50 cycles on a 657–711-cycle call) and −2 … +2% on 1,000. The control (master against master) is −1 … +1%.
- **No correctness issue found:** the result, its keys, references and refcounts are the same as master on 200,000 random calls (37% of them on the new path) and on targeted cases, on all four compilers and under ASan/UBSan; the check catches six deliberate mutations.
- **The fallback cost can be cut, not removed:** checking the first value's type inline before the call cuts the cost on non-int input from 41–48 to 14–20 instructions; scanning the exclusions before the first array makes sparse ints fall back almost free, but makes a first array with a non-int at the end pay for the exclusion scan as well ([below](#reducing-the-fallback-cost)).
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

## Reducing the fallback cost

A call that does not take the bitset path pays for the check first. When the first value of the first array is not an int, that is the call to `php_array_diff_long()` (`zend_never_inline`; with GCC 13.3 it saves and restores six registers) and one type check: 41–48 instructions. Otherwise the arrays are scanned up to the value that rules the bitset out: the whole first array (about 10 instructions per value), then the exclusions (22–25 per value) until a non-int or a value out of range.

Two changes on top of the PR, built and measured the same way in a second series on the same machine (14 October 2026):

- [`variant-peek.diff`](variant-peek.diff): `array_diff()` checks the type of the first value of the first array inline and calls `php_array_diff_long()` only when it is an int;
- [`variant-reorder.diff`](variant-reorder.diff), on top of the first: `php_array_diff_long()` scans the exclusion arrays before checking that the first array holds only ints.

Both give the same [`difftest.php`](difftest.php) output as master with all four compilers (not run under ASan).

Extra instructions per call relative to master, lowest and highest over the four compilers ([`instr-table.py`](instr-table.py)):

| call | PR | PR + inline first-value check | PR + inline check + exclusions first |
|---|--:|--:|--:|
| 10 strings minus 10 strings | +41 … +48 | +14 … +20 | +14 … +19 |
| 1,000 strings minus 1,000 strings | +69 … +100 | −40 … +89 | −78 … +28 |
| 1,000 ints minus 1,000 ints, values up to 10⁹ | +9,900 … +10,100 | +9,900 … +11,100 | −110 … +1,100 |
| 1,000 ints minus 999 dense ints and one far value | +32,000 … +35,100 | +32,500 … +35,000 | +22,000 … +24,900 |
| 1,000 ints minus 999 ints and one string | +31,800 … +35,200 | +32,200 … +35,100 | +22,100 … +25,300 |
| 999 ints and one string minus 1,000 ints | +9,800 … +9,900 | +9,600 … +10,900 | +32,000 … +35,100 |

With GCC 14.2 both variants add about 1,000 more instructions to the fallbacks than the PR (not investigated). In cycles (tables below), the bitset rows stay within 2 points of the PR for both variants, and the 1,000-value fallbacks stay between −3% and +4% for all three builds. 10 strings on clang 18.1 cost +5 … +8% cycles with all three, which the instruction count (+17 … +47 on clang 18.1) does not explain; not investigated.

Change in CPU cycles per call relative to master (negative = fewer cycles, faster), median of five runs, in brackets the lowest and the highest run. Raw data: [`intel-variants-20261014.txt`](intel-variants-20261014.txt), run as in [`runs.txt`](runs.txt) with the groups `<cc>-pr`, `<cc>-peek`, `<cc>-reord` and `aa`.

### GCC 13.3

| call | master, CPU cycles per call | PR | PR + inline check | PR + inline check + exclusions first | instructions, lowest and highest over the three |
|---|--:|--:|--:|--:|--:|
| `range(0, 200000)` minus `range(100000, 300000)` (the description's example) | 47,332,153 | −88% (−88 … −88) | −88% (−88 … −88) | −88% (−88 … −88) | −87% |
| 10 ints minus 10 ints (values 1–30) | 1,554 | −75% (−75 … −74) | −75% (−75 … −74) | −75% (−75 … −75) | −68% … −67% |
| 100 ints minus 100 ints (values 1–300) | 19,647 | −83% (−84 … −82) | −82% (−83 … −79) | −84% (−86 … −84) | −81% |
| 1,000 ints minus 1,000 ints (values 1–3,000) | 239,226 | −86% (−86 … −85) | −86% (−86 … −86) | −87% (−87 … −86) | −83% |
| 1,000 ints minus three arrays of 300 ints | 224,381 | −85% (−86 … −85) | −86% (−86 … −85) | −86% (−86 … −86) | −83% |
| 1,000 ints minus 1,000 ints, values up to 10⁹ (falls back) | 242,769 | 0% (0 … 0) | 0% (−1 … +4) | 0% (0 … 0) | 0% … +1% |
| 1,000 ints minus 999 dense ints and one far value (falls back after the scan) | 238,995 | +1% (0 … +2) | +4% (+3 … +4) | +1% (0 … +1) | +3% … +5% |
| 1,000 ints minus 999 ints and one string (falls back after the scan) | 238,883 | +1% (+1 … +1) | +3% (+2 … +5) | +1% (0 … +1) | +3% … +5% |
| 999 ints and one string minus 1,000 ints (falls back after the scan) | 238,829 | 0% (−1 … +1) | +1% (+1 … +1) | +1% (+1 … +2) | +1% … +5% |
| 1,000 strings minus 1,000 strings (falls back at once) | 75,087 | +1% (0 … +15) | −3% (−3 … −1) | 0% (0 … +2) | 0% |
| 10 strings minus 10 strings (falls back at once) | 665 | −1% (−2 … 0) | −2% (−4 … +8) | −1% (−2 … 0) | 0% … +1% |

### GCC 14.2

| call | master, CPU cycles per call | PR | PR + inline check | PR + inline check + exclusions first | instructions, lowest and highest over the three |
|---|--:|--:|--:|--:|--:|
| `range(0, 200000)` minus `range(100000, 300000)` (the description's example) | 47,464,852 | −88% (−88 … −88) | −88% (−88 … −88) | −88% (−88 … −88) | −87% |
| 10 ints minus 10 ints (values 1–30) | 1,477 | −74% (−75 … −74) | −75% (−75 … −75) | −74% (−74 … −74) | −68% |
| 100 ints minus 100 ints (values 1–300) | 19,206 | −83% (−83 … −83) | −83% (−83 … −83) | −82% (−83 … −82) | −82% … −81% |
| 1,000 ints minus 1,000 ints (values 1–3,000) | 235,059 | −86% (−86 … −85) | −86% (−86 … −86) | −86% (−86 … −86) | −83% |
| 1,000 ints minus three arrays of 300 ints | 219,294 | −85% (−86 … −85) | −85% (−86 … −85) | −86% (−86 … −86) | −83% |
| 1,000 ints minus 1,000 ints, values up to 10⁹ (falls back) | 239,791 | +1% (+1 … +1) | +2% (+2 … +7) | +1% (0 … +2) | 0% … +1% |
| 1,000 ints minus 999 dense ints and one far value (falls back after the scan) | 235,670 | +2% (+2 … +3) | +4% (+4 … +4) | +3% (+3 … +3) | +3% … +5% |
| 1,000 ints minus 999 ints and one string (falls back after the scan) | 235,692 | +3% (+2 … +3) | +4% (+3 … +4) | +3% (+3 … +3) | +3% … +5% |
| 999 ints and one string minus 1,000 ints (falls back after the scan) | 234,893 | +1% (+1 … +2) | +2% (+2 … +4) | +4% (+3 … +4) | +1% … +5% |
| 1,000 strings minus 1,000 strings (falls back at once) | 73,400 | +1% (0 … +1) | 0% (−1 … 0) | 0% (−1 … +1) | 0% |
| 10 strings minus 10 strings (falls back at once) | 666 | +3% (+2 … +5) | 0% (0 … 0) | +1% (0 … +2) | +1% … +2% |

### clang 18.1

| call | master, CPU cycles per call | PR | PR + inline check | PR + inline check + exclusions first | instructions, lowest and highest over the three |
|---|--:|--:|--:|--:|--:|
| `range(0, 200000)` minus `range(100000, 300000)` (the description's example) | 47,307,197 | −88% (−88 … −88) | −88% (−88 … −88) | −88% (−88 … −87) | −86% |
| 10 ints minus 10 ints (values 1–30) | 1,584 | −72% (−72 … −72) | −72% (−72 … −71) | −72% (−73 … −71) | −65% |
| 100 ints minus 100 ints (values 1–300) | 20,367 | −83% (−83 … −82) | −83% (−83 … −83) | −83% (−83 … −83) | −80% |
| 1,000 ints minus 1,000 ints (values 1–3,000) | 246,248 | −87% (−87 … −86) | −87% (−87 … −87) | −87% (−87 … −86) | −82% |
| 1,000 ints minus three arrays of 300 ints | 231,198 | −86% (−86 … −85) | −86% (−86 … −86) | −86% (−86 … −86) | −82% |
| 1,000 ints minus 1,000 ints, values up to 10⁹ (falls back) | 244,161 | 0% (0 … +1) | +1% (+1 … +2) | 0% (0 … +1) | 0% … +1% |
| 1,000 ints minus 999 dense ints and one far value (falls back after the scan) | 247,512 | +2% (+2 … +2) | +2% (+1 … +2) | +1% (0 … +1) | +4% … +5% |
| 1,000 ints minus 999 ints and one string (falls back after the scan) | 246,540 | +2% (+2 … +3) | +2% (+1 … +2) | +1% (0 … +1) | +4% … +5% |
| 999 ints and one string minus 1,000 ints (falls back after the scan) | 246,908 | 0% (0 … +1) | −1% (−1 … 0) | +1% (+1 … +1) | +1% … +5% |
| 1,000 strings minus 1,000 strings (falls back at once) | 75,117 | 0% (0 … +1) | +1% (0 … +2) | +1% (0 … +2) | 0% |
| 10 strings minus 10 strings (falls back at once) | 705 | +6% (+6 … +7) | +5% (+4 … +5) | +8% (+8 … +9) | +1% … +2% |

### clang 20.1

| call | master, CPU cycles per call | PR | PR + inline check | PR + inline check + exclusions first | instructions, lowest and highest over the three |
|---|--:|--:|--:|--:|--:|
| `range(0, 200000)` minus `range(100000, 300000)` (the description's example) | 47,370,895 | −88% (−88 … −88) | −88% (−88 … −88) | −88% (−88 … −88) | −86% |
| 10 ints minus 10 ints (values 1–30) | 1,557 | −73% (−74 … −73) | −72% (−73 … −72) | −73% (−74 … −73) | −66% … −65% |
| 100 ints minus 100 ints (values 1–300) | 20,292 | −84% (−84 … −83) | −82% (−83 … −82) | −82% (−82 … −82) | −80% |
| 1,000 ints minus 1,000 ints (values 1–3,000) | 245,823 | −87% (−87 … −86) | −86% (−86 … −86) | −86% (−86 … −86) | −82% |
| 1,000 ints minus three arrays of 300 ints | 230,988 | −86% (−86 … −86) | −86% (−86 … −85) | −85% (−86 … −81) | −81% |
| 1,000 ints minus 1,000 ints, values up to 10⁹ (falls back) | 243,656 | 0% (0 … +1) | +1% (+1 … +1) | 0% (0 … +2) | 0% … +1% |
| 1,000 ints minus 999 dense ints and one far value (falls back after the scan) | 246,183 | +4% (+3 … +4) | +2% (+2 … +4) | +2% (+2 … +2) | +4% … +5% |
| 1,000 ints minus 999 ints and one string (falls back after the scan) | 245,667 | +4% (+4 … +4) | +3% (+3 … +4) | +3% (+2 … +3) | +4% … +5% |
| 999 ints and one string minus 1,000 ints (falls back after the scan) | 246,352 | −1% (−1 … 0) | −1% (−1 … 0) | +2% (+2 … +4) | +1% … +5% |
| 1,000 strings minus 1,000 strings (falls back at once) | 76,893 | −2% (−3 … −2) | −1% (−2 … 0) | −1% (−2 … −1) | 0% |
| 10 strings minus 10 strings (falls back at once) | 690 | +2% (0 … +2) | 0% (0 … +35) | −1% (−2 … −1) | +1% … +2% |

### Control

| call | master, CPU cycles per call | master against master (GCC 13.3) | instructions |
|---|--:|--:|--:|
| `range(0, 200000)` minus `range(100000, 300000)` (the description's example) | 47,456,190 | +2% (0 … +19) | 0% |
| 10 ints minus 10 ints (values 1–30) | 1,551 | −1% (−1 … +1) | 0% |
| 100 ints minus 100 ints (values 1–300) | 19,621 | 0% (−1 … 0) | 0% |
| 1,000 ints minus 1,000 ints (values 1–3,000) | 240,014 | 0% (−1 … +1) | 0% |
| 1,000 ints minus three arrays of 300 ints | 225,014 | 0% (−1 … 0) | 0% |
| 1,000 ints minus 1,000 ints, values up to 10⁹ (falls back) | 242,381 | 0% (0 … 0) | 0% |
| 1,000 ints minus 999 dense ints and one far value (falls back after the scan) | 238,167 | 0% (0 … 0) | 0% |
| 1,000 ints minus 999 ints and one string (falls back after the scan) | 239,233 | 0% (0 … 0) | 0% |
| 999 ints and one string minus 1,000 ints (falls back after the scan) | 238,183 | 0% (0 … 0) | 0% |
| 1,000 strings minus 1,000 strings (falls back at once) | 75,082 | +1% (0 … +1) | 0% |
| 10 strings minus 10 strings (falls back at once) | 647 | +1% (0 … +1) | 0% |

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
