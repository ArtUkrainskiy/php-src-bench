# Object preparation: first construction and repeated build/release

All times are microseconds. **First** is the first constructor in a fresh PHP process after the dictionary is parsed. PHP startup, parsing and object release are excluded from that timer. Five fresh processes are measured. It does not imply cold CPU or filesystem caches.

**Build/release** repeatedly creates and frees an object, with the same dictionary already loaded. It includes the common closure/loop cost and object release, with 250 ms warmup and 15 samples totaling about one second. It excludes searching. These are different measurements; do not substitute one for the other in payback calculations.

The inputs here are the [memory dictionaries](MEMORY.md), not the moderation policies. Equal string counts do not imply equal constructor cost: lengths, alphabet and shared prefixes/suffixes differ. Use [actual product-job payback](AMORTIZATION.md) for a deployment decision.

## Glossary and constructed catalog

| Strings | Class | GCC first | GCC build/release | Clang first | Clang build/release |
|---|---|---:|---:|---:|---:|
| 8 | Matcher | 8.857 | 2.172 | 8.125 | 2.239 |
| 8 | Replacer | 8.827 | 2.673 | 8.255 | 2.378 |
| 16 | Matcher | 12.003 | 4.003 | 11.241 | 3.757 |
| 16 | Replacer | 13.064 | 4.893 | 12.404 | 4.727 |
| 32 | Matcher | 19.717 | 8.281 | 18.946 | 7.673 |
| 32 | Replacer | 20.588 | 9.299 | 19.957 | 8.973 |
| 64 | Matcher | 38.953 | 18.536 | 37.130 | 17.510 |
| 64 | Replacer | 37.100 | 18.558 | 36.078 | 17.947 |
| 128 | Matcher | 80.321 | 44.777 | 78.668 | 42.940 |
| 128 | Replacer | 77.575 | 43.486 | 77.966 | 43.611 |
| 256 | Matcher | 164.077 | 131.578 | 162.073 | 126.214 |
| 256 | Replacer | 150.562 | 111.354 | 147.055 | 110.756 |
| 512 | Matcher | 379.460 | 350.894 | 373.189 | 343.190 |
| 512 | Replacer | 314.539 | 288.860 | 309.289 | 284.014 |
| 1000 | Matcher | 905.396 | 874.884 | 887.412 | 865.216 |
| 1000 | Replacer | 642.643 | 610.919 | 631.443 | 601.623 |
| 2000 | Matcher | 1965.271 | 1756.260 | 1946.275 | 1758.263 |
| 2000 | Replacer | 1162.708 | 1133.603 | 1154.072 | 1124.216 |
| 5000 | Matcher | 4747.783 | 3943.480 | 4770.225 | 3905.796 |
| 5000 | Replacer | 3629.037 | 3003.977 | 3631.662 | 2983.316 |
| 10000 | Matcher | 10396.122 | 9960.388 | 10396.472 | 10003.429 |
| 10000 | Replacer | 6799.806 | 5704.203 | 6829.421 | 5685.590 |

## Permuted-byte control

| Strings | Class | GCC first | GCC build/release | Clang first | Clang build/release |
|---|---|---:|---:|---:|---:|
| 8 | Matcher | 10.991 | 3.316 | 10.169 | 3.144 |
| 8 | Replacer | 9.217 | 2.936 | 8.756 | 2.924 |
| 16 | Matcher | 17.072 | 6.912 | 16.020 | 6.596 |
| 16 | Replacer | 14.698 | 6.228 | 14.057 | 6.102 |
| 32 | Matcher | 30.336 | 14.054 | 28.654 | 13.584 |
| 32 | Replacer | 28.033 | 12.934 | 27.141 | 13.678 |
| 64 | Matcher | 57.638 | 31.516 | 56.456 | 30.802 |
| 64 | Replacer | 52.629 | 27.740 | 51.346 | 26.858 |
| 128 | Matcher | 114.675 | 78.994 | 113.092 | 75.367 |
| 128 | Replacer | 114.003 | 80.504 | 112.490 | 77.784 |
| 256 | Matcher | 246.823 | 220.776 | 244.378 | 217.295 |
| 256 | Replacer | 242.605 | 215.207 | 248.937 | 212.778 |
| 512 | Matcher | 607.779 | 582.264 | 614.200 | 581.285 |
| 512 | Replacer | 558.596 | 549.337 | 572.242 | 545.209 |
| 1000 | Matcher | 1940.915 | 1839.555 | 1972.695 | 1862.159 |
| 1000 | Replacer | 1831.500 | 1729.916 | 1878.258 | 1753.275 |
| 2000 | Matcher | 6184.984 | 5523.641 | 6272.889 | 5542.005 |
| 2000 | Replacer | 6007.712 | 5332.931 | 6085.157 | 5325.866 |
| 5000 | Matcher | 22656.315 | 22366.312 | 22633.803 | 22291.785 |
| 5000 | Replacer | 22039.650 | 21565.302 | 22360.000 | 21782.478 |
| 10000 | Matcher | 59028.399 | 58645.137 | 58641.825 | 58298.236 |
| 10000 | Replacer | 56296.703 | 55900.906 | 56585.253 | 56176.552 |

All first/warm samples, iteration counts, A/A controls and hashes: [GCC](data/preparation-gcc15.json), [Clang](data/preparation-clang21.json). No subtraction of an empty timing loop is used. Constructor timing is not a measurement of whole-request latency.
