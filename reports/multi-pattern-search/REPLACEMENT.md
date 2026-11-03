# Replacement: add links to support terms

Times are microseconds per complete job; lower is better. Bold marks the lowest median per compiler, not a significance test. GCC 15.2 and Clang 21.1 on the same AMD system. PCRE compilation caches are warm in these tables; first requests are [separate](PCRE-FIRST.md). Exact input dictionaries and expected outputs are saved in the [corpus](../../corpus/multi-pattern-scaling/README.md).

A dagger marks a sample span above 10%. [Order and noise controls](CONFIRMATION.md) retain original and repeat measurements, including close comparisons.

`strtr` is the native map function. `PCRE` is longest-first escaped `preg_replace_callback()`. Replacer has the same leftmost-longest, no-rescan policy. Sequential `str_replace()` would change the result and is excluded.

## One help article

### Dictionary preparation included

| Substrings | GCC strtr | GCC PCRE | GCC Replacer | Clang strtr | Clang PCRE | Clang Replacer |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 4.463 | **2.262** | 3.603 | 4.318 | **2.188** | 3.479 |
| 16 | 7.893 | **5.383** | 6.168 | 7.861 | **5.085** | 5.940 |
| 32 | 16.843 | 10.735 | **10.672** | 16.754 | 10.482 | **10.145** |
| 64 | 31.181 | 23.194 | **20.033** | 31.365 | 22.563 | **19.495** |
| 128 | **38.064** | 47.387 | 46.884 | **38.490** | 47.048 | 45.110 |
| 256 | **41.730** | 113.529 | 115.259 | **42.219** | 107.227 | 112.640 |
| 512 | **42.546** | 264.934 | 292.481 | **43.034** | 265.663 | 288.989 |

### Dictionary already prepared

| Substrings | GCC strtr | GCC PCRE | GCC Replacer | Clang strtr | Clang PCRE | Clang Replacer |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 4.464 | **0.713** | 1.144 | 4.300 | **0.692** | 1.066 |
| 16 | 7.945 | 1.997 | **1.208** | 7.873 | 1.975 | **1.178** |
| 32 | 16.772 | 3.813 | **1.307** | 16.761 | 3.837 | **1.282** |
| 64 | 31.144 | 6.925 | **1.390** | 31.370 | 6.902 | **1.389** |
| 128 | 37.992 | 11.006 | **1.464** | 38.437 | 11.898 | **1.491** |
| 256 | 41.684 | 22.734 | **1.545** | 42.231 | 22.063 | **1.580** |
| 512 | 42.519 | 68.420 | **1.595** | 43.006 | 64.761 | **1.639** |

## A publishing job with eight different help articles

### Dictionary preparation included

| Substrings | GCC strtr | GCC PCRE | GCC Replacer | Clang strtr | Clang PCRE | Clang Replacer |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 34.699 | **6.470** | 11.025 | 34.040 | **6.410** | 10.508 |
| 16 | 62.801 | 18.641 | **14.123** | 62.761 | 18.434 | **13.716** |
| 32 | 133.789 | 37.026 | **19.233** | 133.367 | 36.551 | **18.878** |
| 64 | 248.587 | 71.056 | **29.567** | 249.928 | 70.469 | **28.919** |
| 128 | 303.461 | 123.556 | **60.375** | 307.487 | 129.183 | **58.276** |
| 256 | 332.546 | 270.081 | **131.304** | 336.553 | 261.552 | **129.027** |
| 512 | 339.594 | 760.028 | **309.953** | 343.415 | 718.674 | **306.901** |

### Dictionary already prepared

| Substrings | GCC strtr | GCC PCRE | GCC Replacer | Clang strtr | Clang PCRE | Clang Replacer |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 34.559 | **4.860** | 8.501 | 34.043 | **4.860** | 8.020 |
| 16 | 62.690 | 15.187 | **9.005** | 62.443 | 15.211 | **8.855** |
| 32 | 133.674 | 29.754 | **9.704** | 133.171 | 29.894 | **9.635** |
| 64 | 248.619 | 54.564 | **10.259** | 249.846 | 54.636 | **10.439** |
| 128 | 303.345 | 87.042 | **10.964** | 306.968 | 94.062 | **11.567** |
| 256 | 332.189 | 181.095 | **11.352** | 336.792 | 177.347 | **11.705** |
| 512 | 339.313 | 521.449 | **11.880** | 343.148 | 556.088 | **12.254** |

## Input sizes and results

String bytes are UTF-8 lengths; total string bytes sum the dictionary literals, not engine memory.

| Substrings | Input | Bytes per substring | Total literal bytes | Bytes per document | Replacements |
|---:|---|---:|---:|---:|---:|
| 8 | Add support links to a help article | 5–16 | 91 | 397–465 | 0–7 |
| 16 | Add support links to a help article | 5–16 | 179 | 397–465 | 0–9 |
| 32 | Add support links to a help article | 4–20 | 358 | 397–465 | 2–11 |
| 64 | Add support links to a help article | 3–25 | 716 | 397–465 | 5–14 |
| 128 | Add support links to a help article | 3–25 | 1523 | 397–465 | 13–18 |
| 256 | Add support links to a help article | 3–25 | 3365 | 397–465 | 13–18 |
| 512 | Add support links to a help article | 3–25 | 6898 | 397–465 | 13–19 |
