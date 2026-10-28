# Multi-pattern string search and replace for PHP

Status: prototype, measured 28 October 2026. Not a PR yet; prototype for an upcoming RFC.
Prototype extension `ext/strmatch` on a fork branch:
https://github.com/php/php-src/compare/master...ArtUkrainskiy:php-src:str-matcher-prototype
Measured against `php/php-src` master `758c9ac5492`.

This report compares every way to search or replace many fixed substrings at once on
PHP today, and a C Aho-Corasick prototype (`Str\Matcher` / `Str\Replacer`), across
dictionary sizes, subject sizes, and single-use vs reuse.

## Summary

For a handful of needles a `strpos` loop is fine. At hundreds or thousands of fixed
substrings, every current option breaks down, and a prepared automaton built once and
reused wins by a wide margin.

In one line: this is a prototype (not installable yet) that adds `Str\Matcher` and
`Str\Replacer`. `Str\Replacer` mirrors `strtr` semantics — it is not a `str_replace` or
`html_entity_decode` replacement. It pays off when one automaton is reused across many
subjects (a long-lived worker, or a loop over many inputs). The case for putting it in
core is the build cost: building the automaton in C is about 110x cheaper than any
pure-PHP build (below), so userland cannot match it. The rule for when it wins is the
per-call cost: reuse only amortizes the build, so it beats tools with a higher per-call
cost (the `strpos` loop, `strtr`) but not a specialized native function with a lower one
(`html_entity_decode`).

- **Search.** A `strpos` loop is O(needles × subject) and grows without bound. A `preg`
  alternation is heavy and stops compiling around a 44 KB pattern (about 5000 short
  keywords), returning `false`. A pure-PHP Aho-Corasick library is flat in the needle
  count but carries a high constant and a very expensive build. The prototype's
  `Str\Matcher::matchAll` is flat in the needle count at about 0.49M instructions for a
  16 KB subject — 20x fewer than the `strpos` loop at 500 keywords and 233x fewer at
  5000, and about 18x to 126x faster in wall-clock over that range. If you only need
  presence, `matches()` stops at the first hit (about 1.2K instructions when a match is
  near the start); on a subject with no match it is a full scan, about 246K at 16 KB.
- **Replace.** `Str\Replacer::replace` is about 25x fewer instructions than `strtr` at
  500 keywords and up, and 12.7x faster in wall-clock at 500 keywords (5.7x at 5000
  keywords over a 64 KB subject). The instruction ratio is larger than the wall-clock
  ratio because `strtr` runs at higher IPC and `replace` is partly memory-bound building
  the output string.
- **Build once.** Building the automaton in C costs about 21M instructions for 5000
  keywords, about 110x less than the pure-PHP library's 2.36 billion. That gap is why
  a prepared object in C is worth adding rather than leaving to userland.

Costs to weigh, not hidden at the end:

- **Memory.** The transition table is about 4.3 MB for 5000 ASCII keywords with the
  alphabet-reduced layout (one column per byte value that occurs), and up to ~30 MB with
  a dense 256-column table. This is the prototype's representation, not the shipped one:
  the production target is a compact automaton (double-array trie), which is the memory
  figure that should decide core inclusion. `replace` also uses a transient scratch array
  of 4 bytes per subject byte.
- **No win over a specialist.** A specialized native function beats the general automaton
  at any reuse: `html_entity_decode` is about 8x faster than `Str\Replacer` on named
  entity decoding and has no build (details below). The tool is for arbitrary user
  dictionaries, where the alternatives are the `strpos` loop and `strtr`.
- **Single use.** With no reuse, the build dominates. Search still wins single-use
  (build + one `matchAll` beats one `strpos` loop at 500 and 5000 keywords). Replace
  wins single-use for small and medium dictionaries, but at 5000 keywords a single
  build + `replace` costs more than one `strtr`; the win starts from the second call.
- **Adversarial input.** `matchAll` and `replace` are O(subject + matches); a
  dictionary like `{a, aa, aaa, ...}` over `aaaa...` produces a quadratic number of
  matches. `countMatches` is O(subject) regardless, and `matches` is immune.

## Approaches compared and correctness

Search (which keywords occur / all occurrences):

- `strpos` loop (`str_contains` per needle) — the correctness oracle.
- `preg` alternation, sorted longest-first so PCRE picks the longest match.
- pure-PHP Aho-Corasick (wikimedia/AhoCorasick, used by MediaWiki).
- `Str\Matcher`: `matches`, `countMatches`, `getMatchedKeywords`, `matchAll`.

Replace (replace many fixed substrings):

- `str_replace(array, array, subject)` — note: sequential and cascading, so a
  replacement can be re-matched; not leftmost-longest in general.
- `strtr(subject, array)` — leftmost-longest, non-overlapping, no rescan.
- `preg_replace_callback` over a sorted alternation.
- pure-PHP Aho-Corasick replacer (wikimedia).
- `Str\Replacer::replace` — same semantics as `strtr`.

At 50 and 500 keywords all search approaches return the same presence set as the
`strpos` oracle, and `strtr`, `Str\Replacer`, the pure-PHP replacer and (on these
inputs) `str_replace` and `preg_replace` produce identical output. At 5000 keywords
`preg` fails to compile; the pure-PHP library and the prototype stay correct. This was
checked by `compare.php check`, plus byte-for-byte differential tests (below).

## Results

The instruction-count tables are from the Intel machine (i7-13700H); the wall-clock and
memory tables are from the AMD machine (Ryzen 9 5950X). Both are named in each heading
and in Machine and method; instruction counts and ns are not from the same box.

### Search, instructions per call (16 KB subject, Intel i7-13700H, one core)

| approach | 50 kw | 500 kw | 5000 kw |
|---|---:|---:|---:|
| `strpos` loop | 351,932 | 9,702,445 | 114,027,258 |
| `preg` (sorted) | 4,497,646 | 50,489,093 | does not compile |
| pure-PHP Aho-Corasick | 17,063,071 | 17,404,513 | 18,138,987 |
| `Str\Matcher::matches` | 1,169 | 1,202 | 2,381 |
| `Str\Matcher::countMatches` | 196,870 | 196,906 | 196,774 |
| `Str\Matcher::getMatchedKeywords` | 368,378 | 422,991 | 433,526 |
| `Str\Matcher::matchAll` | 491,234 | 492,108 | 490,433 |

The prototype is flat in the keyword count (one pass over the subject); the `strpos`
loop and `str_replace` grow with it, and the pure-PHP library keeps a ~17M constant.

### Replace, instructions per call (16 KB subject)

| approach | 50 kw | 500 kw | 5000 kw |
|---|---:|---:|---:|
| `str_replace` (cascading) | 2,360,878 | 14,883,635 | 115,582,524 |
| `strtr` | 8,846,410 | 10,943,947 | 11,007,109 |
| `preg_replace_callback` | 4,676,809 | 50,668,961 | does not compile |
| pure-PHP Aho-Corasick replacer | 17,269,696 | 17,651,305 | 18,416,269 |
| `Str\Replacer::replace` | 437,906 | 438,077 | 437,787 |

### Build, instructions per build

| approach | 50 kw | 500 kw | 5000 kw |
|---|---:|---:|---:|
| pure-PHP Aho-Corasick | 1,663,885 | 39,020,703 | 2,359,426,486 |
| `Str\Matcher` | 259,192 | 2,308,870 | 21,035,003 |
| `Str\Replacer` | 250,548 | 2,228,885 | 20,235,028 |

### Wall-clock (master build, official-image flags, GCC 15.2, AMD Ryzen 9 5950X)

Reported as a paired ratio (both timed back to back in one process), because absolute
ns drifts with CPU frequency between processes.

| comparison | 500 kw / 16 KB | 5000 kw / 64 KB |
|---|---:|---:|
| `Str\Matcher::matchAll` vs `strpos` loop | 18x faster | 126x faster |
| `Str\Replacer::replace` vs `strtr` | 12.7x faster | 5.7x faster |

### Memory (resident, prototype)

| keywords | alphabet-reduced table | dense 256-entry table |
|---:|---:|---:|
| 50 | 0.28 MB | 0.6 MB |
| 500 | 0.73 MB | 3.6 MB |
| 5000 | 4.3 MB | 30 MB |

Alphabet reduction costs about 10% more instructions per byte scanned and shrinks with
a wide (CJK, emoji) alphabet; a double-array trie is the production target.

## Why it is faster

Aho-Corasick scans the subject once, following one transition per byte, and reports
every keyword that ends at each position. Cost is O(subject + matches), independent of
the keyword count, versus O(needles × subject) for the `strpos` loop. The structure is
built once and reused across many subjects, so in a long-lived worker (FrankenPHP,
Swoole, RoadRunner) the build cost is paid once. The split query API (`matches` /
`countMatches` / `getMatchedKeywords` / `matchAll`) means a caller pays only for the
result shape it needs; building result objects is the one cost that grows with the
match count.

## Where it does not win: a specialized decoder

A general prepared automaton does not beat a specialized native function. Decoding the
1511 HTML5 named entities (map from `get_html_translation_table`), 16 KB subject,
instructions per call:

| entity density | `html_entity_decode` | `strtr` | `Str\Replacer` |
|---:|---:|---:|---:|
| 10% | 68,127 | 855,277 | 439,835 |
| 25% | 147,859 | 1,639,892 | 451,575 |
| 50% | 276,152 | 2,968,803 | 466,020 |

`Str\Replacer` beats the general `strtr` by about 1.5x in wall-clock, but
`html_entity_decode` is about 8x faster than `Str\Replacer` and has no build. It wins at
any number of calls, because its per-call cost is lower (it skips non-`&` bytes with a
memchr scan, while the automaton takes one transition per byte) and it carries a
compile-time table rather than building at runtime.

The rule: compare the per-call cost. Reuse only amortizes the build. If an alternative
has a lower per-call cost and no build, a prepared automaton never catches it, however
many times it runs. The reuse break-even against `strtr` (which has no build but a high
per-call) is where the automaton pays off: for this entity map, from the 3rd call on a
64 KB subject, the 9th on 16 KB, and about the 146th on 128 bytes. `Str\Matcher` /
`Str\Replacer` is for arbitrary user dictionaries where no specialized function exists —
there the alternatives are the `strpos` loop and `strtr`, and it wins once reused.

## Trade-offs

- Memory, as above; the dense table is the prototype's weak point.
- Single-use replace at a large dictionary loses to `strtr` until the second call.
- `matchAll` on an adversarial dictionary enumerates a quadratic number of matches.
- A specialized native function (e.g. `html_entity_decode`) stays faster at any reuse.
- `str_replace` and `preg` are shown for completeness; `str_replace` has cascading
  semantics and `preg` is correct only when sorted and only below the compile limit.

## Machine and method

- Instruction tables: Intel i7-13700H, core 2 (P-core), `perf stat -e
  cpu_core/instructions/u`, PHP 8.5.11 built with the official-image flags, prototype
  0.7. Per call = (instructions at K ops − at 0 ops, i.e. build only) / K; the subject
  and structure are built once before the loop. instructions:u is reproducible, so one
  pass is used; the spread between passes is under 0.1%.
- Wall-clock and memory: fresh master `758c9ac5492` built with the official-image
  flags (`-O2`, stack-protector, PIE), GCC 15.2, AMD Ryzen 9 5950X, core 15 (second
  CCD), no other load. Wall-clock is a paired ratio over 15 reps; memory is resident
  size of a fresh process before and after building the matcher.
- No JIT, opcache off for the CLI bench; GC is not disabled, so `matchAll` (which
  builds objects) carries some collector cost that the string-returning paths do not.
- Inputs are random lowercase words, length 4–12, about 8% of the subject made of
  dictionary words. Binary bytes, full UTF-8 and adversarial dictionaries are covered
  by the correctness tests but not by these timing tables.

## Output verification

- `compare.php check`: search presence of `preg`, pure-PHP AC and `Str\Matcher` against
  the `strpos` oracle; replace output of `Str\Replacer`, the pure-PHP replacer,
  `preg_replace` and `str_replace` against `strtr`.
- `verify.php`: `getMatchedKeywords`/`matches`/`countMatches`/`matchAll` against the
  `strpos` oracle and an independent occurrence count, N=50..5000, 4..64 KB.
- `verify_replace.php`: `Str\Replacer::replace` byte-for-byte against `strtr`, including
  overlaps, shared prefixes, empty replacement, no-rescan, adjacent keys.
- `verify_mb.php`: English, Spanish, Russian, Chinese, Japanese, Korean, emoji, binary
  bytes, embedded NUL, and NFC vs NFD.
- `htmlbench.php`: the HTML named-entity decode comparison above; named-only text so
  `html_entity_decode`, `strtr` and `Str\Replacer` agree byte-for-byte.
- The extension builds and runs clean under AddressSanitizer and UndefinedBehavior-
  Sanitizer, including the reconstruct, clone-denied and adversarial-dictionary paths,
  and ships 14 `.phpt` tests.

## Not tested

- Wall-clock and memory on a wide (CJK/emoji) alphabet.
- Subjects above 256 KB, and the streaming behaviour of `replace` on very large input.
- Multibyte case folding and Unicode normalization (out of scope; the caller folds or
  normalizes both sides first, as with `strtr`).
- The double-array trie representation (not implemented).

## Reproduce

The scripts in this directory (`compare.php`, `verify.php`, `verify_replace.php`,
`verify_mb.php`, `htmlbench.php`) are the harness. Build the fork branch linked at the
top with `--enable-strmatch`; that links the extension statically, so `php` already has
`Str\Matcher` and no `-d extension=` is needed. `compare.php` and `htmlbench.php` also
use the pure-PHP wikimedia/AhoCorasick as a baseline:

```
git clone https://github.com/wikimedia/AhoCorasick vendor/aho-corasick

# correctness
php compare.php check 500 16384 1
php verify.php 500 16384 1
sapi/cli/php run-tests.php ext/strmatch/tests

# one cell of a table (instructions per call), e.g. Str\Matcher::matchAll, 500 kw, 16 KB
hi=$(perf stat -x, -e instructions:u -- php compare.php ext_matchall 500 16384 200 1)
lo=$(perf stat -x, -e instructions:u -- php compare.php ext_matchall 500 16384 0   1)
# per call = (hi - lo) / 200
```

`compare.php` modes: search `strpos|preg|phpac|ext_matches|ext_count|ext_getkw|ext_matchall`,
replace `str_replace|strtr|preg_replace|phpac_replace|ext_replace`, build `build_*`, and
`check`. On a hybrid Intel CPU use `cpu_core/instructions/u` and pin with `taskset` to a
P-core.
