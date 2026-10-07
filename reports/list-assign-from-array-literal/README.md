# List assignment from an array literal without the array

php-src change: branch `destructure-array-literal`, "Zend: Compile a list assignment from an
array literal without the array" (php/php-src issue GH-23048), compared with its parent on
master, [`e17e2970bc0`](https://github.com/php/php-src/commit/e17e2970bc0).

`[$a, $b] = [$b, $a];` compiled to INIT_ARRAY + ADD_ARRAY_ELEMENT, two FETCH_LIST_R, two
ASSIGN and a FREE. With the change, when the result is unused, the right side is an array
literal and the left side a plain list with a target for every value, it compiles to two
QM_ASSIGN (the variables are copied before any assignment) and two ASSIGN. Nested literals are
handled the same way, and so are assignments in the expression lists of a `for` loop, whose
results are not used either; keys, references, spread, a different number of values and
targets and a used result keep the usual compilation.

Lifetime of the values: a value assigned to a plain variable is held by that variable. For any
other target (an array element, a property, a setter) or a variable the list assigns again, a
COPY_TMP of the value is assigned and the value itself is freed after the last assignment, as
the array was; so a setter that drops the value, or a destructor that throws, sees the same
order as before. What remains observable: an object coerced away on assignment through a
reference to a typed property is released at that assignment, and the order in which pending
values are destroyed when an assignment throws follows the temporaries rather than the array.

Lists with values nobody takes, `[, $b] = [f(), g()]`, are left alone on purpose: the copy that
would keep such a value alive is `T = QM_ASSIGN CV; ...; FREE T`, which opcache's block pass
reduces to `CHECK_VAR CV`, so the form would behave differently with and without opcache.

Holding every value with COPY_TMP, plain variables included, was measured and rejected: swap
922 → 523 instructions instead of 467, ten Fibonacci steps 2,064 instead of 1,504, and with
opcache the swap loop 5 times slower than this version, because the copies stop the DFA pass
from folding the swap into three QM_ASSIGN.

## Summary (i7-13700H, release builds, `perf stat` instructions per statement)

| statement | time | instructions |
|---|---|---|
| `[$a, $b] = [$b, $a]`, ints | 1.8× faster | 922 → 467 |
| the same with strings or arrays | 1.8× faster | 996 → 521 |
| `[$a, $b, $c] = [$b, $c, $a]` | 1.9× faster | 1,119 → 545 |
| ten Fibonacci steps `[$a, $b] = [$b, ($a + $b) % M]` | 3.5× faster | 6,114 → 1,504 |
| the same in the step list of the `for` | 3.6× faster | 6,114 → 1,504 |
| `[$p[0], $p[1]] = [$p[1], $p[0]]` (COPY_TMP path) | 1.5× faster | 1,290 → 879 |
| the same through a temporary | same | 864 |
| `[$o->a, $o->b] = [$o->b, $o->a]` (COPY_TMP path) | 1.3× faster | 1,742 → 1,331 |
| `[$a, $b] = [1, 2]` | 1.4× faster | 396 → 286 |
| swap through a temporary (reference) | same | 493 |
| `[$a, $b] = $array`, keyed list (not covered) | same | same |

A swap of variables through an array literal now costs less than a swap through a temporary
variable (467 vs 493 instructions); a swap of array elements costs about the same as its
temporary form (879 vs 864).

Loops of 300,000 statements (`jit-stress.php`, opcache on, pinned to one core), master → change:

| loop | no JIT | tracing JIT | function JIT |
|---|---|---|---|
| swap of two ints | 5.0 → 0.6 ms | 3.6 → 0.16 ms | 3.6 → 0.11 ms |
| swap of two array elements | 8.0 → 3.6 ms | 4.1 → 1.2 ms | 4.2 → 1.2 ms |
| swap of two properties | 8.1 → 4.7 ms | 7.5 → 4.9 ms | 7.2 → 4.2 ms |
| nested `[[$a, $b], $c] = [[$b, $c], $a]` | 10.7 → 0.7 ms | 7.7 → 0.14 ms | 7.8 → 0.11 ms |

The loop outputs are identical on both builds. The suite is `swap-suite.php` next to this file;
raw run in `swap-suite.json`.

## Verification

- 97 behaviour cases (swap, rotation, nested lists, skipped and extra values, destructor
  order, exceptions in a value and in an assignment, properties, static properties, array
  elements with side effects, `$GLOBALS`, references, keys, spread, compile errors) give
  identical output on master and the change, on a release build, a debug build, with opcache,
  and with the tracing and function JIT. Each case is compiled from a file with
  `opcache.file_update_protection=0`, so the optimizer really runs on it; code given with
  `-r` is not optimized, and an earlier run that used `-r` missed the block-pass issue above.
- About 3,700 generated programs from three review agents (combinations of 15 target kinds and
  4 value kinds, generators and fibers, references, hooks, readonly, string offsets, nesting
  up to 3,000 levels, 500-element lists): no difference besides the two documented ones.
- Zend/tests and ext/opcache/tests on the debug build (with zend_test): 6,499 passed,
  0 failed; Zend/tests with opcache and with the tracing JIT: 5,560 passed, 0 failed each.
- All `.php` files of two large `vendor` trees (46,857 files, 327,462 op_arrays) compiled on
  both builds with the opcodes dumped: 41 op_arrays differ, every one of them contains a
  covered statement (46 statements; 114 of their 124 targets are plain variables, 10 are array
  elements, none repeats a variable); the only opcodes removed are INIT_ARRAY,
  ADD_ARRAY_ELEMENT, FETCH_LIST_R and FREE, the only ones added QM_ASSIGN. Nothing else in
  the output changes.
- Tests added: five in Zend/tests/list (values and targets, `for` loop lists, evaluation order
  and lifetime of the values including a throwing destructor and the typed-property reference
  case, undefined variables in the new path with line numbers, missing values, the two compile
  errors that still apply to nested lists), an opcode-shape test in ext/opcache/tests/opt, and
  a nested-literal case in Zend/tests/stack_limit.
