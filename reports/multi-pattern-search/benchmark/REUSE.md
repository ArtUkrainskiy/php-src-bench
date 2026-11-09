# Repeated Matcher calls

The whole series constructs one object, processes the same string B times, releases each result and destroys the object. Alternatives make B calls with prepared arguments. This is warm repetition of one string, not a batch of different documents. B=1 is shown in the method tables; here B=4/16/64.

| Compiler | Method / input | Calls per object | Best method: whole series, µs | Matcher: whole series, µs | Change |
|---|---|---:|---|---:|---:|
| clang21 | `matchAll()`; 65536 B; 1024 keys; 16 occurrences | 16 | strpos_all: 230885.285 | 3789.092 | -98.36% |
| gcc15 | `matches()`; 128 B; 128 keys; 0 occurrences | 4 | preg_match_chunks: 12.001 | 52.995 | +340.87% |
| clang21 | `matches()`; 128 B; 128 keys; 0 occurrences | 64 | preg_match_chunks: 190.770 | 59.408 | -68.85% |
| gcc15 | `getMatchedKeywords()`; 4096 B; 128 keys; 4 occurrences | 64 | preg_grouped_unique: 6812.274 | 336.219 | -95.07% |
| clang21 | `matchAll()`; 65536 B; 1024 keys; 16 occurrences | 64 | strpos_all: 923120.159 | 12719.416 | -98.62% |
| clang21 | `matches()`; 128 B; 128 keys; 0 occurrences | 16 | preg_match_chunks: 47.516 | 53.722 | +13.01% |
| gcc15 | `matches()`; 4096 B; 128 keys; 0 occurrences | 16 | preg_match_chunks: 1601.168 | 114.443 | -92.86% |
| gcc15 | `matches()`; 4096 B; 128 keys; 0 occurrences | 64 | preg_match_chunks: 6411.363 | 298.288 | -95.36% |
| gcc15 | `matchAll()`; 65536 B; 1024 keys; 16 occurrences | 4 | strpos_all: 61509.888 | 1556.523 | -97.47% |
| clang21 | `getMatchedKeywords()`; 4096 B; 128 keys; 4 occurrences | 64 | preg_grouped_unique: 6832.655 | 276.194 | -95.95% |
| gcc15 | `matchAll()`; 65536 B; 1024 keys; 16 occurrences | 64 | strpos_all: 982325.648 | 13177.647 | -98.66% |
| gcc15 | `matches()`; 4096 B; 128 keys; 0 occurrences | 4 | preg_match_chunks: 401.108 | 69.068 | -82.73% |
| gcc15 | `getMatchedKeywords()`; 4096 B; 128 keys; 4 occurrences | 16 | preg_grouped_unique: 1702.149 | 125.107 | -92.66% |
| clang21 | `matches()`; 4096 B; 128 keys; 0 occurrences | 64 | preg_match_chunks: 6396.260 | 269.862 | -95.79% |
| gcc15 | `matchAll()`; 65536 B; 1024 keys; 16 occurrences | 16 | strpos_all: 246929.518 | 3884.404 | -98.43% |
| clang21 | `getMatchedKeywords()`; 4096 B; 128 keys; 4 occurrences | 16 | preg_grouped_unique: 1706.092† | 115.408† | -93.25%† |
| clang21 | `matches()`; 4096 B; 128 keys; 0 occurrences | 16 | preg_match_chunks: 1599.645 | 107.011 | -93.32% |
| gcc15 | `matches()`; 128 B; 128 keys; 0 occurrences | 16 | preg_match_chunks: 47.739 | 54.221 | +13.67% |
| clang21 | `getMatchedKeywords()`; 4096 B; 128 keys; 4 occurrences | 4 | preg_grouped_unique: 427.160 | 67.047 | -84.31% |
| clang21 | `matches()`; 4096 B; 128 keys; 0 occurrences | 4 | preg_match_chunks: 400.430 | 66.957 | -83.30% |
| clang21 | `matchAll()`; 65536 B; 1024 keys; 16 occurrences | 4 | strpos_all: 57875.576 | 1556.026 | -97.31% |
| gcc15 | `matches()`; 128 B; 128 keys; 0 occurrences | 64 | preg_match_chunks: 190.158 | 60.238 | -68.34% |
| gcc15 | `getMatchedKeywords()`; 4096 B; 128 keys; 4 occurrences | 4 | preg_grouped_unique: 425.249 | 71.758 | -83.11% |
| clang21 | `matches()`; 128 B; 128 keys; 0 occurrences | 4 | preg_match_chunks: 11.932 | 52.191 | +337.27% |

Time ratios refer to the entire series of B calls. Intermediate B values were not measured; the exact minimum reuse needed to break even is not determined. [Arrays and A/A](data/reuse.json).
