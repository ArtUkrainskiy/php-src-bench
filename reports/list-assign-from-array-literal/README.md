# List assignment from an array literal without the array

php-src change: branch `destructure-array-literal`, "Zend: Compile a list assignment from an
array literal without the array" (php/php-src issue GH-23048), compared with its parent on
master, [`e17e2970bc0`](https://github.com/php/php-src/commit/e17e2970bc0).

`[$a, $b] = [$b, $a];` compiled to INIT_ARRAY + ADD_ARRAY_ELEMENT, two FETCH_LIST_R, two
ASSIGN and a FREE. With the change, when the result is unused, the right side is an array
literal and the left side a plain list with a target for every value, it compiles to two
QM_ASSIGN (the variables are copied before any assignment), two COPY_TMP + ASSIGN pairs and
two FREE. Nested literals are handled the same way, and so are assignments in the expression
lists of a `for` loop, whose results are not used either; keys, references, spread, a different
number of values and targets and a used result keep the usual compilation.

Lifetime of the values: the array held every value until after the last assignment, and that
is observable through destructors (a setter that drops the value, two targets that are
references to each other, a destructor that throws and cuts the statement short). So every
target is assigned a COPY_TMP of its value and the values themselves are freed after the last
assignment, exactly when the array was; constants need no copy. Consuming the value directly
when the target is a plain variable was built and measured (swap 467 instead of 523) and
rejected: whether a variable keeps its value until the end of the statement is a runtime
property (references, user code in a later target's expression), not something the compiler
can prove, and a throwing destructor turns the difference into a control-flow change. What
remains observable is the order in which pending values are destroyed when an assignment
throws: that of the temporaries instead of that of the array.

Lists with values nobody takes, `[, $b] = [f(), g()]`, are left alone on purpose: the copy that
would keep such a value alive is `T = QM_ASSIGN CV; ...; FREE T`, which opcache's block pass
reduces to `CHECK_VAR CV`, so the form would behave differently with and without opcache.

## Summary (i7-13700H, release builds, `perf stat` instructions per statement)

| statement | time | instructions |
|---|---|---|
| `[$a, $b] = [$b, $a]`, ints | 1.5× faster | 922 → 523 |
| the same with strings or arrays | 1.6× faster | 996 → 585 |
| `[$a, $b, $c] = [$b, $c, $a]` | 1.5× faster | 1,119 → 629 |
| ten Fibonacci steps `[$a, $b] = [$b, ($a + $b) % M]` | 2.2× faster | 6,114 → 2,064 |
| the same in the step list of the `for` | 2.2× faster | 6,114 → 2,064 |
| `[$p[0], $p[1]] = [$p[1], $p[0]]` | 1.5× faster | 1,290 → 879 |
| the same through a temporary | same | 864 |
| `[$o->a, $o->b] = [$o->b, $o->a]` | 1.3× faster | 1,742 → 1,331 |
| `[$a, $b] = [1, 2]` | 1.4× faster | 396 → 286 |
| swap through a temporary (reference) | same | 493 |
| `[$a, $b] = $array`, keyed list (not covered) | same | same |

Loops of 300,000 statements (`jit-stress.php`, opcache on, pinned to one core), master → change:

| loop | no JIT | tracing JIT | function JIT |
|---|---|---|---|
| swap of two ints | 5.1 → 1.1 ms | 3.8 → 0.5 ms | 4.0 → 0.6 ms |
| swap of two array elements | 7.9 → 3.7 ms | 4.8 → 1.2 ms | 4.6 → 1.2 ms |
| swap of two properties | 8.0 → 4.7 ms | 7.8 → 4.8 ms | 7.1 → 4.7 ms |
| nested `[[$a, $b], $c] = [[$b, $c], $a]` | 10.7 → 0.9 ms | 7.6 → 1.4 ms | 7.7 → 1.3 ms |

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
  up to 3,000 levels, 500-element lists): the only difference left is the destruction order of
  pending values when an assignment throws (30 of the 3,376 combinations, all of that shape).
- Zend/tests and ext/opcache/tests on the debug build (with zend_test): 6,499 passed,
  0 failed; Zend/tests with opcache and with the tracing JIT: 5,560 passed, 0 failed each.
- All `.php` files of two large `vendor` trees (46,857 files, 327,462 op_arrays) compiled on
  both builds with the opcodes dumped: 41 op_arrays differ, every one of them contains a
  covered statement (46 statements; 114 of their 124 targets are plain variables, 10 are array
  elements); the only opcodes removed are INIT_ARRAY, ADD_ARRAY_ELEMENT and FETCH_LIST_R, the
  only ones added QM_ASSIGN, COPY_TMP and FREE. Nothing else in the output changes.
- Tests added: five in Zend/tests/list (values and targets, `for` loop lists, evaluation order
  and lifetime of the values including a throwing destructor, two targets that are references
  to each other and the unwind order, undefined variables in the new path with line numbers, missing values, the two compile
  errors that still apply to nested lists), an opcode-shape test in ext/opcache/tests/opt, and
  a nested-literal case in Zend/tests/stack_limit.
