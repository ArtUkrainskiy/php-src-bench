# Selected inputs: size extremes and larger match counts

Includes a positive comment, the document with 198 occurrences, and both formats of two email templates. Input selection uses no timings. Modes and the reference rule follow the [main report](README.md).

| Input | Best existing method, µs | Prepared, µs | One-shot, µs |
|---|---|---:|---:|
| [Matcher::matches() · text (EN); 72 B; 403 keys; no matches](inputs/cases/comment.69493.any.json) | `preg_match() [prefix]` 1.475 | 0.310 (-79.00%) | 294.861 (199.9 times slower) |
| [Matcher::matches() · text (EN); 985 B; 403 keys; no matches](inputs/cases/comment.55617.any.json) | `preg_match() [prefix]` 13.741 | 1.798 (-86.91%) | 297.608 (21.7 times slower) |
| [Matcher::matches() · text (EN); 577 B; 403 keys; first match at byte 296; matching key is #11 in dictionary order](inputs/cases/comment.69522.any.json) | `strtolower() + strpos() loop` 2.118 | 0.806 (-61.94%) | 298.750 (141.0 times slower) |
| [Matcher::getMatchedKeywords() · text (EN); 2.14 KiB; 48 keys; occurrences: 6; unique matched keys: 1](inputs/cases/document.robotparser.unique.json) | `strpos() loop` 21.801 | 3.387 (-84.46%) | 33.159 (+52.10%) |
| [Matcher::getMatchedKeywords() · text (EN); 40.48 KiB; 48 keys; occurrences: 10; unique matched keys: 2](inputs/cases/document.collections.unique.json) | `strpos() loop` 438.256 | 121.421 (-72.29%) | 159.740 (-63.55%) |
| [Matcher::getMatchedKeywords() · text (EN); 27.22 KiB; 48 keys; occurrences: 198; unique matched keys: 3](inputs/cases/document.cookielib.unique.json) | `strpos() loop` 298.366 | 83.877 (-71.89%) | 125.850 (-57.82%) |
| [Matcher::countMatches() · text (EN); 2.14 KiB; 48 keys; occurrences: 6; unique matched keys: 1](inputs/cases/document.robotparser.count.json) | `preg_match_all() [literal]` 22.152† | 3.176 (-85.66%)† | 32.475 (+46.60%)† |
| [Matcher::countMatches() · text (EN); 40.48 KiB; 48 keys; occurrences: 10; unique matched keys: 2](inputs/cases/document.collections.count.json) | `strpos() loop` 466.372 | 110.862 (-76.23%) | 152.189 (-67.37%) |
| [Matcher::countMatches() · text (EN); 27.22 KiB; 48 keys; occurrences: 198; unique matched keys: 3](inputs/cases/document.cookielib.count.json) | `strpos() loop` 333.142 | 77.040 (-76.87%) | 118.711 (-64.37%) |
| [Matcher::matchAll() · text (EN); 2.14 KiB; 48 keys; occurrences: 6; unique matched keys: 1](inputs/cases/document.robotparser.all.json) | `strpos() loop` 23.170 | 4.720 (-79.63%)† | 33.802 (+45.89%) |
| [Matcher::matchAll() · text (EN); 40.48 KiB; 48 keys; occurrences: 10; unique matched keys: 2](inputs/cases/document.collections.all.json) | `strpos() loop` 468.094 | 125.967 (-73.09%) | 158.273 (-66.19%) |
| [Matcher::matchAll() · text (EN); 27.22 KiB; 48 keys; occurrences: 198; unique matched keys: 3](inputs/cases/document.cookielib.all.json) | `strpos() loop` 403.943† | 98.968 (-75.50%)† | 132.583 (-67.18%)† |
| [Replacer::replace() · text (EN); 2.14 KiB; 48 keys; 6 replacements; output 2.18 KiB](inputs/cases/document.robotparser.replace.json) | `preg_replace_callback() [prefix]` 7.271 | 3.136 (-56.87%) | 21.166 (2.9 times slower) |
| [Replacer::replace() · text (EN); 40.48 KiB; 48 keys; 10 replacements; output 40.5 KiB](inputs/cases/document.collections.replace.json) | `preg_replace_callback() [prefix]` 225.173 | 118.071 (-47.56%) | 136.365 (-39.44%) |
| [Replacer::replace() · HTML template; 15.97 KiB; 3 keys; 7 replacements; output 16.04 KiB](inputs/cases/email.password-reset.html.json) | `preg_replace_callback() [literal]` 1.807 | — | 23.674 (13.1 times slower) |
| [Replacer::replace() · plain-text template; 345 B; 3 keys; 3 replacements; output 370 B](inputs/cases/email.password-reset.txt.json) | `str_replace()` 0.355 | — | 1.759 (5.0 times slower) |
| [Replacer::replace() · HTML template; 28.31 KiB; 10 keys; 15 replacements; output 28.36 KiB](inputs/cases/email.receipt.html.json) | `preg_replace_callback() [prefix]` 3.046 | — | 40.266 (13.2 times slower) |
| [Replacer::replace() · plain-text template; 498 B; 10 keys; 11 replacements; output 542 B](inputs/cases/email.receipt.txt.json) | `strtr()` 0.812 | — | 3.937 (4.8 times slower) |
