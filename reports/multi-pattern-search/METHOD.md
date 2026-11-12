# Method

How every number in the report was measured, and what keeps the comparison fair to both sides.

## What is compared

`Str\Matcher` and `Str\Replacer` from [PR #25122](https://github.com/php/php-src/pull/25122) at commit [bb508627af](https://github.com/php/php-src/pull/25122/commits/bb508627af16e029c3c760109461c7596259484c), built into `ext/standard`.
They are compared with the existing ways to do the same job in PHP:

| Task | Existing methods |
|---|---|
| Does any key occur? | `str_contains()` loop; `stripos()` loop or `strtolower()` + `str_contains()` loop when case is ignored; `preg_match()` |
| Which keys occur? | the same loops; `preg_match_all()` |
| How many occurrences? | `strpos()` or `stripos()` loop, `substr_count()` loop, `preg_match_all()` |
| Every occurrence with its offset | `strpos()` or `stripos()` loop, `preg_match_all()` with offsets |
| Replace keys | `strtr()`; `preg_replace_callback()`, or `preg_replace()` when every key gets the same replacement |

With a single key, a single `str_contains()` call competes too.
Each PCRE method comes as a plain alternation and as an alternation that shares key prefixes, whose greedy optional groups pick the longest key at a position.
For "which keys", "how many" and "every occurrence" the pattern is a lookahead, `(?=(…))`, so that overlapping and nested keys are found as the native call finds them.
For search, large dictionaries also get the same patterns in chunks of 512 or 1024 keys.
For replacement the plain alternation puts longer keys first, so that the longest key wins as in `strtr()` and the native call.

For "which keys", "how many" and "every occurrence", a plain alternation that consumes each match would take 2–25% less time than the lookahead in a probe on four inputs with GCC ([data](data/probe/consuming-alternation.json), methods `pcre_consuming_*`; the recipe isn't kept in `tools/`). It finds the right answer only when no two occurrences overlap, so it isn't used.

The **reference** in every table is the fastest existing method for that input and mode, chosen after the run from the timed methods that are right on every text.
That choice favours the existing side a little: an application would have to pick one method in advance. So does one duplicate: for `matches()` without case folding, two timed methods are the same `str_contains()` loop, and the reference is the faster of the two noisy copies.

## Only methods that are right on every text

An existing method competes only if it gives the same answer as the native call on any text, not just on the measured ones.
`str_replace()` is left out because it rescans its own output, and so are, for replacement, PCRE alternations in dictionary order and several replacement patterns applied in turn.
On short texts some of them are faster, and they would give the right answer on many texts, but not on all of them.
As a check, every method also runs on every text of the cell before timing, and a method whose result differs from the native one is dropped. The check rejected `str_replace()`, dictionary-order PCRE and chunked replacement patterns on replacement cells. For search calls no method gave a different result; no deliberately broken method was tried. PCRE alternations too large to compile were dropped too.
The order of found keys and occurrences doesn't matter: the native call pays for sorting its results and the existing methods don't.

## Two modes

- **Prepared**: the object, pattern strings and arrays exist before the timer starts, wherever they were built. The timer covers the call, the result and its release.
- **One-shot**: one build and one call. The timer also covers building the object, or the pattern strings, callbacks and arrays, and destroying them. Compiled PCRE patterns stay in PCRE's per-process cache, as they do between requests of PHP-FPM. Analysis that depends only on the dictionary, such as sorting keys or grouping nested keys, is done before the timer for the existing methods. If an application keeps a ready pattern as a constant in its code, its one-shot cost is the prepared row.

## How a cell is measured

A **cell** is one operation, one dictionary and a pool of texts. Cells at 1.5, 2 and 3 KiB (`cells/crossover`) are timed in one-shot mode only, to find where a single call starts to pay for the build.

- **Different texts every call.** Repeating one text lets the CPU's branch predictor learn it. On a 16 KiB text, a prepared call took 9.4–14.4 µs on one repeated text and 36.7–45.1 µs on 64 different texts ([probe](data/branch-probe.md), with an earlier version of the extension). A pool of windows holds 2 MiB of text (4 MiB for 64 KiB windows) at random positions of a corpus; windows may overlap. Scenario pools are whole documents in a fixed shuffled order: 10,000 comments, 10,000 User-Agent strings, which repeat as in real traffic, and 4,153 manual pages. The page-length cells (`cells/pages`) take only the manual pages of 1–2, 2–4 or 4–16 KiB. Earlier reports on this API repeated one text and are not comparable with this one.
- **Same texts for every method.** In each pass every method makes the same number of calls on the same texts. The number of calls is set so that the slowest timed method takes at most about 100 ms per pass, and the fastest at least 20 ms when that limit allows; the median pass of the fastest method took 18 ms. A process makes at least 64 calls per method on window pools, and covers the whole pool on scenario pools. The two modes make different numbers of calls, so they time different samples of the pool: compare times within one mode.
- **Slow methods are not timed.** Before timing, every method's time per call is estimated. An existing method more than 5 times slower than the fastest existing one can't be the reference, so it isn't timed; its estimate is in the data. The main runs still timed the replacement methods that are not right on every text; they never count as the reference, and the methods they pushed out of timing were at least 1.42 times slower than the reference.
- **Fair order.** Methods run in a rotated order that reverses every other pass. One untimed call precedes every timed block, so pattern compilation and cold caches are never timed. Calls run back to back, so caches stay warm for both sides.
- **Empty-call correction.** Every pass also times an empty call (loop, closure call, result accounting); it is subtracted from every method. Tables show the corrected change; the change without the correction is in the data. It matters most on short texts: for 32 keys or more the prepared range on random keys is −90…−46% corrected and −89…−41% without the correction.
- **A/A control.** Native is timed twice per pass.
- **Repetition.** Each cell runs in 3 fresh processes; reported values are medians over processes. When the processes disagree by more than 2% or the A/A pair by more than 1.5%, both modes of that cell and compiler get 2 more processes.

The noise floor was calibrated before the run: one process is reproducible to about ±2%, the median of three to about ±0.7% ([calibration](data/calibration.md)). The run was noisier: the processes of a value differ by 3.3% or less in 90% of values, and repeats on the other core moved the ratio by up to 5.1%. Differences within about 3% are not told apart.

In the run, 1061 of 2410 records got the extra processes. The decision was made with those extra replacement methods included, so 15 records whose processes disagree by more than 2% kept 3 processes. The per-process ratios differ by 1.0% in the median record and by 3.3% or less in 90% of them. 340 records still have an A/A pair off by more than 1.5%. Tables mark a value with † when the processes differ by more than 5%, the A/A pair by more than 3%, a process was preempted more than 20 times a second, or the core or its SMT sibling was not idle: 141 records. Every record keeps its per-process range, A/A result and flags in [data/results.json](data/results.json). The page-length cells ran later in a separate series on CPU 15 with the same builds and the current `bench.php`; they are in [data/pages.json](data/pages.json) and not in the counts of this paragraph.

## Environment

AMD Ryzen 9 5950X (Zen 3, two 8-core CCDs), Ubuntu 26.04, Linux 7.0, `performance` governor with boost on. Time is wall time from `hrtime()`; each pass pairs both sides, so frequency drift between passes cancels out. GCC 15.2.0 and Clang 21.1.8, release builds of `--disable-all --enable-cli` with the flags of the official PHP Docker image (`-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64`). PHP runs with OPcache enabled and JIT disabled, PCRE JIT enabled, garbage collection disabled. Each cell runs pinned to one core whose SMT sibling is idle (2 records were flagged when it was not); other cores of the same CCD are not checked. CPU 7: PHP-name grid, languages, one-shot cells at 1.5–3 KiB; CPU 15: random-key grid, scenarios, edge cases, one-shot cells at 1.5–3 KiB. The two cores are on different CCDs. The random-key grid and the PHP-name grid with languages ran at the same time; edge cases and scenarios ran later alone, and the 1.5–3 KiB cells later on both cores. Repeated on the other core ([data/corecheck.json](data/corecheck.json)): 4 random-key, 45 PHP-name 1.5–3 KiB inputs; the tables use the core listed above. Between the cores the native/reference ratio moved by 0.9% in the median and 5.1% at most.

## Inputs

| Source | Revision | Licence | Used for |
|---|---|---|---|
| [doc-en](https://github.com/php/doc-en) | `47ea59c86c44` | CC BY 3.0 | corpus/en.txt, dictionaries/words-en.json, corpus/emoji.txt, corpus/manual-pages.json, dictionaries/words-en-frequent.json, dictionaries/php-identifiers.json, dictionaries/php-functions.json |
| [doc-es](https://github.com/php/doc-es) | `a694c0ea4c59` | CC BY 3.0 | corpus/es.txt, dictionaries/words-es.json |
| [doc-ru](https://github.com/php/doc-ru) | `a9b61bdb2312` | CC BY 3.0 | corpus/ru.txt, dictionaries/words-ru.json |
| [doc-zh](https://github.com/php/doc-zh) | `a8a0380f127e` | CC BY 3.0 | corpus/zh.txt, dictionaries/words-zh.json |
| [doc-ja](https://github.com/php/doc-ja) | `09e7e4138918` | CC BY 3.0 | corpus/ja.txt, dictionaries/words-ja.json |
| [mdn-translated-content](https://github.com/mdn/translated-content) | `5f2b88663958` | CC BY-SA 2.5 | corpus/ko.txt, dictionaries/words-ko.json |
| [civil_comments](https://huggingface.co/datasets/google/civil_comments) | `f2970eb3a557` | CC0 1.0 | corpus/comments.json |
| [crawler-user-agents](https://github.com/monperrus/crawler-user-agents) | `db662d2787f9` | MIT | dictionaries/crawler-patterns.json, corpus/user-agents.json |
| [intoli-user-agents](https://github.com/intoli/user-agents) | `ec0b8d7fe68b` | BSD-2-Clause | corpus/user-agents.json |
| [ldnoobw](https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words) | `5faf2ba42d7b` | CC BY 4.0 | dictionaries/ldnoobw-en.json (copy in dictionaries/ldnoobw) |

Texts are windows at random positions of these corpora, or whole documents. English with emoji is the English corpus with an emoji sequence after about every 40 bytes. Word dictionaries are words of the given frequency ranks in each corpus. In the random-key grid, keys are random strings of the letters a–p that never occur in the corpus; occurrences are written into each window. [corpus/ATTRIBUTION.md](corpus/ATTRIBUTION.md) lists authors, licences and changes. [REPRODUCE.md](REPRODUCE.md) rebuilds every cell byte for byte from [corpus](corpus) and [dictionaries](dictionaries).

## Limits

- Results are from one machine. Other CPUs, especially with different branch predictors, can move the boundaries.
- One build per compiler. GCC and Clang differ near the boundaries, and one build can't separate the compiler from code placement.
- PHP's JIT was disabled, and so was garbage collection. Results with the JIT were not measured.
- Calls run back to back with warm caches. A worker that does other work between calls was not modelled.
- Matching is byte-wise and case-sensitive. The moderation scenario lowercases the text with `strtolower()` for the native call, as an application would. With `/i`, PCRE returns the text's spelling of a key, not the key; the existing method doesn't pay to map it back.
- Approaches with different results are not compared: splitting a text into words and looking them up with `isset()` finds whole words only.
- User-Agent strings repeat as in real traffic; an application could cache results per string, which is not modelled.
- Dictionaries with fewer than 8 keys are outside the intended use. [edge-cases.md](edge-cases.md) shows them for completeness.
