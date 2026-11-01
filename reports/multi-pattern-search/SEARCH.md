# Search: return matching keys, counts or positions

Times are microseconds per complete job; lower is better. Bold marks the lowest median per compiler, not a significance test. GCC 15.2 and Clang 21.1 on the same AMD system. PCRE compilation caches are warm in these tables; first requests are [separate](PCRE-FIRST.md). Exact input dictionaries and expected outputs are saved in the [corpus](../../corpus/multi-pattern-scaling/README.md).

A dagger marks the one noisy original PCRE cell; its [complete-case confirmation](CONFIRMATION.md) preserves the original and repeat measurements.

The same eight commerce help articles are used at every N. `PHP` searches each literal with `strpos()`. `PCRE` searches each literal separately to preserve nested/overlapping matches; this is an exact reference, not a claim of an optimal regex implementation. The number of matched terms grows with the dictionary and is reported below.

## Distinct matching terms

### Dictionary preparation included

| Substrings | GCC PHP | GCC PCRE | GCC Matcher | Clang PHP | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | **1.187** | 2.150 | 3.255 | **1.189** | 2.046 | 3.422 |
| 16 | **2.199** | 3.987 | 5.439 | **2.187** | 3.781 | 5.296 |
| 32 | **3.921** | 7.649 | 9.600 | **3.987** | 7.374 | 9.325 |
| 64 | **7.860** | 14.446 | 21.477 | **8.496** | 14.395 | 20.576 |
| 128 | **15.972** | 28.768 | 48.688 | **16.221** | 28.268 | 46.148 |
| 256 | **32.171** | 60.273 | 109.206 | **32.944** | 60.012 | 105.422 |
| 512 | **62.523** | 135.378 | 305.941 | **63.270** | 132.057 | 292.269 |

### Dictionary already prepared

| Substrings | GCC PHP | GCC PCRE | GCC Matcher | Clang PHP | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 1.184 | 1.488 | **1.149** | **1.176** | 1.463 | 1.343 |
| 16 | 2.160 | 2.737 | **1.228** | 2.283 | 2.827 | **1.429** |
| 32 | 3.907 | 5.238 | **1.356** | 3.968 | 5.272 | **1.542** |
| 64 | 7.909 | 9.853 | **1.569** | 8.181 | 9.868 | **1.732** |
| 128 | 15.961 | 19.092 | **1.886** | 16.301 | 19.088 | **2.055** |
| 256 | 31.978 | 39.282 | **1.958** | 32.852 | 38.661 | **2.112** |
| 512 | 62.095 | 92.959 | **2.110** | 62.293 | 93.300 | **2.292** |

## Count every overlapping occurrence

### Dictionary preparation included

| Substrings | GCC PHP | GCC PCRE | GCC Matcher | Clang PHP | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | **0.959** | 2.394 | 3.177 | **0.985** | 2.294 | 3.135 |
| 16 | **1.817** | 4.490 | 5.586 | **1.883** | 4.299 | 5.136 |
| 32 | **3.323** | 8.518 | 9.527 | **3.418** | 8.201 | 8.987 |
| 64 | **6.747** | 16.733 | 21.080 | **7.107** | 16.288 | 20.223 |
| 128 | **13.938** | 49.666 | 49.716 | **14.840** | 48.466 | 47.015 |
| 256 | **30.319** | 112.761 | 108.260 | **31.460** | 110.994 | 104.518 |
| 512 | **60.930** | 238.069 | 303.777 | **61.878** | 232.903 | 292.738 |

### Dictionary already prepared

| Substrings | GCC PHP | GCC PCRE | GCC Matcher | Clang PHP | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | **0.960** | 1.671 | 1.085 | **0.985** | 1.671 | 1.155 |
| 16 | 1.794 | 3.130 | **1.089** | 1.884 | 3.168 | **1.160** |
| 32 | 3.192 | 5.954 | **1.103** | 3.390 | 5.944 | **1.175** |
| 64 | 6.739 | 11.521 | **1.182** | 7.303 | 11.506 | **1.252** |
| 128 | 13.996 | 37.357 | **1.302** | 14.896 | 37.532 | **1.377** |
| 256 | 30.248 | 89.290 | **1.361** | 30.859 | 89.887 | **1.433** |
| 512 | 60.778 | 192.043 | **1.503** | 61.758 | 191.992 | **1.586** |

## Return every occurrence and byte location

### Dictionary preparation included

| Substrings | GCC PHP | GCC PCRE | GCC Matcher | Clang PHP | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | **1.464** | 3.766 | 3.319 | **1.451** | 3.617 | 3.387 |
| 16 | **2.714** | 7.028 | 5.538 | **2.740** | 6.702 | 5.407 |
| 32 | **5.018** | 13.168 | 9.926 | **5.256** | 12.862 | 9.653 |
| 64 | **9.933** | 24.984 | 21.303 | **10.526** | 24.371 | 20.417 |
| 128 | **19.148** | 66.233 | 49.362 | **19.864** | 64.556 | 46.540 |
| 256 | **35.413** | 137.419 | 105.815 | **35.824** | 133.869 | 102.660 |
| 512 | **66.329** | 275.451 | 304.825 | **67.108** | 268.521 | 292.354 |

### Dictionary already prepared

| Substrings | GCC PHP | GCC PCRE | GCC Matcher | Clang PHP | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 1.457 | 2.840 | **1.215** | 1.467 | 2.828 | **1.397** |
| 16 | 2.711 | 5.234 | **1.322** | 2.798 | 5.217 | **1.514** |
| 32 | 5.008 | 9.827 | **1.510** | 5.249 | 9.825 | **1.710** |
| 64 | 9.921 | 18.269 | **1.911** | 10.563 | 18.309 | **2.058** |
| 128 | 19.186 | 50.710 | **2.264** | 19.805 | 51.319 | **2.514** |
| 256 | 35.367 | 107.636 | **2.318** | 36.416 | 107.333 | **2.536** |
| 512 | 65.857 | 218.943 | **2.481** | 67.481 | 218.991 | **2.698** |

## Input sizes and results

String bytes are UTF-8 lengths; total string bytes sum the dictionary literals, not engine memory.

| Substrings | Input | Bytes per substring | Total literal bytes | Bytes per document | Distinct terms |
|---:|---|---:|---:|---:|---:|
| 8 | Find distinct support terms | 5–16 | 91 | 397–465 | 0–8 |
| 16 | Find distinct support terms | 5–16 | 179 | 397–465 | 0–10 |
| 32 | Find distinct support terms | 4–20 | 358 | 397–465 | 3–12 |
| 64 | Find distinct support terms | 3–25 | 716 | 397–465 | 6–16 |
| 128 | Find distinct support terms | 3–25 | 1523 | 397–465 | 15–21 |
| 256 | Find distinct support terms | 3–25 | 3365 | 397–465 | 15–21 |
| 512 | Find distinct support terms | 3–25 | 6898 | 397–465 | 15–22 |
