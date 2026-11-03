# Search: return matching keys, counts or positions

Times are microseconds per complete job; lower is better. Bold marks the lowest median per compiler, not a significance test. GCC 15.2 and Clang 21.1 on the same AMD system. PCRE compilation caches are warm in these tables; first requests are [separate](PCRE-FIRST.md). Exact input dictionaries and expected outputs are saved in the [corpus](../../corpus/multi-pattern-scaling/README.md).

A dagger marks a sample span above 10%. [Order and noise controls](CONFIRMATION.md) retain original and repeat measurements, including close comparisons.

The same eight commerce help articles are used at every N. `PHP` searches each literal with `strpos()`. `PCRE` searches each literal separately to preserve nested/overlapping matches; this is an exact reference, not a claim of an optimal regex implementation. The number of matched terms grows with the dictionary and is reported below.

## Distinct matching terms

### Dictionary preparation included

| Substrings | GCC PHP | GCC PCRE | GCC Matcher | Clang PHP | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | **1.172** | 2.136 | 3.104 | **1.178** | 2.011 | 3.022 |
| 16 | **2.165** | 3.940 | 5.075 | **2.192** | 3.932 | 4.848 |
| 32 | **3.902** | 7.576 | 10.109 | **4.073** | 7.428 | 9.180 |
| 64 | **7.966** | 14.764 | 20.066 | **8.192** | 14.306 | 19.083 |
| 128 | **16.370** | 28.618 | 47.354 | **16.790** | 27.920 | 46.074 |
| 256 | **31.955** | 60.688 | 134.225 | **32.932** | 59.825 | 129.482 |
| 512 | **61.675** | 134.538 | 362.329 | **63.028** | 131.120 | 348.421 |

### Dictionary already prepared

| Substrings | GCC PHP | GCC PCRE | GCC Matcher | Clang PHP | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 1.212 | 1.551 | **0.906** | 1.185 | 1.520 | **0.941** |
| 16 | 2.183 | 2.762 | **1.109** | 2.230 | 2.720 | **1.098** |
| 32 | 3.925 | 5.274 | **1.195** | 3.996 | 5.304 | **1.195** |
| 64 | 7.850 | 9.763 | **1.332** | 8.393 | 9.921 | **1.344** |
| 128 | 16.051 | 18.958 | **1.546** | 16.414 | 18.994 | **1.612** |
| 256 | 31.938 | 39.566 | **1.582** | 32.505 | 40.055 | **1.632** |
| 512 | 61.891 | 93.074 | **1.670** | 62.470 | 93.350 | **1.722** |

## Count every overlapping occurrence

### Dictionary preparation included

| Substrings | GCC PHP | GCC PCRE | GCC Matcher | Clang PHP | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | **0.959** | 2.365 | 3.045 | **0.996** | 2.257 | 2.887 |
| 16 | **1.799** | 4.479 | 4.878 | **1.872** | 4.259 | 4.679 |
| 32 | **3.195** | 8.322 | 9.030 | **3.415** | 8.202 | 8.658 |
| 64 | **6.760** | 16.394 | 19.337 | **7.257** | 16.479 | 18.662 |
| 128 | **14.250** | 49.375 | 47.142 | **14.357** | 48.732 | 45.894 |
| 256 | **30.313** | 113.576 | 133.896 | **31.261** | 109.740 | 128.693 |
| 512 | **60.819** | 238.058 | 353.678 | **61.660** | 231.790 | 347.195 |

### Dictionary already prepared

| Substrings | GCC PHP | GCC PCRE | GCC Matcher | Clang PHP | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 0.962 | 1.677 | **0.837** | 0.960 | 1.670 | **0.853** |
| 16 | 1.801 | 3.178 | **0.903** | 1.880 | 3.167 | **0.945** |
| 32 | 3.204 | 5.844 | **0.918** | 3.410 | 5.940 | **0.970** |
| 64 | 6.719 | 11.528 | **0.958** | 7.333 | 11.486 | **1.026** |
| 128 | 14.007 | 37.025 | **1.039** | 14.762 | 37.404 | **1.101** |
| 256 | 30.415 | 89.267 | **1.047** | 30.792 | 89.810 | **1.123** |
| 512 | 60.868 | 192.298 | **1.088** | 61.554 | 192.303 | **1.186** |

## Return every occurrence and byte location

### Dictionary preparation included

| Substrings | GCC PHP | GCC PCRE | GCC Matcher | Clang PHP | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | **1.458** | 3.765 | 3.129 | **1.446** | 3.597 | 3.284 |
| 16 | **2.736** | 7.012 | 5.089 | **2.790** | 6.739 | 5.091 |
| 32 | **5.176** | 13.219 | 9.427 | **5.258** | 12.662 | 9.141 |
| 64 | **10.032** | 24.957 | 20.108 | **10.290** | 24.292 | 19.517 |
| 128 | **19.077** | 66.015 | 48.032 | **19.863** | 64.418 | 45.654 |
| 256 | **35.323** | 135.781 | 135.162 | **36.242** | 133.507 | 130.384 |
| 512 | **65.807** | 275.499 | 356.366 | **66.977** | 268.343 | 349.338 |

### Dictionary already prepared

| Substrings | GCC PHP | GCC PCRE | GCC Matcher | Clang PHP | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 1.462 | 2.853 | **0.936** | 1.469 | 2.810 | **1.147** |
| 16 | 2.699 | 5.216 | **1.111** | 2.790 | 5.196 | **1.312** |
| 32 | 5.075 | 9.911 | **1.277** | 5.273 | 9.793 | **1.468** |
| 64 | 9.980 | 18.268 | **1.554** | 10.192 | 18.218 | **1.757** |
| 128 | 19.082 | 50.951 | **1.957** | 19.443 | 51.138 | **2.118** |
| 256 | 35.401 | 107.060 | **1.946** | 36.144 | 108.663 | **2.144** |
| 512 | 65.807 | 219.057 | **2.038** | 67.220 | 218.645 | **2.252** |

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
