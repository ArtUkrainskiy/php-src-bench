# Moderation: find any configured substring

Times are microseconds per complete job; lower is better. Bold marks the lowest median per compiler, not a significance test. GCC 15.2 and Clang 21.1 on the same AMD system. PCRE compilation caches are warm in these tables; first requests are [separate](PCRE-FIRST.md). Exact input dictionaries and expected outputs are saved in the [corpus](../../corpus/multi-pattern-scaling/README.md).

A dagger marks a sample span above 10%. [Order and noise controls](CONFIRMATION.md) retain original and repeat measurements, including close comparisons.

`Loop` is early-exit `str_contains()`. `PCRE` is a single escaped `preg_match()` alternation. Matcher returns the same boolean. English texts are fixed across every N.

## Short comments, no match

### Dictionary preparation included

| Substrings | GCC loop | GCC PCRE | GCC Matcher | Clang loop | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | **0.280** | 0.713 | 2.377 | **0.288** | 0.680 | 2.381 |
| 16 | **0.439** | 1.246 | 5.203 | **0.459** | 1.262 | 5.000 |
| 32 | **0.784** | 2.524 | 12.839 | **0.866** | 2.561 | 12.537 |
| 64 | **1.486** | 4.893 | 26.274 | **1.567** | 5.033 | 25.620 |
| 128 | **3.066** | 9.877 | 58.269 | **3.282** | 10.033 | 56.921 |
| 256 | **6.946** | 19.905 | 152.716 | **7.770** | 20.214 | 149.700 |
| 512 | **16.053** | 49.053 | 295.062 | **17.434** | 50.212 | 293.707 |

### Dictionary already prepared

| Substrings | GCC loop | GCC PCRE | GCC Matcher | Clang loop | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 0.287 | 0.239 | **0.188** | 0.291 | 0.220 | **0.170** |
| 16 | 0.438 | 0.349 | **0.189** | 0.460 | 0.325 | **0.174** |
| 32 | 0.758 | 0.754 | **0.235** | 0.842 | 0.724 | **0.244** |
| 64 | 1.433 | 1.485 | **0.237** | 1.597 | 1.518 | **0.245** |
| 128 | 2.951 | 2.983 | **0.244** | 3.353 | 2.850 | **0.251** |
| 256 | 6.888 | 6.061 | **0.251** | 7.943 | 5.980 | **0.256** |
| 512 | 16.192 | 19.433 | **0.257** | 17.177 | 21.827 | **0.264** |

## Short comments, match at the start

### Dictionary preparation included

| Substrings | GCC loop | GCC PCRE | GCC Matcher | Clang loop | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | **0.202** | 0.651 | 2.450 | **0.203** | 0.600 | 2.318 |
| 16 | **0.282** | 1.040 | 5.086 | **0.286** | 1.067 | 4.919 |
| 32 | **0.473** | 1.932 | 12.552 | **0.499** | 2.016 | 12.111 |
| 64 | **0.870** | 3.615 | 26.089 | **0.930** | 3.710 | 25.486 |
| 128 | **1.658** | 7.049 | 58.473 | **1.745** | 7.449 | 56.575 |
| 256 | **3.529** | 14.176 | 152.237 | **3.872** | 14.319 | 150.366 |
| 512 | **8.704** | 27.670 | 295.204 | **9.531** | 29.281 | 292.175 |

### Dictionary already prepared

| Substrings | GCC loop | GCC PCRE | GCC Matcher | Clang loop | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 0.205 | 0.161 | **0.128** | 0.203 | 0.144 | **0.111** |
| 16 | 0.281 | 0.165 | **0.127** | 0.286 | 0.153 | **0.113** |
| 32 | 0.474 | 0.179 | **0.126** | 0.493 | 0.166 | **0.113** |
| 64 | 0.874 | 0.213 | **0.128** | 0.920 | 0.198 | **0.110** |
| 128 | 1.646 | 0.269 | **0.127** | 1.799 | 0.242 | **0.113** |
| 256 | 3.474 | 0.391 | **0.128** | 4.033 | 0.368 | **0.112** |
| 512 | 8.705 | 0.649 | **0.127** | 9.498 | 0.642 | **0.113** |

## Short comments, match in the body

### Dictionary preparation included

| Substrings | GCC loop | GCC PCRE | GCC Matcher | Clang loop | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | **0.236** | 0.770 | 2.421 | **0.237** | 0.708 | 2.439 |
| 16 | **0.333** | 1.303 | 5.270 | **0.336** | 1.297 | 5.082 |
| 32 | **0.573** | 2.702 | 12.769 | **0.609** | 2.743 | 12.233 |
| 64 | **1.091** | 5.325 | 26.319 | **1.159** | 5.357 | 25.738 |
| 128 | **2.122** | 10.412 | 57.947 | **2.220** | 10.603 | 56.228 |
| 256 | **4.640** | 20.822 | 153.093 | **5.285** | 22.804 | 150.085 |
| 512 | **11.574** | 53.368 | 294.838 | **12.667** | 54.969 | 293.464 |

### Dictionary already prepared

| Substrings | GCC loop | GCC PCRE | GCC Matcher | Clang loop | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 0.237 | 0.278 | **0.212** | 0.238 | 0.254 | **0.190** |
| 16 | 0.336 | 0.422 | **0.217** | 0.343 | 0.392 | **0.196** |
| 32 | 0.574 | 0.952 | **0.271** | 0.601 | 0.919 | **0.283** |
| 64 | 1.106 | 1.859 | **0.275** | 1.159 | 1.895 | **0.284** |
| 128 | 2.133 | 3.655 | **0.282** | 2.274 | 3.482 | **0.294** |
| 256 | 4.525 | 7.233 | **0.290** | 4.979 | 7.063 | **0.301** |
| 512 | 11.623 | 22.569 | **0.299** | 12.464 | 22.768 | **0.307** |

## Short comments, match near the end

### Dictionary preparation included

| Substrings | GCC loop | GCC PCRE | GCC Matcher | Clang loop | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | **0.218** | 0.757 | 2.429 | **0.212** | 0.728 | 2.452 |
| 16 | **0.297** | 1.322 | 5.449 | **0.303** | 1.350 | 5.105 |
| 32 | **0.487** | 2.782 | 12.786 | **0.503** | 2.742 | 12.380 |
| 64 | **0.917** | 5.355 | 26.166 | **0.970** | 5.604 | 25.910 |
| 128 | **1.684** | 10.815 | 58.869 | **1.837** | 10.888 | 57.177 |
| 256 | **3.810** | 21.693 | 152.779 | **3.998** | 21.798 | 150.059 |
| 512 | **8.667** | 53.440 | 294.903 | **9.538** | 57.627 | 293.552 |

### Dictionary already prepared

| Substrings | GCC loop | GCC PCRE | GCC Matcher | Clang loop | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | **0.218** | 0.275 | 0.221 | 0.215 | 0.254 | **0.200** |
| 16 | 0.295 | 0.447 | **0.228** | 0.297 | 0.407 | **0.209** |
| 32 | 0.484 | 0.993 | **0.283** | 0.515 | 0.964 | **0.301** |
| 64 | 0.907 | 1.982 | **0.286** | 0.975 | 2.045 | **0.300** |
| 128 | 1.673 | 3.959 | **0.294** | 1.931 | 3.811 | **0.307** |
| 256 | 3.545 | 7.873 | **0.300** | 3.867 | 7.677 | **0.315** |
| 512 | 8.940 | 26.872 | **0.311** | 9.524 | 24.276 | **0.325** |

## Detailed support messages, no match

### Dictionary preparation included

| Substrings | GCC loop | GCC PCRE | GCC Matcher | Clang loop | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | **0.932** | 1.548 | 3.015 | **0.942** | 1.461 | 2.940 |
| 16 | **1.606** | 3.497 | 5.773 | **1.621** | 3.426 | 5.618 |
| 32 | **3.521** | 8.338 | 13.839 | **3.670** | 8.269 | 13.643 |
| 64 | **6.877** | 17.049 | 27.300 | **7.013** | 17.544 | 26.918 |
| 128 | **13.477** | 34.901 | 59.757 | **14.183** | 33.657 | 58.871 |
| 256 | **30.087** | 68.546 | 154.924 | **30.896** | 73.149 | 153.226 |
| 512 | **68.197** | 233.702 | 295.950 | **71.708** | 233.298 | 303.130 |

### Dictionary already prepared

| Substrings | GCC loop | GCC PCRE | GCC Matcher | Clang loop | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 0.935 | 1.066 | **0.811** | 0.959 | 1.010 | **0.757** |
| 16 | 1.578 | 2.583 | **0.771** | 1.639 | 2.515 | **0.773** |
| 32 | 3.520 | 6.558 | **1.361** | 3.664 | 6.430 | **1.546** |
| 64 | 6.871 | 13.545 | **1.373** | 7.001 | 14.052 | **1.557** |
| 128 | 13.367 | 27.840 | **1.391** | 13.583 | 26.589 | **1.585** |
| 256 | 29.885 | 54.955 | **1.424** | 30.776 | 54.112 | **1.610** |
| 512 | 67.916 | 186.281 | **1.487** | 70.178 | 201.871 | **1.653** |

## Detailed support messages, quoted matching term

### Dictionary preparation included

| Substrings | GCC loop | GCC PCRE | GCC Matcher | Clang loop | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | **0.384** | 0.978 | 2.579 | **0.384** | 0.924 | 2.551 |
| 16 | **0.568** | 1.799 | 5.334 | **0.559** | 1.740 | 5.235 |
| 32 | **1.309** | 4.247 | 13.073 | **1.320** | 4.179 | 12.584 |
| 64 | **2.835** | 8.543 | 26.526 | **2.857** | 8.753 | 26.002 |
| 128 | **5.446** | 17.142 | 58.466 | **5.531** | 16.846 | 57.254 |
| 256 | **11.470** | 34.020 | 153.393 | **11.650** | 34.202 | 150.268 |
| 512 | **25.208** | 105.639 | 295.349 | **25.623** | 111.171 | 292.653 |

### Dictionary already prepared

| Substrings | GCC loop | GCC PCRE | GCC Matcher | Clang loop | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 0.390 | 0.497 | **0.374** | 0.385 | 0.460 | **0.333** |
| 16 | 0.563 | 0.852 | **0.367** | 0.563 | 0.805 | **0.355** |
| 32 | 1.307 | 2.423 | **0.576** | 1.347 | 2.358 | **0.629** |
| 64 | 2.826 | 5.063 | **0.576** | 2.849 | 5.235 | **0.631** |
| 128 | 5.445 | 10.324 | **0.576** | 5.511 | 9.839 | **0.629** |
| 256 | 11.504 | 20.409 | **0.586** | 11.569 | 19.953 | **0.634** |
| 512 | 25.043 | 74.502 | **0.592** | 26.503 | 66.308 | **0.638** |

## Input sizes and results

String bytes are UTF-8 lengths; total string bytes sum the dictionary literals, not engine memory.

| Substrings | Input | Bytes per substring | Total literal bytes | Bytes per document | Literal occurrences |
|---:|---|---:|---:|---:|---:|
| 8 | Check a short comment (No match) | 4–8 | 39 | 56–84 | 0 |
| 8 | Check a short comment (Match at start) | 4–8 | 39 | 89–121 | 1–2 |
| 8 | Check a short comment (Match in body) | 4–8 | 39 | 152–196 | 1–2 |
| 8 | Check a short comment (Match near end) | 4–8 | 39 | 93–125 | 1–2 |
| 8 | Check a detailed support message (No match) | 4–8 | 39 | 749–817 | 0 |
| 8 | Check a detailed support message (Quoted matching term) | 4–8 | 39 | 777–845 | 1 |
| 16 | Check a short comment (No match) | 4–13 | 109 | 56–84 | 0 |
| 16 | Check a short comment (Match at start) | 4–13 | 109 | 89–121 | 1–2 |
| 16 | Check a short comment (Match in body) | 4–13 | 109 | 152–196 | 1–2 |
| 16 | Check a short comment (Match near end) | 4–13 | 109 | 93–125 | 1–2 |
| 16 | Check a detailed support message (No match) | 4–13 | 109 | 749–817 | 0 |
| 16 | Check a detailed support message (Quoted matching term) | 4–13 | 109 | 777–845 | 1 |
| 32 | Check a short comment (No match) | 4–23 | 299 | 56–84 | 0 |
| 32 | Check a short comment (Match at start) | 4–23 | 299 | 89–121 | 1–2 |
| 32 | Check a short comment (Match in body) | 4–23 | 299 | 152–196 | 1–2 |
| 32 | Check a short comment (Match near end) | 4–23 | 299 | 93–125 | 1–2 |
| 32 | Check a detailed support message (No match) | 4–23 | 299 | 749–817 | 0 |
| 32 | Check a detailed support message (Quoted matching term) | 4–23 | 299 | 777–845 | 1 |
| 64 | Check a short comment (No match) | 3–23 | 605 | 56–84 | 0 |
| 64 | Check a short comment (Match at start) | 3–23 | 605 | 89–121 | 1–2 |
| 64 | Check a short comment (Match in body) | 3–23 | 605 | 152–196 | 1–2 |
| 64 | Check a short comment (Match near end) | 3–23 | 605 | 93–125 | 1–2 |
| 64 | Check a detailed support message (No match) | 3–23 | 605 | 749–817 | 0 |
| 64 | Check a detailed support message (Quoted matching term) | 3–23 | 605 | 777–845 | 1 |
| 128 | Check a short comment (No match) | 3–30 | 1250 | 56–84 | 0 |
| 128 | Check a short comment (Match at start) | 3–30 | 1250 | 89–121 | 1–2 |
| 128 | Check a short comment (Match in body) | 3–30 | 1250 | 152–196 | 1–2 |
| 128 | Check a short comment (Match near end) | 3–30 | 1250 | 93–125 | 1–2 |
| 128 | Check a detailed support message (No match) | 3–30 | 1250 | 749–817 | 0 |
| 128 | Check a detailed support message (Quoted matching term) | 3–30 | 1250 | 777–845 | 1 |
| 256 | Check a short comment (No match) | 3–30 | 2452 | 56–84 | 0 |
| 256 | Check a short comment (Match at start) | 3–30 | 2452 | 89–121 | 1–2 |
| 256 | Check a short comment (Match in body) | 3–30 | 2452 | 152–196 | 1–2 |
| 256 | Check a short comment (Match near end) | 3–30 | 2452 | 93–125 | 1–2 |
| 256 | Check a detailed support message (No match) | 3–30 | 2452 | 749–817 | 0 |
| 256 | Check a detailed support message (Quoted matching term) | 3–30 | 2452 | 777–845 | 1 |
| 512 | Check a short comment (No match) | 3–30 | 4839 | 56–84 | 0 |
| 512 | Check a short comment (Match at start) | 3–30 | 4839 | 89–121 | 1–2 |
| 512 | Check a short comment (Match in body) | 3–30 | 4839 | 152–196 | 1–2 |
| 512 | Check a short comment (Match near end) | 3–30 | 4839 | 93–125 | 1–2 |
| 512 | Check a detailed support message (No match) | 3–30 | 4839 | 749–817 | 0 |
| 512 | Check a detailed support message (Quoted matching term) | 3–30 | 4839 | 777–845 | 1 |
