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
core is the build cost: building the automaton in C is about 110x cheaper than the
measured pure-PHP library (below). An optimized userland build would do better than that
library, so this is the gap against the available one, not a claim about every possible
PHP implementation. The rule for when it wins is the
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
  keywords, about 110x less than the measured pure-PHP library's 2.36 billion
  (wikimedia/AhoCorasick; part of that is an O(n) `array_shift` BFS queue, so an
  optimized userland build would be faster — this is the gap against the available one).

Costs to weigh, not hidden at the end:

- **Memory.** The built automaton is about 4.0 MB for 5000 ASCII keywords with the
  alphabet-reduced layout (one column per byte value that occurs; precise Zend-heap
  size, resident RSS ~5–6 MB), roughly 10x less than a dense 256-column table (~30 MB).
  This is the prototype's representation, not the shipped one: the production target is a
  compact automaton (double-array trie), which is the memory figure that should decide
  core inclusion. `replace` also uses a transient scratch array of 4 bytes per subject
  byte.
- **No win over a specialist.** A specialized native function beats the general automaton
  at any reuse: `html_entity_decode` is about 8x faster than `Str\Replacer` on named
  entity decoding and has no build (details below). The tool is for arbitrary user
  dictionaries, where the alternatives are the `strpos` loop and `strtr`.
- **Single use.** With no reuse, the build dominates. Search still wins single-use
  (build + one `matchAll` beats one `strpos` loop at 500 and 5000 keywords). Replace
  wins single-use for small and medium dictionaries, but at 5000 keywords a single
  build + `replace` costs more than one `strtr`; the win starts from the second call.
- **Adversarial input.** `matchAll` is O(subject + matches·log matches) — it sorts the
  collected matches — and `replace` is O(subject + matches). A dictionary like
  `{a, aa, aaa, ...}` over `aaaa...` produces a quadratic number of matches.
  `countMatches` is O(subject) regardless, and `matches` is immune (first hit).

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

The hard-equal contracts are: `strpos` presence against the pure-PHP library and
`Str\Matcher::getMatchedKeywords` (distinct keywords), and `strtr` against
`Str\Replacer`, the pure-PHP replacer and `preg_replace`; all agree at 50 and 500
keywords. Two approaches have a different contract and are not required to match:
`preg_match_all` is non-overlapping, so its presence set can miss a keyword that only
occurs inside another (it coincides with the oracle on these random inputs but need
not in general), and `str_replace` cascades. At 5000 keywords the `preg` pattern does
not compile; the pure-PHP library and the prototype stay correct. Checked by
`compare.php check` (non-zero exit on an unexpected mismatch) plus the differential
tests below.

## Results

The instruction-count and memory tables are from the Intel machine (i7-13700H); the
wall-clock table is from the AMD machine (Ryzen 9 5950X). Both are named in each heading
and in Machine and method; instruction counts and ns are not from the same box (the
memory figure is deterministic, so the machine does not matter for it).

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

These are not all the same operation, so compare like with like. The matched-contract
pair is `getMatchedKeywords` (distinct matched keywords) versus the `strpos` loop
(presence): about 23x fewer instructions at 500 keywords, 263x at 5000. `matchAll` does
strictly more — it returns every occurrence with offsets — and is still far below the
loop. `matches` (any match) is an early exit and is cheapest; the `strpos` loop here
scans every keyword rather than stopping at the first, so it is not a fair "any match"
baseline for `matches` (see Machine and method). The prototype is flat in the keyword
count; the `strpos` loop and `str_replace` grow with it, the pure-PHP library keeps a
~17M constant.

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

| comparison | 500 kw / 16 KB | 5000 kw / 64 KB | spread of the paired ratio |
|---|---:|---:|---|
| `Str\Matcher::matchAll` vs `strpos` loop | 18x faster | 126x faster | 17.7–18.4x / 124.5–126.4x |
| `Str\Replacer::replace` vs `strtr` | 12.7x faster | 5.7x faster | 12.2–12.8x / 5.6–5.8x |

### Memory (prepared automaton)

Zend-heap allocation of the built automaton (`memory_get_usage` delta, the precise
`emalloc`'d size; resident RSS is higher and page-granular, ~5–6 MB at 5000 keywords):

| keywords | alphabet-reduced (a–z) |
|---:|---:|
| 50 | 0.06 MB |
| 500 | 0.5 MB |
| 5000 | 4.0 MB |

A full 256-column (dense) table is about ten times larger — roughly 30 MB at 5000
keywords, measured on the pre-reduction prototype. Alphabet reduction costs about 10%
more instructions per byte scanned and its win shrinks on a wide (CJK, emoji) alphabet;
a double-array trie is the production target. The per-call scratch is separate and
transient: `replace` holds 4 bytes per subject byte (256 KB for 64 KB), `matchAll` a
growable hit buffer (~140 KB here), both freed on return.

## Why it is faster

Aho-Corasick scans the subject once, following one transition per byte, and reports
every keyword that ends at each position. The scan is O(subject + matches), independent
of the keyword count, versus O(needles × subject) for the `strpos` loop; `matchAll` then
sorts its matches, so it is O(subject + matches·log matches). The structure is
built once and reused across many subjects, so in a long-lived worker (FrankenPHP,
Swoole, RoadRunner) the build cost is paid once. The split query API lets a caller pay
only for the work it needs: `matches` and `countMatches` never enumerate the individual
matches (first-hit and a summed per-state count), while `getMatchedKeywords`, `matchAll`
and `replace` do walk every occurrence, so their cost grows with the match count even
when the returned result is small.

## Where it does not win: a specialized decoder

A general prepared automaton does not beat a specialized native function. Decoding the
1511 named entities from `get_html_translation_table(HTML_ENTITIES, ENT_QUOTES |
ENT_HTML5)` — the canonical set, not every HTML5 alias — 16 KB subject, instructions
per call. The "entity rate" is the probability that a generated token is an entity (the
`DENS` parameter); the resulting entity share of the bytes is higher, as the last
column shows:

| entity rate | `html_entity_decode` | `strtr` | `Str\Replacer` | entity bytes |
|---:|---:|---:|---:|---:|
| 10% | 68,127 | 855,277 | 439,835 | 13% |
| 25% | 147,859 | 1,639,892 | 451,575 | 31% |
| 50% | 276,152 | 2,968,803 | 466,020 | 59% |

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

- Prototype commit: the numbers are from the extension at version 0.7, branch commit
  `33bc4bb8738`. The search and replace hot paths are unchanged through the current head
  `687870a8abe` (0.8, which only added strtr-compatible key/reference handling), so the
  counts hold for the branch as it stands.
- Instruction tables: Intel i7-13700H, core 2 (P-core), `perf stat -e
  cpu_core/instructions/u`, PHP 8.5.11 built with the official-image flags. Per call =
  (instructions at K ops − at 0 ops, i.e. build only) / K; the subject and structure are
  built once before the loop. instructions:u is reproducible, so one pass is used; the
  spread between passes is under 0.1%.
- Wall-clock: fresh master `758c9ac5492` built with the official-image flags (`-O2`,
  stack-protector, PIE), GCC 15.2, AMD Ryzen 9 5950X, core 15 (second CCD), no other
  load. Paired ratio (both timed back to back, order alternated), 15 reps for the
  500-keyword rows and 9–11 for the heavier 5000-keyword rows; the spread is in the table.
- Memory: the Zend-heap delta across building the matcher in a fresh process
  (`memtest.php`), measured on the Intel/8.5.11 build. It is the `emalloc`'d size of the
  automaton, which is fixed by the data structure, so the figure is deterministic and
  does not depend on the machine or compiler (only Zend MM's bin rounding does, slightly).
- CLI with `opcache.enable_cli=0` and `opcache.jit=0` (no PHP JIT); `pcre.jit` is left
  at its default on, so the `preg` numbers include PCRE's JIT. GC is not disabled, so
  `matchAll` (which builds objects) carries some collector cost the string-returning
  paths do not.
- Inputs are random lowercase words, length 4–12; about 8% of the generated tokens (not
  of the bytes) are dictionary words. `matches()` therefore meets a match early and its
  number is an early-exit cost; a no-match subject is a full scan (~246K at 16 KB). The
  `strpos` presence loop always scans every keyword; for a pure "any match" question it
  would also stop at the first hit. Binary bytes, full UTF-8 and adversarial
  dictionaries are in the correctness tests, not these timing tables.
- The `preg` pattern stops compiling at 44,755 bytes in this PHP/PCRE2 build; that
  threshold depends on the pattern and the PCRE2 version, it is not a fixed 44 KB limit.
  `build_preg` measures building the pattern string, not PCRE compilation.

## Output verification

- `compare.php check`: search presence of `preg`, pure-PHP AC and `Str\Matcher` against
  the `strpos` oracle; replace output of `Str\Replacer`, the pure-PHP replacer,
  `preg_replace` and `str_replace` against `strtr`. Exits non-zero on any unexpected
  mismatch; a `preg` that does not compile is reported UNSUPPORTED, not failed.
- `verify.php`: `getMatchedKeywords`/`matches`/`countMatches`/`matchAll` against the
  `strpos` oracle, an independent occurrence count, a full (offset, length, keyword)
  oracle for `matchAll`, the first-start-offset order of `getMatchedKeywords`, and a
  no-match case for `matches`. N=50..5000, 4..64 KB.
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

The scripts in this directory are the harness: `compare.php` (all approaches, every
operation, plus a `check` mode), `verify.php` / `verify_replace.php` / `verify_mb.php`
(correctness), `htmlbench.php` (the HTML section, with a `check` mode), `nsratio.php`
(paired wall-clock), `memtest.php` (automaton memory), `worstbench.php` (adversarial
dictionary). Build the fork branch linked at the top with `--enable-strmatch`; that
links the extension statically, so `php` already has `Str\Matcher` and no `-d extension=`
is needed. `compare.php` and `htmlbench.php` also use the pure-PHP wikimedia/AhoCorasick
as a baseline.

```
git clone https://github.com/wikimedia/AhoCorasick vendor/aho-corasick

# correctness (compare.php check and htmlbench.php check exit non-zero on a mismatch)
php compare.php check 500 16384 1
php htmlbench.php check 16384 25 5
php verify.php 500 16384 1
sapi/cli/php run-tests.php ext/strmatch/tests

# one instruction-table cell, e.g. Str\Matcher::matchAll, 500 kw, 16 KB.
# perf writes to stderr, so capture stderr and parse the counter, not the script's stdout:
getins() { perf stat -x, -e instructions:u -- php "$@" 2>&1 >/dev/null | awk -F, '/instructions/{print $1}'; }
hi=$(getins compare.php ext_matchall 500 16384 200 1)
lo=$(getins compare.php ext_matchall 500 16384 0   1)
# per call = (hi - lo) / 200   (on a hybrid Intel CPU use cpu_core/instructions/u and taskset to a P-core)

# wall-clock: paired ratio in one process (prints "A ns, B ns, B/A ratio median ...")
php nsratio.php replace-vs-strtr 500 16384 500 15 1
php nsratio.php matchall-vs-strpos 5000 65536 25 9 7

# resident memory of the built automaton (one N per process)
php memtest.php 5000 65536 7
```

These are the exact harness and parameters behind the tables; the numbers were taken
with the builds named in Machine and method.

`compare.php` modes: search `strpos|preg|phpac|ext_matches|ext_count|ext_getkw|ext_matchall`,
replace `str_replace|strtr|preg_replace|phpac_replace|ext_replace`, build `build_*`, and
`check`. On a hybrid Intel CPU use `cpu_core/instructions/u` and pin with `taskset` to a
P-core.
