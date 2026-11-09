# Matcher and Replacer on 256-byte texts

9 November 2026. GCC 14.2, Intel Core i7-13700H. Short-text inputs are exactly 256 bytes; a separate 4 KiB control checks the count baseline. Dictionary order and match count stay fixed while N changes.

[All inputs](TIMINGS.md) · [Every implementation](RECIPES.md) · [Counters](COUNTERS.md) · [Quality](QUALITY.md) · [Method](METHOD.md) · [Build identity](data/build.json)

33 short inputs and one 4 KiB count-baseline check. 68 of 68 native comparisons passed timing quality checks. All selected inputs passed exact-output checks; [overlap-specific baseline checks](data/count-baseline-checks.json) also rejected a deliberately incorrect counting recipe.

## What pays on a short text

No tested 256-byte input produced a confirmed one-shot win. Faster prepared calls therefore require object reuse to pay for construction on this slice.

The smallest tested confirmed prepared wins on the primary text use 8 or 16 keys, depending on the operation. The next table shows the smaller losses and the second-text checks.

The winner changes between texts for `Matcher::matchAll()` with 8 keys.

## Prepared: smallest tested winning dictionary

The loss and win cells each show the input size, best measured existing time and prepared-object time. These are tested points, not universal key-count thresholds. Intermediate close or flagged observations retain their measured times and relative changes.

| Operation | Nearest smaller loss, µs | Smallest tested win, µs | Same mode on the second text, µs |
|---|---|---|---|
| `Matcher::matches()`; no matches | [8 keys](inputs/cases/technical.any.n8.b256.absent.json)<br>`str_contains() loop` 0.377<br>Prepared: 0.521 (+38.11%) | [16 keys](inputs/cases/technical.any.n16.b256.absent.json)<br>`preg_match() [prefix]` 0.629<br>Prepared: 0.529 (-15.91%) | [Input](inputs/cases/comments.any.n16.b256.absent.json)<br>`preg_match() [prefix]` 0.588<br>Prepared: 0.512 (-12.88%)<br>win |
| `Matcher::getMatchedKeywords()`; one occurrence | [1 key](inputs/cases/technical.unique.n1.b256.single.json)<br>`strpos() + result list` 0.196<br>Prepared: 0.346 (+76.37%) | [8 keys](inputs/cases/technical.unique.n8.b256.single.json)<br>`strpos() loop` 0.662<br>Prepared: 0.543 (-18.01%)<br>Intermediate observations:<br>[4 keys](inputs/cases/technical.unique.n4.b256.single.json)<br>`strpos() loop` 0.540<br>Prepared: 0.544 (+0.69%) | [Input](inputs/cases/comments.unique.n8.b256.single.json)<br>`strpos() loop` 0.605<br>Prepared: 0.536 (-11.46%)<br>win |
| `Matcher::countMatches()`; one occurrence | [8 keys](inputs/cases/technical.count.n8.b256.single.json)<br>`substr_count()/strpos() loop` 0.436<br>Prepared: 0.542 (+24.12%) | [16 keys](inputs/cases/technical.count.n16.b256.single.json)<br>`substr_count()/strpos() loop` 0.873<br>Prepared: 0.544 (-37.68%) | [Input](inputs/cases/comments.count.n16.b256.single.json)<br>`substr_count()/strpos() loop` 0.938<br>Prepared: 0.542 (-42.29%)<br>win |
| `Matcher::matchAll()`; one occurrence | [4 keys](inputs/cases/technical.all.n4.b256.single.json)<br>`strpos() loop` 0.537<br>Prepared: 0.665 (+23.81%) | [8 keys](inputs/cases/technical.all.n8.b256.single.json)<br>`strpos() loop` 0.660<br>Prepared: 0.644 (-2.30%) | [Input](inputs/cases/comments.all.n8.b256.single.json)<br>`strpos() loop` 0.605<br>Prepared: 0.629 (+4.00%)<br>loss |
| `Replacer::replace()`; replacements: 1 | [8 keys](inputs/cases/technical.replace.n8.b256.single.json)<br>`str_replace()` 0.394<br>Prepared: 0.605 (+53.27%) | [16 keys](inputs/cases/technical.replace.n16.b256.single.json)<br>`preg_replace_callback() [prefix]` 0.693<br>Prepared: 0.609 (-12.05%) | [Input](inputs/cases/comments.replace.n16.b256.single.json)<br>`preg_replace_callback() [prefix]` 0.654<br>Prepared: 0.602 (-7.96%)<br>win |

## All five operations with the same 48-key dictionary

Prepared excludes construction and destruction; one-shot includes both. Percentages use the single reference median in the row.

| Operation | Result | Best measured existing, µs | Prepared, µs | One-shot, µs |
|---|---|---|---:|---:|
| [`Matcher::matches()`](inputs/cases/technical.any.n48.b256.absent.json) | false | `preg_match() [prefix]` 1.181 | 0.513 (-56.54%) | 29.311 (24.8 times slower) |
| [`Matcher::getMatchedKeywords()`](inputs/cases/technical.unique.n48.b256.single.json) | 1 unique key | `strpos() loop` 2.218 | 0.533 (-75.95%) | 29.159 (13.1 times slower) |
| [`Matcher::countMatches()`](inputs/cases/technical.count.n48.b256.single.json) | int 1 | `strpos() loop` 2.069 | 0.542 (-73.78%) | 29.404 (14.2 times slower) |
| [`Matcher::matchAll()`](inputs/cases/technical.all.n48.b256.single.json) | list of 1 MatchResult | `strpos() loop` 2.190 | 0.634 (-71.04%) | 29.828 (13.6 times slower) |
| [`Replacer::replace()`](inputs/cases/technical.replace.n48.b256.single.json) | 1 replacement; output 250 B | `preg_replace_callback() [prefix]` 1.201 | 0.621 (-48.32%) | 19.276 (16.1 times slower) |

## Presence: early, middle and late matches

The matching key is #25 of the same 48-key dictionary.

| Match starts at byte | Best measured existing, µs | Prepared, µs | One-shot, µs |
|---:|---|---:|---:|
| [8](inputs/cases/technical.any.n48.b256.early.json) | `preg_match() [prefix]` 0.335 | 0.222 (-33.85%) | 29.623 (88.4 times slower) |
| [123](inputs/cases/technical.any.n48.b256.middle.json) | `preg_match() [prefix]` 0.735 | 0.359 (-51.13%) | 28.831 (39.2 times slower) |
| [238](inputs/cases/technical.any.n48.b256.late.json) | `str_contains() loop` 1.002 | 0.503 (-49.86%) | 29.139 (29.1 times slower) |

## Counting: 4 KiB baseline crosscheck

The two PHP count loops are within 2%; one-shot Matcher still wins against both.

The additional recipe uses `substr_count()` for keys without self-overlap and a one-byte-advancing `strpos()` loop for the other keys. Preparation of this eligibility map is outside timing. The 4 KiB control has 48 keys and one occurrence.

| Best measured existing, µs | Prepared, µs | One-shot, µs |
|---|---:|---:|
| `strpos() loop` 41.962 | 5.529 (-86.82%) | 37.124 (-11.53%) |

This is a separate baseline check, not a 256-byte observation. Its complete input and every recipe are in [TIMINGS](TIMINGS.md) and [RECIPES](RECIPES.md).

## Limits and reproduction

The slice tests one dictionary family, two controlled English backgrounds and zero or one occurrence. Values between sampled N are unknown. Short repeated texts favor a warm working set; these are not full-request or production-throughput measurements. † marks a quality issue while retaining the observed time and relative change.

[Reproduction](REPRODUCE.md) · [Frozen plan](plan.json) · [Exact observations](data/timings.json.gz) · [All capture attempts](data/captures.json.gz).
