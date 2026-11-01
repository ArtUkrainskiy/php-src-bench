# Positive primary time deltas

[Interpretation](../README.md). Every positive primary median is listed, including tiny changes and noisy observations. A positive median alone does not establish a regression. Repeats, when selected by the stated rule, are in [repeats.md](repeats.md). Controls are separate from application results.

## product

### Intel gcc13

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `moderation/medium/en/start` | 7.9580 | 7.9580 | +0.01% | -0.10% | +0.23% | -0.21% | -2.38% |
| `moderation/medium/en/end` | 9.0168 | 9.0308 | +0.14% | -0.04% | +0.47% | -0.13% | -2.12% |
| `moderation/long/en/absent` | 232.1100 | 233.0089 | +0.44% | -1.21% | +1.01% | +0.03% | -0.17% |
| `moderation/long/en/start` | 140.7287 | 141.7955 | +1.23% | -0.35% | +3.72% | +0.01% | -0.16% |
| `moderation/long/en/middle` | 148.9693 | 150.5571 | +0.40% | -0.71% | +1.07% | +0.26% | -0.15% |
| `moderation/long/ru/absent` | 307.6055 | 308.7977 | +0.39% | -0.96% | +0.63% | +0.25% | -0.17% |
| `moderation/long/ru/start` | 205.4358 | 206.6618 | +0.60% | -0.39% | +1.82% | +0.58% | -0.15% |
| `moderation/long/ru/end` | 239.6455 | 240.9941 | +0.56% | -0.10% | +1.91% | +0.13% | -0.13% |
| `moderation/long/zh/start` | 137.5252 | 136.1976 | +0.77% | -1.54% | +4.08% | +0.15% | -0.19% |
| `moderation/long/zh/middle` | 152.7230 | 153.6481 | +0.28% | -0.68% | +1.48% | +0.24% | -0.18% |
| `moderation/long/zh/end` † | 161.2914 | 162.4371 | +0.33% | -4.02% | +1.40% | +0.11% | -0.17% |
| `str_contains/en/absent` | 0.8087 | 0.8081 | +0.47% | -1.24% | +4.21% | -1.78% | -3.49% |
| `substr_count/en/start` | 1.0198 | 1.0322 | +1.43% | -1.79% | +2.28% | -1.51% | -5.39% |
| `stream_get_line/en/absent` | 1.0084 | 1.0056 | +0.04% | -1.90% | +0.12% | -0.74% | -2.59% |
| `stream_get_line/en/end` | 1.0023 | 1.0053 | +0.26% | -0.58% | +3.24% | -0.71% | -2.52% |
| `strpos/en/64k/absent` | 12.8276 | 12.8333 | +0.04% | -0.57% | +1.79% | -0.31% | -0.23% |
| `strpos/en/64k/middle` | 6.4195 | 6.4423 | +0.01% | -1.24% | +1.18% | -0.32% | -0.45% |
| `documents/search/log_long/absent` | 15.9613 | 15.9414 | +0.82% | -0.79% | +1.50% | +0.88% | -0.16% |
| `documents/search/log_long/present` | 8.3073 | 8.3589 | +0.62% | -0.89% | +1.42% | +0.23% | -0.31% |
| `documents/count/receipt` | 0.4753 | 0.4768 | +0.31% | +0.22% | +0.38% | +0.30% | -8.64% |
| `documents/repeated/substr_count/23` | 3.4733 | 3.4738 | +0.02% | -0.24% | +0.23% | +0.31% | -12.45% |

### Intel gcc14

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `moderation/long/en/absent` | 240.7688 | 241.4169 | +0.02% | -0.61% | +1.71% | +0.10% | -0.16% |
| `moderation/long/en/end` | 169.2134 | 169.2686 | +0.28% | -1.32% | +0.57% | +0.23% | -0.13% |
| `moderation/long/ru/middle` | 233.9428 | 232.5875 | +0.08% | -1.92% | +0.60% | -0.27% | -0.13% |
| `moderation/long/zh/start` | 151.7911 | 151.2366 | +1.20% | -1.25% | +3.31% | -0.50% | -0.18% |
| `moderation/long/zh/middle` | 160.7897 | 162.2216 | +0.14% | -0.20% | +1.07% | -0.29% | -0.17% |
| `moderation/long/zh/end` | 173.7695 | 173.3166 | +0.08% | -0.26% | +0.71% | +0.00% | -0.16% |
| `str_contains/en/middle` | 0.4380 | 0.4430 | +0.57% | +0.29% | +1.13% | -1.84% | -5.30% |
| `strstr/en/end` | 0.9241 | 0.9309 | +0.83% | -0.71% | +1.44% | -0.59% | -2.79% |
| `strpos/en/64k/absent` | 12.4246 | 12.5397 | +0.44% | -2.01% | +1.70% | +0.30% | -0.22% |
| `strpos/en/64k/end` | 13.0522 | 13.1061 | +0.22% | -0.61% | +2.63% | -0.27% | -0.22% |
| `documents/moderation/en/middle` | 3.2314 | 3.2592 | +0.61% | -1.49% | +5.50% | -2.00% | -5.27% |
| `documents/search/log_short/absent` | 0.9633 | 0.9709 | +0.79% | -0.93% | +9.13% | +1.41% | -2.24% |
| `documents/replace/receipt/array` | 2.5958 | 2.6221 | +1.01% | +0.81% | +1.18% | +0.88% | -8.00% |
| `documents/ireplace/receipt/equal` | 0.6209 | 0.6340 | +2.10% | +1.81% | +2.37% | +1.48% | -4.77% |
| `documents/ireplace/receipt/longer` | 1.1230 | 1.1346 | +1.02% | +0.77% | +1.23% | +0.50% | -5.90% |
| `documents/stream/mail_delivery/closing` | 0.7460 | 0.7472 | +0.14% | +0.12% | +0.22% | +0.17% | -2.79% |

### Intel clang18

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `moderation/long/ru/absent` | 322.6537 | 335.9517 | +4.12% | +3.20% | +4.53% | +2.51% | -11.09% |
| `moderation/long/ru/start` | 214.3528 | 222.7869 | +4.72% | +3.13% | +5.29% | +2.75% | -10.81% |
| `moderation/long/ru/middle` | 233.5566 | 242.2776 | +3.63% | +3.13% | +6.27% | +3.63% | -10.83% |
| `moderation/long/ru/end` | 249.7696 | 259.4917 | +3.89% | +3.65% | +5.37% | +3.45% | -10.85% |
| `moderation/long/zh/start` | 142.7185 | 142.7157 | +0.13% | -2.83% | +0.57% | +2.05% | -11.88% |
| `moderation/long/zh/middle` | 155.6299 | 156.8494 | +0.26% | -0.19% | +2.54% | +1.30% | -11.88% |
| `str_contains/en/middle` † | 0.4463 | 0.4460 | +0.81% | -11.96% | +1.96% | +0.59% | -11.57% |
| `str_replace/en/absent` | 0.9950 | 1.0058 | +1.53% | -0.02% | +3.03% | -0.40% | -12.13% |
| `documents/search/receipt/absent` | 0.5592 | 0.5661 | +1.82% | +0.41% | +2.89% | -0.28% | -12.34% |

### Intel clang20

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `moderation/medium/en/start` | 7.9895 | 8.0022 | +0.16% | +0.00% | +0.29% | +0.09% | -12.25% |
| `str_contains/en/absent` | 0.8083 | 0.8043 | +0.04% | -1.53% | +4.16% | +0.98% | -12.44% |
| `str_contains/en/middle` | 0.4188 | 0.4190 | +1.59% | -0.39% | +3.78% | +2.82% | -11.64% |
| `strtr/en/start` | 2.0212 | 2.0428 | +0.51% | -1.02% | +1.07% | -0.86% | -12.23% |
| `explode/en/middle` | 0.9257 | 0.9299 | +0.31% | -1.13% | +0.76% | -1.03% | -10.45% |
| `strpos/en/64k/absent` | 12.6702 | 12.7724 | +0.16% | -0.67% | +0.81% | +0.91% | -11.75% |
| `documents/search/log_long/absent` † | 16.3596 | 16.4720 | +0.69% | -0.67% | +8.21% | +0.82% | -10.25% |
| `documents/search/log_long/present` | 8.4260 | 8.4965 | +0.38% | -1.27% | +1.00% | +0.07% | -10.11% |
| `documents/ireplace/receipt/shorter` | 1.0814 | 1.1274 | +4.27% | +4.13% | +4.41% | +3.93% | -8.18% |
| `documents/ireplace/receipt/equal` | 0.6149 | 0.6378 | +3.73% | +3.58% | +3.79% | +3.13% | -6.49% |
| `documents/ireplace/receipt/longer` | 1.0794 | 1.1251 | +4.32% | +3.89% | +4.33% | +3.89% | -8.16% |
| `documents/repeated/substr_count/3` | 3.5574 | 3.6097 | +1.47% | +1.37% | +1.69% | +1.77% | -11.20% |
| `documents/repeated/str_replace/3` | 7.2227 | 7.3260 | +1.42% | +1.37% | +2.09% | +1.87% | -11.05% |
| `documents/repeated/str_replace/23` | 7.0452 | 7.1427 | +1.57% | +0.55% | +3.49% | +2.47% | -11.61% |

## extensions

### AMD gcc15

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_stristr/ru/middle` | 14.6292 | 14.6277 | +0.52% | -0.13% | +1.16% | +0.05% | -0.05% |
| `mb_stristr/zh/middle` † | 13.3924 | 13.3446 | +0.37% | -1.17% | +28.53% | -0.15% | -0.05% |

### AMD clang21

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_stripos/ru/middle` | 10.3539 | 10.3278 | +0.98% | -4.18% | +3.59% | -0.81% | -0.02% |
| `mb_stristr/ru/middle` | 14.3939 | 14.7068 | +2.17% | -0.31% | +2.57% | -0.85% | -0.02% |
| `mb_stripos/zh/middle` | 9.7925 | 9.7686 | +0.00% | -0.33% | +3.32% | -0.40% | -0.02% |

### Intel gcc13

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_stripos/en/absent` | 10.1674 | 10.2028 | +0.61% | -3.08% | +0.85% | -0.26% | -0.08% |
| `mb_strstr/en/middle` | 3.5245 | 3.5256 | +0.04% | -0.30% | +0.05% | +0.30% | -0.20% |
| `mb_stristr/en/absent` | 9.4898 | 9.5278 | +0.36% | +0.16% | +0.91% | +0.38% | -0.08% |
| `mb_strstr/ru/middle` | 4.9330 | 4.9225 | +0.02% | -0.46% | +0.09% | -1.33% | -0.16% |
| `mb_stristr/ru/middle` | 14.4345 | 14.0414 | +0.18% | -3.93% | +1.99% | +0.42% | -0.05% |
| `mb_strpos/zh/middle` | 0.6493 | 0.6554 | +0.85% | +0.80% | +1.20% | +0.68% | -2.88% |
| `mb_strstr/zh/middle` | 5.5712 | 5.5973 | +0.47% | -0.01% | +1.70% | +0.34% | -0.16% |

### Intel gcc14

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_stripos/en/absent` | 9.8994 | 9.9021 | +0.19% | -1.03% | +0.33% | -0.53% | -0.08% |
| `mb_strstr/en/middle` | 3.5088 | 3.5161 | +0.02% | -0.15% | +0.24% | -0.19% | -0.20% |
| `mb_substr_count/en/absent` | 1.2322 | 1.2427 | +0.73% | +0.59% | +0.95% | +0.62% | -1.94% |
| `mb_strpos/ru/middle` | 0.6653 | 0.6676 | +0.37% | +0.26% | +0.45% | +0.40% | -2.46% |
| `mb_stripos/ru/absent` | 10.5131 | 10.5123 | +0.01% | -3.04% | +0.30% | -0.99% | -0.07% |
| `mb_stristr/zh/absent` | 11.2300 | 11.3713 | +1.06% | -1.29% | +4.85% | +0.30% | -0.08% |
| `grapheme_strpos/en/absent` | 3.0542 | 3.0559 | +0.03% | -0.79% | +0.63% | -0.03% | -0.38% |
| `grapheme_stripos/en/middle` | 2.8679 | 2.8746 | +0.57% | -0.56% | +1.54% | +0.40% | -0.36% |
| `grapheme_stripos/en/end` | 3.2327 | 3.2673 | +0.74% | +0.03% | +1.81% | +2.10% | -0.34% |
| `grapheme_strstr/en/middle` | 2.7627 | 2.7403 | +0.00% | -1.74% | +0.48% | -0.23% | -0.39% |

### Intel clang18

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_stripos/en/absent` | 8.8263 | 8.8676 | +0.57% | -0.94% | +1.20% | +0.07% | -0.43% |
| `mb_stripos/en/middle` | 8.8984 | 8.9659 | +0.80% | -0.61% | +1.55% | +0.43% | -0.23% |
| `mb_stristr/en/absent` | 8.2811 | 8.2972 | +0.14% | -0.29% | +0.42% | +0.49% | -0.43% |
| `mb_stristr/en/middle` | 10.9312 | 10.9645 | +0.30% | +0.25% | +0.74% | +0.43% | -0.16% |
| `mb_strstr/ru/middle` | 4.8461 | 4.8700 | +0.64% | +0.15% | +5.16% | +1.03% | -0.49% |
| `mb_stripos/zh/middle` | 9.1296 | 9.1721 | +0.38% | -0.87% | +0.71% | -0.23% | -0.16% |
| `mb_stristr/zh/absent` | 10.5078 | 10.5266 | +0.18% | -7.28% | +0.54% | -0.15% | -0.30% |
| `grapheme_stripos/en/middle` | 2.2614 | 2.2667 | +0.10% | -0.10% | +0.65% | -0.82% | -0.70% |

### Intel clang20

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_stripos/en/absent` | 8.9981 | 8.9452 | +0.23% | -0.77% | +5.08% | +0.66% | -0.43% |
| `mb_stripos/en/middle` | 8.8636 | 8.9056 | +0.54% | -0.36% | +3.08% | +0.20% | -0.23% |
| `mb_stristr/ru/absent` | 8.7665 | 8.7506 | +0.03% | -2.41% | +2.55% | +0.71% | -0.27% |
| `mb_stripos/zh/middle` | 9.1749 | 9.2349 | +0.01% | -0.16% | +0.88% | +0.75% | -0.15% |
| `mb_strstr/zh/middle` | 6.4947 | 6.5736 | +1.66% | -0.02% | +3.20% | +0.50% | -0.41% |
| `mb_stristr/zh/absent` | 10.6988 | 10.7358 | +0.38% | -0.62% | +0.92% | +0.19% | -0.28% |
| `grapheme_strpos/en/absent` | 2.7002 | 2.6638 | +0.12% | -4.39% | +2.06% | -3.51% | -1.32% |
| `grapheme_strpos/en/start` | 1.6816 | 1.6824 | +0.05% | -1.08% | +0.19% | -0.27% | -0.13% |
| `grapheme_strpos/en/middle` | 2.3169 | 2.3157 | +0.72% | -1.29% | +3.18% | +1.07% | -0.76% |
| `grapheme_stripos/en/absent` | 2.8706 | 2.8923 | +0.53% | -0.64% | +1.78% | +2.29% | -1.21% |
| `grapheme_stripos/en/middle` | 2.5140 | 2.4984 | +0.27% | -2.81% | +1.97% | +0.74% | -0.70% |
| `grapheme_stripos/en/end` | 2.8233 | 2.8407 | +0.82% | -1.94% | +1.27% | -1.22% | -1.22% |
| `grapheme_strstr/en/start` | 1.7437 | 1.7443 | +0.03% | -0.46% | +0.24% | -0.87% | -0.13% |
| `grapheme_strstr/en/middle` | 2.5221 | 2.5983 | +1.95% | +0.24% | +8.16% | +2.08% | -0.75% |
| `grapheme_strstr/en/end` | 3.0164 | 3.0824 | +1.16% | -0.12% | +3.02% | -0.13% | -1.31% |

## controls

### AMD gcc15

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `moderation/short/en/start` | 0.2400 | 0.2405 | +0.06% | -0.28% | +7.00% | -0.03% | -0.00% |
| `moderation/short/ru/start` | 1.7243 | 1.7272 | +0.16% | -2.52% | +0.24% | +0.28% | -0.00% |
| `moderation/short/ru/middle` | 1.8948 | 1.8952 | +0.03% | -0.07% | +0.47% | +0.45% | +0.00% |
| `moderation/short/ru/end` | 2.0792 | 2.0808 | +0.16% | -1.66% | +1.17% | +0.39% | +0.00% |
| `moderation/short/zh/absent` | 0.5492 | 0.5514 | +0.76% | -0.23% | +1.35% | +0.31% | +0.00% |
| `moderation/short/zh/middle` | 0.4583 | 0.4589 | +0.14% | -0.58% | +0.34% | +0.12% | -0.00% |
| `moderation/short/zh/end` | 0.4712 | 0.4718 | +0.21% | -0.23% | +0.88% | +0.06% | +0.00% |
| `controls/haystack-1023/absent` | 0.1815 | 0.1816 | +0.02% | -0.27% | +3.33% | +0.24% | -0.00% |
| `controls/haystack-1023/origin` | 0.0162 | 0.0162 | +1.05% | -1.32% | +5.53% | +0.04% | -0.00% |
| `controls/needle-8/absent` | 0.8774 | 0.8779 | +0.24% | -0.19% | +0.36% | +0.39% | -0.00% |
| `controls/needle-32/absent` | 0.4655 | 0.4765 | +2.30% | +1.95% | +2.63% | +1.82% | +0.14% |
| `controls/needle-32/origin` | 0.0353 | 0.0348 | +0.65% | -1.69% | +3.00% | +0.21% | +0.65% |
| `controls/prefix-31/absent` | 15.4023 | 16.1107 | +3.29% | -0.19% | +5.09% | +0.39% | -0.04% |
| `controls/prefix-64/absent` | 30.8218 | 40.3031 | +30.76% | +29.38% | +30.90% | +31.12% | +0.00% |

### AMD clang21

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `moderation/short/en/start` | 0.2360 | 0.2365 | +0.38% | -0.42% | +0.64% | +0.11% | +0.00% |
| `moderation/short/ru/start` | 1.7616 | 1.7673 | +0.14% | -0.18% | +1.64% | +0.17% | -0.00% |
| `moderation/short/ru/end` | 2.1391 | 2.1428 | +0.13% | -2.12% | +2.84% | -0.28% | -0.00% |
| `moderation/short/zh/absent` | 0.5870 | 0.5893 | +0.55% | +0.26% | +1.04% | +0.44% | -0.00% |
| `moderation/short/zh/middle` | 0.5003 | 0.5036 | +0.66% | -1.96% | +1.37% | +1.97% | -0.00% |
| `moderation/short/zh/end` | 0.4960 | 0.4966 | +0.22% | -1.75% | +0.57% | +0.60% | +0.00% |
| `controls/haystack-1023/origin` | 0.0127 | 0.0127 | +0.09% | -1.62% | +1.83% | +1.24% | -0.00% |
| `controls/needle-8/origin` | 0.0125 | 0.0125 | +0.11% | +0.06% | +0.15% | -0.11% | -0.00% |
| `controls/needle-32/absent` | 0.4279 | 0.4296 | +0.33% | +0.23% | +0.47% | +0.37% | -5.62% |
| `controls/needle-32/origin` † | 0.0293 | 0.0317 | +8.55% | +6.94% | +26.18% | +5.72% | +2.89% |
| `controls/needle-64/absent` | 0.2080 | 0.2101 | +1.00% | +0.84% | +1.10% | +1.06% | -3.49% |
| `controls/needle-256/absent` | 0.0891 | 0.0929 | +4.35% | +3.98% | +5.60% | +4.50% | +3.89% |
| `controls/remaining-1023/absent` | 0.2266 | 0.2272 | +0.27% | +0.09% | +1.58% | +0.03% | +0.00% |

### Intel gcc13

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `moderation/short/en/start` | 0.2550 | 0.2559 | +0.23% | -0.37% | +1.02% | -0.04% | +0.00% |
| `moderation/short/en/middle` | 0.2707 | 0.2725 | +0.82% | -0.56% | +1.27% | -0.12% | +0.00% |
| `moderation/short/ru/absent` | 2.8598 | 2.8598 | +0.00% | -0.05% | +0.41% | -0.25% | -0.00% |
| `moderation/short/ru/middle` | 2.2881 | 2.2891 | +0.04% | -0.16% | +0.11% | +0.03% | -0.00% |
| `moderation/short/ru/end` | 2.5862 | 2.5855 | +0.01% | -0.05% | +0.20% | +0.07% | +0.00% |
| `moderation/short/zh/start` | 0.5087 | 0.5114 | +0.38% | -0.04% | +0.71% | +0.15% | -0.00% |
| `moderation/short/zh/end` | 0.5258 | 0.5245 | +0.17% | -0.42% | +0.60% | +0.15% | -0.00% |
| `controls/length-31/middle` | 0.2710 | 0.2841 | +4.84% | +4.67% | +5.27% | +7.25% | -6.99% |
| `controls/haystack-1023/absent` | 0.2037 | 0.2057 | +0.27% | -0.15% | +1.00% | +0.02% | +0.00% |
| `controls/needle-8/absent` | 1.0713 | 1.0709 | +0.03% | -0.05% | +0.04% | -0.04% | -0.00% |
| `controls/needle-8/origin` | 0.0152 | 0.0152 | +0.34% | -0.84% | +1.00% | +0.04% | +0.00% |
| `controls/needle-32/origin` | 0.0436 | 0.0496 | +13.55% | +10.34% | +17.64% | +14.06% | +0.52% |
| `controls/needle-64/absent` | 0.2762 | 0.2762 | +0.01% | +0.01% | +0.06% | +0.11% | +0.19% |
| `controls/needle-256/absent` † | 0.1244 | 0.1259 | +1.26% | -62.16% | +1.37% | +1.17% | +0.17% |
| `controls/prefix-9/absent` | 7.7817 | 7.7942 | +0.17% | +0.10% | +0.23% | +0.17% | -0.11% |
| `controls/prefix-31/absent` | 18.4485 | 19.1849 | +4.56% | +2.92% | +5.64% | +4.43% | -0.04% |
| `controls/prefix-64/absent` | 44.2876 | 70.3100 | +58.29% | +57.17% | +60.16% | +52.85% | +0.00% |

### Intel gcc14

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `moderation/short/en/absent` | 0.4674 | 0.4665 | +0.30% | -0.95% | +0.74% | +0.30% | -0.00% |
| `moderation/short/en/middle` | 0.2760 | 0.2766 | +0.20% | -0.52% | +1.18% | +0.58% | -0.00% |
| `moderation/short/ru/start` | 2.1258 | 2.1269 | +0.01% | -0.15% | +3.38% | +0.01% | -0.00% |
| `moderation/short/ru/middle` | 2.2909 | 2.2895 | +0.00% | -0.19% | +0.78% | -0.18% | +0.00% |
| `moderation/short/ru/end` | 2.5798 | 2.5787 | +0.01% | -0.20% | +0.09% | -0.17% | -0.00% |
| `moderation/short/zh/absent` | 0.5980 | 0.5988 | +0.13% | -0.74% | +1.26% | +0.22% | +0.00% |
| `moderation/short/zh/start` | 0.5041 | 0.5095 | +0.36% | +0.01% | +1.05% | +0.20% | -0.00% |
| `moderation/short/zh/middle` | 0.5018 | 0.5029 | +0.04% | -1.05% | +0.50% | +0.01% | +0.00% |
| `controls/length-16/middle` | 0.5382 | 0.5399 | +0.43% | -0.30% | +0.70% | -1.56% | -4.62% |
| `controls/length-16/end` | 0.9797 | 0.9823 | +0.10% | -1.04% | +0.70% | +2.79% | -2.59% |
| `controls/haystack-1023/absent` | 0.2027 | 0.2028 | +0.02% | -0.00% | +0.11% | +0.07% | -0.00% |
| `controls/needle-8/absent` | 1.0707 | 1.0708 | +0.02% | -0.04% | +0.03% | -0.10% | +0.00% |
| `controls/needle-8/origin` | 0.0147 | 0.0148 | +0.50% | -0.58% | +0.74% | -0.01% | -0.00% |
| `controls/needle-32/absent` | 0.6171 | 0.6232 | +0.99% | +0.44% | +2.06% | +1.25% | +0.14% |
| `controls/needle-64/absent` | 0.2760 | 0.2762 | +0.06% | +0.01% | +0.09% | +0.08% | +0.23% |
| `controls/needle-256/absent` | 0.1502 | 0.1521 | +1.33% | +0.97% | +1.51% | +1.01% | +0.21% |
| `controls/remaining-1023/absent` | 0.2763 | 0.2763 | +0.02% | -0.26% | +0.04% | -0.07% | -0.00% |
| `controls/prefix-64/absent` † | 48.4370 | 48.8958 | +1.65% | -14.68% | +3.42% | +0.16% | +0.00% |

### Intel clang18

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `moderation/short/en/absent` | 0.5082 | 0.5096 | +0.33% | -0.32% | +0.63% | -0.52% | -0.00% |
| `moderation/short/en/middle` | 0.3062 | 0.3070 | +0.11% | -0.57% | +0.51% | +0.17% | +0.00% |
| `moderation/short/en/end` | 0.3148 | 0.3150 | +0.32% | -0.23% | +0.70% | +0.03% | +0.00% |
| `moderation/short/ru/absent` | 2.9110 | 2.9134 | +0.03% | -0.04% | +0.19% | +0.37% | -0.00% |
| `moderation/short/ru/start` | 2.1179 | 2.1189 | +0.26% | -0.21% | +0.38% | +0.03% | -0.00% |
| `moderation/short/ru/middle` | 2.3470 | 2.3484 | +0.06% | -0.28% | +0.29% | -0.27% | +0.00% |
| `moderation/short/ru/end` | 2.5359 | 2.5365 | +0.04% | -0.12% | +0.17% | -0.15% | +0.00% |
| `moderation/short/zh/absent` | 0.6297 | 0.6311 | +0.22% | -0.65% | +1.15% | -0.25% | -0.00% |
| `controls/haystack-1023/absent` | 0.2029 | 0.2030 | +0.05% | -0.53% | +0.46% | -0.15% | +0.00% |
| `controls/haystack-1023/origin` | 0.0179 | 0.0179 | +0.07% | -0.74% | +0.93% | +1.10% | -0.00% |
| `controls/needle-8/absent` | 1.0671 | 1.0670 | +0.01% | -0.04% | +0.05% | +0.19% | -0.00% |
| `controls/needle-32/origin` | 0.0330 | 0.0404 | +22.23% | +15.76% | +24.07% | +25.64% | +0.17% |
| `controls/needle-64/absent` | 0.2701 | 0.2707 | +0.18% | +0.17% | +0.22% | +0.14% | +0.05% |
| `controls/remaining-1023/absent` | 0.2819 | 0.2825 | +0.46% | -0.45% | +0.80% | -0.32% | -0.00% |
| `controls/prefix-9/absent` | 7.7766 | 7.9589 | +2.34% | +2.25% | +2.38% | +2.53% | -3.15% |
| `controls/prefix-16/absent` | 9.8993 | 10.6713 | +7.62% | +7.27% | +8.46% | +10.12% | -1.90% |
| `controls/prefix-31/absent` | 18.7383 | 18.8037 | +0.34% | -1.57% | +2.11% | +4.21% | -1.03% |
| `controls/prefix-64/absent` | 38.6007 | 68.2967 | +76.27% | +72.90% | +78.55% | +53.32% | +0.00% |

### Intel clang20

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `moderation/short/en/absent` | 0.4491 | 0.4496 | +0.52% | -0.06% | +0.76% | +0.37% | +0.00% |
| `moderation/short/en/start` | 0.2438 | 0.2443 | +0.68% | -0.03% | +0.79% | +0.58% | -0.00% |
| `moderation/short/en/middle` | 0.2607 | 0.2608 | +0.03% | -0.82% | +0.95% | +0.49% | +0.00% |
| `moderation/short/en/end` | 0.2771 | 0.2770 | +0.28% | -0.52% | +2.03% | +0.10% | +0.00% |
| `moderation/short/ru/start` | 2.0742 | 2.0746 | +0.03% | -0.01% | +0.15% | -0.07% | -0.00% |
| `moderation/short/ru/end` | 2.5834 | 2.5839 | +0.03% | -0.01% | +0.26% | +0.04% | -0.00% |
| `moderation/short/zh/absent` | 0.5864 | 0.5869 | +0.09% | -0.25% | +0.84% | +0.47% | -0.00% |
| `moderation/short/zh/start` | 0.5013 | 0.5011 | +0.09% | -0.43% | +0.54% | +0.28% | -0.00% |
| `controls/haystack-1023/origin` | 0.0141 | 0.0141 | +0.22% | -0.16% | +0.98% | -1.11% | -0.00% |
| `controls/needle-8/origin` | 0.0137 | 0.0137 | +0.08% | -0.56% | +0.47% | +1.58% | +0.00% |
| `controls/needle-32/absent` | 0.5657 | 0.5670 | +0.25% | +0.17% | +0.33% | +0.27% | -16.02% |
| `controls/needle-64/absent` | 0.2690 | 0.2692 | +0.09% | +0.06% | +0.14% | +0.06% | -12.18% |
| `controls/remaining-1023/absent` | 0.2764 | 0.2770 | +0.19% | +0.09% | +0.99% | -0.29% | +0.00% |
