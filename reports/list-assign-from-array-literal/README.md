# List assignment from an array literal without the array (php-src PR 24180)

php-src pull request [#24180](https://github.com/php/php-src/pull/24180) (issue [GH-23048](https://github.com/php/php-src/issues/23048)), commit [`86a9f1ed916`](https://github.com/php/php-src/pull/24180/commits/86a9f1ed916) "Zend: Compile a list assignment from an array literal without the array", compared with its parent on master, [`5ccc56b1e43`](https://github.com/php/php-src/commit/5ccc56b1e43). This version follows the review of 16 October 2026: the earlier one gave every target of a non-constant value a `COPY_TMP` of it and freed the values after the last assignment, to keep the destruction order of the array; the reviewers agreed that the order within one statement need not be kept, and the copies are gone. Measured on 17 October 2026 on a 13th Gen Intel(R) Core(TM) i7-13700H.

`[$a, $b] = [$b, $a];` compiled to INIT_ARRAY + ADD_ARRAY_ELEMENT, two FETCH_LIST_R, two ASSIGN and a FREE. With the change, when the result is unused, the right side is an array literal and the left side a flat list with a target for every value, it compiles to the four opcodes of the issue:

```
T2 = QM_ASSIGN CV1($b)
T3 = QM_ASSIGN CV0($a)
ASSIGN CV0($a) T2
ASSIGN CV1($b) T3
```

The values are evaluated in order before the first assignment and a variable among them is copied first, so the swap still swaps. Assignments in the expression lists of a `for` loop, whose results are not used either, are compiled the same way. Nested lists, keys, references, spread, a different number of values and targets and a used result keep the usual compilation.

## Summary

- A swap of two variables: 47% fewer cycles per call of a function doing it, 922 → 467 instructions, below a swap through a temporary variable (493). Rotation of three: −49%; ten Fibonacci steps: −71%, the same in the step list of a `for`: −72%; array elements: −36%; properties: −27%; `[$a, $b] = [1, 2]`: −28% (GCC 13.3, release build with the flags of the official Docker image).
- Loops of 300,000 statements with opcache ([`jit-stress.php`](jit-stress.php), wall time, median of five): a swap of two ints 10.4 → 1.2 ms without the JIT, 8.5 → 0.32 ms with the tracing JIT, 8.4 → 0.25 ms with the function JIT.
- Behaviour change, accepted in the review: a value its target does not keep (a setter that drops it, the same variable twice, a typed property that coerces it) is released at that assignment instead of after the last one, and a destructor that throws there stops the rest of the statement. Statements this does not cover, and the outputs of all hand-written cases, are as on master.
- The new path behaves the same without opcache, with the optimizer and with the tracing and function JIT (3,376 generated programs).
- Not measured: other compilers and the AMD machine; the change is in the compiler, the executed opcodes are what changes.

## Results

Each row is a call of a function that does the statement once, from [`swap-suite.php`](swap-suite.php); the empty call of that function is the first row. Change in CPU cycles per call relative to master (negative = fewer cycles, faster); median over the passes of B against A of the same pass.

<!-- bench-table compare.json --labels labels.txt --header -->
Machine: 13th Gen Intel(R) Core(TM) i7-13700H, CPU 2, kernel 7.0.0-34-generic.
Group gcc13: A = gh23048-master (5ccc56b1e43 GCC 13.3, profile docker), B = gh23048-head (86a9f1ed916 GCC 13.3, profile docker).
5 alternating passes per case, user-space cycles per call (perf stat, minus the empty loop), A against A at the start and the end.
Machine: CPU governor is 'powersave': frequency scaling adds noise (sudo ./bench tune on).
Machine: turbo boost is on: thermal and frequency drift between rounds (sudo ./bench tune on).
Machine: load average is 15.6: other programs are competing for the CPU.
negative = fewer cycles (faster)

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 |
|---|--:|--:|
| empty call of the function, for reference (ints) | 71 | 0% ~ |
| empty call of the function, for reference (strings) | 84 | +1% ~ |
| empty call of the function, for reference (arrays) | 84 | 0% ~ |
| `[$a, $b] = [$b, $a]`, ints | 173 | −47% |
| `[$a, $b] = [$b, $a]`, strings | 195 | −43% |
| `[$a, $b] = [$b, $a]`, arrays | 197 | −42% |
| `$t = $a; $a = $b; $b = $t;`, ints (not changed) | 95 | 0% ~ |
| `$t = $a; $a = $b; $b = $t;`, strings (not changed) | 114 | 0% ~ |
| `$t = $a; $a = $b; $b = $t;`, arrays (not changed) | 117 | −2% |
| `[$a, $b, $c] = [$b, $c, $a]` | 209 | −49% |
| 10 × `[$a, $b] = [$b, $a + $b]` | 1,212 | −71% |
| 10 × the same in the step list of a `for` | 1,224 | −72% |
| `[$p[0], $p[1]] = [$p[1], $p[0]]` | 234 | −36% |
| the same through a temporary (not changed) | 160 | +1% |
| `[$o->a, $o->b] = [$o->b, $o->a]` | 347 | −27% |
| `[$a, $b] = [1, 2]` | 74 | −28% |
| `[$a, $b] = $pair` (not covered) | 91 | 0% ~ |
| `['x' => $a, 'y' => $b] = ['x' => $b, 'y' => $a]` (not covered) | 191 | −2% |

Control: master against itself.

| call | master, CPU cycles per call (GCC 13.3) | A/A start | A/A end |
|---|--:|--:|--:|
| empty call of the function, for reference (ints) | 72 | −1% | +1% |
| empty call of the function, for reference (strings) | 83 | 0% | +4% |
| empty call of the function, for reference (arrays) | 84 | 0% | −4% |
| `[$a, $b] = [$b, $a]`, ints | 172 | 0% | 0% |
| `[$a, $b] = [$b, $a]`, strings | 199 | −1% | +1% |
| `[$a, $b] = [$b, $a]`, arrays | 197 | +1% | 0% |
| `$t = $a; $a = $b; $b = $t;`, ints (not changed) | 96 | 0% | +2% |
| `$t = $a; $a = $b; $b = $t;`, strings (not changed) | 116 | 0% | +2% |
| `$t = $a; $a = $b; $b = $t;`, arrays (not changed) | 116 | 0% | −1% |
| `[$a, $b, $c] = [$b, $c, $a]` | 209 | −1% | −1% |
| 10 × `[$a, $b] = [$b, $a + $b]` | 1,201 | 0% | +2% |
| 10 × the same in the step list of a `for` | 1,238 | +1% | −2% |
| `[$p[0], $p[1]] = [$p[1], $p[0]]` | 235 | +2% | 0% |
| the same through a temporary (not changed) | 159 | 0% | 0% |
| `[$o->a, $o->b] = [$o->b, $o->a]` | 348 | 0% | −3% |
| `[$a, $b] = [1, 2]` | 74 | 0% | −1% |
| `[$a, $b] = $pair` (not covered) | 92 | 0% | 0% |
| `['x' => $a, 'y' => $b] = ['x' => $b, 'y' => $a]` (not covered) | 187 | 0% | 0% |

~: the change is not larger than the A/A control of the same row: not evidence of a difference.
<!-- /bench-table -->

Full table, with the range over the passes and the change in instructions:

<!-- bench-table compare.json --labels labels.txt --full -->
| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | instructions |
|---|--:|--:|--:|
| empty call of the function, for reference (ints) | 71 | 0% (−2 … +8) ~ | 0% |
| empty call of the function, for reference (strings) | 84 | +1% (−1 … +2) ~ | 0% |
| empty call of the function, for reference (arrays) | 84 | 0% (0 … +2) ~ | 0% |
| `[$a, $b] = [$b, $a]`, ints | 173 | −47% (−49 … −44) | −49% |
| `[$a, $b] = [$b, $a]`, strings | 195 | −43% (−45 … −42) | −48% |
| `[$a, $b] = [$b, $a]`, arrays | 197 | −42% (−44 … −39) | −48% |
| `$t = $a; $a = $b; $b = $t;`, ints (not changed) | 95 | 0% (−5 … +2) ~ | 0% |
| `$t = $a; $a = $b; $b = $t;`, strings (not changed) | 114 | 0% (−2 … +3) ~ | 0% |
| `$t = $a; $a = $b; $b = $t;`, arrays (not changed) | 117 | −2% (−4 … 0) | 0% |
| `[$a, $b, $c] = [$b, $c, $a]` | 209 | −49% (−49 … −48) | −51% |
| 10 × `[$a, $b] = [$b, $a + $b]` | 1,212 | −71% (−72 … −69) | −75% |
| 10 × the same in the step list of a `for` | 1,224 | −72% (−73 … −71) | −75% |
| `[$p[0], $p[1]] = [$p[1], $p[0]]` | 234 | −36% (−38 … −34) | −36% |
| the same through a temporary (not changed) | 160 | +1% (−2 … +5) | 0% |
| `[$o->a, $o->b] = [$o->b, $o->a]` | 347 | −27% (−28 … −25) | −27% |
| `[$a, $b] = [1, 2]` | 74 | −28% (−31 … −26) | −28% |
| `[$a, $b] = $pair` (not covered) | 91 | 0% (−4 … +2) ~ | 0% |
| `['x' => $a, 'y' => $b] = ['x' => $b, 'y' => $a]` (not covered) | 191 | −2% (−9 … 0) | 0% |

Control: master against itself.

| call | master, CPU cycles per call (GCC 13.3) | A/A start | A/A end |
|---|--:|--:|--:|
| empty call of the function, for reference (ints) | 72 | −1% (−2 … +2) | +1% (−2 … +2) |
| empty call of the function, for reference (strings) | 83 | 0% (−1 … +6) | +4% (0 … +4) |
| empty call of the function, for reference (arrays) | 84 | 0% (−10 … 0) | −4% (−6 … +3) |
| `[$a, $b] = [$b, $a]`, ints | 172 | 0% (−8 … +4) | 0% (−1 … +4) |
| `[$a, $b] = [$b, $a]`, strings | 199 | −1% (−2 … +5) | +1% (−2 … +2) |
| `[$a, $b] = [$b, $a]`, arrays | 197 | +1% (−3 … +2) | 0% (−3 … +1) |
| `$t = $a; $a = $b; $b = $t;`, ints (not changed) | 96 | 0% (−4 … +4) | +2% (−1 … +5) |
| `$t = $a; $a = $b; $b = $t;`, strings (not changed) | 116 | 0% (−5 … +1) | +2% (−1 … +4) |
| `$t = $a; $a = $b; $b = $t;`, arrays (not changed) | 116 | 0% (−4 … +1) | −1% (−14 … +3) |
| `[$a, $b, $c] = [$b, $c, $a]` | 209 | −1% (−10 … +6) | −1% (−3 … +5) |
| 10 × `[$a, $b] = [$b, $a + $b]` | 1,201 | 0% (−3 … +6) | +2% (−1 … +6) |
| 10 × the same in the step list of a `for` | 1,238 | +1% (−18 … +76) | −2% (−5 … +3) |
| `[$p[0], $p[1]] = [$p[1], $p[0]]` | 235 | +2% (−1 … +5) | 0% (−1 … +8) |
| the same through a temporary (not changed) | 159 | 0% (−2 … +4) | 0% (−2 … +1) |
| `[$o->a, $o->b] = [$o->b, $o->a]` | 348 | 0% (−3 … +6) | −3% (−7 … −1) |
| `[$a, $b] = [1, 2]` | 74 | 0% (−6 … 0) | −1% (−2 … +2) |
| `[$a, $b] = $pair` (not covered) | 92 | 0% (−1 … +1) | 0% (−4 … +1) |
| `['x' => $a, 'y' => $b] = ['x' => $b, 'y' => $a]` (not covered) | 187 | 0% (−2 … +4) | 0% (−7 … +6) |

~: the change is not larger than the A/A control of the same row: not evidence of a difference.
<!-- /bench-table -->

### Loops with opcache and the JIT

[`jit-stress.php`](jit-stress.php) with 300,000 iterations per loop, run by [`jit-loops.sh`](jit-loops.sh): opcache with `optimization_level=-1`, no JIT, tracing JIT with the default thresholds, function JIT; master and the change alternating, five passes, pinned to CPU 2. Wall time in ms, median of five ([`jit-loops.txt`](jit-loops.txt)); the outputs of both builds are identical in every mode.

| loop | no JIT | tracing JIT | function JIT |
|---|--:|--:|--:|
| swap of two ints | 10.43 → 1.21 | 8.48 → 0.32 | 8.41 → 0.25 |
| Fibonacci step | 13.34 → 2.21 | 8.84 → 2.33 | 9.32 → 2.35 |
| rotation of three strings | 19.25 → 4.15 | 13.11 → 1.04 | 13.89 → 1.93 |
| swap of two array elements | 20.62 → 7.13 | 11.70 → 1.34 | 12.32 → 2.02 |
| swap of two properties | 21.42 → 8.47 | 20.17 → 9.42 | 19.95 → 8.75 |
| swap with the types changing half-way | 16.20 → 3.73 | 12.08 → 1.38 | 11.91 → 0.74 |
| skipped and extra values (not covered) | 15.56 → 14.73 | 11.42 → 10.71 | 12.41 → 10.94 |
| nested list (not covered) | 28.53 → 28.46 | 20.91 → 20.76 | 21.73 → 21.52 |

The two loops that are not covered compile to the same opcodes on both builds (checked with `opcache.opt_debug_level=0x20000`); their 0–12% is code placement and the noise of wall times, not the change.

## Code

`Zend/zend_compile.c`, +73/−4. `zend_list_assign_from_array_applies()` accepts a flat unkeyed list and literal without references or spread, with one value per target; `zend_try_compile_list_assign_from_array()` compiles the values in order into a `safe_emalloc` array of znodes, copies a variable with `QM_ASSIGN`, then assigns each value to its target with `zend_emit_assign_znode()`, which consumes it. `zend_compile_for_expr_list()` compiles an assignment whose result is unused as a statement.

Why the restrictions stay:

- Skipped or extra values: the copy that would keep an untaken value alive until the end is `QM_ASSIGN` + `FREE`, which the block pass of opcache reduces to `CHECK_VAR`, so the result would differ with and without opcache.
- Nested lists: excluded in this version. Without the copies they could take the same path: the mutation that lets nested targets through gives the same output as master on every nested case (see Tests), so this is a follow-up, not a correctness limit.

A fatal compile error inside the new path (`[$a, f()] = [1, 2]`, `[$a, $b] = [1, $this = 2]`) leaves the znode array unfreed (48 bytes, seen by LeakSanitizer with `USE_ZEND_ALLOC=0`); `switch`, `match` and multi-catch leak their jump arrays on master the same way, and the Zend allocator releases them at the end of the request.

## Tests

Builds: master and the change with the flags of the official Docker image (`--enable-werror`), and both as debug builds with ASan and UBSan. Modes: [`modes.sh`](modes.sh) runs a file without opcache, with the optimizer (`optimization_level=-1`), with the tracing JIT (every hot threshold 1) and with the function JIT; every case is a file with `opcache.file_update_protection=0`, since opcache does not optimize code given with `-r`.

- [`combo2.php`](combo2.php): 3,376 generated programs, two targets of 15 kinds (variables, typed properties, `ArrayAccess` that drops or stores, `__set`, hooks that drop or store, static properties, `$arr[]`, string offsets, a nested list) and two values of 4 kinds, with printing destructors and setters. The change gives the same output in all four modes. Against master 273 programs differ, and every one of them prints the same events in another order: the first target does not keep its value, which is now released at its assignment. Output: [`combo2-output.txt`](combo2-output.txt).
- [`destructure-cases.php`](destructure-cases.php) (run through `modes.sh`) and [`destructure-cases-2.php`](destructure-cases-2.php) (each case in its own process from a file; the mode from the environment, `OPC=1` and `JIT=tracing|function`, with the default JIT thresholds): 96 hand-written cases (nested lists, skipped and extra values, references, generators, fibers, `$GLOBALS`, exceptions in a value, a target and an assignment, compile errors): the same output as master, without opcache, with the optimizer and with both JITs.
- Zend/tests and ext/opcache/tests on the ASan build: 6,504 passed; Zend/tests with opcache and with the tracing JIT: 5,552 passed each. The only failures were the three tests whose expectations this version changes, run from the build tree before they were updated; the updated ones pass in all four modes on the ASan build.
- The repro files of the earlier review rounds under ASan in all four modes: the leak reports are the same as on master (files that end in a fatal compile error).
- Real code (measured on the previous version, whose `zend_list_assign_from_array_applies()` and `for` hook are unchanged, so the same statements are covered): all `.php` files of two large `vendor` trees, 46,857 files and 327,462 op_arrays, compiled on both builds with the opcodes dumped — 41 op_arrays differ, all because of 56 covered statements; 157 of their 167 targets are plain variables, 10 array elements.
- Tests in the PR: [`Zend/tests/list/list_from_array_literal.phpt`](https://github.com/php/php-src/blob/86a9f1ed916/Zend/tests/list/list_from_array_literal.phpt) (values and targets of every kind, `for` lists, keyed values and a nested list that keep the usual path; expectations from master), `list_from_array_literal_order.phpt` and its `_opt` twin (evaluation order and the new lifetime, the same with `optimization_level=-1`), `list_from_array_literal_undefined.phpt`, and the opcode shape in `ext/opcache/tests/opt/list_assign_from_array_literal.phpt`.

Mutations ([`mutations.php`](mutations.php), `bench mutate` on the ASan build, checks: the tests above). No differential test: the order of destructors differs from master on purpose.

| mutation | tests |
|---|---|
| a variable value is not copied before the assignments | caught (5 failed) |
| values assigned to the targets in reverse order | caught (6 failed) |
| extra values accepted | caught (2 failed) |
| the condition list of a `for` compiled as unused | caught (1 failed) |
| keyed values accepted | caught (1 failed), after the keyed case was added; missed before |
| nested list targets accepted | missed: same output as master on every nested case |

## Reproduce

From the root of [php-src-bench](https://github.com/ArtUkrainskiy/php-src-bench), with php-src next to it: (`86a9f1ed916` is the PR head: `git fetch https://github.com/php/php-src pull/24180/head`):

```
CC=cc ./bench build --slim --profile docker gh23048-master 5ccc56b1e43
CC=cc ./bench build --slim --profile docker gh23048-head 86a9f1ed916
./bench compare reports/list-assign-from-array-literal/swap-suite.php gcc13=gh23048-master:gh23048-head
./bench table results/<date>-compare-swap-suite.json --labels reports/list-assign-from-array-literal/labels.txt --full
```

The series in this report: [`compare.json`](compare.json); `bench table compare.json` renders it.
