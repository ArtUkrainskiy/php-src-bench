# Direct checks of reuse estimates

A batch builds one candidate object, processes the stated number of strings and destroys it. Native arrays, regex strings and callbacks are already prepared, with warm PCRE caches. All four saved variants are processed equally often over each timed sample. Values are µs for the **whole batch**, not per string.

Checks select one call and points at approximately 75% and 125% of model estimates, capped at 4096. The complete tested counts are shown below. These observations do not establish an exact minimum; large capped estimates are not bracketed. In this input-length series, near-start/middle/end and 64 KiB cases have estimates only. Direct one-operation checks at all four 4 KiB match positions are in [FIXED-4K](FIXED-4K.md). Negative API Δ means the candidate batch was faster.

## gcc15

| Task | Input | Calls/object | Method | µs/batch | API Δ vs method |
|---|---:|---:|---|---:|---:|
| Moderation: no match | 128 B | 1 | `contains_loop` | 3.578 | +1525.88% |
| Moderation: no match | 128 B | 1 | `preg_match` | 4.722 | +1133.42% |
| Moderation: no match | 128 B | 1 | `matcher` | 58.275 | — |
| Moderation: no match | 128 B | 10 | `contains_loop` | 34.116 | +78.49% |
| Moderation: no match | 128 B | 10 | `preg_match` | 46.314 | +31.39% |
| Moderation: no match | 128 B | 10 | `matcher` | 60.763 | — |
| Moderation: no match | 128 B | 14 | `contains_loop` | 45.971 | +34.54% |
| Moderation: no match | 128 B | 14 | `preg_match` | 64.856 | -4.32% |
| Moderation: no match | 128 B | 14 | `matcher` | 62.134 | — |
| Moderation: no match | 128 B | 18 | `contains_loop` | 64.601 | -2.02% |
| Moderation: no match | 128 B | 18 | `preg_match` | 83.196 | -24.28% |
| Moderation: no match | 128 B | 18 | `matcher` | 62.990 | — |
| Moderation: no match | 128 B | 24 | `contains_loop` | 82.863 | -21.72% |
| Moderation: no match | 128 B | 24 | `preg_match` | 111.040 | -41.30% |
| Moderation: no match | 128 B | 24 | `matcher` | 65.154 | — |
| Moderation: no match | 4 KiB | 1 | `contains_loop` | 122.361 | -46.00% |
| Moderation: no match | 4 KiB | 1 | `preg_match` | 142.985 | -53.86% |
| Moderation: no match | 4 KiB | 1 | `matcher` | 65.950 | — |
| Moderation: no match | 4 KiB | 2 | `contains_loop` | 244.656 | -70.42% |
| Moderation: no match | 4 KiB | 2 | `preg_match` | 286.078 | -74.68% |
| Moderation: no match | 4 KiB | 2 | `matcher` | 72.404 | — |
| Moderation: no match | 16 KiB | 1 | `contains_loop` | 499.866 | -82.68% |
| Moderation: no match | 16 KiB | 1 | `preg_match` | 572.910 | -84.89% |
| Moderation: no match | 16 KiB | 1 | `matcher` | 86.576 | — |
| Moderation: no match | 16 KiB | 2 | `contains_loop` | 998.635 | -88.57% |
| Moderation: no match | 16 KiB | 2 | `preg_match` | 1145.478 | -90.04% |
| Moderation: no match | 16 KiB | 2 | `matcher` | 114.111 | — |
| List matching support terms | 512 B | 1 | `strpos_unique` | 17.648 | +168.75% |
| List matching support terms | 512 B | 1 | `preg_each_unique` | 20.048 | +136.48% |
| List matching support terms | 512 B | 1 | `matcher` | 47.486 | — |
| List matching support terms | 512 B | 2 | `strpos_unique` | 35.135 | +41.76% |
| List matching support terms | 512 B | 2 | `preg_each_unique` | 39.742 | +25.24% |
| List matching support terms | 512 B | 2 | `matcher` | 49.827 | — |
| List matching support terms | 512 B | 4 | `strpos_unique` | 70.680 | -23.59% |
| List matching support terms | 512 B | 4 | `preg_each_unique` | 79.905 | -32.33% |
| List matching support terms | 512 B | 4 | `matcher` | 54.014 | — |
| Replace terms with help URLs | 512 B | 1 | `strtr` | 38.361 | +20.90% |
| Replace terms with help URLs | 512 B | 1 | `preg_replace_callback` | 12.910 | +259.35% |
| Replace terms with help URLs | 512 B | 1 | `replacer` | 46.389 | — |
| Replace terms with help URLs | 512 B | 3 | `strtr` | 115.387 | -56.91% |
| Replace terms with help URLs | 512 B | 3 | `preg_replace_callback` | 38.587 | +28.65% |
| Replace terms with help URLs | 512 B | 3 | `replacer` | 49.646 | — |
| Replace terms with help URLs | 512 B | 5 | `strtr` | 191.483 | -72.38% |
| Replace terms with help URLs | 512 B | 5 | `preg_replace_callback` | 64.169 | -17.42% |
| Replace terms with help URLs | 512 B | 5 | `replacer` | 52.966 | — |
| List matching support terms | 4 KiB | 1 | `strpos_unique` | 105.032 | -41.96% |
| List matching support terms | 4 KiB | 1 | `preg_each_unique` | 64.428 | -5.47% |
| List matching support terms | 4 KiB | 1 | `matcher` | 60.862 | — |
| List matching support terms | 4 KiB | 2 | `strpos_unique` | 210.253 | -64.69% |
| List matching support terms | 4 KiB | 2 | `preg_each_unique` | 130.702 | -43.14% |
| List matching support terms | 4 KiB | 2 | `matcher` | 74.251 | — |
| Replace terms with help URLs | 4 KiB | 1 | `strtr` | 357.298 | -83.39% |
| Replace terms with help URLs | 4 KiB | 1 | `preg_replace_callback` | 98.911 | -39.98% |
| Replace terms with help URLs | 4 KiB | 1 | `replacer` | 59.369 | — |
| Replace terms with help URLs | 4 KiB | 2 | `strtr` | 714.340 | -89.98% |
| Replace terms with help URLs | 4 KiB | 2 | `preg_replace_callback` | 196.832 | -63.69% |
| Replace terms with help URLs | 4 KiB | 2 | `replacer` | 71.526 | — |
| List matching support terms | 16 KiB | 1 | `strpos_unique` | 207.212 | -56.01% |
| List matching support terms | 16 KiB | 1 | `preg_each_unique` | 103.094 | -11.71% |
| List matching support terms | 16 KiB | 1 | `matcher` | 91.136 | — |
| List matching support terms | 16 KiB | 2 | `strpos_unique` | 414.855 | -67.92% |
| List matching support terms | 16 KiB | 2 | `preg_each_unique` | 205.994 | -35.42% |
| List matching support terms | 16 KiB | 2 | `matcher` | 132.998 | — |
| Replace terms with help URLs | 16 KiB | 1 | `strtr` | 1440.585 | -93.42% |
| Replace terms with help URLs | 16 KiB | 1 | `preg_replace_callback` | 390.556 | -75.75% |
| Replace terms with help URLs | 16 KiB | 1 | `replacer` | 94.740 | — |
| Replace terms with help URLs | 16 KiB | 2 | `strtr` | 2881.754 | -95.07% |
| Replace terms with help URLs | 16 KiB | 2 | `preg_replace_callback` | 790.790 | -82.02% |
| Replace terms with help URLs | 16 KiB | 2 | `replacer` | 142.170 | — |

### Additional A/A controls

| Stage | Control | Time Δ |
|---|---|---:|
| before | constructor | -0.096% |
| before | batch | +0.059% |
| after | constructor | -0.016% |
| after | batch | +0.031% |

## clang21

| Task | Input | Calls/object | Method | µs/batch | API Δ vs method |
|---|---:|---:|---|---:|---:|
| Moderation: no match | 128 B | 1 | `contains_loop` | 3.649 | +1459.32% |
| Moderation: no match | 128 B | 1 | `preg_match` | 4.491 | +1169.25% |
| Moderation: no match | 128 B | 1 | `matcher` | 56.991 | — |
| Moderation: no match | 128 B | 10 | `contains_loop` | 36.793 | +64.01% |
| Moderation: no match | 128 B | 10 | `preg_match` | 44.357 | +35.92% |
| Moderation: no match | 128 B | 10 | `matcher` | 60.225 | — |
| Moderation: no match | 128 B | 12 | `contains_loop` | 43.080 | +40.06% |
| Moderation: no match | 128 B | 12 | `preg_match` | 53.199 | +13.59% |
| Moderation: no match | 128 B | 12 | `matcher` | 60.437 | — |
| Moderation: no match | 128 B | 18 | `contains_loop` | 66.966 | -6.02% |
| Moderation: no match | 128 B | 18 | `preg_match` | 80.144 | -21.70% |
| Moderation: no match | 128 B | 18 | `matcher` | 62.805 | — |
| Moderation: no match | 128 B | 22 | `contains_loop` | 79.134 | -19.62% |
| Moderation: no match | 128 B | 22 | `preg_match` | 97.413 | -34.67% |
| Moderation: no match | 128 B | 22 | `matcher` | 63.671 | — |
| Moderation: no match | 4 KiB | 1 | `contains_loop` | 117.647 | -44.96% |
| Moderation: no match | 4 KiB | 1 | `preg_match` | 136.647 | -52.65% |
| Moderation: no match | 4 KiB | 1 | `matcher` | 64.691 | — |
| Moderation: no match | 4 KiB | 2 | `contains_loop` | 235.222 | -69.02% |
| Moderation: no match | 4 KiB | 2 | `preg_match` | 273.267 | -73.26% |
| Moderation: no match | 4 KiB | 2 | `matcher` | 73.030 | — |
| Moderation: no match | 16 KiB | 1 | `contains_loop` | 482.468 | -81.53% |
| Moderation: no match | 16 KiB | 1 | `preg_match` | 546.589 | -83.70% |
| Moderation: no match | 16 KiB | 1 | `matcher` | 89.050 | — |
| Moderation: no match | 16 KiB | 2 | `contains_loop` | 965.435 | -87.47% |
| Moderation: no match | 16 KiB | 2 | `preg_match` | 1092.787 | -88.93% |
| Moderation: no match | 16 KiB | 2 | `matcher` | 121.016 | — |
| List matching support terms | 512 B | 1 | `strpos_unique` | 18.093 | +152.51% |
| List matching support terms | 512 B | 1 | `preg_each_unique` | 20.459 | +123.00% |
| List matching support terms | 512 B | 1 | `matcher` | 45.538 | — |
| List matching support terms | 512 B | 2 | `strpos_unique` | 36.149 | +32.05% |
| List matching support terms | 512 B | 2 | `preg_each_unique` | 40.178 | +18.59% |
| List matching support terms | 512 B | 2 | `matcher` | 47.741 | — |
| List matching support terms | 512 B | 4 | `strpos_unique` | 72.345 | -27.75% |
| List matching support terms | 512 B | 4 | `preg_each_unique` | 81.180 | -35.64% |
| List matching support terms | 512 B | 4 | `matcher` | 52.235 | — |
| Replace terms with help URLs | 512 B | 1 | `strtr` | 39.176 | +15.32% |
| Replace terms with help URLs | 512 B | 1 | `preg_replace_callback` | 13.991 | +222.77% |
| Replace terms with help URLs | 512 B | 1 | `replacer` | 45.149 | — |
| Replace terms with help URLs | 512 B | 3 | `strtr` | 116.828 | -57.98% |
| Replace terms with help URLs | 512 B | 3 | `preg_replace_callback` | 41.810 | +17.51% |
| Replace terms with help URLs | 512 B | 3 | `replacer` | 49.130 | — |
| Replace terms with help URLs | 512 B | 5 | `strtr` | 195.095 | -73.32% |
| Replace terms with help URLs | 512 B | 5 | `preg_replace_callback` | 69.437 | -25.06% |
| Replace terms with help URLs | 512 B | 5 | `replacer` | 52.029 | — |
| List matching support terms | 4 KiB | 1 | `strpos_unique` | 101.717 | -41.16% |
| List matching support terms | 4 KiB | 1 | `preg_each_unique` | 63.926 | -6.09% |
| List matching support terms | 4 KiB | 1 | `matcher` | 60.016 | — |
| List matching support terms | 4 KiB | 2 | `strpos_unique` | 203.513 | -63.80% |
| List matching support terms | 4 KiB | 2 | `preg_each_unique` | 129.866 | -43.19% |
| List matching support terms | 4 KiB | 2 | `matcher` | 73.752 | — |
| Replace terms with help URLs | 4 KiB | 1 | `strtr` | 361.512 | -83.82% |
| Replace terms with help URLs | 4 KiB | 1 | `preg_replace_callback` | 108.257 | -46.03% |
| Replace terms with help URLs | 4 KiB | 1 | `replacer` | 58.486 | — |
| Replace terms with help URLs | 4 KiB | 2 | `strtr` | 722.923 | -90.10% |
| Replace terms with help URLs | 4 KiB | 2 | `preg_replace_callback` | 216.153 | -66.85% |
| Replace terms with help URLs | 4 KiB | 2 | `replacer` | 71.515 | — |
| List matching support terms | 16 KiB | 1 | `strpos_unique` | 199.393 | -54.49% |
| List matching support terms | 16 KiB | 1 | `preg_each_unique` | 103.070 | -12.15% |
| List matching support terms | 16 KiB | 1 | `matcher` | 90.653 | — |
| List matching support terms | 16 KiB | 2 | `strpos_unique` | 397.503 | -66.09% |
| List matching support terms | 16 KiB | 2 | `preg_each_unique` | 205.504 | -34.43% |
| List matching support terms | 16 KiB | 2 | `matcher` | 134.641 | — |
| Replace terms with help URLs | 16 KiB | 1 | `strtr` | 1457.699 | -93.53% |
| Replace terms with help URLs | 16 KiB | 1 | `preg_replace_callback` | 429.791 | -78.05% |
| Replace terms with help URLs | 16 KiB | 1 | `replacer` | 94.292 | — |
| Replace terms with help URLs | 16 KiB | 2 | `strtr` | 2913.946 | -95.07% |
| Replace terms with help URLs | 16 KiB | 2 | `preg_replace_callback` | 859.461 | -83.31% |
| Replace terms with help URLs | 16 KiB | 2 | `replacer` | 143.513 | — |

### Additional A/A controls

| Stage | Control | Time Δ |
|---|---|---:|
| before | constructor | +0.012% |
| before | batch | -0.105% |
| after | constructor | +0.134% |
| after | batch | +0.200% |

All estimated counts, chosen direct points and raw samples: [GCC](data/length-payback-gcc15.json), [Clang](data/length-payback-clang21.json).
