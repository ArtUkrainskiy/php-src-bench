# array_push() appending to packed arrays in bulk (php-src PR #24157)

Review material for [php/php-src#24157](https://github.com/php/php-src/pull/24157) by mehmetcansahin, "array_push(): Append to packed arrays in bulk". PR head [`d8ef5ef635f`](https://github.com/php/php-src/pull/24157/commits/d8ef5ef635f53431827bd1e8f35813b58235530b), merged onto master [`c65321c70f7`](https://github.com/php/php-src/commit/c65321c70f7) without conflicts. Measured and checked on 14 October 2026.

When the array is packed (or uninitialized and at least two values are pushed) and its next free index is right after the last used slot, the PR makes room once and writes the values with `ZEND_HASH_FILL_*` instead of calling `zend_hash_next_index_insert()` per value. Hash arrays, packed arrays whose next free index is past the last used slot, packed arrays with holes that would have to grow, and one value pushed onto an uninitialized array keep the old loop.

## Summary

- **Several values:** three values onto a list take 9 … 16% fewer cycles (19 … 22% fewer instructions), 16 values via `...` 19 … 31% (28 … 30%), 1,000 values via `...` onto `[]` 35 … 38% (34 … 37%).
- **One value onto a list:** 0 … −7%, with 1 … 4% fewer instructions. This is the common call, and it does not get slower on any compiler.
- **Paths that keep the old loop:** a hash array −3 … +3% (1 … 3% more instructions), one value onto `[]` −2 … +3% (1 … 2% more instructions): the new checks run before the old loop. Master against master in the same series: −2 … +1%.
- **Two values onto `[]`** (mixed in the PR description, +2.0% on M1 and −8.2% on Xeon): 5 … 11% fewer cycles here on all four compilers, 6 … 8% fewer instructions.
- **No difference from master found:** 13,879 `array_push()` calls with the array state after each one (keys, values, `key()`/`current()`, the next free index, `memory_get_usage()`) give the same output as master with all four compilers and under ASan/UBSan; the check catches seven of seven deliberate mutations; `ext/standard/tests/array` under ASan pass.
- **Test gaps:** three of the seven mutations pass `ext/standard/tests/array` (with the PR's new test): the growth path one slot short in two ways, and growth allowed for arrays with holes. Two short tests catch all three ([below](#tests)).
- **Code:** the fast path repeats `zend_hash` internals inside `array_push()`. The same code moved into a separate non-inlined function, as a `zend_hash.c` API would be, is slower: one int or string onto a list takes 5% more cycles than master with GCC 14.2 and 7% more with clang 18.1 (one value onto a list with a hole: 4% and 15%), and the paths that keep the old loop stay within one point of the PR ([below](#code)).
- **Not checked:** AMD, 32-bit builds, opcache/JIT.

## Results

Change in CPU cycles per call with the PR, relative to master (negative = fewer cycles, faster). Intel i7-13700H, one column per compiler, median of five alternating runs; the second column is master's cost for scale. The calls run in a loop that also counts and, in the `$a = []` rows, creates and frees the array, so the percentages are of the whole statement:

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 |
|---|--:|--:|--:|--:|--:|
| `array_push($a, $i)`, one int; `$a` starts again from `[]` every 1,024 calls | 60 | −2% | −2% | 0% | −7% |
| `array_push($a, $s)`, one string; same | 62 | −5% | −2% | 0% | −6% |
| `array_push($a, $i, $i, $i)`; same | 94 | −14% | −13% | −9% | −16% |
| `array_push($a, ...$v)`, 16 ints; same | 538 | −25% | −25% | −26% | −31% |
| `array_push($a, $i)`, list with a hole (`unset($a[3])`) | 61 | −3% | −2% | −1% | −6% |
| `array_push($a, $i)` onto `['k' => 0]` (hash, old code path) | 78 | 0% | +1% | −3% | 0% |
| `array_push($a, $i, $i, $i)` onto `['k' => 0]` | 130 | −1% | +1% | +3% | +1% |
| `$a = []; array_push($a, $i);` | 91 | +3% | +2% | −2% | +1% |
| `$a = []; array_push($a, $i, $i);` | 111 | −5% | −8% | −10% | −11% |
| `$a = []; array_push($a, ...$v);`, 16 ints | 575 | −23% | −19% | −25% | −31% |
| `$a = []; array_push($a, ...$v);`, 1,000 ints | 23,735 | −36% | −36% | −35% | −38% |

`zif_array_push` grows from 85 to 168 instructions (GCC 13.3; 105 to 190 with its `.cold` part). On the paths that keep the old loop the new checks execute 5–14 more instructions per call (hash rows and one value onto `[]`, all four compilers), which shows up as −3 … +3% in cycles.

## Code

The fast path works with `zend_hash` internals from `ext/standard`: it repeats the next-index rule (`nNextFreeElement == ZEND_LONG_MIN` means 0), grows the packed table itself and restores the internal pointer that `ZEND_HASH_FILL_END()` resets. A function in `zend_hash.c` that appends n values to a packed array would keep this next to `zend_hash_next_index_insert()`, but it would be an out-of-line call. I measured that shape: the same code in a `static zend_never_inline` helper, with the flag check left in `array_push()` ([`helper-variant.diff`](helper-variant.diff); output identical to master on all four compilers, [`difftest-builds.txt`](difftest-builds.txt)). `zif_array_push` is then 106 instructions plus 82 in the helper (GCC 13.3), against 168 with the PR.

Change in CPU cycles per call with the helper variant, relative to master (negative = fewer cycles, faster), same series as the PR's numbers below:

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 |
|---|--:|--:|--:|--:|--:|
| `array_push($a, $i)`, one int; `$a` starts again from `[]` every 1,024 calls | 64 | −3% | +5% | +7% | −3% |
| `array_push($a, $s)`, one string; same | 61 | 0% | +5% | +7% | −3% |
| `array_push($a, $i, $i, $i)`; same | 94 | −11% | −8% | −6% | −22% |
| `array_push($a, ...$v)`, 16 ints; same | 542 | −25% | −24% | −27% | −30% |
| `array_push($a, $i)`, list with a hole (`unset($a[3])`) | 61 | +2% | +4% | +15% | −4% |
| `array_push($a, $i)` onto `['k' => 0]` (hash, old code path) | 77 | 0% | +1% | 0% | −1% |
| `array_push($a, $i, $i, $i)` onto `['k' => 0]` | 128 | 0% | −1% | +1% | +1% |
| `$a = []; array_push($a, $i);` | 91 | +2% | +2% | 0% | 0% |
| `$a = []; array_push($a, $i, $i);` | 109 | −4% | −5% | −4% | −8% |
| `$a = []; array_push($a, ...$v);`, 16 ints | 586 | −26% | −16% | −26% | −30% |
| `$a = []; array_push($a, ...$v);`, 1,000 ints | 23,449 | −35% | −35% | −36% | −36% |

The PR in the same series (the table under [Results](#results) is the earlier series):

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 |
|---|--:|--:|--:|--:|--:|
| `array_push($a, $i)`, one int; `$a` starts again from `[]` every 1,024 calls | 61 | −3% | −4% | +1% | −7% |
| `array_push($a, $s)`, one string; same | 61 | −3% | −2% | +1% | −7% |
| `array_push($a, $i, $i, $i)`; same | 94 | −13% | −13% | −10% | −17% |
| `array_push($a, ...$v)`, 16 ints; same | 537 | −25% | −25% | −25% | −32% |
| `array_push($a, $i)`, list with a hole (`unset($a[3])`) | 61 | −3% | −3% | 0% | −6% |
| `array_push($a, $i)` onto `['k' => 0]` (hash, old code path) | 77 | +1% | +1% | 0% | −1% |
| `array_push($a, $i, $i, $i)` onto `['k' => 0]` | 128 | +1% | 0% | +1% | +1% |
| `$a = []; array_push($a, $i);` | 91 | +3% | +2% | −1% | 0% |
| `$a = []; array_push($a, $i, $i);` | 109 | −6% | −9% | −9% | −12% |
| `$a = []; array_push($a, ...$v);`, 16 ints | 576 | −24% | −19% | −24% | −33% |
| `$a = []; array_push($a, ...$v);`, 1,000 ints | 23,498 | −36% | −36% | −35% | −38% |

One value onto a list goes from −7 … +1% with the PR to −4 … +15% with the helper (one int or string: +5% with GCC 14.2 and +7% with clang 18.1; onto a list with a hole: +4% and +15%, runs +7 … +33% with clang 18.1), three values save less on three of four compilers (more with clang 20.1), and the paths that keep the old loop are within one point of the PR. So the inline fast path in the PR is the faster shape; the duplication of `zend_hash` logic is its cost. Master against master in this series: −2 … +2% ([full table](#helper-variant-series-full-table)). Raw data: [`intel-docker-helper-20261014.txt`](intel-docker-helper-20261014.txt).

## Correctness

- [`difftest.php`](difftest.php) records after every call the return value, any exception, the keys and values, `key()` and `current()`, the next free index (by appending a marker to a copy) and `memory_get_usage()` relative to before the call (which shows a different table size):
  - 4,788 targeted calls: 57 starting arrays (empty literal, `array_values([])`, a negative next index with and without a copy, hash arrays, packed with a key gap, the last/middle/first element unset, after `array_pop()`/`array_shift()`, the internal pointer in the middle, at the end and past the end, few and many holes with and without room, references inside, last key `PHP_INT_MAX - 1` (next index `PHP_INT_MAX`) and `PHP_INT_MAX` (full), lists of 1–1,025 elements built by `range()` and by `$a[] =`), each with 0–1,025 pushed ints, strings or mixed values, and a second push onto the result;
  - 17 calls on special cases: copy-on-write source unchanged, the array pushed onto itself (also via `...`), a reference to the array, refcounted values freed afterwards, typed and untyped properties, `foreach` by reference and by value while pushing, the full-array error;
  - 3,000 random sequences of 12 operations (push of 0–40 values, unset, pop, shift, assignment to a random index, `next()`, `end()`, `reset()`, copy, `$a[] =`) with 9,074 pushes (seed 7).
- Master gives the same output with all four compilers, and so does the PR with all four ([`difftest-builds.txt`](difftest-builds.txt)); under `--enable-debug --enable-address-sanitizer --enable-undefined-sanitizer` (clang 18.1, `USE_ZEND_ALLOC=0`) the PR's output equals master's apart from `memory_get_usage()`, which a debug build changes, and stderr is empty.
- [`mutate.py`](mutate.py) applies seven mutations to the PR: the internal pointer not restored, growth allowed for arrays with holes, the next index not compared with the last used slot, the room check one too large, the table one slot short, the values' refcount not incremented, the uninitialized array not initialized. Each is caught by a changed output, ASan or an assertion ([`mutate-output.txt`](mutate-output.txt)); the holes mutation changes `key()` (next section).
- `ext/standard/tests/array` under ASan (with the PR's new test): 816 passed, 0 failed, 17 skipped ([`asan-tests.txt`](asan-tests.txt)).

## Tests

[`mutate-phpt.py`](mutate-phpt.py) applies the same seven mutations and runs `ext/standard/tests/array` (with the PR's `array_push_packed_bulk_metadata.phpt`) under ASan ([`mutate-phpt-output.txt`](mutate-phpt-output.txt)):

| mutation | caught by |
|---|---|
| internal pointer not restored | `array_push_packed_bulk_metadata.phpt` |
| growth allowed for arrays with holes | — |
| next index not compared with the last used slot | `array_push_packed_bulk_metadata.phpt` |
| room check one too large (`argc > room + 1`) | — |
| table one slot short (`zend_hash_extend(ht, nNumUsed + argc - 1, …)`) | — |
| values' refcount not incremented | `array_push_variation2.phpt`, `array_push_variation3.phpt` |
| uninitialized array not initialized | `array_push.phpt` |

The room and table mutations are the growth path: they only show when the values need exactly one slot more than the table has room for, and no test pushes such a count. [`array_push_grow_boundary.phpt`](array_push_grow_boundary.phpt) (`range(1, 7)` plus two values: 9 slots of 8) fails under ASan with both mutations and passes with the PR.

The holes mutation removes the `HT_IS_WITHOUT_HOLES()` condition. Without it, a full packed array with holes grows as packed instead of taking the old loop, which converts it to a hash; the observable difference is the internal pointer. On master, and with the PR:

```php
$a = range(0, 15);
for ($i = 0; $i < 14; $i++) unset($a[$i]);
end($a);
next($a);
array_push($a, 16, 17);
var_dump(key($a)); // NULL; with the condition removed: int(16)
```

[`array_push_holes_pointer.phpt`](array_push_holes_pointer.phpt) checks this and fails with the mutation. Each proposed test against the three mutations, under ASan: [`mutate-proposed-output.txt`](mutate-proposed-output.txt) ([`mutate-proposed.py`](mutate-proposed.py)).

## Method

- Machine: Intel i7-13700H, P-core CPU 2, governor `powersave`, turbo on, kernel 7.0.0-34. Compilers GCC 13.3.0, GCC 14.2.0, clang 18.1.3, clang 20.1.2.
- Builds: `bench build`, CLI only (`--disable-all`, plus `--with-openssl`, which does not touch `array_push()`: the master builds are shared with another review), with the compiler and linker flags of the official Docker image plus `-g`: `BENCH_CFLAGS='-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64'`, `LDFLAGS='-Wl,-O1 -pie'`, `--enable-werror`. The PR merged onto `c65321c70f7` as `5dc5247103b`.
- Metric: CPU cycles and instructions per call from `perf stat`, N calls minus the same process with 0 calls, divided by N ([`pairs-run.sh`](pairs-run.sh), cases in [`cases.php`](cases.php)). Five runs per case, master and the PR alternating; the value is the median over runs of the PR's cycles divided by the median of master's runs, written as a change in percent.
- Control: master against master at the start and at the end of the same series (table below). A first series was discarded: master against master gave +10% on one row, from three runs of 86–102 cycles against 77–83 (median 78) at the end of the series.
- Raw data: [`intel-docker-20261014.txt`](intel-docker-20261014.txt) (how it was run: [`runs.txt`](runs.txt)). Tables: [`speedup-table.py`](speedup-table.py) with [`rows.txt`](rows.txt).

## Full table

Change in CPU cycles per call relative to master (negative = fewer cycles, faster), median of five runs, in brackets the lowest and the highest run; last column: change in instructions, lowest and highest over the four compilers.

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | instructions |
|---|--:|--:|--:|--:|--:|--:|
| `array_push($a, $i)`, one int; `$a` starts again from `[]` every 1,024 calls | 60 | −2% (−2 … +3) | −2% (−3 … +5) | 0% (−1 … +1) | −7% (−7 … −6) | −4% … −1% |
| `array_push($a, $s)`, one string; same | 62 | −5% (−5 … −2) | −2% (−3 … −2) | 0% (0 … +5) | −6% (−6 … −6) | −4% … −1% |
| `array_push($a, $i, $i, $i)`; same | 94 | −14% (−14 … −13) | −13% (−13 … −12) | −9% (−9 … −5) | −16% (−18 … −16) | −22% … −19% |
| `array_push($a, ...$v)`, 16 ints; same | 538 | −25% (−25 … −23) | −25% (−25 … −24) | −26% (−26 … −24) | −31% (−32 … −29) | −30% … −28% |
| `array_push($a, $i)`, list with a hole (`unset($a[3])`) | 61 | −3% (−3 … −3) | −2% (−3 … +2) | −1% (−1 … 0) | −6% (−7 … −6) | −4% … −1% |
| `array_push($a, $i)` onto `['k' => 0]` (hash, old code path) | 78 | 0% (0 … +5) | +1% (0 … +1) | −3% (−3 … 0) | 0% (0 … +1) | +1% … +3% |
| `array_push($a, $i, $i, $i)` onto `['k' => 0]` | 130 | −1% (−1 … +3) | +1% (0 … +3) | +3% (+1 … +63) | +1% (0 … +2) | +1% … +2% |
| `$a = []; array_push($a, $i);` | 91 | +3% (+3 … +3) | +2% (+1 … +2) | −2% (−3 … 0) | +1% (−1 … +6) | +1% … +2% |
| `$a = []; array_push($a, $i, $i);` | 111 | −5% (−7 … +7) | −8% (−8 … −7) | −10% (−10 … −9) | −11% (−12 … −7) | −8% … −6% |
| `$a = []; array_push($a, ...$v);`, 16 ints | 575 | −23% (−24 … −15) | −19% (−20 … −8) | −25% (−26 … −24) | −31% (−31 … −29) | −30% … −28% |
| `$a = []; array_push($a, ...$v);`, 1,000 ints | 23,735 | −36% (−37 … −33) | −36% (−36 … −35) | −35% (−35 … −35) | −38% (−38 … −33) | −37% … −34% |

Master against master (GCC 13.3), same series:

| call | master, CPU cycles per call (start of the series) | start of the series | end of the series |
|---|--:|--:|--:|
| `array_push($a, $i)`, one int; `$a` starts again from `[]` every 1,024 calls | 60 | 0% (0 … +2) | 0% (0 … +2) |
| `array_push($a, $s)`, one string; same | 61 | −2% (−2 … +3) | 0% (0 … 0) |
| `array_push($a, $i, $i, $i)`; same | 93 | 0% (0 … +3) | 0% (0 … +1) |
| `array_push($a, ...$v)`, 16 ints; same | 536 | 0% (0 … 0) | 0% (0 … 0) |
| `array_push($a, $i)`, list with a hole (`unset($a[3])`) | 61 | 0% (−2 … 0) | 0% (0 … +5) |
| `array_push($a, $i)` onto `['k' => 0]` (hash, old code path) | 78 | −1% (−1 … +4) | +1% (0 … +34) |
| `array_push($a, $i, $i, $i)` onto `['k' => 0]` | 129 | −1% (−1 … 0) | −1% (−1 … 0) |
| `$a = []; array_push($a, $i);` | 91 | +1% (0 … +22) | 0% (0 … +2) |
| `$a = []; array_push($a, $i, $i);` | 109 | 0% (0 … +2) | 0% (0 … +4) |
| `$a = []; array_push($a, ...$v);`, 16 ints | 581 | −2% (−10 … 0) | −1% (−2 … −1) |
| `$a = []; array_push($a, ...$v);`, 1,000 ints | 23,646 | −1% (−2 … +5) | 0% (0 … +3) |

## Helper variant series, full table

Series [`intel-docker-helper-20261014.txt`](intel-docker-helper-20261014.txt), same format as above. Helper variant against master:

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | instructions |
|---|--:|--:|--:|--:|--:|--:|
| `array_push($a, $i)`, one int; `$a` starts again from `[]` every 1,024 calls | 64 | −3% (−5 … −2) | +5% (+5 … +6) | +7% (+7 … +7) | −3% (−3 … −1) | +1% … +3% |
| `array_push($a, $s)`, one string; same | 61 | 0% (0 … +2) | +5% (+5 … +6) | +7% (+6 … +7) | −3% (−3 … −2) | +1% … +3% |
| `array_push($a, $i, $i, $i)`; same | 94 | −11% (−11 … −11) | −8% (−8 … −7) | −6% (−7 … −5) | −22% (−23 … −21) | −19% … −15% |
| `array_push($a, ...$v)`, 16 ints; same | 542 | −25% (−25 … −24) | −24% (−24 … −24) | −27% (−27 … −25) | −30% (−31 … −30) | −29% … −27% |
| `array_push($a, $i)`, list with a hole (`unset($a[3])`) | 61 | +2% (+2 … +2) | +4% (+3 … +4) | +15% (+7 … +33) | −4% (−4 … −1) | +2% … +3% |
| `array_push($a, $i)` onto `['k' => 0]` (hash, old code path) | 77 | 0% (0 … +3) | +1% (0 … +1) | 0% (−1 … +7) | −1% (−2 … −1) | +1% … +2% |
| `array_push($a, $i, $i, $i)` onto `['k' => 0]` | 128 | 0% (−1 … +1) | −1% (−1 … −1) | +1% (+1 … +2) | +1% (+1 … +8) | +1% |
| `$a = []; array_push($a, $i);` | 91 | +2% (+1 … +11) | +2% (+1 … +3) | 0% (−2 … +3) | 0% (−1 … 0) | +1% |
| `$a = []; array_push($a, $i, $i);` | 109 | −4% (−5 … +2) | −5% (−5 … −5) | −4% (−4 … −4) | −8% (−9 … −8) | −5% … −3% |
| `$a = []; array_push($a, ...$v);`, 16 ints | 586 | −26% (−26 … −23) | −16% (−17 … −14) | −26% (−26 … −26) | −30% (−31 … −30) | −29% … −27% |
| `$a = []; array_push($a, ...$v);`, 1,000 ints | 23,449 | −35% (−36 … −35) | −35% (−36 … −35) | −36% (−37 … +5) | −36% (−36 … −36) | −37% … −34% |

The PR against master:

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | instructions |
|---|--:|--:|--:|--:|--:|--:|
| `array_push($a, $i)`, one int; `$a` starts again from `[]` every 1,024 calls | 61 | −3% (−3 … −3) | −4% (−4 … −1) | +1% (−1 … +1) | −7% (−7 … −6) | −4% … −1% |
| `array_push($a, $s)`, one string; same | 61 | −3% (−3 … +2) | −2% (−3 … +2) | +1% (0 … +1) | −7% (−7 … −6) | −4% … −1% |
| `array_push($a, $i, $i, $i)`; same | 94 | −13% (−14 … −13) | −13% (−13 … −12) | −10% (−10 … −10) | −17% (−17 … −16) | −22% … −19% |
| `array_push($a, ...$v)`, 16 ints; same | 537 | −25% (−25 … −25) | −25% (−26 … −25) | −25% (−26 … −25) | −32% (−32 … −31) | −30% … −28% |
| `array_push($a, $i)`, list with a hole (`unset($a[3])`) | 61 | −3% (−3 … −3) | −3% (−4 … −3) | 0% (0 … +1) | −6% (−7 … −1) | −4% … −1% |
| `array_push($a, $i)` onto `['k' => 0]` (hash, old code path) | 77 | +1% (0 … +1) | +1% (−1 … +2) | 0% (0 … +3) | −1% (−1 … +1) | +1% … +3% |
| `array_push($a, $i, $i, $i)` onto `['k' => 0]` | 128 | +1% (+1 … +1) | 0% (0 … +1) | +1% (+1 … +3) | +1% (0 … +1) | +1% … +2% |
| `$a = []; array_push($a, $i);` | 91 | +3% (+2 … +5) | +2% (+2 … +5) | −1% (−2 … +2) | 0% (−1 … +3) | +1% … +2% |
| `$a = []; array_push($a, $i, $i);` | 109 | −6% (−6 … +1) | −9% (−9 … −9) | −9% (−10 … −7) | −12% (−13 … −11) | −8% … −6% |
| `$a = []; array_push($a, ...$v);`, 16 ints | 576 | −24% (−24 … −23) | −19% (−20 … −17) | −24% (−24 … −23) | −33% (−34 … −32) | −30% … −28% |
| `$a = []; array_push($a, ...$v);`, 1,000 ints | 23,498 | −36% (−36 … −35) | −36% (−36 … −35) | −35% (−36 … −35) | −38% (−38 … −37) | −37% … −34% |

Master against master (GCC 13.3) at the start and at the end of the series:

| call | master, CPU cycles per call (A/A first) | A/A first | A/A last |
|---|--:|--:|--:|
| `array_push($a, $i)`, one int; `$a` starts again from `[]` every 1,024 calls | 61 | 0% (0 … +7) | 0% (−2 … +10) |
| `array_push($a, $s)`, one string; same | 60 | 0% (0 … +22) | +2% (0 … +3) |
| `array_push($a, $i, $i, $i)`; same | 94 | 0% (−1 … +2) | 0% (0 … +6) |
| `array_push($a, ...$v)`, 16 ints; same | 535 | 0% (0 … +1) | +1% (0 … +1) |
| `array_push($a, $i)`, list with a hole (`unset($a[3])`) | 62 | 0% (−2 … +50) | −2% (−3 … 0) |
| `array_push($a, $i)` onto `['k' => 0]` (hash, old code path) | 77 | +1% (0 … +1) | 0% (−3 … +41) |
| `array_push($a, $i, $i, $i)` onto `['k' => 0]` | 129 | 0% (−1 … +2) | +1% (−1 … +2) |
| `$a = []; array_push($a, $i);` | 91 | 0% (0 … +22) | +1% (0 … +1) |
| `$a = []; array_push($a, $i, $i);` | 109 | 0% (0 … +1) | −1% (−1 … 0) |
| `$a = []; array_push($a, ...$v);`, 16 ints | 576 | 0% (−2 … +5) | −2% (−4 … +4) |
| `$a = []; array_push($a, ...$v);`, 1,000 ints | 23,487 | 0% (0 … +1) | 0% (−1 … 0) |
