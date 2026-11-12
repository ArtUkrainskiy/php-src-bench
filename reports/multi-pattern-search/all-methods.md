# Every measured value against every existing method

Times per call in µs for the new class and for each existing method that was run on the same texts.
**Bold** is the fastest existing method: the base for the change in the last column and in every other table of the report.
[README.md](README.md) has the summary, [METHOD.md](METHOD.md) how the methods were built and timed.

- **≈** — the method was more than 5 times slower than the fastest in a short check run, so it was not timed in full. The value is that check's estimate.
- **—** — not run for this input.
- **Change against the fastest**: negative = the new class is faster; −50% is twice as fast, −90% ten times. † = noisy value, see [METHOD.md](METHOD.md).
- **too large** — PCRE refused to compile the pattern.
- **in chunks of 512 / 1024**: PCRE with the keys split into several patterns of that many keys, for dictionaries too large for one pattern.
- **second copy**: for `matches()` without case folding two timed methods are the same `str_contains()` loop; the faster of the two counts.
- Replacement methods that are wrong on some texts (`str_replace()`, PCRE in dictionary order, several patterns applied in turn) never compete and are not listed; see [METHOD.md](METHOD.md).

## Random keys

### `matches()`

**8 keys, prepared**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | `str_contains()` loop, second copy, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 8 keys, 128 B, no occurrence | GCC | 0.27 | 0.35 | 0.36 | **0.31** | 0.33 | −14% |
| 8 keys, 128 B, no occurrence | Clang | 0.27 | 0.34 | 0.36 | **0.30** | 0.33 | −11%† |
| 8 keys, 1 KiB, no occurrence | GCC | 1.51 | **1.74** | 1.74 | 1.97 | 2.1 | −13% |
| 8 keys, 1 KiB, no occurrence | Clang | 1.73 | **1.64** | 1.65 | 1.97 | 2.14 | +5.4% |
| 8 keys, 4 KiB, no occurrence | GCC | 5.56 | **6.19** | 6.2 | 7.68 | 8.06 | −10% |
| 8 keys, 4 KiB, no occurrence | Clang | 6.57 | **5.9** | 5.91 | 7.68 | 8.24 | +11% |
| 8 keys, 16 KiB, no occurrence | GCC | 21.9 | **23.8** | 23.8 | 29.7 | 30.8 | −7.8% |
| 8 keys, 16 KiB, no occurrence | Clang | 25.9 | **22.6** | 22.7 | 29.4 | 31.4 | +15% |
| 8 keys, 64 KiB, no occurrence | GCC | 85.5 | **94.2** | 94.4 | 118 | 123 | −9.1% |
| 8 keys, 64 KiB, no occurrence | Clang | 103 | 90 | **89.7** | 119 | 126 | +14% |
| 8 keys, 4 KiB, one occurrence in the last 64 bytes | GCC | 5.47 | 3.74 | **3.74** | 7.49 | 7.92 | +46% |
| 8 keys, 4 KiB, one occurrence in the last 64 bytes | Clang | 6.48 | **3.61** | 3.62 | 7.47 | 8.09 | +80% |
| 8 keys, 64 KiB, one occurrence in the last 64 bytes | GCC | 88.4 | 57.1 | **57.1** | 117 | 121 | +54% |
| 8 keys, 64 KiB, one occurrence in the last 64 bytes | Clang | 105 | 55.3 | **55.2** | 116 | 124 | +89% |
| 8 keys, 128 B, one occurrence in the middle third | GCC | 0.21 | 0.22 | 0.23 | **0.18** | 0.20 | +16% |
| 8 keys, 128 B, one occurrence in the middle third | Clang | 0.20 | 0.22 | 0.23 | **0.18** | 0.20 | +10%† |
| 8 keys, 1 KiB, one occurrence in the middle third | GCC | 0.88 | **0.97** | 0.98 | 1.01 | 1.08 | −9.5% |
| 8 keys, 1 KiB, one occurrence in the middle third | Clang | 0.97 | **0.94** | 0.94 | 1.01 | 1.11 | +3.2% |
| 8 keys, 4 KiB, one occurrence in the middle third | GCC | 2.87 | **3.34** | 3.36 | 3.82 | 4.07 | −14% |
| 8 keys, 4 KiB, one occurrence in the middle third | Clang | 3.36 | **3.23** | 3.23 | 3.8 | 4.17 | +3.8% |
| 8 keys, 16 KiB, one occurrence in the middle third | GCC | 11.1 | **12.8** | 12.8 | 15.1 | 15.8 | −13% |
| 8 keys, 16 KiB, one occurrence in the middle third | Clang | 13.3 | **12.4** | 12.4 | 15 | 16.2 | +7.3% |
| 8 keys, 64 KiB, one occurrence in the middle third | GCC | 41.6 | **50.2** | 50.4 | 57.7 | 60.7 | −17% |
| 8 keys, 64 KiB, one occurrence in the middle third | Clang | 50 | **48.7** | 48.8 | 57.5 | 61.9 | +2.3% |
| 8 keys, 4 KiB, one occurrence in the first 64 bytes | GCC | 0.27 | ≈3.04 | ≈3.04 | 0.12 | **0.12** | +127% |
| 8 keys, 4 KiB, one occurrence in the first 64 bytes | Clang | 0.23 | ≈2.93 | ≈2.97 | 0.12 | **0.12** | +94% |
| 8 keys, 64 KiB, one occurrence in the first 64 bytes | GCC | 0.27 | ≈45.1 | ≈45.7 | 0.11 | **0.11** | +155% |
| 8 keys, 64 KiB, one occurrence in the first 64 bytes | Clang | 0.23 | ≈44 | ≈44.4 | **0.10** | 0.11 | +119% |

**8 keys, one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | `str_contains()` loop, second copy, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 8 keys, 128 B, no occurrence | GCC | 2.65 | **0.42** | 0.44 | 1.12 | ≈17.9 | +531% |
| 8 keys, 128 B, no occurrence | Clang | 2.6 | **0.42** | 0.43 | 1.05 | ≈18.9 | +524% |
| 8 keys, 1 KiB, no occurrence | GCC | 3.91 | **1.81** | 1.83 | 2.78 | ≈19.5 | +116% |
| 8 keys, 1 KiB, no occurrence | Clang | 4.06 | **1.73** | 1.75 | 2.72 | ≈20.7 | +135% |
| 8 keys, 4 KiB, no occurrence | GCC | 7.93 | **6.26** | 6.28 | 8.5 | 25.7 | +27% |
| 8 keys, 4 KiB, no occurrence | Clang | 8.89 | **5.99** | 6.01 | 8.41 | 26.9 | +48% |
| 8 keys, 16 KiB, no occurrence | GCC | 24.4 | 23.8 | **23.8** | 30.5 | 48.5 | +2.1% |
| 8 keys, 16 KiB, no occurrence | Clang | 28.3 | **22.8** | 22.8 | 30.5 | 50.2 | +24% |
| 8 keys, 64 KiB, no occurrence | GCC | 88.4 | 94.6 | **94.6** | 119 | 141 | −6.6% |
| 8 keys, 64 KiB, no occurrence | Clang | 105 | **90** | 90.1 | 120 | 144 | +16% |
| 8 keys, 4 KiB, one occurrence in the last 64 bytes | GCC | 7.88 | **3.81** | 3.84 | 8.3 | ≈25.2 | +106% |
| 8 keys, 4 KiB, one occurrence in the last 64 bytes | Clang | 8.79 | **3.69** | 3.71 | 8.2 | ≈26.4 | +137% |
| 8 keys, 64 KiB, one occurrence in the last 64 bytes | GCC | 90.9 | **57.5** | 57.5 | 118 | 139 | +58% |
| 8 keys, 64 KiB, one occurrence in the last 64 bytes | Clang | 107 | **55.4** | 55.4 | 117 | 143 | +93% |
| 8 keys, 128 B, one occurrence in the middle third | GCC | 2.59 | **0.30** | 0.31 | 0.99 | ≈17.8 | +779% |
| 8 keys, 128 B, one occurrence in the middle third | Clang | 2.55 | **0.29** | 0.31 | 0.92 | ≈18.8 | +772% |
| 8 keys, 1 KiB, one occurrence in the middle third | GCC | 3.27 | **1.05** | 1.06 | 1.82 | ≈18.5 | +212% |
| 8 keys, 1 KiB, one occurrence in the middle third | Clang | 3.29 | **1.01** | 1.04 | 1.74 | ≈19.5 | +223% |
| 8 keys, 4 KiB, one occurrence in the middle third | GCC | 5.25 | **3.42** | 3.45 | 4.64 | ≈21.5 | +54% |
| 8 keys, 4 KiB, one occurrence in the middle third | Clang | 5.68 | **3.32** | 3.34 | 4.55 | ≈22.8 | +71% |
| 8 keys, 16 KiB, one occurrence in the middle third | GCC | 13.6 | **12.9** | 13 | 15.9 | 33.3 | +5.1% |
| 8 keys, 16 KiB, one occurrence in the middle third | Clang | 15.6 | **12.5** | 12.5 | 15.8 | 34.8 | +25% |
| 8 keys, 64 KiB, one occurrence in the middle third | GCC | 44.2 | 50.5 | **50.4** | 58.5 | 78.6 | −12% |
| 8 keys, 64 KiB, one occurrence in the middle third | Clang | 52.2 | **48.8** | 48.9 | 58.2 | 81 | +6.7% |
| 8 keys, 4 KiB, one occurrence in the first 64 bytes | GCC | 2.65 | 3.07 | 3.09 | **0.92** | ≈17.8 | +188% |
| 8 keys, 4 KiB, one occurrence in the first 64 bytes | Clang | 2.56 | 2.99 | 3.01 | **0.87** | ≈18.8 | +200% |
| 8 keys, 64 KiB, one occurrence in the first 64 bytes | GCC | 2.66 | ≈45.9 | ≈46.4 | **0.92** | ≈17.7 | +190%† |
| 8 keys, 64 KiB, one occurrence in the first 64 bytes | Clang | 2.58 | ≈44.6 | ≈45 | **0.85** | ≈18.7 | +204% |

**16 keys, prepared**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | `str_contains()` loop, second copy, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 16 keys, 128 B, no occurrence | GCC | 0.27 | 0.64 | 0.65 | **0.52** | 0.53 | −49% |
| 16 keys, 128 B, no occurrence | Clang | 0.27 | 0.63 | 0.65 | 0.52 | **0.51** | −47% |
| 16 keys, 1 KiB, no occurrence | GCC | 1.51 | 3.51 | 3.53 | 3.51 | **3.36** | −55% |
| 16 keys, 1 KiB, no occurrence | Clang | 1.73 | 3.33 | 3.36 | 3.47 | **3.3** | −48% |
| 16 keys, 4 KiB, no occurrence | GCC | 5.52 | 12.5 | 12.6 | 13 | **12.2** | −55% |
| 16 keys, 4 KiB, no occurrence | Clang | 6.54 | **11.9** | 11.9 | 12.9 | 12.1 | −45% |
| 16 keys, 16 KiB, no occurrence | GCC | 21.4 | 49 | 49 | 51.5 | **48.1** | −55% |
| 16 keys, 16 KiB, no occurrence | Clang | 25.6 | 46.6 | **46.5** | 51.3 | 47.3 | −45% |
| 16 keys, 64 KiB, no occurrence | GCC | 86.6 | 192 | 192 | 195 | **180** | −52% |
| 16 keys, 64 KiB, no occurrence | Clang | 103 | 182 | 182 | 194 | **178** | −42% |
| 16 keys, 4 KiB, one occurrence in the last 64 bytes | GCC | 5.5 | **6.95** | 6.99 | 13.1 | 12.2 | −21% |
| 16 keys, 4 KiB, one occurrence in the last 64 bytes | Clang | 6.48 | **6.62** | 6.66 | 13.1 | 12 | −2.0% |
| 16 keys, 64 KiB, one occurrence in the last 64 bytes | GCC | 85.2 | **107** | 107 | 202 | 183 | −20% |
| 16 keys, 64 KiB, one occurrence in the last 64 bytes | Clang | 102 | **101** | 102 | 201 | 181 | +0.7% |
| 16 keys, 128 B, one occurrence in the middle third | GCC | 0.21 | 0.39 | 0.40 | 0.29 | **0.28** | −26%† |
| 16 keys, 128 B, one occurrence in the middle third | Clang | 0.20 | 0.39 | 0.40 | 0.28 | **0.27** | −28% |
| 16 keys, 1 KiB, one occurrence in the middle third | GCC | 0.88 | 1.89 | 1.9 | 1.81 | **1.73** | −49% |
| 16 keys, 1 KiB, one occurrence in the middle third | Clang | 0.96 | 1.79 | 1.8 | 1.8 | **1.71** | −44% |
| 16 keys, 4 KiB, one occurrence in the middle third | GCC | 2.86 | 6.63 | 6.63 | 6.83 | **6.39** | −55% |
| 16 keys, 4 KiB, one occurrence in the middle third | Clang | 3.37 | **6.3** | 6.31 | 6.81 | 6.32 | −47% |
| 16 keys, 16 KiB, one occurrence in the middle third | GCC | 10.9 | 25.4 | 25.3 | 26.2 | **24.3** | −55% |
| 16 keys, 16 KiB, one occurrence in the middle third | Clang | 12.9 | 24.2 | 24.2 | 26.2 | **23.9** | −46% |
| 16 keys, 64 KiB, one occurrence in the middle third | GCC | 41.4 | 99.8 | 99.8 | 97.8 | **89.6** | −54% |
| 16 keys, 64 KiB, one occurrence in the middle third | Clang | 49.6 | 94.9 | 94.9 | 97.4 | **88.3** | −44% |
| 16 keys, 4 KiB, one occurrence in the first 64 bytes | GCC | 0.27 | ≈6.29 | ≈6.33 | 0.18 | **0.16** | +74% |
| 16 keys, 4 KiB, one occurrence in the first 64 bytes | Clang | 0.23 | ≈5.99 | ≈6.05 | 0.18 | **0.14** | +58% |
| 16 keys, 64 KiB, one occurrence in the first 64 bytes | GCC | 0.27 | ≈93 | ≈93.5 | 0.14 | **0.12** | +115%† |
| 16 keys, 64 KiB, one occurrence in the first 64 bytes | Clang | 0.23 | ≈88.6 | ≈89.2 | 0.13 | **0.12** | +96% |

**16 keys, one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | `str_contains()` loop, second copy, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 16 keys, 128 B, no occurrence | GCC | 4.43 | **0.70** | 0.73 | 1.75 | ≈32.7 | +533% |
| 16 keys, 128 B, no occurrence | Clang | 4.44 | **0.69** | 0.72 | 1.6 | ≈33.8 | +540% |
| 16 keys, 1 KiB, no occurrence | GCC | 5.71 | **3.6** | 3.63 | 4.72 | ≈35.3 | +59% |
| 16 keys, 1 KiB, no occurrence | Clang | 5.86 | **3.41** | 3.46 | 4.57 | ≈37.1 | +72% |
| 16 keys, 4 KiB, no occurrence | GCC | 9.75 | **12.6** | 12.7 | 14.2 | 44.9 | −23% |
| 16 keys, 4 KiB, no occurrence | Clang | 10.7 | 12.1 | **12** | 14.1 | 45.8 | −11% |
| 16 keys, 16 KiB, no occurrence | GCC | 25.7 | 49.1 | **49.1** | 52.8 | 80.3 | −48% |
| 16 keys, 16 KiB, no occurrence | Clang | 29.9 | **46.5** | 46.7 | 52.6 | 81.3 | −36% |
| 16 keys, 64 KiB, no occurrence | GCC | 91.2 | 192 | **192** | 196 | 213 | −53% |
| 16 keys, 64 KiB, no occurrence | Clang | 107 | 183 | **183** | 195 | 211 | −41% |
| 16 keys, 4 KiB, one occurrence in the last 64 bytes | GCC | 9.66 | **7.04** | 7.09 | 14.4 | ≈44 | +37% |
| 16 keys, 4 KiB, one occurrence in the last 64 bytes | Clang | 10.7 | **6.72** | 6.77 | 14.2 | ≈45.5 | +59% |
| 16 keys, 64 KiB, one occurrence in the last 64 bytes | GCC | 89.7 | **107** | 107 | 203 | 215 | −16% |
| 16 keys, 64 KiB, one occurrence in the last 64 bytes | Clang | 107 | **102** | 102 | 203 | 215 | +4.7% |
| 16 keys, 128 B, one occurrence in the middle third | GCC | 4.39 | **0.46** | 0.48 | 1.49 | ≈31.7 | +856% |
| 16 keys, 128 B, one occurrence in the middle third | Clang | 4.35 | **0.45** | 0.47 | 1.36 | ≈33.6 | +859% |
| 16 keys, 1 KiB, one occurrence in the middle third | GCC | 5.09 | **1.97** | 1.99 | 3.02 | ≈33.9 | +159% |
| 16 keys, 1 KiB, one occurrence in the middle third | Clang | 5.1 | **1.87** | 1.91 | 2.88 | ≈36.4 | +173% |
| 16 keys, 4 KiB, one occurrence in the middle third | GCC | 7.06 | **6.7** | 6.75 | 8.07 | ≈38.4 | +5.1%† |
| 16 keys, 4 KiB, one occurrence in the middle third | Clang | 7.49 | **6.4** | 6.43 | 7.91 | ≈39.8 | +17% |
| 16 keys, 16 KiB, one occurrence in the middle third | GCC | 15.1 | **25.4** | 25.5 | 27.5 | 56.5 | −41% |
| 16 keys, 16 KiB, one occurrence in the middle third | Clang | 17.2 | **24.3** | 24.3 | 27.3 | 57.5 | −29% |
| 16 keys, 64 KiB, one occurrence in the middle third | GCC | 45.8 | 99.9 | 100 | **99** | 122 | −54% |
| 16 keys, 64 KiB, one occurrence in the middle third | Clang | 53.7 | **95.2** | 95.2 | 98.5 | 122 | −44% |
| 16 keys, 4 KiB, one occurrence in the first 64 bytes | GCC | 4.43 | 6.3 | 6.33 | **1.38** | ≈31.6 | +221% |
| 16 keys, 4 KiB, one occurrence in the first 64 bytes | Clang | 4.39 | 6.03 | 6.07 | **1.25** | ≈33.5 | +250% |
| 16 keys, 64 KiB, one occurrence in the first 64 bytes | GCC | 4.45 | ≈94.1 | ≈95.1 | **1.34** | ≈32 | +231% |
| 16 keys, 64 KiB, one occurrence in the first 64 bytes | Clang | 4.42 | ≈90.5 | ≈90.9 | **1.2** | ≈33.4 | +266% |

**32 keys, prepared**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | `str_contains()` loop, second copy, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 32 keys, 128 B, no occurrence | GCC | 0.27 | 1.32 | 1.35 | 0.84 | **0.71** | −62% |
| 32 keys, 128 B, no occurrence | Clang | 0.27 | 1.32 | 1.35 | 0.80 | **0.71** | −62% |
| 32 keys, 1 KiB, no occurrence | GCC | 1.52 | 7.71 | 7.74 | 6.16 | **4.74** | −68% |
| 32 keys, 1 KiB, no occurrence | Clang | 1.74 | 7.34 | 7.41 | 5.9 | **4.68** | −63% |
| 32 keys, 4 KiB, no occurrence | GCC | 5.52 | 28 | 28 | 24.5 | **17.8** | −69% |
| 32 keys, 4 KiB, no occurrence | Clang | 6.56 | 26.6 | 26.6 | 23.4 | **17.6** | −63% |
| 32 keys, 16 KiB, no occurrence | GCC | 21.5 | 108 | 108 | 94.7 | **67.8** | −68% |
| 32 keys, 16 KiB, no occurrence | Clang | 25.9 | 103 | 103 | 90.6 | **67** | −61% |
| 32 keys, 64 KiB, no occurrence | GCC | 86.8 | 431 | 432 | 380 | **266** | −67% |
| 32 keys, 64 KiB, no occurrence | Clang | 104 | 411 | 410 | 364 | **263** | −61% |
| 32 keys, 4 KiB, one occurrence in the last 64 bytes | GCC | 5.53 | **13.7** | 13.8 | 23.8 | 17.5 | −60% |
| 32 keys, 4 KiB, one occurrence in the last 64 bytes | Clang | 6.57 | **13.1** | 13.1 | 22.9 | 17.3 | −50% |
| 32 keys, 64 KiB, one occurrence in the last 64 bytes | GCC | 86.2 | **215** | 215 | 388 | 270 | −60% |
| 32 keys, 64 KiB, one occurrence in the last 64 bytes | Clang | 103 | **205** | 205 | 371 | 268 | −50% |
| 32 keys, 128 B, one occurrence in the middle third | GCC | 0.21 | 0.70 | 0.72 | 0.45 | **0.39** | −46% |
| 32 keys, 128 B, one occurrence in the middle third | Clang | 0.19 | 0.70 | 0.71 | 0.43 | **0.39** | −51% |
| 32 keys, 1 KiB, one occurrence in the middle third | GCC | 0.88 | 3.73 | 3.74 | 3.13 | **2.46** | −64% |
| 32 keys, 1 KiB, one occurrence in the middle third | Clang | 0.96 | 3.53 | 3.56 | 2.99 | **2.44** | −61% |
| 32 keys, 4 KiB, one occurrence in the middle third | GCC | 2.93 | 13.3 | 13.3 | 12.5 | **9.36** | −69% |
| 32 keys, 4 KiB, one occurrence in the middle third | Clang | 3.42 | 12.7 | 12.7 | 11.9 | **9.28** | −63% |
| 32 keys, 16 KiB, one occurrence in the middle third | GCC | 10.7 | 51.2 | 51.2 | 47.2 | **34** | −68% |
| 32 keys, 16 KiB, one occurrence in the middle third | Clang | 12.8 | 48.7 | 48.8 | 45.2 | **33.7** | −62% |
| 32 keys, 64 KiB, one occurrence in the middle third | GCC | 43.9 | 201 | 201 | 189 | **134** | −67% |
| 32 keys, 64 KiB, one occurrence in the middle third | Clang | 52.6 | 191 | 191 | 181 | **132** | −60% |
| 32 keys, 4 KiB, one occurrence in the first 64 bytes | GCC | 0.26 | ≈12.5 | ≈12.6 | 0.27 | **0.23** | +15% |
| 32 keys, 4 KiB, one occurrence in the first 64 bytes | Clang | 0.22 | ≈11.9 | ≈12.1 | 0.26 | **0.23** | −4.0% |
| 32 keys, 64 KiB, one occurrence in the first 64 bytes | GCC | 0.27 | ≈192 | ≈193 | 0.29 | **0.18** | +49% |
| 32 keys, 64 KiB, one occurrence in the first 64 bytes | Clang | 0.22 | ≈182 | ≈184 | 0.28 | **0.17** | +27% |

**32 keys, one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | `str_contains()` loop, second copy, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 32 keys, 128 B, no occurrence | GCC | 8.39 | **1.38** | 1.42 | 2.84 | ≈62.1 | +505%† |
| 32 keys, 128 B, no occurrence | Clang | 8.16 | **1.39** | 1.42 | 2.62 | ≈64.2 | +491% |
| 32 keys, 1 KiB, no occurrence | GCC | 9.38 | **7.82** | 7.89 | 8.18 | ≈64.8 | +20% |
| 32 keys, 1 KiB, no occurrence | Clang | 9.54 | **7.43** | 7.55 | 7.68 | ≈68.4 | +28% |
| 32 keys, 4 KiB, no occurrence | GCC | 13.4 | 28.1 | 28.1 | **26.6** | 79.5 | −50% |
| 32 keys, 4 KiB, no occurrence | Clang | 14.4 | 26.7 | 26.8 | **25.2** | 82.1 | −43% |
| 32 keys, 16 KiB, no occurrence | GCC | 29.5 | 108 | 108 | **96.7** | 129 | −69% |
| 32 keys, 16 KiB, no occurrence | Clang | 33.7 | 102 | 103 | **92.4** | 131 | −64% |
| 32 keys, 64 KiB, no occurrence | GCC | 95 | 432 | 432 | 382 | **329** | −71% |
| 32 keys, 64 KiB, no occurrence | Clang | 112 | 410 | 411 | 365 | **328** | −66% |
| 32 keys, 4 KiB, one occurrence in the last 64 bytes | GCC | 13.3 | **13.9** | 14 | 25.8 | ≈77.9 | −3.7% |
| 32 keys, 4 KiB, one occurrence in the last 64 bytes | Clang | 14.3 | **13.2** | 13.3 | 24.7 | ≈80.7 | +8.4% |
| 32 keys, 64 KiB, one occurrence in the last 64 bytes | GCC | 94.3 | 215 | **214** | 391 | 332 | −56% |
| 32 keys, 64 KiB, one occurrence in the last 64 bytes | Clang | 111 | **205** | 206 | 374 | 336 | −46% |
| 32 keys, 128 B, one occurrence in the middle third | GCC | 8.08 | **0.78** | 0.80 | 2.48 | ≈60.8 | +945% |
| 32 keys, 128 B, one occurrence in the middle third | Clang | 8.01 | **0.77** | 0.79 | 2.24 | ≈64.2 | +948% |
| 32 keys, 1 KiB, one occurrence in the middle third | GCC | 8.69 | **3.79** | 3.86 | 5.16 | ≈62.9 | +129% |
| 32 keys, 1 KiB, one occurrence in the middle third | Clang | 8.68 | **3.61** | 3.67 | 4.76 | ≈66.2 | +140% |
| 32 keys, 4 KiB, one occurrence in the middle third | GCC | 10.8 | **13.4** | 13.4 | 14.5 | ≈69.6 | −19% |
| 32 keys, 4 KiB, one occurrence in the middle third | Clang | 11.3 | **12.8** | 12.8 | 13.7 | ≈73.3 | −12% |
| 32 keys, 16 KiB, one occurrence in the middle third | GCC | 18.7 | 51.2 | 51.3 | **49.4** | 95.2 | −62% |
| 32 keys, 16 KiB, one occurrence in the middle third | Clang | 20.6 | 48.9 | 49.2 | **47** | 97.7 | −56% |
| 32 keys, 64 KiB, one occurrence in the middle third | GCC | 51.9 | 201 | 201 | **191** | 195 | −73% |
| 32 keys, 64 KiB, one occurrence in the middle third | Clang | 60.5 | 191 | 192 | **183** | 197 | −67% |
| 32 keys, 4 KiB, one occurrence in the first 64 bytes | GCC | 8.11 | ≈12.9 | ≈13 | **2.3** | ≈60.7 | +255% |
| 32 keys, 4 KiB, one occurrence in the first 64 bytes | Clang | 8.03 | ≈12.2 | ≈12.3 | **2.02** | ≈64.1 | +298% |
| 32 keys, 64 KiB, one occurrence in the first 64 bytes | GCC | 8.1 | ≈195 | ≈197 | **2.33** | ≈60.4 | +250% |
| 32 keys, 64 KiB, one occurrence in the first 64 bytes | Clang | 8.05 | ≈185 | ≈186 | **2.01** | ≈63.1 | +301% |

**128 keys, prepared**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | `str_contains()` loop, second copy, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 128 keys, 128 B, no occurrence | GCC | 0.27 | 5.13 | ≈5.26 | 2.69 | **1.01** | −73% |
| 128 keys, 128 B, no occurrence | Clang | 0.27 | ≈5.41 | ≈5.46 | 2.74 | **1.01** | −73% |
| 128 keys, 1 KiB, no occurrence | GCC | 1.54 | 30.3 | 30.4 | 20.7 | **6.58** | −77% |
| 128 keys, 1 KiB, no occurrence | Clang | 1.77 | 29 | 29.2 | 21.2 | **6.65** | −74% |
| 128 keys, 4 KiB, no occurrence | GCC | 5.65 | 110 | 110 | 82.8 | **25** | −77% |
| 128 keys, 4 KiB, no occurrence | Clang | 6.68 | 106 | 106 | 84.8 | **25.3** | −74% |
| 128 keys, 16 KiB, no occurrence | GCC | 21.9 | 433 | 433 | 329 | **95.2** | −77% |
| 128 keys, 16 KiB, no occurrence | Clang | 26.2 | 415 | 415 | 337 | **96.9** | −73% |
| 128 keys, 64 KiB, no occurrence | GCC | 88.5 | 1,752 | 1,748 | 1,310 | **370** | −76% |
| 128 keys, 64 KiB, no occurrence | Clang | 106 | 1,679 | 1,680 | 1,341 | **376** | −72% |
| 128 keys, 4 KiB, one occurrence in the last 64 bytes | GCC | 5.58 | 57.2 | 57.3 | 81 | **24.3** | −77% |
| 128 keys, 4 KiB, one occurrence in the last 64 bytes | Clang | 6.63 | 54.4 | 54.5 | 83 | **24.7** | −73% |
| 128 keys, 64 KiB, one occurrence in the last 64 bytes | GCC | 87.3 | 895 | 895 | 1,309 | **374** | −77% |
| 128 keys, 64 KiB, one occurrence in the last 64 bytes | Clang | 105 | 854 | 855 | 1,342 | **382** | −73% |
| 128 keys, 128 B, one occurrence in the middle third | GCC | 0.21 | 2.79 | 2.84 | 1.33 | **0.54** | −61% |
| 128 keys, 128 B, one occurrence in the middle third | Clang | 0.19 | 2.81 | 2.85 | 1.34 | **0.54** | −64% |
| 128 keys, 1 KiB, one occurrence in the middle third | GCC | 0.89 | 15.7 | 15.8 | 10.3 | **3.41** | −74% |
| 128 keys, 1 KiB, one occurrence in the middle third | Clang | 0.97 | 15 | 15.1 | 10.5 | **3.48** | −72% |
| 128 keys, 4 KiB, one occurrence in the middle third | GCC | 2.88 | 56.8 | 57 | 40.7 | **12.6** | −77% |
| 128 keys, 4 KiB, one occurrence in the middle third | Clang | 3.37 | 54.2 | 54.4 | 41.7 | **12.9** | −74% |
| 128 keys, 16 KiB, one occurrence in the middle third | GCC | 11.2 | 222 | 222 | 169 | **50.1** | −78% |
| 128 keys, 16 KiB, one occurrence in the middle third | Clang | 13.3 | 212 | 211 | 173 | **51** | −74% |
| 128 keys, 64 KiB, one occurrence in the middle third | GCC | 44.8 | 891 | 889 | 686 | **196** | −77% |
| 128 keys, 64 KiB, one occurrence in the middle third | Clang | 53.9 | 849 | 850 | 702 | **201** | −73% |
| 128 keys, 4 KiB, one occurrence in the first 64 bytes | GCC | 0.27 | ≈55 | ≈55.5 | 0.76 | **0.34** | −20% |
| 128 keys, 4 KiB, one occurrence in the first 64 bytes | Clang | 0.22 | ≈52.6 | ≈53.1 | 0.77 | **0.33** | −34% |
| 128 keys, 64 KiB, one occurrence in the first 64 bytes | GCC | 0.26 | ≈865 | ≈871 | 0.74 | **0.25** | +5.5% |
| 128 keys, 64 KiB, one occurrence in the first 64 bytes | Clang | 0.22 | ≈826 | ≈826 | 0.74 | **0.25** | −13%† |

**128 keys, one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | `str_contains()` loop, second copy, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 128 keys, 128 B, no occurrence | GCC | 30.8 | **5.13** | 5.2 | 9.26 | ≈219 | +500% |
| 128 keys, 128 B, no occurrence | Clang | 30.5 | **5.32** | 5.39 | 8.68 | ≈234 | +473% |
| 128 keys, 1 KiB, no occurrence | GCC | 32.2 | 30.5 | 30.8 | **27.5** | ≈224 | +17% |
| 128 keys, 1 KiB, no occurrence | Clang | 32.1 | 29.3 | 29.5 | **27.3** | ≈237 | +18% |
| 128 keys, 4 KiB, no occurrence | GCC | 36.8 | 110 | 111 | **89.6** | 245 | −59% |
| 128 keys, 4 KiB, no occurrence | Clang | 37.3 | 106 | 106 | **90.8** | 258 | −59% |
| 128 keys, 16 KiB, no occurrence | GCC | 52.9 | 433 | 433 | 336 | **318** | −83% |
| 128 keys, 16 KiB, no occurrence | Clang | 56.9 | 415 | 415 | 343 | **335** | −83% |
| 128 keys, 64 KiB, no occurrence | GCC | 121 | 1,748 | 1,751 | 1,320 | **594** | −80% |
| 128 keys, 64 KiB, no occurrence | Clang | 139 | 1,681 | 1,682 | 1,351 | **616** | −77% |
| 128 keys, 4 KiB, one occurrence in the last 64 bytes | GCC | 36.5 | **57** | 57.5 | 87.6 | 245 | −36% |
| 128 keys, 4 KiB, one occurrence in the last 64 bytes | Clang | 37.2 | **54.5** | 55.1 | 89.2 | 258 | −32% |
| 128 keys, 64 KiB, one occurrence in the last 64 bytes | GCC | 119 | 896 | 896 | 1,318 | **599** | −80% |
| 128 keys, 64 KiB, one occurrence in the last 64 bytes | Clang | 137 | 855 | 855 | 1,348 | **617** | −78% |
| 128 keys, 128 B, one occurrence in the middle third | GCC | 30.7 | **2.85** | 2.91 | 7.99 | ≈218 | +982% |
| 128 keys, 128 B, one occurrence in the middle third | Clang | 30.6 | **2.91** | 2.96 | 7.43 | ≈232 | +959% |
| 128 keys, 1 KiB, one occurrence in the middle third | GCC | 31.6 | **15.8** | 16.1 | 17 | ≈222 | +100% |
| 128 keys, 1 KiB, one occurrence in the middle third | Clang | 31.4 | **15.1** | 15.4 | 16.5 | ≈234 | +108% |
| 128 keys, 4 KiB, one occurrence in the middle third | GCC | 33.7 | 57 | 57.4 | **47.5** | 232 | −29% |
| 128 keys, 4 KiB, one occurrence in the middle third | Clang | 34.1 | 54.4 | 54.9 | **47.7** | ≈244 | −29% |
| 128 keys, 16 KiB, one occurrence in the middle third | GCC | 42.1 | 222 | 222 | **176** | 272 | −76% |
| 128 keys, 16 KiB, one occurrence in the middle third | Clang | 44 | 212 | 212 | **179** | 284 | −75% |
| 128 keys, 64 KiB, one occurrence in the middle third | GCC | 76.6 | 890 | 889 | 693 | **418** | −82% |
| 128 keys, 64 KiB, one occurrence in the middle third | Clang | 84.6 | 850 | 850 | 709 | **436** | −81% |
| 128 keys, 4 KiB, one occurrence in the first 64 bytes | GCC | 30.8 | ≈55.8 | ≈56.4 | **7.4** | ≈218 | +317% |
| 128 keys, 4 KiB, one occurrence in the first 64 bytes | Clang | 30.6 | ≈53.3 | ≈54 | **6.64** | ≈232 | +362%† |
| 128 keys, 64 KiB, one occurrence in the first 64 bytes | GCC | 30.9 | ≈872 | ≈881 | **7.47** | ≈219 | +315% |
| 128 keys, 64 KiB, one occurrence in the first 64 bytes | Clang | 30.5 | ≈835 | ≈841 | **6.61** | ≈231 | +361%† |

**1024 keys, prepared**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | `str_contains()` loop, second copy, µs | PCRE alternation, µs | PCRE alternation in chunks of 1024, µs | PCRE alternation in chunks of 512, µs | PCRE, shared prefixes, µs | PCRE, shared prefixes in chunks of 1024, µs | PCRE, shared prefixes in chunks of 512, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1024 keys, 128 B, no occurrence | GCC | 0.28 | ≈37.8 | ≈38.5 | ≈53.9 | ≈53.6 | ≈40.9 | 1.68 | **1.67** | 2.99 | −84% |
| 1024 keys, 128 B, no occurrence | Clang | 0.28 | ≈39 | ≈39.5 | ≈54.3 | ≈54 | ≈40.3 | 1.61 | **1.61** | 2.98 | −83% |
| 1024 keys, 1 KiB, no occurrence | GCC | 1.56 | ≈226 | ≈228 | ≈480 | ≈476 | ≈352 | **9.33** | 9.34 | 16.9 | −83% |
| 1024 keys, 1 KiB, no occurrence | Clang | 1.79 | ≈217 | ≈218 | ≈500 | ≈494 | ≈373 | **8.88** | 8.92 | 16.9 | −80% |
| 1024 keys, 4 KiB, no occurrence | GCC | 5.67 | ≈834 | ≈841 | ≈1,741 | ≈1,736 | ≈1,175 | 35.2 | **35.1** | 62.4 | −84% |
| 1024 keys, 4 KiB, no occurrence | Clang | 6.76 | ≈792 | ≈802 | ≈1,786 | ≈1,784 | ≈1,272 | **33.3** | 33.3 | 62.8 | −80% |
| 1024 keys, 16 KiB, no occurrence | GCC | 22.3 | ≈3,116 | ≈3,157 | ≈5,844 | ≈5,704 | ≈3,934 | **134** | 134 | 239 | −83% |
| 1024 keys, 16 KiB, no occurrence | Clang | 26.7 | ≈2,980 | ≈3,000 | ≈5,873 | ≈5,910 | ≈4,261 | **127** | 127 | 238 | −79% |
| 1024 keys, 64 KiB, no occurrence | GCC | 88.2 | ≈13,608 | ≈13,569 | ≈26,096 | ≈26,067 | ≈19,859 | 525 | **523** | 929 | −83% |
| 1024 keys, 64 KiB, no occurrence | Clang | 106 | ≈13,009 | ≈13,023 | ≈26,847 | ≈26,792 | ≈19,565 | **496** | 497 | 926 | −79% |
| 1024 keys, 4 KiB, one occurrence in the last 64 bytes | GCC | 5.68 | ≈394 | ≈395 | ≈1,556 | ≈1,560 | ≈1,348 | **34.6** | 34.6 | 61.9 | −84% |
| 1024 keys, 4 KiB, one occurrence in the last 64 bytes | Clang | 6.75 | ≈376 | ≈378 | ≈1,615 | ≈1,629 | ≈1,386 | 32.9 | **32.9** | 62.2 | −79% |
| 1024 keys, 64 KiB, one occurrence in the last 64 bytes | GCC | 87.2 | ≈6,963 | ≈6,981 | ≈22,104 | ≈22,247 | ≈18,286 | **523** | 523 | 912 | −83% |
| 1024 keys, 64 KiB, one occurrence in the last 64 bytes | Clang | 105 | ≈6,644 | ≈6,701 | ≈22,828 | ≈22,797 | ≈18,791 | 497 | **497** | 919 | −79% |
| 1024 keys, 128 B, one occurrence in the middle third | GCC | 0.21 | ≈20.3 | ≈20.5 | ≈22 | ≈21.9 | ≈29.5 | **1.04** | 1.04 | 2.39 | −80%† |
| 1024 keys, 128 B, one occurrence in the middle third | Clang | 0.19 | ≈20.8 | ≈20.8 | ≈21.9 | ≈21.9 | ≈27.3 | **1** | 1.01 | 2.38 | −81% |
| 1024 keys, 1 KiB, one occurrence in the middle third | GCC | 0.90 | ≈114 | ≈115 | ≈173 | ≈172 | ≈225 | 4.99 | **4.98** | 13 | −82% |
| 1024 keys, 1 KiB, one occurrence in the middle third | Clang | 0.99 | ≈110 | ≈110 | ≈176 | ≈174 | ≈230 | **4.78** | 4.78 | 13 | −79% |
| 1024 keys, 4 KiB, one occurrence in the middle third | GCC | 2.96 | ≈410 | ≈410 | ≈825 | ≈807 | ≈1,001 | **17.7** | 17.8 | 47.4 | −83% |
| 1024 keys, 4 KiB, one occurrence in the middle third | Clang | 3.47 | ≈387 | ≈390 | ≈809 | ≈809 | ≈1,078 | **17** | 17 | 46.9 | −80% |
| 1024 keys, 16 KiB, one occurrence in the middle third | GCC | 11.1 | ≈1,662 | ≈1,684 | ≈3,425 | ≈3,448 | ≈3,947 | **68.3** | 68.5 | 179 | −84% |
| 1024 keys, 16 KiB, one occurrence in the middle third | Clang | 13.4 | ≈1,600 | ≈1,619 | ≈3,422 | ≈3,459 | ≈4,063 | **65.1** | 65.3 | 180 | −79% |
| 1024 keys, 64 KiB, one occurrence in the middle third | GCC | 43.6 | ≈7,093 | ≈7,113 | ≈14,001 | ≈13,757 | ≈15,796 | **265** | 265 | 695 | −84% |
| 1024 keys, 64 KiB, one occurrence in the middle third | Clang | 52.6 | ≈6,791 | ≈6,807 | ≈14,612 | ≈14,544 | ≈17,199 | **252** | 252 | 698 | −79% |
| 1024 keys, 4 KiB, one occurrence in the first 64 bytes | GCC | 0.27 | ≈412 | ≈412 | ≈12.9 | ≈12.7 | ≈632 | **0.75** | 0.75 | ≈31.6 | −64% |
| 1024 keys, 4 KiB, one occurrence in the first 64 bytes | Clang | 0.22 | ≈393 | ≈397 | ≈13 | ≈12.8 | ≈625 | **0.72** | 0.72 | ≈31.5 | −70%† |
| 1024 keys, 64 KiB, one occurrence in the first 64 bytes | GCC | 0.26 | ≈6,822 | ≈6,867 | ≈12.8 | ≈12.8 | ≈9,450 | 0.68 | **0.68** | ≈406 | −61% |
| 1024 keys, 64 KiB, one occurrence in the first 64 bytes | Clang | 0.22 | ≈6,551 | ≈6,604 | ≈13.2 | ≈13 | ≈10,399 | 0.66 | **0.65** | ≈404 | −67% |

**1024 keys, one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | `str_contains()` loop, second copy, µs | PCRE alternation, µs | PCRE alternation in chunks of 1024, µs | PCRE alternation in chunks of 512, µs | PCRE, shared prefixes, µs | PCRE, shared prefixes in chunks of 1024, µs | PCRE, shared prefixes in chunks of 512, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1024 keys, 128 B, no occurrence | GCC | 393 | **38** | 38.2 | 103 | 104 | 94.3 | ≈1,836 | ≈1,895 | ≈1,926 | +935% |
| 1024 keys, 128 B, no occurrence | Clang | 382 | **39.4** | 39.5 | 99.7 | 102 | 89.8 | ≈1,919 | ≈1,959 | ≈2,003 | +874% |
| 1024 keys, 1 KiB, no occurrence | GCC | 394 | 229 | **229** | 468 | 468 | 370 | ≈1,821 | ≈1,894 | ≈1,941 | +71% |
| 1024 keys, 1 KiB, no occurrence | Clang | 382 | **219** | 221 | 486 | 488 | 382 | ≈1,938 | ≈1,984 | ≈2,034 | +74% |
| 1024 keys, 4 KiB, no occurrence | GCC | 401 | **832** | 834 | 1,722 | 1,739 | 1,301 | 1,941 | 1,953 | 2,030 | −52% |
| 1024 keys, 4 KiB, no occurrence | Clang | 388 | **796** | 799 | 1,785 | 1,793 | 1,396 | 2,035 | 2,036 | 2,122 | −51% |
| 1024 keys, 16 KiB, no occurrence | GCC | 416 | 3,315 | 3,331 | 6,805 | 6,866 | 4,935 | **2,041** | 2,056 | 2,204 | −80% |
| 1024 keys, 16 KiB, no occurrence | Clang | 413 | 3,181 | 3,185 | 6,888 | 6,976 | 5,402 | **2,111** | 2,131 | 2,288 | −81% |
| 1024 keys, 64 KiB, no occurrence | GCC | 483 | ≈13,645 | ≈13,623 | ≈26,089 | ≈25,835 | ≈20,482 | **2,450** | 2,454 | 2,894 | −80% |
| 1024 keys, 64 KiB, no occurrence | Clang | 490 | ≈13,140 | ≈13,083 | ≈26,774 | ≈26,601 | ≈20,310 | **2,494** | 2,497 | 2,974 | −80% |
| 1024 keys, 4 KiB, one occurrence in the last 64 bytes | GCC | 396 | **421** | 422 | 1,513 | 1,533 | 1,340 | 1,948 | 1,945 | ≈1,998 | −5.8% |
| 1024 keys, 4 KiB, one occurrence in the last 64 bytes | Clang | 388 | **402** | 403 | 1,587 | 1,617 | 1,368 | ≈1,952 | ≈1,986 | ≈2,067 | −3.4% |
| 1024 keys, 64 KiB, one occurrence in the last 64 bytes | GCC | 479 | 6,967 | 7,000 | ≈22,451 | ≈22,081 | ≈18,648 | **2,441** | 2,455 | 2,901 | −80% |
| 1024 keys, 64 KiB, one occurrence in the last 64 bytes | Clang | 492 | 6,701 | 6,709 | ≈22,706 | ≈22,333 | ≈19,126 | **2,484** | 2,505 | 2,986 | −80% |
| 1024 keys, 128 B, one occurrence in the middle third | GCC | 391 | **20.5** | 20.7 | 72.5 | 74.7 | 84.6 | ≈1,831 | ≈1,892 | ≈1,944 | +1805% |
| 1024 keys, 128 B, one occurrence in the middle third | Clang | 383 | 21 | **21** | 70.2 | 72.4 | 81.1 | ≈1,911 | ≈1,959 | ≈2,005 | +1724% |
| 1024 keys, 1 KiB, one occurrence in the middle third | GCC | 389 | **116** | 117 | 230 | 231 | 297 | ≈1,819 | ≈1,884 | ≈1,933 | +234% |
| 1024 keys, 1 KiB, one occurrence in the middle third | Clang | 380 | **111** | 112 | 230 | 230 | 287 | ≈1,917 | ≈1,959 | ≈2,009 | +242% |
| 1024 keys, 4 KiB, one occurrence in the middle third | GCC | 394 | **421** | 423 | 777 | 793 | 1,018 | 1,929 | 1,935 | 2,019 | −6.3% |
| 1024 keys, 4 KiB, one occurrence in the middle third | Clang | 384 | **403** | 406 | 757 | 765 | 1,074 | 1,986 | ≈1,993 | ≈2,075 | −4.9% |
| 1024 keys, 16 KiB, one occurrence in the middle third | GCC | 405 | 1,698 | **1,691** | 3,069 | 3,066 | 3,972 | 1,984 | 1,995 | 2,162 | −76% |
| 1024 keys, 16 KiB, one occurrence in the middle third | Clang | 397 | 1,622 | **1,621** | 3,134 | 3,149 | 4,054 | 2,047 | 2,051 | 2,223 | −76% |
| 1024 keys, 64 KiB, one occurrence in the middle third | GCC | 437 | 6,939 | 6,957 | ≈14,003 | ≈13,760 | ≈15,989 | **2,188** | 2,196 | 2,675 | −80%† |
| 1024 keys, 64 KiB, one occurrence in the middle third | Clang | 440 | 6,668 | 6,662 | ≈14,731 | ≈14,309 | ≈17,985 | **2,233** | 2,239 | 2,741 | −80% |
| 1024 keys, 4 KiB, one occurrence in the first 64 bytes | GCC | 392 | ≈412 | ≈416 | **62.1** | 64 | ≈725 | ≈1,829 | ≈1,882 | ≈1,962 | +531% |
| 1024 keys, 4 KiB, one occurrence in the first 64 bytes | Clang | 381 | ≈393 | ≈398 | **58.6** | 60.5 | ≈720 | ≈1,936 | ≈1,975 | ≈2,039 | +550% |
| 1024 keys, 64 KiB, one occurrence in the first 64 bytes | GCC | 391 | ≈6,880 | ≈6,943 | **62.4** | 64.5 | ≈9,553 | ≈1,830 | ≈1,873 | ≈2,372 | +526% |
| 1024 keys, 64 KiB, one occurrence in the first 64 bytes | Clang | 381 | ≈6,604 | ≈6,670 | **59.5** | 61.4 | ≈10,038 | ≈1,919 | ≈1,971 | ≈2,459 | +540% |

### `getMatchedKeywords()`

**8 keys, prepared**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 8 keys, 128 B, one occurrence in the middle third | GCC | 0.31 | **0.39** | 0.73 | 0.79 | −20% |
| 8 keys, 128 B, one occurrence in the middle third | Clang | 0.31 | **0.38** | 0.71 | 0.76 | −18% |
| 8 keys, 1 KiB, one occurrence in the middle third | GCC | 1.56 | **1.7** | 2.57 | 2.77 | −8.3% |
| 8 keys, 1 KiB, one occurrence in the middle third | Clang | 1.78 | **1.61** | 2.56 | 2.75 | +11% |
| 8 keys, 4 KiB, one occurrence in the middle third | GCC | 5.61 | **5.85** | 8.67 | 9.21 | −4.2% |
| 8 keys, 4 KiB, one occurrence in the middle third | Clang | 6.62 | **5.58** | 8.74 | 9.38 | +19% |
| 8 keys, 16 KiB, one occurrence in the middle third | GCC | 21.6 | **22.5** | 33.3 | 35.1 | −4.4% |
| 8 keys, 16 KiB, one occurrence in the middle third | Clang | 25.7 | **21.5** | 33.5 | 35.6 | +20% |
| 8 keys, 64 KiB, one occurrence in the middle third | GCC | 86.4 | **87.8** | 128 | 134 | −1.9% |
| 8 keys, 64 KiB, one occurrence in the middle third | Clang | 103 | **83.8** | 129 | 136 | +23% |
| 8 keys, 1 KiB, 16 occurrences across the text | GCC | 1.88 | **1.17** | 5.53 | 5.85 | +59% |
| 8 keys, 1 KiB, 16 occurrences across the text | Clang | 2.12 | **1.12** | 5.47 | 5.81 | +88% |
| 8 keys, 4 KiB, 16 occurrences across the text | GCC | 5.56 | **3.34** | 11.7 | 12.4 | +66% |
| 8 keys, 4 KiB, 16 occurrences across the text | Clang | 6.51 | **3.19** | 11.7 | 12.4 | +104% |
| 8 keys, 16 KiB, 16 occurrences across the text | GCC | 20.1 | **11.8** | 36.3 | 38.3 | +69% |
| 8 keys, 16 KiB, 16 occurrences across the text | Clang | 23.9 | **11.3** | 36.6 | 38.8 | +112% |
| 8 keys, 64 KiB, 16 occurrences across the text | GCC | 80.3 | **46.1** | 133 | 139 | +74% |
| 8 keys, 64 KiB, 16 occurrences across the text | Clang | 95.1 | **43.7** | 134 | 141 | +117% |

**8 keys, one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 8 keys, 128 B, one occurrence in the middle third | GCC | 2.72 | **0.47** | 1.59 | ≈18.7 | +476% |
| 8 keys, 128 B, one occurrence in the middle third | Clang | 2.68 | **0.46** | 1.55 | ≈19.6 | +483%† |
| 8 keys, 1 KiB, one occurrence in the middle third | GCC | 3.97 | **1.79** | 3.44 | ≈20.6 | +121% |
| 8 keys, 1 KiB, one occurrence in the middle third | Clang | 4.17 | **1.71** | 3.42 | ≈21.6 | +144% |
| 8 keys, 4 KiB, one occurrence in the middle third | GCC | 8.01 | **5.93** | 9.55 | 27.2 | +35% |
| 8 keys, 4 KiB, one occurrence in the middle third | Clang | 9 | **5.68** | 9.61 | 28.2 | +58% |
| 8 keys, 16 KiB, one occurrence in the middle third | GCC | 24.1 | **22.6** | 34.2 | 53 | +6.7% |
| 8 keys, 16 KiB, one occurrence in the middle third | Clang | 28.1 | **21.5** | 34.4 | 54.5 | +30% |
| 8 keys, 64 KiB, one occurrence in the middle third | GCC | 89.1 | **87.9** | 129 | 152 | +0.9% |
| 8 keys, 64 KiB, one occurrence in the middle third | Clang | 105 | **84** | 130 | 155 | +25% |
| 8 keys, 1 KiB, 16 occurrences across the text | GCC | 4.36 | **1.26** | 6.41 | ≈23.7 | +245% |
| 8 keys, 1 KiB, 16 occurrences across the text | Clang | 4.53 | **1.21** | ≈6.44 | ≈24.9 | +273% |
| 8 keys, 4 KiB, 16 occurrences across the text | GCC | 7.99 | **3.43** | 12.5 | ≈30.3 | +133% |
| 8 keys, 4 KiB, 16 occurrences across the text | Clang | 8.91 | **3.29** | 12.7 | ≈32 | +171% |
| 8 keys, 16 KiB, 16 occurrences across the text | GCC | 22.6 | **12** | 37.3 | 56.4 | +89% |
| 8 keys, 16 KiB, 16 occurrences across the text | Clang | 26.4 | **11.3** | 37.6 | 58.1 | +133% |
| 8 keys, 64 KiB, 16 occurrences across the text | GCC | 84 | **46.4** | 133 | 158 | +81% |
| 8 keys, 64 KiB, 16 occurrences across the text | Clang | 97.7 | **44** | 134 | 160 | +123% |

**16 keys, prepared**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 16 keys, 128 B, one occurrence in the middle third | GCC | 0.31 | **0.71** | 1 | 0.94 | −57% |
| 16 keys, 128 B, one occurrence in the middle third | Clang | 0.31 | **0.70** | 1 | 0.94 | −55% |
| 16 keys, 1 KiB, one occurrence in the middle third | GCC | 1.55 | **3.53** | 4.07 | 3.88 | −56% |
| 16 keys, 1 KiB, one occurrence in the middle third | Clang | 1.79 | **3.35** | 4.13 | 3.89 | −47% |
| 16 keys, 4 KiB, one occurrence in the middle third | GCC | 5.58 | **12.2** | 13.7 | 13 | −54% |
| 16 keys, 4 KiB, one occurrence in the middle third | Clang | 6.58 | **11.6** | 14.1 | 13.1 | −43% |
| 16 keys, 16 KiB, one occurrence in the middle third | GCC | 21.6 | **47.3** | 52.6 | 49.1 | −54% |
| 16 keys, 16 KiB, one occurrence in the middle third | Clang | 25.8 | **45.1** | 54.3 | 49.6 | −43% |
| 16 keys, 64 KiB, one occurrence in the middle third | GCC | 85.8 | **189** | 210 | 194 | −55% |
| 16 keys, 64 KiB, one occurrence in the middle third | Clang | 103 | **180** | 217 | 197 | −43% |
| 16 keys, 1 KiB, 16 occurrences across the text | GCC | 2.12 | **2.6** | 8.23 | 7.72 | −18% |
| 16 keys, 1 KiB, 16 occurrences across the text | Clang | 2.33 | **2.49** | 8.32 | 7.65 | −6.2% |
| 16 keys, 4 KiB, 16 occurrences across the text | GCC | 5.99 | **7.45** | 18.2 | 17.2 | −20% |
| 16 keys, 4 KiB, 16 occurrences across the text | Clang | 6.87 | **7.1** | 18.7 | 17.3 | −3.2% |
| 16 keys, 16 KiB, 16 occurrences across the text | GCC | 21.5 | **26.6** | 58.4 | 54.9 | −20% |
| 16 keys, 16 KiB, 16 occurrences across the text | Clang | 25 | **25.4** | 60.2 | 55.5 | −1.7% |
| 16 keys, 64 KiB, 16 occurrences across the text | GCC | 84.2 | **103** | 210 | 195 | −17% |
| 16 keys, 64 KiB, 16 occurrences across the text | Clang | 98 | **97.4** | 217 | 197 | +0.6% |

**16 keys, one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 16 keys, 128 B, one occurrence in the middle third | GCC | 4.53 | **0.80** | 2.27 | ≈33.4 | +470% |
| 16 keys, 128 B, one occurrence in the middle third | Clang | 4.52 | **0.78** | 2.23 | ≈34.9 | +479% |
| 16 keys, 1 KiB, one occurrence in the middle third | GCC | 5.76 | **3.64** | 5.33 | ≈35.6 | +58% |
| 16 keys, 1 KiB, one occurrence in the middle third | Clang | 5.97 | **3.47** | 5.36 | ≈38 | +72% |
| 16 keys, 4 KiB, one occurrence in the middle third | GCC | 9.82 | **12.3** | 15 | 45.6 | −20% |
| 16 keys, 4 KiB, one occurrence in the middle third | Clang | 10.9 | **11.7** | 15.3 | 47.3 | −7.3% |
| 16 keys, 16 KiB, one occurrence in the middle third | GCC | 26 | **47.5** | 54 | 82 | −45% |
| 16 keys, 16 KiB, one occurrence in the middle third | Clang | 30.1 | **45.1** | 55.4 | 84.1 | −33% |
| 16 keys, 64 KiB, one occurrence in the middle third | GCC | 90.7 | **190** | 211 | 228 | −52% |
| 16 keys, 64 KiB, one occurrence in the middle third | Clang | 107 | **180** | 218 | 230 | −41% |
| 16 keys, 1 KiB, 16 occurrences across the text | GCC | 6.41 | **2.69** | 9.56 | ≈40 | +138% |
| 16 keys, 1 KiB, 16 occurrences across the text | Clang | 6.55 | **2.59** | 9.71 | ≈41.6 | +153% |
| 16 keys, 4 KiB, 16 occurrences across the text | GCC | 10.3 | **7.57** | 19.6 | ≈49.9 | +36% |
| 16 keys, 4 KiB, 16 occurrences across the text | Clang | 11.1 | **7.21** | 20 | ≈51.2 | +54% |
| 16 keys, 16 KiB, 16 occurrences across the text | GCC | 26 | **26.8** | 59.9 | 88.1 | −3.3% |
| 16 keys, 16 KiB, 16 occurrences across the text | Clang | 29.2 | **25.4** | 61.5 | 90.1 | +15% |
| 16 keys, 64 KiB, 16 occurrences across the text | GCC | 89.6 | **103** | 212 | 227 | −13% |
| 16 keys, 64 KiB, 16 occurrences across the text | Clang | 103 | **97.3** | 218 | 231 | +5.2% |

**32 keys, prepared**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 32 keys, 128 B, one occurrence in the middle third | GCC | 0.31 | 1.39 | 1.45 | **1.25** | −76% |
| 32 keys, 128 B, one occurrence in the middle third | Clang | 0.31 | 1.4 | 1.37 | **1.25** | −75% |
| 32 keys, 1 KiB, one occurrence in the middle third | GCC | 1.56 | 7.69 | 6.83 | **5.48** | −71% |
| 32 keys, 1 KiB, one occurrence in the middle third | Clang | 1.79 | 7.3 | 6.53 | **5.57** | −68% |
| 32 keys, 4 KiB, one occurrence in the middle third | GCC | 5.59 | 27.4 | 25 | **18.9** | −70% |
| 32 keys, 4 KiB, one occurrence in the middle third | Clang | 6.62 | 26.1 | 24 | **19.4** | −66% |
| 32 keys, 16 KiB, one occurrence in the middle third | GCC | 21.7 | 106 | 97.8 | **70.6** | −69% |
| 32 keys, 16 KiB, one occurrence in the middle third | Clang | 25.8 | 101 | 93.7 | **72.8** | −65% |
| 32 keys, 64 KiB, one occurrence in the middle third | GCC | 86.7 | 426 | 394 | **282** | −69% |
| 32 keys, 64 KiB, one occurrence in the middle third | Clang | 104 | 404 | 377 | **290** | −64% |
| 32 keys, 1 KiB, 16 occurrences across the text | GCC | 2.14 | **7.13** | 13.4 | 10.1 | −70% |
| 32 keys, 1 KiB, 16 occurrences across the text | Clang | 2.38 | **6.85** | 12.8 | 10.2 | −65% |
| 32 keys, 4 KiB, 16 occurrences across the text | GCC | 6.17 | **22.6** | 31.6 | 24 | −73% |
| 32 keys, 4 KiB, 16 occurrences across the text | Clang | 7.14 | **21.6** | 30.5 | 24.6 | −67% |
| 32 keys, 16 KiB, 16 occurrences across the text | GCC | 22.2 | 84.4 | 106 | **78.3** | −72% |
| 32 keys, 16 KiB, 16 occurrences across the text | Clang | 26 | **80.4** | 102 | 80.8 | −68% |
| 32 keys, 64 KiB, 16 occurrences across the text | GCC | 86.2 | 331 | 399 | **285** | −70% |
| 32 keys, 64 KiB, 16 occurrences across the text | Clang | 102 | 316 | 385 | **295** | −66% |

**32 keys, one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 32 keys, 128 B, one occurrence in the middle third | GCC | 8.26 | **1.49** | 3.52 | ≈62.3 | +454% |
| 32 keys, 128 B, one occurrence in the middle third | Clang | 8.11 | **1.47** | 3.32 | ≈65.1 | +451% |
| 32 keys, 1 KiB, one occurrence in the middle third | GCC | 9.46 | **7.88** | 8.92 | ≈66.2 | +20% |
| 32 keys, 1 KiB, one occurrence in the middle third | Clang | 9.6 | **7.48** | 8.45 | ≈69.9 | +29% |
| 32 keys, 4 KiB, one occurrence in the middle third | GCC | 13.5 | 27.7 | **27.1** | 81.6 | −50% |
| 32 keys, 4 KiB, one occurrence in the middle third | Clang | 14.4 | 26.4 | **25.9** | 84.4 | −44% |
| 32 keys, 16 KiB, one occurrence in the middle third | GCC | 29.7 | 107 | **99.9** | 132 | −70% |
| 32 keys, 16 KiB, one occurrence in the middle third | Clang | 33.7 | 101 | **95.5** | 137 | −65%† |
| 32 keys, 64 KiB, one occurrence in the middle third | GCC | 95.1 | 426 | 396 | **344** | −72% |
| 32 keys, 64 KiB, one occurrence in the middle third | Clang | 111 | 405 | 379 | **355** | −69% |
| 32 keys, 1 KiB, 16 occurrences across the text | GCC | 10.1 | **7.3** | 15.5 | ≈70.6 | +39% |
| 32 keys, 1 KiB, 16 occurrences across the text | Clang | 10.3 | **7** | 14.9 | ≈75.4 | +47% |
| 32 keys, 4 KiB, 16 occurrences across the text | GCC | 14.1 | **22.9** | 33.8 | 86.5 | −38% |
| 32 keys, 4 KiB, 16 occurrences across the text | Clang | 15 | **21.8** | 32.6 | 90 | −31% |
| 32 keys, 16 KiB, 16 occurrences across the text | GCC | 30.2 | **84.6** | 108 | 140 | −64% |
| 32 keys, 16 KiB, 16 occurrences across the text | Clang | 33.9 | **80.7** | 104 | 145 | −58% |
| 32 keys, 64 KiB, 16 occurrences across the text | GCC | 94.4 | **332** | 401 | 348 | −72% |
| 32 keys, 64 KiB, 16 occurrences across the text | Clang | 109 | **315** | 387 | 360 | −65% |

**128 keys, prepared**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 128 keys, 128 B, one occurrence in the middle third | GCC | 0.31 | 5.47 | 4.29 | **1.75** | −82% |
| 128 keys, 128 B, one occurrence in the middle third | Clang | 0.32 | 5.61 | 4.16 | **1.73** | −82% |
| 128 keys, 1 KiB, one occurrence in the middle third | GCC | 1.58 | 30.4 | 23.2 | **7.8** | −80% |
| 128 keys, 1 KiB, one occurrence in the middle third | Clang | 1.81 | 29.2 | 22.5 | **7.95** | −77% |
| 128 keys, 4 KiB, one occurrence in the middle third | GCC | 5.67 | 110 | 88.1 | **27.5** | −79% |
| 128 keys, 4 KiB, one occurrence in the middle third | Clang | 6.74 | 105 | 85.5 | **28.1** | −76% |
| 128 keys, 16 KiB, one occurrence in the middle third | GCC | 22.4 | 436 | 355 | **106** | −79% |
| 128 keys, 16 KiB, one occurrence in the middle third | Clang | 26.5 | 419 | 344 | **109** | −76% |
| 128 keys, 64 KiB, one occurrence in the middle third | GCC | 88.3 | 1,753 | 1,409 | **410** | −78% |
| 128 keys, 64 KiB, one occurrence in the middle third | Clang | 105 | 1,690 | 1,366 | **423** | −75% |
| 128 keys, 1 KiB, 16 occurrences across the text | GCC | 2.23 | 32.4 | 41.9 | **13.4** | −83% |
| 128 keys, 1 KiB, 16 occurrences across the text | Clang | 2.45 | 31.3 | 40.3 | **13.4** | −82% |
| 128 keys, 4 KiB, 16 occurrences across the text | GCC | 6.4 | 108 | 107 | **33.3** | −81% |
| 128 keys, 4 KiB, 16 occurrences across the text | Clang | 7.41 | 103 | 103 | **34** | −78% |
| 128 keys, 16 KiB, 16 occurrences across the text | GCC | 22.7 | 413 | 366 | **110** | −79% |
| 128 keys, 16 KiB, 16 occurrences across the text | Clang | 27 | 396 | 354 | **113** | −76% |
| 128 keys, 64 KiB, 16 occurrences across the text | GCC | 88 | 1,630 | 1,372 | **400** | −78% |
| 128 keys, 64 KiB, 16 occurrences across the text | Clang | 105 | 1,566 | 1,333 | **412** | −75% |

**128 keys, one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 128 keys, 128 B, one occurrence in the middle third | GCC | 31 | **5.55** | 11 | ≈222 | +454% |
| 128 keys, 128 B, one occurrence in the middle third | Clang | 30.8 | **5.71** | 10.2 | ≈238 | +439% |
| 128 keys, 1 KiB, one occurrence in the middle third | GCC | 32.5 | 30.9 | **30** | ≈231 | +8.3% |
| 128 keys, 1 KiB, one occurrence in the middle third | Clang | 32.2 | 29.6 | **28.7** | ≈246 | +12% |
| 128 keys, 4 KiB, one occurrence in the middle third | GCC | 36.7 | 110 | **95.2** | 251 | −62% |
| 128 keys, 4 KiB, one occurrence in the middle third | Clang | 37.4 | 106 | **91.9** | 264 | −59% |
| 128 keys, 16 KiB, one occurrence in the middle third | GCC | 53.4 | 435 | 362 | **331** | −84% |
| 128 keys, 16 KiB, one occurrence in the middle third | Clang | 57.3 | 419 | 351 | **346** | −83% |
| 128 keys, 64 KiB, one occurrence in the middle third | GCC | 120 | 1,756 | 1,413 | **633** | −81% |
| 128 keys, 64 KiB, one occurrence in the middle third | Clang | 137 | 1,688 | 1,372 | **663** | −79% |
| 128 keys, 1 KiB, 16 occurrences across the text | GCC | 33.2 | **32.9** | 48.6 | ≈238 | +1.1% |
| 128 keys, 1 KiB, 16 occurrences across the text | Clang | 33.1 | **31.7** | 46.4 | ≈249 | +4.5%† |
| 128 keys, 4 KiB, 16 occurrences across the text | GCC | 37.6 | **108** | 114 | 256 | −65% |
| 128 keys, 4 KiB, 16 occurrences across the text | Clang | 38.1 | **104** | 110 | 272 | −63% |
| 128 keys, 16 KiB, 16 occurrences across the text | GCC | 53.9 | 412 | 373 | **337** | −84% |
| 128 keys, 16 KiB, 16 occurrences across the text | Clang | 57.6 | 396 | 362 | **352** | −84% |
| 128 keys, 64 KiB, 16 occurrences across the text | GCC | 120 | 1,632 | 1,383 | **626** | −81% |
| 128 keys, 64 KiB, 16 occurrences across the text | Clang | 137 | 1,566 | 1,341 | **653** | −79% |

**1024 keys, prepared**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE alternation in chunks of 1024, µs | PCRE alternation in chunks of 512, µs | PCRE, shared prefixes, µs | PCRE, shared prefixes in chunks of 1024, µs | PCRE, shared prefixes in chunks of 512, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1024 keys, 128 B, one occurrence in the middle third | GCC | 0.32 | ≈40.8 | ≈66.6 | ≈65.7 | ≈48.4 | 2.57 | **2.57** | 4.13 | −88% |
| 1024 keys, 128 B, one occurrence in the middle third | Clang | 0.33 | ≈42.1 | ≈64.2 | ≈64.4 | ≈47.2 | 2.71 | **2.64** | 4.31 | −88% |
| 1024 keys, 1 KiB, one occurrence in the middle third | GCC | 1.62 | ≈230 | ≈504 | ≈504 | ≈361 | **10.9** | 10.9 | 19.5 | −85% |
| 1024 keys, 1 KiB, one occurrence in the middle third | Clang | 1.86 | ≈219 | ≈500 | ≈459 | ≈339 | 11.2 | **11.2** | 19.7 | −83% |
| 1024 keys, 4 KiB, one occurrence in the middle third | GCC | 5.79 | ≈816 | ≈2,118 | ≈2,126 | ≈1,473 | **37.9** | 37.9 | 68.9 | −85% |
| 1024 keys, 4 KiB, one occurrence in the middle third | Clang | 6.9 | ≈780 | ≈2,164 | ≈2,148 | ≈1,476 | **38.6** | 38.6 | 69.1 | −82% |
| 1024 keys, 16 KiB, one occurrence in the middle third | GCC | 22.3 | ≈3,390 | ≈7,302 | ≈7,249 | ≈5,585 | **138** | 139 | 252 | −84% |
| 1024 keys, 16 KiB, one occurrence in the middle third | Clang | 26.7 | ≈3,251 | ≈7,383 | ≈7,521 | ≈5,468 | **141** | 142 | 252 | −81% |
| 1024 keys, 64 KiB, one occurrence in the middle third | GCC | 90.6 | ≈14,479 | ≈29,382 | ≈29,312 | ≈23,987 | 559 | **556** | 1,016 | −84% |
| 1024 keys, 64 KiB, one occurrence in the middle third | Clang | 108 | ≈13,919 | ≈29,514 | ≈29,415 | ≈22,527 | 572 | **572** | 1,019 | −81% |
| 1024 keys, 1 KiB, 16 occurrences across the text | GCC | 2.35 | ≈252 | ≈546 | ≈545 | ≈422 | **19.9** | 20 | 30.2 | −88% |
| 1024 keys, 1 KiB, 16 occurrences across the text | Clang | 2.55 | ≈245 | ≈531 | ≈534 | ≈416 | 20.2 | **20.2** | 30 | −87% |
| 1024 keys, 4 KiB, 16 occurrences across the text | GCC | 6.58 | ≈832 | ≈2,176 | ≈2,182 | ≈1,343 | 47.6 | **47.5** | 80.2 | −86% |
| 1024 keys, 4 KiB, 16 occurrences across the text | Clang | 7.48 | ≈793 | ≈2,130 | ≈2,135 | ≈1,338 | **48.7** | 48.7 | 80.6 | −85% |
| 1024 keys, 16 KiB, 16 occurrences across the text | GCC | 23.3 | ≈3,472 | ≈7,808 | ≈7,611 | ≈5,456 | 155 | **155** | 274 | −85% |
| 1024 keys, 16 KiB, 16 occurrences across the text | Clang | 27 | ≈3,345 | ≈7,183 | ≈7,303 | ≈5,560 | **159** | 159 | 275 | −83% |
| 1024 keys, 64 KiB, 16 occurrences across the text | GCC | 88.5 | ≈14,018 | ≈27,706 | ≈27,878 | ≈21,243 | **567** | 570 | 1,031 | −84% |
| 1024 keys, 64 KiB, 16 occurrences across the text | Clang | 104 | ≈13,446 | ≈26,991 | ≈27,275 | ≈20,761 | **586** | 588 | 1,035 | −82% |

**1024 keys, one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE alternation in chunks of 1024, µs | PCRE alternation in chunks of 512, µs | PCRE, shared prefixes, µs | PCRE, shared prefixes in chunks of 1024, µs | PCRE, shared prefixes in chunks of 512, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1024 keys, 128 B, one occurrence in the middle third | GCC | 396 | **39.9** | 114 | 116 | 97.8 | ≈1,846 | ≈1,913 | ≈1,949 | +892% |
| 1024 keys, 128 B, one occurrence in the middle third | Clang | 387 | **40.8** | 110 | 112 | 95 | ≈1,919 | ≈1,965 | ≈2,001 | +847% |
| 1024 keys, 1 KiB, one occurrence in the middle third | GCC | 396 | **232** | 493 | 499 | 399 | ≈1,842 | ≈1,910 | ≈1,955 | +72% |
| 1024 keys, 1 KiB, one occurrence in the middle third | Clang | 389 | **222** | 490 | 490 | 380 | ≈1,946 | ≈1,994 | ≈2,026 | +76% |
| 1024 keys, 4 KiB, one occurrence in the middle third | GCC | 398 | **834** | 1,775 | 1,782 | 1,319 | 1,938 | 1,955 | 2,031 | −52% |
| 1024 keys, 4 KiB, one occurrence in the middle third | Clang | 391 | **798** | 1,781 | 1,796 | 1,369 | 2,026 | 2,027 | 2,108 | −51% |
| 1024 keys, 16 KiB, one occurrence in the middle third | GCC | 417 | 3,320 | 6,751 | 6,789 | 5,276 | **2,052** | 2,061 | 2,235 | −80% |
| 1024 keys, 16 KiB, one occurrence in the middle third | Clang | 413 | 3,163 | 6,823 | 6,875 | 5,131 | **2,125** | 2,132 | 2,296 | −81% |
| 1024 keys, 64 KiB, one occurrence in the middle third | GCC | 485 | ≈14,528 | ≈29,401 | ≈29,122 | ≈23,551 | **2,482** | 2,490 | 3,001 | −80% |
| 1024 keys, 64 KiB, one occurrence in the middle third | Clang | 494 | ≈13,956 | ≈29,703 | ≈29,380 | ≈22,760 | **2,559** | 2,565 | 3,059 | −81% |
| 1024 keys, 1 KiB, 16 occurrences across the text | GCC | 394 | **250** | 659 | 660 | 472 | ≈1,845 | ≈1,927 | ≈1,966 | +57% |
| 1024 keys, 1 KiB, 16 occurrences across the text | Clang | 384 | **240** | 646 | 652 | 468 | ≈1,957 | ≈2,007 | ≈2,053 | +60% |
| 1024 keys, 4 KiB, 16 occurrences across the text | GCC | 401 | **842** | 1,903 | 1,906 | 1,340 | 1,969 | 1,966 | 2,051 | −53% |
| 1024 keys, 4 KiB, 16 occurrences across the text | Clang | 392 | **806** | 1,865 | 1,873 | 1,327 | 2,042 | 2,048 | 2,127 | −51% |
| 1024 keys, 16 KiB, 16 occurrences across the text | GCC | 418 | 3,366 | 7,209 | 7,217 | 5,191 | **2,077** | 2,082 | 2,267 | −80% |
| 1024 keys, 16 KiB, 16 occurrences across the text | Clang | 412 | 3,239 | 7,090 | 7,075 | 5,383 | **2,143** | 2,154 | 2,329 | −81% |
| 1024 keys, 64 KiB, 16 occurrences across the text | GCC | 484 | ≈14,048 | ≈27,637 | ≈28,074 | ≈21,397 | **2,493** | 2,499 | 2,999 | −81% |
| 1024 keys, 64 KiB, 16 occurrences across the text | Clang | 489 | ≈13,433 | ≈27,413 | ≈27,208 | ≈20,260 | **2,590** | 2,598 | 3,110 | −81% |

### `countMatches()`

**8 keys, prepared**

| Input | Compiler | New class, µs | `strpos()` loop, µs | `substr_count()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 8 keys, 128 B, one occurrence in the middle third | GCC | 0.28 | **0.41** | 0.43 | 0.52 | 0.56 | −32% |
| 8 keys, 128 B, one occurrence in the middle third | Clang | 0.28 | **0.42** | 0.43 | 0.50 | 0.54 | −33% |
| 8 keys, 1 KiB, one occurrence in the middle third | GCC | 1.54 | **1.87** | 1.89 | 2.19 | 2.42 | −18% |
| 8 keys, 1 KiB, one occurrence in the middle third | Clang | 1.76 | **1.79** | 1.8 | 2.19 | 2.38 | −1.7% |
| 8 keys, 4 KiB, one occurrence in the middle third | GCC | 5.57 | **6.22** | 6.23 | 7.78 | 8.57 | −11% |
| 8 keys, 4 KiB, one occurrence in the middle third | Clang | 6.62 | **5.92** | 5.93 | 7.85 | 8.44 | +12% |
| 8 keys, 16 KiB, one occurrence in the middle third | GCC | 21.5 | **23.8** | 23.9 | 30.2 | 33 | −9.6% |
| 8 keys, 16 KiB, one occurrence in the middle third | Clang | 25.7 | **22.7** | 22.7 | 30.4 | 32.3 | +13% |
| 8 keys, 64 KiB, one occurrence in the middle third | GCC | 85.7 | **94.2** | 94.2 | 117 | 127 | −9.2% |
| 8 keys, 64 KiB, one occurrence in the middle third | Clang | 103 | **89.5** | 89.6 | 118 | 125 | +14% |
| 8 keys, 1 KiB, 16 occurrences across the text | GCC | 1.84 | 2.54 | **2.36** | 4.46 | 4.84 | −22% |
| 8 keys, 1 KiB, 16 occurrences across the text | Clang | 2.03 | 2.49 | **2.32** | 4.37 | 4.65 | −13% |
| 8 keys, 4 KiB, 16 occurrences across the text | GCC | 5.87 | 7.06 | **6.9** | 10.1 | 11 | −15% |
| 8 keys, 4 KiB, 16 occurrences across the text | Clang | 6.94 | 6.83 | **6.64** | 10.2 | 10.8 | +4.1% |
| 8 keys, 16 KiB, 16 occurrences across the text | GCC | 21.7 | 24.9 | **24.8** | 32.7 | 35.5 | −12% |
| 8 keys, 16 KiB, 16 occurrences across the text | Clang | 26.2 | 23.8 | **23.6** | 33.1 | 34.8 | +11% |
| 8 keys, 64 KiB, 16 occurrences across the text | GCC | 86.3 | 96.1 | **95.9** | 122 | 133 | −10% |
| 8 keys, 64 KiB, 16 occurrences across the text | Clang | 104 | 91.8 | **91.5** | 125 | 131 | +13% |

**8 keys, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | `substr_count()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 8 keys, 128 B, one occurrence in the middle third | GCC | 2.7 | **0.50** | 0.52 | 1.35 | ≈18.2 | +443% |
| 8 keys, 128 B, one occurrence in the middle third | Clang | 2.67 | **0.50** | 0.52 | 1.3 | ≈19.3 | +434% |
| 8 keys, 1 KiB, one occurrence in the middle third | GCC | 3.96 | **1.96** | 1.97 | 3.05 | ≈20.2 | +101%† |
| 8 keys, 1 KiB, one occurrence in the middle third | Clang | 4.1 | **1.9** | 1.9 | 2.99 | ≈21.2 | +117% |
| 8 keys, 4 KiB, one occurrence in the middle third | GCC | 8 | **6.3** | 6.32 | 8.64 | 26 | +27% |
| 8 keys, 4 KiB, one occurrence in the middle third | Clang | 8.99 | 6.04 | **6.03** | 8.67 | 27.1 | +48% |
| 8 keys, 16 KiB, one occurrence in the middle third | GCC | 24 | **23.9** | 23.9 | 31.1 | 50.8 | +0.5% |
| 8 keys, 16 KiB, one occurrence in the middle third | Clang | 28.1 | **22.8** | 22.9 | 31.3 | 51.2 | +23% |
| 8 keys, 64 KiB, one occurrence in the middle third | GCC | 88.3 | 94.3 | **94.1** | 118 | 145 | −6.4% |
| 8 keys, 64 KiB, one occurrence in the middle third | Clang | 105 | **89.6** | 89.6 | 119 | 144 | +17% |
| 8 keys, 1 KiB, 16 occurrences across the text | GCC | 4.27 | 2.63 | **2.46** | 5.36 | ≈22.6 | +73% |
| 8 keys, 1 KiB, 16 occurrences across the text | Clang | 4.4 | 2.58 | **2.42** | 5.18 | ≈23.4 | +82% |
| 8 keys, 4 KiB, 16 occurrences across the text | GCC | 8.3 | 7.18 | **7.01** | 11 | 28.7 | +18% |
| 8 keys, 4 KiB, 16 occurrences across the text | Clang | 9.33 | 6.91 | **6.75** | 11 | 29.6 | +38% |
| 8 keys, 16 KiB, 16 occurrences across the text | GCC | 24.3 | 25.1 | **24.9** | 33.6 | 53.2 | −2.4% |
| 8 keys, 16 KiB, 16 occurrences across the text | Clang | 28.6 | 23.9 | **23.8** | 34 | 53.7 | +20% |
| 8 keys, 64 KiB, 16 occurrences across the text | GCC | 88.9 | 96.3 | **95.9** | 123 | 151 | −7.5% |
| 8 keys, 64 KiB, 16 occurrences across the text | Clang | 106 | 92.1 | **91.7** | 126 | 150 | +16% |

**16 keys, prepared**

| Input | Compiler | New class, µs | `strpos()` loop, µs | `substr_count()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 16 keys, 128 B, one occurrence in the middle third | GCC | 0.28 | **0.73** | 0.78 | 0.83 | 0.74 | −62% |
| 16 keys, 128 B, one occurrence in the middle third | Clang | 0.28 | 0.76 | 0.79 | 0.80 | **0.71** | −60% |
| 16 keys, 1 KiB, one occurrence in the middle third | GCC | 1.53 | **3.61** | 3.67 | 4 | 3.7 | −58% |
| 16 keys, 1 KiB, one occurrence in the middle third | Clang | 1.75 | **3.47** | 3.5 | 3.89 | 3.54 | −50% |
| 16 keys, 4 KiB, one occurrence in the middle third | GCC | 5.58 | **12.8** | 12.8 | 14.4 | 13.1 | −56% |
| 16 keys, 4 KiB, one occurrence in the middle third | Clang | 6.59 | **12.1** | 12.1 | 14 | 12.6 | −46% |
| 16 keys, 16 KiB, one occurrence in the middle third | GCC | 22.1 | **49.1** | 49.2 | 55.9 | 50.6 | −56% |
| 16 keys, 16 KiB, one occurrence in the middle third | Clang | 26 | **46.6** | 46.7 | 54.3 | 48.4 | −44% |
| 16 keys, 64 KiB, one occurrence in the middle third | GCC | 85.4 | 190 | 191 | 206 | **184** | −53% |
| 16 keys, 64 KiB, one occurrence in the middle third | Clang | 103 | 181 | 181 | 200 | **174** | −41% |
| 16 keys, 1 KiB, 16 occurrences across the text | GCC | 1.83 | 4.67 | **4.54** | 7.43 | 6.6 | −60% |
| 16 keys, 1 KiB, 16 occurrences across the text | Clang | 1.99 | 4.6 | **4.43** | 7.22 | 6.35 | −55% |
| 16 keys, 4 KiB, 16 occurrences across the text | GCC | 5.86 | 13.9 | **13.8** | 18.1 | 16.4 | −58% |
| 16 keys, 4 KiB, 16 occurrences across the text | Clang | 6.7 | 13.4 | **13.2** | 17.7 | 15.7 | −49% |
| 16 keys, 16 KiB, 16 occurrences across the text | GCC | 22.1 | 50.4 | **50.3** | 59.4 | 53.9 | −56% |
| 16 keys, 16 KiB, 16 occurrences across the text | Clang | 25.6 | 47.9 | **47.7** | 57.9 | 51.7 | −46% |
| 16 keys, 64 KiB, 16 occurrences across the text | GCC | 86.2 | **195** | 196 | 221 | 198 | −56% |
| 16 keys, 64 KiB, 16 occurrences across the text | Clang | 101 | 186 | **185** | 215 | 189 | −46% |

**16 keys, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | `substr_count()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 16 keys, 128 B, one occurrence in the middle third | GCC | 4.5 | **0.84** | 0.87 | 2.08 | ≈32.9 | +436% |
| 16 keys, 128 B, one occurrence in the middle third | Clang | 4.5 | **0.84** | 0.87 | 1.94 | ≈34.3 | +436% |
| 16 keys, 1 KiB, one occurrence in the middle third | GCC | 5.8 | **3.73** | 3.77 | 5.28 | ≈35.9 | +54%† |
| 16 keys, 1 KiB, one occurrence in the middle third | Clang | 5.95 | **3.58** | 3.59 | 5.07 | ≈37.8 | +66% |
| 16 keys, 4 KiB, one occurrence in the middle third | GCC | 9.81 | 12.9 | **12.8** | 15.7 | 45.3 | −24% |
| 16 keys, 4 KiB, one occurrence in the middle third | Clang | 10.8 | **12.3** | 12.3 | 15.3 | 47.2 | −12% |
| 16 keys, 16 KiB, one occurrence in the middle third | GCC | 26.2 | **49.4** | 49.5 | 57.1 | 83.2 | −47% |
| 16 keys, 16 KiB, one occurrence in the middle third | Clang | 30.3 | **46.8** | 46.9 | 55.5 | 82.5 | −35% |
| 16 keys, 64 KiB, one occurrence in the middle third | GCC | 90.3 | **191** | 191 | 207 | 217 | −53% |
| 16 keys, 64 KiB, one occurrence in the middle third | Clang | 107 | 182 | **182** | 201 | 209 | −41% |
| 16 keys, 1 KiB, 16 occurrences across the text | GCC | 6.07 | 4.77 | **4.64** | 8.79 | ≈38.7 | +30% |
| 16 keys, 1 KiB, 16 occurrences across the text | Clang | 6.19 | 4.72 | **4.56** | 8.41 | ≈39.9 | +36% |
| 16 keys, 4 KiB, 16 occurrences across the text | GCC | 10.1 | 14.1 | **13.9** | 19.5 | 49 | −27% |
| 16 keys, 4 KiB, 16 occurrences across the text | Clang | 11 | 13.5 | **13.3** | 18.9 | 50.4 | −18% |
| 16 keys, 16 KiB, 16 occurrences across the text | GCC | 26.4 | 50.5 | **50.4** | 60.9 | 86.1 | −47% |
| 16 keys, 16 KiB, 16 occurrences across the text | Clang | 30.1 | 48.1 | **47.9** | 59.2 | 85.7 | −37% |
| 16 keys, 64 KiB, 16 occurrences across the text | GCC | 90.6 | 195 | **195** | 223 | 231 | −54% |
| 16 keys, 64 KiB, 16 occurrences across the text | Clang | 105 | 186 | **186** | 216 | 223 | −43% |

**32 keys, prepared**

| Input | Compiler | New class, µs | `strpos()` loop, µs | `substr_count()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 32 keys, 128 B, one occurrence in the middle third | GCC | 0.28 | 1.44 | 1.54 | 1.2 | **1.01** | −73% |
| 32 keys, 128 B, one occurrence in the middle third | Clang | 0.28 | 1.49 | 1.56 | 1.13 | **0.96** | −71% |
| 32 keys, 1 KiB, one occurrence in the middle third | GCC | 1.53 | 7.95 | 8.06 | 6.49 | **5.11** | −70% |
| 32 keys, 1 KiB, one occurrence in the middle third | Clang | 1.76 | 7.57 | 7.62 | 6.12 | **4.88** | −64% |
| 32 keys, 4 KiB, one occurrence in the middle third | GCC | 5.51 | 28.3 | 28.3 | 24.5 | **18.3** | −70% |
| 32 keys, 4 KiB, one occurrence in the middle third | Clang | 6.6 | 26.9 | 26.8 | 23.1 | **17.4** | −62% |
| 32 keys, 16 KiB, one occurrence in the middle third | GCC | 21.8 | 108 | 108 | 93 | **66.9** | −67% |
| 32 keys, 16 KiB, one occurrence in the middle third | Clang | 26.1 | 103 | 103 | 87.9 | **63.4** | −59% |
| 32 keys, 64 KiB, one occurrence in the middle third | GCC | 89.2 | 434 | 433 | 379 | **268** | −67% |
| 32 keys, 64 KiB, one occurrence in the middle third | Clang | 106 | 413 | 413 | 360 | **255** | −59% |
| 32 keys, 1 KiB, 16 occurrences across the text | GCC | 1.86 | 9.25 | 9.14 | 12.1 | **8.9** | −79% |
| 32 keys, 1 KiB, 16 occurrences across the text | Clang | 2 | 9.03 | 8.86 | 11.6 | **8.37** | −76% |
| 32 keys, 4 KiB, 16 occurrences across the text | GCC | 5.91 | 29.6 | 29.5 | 29.9 | **22.3** | −73% |
| 32 keys, 4 KiB, 16 occurrences across the text | Clang | 6.76 | 28.4 | 28.2 | 28.2 | **21.2** | −68% |
| 32 keys, 16 KiB, 16 occurrences across the text | GCC | 22.1 | 111 | 111 | 103 | **74.3** | −70% |
| 32 keys, 16 KiB, 16 occurrences across the text | Clang | 25.7 | 106 | 106 | 97.1 | **70.4** | −63% |
| 32 keys, 64 KiB, 16 occurrences across the text | GCC | 85.8 | 437 | 436 | 391 | **279** | −69% |
| 32 keys, 64 KiB, 16 occurrences across the text | Clang | 101 | 415 | 415 | 371 | **265** | −62% |

**32 keys, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | `substr_count()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 32 keys, 128 B, one occurrence in the middle third | GCC | 8.15 | **1.53** | 1.63 | 3.27 | ≈60.9 | +431% |
| 32 keys, 128 B, one occurrence in the middle third | Clang | 8.11 | **1.58** | 1.64 | 2.97 | ≈65.1 | +412% |
| 32 keys, 1 KiB, one occurrence in the middle third | GCC | 9.45 | **8.09** | 8.14 | 8.6 | ≈65.3 | +16% |
| 32 keys, 1 KiB, one occurrence in the middle third | Clang | 9.55 | **7.74** | 7.75 | 7.91 | ≈68.4 | +23% |
| 32 keys, 4 KiB, one occurrence in the middle third | GCC | 13.4 | 28.4 | 28.3 | **26.6** | 79.5 | −49% |
| 32 keys, 4 KiB, one occurrence in the middle third | Clang | 14.5 | 27.1 | 27 | **24.9** | 81.7 | −42% |
| 32 keys, 16 KiB, one occurrence in the middle third | GCC | 29.9 | 109 | 108 | **95.2** | 128 | −69% |
| 32 keys, 16 KiB, one occurrence in the middle third | Clang | 34 | 103 | 103 | **89.8** | 128 | −62% |
| 32 keys, 64 KiB, one occurrence in the middle third | GCC | 97.6 | 436 | 435 | 381 | **329** | −70% |
| 32 keys, 64 KiB, one occurrence in the middle third | Clang | 114 | 414 | 413 | 361 | **323** | −64% |
| 32 keys, 1 KiB, 16 occurrences across the text | GCC | 9.79 | 9.49 | **9.33** | 14.3 | ≈70.6 | +4.9% |
| 32 keys, 1 KiB, 16 occurrences across the text | Clang | 9.8 | 9.21 | **9.01** | 13.5 | ≈72.4 | +8.5% |
| 32 keys, 4 KiB, 16 occurrences across the text | GCC | 13.9 | 29.8 | **29.6** | 32.1 | 83.5 | −53% |
| 32 keys, 4 KiB, 16 occurrences across the text | Clang | 14.8 | 28.6 | **28.4** | 30.2 | 85.9 | −48% |
| 32 keys, 16 KiB, 16 occurrences across the text | GCC | 30.1 | 111 | 111 | **105** | 136 | −71% |
| 32 keys, 16 KiB, 16 occurrences across the text | Clang | 33.7 | 106 | 106 | **99.1** | 135 | −66% |
| 32 keys, 64 KiB, 16 occurrences across the text | GCC | 94 | 438 | 435 | 393 | **340** | −72% |
| 32 keys, 64 KiB, 16 occurrences across the text | Clang | 109 | 416 | 414 | 373 | **331** | −67% |

**128 keys, prepared**

| Input | Compiler | New class, µs | `strpos()` loop, µs | `substr_count()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 128 keys, 128 B, one occurrence in the middle third | GCC | 0.28 | 5.55 | 6.05 | 3.89 | **1.5** | −81% |
| 128 keys, 128 B, one occurrence in the middle third | Clang | 0.28 | 5.62 | 6.26 | 3.8 | **1.43** | −80% |
| 128 keys, 1 KiB, one occurrence in the middle third | GCC | 1.55 | 30.9 | 31.6 | 22.2 | **7.55** | −80% |
| 128 keys, 1 KiB, one occurrence in the middle third | Clang | 1.77 | 29.8 | 30.3 | 22.1 | **7.23** | −75% |
| 128 keys, 4 KiB, one occurrence in the middle third | GCC | 5.58 | 111 | 111 | 84.8 | **27.3** | −80% |
| 128 keys, 4 KiB, one occurrence in the middle third | Clang | 6.65 | 107 | 107 | 84.5 | **26.2** | −75% |
| 128 keys, 16 KiB, one occurrence in the middle third | GCC | 21.9 | 427 | 427 | 321 | **100** | −78% |
| 128 keys, 16 KiB, one occurrence in the middle third | Clang | 26.3 | 410 | 410 | 319 | **95.6** | −73% |
| 128 keys, 64 KiB, one occurrence in the middle third | GCC | 87.8 | 1,757 | 1,756 | 1,328 | **405** | −78% |
| 128 keys, 64 KiB, one occurrence in the middle third | Clang | 105 | 1,689 | 1,688 | 1,317 | **385** | −73% |
| 128 keys, 1 KiB, 16 occurrences across the text | GCC | 1.87 | 35 | 35.1 | 39.2 | **12.2** | −85% |
| 128 keys, 1 KiB, 16 occurrences across the text | Clang | 2.05 | 34 | 34.1 | 38.2 | **11.6** | −82% |
| 128 keys, 4 KiB, 16 occurrences across the text | GCC | 5.96 | 115 | 114 | 100 | **31.8** | −81% |
| 128 keys, 4 KiB, 16 occurrences across the text | Clang | 7.05 | 111 | 111 | 98.7 | **30.5** | −77% |
| 128 keys, 16 KiB, 16 occurrences across the text | GCC | 22.2 | 442 | 440 | 354 | **111** | −80% |
| 128 keys, 16 KiB, 16 occurrences across the text | Clang | 26.7 | 427 | 425 | 351 | **107** | −75% |
| 128 keys, 64 KiB, 16 occurrences across the text | GCC | 87.1 | 1,744 | 1,741 | 1,318 | **404** | −78% |
| 128 keys, 64 KiB, 16 occurrences across the text | Clang | 105 | 1,677 | 1,673 | 1,316 | **388** | −73% |

**128 keys, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | `substr_count()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 128 keys, 128 B, one occurrence in the middle third | GCC | 31.1 | **5.71** | 6.13 | 10.9 | ≈221 | +444% |
| 128 keys, 128 B, one occurrence in the middle third | Clang | 30.9 | **5.75** | 6.37 | 9.87 | ≈236 | +435% |
| 128 keys, 1 KiB, one occurrence in the middle third | GCC | 32.5 | 31.2 | 31.8 | **28.9** | ≈229 | +12% |
| 128 keys, 1 KiB, one occurrence in the middle third | Clang | 32.5 | 30.2 | 30.4 | **28.1** | ≈242 | +15% |
| 128 keys, 4 KiB, one occurrence in the middle third | GCC | 36.9 | 111 | 112 | **91.7** | 249 | −60% |
| 128 keys, 4 KiB, one occurrence in the middle third | Clang | 37.4 | 107 | 107 | **90.7** | 261 | −59% |
| 128 keys, 16 KiB, one occurrence in the middle third | GCC | 53.2 | 427 | 427 | 328 | **324** | −84% |
| 128 keys, 16 KiB, one occurrence in the middle third | Clang | 57 | 410 | 410 | **325** | 332 | −82% |
| 128 keys, 64 KiB, one occurrence in the middle third | GCC | 120 | 1,760 | 1,761 | 1,333 | **631** | −81% |
| 128 keys, 64 KiB, one occurrence in the middle third | Clang | 137 | 1,688 | 1,688 | 1,326 | **623** | −78% |
| 128 keys, 1 KiB, 16 occurrences across the text | GCC | 32.6 | 35.3 | **35.2** | 46.3 | ≈231 | −7.4% |
| 128 keys, 1 KiB, 16 occurrences across the text | Clang | 32.7 | 34.4 | **34.2** | 44.4 | ≈248 | −4.1% |
| 128 keys, 4 KiB, 16 occurrences across the text | GCC | 36.9 | 115 | 115 | **108** | 254 | −66% |
| 128 keys, 4 KiB, 16 occurrences across the text | Clang | 37.8 | 111 | 111 | **105** | 267 | −64% |
| 128 keys, 16 KiB, 16 occurrences across the text | GCC | 53.3 | 443 | 440 | 362 | **333** | −84% |
| 128 keys, 16 KiB, 16 occurrences across the text | Clang | 57.9 | 427 | 425 | 358 | **346** | −83% |
| 128 keys, 64 KiB, 16 occurrences across the text | GCC | 119 | 1,745 | 1,739 | 1,328 | **628** | −81% |
| 128 keys, 64 KiB, 16 occurrences across the text | Clang | 137 | 1,679 | 1,677 | 1,324 | **624** | −78% |

**1024 keys, prepared**

| Input | Compiler | New class, µs | `strpos()` loop, µs | `substr_count()` loop, µs | PCRE alternation, µs | PCRE alternation in chunks of 1024, µs | PCRE alternation in chunks of 512, µs | PCRE, shared prefixes, µs | PCRE, shared prefixes in chunks of 1024, µs | PCRE, shared prefixes in chunks of 512, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1024 keys, 128 B, one occurrence in the middle third | GCC | 0.28 | ≈39.9 | ≈43.1 | ≈65 | ≈65.1 | ≈42.6 | **2.23** | 2.23 | 3.64 | −87% |
| 1024 keys, 128 B, one occurrence in the middle third | Clang | 0.29 | ≈41.2 | ≈44.9 | ≈66.9 | ≈66.3 | ≈41.1 | **2.14** | 2.14 | 3.61 | −87% |
| 1024 keys, 1 KiB, one occurrence in the middle third | GCC | 1.57 | ≈233 | ≈236 | ≈449 | ≈454 | ≈324 | 10.5 | **10.5** | 18.5 | −85% |
| 1024 keys, 1 KiB, one occurrence in the middle third | Clang | 1.8 | ≈225 | ≈227 | ≈456 | ≈452 | ≈329 | **9.9** | 9.9 | 18.3 | −82% |
| 1024 keys, 4 KiB, one occurrence in the middle third | GCC | 5.71 | ≈861 | ≈862 | ≈1,828 | ≈1,827 | ≈1,218 | 36.8 | **36.7** | 65.4 | −84% |
| 1024 keys, 4 KiB, one occurrence in the middle third | Clang | 6.78 | ≈826 | ≈827 | ≈1,772 | ≈1,758 | ≈1,236 | **34.9** | 34.9 | 65.2 | −81% |
| 1024 keys, 16 KiB, one occurrence in the middle third | GCC | 22.4 | ≈3,374 | ≈3,355 | ≈6,747 | ≈6,677 | ≈4,878 | **141** | 142 | 251 | −84% |
| 1024 keys, 16 KiB, one occurrence in the middle third | Clang | 26.8 | ≈3,251 | ≈3,234 | ≈6,799 | ≈6,792 | ≈4,646 | **134** | 134 | 250 | −80% |
| 1024 keys, 64 KiB, one occurrence in the middle third | GCC | 89 | ≈14,556 | ≈14,604 | ≈29,926 | ≈29,785 | ≈21,353 | **545** | 546 | 976 | −84% |
| 1024 keys, 64 KiB, one occurrence in the middle third | Clang | 107 | ≈14,114 | ≈14,091 | ≈30,169 | ≈30,120 | ≈21,089 | **521** | 521 | 971 | −80% |
| 1024 keys, 1 KiB, 16 occurrences across the text | GCC | 1.92 | ≈254 | ≈258 | ≈630 | ≈633 | ≈390 | **18.4** | 18.4 | 27.8 | −90% |
| 1024 keys, 1 KiB, 16 occurrences across the text | Clang | 2.08 | ≈247 | ≈247 | ≈655 | ≈645 | ≈378 | 17.5 | **17.4** | 27.3 | −88% |
| 1024 keys, 4 KiB, 16 occurrences across the text | GCC | 6.12 | ≈857 | ≈853 | ≈1,897 | ≈1,886 | ≈1,262 | **45.8** | 45.9 | 76.8 | −87% |
| 1024 keys, 4 KiB, 16 occurrences across the text | Clang | 7.01 | ≈814 | ≈816 | ≈1,855 | ≈1,840 | ≈1,187 | 43.8 | **43.7** | 76 | −84% |
| 1024 keys, 16 KiB, 16 occurrences across the text | GCC | 22.7 | ≈3,468 | ≈3,438 | ≈7,145 | ≈7,077 | ≈4,916 | **148** | 148 | 256 | −85% |
| 1024 keys, 16 KiB, 16 occurrences across the text | Clang | 26.4 | ≈3,343 | ≈3,295 | ≈7,218 | ≈7,127 | ≈4,810 | **140** | 140 | 255 | −81% |
| 1024 keys, 64 KiB, 16 occurrences across the text | GCC | 89.4 | ≈14,441 | ≈14,421 | ≈29,432 | ≈29,180 | ≈21,138 | 560 | **560** | 990 | −84% |
| 1024 keys, 64 KiB, 16 occurrences across the text | Clang | 104 | ≈13,846 | ≈13,981 | ≈29,883 | ≈29,664 | ≈20,434 | **539** | 539 | 986 | −81% |

**1024 keys, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | `substr_count()` loop, µs | PCRE alternation, µs | PCRE alternation in chunks of 1024, µs | PCRE alternation in chunks of 512, µs | PCRE, shared prefixes, µs | PCRE, shared prefixes in chunks of 1024, µs | PCRE, shared prefixes in chunks of 512, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1024 keys, 128 B, one occurrence in the middle third | GCC | 395 | **40.6** | 44.2 | 113 | 115 | 95.9 | ≈1,824 | ≈1,892 | ≈1,929 | +874% |
| 1024 keys, 128 B, one occurrence in the middle third | Clang | 385 | **40.7** | 46.2 | 110 | 112 | 93.1 | ≈1,906 | ≈1,971 | ≈2,001 | +845% |
| 1024 keys, 1 KiB, one occurrence in the middle third | GCC | 394 | **233** | 236 | 476 | 481 | 357 | ≈1,836 | ≈1,902 | ≈1,948 | +70% |
| 1024 keys, 1 KiB, one occurrence in the middle third | Clang | 386 | **222** | 227 | 487 | 487 | 368 | ≈1,935 | ≈2,011 | ≈2,043 | +74% |
| 1024 keys, 4 KiB, one occurrence in the middle third | GCC | 399 | **829** | 832 | 1,724 | 1,724 | 1,242 | 1,946 | 1,960 | 2,027 | −52% |
| 1024 keys, 4 KiB, one occurrence in the middle third | Clang | 389 | **791** | 799 | 1,666 | 1,673 | 1,249 | 2,016 | 2,024 | 2,098 | −51% |
| 1024 keys, 16 KiB, one occurrence in the middle third | GCC | 417 | 3,334 | 3,332 | 6,640 | 6,685 | 4,927 | **2,053** | 2,061 | 2,229 | −80%† |
| 1024 keys, 16 KiB, one occurrence in the middle third | Clang | 412 | 3,189 | 3,202 | 6,708 | 6,778 | 4,789 | **2,116** | 2,118 | 2,295 | −81% |
| 1024 keys, 64 KiB, one occurrence in the middle third | GCC | 483 | ≈14,647 | ≈14,568 | ≈29,972 | ≈29,430 | ≈21,258 | 2,471 | **2,468** | 2,951 | −80% |
| 1024 keys, 64 KiB, one occurrence in the middle third | Clang | 492 | ≈14,099 | ≈14,082 | ≈30,267 | ≈29,729 | ≈20,990 | **2,510** | 2,514 | 3,020 | −80% |
| 1024 keys, 1 KiB, 16 occurrences across the text | GCC | 395 | **254** | 258 | 643 | 652 | 443 | ≈1,841 | ≈1,906 | ≈1,956 | +55% |
| 1024 keys, 1 KiB, 16 occurrences across the text | Clang | 384 | **245** | 247 | 661 | 664 | 428 | ≈1,935 | ≈1,988 | ≈2,032 | +56% |
| 1024 keys, 4 KiB, 16 occurrences across the text | GCC | 400 | **860** | 865 | 1,880 | 1,903 | 1,322 | 1,971 | 1,979 | 2,057 | −54% |
| 1024 keys, 4 KiB, 16 occurrences across the text | Clang | 390 | **824** | 829 | 1,880 | 1,888 | 1,250 | 2,035 | 2,042 | 2,121 | −53% |
| 1024 keys, 16 KiB, 16 occurrences across the text | GCC | 418 | 3,370 | 3,371 | 6,639 | 6,751 | 4,874 | **2,059** | 2,061 | 2,225 | −80% |
| 1024 keys, 16 KiB, 16 occurrences across the text | Clang | 411 | 3,248 | 3,267 | 7,035 | 7,024 | 4,730 | **2,127** | 2,129 | 2,304 | −81% |
| 1024 keys, 64 KiB, 16 occurrences across the text | GCC | 484 | ≈14,389 | ≈14,376 | ≈29,078 | ≈29,258 | ≈21,221 | 2,480 | **2,479** | 2,962 | −81% |
| 1024 keys, 64 KiB, 16 occurrences across the text | Clang | 491 | ≈13,986 | ≈13,965 | ≈29,813 | ≈29,575 | ≈20,591 | 2,546 | **2,542** | 3,037 | −81% |

### `matchAll()`

**8 keys, prepared**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 8 keys, 128 B, one occurrence in the middle third | GCC | 0.33 | **0.46** | 0.74 | 0.81 | −30%† |
| 8 keys, 128 B, one occurrence in the middle third | Clang | 0.33 | **0.46** | 0.70 | 0.75 | −28% |
| 8 keys, 1 KiB, one occurrence in the middle third | GCC | 1.58 | **1.91** | 2.56 | 2.76 | −17% |
| 8 keys, 1 KiB, one occurrence in the middle third | Clang | 1.82 | **1.83** | 2.55 | 2.74 | −0.6% |
| 8 keys, 4 KiB, one occurrence in the middle third | GCC | 5.56 | **6.29** | 8.68 | 9.23 | −12% |
| 8 keys, 4 KiB, one occurrence in the middle third | Clang | 6.65 | **6** | 8.77 | 9.34 | +11% |
| 8 keys, 16 KiB, one occurrence in the middle third | GCC | 21.7 | **23.9** | 32.6 | 34.4 | −9.4% |
| 8 keys, 16 KiB, one occurrence in the middle third | Clang | 26 | **22.8** | 33 | 34.9 | +15% |
| 8 keys, 64 KiB, one occurrence in the middle third | GCC | 85.8 | **94.9** | 131 | 138 | −9.8% |
| 8 keys, 64 KiB, one occurrence in the middle third | Clang | 103 | **90.4** | 132 | 139 | +14% |
| 8 keys, 1 KiB, 16 occurrences across the text | GCC | 2.42 | **3** | 5.82 | 6.26 | −19% |
| 8 keys, 1 KiB, 16 occurrences across the text | Clang | 2.66 | **2.97** | 5.68 | 6 | −10% |
| 8 keys, 4 KiB, 16 occurrences across the text | GCC | 6.53 | **7.57** | 11.9 | 12.6 | −14% |
| 8 keys, 4 KiB, 16 occurrences across the text | Clang | 7.59 | **7.29** | 11.9 | 12.6 | +4.1% |
| 8 keys, 16 KiB, 16 occurrences across the text | GCC | 22.9 | **25.5** | 36.6 | 38.5 | −9.9% |
| 8 keys, 16 KiB, 16 occurrences across the text | Clang | 27.4 | **24.5** | 36.8 | 38.8 | +12% |
| 8 keys, 64 KiB, 16 occurrences across the text | GCC | 88.9 | **97.3** | 135 | 141 | −8.7% |
| 8 keys, 64 KiB, 16 occurrences across the text | Clang | 106 | **93** | 136 | 143 | +14% |

**8 keys, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 8 keys, 128 B, one occurrence in the middle third | GCC | 2.72 | **0.56** | 1.58 | ≈18.7 | +387% |
| 8 keys, 128 B, one occurrence in the middle third | Clang | 2.73 | **0.54** | 1.59 | ≈19.7 | +401% |
| 8 keys, 1 KiB, one occurrence in the middle third | GCC | 3.98 | **2.01** | 3.4 | ≈20.6 | +98% |
| 8 keys, 1 KiB, one occurrence in the middle third | Clang | 4.22 | **1.93** | 3.43 | ≈21.8 | +118% |
| 8 keys, 4 KiB, one occurrence in the middle third | GCC | 8.01 | **6.39** | 9.55 | 27.1 | +25% |
| 8 keys, 4 KiB, one occurrence in the middle third | Clang | 9.1 | **6.12** | 9.63 | 28.2 | +49% |
| 8 keys, 16 KiB, one occurrence in the middle third | GCC | 24.2 | **24** | 33.5 | 52.3 | +0.4% |
| 8 keys, 16 KiB, one occurrence in the middle third | Clang | 28.6 | **22.9** | 33.8 | 53.6 | +24% |
| 8 keys, 64 KiB, one occurrence in the middle third | GCC | 88.6 | **95.1** | 132 | 156 | −6.8% |
| 8 keys, 64 KiB, one occurrence in the middle third | Clang | 106 | **90.7** | 133 | 159 | +16% |
| 8 keys, 1 KiB, 16 occurrences across the text | GCC | 4.92 | **3.08** | 6.74 | ≈24.3 | +59% |
| 8 keys, 1 KiB, 16 occurrences across the text | Clang | 5.19 | **3.12** | 6.59 | ≈25.2 | +66% |
| 8 keys, 4 KiB, 16 occurrences across the text | GCC | 9.02 | **7.64** | 12.8 | 30.8 | +18% |
| 8 keys, 4 KiB, 16 occurrences across the text | Clang | 10.1 | **7.46** | 12.8 | 31.8 | +35% |
| 8 keys, 16 KiB, 16 occurrences across the text | GCC | 25.5 | **25.6** | 37.5 | 56.6 | −0.6% |
| 8 keys, 16 KiB, 16 occurrences across the text | Clang | 29.8 | **24.7** | 37.7 | 58.1 | +21% |
| 8 keys, 64 KiB, 16 occurrences across the text | GCC | 91.8 | **97.5** | 136 | 160 | −5.9% |
| 8 keys, 64 KiB, 16 occurrences across the text | Clang | 109 | **93.3** | 137 | 162 | +16% |

**16 keys, prepared**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 16 keys, 128 B, one occurrence in the middle third | GCC | 0.33 | **0.79** | 1.02 | 0.97 | −58% |
| 16 keys, 128 B, one occurrence in the middle third | Clang | 0.33 | **0.79** | 1.00 | 0.94 | −58% |
| 16 keys, 1 KiB, one occurrence in the middle third | GCC | 1.58 | **3.68** | 4.08 | 3.89 | −57% |
| 16 keys, 1 KiB, one occurrence in the middle third | Clang | 1.81 | **3.54** | 4.14 | 3.88 | −49% |
| 16 keys, 4 KiB, one occurrence in the middle third | GCC | 5.58 | **12.8** | 14 | 13.2 | −56% |
| 16 keys, 4 KiB, one occurrence in the middle third | Clang | 6.65 | **12.1** | 14.4 | 13.3 | −45% |
| 16 keys, 16 KiB, one occurrence in the middle third | GCC | 21.5 | 49.1 | 52.4 | **48.5** | −56% |
| 16 keys, 16 KiB, one occurrence in the middle third | Clang | 26 | **46.6** | 54 | 49.2 | −44% |
| 16 keys, 64 KiB, one occurrence in the middle third | GCC | 86.3 | 193 | 203 | **187** | −54% |
| 16 keys, 64 KiB, one occurrence in the middle third | Clang | 104 | **184** | 209 | 189 | −43% |
| 16 keys, 1 KiB, 16 occurrences across the text | GCC | 2.43 | **5.15** | 8.47 | 8.04 | −53% |
| 16 keys, 1 KiB, 16 occurrences across the text | Clang | 2.66 | **5.1** | 8.46 | 7.77 | −48% |
| 16 keys, 4 KiB, 16 occurrences across the text | GCC | 6.52 | **14.4** | 18.6 | 17.7 | −55% |
| 16 keys, 4 KiB, 16 occurrences across the text | Clang | 7.56 | **13.8** | 18.9 | 17.6 | −45% |
| 16 keys, 16 KiB, 16 occurrences across the text | GCC | 23 | **50.5** | 57.4 | 53.8 | −55% |
| 16 keys, 16 KiB, 16 occurrences across the text | Clang | 27.2 | **48.1** | 58.8 | 54 | −44% |
| 16 keys, 64 KiB, 16 occurrences across the text | GCC | 87.9 | 194 | 207 | **191** | −54% |
| 16 keys, 64 KiB, 16 occurrences across the text | Clang | 105 | **184** | 213 | 193 | −43% |

**16 keys, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 16 keys, 128 B, one occurrence in the middle third | GCC | 4.58 | **0.89** | 2.25 | ≈33.2 | +416% |
| 16 keys, 128 B, one occurrence in the middle third | Clang | 4.57 | **0.87** | 2.31 | ≈35.1 | +417%† |
| 16 keys, 1 KiB, one occurrence in the middle third | GCC | 5.84 | **3.8** | 5.34 | ≈36.3 | +54% |
| 16 keys, 1 KiB, one occurrence in the middle third | Clang | 6.01 | **3.64** | 5.38 | ≈38 | +65% |
| 16 keys, 4 KiB, one occurrence in the middle third | GCC | 9.86 | **12.9** | 15.3 | 46 | −24% |
| 16 keys, 4 KiB, one occurrence in the middle third | Clang | 10.9 | **12.3** | 15.6 | 48 | −11%† |
| 16 keys, 16 KiB, one occurrence in the middle third | GCC | 25.9 | **49.3** | 53.7 | 81.5 | −47% |
| 16 keys, 16 KiB, one occurrence in the middle third | Clang | 30.2 | **46.7** | 55.2 | 83.5 | −35% |
| 16 keys, 64 KiB, one occurrence in the middle third | GCC | 90.9 | **194** | 204 | 220 | −53% |
| 16 keys, 64 KiB, one occurrence in the middle third | Clang | 108 | **184** | 211 | 223 | −41% |
| 16 keys, 1 KiB, 16 occurrences across the text | GCC | 6.76 | **5.27** | 9.79 | ≈41 | +28%† |
| 16 keys, 1 KiB, 16 occurrences across the text | Clang | 6.93 | **5.26** | 9.83 | ≈42.4 | +32% |
| 16 keys, 4 KiB, 16 occurrences across the text | GCC | 10.8 | **14.6** | 20 | 50.4 | −26% |
| 16 keys, 4 KiB, 16 occurrences across the text | Clang | 11.9 | **14** | 20.2 | 52.2 | −15% |
| 16 keys, 16 KiB, 16 occurrences across the text | GCC | 27.4 | **50.7** | 58.9 | 87.2 | −46% |
| 16 keys, 16 KiB, 16 occurrences across the text | Clang | 31.7 | **48.4** | 60.1 | 88.7 | −35% |
| 16 keys, 64 KiB, 16 occurrences across the text | GCC | 92.6 | **195** | 209 | 225 | −53% |
| 16 keys, 64 KiB, 16 occurrences across the text | Clang | 110 | **184** | 215 | 228 | −40% |

**32 keys, prepared**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 32 keys, 128 B, one occurrence in the middle third | GCC | 0.33 | 1.49 | 1.45 | **1.27** | −74% |
| 32 keys, 128 B, one occurrence in the middle third | Clang | 0.33 | 1.51 | 1.37 | **1.24** | −73% |
| 32 keys, 1 KiB, one occurrence in the middle third | GCC | 1.58 | 7.91 | 6.77 | **5.42** | −71% |
| 32 keys, 1 KiB, one occurrence in the middle third | Clang | 1.82 | 7.55 | 6.47 | **5.49** | −67% |
| 32 keys, 4 KiB, one occurrence in the middle third | GCC | 5.62 | 28.1 | 25.1 | **18.9** | −70% |
| 32 keys, 4 KiB, one occurrence in the middle third | Clang | 6.71 | 26.8 | 24 | **19.5** | −66% |
| 32 keys, 16 KiB, one occurrence in the middle third | GCC | 21.9 | 110 | 98.9 | **71.3** | −69% |
| 32 keys, 16 KiB, one occurrence in the middle third | Clang | 26.2 | 104 | 94.8 | **73.4** | −64% |
| 32 keys, 64 KiB, one occurrence in the middle third | GCC | 88.5 | 435 | 393 | **278** | −68% |
| 32 keys, 64 KiB, one occurrence in the middle third | Clang | 105 | 413 | 377 | **287** | −63% |
| 32 keys, 1 KiB, 16 occurrences across the text | GCC | 2.45 | **9.7** | 13.5 | 10.4 | −75% |
| 32 keys, 1 KiB, 16 occurrences across the text | Clang | 2.67 | **9.53** | 13 | 10.3 | −72% |
| 32 keys, 4 KiB, 16 occurrences across the text | GCC | 6.56 | 30.1 | 31.9 | **24.3** | −73% |
| 32 keys, 4 KiB, 16 occurrences across the text | Clang | 7.61 | 28.8 | 30.8 | **24.8** | −69% |
| 32 keys, 16 KiB, 16 occurrences across the text | GCC | 23.2 | 111 | 106 | **77.6** | −70% |
| 32 keys, 16 KiB, 16 occurrences across the text | Clang | 27.5 | 106 | 102 | **79.9** | −66% |
| 32 keys, 64 KiB, 16 occurrences across the text | GCC | 89.1 | 435 | 398 | **285** | −69% |
| 32 keys, 64 KiB, 16 occurrences across the text | Clang | 106 | 413 | 385 | **295** | −64% |

**32 keys, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 32 keys, 128 B, one occurrence in the middle third | GCC | 8.31 | **1.6** | 3.49 | ≈62.6 | +420% |
| 32 keys, 128 B, one occurrence in the middle third | Clang | 8.22 | **1.61** | 3.42 | ≈66.4 | +411% |
| 32 keys, 1 KiB, one occurrence in the middle third | GCC | 9.51 | **8.12** | 8.86 | ≈66.2 | +17% |
| 32 keys, 1 KiB, one occurrence in the middle third | Clang | 9.61 | **7.78** | 8.51 | ≈70.7 | +24% |
| 32 keys, 4 KiB, one occurrence in the middle third | GCC | 13.5 | 28.4 | **27.2** | 80.6 | −50% |
| 32 keys, 4 KiB, one occurrence in the middle third | Clang | 14.6 | 27.1 | **26.1** | 84.7 | −44% |
| 32 keys, 16 KiB, one occurrence in the middle third | GCC | 29.8 | 110 | **101** | 133 | −70% |
| 32 keys, 16 KiB, one occurrence in the middle third | Clang | 34.3 | 104 | **96.8** | 139 | −65% |
| 32 keys, 64 KiB, one occurrence in the middle third | GCC | 96.2 | 435 | 395 | **341** | −72% |
| 32 keys, 64 KiB, one occurrence in the middle third | Clang | 114 | 413 | 379 | **352** | −68% |
| 32 keys, 1 KiB, 16 occurrences across the text | GCC | 10.4 | **9.91** | 15.7 | ≈71.3 | +4.7% |
| 32 keys, 1 KiB, 16 occurrences across the text | Clang | 10.5 | **9.76** | 15.1 | ≈76.2 | +7.9% |
| 32 keys, 4 KiB, 16 occurrences across the text | GCC | 14.6 | **30.3** | 34.1 | 86.9 | −52% |
| 32 keys, 4 KiB, 16 occurrences across the text | Clang | 15.6 | **29.2** | 32.8 | 90.2 | −47% |
| 32 keys, 16 KiB, 16 occurrences across the text | GCC | 31.2 | 112 | **108** | 140 | −71%† |
| 32 keys, 16 KiB, 16 occurrences across the text | Clang | 35.3 | 106 | **105** | 145 | −66% |
| 32 keys, 64 KiB, 16 occurrences across the text | GCC | 97.3 | 435 | 400 | **348** | −72% |
| 32 keys, 64 KiB, 16 occurrences across the text | Clang | 115 | 414 | 386 | **361** | −68% |

**128 keys, prepared**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 128 keys, 128 B, one occurrence in the middle third | GCC | 0.33 | 5.63 | 4.29 | **1.76** | −81% |
| 128 keys, 128 B, one occurrence in the middle third | Clang | 0.34 | 5.71 | 4.16 | **1.75** | −81% |
| 128 keys, 1 KiB, one occurrence in the middle third | GCC | 1.61 | 31 | 23.4 | **7.87** | −80% |
| 128 keys, 1 KiB, one occurrence in the middle third | Clang | 1.85 | 29.9 | 22.7 | **8.03** | −77% |
| 128 keys, 4 KiB, one occurrence in the middle third | GCC | 5.71 | 111 | 88.4 | **27.4** | −79% |
| 128 keys, 4 KiB, one occurrence in the middle third | Clang | 6.79 | 106 | 85.9 | **28.1** | −76% |
| 128 keys, 16 KiB, one occurrence in the middle third | GCC | 22 | 436 | 351 | **104** | −79% |
| 128 keys, 16 KiB, one occurrence in the middle third | Clang | 26.5 | 419 | 341 | **107** | −75% |
| 128 keys, 64 KiB, one occurrence in the middle third | GCC | 87 | 1,760 | 1,409 | **409** | −79% |
| 128 keys, 64 KiB, one occurrence in the middle third | Clang | 105 | 1,698 | 1,364 | **422** | −75% |
| 128 keys, 1 KiB, 16 occurrences across the text | GCC | 2.5 | 35.4 | 42.4 | **13.8** | −82% |
| 128 keys, 1 KiB, 16 occurrences across the text | Clang | 2.74 | 34.6 | 40.7 | **13.7** | −80% |
| 128 keys, 4 KiB, 16 occurrences across the text | GCC | 6.7 | 116 | 108 | **33.8** | −80% |
| 128 keys, 4 KiB, 16 occurrences across the text | Clang | 7.73 | 112 | 104 | **34.4** | −78% |
| 128 keys, 16 KiB, 16 occurrences across the text | GCC | 23.6 | 443 | 372 | **113** | −79%† |
| 128 keys, 16 KiB, 16 occurrences across the text | Clang | 27.8 | 427 | 360 | **116** | −76% |
| 128 keys, 64 KiB, 16 occurrences across the text | GCC | 92.5 | 1,764 | 1,405 | **414** | −78% |
| 128 keys, 64 KiB, 16 occurrences across the text | Clang | 108 | 1,695 | 1,363 | **425** | −75% |

**128 keys, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 128 keys, 128 B, one occurrence in the middle third | GCC | 31 | **5.87** | 11 | ≈224 | +432% |
| 128 keys, 128 B, one occurrence in the middle third | Clang | 30.8 | **5.85** | 10.3 | ≈237 | +426%† |
| 128 keys, 1 KiB, one occurrence in the middle third | GCC | 32.4 | 31.5 | **30.2** | ≈231 | +6.8% |
| 128 keys, 1 KiB, one occurrence in the middle third | Clang | 32.2 | 30.3 | **28.8** | ≈244 | +12% |
| 128 keys, 4 KiB, one occurrence in the middle third | GCC | 36.7 | 111 | **95.3** | 252 | −62% |
| 128 keys, 4 KiB, one occurrence in the middle third | Clang | 37.4 | 107 | **92.3** | 266 | −60% |
| 128 keys, 16 KiB, one occurrence in the middle third | GCC | 53.3 | 435 | 358 | **329** | −84% |
| 128 keys, 16 KiB, one occurrence in the middle third | Clang | 57.1 | 419 | 348 | **342** | −83% |
| 128 keys, 64 KiB, one occurrence in the middle third | GCC | 119 | 1,761 | 1,416 | **631** | −81% |
| 128 keys, 64 KiB, one occurrence in the middle third | Clang | 136 | 1,699 | 1,373 | **661** | −79% |
| 128 keys, 1 KiB, 16 occurrences across the text | GCC | 33.2 | **35.9** | 49.3 | ≈237 | −7.4% |
| 128 keys, 1 KiB, 16 occurrences across the text | Clang | 33.5 | **35** | 46.8 | ≈249 | −3.9% |
| 128 keys, 4 KiB, 16 occurrences across the text | GCC | 37.9 | 117 | **114** | 258 | −67% |
| 128 keys, 4 KiB, 16 occurrences across the text | Clang | 38.6 | 112 | **110** | 273 | −65% |
| 128 keys, 16 KiB, 16 occurrences across the text | GCC | 54.7 | 443 | 379 | **340** | −84% |
| 128 keys, 16 KiB, 16 occurrences across the text | Clang | 58.5 | 427 | 367 | **353** | −83% |
| 128 keys, 64 KiB, 16 occurrences across the text | GCC | 125 | 1,766 | 1,413 | **641** | −80% |
| 128 keys, 64 KiB, 16 occurrences across the text | Clang | 141 | 1,698 | 1,370 | **668** | −79% |

**1024 keys, prepared**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE alternation in chunks of 1024, µs | PCRE alternation in chunks of 512, µs | PCRE, shared prefixes, µs | PCRE, shared prefixes in chunks of 1024, µs | PCRE, shared prefixes in chunks of 512, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1024 keys, 128 B, one occurrence in the middle third | GCC | 0.34 | ≈41.4 | ≈66.2 | ≈65.7 | ≈48.5 | **2.57** | 2.57 | 4.1 | −87% |
| 1024 keys, 128 B, one occurrence in the middle third | Clang | 0.34 | ≈42 | ≈63.4 | ≈63.1 | ≈46.8 | 2.68 | **2.64** | 4.1 | −87% |
| 1024 keys, 1 KiB, one occurrence in the middle third | GCC | 1.64 | ≈235 | ≈441 | ≈437 | ≈344 | **10.8** | 10.8 | 19.4 | −85% |
| 1024 keys, 1 KiB, one occurrence in the middle third | Clang | 1.87 | ≈224 | ≈448 | ≈443 | ≈325 | 11.1 | **11.1** | 19.4 | −83% |
| 1024 keys, 4 KiB, one occurrence in the middle third | GCC | 5.78 | ≈802 | ≈1,589 | ≈1,583 | ≈1,297 | **37.7** | 37.8 | 68.6 | −85% |
| 1024 keys, 4 KiB, one occurrence in the middle third | Clang | 6.85 | ≈761 | ≈1,585 | ≈1,595 | ≈1,148 | 38.8 | **38.8** | 68.6 | −82% |
| 1024 keys, 16 KiB, one occurrence in the middle third | GCC | 22.3 | ≈3,434 | ≈6,974 | ≈6,971 | ≈5,109 | 145 | **145** | 263 | −85% |
| 1024 keys, 16 KiB, one occurrence in the middle third | Clang | 26.6 | ≈3,290 | ≈7,086 | ≈6,984 | ≈5,168 | 148 | **148** | 264 | −82% |
| 1024 keys, 64 KiB, one occurrence in the middle third | GCC | 89 | ≈13,804 | ≈26,662 | ≈26,401 | ≈21,522 | **556** | 557 | 1,017 | −84% |
| 1024 keys, 64 KiB, one occurrence in the middle third | Clang | 106 | ≈13,362 | ≈25,966 | ≈25,796 | ≈20,123 | **567** | 568 | 1,018 | −81% |
| 1024 keys, 1 KiB, 16 occurrences across the text | GCC | 2.62 | ≈261 | ≈627 | ≈622 | ≈441 | **20.4** | 20.4 | 30.5 | −87% |
| 1024 keys, 1 KiB, 16 occurrences across the text | Clang | 2.85 | ≈252 | ≈609 | ≈614 | ≈418 | **20.5** | 20.5 | 30.1 | −86% |
| 1024 keys, 4 KiB, 16 occurrences across the text | GCC | 6.88 | ≈886 | ≈1,816 | ≈1,872 | ≈1,295 | 47.8 | **47.8** | 80.3 | −86% |
| 1024 keys, 4 KiB, 16 occurrences across the text | Clang | 7.92 | ≈851 | ≈1,843 | ≈1,840 | ≈1,283 | 48.8 | **48.8** | 80.8 | −84% |
| 1024 keys, 16 KiB, 16 occurrences across the text | GCC | 23.7 | ≈3,528 | ≈7,605 | ≈7,594 | ≈5,504 | **150** | 150 | 267 | −84% |
| 1024 keys, 16 KiB, 16 occurrences across the text | Clang | 27.8 | ≈3,384 | ≈7,402 | ≈7,431 | ≈5,544 | **153** | 154 | 268 | −82% |
| 1024 keys, 64 KiB, 16 occurrences across the text | GCC | 90.8 | ≈14,335 | ≈28,965 | ≈28,777 | ≈21,791 | **566** | 567 | 1,026 | −84% |
| 1024 keys, 64 KiB, 16 occurrences across the text | Clang | 107 | ≈13,715 | ≈29,536 | ≈29,371 | ≈21,192 | **584** | 585 | 1,030 | −82% |

**1024 keys, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE alternation in chunks of 1024, µs | PCRE alternation in chunks of 512, µs | PCRE, shared prefixes, µs | PCRE, shared prefixes in chunks of 1024, µs | PCRE, shared prefixes in chunks of 512, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1024 keys, 128 B, one occurrence in the middle third | GCC | 393 | **41.2** | 114 | 116 | 100 | ≈1,822 | ≈1,891 | ≈1,938 | +856% |
| 1024 keys, 128 B, one occurrence in the middle third | Clang | 386 | **40.7** | 109 | 112 | 96 | ≈1,914 | ≈1,978 | ≈2,028 | +853% |
| 1024 keys, 1 KiB, one occurrence in the middle third | GCC | 393 | **232** | 476 | 478 | 391 | ≈1,862 | ≈1,910 | ≈1,966 | +70% |
| 1024 keys, 1 KiB, one occurrence in the middle third | Clang | 386 | **222** | 478 | 482 | 378 | ≈1,960 | ≈2,003 | ≈2,046 | +74% |
| 1024 keys, 4 KiB, one occurrence in the middle third | GCC | 398 | **834** | 1,717 | 1,742 | 1,436 | 1,961 | 1,965 | 2,031 | −52% |
| 1024 keys, 4 KiB, one occurrence in the middle third | Clang | 388 | **794** | 1,724 | 1,737 | 1,306 | 2,024 | 2,018 | 2,113 | −51% |
| 1024 keys, 16 KiB, one occurrence in the middle third | GCC | 415 | 3,389 | 7,086 | 7,023 | 5,389 | **2,069** | 2,074 | 2,252 | −80% |
| 1024 keys, 16 KiB, one occurrence in the middle third | Clang | 413 | 3,246 | 7,155 | 7,189 | 5,221 | 2,139 | **2,137** | 2,314 | −81% |
| 1024 keys, 64 KiB, one occurrence in the middle third | GCC | 481 | ≈13,896 | ≈26,395 | ≈26,508 | ≈21,646 | **2,481** | 2,482 | 2,972 | −81% |
| 1024 keys, 64 KiB, one occurrence in the middle third | Clang | 493 | ≈13,319 | ≈25,459 | ≈26,351 | ≈20,022 | **2,558** | 2,570 | 3,065 | −81% |
| 1024 keys, 1 KiB, 16 occurrences across the text | GCC | 394 | **255** | 667 | 670 | 483 | ≈1,854 | ≈1,927 | ≈2,003 | +55% |
| 1024 keys, 1 KiB, 16 occurrences across the text | Clang | 383 | **245** | 661 | 665 | 454 | ≈1,976 | ≈2,036 | ≈2,050 | +56% |
| 1024 keys, 4 KiB, 16 occurrences across the text | GCC | 398 | **854** | 1,918 | 1,940 | 1,388 | 1,964 | 1,969 | 2,051 | −53% |
| 1024 keys, 4 KiB, 16 occurrences across the text | Clang | 392 | **819** | 1,920 | 1,928 | 1,405 | 2,050 | 2,058 | 2,146 | −52% |
| 1024 keys, 16 KiB, 16 occurrences across the text | GCC | 417 | 3,346 | 6,723 | 6,780 | 4,926 | **2,067** | 2,078 | 2,252 | −80%† |
| 1024 keys, 16 KiB, 16 occurrences across the text | Clang | 413 | 3,182 | 6,481 | 6,502 | 5,000 | **2,140** | 2,148 | 2,308 | −81% |
| 1024 keys, 64 KiB, 16 occurrences across the text | GCC | 488 | ≈14,294 | ≈28,858 | ≈28,855 | ≈21,935 | **2,499** | 2,500 | 3,012 | −81% |
| 1024 keys, 64 KiB, 16 occurrences across the text | Clang | 492 | ≈13,761 | ≈29,535 | ≈29,468 | ≈21,809 | **2,589** | 2,595 | 3,087 | −81% |

### `replace()`

**8 keys, prepared**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 8 keys, 128 B, no occurrence | GCC | 0.28 | 1.34 | **0.32** | 0.34 | −15% |
| 8 keys, 128 B, no occurrence | Clang | 0.26 | 1.3 | **0.33** | 0.34 | −20% |
| 8 keys, 1 KiB, no occurrence | GCC | 1.57 | ≈10.8 | **2** | 2.12 | −22% |
| 8 keys, 1 KiB, no occurrence | Clang | 1.68 | ≈10.6 | **2.06** | 2.17 | −18% |
| 8 keys, 4 KiB, no occurrence | GCC | 5.77 | ≈42.1 | **7.66** | 8.07 | −25%† |
| 8 keys, 4 KiB, no occurrence | Clang | 6.34 | ≈41.5 | **7.92** | 8.25 | −20% |
| 8 keys, 16 KiB, no occurrence | GCC | 22.5 | ≈158 | **29.6** | 30.9 | −23% |
| 8 keys, 16 KiB, no occurrence | Clang | 25.1 | ≈156 | **30.7** | 31.5 | −18% |
| 8 keys, 64 KiB, no occurrence | GCC | 88.1 | ≈606 | **115** | 120 | −23% |
| 8 keys, 64 KiB, no occurrence | Clang | 99.2 | ≈594 | **119** | 123 | −17% |
| 8 keys, 128 B, one occurrence in the middle third | GCC | 0.31 | 1.24 | **0.45** | 0.47 | −31% |
| 8 keys, 128 B, one occurrence in the middle third | Clang | 0.31 | 1.19 | **0.45** | 0.48 | −31% |
| 8 keys, 1 KiB, one occurrence in the middle third | GCC | 1.6 | ≈10.6 | **2.15** | 2.27 | −26% |
| 8 keys, 1 KiB, one occurrence in the middle third | Clang | 1.74 | ≈10.3 | **2.2** | 2.32 | −21% |
| 8 keys, 4 KiB, one occurrence in the middle third | GCC | 5.74 | ≈40.5 | **7.83** | 8.22 | −27% |
| 8 keys, 4 KiB, one occurrence in the middle third | Clang | 6.49 | ≈39.5 | **8.1** | 8.42 | −20% |
| 8 keys, 16 KiB, one occurrence in the middle third | GCC | 22 | ≈163 | **30.1** | 31.4 | −27% |
| 8 keys, 16 KiB, one occurrence in the middle third | Clang | 25.2 | ≈160 | **31.3** | 32.2 | −20% |
| 8 keys, 64 KiB, one occurrence in the middle third | GCC | 89.5 | ≈697 | **119** | 124 | −25% |
| 8 keys, 64 KiB, one occurrence in the middle third | Clang | 102 | ≈685 | **123** | 127 | −18% |
| 8 keys, 1 KiB, 16 occurrences across the text | GCC | 2.07 | 9.88 | **3.58** | 3.67 | −42% |
| 8 keys, 1 KiB, 16 occurrences across the text | Clang | 2.25 | 9.65 | **3.73** | 3.87 | −40% |
| 8 keys, 4 KiB, 16 occurrences across the text | GCC | 6.21 | ≈41.4 | **9.4** | 9.8 | −34% |
| 8 keys, 4 KiB, 16 occurrences across the text | Clang | 6.97 | ≈40.7 | **9.76** | 10.2 | −29% |
| 8 keys, 16 KiB, 16 occurrences across the text | GCC | 22.9 | ≈174 | **31.7** | 32.8 | −28% |
| 8 keys, 16 KiB, 16 occurrences across the text | Clang | 25.9 | ≈170 | **32.7** | 33.7 | −21% |
| 8 keys, 64 KiB, 16 occurrences across the text | GCC | 88.7 | ≈678 | **120** | 125 | −26% |
| 8 keys, 64 KiB, 16 occurrences across the text | Clang | 101 | ≈660 | **125** | 128 | −19% |

**8 keys, one-shot**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 8 keys, 128 B, no occurrence | GCC | 2.51 | 1.41 | **1.21** | ≈18 | +107% |
| 8 keys, 128 B, no occurrence | Clang | 2.48 | 1.37 | **1.1** | ≈19.5 | +127% |
| 8 keys, 1 KiB, no occurrence | GCC | 3.82 | ≈11 | **2.9** | ≈19.7 | +32% |
| 8 keys, 1 KiB, no occurrence | Clang | 3.92 | ≈10.8 | **2.84** | ≈20.9 | +38%† |
| 8 keys, 4 KiB, no occurrence | GCC | 8.03 | ≈42.3 | **8.57** | 25.9 | −6.5% |
| 8 keys, 4 KiB, no occurrence | Clang | 8.55 | ≈41.6 | **8.75** | 27.3 | −2.2% |
| 8 keys, 16 KiB, no occurrence | GCC | 25 | ≈159 | **30.5** | 48.7 | −18% |
| 8 keys, 16 KiB, no occurrence | Clang | 27.4 | ≈157 | **31.5** | 50.4 | −13% |
| 8 keys, 64 KiB, no occurrence | GCC | 91.4 | ≈605 | **116** | 138 | −21%† |
| 8 keys, 64 KiB, no occurrence | Clang | 102 | ≈594 | **120** | 142 | −15% |
| 8 keys, 128 B, one occurrence in the middle third | GCC | 2.57 | **1.32** | 1.34 | ≈18 | +94% |
| 8 keys, 128 B, one occurrence in the middle third | Clang | 2.56 | **1.27** | 1.3 | ≈19.4 | +101% |
| 8 keys, 1 KiB, one occurrence in the middle third | GCC | 3.87 | ≈10.8 | **3.05** | ≈20 | +27% |
| 8 keys, 1 KiB, one occurrence in the middle third | Clang | 3.99 | ≈10.5 | **3.07** | ≈21.1 | +30%† |
| 8 keys, 4 KiB, one occurrence in the middle third | GCC | 8.02 | ≈40.7 | **8.76** | 26.1 | −8.5% |
| 8 keys, 4 KiB, one occurrence in the middle third | Clang | 8.86 | ≈40 | **8.97** | 27.6 | −1.2% |
| 8 keys, 16 KiB, one occurrence in the middle third | GCC | 24.3 | ≈164 | **31.1** | 49.2 | −22% |
| 8 keys, 16 KiB, one occurrence in the middle third | Clang | 27.4 | ≈160 | **32.2** | 51.1 | −15% |
| 8 keys, 64 KiB, one occurrence in the middle third | GCC | 92.1 | ≈706 | **120** | 143 | −23% |
| 8 keys, 64 KiB, one occurrence in the middle third | Clang | 104 | ≈690 | **124** | 146 | −16% |
| 8 keys, 1 KiB, 16 occurrences across the text | GCC | 4.38 | 9.97 | **4.5** | ≈21.4 | −2.5% |
| 8 keys, 1 KiB, 16 occurrences across the text | Clang | 4.54 | 9.75 | **4.65** | ≈22.4 | −2.1%† |
| 8 keys, 4 KiB, 16 occurrences across the text | GCC | 8.5 | ≈41.7 | **10.4** | 27.8 | −18% |
| 8 keys, 4 KiB, 16 occurrences across the text | Clang | 9.25 | ≈40.9 | **10.7** | 29.4 | −14% |
| 8 keys, 16 KiB, 16 occurrences across the text | GCC | 25.3 | ≈174 | **32.5** | 50.9 | −22% |
| 8 keys, 16 KiB, 16 occurrences across the text | Clang | 28.2 | ≈171 | **33.7** | 52.6 | −16% |
| 8 keys, 64 KiB, 16 occurrences across the text | GCC | 91 | ≈682 | **121** | 144 | −25% |
| 8 keys, 64 KiB, 16 occurrences across the text | Clang | 104 | ≈666 | **126** | 148 | −18% |

**16 keys, prepared**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 16 keys, 128 B, no occurrence | GCC | 0.27 | 1.94 | 0.55 | **0.54** | −49% |
| 16 keys, 128 B, no occurrence | Clang | 0.26 | 1.89 | 0.54 | **0.53** | −51% |
| 16 keys, 1 KiB, no occurrence | GCC | 1.58 | 15.3 | 3.47 | **3.36** | −53% |
| 16 keys, 1 KiB, no occurrence | Clang | 1.69 | 15 | 3.53 | **3.32** | −49% |
| 16 keys, 4 KiB, no occurrence | GCC | 5.67 | 59.5 | 12.9 | **12.3** | −54% |
| 16 keys, 4 KiB, no occurrence | Clang | 6.31 | 58.8 | 13.2 | **12.1** | −48% |
| 16 keys, 16 KiB, no occurrence | GCC | 22.2 | 241 | 50.8 | **48.1** | −54%† |
| 16 keys, 16 KiB, no occurrence | Clang | 24.9 | 238 | 51.9 | **47.3** | −47% |
| 16 keys, 64 KiB, no occurrence | GCC | 87.4 | ≈1,142 | 189 | **177** | −51% |
| 16 keys, 64 KiB, no occurrence | Clang | 98.7 | ≈1,135 | 193 | **174** | −43% |
| 16 keys, 128 B, one occurrence in the middle third | GCC | 0.31 | 1.82 | **0.66** | 0.66 | −53% |
| 16 keys, 128 B, one occurrence in the middle third | Clang | 0.31 | 1.76 | 0.66 | **0.65** | −52% |
| 16 keys, 1 KiB, one occurrence in the middle third | GCC | 1.6 | 15.3 | 3.62 | **3.54** | −55% |
| 16 keys, 1 KiB, one occurrence in the middle third | Clang | 1.75 | 15.1 | 3.69 | **3.48** | −50% |
| 16 keys, 4 KiB, one occurrence in the middle third | GCC | 5.75 | 59.1 | 13 | **12.4** | −54% |
| 16 keys, 4 KiB, one occurrence in the middle third | Clang | 6.49 | 58.3 | 13.3 | **12.3** | −47% |
| 16 keys, 16 KiB, one occurrence in the middle third | GCC | 22.7 | ≈247 | 49.6 | **47** | −52% |
| 16 keys, 16 KiB, one occurrence in the middle third | Clang | 25.4 | ≈242 | 50.8 | **46.3** | −45% |
| 16 keys, 64 KiB, one occurrence in the middle third | GCC | 89.4 | ≈1,042 | 200 | **187** | −52% |
| 16 keys, 64 KiB, one occurrence in the middle third | Clang | 101 | ≈1,026 | 203 | **184** | −45% |
| 16 keys, 1 KiB, 16 occurrences across the text | GCC | 2.07 | 14.2 | **4.97** | 5.02 | −58% |
| 16 keys, 1 KiB, 16 occurrences across the text | Clang | 2.25 | 13.9 | 5.11 | **5.09** | −56% |
| 16 keys, 4 KiB, 16 occurrences across the text | GCC | 6.22 | 59 | 14.6 | **14.4** | −57% |
| 16 keys, 4 KiB, 16 occurrences across the text | Clang | 6.93 | 58 | 15.1 | **14.3** | −51% |
| 16 keys, 16 KiB, 16 occurrences across the text | GCC | 22.8 | 235 | 51.7 | **49.1** | −54% |
| 16 keys, 16 KiB, 16 occurrences across the text | Clang | 25.8 | 232 | 53 | **48.5** | −47% |
| 16 keys, 64 KiB, 16 occurrences across the text | GCC | 90.3 | 940 | 198 | **187** | −52% |
| 16 keys, 64 KiB, 16 occurrences across the text | Clang | 102 | 932 | 203 | **183** | −44% |

**16 keys, one-shot**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 16 keys, 128 B, no occurrence | GCC | 4.19 | 2.01 | **1.83** | ≈32.7 | +129% |
| 16 keys, 128 B, no occurrence | Clang | 4.19 | 1.97 | **1.66** | ≈34.1 | +151% |
| 16 keys, 1 KiB, no occurrence | GCC | 5.52 | 15.4 | **4.74** | ≈35.4 | +16% |
| 16 keys, 1 KiB, no occurrence | Clang | 5.65 | 15.1 | **4.66** | ≈37.1 | +22% |
| 16 keys, 4 KiB, no occurrence | GCC | 9.72 | 59.7 | **14.2** | 44.5 | −31% |
| 16 keys, 4 KiB, no occurrence | Clang | 10.2 | 58.9 | **14.3** | 46 | −28%† |
| 16 keys, 16 KiB, no occurrence | GCC | 26.5 | 241 | **52** | 80.4 | −49% |
| 16 keys, 16 KiB, no occurrence | Clang | 28.8 | 238 | **53** | 81.6 | −46% |
| 16 keys, 64 KiB, no occurrence | GCC | 92.6 | ≈1,145 | **190** | 210 | −51% |
| 16 keys, 64 KiB, no occurrence | Clang | 103 | ≈1,139 | **194** | 208 | −47% |
| 16 keys, 128 B, one occurrence in the middle third | GCC | 4.27 | **1.89** | 1.95 | ≈32.9 | +126% |
| 16 keys, 128 B, one occurrence in the middle third | Clang | 4.28 | 1.85 | **1.84** | ≈35.2 | +134% |
| 16 keys, 1 KiB, one occurrence in the middle third | GCC | 5.59 | 15.4 | **4.91** | ≈36.1 | +14% |
| 16 keys, 1 KiB, one occurrence in the middle third | Clang | 5.7 | 15.2 | **4.87** | ≈37.2 | +17% |
| 16 keys, 4 KiB, one occurrence in the middle third | GCC | 9.68 | 59.3 | **14.3** | 45 | −32% |
| 16 keys, 4 KiB, one occurrence in the middle third | Clang | 10.4 | 58.5 | **14.5** | 46.8 | −28% |
| 16 keys, 16 KiB, one occurrence in the middle third | GCC | 26.6 | ≈248 | **50.9** | 80 | −48% |
| 16 keys, 16 KiB, one occurrence in the middle third | Clang | 29.4 | ≈244 | **52** | 80.3 | −43% |
| 16 keys, 64 KiB, one occurrence in the middle third | GCC | 93.5 | ≈1,045 | **200** | 220 | −53% |
| 16 keys, 64 KiB, one occurrence in the middle third | Clang | 105 | ≈1,033 | **204** | 219 | −49% |
| 16 keys, 1 KiB, 16 occurrences across the text | GCC | 6.07 | 14.3 | **6.32** | ≈37.3 | −3.7% |
| 16 keys, 1 KiB, 16 occurrences across the text | Clang | 6.27 | 14 | **6.38** | ≈38.9 | −2.0% |
| 16 keys, 4 KiB, 16 occurrences across the text | GCC | 10.2 | 59.3 | **16.1** | 46.8 | −37% |
| 16 keys, 4 KiB, 16 occurrences across the text | Clang | 10.9 | 58.3 | **16.4** | 48.8 | −34% |
| 16 keys, 16 KiB, 16 occurrences across the text | GCC | 26.7 | 235 | **53.1** | 82.2 | −50% |
| 16 keys, 16 KiB, 16 occurrences across the text | Clang | 29.7 | 232 | **54.3** | 82.8 | −45% |
| 16 keys, 64 KiB, 16 occurrences across the text | GCC | 94.1 | 944 | **200** | 220 | −53% |
| 16 keys, 64 KiB, 16 occurrences across the text | Clang | 106 | 932 | **205** | 218 | −48% |

**32 keys, prepared**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 32 keys, 128 B, no occurrence | GCC | 0.28 | 3.83 | 0.85 | **0.73** | −62% |
| 32 keys, 128 B, no occurrence | Clang | 0.26 | 3.81 | 0.81 | **0.72** | −64% |
| 32 keys, 1 KiB, no occurrence | GCC | 1.59 | ≈29.8 | 6.07 | **4.78** | −67% |
| 32 keys, 1 KiB, no occurrence | Clang | 1.69 | ≈29.8 | 5.84 | **4.7** | −64% |
| 32 keys, 4 KiB, no occurrence | GCC | 5.74 | ≈113 | 24.1 | **17.9** | −68% |
| 32 keys, 4 KiB, no occurrence | Clang | 6.33 | ≈113 | 23 | **17.8** | −64% |
| 32 keys, 16 KiB, no occurrence | GCC | 22.9 | ≈455 | 95.7 | **68.4** | −66% |
| 32 keys, 16 KiB, no occurrence | Clang | 25.2 | ≈455 | 90.9 | **67.6** | −63% |
| 32 keys, 64 KiB, no occurrence | GCC | 88.7 | ≈2,038 | 380 | **270** | −67% |
| 32 keys, 64 KiB, no occurrence | Clang | 99.6 | ≈2,026 | 361 | **267** | −63% |
| 32 keys, 128 B, one occurrence in the middle third | GCC | 0.31 | 3.71 | 0.97 | **0.87** | −64% |
| 32 keys, 128 B, one occurrence in the middle third | Clang | 0.30 | 3.68 | 0.94 | **0.86** | −65% |
| 32 keys, 1 KiB, one occurrence in the middle third | GCC | 1.59 | ≈30.2 | 6.24 | **4.95** | −68% |
| 32 keys, 1 KiB, one occurrence in the middle third | Clang | 1.74 | ≈30.5 | 6 | **4.89** | −64% |
| 32 keys, 4 KiB, one occurrence in the middle third | GCC | 5.75 | ≈116 | 24.7 | **18.4** | −69% |
| 32 keys, 4 KiB, one occurrence in the middle third | Clang | 6.48 | ≈116 | 23.7 | **18.3** | −64% |
| 32 keys, 16 KiB, one occurrence in the middle third | GCC | 22.1 | ≈491 | 97 | **69.9** | −68% |
| 32 keys, 16 KiB, one occurrence in the middle third | Clang | 25.3 | ≈487 | 92.4 | **69** | −63% |
| 32 keys, 64 KiB, one occurrence in the middle third | GCC | 89.9 | ≈2,263 | 379 | **271** | −67% |
| 32 keys, 64 KiB, one occurrence in the middle third | Clang | 102 | ≈2,270 | 361 | **268** | −62% |
| 32 keys, 1 KiB, 16 occurrences across the text | GCC | 2.1 | 26.7 | 7 | **6.26** | −67% |
| 32 keys, 1 KiB, 16 occurrences across the text | Clang | 2.27 | 26.7 | 6.91 | **6.36** | −64% |
| 32 keys, 4 KiB, 16 occurrences across the text | GCC | 6.26 | ≈117 | 24.8 | **19.5** | −68% |
| 32 keys, 4 KiB, 16 occurrences across the text | Clang | 7.02 | ≈118 | 24.1 | **19.4** | −64% |
| 32 keys, 16 KiB, 16 occurrences across the text | GCC | 22.6 | ≈509 | 96 | **69.7** | −68% |
| 32 keys, 16 KiB, 16 occurrences across the text | Clang | 25.8 | ≈511 | 92.5 | **69** | −63% |
| 32 keys, 64 KiB, 16 occurrences across the text | GCC | 88 | ≈1,751 | 380 | **272** | −68% |
| 32 keys, 64 KiB, 16 occurrences across the text | Clang | 101 | ≈1,751 | 365 | **269** | −62% |

**32 keys, one-shot**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 32 keys, 128 B, no occurrence | GCC | 8.13 | 3.91 | **2.98** | ≈62 | +173% |
| 32 keys, 128 B, no occurrence | Clang | 8.2 | 3.9 | **2.64** | ≈64.5 | +210% |
| 32 keys, 1 KiB, no occurrence | GCC | 9.33 | 30.4 | **8.23** | ≈65.4 | +14% |
| 32 keys, 1 KiB, no occurrence | Clang | 9.44 | 30.4 | **7.67** | ≈68.8 | +23% |
| 32 keys, 4 KiB, no occurrence | GCC | 13.5 | 119 | **26.1** | 78.8 | −48% |
| 32 keys, 4 KiB, no occurrence | Clang | 14.1 | 119 | **24.9** | 82.1 | −43% |
| 32 keys, 16 KiB, no occurrence | GCC | 30.9 | 469 | **97.9** | 130 | −68% |
| 32 keys, 16 KiB, no occurrence | Clang | 33.3 | 471 | **92.9** | 132 | −64% |
| 32 keys, 64 KiB, no occurrence | GCC | 96.9 | ≈2,040 | 383 | **332** | −71% |
| 32 keys, 64 KiB, no occurrence | Clang | 107 | ≈2,038 | 363 | **332** | −68% |
| 32 keys, 128 B, one occurrence in the middle third | GCC | 8.02 | 3.79 | **3.1** | ≈62.2 | +159% |
| 32 keys, 128 B, one occurrence in the middle third | Clang | 8.09 | 3.76 | **2.83** | ≈65.1 | +187% |
| 32 keys, 1 KiB, one occurrence in the middle third | GCC | 9.33 | 30.3 | **8.37** | ≈65.4 | +11% |
| 32 keys, 1 KiB, one occurrence in the middle third | Clang | 9.53 | 30.4 | **7.92** | ≈69.1 | +20% |
| 32 keys, 4 KiB, one occurrence in the middle third | GCC | 13.6 | 122 | **26.8** | 79.6 | −50% |
| 32 keys, 4 KiB, one occurrence in the middle third | Clang | 14.3 | 122 | **25.6** | 82.7 | −44% |
| 32 keys, 16 KiB, one occurrence in the middle third | GCC | 30.3 | 476 | **99.3** | 132 | −70% |
| 32 keys, 16 KiB, one occurrence in the middle third | Clang | 33.1 | ≈489 | **94.4** | 134 | −65% |
| 32 keys, 64 KiB, one occurrence in the middle third | GCC | 97.7 | ≈2,275 | 382 | **334** | −71% |
| 32 keys, 64 KiB, one occurrence in the middle third | Clang | 110 | ≈2,293 | 362 | **334** | −67% |
| 32 keys, 1 KiB, 16 occurrences across the text | GCC | 9.83 | 26.8 | **9.2** | ≈67.7 | +7.4% |
| 32 keys, 1 KiB, 16 occurrences across the text | Clang | 10.1 | 26.8 | **8.87** | ≈70.9 | +14% |
| 32 keys, 4 KiB, 16 occurrences across the text | GCC | 14.1 | 115 | **27.1** | 80.8 | −48% |
| 32 keys, 4 KiB, 16 occurrences across the text | Clang | 14.9 | 115 | **26.1** | 84.6 | −43% |
| 32 keys, 16 KiB, 16 occurrences across the text | GCC | 30.5 | ≈513 | **98.2** | 132 | −69% |
| 32 keys, 16 KiB, 16 occurrences across the text | Clang | 33.9 | ≈515 | **94.4** | 134 | −64% |
| 32 keys, 64 KiB, 16 occurrences across the text | GCC | 96.2 | ≈1,754 | 382 | **335** | −71% |
| 32 keys, 64 KiB, 16 occurrences across the text | Clang | 109 | ≈1,749 | 367 | **336** | −67% |

**128 keys, prepared**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 128 keys, 128 B, no occurrence | GCC | 0.28 | ≈6.14 | 2.9 | **1.02** | −73% |
| 128 keys, 128 B, no occurrence | Clang | 0.27 | ≈6.14 | 2.79 | **1.04** | −74% |
| 128 keys, 1 KiB, no occurrence | GCC | 1.61 | ≈49.2 | 22.3 | **6.63** | −76% |
| 128 keys, 1 KiB, no occurrence | Clang | 1.71 | ≈48.9 | 21.6 | **6.73** | −75% |
| 128 keys, 4 KiB, no occurrence | GCC | 5.81 | ≈194 | 87.6 | **24.5** | −76% |
| 128 keys, 4 KiB, no occurrence | Clang | 6.43 | ≈194 | 84.8 | **24.9** | −74% |
| 128 keys, 16 KiB, no occurrence | GCC | 22.9 | ≈696 | 350 | **94.2** | −76% |
| 128 keys, 16 KiB, no occurrence | Clang | 25.4 | ≈695 | 339 | **95.6** | −73% |
| 128 keys, 64 KiB, no occurrence | GCC | 89.7 | ≈3,241 | 1,410 | **379** | −76% |
| 128 keys, 64 KiB, no occurrence | Clang | 101 | ≈3,219 | 1,372 | **385** | −74% |
| 128 keys, 128 B, one occurrence in the middle third | GCC | 0.32 | 5.77 | 2.87 | **1.16** | −73% |
| 128 keys, 128 B, one occurrence in the middle third | Clang | 0.31 | 5.75 | 2.74 | **1.15** | −73% |
| 128 keys, 1 KiB, one occurrence in the middle third | GCC | 1.62 | ≈50.1 | 22.4 | **6.86** | −76% |
| 128 keys, 1 KiB, one occurrence in the middle third | Clang | 1.77 | ≈49.9 | 21.6 | **6.93** | −74% |
| 128 keys, 4 KiB, one occurrence in the middle third | GCC | 5.83 | ≈198 | 88.1 | **25** | −77% |
| 128 keys, 4 KiB, one occurrence in the middle third | Clang | 6.55 | ≈198 | 85.3 | **25.3** | −74% |
| 128 keys, 16 KiB, one occurrence in the middle third | GCC | 22.6 | ≈645 | 350 | **95.8** | −77% |
| 128 keys, 16 KiB, one occurrence in the middle third | Clang | 25.7 | ≈645 | 338 | **97.1** | −74% |
| 128 keys, 64 KiB, one occurrence in the middle third | GCC | 89.4 | ≈3,095 | 1,422 | **379** | −76% |
| 128 keys, 64 KiB, one occurrence in the middle third | Clang | 102 | ≈3,091 | 1,375 | **384** | −73% |
| 128 keys, 1 KiB, 16 occurrences across the text | GCC | 2.14 | ≈41.5 | 20.8 | **7.96** | −73% |
| 128 keys, 1 KiB, 16 occurrences across the text | Clang | 2.29 | ≈41.4 | 19.9 | **8.13** | −72% |
| 128 keys, 4 KiB, 16 occurrences across the text | GCC | 6.4 | ≈188 | 87.7 | **26.6** | −76% |
| 128 keys, 4 KiB, 16 occurrences across the text | Clang | 7.15 | ≈187 | 84.9 | **27.1** | −74% |
| 128 keys, 16 KiB, 16 occurrences across the text | GCC | 23 | ≈739 | 349 | **96.5** | −76% |
| 128 keys, 16 KiB, 16 occurrences across the text | Clang | 26.2 | ≈735 | 338 | **98.3** | −73% |
| 128 keys, 64 KiB, 16 occurrences across the text | GCC | 89.2 | ≈3,196 | 1,416 | **385** | −77% |
| 128 keys, 64 KiB, 16 occurrences across the text | Clang | 102 | ≈3,181 | 1,374 | **390** | −74% |

**128 keys, one-shot**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 128 keys, 128 B, no occurrence | GCC | 29.3 | **6.26** | 9.38 | ≈221 | +369% |
| 128 keys, 128 B, no occurrence | Clang | 29.5 | **6.27** | 8.47 | ≈233 | +370% |
| 128 keys, 1 KiB, no occurrence | GCC | 30.9 | 49.1 | **28.8** | ≈230 | +7.4% |
| 128 keys, 1 KiB, no occurrence | Clang | 31 | 49 | **27.3** | ≈238 | +14% |
| 128 keys, 4 KiB, no occurrence | GCC | 35.3 | 190 | **94.3** | 248 | −63% |
| 128 keys, 4 KiB, no occurrence | Clang | 35.6 | 189 | **90.8** | 262 | −61% |
| 128 keys, 16 KiB, no occurrence | GCC | 52.5 | 748 | 358 | **319** | −83% |
| 128 keys, 16 KiB, no occurrence | Clang | 54.7 | 747 | 345 | **329** | −83% |
| 128 keys, 64 KiB, no occurrence | GCC | 120 | ≈3,263 | 1,419 | **606** | −80% |
| 128 keys, 64 KiB, no occurrence | Clang | 130 | ≈3,236 | 1,378 | **623** | −79% |
| 128 keys, 128 B, one occurrence in the middle third | GCC | 29.5 | **5.87** | 9.38 | ≈221 | +402% |
| 128 keys, 128 B, one occurrence in the middle third | Clang | 29.5 | **5.86** | 8.61 | ≈237 | +403% |
| 128 keys, 1 KiB, one occurrence in the middle third | GCC | 30.7 | 48.9 | **28.9** | ≈226 | +7.2% |
| 128 keys, 1 KiB, one occurrence in the middle third | Clang | 31 | 48.9 | **27.5** | ≈239 | +13% |
| 128 keys, 4 KiB, one occurrence in the middle third | GCC | 35.2 | 190 | **94.8** | 246 | −63% |
| 128 keys, 4 KiB, one occurrence in the middle third | Clang | 36.5 | 191 | **91.4** | 260 | −60% |
| 128 keys, 16 KiB, one occurrence in the middle third | GCC | 52.1 | 750 | 357 | **317** | −84%† |
| 128 keys, 16 KiB, one occurrence in the middle third | Clang | 55 | 750 | 345 | **331** | −83% |
| 128 keys, 64 KiB, one occurrence in the middle third | GCC | 120 | ≈3,120 | 1,429 | **605** | −80% |
| 128 keys, 64 KiB, one occurrence in the middle third | Clang | 133 | ≈3,109 | 1,384 | **627** | −79% |
| 128 keys, 1 KiB, 16 occurrences across the text | GCC | 31.4 | 42.3 | **27.5** | ≈231 | +15% |
| 128 keys, 1 KiB, 16 occurrences across the text | Clang | 31.6 | 42.3 | **25.9** | ≈242 | +22% |
| 128 keys, 4 KiB, 16 occurrences across the text | GCC | 35.8 | 187 | **94.5** | 249 | −62%† |
| 128 keys, 4 KiB, 16 occurrences across the text | Clang | 36.4 | 187 | **91.3** | 262 | −60% |
| 128 keys, 16 KiB, 16 occurrences across the text | GCC | 52.6 | 742 | 357 | **321** | −84% |
| 128 keys, 16 KiB, 16 occurrences across the text | Clang | 55.5 | 744 | 345 | **335** | −83% |
| 128 keys, 64 KiB, 16 occurrences across the text | GCC | 120 | ≈3,206 | 1,423 | **609** | −80% |
| 128 keys, 64 KiB, 16 occurrences across the text | Clang | 133 | ≈3,191 | 1,380 | **628** | −79% |

**1024 keys, prepared**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 1024 keys, 128 B, no occurrence | GCC | 0.28 | 7.74 | ≈51.1 | **1.69** | −83% |
| 1024 keys, 128 B, no occurrence | Clang | 0.27 | 7.89 | ≈52.7 | **1.63** | −84% |
| 1024 keys, 1 KiB, no occurrence | GCC | 1.62 | ≈47.9 | ≈400 | **9.39** | −83% |
| 1024 keys, 1 KiB, no occurrence | Clang | 1.72 | ≈48.1 | ≈411 | **8.98** | −81% |
| 1024 keys, 4 KiB, no occurrence | GCC | 5.89 | 193 | ≈1,624 | **34.8** | −83% |
| 1024 keys, 4 KiB, no occurrence | Clang | 6.46 | ≈170 | ≈1,651 | **33** | −80% |
| 1024 keys, 16 KiB, no occurrence | GCC | 23.2 | ≈748 | ≈5,700 | **138** | −83% |
| 1024 keys, 16 KiB, no occurrence | Clang | 25.5 | ≈748 | ≈5,784 | **131** | −81% |
| 1024 keys, 64 KiB, no occurrence | GCC | 90.3 | ≈3,021 | ≈23,895 | **526** | −83% |
| 1024 keys, 64 KiB, no occurrence | Clang | 100 | ≈2,998 | ≈23,889 | **500** | −80% |
| 1024 keys, 128 B, one occurrence in the middle third | GCC | 0.32 | 7.6 | ≈49.1 | **1.88** | −83% |
| 1024 keys, 128 B, one occurrence in the middle third | Clang | 0.31 | 7.65 | ≈49.6 | **1.8** | −83% |
| 1024 keys, 1 KiB, one occurrence in the middle third | GCC | 1.66 | ≈52 | ≈403 | **9.78** | −83% |
| 1024 keys, 1 KiB, one occurrence in the middle third | Clang | 1.8 | ≈51.8 | ≈416 | **9.3** | −81% |
| 1024 keys, 4 KiB, one occurrence in the middle third | GCC | 5.92 | ≈207 | ≈1,543 | **35.3** | −83% |
| 1024 keys, 4 KiB, one occurrence in the middle third | Clang | 6.67 | ≈208 | ≈1,580 | **33.6** | −80% |
| 1024 keys, 16 KiB, one occurrence in the middle third | GCC | 22.8 | ≈839 | ≈6,776 | **138** | −83%† |
| 1024 keys, 16 KiB, one occurrence in the middle third | Clang | 26 | ≈838 | ≈6,915 | **130** | −80% |
| 1024 keys, 64 KiB, one occurrence in the middle third | GCC | 89.3 | ≈3,123 | ≈26,526 | **532** | −83% |
| 1024 keys, 64 KiB, one occurrence in the middle third | Clang | 102 | ≈3,096 | ≈27,003 | **503** | −80% |
| 1024 keys, 1 KiB, 16 occurrences across the text | GCC | 2.27 | 45.8 | ≈338 | **11.8** | −81% |
| 1024 keys, 1 KiB, 16 occurrences across the text | Clang | 2.42 | 45.8 | ≈349 | **11.1** | −78% |
| 1024 keys, 4 KiB, 16 occurrences across the text | GCC | 6.65 | 188 | ≈1,515 | **38** | −83% |
| 1024 keys, 4 KiB, 16 occurrences across the text | Clang | 7.37 | 187 | ≈1,563 | **35.7** | −79% |
| 1024 keys, 16 KiB, 16 occurrences across the text | GCC | 23.5 | 750 | ≈4,969 | **137** | −83% |
| 1024 keys, 16 KiB, 16 occurrences across the text | Clang | 26.8 | 750 | ≈5,155 | **130** | −79% |
| 1024 keys, 64 KiB, 16 occurrences across the text | GCC | 90.1 | ≈2,642 | ≈22,106 | **533** | −83% |
| 1024 keys, 64 KiB, 16 occurrences across the text | Clang | 103 | ≈2,642 | ≈23,076 | **502** | −79% |

**1024 keys, one-shot**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 1024 keys, 128 B, no occurrence | GCC | 388 | **7.87** | ≈98.7 | ≈1,832 | +4849% |
| 1024 keys, 128 B, no occurrence | Clang | 379 | **8.02** | ≈95 | ≈1,911 | +4659% |
| 1024 keys, 1 KiB, no occurrence | GCC | 390 | **50.4** | ≈453 | ≈1,819 | +671% |
| 1024 keys, 1 KiB, no occurrence | Clang | 380 | **50.4** | ≈456 | ≈1,917 | +654% |
| 1024 keys, 4 KiB, no occurrence | GCC | 395 | **192** | ≈1,659 | ≈1,869 | +106% |
| 1024 keys, 4 KiB, no occurrence | Clang | 384 | **192** | ≈1,719 | ≈1,947 | +101% |
| 1024 keys, 16 KiB, no occurrence | GCC | 411 | **782** | ≈5,702 | 2,054 | −47% |
| 1024 keys, 16 KiB, no occurrence | Clang | 405 | **785** | ≈5,891 | 2,108 | −48% |
| 1024 keys, 64 KiB, no occurrence | GCC | 479 | 2,984 | ≈23,981 | **2,447** | −80% |
| 1024 keys, 64 KiB, no occurrence | Clang | 487 | 2,984 | ≈24,283 | **2,508** | −81% |
| 1024 keys, 128 B, one occurrence in the middle third | GCC | 390 | **7.63** | ≈98.9 | ≈1,816 | +5012% |
| 1024 keys, 128 B, one occurrence in the middle third | Clang | 384 | **7.68** | ≈95.4 | ≈1,938 | +4893% |
| 1024 keys, 1 KiB, one occurrence in the middle third | GCC | 389 | **51.4** | ≈455 | ≈1,828 | +658% |
| 1024 keys, 1 KiB, one occurrence in the middle third | Clang | 380 | **51.5** | ≈459 | ≈1,921 | +635% |
| 1024 keys, 4 KiB, one occurrence in the middle third | GCC | 391 | **198** | ≈1,605 | ≈1,849 | +98% |
| 1024 keys, 4 KiB, one occurrence in the middle third | Clang | 385 | **198** | ≈1,657 | ≈1,946 | +95% |
| 1024 keys, 16 KiB, one occurrence in the middle third | GCC | 410 | **773** | ≈6,709 | 2,063 | −47% |
| 1024 keys, 16 KiB, one occurrence in the middle third | Clang | 408 | **776** | ≈6,970 | 2,126 | −47% |
| 1024 keys, 64 KiB, one occurrence in the middle third | GCC | 477 | 3,054 | ≈26,266 | **2,452** | −81% |
| 1024 keys, 64 KiB, one occurrence in the middle third | Clang | 483 | 3,057 | ≈27,583 | **2,502** | −81% |
| 1024 keys, 1 KiB, 16 occurrences across the text | GCC | 393 | **46.2** | ≈389 | ≈1,857 | +751% |
| 1024 keys, 1 KiB, 16 occurrences across the text | Clang | 383 | **46.1** | ≈393 | ≈1,920 | +729% |
| 1024 keys, 4 KiB, 16 occurrences across the text | GCC | 393 | **187** | ≈1,587 | ≈1,880 | +110% |
| 1024 keys, 4 KiB, 16 occurrences across the text | Clang | 383 | **187** | ≈1,629 | ≈1,960 | +105% |
| 1024 keys, 16 KiB, 16 occurrences across the text | GCC | 410 | **741** | ≈5,074 | 2,077 | −44% |
| 1024 keys, 16 KiB, 16 occurrences across the text | Clang | 408 | **744** | ≈5,313 | 2,112 | −45% |
| 1024 keys, 64 KiB, 16 occurrences across the text | GCC | 478 | 3,036 | ≈21,808 | **2,455** | −81% |
| 1024 keys, 64 KiB, 16 occurrences across the text | Clang | 486 | 3,036 | ≈22,947 | **2,503** | −81% |

## PHP names

### `matches()`

**8 PHP names, prepared**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | `str_contains()` loop, second copy, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 8 PHP names, 128 B | GCC | 0.27 | 0.22 | 0.23 | **0.20** | 0.20 | +38% |
| 8 PHP names, 128 B | Clang | 0.27 | 0.21 | 0.22 | **0.19** | 0.20 | +39% |
| 8 PHP names, 1 KiB | GCC | 1.54 | 1.58 | 1.6 | **1.11** | 1.11 | +38% |
| 8 PHP names, 1 KiB | Clang | 1.78 | 1.49 | 1.5 | 1.13 | **1.11** | +58% |
| 8 PHP names, 4 KiB | GCC | 5.57 | 5.5 | 5.52 | 4.27 | **4.26** | +31% |
| 8 PHP names, 4 KiB | Clang | 6.64 | 5.14 | 5.16 | 4.33 | **4.27** | +56% |
| 8 PHP names, 64 KiB | GCC | 81.3 | 80.2 | 80.2 | 62.8 | **62.7** | +30% |
| 8 PHP names, 64 KiB | Clang | 97.5 | 74.3 | 73.7 | 63.7 | **62.6** | +56% |

**8 PHP names, one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | `str_contains()` loop, second copy, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 8 PHP names, 128 B | GCC | 3.87 | **0.28** | 0.30 | 1.3 | ≈27 | +1269% |
| 8 PHP names, 128 B | Clang | 3.86 | **0.28** | 0.29 | 1.38 | ≈28.5 | +1281% |
| 8 PHP names, 1 KiB | GCC | 5.15 | **1.67** | 1.69 | 2.23 | ≈28.2 | +209% |
| 8 PHP names, 1 KiB | Clang | 5.36 | **1.55** | 1.57 | 2.32 | ≈30.1 | +246% |
| 8 PHP names, 4 KiB | GCC | 9.22 | 5.59 | 5.63 | **5.39** | ≈30.7 | +71% |
| 8 PHP names, 4 KiB | Clang | 10.2 | **5.17** | 5.21 | 5.52 | ≈33.2 | +98% |
| 8 PHP names, 64 KiB | GCC | 85.8 | 80.9 | 80.8 | **64.5** | 90.2 | +33% |
| 8 PHP names, 64 KiB | Clang | 101 | 74.8 | 74.7 | **65.2** | 92.1 | +56% |

**32 PHP names, prepared**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | `str_contains()` loop, second copy, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 32 PHP names, 128 B | GCC | 0.28 | 1.06 | 1.09 | 0.95 | **0.75** | −63% |
| 32 PHP names, 128 B | Clang | 0.28 | 1.03 | 1.04 | 0.92 | **0.76** | −63% |
| 32 PHP names, 1 KiB | GCC | 1.58 | 6.58 | 6.65 | 6.88 | **5.06** | −69% |
| 32 PHP names, 1 KiB | Clang | 1.79 | 6.2 | 6.3 | 6.59 | **5.14** | −65% |
| 32 PHP names, 4 KiB | GCC | 5.61 | 23.2 | 23.2 | 27.1 | **19.1** | −71% |
| 32 PHP names, 4 KiB | Clang | 6.61 | 21.6 | 21.7 | 26 | **19.6** | −66% |
| 32 PHP names, 64 KiB | GCC | 71 | 296 | 297 | 346 | **241** | −70% |
| 32 PHP names, 64 KiB | Clang | 85.2 | 279 | 280 | 334 | **247** | −66% |

**32 PHP names, one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | `str_contains()` loop, second copy, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 32 PHP names, 128 B | GCC | 14 | **1.13** | 1.16 | 4.06 | ≈102 | +1148% |
| 32 PHP names, 128 B | Clang | 14.3 | **1.09** | 1.11 | 4.31 | ≈107 | +1215% |
| 32 PHP names, 1 KiB | GCC | 15.3 | **6.68** | 6.71 | 10 | ≈105 | +130% |
| 32 PHP names, 1 KiB | Clang | 15.9 | **6.25** | 6.36 | 10 | ≈111 | +154% |
| 32 PHP names, 4 KiB | GCC | 19.3 | **23.1** | 23.2 | 30.2 | ≈119 | −16% |
| 32 PHP names, 4 KiB | Clang | 20.5 | 21.8 | **21.8** | 29.2 | ≈125 | −5.4% |
| 32 PHP names, 64 KiB | GCC | 84.6 | 297 | **297** | 349 | 342 | −72% |
| 32 PHP names, 64 KiB | Clang | 99 | **279** | 279 | 338 | 356 | −64% |

**128 PHP names, prepared**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | `str_contains()` loop, second copy, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 128 PHP names, 128 B | GCC | 0.29 | 4.12 | 4.22 | 3.4 | **1.44** | −80% |
| 128 PHP names, 128 B | Clang | 0.29 | 4.04 | 4.08 | 3.34 | **1.43** | −80% |
| 128 PHP names, 1 KiB | GCC | 1.62 | 24.9 | 25.1 | 24.7 | **9.62** | −83% |
| 128 PHP names, 1 KiB | Clang | 1.81 | 23.5 | 23.7 | 24.7 | **9.57** | −81% |
| 128 PHP names, 4 KiB | GCC | 5.59 | 83.7 | 84.3 | 95.3 | **35.4** | −84% |
| 128 PHP names, 4 KiB | Clang | 6.56 | 79.1 | 79.1 | 93.7 | **35.7** | −82% |
| 128 PHP names, 64 KiB | GCC | 51.9 | 794 | 782 | ≈1,424 | **337** | −84% |
| 128 PHP names, 64 KiB | Clang | 62.1 | 742 | 740 | 917 | **336** | −82% |

**128 PHP names, one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | `str_contains()` loop, second copy, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 128 PHP names, 128 B | GCC | 57.7 | **4.19** | 4.23 | 15.2 | ≈427 | +1269%† |
| 128 PHP names, 128 B | Clang | 58.2 | **4.05** | 4.19 | 16.6 | ≈445 | +1312% |
| 128 PHP names, 1 KiB | GCC | 58.4 | 24.8 | **24.7** | 36.9 | ≈438 | +135% |
| 128 PHP names, 1 KiB | Clang | 58.4 | **23.8** | 24 | 38 | ≈455 | +149%† |
| 128 PHP names, 4 KiB | GCC | 64.1 | **83.6** | 84.2 | 107 | ≈456 | −23% |
| 128 PHP names, 4 KiB | Clang | 62.3 | **78.8** | 78.9 | 107 | ≈490 | −19% |
| 128 PHP names, 64 KiB | GCC | 111 | 789 | 793 | 946 | **763** | −85% |
| 128 PHP names, 64 KiB | Clang | 120 | 738 | **733** | 932 | 786 | −84% |

**512 PHP names, prepared**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | `str_contains()` loop, second copy, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 512 PHP names, 128 B | GCC | 0.31 | ≈15.9 | ≈16.1 | ≈28.8 | **2.35** | −87% |
| 512 PHP names, 128 B | Clang | 0.30 | ≈15.7 | ≈15.8 | ≈27.5 | **2.45** | −88% |
| 512 PHP names, 1 KiB | GCC | 1.58 | ≈92.6 | ≈93 | ≈195 | **13.5** | −88% |
| 512 PHP names, 1 KiB | Clang | 1.74 | ≈85.2 | ≈85.4 | ≈181 | **14.2** | −88% |
| 512 PHP names, 4 KiB | GCC | 4.53 | ≈308 | ≈309 | ≈537 | **41.4** | −89% |
| 512 PHP names, 4 KiB | Clang | 5.19 | ≈292 | ≈294 | ≈584 | **43.9** | −88% |
| 512 PHP names, 64 KiB | GCC | 12.1 | ≈1,021 | ≈1,017 | 1,942 | **116** | −90% |
| 512 PHP names, 64 KiB | Clang | 13.6 | ≈960 | ≈960 | 1,832 | **123** | −89% |

**512 PHP names, one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | `str_contains()` loop, second copy, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 512 PHP names, 128 B | GCC | 315 | **15.7** | 16 | 79.4 | ≈1,487 | +1901% |
| 512 PHP names, 128 B | Clang | 298 | **15.3** | 15.6 | ≈82.3 | ≈1,583 | +1848% |
| 512 PHP names, 1 KiB | GCC | 316 | **90.7** | 91.5 | 259 | ≈1,495 | +246% |
| 512 PHP names, 1 KiB | Clang | 298 | **85.7** | 86.3 | 255 | ≈1,599 | +246% |
| 512 PHP names, 4 KiB | GCC | 321 | 257 | **257** | 707 | ≈1,543 | +24% |
| 512 PHP names, 4 KiB | Clang | 306 | **242** | 244 | 703 | ≈1,639 | +27% |
| 512 PHP names, 64 KiB | GCC | 326 | 1,299 | **1,283** | 1,993 | 1,777 | −75% |
| 512 PHP names, 64 KiB | Clang | 314 | 1,202 | **1,198** | 1,883 | 1,841 | −74% |

**2048 PHP names, prepared**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | `str_contains()` loop, second copy, µs | PCRE alternation, µs | PCRE alternation in chunks of 1024, µs | PCRE alternation in chunks of 512, µs | PCRE, shared prefixes, µs | PCRE, shared prefixes in chunks of 1024, µs | PCRE, shared prefixes in chunks of 512, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2048 PHP names, 128 B | GCC | 0.30 | ≈50.7 | ≈51.3 | too large | ≈150 | ≈102 | **3.1** | 5 | 8.5 | −90% |
| 2048 PHP names, 128 B | Clang | 0.29 | ≈49.7 | ≈50.5 | too large | ≈150 | ≈101 | **2.99** | 4.98 | 8.58 | −90% |
| 2048 PHP names, 1 KiB | GCC | 0.90 | ≈187 | ≈186 | too large | ≈695 | ≈532 | **8.14** | 15.8 | 29.7 | −89% |
| 2048 PHP names, 1 KiB | Clang | 0.94 | ≈173 | ≈176 | too large | ≈678 | ≈499 | **7.94** | 15.4 | 30 | −88% |
| 2048 PHP names, 4 KiB | GCC | 1.1 | ≈311 | ≈311 | too large | ≈1,291 | ≈1,806 | **10.4** | 23.9 | ≈86.8 | −89% |
| 2048 PHP names, 4 KiB | Clang | 1.14 | ≈294 | ≈295 | too large | ≈1,234 | ≈1,699 | **10.1** | 22.8 | ≈89.2 | −89% |
| 2048 PHP names, 64 KiB | GCC | 1.07 | ≈2,447 | ≈2,456 | too large | ≈1,352 | ≈1,583 | **11.2** | 25.2 | ≈146 | −90% |
| 2048 PHP names, 64 KiB | Clang | 1.14 | ≈2,238 | ≈2,247 | too large | ≈1,255 | ≈1,623 | **10.9** | 24.3 | ≈152 | −89%† |

**2048 PHP names, one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | `str_contains()` loop, second copy, µs | PCRE alternation, µs | PCRE alternation in chunks of 1024, µs | PCRE alternation in chunks of 512, µs | PCRE, shared prefixes, µs | PCRE, shared prefixes in chunks of 1024, µs | PCRE, shared prefixes in chunks of 512, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2048 PHP names, 128 B | GCC | 1,303 | **50.6** | 51 | too large | ≈381 | ≈338 | ≈5,421 | ≈6,417 | ≈6,880 | +2475% |
| 2048 PHP names, 128 B | Clang | 1,267 | **49.1** | 49.8 | too large | ≈387 | ≈343 | ≈5,739 | ≈6,719 | ≈7,227 | +2503% |
| 2048 PHP names, 1 KiB | GCC | 1,296 | **194** | 196 | too large | 807 | 666 | ≈5,413 | ≈6,351 | ≈6,813 | +567% |
| 2048 PHP names, 1 KiB | Clang | 1,276 | **184** | 185 | too large | 793 | 652 | ≈5,760 | ≈6,749 | ≈7,242 | +590% |
| 2048 PHP names, 4 KiB | GCC | 1,304 | 367 | **363** | too large | ≈1,488 | ≈1,663 | ≈5,458 | ≈6,363 | ≈6,882 | +251% |
| 2048 PHP names, 4 KiB | Clang | 1,282 | **351** | 351 | too large | ≈1,480 | ≈1,568 | ≈5,828 | ≈6,692 | ≈7,162 | +265% |
| 2048 PHP names, 64 KiB | GCC | 1,307 | 1,476 | 1,479 | too large | **1,087** | 2,533 | 6,070 | 6,645 | 7,340 | +20%† |
| 2048 PHP names, 64 KiB | Clang | 1,262 | 1,385 | 1,381 | too large | **1,085** | 2,604 | 6,328 | 6,899 | ≈7,118 | +16%† |

### `getMatchedKeywords()`

**8 PHP names, prepared**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 8 PHP names, 128 B | GCC | 0.28 | **0.22** | 0.30 | 0.30 | +24% |
| 8 PHP names, 128 B | Clang | 0.28 | **0.21** | 0.29 | 0.30 | +32% |
| 8 PHP names, 1 KiB | GCC | 1.55 | 1.57 | **1.27** | 1.28 | +21% |
| 8 PHP names, 1 KiB | Clang | 1.79 | 1.5 | **1.28** | 1.28 | +40% |
| 8 PHP names, 4 KiB | GCC | 5.57 | 5.46 | 4.67 | **4.61** | +20% |
| 8 PHP names, 4 KiB | Clang | 6.6 | 5.1 | 4.61 | **4.58** | +44% |
| 8 PHP names, 64 KiB | GCC | 86.2 | 82.1 | 70.6 | **70.4** | +23% |
| 8 PHP names, 64 KiB | Clang | 104 | 75.9 | 69.5 | **69.5** | +49% |

**8 PHP names, one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 8 PHP names, 128 B | GCC | 3.86 | **0.30** | 1.41 | ≈27.2 | +1218% |
| 8 PHP names, 128 B | Clang | 3.83 | **0.29** | 1.48 | ≈28.6 | +1230% |
| 8 PHP names, 1 KiB | GCC | 5.11 | **1.68** | 2.38 | ≈28.2 | +206% |
| 8 PHP names, 1 KiB | Clang | 5.37 | **1.58** | 2.47 | ≈29.6 | +244% |
| 8 PHP names, 4 KiB | GCC | 9.12 | **5.53** | 5.7 | ≈31.8 | +64% |
| 8 PHP names, 4 KiB | Clang | 10.1 | **5.15** | 5.79 | ≈33.4 | +97% |
| 8 PHP names, 64 KiB | GCC | 89.7 | 81.8 | **71.9** | 97.3 | +25% |
| 8 PHP names, 64 KiB | Clang | 108 | 75.9 | **71.6** | 99.8 | +51% |

**32 PHP names, prepared**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 32 PHP names, 128 B | GCC | 0.28 | 1.04 | 1.07 | **0.90** | −68% |
| 32 PHP names, 128 B | Clang | 0.29 | 1.03 | 1.03 | **0.91** | −69% |
| 32 PHP names, 1 KiB | GCC | 1.59 | 6.78 | 7.23 | **5.71** | −72% |
| 32 PHP names, 1 KiB | Clang | 1.82 | 6.32 | 6.92 | **5.77** | −68% |
| 32 PHP names, 4 KiB | GCC | 5.79 | 23.3 | 28.1 | **21.5** | −73% |
| 32 PHP names, 4 KiB | Clang | 6.81 | **22** | 27 | 22.2 | −69% |
| 32 PHP names, 64 KiB | GCC | 88.7 | 352 | 440 | **336** | −73% |
| 32 PHP names, 64 KiB | Clang | 107 | **335** | 423 | 342 | −68% |

**32 PHP names, one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 32 PHP names, 128 B | GCC | 14.1 | **1.14** | 4.2 | ≈104 | +1144% |
| 32 PHP names, 128 B | Clang | 14.3 | **1.1** | 4.5 | ≈107 | +1197% |
| 32 PHP names, 1 KiB | GCC | 15.3 | **6.74** | 10.3 | ≈107 | +126% |
| 32 PHP names, 1 KiB | Clang | 16 | **6.43** | 10.4 | ≈112 | +147% |
| 32 PHP names, 4 KiB | GCC | 19.5 | **23.6** | 31.2 | ≈122 | −17% |
| 32 PHP names, 4 KiB | Clang | 20.8 | **21.9** | 30.5 | ≈129 | −5.9% |
| 32 PHP names, 64 KiB | GCC | 104 | **358** | 444 | 435 | −71% |
| 32 PHP names, 64 KiB | Clang | 121 | **333** | 423 | 451 | −64% |

**128 PHP names, prepared**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 128 PHP names, 128 B | GCC | 0.29 | 4.11 | 3.7 | **1.68** | −83% |
| 128 PHP names, 128 B | Clang | 0.30 | 4 | 3.7 | **1.66** | −82% |
| 128 PHP names, 1 KiB | GCC | 1.67 | 25.3 | 26.4 | **10.9** | −85% |
| 128 PHP names, 1 KiB | Clang | 1.89 | 24.2 | 26.8 | **10.5** | −82% |
| 128 PHP names, 4 KiB | GCC | 5.96 | 88.3 | 104 | **41.3** | −86% |
| 128 PHP names, 4 KiB | Clang | 7.06 | 84.3 | 106 | **39.9** | −82% |
| 128 PHP names, 64 KiB | GCC | 92.7 | 1,345 | 1,673 | **641** | −86% |
| 128 PHP names, 64 KiB | Clang | 109 | 1,274 | 1,685 | **617** | −82% |

**128 PHP names, one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 128 PHP names, 128 B | GCC | 57.5 | **4.16** | 15.6 | ≈422 | +1294% |
| 128 PHP names, 128 B | Clang | 58.8 | **4.13** | 17.1 | ≈450 | +1333%† |
| 128 PHP names, 1 KiB | GCC | 59.3 | **25.4** | 38.3 | ≈430 | +132% |
| 128 PHP names, 1 KiB | Clang | 58.3 | **24.2** | 40.1 | ≈460 | +140%† |
| 128 PHP names, 4 KiB | GCC | 63.2 | **89.4** | 116 | ≈465 | −29% |
| 128 PHP names, 4 KiB | Clang | 64.2 | **84.6** | 119 | ≈484 | −25% |
| 128 PHP names, 64 KiB | GCC | 153 | 1,355 | 1,681 | **1,073** | −86% |
| 128 PHP names, 64 KiB | Clang | 167 | 1,256 | 1,688 | **1,078** | −85% |

**512 PHP names, prepared**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 512 PHP names, 128 B | GCC | 0.33 | 16 | ≈31.6 | **3.41** | −90% |
| 512 PHP names, 128 B | Clang | 0.33 | 15.7 | ≈29.7 | **3.26** | −90% |
| 512 PHP names, 1 KiB | GCC | 1.85 | ≈105 | ≈239 | **21** | −91% |
| 512 PHP names, 1 KiB | Clang | 2.06 | ≈100 | ≈235 | **19.6** | −90% |
| 512 PHP names, 4 KiB | GCC | 6.57 | 367 | ≈924 | **79** | −92% |
| 512 PHP names, 4 KiB | Clang | 7.45 | 343 | ≈920 | **73.6** | −90% |
| 512 PHP names, 64 KiB | GCC | 97.8 | 5,585 | ≈12,715 | **1,209** | −92% |
| 512 PHP names, 64 KiB | Clang | 115 | 5,239 | ≈12,528 | **1,147** | −90% |

**512 PHP names, one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 512 PHP names, 128 B | GCC | 314 | **15.9** | 79.6 | ≈1,512 | +1854% |
| 512 PHP names, 128 B | Clang | 297 | **15.6** | ≈85.3 | ≈1,575 | +1803% |
| 512 PHP names, 1 KiB | GCC | 316 | **105** | 296 | ≈1,489 | +200% |
| 512 PHP names, 1 KiB | Clang | 301 | **99.6** | 294 | ≈1,611 | +205% |
| 512 PHP names, 4 KiB | GCC | 321 | **368** | 979 | 1,742 | −13% |
| 512 PHP names, 4 KiB | Clang | 304 | **344** | 992 | 1,822 | −11% |
| 512 PHP names, 64 KiB | GCC | 414 | 5,539 | ≈12,586 | **2,874** | −86% |
| 512 PHP names, 64 KiB | Clang | 420 | 5,223 | ≈12,570 | **2,871** | −86% |

**2048 PHP names, prepared**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE alternation in chunks of 1024, µs | PCRE alternation in chunks of 512, µs | PCRE, shared prefixes, µs | PCRE, shared prefixes in chunks of 1024, µs | PCRE, shared prefixes in chunks of 512, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2048 PHP names, 128 B | GCC | 0.40 | ≈62.6 | too large | ≈179 | ≈130 | **5.7** | 8.63 | 13.6 | −93% |
| 2048 PHP names, 128 B | Clang | 0.40 | ≈59.6 | too large | ≈172 | ≈128 | **5.74** | 8.56 | 13.5 | −93% |
| 2048 PHP names, 1 KiB | GCC | 2.19 | ≈396 | too large | ≈1,519 | ≈1,051 | **31.7** | 49.9 | 80.9 | −93% |
| 2048 PHP names, 1 KiB | Clang | 2.38 | ≈377 | too large | ≈1,437 | ≈1,009 | **31.7** | 49.8 | 78.6 | −92% |
| 2048 PHP names, 4 KiB | GCC | 7.8 | ≈1,477 | too large | ≈5,541 | ≈3,632 | **119** | 188 | 306 | −93% |
| 2048 PHP names, 4 KiB | Clang | 8.55 | ≈1,376 | too large | ≈5,166 | ≈3,500 | **118** | 186 | 294 | −93% |
| 2048 PHP names, 64 KiB | GCC | 113 | ≈21,771 | too large | ≈79,021 | ≈55,162 | **1,801** | 2,842 | 4,617 | −94% |
| 2048 PHP names, 64 KiB | Clang | 127 | ≈19,997 | too large | ≈75,644 | ≈53,427 | **1,785** | 2,822 | 4,488 | −93% |

**2048 PHP names, one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE alternation in chunks of 1024, µs | PCRE alternation in chunks of 512, µs | PCRE, shared prefixes, µs | PCRE, shared prefixes in chunks of 1024, µs | PCRE, shared prefixes in chunks of 512, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2048 PHP names, 128 B | GCC | 1,290 | **61.7** | too large | ≈427 | ≈371 | ≈5,616 | ≈6,475 | ≈6,915 | +1993% |
| 2048 PHP names, 128 B | Clang | 1,258 | **59.4** | too large | ≈422 | ≈371 | ≈5,850 | ≈6,763 | ≈7,172 | +2013% |
| 2048 PHP names, 1 KiB | GCC | 1,290 | **409** | too large | 1,560 | 1,187 | ≈5,571 | ≈6,372 | ≈6,910 | +216% |
| 2048 PHP names, 1 KiB | Clang | 1,268 | **394** | too large | 1,556 | 1,154 | ≈5,898 | ≈6,738 | ≈7,272 | +224% |
| 2048 PHP names, 4 KiB | GCC | 1,320 | **1,446** | too large | 5,488 | 3,875 | 6,261 | 6,910 | ≈7,177 | −9.4% |
| 2048 PHP names, 4 KiB | Clang | 1,291 | **1,362** | too large | 5,234 | 3,726 | 6,589 | ≈7,019 | ≈7,595 | −5.2% |
| 2048 PHP names, 64 KiB | GCC | 1,398 | 21,913 | too large | ≈80,180 | ≈56,859 | **7,919** | 9,513 | 11,785 | −82% |
| 2048 PHP names, 64 KiB | Clang | 1,386 | 20,479 | too large | ≈78,051 | ≈53,947 | **8,188** | 9,802 | 11,946 | −83% |

### `countMatches()`

**8 PHP names, prepared**

| Input | Compiler | New class, µs | `strpos()` loop, µs | `substr_count()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 8 PHP names, 128 B | GCC | 0.26 | 0.23 | 0.26 | **0.21** | 0.21 | +27% |
| 8 PHP names, 128 B | Clang | 0.27 | 0.24 | 0.26 | 0.21 | **0.20** | +32% |
| 8 PHP names, 1 KiB | GCC | 1.54 | 1.62 | 1.64 | 1.16 | **1.13** | +34% |
| 8 PHP names, 1 KiB | Clang | 1.76 | 1.52 | 1.52 | 1.17 | **1.11** | +58% |
| 8 PHP names, 4 KiB | GCC | 5.63 | 5.56 | 5.54 | 4.42 | **4.3** | +30% |
| 8 PHP names, 4 KiB | Clang | 6.63 | 5.12 | 5.11 | 4.44 | **4.22** | +58% |
| 8 PHP names, 64 KiB | GCC | 86.4 | 83.2 | 83.7 | 70.1 | **68** | +27% |
| 8 PHP names, 64 KiB | Clang | 105 | 79.4 | 78.6 | 70.6 | **67.6** | +56% |

**8 PHP names, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | `substr_count()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 8 PHP names, 128 B | GCC | 3.89 | **0.31** | 0.34 | 1.3 | ≈26.9 | +1156% |
| 8 PHP names, 128 B | Clang | 3.89 | **0.32** | 0.33 | 1.4 | ≈28.8 | +1150%† |
| 8 PHP names, 1 KiB | GCC | 5.17 | **1.69** | 1.74 | 2.25 | ≈27.8 | +208% |
| 8 PHP names, 1 KiB | Clang | 5.39 | **1.58** | 1.61 | 2.38 | ≈29.3 | +235% |
| 8 PHP names, 4 KiB | GCC | 9.16 | 5.54 | 5.5 | **5.45** | ≈31.3 | +68% |
| 8 PHP names, 4 KiB | Clang | 10.3 | 5.29 | **5.27** | 5.63 | ≈32.5 | +95% |
| 8 PHP names, 64 KiB | GCC | 90.4 | 85.5 | 85.3 | **71.6** | 95.1 | +27% |
| 8 PHP names, 64 KiB | Clang | 107 | 78.7 | 78 | **72** | 96.1 | +49% |

**32 PHP names, prepared**

| Input | Compiler | New class, µs | `strpos()` loop, µs | `substr_count()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 32 PHP names, 128 B | GCC | 0.27 | 1.09 | 1.2 | 0.99 | **0.80** | −66% |
| 32 PHP names, 128 B | Clang | 0.28 | 1.11 | 1.21 | 0.98 | **0.80** | −65% |
| 32 PHP names, 1 KiB | GCC | 1.57 | 6.7 | 6.83 | 7.13 | **5.49** | −71% |
| 32 PHP names, 1 KiB | Clang | 1.81 | 6.35 | 6.48 | 7.02 | **5.39** | −66% |
| 32 PHP names, 4 KiB | GCC | 5.78 | 23.4 | 23.6 | 27.9 | **21.2** | −73% |
| 32 PHP names, 4 KiB | Clang | 6.86 | 22.2 | 22.3 | 27.5 | **20.8** | −67% |
| 32 PHP names, 64 KiB | GCC | 89.4 | 361 | 359 | 445 | **336** | −73% |
| 32 PHP names, 64 KiB | Clang | 107 | 338 | 337 | 446 | **328** | −68% |

**32 PHP names, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | `substr_count()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 32 PHP names, 128 B | GCC | 14 | **1.17** | 1.28 | 4.09 | ≈101 | +1102% |
| 32 PHP names, 128 B | Clang | 14.4 | **1.19** | 1.27 | 4.38 | ≈108 | +1109% |
| 32 PHP names, 1 KiB | GCC | 15.5 | **6.81** | 6.93 | 10.3 | ≈107 | +128% |
| 32 PHP names, 1 KiB | Clang | 15.9 | **6.46** | 6.6 | 10.5 | ≈112 | +147% |
| 32 PHP names, 4 KiB | GCC | 19.6 | **23.8** | 23.9 | 31.3 | ≈123 | −17% |
| 32 PHP names, 4 KiB | Clang | 21 | 22.5 | **22.2** | 30.9 | ≈127 | −6.8% |
| 32 PHP names, 64 KiB | GCC | 103 | **358** | 363 | 450 | 437 | −72% |
| 32 PHP names, 64 KiB | Clang | 120 | **335** | 335 | 445 | 434 | −64% |

**128 PHP names, prepared**

| Input | Compiler | New class, µs | `strpos()` loop, µs | `substr_count()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 128 PHP names, 128 B | GCC | 0.28 | 4.19 | 4.63 | 3.57 | **1.53** | −81% |
| 128 PHP names, 128 B | Clang | 0.29 | 4.38 | 4.69 | 3.53 | **1.57** | −82% |
| 128 PHP names, 1 KiB | GCC | 1.65 | 25.8 | 26.1 | 26.4 | **10.3** | −84% |
| 128 PHP names, 1 KiB | Clang | 1.88 | 24.5 | 24.9 | 26.1 | **10.6** | −82% |
| 128 PHP names, 4 KiB | GCC | 5.94 | 89.5 | 89.4 | 104 | **38.8** | −85% |
| 128 PHP names, 4 KiB | Clang | 6.9 | 83.9 | 85 | 103 | **40** | −83% |
| 128 PHP names, 64 KiB | GCC | 91.8 | 1,369 | 1,369 | 1,668 | **613** | −85% |
| 128 PHP names, 64 KiB | Clang | 109 | 1,283 | 1,287 | 1,640 | **631** | −83% |

**128 PHP names, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | `substr_count()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 128 PHP names, 128 B | GCC | 57.1 | **4.27** | 4.74 | 15.3 | ≈422 | +1218%† |
| 128 PHP names, 128 B | Clang | 57 | **4.29** | 4.77 | 16.9 | ≈449 | +1207% |
| 128 PHP names, 1 KiB | GCC | 59.7 | **25.7** | 26 | 38.5 | ≈433 | +130%† |
| 128 PHP names, 1 KiB | Clang | 57.4 | **24.5** | 24.8 | 39.4 | ≈454 | +135% |
| 128 PHP names, 4 KiB | GCC | 62.8 | **89.6** | 89.8 | 117 | ≈454 | −30% |
| 128 PHP names, 4 KiB | Clang | 63.8 | 84 | **83.9** | 117 | ≈492 | −24% |
| 128 PHP names, 64 KiB | GCC | 151 | 1,368 | 1,369 | 1,680 | **1,041** | −85% |
| 128 PHP names, 64 KiB | Clang | 167 | 1,289 | 1,288 | 1,659 | **1,088** | −85% |

**512 PHP names, prepared**

| Input | Compiler | New class, µs | `strpos()` loop, µs | `substr_count()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 512 PHP names, 128 B | GCC | 0.31 | ≈16.8 | ≈18.2 | ≈31.3 | **2.93** | −89% |
| 512 PHP names, 128 B | Clang | 0.31 | ≈17.3 | ≈18.3 | ≈29.9 | **3.05** | −90%† |
| 512 PHP names, 1 KiB | GCC | 1.8 | ≈107 | ≈108 | ≈222 | **18.4** | −90% |
| 512 PHP names, 1 KiB | Clang | 2 | ≈102 | ≈103 | ≈220 | **19.4** | −90% |
| 512 PHP names, 4 KiB | GCC | 6.53 | ≈360 | ≈362 | ≈955 | **69.2** | −91% |
| 512 PHP names, 4 KiB | Clang | 7.4 | 349 | 348 | ≈972 | **73.1** | −90% |
| 512 PHP names, 64 KiB | GCC | 99.2 | ≈5,516 | ≈5,540 | ≈14,492 | **1,072** | −91% |
| 512 PHP names, 64 KiB | Clang | 116 | 5,339 | 5,324 | ≈14,049 | **1,157** | −90% |

**512 PHP names, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | `substr_count()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 512 PHP names, 128 B | GCC | 314 | **16.4** | 18 | 81 | ≈1,502 | +1803% |
| 512 PHP names, 128 B | Clang | 300 | **16.4** | 18.2 | ≈82.5 | ≈1,576 | +1718%† |
| 512 PHP names, 1 KiB | GCC | 317 | **105** | 107 | 298 | ≈1,509 | +200% |
| 512 PHP names, 1 KiB | Clang | 298 | **101** | 103 | 293 | ≈1,603 | +197% |
| 512 PHP names, 4 KiB | GCC | 321 | **368** | 370 | 985 | 1,720 | −13% |
| 512 PHP names, 4 KiB | Clang | 306 | 349 | **349** | 1,008 | 1,787 | −12% |
| 512 PHP names, 64 KiB | GCC | 419 | 5,700 | 5,720 | ≈14,424 | **2,760** | −85% |
| 512 PHP names, 64 KiB | Clang | 416 | 5,351 | 5,374 | ≈14,329 | **2,883** | −86% |

**2048 PHP names, prepared**

| Input | Compiler | New class, µs | `strpos()` loop, µs | `substr_count()` loop, µs | PCRE alternation, µs | PCRE alternation in chunks of 1024, µs | PCRE alternation in chunks of 512, µs | PCRE, shared prefixes, µs | PCRE, shared prefixes in chunks of 1024, µs | PCRE, shared prefixes in chunks of 512, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2048 PHP names, 128 B | GCC | 0.35 | ≈63.2 | ≈69.6 | too large | ≈170 | ≈121 | **5.38** | 7.97 | 12.5 | −93% |
| 2048 PHP names, 128 B | Clang | 0.35 | ≈66.3 | ≈70.2 | too large | ≈172 | ≈119 | **5.43** | 8.06 | 12.7 | −93% |
| 2048 PHP names, 1 KiB | GCC | 2.06 | ≈412 | ≈421 | too large | ≈1,140 | ≈883 | **31** | 47.9 | 75.9 | −93% |
| 2048 PHP names, 1 KiB | Clang | 2.23 | ≈392 | ≈398 | too large | ≈1,112 | ≈878 | **31** | 48 | 77.7 | −93% |
| 2048 PHP names, 4 KiB | GCC | 7.32 | ≈1,458 | ≈1,462 | too large | ≈4,861 | ≈3,255 | **115** | 179 | 284 | −94% |
| 2048 PHP names, 4 KiB | Clang | 8.09 | ≈1,390 | ≈1,396 | too large | ≈4,914 | ≈3,335 | **115** | 178 | 288 | −93% |
| 2048 PHP names, 64 KiB | GCC | 108 | ≈21,923 | ≈22,158 | too large | ≈76,363 | ≈50,905 | **1,715** | 2,680 | 4,229 | −94% |
| 2048 PHP names, 64 KiB | Clang | 121 | ≈20,782 | ≈20,578 | too large | ≈75,705 | ≈51,515 | **1,750** | 2,682 | 4,345 | −93% |

**2048 PHP names, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | `substr_count()` loop, µs | PCRE alternation, µs | PCRE alternation in chunks of 1024, µs | PCRE alternation in chunks of 512, µs | PCRE, shared prefixes, µs | PCRE, shared prefixes in chunks of 1024, µs | PCRE, shared prefixes in chunks of 512, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2048 PHP names, 128 B | GCC | 1,306 | **63.7** | 71.1 | too large | ≈396 | ≈344 | ≈5,462 | ≈6,387 | ≈6,792 | +1956% |
| 2048 PHP names, 128 B | Clang | 1,285 | **64.5** | 72.5 | too large | ≈409 | ≈353 | ≈5,903 | ≈6,748 | ≈7,193 | +1896% |
| 2048 PHP names, 1 KiB | GCC | 1,300 | **415** | 418 | too large | 1,544 | 1,105 | ≈5,595 | ≈6,497 | ≈7,011 | +215% |
| 2048 PHP names, 1 KiB | Clang | 1,267 | **399** | 404 | too large | 1,541 | 1,114 | ≈6,052 | ≈6,799 | ≈7,313 | +219% |
| 2048 PHP names, 4 KiB | GCC | 1,314 | **1,461** | 1,463 | too large | 5,430 | 3,559 | 6,230 | 6,835 | 7,443 | −11% |
| 2048 PHP names, 4 KiB | Clang | 1,286 | **1,369** | 1,383 | too large | 5,307 | 3,553 | 6,547 | ≈6,946 | ≈7,517 | −6.6% |
| 2048 PHP names, 64 KiB | GCC | 1,403 | 22,273 | 22,311 | too large | ≈77,923 | ≈53,091 | **7,886** | 9,309 | 11,488 | −82% |
| 2048 PHP names, 64 KiB | Clang | 1,402 | 21,018 | 20,969 | too large | ≈76,740 | ≈51,702 | **8,229** | 9,708 | 11,851 | −83% |

### `matchAll()`

**8 PHP names, prepared**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 8 PHP names, 128 B | GCC | 0.27 | **0.23** | 0.33 | 0.33 | +17% |
| 8 PHP names, 128 B | Clang | 0.27 | **0.23** | 0.31 | 0.32 | +19%† |
| 8 PHP names, 1 KiB | GCC | 1.55 | 1.62 | 1.32 | **1.3** | +19% |
| 8 PHP names, 1 KiB | Clang | 1.77 | 1.49 | **1.27** | 1.28 | +37% |
| 8 PHP names, 4 KiB | GCC | 5.54 | 5.48 | 4.76 | **4.73** | +18% |
| 8 PHP names, 4 KiB | Clang | 6.67 | 5.2 | 4.7 | **4.69** | +42% |
| 8 PHP names, 64 KiB | GCC | 85.8 | 82.9 | 72.1 | **71.3** | +21% |
| 8 PHP names, 64 KiB | Clang | 103 | 77.4 | 71 | **69.9** | +47% |

**8 PHP names, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 8 PHP names, 128 B | GCC | 3.91 | **0.30** | 1.42 | ≈27.6 | +1174% |
| 8 PHP names, 128 B | Clang | 3.89 | **0.31** | 1.51 | ≈29 | +1175%† |
| 8 PHP names, 1 KiB | GCC | 5.18 | **1.69** | 2.39 | ≈28.2 | +206% |
| 8 PHP names, 1 KiB | Clang | 5.41 | **1.6** | 2.51 | ≈29.9 | +238% |
| 8 PHP names, 4 KiB | GCC | 9.28 | **5.65** | 5.82 | ≈32 | +64% |
| 8 PHP names, 4 KiB | Clang | 10.1 | **5.18** | 5.79 | ≈32.9 | +95% |
| 8 PHP names, 64 KiB | GCC | 89.6 | 83.5 | **72.1** | 97.8 | +24% |
| 8 PHP names, 64 KiB | Clang | 107 | 77.3 | **72.3** | 98.8 | +49% |

**32 PHP names, prepared**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 32 PHP names, 128 B | GCC | 0.28 | 1.08 | 1.1 | **0.92** | −70% |
| 32 PHP names, 128 B | Clang | 0.28 | 1.1 | 1.05 | **0.93** | −70% |
| 32 PHP names, 1 KiB | GCC | 1.6 | 6.66 | 7.22 | **5.66** | −72%† |
| 32 PHP names, 1 KiB | Clang | 1.83 | 6.46 | 6.91 | **5.74** | −68% |
| 32 PHP names, 4 KiB | GCC | 5.81 | 23.4 | 27.6 | **21.3** | −73% |
| 32 PHP names, 4 KiB | Clang | 6.89 | 22.3 | 26.8 | **21.7** | −69% |
| 32 PHP names, 64 KiB | GCC | 89.9 | 361 | 441 | **335** | −73% |
| 32 PHP names, 64 KiB | Clang | 107 | **336** | 424 | 342 | −68% |

**32 PHP names, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 32 PHP names, 128 B | GCC | 14 | **1.16** | 4.21 | ≈103 | +1119%† |
| 32 PHP names, 128 B | Clang | 14.3 | **1.2** | 4.51 | ≈108 | +1093% |
| 32 PHP names, 1 KiB | GCC | 15.4 | **6.86** | 10.3 | ≈107 | +125% |
| 32 PHP names, 1 KiB | Clang | 16.1 | **6.56** | 10.3 | ≈113 | +146% |
| 32 PHP names, 4 KiB | GCC | 19.6 | **23.6** | 30.9 | ≈122 | −17% |
| 32 PHP names, 4 KiB | Clang | 20.8 | **22.4** | 30.3 | ≈130 | −6.5% |
| 32 PHP names, 64 KiB | GCC | 103 | **361** | 445 | 437 | −71% |
| 32 PHP names, 64 KiB | Clang | 121 | **335** | 429 | 451 | −64% |

**128 PHP names, prepared**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 128 PHP names, 128 B | GCC | 0.29 | 4.25 | 3.73 | **1.74** | −83% |
| 128 PHP names, 128 B | Clang | 0.29 | 4.34 | 3.74 | **1.68** | −83% |
| 128 PHP names, 1 KiB | GCC | 1.65 | 25.6 | 26.5 | **10.9** | −85% |
| 128 PHP names, 1 KiB | Clang | 1.87 | 24.5 | 26.9 | **10.5** | −82% |
| 128 PHP names, 4 KiB | GCC | 6 | 89.3 | 104 | **41.4** | −85% |
| 128 PHP names, 4 KiB | Clang | 7.06 | 84 | 105 | **39.8** | −82% |
| 128 PHP names, 64 KiB | GCC | 92.9 | 1,379 | 1,674 | **650** | −86% |
| 128 PHP names, 64 KiB | Clang | 109 | 1,292 | 1,697 | **621** | −82% |

**128 PHP names, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 128 PHP names, 128 B | GCC | 56.7 | **4.36** | 15.5 | ≈429 | +1206%† |
| 128 PHP names, 128 B | Clang | 57.5 | **4.42** | 17.1 | ≈451 | +1180%† |
| 128 PHP names, 1 KiB | GCC | 58.9 | **25.9** | 38.3 | ≈438 | +127% |
| 128 PHP names, 1 KiB | Clang | 58.1 | **24.7** | 39.8 | ≈462 | +136% |
| 128 PHP names, 4 KiB | GCC | 64 | **90.1** | 116 | ≈472 | −28% |
| 128 PHP names, 4 KiB | Clang | 65.6 | **84.8** | 119 | ≈492 | −22%† |
| 128 PHP names, 64 KiB | GCC | 153 | 1,377 | 1,685 | **1,083** | −86% |
| 128 PHP names, 64 KiB | Clang | 169 | 1,293 | 1,706 | **1,084** | −84% |

**512 PHP names, prepared**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 512 PHP names, 128 B | GCC | 0.33 | 16.4 | ≈31.6 | **3.4** | −90% |
| 512 PHP names, 128 B | Clang | 0.32 | ≈17.1 | ≈31.4 | **3.24** | −90% |
| 512 PHP names, 1 KiB | GCC | 1.86 | ≈107 | ≈237 | **21** | −91% |
| 512 PHP names, 1 KiB | Clang | 2 | ≈102 | ≈237 | **19.6** | −90% |
| 512 PHP names, 4 KiB | GCC | 6.68 | 366 | ≈955 | **79.2** | −92% |
| 512 PHP names, 4 KiB | Clang | 7.54 | 347 | ≈994 | **74.6** | −90% |
| 512 PHP names, 64 KiB | GCC | 104 | 5,657 | ≈15,479 | **1,250** | −92% |
| 512 PHP names, 64 KiB | Clang | 120 | 5,317 | ≈15,304 | **1,165** | −90% |

**512 PHP names, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 512 PHP names, 128 B | GCC | 312 | **16.6** | 79.6 | ≈1,505 | +1784% |
| 512 PHP names, 128 B | Clang | 299 | **17.1** | ≈84.8 | ≈1,598 | +1644%† |
| 512 PHP names, 1 KiB | GCC | 316 | **106** | 295 | ≈1,536 | +199% |
| 512 PHP names, 1 KiB | Clang | 301 | **100** | 297 | ≈1,637 | +202% |
| 512 PHP names, 4 KiB | GCC | 320 | **370** | 1,008 | 1,742 | −14% |
| 512 PHP names, 4 KiB | Clang | 307 | **348** | 1,032 | 1,811 | −11% |
| 512 PHP names, 64 KiB | GCC | 421 | 5,673 | ≈15,911 | **2,938** | −86% |
| 512 PHP names, 64 KiB | Clang | 425 | 5,326 | ≈15,665 | **2,916** | −86% |

**2048 PHP names, prepared**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE alternation in chunks of 1024, µs | PCRE alternation in chunks of 512, µs | PCRE, shared prefixes, µs | PCRE, shared prefixes in chunks of 1024, µs | PCRE, shared prefixes in chunks of 512, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2048 PHP names, 128 B | GCC | 0.40 | ≈66.3 | too large | ≈184 | ≈133 | **5.74** | 8.64 | 13.7 | −93% |
| 2048 PHP names, 128 B | Clang | 0.40 | ≈66.6 | too large | ≈173 | ≈128 | **5.66** | 8.54 | 13.5 | −93% |
| 2048 PHP names, 1 KiB | GCC | 2.35 | ≈420 | too large | ≈1,409 | ≈1,009 | **32.1** | 50.4 | 81.6 | −93% |
| 2048 PHP names, 1 KiB | Clang | 2.54 | ≈400 | too large | ≈1,370 | ≈963 | **31.8** | 50 | 79.7 | −92% |
| 2048 PHP names, 4 KiB | GCC | 8.49 | ≈1,368 | too large | ≈4,560 | ≈3,166 | **120** | 187 | 304 | −93% |
| 2048 PHP names, 4 KiB | Clang | 9.43 | ≈1,294 | too large | ≈4,365 | ≈2,999 | **120** | 187 | 296 | −92% |
| 2048 PHP names, 64 KiB | GCC | 131 | ≈21,993 | too large | ≈74,329 | ≈53,649 | **1,881** | 2,958 | 4,757 | −93% |
| 2048 PHP names, 64 KiB | Clang | 146 | ≈20,586 | too large | ≈69,933 | ≈50,942 | **1,865** | 2,926 | 4,582 | −92% |

**2048 PHP names, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE alternation in chunks of 1024, µs | PCRE alternation in chunks of 512, µs | PCRE, shared prefixes, µs | PCRE, shared prefixes in chunks of 1024, µs | PCRE, shared prefixes in chunks of 512, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2048 PHP names, 128 B | GCC | 1,281 | **63.9** | too large | ≈442 | ≈386 | ≈5,634 | ≈6,507 | ≈6,949 | +1917% |
| 2048 PHP names, 128 B | Clang | 1,263 | **62.6** | too large | ≈439 | ≈386 | ≈5,947 | ≈6,785 | ≈7,165 | +1899% |
| 2048 PHP names, 1 KiB | GCC | 1,302 | **416** | too large | 1,609 | 1,169 | ≈5,668 | ≈6,513 | ≈7,034 | +213% |
| 2048 PHP names, 1 KiB | Clang | 1,264 | **396** | too large | 1,565 | 1,151 | ≈5,972 | ≈6,747 | ≈7,294 | +220% |
| 2048 PHP names, 4 KiB | GCC | 1,316 | **1,472** | too large | 5,495 | 3,865 | 6,255 | 6,902 | ≈7,160 | −11% |
| 2048 PHP names, 4 KiB | Clang | 1,291 | **1,385** | too large | 5,304 | 3,710 | 6,594 | ≈6,968 | ≈7,537 | −7.6% |
| 2048 PHP names, 64 KiB | GCC | 1,425 | 22,491 | too large | ≈72,498 | ≈54,849 | **8,060** | 9,508 | 11,902 | −82% |
| 2048 PHP names, 64 KiB | Clang | 1,423 | 21,178 | too large | ≈70,934 | ≈51,026 | **8,341** | 9,943 | 12,106 | −83% |

### `replace()`

**8 PHP names, prepared**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 8 PHP names, 128 B | GCC | 0.28 | 0.78 | **0.21** | 0.22 | +32% |
| 8 PHP names, 128 B | Clang | 0.27 | 0.74 | 0.21 | **0.20** | +30% |
| 8 PHP names, 1 KiB | GCC | 1.58 | ≈6.61 | 1.15 | **1.14** | +37% |
| 8 PHP names, 1 KiB | Clang | 1.73 | ≈6.39 | **1.12** | 1.13 | +53% |
| 8 PHP names, 4 KiB | GCC | 5.66 | ≈25.5 | **4.31** | 4.31 | +31% |
| 8 PHP names, 4 KiB | Clang | 6.46 | ≈24.7 | 4.25 | **4.25** | +50% |
| 8 PHP names, 64 KiB | GCC | 87.6 | ≈415 | 67.4 | **67** | +30% |
| 8 PHP names, 64 KiB | Clang | 100 | ≈398 | **65.9** | 66.4 | +52% |

**8 PHP names, one-shot**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 8 PHP names, 128 B | GCC | 4.29 | **0.85** | 1.38 | ≈27.4 | +406% |
| 8 PHP names, 128 B | Clang | 4.37 | **0.81** | 1.44 | ≈29 | +437% |
| 8 PHP names, 1 KiB | GCC | 5.64 | 6.66 | **2.3** | ≈28 | +143% |
| 8 PHP names, 1 KiB | Clang | 5.9 | 6.47 | **2.36** | ≈29.9 | +148%† |
| 8 PHP names, 4 KiB | GCC | 9.63 | 26.2 | **5.45** | ≈31.1 | +76% |
| 8 PHP names, 4 KiB | Clang | 10.5 | 25.3 | **5.49** | ≈32.8 | +92% |
| 8 PHP names, 64 KiB | GCC | 90.9 | ≈406 | **68.9** | 94.3 | +33% |
| 8 PHP names, 64 KiB | Clang | 105 | ≈397 | **67.9** | 96 | +55% |

**32 PHP names, prepared**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 32 PHP names, 128 B | GCC | 0.29 | ≈9.46 | 0.98 | **0.76** | −62% |
| 32 PHP names, 128 B | Clang | 0.28 | ≈9.48 | 0.95 | **0.77** | −64% |
| 32 PHP names, 1 KiB | GCC | 1.67 | ≈87.8 | 7.09 | **5.11** | −67% |
| 32 PHP names, 1 KiB | Clang | 1.8 | ≈88.8 | 6.79 | **5.22** | −66% |
| 32 PHP names, 4 KiB | GCC | 5.97 | ≈369 | 27.9 | **19.5** | −69% |
| 32 PHP names, 4 KiB | Clang | 6.76 | ≈373 | 26.8 | **20.2** | −67% |
| 32 PHP names, 64 KiB | GCC | 92.5 | ≈5,854 | 441 | **301** | −69% |
| 32 PHP names, 64 KiB | Clang | 105 | ≈5,907 | 413 | **308** | −66% |

**32 PHP names, one-shot**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 32 PHP names, 128 B | GCC | 15.4 | ≈9.43 | **4.15** | ≈101 | +271% |
| 32 PHP names, 128 B | Clang | 15.6 | ≈9.44 | **4.35** | ≈106 | +261% |
| 32 PHP names, 1 KiB | GCC | 16.7 | ≈86.1 | **10.3** | ≈105 | +62%† |
| 32 PHP names, 1 KiB | Clang | 17.2 | ≈88.1 | **10.2** | ≈111 | +69% |
| 32 PHP names, 4 KiB | GCC | 21 | ≈370 | **31.1** | ≈121 | −33% |
| 32 PHP names, 4 KiB | Clang | 22.3 | ≈379 | **30.2** | ≈127 | −26% |
| 32 PHP names, 64 KiB | GCC | 108 | ≈5,874 | 444 | **403** | −74% |
| 32 PHP names, 64 KiB | Clang | 120 | ≈5,869 | **418** | 420 | −71% |

**128 PHP names, prepared**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 128 PHP names, 128 B | GCC | 0.32 | ≈22.2 | 3.46 | **1.44** | −78% |
| 128 PHP names, 128 B | Clang | 0.31 | ≈23.3 | 3.3 | **1.46** | −79% |
| 128 PHP names, 1 KiB | GCC | 1.86 | ≈212 | 26.4 | **9.79** | −81% |
| 128 PHP names, 1 KiB | Clang | 2.01 | ≈218 | 24.8 | **9.9** | −80% |
| 128 PHP names, 4 KiB | GCC | 6.84 | ≈810 | 105 | **37.7** | −82% |
| 128 PHP names, 4 KiB | Clang | 7.48 | ≈825 | 98 | **37.9** | −80% |
| 128 PHP names, 64 KiB | GCC | 105 | ≈13,830 | 1,673 | **582** | −82% |
| 128 PHP names, 64 KiB | Clang | 116 | ≈14,305 | 1,571 | **588** | −80% |

**128 PHP names, one-shot**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 128 PHP names, 128 B | GCC | 69.5 | ≈22.4 | **15.2** | ≈421 | +362%† |
| 128 PHP names, 128 B | Clang | 68.9 | ≈23.3 | **16.4** | ≈453 | +322%† |
| 128 PHP names, 1 KiB | GCC | 71 | ≈211 | **38.2** | ≈427 | +86%† |
| 128 PHP names, 1 KiB | Clang | 70.6 | ≈215 | **38** | ≈457 | +85%† |
| 128 PHP names, 4 KiB | GCC | 75.1 | ≈810 | **116** | ≈465 | −35%† |
| 128 PHP names, 4 KiB | Clang | 77.2 | ≈825 | **111** | ≈479 | −30%† |
| 128 PHP names, 64 KiB | GCC | 174 | ≈13,937 | 1,682 | **1,023** | −83% |
| 128 PHP names, 64 KiB | Clang | 188 | ≈14,304 | 1,587 | **1,047** | −82% |

**512 PHP names, prepared**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 512 PHP names, 128 B | GCC | 0.40 | ≈34 | ≈26 | **2.42** | −83% |
| 512 PHP names, 128 B | Clang | 0.40 | ≈35.5 | ≈26 | **2.56** | −84%† |
| 512 PHP names, 1 KiB | GCC | 2.41 | ≈349 | ≈201 | **15.5** | −84% |
| 512 PHP names, 1 KiB | Clang | 2.53 | ≈352 | ≈214 | **16.3** | −84% |
| 512 PHP names, 4 KiB | GCC | 8.86 | ≈1,275 | ≈836 | **59.3** | −85% |
| 512 PHP names, 4 KiB | Clang | 9.5 | ≈1,308 | ≈835 | **62.5** | −85% |
| 512 PHP names, 64 KiB | GCC | 132 | ≈21,345 | ≈14,089 | **904** | −86% |
| 512 PHP names, 64 KiB | Clang | 143 | ≈22,048 | ≈14,305 | **966** | −85% |

**512 PHP names, one-shot**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 512 PHP names, 128 B | GCC | 449 | **34.5** | ≈77.2 | ≈1,492 | +1192% |
| 512 PHP names, 128 B | Clang | 434 | **35.7** | ≈82.3 | ≈1,570 | +1108% |
| 512 PHP names, 1 KiB | GCC | 448 | 328 | **272** | ≈1,502 | +64% |
| 512 PHP names, 1 KiB | Clang | 431 | 336 | **301** | ≈1,613 | +43%† |
| 512 PHP names, 4 KiB | GCC | 459 | 1,363 | **927** | 1,729 | −51% |
| 512 PHP names, 4 KiB | Clang | 441 | 1,388 | **949** | 1,812 | −54%† |
| 512 PHP names, 64 KiB | GCC | 583 | ≈21,716 | ≈14,397 | **2,574** | −77% |
| 512 PHP names, 64 KiB | Clang | 578 | ≈21,901 | ≈14,223 | **2,705** | −79% |

**2048 PHP names, prepared**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 2048 PHP names, 128 B | GCC | 0.54 | ≈49.3 | too large | **3.76** | −86% |
| 2048 PHP names, 128 B | Clang | 0.53 | ≈51.6 | too large | **3.68** | −86% |
| 2048 PHP names, 1 KiB | GCC | 3.26 | ≈449 | too large | **20.4** | −84% |
| 2048 PHP names, 1 KiB | Clang | 3.37 | ≈479 | too large | **19.6** | −83% |
| 2048 PHP names, 4 KiB | GCC | 11.6 | ≈1,947 | too large | **75.6** | −85% |
| 2048 PHP names, 4 KiB | Clang | 12.5 | ≈2,021 | too large | **72.9** | −83% |
| 2048 PHP names, 64 KiB | GCC | 169 | ≈29,922 | too large | **1,170** | −86% |
| 2048 PHP names, 64 KiB | Clang | 178 | ≈31,337 | too large | **1,114** | −84% |

**2048 PHP names, one-shot**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 2048 PHP names, 128 B | GCC | 2,532 | **49.3** | too large | ≈5,151 | +5049% |
| 2048 PHP names, 128 B | Clang | 2,449 | **52.1** | too large | ≈5,473 | +4614% |
| 2048 PHP names, 1 KiB | GCC | 2,511 | **461** | too large | ≈5,134 | +443% |
| 2048 PHP names, 1 KiB | Clang | 2,455 | **485** | too large | ≈5,524 | +408% |
| 2048 PHP names, 4 KiB | GCC | 3,544 | **1,872** | too large | 6,147 | +88% |
| 2048 PHP names, 4 KiB | Clang | 3,480 | **1,965** | too large | ≈5,678 | +75% |
| 2048 PHP names, 64 KiB | GCC | 2,678 | 30,045 | too large | **7,283** | −63% |
| 2048 PHP names, 64 KiB | Clang | 2,643 | 31,441 | too large | **7,564** | −65% |

## Crossover lengths

### `matches()`

**16 keys, one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | `str_contains()` loop, second copy, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 16 keys, 1536 B, no occurrence | GCC | 6.34 | **5.07** | 5.1 | 6.33 | ≈36.4 | +25% |
| 16 keys, 1536 B, no occurrence | Clang | 6.66 | **4.83** | 4.87 | 6.18 | ≈37.9 | +38% |
| 16 keys, 2 KiB, no occurrence | GCC | 7.01 | **6.55** | 6.6 | 7.95 | ≈38.3 | +6.8% |
| 16 keys, 2 KiB, no occurrence | Clang | 7.47 | **6.25** | 6.29 | 7.75 | ≈39.9 | +19% |
| 16 keys, 3 KiB, no occurrence | GCC | 8.4 | **9.55** | 9.62 | 11.2 | 41.5 | −12% |
| 16 keys, 3 KiB, no occurrence | Clang | 9.1 | **9.09** | 9.14 | 11 | 43.1 | +0.1% |
| 16 keys, 1536 B, one occurrence in the middle third | GCC | 5.38 | **2.73** | 2.77 | 3.85 | ≈34.1 | +96% |
| 16 keys, 1536 B, one occurrence in the middle third | Clang | 5.48 | **2.61** | 2.64 | 3.7 | ≈35.7 | +111% |
| 16 keys, 2 KiB, one occurrence in the middle third | GCC | 5.7 | **3.49** | 3.53 | 4.64 | ≈35.1 | +63% |
| 16 keys, 2 KiB, one occurrence in the middle third | Clang | 5.87 | **3.34** | 3.37 | 4.48 | ≈36.3 | +76% |
| 16 keys, 3 KiB, one occurrence in the middle third | GCC | 6.39 | **5.07** | 5.11 | 6.34 | ≈36.5 | +25% |
| 16 keys, 3 KiB, one occurrence in the middle third | Clang | 6.7 | **4.84** | 4.89 | 6.19 | ≈38.5 | +38% |

**32 keys, one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | `str_contains()` loop, second copy, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 32 keys, 1536 B, no occurrence | GCC | 9.93 | **11.1** | 11.2 | 11.2 | ≈66.7 | −10% |
| 32 keys, 1536 B, no occurrence | Clang | 10.3 | **10.5** | 10.6 | 10.6 | ≈69.9 | −2.9% |
| 32 keys, 2 KiB, no occurrence | GCC | 10.7 | 14.4 | 14.6 | **14.3** | 69.9 | −25% |
| 32 keys, 2 KiB, no occurrence | Clang | 11 | 13.8 | 13.9 | **13.5** | ≈74.4 | −18% |
| 32 keys, 3 KiB, no occurrence | GCC | 12 | 21.2 | 21.3 | **20.4** | 75.1 | −41% |
| 32 keys, 3 KiB, no occurrence | Clang | 12.6 | 20.2 | 20.3 | **19.4** | 79.1 | −35% |
| 32 keys, 1536 B, one occurrence in the middle third | GCC | 9.05 | **5.35** | 5.4 | 6.61 | ≈63.2 | +69% |
| 32 keys, 1536 B, one occurrence in the middle third | Clang | 9.08 | **5.05** | 5.12 | 6.18 | ≈66.5 | +79%† |
| 32 keys, 2 KiB, one occurrence in the middle third | GCC | 9.34 | **6.89** | 6.96 | 8.09 | ≈63.8 | +35% |
| 32 keys, 2 KiB, one occurrence in the middle third | Clang | 9.58 | **6.6** | 6.64 | 7.59 | ≈67.8 | +45% |
| 32 keys, 3 KiB, one occurrence in the middle third | GCC | 10 | **10.1** | 10.2 | 11.2 | ≈67 | −1.2% |
| 32 keys, 3 KiB, one occurrence in the middle third | Clang | 10.3 | **9.63** | 9.7 | 10.5 | ≈69.8 | +6.6% |
| 32 PHP names, 1536 B | GCC | 15.9 | **9.15** | 9.44 | 13.4 | ≈108 | +70% |
| 32 PHP names, 1536 B | Clang | 16.6 | **8.86** | 8.88 | 13.3 | ≈112 | +88% |
| 32 PHP names, 2 KiB | GCC | 16.5 | **11.8** | 12 | 16.5 | ≈109 | +38% |
| 32 PHP names, 2 KiB | Clang | 17.4 | **11.4** | 11.4 | 16.3 | ≈115 | +53% |
| 32 PHP names, 3 KiB | GCC | 18 | 17.6 | **17.6** | 23.3 | ≈114 | +3.3%† |
| 32 PHP names, 3 KiB | Clang | 18.7 | 16.6 | **16.5** | 22.3 | ≈121 | +16% |

**128 keys, one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | `str_contains()` loop, second copy, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 128 keys, 1536 B, no occurrence | GCC | 32.8 | 43.3 | 43.7 | **37.8** | ≈227 | −13% |
| 128 keys, 1536 B, no occurrence | Clang | 32.9 | 41.5 | 41.9 | **37.8** | ≈239 | −13% |
| 128 keys, 2 KiB, no occurrence | GCC | 33.6 | 56.9 | 57.4 | **48.9** | 235 | −31% |
| 128 keys, 2 KiB, no occurrence | Clang | 33.8 | 54.6 | 55 | **48.9** | ≈247 | −31% |
| 128 keys, 3 KiB, no occurrence | GCC | 35.1 | 82.6 | 82.8 | **68.5** | 237 | −49% |
| 128 keys, 3 KiB, no occurrence | Clang | 35.7 | 79.4 | 79.6 | **69.5** | 254 | −49% |
| 128 keys, 1536 B, one occurrence in the middle third | GCC | 31.7 | 22.6 | 22.9 | **22.3** | ≈223 | +42% |
| 128 keys, 1536 B, one occurrence in the middle third | Clang | 31.8 | **21.6** | 21.9 | 21.9 | ≈235 | +47% |
| 128 keys, 2 KiB, one occurrence in the middle third | GCC | 32.1 | 29.3 | 29.6 | **27.1** | ≈229 | +19% |
| 128 keys, 2 KiB, one occurrence in the middle third | Clang | 32 | 28.1 | 28.4 | **27** | ≈233 | +18% |
| 128 keys, 3 KiB, one occurrence in the middle third | GCC | 33 | 42.9 | 43.2 | **37.9** | ≈232 | −13% |
| 128 keys, 3 KiB, one occurrence in the middle third | Clang | 32.7 | 40.9 | 41.3 | **37.9** | ≈240 | −13% |
| 128 PHP names, 1536 B | GCC | 60.6 | **34.8** | 35.1 | 48.6 | ≈424 | +74%† |
| 128 PHP names, 1536 B | Clang | 60.4 | **33** | 33.2 | 50.5 | ≈460 | +86%† |
| 128 PHP names, 2 KiB | GCC | 60 | **44.4** | 44.5 | 60.1 | ≈433 | +37% |
| 128 PHP names, 2 KiB | Clang | 59.2 | 41.6 | **41.1** | 60.7 | ≈456 | +44% |
| 128 PHP names, 3 KiB | GCC | 61.6 | 62.6 | **61.1** | 81.6 | ≈444 | −1.2% |
| 128 PHP names, 3 KiB | Clang | 62.1 | **57.8** | 58.9 | 83.1 | ≈467 | +7.7%† |

**512 PHP names, one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | `str_contains()` loop, second copy, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 512 PHP names, 1536 B | GCC | 314 | **125** | 126 | 355 | ≈1,507 | +151% |
| 512 PHP names, 1536 B | Clang | 301 | 120 | **119** | 349 | ≈1,580 | +152% |
| 512 PHP names, 2 KiB | GCC | 315 | **157** | 157 | 429 | ≈1,498 | +100% |
| 512 PHP names, 2 KiB | Clang | 302 | 152 | **150** | 427 | ≈1,580 | +99% |
| 512 PHP names, 3 KiB | GCC | 318 | 210 | **208** | 603 | ≈1,500 | +48% |
| 512 PHP names, 3 KiB | Clang | 301 | 202 | **202** | 572 | ≈1,561 | +49% |

**1024 keys, one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | `str_contains()` loop, second copy, µs | PCRE alternation, µs | PCRE alternation in chunks of 1024, µs | PCRE alternation in chunks of 512, µs | PCRE, shared prefixes, µs | PCRE, shared prefixes in chunks of 1024, µs | PCRE, shared prefixes in chunks of 512, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1024 keys, 1536 B, no occurrence | GCC | 391 | **325** | 328 | 667 | 660 | 530 | ≈1,835 | ≈1,895 | ≈1,960 | +20% |
| 1024 keys, 1536 B, no occurrence | Clang | 383 | **311** | 313 | 704 | 706 | 552 | ≈1,927 | ≈1,972 | ≈2,035 | +23% |
| 1024 keys, 2 KiB, no occurrence | GCC | 394 | **423** | 426 | 880 | 884 | 699 | 1,912 | 1,918 | 1,981 | −7.1% |
| 1024 keys, 2 KiB, no occurrence | Clang | 384 | **405** | 407 | 900 | 902 | 711 | 1,992 | 1,995 | ≈2,037 | −5.0% |
| 1024 keys, 3 KiB, no occurrence | GCC | 396 | **618** | 622 | 1,305 | 1,315 | 993 | 1,927 | 1,934 | 2,003 | −36% |
| 1024 keys, 3 KiB, no occurrence | Clang | 388 | **592** | 593 | 1,305 | 1,312 | 1,025 | 2,021 | 2,028 | 2,084 | −34% |
| 1024 keys, 1536 B, one occurrence in the middle third | GCC | 389 | **166** | 168 | 320 | 323 | 431 | ≈1,808 | ≈1,874 | ≈1,925 | +134% |
| 1024 keys, 1536 B, one occurrence in the middle third | Clang | 379 | **159** | 160 | 334 | 336 | 445 | ≈1,903 | ≈1,964 | ≈2,026 | +138% |
| 1024 keys, 2 KiB, one occurrence in the middle third | GCC | 396 | **217** | 217 | 423 | 426 | 557 | ≈1,827 | ≈1,879 | ≈1,935 | +82% |
| 1024 keys, 2 KiB, one occurrence in the middle third | Clang | 385 | **208** | 209 | 420 | 420 | 538 | ≈1,914 | ≈1,971 | ≈2,036 | +85% |
| 1024 keys, 3 KiB, one occurrence in the middle third | GCC | 398 | **317** | 318 | 596 | 600 | 801 | ≈1,828 | ≈1,892 | ≈1,972 | +26% |
| 1024 keys, 3 KiB, one occurrence in the middle third | Clang | 386 | **302** | 305 | 602 | 605 | 769 | ≈1,946 | ≈1,981 | ≈2,044 | +27% |

### `getMatchedKeywords()`

**16 keys, one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 16 keys, 1536 B, one occurrence in the middle third | GCC | 6.42 | **5.07** | 6.91 | ≈37.6 | +27% |
| 16 keys, 1536 B, one occurrence in the middle third | Clang | 6.74 | **4.82** | 7 | ≈38.9 | +39% |
| 16 keys, 2 KiB, one occurrence in the middle third | GCC | 7.09 | **6.51** | 8.6 | ≈38.6 | +9.0% |
| 16 keys, 2 KiB, one occurrence in the middle third | Clang | 7.47 | **6.19** | 8.69 | ≈40.1 | +21% |
| 16 keys, 3 KiB, one occurrence in the middle third | GCC | 8.5 | **9.41** | 11.8 | 42.5 | −9.8% |
| 16 keys, 3 KiB, one occurrence in the middle third | Clang | 9.14 | **8.96** | 12 | 44.1 | +2.0% |

**32 keys, one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 32 keys, 1536 B, one occurrence in the middle third | GCC | 10 | **11.1** | 11.8 | ≈67.6 | −9.5%† |
| 32 keys, 1536 B, one occurrence in the middle third | Clang | 10.3 | **10.5** | 11.2 | ≈70.9 | −2.1% |
| 32 keys, 2 KiB, one occurrence in the middle third | GCC | 10.8 | **14.4** | 14.9 | 71.5 | −26% |
| 32 keys, 2 KiB, one occurrence in the middle third | Clang | 11.2 | **13.7** | 14.2 | ≈74.4 | −18% |
| 32 keys, 3 KiB, one occurrence in the middle third | GCC | 12.2 | **21** | 21.1 | 75.7 | −42% |
| 32 keys, 3 KiB, one occurrence in the middle third | Clang | 12.8 | **20** | 20.2 | 78.9 | −36% |
| 32 PHP names, 1536 B | GCC | 15.9 | **9.53** | 13.7 | ≈109 | +68% |
| 32 PHP names, 1536 B | Clang | 16.8 | **8.95** | 13.6 | ≈115 | +87% |
| 32 PHP names, 2 KiB | GCC | 16.8 | **12.4** | 17.2 | ≈113 | +36% |
| 32 PHP names, 2 KiB | Clang | 17.4 | **11.6** | 17 | ≈116 | +51% |
| 32 PHP names, 3 KiB | GCC | 18.2 | **17.9** | 23.9 | ≈119 | +1.7% |
| 32 PHP names, 3 KiB | Clang | 19.2 | **16.9** | 23.4 | ≈126 | +13% |

**128 keys, one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 128 keys, 1536 B, one occurrence in the middle third | GCC | 32.9 | 43.8 | **40.9** | ≈230 | −20% |
| 128 keys, 1536 B, one occurrence in the middle third | Clang | 32.9 | 42 | **39.4** | ≈243 | −16% |
| 128 keys, 2 KiB, one occurrence in the middle third | GCC | 33.8 | 56.9 | **51.5** | 237 | −34% |
| 128 keys, 2 KiB, one occurrence in the middle third | Clang | 33.8 | 54.5 | **49.5** | ≈242 | −32% |
| 128 keys, 3 KiB, one occurrence in the middle third | GCC | 35.1 | 83 | **73.2** | 243 | −52% |
| 128 keys, 3 KiB, one occurrence in the middle third | Clang | 35.5 | 79.7 | **70.7** | 259 | −50% |
| 128 PHP names, 1536 B | GCC | 58.7 | **35.7** | 50.7 | ≈442 | +65% |
| 128 PHP names, 1536 B | Clang | 58.8 | **33.9** | 53 | ≈464 | +75%† |
| 128 PHP names, 2 KiB | GCC | 62 | **46.5** | 64.3 | ≈447 | +32%† |
| 128 PHP names, 2 KiB | Clang | 60 | **43.8** | 65.9 | ≈459 | +37% |
| 128 PHP names, 3 KiB | GCC | 62.2 | **68.2** | 91 | ≈451 | −7.6% |
| 128 PHP names, 3 KiB | Clang | 62.5 | **64.7** | 92.8 | ≈475 | −2.1% |

**512 PHP names, one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 512 PHP names, 1536 B | GCC | 317 | **148** | 405 | ≈1,535 | +114% |
| 512 PHP names, 1536 B | Clang | 301 | **140** | 429 | ≈1,628 | +115% |
| 512 PHP names, 2 KiB | GCC | 315 | **188** | 528 | ≈1,541 | +66% |
| 512 PHP names, 2 KiB | Clang | 303 | **181** | 540 | ≈1,630 | +67% |
| 512 PHP names, 3 KiB | GCC | 317 | **280** | 752 | ≈1,559 | +15% |
| 512 PHP names, 3 KiB | Clang | 302 | **262** | 774 | ≈1,621 | +16% |

**1024 keys, one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE alternation in chunks of 1024, µs | PCRE alternation in chunks of 512, µs | PCRE, shared prefixes, µs | PCRE, shared prefixes in chunks of 1024, µs | PCRE, shared prefixes in chunks of 512, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1024 keys, 1536 B, one occurrence in the middle third | GCC | 390 | **327** | 697 | 704 | 557 | ≈1,846 | ≈1,921 | ≈1,969 | +19% |
| 1024 keys, 1536 B, one occurrence in the middle third | Clang | 383 | **314** | 674 | 682 | 558 | ≈1,938 | ≈1,980 | ≈2,038 | +21% |
| 1024 keys, 2 KiB, one occurrence in the middle third | GCC | 392 | **427** | 919 | 929 | 736 | 1,924 | 1,930 | 1,995 | −7.9% |
| 1024 keys, 2 KiB, one occurrence in the middle third | Clang | 386 | **406** | 883 | 886 | 692 | 1,987 | 1,991 | 2,062 | −5.0% |
| 1024 keys, 3 KiB, one occurrence in the middle third | GCC | 392 | **628** | 1,326 | 1,343 | 1,066 | 1,936 | 1,939 | 2,015 | −38% |
| 1024 keys, 3 KiB, one occurrence in the middle third | Clang | 387 | **600** | 1,365 | 1,372 | 1,004 | 1,998 | 2,001 | 2,081 | −35% |

### `countMatches()`

**16 keys, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | `substr_count()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 16 keys, 1536 B, one occurrence in the middle third | GCC | 6.4 | **5.2** | 5.21 | 6.92 | ≈37.2 | +23% |
| 16 keys, 1536 B, one occurrence in the middle third | Clang | 6.71 | **4.97** | 4.98 | 6.69 | ≈38.2 | +35% |
| 16 keys, 2 KiB, one occurrence in the middle third | GCC | 7.05 | **6.74** | 6.77 | 8.71 | ≈38.5 | +4.8% |
| 16 keys, 2 KiB, one occurrence in the middle third | Clang | 7.51 | 6.46 | **6.44** | 8.45 | ≈40 | +17% |
| 16 keys, 3 KiB, one occurrence in the middle third | GCC | 8.43 | **9.86** | 9.9 | 12.2 | 42.4 | −14% |
| 16 keys, 3 KiB, one occurrence in the middle third | Clang | 9.18 | **9.31** | 9.43 | 11.9 | 43.8 | −1.5% |

**32 keys, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | `substr_count()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 32 keys, 1536 B, one occurrence in the middle third | GCC | 9.99 | **11.4** | 11.4 | 11.5 | ≈66.7 | −12% |
| 32 keys, 1536 B, one occurrence in the middle third | Clang | 10.4 | 10.9 | 10.9 | **10.7** | ≈70.1 | −3.8% |
| 32 keys, 2 KiB, one occurrence in the middle third | GCC | 10.7 | 14.8 | 14.8 | **14.5** | 70.8 | −26% |
| 32 keys, 2 KiB, one occurrence in the middle third | Clang | 11.1 | 14.1 | 14 | **13.5** | ≈73.5 | −18% |
| 32 keys, 3 KiB, one occurrence in the middle third | GCC | 12 | 21.4 | 21.3 | **20.2** | 75.3 | −41% |
| 32 keys, 3 KiB, one occurrence in the middle third | Clang | 12.8 | 20.5 | 20.3 | **18.9** | 77.1 | −32% |
| 32 PHP names, 1536 B | GCC | 16 | **9.54** | 9.65 | 13.6 | ≈109 | +67% |
| 32 PHP names, 1536 B | Clang | 16.7 | **9.09** | 9.17 | 13.8 | ≈111 | +84% |
| 32 PHP names, 2 KiB | GCC | 16.8 | **12.4** | 12.6 | 17.1 | ≈112 | +35% |
| 32 PHP names, 2 KiB | Clang | 17.7 | **11.9** | 12 | 17.6 | ≈117 | +49% |
| 32 PHP names, 3 KiB | GCC | 17.9 | **18** | 18.1 | 24.1 | ≈117 | +0.1% |
| 32 PHP names, 3 KiB | Clang | 19.2 | **17.1** | 17.2 | 24.4 | ≈123 | +12%† |

**128 keys, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | `substr_count()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 128 keys, 1536 B, one occurrence in the middle third | GCC | 33.1 | 44.2 | 44.8 | **38.9** | ≈229 | −16% |
| 128 keys, 1536 B, one occurrence in the middle third | Clang | 32.9 | 42.5 | 42.8 | **38.1** | ≈242 | −14% |
| 128 keys, 2 KiB, one occurrence in the middle third | GCC | 33.7 | 57.3 | 57.7 | **49.4** | 239 | −31% |
| 128 keys, 2 KiB, one occurrence in the middle third | Clang | 33.6 | 54.9 | 55.3 | **48.2** | ≈248 | −31% |
| 128 keys, 3 KiB, one occurrence in the middle third | GCC | 35.2 | 83.3 | 83.7 | **70** | 242 | −50% |
| 128 keys, 3 KiB, one occurrence in the middle third | Clang | 35.5 | 80.3 | 80.5 | **68.9** | 255 | −48% |
| 128 PHP names, 1536 B | GCC | 61.9 | **36.1** | 36.5 | 51 | ≈437 | +71% |
| 128 PHP names, 1536 B | Clang | 59.7 | **34.5** | 34.9 | 51.9 | ≈459 | +77%† |
| 128 PHP names, 2 KiB | GCC | 60.9 | **46.9** | 47.4 | 64.4 | ≈445 | +30% |
| 128 PHP names, 2 KiB | Clang | 60.3 | **44.5** | 44.6 | 64.2 | ≈469 | +38% |
| 128 PHP names, 3 KiB | GCC | 62.2 | **68** | 68.5 | 90.3 | ≈451 | −8.6% |
| 128 PHP names, 3 KiB | Clang | 61.7 | **64.3** | 64.7 | 90.2 | ≈474 | −3.6%† |

**512 PHP names, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | `substr_count()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| 512 PHP names, 1536 B | GCC | 315 | **149** | 151 | 408 | ≈1,531 | +111% |
| 512 PHP names, 1536 B | Clang | 301 | **141** | 143 | 428 | ≈1,602 | +112% |
| 512 PHP names, 2 KiB | GCC | 315 | **193** | 196 | 526 | ≈1,515 | +63% |
| 512 PHP names, 2 KiB | Clang | 303 | **183** | 184 | 511 | ≈1,620 | +66% |
| 512 PHP names, 3 KiB | GCC | 318 | **279** | 281 | 759 | ≈1,551 | +15% |
| 512 PHP names, 3 KiB | Clang | 306 | **265** | 266 | 741 | ≈1,619 | +15% |

**1024 keys, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | `substr_count()` loop, µs | PCRE alternation, µs | PCRE alternation in chunks of 1024, µs | PCRE alternation in chunks of 512, µs | PCRE, shared prefixes, µs | PCRE, shared prefixes in chunks of 1024, µs | PCRE, shared prefixes in chunks of 512, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1024 keys, 1536 B, one occurrence in the middle third | GCC | 392 | **330** | 333 | 671 | 673 | 513 | ≈1,829 | ≈1,898 | ≈1,952 | +19% |
| 1024 keys, 1536 B, one occurrence in the middle third | Clang | 381 | **315** | 320 | 709 | 712 | 504 | ≈1,934 | ≈1,983 | ≈2,041 | +21% |
| 1024 keys, 2 KiB, one occurrence in the middle third | GCC | 394 | **431** | 432 | 880 | 887 | 647 | 1,930 | 1,929 | 1,984 | −8.6% |
| 1024 keys, 2 KiB, one occurrence in the middle third | Clang | 384 | **410** | 412 | 892 | 894 | 640 | 1,996 | 1,999 | 2,068 | −6.3% |
| 1024 keys, 3 KiB, one occurrence in the middle third | GCC | 394 | **627** | 629 | 1,334 | 1,336 | 990 | 1,958 | 1,959 | 2,035 | −37% |
| 1024 keys, 3 KiB, one occurrence in the middle third | Clang | 387 | **599** | 606 | 1,312 | 1,322 | 970 | 2,009 | 2,011 | 2,087 | −35% |

### `matchAll()`

**16 keys, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 16 keys, 1536 B, one occurrence in the middle third | GCC | 6.49 | **5.27** | 6.99 | ≈38 | +22% |
| 16 keys, 1536 B, one occurrence in the middle third | Clang | 6.78 | **5.02** | 7.09 | ≈39.5 | +35% |
| 16 keys, 2 KiB, one occurrence in the middle third | GCC | 7.13 | **6.79** | 8.58 | ≈39 | +5.3% |
| 16 keys, 2 KiB, one occurrence in the middle third | Clang | 7.59 | **6.46** | 8.7 | ≈40.4 | +18% |
| 16 keys, 3 KiB, one occurrence in the middle third | GCC | 8.49 | **9.8** | 11.8 | 42.7 | −14% |
| 16 keys, 3 KiB, one occurrence in the middle third | Clang | 9.21 | **9.29** | 12 | 44 | −0.8%† |

**32 keys, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 32 keys, 1536 B, one occurrence in the middle third | GCC | 10.1 | **11.5** | 12 | ≈67.4 | −13% |
| 32 keys, 1536 B, one occurrence in the middle third | Clang | 10.4 | **11** | 11.4 | ≈71.9 | −4.9% |
| 32 keys, 2 KiB, one occurrence in the middle third | GCC | 10.8 | **14.8** | 14.9 | ≈70.8 | −27% |
| 32 keys, 2 KiB, one occurrence in the middle third | Clang | 11.2 | **14.1** | 14.3 | ≈73.6 | −21% |
| 32 keys, 3 KiB, one occurrence in the middle third | GCC | 12.2 | 21.6 | **21.1** | 76.2 | −42% |
| 32 keys, 3 KiB, one occurrence in the middle third | Clang | 12.9 | 20.6 | **20.3** | 79.7 | −36% |
| 32 PHP names, 1536 B | GCC | 16 | **9.56** | 13.7 | ≈109 | +69% |
| 32 PHP names, 1536 B | Clang | 16.7 | **8.97** | 13.5 | ≈115 | +86% |
| 32 PHP names, 2 KiB | GCC | 16.7 | **12.4** | 16.9 | ≈111 | +35% |
| 32 PHP names, 2 KiB | Clang | 17.4 | **11.7** | 17 | ≈117 | +49% |
| 32 PHP names, 3 KiB | GCC | 18 | **18.1** | 24 | ≈117 | −0.2% |
| 32 PHP names, 3 KiB | Clang | 19.1 | **17** | 23.6 | ≈122 | +13% |

**128 keys, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 128 keys, 1536 B, one occurrence in the middle third | GCC | 32.9 | 44.4 | **40.7** | ≈229 | −20%† |
| 128 keys, 1536 B, one occurrence in the middle third | Clang | 33.3 | 43.1 | **39.3** | ≈245 | −16% |
| 128 keys, 2 KiB, one occurrence in the middle third | GCC | 33.8 | 57.5 | **51.5** | 237 | −34% |
| 128 keys, 2 KiB, one occurrence in the middle third | Clang | 33.9 | 55.6 | **49.8** | ≈249 | −32% |
| 128 keys, 3 KiB, one occurrence in the middle third | GCC | 35.3 | 83.4 | **72.8** | 245 | −52% |
| 128 keys, 3 KiB, one occurrence in the middle third | Clang | 35.6 | 80.3 | **70.4** | 257 | −49% |
| 128 PHP names, 1536 B | GCC | 60 | **36.2** | 50.9 | ≈437 | +67% |
| 128 PHP names, 1536 B | Clang | 60.3 | **34.3** | 53 | ≈462 | +75%† |
| 128 PHP names, 2 KiB | GCC | 60.9 | **46.8** | 63.9 | ≈443 | +31% |
| 128 PHP names, 2 KiB | Clang | 59 | **44.3** | 66.1 | ≈463 | +33% |
| 128 PHP names, 3 KiB | GCC | 62.1 | **67.8** | 89.6 | ≈457 | −8.9% |
| 128 PHP names, 3 KiB | Clang | 62.4 | **62.8** | 91.5 | ≈478 | −0.5%† |

**512 PHP names, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 512 PHP names, 1536 B | GCC | 316 | **149** | 416 | ≈1,523 | +112%† |
| 512 PHP names, 1536 B | Clang | 302 | **140** | 410 | ≈1,628 | +114% |
| 512 PHP names, 2 KiB | GCC | 314 | **190** | 526 | ≈1,529 | +65% |
| 512 PHP names, 2 KiB | Clang | 299 | **178** | 529 | ≈1,610 | +67%† |
| 512 PHP names, 3 KiB | GCC | 314 | **276** | 761 | ≈1,545 | +13% |
| 512 PHP names, 3 KiB | Clang | 300 | **258** | 776 | ≈1,656 | +16% |

**1024 keys, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE alternation in chunks of 1024, µs | PCRE alternation in chunks of 512, µs | PCRE, shared prefixes, µs | PCRE, shared prefixes in chunks of 1024, µs | PCRE, shared prefixes in chunks of 512, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1024 keys, 1536 B, one occurrence in the middle third | GCC | 391 | **333** | 696 | 696 | 590 | ≈1,851 | ≈1,908 | ≈1,964 | +18% |
| 1024 keys, 1536 B, one occurrence in the middle third | Clang | 387 | **318** | 688 | 688 | 561 | ≈1,937 | ≈1,977 | ≈2,038 | +21% |
| 1024 keys, 2 KiB, one occurrence in the middle third | GCC | 395 | **432** | 922 | 918 | 728 | 1,934 | 1,947 | 2,008 | −9.0% |
| 1024 keys, 2 KiB, one occurrence in the middle third | Clang | 385 | **413** | 892 | 904 | 710 | 2,012 | 2,020 | 2,072 | −7.5% |
| 1024 keys, 3 KiB, one occurrence in the middle third | GCC | 399 | **621** | 1,327 | 1,322 | 1,043 | 1,960 | 1,962 | 2,038 | −36% |
| 1024 keys, 3 KiB, one occurrence in the middle third | Clang | 386 | **599** | 1,352 | 1,351 | 1,005 | 2,019 | 2,025 | 2,097 | −35% |

### `replace()`

**16 keys, one-shot**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 16 keys, 1536 B, no occurrence | GCC | 6.21 | 22.9 | **6.3** | ≈36.5 | −1.7% |
| 16 keys, 1536 B, no occurrence | Clang | 6.39 | 22.6 | **6.31** | ≈38.2 | +1.7% |
| 16 keys, 2 KiB, no occurrence | GCC | 6.86 | 30.2 | **7.87** | 38.3 | −13% |
| 16 keys, 2 KiB, no occurrence | Clang | 7.1 | 29.8 | **7.92** | 40.1 | −10% |
| 16 keys, 3 KiB, no occurrence | GCC | 8.25 | 45.1 | **11** | 41.6 | −25% |
| 16 keys, 3 KiB, no occurrence | Clang | 8.62 | 44.4 | **11.1** | 43.2 | −22% |
| 16 keys, 1536 B, one occurrence in the middle third | GCC | 6.21 | 22.7 | **6.44** | ≈36.5 | −3.6% |
| 16 keys, 1536 B, one occurrence in the middle third | Clang | 6.46 | 22.3 | **6.49** | ≈38.5 | −0.8% |
| 16 keys, 2 KiB, one occurrence in the middle third | GCC | 6.89 | 30.4 | **8.09** | 38.5 | −15% |
| 16 keys, 2 KiB, one occurrence in the middle third | Clang | 7.21 | 29.9 | **8.2** | 40.4 | −12% |
| 16 keys, 3 KiB, one occurrence in the middle third | GCC | 8.26 | 45.1 | **11.2** | 41.6 | −26% |
| 16 keys, 3 KiB, one occurrence in the middle third | Clang | 8.81 | 44.5 | **11.5** | 43.7 | −24% |

**32 keys, one-shot**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 32 keys, 1536 B, no occurrence | GCC | 9.92 | 45.4 | **10.9** | ≈67 | −8.6% |
| 32 keys, 1536 B, no occurrence | Clang | 10.1 | 45.4 | **10.8** | ≈69.5 | −6.4% |
| 32 keys, 2 KiB, no occurrence | GCC | 10.6 | 59.5 | **13.6** | ≈69.5 | −22% |
| 32 keys, 2 KiB, no occurrence | Clang | 10.9 | 59.4 | **13.6** | ≈72.3 | −20% |
| 32 keys, 3 KiB, no occurrence | GCC | 12 | 89.5 | **19.4** | 73.9 | −38% |
| 32 keys, 3 KiB, no occurrence | Clang | 12.5 | 89.7 | **19.7** | 77.7 | −36% |
| 32 keys, 1536 B, one occurrence in the middle third | GCC | 9.96 | 45 | **10.9** | ≈66.9 | −9.1% |
| 32 keys, 1536 B, one occurrence in the middle third | Clang | 10.3 | 45.1 | **11** | ≈71 | −6.6%† |
| 32 keys, 2 KiB, one occurrence in the middle third | GCC | 10.7 | 59.6 | **13.9** | ≈69.6 | −23% |
| 32 keys, 2 KiB, one occurrence in the middle third | Clang | 11 | 59.6 | **14** | ≈72.3 | −21% |
| 32 keys, 3 KiB, one occurrence in the middle third | GCC | 12 | 87.8 | **19.4** | 74.3 | −38% |
| 32 keys, 3 KiB, one occurrence in the middle third | Clang | 12.6 | 87.7 | **19.7** | 77.2 | −36% |
| 32 PHP names, 1536 B | GCC | 17 | ≈128 | **13.2** | ≈107 | +29% |
| 32 PHP names, 1536 B | Clang | 17.7 | ≈128 | **13.4** | ≈113 | +32% |
| 32 PHP names, 2 KiB | GCC | 18.1 | ≈171 | **16.6** | ≈110 | +7.9% |
| 32 PHP names, 2 KiB | Clang | 18.7 | ≈172 | **16.8** | ≈114 | +11% |
| 32 PHP names, 3 KiB | GCC | 19.3 | ≈255 | **23.3** | 115 | −17% |
| 32 PHP names, 3 KiB | Clang | 20.1 | ≈260 | **23.2** | ≈119 | −13% |

**128 keys, one-shot**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 128 keys, 1536 B, no occurrence | GCC | 31.4 | 72.6 | **38.8** | ≈227 | −19% |
| 128 keys, 1536 B, no occurrence | Clang | 31.6 | 72.6 | **37.8** | ≈240 | −17% |
| 128 keys, 2 KiB, no occurrence | GCC | 32.1 | 95.7 | **49.3** | 236 | −35% |
| 128 keys, 2 KiB, no occurrence | Clang | 32.5 | 95.3 | **48.2** | ≈241 | −33% |
| 128 keys, 3 KiB, no occurrence | GCC | 33.6 | 144 | **71.3** | 240 | −53% |
| 128 keys, 3 KiB, no occurrence | Clang | 33.9 | 144 | **70.1** | 253 | −52% |
| 128 keys, 1536 B, one occurrence in the middle third | GCC | 31.4 | 71.1 | **38.3** | ≈228 | −18% |
| 128 keys, 1536 B, one occurrence in the middle third | Clang | 31.6 | 70.7 | **37.3** | ≈238 | −15% |
| 128 keys, 2 KiB, one occurrence in the middle third | GCC | 32.2 | 94.8 | **49.2** | 235 | −35% |
| 128 keys, 2 KiB, one occurrence in the middle third | Clang | 32.5 | 94.9 | **48.3** | ≈244 | −33% |
| 128 keys, 3 KiB, one occurrence in the middle third | GCC | 33.6 | 143 | **71.2** | 241 | −53% |
| 128 keys, 3 KiB, one occurrence in the middle third | Clang | 34.1 | 142 | **70.1** | 257 | −51% |
| 128 PHP names, 1536 B | GCC | 68.7 | ≈294 | **49.3** | ≈437 | +39%† |
| 128 PHP names, 1536 B | Clang | 73.5 | ≈300 | **50.9** | ≈456 | +42%† |
| 128 PHP names, 2 KiB | GCC | 68.9 | ≈392 | **61.6** | ≈445 | +12%† |
| 128 PHP names, 2 KiB | Clang | 73.5 | ≈395 | **64.1** | ≈462 | +15%† |
| 128 PHP names, 3 KiB | GCC | 73.7 | ≈650 | **85.9** | ≈440 | −15%† |
| 128 PHP names, 3 KiB | Clang | 72.1 | ≈670 | **89** | ≈467 | −18%† |

**512 PHP names, one-shot**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 512 PHP names, 1536 B | GCC | 446 | 500 | **382** | 1,665 | +17% |
| 512 PHP names, 1536 B | Clang | 431 | 507 | **403** | 1,732 | +7.5% |
| 512 PHP names, 2 KiB | GCC | 447 | 656 | **483** | 1,681 | −6.7%† |
| 512 PHP names, 2 KiB | Clang | 430 | 675 | **494** | 1,743 | −13% |
| 512 PHP names, 3 KiB | GCC | 447 | 985 | **719** | 1,685 | −38% |
| 512 PHP names, 3 KiB | Clang | 436 | 1,015 | **725** | 1,766 | −40%† |

**1024 keys, one-shot**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 1024 keys, 1536 B, no occurrence | GCC | 388 | **75.8** | ≈688 | ≈1,772 | +412% |
| 1024 keys, 1536 B, no occurrence | Clang | 379 | **75.6** | ≈728 | ≈1,864 | +401% |
| 1024 keys, 2 KiB, no occurrence | GCC | 387 | **99.7** | ≈855 | ≈1,776 | +288% |
| 1024 keys, 2 KiB, no occurrence | Clang | 380 | **99.8** | ≈906 | ≈1,865 | +279% |
| 1024 keys, 3 KiB, no occurrence | GCC | 390 | **150** | ≈1,057 | ≈1,777 | +161% |
| 1024 keys, 3 KiB, no occurrence | Clang | 380 | **150** | ≈1,118 | ≈1,866 | +154% |
| 1024 keys, 1536 B, one occurrence in the middle third | GCC | 391 | **74.9** | ≈681 | ≈1,777 | +423% |
| 1024 keys, 1536 B, one occurrence in the middle third | Clang | 382 | **75.3** | ≈733 | ≈1,874 | +411% |
| 1024 keys, 2 KiB, one occurrence in the middle third | GCC | 392 | **98** | ≈806 | ≈1,774 | +298% |
| 1024 keys, 2 KiB, one occurrence in the middle third | Clang | 385 | **98.1** | ≈831 | ≈1,872 | +290% |
| 1024 keys, 3 KiB, one occurrence in the middle third | GCC | 390 | **146** | ≈1,259 | ≈1,780 | +169% |
| 1024 keys, 3 KiB, one occurrence in the middle third | Clang | 385 | **146** | ≈1,337 | ≈1,878 | +165% |

## Text languages

### `matches()`

**prepared**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | `str_contains()` loop, second copy, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| English with emoji, PHP names, 4 KiB | GCC | 5.62 | 79.6 | 79.6 | 81.4 | **30.7** | −82% |
| English with emoji, PHP names, 4 KiB | Clang | 6.58 | 75.2 | 75.6 | 81.1 | **30.9** | −79% |
| English with emoji, PHP names, 64 KiB | GCC | 52.1 | 791 | 794 | 790 | **293** | −82% |
| English with emoji, PHP names, 64 KiB | Clang | 62.4 | 740 | 743 | 790 | **294** | −79% |
| English with emoji, frequent words, 4 KiB | GCC | 0.93 | 15.5 | 15.4 | 12.2 | **5.31** | −83% |
| English with emoji, frequent words, 4 KiB | Clang | 0.99 | 15 | 14.9 | 12 | **5.33** | −81% |
| English with emoji, frequent words, 64 KiB | GCC | 0.95 | 26.3 | 26.3 | 13 | **5.43** | −83% |
| English with emoji, frequent words, 64 KiB | Clang | 1.01 | 26.2 | 26 | 12.7 | **5.48** | −82% |
| English, PHP names, 4 KiB | GCC | 5.59 | 83.2 | 83.6 | 95.3 | **35.3** | −84% |
| English, PHP names, 4 KiB | Clang | 6.48 | 77.9 | 77.7 | 94 | **35.1** | −82% |
| English, PHP names, 64 KiB | GCC | 62 | 832 | 846 | 1,108 | **401** | −85% |
| English, PHP names, 64 KiB | Clang | 74 | 794 | 792 | 1,098 | **402** | −82% |
| English, frequent words, 4 KiB | GCC | 0.74 | 14.9 | 15 | 10.5 | **4.57** | −84% |
| English, frequent words, 4 KiB | Clang | 0.77 | 14.6 | 14.7 | 10.3 | **4.56** | −83% |
| English, frequent words, 64 KiB | GCC | 0.82 | 24 | 24 | 12.7 | **5.21** | −84% |
| English, frequent words, 64 KiB | Clang | 0.86 | 23.5 | 23.6 | 12.4 | **5.23** | −83% |
| Spanish, PHP names, 4 KiB | GCC | 5.51 | 81.8 | 81.6 | 92 | **34.6** | −84% |
| Spanish, PHP names, 4 KiB | Clang | 6.39 | 77.9 | 78 | 90.9 | **34.7** | −82% |
| Spanish, PHP names, 64 KiB | GCC | 57.9 | 885 | 889 | 1,021 | **375** | −85% |
| Spanish, PHP names, 64 KiB | Clang | 68 | 859 | 835 | 1,006 | **377** | −82% |
| Spanish, frequent words, 4 KiB | GCC | 1.13 | 14.6 | 14.6 | 17 | **6.99** | −84% |
| Spanish, frequent words, 4 KiB | Clang | 1.22 | 14.3 | 14.3 | 16.6 | **7.03** | −83% |
| Spanish, frequent words, 64 KiB | GCC | 0.95 | ≈46.1 | ≈46.4 | 14.7 | **6.03** | −84% |
| Spanish, frequent words, 64 KiB | Clang | 1.03 | ≈44.7 | ≈44.5 | 14.3 | **6.01** | −83% |
| Japanese, PHP names, 4 KiB | GCC | 3.83 | 66.3 | 66.3 | 37.1 | **14** | −73% |
| Japanese, PHP names, 4 KiB | Clang | 4.16 | 61.8 | 62.1 | 36.9 | **14.2** | −71% |
| Japanese, PHP names, 64 KiB | GCC | 41.4 | ≈1,075 | ≈1,083 | 448 | **161** | −74% |
| Japanese, PHP names, 64 KiB | Clang | 46.2 | ≈1,005 | ≈1,006 | 447 | **164** | −72% |
| Japanese, frequent words, 4 KiB | GCC | 0.73 | ≈21.6 | ≈21.6 | 2.26 | **0.83** | −12% |
| Japanese, frequent words, 4 KiB | Clang | 0.69 | ≈21.7 | ≈21.7 | 2.27 | **0.83** | −17% |
| Japanese, frequent words, 64 KiB | GCC | 1.21 | ≈46.4 | ≈46.9 | 2.52 | **0.98** | +23% |
| Japanese, frequent words, 64 KiB | Clang | 1.16 | ≈45.6 | ≈45.6 | 2.53 | **0.98** | +18% |
| Korean, PHP names, 4 KiB | GCC | 4.28 | 70.6 | 71 | 37.4 | **14.7** | −71% |
| Korean, PHP names, 4 KiB | Clang | 4.69 | 66.1 | 66.1 | 36.9 | **14.7** | −68% |
| Korean, PHP names, 64 KiB | GCC | 65.4 | ≈1,085 | ≈1,090 | 614 | **230** | −71% |
| Korean, PHP names, 64 KiB | Clang | 72.6 | 1,011 | 990 | 606 | **232** | −68% |
| Korean, frequent words, 4 KiB | GCC | 1.24 | ≈30.1 | ≈31.4 | 5.32 | **2.09** | −40% |
| Korean, frequent words, 4 KiB | Clang | 1.28 | ≈29.3 | ≈29.4 | 5.18 | **2.12** | −40% |
| Korean, frequent words, 64 KiB | GCC | 1.4 | ≈28.1 | ≈28.2 | 7.19 | **2.7** | −48% |
| Korean, frequent words, 64 KiB | Clang | 1.53 | ≈27.5 | ≈27.2 | 7 | **2.76** | −44% |
| Russian, PHP names, 4 KiB | GCC | 3.28 | ≈63.2 | ≈63.2 | 26.5 | **10.4** | −68% |
| Russian, PHP names, 4 KiB | Clang | 3.48 | ≈58.8 | ≈59 | 25.9 | **10.4** | −67% |
| Russian, PHP names, 64 KiB | GCC | 32.5 | 701 | 699 | 273 | **103** | −69% |
| Russian, PHP names, 64 KiB | Clang | 35 | 649 | 651 | 271 | **104** | −66% |
| Russian, frequent words, 4 KiB | GCC | 2.48 | ≈66.9 | ≈67.1 | 16.5 | **5.58** | −56% |
| Russian, frequent words, 4 KiB | Clang | 2.49 | ≈65.2 | ≈65.9 | 16.8 | **5.61** | −56% |
| Russian, frequent words, 64 KiB | GCC | 1.97 | ≈73.4 | ≈73.5 | 15.8 | **5.14** | −62%† |
| Russian, frequent words, 64 KiB | Clang | 2.08 | ≈72.7 | ≈73.8 | 16.1 | **5.17** | −60% |
| Chinese, PHP names, 4 KiB | GCC | 4.19 | 68.2 | 68.5 | 41.5 | **15.9** | −74% |
| Chinese, PHP names, 4 KiB | Clang | 4.59 | 63.4 | 63.2 | 41.3 | **15.9** | −71% |
| Chinese, PHP names, 64 KiB | GCC | 32 | 622 | 620 | 324 | **121** | −74% |
| Chinese, PHP names, 64 KiB | Clang | 34.5 | ≈840 | ≈843 | 324 | **123** | −72% |
| Chinese, frequent words, 4 KiB | GCC | 1.1 | ≈21.7 | ≈21.7 | 4.28 | **1.72** | −36% |
| Chinese, frequent words, 4 KiB | Clang | 1.08 | ≈20.5 | ≈20.6 | 4.35 | **1.68** | −37% |
| Chinese, frequent words, 64 KiB | GCC | 0.95 | ≈34.8 | ≈35.8 | 4.43 | **1.56** | −39% |
| Chinese, frequent words, 64 KiB | Clang | 0.94 | ≈36.7 | ≈36.9 | 4.52 | **1.54** | −39% |

**one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | `str_contains()` loop, second copy, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| English with emoji, PHP names, 4 KiB | GCC | 62.5 | **78.4** | 78.7 | 91.9 | ≈451 | −20% |
| English with emoji, PHP names, 4 KiB | Clang | 64.3 | **73.8** | 74.1 | 93.6 | ≈478 | −14% |
| English with emoji, PHP names, 64 KiB | GCC | 111 | 791 | 793 | 815 | **722** | −85% |
| English with emoji, PHP names, 64 KiB | Clang | 123 | **740** | 745 | 809 | 748 | −84% |
| English with emoji, frequent words, 4 KiB | GCC | 31.6 | 15.5 | **15.4** | 18.1 | ≈147 | +106% |
| English with emoji, frequent words, 4 KiB | Clang | 33.1 | **14.8** | 15 | 17.4 | ≈153 | +123% |
| English with emoji, frequent words, 64 KiB | GCC | 31.3 | 26.7 | 26.6 | **18.9** | ≈149 | +66% |
| English with emoji, frequent words, 64 KiB | Clang | 33 | 26.1 | 26.1 | **18.2** | ≈155 | +82% |
| English, PHP names, 4 KiB | GCC | 63 | **83** | 83.2 | 107 | ≈463 | −24% |
| English, PHP names, 4 KiB | Clang | 62.6 | 77.2 | **77.1** | 107 | ≈485 | −20%† |
| English, PHP names, 64 KiB | GCC | 120 | 848 | 849 | 1,114 | **830** | −85% |
| English, PHP names, 64 KiB | Clang | 133 | **783** | 796 | 1,108 | 852 | −83% |
| English, frequent words, 4 KiB | GCC | 31.2 | 15.1 | **15.1** | 16.4 | ≈148 | +107% |
| English, frequent words, 4 KiB | Clang | 33.2 | **14.7** | 14.8 | 15.8 | ≈153 | +125% |
| English, frequent words, 64 KiB | GCC | 31.6 | 24.1 | 24.1 | **18.6** | ≈153 | +69% |
| English, frequent words, 64 KiB | Clang | 33.2 | 23.8 | 23.6 | **17.9** | ≈159 | +85% |
| Spanish, PHP names, 4 KiB | GCC | 62.9 | 82.8 | **82.4** | 104 | ≈451 | −24% |
| Spanish, PHP names, 4 KiB | Clang | 61.7 | **77.5** | 77.6 | 105 | ≈476 | −20% |
| Spanish, PHP names, 64 KiB | GCC | 116 | 890 | 889 | 1,024 | **801** | −85% |
| Spanish, PHP names, 64 KiB | Clang | 127 | 860 | 854 | 1,024 | **830** | −85% |
| Spanish, frequent words, 4 KiB | GCC | 35.6 | **14.6** | 14.8 | 23 | ≈162 | +143% |
| Spanish, frequent words, 4 KiB | Clang | 37.3 | 14.3 | **14.3** | 22.2 | ≈171 | +163% |
| Spanish, frequent words, 64 KiB | GCC | 35.3 | 45.8 | 45.8 | **20.9** | ≈163 | +70% |
| Spanish, frequent words, 64 KiB | Clang | 37.2 | 44 | 43.9 | **19.9** | ≈170 | +87% |
| Japanese, PHP names, 4 KiB | GCC | 60.7 | 66 | 65.8 | **48.9** | ≈436 | +24%† |
| Japanese, PHP names, 4 KiB | Clang | 61.8 | 61.6 | 61.9 | **50.1** | ≈459 | +25%† |
| Japanese, PHP names, 64 KiB | GCC | 104 | 745 | 745 | **465** | 595 | −78% |
| Japanese, PHP names, 64 KiB | Clang | 105 | 696 | 697 | **457** | 616 | −77% |
| Japanese, frequent words, 4 KiB | GCC | 44.4 | 19.4 | 19.6 | **7.61** | ≈117 | +484% |
| Japanese, frequent words, 4 KiB | Clang | 43.7 | 19.3 | 19.2 | **7.75** | ≈125 | +469% |
| Japanese, frequent words, 64 KiB | GCC | 45 | ≈46.4 | ≈46.8 | **7.9** | ≈118 | +472% |
| Japanese, frequent words, 64 KiB | Clang | 44.8 | ≈45.4 | ≈45.9 | **8.07** | ≈124 | +459%† |
| Korean, PHP names, 4 KiB | GCC | 62.2 | 71.2 | 71.3 | **48.7** | ≈436 | +26%† |
| Korean, PHP names, 4 KiB | Clang | 61.3 | 66.4 | 66.7 | **50.2** | ≈463 | +21% |
| Korean, PHP names, 64 KiB | GCC | 130 | 1,073 | 1,078 | **623** | 660 | −79%† |
| Korean, PHP names, 64 KiB | Clang | 135 | 1,005 | 990 | **618** | 674 | −78% |
| Korean, frequent words, 4 KiB | GCC | 35.1 | 30.2 | 30.3 | **11.1** | ≈178 | +214% |
| Korean, frequent words, 4 KiB | Clang | 36.2 | 29.1 | 29.1 | **11** | ≈185 | +227% |
| Korean, frequent words, 64 KiB | GCC | 35.2 | 27.9 | 28 | **13.1** | ≈177 | +170% |
| Korean, frequent words, 64 KiB | Clang | 36.8 | 27.2 | 27.3 | **12.8** | ≈189 | +187% |
| Russian, PHP names, 4 KiB | GCC | 60.7 | 63.9 | 64.1 | **38.3** | ≈438 | +56%† |
| Russian, PHP names, 4 KiB | Clang | 60 | 59.7 | 59.8 | **39.3** | ≈462 | +53% |
| Russian, PHP names, 64 KiB | GCC | 93.3 | 694 | 696 | **284** | 534 | −67% |
| Russian, PHP names, 64 KiB | Clang | 94 | 651 | 650 | **287** | 554 | −67% |
| Russian, frequent words, 4 KiB | GCC | 64.6 | 59.2 | 58.9 | **23.7** | ≈312 | +174% |
| Russian, frequent words, 4 KiB | Clang | 62.3 | 58.2 | 58.3 | **23.6** | ≈330 | +166% |
| Russian, frequent words, 64 KiB | GCC | 64.4 | 78.2 | 78.2 | **22.8** | ≈313 | +184% |
| Russian, frequent words, 64 KiB | Clang | 62.3 | 77.4 | 77.2 | **22.7** | ≈329 | +176% |
| Chinese, PHP names, 4 KiB | GCC | 61.9 | 68.4 | 68.4 | **52.9** | ≈443 | +16%† |
| Chinese, PHP names, 4 KiB | Clang | 62.7 | 64 | 63.9 | **54.1** | ≈466 | +16% |
| Chinese, PHP names, 64 KiB | GCC | 95.2 | 624 | 627 | **340** | 555 | −72% |
| Chinese, PHP names, 64 KiB | Clang | 93.4 | 577 | 580 | **339** | 577 | −72% |
| Chinese, frequent words, 4 KiB | GCC | 47.1 | 20 | 20.1 | **9.54** | ≈124 | +391% |
| Chinese, frequent words, 4 KiB | Clang | 45.8 | 19.7 | 19.5 | **9.76** | ≈129 | +371% |
| Chinese, frequent words, 64 KiB | GCC | 46.8 | 35.7 | 35.9 | **9.74** | ≈123 | +380% |
| Chinese, frequent words, 64 KiB | Clang | 46 | 36.4 | 36.6 | **9.88** | ≈127 | +366% |

### `getMatchedKeywords()`

**prepared**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| English with emoji, PHP names, 4 KiB | GCC | 5.96 | 85 | 89.9 | **36.3** | −84% |
| English with emoji, PHP names, 4 KiB | Clang | 6.94 | 79.7 | 90.2 | **34.9** | −80% |
| English with emoji, PHP names, 64 KiB | GCC | 92.6 | 1,282 | 1,418 | **560** | −83% |
| English with emoji, PHP names, 64 KiB | Clang | 109 | 1,199 | 1,422 | **534** | −80% |
| English with emoji, frequent words, 4 KiB | GCC | 6.63 | 88.1 | 130 | **63.4** | −90% |
| English with emoji, frequent words, 4 KiB | Clang | 7.51 | 86.4 | 123 | **60.2** | −88% |
| English with emoji, frequent words, 64 KiB | GCC | 101 | 1,257 | 2,104 | **1,002** | −90% |
| English with emoji, frequent words, 64 KiB | Clang | 115 | 1,223 | 1,992 | **944** | −88% |
| English, PHP names, 4 KiB | GCC | 5.95 | 88.7 | 104 | **41.5** | −86% |
| English, PHP names, 4 KiB | Clang | 6.98 | 83.7 | 106 | **39.6** | −82% |
| English, PHP names, 64 KiB | GCC | 92.2 | 1,337 | 1,657 | **640** | −86% |
| English, PHP names, 64 KiB | Clang | 108 | 1,259 | 1,656 | **605** | −82% |
| English, frequent words, 4 KiB | GCC | 6.84 | 96.6 | 151 | **73.4** | −91% |
| English, frequent words, 4 KiB | Clang | 7.65 | 93.5 | 145 | **69** | −89% |
| English, frequent words, 64 KiB | GCC | 101 | 1,299 | 2,395 | **1,118** | −91% |
| English, frequent words, 64 KiB | Clang | 116 | 1,267 | 2,293 | **1,071** | −89% |
| Spanish, PHP names, 4 KiB | GCC | 6 | 89.7 | 104 | **42.3** | −86% |
| Spanish, PHP names, 4 KiB | Clang | 7.09 | 84.6 | 104 | **40.4** | −83% |
| Spanish, PHP names, 64 KiB | GCC | 92.4 | 1,361 | 1,633 | **649** | −86% |
| Spanish, PHP names, 64 KiB | Clang | 110 | 1,275 | 1,656 | **623** | −82% |
| Spanish, frequent words, 4 KiB | GCC | 6.85 | 113 | 142 | **64.1** | −89% |
| Spanish, frequent words, 4 KiB | Clang | 7.74 | 110 | 143 | **64.2** | −88% |
| Spanish, frequent words, 64 KiB | GCC | 103 | 1,531 | 2,269 | **992** | −90% |
| Spanish, frequent words, 64 KiB | Clang | 117 | 1,489 | 2,299 | **994** | −88% |
| Japanese, PHP names, 4 KiB | GCC | 4.55 | 70 | 38.8 | **15.9** | −71% |
| Japanese, PHP names, 4 KiB | Clang | 4.28 | 64.9 | 39.3 | **15.4** | −72% |
| Japanese, PHP names, 64 KiB | GCC | 63.9 | 1,053 | 610 | **241** | −74% |
| Japanese, PHP names, 64 KiB | Clang | 63.7 | 984 | 620 | **233** | −73% |
| Japanese, frequent words, 4 KiB | GCC | 7.93 | ≈165 | 61.6 | **28** | −72% |
| Japanese, frequent words, 4 KiB | Clang | 8.01 | ≈165 | 60.6 | **27.4** | −71% |
| Japanese, frequent words, 64 KiB | GCC | 110 | ≈2,057 | 951 | **408** | −73% |
| Japanese, frequent words, 64 KiB | Clang | 112 | ≈2,039 | 922 | **401** | −72% |
| Korean, PHP names, 4 KiB | GCC | 4.78 | 70.8 | 38.1 | **16** | −70% |
| Korean, PHP names, 4 KiB | Clang | 4.78 | 66.5 | 38.5 | **15.4** | −69% |
| Korean, PHP names, 64 KiB | GCC | 73.3 | 1,077 | 628 | **253** | −71% |
| Korean, PHP names, 64 KiB | Clang | 73.5 | 999 | 635 | **242** | −70% |
| Korean, frequent words, 4 KiB | GCC | 6.97 | ≈153 | 50.7 | **23** | −70% |
| Korean, frequent words, 4 KiB | Clang | 7.43 | ≈151 | 50.9 | **22.9** | −68% |
| Korean, frequent words, 64 KiB | GCC | 109 | ≈2,050 | 809 | **354** | −69% |
| Korean, frequent words, 64 KiB | Clang | 117 | ≈2,005 | 824 | **356** | −67% |
| Russian, PHP names, 4 KiB | GCC | 4.14 | ≈69 | 29.1 | **12.1** | −66% |
| Russian, PHP names, 4 KiB | Clang | 3.75 | ≈65.2 | 29.4 | **11.7** | −68% |
| Russian, PHP names, 64 KiB | GCC | 56.9 | ≈1,012 | 460 | **186** | −69% |
| Russian, PHP names, 64 KiB | Clang | 53.6 | ≈963 | 460 | **177** | −70% |
| Russian, frequent words, 4 KiB | GCC | 8.87 | ≈236 | 71.6 | **29.2** | −70% |
| Russian, frequent words, 4 KiB | Clang | 9.14 | ≈231 | 71 | **29.2** | −69% |
| Russian, frequent words, 64 KiB | GCC | 132 | ≈3,180 | 1,136 | **445** | −70% |
| Russian, frequent words, 64 KiB | Clang | 137 | ≈3,144 | 1,118 | **442** | −69% |
| Chinese, PHP names, 4 KiB | GCC | 4.93 | 71.8 | 46.7 | **19** | −74% |
| Chinese, PHP names, 4 KiB | Clang | 4.99 | 67.7 | 46.8 | **18.4** | −73% |
| Chinese, PHP names, 64 KiB | GCC | 72.8 | 1,087 | 752 | **298** | −76% |
| Chinese, PHP names, 64 KiB | Clang | 75.3 | 1,013 | 763 | **288** | −74% |
| Chinese, frequent words, 4 KiB | GCC | 5.79 | 105 | 42.4 | **22.2** | −74% |
| Chinese, frequent words, 4 KiB | Clang | 5.79 | 103 | 43.8 | **22** | −74% |
| Chinese, frequent words, 64 KiB | GCC | 80.2 | 1,267 | 643 | **325** | −75% |
| Chinese, frequent words, 64 KiB | Clang | 82.4 | 1,264 | 665 | **321** | −75% |

**one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| English with emoji, PHP names, 4 KiB | GCC | 64.6 | **85.6** | 102 | ≈463 | −25% |
| English with emoji, PHP names, 4 KiB | Clang | 63.5 | **80** | 104 | ≈480 | −21% |
| English with emoji, PHP names, 64 KiB | GCC | 155 | 1,287 | 1,430 | **999** | −85% |
| English with emoji, PHP names, 64 KiB | Clang | 169 | 1,209 | 1,449 | **989** | −83% |
| English with emoji, frequent words, 4 KiB | GCC | 37.6 | **88.8** | 136 | 212 | −58% |
| English with emoji, frequent words, 4 KiB | Clang | 40.1 | **86.6** | 129 | 215 | −54% |
| English with emoji, frequent words, 64 KiB | GCC | 133 | 1,254 | 2,116 | **1,157** | −88% |
| English with emoji, frequent words, 64 KiB | Clang | 149 | 1,225 | 2,004 | **1,108** | −87% |
| English, PHP names, 4 KiB | GCC | 63.1 | **89.6** | 116 | ≈469 | −30% |
| English, PHP names, 4 KiB | Clang | 64.2 | **83.9** | 119 | ≈489 | −24%† |
| English, PHP names, 64 KiB | GCC | 153 | 1,345 | 1,670 | **1,076** | −86% |
| English, PHP names, 64 KiB | Clang | 166 | 1,257 | 1,668 | **1,060** | −84% |
| English, frequent words, 4 KiB | GCC | 37.6 | **96.1** | 158 | 221 | −61% |
| English, frequent words, 4 KiB | Clang | 39.9 | **95.1** | 152 | 225 | −57% |
| English, frequent words, 64 KiB | GCC | 133 | 1,296 | 2,413 | **1,280** | −90% |
| English, frequent words, 64 KiB | Clang | 149 | 1,271 | 2,285 | **1,227** | −88% |
| Spanish, PHP names, 4 KiB | GCC | 63.6 | **90.4** | 115 | ≈464 | −30% |
| Spanish, PHP names, 4 KiB | Clang | 64.7 | **84.6** | 118 | ≈488 | −23% |
| Spanish, PHP names, 64 KiB | GCC | 153 | 1,352 | 1,650 | **1,083** | −86% |
| Spanish, PHP names, 64 KiB | Clang | 169 | 1,287 | 1,664 | **1,085** | −85% |
| Spanish, frequent words, 4 KiB | GCC | 41.7 | **114** | 150 | 227 | −63% |
| Spanish, frequent words, 4 KiB | Clang | 43.5 | **109** | 150 | 235 | −60% |
| Spanish, frequent words, 64 KiB | GCC | 139 | 1,523 | 2,283 | **1,165** | −88% |
| Spanish, frequent words, 64 KiB | Clang | 156 | 1,510 | 2,313 | **1,167** | −87% |
| Japanese, PHP names, 4 KiB | GCC | 61.6 | 70.9 | **50.5** | ≈441 | +22% |
| Japanese, PHP names, 4 KiB | Clang | 60.4 | 66.1 | **52.8** | ≈463 | +14%† |
| Japanese, PHP names, 64 KiB | GCC | 128 | 1,067 | **620** | 672 | −80% |
| Japanese, PHP names, 64 KiB | Clang | 124 | 989 | **633** | 688 | −80% |
| Japanese, frequent words, 4 KiB | GCC | 52.8 | 209 | **67.3** | 155 | −22% |
| Japanese, frequent words, 4 KiB | Clang | 51.7 | 209 | **66.6** | 161 | −22% |
| Japanese, frequent words, 64 KiB | GCC | 162 | 2,015 | 951 | **539** | −70%† |
| Japanese, frequent words, 64 KiB | Clang | 163 | 2,002 | 929 | **537** | −70% |
| Korean, PHP names, 4 KiB | GCC | 62.1 | 71 | **50.2** | ≈439 | +24%† |
| Korean, PHP names, 4 KiB | Clang | 62.2 | 66.3 | **51.7** | ≈459 | +21% |
| Korean, PHP names, 64 KiB | GCC | 136 | 1,077 | **641** | 684 | −79% |
| Korean, PHP names, 64 KiB | Clang | 136 | 999 | **650** | 696 | −79% |
| Korean, frequent words, 4 KiB | GCC | 40.9 | 151 | **56.7** | 205 | −28% |
| Korean, frequent words, 4 KiB | Clang | 42.6 | 146 | **57.2** | 213 | −25% |
| Korean, frequent words, 64 KiB | GCC | 146 | 1,963 | 815 | **536** | −73% |
| Korean, frequent words, 64 KiB | Clang | 155 | 1,920 | 827 | **546** | −71% |
| Russian, PHP names, 4 KiB | GCC | 61.5 | 68.6 | **40.9** | ≈437 | +49%† |
| Russian, PHP names, 4 KiB | Clang | 60.2 | 63.3 | **42.5** | ≈455 | +41% |
| Russian, PHP names, 64 KiB | GCC | 120 | 1,020 | **474** | 616 | −75%† |
| Russian, PHP names, 64 KiB | Clang | 113 | 951 | **478** | 631 | −76% |
| Russian, frequent words, 4 KiB | GCC | 72.5 | 221 | **79.3** | 345 | −8.0% |
| Russian, frequent words, 4 KiB | Clang | 70.1 | 217 | **77.4** | 361 | −9.1% |
| Russian, frequent words, 64 KiB | GCC | 209 | 3,000 | 1,135 | **757** | −72% |
| Russian, frequent words, 64 KiB | Clang | 212 | 2,973 | 1,132 | **778** | −73% |
| Chinese, PHP names, 4 KiB | GCC | 62.2 | 73.1 | **58.4** | ≈440 | +5.2%† |
| Chinese, PHP names, 4 KiB | Clang | 61.7 | 67 | **60.5** | ≈457 | +0.8% |
| Chinese, PHP names, 64 KiB | GCC | 137 | 1,089 | 768 | **721** | −81% |
| Chinese, PHP names, 64 KiB | Clang | 138 | 1,022 | 777 | **743** | −81% |
| Chinese, frequent words, 4 KiB | GCC | 51.9 | 105 | **47.9** | 155 | +8.8% |
| Chinese, frequent words, 4 KiB | Clang | 51.2 | 103 | **49.3** | 159 | +3.6% |
| Chinese, frequent words, 64 KiB | GCC | 133 | 1,274 | 648 | **462** | −71% |
| Chinese, frequent words, 64 KiB | Clang | 131 | 1,263 | 673 | **463** | −72% |

### `countMatches()`

**prepared**

| Input | Compiler | New class, µs | `strpos()` loop, µs | `substr_count()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| English with emoji, PHP names, 4 KiB | GCC | 5.91 | 84.9 | 85.4 | 88.7 | **33.9** | −83% |
| English with emoji, PHP names, 4 KiB | Clang | 6.96 | 80.2 | 80.1 | 87.7 | **34.8** | −80% |
| English with emoji, PHP names, 64 KiB | GCC | 89.9 | 1,286 | 1,285 | 1,408 | **520** | −83% |
| English with emoji, PHP names, 64 KiB | Clang | 107 | 1,197 | 1,200 | 1,390 | **539** | −80% |
| English with emoji, frequent words, 4 KiB | GCC | 6.38 | 92.1 | 92.2 | 121 | **57.8** | −89% |
| English with emoji, frequent words, 4 KiB | Clang | 7.27 | 90.9 | 90.9 | 119 | **57.3** | −87% |
| English with emoji, frequent words, 64 KiB | GCC | 98.5 | 1,519 | 1,502 | 1,920 | **893** | −89%† |
| English with emoji, frequent words, 64 KiB | Clang | 111 | 1,489 | 1,471 | 1,871 | **880** | −87% |
| English, PHP names, 4 KiB | GCC | 5.96 | 89 | 89.4 | 104 | **38.9** | −85% |
| English, PHP names, 4 KiB | Clang | 7.02 | 84.3 | 84.6 | 102 | **40.2** | −83% |
| English, PHP names, 64 KiB | GCC | 93.5 | 1,355 | 1,359 | 1,669 | **604** | −84% |
| English, PHP names, 64 KiB | Clang | 111 | 1,275 | 1,270 | 1,646 | **635** | −83% |
| English, frequent words, 4 KiB | GCC | 6.54 | 102 | 102 | 145 | **67.6** | −90% |
| English, frequent words, 4 KiB | Clang | 7.39 | 99.6 | 100 | 140 | **66.4** | −89% |
| English, frequent words, 64 KiB | GCC | 99.7 | 1,636 | 1,611 | 2,258 | **1,046** | −91% |
| English, frequent words, 64 KiB | Clang | 112 | 1,612 | 1,599 | 2,190 | **1,009** | −89% |
| Spanish, PHP names, 4 KiB | GCC | 6.04 | 90.9 | 90.8 | 104 | **40** | −85% |
| Spanish, PHP names, 4 KiB | Clang | 7.05 | 84.8 | 85.1 | 101 | **40.8** | −83% |
| Spanish, PHP names, 64 KiB | GCC | 92.6 | 1,378 | 1,378 | 1,654 | **615** | −85% |
| Spanish, PHP names, 64 KiB | Clang | 109 | 1,290 | 1,287 | 1,608 | **633** | −83% |
| Spanish, frequent words, 4 KiB | GCC | 6.54 | 117 | 116 | 136 | **60.3** | −89% |
| Spanish, frequent words, 4 KiB | Clang | 7.46 | 115 | 114 | 134 | **60.6** | −88% |
| Spanish, frequent words, 64 KiB | GCC | 101 | 1,884 | 1,873 | 2,132 | **908** | −89% |
| Spanish, frequent words, 64 KiB | Clang | 115 | 1,850 | 1,838 | 2,119 | **921** | −88% |
| Japanese, PHP names, 4 KiB | GCC | 4.08 | 71.1 | 71.4 | 40.5 | **15.5** | −74% |
| Japanese, PHP names, 4 KiB | Clang | 4.43 | 66.9 | 66.7 | 39.5 | **15.9** | −72% |
| Japanese, PHP names, 64 KiB | GCC | 59.6 | 1,066 | 1,067 | 650 | **238** | −75% |
| Japanese, PHP names, 64 KiB | Clang | 66.2 | 992 | 999 | 634 | **245** | −73% |
| Japanese, frequent words, 4 KiB | GCC | 7.62 | ≈218 | ≈219 | 60.5 | **25.3** | −70% |
| Japanese, frequent words, 4 KiB | Clang | 7.9 | ≈219 | ≈218 | 58.4 | **25.4** | −69% |
| Japanese, frequent words, 64 KiB | GCC | 114 | ≈2,846 | ≈2,793 | 958 | **388** | −70% |
| Japanese, frequent words, 64 KiB | Clang | 120 | ≈2,860 | ≈2,857 | 934 | **395** | −70% |
| Korean, PHP names, 4 KiB | GCC | 4.31 | 71.1 | 71.6 | 39.5 | **15.4** | −72% |
| Korean, PHP names, 4 KiB | Clang | 4.79 | 66.7 | 66.8 | 38.8 | **16** | −70% |
| Korean, PHP names, 64 KiB | GCC | 65.2 | 1,066 | 1,068 | 604 | **232** | −72% |
| Korean, PHP names, 64 KiB | Clang | 72.8 | 999 | 1,002 | 596 | **244** | −70% |
| Korean, frequent words, 4 KiB | GCC | 6.49 | ≈153 | ≈153 | 46.6 | **20.2** | −68% |
| Korean, frequent words, 4 KiB | Clang | 7.17 | ≈148 | ≈148 | 45.7 | **20.8** | −66% |
| Korean, frequent words, 64 KiB | GCC | 103 | ≈2,604 | ≈2,594 | 734 | **309** | −67% |
| Korean, frequent words, 64 KiB | Clang | 115 | ≈2,491 | ≈2,523 | 728 | **319** | −64% |
| Russian, PHP names, 4 KiB | GCC | 3.54 | ≈67.9 | ≈68.1 | 28.3 | **11.3** | −69% |
| Russian, PHP names, 4 KiB | Clang | 3.76 | ≈63.3 | ≈63.4 | 27.6 | **11.6** | −68% |
| Russian, PHP names, 64 KiB | GCC | 50.1 | ≈1,076 | ≈1,068 | 443 | **170** | −70% |
| Russian, PHP names, 64 KiB | Clang | 53.5 | ≈1,005 | ≈1,006 | 436 | **174** | −69% |
| Russian, frequent words, 4 KiB | GCC | 8.71 | ≈224 | ≈224 | 71.8 | **27.4** | −68% |
| Russian, frequent words, 4 KiB | Clang | 8.96 | ≈221 | ≈219 | 71.4 | **27.7** | −68% |
| Russian, frequent words, 64 KiB | GCC | 129 | ≈3,587 | ≈3,581 | 1,145 | **422** | −69% |
| Russian, frequent words, 64 KiB | Clang | 135 | ≈3,540 | ≈3,481 | 1,144 | **426** | −68% |
| Chinese, PHP names, 4 KiB | GCC | 4.59 | 73.2 | 73.2 | 47.8 | **18.4** | −75% |
| Chinese, PHP names, 4 KiB | Clang | 5.03 | 68.8 | 68.9 | 46.7 | **18.9** | −73% |
| Chinese, PHP names, 64 KiB | GCC | 69.9 | 1,117 | 1,121 | 785 | **288** | −76% |
| Chinese, PHP names, 64 KiB | Clang | 77.9 | 1,036 | 1,039 | 768 | **298** | −74% |
| Chinese, frequent words, 4 KiB | GCC | 5.44 | ≈105 | ≈104 | 39.1 | **20.2** | −73% |
| Chinese, frequent words, 4 KiB | Clang | 5.62 | ≈98 | ≈97.3 | 39.7 | **20** | −72% |
| Chinese, frequent words, 64 KiB | GCC | 83.9 | ≈1,601 | 1,863 | 644 | **318** | −74% |
| Chinese, frequent words, 64 KiB | Clang | 89.5 | 1,878 | 1,826 | 647 | **315** | −72% |

**one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | `substr_count()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| English with emoji, PHP names, 4 KiB | GCC | 64 | 84.8 | **84.5** | 100 | ≈457 | −25% |
| English with emoji, PHP names, 4 KiB | Clang | 63.5 | **79.8** | 80 | 101 | ≈481 | −21%† |
| English with emoji, PHP names, 64 KiB | GCC | 149 | 1,274 | 1,276 | 1,426 | **948** | −84% |
| English with emoji, PHP names, 64 KiB | Clang | 164 | 1,203 | 1,201 | 1,401 | **994** | −84% |
| English with emoji, frequent words, 4 KiB | GCC | 37.5 | **91.8** | 92.3 | 129 | 207 | −60% |
| English with emoji, frequent words, 4 KiB | Clang | 40.1 | **91.2** | 91.5 | 127 | 211 | −56% |
| English with emoji, frequent words, 64 KiB | GCC | 131 | 1,524 | 1,507 | 1,934 | **1,048** | −87% |
| English with emoji, frequent words, 64 KiB | Clang | 146 | 1,494 | 1,466 | 1,893 | **1,041** | −86% |
| English, PHP names, 4 KiB | GCC | 65 | **89.3** | 89.6 | 117 | ≈463 | −28% |
| English, PHP names, 4 KiB | Clang | 64 | **84.6** | 84.7 | 116 | ≈494 | −24% |
| English, PHP names, 64 KiB | GCC | 156 | 1,372 | 1,370 | 1,691 | **1,044** | −85% |
| English, PHP names, 64 KiB | Clang | 170 | 1,272 | 1,282 | 1,654 | **1,079** | −84% |
| English, frequent words, 4 KiB | GCC | 37.2 | **101** | 101 | 151 | 214 | −63% |
| English, frequent words, 4 KiB | Clang | 39.9 | **99.5** | 99.7 | 146 | 220 | −60% |
| English, frequent words, 64 KiB | GCC | 131 | 1,633 | 1,651 | 2,257 | **1,192** | −89% |
| English, frequent words, 64 KiB | Clang | 146 | 1,609 | 1,597 | 2,208 | **1,189** | −88% |
| Spanish, PHP names, 4 KiB | GCC | 63.8 | **90.1** | 91 | 115 | ≈464 | −29% |
| Spanish, PHP names, 4 KiB | Clang | 63.7 | **85** | 85.8 | 115 | ≈486 | −25% |
| Spanish, PHP names, 64 KiB | GCC | 153 | 1,370 | 1,368 | 1,657 | **1,052** | −85% |
| Spanish, PHP names, 64 KiB | Clang | 166 | 1,279 | 1,288 | 1,622 | **1,088** | −85% |
| Spanish, frequent words, 4 KiB | GCC | 41 | 116 | **116** | 143 | 220 | −64% |
| Spanish, frequent words, 4 KiB | Clang | 43.7 | 114 | **114** | 141 | 227 | −62% |
| Spanish, frequent words, 64 KiB | GCC | 137 | 1,885 | 1,871 | 2,140 | **1,076** | −87% |
| Spanish, frequent words, 64 KiB | Clang | 154 | 1,854 | 1,845 | 2,138 | **1,096** | −86% |
| Japanese, PHP names, 4 KiB | GCC | 60.8 | 71.4 | 71.7 | **52.4** | ≈439 | +17% |
| Japanese, PHP names, 4 KiB | Clang | 61.2 | 66.8 | 66.4 | **53.3** | ≈466 | +13%† |
| Japanese, PHP names, 64 KiB | GCC | 123 | 1,060 | 1,059 | **658** | 668 | −81% |
| Japanese, PHP names, 64 KiB | Clang | 126 | 992 | 991 | **652** | 697 | −81% |
| Japanese, frequent words, 4 KiB | GCC | 52.2 | 228 | 226 | **65.4** | 151 | −21% |
| Japanese, frequent words, 4 KiB | Clang | 52 | 229 | 227 | **63.4** | 157 | −18% |
| Japanese, frequent words, 64 KiB | GCC | 162 | ≈2,869 | ≈2,851 | 971 | **514** | −68% |
| Japanese, frequent words, 64 KiB | Clang | 167 | ≈2,842 | ≈2,846 | 934 | **535** | −68% |
| Korean, PHP names, 4 KiB | GCC | 61.9 | 71.4 | 71.9 | **51.1** | ≈432 | +21% |
| Korean, PHP names, 4 KiB | Clang | 60.8 | 66.5 | 67.1 | **52.1** | ≈464 | +16%† |
| Korean, PHP names, 64 KiB | GCC | 132 | 1,077 | 1,072 | **617** | 658 | −79% |
| Korean, PHP names, 64 KiB | Clang | 134 | 1,004 | 1,006 | **612** | 700 | −78% |
| Korean, frequent words, 4 KiB | GCC | 40.6 | 153 | 153 | **52.3** | 201 | −23% |
| Korean, frequent words, 4 KiB | Clang | 42.4 | 149 | 149 | **51.8** | 209 | −18% |
| Korean, frequent words, 64 KiB | GCC | 142 | ≈2,607 | ≈2,606 | 744 | **494** | −71% |
| Korean, frequent words, 64 KiB | Clang | 156 | ≈2,559 | 2,349 | 737 | **514** | −70% |
| Russian, PHP names, 4 KiB | GCC | 60.4 | 68.5 | 69.1 | **40** | ≈439 | +51%† |
| Russian, PHP names, 4 KiB | Clang | 59.5 | 64.1 | 64.8 | **41.1** | ≈460 | +44%† |
| Russian, PHP names, 64 KiB | GCC | 113 | 1,033 | 1,032 | **465** | 602 | −75% |
| Russian, PHP names, 64 KiB | Clang | 114 | 955 | 952 | **457** | 632 | −75% |
| Russian, frequent words, 4 KiB | GCC | 72.9 | 225 | 225 | **78.6** | 342 | −7.0% |
| Russian, frequent words, 4 KiB | Clang | 71.1 | 222 | 223 | **78.2** | 362 | −10% |
| Russian, frequent words, 64 KiB | GCC | 206 | 3,510 | 3,511 | 1,148 | **731** | −72% |
| Russian, frequent words, 64 KiB | Clang | 208 | 3,460 | 3,467 | 1,155 | **761** | −73% |
| Chinese, PHP names, 4 KiB | GCC | 61.6 | 73.6 | 74.2 | **60.2** | ≈444 | +3.9% |
| Chinese, PHP names, 4 KiB | Clang | 60.8 | 69.3 | 69.7 | **60.7** | ≈463 | +1.0% |
| Chinese, PHP names, 64 KiB | GCC | 136 | 1,119 | 1,119 | 797 | **721** | −81% |
| Chinese, PHP names, 64 KiB | Clang | 140 | 1,048 | 1,046 | 785 | **751** | −81% |
| Chinese, frequent words, 4 KiB | GCC | 51.8 | 109 | 108 | **45.2** | 153 | +14% |
| Chinese, frequent words, 4 KiB | Clang | 51 | 106 | 106 | **45.6** | 156 | +11% |
| Chinese, frequent words, 64 KiB | GCC | 133 | 1,913 | 1,866 | 650 | **454** | −71% |
| Chinese, frequent words, 64 KiB | Clang | 138 | 1,899 | 1,838 | 664 | **455** | −70% |

### `matchAll()`

**prepared**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| English with emoji, PHP names, 4 KiB | GCC | 5.92 | 83.3 | 88.3 | **35.6** | −83% |
| English with emoji, PHP names, 4 KiB | Clang | 7.01 | 79.1 | 89 | **34.5** | −80% |
| English with emoji, PHP names, 64 KiB | GCC | 92.6 | 1,288 | 1,395 | **550** | −83% |
| English with emoji, PHP names, 64 KiB | Clang | 109 | 1,204 | 1,422 | **532** | −79% |
| English with emoji, frequent words, 4 KiB | GCC | 7.36 | 92.4 | 131 | **63.9** | −88% |
| English with emoji, frequent words, 4 KiB | Clang | 8.44 | 91.6 | 125 | **61** | −86% |
| English with emoji, frequent words, 64 KiB | GCC | 115 | 1,528 | 2,082 | **993** | −88% |
| English with emoji, frequent words, 64 KiB | Clang | 133 | 1,495 | 1,985 | **946** | −86% |
| English, PHP names, 4 KiB | GCC | 5.97 | 89.5 | 105 | **41.7** | −86% |
| English, PHP names, 4 KiB | Clang | 7.02 | 83.9 | 106 | **39.9** | −82% |
| English, PHP names, 64 KiB | GCC | 92 | 1,371 | 1,667 | **649** | −86% |
| English, PHP names, 64 KiB | Clang | 109 | 1,285 | 1,696 | **622** | −82% |
| English, frequent words, 4 KiB | GCC | 7.77 | 101 | 155 | **75.2** | −90% |
| English, frequent words, 4 KiB | Clang | 8.85 | 99.3 | 146 | **70.5** | −87% |
| English, frequent words, 64 KiB | GCC | 119 | 1,661 | 2,426 | **1,147** | −90% |
| English, frequent words, 64 KiB | Clang | 136 | 1,640 | 2,322 | **1,090** | −87% |
| Spanish, PHP names, 4 KiB | GCC | 5.94 | 90.3 | 102 | **41.5** | −86% |
| Spanish, PHP names, 4 KiB | Clang | 7.02 | 84.7 | 104 | **40.1** | −83% |
| Spanish, PHP names, 64 KiB | GCC | 91.3 | 1,370 | 1,623 | **649** | −86% |
| Spanish, PHP names, 64 KiB | Clang | 109 | 1,279 | 1,642 | **622** | −83% |
| Spanish, frequent words, 4 KiB | GCC | 7.32 | 117 | 142 | **63.9** | −89% |
| Spanish, frequent words, 4 KiB | Clang | 8.3 | 115 | 143 | **64.1** | −87% |
| Spanish, frequent words, 64 KiB | GCC | 112 | 1,910 | 2,225 | **971** | −89% |
| Spanish, frequent words, 64 KiB | Clang | 128 | 1,882 | 2,272 | **979** | −87% |
| Japanese, PHP names, 4 KiB | GCC | 4.16 | 71.7 | 41.3 | **16.9** | −75% |
| Japanese, PHP names, 4 KiB | Clang | 4.49 | 67 | 41.6 | **16.3** | −72% |
| Japanese, PHP names, 64 KiB | GCC | 62.9 | 1,093 | 684 | **267** | −76% |
| Japanese, PHP names, 64 KiB | Clang | 65.2 | 1,013 | 689 | **256** | −75% |
| Japanese, frequent words, 4 KiB | GCC | 8.9 | ≈230 | 64.7 | **29.3** | −70% |
| Japanese, frequent words, 4 KiB | Clang | 8.75 | ≈229 | 63 | **28.2** | −69% |
| Japanese, frequent words, 64 KiB | GCC | 133 | ≈3,986 | 994 | **432** | −70% |
| Japanese, frequent words, 64 KiB | Clang | 129 | ≈3,964 | 973 | **420** | −69% |
| Korean, PHP names, 4 KiB | GCC | 4.28 | 71 | 38.4 | **16.1** | −73% |
| Korean, PHP names, 4 KiB | Clang | 4.76 | 66.7 | 38.8 | **15.6** | −69% |
| Korean, PHP names, 64 KiB | GCC | 67.8 | 1,078 | 615 | **249** | −73% |
| Korean, PHP names, 64 KiB | Clang | 77.6 | 1,006 | 624 | **240** | −68% |
| Korean, frequent words, 4 KiB | GCC | 6.98 | ≈163 | 49.2 | **22.4** | −69% |
| Korean, frequent words, 4 KiB | Clang | 7.46 | ≈156 | 49.9 | **22.3** | −67% |
| Korean, frequent words, 64 KiB | GCC | 109 | ≈2,498 | 796 | **348** | −69% |
| Korean, frequent words, 64 KiB | Clang | 117 | ≈2,466 | 797 | **345** | −66% |
| Russian, PHP names, 4 KiB | GCC | 3.56 | ≈70.1 | 28.5 | **12.1** | −71% |
| Russian, PHP names, 4 KiB | Clang | 3.76 | ≈65.9 | 28.9 | **11.7** | −68% |
| Russian, PHP names, 64 KiB | GCC | 52.9 | ≈1,100 | 441 | **179** | −70% |
| Russian, PHP names, 64 KiB | Clang | 52.5 | ≈1,017 | 443 | **171** | −69% |
| Russian, frequent words, 4 KiB | GCC | 8.93 | ≈231 | 72.6 | **29.1** | −69% |
| Russian, frequent words, 4 KiB | Clang | 9.08 | ≈223 | 71.2 | **28.9** | −69% |
| Russian, frequent words, 64 KiB | GCC | 136 | ≈3,662 | 1,156 | **454** | −70% |
| Russian, frequent words, 64 KiB | Clang | 136 | ≈3,541 | 1,143 | **451** | −70%† |
| Chinese, PHP names, 4 KiB | GCC | 4.49 | 72.6 | 46.6 | **19.2** | −76% |
| Chinese, PHP names, 4 KiB | Clang | 4.94 | 68.3 | 47.4 | **18.4** | −73% |
| Chinese, PHP names, 64 KiB | GCC | 70.6 | 1,098 | 742 | **294** | −76% |
| Chinese, PHP names, 64 KiB | Clang | 75.8 | 1,030 | 752 | **284** | −73% |
| Chinese, frequent words, 4 KiB | GCC | 6.12 | 108 | 42.5 | **22.4** | −73% |
| Chinese, frequent words, 4 KiB | Clang | 5.89 | 107 | 43.2 | **21.7** | −73% |
| Chinese, frequent words, 64 KiB | GCC | 90.9 | ≈2,114 | 653 | **333** | −73% |
| Chinese, frequent words, 64 KiB | Clang | 87.8 | ≈2,115 | 673 | **325** | −73% |

**one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| English with emoji, PHP names, 4 KiB | GCC | 62.4 | **83.7** | 100 | ≈464 | −25% |
| English with emoji, PHP names, 4 KiB | Clang | 63.1 | **80.1** | 102 | ≈475 | −20% |
| English with emoji, PHP names, 64 KiB | GCC | 153 | 1,280 | 1,418 | **988** | −85% |
| English with emoji, PHP names, 64 KiB | Clang | 167 | 1,204 | 1,431 | **982** | −83% |
| English with emoji, frequent words, 4 KiB | GCC | 37.9 | **93.1** | 137 | 213 | −59% |
| English with emoji, frequent words, 4 KiB | Clang | 40.9 | **91.5** | 131 | 215 | −55% |
| English with emoji, frequent words, 64 KiB | GCC | 148 | 1,529 | 2,101 | **1,154** | −87% |
| English with emoji, frequent words, 64 KiB | Clang | 168 | 1,503 | 2,002 | **1,117** | −85% |
| English, PHP names, 4 KiB | GCC | 64.6 | **89.1** | 117 | ≈469 | −28% |
| English, PHP names, 4 KiB | Clang | 62.4 | **83.9** | 119 | ≈495 | −25% |
| English, PHP names, 64 KiB | GCC | 150 | 1,362 | 1,670 | **1,074** | −86% |
| English, PHP names, 64 KiB | Clang | 167 | 1,286 | 1,701 | **1,081** | −85% |
| English, frequent words, 4 KiB | GCC | 38.1 | **100** | 161 | 223 | −62% |
| English, frequent words, 4 KiB | Clang | 41.1 | **100** | 153 | 225 | −58% |
| English, frequent words, 64 KiB | GCC | 151 | 1,661 | 2,460 | **1,307** | −88% |
| English, frequent words, 64 KiB | Clang | 172 | 1,642 | 2,313 | **1,268** | −86% |
| Spanish, PHP names, 4 KiB | GCC | 63.3 | **90.6** | 115 | ≈465 | −30% |
| Spanish, PHP names, 4 KiB | Clang | 64.6 | **85.2** | 118 | ≈485 | −23% |
| Spanish, PHP names, 64 KiB | GCC | 150 | 1,361 | 1,661 | **1,084** | −86% |
| Spanish, PHP names, 64 KiB | Clang | 165 | 1,276 | 1,665 | **1,079** | −85% |
| Spanish, frequent words, 4 KiB | GCC | 41.8 | **117** | 149 | 229 | −64% |
| Spanish, frequent words, 4 KiB | Clang | 44.4 | **114** | 150 | 233 | −61% |
| Spanish, frequent words, 64 KiB | GCC | 147 | 1,913 | 2,250 | **1,148** | −87% |
| Spanish, frequent words, 64 KiB | Clang | 166 | 1,887 | 2,276 | **1,158** | −86% |
| Japanese, PHP names, 4 KiB | GCC | 60.9 | 71.7 | **53.1** | ≈444 | +16% |
| Japanese, PHP names, 4 KiB | Clang | 63.3 | 67.3 | **55.2** | ≈463 | +15% |
| Japanese, PHP names, 64 KiB | GCC | 128 | 1,081 | **698** | 701 | −82% |
| Japanese, PHP names, 64 KiB | Clang | 127 | 1,020 | **705** | 719 | −82% |
| Japanese, frequent words, 4 KiB | GCC | 53.7 | 233 | **70.5** | 158 | −24% |
| Japanese, frequent words, 4 KiB | Clang | 52.8 | 232 | **68.8** | 161 | −24%† |
| Japanese, frequent words, 64 KiB | GCC | 181 | ≈3,959 | 1,002 | **569** | −68% |
| Japanese, frequent words, 64 KiB | Clang | 181 | ≈4,032 | 976 | **565** | −68% |
| Korean, PHP names, 4 KiB | GCC | 62 | 71.7 | **50.4** | ≈436 | +22%† |
| Korean, PHP names, 4 KiB | Clang | 61.3 | 67.1 | **51.8** | ≈456 | +19% |
| Korean, PHP names, 64 KiB | GCC | 132 | 1,081 | **634** | 682 | −79%† |
| Korean, PHP names, 64 KiB | Clang | 138 | 1,006 | **639** | 695 | −78% |
| Korean, frequent words, 4 KiB | GCC | 40.6 | 154 | **55.5** | 205 | −27% |
| Korean, frequent words, 4 KiB | Clang | 42.9 | 150 | **55.7** | 214 | −23% |
| Korean, frequent words, 64 KiB | GCC | 148 | 2,460 | 803 | **536** | −72% |
| Korean, frequent words, 64 KiB | Clang | 157 | 2,419 | 811 | **540** | −71% |
| Russian, PHP names, 4 KiB | GCC | 61.3 | 68.6 | **40.2** | ≈435 | +53%† |
| Russian, PHP names, 4 KiB | Clang | 59.6 | 64 | **42.2** | ≈461 | +42% |
| Russian, PHP names, 64 KiB | GCC | 117 | 1,034 | **456** | 615 | −74% |
| Russian, PHP names, 64 KiB | Clang | 113 | 957 | **457** | 633 | −75% |
| Russian, frequent words, 4 KiB | GCC | 73.2 | 224 | **80.3** | 345 | −8.4% |
| Russian, frequent words, 4 KiB | Clang | 70.7 | 224 | **78.1** | 365 | −9.9% |
| Russian, frequent words, 64 KiB | GCC | 211 | 3,548 | 1,168 | **770** | −72% |
| Russian, frequent words, 64 KiB | Clang | 209 | 3,483 | 1,155 | **792** | −74% |
| Chinese, PHP names, 4 KiB | GCC | 61.9 | 72.2 | **58.3** | ≈447 | +5.9%† |
| Chinese, PHP names, 4 KiB | Clang | 61 | 68.8 | **60.8** | ≈465 | −0.1%† |
| Chinese, PHP names, 64 KiB | GCC | 136 | 1,106 | 758 | **729** | −81% |
| Chinese, PHP names, 64 KiB | Clang | 137 | 1,034 | 765 | **745** | −82% |
| Chinese, frequent words, 4 KiB | GCC | 52.4 | 108 | **48** | 155 | +7.7% |
| Chinese, frequent words, 4 KiB | Clang | 50.2 | 105 | **49.4** | 158 | +2.6%† |
| Chinese, frequent words, 64 KiB | GCC | 140 | 1,884 | 657 | **467** | −70% |
| Chinese, frequent words, 64 KiB | Clang | 136 | 1,856 | 675 | **464** | −71% |

### `replace()`

**prepared**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| English with emoji, PHP names, 4 KiB | GCC | 6.71 | ≈753 | 88.5 | **32.4** | −79% |
| English with emoji, PHP names, 4 KiB | Clang | 7.35 | ≈771 | 83 | **32.6** | −78%† |
| English with emoji, PHP names, 64 KiB | GCC | 103 | ≈12,796 | 1,418 | **508** | −80% |
| English with emoji, PHP names, 64 KiB | Clang | 115 | ≈13,122 | 1,326 | **510** | −78% |
| English with emoji, frequent words, 4 KiB | GCC | 7.21 | ≈273 | 99 | **43.9** | −84% |
| English with emoji, frequent words, 4 KiB | Clang | 7.99 | ≈276 | 102 | **49.1** | −84% |
| English with emoji, frequent words, 64 KiB | GCC | 108 | ≈4,185 | 1,580 | **691** | −84% |
| English with emoji, frequent words, 64 KiB | Clang | 123 | ≈4,274 | 1,635 | **774** | −84% |
| English, PHP names, 4 KiB | GCC | 6.68 | ≈718 | 104 | **37.3** | −82% |
| English, PHP names, 4 KiB | Clang | 7.46 | ≈745 | 98 | **37.7** | −80% |
| English, PHP names, 64 KiB | GCC | 105 | ≈12,811 | 1,674 | **593** | −82% |
| English, PHP names, 64 KiB | Clang | 117 | ≈13,183 | 1,574 | **595** | −80% |
| English, frequent words, 4 KiB | GCC | 7.4 | ≈289 | 117 | **51.2** | −85% |
| English, frequent words, 4 KiB | Clang | 8.21 | ≈287 | 120 | **56.8** | −86% |
| English, frequent words, 64 KiB | GCC | 112 | ≈4,899 | 1,851 | **793** | −86% |
| English, frequent words, 64 KiB | Clang | 126 | ≈4,995 | 1,886 | **893** | −86% |
| Spanish, PHP names, 4 KiB | GCC | 6.35 | ≈834 | 104 | **38.3** | −83% |
| Spanish, PHP names, 4 KiB | Clang | 7.1 | ≈853 | 97.2 | **38.4** | −81% |
| Spanish, PHP names, 64 KiB | GCC | 96.8 | ≈13,585 | 1,652 | **596** | −84% |
| Spanish, PHP names, 64 KiB | Clang | 109 | ≈13,614 | 1,548 | **596** | −82% |
| Spanish, frequent words, 4 KiB | GCC | 7.21 | ≈320 | 117 | **49.9** | −86% |
| Spanish, frequent words, 4 KiB | Clang | 7.97 | ≈321 | 121 | **49.7** | −84% |
| Spanish, frequent words, 64 KiB | GCC | 108 | ≈5,128 | 1,837 | **775** | −86% |
| Spanish, frequent words, 64 KiB | Clang | 122 | ≈5,189 | 1,917 | **772** | −84% |
| Japanese, PHP names, 4 KiB | GCC | 4.57 | ≈271 | 40.4 | **15** | −70% |
| Japanese, PHP names, 4 KiB | Clang | 4.27 | ≈278 | 38 | **15** | −72% |
| Japanese, PHP names, 64 KiB | GCC | 67 | ≈4,269 | 615 | **221** | −70% |
| Japanese, PHP names, 64 KiB | Clang | 62.7 | ≈4,255 | 582 | **223** | −72% |
| Japanese, frequent words, 4 KiB | GCC | 6.01 | 15.4 | 35.8 | **13.4** | −55% |
| Japanese, frequent words, 4 KiB | Clang | 5.93 | 14.9 | 35.8 | **13.6** | −56% |
| Japanese, frequent words, 64 KiB | GCC | 93 | 243 | 585 | **209** | −56% |
| Japanese, frequent words, 64 KiB | Clang | 91.8 | 237 | 589 | **215** | −58%† |
| Korean, PHP names, 4 KiB | GCC | 4.9 | ≈290 | 38.1 | **14.5** | −66% |
| Korean, PHP names, 4 KiB | Clang | 4.73 | ≈297 | 35.8 | **14.6** | −68% |
| Korean, PHP names, 64 KiB | GCC | 75.9 | ≈4,303 | 636 | **232** | −67% |
| Korean, PHP names, 64 KiB | Clang | 71.6 | ≈4,280 | 591 | **232** | −70% |
| Korean, frequent words, 4 KiB | GCC | 6.93 | 32.9 | 36.2 | **14.5** | −52% |
| Korean, frequent words, 4 KiB | Clang | 7.14 | 32.1 | 36.4 | **14.7** | −52% |
| Korean, frequent words, 64 KiB | GCC | 103 | 480 | 534 | **206** | −50% |
| Korean, frequent words, 64 KiB | Clang | 109 | 467 | 534 | **208** | −48% |
| Russian, PHP names, 4 KiB | GCC | 3.93 | ≈299 | 29.1 | **11.2** | −65% |
| Russian, PHP names, 4 KiB | Clang | 3.57 | ≈315 | 27.3 | **11.3** | −69% |
| Russian, PHP names, 64 KiB | GCC | 60 | ≈2,504 | 460 | **170** | −65% |
| Russian, PHP names, 64 KiB | Clang | 55.2 | ≈2,547 | 433 | **171** | −68% |
| Russian, frequent words, 4 KiB | GCC | 9.19 | ≈181 | 62.7 | **21.7** | −58% |
| Russian, frequent words, 4 KiB | Clang | 9.1 | ≈183 | 62.5 | **21.7** | −58% |
| Russian, frequent words, 64 KiB | GCC | 134 | ≈3,074 | 989 | **329** | −59% |
| Russian, frequent words, 64 KiB | Clang | 133 | ≈3,144 | 982 | **327** | −59% |
| Chinese, PHP names, 4 KiB | GCC | 5.11 | ≈340 | 46.2 | **17.2** | −70% |
| Chinese, PHP names, 4 KiB | Clang | 4.85 | ≈352 | 43.3 | **17.1** | −72% |
| Chinese, PHP names, 64 KiB | GCC | 79.3 | ≈6,069 | 732 | **262** | −70% |
| Chinese, PHP names, 64 KiB | Clang | 77.2 | ≈5,996 | 678 | **262** | −71% |
| Chinese, frequent words, 4 KiB | GCC | 5.63 | 14.1 | 28.6 | **11.6** | −52% |
| Chinese, frequent words, 4 KiB | Clang | 5.39 | 13.5 | 28.7 | **11.6** | −54% |
| Chinese, frequent words, 64 KiB | GCC | 85.4 | 217 | 453 | **178** | −52% |
| Chinese, frequent words, 64 KiB | Clang | 81.2 | 209 | 458 | **176** | −54% |

**one-shot**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| English with emoji, PHP names, 4 KiB | GCC | 73.6 | ≈746 | **100** | ≈452 | −27% |
| English with emoji, PHP names, 4 KiB | Clang | 77.1 | ≈768 | **95.9** | ≈476 | −20%† |
| English with emoji, PHP names, 64 KiB | GCC | 176 | ≈12,870 | 1,439 | **945** | −81% |
| English with emoji, PHP names, 64 KiB | Clang | 186 | ≈13,120 | 1,338 | **968** | −81% |
| English with emoji, frequent words, 4 KiB | GCC | 36.1 | 256 | **106** | 191 | −66% |
| English with emoji, frequent words, 4 KiB | Clang | 38.4 | 259 | **107** | 200 | −64% |
| English with emoji, frequent words, 64 KiB | GCC | 140 | ≈4,243 | 1,603 | **846** | −83% |
| English with emoji, frequent words, 64 KiB | Clang | 155 | 4,140 | 1,622 | **920** | −83% |
| English, PHP names, 4 KiB | GCC | 74.5 | ≈729 | **116** | ≈461 | −35% |
| English, PHP names, 4 KiB | Clang | 76.9 | ≈750 | **112** | ≈487 | −31%† |
| English, PHP names, 64 KiB | GCC | 178 | ≈12,880 | 1,702 | **1,028** | −83% |
| English, PHP names, 64 KiB | Clang | 187 | ≈13,322 | 1,577 | **1,045** | −82% |
| English, frequent words, 4 KiB | GCC | 36.5 | 296 | **123** | 199 | −70% |
| English, frequent words, 4 KiB | Clang | 38.5 | 300 | **125** | 209 | −69% |
| English, frequent words, 64 KiB | GCC | 144 | ≈4,824 | 1,854 | **949** | −85% |
| English, frequent words, 64 KiB | Clang | 158 | 4,740 | 1,902 | **1,055** | −85% |
| Spanish, PHP names, 4 KiB | GCC | 74.8 | ≈837 | **116** | ≈461 | −35%† |
| Spanish, PHP names, 4 KiB | Clang | 75.5 | ≈850 | **111** | ≈487 | −31% |
| Spanish, PHP names, 64 KiB | GCC | 169 | ≈13,471 | 1,651 | **1,025** | −84% |
| Spanish, PHP names, 64 KiB | Clang | 179 | ≈13,830 | 1,562 | **1,054** | −83% |
| Spanish, frequent words, 4 KiB | GCC | 44.4 | 315 | **123** | 210 | −64% |
| Spanish, frequent words, 4 KiB | Clang | 46 | 316 | **127** | 216 | −64% |
| Spanish, frequent words, 64 KiB | GCC | 148 | ≈5,248 | 1,846 | **929** | −84% |
| Spanish, frequent words, 64 KiB | Clang | 164 | ≈5,141 | 1,937 | **932** | −83% |
| Japanese, PHP names, 4 KiB | GCC | 71 | ≈272 | **52.5** | ≈437 | +34%† |
| Japanese, PHP names, 4 KiB | Clang | 73.7 | ≈278 | **51.3** | ≈462 | +45% |
| Japanese, PHP names, 64 KiB | GCC | 143 | ≈4,164 | **630** | 651 | −77% |
| Japanese, PHP names, 64 KiB | Clang | 133 | ≈4,322 | **593** | 682 | −78% |
| Japanese, frequent words, 4 KiB | GCC | 54.4 | **15.6** | 41.1 | ≈132 | +248% |
| Japanese, frequent words, 4 KiB | Clang | 53.6 | **15.1** | 41.5 | ≈138 | +256% |
| Japanese, frequent words, 64 KiB | GCC | 145 | **245** | 590 | 332 | −41% |
| Japanese, frequent words, 64 KiB | Clang | 143 | **238** | 597 | 343 | −40% |
| Korean, PHP names, 4 KiB | GCC | 71.3 | ≈289 | **50.3** | ≈435 | +42%† |
| Korean, PHP names, 4 KiB | Clang | 71.4 | ≈297 | **48.8** | ≈455 | +47%† |
| Korean, PHP names, 64 KiB | GCC | 152 | ≈4,163 | **642** | 664 | −76% |
| Korean, PHP names, 64 KiB | Clang | 146 | ≈4,361 | **602** | 685 | −76% |
| Korean, frequent words, 4 KiB | GCC | 39.4 | **33.1** | 42 | ≈195 | +19% |
| Korean, frequent words, 4 KiB | Clang | 40.2 | **32.2** | 41.9 | ≈203 | +25% |
| Korean, frequent words, 64 KiB | GCC | 140 | 478 | 540 | **392** | −64% |
| Korean, frequent words, 64 KiB | Clang | 145 | 464 | 542 | **400** | −64% |
| Russian, PHP names, 4 KiB | GCC | 72.9 | ≈305 | **40.6** | ≈438 | +79%† |
| Russian, PHP names, 4 KiB | Clang | 71 | ≈313 | **40.7** | ≈469 | +74%† |
| Russian, PHP names, 64 KiB | GCC | 136 | 3,504 | **465** | 597 | −71% |
| Russian, PHP names, 64 KiB | Clang | 127 | ≈2,544 | **442** | 625 | −72% |
| Russian, frequent words, 4 KiB | GCC | 73.3 | 184 | **70** | 336 | +4.8% |
| Russian, frequent words, 4 KiB | Clang | 70.5 | 182 | **68.9** | ≈355 | +2.5% |
| Russian, frequent words, 64 KiB | GCC | 209 | 2,866 | 997 | **647** | −67% |
| Russian, frequent words, 64 KiB | Clang | 206 | 2,885 | 993 | **657** | −69%† |
| Chinese, PHP names, 4 KiB | GCC | 73.9 | ≈345 | **57.7** | ≈443 | +28%† |
| Chinese, PHP names, 4 KiB | Clang | 72.6 | ≈354 | **56.3** | ≈466 | +31%† |
| Chinese, PHP names, 64 KiB | GCC | 159 | ≈5,879 | 747 | **695** | −77% |
| Chinese, PHP names, 64 KiB | Clang | 152 | ≈6,070 | **695** | 714 | −78% |
| Chinese, frequent words, 4 KiB | GCC | 51.5 | **14.1** | 34 | ≈134 | +266% |
| Chinese, frequent words, 4 KiB | Clang | 52.1 | **13.4** | 34.3 | ≈137 | +289%† |
| Chinese, frequent words, 64 KiB | GCC | 136 | **218** | 460 | 307 | −38% |
| Chinese, frequent words, 64 KiB | Clang | 131 | **209** | 463 | 309 | −37% |

## Application scenarios

### Bot detection: is this User-Agent a crawler?

**prepared**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | `str_contains()` loop, second copy, µs | PCRE alternation, µs | PCRE alternation in chunks of 1024, µs | PCRE alternation in chunks of 512, µs | PCRE, shared prefixes, µs | PCRE, shared prefixes in chunks of 1024, µs | PCRE, shared prefixes in chunks of 512, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| all texts of the scenario | GCC | 0.27 | ≈34.5 | ≈34.6 | ≈133 | ≈102 | ≈74.6 | **3.15** | 4.41 | 6.1 | −92% |
| all texts of the scenario | Clang | 0.27 | ≈36.1 | ≈36.1 | ≈133 | ≈99 | ≈72.3 | **3.15** | 4.44 | 6.02 | −91% |

**one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | `str_contains()` loop, second copy, µs | PCRE alternation, µs | PCRE alternation in chunks of 1024, µs | PCRE alternation in chunks of 512, µs | PCRE, shared prefixes, µs | PCRE, shared prefixes in chunks of 1024, µs | PCRE, shared prefixes in chunks of 512, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| all texts of the scenario | GCC | 1,019 | **32.7** | 32.8 | ≈251 | ≈186 | 179 | ≈3,092 | ≈3,371 | ≈3,400 | +3004% |
| all texts of the scenario | Clang | 1,010 | 34 | **34** | ≈251 | ≈182 | 175 | ≈3,231 | ≈3,479 | ≈3,550 | +2873% |

### Moderation: does a comment contain a listed word?

**prepared**

| Input | Compiler | New class, µs | `strtolower()` + `str_contains()` loop, µs | `stripos()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| all texts of the scenario | GCC | 0.53 | 20.2 | ≈23.5 | ≈66.4 | **4.24** | −87% |
| all texts of the scenario | Clang | 0.55 | 21.5 | 24 | ≈73.8 | **4.36** | −87% |

**one-shot**

| Input | Compiler | New class, µs | `strtolower()` + `str_contains()` loop, µs | `stripos()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| all texts of the scenario | GCC | 119 | **20.4** | 24.9 | 82.5 | ≈508 | +483% |
| all texts of the scenario | Clang | 111 | **21.7** | 24.2 | 87.6 | ≈525 | +417% |

### Auto-linking, all pages, 3,345 names: which names occur?

**prepared**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE alternation in chunks of 1024, µs | PCRE alternation in chunks of 512, µs | PCRE, shared prefixes, µs | PCRE, shared prefixes in chunks of 1024, µs | PCRE, shared prefixes in chunks of 512, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| all texts of the scenario | GCC | 2.03 | ≈759 | too large | ≈852 | ≈629 | **27.3** | 49 | 82 | −93% |
| all texts of the scenario | Clang | 2.23 | ≈733 | too large | ≈860 | ≈632 | **28.1** | 50.1 | 82.1 | −92% |

**one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE alternation in chunks of 1024, µs | PCRE alternation in chunks of 512, µs | PCRE, shared prefixes, µs | PCRE, shared prefixes in chunks of 1024, µs | PCRE, shared prefixes in chunks of 512, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| all texts of the scenario | GCC | 1,651 | **618** | too large | 1,833 | 1,373 | ≈7,476 | ≈8,634 | ≈9,066 | +167% |
| all texts of the scenario | Clang | 1,620 | **585** | too large | 1,828 | 1,371 | ≈7,933 | ≈9,075 | ≈9,529 | +177% |

### Bot detection: which crawler patterns match?

**prepared**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE alternation in chunks of 1024, µs | PCRE alternation in chunks of 512, µs | PCRE, shared prefixes, µs | PCRE, shared prefixes in chunks of 1024, µs | PCRE, shared prefixes in chunks of 512, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| all texts of the scenario | GCC | 0.33 | ≈37.2 | ≈134 | ≈107 | ≈79.8 | **3.84** | 5.7 | 7.67 | −91% |
| all texts of the scenario | Clang | 0.34 | ≈38.6 | ≈137 | ≈107 | ≈77.4 | **3.85** | 5.88 | 7.92 | −91% |

**one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE alternation in chunks of 1024, µs | PCRE alternation in chunks of 512, µs | PCRE, shared prefixes, µs | PCRE, shared prefixes in chunks of 1024, µs | PCRE, shared prefixes in chunks of 512, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| all texts of the scenario | GCC | 1,013 | **35.8** | ≈265 | ≈209 | ≈185 | ≈3,104 | ≈3,359 | ≈3,398 | +2730% |
| all texts of the scenario | Clang | 1,008 | **37.3** | ≈267 | ≈211 | 188 | ≈3,254 | ≈3,464 | ≈3,524 | +2604% |

### Moderation: which listed words occur?

**prepared**

| Input | Compiler | New class, µs | `strtolower()` + `str_contains()` loop, µs | `stripos()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| all texts of the scenario | GCC | 0.64 | 25.9 | 31.5 | ≈82.9 | **8.54** | −93% |
| all texts of the scenario | Clang | 0.66 | 27.3 | 30.4 | ≈90.2 | **8.82** | −93% |

**one-shot**

| Input | Compiler | New class, µs | `strtolower()` + `str_contains()` loop, µs | `stripos()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| all texts of the scenario | GCC | 119 | **26** | 31.8 | 96 | ≈526 | +359% |
| all texts of the scenario | Clang | 112 | **27.6** | 30.6 | 101 | ≈549 | +304% |

### Auto-linking, all pages, 3,345 names: every name with its offset

**prepared**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE alternation in chunks of 1024, µs | PCRE alternation in chunks of 512, µs | PCRE, shared prefixes, µs | PCRE, shared prefixes in chunks of 1024, µs | PCRE, shared prefixes in chunks of 512, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| all texts of the scenario | GCC | 2.07 | ≈761 | too large | ≈860 | ≈640 | **27.1** | 49.1 | 82.2 | −93% |
| all texts of the scenario | Clang | 2.28 | ≈738 | too large | ≈863 | ≈640 | **27.9** | 49.8 | 81.6 | −92% |

**one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE alternation in chunks of 1024, µs | PCRE alternation in chunks of 512, µs | PCRE, shared prefixes, µs | PCRE, shared prefixes in chunks of 1024, µs | PCRE, shared prefixes in chunks of 512, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| all texts of the scenario | GCC | 1,642 | **622** | too large | 1,848 | 1,401 | ≈7,483 | ≈8,669 | ≈9,104 | +164% |
| all texts of the scenario | Clang | 1,618 | **602** | too large | 1,828 | 1,371 | ≈7,961 | ≈9,082 | ≈9,565 | +169% |

### Auto-linking, all pages, 3,345 names: link them

**prepared**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| all texts of the scenario | GCC | 2.99 | **363** | too large | too large | −99% |
| all texts of the scenario | Clang | 3.07 | **373** | too large | too large | −99% |

**one-shot**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| all texts of the scenario | GCC | 3,169 | **345** | too large | too large | +851% |
| all texts of the scenario | Clang | 3,133 | **361** | too large | too large | +796% |

## Edge cases

### `matches()`

**prepared**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | `str_contains()`, µs | `str_contains()` loop, second copy, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| few keys, 1 keys, 4 KiB | GCC | 2.79 | 0.22 | 0.21 | 0.23 | **0.15** | 0.15 | +1707% |
| few keys, 1 keys, 4 KiB | Clang | 3.25 | 0.17 | 0.18 | 0.17 | 0.15 | **0.15** | +2071% |
| few keys, 4 keys, 4 KiB | GCC | 2.79 | 1.94 | — | 1.94 | **0.95** | 0.96 | +196% |
| few keys, 4 keys, 4 KiB | Clang | 3.28 | 1.87 | — | 1.87 | **0.95** | 0.95 | +245% |

**one-shot**

| Input | Compiler | New class, µs | `str_contains()` loop, µs | `str_contains()`, µs | `str_contains()` loop, second copy, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| few keys, 1 keys, 4 KiB | GCC | 3.26 | 0.23 | **0.22** | 0.24 | 0.56 | ≈1.82 | +1368% |
| few keys, 1 keys, 4 KiB | Clang | 3.67 | 0.23 | **0.23** | 0.25 | 0.57 | ≈1.9 | +1508%† |
| few keys, 4 keys, 4 KiB | GCC | 4.09 | 2.01 | — | 2.03 | **1.54** | ≈8.42 | +167% |
| few keys, 4 keys, 4 KiB | Clang | 4.55 | 1.95 | — | 1.96 | **1.52** | ≈8.97 | +199% |

### `getMatchedKeywords()`

**prepared**

| Input | Compiler | New class, µs | `str_contains()`, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| dense matches, 4 KiB | GCC | 7.86 | — | **88.8** | 188 | 92.2 | −91% |
| dense matches, 4 KiB | Clang | 8.79 | — | **88.1** | 193 | 90 | −90% |
| dense matches, 64 KiB | GCC | 110 | — | **775** | 2,964 | 1,420 | −86% |
| dense matches, 64 KiB | Clang | 126 | — | **773** | 3,047 | 1,379 | −84% |
| few keys, 1 keys, 4 KiB | GCC | 2.78 | **0.17** | 0.19 | 1.16 | 1.16 | +1508%† |
| few keys, 1 keys, 4 KiB | Clang | 3.27 | **0.17** | 0.19 | ≈1.18 | ≈1.18 | +1785%† |
| few keys, 4 keys, 4 KiB | GCC | 5.56 | — | **2.54** | 5.42 | 5.48 | +119% |
| few keys, 4 keys, 4 KiB | Clang | 6.58 | — | **2.46** | 5.25 | 5.67 | +167% |

**one-shot**

| Input | Compiler | New class, µs | `str_contains()`, µs | `str_contains()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| dense matches, 4 KiB | GCC | 33.8 | — | **89.2** | 194 | 211 | −62% |
| dense matches, 4 KiB | Clang | 36.2 | — | **88.2** | 199 | 212 | −59% |
| dense matches, 64 KiB | GCC | 138 | — | **777** | 2,972 | 1,552 | −82% |
| dense matches, 64 KiB | Clang | 155 | — | **772** | 3,077 | 1,517 | −80% |
| few keys, 1 keys, 4 KiB | GCC | 3.27 | **0.24** | 0.26 | ≈1.66 | ≈2.95 | +1283% |
| few keys, 1 keys, 4 KiB | Clang | 3.72 | **0.24** | 0.27 | ≈1.65 | ≈2.95 | +1474% |
| few keys, 4 keys, 4 KiB | GCC | 6.88 | — | **2.63** | 6.04 | 13.2 | +162% |
| few keys, 4 keys, 4 KiB | Clang | 7.86 | — | **2.56** | 5.88 | ≈13.8 | +207% |

### `countMatches()`

**prepared**

| Input | Compiler | New class, µs | `strpos()` loop, µs | `substr_count()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| dense matches, 4 KiB | GCC | 6.88 | 104 | 102 | 181 | **85.8** | −92% |
| dense matches, 4 KiB | Clang | 7.73 | 103 | 101 | 179 | **82.4** | −91% |
| dense matches, 64 KiB | GCC | 106 | 1,729 | 1,697 | 2,887 | **1,353** | −92% |
| dense matches, 64 KiB | Clang | 119 | 1,726 | 1,688 | 2,847 | **1,290** | −91% |
| few keys, 1 keys, 4 KiB | GCC | 5.39 | **0.52** | 0.52 | 0.94 | 0.94 | +938% |
| few keys, 1 keys, 4 KiB | Clang | 6.39 | **0.53** | 0.53 | 0.92 | 0.92 | +1108% |
| few keys, 4 keys, 4 KiB | GCC | 5.54 | **2.96** | 2.97 | 4.91 | 4.85 | +87% |
| few keys, 4 keys, 4 KiB | Clang | 6.58 | 2.88 | **2.87** | 4.88 | 4.81 | +130% |

**one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | `substr_count()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| dense matches, 4 KiB | GCC | 32.8 | 104 | **102** | 188 | 205 | −68% |
| dense matches, 4 KiB | Clang | 35.1 | 104 | **102** | 186 | 204 | −66% |
| dense matches, 64 KiB | GCC | 133 | 1,732 | 1,699 | 2,917 | **1,481** | −91% |
| dense matches, 64 KiB | Clang | 149 | 1,731 | 1,692 | 2,877 | **1,423** | −90% |
| few keys, 1 keys, 4 KiB | GCC | 5.89 | **0.61** | 0.61 | 1.37 | 2.61 | +868% |
| few keys, 1 keys, 4 KiB | Clang | 6.83 | **0.61** | 0.62 | 1.36 | 2.61 | +1012% |
| few keys, 4 keys, 4 KiB | GCC | 6.87 | 3.06 | **3.05** | 5.53 | 12.5 | +125% |
| few keys, 4 keys, 4 KiB | Clang | 7.89 | 2.98 | **2.97** | 5.51 | 12.9 | +166% |

### `matchAll()`

**prepared**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| dense matches, 4 KiB | GCC | 10.4 | 105 | 187 | **91.9** | −89% |
| dense matches, 4 KiB | Clang | 11.7 | 105 | 192 | **89.2** | −87% |
| dense matches, 64 KiB | GCC | 167 | 1,772 | 2,997 | **1,475** | −89% |
| dense matches, 64 KiB | Clang | 190 | 1,770 | 3,089 | **1,442** | −87% |

**one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| dense matches, 4 KiB | GCC | 36.3 | **106** | 193 | 213 | −66% |
| dense matches, 4 KiB | Clang | 39.3 | **105** | 199 | 213 | −63% |
| dense matches, 64 KiB | GCC | 197 | 1,774 | 3,015 | **1,607** | −88% |
| dense matches, 64 KiB | Clang | 221 | 1,773 | 3,101 | **1,572** | −86% |

### `replace()`

**prepared**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | `preg_replace()`, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| dense matches, 4 KiB | GCC | 8.71 | 197 | 125 | **55.5** | — | −84% |
| dense matches, 4 KiB | Clang | 9.57 | 198 | 116 | **57.7** | — | −83% |
| dense matches, 64 KiB | GCC | 169 | 3,094 | 1,985 | **868** | — | −81% |
| dense matches, 64 KiB | Clang | 192 | 3,127 | 1,851 | **911** | — | −79% |
| few keys, 1 keys, 4 KiB | GCC | 5.53 | 0.55 | 0.46 | 0.46 | **0.34** | +1506% |
| few keys, 1 keys, 4 KiB | Clang | 6.19 | 0.55 | 0.46 | 0.46 | **0.34** | +1718% |
| few keys, 4 keys, 4 KiB | GCC | 5.62 | ≈15.8 | **2.05** | 2.06 | — | +173% |
| few keys, 4 keys, 4 KiB | Clang | 6.33 | ≈15.8 | **2.04** | 2.05 | — | +210% |

**one-shot**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | `preg_replace()`, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|
| dense matches, 4 KiB | GCC | 31.7 | 197 | **131** | 171 | — | −76% |
| dense matches, 4 KiB | Clang | 33.5 | 199 | **121** | 177 | — | −72% |
| dense matches, 64 KiB | GCC | 195 | 3,093 | 1,992 | **988** | — | −80% |
| dense matches, 64 KiB | Clang | 219 | 3,120 | 1,853 | **1,033** | — | −79% |
| few keys, 1 keys, 4 KiB | GCC | 6.01 | **0.63** | 0.95 | 2.24 | 2.03 | +847% |
| few keys, 1 keys, 4 KiB | Clang | 6.61 | **0.63** | 0.91 | 2.24 | 2.02 | +948% |
| few keys, 4 keys, 4 KiB | GCC | 6.91 | ≈16.1 | **2.79** | 9.89 | — | +148% |
| few keys, 4 keys, 4 KiB | Clang | 7.64 | ≈16 | **2.75** | 10.3 | — | +178% |

## Manual pages by length

### `matchAll()`

**128 PHP names, prepared**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 128 PHP names, pages of 1–2 KiB | GCC | 2.16 | 40.6 | 41 | **12.7** | −83% |
| 128 PHP names, pages of 1–2 KiB | Clang | 2.5 | 38.7 | 38.9 | **12.8** | −80% |
| 128 PHP names, pages of 2–4 KiB | GCC | 4.03 | 74.6 | 75.4 | **22.9** | −82% |
| 128 PHP names, pages of 2–4 KiB | Clang | 4.76 | 70.7 | 71.4 | **23.3** | −80% |
| 128 PHP names, pages of 4–16 KiB | GCC | 9.57 | 175 | 173 | **51** | −81% |
| 128 PHP names, pages of 4–16 KiB | Clang | 11.4 | 165 | 164 | **51.9** | −78% |

**128 PHP names, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 128 PHP names, pages of 1–2 KiB | GCC | 41.6 | **41.4** | 49.2 | ≈331 | +0.5% |
| 128 PHP names, pages of 1–2 KiB | Clang | 42.8 | **39.3** | 45.5 | ≈347 | +8.9% |
| 128 PHP names, pages of 2–4 KiB | GCC | 44.3 | **75.8** | 83.5 | 341 | −42% |
| 128 PHP names, pages of 2–4 KiB | Clang | 44.6 | **71.7** | 78.2 | 360 | −38%† |
| 128 PHP names, pages of 4–16 KiB | GCC | 49.5 | **176** | 182 | 371 | −72% |
| 128 PHP names, pages of 4–16 KiB | Clang | 51.2 | **166** | 172 | 387 | −69% |

**512 PHP names, prepared**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 512 PHP names, pages of 1–2 KiB | GCC | 2.28 | ≈163 | ≈372 | **18.1** | −87% |
| 512 PHP names, pages of 1–2 KiB | Clang | 2.6 | ≈154 | ≈343 | **18.6** | −86% |
| 512 PHP names, pages of 2–4 KiB | GCC | 4.2 | ≈281 | ≈557 | **32.5** | −87% |
| 512 PHP names, pages of 2–4 KiB | Clang | 4.91 | ≈267 | ≈508 | **33.5** | −85% |
| 512 PHP names, pages of 4–16 KiB | GCC | 9.88 | ≈686 | ≈2,440 | **72** | −86% |
| 512 PHP names, pages of 4–16 KiB | Clang | 11.7 | ≈648 | ≈2,386 | **74.6** | −84% |

**512 PHP names, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 512 PHP names, pages of 1–2 KiB | GCC | 223 | **161** | 354 | ≈1,229 | +38% |
| 512 PHP names, pages of 1–2 KiB | Clang | 210 | **154** | 326 | ≈1,302 | +37% |
| 512 PHP names, pages of 2–4 KiB | GCC | 227 | **297** | 628 | 1,337 | −24% |
| 512 PHP names, pages of 2–4 KiB | Clang | 214 | **282** | 580 | 1,401 | −25% |
| 512 PHP names, pages of 4–16 KiB | GCC | 232 | **678** | 1,331 | 1,382 | −66%† |
| 512 PHP names, pages of 4–16 KiB | Clang | 221 | **663** | 1,401 | 1,435 | −67%† |

**3345 PHP names, prepared**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE alternation in chunks of 1024, µs | PCRE alternation in chunks of 512, µs | PCRE, shared prefixes, µs | PCRE, shared prefixes in chunks of 1024, µs | PCRE, shared prefixes in chunks of 512, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3345 PHP names, pages of 1–2 KiB | GCC | 2.87 | ≈1,050 | too large | ≈3,220 | ≈2,450 | **39.2** | 71.2 | 120 | −93% |
| 3345 PHP names, pages of 1–2 KiB | Clang | 3.19 | ≈998 | too large | ≈3,230 | ≈2,435 | **39.9** | 71.3 | 117 | −92% |
| 3345 PHP names, pages of 2–4 KiB | GCC | 5.11 | ≈2,254 | too large | ≈4,652 | ≈3,374 | **68.4** | 126 | 213 | −93% |
| 3345 PHP names, pages of 2–4 KiB | Clang | 5.78 | ≈2,122 | too large | ≈4,594 | ≈3,386 | **69.9** | 126 | 208 | −92% |
| 3345 PHP names, pages of 4–16 KiB | GCC | 11.3 | ≈7,969 | too large | ≈18,491 | ≈13,568 | **147** | 275 | 465 | −92% |
| 3345 PHP names, pages of 4–16 KiB | Clang | 13 | ≈7,500 | too large | ≈18,689 | ≈13,460 | **150** | 274 | 453 | −91% |

**3345 PHP names, one-shot**

| Input | Compiler | New class, µs | `strpos()` loop, µs | PCRE alternation, µs | PCRE alternation in chunks of 1024, µs | PCRE alternation in chunks of 512, µs | PCRE, shared prefixes, µs | PCRE, shared prefixes in chunks of 1024, µs | PCRE, shared prefixes in chunks of 512, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3345 PHP names, pages of 1–2 KiB | GCC | 1,646 | **1,025** | too large | 2,671 | 1,997 | ≈7,528 | ≈8,813 | ≈9,332 | +60% |
| 3345 PHP names, pages of 1–2 KiB | Clang | 1,626 | **971** | too large | 2,631 | 1,969 | ≈8,010 | ≈9,286 | ≈9,736 | +67% |
| 3345 PHP names, pages of 2–4 KiB | GCC | 1,648 | **1,902** | too large | 4,726 | 3,500 | 8,114 | 8,977 | 9,582 | −13% |
| 3345 PHP names, pages of 2–4 KiB | Clang | 1,629 | **1,794** | too large | 4,700 | 3,433 | 8,442 | 9,340 | 9,934 | −9.5% |
| 3345 PHP names, pages of 4–16 KiB | GCC | 1,652 | **4,310** | too large | 9,844 | 7,260 | 8,174 | 9,086 | 9,800 | −62% |
| 3345 PHP names, pages of 4–16 KiB | Clang | 1,629 | **4,060** | too large | 9,740 | 7,153 | 8,533 | 9,492 | 10,179 | −60% |

### `replace()`

**128 PHP names, prepared**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 128 PHP names, pages of 1–2 KiB | GCC | 2.4 | ≈253 | 40.5 | **11.5** | −79% |
| 128 PHP names, pages of 1–2 KiB | Clang | 2.62 | ≈256 | 39.7 | **11.6** | −77% |
| 128 PHP names, pages of 2–4 KiB | GCC | 4.48 | ≈387 | 74.8 | **21.1** | −79% |
| 128 PHP names, pages of 2–4 KiB | Clang | 4.99 | ≈392 | 72.9 | **21.4** | −77% |
| 128 PHP names, pages of 4–16 KiB | GCC | 10.6 | ≈950 | 173 | **47.2** | −78% |
| 128 PHP names, pages of 4–16 KiB | Clang | 11.9 | ≈960 | 168 | **48** | −75% |

**128 PHP names, one-shot**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 128 PHP names, pages of 1–2 KiB | GCC | 52.2 | ≈257 | **48.9** | ≈328 | +5.5%† |
| 128 PHP names, pages of 1–2 KiB | Clang | 52.8 | ≈260 | **46.1** | ≈347 | +14% |
| 128 PHP names, pages of 2–4 KiB | GCC | 53.9 | 415 | **82.7** | 340 | −35% |
| 128 PHP names, pages of 2–4 KiB | Clang | 53.7 | 421 | **79.4** | 358 | −32% |
| 128 PHP names, pages of 4–16 KiB | GCC | 59.4 | ≈959 | **181** | 371 | −67% |
| 128 PHP names, pages of 4–16 KiB | Clang | 60.8 | ≈973 | **175** | 383 | −65% |

**512 PHP names, prepared**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 512 PHP names, pages of 1–2 KiB | GCC | 3.01 | ≈474 | ≈298 | **13.8** | −78% |
| 512 PHP names, pages of 1–2 KiB | Clang | 3.22 | ≈490 | ≈300 | **14** | −77% |
| 512 PHP names, pages of 2–4 KiB | GCC | 5.53 | ≈752 | ≈469 | **25.1** | −78% |
| 512 PHP names, pages of 2–4 KiB | Clang | 6.02 | ≈779 | ≈466 | **25.5** | −76% |
| 512 PHP names, pages of 4–16 KiB | GCC | 12.6 | ≈3,311 | ≈2,169 | **55.6** | −77% |
| 512 PHP names, pages of 4–16 KiB | Clang | 13.9 | ≈3,419 | ≈2,131 | **56.6** | −75% |

**512 PHP names, one-shot**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 512 PHP names, pages of 1–2 KiB | GCC | 343 | 423 | **323** | 1,315 | +6.2% |
| 512 PHP names, pages of 1–2 KiB | Clang | 333 | 432 | **312** | 1,367 | +6.6% |
| 512 PHP names, pages of 2–4 KiB | GCC | 346 | 796 | **564** | 1,331 | −39% |
| 512 PHP names, pages of 2–4 KiB | Clang | 336 | 818 | **545** | 1,378 | −38% |
| 512 PHP names, pages of 4–16 KiB | GCC | 353 | 1,731 | **1,204** | 1,350 | −71%† |
| 512 PHP names, pages of 4–16 KiB | Clang | 346 | 1,778 | **1,162** | 1,403 | −70% |

**3345 PHP names, prepared**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 3345 PHP names, pages of 1–2 KiB | GCC | 4.21 | **534** | too large | too large | −99% |
| 3345 PHP names, pages of 1–2 KiB | Clang | 4.39 | **558** | too large | too large | −99% |
| 3345 PHP names, pages of 2–4 KiB | GCC | 7.55 | **997** | too large | too large | −99% |
| 3345 PHP names, pages of 2–4 KiB | Clang | 7.96 | **1,045** | too large | too large | −99% |
| 3345 PHP names, pages of 4–16 KiB | GCC | 16.4 | **2,313** | too large | too large | −99% |
| 3345 PHP names, pages of 4–16 KiB | Clang | 18.1 | **2,413** | too large | too large | −99% |

**3345 PHP names, one-shot**

| Input | Compiler | New class, µs | `strtr()`, µs | PCRE, longest first, µs | PCRE, shared prefixes, µs | Change against the fastest |
|---|---|---:|---:|---:|---:|---:|
| 3345 PHP names, pages of 1–2 KiB | GCC | 3,198 | **531** | too large | too large | +502% |
| 3345 PHP names, pages of 1–2 KiB | Clang | 3,151 | **558** | too large | too large | +465% |
| 3345 PHP names, pages of 2–4 KiB | GCC | 3,194 | **994** | too large | too large | +222% |
| 3345 PHP names, pages of 2–4 KiB | Clang | 3,159 | **1,064** | too large | too large | +197% |
| 3345 PHP names, pages of 4–16 KiB | GCC | 3,194 | **2,273** | too large | too large | +40% |
| 3345 PHP names, pages of 4–16 KiB | Clang | 3,149 | **2,394** | too large | too large | +32% |
