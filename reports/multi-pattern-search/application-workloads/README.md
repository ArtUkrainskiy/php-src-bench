# Matcher and Replacer: results on open-data texts

Standard PHP functions, PCRE and Matcher/Replacer compared on comments, complete documents and email templates. Measured on 9 November 2026: Intel Core i7-13700H, Linux x86-64, GCC 14.2. These samples are separate from the AMD study.

[All comparisons](TIMINGS.md) · [Every recipe](RECIPES.md) · [Hardware counters](COUNTERS.md) · [Memory](MEMORY.md) · [Quality](QUALITY.md) · [Source identity and licenses](SOURCE.md) · [Reproduce](REPRODUCE.md)

## Tasks and inputs

| Task | Saved inputs | Dictionary and policy |
|---|---|---|
| Comment checks: presence and unique keys | 16 individual comments; batches use 64 distinct comments from Civil Comments | All 403 English LDNOOBW entries, 2–27 bytes; ASCII-insensitive literal substrings |
| Document searches: unique keys, count and all occurrences | 16 complete CPython documentation source files | 48 names, 3–18 bytes, from the existing lib2to3 mapping; case-sensitive literals |
| Literal document rewriting | The same 16 complete files | The same old-name/new-name mapping; leftmost-longest replacement |
| Email substitution | 12 Groundmail template families, HTML and text: 24 inputs | Existing placeholders and deterministic example values; 2–10 keys |

120 single-document tasks and 20 batch tasks produce 236 comparisons: 96 single-document tasks have two object lifetimes; 24 email tasks have one. Inputs, dictionary order and batch membership were fixed before timing. Texts are unchanged; no matches were inserted. [Corpus and selection](DESIGN.md).

## Findings: when preparation pays

**Creating a Matcher for each of these short messages is slower.** With the 403-key dictionary, creating and destroying the object costs more than the search saves. On the 985-byte negative input, PCRE takes about 14 µs and a new Matcher about 298 µs. The prepared Matcher takes about 2 µs, but that alone does not pay for creating it.

**Reuse can make short-message searches worthwhile, depending on the result needed.** Getting unique matched keys from 16 different comments with one Matcher is 48% faster than the best measured alternative, including construction and destruction. A presence check with `matches()` still shows no advantage at 64 comments. The tests establish these batch results, not an exact break-even count.

**Matcher can pay for itself on a single document.** On the 40.48 KiB text with 48 keys and 10 occurrences, unique-key reporting, counting and listing occurrences are each faster even with construction and destruction included. On the 2.14 KiB text, one-shot unique-key reporting is slower. Long-running workers are therefore one useful setting, not a requirement for a benefit.

**Replacer also has useful one-shot cases.** Replacing 10 occurrences in the 40.48 KiB text with 48 rules is 39% faster than the best measured alternative, including object creation. On the 2.14 KiB text with the same rules, one-shot Replacer is 2.9 times slower. These are different texts; they do not establish a size threshold.

**For these small email dictionaries, use existing functions.** Every email comparison that passed quality checks favors a standard function or PCRE. In the displayed HTML template with 10 keys and 15 replacements, one-shot Replacer is 13.2 times slower. Replacement values vary between messages, so one unchanged Replacer cannot be reused for this task.

## Selected results

The rows show the smallest and largest single texts, one positive comment, and HTML/text versions of one template. Selection uses input properties, not timings. [More selected inputs](SUMMARY-TABLE.md) include the text with 198 occurrences. Each row links to the exact text, dictionary and expected result.

**Prepared** excludes object construction. **One-shot** includes construction and destruction. Both include required preprocessing and result creation, consumption and release. For ASCII-insensitive checks, Matcher pays for `strtolower()` inside the timer; alternatives can use `stripos()` or PCRE `/i`. Replacer is called without the optional count argument.

Existing functions use prebuilt arguments and warm PCRE caches. Both object columns use the one displayed reference time, selected from the one-shot series. Percentages are ratios of medians; negative means faster. Changes below 2% are treated as close. † marks a quality issue with the object or reference; the observed time and relative change are always shown. [Measured variability](QUALITY.md) and [sampling](SOURCE.md).

212 of 236 timing comparisons passed quality checks; 24 remain flagged. Hardware counters have separate checks: 855 of 1096 method results passed. [Affected results](QUALITY.md).

### Matcher: short texts and 403 keys

| Input | Best existing method, µs | Prepared, µs | One-shot, µs |
|---|---|---:|---:|
| [Matcher::matches() · text (EN); 72 B; 403 keys; no matches](inputs/cases/comment.69493.any.json) | `preg_match() [prefix]` 1.475 | 0.310 (-79.00%) | 294.861 (199.9 times slower) |
| [Matcher::matches() · text (EN); 985 B; 403 keys; no matches](inputs/cases/comment.55617.any.json) | `preg_match() [prefix]` 13.741 | 1.798 (-86.91%) | 297.608 (21.7 times slower) |
| [Matcher::matches() · text (EN); 577 B; 403 keys; first match at byte 296; matching key is #11 in dictionary order](inputs/cases/comment.69522.any.json) | `strtolower() + strpos() loop` 2.118 | 0.806 (-61.94%) | 298.750 (141.0 times slower) |


### Matcher and Replacer: complete texts and 48 keys

| Input | Best existing method, µs | Prepared, µs | One-shot, µs |
|---|---|---:|---:|
| [Matcher::getMatchedKeywords() · text (EN); 2.14 KiB; 48 keys; occurrences: 6; unique matched keys: 1](inputs/cases/document.robotparser.unique.json) | `strpos() loop` 21.801 | 3.387 (-84.46%) | 33.159 (+52.10%) |
| [Matcher::getMatchedKeywords() · text (EN); 40.48 KiB; 48 keys; occurrences: 10; unique matched keys: 2](inputs/cases/document.collections.unique.json) | `strpos() loop` 438.256 | 121.421 (-72.29%) | 159.740 (-63.55%) |
| [Matcher::countMatches() · text (EN); 40.48 KiB; 48 keys; occurrences: 10; unique matched keys: 2](inputs/cases/document.collections.count.json) | `strpos() loop` 466.372 | 110.862 (-76.23%) | 152.189 (-67.37%) |
| [Matcher::matchAll() · text (EN); 40.48 KiB; 48 keys; occurrences: 10; unique matched keys: 2](inputs/cases/document.collections.all.json) | `strpos() loop` 468.094 | 125.967 (-73.09%) | 158.273 (-66.19%) |
| [Replacer::replace() · text (EN); 2.14 KiB; 48 keys; 6 replacements; output 2.18 KiB](inputs/cases/document.robotparser.replace.json) | `preg_replace_callback() [prefix]` 7.271 | 3.136 (-56.87%) | 21.166 (2.9 times slower) |
| [Replacer::replace() · text (EN); 40.48 KiB; 48 keys; 10 replacements; output 40.5 KiB](inputs/cases/document.collections.replace.json) | `preg_replace_callback() [prefix]` 225.173 | 118.071 (-47.56%) | 136.365 (-39.44%) |


### Replacer: email templates and 10 keys

| Input | Best existing method, µs | Prepared, µs | One-shot, µs |
|---|---|---:|---:|
| [Replacer::replace() · HTML template; 28.31 KiB; 10 keys; 15 replacements; output 28.36 KiB](inputs/cases/email.receipt.html.json) | `preg_replace_callback() [prefix]` 3.046 | — | 40.266 (13.2 times slower) |
| [Replacer::replace() · plain-text template; 498 B; 10 keys; 11 replacements; output 542 B](inputs/cases/email.receipt.txt.json) | `strtr()` 0.812 | — | 3.937 (4.8 times slower) |


## Reuse: one object, different texts

Each row includes construction, processing of every listed document, release of each result and destruction. Times are batch totals. Larger batches extend the same saved document order; every member is listed in the linked input.

| Exact batch | Best existing: total µs | Object: total µs |
|---|---|---:|
| [Matcher::matches() · 1 document; 456 B total; 403 keys](inputs/cases/batch.validation.any.b1.json) | `preg_match() [prefix]` 6.610 | 295.954 (44.8 times slower) |
| [Matcher::matches() · 16 different documents; 5.23 KiB total; 403 keys](inputs/cases/batch.validation.any.b16.json) | `preg_match() [prefix]` 72.476 | 307.352 (4.2 times slower) |
| [Matcher::matches() · 64 different documents; 21.09 KiB total; 403 keys](inputs/cases/batch.validation.any.b64.json) | `preg_match() [prefix]` 328.861 | 340.234 (+3.46%) |
| [Matcher::getMatchedKeywords() · 1 document; 456 B total; 403 keys](inputs/cases/batch.validation.unique.b1.json) | `preg_match_all() [prefix]` 31.455 | 298.619 (9.5 times slower) |
| [Matcher::getMatchedKeywords() · 4 different documents; 2.11 KiB total; 403 keys](inputs/cases/batch.validation.unique.b4.json) | `strtolower() + strpos() loop` 203.957 | 304.377 (+49.24%)† |
| [Matcher::getMatchedKeywords() · 16 different documents; 5.23 KiB total; 403 keys](inputs/cases/batch.validation.unique.b16.json) | `strtolower() + strpos() loop` 601.791 | 312.351 (-48.10%) |
| [Matcher::getMatchedKeywords() · 64 different documents; 21.09 KiB total; 403 keys](inputs/cases/batch.validation.unique.b64.json) | `strtolower() + strpos() loop` 2461.223 | 357.304 (-85.48%) |
| [Replacer::replace() · 1 document; 36.39 KiB total; 48 keys; replacements: 44 total](inputs/cases/batch.rewrite.replace.b1.json) | `preg_replace_callback() [prefix]` 233.945 | 122.920 (-47.46%) |
| [Replacer::replace() · 4 different documents; 100.15 KiB total; 48 keys; replacements: 135 total](inputs/cases/batch.rewrite.replace.b4.json) | `preg_replace_callback() [prefix]` 549.788 | 275.989 (-49.80%) |
| [Replacer::replace() · 16 different documents; 274.46 KiB total; 48 keys; replacements: 796 total](inputs/cases/batch.rewrite.replace.b16.json) | `preg_replace_callback() [prefix]` 1770.753 | 866.177 (-51.08%) |


## Object and result memory

Fresh-process Zend allocator measurements, excluding loaded inputs. Constructor peak includes the retained object; method peak is additional to that object and includes preprocessing and results. The peaks occur separately and must not be added. These are not RSS measurements; existing-method memory was not measured.

| Exact input | Object retained, B | Constructor peak above inputs, B | Method peak above object, B |
|---|---:|---:|---:|
| [Matcher::matches() · text (EN); 90 B; 403 keys; no matches](inputs/cases/comment.13.any.json) | 136960 | 210688 | 128 |
| [Matcher::matchAll() · text (EN); 27.22 KiB; 48 keys; occurrences: 198; unique matched keys: 3](inputs/cases/document.cookielib.all.json) | 33976 | 47544 | 35448 |
| [Replacer::replace() · text (EN); 40.48 KiB; 48 keys; 10 replacements; output 40.5 KiB](inputs/cases/document.collections.replace.json) | 22400 | 34176 | 45312 |
| [Replacer::replace() · HTML template; 28.31 KiB; 10 keys; 15 replacements; output 28.36 KiB](inputs/cases/email.receipt.html.json) | 3568 | 7792 | 33024 |

`matchAll()` creates one `MatchResult` per occurrence. The largest single-document output has 198 occurrences; thousands or millions of results in one call were not tested. [All memory measurements](MEMORY.md).

## Correctness and limits

An independent Python oracle computes expected occurrences, their order and leftmost-longest replacements. Every included implementation must produce the same content. `matchAll()` object-to-array conversion is used only for checking, outside timing. `str_replace()` is included only where its sequential behavior gives the expected result.

Correctness checks passed on four release builds: 1,096 comparisons per compiler, 4,384 total. A deliberately wrong expected output was rejected on each. Performance was measured only with GCC 14; other compilers and the initial pilot do not contribute samples.

Measurements repeat a fixed text or fixed batch with warm caches. They cover a small set of English-focused sources, not production traffic. They do not measure complete HTTP requests or establish universal text-size or dictionary-size thresholds.

Banword checks are literal substring searches, not word-boundary matching or toxicity classification. Document rewriting can alter substrings inside prose and identifiers; it is not semantic code migration. Email values are deterministic fixtures supplied ready for substitution; escaping and delivery are excluded. Exact source identities and runtime settings, including PCRE JIT limitations, are in [SOURCE](SOURCE.md).
