# Every 256-byte input and the count-baseline control

[Summary](README.md) · [Method](METHOD.md) · [Quality](QUALITY.md)

One reference median is shared by both object modes. Relative changes use the displayed medians. † marks a quality issue.

| Operation and exact input | Best measured existing, µs | Prepared, µs | One-shot, µs | Paired decisions |
|---|---|---:|---:|---|
| `Matcher::matchAll()`; comments; [256 B; 8 keys; one match at byte 124](inputs/cases/comments.all.n8.b256.single.json) | `strpos() loop` 0.605 | 0.629 (+4.00%) | 4.498 (7.4 times slower) | loss / loss |
| `Matcher::matches()`; comments; [256 B; 16 keys; no matches](inputs/cases/comments.any.n16.b256.absent.json) | `preg_match() [prefix]` 0.588 | 0.512 (-12.88%) | 10.831 (18.4 times slower) | win / loss |
| `Matcher::countMatches()`; comments; [256 B; 16 keys; one match at byte 124](inputs/cases/comments.count.n16.b256.single.json) | `substr_count()/strpos() loop` 0.938 | 0.542 (-42.29%) | 10.855 (11.6 times slower) | win / loss |
| `Replacer::replace()`; comments; [256 B; 16 keys; replacements: 1; start byte 124; output 250 B](inputs/cases/comments.replace.n16.b256.single.json) | `preg_replace_callback() [prefix]` 0.654 | 0.602 (-7.96%) | 4.920 (7.5 times slower) | win / loss |
| `Matcher::getMatchedKeywords()`; comments; [256 B; 8 keys; one match at byte 124](inputs/cases/comments.unique.n8.b256.single.json) | `strpos() loop` 0.605 | 0.536 (-11.46%) | 4.459 (7.4 times slower) | win / loss |
| `Matcher::matchAll()`; technical; [256 B; 1 key; one match at byte 124](inputs/cases/technical.all.n1.b256.single.json) | `strpos() loop` 0.437 | 0.608 (+39.17%) | 1.084 (2.5 times slower) | loss / loss |
| `Matcher::matchAll()`; technical; [256 B; 16 keys; one match at byte 124](inputs/cases/technical.all.n16.b256.single.json) | `strpos() loop` 1.048 | 0.645 (-38.47%) | 11.138 (10.6 times slower) | win / loss |
| `Matcher::matchAll()`; technical; [256 B; 4 keys; one match at byte 124](inputs/cases/technical.all.n4.b256.single.json) | `strpos() loop` 0.537 | 0.665 (+23.81%) | 2.607 (4.9 times slower) | loss / loss |
| `Matcher::matchAll()`; technical; [256 B; 48 keys; one match at byte 124](inputs/cases/technical.all.n48.b256.single.json) | `strpos() loop` 2.190 | 0.634 (-71.04%) | 29.828 (13.6 times slower) | win / loss |
| `Matcher::matchAll()`; technical; [256 B; 8 keys; one match at byte 124](inputs/cases/technical.all.n8.b256.single.json) | `strpos() loop` 0.660 | 0.644 (-2.30%) | 4.518 (6.8 times slower) | win / loss |
| `Matcher::matches()`; technical; [256 B; 1 key; no matches](inputs/cases/technical.any.n1.b256.absent.json) | `str_contains()` 0.190 | 0.488 (2.6 times slower) | 0.962 (5.1 times slower) | loss / loss |
| `Matcher::matches()`; technical; [256 B; 16 keys; no matches](inputs/cases/technical.any.n16.b256.absent.json) | `preg_match() [prefix]` 0.629 | 0.529 (-15.91%) | 10.890 (17.3 times slower) | win / loss |
| `Matcher::matches()`; technical; [256 B; 4 keys; no matches](inputs/cases/technical.any.n4.b256.absent.json) | `str_contains() loop` 0.290 | 0.539 (+85.97%) | 2.440 (8.4 times slower) | loss / loss |
| `Matcher::matches()`; technical; [256 B; 48 keys; no matches](inputs/cases/technical.any.n48.b256.absent.json) | `preg_match() [prefix]` 1.181 | 0.513 (-56.54%) | 29.311 (24.8 times slower) | win / loss |
| `Matcher::matches()`; technical; [256 B; 48 keys; one match at byte 8](inputs/cases/technical.any.n48.b256.early.json) | `preg_match() [prefix]` 0.335 | 0.222 (-33.85%) | 29.623 (88.4 times slower) | win / loss |
| `Matcher::matches()`; technical; [256 B; 48 keys; one match at byte 238](inputs/cases/technical.any.n48.b256.late.json) | `str_contains() loop` 1.002 | 0.503 (-49.86%) | 29.139 (29.1 times slower) | win / loss |
| `Matcher::matches()`; technical; [256 B; 48 keys; one match at byte 123](inputs/cases/technical.any.n48.b256.middle.json) | `preg_match() [prefix]` 0.735 | 0.359 (-51.13%) | 28.831 (39.2 times slower) | win / loss |
| `Matcher::matches()`; technical; [256 B; 8 keys; no matches](inputs/cases/technical.any.n8.b256.absent.json) | `str_contains() loop` 0.377 | 0.521 (+38.11%) | 4.376 (11.6 times slower) | loss / loss |
| `Matcher::countMatches()`; technical; [256 B; 1 key; one match at byte 124](inputs/cases/technical.count.n1.b256.single.json) | `substr_count()` 0.185 | 0.465 (2.5 times slower) | 0.929 (5.0 times slower) | loss / loss |
| `Matcher::countMatches()`; technical; [256 B; 16 keys; one match at byte 124](inputs/cases/technical.count.n16.b256.single.json) | `substr_count()/strpos() loop` 0.873 | 0.544 (-37.68%) | 10.907 (12.5 times slower) | win / loss |
| `Matcher::countMatches()`; technical; [256 B; 4 keys; one match at byte 124](inputs/cases/technical.count.n4.b256.single.json) | `substr_count()/strpos() loop` 0.306 | 0.523 (+71.05%) | 2.334 (7.6 times slower) | loss / loss |
| `Matcher::countMatches()`; technical; [256 B; 48 keys; one match at byte 124](inputs/cases/technical.count.n48.b256.single.json) | `strpos() loop` 2.069 | 0.542 (-73.78%) | 29.404 (14.2 times slower) | win / loss |
| `Matcher::countMatches()`; technical; [4 KiB; 48 keys; one match at byte 2044](inputs/cases/technical.count.n48.b4096.single.json) | `strpos() loop` 41.962 | 5.529 (-86.82%) | 37.124 (-11.53%) | win / win |
| `Matcher::countMatches()`; technical; [256 B; 8 keys; one match at byte 124](inputs/cases/technical.count.n8.b256.single.json) | `substr_count()/strpos() loop` 0.436 | 0.542 (+24.12%) | 4.451 (10.2 times slower) | loss / loss |
| `Replacer::replace()`; technical; [256 B; 1 key; replacements: 1; start byte 124; output 250 B](inputs/cases/technical.replace.n1.b256.single.json) | `strtr()` 0.243 | 0.521 (2.1 times slower) | 0.991 (4.1 times slower) | loss / loss |
| `Replacer::replace()`; technical; [256 B; 16 keys; replacements: 1; start byte 124; output 250 B](inputs/cases/technical.replace.n16.b256.single.json) | `preg_replace_callback() [prefix]` 0.693 | 0.609 (-12.05%) | 4.914 (7.1 times slower) | win / loss |
| `Replacer::replace()`; technical; [256 B; 4 keys; replacements: 1; start byte 124; output 250 B](inputs/cases/technical.replace.n4.b256.single.json) | `str_replace()` 0.321 | 0.576 (+79.51%) | 1.791 (5.6 times slower) | loss / loss |
| `Replacer::replace()`; technical; [256 B; 48 keys; replacements: 1; start byte 124; output 250 B](inputs/cases/technical.replace.n48.b256.single.json) | `preg_replace_callback() [prefix]` 1.201 | 0.621 (-48.32%) | 19.276 (16.1 times slower) | win / loss |
| `Replacer::replace()`; technical; [256 B; 8 keys; replacements: 1; start byte 124; output 250 B](inputs/cases/technical.replace.n8.b256.single.json) | `str_replace()` 0.394 | 0.605 (+53.27%) | 3.516 (8.9 times slower) | loss / loss |
| `Matcher::getMatchedKeywords()`; technical; [256 B; 1 key; one match at byte 124](inputs/cases/technical.unique.n1.b256.single.json) | `strpos() + result list` 0.196 | 0.346 (+76.37%) | 0.842 (4.3 times slower) | loss / loss |
| `Matcher::getMatchedKeywords()`; technical; [256 B; 16 keys; one match at byte 124](inputs/cases/technical.unique.n16.b256.single.json) | `strpos() loop` 1.062 | 0.547 (-48.49%) | 11.010 (10.4 times slower) | win / loss |
| `Matcher::getMatchedKeywords()`; technical; [256 B; 4 keys; one match at byte 124](inputs/cases/technical.unique.n4.b256.single.json) | `strpos() loop` 0.540 | 0.544 (+0.69%) | 2.375 (4.4 times slower) | close / loss |
| `Matcher::getMatchedKeywords()`; technical; [256 B; 48 keys; one match at byte 124](inputs/cases/technical.unique.n48.b256.single.json) | `strpos() loop` 2.218 | 0.533 (-75.95%) | 29.159 (13.1 times slower) | win / loss |
| `Matcher::getMatchedKeywords()`; technical; [256 B; 8 keys; one match at byte 124](inputs/cases/technical.unique.n8.b256.single.json) | `strpos() loop` 0.662 | 0.543 (-18.01%) | 4.493 (6.8 times slower) | win / loss |
