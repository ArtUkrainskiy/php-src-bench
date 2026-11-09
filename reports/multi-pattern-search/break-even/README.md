# Matcher and Replacer: measured break-even points

9 November 2026. GCC 14.2, Intel Core i7-13700H. The saved dictionary has 48 case-sensitive literal keys of 3–18 B; smaller dictionaries preserve its order. Controlled derived texts test when one-shot and prepared calls beat existing PHP/PCRE implementations. These are measured configurations, not universal thresholds.

[Prepared grid](prepared-grid/README.md) · [One-shot length study](TIMINGS.md) · [256-byte one-shot checks](short-256/README.md) · [Cycles and instructions](COUNTERS.md) · [Quality](QUALITY.md) · [Method and source inputs](METHOD.md) · [Build identity](data/build.json)

## What these results tell you

For prepared objects, the explicit starting point is 128 B / 8 keys: unique-key reporting, counting, listing occurrences won; presence checking was inconclusive; replacement lost. The grid below shows all tested dictionary sizes at 128 B, 256 B, 1 KiB and 4 KiB.

At 128 B, the smallest confirmed winning dictionaries also won on the second text: 8 keys for unique-key reporting, counting, listing occurrences; 16 keys for presence checking, replacement.

36 of 85 prepared comparisons have quality flags. Their observed times and relative changes remain in every table; sample spread and A/A deviation are reported separately.

No tested 256-byte input produced a confirmed one-shot win. A fast prepared call alone does not pay the cost of creating a new object for each text.

With 48 keys and one occurrence, one-shot unique-key reporting, counting and listing all win at 4 KiB and lose at 2 KiB. The 4 KiB wins also passed on the second text, although the smallest gains are only a few percent.

A one-shot presence check first wins at 32 KiB with no matches. That result does not extend to early matches: on the 64 KiB control with a hit at byte 8, PCRE remains much faster than creating a Matcher.

For one replacement with 48 rules, one-shot Replacer loses at 8 KiB and wins at 16 KiB.

## One-shot: text length with 48 keys

Includes object construction, operation, result release and destruction. Existing arguments and compiled PCRE caches are already prepared. Counterexamples and close results remain in the full tables.

**Reading the one-shot table:** each row compares the nearest smaller confirmed loss with the smallest tested win for the same operation and 48 keys. Values between tested lengths remain unknown. The last column checks the winning configuration on a second text. Percentages use the displayed medians; win/loss decisions use paired samples.

| Operation | Nearest smaller loss, µs | Smallest tested win, µs | Same mode on the second text, µs |
|---|---|---|---|
| `Matcher::matches()`; no matches | [8 KiB](inputs/cases/technical.any.n48.b8192.absent.json)<br>`preg_match() [prefix]` 33.398<br>One-shot: 52.785 (+58.05%) | [32 KiB](inputs/cases/technical.any.n48.b32768.absent.json)<br>`preg_match() [prefix]` 175.445<br>One-shot: 134.120 (-23.55%)<br>Intermediate observations:<br>[16 KiB](inputs/cases/technical.any.n48.b16384.absent.json)<br>`preg_match() [prefix]` 78.717<br>One-shot: 79.824 (+1.41%) | [Input](inputs/cases/comments.any.n48.b32768.absent.json)<br>`preg_match() [prefix]` 210.190<br>One-shot: 123.149 (-41.41%)<br>win |
| `Matcher::getMatchedKeywords()`; one occurrence | [2 KiB](inputs/cases/technical.unique.n48.b2048.single.json)<br>`preg_match_all() [literal]` 21.781<br>One-shot: 33.256 (+52.68%) | [4 KiB](inputs/cases/technical.unique.n48.b4096.single.json)<br>`strpos() loop` 42.178<br>One-shot: 39.316 (-6.79%) | [Input](inputs/cases/comments.unique.n48.b4096.single.json)<br>`strpos() loop` 41.950<br>One-shot: 40.541 (-3.36%)<br>win |
| `Matcher::countMatches()`; one occurrence | [2 KiB](inputs/cases/technical.count.n48.b2048.single.json)<br>`preg_match_all() [literal]` 20.592<br>One-shot: 31.917 (+54.99%) | [4 KiB](inputs/cases/technical.count.n48.b4096.single.json)<br>`strpos() loop` 42.120<br>One-shot: 37.294 (-11.46%) | [Input](inputs/cases/comments.count.n48.b4096.single.json)<br>`strpos() loop` 41.904<br>One-shot: 37.942 (-9.46%)<br>win |
| `Matcher::matchAll()`; one occurrence | [2 KiB](inputs/cases/technical.all.n48.b2048.single.json)<br>`preg_match_all() [literal]` 21.759<br>One-shot: 33.912 (+55.85%) | [4 KiB](inputs/cases/technical.all.n48.b4096.single.json)<br>`strpos() loop` 42.236<br>One-shot: 40.456 (-4.21%) | [Input](inputs/cases/comments.all.n48.b4096.single.json)<br>`strpos() loop` 42.021<br>One-shot: 40.788 (-2.93%)<br>win |
| `Replacer::replace()`; replacements: 1 | [8 KiB](inputs/cases/technical.replace.n48.b8192.single.json)<br>`preg_replace_callback() [prefix]` 32.126<br>One-shot: 36.191 (+12.65%) | [16 KiB](inputs/cases/technical.replace.n48.b16384.single.json)<br>`preg_replace_callback() [prefix]` 80.320<br>One-shot: 61.388 (-23.57%) | [Input](inputs/cases/comments.replace.n48.b16384.single.json)<br>`preg_replace_callback() [prefix]` 99.329<br>One-shot: 67.569 (-31.97%)<br>win |

## Prepared objects: which dictionary wins at each text length?

Objects are constructed before timing. Each call includes result creation, consumption and release. Every length tests 8, 16, 32 and 48 keys with the same dictionary order. Replacer performs exactly one replacement in every row, regardless of dictionary size.

**Each entry is key count: prepared time in µs (observed change against the best measured existing method).** Negative means faster; positive means slower. † marks a quality issue and never removes the measured change. Click an entry for the reference name and time; [quality details](prepared-grid/QUALITY.md) give the actual sample spread and A/A deviation.

| Operation | 128 B | 256 B | 1 KiB | 4 KiB |
|---|---|---|---|---|
| `Matcher::matches()`; no matches | [8: 0.364 (+1.28%)](prepared-grid/TIMINGS.md#any-b128)<br>[16: 0.363 (-21.44%)](prepared-grid/TIMINGS.md#any-b128)<br>[32: 0.375 (-36.05%)](prepared-grid/TIMINGS.md#any-b128)<br>[48: 0.352 (-52.70%)](prepared-grid/TIMINGS.md#any-b128) | [8: 0.525 (+38.52%)](prepared-grid/TIMINGS.md#any-b256)<br>[16: 0.556 (-15.01%)†](prepared-grid/TIMINGS.md#any-b256)<br>[32: 0.517 (-44.15%)](prepared-grid/TIMINGS.md#any-b256)<br>[48: 0.515 (-56.57%)†](prepared-grid/TIMINGS.md#any-b256) | [8: 2.946 (2.2 times slower)†](prepared-grid/TIMINGS.md#any-b1024)<br>[16: 2.617 (+52.71%)†](prepared-grid/TIMINGS.md#any-b1024)<br>[32: 2.415 (-15.18%)†](prepared-grid/TIMINGS.md#any-b1024)<br>[48: 2.367 (-46.39%)†](prepared-grid/TIMINGS.md#any-b1024) | [8: 13.336 (3.2 times slower)](prepared-grid/TIMINGS.md#any-b4096)<br>[16: 12.527 (2.0 times slower)†](prepared-grid/TIMINGS.md#any-b4096)<br>[32: 11.250 (+15.02%)](prepared-grid/TIMINGS.md#any-b4096)<br>[48: 10.881 (-29.55%)†](prepared-grid/TIMINGS.md#any-b4096) |
| `Matcher::getMatchedKeywords()`; one occurrence | [8: 0.385 (-38.50%)](prepared-grid/TIMINGS.md#unique-b128)<br>[16: 0.391 (-55.51%)](prepared-grid/TIMINGS.md#unique-b128)<br>[32: 0.390 (-71.07%)†](prepared-grid/TIMINGS.md#unique-b128)<br>[48: 0.378 (-78.83%)](prepared-grid/TIMINGS.md#unique-b128) | [8: 0.542 (-18.01%)](prepared-grid/TIMINGS.md#unique-b256)<br>[16: 0.626 (-48.54%)†](prepared-grid/TIMINGS.md#unique-b256)<br>[32: 0.555 (-68.55%)](prepared-grid/TIMINGS.md#unique-b256)<br>[48: 0.783 (-75.58%)†](prepared-grid/TIMINGS.md#unique-b256) | [8: 1.611 (-22.90%)](prepared-grid/TIMINGS.md#unique-b1024)<br>[16: 1.613 (-61.48%)†](prepared-grid/TIMINGS.md#unique-b1024)<br>[32: 2.039 (-76.06%)†](prepared-grid/TIMINGS.md#unique-b1024)<br>[48: 1.861 (-84.51%)†](prepared-grid/TIMINGS.md#unique-b1024) | [8: 11.965 (+86.60%)†](prepared-grid/TIMINGS.md#unique-b4096)<br>[16: 11.310 (-16.07%)†](prepared-grid/TIMINGS.md#unique-b4096)<br>[32: 10.501 (-62.16%)](prepared-grid/TIMINGS.md#unique-b4096)<br>[48: 10.234 (-76.02%)†](prepared-grid/TIMINGS.md#unique-b4096) |
| `Matcher::countMatches()`; one occurrence | [8: 0.380 (-7.30%)](prepared-grid/TIMINGS.md#count-b128)<br>[16: 0.369 (-43.95%)](prepared-grid/TIMINGS.md#count-b128)<br>[32: 0.368 (-67.78%)](prepared-grid/TIMINGS.md#count-b128)<br>[48: 0.370 (-76.93%)†](prepared-grid/TIMINGS.md#count-b128) | [8: 0.542 (+23.49%)](prepared-grid/TIMINGS.md#count-b256)<br>[16: 0.597 (-38.61%)†](prepared-grid/TIMINGS.md#count-b256)<br>[32: 0.547 (-64.81%)](prepared-grid/TIMINGS.md#count-b256)<br>[48: 0.710 (-73.60%)†](prepared-grid/TIMINGS.md#count-b256) | [8: 1.604 (-13.45%)](prepared-grid/TIMINGS.md#count-b1024)<br>[16: 2.028 (-50.95%)†](prepared-grid/TIMINGS.md#count-b1024)<br>[32: 1.876 (-79.39%)](prepared-grid/TIMINGS.md#count-b1024)<br>[48: 1.685 (-85.79%)†](prepared-grid/TIMINGS.md#count-b1024) | [8: 5.622 (+2.45%)†](prepared-grid/TIMINGS.md#count-b4096)<br>[16: 5.941 (-50.29%)†](prepared-grid/TIMINGS.md#count-b4096)<br>[32: 5.651 (-79.52%)](prepared-grid/TIMINGS.md#count-b4096)<br>[48: 5.795 (-86.36%)†](prepared-grid/TIMINGS.md#count-b4096) |
| `Matcher::matchAll()`; one occurrence | [8: 0.451 (-28.60%)](prepared-grid/TIMINGS.md#all-b128)<br>[16: 0.444 (-48.31%)](prepared-grid/TIMINGS.md#all-b128)<br>[32: 0.439 (-66.83%)](prepared-grid/TIMINGS.md#all-b128)<br>[48: 0.432 (-75.53%)](prepared-grid/TIMINGS.md#all-b128) | [8: 0.651 (-1.96%)](prepared-grid/TIMINGS.md#all-b256)<br>[16: 0.653 (-41.40%)](prepared-grid/TIMINGS.md#all-b256)<br>[32: 0.635 (-62.79%)](prepared-grid/TIMINGS.md#all-b256)<br>[48: 1.758 (-69.76%)†](prepared-grid/TIMINGS.md#all-b256) | [8: 2.635 (+25.52%)†](prepared-grid/TIMINGS.md#all-b1024)<br>[16: 2.718 (-36.18%)†](prepared-grid/TIMINGS.md#all-b1024)<br>[32: 2.633 (-69.21%)†](prepared-grid/TIMINGS.md#all-b1024)<br>[48: 2.396 (-79.87%)†](prepared-grid/TIMINGS.md#all-b1024) | [8: 14.039 (2.2 times slower)](prepared-grid/TIMINGS.md#all-b4096)<br>[16: 12.979 (-2.51%)](prepared-grid/TIMINGS.md#all-b4096)<br>[32: 11.407 (-58.61%)](prepared-grid/TIMINGS.md#all-b4096)<br>[48: 11.400 (-73.21%)](prepared-grid/TIMINGS.md#all-b4096) |
| `Replacer::replace()`; replacements: 1 | [8: 0.396 (+8.10%)](prepared-grid/TIMINGS.md#replace-b128)<br>[16: 0.398 (-20.75%)](prepared-grid/TIMINGS.md#replace-b128)<br>[32: 0.398 (-37.80%)](prepared-grid/TIMINGS.md#replace-b128)<br>[48: 0.400 (-46.73%)](prepared-grid/TIMINGS.md#replace-b128) | [8: 0.612 (+54.65%)](prepared-grid/TIMINGS.md#replace-b256)<br>[16: 0.618 (-15.01%)](prepared-grid/TIMINGS.md#replace-b256)<br>[32: 0.604 (-39.64%)](prepared-grid/TIMINGS.md#replace-b256)<br>[48: 0.712 (-50.03%)](prepared-grid/TIMINGS.md#replace-b256) | [8: 1.655 (+21.73%)](prepared-grid/TIMINGS.md#replace-b1024)<br>[16: 1.732 (-8.50%)†](prepared-grid/TIMINGS.md#replace-b1024)<br>[32: 1.841 (-43.20%)†](prepared-grid/TIMINGS.md#replace-b1024)<br>[48: 1.714 (-59.69%)](prepared-grid/TIMINGS.md#replace-b1024) | [8: 6.191 (+38.58%)†](prepared-grid/TIMINGS.md#replace-b4096)<br>[16: 6.790 (+9.09%)†](prepared-grid/TIMINGS.md#replace-b4096)<br>[32: 6.700 (-28.91%)†](prepared-grid/TIMINGS.md#replace-b4096)<br>[48: 6.520 (-56.11%)†](prepared-grid/TIMINGS.md#replace-b4096) |

### Starting point: 128 B and 8 keys

The presence check has no matches. Each other operation has one occurrence; Replacer makes one replacement and returns 122 bytes. Construction and destruction are excluded.

| Operation | Best measured existing, µs | Prepared, µs | Decision |
|---|---|---:|---|
| [`Matcher::matches()`](prepared-grid/inputs/cases/technical.any.n8.b128.absent.json) | `str_contains() loop` 0.359 | 0.364 (+1.28%) | inconclusive |
| [`Matcher::getMatchedKeywords()`](prepared-grid/inputs/cases/technical.unique.n8.b128.single.json) | `strpos() loop` 0.627 | 0.385 (-38.50%) | win |
| [`Matcher::countMatches()`](prepared-grid/inputs/cases/technical.count.n8.b128.single.json) | `substr_count()/strpos() loop` 0.410 | 0.380 (-7.30%) | win |
| [`Matcher::matchAll()`](prepared-grid/inputs/cases/technical.all.n8.b128.single.json) | `strpos() loop` 0.631 | 0.451 (-28.60%) | win |
| [`Replacer::replace()`; replacements: 1](prepared-grid/inputs/cases/technical.replace.n8.b128.single.json) | `str_replace()` 0.366 | 0.396 (+8.10%) | loss |

[Full prepared grid, second-text checks and raw captures](prepared-grid/README.md). This is a prepared-call study; it does not measure how many calls repay construction.

## Presence checks: the same dictionary, different match positions

All three controls use a 64 KiB text and the same 48-key dictionary. The matching key is #25. Both native and existing algorithms can stop early; their stopping conditions differ.

| Match starts at byte | Text | Best existing, µs | Prepared, µs | One-shot, µs |
|---:|---|---|---:|---:|
| 8 | [64 KiB; 48 keys; one match at byte 8](inputs/cases/technical.any.n48.b65536.early.json) | `preg_match() [prefix]` 0.323 | 0.211 (-34.61%) | 28.892 (89.5 times slower) |
| 32763 | [64 KiB; 48 keys; one match at byte 32763](inputs/cases/technical.any.n48.b65536.middle.json) | `preg_match() [prefix]` 176.161 | 97.101 (-44.88%)† | 135.497 (-23.08%)† |
| 65518 | [64 KiB; 48 keys; one match at byte 65518](inputs/cases/technical.any.n48.b65536.late.json) | `preg_match() [prefix]` 384.223 | 193.642 (-49.60%)† | 235.941 (-38.59%) |

## Measurement sets and quality

Prepared grid: 80 primary comparisons and 5 second-text checks; 49 of 85 passed. [Quality register](prepared-grid/QUALITY.md).

The length and 4 KiB search measured 64 inputs: 111 of 128 native comparisons passed timing quality checks. All selected inputs passed independent expected-output checks, and a deliberately wrong expected output was rejected.

The 256-byte slice measured 33 short inputs and one separate 4 KiB count-baseline control; 68 of 68 timing comparisons passed. [Its quality register](short-256/QUALITY.md) and samples remain separate.

The extension build is shared; captures and their quality checks remain separate. Timings from different cohorts are not averaged together.

## Limits and reproduction

Zero or one occurrence is held fixed; this series does not measure dense results. Technical prose and comment text have different byte distributions. A failed second-text check or a later reversal limits the recommendation to the confirmed input. Close or flagged points cannot establish a losing endpoint.

[Reproduction commands](REPRODUCE.md), the [plan](plan.json), [collector](study.py), [harness](harness.php), exact input JSONs and [raw captures](data/captures.json.gz) are saved. No AMD or earlier application timings are merged.
