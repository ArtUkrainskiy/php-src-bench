# Prepared calls: every length/dictionary combination

[Summary](README.md) · [Method](METHOD.md) · [Quality](QUALITY.md)

One row is one exact input and one prepared call. Construction and destruction are outside timing. Percentages use the shown medians. † marks failed quality checks.

## Matcher::matches()

<a id="any-b128"></a>
### 128 B

| Keys and exact input | Best measured existing, µs | Prepared, µs | Decision |
|---|---|---:|---|
| [8](inputs/cases/technical.any.n8.b128.absent.json) | `str_contains() loop` 0.359 | 0.364 (+1.28%) | inconclusive |
| [16](inputs/cases/technical.any.n16.b128.absent.json) | `preg_match() [prefix]` 0.462 | 0.363 (-21.44%) | win |
| [32](inputs/cases/technical.any.n32.b128.absent.json) | `preg_match() [prefix]` 0.587 | 0.375 (-36.05%) | win |
| [48](inputs/cases/technical.any.n48.b128.absent.json) | `preg_match() [prefix]` 0.744 | 0.352 (-52.70%) | win |

<a id="any-b256"></a>
### 256 B

| Keys and exact input | Best measured existing, µs | Prepared, µs | Decision |
|---|---|---:|---|
| [8](inputs/cases/technical.any.n8.b256.absent.json) | `str_contains() loop` 0.379 | 0.525 (+38.52%) | loss |
| [16](inputs/cases/technical.any.n16.b256.absent.json) | `preg_match() [prefix]` 0.654 | 0.556 (-15.01%)† | flagged |
| [32](inputs/cases/technical.any.n32.b256.absent.json) | `preg_match() [prefix]` 0.926 | 0.517 (-44.15%) | win |
| [48](inputs/cases/technical.any.n48.b256.absent.json) | `preg_match() [prefix]` 1.185 | 0.515 (-56.57%)† | flagged |

<a id="any-b1024"></a>
### 1 KiB

| Keys and exact input | Best measured existing, µs | Prepared, µs | Decision |
|---|---|---:|---|
| [8](inputs/cases/technical.any.n8.b1024.absent.json) | `preg_match() [literal]` 1.370 | 2.946 (2.2 times slower)† | flagged |
| [16](inputs/cases/technical.any.n16.b1024.absent.json) | `preg_match() [prefix]` 1.714 | 2.617 (+52.71%)† | flagged |
| [32](inputs/cases/technical.any.n32.b1024.absent.json) | `preg_match() [prefix]` 2.847 | 2.415 (-15.18%)† | flagged |
| [48](inputs/cases/technical.any.n48.b1024.absent.json) | `preg_match() [prefix]` 4.415 | 2.367 (-46.39%)† | flagged |

<a id="any-b4096"></a>
### 4 KiB

| Keys and exact input | Best measured existing, µs | Prepared, µs | Decision |
|---|---|---:|---|
| [8](inputs/cases/technical.any.n8.b4096.absent.json) | `preg_match() [literal]` 4.181 | 13.336 (3.2 times slower) | loss |
| [16](inputs/cases/technical.any.n16.b4096.absent.json) | `preg_match() [prefix]` 6.171 | 12.527 (2.0 times slower)† | flagged |
| [32](inputs/cases/technical.any.n32.b4096.absent.json) | `preg_match() [prefix]` 9.780 | 11.250 (+15.02%) | loss |
| [48](inputs/cases/technical.any.n48.b4096.absent.json) | `preg_match() [prefix]` 15.445 | 10.881 (-29.55%)† | flagged |

## Matcher::getMatchedKeywords()

<a id="unique-b128"></a>
### 128 B

| Keys and exact input | Best measured existing, µs | Prepared, µs | Decision |
|---|---|---:|---|
| [8](inputs/cases/technical.unique.n8.b128.single.json) | `strpos() loop` 0.627 | 0.385 (-38.50%) | win |
| [16](inputs/cases/technical.unique.n16.b128.single.json) | `strpos() loop` 0.878 | 0.391 (-55.51%) | win |
| [32](inputs/cases/technical.unique.n32.b128.single.json) | `strpos() loop` 1.348 | 0.390 (-71.07%)† | flagged |
| [48](inputs/cases/technical.unique.n48.b128.single.json) | `strpos() loop` 1.786 | 0.378 (-78.83%) | win |

<a id="unique-b256"></a>
### 256 B

| Keys and exact input | Best measured existing, µs | Prepared, µs | Decision |
|---|---|---:|---|
| [8](inputs/cases/technical.unique.n8.b256.single.json) | `strpos() loop` 0.661 | 0.542 (-18.01%) | win |
| [16](inputs/cases/technical.unique.n16.b256.single.json) | `strpos() loop` 1.216 | 0.626 (-48.54%)† | flagged |
| [32](inputs/cases/technical.unique.n32.b256.single.json) | `strpos() loop` 1.765 | 0.555 (-68.55%) | win |
| [48](inputs/cases/technical.unique.n48.b256.single.json) | `strpos() loop` 3.207 | 0.783 (-75.58%)† | flagged |

<a id="unique-b1024"></a>
### 1 KiB

| Keys and exact input | Best measured existing, µs | Prepared, µs | Decision |
|---|---|---:|---|
| [8](inputs/cases/technical.unique.n8.b1024.single.json) | `strpos() loop` 2.089 | 1.611 (-22.90%) | win |
| [16](inputs/cases/technical.unique.n16.b1024.single.json) | `strpos() loop` 4.188 | 1.613 (-61.48%)† | flagged |
| [32](inputs/cases/technical.unique.n32.b1024.single.json) | `strpos() loop` 8.516 | 2.039 (-76.06%)† | flagged |
| [48](inputs/cases/technical.unique.n48.b1024.single.json) | `strpos() loop` 12.009 | 1.861 (-84.51%)† | flagged |

<a id="unique-b4096"></a>
### 4 KiB

| Keys and exact input | Best measured existing, µs | Prepared, µs | Decision |
|---|---|---:|---|
| [8](inputs/cases/technical.unique.n8.b4096.single.json) | `strpos() loop` 6.412 | 11.965 (+86.60%)† | flagged |
| [16](inputs/cases/technical.unique.n16.b4096.single.json) | `preg_match_all() [literal]` 13.475 | 11.310 (-16.07%)† | flagged |
| [32](inputs/cases/technical.unique.n32.b4096.single.json) | `strpos() loop` 27.750 | 10.501 (-62.16%) | win |
| [48](inputs/cases/technical.unique.n48.b4096.single.json) | `strpos() loop` 42.680 | 10.234 (-76.02%)† | flagged |

## Matcher::countMatches()

<a id="count-b128"></a>
### 128 B

| Keys and exact input | Best measured existing, µs | Prepared, µs | Decision |
|---|---|---:|---|
| [8](inputs/cases/technical.count.n8.b128.single.json) | `substr_count()/strpos() loop` 0.410 | 0.380 (-7.30%) | win |
| [16](inputs/cases/technical.count.n16.b128.single.json) | `substr_count()/strpos() loop` 0.659 | 0.369 (-43.95%) | win |
| [32](inputs/cases/technical.count.n32.b128.single.json) | `substr_count()/strpos() loop` 1.143 | 0.368 (-67.78%) | win |
| [48](inputs/cases/technical.count.n48.b128.single.json) | `substr_count()/strpos() loop` 1.602 | 0.370 (-76.93%)† | flagged |

<a id="count-b256"></a>
### 256 B

| Keys and exact input | Best measured existing, µs | Prepared, µs | Decision |
|---|---|---:|---|
| [8](inputs/cases/technical.count.n8.b256.single.json) | `substr_count()/strpos() loop` 0.439 | 0.542 (+23.49%) | loss |
| [16](inputs/cases/technical.count.n16.b256.single.json) | `substr_count()/strpos() loop` 0.973 | 0.597 (-38.61%)† | flagged |
| [32](inputs/cases/technical.count.n32.b256.single.json) | `strpos() loop` 1.553 | 0.547 (-64.81%) | win |
| [48](inputs/cases/technical.count.n48.b256.single.json) | `strpos() loop` 2.689 | 0.710 (-73.60%)† | flagged |

<a id="count-b1024"></a>
### 1 KiB

| Keys and exact input | Best measured existing, µs | Prepared, µs | Decision |
|---|---|---:|---|
| [8](inputs/cases/technical.count.n8.b1024.single.json) | `substr_count()/strpos() loop` 1.853 | 1.604 (-13.45%) | win |
| [16](inputs/cases/technical.count.n16.b1024.single.json) | `preg_match_all() [prefix]` 4.135 | 2.028 (-50.95%)† | flagged |
| [32](inputs/cases/technical.count.n32.b1024.single.json) | `strpos() loop` 9.106 | 1.876 (-79.39%) | win |
| [48](inputs/cases/technical.count.n48.b1024.single.json) | `strpos() loop` 11.855 | 1.685 (-85.79%)† | flagged |

<a id="count-b4096"></a>
### 4 KiB

| Keys and exact input | Best measured existing, µs | Prepared, µs | Decision |
|---|---|---:|---|
| [8](inputs/cases/technical.count.n8.b4096.single.json) | `preg_match_all() [prefix]` 5.487 | 5.622 (+2.45%)† | flagged |
| [16](inputs/cases/technical.count.n16.b4096.single.json) | `preg_match_all() [prefix]` 11.953 | 5.941 (-50.29%)† | flagged |
| [32](inputs/cases/technical.count.n32.b4096.single.json) | `strpos() loop` 27.595 | 5.651 (-79.52%) | win |
| [48](inputs/cases/technical.count.n48.b4096.single.json) | `strpos() loop` 42.496 | 5.795 (-86.36%)† | flagged |

## Matcher::matchAll()

<a id="all-b128"></a>
### 128 B

| Keys and exact input | Best measured existing, µs | Prepared, µs | Decision |
|---|---|---:|---|
| [8](inputs/cases/technical.all.n8.b128.single.json) | `strpos() loop` 0.631 | 0.451 (-28.60%) | win |
| [16](inputs/cases/technical.all.n16.b128.single.json) | `strpos() loop` 0.859 | 0.444 (-48.31%) | win |
| [32](inputs/cases/technical.all.n32.b128.single.json) | `strpos() loop` 1.322 | 0.439 (-66.83%) | win |
| [48](inputs/cases/technical.all.n48.b128.single.json) | `strpos() loop` 1.766 | 0.432 (-75.53%) | win |

<a id="all-b256"></a>
### 256 B

| Keys and exact input | Best measured existing, µs | Prepared, µs | Decision |
|---|---|---:|---|
| [8](inputs/cases/technical.all.n8.b256.single.json) | `strpos() loop` 0.664 | 0.651 (-1.96%) | inconclusive |
| [16](inputs/cases/technical.all.n16.b256.single.json) | `strpos() loop` 1.115 | 0.653 (-41.40%) | win |
| [32](inputs/cases/technical.all.n32.b256.single.json) | `strpos() loop` 1.707 | 0.635 (-62.79%) | win |
| [48](inputs/cases/technical.all.n48.b256.single.json) | `strpos() loop` 5.812 | 1.758 (-69.76%)† | flagged |

<a id="all-b1024"></a>
### 1 KiB

| Keys and exact input | Best measured existing, µs | Prepared, µs | Decision |
|---|---|---:|---|
| [8](inputs/cases/technical.all.n8.b1024.single.json) | `strpos() loop` 2.099 | 2.635 (+25.52%)† | flagged |
| [16](inputs/cases/technical.all.n16.b1024.single.json) | `strpos() loop` 4.258 | 2.718 (-36.18%)† | flagged |
| [32](inputs/cases/technical.all.n32.b1024.single.json) | `strpos() loop` 8.553 | 2.633 (-69.21%)† | flagged |
| [48](inputs/cases/technical.all.n48.b1024.single.json) | `strpos() loop` 11.905 | 2.396 (-79.87%)† | flagged |

<a id="all-b4096"></a>
### 4 KiB

| Keys and exact input | Best measured existing, µs | Prepared, µs | Decision |
|---|---|---:|---|
| [8](inputs/cases/technical.all.n8.b4096.single.json) | `strpos() loop` 6.368 | 14.039 (2.2 times slower) | loss |
| [16](inputs/cases/technical.all.n16.b4096.single.json) | `preg_match_all() [prefix]` 13.313 | 12.979 (-2.51%) | win |
| [32](inputs/cases/technical.all.n32.b4096.single.json) | `strpos() loop` 27.558 | 11.407 (-58.61%) | win |
| [48](inputs/cases/technical.all.n48.b4096.single.json) | `strpos() loop` 42.553 | 11.400 (-73.21%) | win |

## Replacer::replace()

<a id="replace-b128"></a>
### 128 B

| Keys and exact input | Best measured existing, µs | Prepared, µs | Decision |
|---|---|---:|---|
| [8 keys; replacements: 1; output 122 B](inputs/cases/technical.replace.n8.b128.single.json) | `str_replace()` 0.366 | 0.396 (+8.10%) | loss |
| [16 keys; replacements: 1; output 122 B](inputs/cases/technical.replace.n16.b128.single.json) | `str_replace()` 0.502 | 0.398 (-20.75%) | win |
| [32 keys; replacements: 1; output 122 B](inputs/cases/technical.replace.n32.b128.single.json) | `preg_replace_callback() [prefix]` 0.640 | 0.398 (-37.80%) | win |
| [48 keys; replacements: 1; output 122 B](inputs/cases/technical.replace.n48.b128.single.json) | `preg_replace_callback() [prefix]` 0.750 | 0.400 (-46.73%) | win |

<a id="replace-b256"></a>
### 256 B

| Keys and exact input | Best measured existing, µs | Prepared, µs | Decision |
|---|---|---:|---|
| [8 keys; replacements: 1; output 250 B](inputs/cases/technical.replace.n8.b256.single.json) | `str_replace()` 0.396 | 0.612 (+54.65%) | loss |
| [16 keys; replacements: 1; output 250 B](inputs/cases/technical.replace.n16.b256.single.json) | `str_replace()` 0.727 | 0.618 (-15.01%) | win |
| [32 keys; replacements: 1; output 250 B](inputs/cases/technical.replace.n32.b256.single.json) | `preg_replace_callback() [prefix]` 1.001 | 0.604 (-39.64%) | win |
| [48 keys; replacements: 1; output 250 B](inputs/cases/technical.replace.n48.b256.single.json) | `preg_replace_callback() [prefix]` 1.425 | 0.712 (-50.03%) | win |

<a id="replace-b1024"></a>
### 1 KiB

| Keys and exact input | Best measured existing, µs | Prepared, µs | Decision |
|---|---|---:|---|
| [8 keys; replacements: 1; output 1018 B](inputs/cases/technical.replace.n8.b1024.single.json) | `preg_replace_callback() [literal]` 1.360 | 1.655 (+21.73%) | loss |
| [16 keys; replacements: 1; output 1018 B](inputs/cases/technical.replace.n16.b1024.single.json) | `preg_replace_callback() [prefix]` 1.893 | 1.732 (-8.50%)† | flagged |
| [32 keys; replacements: 1; output 1018 B](inputs/cases/technical.replace.n32.b1024.single.json) | `preg_replace_callback() [prefix]` 3.242 | 1.841 (-43.20%)† | flagged |
| [48 keys; replacements: 1; output 1018 B](inputs/cases/technical.replace.n48.b1024.single.json) | `preg_replace_callback() [prefix]` 4.253 | 1.714 (-59.69%) | win |

<a id="replace-b4096"></a>
### 4 KiB

| Keys and exact input | Best measured existing, µs | Prepared, µs | Decision |
|---|---|---:|---|
| [8 keys; replacements: 1; output 3.99414 KiB](inputs/cases/technical.replace.n8.b4096.single.json) | `preg_replace_callback() [prefix]` 4.467 | 6.191 (+38.58%)† | flagged |
| [16 keys; replacements: 1; output 3.99414 KiB](inputs/cases/technical.replace.n16.b4096.single.json) | `preg_replace_callback() [prefix]` 6.224 | 6.790 (+9.09%)† | flagged |
| [32 keys; replacements: 1; output 3.99414 KiB](inputs/cases/technical.replace.n32.b4096.single.json) | `preg_replace_callback() [prefix]` 9.425 | 6.700 (-28.91%)† | flagged |
| [48 keys; replacements: 1; output 3.99414 KiB](inputs/cases/technical.replace.n48.b4096.single.json) | `preg_replace_callback() [prefix]` 14.857 | 6.520 (-56.11%)† | flagged |

## Checks on the second text

| Operation and exact input | Best measured existing, µs | Prepared, µs | Decision |
|---|---|---:|---|
| `Matcher::matchAll()`; [128 B; 8 keys; one match at byte 60](inputs/cases/comments.all.n8.b128.single.json) | `strpos() loop` 0.710 | 0.490 (-30.94%) | win |
| `Matcher::matches()`; [128 B; 16 keys; no matches](inputs/cases/comments.any.n16.b128.absent.json) | `preg_match() [prefix]` 0.522 | 0.400 (-23.36%) | win |
| `Matcher::countMatches()`; [128 B; 8 keys; one match at byte 60](inputs/cases/comments.count.n8.b128.single.json) | `substr_count()/strpos() loop` 0.456 | 0.413 (-9.43%) | win |
| `Replacer::replace()`; [128 B; 16 keys; replacements: 1; start byte 60; output 122 B](inputs/cases/comments.replace.n16.b128.single.json) | `preg_replace_callback() [prefix]` 0.606 | 0.447 (-26.17%) | win |
| `Matcher::getMatchedKeywords()`; [128 B; 8 keys; one match at byte 60](inputs/cases/comments.unique.n8.b128.single.json) | `strpos() loop` 0.721 | 0.441 (-38.76%) | win |
