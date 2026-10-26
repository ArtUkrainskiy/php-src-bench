# PR #23585 — sort/rsort/usort on packed arrays

Status: open pull request, independent review. Not in any release.

- PR: [php/php-src#23585](https://github.com/php/php-src/pull/23585) by LamentXU123
- Change head: [`b0208d10b1c3`](https://github.com/php/php-src/commit/b0208d10b1c3ca77f31ec9ea5e38906aa44d2daa) (unchanged since 10 September 2026)
- Measured against the PR's own base `f47cdadfb8d` (see Method)

## Summary

The PR makes `sort()`, `rsort()` and `usort()` sort a packed array of simple
values in place, instead of first turning it into a hash table and back. A packed
array is PHP's compact layout for a plain list with keys `0, 1, 2, …`. The win
is largest for integers: integer `sort`/`rsort` run **64–79% fewer instructions**
across four compilers, and **40–50% fewer CPU cycles** on large integer arrays.
Floats and strings gain less, `usort` gains 2–8%. No input in the matrix got
slower. The speed-up is automatic for qualifying arrays, with no change to user
code.

The cycles win is smaller than the instruction win because quicksort stays bound
by branch prediction and cache, not instruction count. The change removes the
per-element copies between the packed `zval` layout and the hash-table `Bucket`
layout, so the comparisons themselves, and their mispredictions, are unchanged.

Correctness is covered by differential fuzzing against the PR base (same inputs,
both binaries, output compared byte for byte) over scalars, floats, NaN, holes,
ties, all six sort flags, cross-type equal values, references, objects and a
re-entrant `usort`. Every case matched on all four compilers.

## What changes and why it is faster

Today `sort()` on a packed array converts it to a hash table (`Bucket` entries),
sorts the buckets, then rebuilds a packed array. Each element is copied twice.

The PR sorts the `zval` slots in place when the array is packed and holds only
simple values (null, bool, int, string, non-NaN double), with an integer-only
fast path that swaps just the `zval` value word. Objects, references, NaN, and
mixed or hash arrays keep the old `Bucket` path. `usort` sorts a duplicate of the
array, as before.

Stability: equal values keep their original order through a position marker
stored in `Z_EXTRA` on each slot, carried along by the full-`zval` swap. `rsort`
inverts the comparison result but not that marker, so reverse order is stable too.

## Trade-offs

No measured regression. Two limits worth stating:

- Strings at 65535 elements could not be measured here: building the string
  arrays costs ~2.75 billion instructions per batch, which swamps the sort cost,
  so the subtraction lands in noise. Strings at 10 and 64 elements are clean and
  shown below. This is a limit of the bench, not the PR.
- Cycles were measured only for integer `sort`/`rsort` and one float case, on one
  Intel laptop. The instruction counts below cover the full matrix on four
  compilers.

## Machine and method

- Intel Core i7-13700H laptop, Ubuntu. Instructions on E-cores (`taskset -c
  12-19`); cycles on one P-core (`taskset -c 2`), performance governor. Both core
  sets are overridable (`CORES_INS`, `CORE_CYC`); any isolated core(s) work.
- `perf` with `kernel.perf_event_paranoid <= 1` (the scripts abort if a counter
  comes back empty rather than print a plausible-looking wrong number).
- Compilers: GCC 13.3, GCC 14.2, clang 18.1, clang 20.1.
- Both binaries built with `bench pr` (an A/B build wrapper, part of this repo,
  `../../`): the PR head `b0208d10b1c3` and its own base `f47cdadfb8d`, so the
  delta is the change alone. Current `master` was not merged in (the PR needs a
  trivial rebase, see Merge). Builds land in `$BUILDS` (default `~/php-builds`) as
  `pr23585-{base,head}-<cc>`, where `<cc>` is the compiler version
  (`gcc13`/`gcc14`/`clang18`/`clang20`), not the `--cc` token.
- Build flags are the official PHP Docker image's release flags, so the numbers
  are not a debug build:
  `./configure --disable-all --disable-cgi --disable-phpdbg --enable-cli --enable-werror`
  with `CFLAGS='-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64'`
  and `LDFLAGS='-Wl,-O1 -pie'`. The sort code is in `ext/standard`, always built;
  opcache/JIT are off and do not touch this path.
- On another CPU or compiler the comparable quantity is the change-vs-base
  percentage, not the absolute counts. The large integer `sort`/`rsort` win holds
  on any recent compiler; exact percentages shift with code layout.
- Metric: a sort costs `instructions(sort mode) − instructions(nop mode)` per
  sort, where nop mode pre-generates the same arrays and does not sort. The
  per-sort figure is that difference divided by the batch size. Cycles use the
  same subtraction; the figure is the median of the head/base% column over five
  passes (the sort passes are paired base/head; the nop baseline is one pass,
  since generation cycles are stable).
- `cases`: `sort_bench.php` generates `batch` packed arrays of `size` random
  values (fixed seed `mt_srand(717)`), then sorts each once. Sizes 10, 64, 65535;
  batch 60000 / 20000 / 60.

## Results

Instructions per call, change vs base, range (min…max) across the four compilers.
Negative = fewer instructions (faster). The ranges here are read by hand from the
four per-compiler blocks in `instructions.txt`; there is no table generator.

| Call | size 10 | size 64 | size 65535 |
|---|---:|---:|---:|
| `sort` ints | −64…−68% | −68…−71% | −71…−75% |
| `rsort` ints | −68…−71% | −71…−75% | −75…−79% |
| `sort` floats | −17…−23% | −6…−12% | −2…−8% |
| `rsort` floats | −24…−28% | −16…−20% | −14…−18% |
| `sort` strings | −12…−15% | −4…−7% | — |
| `rsort` strings | −18…−20% | −11…−12% | — |
| `usort` ints | −7…−8% | −4…−5% | −2…−4% |
| `usort` floats | −7…−8% | −4…−5% | −2…−4% |
| `usort` strings | −6…−7% | −3…−4% | — |

Cycles, Intel P-core, median of the head/base% column over five passes
(`cycles.txt`):

| Call | GCC 13 | clang 20 |
|---|---:|---:|
| `sort` ints, 65535 | −41% | −43% |
| `rsort` ints, 65535 | −49% | — |
| `sort` ints, 64 | −37% | — |
| `sort` floats, 65535 | −5% | — |

Float cycles are noisy at this size: the five `sort` floats passes run −5% to
−10% (median −5%).

Base cost for scale (GCC 13, instructions per sort): `sort` ints is 3,493 at
size 10, 33,195 at 64, 91.1M at 65535.

## Output verification

Differential fuzzing, base vs head, same seed on both binaries. The hash (xxh128)
covers the sorted values, the keys, the internal array pointer and any warnings;
a mismatch would change it. All four compilers returned identical hashes.

- `sort_difftest.php` — scalars, floats, NaN, ±0, INF, holes, many ties, all six
  flags (`SORT_REGULAR`/`NUMERIC`/`STRING`/`NATURAL`/`STRING|CASE`/`NATURAL|CASE`),
  numeric strings, values near 2^53 and integer limits; `sort`, `rsort`, plain
  `usort`, a re-entrant `usort` that mutates the array, and one that reads the
  internal pointer.
- `sort_difftest2.php` — adds objects, references shared through a variable, and
  arrays of 256 and 1000 elements.
- `sort_difftest3.php` — adds mixed arrays where equal values of different types
  (`5 == 5.0 == "5" == true` under `SORT_REGULAR`) must keep their original order.

Sensitivity check: different seeds produce different hashes, so the comparison
does catch order and pointer differences.

The same fuzzers run clean on the PR head under an ASan + UBSan build
(`USE_ZEND_ALLOC=0`), with no sanitizer report. That covers the memory side the
output comparison cannot see: the ownership transfer during hole compaction, the
`usort` pin refcount, and the value-word-only swap.

The PR's 16 new `.phpt` tests pass in CI. For sort/rsort, objects and references
take the old `Bucket` path, so the fuzzer compares that path with itself there;
the new packed path is exercised on simple values and, for objects, through
`usort`.

## Not tested

- Cycles on AMD, and cycles for the full matrix (only integer `sort`/`rsort` and
  one float case were timed).
- Strings at 65535 elements (generation cost swamps the signal).
- A callgrind breakdown of why cycles drop ~41% while instructions drop ~71%
  (branch/cache-bound is the hypothesis, not profiled here).
- 32-bit and ZTS builds dynamically (reviewed by reading only).

## Merge

`git merge-tree` against current `master`: only `UPGRADING` and
`UPGRADING.INTERNALS` conflict, where both sides added changelog entries.
`Zend/zend_hash.c`, `Zend/zend_hash.h` and `ext/standard/array.c` merge cleanly.
A rebase is trivial.

## Reproduce

Run the scripts from this report directory (they `cd` to their own folder, where
`sort_bench.php` lives). Set `BUILDS` to wherever your two builds landed.

The scripts take a build-dir suffix (`gcc13`, `clang20`, …) and look for
`$BUILDS/pr23585-{base,head}-<suffix>/sapi/cli/php`. Replace the suffixes in the
commands with whatever yours are (`ls $BUILDS/pr23585-*`); on a box with gcc 15
and clang 19 they would be `gcc15` and `clang19`.

```
export BUILDS=$HOME/php-builds   # wherever the builds are

# 1. Build the PR head and its own base, four compilers (~10 min, ~400 MB).
bench pr 23585 --no-merge --slim --cc gcc,gcc-14,clang,clang-20

# 2. Instruction matrix, per compiler (~2 min each). Writes to stdout.
bash sort_measure.sh gcc13
bash sort_measure.sh clang20

# 3. Cycles headline on a quiet P-core.
bash sort_cycles.sh gcc13 65535 60 ints sort
bash sort_cycles.sh gcc13 65535 60 ints rsort

# 4. Correctness: same hash from base and head on each compiler.
for cc in gcc13 gcc14 clang18 clang20; do
  b=$BUILDS/pr23585-base-$cc/sapi/cli/php
  h=$BUILDS/pr23585-head-$cc/sapi/cli/php
  echo "$cc: $($b -n sort_difftest3.php 1 15000) vs $($h -n sort_difftest3.php 1 15000)"
done
```

Each script prints its own column headers and sweeps its matrix internally. The
ASan check is the same fuzzers on an ASan + UBSan build, run with
`USE_ZEND_ALLOC=0`.

Without the `bench pr` wrapper (this repo, `../../`), build the two commits by
hand into the layout step 1 produces:

```
for side in base:f47cdadfb8d head:b0208d10b1c3; do
  name=${side%%:*}; sha=${side#*:}
  git -C php-src worktree add ../wt-$name $sha
  ( cd ../wt-$name && ./buildconf --force
    ./configure --disable-all --disable-cgi --disable-phpdbg --enable-cli --enable-werror \
      CFLAGS='-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64' \
      LDFLAGS='-Wl,-O1 -pie'
    make -j"$(nproc)" )
  mkdir -p "$BUILDS/pr23585-$name-gcc13/sapi/cli"
  cp ../wt-$name/sapi/cli/php "$BUILDS/pr23585-$name-gcc13/sapi/cli/php"
done
```

Set `CC=clang` before `./configure` for a clang build, and name the dir to match.
