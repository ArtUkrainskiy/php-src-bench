# Replacement: add links to support terms

Times are microseconds per complete job; lower is better. Bold marks the lowest median per compiler, not a significance test. GCC 15.2 and Clang 21.1 on the same AMD system. PCRE compilation caches are warm in these tables; first requests are [separate](PCRE-FIRST.md). Exact input dictionaries and expected outputs are saved in the [corpus](../../corpus/multi-pattern-scaling/README.md).

A dagger marks the one noisy original PCRE cell; its [complete-case confirmation](CONFIRMATION.md) preserves the original and repeat measurements.

`strtr` is the native map function. `PCRE` is longest-first escaped `preg_replace_callback()`. Replacer has the same leftmost-longest, no-rescan policy. Sequential `str_replace()` would change the result and is excluded.

## One help article

### Dictionary preparation included

| Substrings | GCC strtr | GCC PCRE | GCC Replacer | Clang strtr | Clang PCRE | Clang Replacer |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 4.432 | **2.260** | 3.707 | 4.343 | **2.188** | 3.710 |
| 16 | 7.913 | **5.285** | 6.568 | 7.887 | **5.146** | 6.355 |
| 32 | 16.769 | **10.628** | 11.741 | 16.722 | **10.439** | 11.152 |
| 64 | 31.154 | **23.111** | 24.363 | 31.324 | **22.785** | 23.369 |
| 128 | **37.993** | 47.099 | 52.396 | **38.501** | 47.117 | 49.294 |
| 256 | **41.643** | 116.729 | 105.458 | **42.149** | 108.814 | 101.300 |
| 512 | **42.505** | 273.277 | 280.263 | **43.089** | 260.801 | 267.681 |

### Dictionary already prepared

| Substrings | GCC strtr | GCC PCRE | GCC Replacer | Clang strtr | Clang PCRE | Clang Replacer |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 4.449 | **0.701** | 1.257 | 4.263 | **0.699** | 1.357 |
| 16 | 7.878 | 1.988 | **1.335** | 7.902 | 1.990 | **1.407** |
| 32 | 16.793 | 3.814 | **1.462** | 16.776 | 3.818 | **1.502** |
| 64 | 31.114 | 6.938 | **1.606** | 31.261 | 6.887 | **1.633** |
| 128 | 37.987 | 10.983 | **1.786** | 38.414 | 11.881 | **1.778** |
| 256 | 41.586 | 22.755 | **1.852** | 42.097 | 22.092 | **1.873** |
| 512 | 42.540 | 69.161 | **2.079** | 42.954 | 67.445 | **2.005** |

## A publishing job with eight different help articles

### Dictionary preparation included

| Substrings | GCC strtr | GCC PCRE | GCC Replacer | Clang strtr | Clang PCRE | Clang Replacer |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 35.059 | **6.468** | 12.058 | 34.348 | **6.458** | 12.877 |
| 16 | 62.602 | 18.862 | **15.398** | 62.308 | 18.500 | **15.569** |
| 32 | 133.637 | 36.785 | **21.198** | 133.113 | 36.729 | **21.123** |
| 64 | 248.701 | 71.273 | **35.031** | 250.230 | 70.845 | **34.052** |
| 128 | 303.644 | 123.129 | **63.106** | 307.146 | 129.887 | **60.122** |
| 256 | 332.242 | 271.947 | **116.937** | 336.815 | 262.055 | **112.678** |
| 512 | 340.039 | 710.263 | **308.233** | 343.591 | 741.988 | **293.572** |

### Dictionary already prepared

| Substrings | GCC strtr | GCC PCRE | GCC Replacer | Clang strtr | Clang PCRE | Clang Replacer |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 34.634 | **4.839** | 9.433 | 33.810 | **4.924** | 10.309 |
| 16 | 62.790 | 15.178 | **10.134** | 62.679 | 15.223 | **10.693** |
| 32 | 133.691 | 30.309 | **10.996** | 133.045 | 29.910 | **11.363** |
| 64 | 248.610 | 54.646 | **12.133** | 249.861 | 54.566 | **12.345** |
| 128 | 302.936 | 86.735 | **13.453** | 306.588 | 94.085 | **13.567** |
| 256 | 331.712 | 180.085 | **14.137** | 336.576 | 202.324 | **14.358** |
| 512 | 339.351 | 531.474 | **14.936** | 342.755 | 554.760 | **15.214** |

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
