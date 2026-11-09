# Prepared objects: dictionary size by text length

GCC 14.2, Intel Core i7-13700H. All native objects are created before timing. Each result includes the call, result creation, consumption and release.

[General break-even report](../README.md) · [Every comparison](TIMINGS.md) · [Every implementation](RECIPES.md) · [Counters](COUNTERS.md) · [Quality](QUALITY.md) · [Method](METHOD.md)

80 primary comparisons and 5 second-text checks; 49 passed timing quality checks. All inputs passed 391 exact-output comparisons before timing; wrong expected output was rejected.

## Prepared time and observed advantage at every dictionary size

Each entry is key count: prepared time in µs (observed change against the best measured existing method). Every cell tests N=8, 16, 32, 48. Negative means faster; positive means slower. † marks a quality issue; its measured change is still shown. Click an entry for all reference times. [Quality details](QUALITY.md) quantify sample spread and A/A deviation.

| Operation | 128 B | 256 B | 1 KiB | 4 KiB |
|---|---|---|---|---|
| `Matcher::matches()`; no matches | [8: 0.364 (+1.28%)](TIMINGS.md#any-b128)<br>[16: 0.363 (-21.44%)](TIMINGS.md#any-b128)<br>[32: 0.375 (-36.05%)](TIMINGS.md#any-b128)<br>[48: 0.352 (-52.70%)](TIMINGS.md#any-b128) | [8: 0.525 (+38.52%)](TIMINGS.md#any-b256)<br>[16: 0.556 (-15.01%)†](TIMINGS.md#any-b256)<br>[32: 0.517 (-44.15%)](TIMINGS.md#any-b256)<br>[48: 0.515 (-56.57%)†](TIMINGS.md#any-b256) | [8: 2.946 (2.2 times slower)†](TIMINGS.md#any-b1024)<br>[16: 2.617 (+52.71%)†](TIMINGS.md#any-b1024)<br>[32: 2.415 (-15.18%)†](TIMINGS.md#any-b1024)<br>[48: 2.367 (-46.39%)†](TIMINGS.md#any-b1024) | [8: 13.336 (3.2 times slower)](TIMINGS.md#any-b4096)<br>[16: 12.527 (2.0 times slower)†](TIMINGS.md#any-b4096)<br>[32: 11.250 (+15.02%)](TIMINGS.md#any-b4096)<br>[48: 10.881 (-29.55%)†](TIMINGS.md#any-b4096) |
| `Matcher::getMatchedKeywords()`; one occurrence | [8: 0.385 (-38.50%)](TIMINGS.md#unique-b128)<br>[16: 0.391 (-55.51%)](TIMINGS.md#unique-b128)<br>[32: 0.390 (-71.07%)†](TIMINGS.md#unique-b128)<br>[48: 0.378 (-78.83%)](TIMINGS.md#unique-b128) | [8: 0.542 (-18.01%)](TIMINGS.md#unique-b256)<br>[16: 0.626 (-48.54%)†](TIMINGS.md#unique-b256)<br>[32: 0.555 (-68.55%)](TIMINGS.md#unique-b256)<br>[48: 0.783 (-75.58%)†](TIMINGS.md#unique-b256) | [8: 1.611 (-22.90%)](TIMINGS.md#unique-b1024)<br>[16: 1.613 (-61.48%)†](TIMINGS.md#unique-b1024)<br>[32: 2.039 (-76.06%)†](TIMINGS.md#unique-b1024)<br>[48: 1.861 (-84.51%)†](TIMINGS.md#unique-b1024) | [8: 11.965 (+86.60%)†](TIMINGS.md#unique-b4096)<br>[16: 11.310 (-16.07%)†](TIMINGS.md#unique-b4096)<br>[32: 10.501 (-62.16%)](TIMINGS.md#unique-b4096)<br>[48: 10.234 (-76.02%)†](TIMINGS.md#unique-b4096) |
| `Matcher::countMatches()`; one occurrence | [8: 0.380 (-7.30%)](TIMINGS.md#count-b128)<br>[16: 0.369 (-43.95%)](TIMINGS.md#count-b128)<br>[32: 0.368 (-67.78%)](TIMINGS.md#count-b128)<br>[48: 0.370 (-76.93%)†](TIMINGS.md#count-b128) | [8: 0.542 (+23.49%)](TIMINGS.md#count-b256)<br>[16: 0.597 (-38.61%)†](TIMINGS.md#count-b256)<br>[32: 0.547 (-64.81%)](TIMINGS.md#count-b256)<br>[48: 0.710 (-73.60%)†](TIMINGS.md#count-b256) | [8: 1.604 (-13.45%)](TIMINGS.md#count-b1024)<br>[16: 2.028 (-50.95%)†](TIMINGS.md#count-b1024)<br>[32: 1.876 (-79.39%)](TIMINGS.md#count-b1024)<br>[48: 1.685 (-85.79%)†](TIMINGS.md#count-b1024) | [8: 5.622 (+2.45%)†](TIMINGS.md#count-b4096)<br>[16: 5.941 (-50.29%)†](TIMINGS.md#count-b4096)<br>[32: 5.651 (-79.52%)](TIMINGS.md#count-b4096)<br>[48: 5.795 (-86.36%)†](TIMINGS.md#count-b4096) |
| `Matcher::matchAll()`; one occurrence | [8: 0.451 (-28.60%)](TIMINGS.md#all-b128)<br>[16: 0.444 (-48.31%)](TIMINGS.md#all-b128)<br>[32: 0.439 (-66.83%)](TIMINGS.md#all-b128)<br>[48: 0.432 (-75.53%)](TIMINGS.md#all-b128) | [8: 0.651 (-1.96%)](TIMINGS.md#all-b256)<br>[16: 0.653 (-41.40%)](TIMINGS.md#all-b256)<br>[32: 0.635 (-62.79%)](TIMINGS.md#all-b256)<br>[48: 1.758 (-69.76%)†](TIMINGS.md#all-b256) | [8: 2.635 (+25.52%)†](TIMINGS.md#all-b1024)<br>[16: 2.718 (-36.18%)†](TIMINGS.md#all-b1024)<br>[32: 2.633 (-69.21%)†](TIMINGS.md#all-b1024)<br>[48: 2.396 (-79.87%)†](TIMINGS.md#all-b1024) | [8: 14.039 (2.2 times slower)](TIMINGS.md#all-b4096)<br>[16: 12.979 (-2.51%)](TIMINGS.md#all-b4096)<br>[32: 11.407 (-58.61%)](TIMINGS.md#all-b4096)<br>[48: 11.400 (-73.21%)](TIMINGS.md#all-b4096) |
| `Replacer::replace()`; replacements: 1 | [8: 0.396 (+8.10%)](TIMINGS.md#replace-b128)<br>[16: 0.398 (-20.75%)](TIMINGS.md#replace-b128)<br>[32: 0.398 (-37.80%)](TIMINGS.md#replace-b128)<br>[48: 0.400 (-46.73%)](TIMINGS.md#replace-b128) | [8: 0.612 (+54.65%)](TIMINGS.md#replace-b256)<br>[16: 0.618 (-15.01%)](TIMINGS.md#replace-b256)<br>[32: 0.604 (-39.64%)](TIMINGS.md#replace-b256)<br>[48: 0.712 (-50.03%)](TIMINGS.md#replace-b256) | [8: 1.655 (+21.73%)](TIMINGS.md#replace-b1024)<br>[16: 1.732 (-8.50%)†](TIMINGS.md#replace-b1024)<br>[32: 1.841 (-43.20%)†](TIMINGS.md#replace-b1024)<br>[48: 1.714 (-59.69%)](TIMINGS.md#replace-b1024) | [8: 6.191 (+38.58%)†](TIMINGS.md#replace-b4096)<br>[16: 6.790 (+9.09%)†](TIMINGS.md#replace-b4096)<br>[32: 6.700 (-28.91%)†](TIMINGS.md#replace-b4096)<br>[48: 6.520 (-56.11%)†](TIMINGS.md#replace-b4096) |

## Starting point: 128 B and 8 keys

Presence has no matches. Other operations have one occurrence; replacement returns 122 bytes.

| Operation | Best measured existing, µs | Prepared, µs | Decision |
|---|---|---:|---|
| [`Matcher::matches()`](inputs/cases/technical.any.n8.b128.absent.json) | `str_contains() loop` 0.359 | 0.364 (+1.28%) | inconclusive |
| [`Matcher::getMatchedKeywords()`](inputs/cases/technical.unique.n8.b128.single.json) | `strpos() loop` 0.627 | 0.385 (-38.50%) | win |
| [`Matcher::countMatches()`](inputs/cases/technical.count.n8.b128.single.json) | `substr_count()/strpos() loop` 0.410 | 0.380 (-7.30%) | win |
| [`Matcher::matchAll()`](inputs/cases/technical.all.n8.b128.single.json) | `strpos() loop` 0.631 | 0.451 (-28.60%) | win |
| [`Replacer::replace()`; replacements: 1](inputs/cases/technical.replace.n8.b128.single.json) | `str_replace()` 0.366 | 0.396 (+8.10%) | loss |

## Limits and reproduction

The grid uses one real dictionary family and controlled prefixes of one primary background. The smallest confirmed winning N at 128 bytes is checked on a second background; all five checks won. Those checks are listed in the full timing table. This is a prepared-call comparison, not the number of calls needed to amortize construction.

[Reproduce](REPRODUCE.md) · [Frozen plan](plan.json) · [Exact points](data/timings.json.gz) · [Raw captures](data/captures.json.gz).
