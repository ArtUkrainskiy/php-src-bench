# Moderation: find any configured substring

Times are microseconds per complete job; lower is better. Bold marks the lowest median per compiler, not a significance test. GCC 15.2 and Clang 21.1 on the same AMD system. PCRE compilation caches are warm in these tables; first requests are [separate](PCRE-FIRST.md). Exact input dictionaries and expected outputs are saved in the [corpus](../../corpus/multi-pattern-scaling/README.md).

A dagger marks the one noisy original PCRE cell; its [complete-case confirmation](CONFIRMATION.md) preserves the original and repeat measurements.

`Loop` is early-exit `str_contains()`. `PCRE` is a single escaped `preg_match()` alternation. Matcher returns the same boolean. English texts are fixed across every N.

## Short comments, no match

### Dictionary preparation included

| Substrings | GCC loop | GCC PCRE | GCC Matcher | Clang loop | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | **0.281** | 0.710 | 1.398 | **0.291** | 0.683 | 1.353 |
| 16 | **0.434** | 1.237 | 3.615 | **0.455** | 1.233 | 3.462 |
| 32 | **0.786** | 2.558 | 10.546 | **0.829** | 2.553 | 9.892 |
| 64 | **1.457** | 4.891 | 21.533 | **1.557** | 4.986 | 20.686 |
| 128 | **2.870** | 9.920 | 47.788 | **3.238** | 10.031 | 44.924 |
| 256 | **6.749** | 19.853 | 90.183 | **7.679** | 20.075 | 86.337 |
| 512 | **16.077** | 48.315 | 165.833 | **17.685** | 50.060 | 158.689 |

### Dictionary already prepared

| Substrings | GCC loop | GCC PCRE | GCC Matcher | Clang loop | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 0.282 | **0.236** | 0.266 | 0.288 | **0.220** | 0.274 |
| 16 | 0.444 | 0.347 | **0.266** | 0.463 | 0.324 | **0.273** |
| 32 | 0.780 | 0.754 | **0.267** | 0.857 | 0.722 | **0.273** |
| 64 | 1.406 | 1.482 | **0.271** | 1.653 | 1.519 | **0.278** |
| 128 | 2.920 | 2.975 | **0.276** | 3.450 | 2.854 | **0.285** |
| 256 | 6.760 | 6.079 | **0.294** | 7.934 | 5.979 | **0.304** |
| 512 | 16.203 | 20.267 | **0.313** | 17.747 | 20.411 | **0.324** |

## Short comments, match at the start

### Dictionary preparation included

| Substrings | GCC loop | GCC PCRE | GCC Matcher | Clang loop | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | **0.206** | 0.633 | 1.244 | **0.203** | 0.605 | 1.198 |
| 16 | **0.276** | 1.031 | 3.483 | **0.280** | 1.070 | 3.239 |
| 32 | **0.479** | 1.954 | 10.409 | **0.497** | 1.951 | 9.712 |
| 64 | **0.868** | 3.631 | 21.360 | **0.937** | 3.650 | 20.284 |
| 128 | **1.665** | 6.902 | 47.438 | **1.753** | 7.249 | 44.355 |
| 256 | **3.482** | 14.180 | 90.119 | **3.948** | 14.557 | 86.289 |
| 512 | **8.656** | 27.972 | 165.010 | **9.320** | 29.095 | 159.040 |

### Dictionary already prepared

| Substrings | GCC loop | GCC PCRE | GCC Matcher | Clang loop | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 0.206 | 0.163 | **0.121** | 0.205 | 0.153 | **0.116** |
| 16 | 0.278 | 0.167 | **0.121** | 0.287 | 0.151 | **0.115** |
| 32 | 0.472 | 0.182 | **0.122** | 0.514 | 0.167 | **0.115** |
| 64 | 0.890 | 0.217 | **0.119** | 0.917 | 0.197 | **0.113** |
| 128 | 1.699 | 0.273 | **0.119** | 1.807 | 0.239 | **0.112** |
| 256 | 3.564 | 0.391 | **0.119** | 3.916 | 0.376 | **0.115** |
| 512 | 8.669 | 0.657 | **0.118** | 9.537 | 0.620 | **0.115** |

## Short comments, match in the body

### Dictionary preparation included

| Substrings | GCC loop | GCC PCRE | GCC Matcher | Clang loop | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | **0.243** | 0.759 | 1.466 | **0.238** | 0.715 | 1.437 |
| 16 | **0.335** | 1.304 | 3.693 | **0.335** | 1.308 | 3.503 |
| 32 | **0.588** | 2.761 | 10.876 | **0.608** | 2.729 | 10.268 |
| 64 | **1.109** | 5.213 | 21.649 | **1.182** | 5.369 | 20.613 |
| 128 | **2.149** | 10.347 | 47.606 | **2.309** | 10.684 | 44.876 |
| 256 | **4.574** | 20.803 | 90.132 | **5.259** | 22.612 | 86.506 |
| 512 | **11.584** | 55.309 | 165.892 | **12.706** | 53.915 | 160.719 |

### Dictionary already prepared

| Substrings | GCC loop | GCC PCRE | GCC Matcher | Clang loop | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | **0.243** | 0.279 | 0.339 | **0.237** | 0.255 | 0.356 |
| 16 | **0.332** | 0.409 | 0.339 | **0.328** | 0.387 | 0.359 |
| 32 | 0.588 | 0.952 | **0.340** | 0.608 | 0.919 | **0.357** |
| 64 | 1.125 | 1.847 | **0.346** | 1.178 | 1.896 | **0.365** |
| 128 | 2.102 | 3.657 | **0.350** | 2.219 | 3.474 | **0.371** |
| 256 | 4.439 | 7.232 | **0.374** | 5.157 | 7.061 | **0.399** |
| 512 | 11.813 | 22.684 | **0.395** | 12.322 | 23.226† | **0.419** |

## Short comments, match near the end

### Dictionary preparation included

| Substrings | GCC loop | GCC PCRE | GCC Matcher | Clang loop | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | **0.214** | 0.746 | 1.524 | **0.212** | 0.712 | 1.450 |
| 16 | **0.297** | 1.332 | 3.714 | **0.296** | 1.310 | 3.577 |
| 32 | **0.475** | 2.789 | 10.581 | **0.510** | 2.777 | 9.993 |
| 64 | **0.908** | 5.402 | 21.689 | **0.988** | 5.597 | 20.558 |
| 128 | **1.713** | 10.850 | 47.736 | **1.792** | 10.876 | 44.835 |
| 256 | **3.614** | 21.700 | 90.194 | **3.988** | 23.000 | 86.258 |
| 512 | **8.716** | 57.250 | 165.712 | **9.584** | 57.339 | 159.330 |

### Dictionary already prepared

| Substrings | GCC loop | GCC PCRE | GCC Matcher | Clang loop | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | **0.219** | 0.272 | 0.364 | **0.213** | 0.251 | 0.379 |
| 16 | **0.289** | 0.429 | 0.365 | **0.304** | 0.405 | 0.385 |
| 32 | 0.491 | 0.989 | **0.366** | 0.503 | 0.958 | **0.379** |
| 64 | 0.908 | 1.983 | **0.373** | 0.974 | 2.042 | **0.387** |
| 128 | 1.674 | 3.956 | **0.376** | 1.869 | 3.778 | **0.392** |
| 256 | 3.712 | 7.854 | **0.395** | 3.901 | 7.672 | **0.414** |
| 512 | 8.863 | 28.092 | **0.426** | 9.636 | 25.386 | **0.444** |

## Detailed support messages, no match

### Dictionary preparation included

| Substrings | GCC loop | GCC PCRE | GCC Matcher | Clang loop | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | **0.974** | 1.533 | 2.934 | **0.961** | 1.490 | 3.039 |
| 16 | **1.570** | 3.499 | 5.080 | **1.621** | 3.447 | 5.011 |
| 32 | **3.522** | 8.371 | 12.344 | **3.659** | 8.219 | 11.811 |
| 64 | **6.895** | 17.000 | 23.005 | **7.227** | 17.595 | 22.107 |
| 128 | **13.418** | 34.743 | 48.206 | **14.132** | 33.684 | 45.453 |
| 256 | **30.017** | 68.710 | 91.713 | **30.735** | 80.405 | 88.371 |
| 512 | **68.080** | 226.290 | 167.197 | **70.372** | 233.067 | 160.763 |

### Dictionary already prepared

| Substrings | GCC loop | GCC PCRE | GCC Matcher | Clang loop | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | **0.937** | 1.063 | 1.818 | **0.940** | 1.006 | 1.979 |
| 16 | **1.572** | 2.580 | 1.817 | **1.615** | 2.513 | 1.978 |
| 32 | 3.518 | 6.563 | **1.819** | 3.622 | 6.442 | **1.977** |
| 64 | 6.837 | 13.533 | **1.837** | 7.198 | 14.054 | **1.994** |
| 128 | 13.351 | 27.811 | **1.851** | 14.132 | 26.568 | **2.013** |
| 256 | 30.008 | 55.000 | **1.934** | 30.699 | 67.249 | **2.101** |
| 512 | 67.982 | 194.352 | **2.043** | 71.652 | 185.207 | **2.209** |

## Detailed support messages, quoted matching term

### Dictionary preparation included

| Substrings | GCC loop | GCC PCRE | GCC Matcher | Clang loop | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | **0.390** | 0.978 | 1.881 | **0.386** | 0.922 | 1.890 |
| 16 | **0.555** | 1.735 | 4.047 | **0.552** | 1.723 | 3.852 |
| 32 | **1.306** | 4.192 | 11.166 | **1.352** | 4.198 | 10.590 |
| 64 | **2.833** | 8.503 | 21.987 | **2.901** | 8.821 | 20.995 |
| 128 | **5.474** | 17.059 | 46.899 | **5.675** | 16.864 | 44.408 |
| 256 | **11.498** | 33.833 | 90.497 | **12.020** | 33.957 | 87.543 |
| 512 | **25.079** | 112.783 | 165.785 | **25.553** | 114.737 | 159.855 |

### Dictionary already prepared

| Substrings | GCC loop | GCC PCRE | GCC Matcher | Clang loop | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | **0.384** | 0.496 | 0.756 | **0.386** | 0.465 | 0.810 |
| 16 | **0.567** | 0.850 | 0.758 | **0.553** | 0.804 | 0.810 |
| 32 | 1.374 | 2.420 | **0.757** | 1.349 | 2.357 | **0.809** |
| 64 | 2.846 | 5.050 | **0.763** | 2.902 | 5.238 | **0.814** |
| 128 | 5.461 | 10.320 | **0.761** | 5.541 | 9.833 | **0.813** |
| 256 | 11.462 | 20.401 | **0.810** | 11.744 | 19.979 | **0.866** |
| 512 | 24.990 | 67.443 | **0.849** | 26.359 | 67.255 | **0.906** |

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
