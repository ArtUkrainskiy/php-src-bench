# Timings: every input and object lifetime

[Summary](README.md) · [Corpus](DESIGN.md) · [Quality](QUALITY.md)

Both object columns compare against the one reference median shown in the row, taken from the one-shot series. Each batch has its own reference. † marks a quality issue with the object or reference. [Every implementation and control](RECIPES.md) is retained.

## Matcher: ASCII-insensitive searches in comments

| Input | Best existing method, µs | Prepared, µs | One-shot, µs |
|---|---|---:|---:|
| [Matcher::matches() · text (EN); 90 B; 403 keys; no matches](inputs/cases/comment.13.any.json) | `preg_match() [prefix]` 1.678 | 0.343 (-79.56%) | 295.515 (176.2 times slower) |
| [Matcher::getMatchedKeywords() · text (EN); 90 B; 403 keys; occurrences: 0; unique matched keys: 0](inputs/cases/comment.13.unique.json) | `preg_match_all() [prefix]` 8.871 | 0.372 (-95.81%) | 299.053 (33.7 times slower) |
| [Matcher::matches() · text (EN); 84 B; 403 keys; no matches](inputs/cases/comment.41710.any.json) | `preg_match() [prefix]` 1.681 | 0.359 (-78.65%) | 294.977 (175.5 times slower) |
| [Matcher::getMatchedKeywords() · text (EN); 84 B; 403 keys; occurrences: 0; unique matched keys: 0](inputs/cases/comment.41710.unique.json) | `preg_match_all() [prefix]` 8.941 | 0.385 (-95.70%) | 295.870 (33.1 times slower) |
| [Matcher::matches() · text (EN); 73 B; 403 keys; no matches](inputs/cases/comment.28.any.json) | `preg_match() [prefix]` 1.457 | 0.318 (-78.15%) | 295.676 (202.9 times slower) |
| [Matcher::getMatchedKeywords() · text (EN); 73 B; 403 keys; occurrences: 0; unique matched keys: 0](inputs/cases/comment.28.unique.json) | `preg_match_all() [prefix]` 8.171 | 0.347 (-95.75%) | 295.702 (36.2 times slower) |
| [Matcher::matches() · text (EN); 72 B; 403 keys; no matches](inputs/cases/comment.69493.any.json) | `preg_match() [prefix]` 1.475 | 0.310 (-79.00%) | 294.861 (199.9 times slower) |
| [Matcher::getMatchedKeywords() · text (EN); 72 B; 403 keys; occurrences: 0; unique matched keys: 0](inputs/cases/comment.69493.unique.json) | `preg_match_all() [prefix]` 7.972 | 0.337 (-95.78%) | 295.781 (37.1 times slower) |
| [Matcher::matches() · text (EN); 146 B; 403 keys; no matches](inputs/cases/comment.41719.any.json) | `preg_match() [prefix]` 2.499 | 0.467 (-81.29%) | 296.010 (118.5 times slower) |
| [Matcher::getMatchedKeywords() · text (EN); 146 B; 403 keys; occurrences: 0; unique matched keys: 0](inputs/cases/comment.41719.unique.json) | `preg_match_all() [prefix]` 12.807† | 0.507 (-96.04%)† | 296.384 (23.1 times slower)† |
| [Matcher::matches() · text (EN); 115 B; 403 keys; no matches](inputs/cases/comment.69503.any.json) | `preg_match() [prefix]` 2.055 | 0.434 (-78.88%) | 296.028 (144.1 times slower) |
| [Matcher::getMatchedKeywords() · text (EN); 115 B; 403 keys; occurrences: 0; unique matched keys: 0](inputs/cases/comment.69503.unique.json) | `preg_match_all() [prefix]` 10.766 | 0.461 (-95.72%) | 295.271 (27.4 times slower) |
| [Matcher::matches() · text (EN); 152 B; 403 keys; no matches](inputs/cases/comment.41704.any.json) | `preg_match() [prefix]` 2.583 | 0.500 (-80.66%) | 296.981 (115.0 times slower) |
| [Matcher::getMatchedKeywords() · text (EN); 152 B; 403 keys; occurrences: 0; unique matched keys: 0](inputs/cases/comment.41704.unique.json) | `preg_match_all() [prefix]` 13.251 | 0.534 (-95.97%) | 296.328 (22.4 times slower) |
| [Matcher::matches() · text (EN); 119 B; 403 keys; no matches](inputs/cases/comment.10.any.json) | `preg_match() [prefix]` 2.110 | 0.372 (-82.35%) | 295.451 (140.0 times slower) |
| [Matcher::getMatchedKeywords() · text (EN); 119 B; 403 keys; occurrences: 0; unique matched keys: 0](inputs/cases/comment.10.unique.json) | `preg_match_all() [prefix]` 10.955 | 0.408 (-96.28%) | 298.035 (27.2 times slower) |
| [Matcher::matches() · text (EN); 338 B; 403 keys; no matches](inputs/cases/comment.41698.any.json) | `preg_match() [prefix]` 4.909 | 0.826 (-83.17%) | 297.329 (60.6 times slower) |
| [Matcher::getMatchedKeywords() · text (EN); 338 B; 403 keys; occurrences: 0; unique matched keys: 0](inputs/cases/comment.41698.unique.json) | `preg_match_all() [prefix]` 23.802 | 0.885 (-96.28%) | 295.979 (12.4 times slower) |
| [Matcher::matches() · text (EN); 365 B; 403 keys; first match at byte 91; matching key is #11 in dictionary order](inputs/cases/comment.97301.any.json) | `strtolower() + strpos() loop` 1.382 | 0.378 (-72.64%) | 295.502 (213.8 times slower) |
| [Matcher::getMatchedKeywords() · text (EN); 365 B; 403 keys; occurrences: 1; unique matched keys: 1](inputs/cases/comment.97301.unique.json) | `preg_match_all() [prefix]` 26.603 | 1.023 (-96.15%) | 296.577 (11.1 times slower) |
| [Matcher::matches() · text (EN); 248 B; 403 keys; no matches](inputs/cases/comment.83414.any.json) | `preg_match() [prefix]` 3.675 | 0.685 (-81.37%) | 295.693 (80.5 times slower) |
| [Matcher::getMatchedKeywords() · text (EN); 248 B; 403 keys; occurrences: 0; unique matched keys: 0](inputs/cases/comment.83414.unique.json) | `preg_match_all() [prefix]` 18.287 | 0.714 (-96.09%) | 296.121 (16.2 times slower) |
| [Matcher::matches() · text (EN); 237 B; 403 keys; no matches](inputs/cases/comment.13918.any.json) | `preg_match() [prefix]` 3.673 | 0.649 (-82.34%) | 296.354 (80.7 times slower) |
| [Matcher::getMatchedKeywords() · text (EN); 237 B; 403 keys; occurrences: 0; unique matched keys: 0](inputs/cases/comment.13918.unique.json) | `preg_match_all() [prefix]` 18.503† | 0.680 (-96.32%)† | 296.000 (16.0 times slower)† |
| [Matcher::matches() · text (EN); 456 B; 403 keys; no matches](inputs/cases/comment.41696.any.json) | `preg_match() [prefix]` 6.611 | 1.062 (-83.94%) | 297.146 (44.9 times slower) |
| [Matcher::getMatchedKeywords() · text (EN); 456 B; 403 keys; occurrences: 0; unique matched keys: 0](inputs/cases/comment.41696.unique.json) | `preg_match_all() [prefix]` 31.336 | 1.117 (-96.44%) | 296.404 (9.5 times slower) |
| [Matcher::matches() · text (EN); 985 B; 403 keys; no matches](inputs/cases/comment.55617.any.json) | `preg_match() [prefix]` 13.741 | 1.798 (-86.91%) | 297.608 (21.7 times slower) |
| [Matcher::getMatchedKeywords() · text (EN); 985 B; 403 keys; occurrences: 0; unique matched keys: 0](inputs/cases/comment.55617.unique.json) | `strtolower() + strpos() loop` 70.742 | 1.883 (-97.34%) | 301.131 (4.3 times slower) |
| [Matcher::matches() · text (EN); 577 B; 403 keys; first match at byte 296; matching key is #11 in dictionary order](inputs/cases/comment.69522.any.json) | `strtolower() + strpos() loop` 2.118 | 0.806 (-61.94%) | 298.750 (141.0 times slower) |
| [Matcher::getMatchedKeywords() · text (EN); 577 B; 403 keys; occurrences: 1; unique matched keys: 1](inputs/cases/comment.69522.unique.json) | `preg_match_all() [prefix]` 39.698 | 1.432 (-96.39%) | 297.598 (7.5 times slower) |
| [Matcher::matches() · text (EN); 464 B; 403 keys; no matches](inputs/cases/comment.13909.any.json) | `preg_match() [prefix]` 6.747 | 1.072 (-84.12%) | 297.333 (44.1 times slower) |
| [Matcher::getMatchedKeywords() · text (EN); 464 B; 403 keys; occurrences: 0; unique matched keys: 0](inputs/cases/comment.13909.unique.json) | `preg_match_all() [prefix]` 31.685 | 1.121 (-96.46%) | 297.680 (9.4 times slower) |


## Matcher: case-sensitive searches in complete texts

| Input | Best existing method, µs | Prepared, µs | One-shot, µs |
|---|---|---:|---:|
| [Matcher::getMatchedKeywords() · text (EN); 36.39 KiB; 48 keys; occurrences: 45; unique matched keys: 5](inputs/cases/document.pickle.unique.json) | `strpos() loop` 413.135 | 119.394 (-71.10%) | 155.945 (-62.25%) |
| [Matcher::countMatches() · text (EN); 36.39 KiB; 48 keys; occurrences: 45; unique matched keys: 5](inputs/cases/document.pickle.count.json) | `strpos() loop` 448.949 | 111.651 (-75.13%) | 148.767 (-66.86%) |
| [Matcher::matchAll() · text (EN); 36.39 KiB; 48 keys; occurrences: 45; unique matched keys: 5](inputs/cases/document.pickle.all.json) | `strpos() loop` 463.257 | 118.258 (-74.47%) | 149.283 (-67.78%) |
| [Matcher::getMatchedKeywords() · text (EN); 16.56 KiB; 48 keys; occurrences: 31; unique matched keys: 2](inputs/cases/document.urlparse.unique.json) | `strpos() loop` 157.294 | 42.038 (-73.27%) | 76.393 (-51.43%) |
| [Matcher::countMatches() · text (EN); 16.56 KiB; 48 keys; occurrences: 31; unique matched keys: 2](inputs/cases/document.urlparse.count.json) | `strpos() loop` 161.164 | 33.957 (-78.93%) | 72.157 (-55.23%) |
| [Matcher::matchAll() · text (EN); 16.56 KiB; 48 keys; occurrences: 31; unique matched keys: 2](inputs/cases/document.urlparse.all.json) | `strpos() loop` 167.722 | 46.389 (-72.34%) | 77.518 (-53.78%) |
| [Matcher::getMatchedKeywords() · text (EN); 36.58 KiB; 48 keys; occurrences: 24; unique matched keys: 2](inputs/cases/document.httplib.unique.json) | `strpos() loop` 308.407 | 63.304 (-79.47%) | 99.658 (-67.69%) |
| [Matcher::countMatches() · text (EN); 36.58 KiB; 48 keys; occurrences: 24; unique matched keys: 2](inputs/cases/document.httplib.count.json) | `strpos() loop` 323.420 | 56.306 (-82.59%) | 95.431 (-70.49%) |
| [Matcher::matchAll() · text (EN); 36.58 KiB; 48 keys; occurrences: 24; unique matched keys: 2](inputs/cases/document.httplib.all.json) | `strpos() loop` 329.785 | 72.674 (-77.96%) | 103.964 (-68.48%) |
| [Matcher::getMatchedKeywords() · text (EN); 10.63 KiB; 48 keys; occurrences: 36; unique matched keys: 4](inputs/cases/document.simplexmlrpcserver.unique.json) | `strpos() loop` 103.159 | 28.445 (-72.43%) | 61.574 (-40.31%) |
| [Matcher::countMatches() · text (EN); 10.63 KiB; 48 keys; occurrences: 36; unique matched keys: 4](inputs/cases/document.simplexmlrpcserver.count.json) | `strpos() loop` 114.560 | 26.484 (-76.88%) | 63.551 (-44.53%) |
| [Matcher::matchAll() · text (EN); 10.63 KiB; 48 keys; occurrences: 36; unique matched keys: 4](inputs/cases/document.simplexmlrpcserver.all.json) | `strpos() loop` 124.220 | 32.635 (-73.73%) | 64.474 (-48.10%) |
| [Matcher::getMatchedKeywords() · text (EN); 27.22 KiB; 48 keys; occurrences: 198; unique matched keys: 3](inputs/cases/document.cookielib.unique.json) | `strpos() loop` 298.366 | 83.877 (-71.89%) | 125.850 (-57.82%) |
| [Matcher::countMatches() · text (EN); 27.22 KiB; 48 keys; occurrences: 198; unique matched keys: 3](inputs/cases/document.cookielib.count.json) | `strpos() loop` 333.142 | 77.040 (-76.87%) | 118.711 (-64.37%) |
| [Matcher::matchAll() · text (EN); 27.22 KiB; 48 keys; occurrences: 198; unique matched keys: 3](inputs/cases/document.cookielib.all.json) | `strpos() loop` 403.943† | 98.968 (-75.50%)† | 132.583 (-67.18%)† |
| [Matcher::getMatchedKeywords() · text (EN); 19.15 KiB; 48 keys; occurrences: 89; unique matched keys: 2](inputs/cases/document.configparser.unique.json) | `strpos() loop` 199.166 | 55.691 (-72.04%) | 91.196 (-54.21%) |
| [Matcher::countMatches() · text (EN); 19.15 KiB; 48 keys; occurrences: 89; unique matched keys: 2](inputs/cases/document.configparser.count.json) | `strpos() loop` 214.279 | 50.054 (-76.64%) | 88.761 (-58.58%) |
| [Matcher::matchAll() · text (EN); 19.15 KiB; 48 keys; occurrences: 89; unique matched keys: 2](inputs/cases/document.configparser.all.json) | `strpos() loop` 236.038 | 62.947 (-73.33%) | 95.746 (-59.44%) |
| [Matcher::getMatchedKeywords() · text (EN); 9.32 KiB; 48 keys; occurrences: 80; unique matched keys: 3](inputs/cases/document.cookie.unique.json) | `strpos() loop` 91.089 | 22.645 (-75.14%) | 56.803 (-37.64%) |
| [Matcher::countMatches() · text (EN); 9.32 KiB; 48 keys; occurrences: 80; unique matched keys: 3](inputs/cases/document.cookie.count.json) | `strpos() loop` 97.340 | 21.425 (-77.99%) | 57.924 (-40.49%) |
| [Matcher::matchAll() · text (EN); 9.32 KiB; 48 keys; occurrences: 80; unique matched keys: 3](inputs/cases/document.cookie.all.json) | `strpos() loop` 118.377 | 30.636 (-74.12%) | 62.983 (-46.79%) |
| [Matcher::getMatchedKeywords() · text (EN); 4.07 KiB; 48 keys; occurrences: 47; unique matched keys: 2](inputs/cases/document.stringio.unique.json) | `strpos() loop` 41.913† | 8.084 (-80.71%)† | 39.708 (-5.26%)† |
| [Matcher::countMatches() · text (EN); 4.07 KiB; 48 keys; occurrences: 47; unique matched keys: 2](inputs/cases/document.stringio.count.json) | `strpos() loop` 43.920 | 5.995 (-86.35%) | 37.427 (-14.78%) |
| [Matcher::matchAll() · text (EN); 4.07 KiB; 48 keys; occurrences: 47; unique matched keys: 2](inputs/cases/document.stringio.all.json) | `strpos() loop` 54.457 | 11.868 (-78.21%) | 41.432 (-23.92%) |
| [Matcher::getMatchedKeywords() · text (EN); 22.03 KiB; 48 keys; occurrences: 51; unique matched keys: 4](inputs/cases/document.xmlrpclib.unique.json) | `strpos() loop` 225.165 | 63.324 (-71.88%) | 97.900 (-56.52%) |
| [Matcher::countMatches() · text (EN); 22.03 KiB; 48 keys; occurrences: 51; unique matched keys: 4](inputs/cases/document.xmlrpclib.count.json) | `strpos() loop` 245.228 | 60.171 (-75.46%) | 98.697 (-59.75%) |
| [Matcher::matchAll() · text (EN); 22.03 KiB; 48 keys; occurrences: 51; unique matched keys: 4](inputs/cases/document.xmlrpclib.all.json) | `strpos() loop` 260.023 | 67.289 (-74.12%) | 99.607 (-61.69%) |
| [Matcher::getMatchedKeywords() · text (EN); 6.43 KiB; 48 keys; occurrences: 56; unique matched keys: 2](inputs/cases/document.thread.unique.json) | `strpos() loop` 64.294 | 14.817 (-76.95%) | 47.996 (-25.35%) |
| [Matcher::countMatches() · text (EN); 6.43 KiB; 48 keys; occurrences: 56; unique matched keys: 2](inputs/cases/document.thread.count.json) | `strpos() loop` 69.400 | 12.424 (-82.10%) | 47.364 (-31.75%) |
| [Matcher::matchAll() · text (EN); 6.43 KiB; 48 keys; occurrences: 56; unique matched keys: 2](inputs/cases/document.thread.all.json) | `strpos() loop` 80.576 | 19.380 (-75.95%)† | 50.327 (-37.54%) |
| [Matcher::getMatchedKeywords() · text (EN); 4.45 KiB; 48 keys; occurrences: 17; unique matched keys: 3](inputs/cases/document.simplehttpserver.unique.json) | `strpos() loop` 45.131 | 9.907 (-78.05%) | 41.386 (-8.30%) |
| [Matcher::countMatches() · text (EN); 4.45 KiB; 48 keys; occurrences: 17; unique matched keys: 3](inputs/cases/document.simplehttpserver.count.json) | `strpos() loop` 47.204 | 6.787 (-85.62%) | 39.839 (-15.60%) |
| [Matcher::matchAll() · text (EN); 4.45 KiB; 48 keys; occurrences: 17; unique matched keys: 3](inputs/cases/document.simplehttpserver.all.json) | `strpos() loop` 50.891† | 11.856 (-76.70%)† | 41.549 (-18.36%)† |
| [Matcher::getMatchedKeywords() · text (EN); 21.98 KiB; 48 keys; occurrences: 52; unique matched keys: 3](inputs/cases/document.socketserver.unique.json) | `strpos() loop` 229.145 | 64.099 (-72.03%) | 98.884 (-56.85%) |
| [Matcher::countMatches() · text (EN); 21.98 KiB; 48 keys; occurrences: 52; unique matched keys: 3](inputs/cases/document.socketserver.count.json) | `strpos() loop` 258.148 | 58.272 (-77.43%) | 97.658 (-62.17%) |
| [Matcher::matchAll() · text (EN); 21.98 KiB; 48 keys; occurrences: 52; unique matched keys: 3](inputs/cases/document.socketserver.all.json) | `strpos() loop` 272.536 | 68.618 (-74.82%) | 100.356 (-63.18%) |
| [Matcher::getMatchedKeywords() · text (EN); 6.87 KiB; 48 keys; occurrences: 43; unique matched keys: 2](inputs/cases/document.queue.unique.json) | `strpos() loop` 67.935 | 16.158 (-76.22%) | 48.746 (-28.25%) |
| [Matcher::countMatches() · text (EN); 6.87 KiB; 48 keys; occurrences: 43; unique matched keys: 2](inputs/cases/document.queue.count.json) | `strpos() loop` 71.341 | 11.457 (-83.94%) | 47.270 (-33.74%) |
| [Matcher::matchAll() · text (EN); 6.87 KiB; 48 keys; occurrences: 43; unique matched keys: 2](inputs/cases/document.queue.all.json) | `strpos() loop` 82.701 | 22.846 (-72.38%) | 54.320 (-34.32%) |
| [Matcher::getMatchedKeywords() · text (EN); 10.16 KiB; 48 keys; occurrences: 18; unique matched keys: 4](inputs/cases/document.basehttpserver.unique.json) | `strpos() loop` 97.766 | 27.631 (-71.74%) | 60.035 (-38.59%) |
| [Matcher::countMatches() · text (EN); 10.16 KiB; 48 keys; occurrences: 18; unique matched keys: 4](inputs/cases/document.basehttpserver.count.json) | `strpos() loop` 107.866 | 23.440 (-78.27%) | 59.976 (-44.40%) |
| [Matcher::matchAll() · text (EN); 10.16 KiB; 48 keys; occurrences: 18; unique matched keys: 4](inputs/cases/document.basehttpserver.all.json) | `strpos() loop` 111.884 | 30.410 (-72.82%) | 60.774 (-45.68%) |
| [Matcher::getMatchedKeywords() · text (EN); 40.48 KiB; 48 keys; occurrences: 10; unique matched keys: 2](inputs/cases/document.collections.unique.json) | `strpos() loop` 438.256 | 121.421 (-72.29%) | 159.740 (-63.55%) |
| [Matcher::countMatches() · text (EN); 40.48 KiB; 48 keys; occurrences: 10; unique matched keys: 2](inputs/cases/document.collections.count.json) | `strpos() loop` 466.372 | 110.862 (-76.23%) | 152.189 (-67.37%) |
| [Matcher::matchAll() · text (EN); 40.48 KiB; 48 keys; occurrences: 10; unique matched keys: 2](inputs/cases/document.collections.all.json) | `strpos() loop` 468.094 | 125.967 (-73.09%) | 158.273 (-66.19%) |
| [Matcher::getMatchedKeywords() · text (EN); 2.14 KiB; 48 keys; occurrences: 6; unique matched keys: 1](inputs/cases/document.robotparser.unique.json) | `strpos() loop` 21.801 | 3.387 (-84.46%) | 33.159 (+52.10%) |
| [Matcher::countMatches() · text (EN); 2.14 KiB; 48 keys; occurrences: 6; unique matched keys: 1](inputs/cases/document.robotparser.count.json) | `preg_match_all() [literal]` 22.152† | 3.176 (-85.66%)† | 32.475 (+46.60%)† |
| [Matcher::matchAll() · text (EN); 2.14 KiB; 48 keys; occurrences: 6; unique matched keys: 1](inputs/cases/document.robotparser.all.json) | `strpos() loop` 23.170 | 4.720 (-79.63%)† | 33.802 (+45.89%) |


## Replacer: literal substitution in complete texts

| Input | Best existing method, µs | Prepared, µs | One-shot, µs |
|---|---|---:|---:|
| [Replacer::replace() · text (EN); 36.39 KiB; 48 keys; 44 replacements; output 36.34 KiB](inputs/cases/document.pickle.replace.json) | `preg_replace_callback() [prefix]` 234.267 | 107.187 (-54.25%) | 126.648 (-45.94%) |
| [Replacer::replace() · text (EN); 16.56 KiB; 48 keys; 31 replacements; output 16.68 KiB](inputs/cases/document.urlparse.replace.json) | `preg_replace_callback() [prefix]` 62.363 | 36.024 (-42.23%) | 53.691 (-13.91%) |
| [Replacer::replace() · text (EN); 36.58 KiB; 48 keys; 24 replacements; output 36.67 KiB](inputs/cases/document.httplib.replace.json) | `preg_replace_callback() [prefix]` 105.572 | 56.716 (-46.28%) | 74.796 (-29.15%) |
| [Replacer::replace() · text (EN); 10.63 KiB; 48 keys; 36 replacements; output 10.52 KiB](inputs/cases/document.simplexmlrpcserver.replace.json) | `preg_replace_callback() [prefix]` 45.277 | 24.471 (-45.95%) | 42.622 (-5.86%) |
| [Replacer::replace() · text (EN); 27.22 KiB; 48 keys; 198 replacements; output 28.34 KiB](inputs/cases/document.cookielib.replace.json) | `preg_replace_callback() [prefix]` 166.368 | 74.117 (-55.45%) | 92.268 (-44.54%) |
| [Replacer::replace() · text (EN); 19.15 KiB; 48 keys; 89 replacements; output 19.15 KiB](inputs/cases/document.configparser.replace.json) | `preg_replace_callback() [prefix]` 93.288 | 49.481 (-46.96%)† | 69.504 (-25.49%) |
| [Replacer::replace() · text (EN); 9.32 KiB; 48 keys; 80 replacements; output 9.77 KiB](inputs/cases/document.cookie.replace.json) | `preg_replace_callback() [prefix]` 40.651 | 20.240 (-50.21%)† | 37.940 (-6.67%) |
| [Replacer::replace() · text (EN); 4.07 KiB; 48 keys; 42 replacements; output 3.82 KiB](inputs/cases/document.stringio.replace.json) | `preg_replace_callback() [prefix]` 15.285 | 6.539 (-57.22%)† | 24.573 (+60.76%) |
| [Replacer::replace() · text (EN); 22.03 KiB; 48 keys; 51 replacements; output 22.09 KiB](inputs/cases/document.xmlrpclib.replace.json) | `preg_replace_callback() [prefix]` 114.586 | 57.610 (-49.72%) | 75.972 (-33.70%) |
| [Replacer::replace() · text (EN); 6.43 KiB; 48 keys; 55 replacements; output 6.49 KiB](inputs/cases/document.thread.replace.json) | `preg_replace_callback() [prefix]` 26.811† | 13.626 (-49.18%)† | 31.551 (+17.68%)† |
| [Replacer::replace() · text (EN); 4.45 KiB; 48 keys; 17 replacements; output 4.39 KiB](inputs/cases/document.simplehttpserver.replace.json) | `preg_replace_callback() [prefix]` 15.741† | 8.036 (-48.95%)† | 25.615 (+62.72%)† |
| [Replacer::replace() · text (EN); 21.98 KiB; 48 keys; 52 replacements; output 22.02 KiB](inputs/cases/document.socketserver.replace.json) | `preg_replace_callback() [prefix]` 120.251 | 59.987 (-50.12%) | 77.730 (-35.36%) |
| [Replacer::replace() · text (EN); 6.87 KiB; 48 keys; 43 replacements; output 6.88 KiB](inputs/cases/document.queue.replace.json) | `preg_replace_callback() [prefix]` 25.388 | 13.534 (-46.69%) | 31.645 (+24.64%) |
| [Replacer::replace() · text (EN); 10.16 KiB; 48 keys; 18 replacements; output 10.11 KiB](inputs/cases/document.basehttpserver.replace.json) | `preg_replace_callback() [prefix]` 46.774 | 24.352 (-47.94%) | 41.902 (-10.42%) |
| [Replacer::replace() · text (EN); 40.48 KiB; 48 keys; 10 replacements; output 40.5 KiB](inputs/cases/document.collections.replace.json) | `preg_replace_callback() [prefix]` 225.173 | 118.071 (-47.56%) | 136.365 (-39.44%) |
| [Replacer::replace() · text (EN); 2.14 KiB; 48 keys; 6 replacements; output 2.18 KiB](inputs/cases/document.robotparser.replace.json) | `preg_replace_callback() [prefix]` 7.271 | 3.136 (-56.87%) | 21.166 (2.9 times slower) |


## Replacer: email templates with changing values

| Input | Best existing method, µs | Prepared, µs | One-shot, µs |
|---|---|---:|---:|
| [Replacer::replace() · HTML template; 15.8 KiB; 3 keys; 6 replacements; output 15.85 KiB](inputs/cases/email.account-deletion.html.json) | `preg_replace_callback() [literal]` 1.515 | — | 23.021 (15.2 times slower) |
| [Replacer::replace() · plain-text template; 445 B; 3 keys; 4 replacements; output 489 B](inputs/cases/email.account-deletion.txt.json) | `str_replace()` 0.371 | — | 1.989 (5.4 times slower) |
| [Replacer::replace() · HTML template; 15.91 KiB; 3 keys; 5 replacements; output 15.99 KiB](inputs/cases/email.email-verification.html.json) | `preg_replace_callback() [prefix]` 1.453 | — | 22.373 (15.4 times slower) |
| [Replacer::replace() · plain-text template; 299 B; 3 keys; 3 replacements; output 324 B](inputs/cases/email.email-verification.txt.json) | `str_replace()` 0.355 | — | 1.782 (5.0 times slower) |
| [Replacer::replace() · HTML template; 15.55 KiB; 2 keys; 6 replacements; output 15.63 KiB](inputs/cases/email.magic-link.html.json) | `preg_replace_callback() [prefix]` 1.472 | — | 21.660 (14.7 times slower) |
| [Replacer::replace() · plain-text template; 266 B; 2 keys; 2 replacements; output 292 B](inputs/cases/email.magic-link.txt.json) | `str_replace()` 0.281 | — | 1.495 (5.3 times slower) |
| [Replacer::replace() · HTML template; 23.3 KiB; 6 keys; 10 replacements; output 23.36 KiB](inputs/cases/email.new-sign-in.html.json) | `preg_replace_callback() [tokens]` 2.411 | — | 34.629 (14.4 times slower) |
| [Replacer::replace() · plain-text template; 521 B; 6 keys; 6 replacements; output 571 B](inputs/cases/email.new-sign-in.txt.json) | `strtr()` 0.659 | — | 2.855 (4.3 times slower) |
| [Replacer::replace() · HTML template; 13.43 KiB; 2 keys; 6 replacements; output 13.42 KiB](inputs/cases/email.one-time-code.html.json) | `preg_replace_callback() [literal]` 1.451 | — | 18.180 (12.5 times slower) |
| [Replacer::replace() · plain-text template; 352 B; 2 keys; 2 replacements; output 346 B](inputs/cases/email.one-time-code.txt.json) | `str_replace()` 0.280 | — | 1.522 (5.4 times slower) |
| [Replacer::replace() · HTML template; 15.97 KiB; 3 keys; 7 replacements; output 16.04 KiB](inputs/cases/email.password-reset.html.json) | `preg_replace_callback() [literal]` 1.807 | — | 23.674 (13.1 times slower) |
| [Replacer::replace() · plain-text template; 345 B; 3 keys; 3 replacements; output 370 B](inputs/cases/email.password-reset.txt.json) | `str_replace()` 0.355 | — | 1.759 (5.0 times slower) |
| [Replacer::replace() · HTML template; 20.77 KiB; 6 keys; 12 replacements; output 20.85 KiB](inputs/cases/email.payment-failed.html.json) | `preg_replace_callback() [tokens]` 2.453 | — | 30.834 (12.6 times slower) |
| [Replacer::replace() · plain-text template; 495 B; 6 keys; 8 replacements; output 550 B](inputs/cases/email.payment-failed.txt.json) | `strtr()` 0.657 | — | 2.692 (4.1 times slower) |
| [Replacer::replace() · HTML template; 28.31 KiB; 10 keys; 15 replacements; output 28.36 KiB](inputs/cases/email.receipt.html.json) | `preg_replace_callback() [prefix]` 3.046 | — | 40.266 (13.2 times slower) |
| [Replacer::replace() · plain-text template; 498 B; 10 keys; 11 replacements; output 542 B](inputs/cases/email.receipt.txt.json) | `strtr()` 0.812 | — | 3.937 (4.8 times slower) |
| [Replacer::replace() · HTML template; 22.37 KiB; 6 keys; 15 replacements; output 22.42 KiB](inputs/cases/email.subscription-renewal.html.json) | `preg_replace_callback() [tokens]` 2.909 | — | 32.214 (11.1 times slower) |
| [Replacer::replace() · plain-text template; 492 B; 6 keys; 9 replacements; output 538 B](inputs/cases/email.subscription-renewal.txt.json) | `strtr()` 0.707 | — | 2.782 (3.9 times slower) |
| [Replacer::replace() · HTML template; 15.79 KiB; 5 keys; 12 replacements; output 15.86 KiB](inputs/cases/email.team-invite.html.json) | `preg_replace_callback() [tokens]` 2.323 | — | 24.153 (10.4 times slower) |
| [Replacer::replace() · plain-text template; 311 B; 5 keys; 6 replacements; output 337 B](inputs/cases/email.team-invite.txt.json) | `strtr()` 0.511 | — | 2.217 (4.3 times slower) |
| [Replacer::replace() · HTML template; 20.94 KiB; 7 keys; 17 replacements; output 21.02 KiB](inputs/cases/email.usage-alert.html.json) | `preg_replace_callback() [tokens]` 2.986 | — | 32.174 (10.8 times slower) |
| [Replacer::replace() · plain-text template; 413 B; 7 keys; 7 replacements; output 466 B](inputs/cases/email.usage-alert.txt.json) | `strtr()` 0.643† | — | 2.930 (4.6 times slower)† |
| [Replacer::replace() · HTML template; 17.23 KiB; 3 keys; 3 replacements; output 17.29 KiB](inputs/cases/email.welcome.html.json) | `preg_replace_callback() [prefix]` 1.260 | — | 26.326 (20.9 times slower) |
| [Replacer::replace() · plain-text template; 537 B; 3 keys; 3 replacements; output 596 B](inputs/cases/email.welcome.txt.json) | `str_replace()` 0.359 | — | 2.008 (5.6 times slower) |


## Reuse across different texts

Batch totals include construction once, all B documents and destruction. Each linked input lists every member.

| Exact batch | Best existing: total µs | Object: total µs |
|---|---|---:|
| [Matcher::matches() · 1 document; 456 B total; 403 keys](inputs/cases/batch.validation.any.b1.json) | `preg_match() [prefix]` 6.610 | 295.954 (44.8 times slower) |
| [Matcher::getMatchedKeywords() · 1 document; 456 B total; 403 keys](inputs/cases/batch.validation.unique.b1.json) | `preg_match_all() [prefix]` 31.455 | 298.619 (9.5 times slower) |
| [Matcher::matches() · 4 different documents; 2.11 KiB total; 403 keys](inputs/cases/batch.validation.any.b4.json) | `preg_match() [prefix]` 28.047 | 301.606 (10.8 times slower)† |
| [Matcher::getMatchedKeywords() · 4 different documents; 2.11 KiB total; 403 keys](inputs/cases/batch.validation.unique.b4.json) | `strtolower() + strpos() loop` 203.957 | 304.377 (+49.24%)† |
| [Matcher::matches() · 16 different documents; 5.23 KiB total; 403 keys](inputs/cases/batch.validation.any.b16.json) | `preg_match() [prefix]` 72.476 | 307.352 (4.2 times slower) |
| [Matcher::getMatchedKeywords() · 16 different documents; 5.23 KiB total; 403 keys](inputs/cases/batch.validation.unique.b16.json) | `strtolower() + strpos() loop` 601.791 | 312.351 (-48.10%) |
| [Matcher::matches() · 64 different documents; 21.09 KiB total; 403 keys](inputs/cases/batch.validation.any.b64.json) | `preg_match() [prefix]` 328.861 | 340.234 (+3.46%) |
| [Matcher::getMatchedKeywords() · 64 different documents; 21.09 KiB total; 403 keys](inputs/cases/batch.validation.unique.b64.json) | `strtolower() + strpos() loop` 2461.223 | 357.304 (-85.48%) |
| [Matcher::getMatchedKeywords() · 1 document; 36.39 KiB total; 48 keys](inputs/cases/batch.references.unique.b1.json) | `strpos() loop` 413.443 | 154.219 (-62.70%) |
| [Matcher::countMatches() · 1 document; 36.39 KiB total; 48 keys](inputs/cases/batch.references.count.b1.json) | `strpos() loop` 449.482 | 150.029 (-66.62%) |
| [Matcher::matchAll() · 1 document; 36.39 KiB total; 48 keys](inputs/cases/batch.references.all.b1.json) | `strpos() loop` 462.594 | 148.757 (-67.84%)† |
| [Replacer::replace() · 1 document; 36.39 KiB total; 48 keys; replacements: 44 total](inputs/cases/batch.rewrite.replace.b1.json) | `preg_replace_callback() [prefix]` 233.945 | 122.920 (-47.46%) |
| [Matcher::getMatchedKeywords() · 4 different documents; 100.15 KiB total; 48 keys](inputs/cases/batch.references.unique.b4.json) | `strpos() loop` 1096.212 | 315.984 (-71.17%) |
| [Matcher::countMatches() · 4 different documents; 100.15 KiB total; 48 keys](inputs/cases/batch.references.count.b4.json) | `strpos() loop` 1169.026 | 308.602 (-73.60%) |
| [Matcher::matchAll() · 4 different documents; 100.15 KiB total; 48 keys](inputs/cases/batch.references.all.b4.json) | `strpos() loop` 1199.981 | 316.252 (-73.65%) |
| [Replacer::replace() · 4 different documents; 100.15 KiB total; 48 keys; replacements: 135 total](inputs/cases/batch.rewrite.replace.b4.json) | `preg_replace_callback() [prefix]` 549.788 | 275.989 (-49.80%) |
| [Matcher::getMatchedKeywords() · 16 different documents; 274.46 KiB total; 48 keys](inputs/cases/batch.references.unique.b16.json) | `strpos() loop` 3233.518 | 898.746 (-72.21%)† |
| [Matcher::countMatches() · 16 different documents; 274.46 KiB total; 48 keys](inputs/cases/batch.references.count.b16.json) | `strpos() loop` 3456.451 | 897.036 (-74.05%)† |
| [Matcher::matchAll() · 16 different documents; 274.46 KiB total; 48 keys](inputs/cases/batch.references.all.b16.json) | `strpos() loop` 3667.411 | 938.867 (-74.40%)† |
| [Replacer::replace() · 16 different documents; 274.46 KiB total; 48 keys; replacements: 796 total](inputs/cases/batch.rewrite.replace.b16.json) | `preg_replace_callback() [prefix]` 1770.753 | 866.177 (-51.08%) |
