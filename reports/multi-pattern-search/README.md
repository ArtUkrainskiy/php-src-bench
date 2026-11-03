# Prepared substring search and replacement

**RFC prototype:** `Str\Matcher` / `Str\Replacer` 0.9-dev. [Source](https://github.com/ArtUkrainskiy/php-src/tree/str-matcher-prototype) · [PR #25122](https://github.com/php/php-src/pull/25122).

Create an object from a fixed dictionary and reuse it within a request or worker. Objects do not automatically survive FPM requests; compiled PCRE patterns can remain cached in that worker.

**Choose by workload and reuse:**

- **One new object per call:** on the tested 4 KiB texts, no-match `matches()` and term `replace()` win at 16, 32, 64, 128, 256 and 512 keys on both compilers. This is not a universal threshold.
- **Repeated short strings:** a 128-key Matcher for 128 B no-match messages needs **~19 strings per object against the PHP loop, ~14 against PCRE** (estimates).
- **Matching can favor alternatives:** at eight keys, a ready Matcher wins on these no-match texts, but a new one loses to PHP; PCRE replacement beats even a ready Replacer. With 128 keys, early PCRE matches and middle/end PHP matches can beat a new Matcher.
- **Everyday counterexamples:** `strtr()` wins one order email including Replacer construction/destruction; `preg_replace()` wins one complete incident log even against a ready Replacer.

**Ryzen 9 5950X, GCC 15.2 and Clang 21.1; controlled authored texts.** Listed wins require a 2% margin, a noise filter rather than statistical confidence. These results are not application/FPM throughput. [Object memory](#construction-and-memory) is additional to the input dictionary; totals and peaks already include their components and should not be summed.

## Operations and comparators

Matching uses case-sensitive literal substrings, without word-boundary rules.

| Method | Result | PHP built-ins | PCRE |
|---|---|---|---|
| `Matcher::matches()` | Whether any key occurs | `str_contains()` loop, stop at first matching key | `preg_match()`, one pattern containing all keys |
| `Matcher::getMatchedKeywords()` | Each matching key once, ordered by first occurrence | `strpos()` per key | `preg_match()` per key |
| `Replacer::replace()` | Replaced string; longest key at the earliest position | `strtr()` with a replacement map | `preg_replace_callback()`, longest-first literal alternatives |

Keyword listing includes keys contained in longer matching keys: both `invoice` and `invoice number` can be returned. Replacement text is not searched again.

## Time per string

**128 keys; GCC 15.2; µs, lower is better.** Each call processes **one string against the entire dictionary**. Four different saved strings of each exact length cycle equally. Times are medians of fifteen samples of repeated calls.

**Prepared:** a call on an existing object. **One-shot:** **construction + one call + destruction**, measured together. Dictionaries, maps, regex strings/callbacks and compiled PCRE patterns already exist; input loading, regex construction and first compilation are excluded. These columns are separate measurements; do not add them.

<!-- LENGTH-TABLE -->
| Method | Input | PHP built-ins µs | PCRE µs | Prepared µs | One-shot µs |
|---|---:|---:|---:|---:|---:|
| `Matcher::matches()` (no match) | 128 B | 3.351 | 4.693 | 0.316 | 58.275 |
| `Matcher::matches()` (no match) | 4 KiB | 121.892 | 142.626 | 6.978 | 65.950 |
| `Matcher::matches()` (no match) | 16 KiB | 497.911 | 571.130 | 27.241 | 86.576 |
| `Matcher::getMatchedKeywords()` | 512 B | 17.842 | 20.329 | 1.707 | 47.486 |
| `Matcher::getMatchedKeywords()` | 4 KiB | 105.104 | 64.442 | 12.469 | 60.862 |
| `Matcher::getMatchedKeywords()` | 16 KiB | 207.546 | 103.328 | 40.338 | 91.136 |
| `Replacer::replace()` | 512 B | 38.278 | 12.880 | 1.566 | 46.389 |
| `Replacer::replace()` | 4 KiB | 359.125 | 98.547 | 12.016 | 59.369 |
| `Replacer::replace()` | 16 KiB | 1438.517 | 401.335 | 46.766 | 94.740 |
<!-- /LENGTH-TABLE -->

The `matches()` rows have no matches. Listing and replacement rows contain support terms. [Exact inputs](../../corpus/multi-pattern-length/README.md); [all lengths, Clang and counters](LENGTH.md).

### How many strings make reuse worthwhile?

Counts mean **strings per object needed to beat the comparator, including construction and destruction**. `~N` is an estimate, not an exact minimum. For the 4/16 KiB cases above, a one-string win was directly measured on both compilers.

<!-- REUSE-TABLE -->
| Method | Input | Strings/object to beat PHP | Strings/object to beat PCRE |
|---|---:|---:|---:|
| `Matcher::matches()` (no match) | 128 B | ~19 | ~14 |
| `Matcher::getMatchedKeywords()` | 512 B | ~3 | ~3 |
| `Replacer::replace()` | 512 B | ~2 | ~4 |
<!-- /REUSE-TABLE -->

For the 128 B no-match case, creation and destruction cost 57.041 µs once. Each prepared call saves `3.351 − 0.316 = 3.035 µs` against the PHP loop: `57.041 / 3.035 ≈ 18.79`, or **~19 strings per object**; against `preg_match()`, **~14**. [Direct batch checks and estimates](LENGTH-PAYBACK.md).

## Construction and memory

**`new`:** construction from the loaded dictionary, excluding search/destruction. **Added:** extra PHP-tracked memory of the ready object above that dictionary. Process RSS, construction peaks and PCRE memory are outside this table.

<!-- BUILD-MEMORY-TABLE -->
| Dictionary | Keys | Matcher new, µs | Matcher added, KiB | Replacer new, µs | Replacer added, KiB |
|---|---:|---:|---:|---:|---:|
| Moderation phrases | 128 | 56.871 | 58.0 | n/a | n/a |
| Support glossary/catalog | 8 | 2.133 | 3.5 | 2.341 | 3.5 |
| Support glossary/catalog | 32 | 7.994 | 10.6 | 9.401 | 13.6 |
| Support glossary/catalog | 128 | 44.716 | 46.1 | 43.353 | 43.2 |
| Support glossary/catalog | 512 | 351.759 | 187.8 | 288.682 | 140.8 |
| Support glossary/catalog | 10000 | 10264.009 | 2272.8 | 6931.491 | 1324.8 |
<!-- /BUILD-MEMORY-TABLE -->

`n/a`: not measured. [Memory totals and peaks](MEMORY.md) already include the input and object: **do not add those columns**. Dictionary structure matters beyond key count. [All sizes/compilers](BUILD-MEMORY.md).

## First-match position

`Matcher::matches()`, **128 keys, 4 KiB/string, GCC 15.2; µs per string**. Each of four positive texts matches one key, respectively at dictionary ranks **1, 37, 91 and 128**. These assignments stay fixed across match positions.

<!-- POSITION-TABLE -->
| First match: Matcher::matches() | PHP µs | PCRE µs | Prepared µs | One-shot µs |
|---|---:|---:|---:|---:|
| No match | 122.299 | 143.059 | 6.987 | 65.786 |
| Near start (byte 18) | 58.812 | 0.910 | 0.142 | 58.600 |
| Middle (about 2 KiB) | 61.071 | 72.355 | 3.577 | 62.233 |
| Near end (last 9 bytes) | 59.414 | 142.695 | 6.999 | 65.477 |
<!-- /POSITION-TABLE -->

The new object loses to PCRE at the start and to PHP at the end; the middle case is also slightly slower than PHP. Prepared Matcher remains faster here. **Input length alone does not decide.**

## Dictionary size on the same 4 KiB texts

**8, 16, 32, 64, 128, 256 and 512 keys**, with identical input strings across sizes. Moderation has no matches; replacement has matching terms. More keys also mean more replacements and output.

<!-- DICTIONARY-4K-SUMMARY -->
**On both compilers**, one-shot `Matcher::matches()` (no match) and `Replacer::replace()` beat both comparators at **16, 32, 64, 128, 256, 512 keys** on these inputs.

**Eight-key replacement favors PCRE:** with GCC, `preg_replace_callback()` takes **4.958 µs**, against **10.319 µs** for a prepared Replacer and **12.807 µs** including construction and destruction.
<!-- /DICTIONARY-4K-SUMMARY -->

A listed win requires a 2% saving: a noise filter, not statistical confidence. Untested sizes do not establish an exact crossover. [Full moderation/replacement tables](FIXED-4K.md): all tested sizes, both compilers and counters.

## Where existing tools win

**Time per whole email or whole log string.** The email substitutes order values into template fields. The log replaces sparse occurrences of registered secrets with one marker, using one call on the whole log. PCRE is compiled/cached.

<!-- EVERYDAY-LOSSES -->
| One operation | Replacer lifetime | Fastest comparator | Comparator µs | Replacer µs |
|---|---|---|---:|---:|
| One order email, 10 placeholders | Create, replace, destroy | `strtr()` | 0.962 | 4.800 |
| One complete log: 384 records, 24 secrets | Prepared Replacer call | `preg_replace()` | 3.946 | 137.312 |
<!-- /EVERYDAY-LOSSES -->

## Full results

[Dictionary sizes on short texts: moderation](MODERATION.md) · [keyword results](SEARCH.md) · [replacement](REPLACEMENT.md) · [EN/RU/ZH and other application cases](PRODUCT-CASES.md).

[Time](FULL-TIME.md) · [cycles](FULL-CYCLES.md) · [instructions](FULL-INSTRUCTIONS.md) · [first PCRE requests](PCRE-FIRST.md) · [method and controls](METHOD.md) · [reproduce](REPRODUCE.md).
