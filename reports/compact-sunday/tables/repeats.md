# Replication cohort

[Interpretation](../README.md). These fresh five-pair measurements supplement the primary cohort; they do not replace it. Selection: process spread >10%, sample MAD >5%, A/A median outside ±2%, or application median regression >3%. Two additional 64-byte prefix controls use the two-argument strpos call. Min/max are observed paired extrema. † marks remaining noise in the replication itself. The comparison column explicitly distinguishes master/compact A/B from master/master or compact/compact A/A; A and B times refer to those named sides.

## AMD gcc15

| Case | A / B | Primary Δ time | Repeat A µs | Repeat B µs | Repeat Δ time | Min Δ | Max Δ |
|---|---|---:|---:|---:|---:|---:|---:|
| `moderation/medium/ru/start` † | master / compact | -8.65% | 5.8244 | 5.3124 | -8.79% | -20.36% | -8.73% |
| `strstr/en/start` † | master / compact | -10.59% | 0.0752 | 0.0674 | -10.65% | -12.06% | -0.43% |
| `explode/en/start` | master / compact | -8.82% | 0.6900 | 0.6263 | -9.19% | -9.71% | -8.98% |
| `documents/search/support/present` | master / compact | -16.10% | 0.0689 | 0.0581 | -15.55% | -16.51% | -14.50% |
| `moderation/short/en/absent` | master / compact | -0.27% | 0.4352 | 0.4353 | +0.15% | -0.14% | +4.64% |
| `controls/length-16/absent` | master / compact | -9.80% | 0.7568 | 0.6866 | -8.89% | -10.38% | -8.45% |
| `controls/haystack-1024/absent` | master / compact | -10.76% | 0.2004 | 0.1806 | -9.91% | -11.10% | -8.84% |
| `controls/prefix-9/absent` | master / compact | -4.31% | 6.1822 | 6.0542 | -2.07% | -6.12% | +0.72% |
| `mb_stripos/ru/absent` † | master / compact | -0.70% | 10.6595 | 10.6149 | -0.44% | -33.24% | -0.27% |
| `mb_stristr/ru/absent` † | master / compact | -0.55% | 10.6533 | 10.5931 | -0.48% | -1.18% | +40.50% |
| `mb_stripos/zh/absent` † | master / compact | -0.35% | 9.5781 | 9.4913 | -0.91% | -30.17% | +0.43% |
| `mb_stripos/zh/middle` † | master / compact | -0.91% | 9.3151 | 9.2812 | -0.12% | -28.53% | +0.22% |
| `mb_stristr/zh/absent` | master / compact | -0.85% | 9.5116 | 9.4892 | +0.56% | -0.97% | +2.19% |
| `mb_stristr/zh/middle` | master / compact | +0.37% | 13.3462 | 13.3214 | -0.19% | -1.58% | +2.63% |
| `legacy-prefix/default-offset` | master / compact | separate call shape | 30.8288 | 40.2990 | +30.73% | +30.68% | +31.07% |

## AMD clang21

| Case | A / B | Primary Δ time | Repeat A µs | Repeat B µs | Repeat Δ time | Min Δ | Max Δ |
|---|---|---:|---:|---:|---:|---:|---:|
| `substr_count/en/absent` | master / master | +0.11% | 0.6863 | 0.6848 | -0.27% | -0.33% | +1.91% |
| `str_replace/en/repeated` | compact / compact | +2.11% | 1.1745 | 1.1657 | -0.44% | -6.46% | +1.81% |
| `moderation/medium/en/start` | master / compact | -10.24% | 6.1868 | 5.5404 | -10.47% | -10.75% | -10.09% |
| `strstr/en/absent` | master / compact | -10.41% | 0.6292 | 0.5640 | -10.54% | -10.67% | -10.17% |
| `strstr/en/end` | master / compact | -10.26% | 0.6478 | 0.5810 | -10.43% | -10.88% | -10.00% |
| `documents/search/receipt/absent` | master / compact | -10.84% | 0.3878 | 0.3459 | -10.79% | -10.93% | -10.70% |
| `documents/search/log_short/present` | master / compact | -8.86% | 0.3887 | 0.3551 | -8.65% | -9.18% | -8.39% |
| `documents/explode/mail_receipt/limit2` | master / compact | -10.22% | 0.1381 | 0.1281 | -8.92% | -10.63% | -6.65% |
| `controls/length-24/absent` | master / compact | -9.59% | 0.4655 | 0.4207 | -9.66% | -10.49% | -9.55% |
| `controls/length-31/middle` | master / compact | -10.30% | 0.2131 | 0.1900 | -11.19% | -11.92% | -10.00% |
| `controls/haystack-1024/origin` | master / compact | -24.52% | 0.0215 | 0.0160 | -25.19% | -28.95% | -19.28% |
| `controls/needle-32/origin` | master / compact | +8.55% | 0.0293 | 0.0315 | +7.69% | +6.79% | +8.55% |
| `mb_stripos/en/absent` | master / compact | -0.96% | 8.3254 | 8.2575 | -0.77% | -1.03% | -0.72% |
| `mb_stripos/en/middle` † | master / compact | -0.53% | 8.1054 | 8.0694 | -0.23% | -3.20% | +2.06% |
| `mb_strstr/en/absent` | master / compact | -10.89% | 0.9188 | 0.8199 | -10.84% | -10.94% | -10.66% |
| `mb_stristr/en/absent` † | master / compact | -0.92% | 8.3232 | 8.2501 | -0.89% | -1.06% | -0.86% |
| `mb_stristr/ru/absent` | master / compact | -0.38% | 10.4441 | 10.3983 | -0.37% | -4.37% | +2.38% |
| `mb_strstr/zh/absent` | master / compact | -11.11% | 0.8185 | 0.7269 | -11.20% | -11.41% | -11.09% |
| `legacy-prefix/default-offset` | master / compact | separate call shape | 40.2629 | 30.8226 | -23.46% | -23.52% | -23.26% |

## Intel gcc13

| Case | A / B | Primary Δ time | Repeat A µs | Repeat B µs | Repeat Δ time | Min Δ | Max Δ |
|---|---|---:|---:|---:|---:|---:|---:|
| `moderation/medium/zh/absent` | master / compact | -0.53% | 10.6365 | 10.5270 | -1.03% | -1.22% | -0.29% |
| `moderation/long/zh/end` | master / compact | +0.33% | 143.1456 | 143.1726 | +0.02% | -0.19% | +0.30% |
| `str_contains/en/start` | master / compact | -27.99% | 0.0407 | 0.0297 | -27.04% | -29.33% | -24.80% |
| `strtr/en/repeated` | master / compact | -3.00% | 1.2915 | 1.2962 | +0.31% | +0.14% | +1.21% |
| `explode/en/repeated` † | master / compact | -8.79% | 0.7291 | 0.6677 | -8.42% | -16.14% | -8.08% |
| `documents/search/log_short/present` | master / compact | -2.44% | 0.5114 | 0.5009 | -2.06% | -2.24% | -2.03% |
| `documents/replace/receipt/equal` | master / compact | -4.15% | 0.5091 | 0.4885 | -4.03% | -4.14% | -4.02% |
| `controls/needle-31/origin` | master / compact | -27.15% | 0.0417 | 0.0293 | -29.53% | -30.77% | -27.19% |
| `controls/needle-256/absent` | master / compact | +1.26% | 0.1245 | 0.1260 | +1.19% | +1.14% | +1.33% |

## Intel gcc14

| Case | A / B | Primary Δ time | Repeat A µs | Repeat B µs | Repeat Δ time | Min Δ | Max Δ |
|---|---|---:|---:|---:|---:|---:|---:|
| `strpos/en/start` | master / compact | -26.57% | 0.0300 | 0.0210 | -29.99% | -31.19% | -29.06% |
| `str_contains/en/start` | master / compact | -26.90% | 0.0435 | 0.0300 | -30.76% | -32.97% | -29.23% |
| `documents/search/log_short/present` | master / compact | -2.14% | 0.5116 | 0.5008 | -2.12% | -2.13% | -2.03% |
| `controls/needle-31/origin` † | master / compact | -21.64% | 0.0362 | 0.0277 | -23.37% | -23.67% | -19.76% |
| `controls/prefix-64/absent` | master / compact | +1.65% | 50.5080 | 48.9169 | -0.57% | -6.57% | +0.80% |

## Intel clang18

| Case | A / B | Primary Δ time | Repeat A µs | Repeat B µs | Repeat Δ time | Min Δ | Max Δ |
|---|---|---:|---:|---:|---:|---:|---:|
| `moderation/long/ru/absent` | master / compact | +4.12% | 281.1951 | 289.3257 | +2.92% | +2.85% | +3.19% |
| `moderation/long/ru/start` | master / compact | +4.72% | 182.2459 | 189.2779 | +3.82% | +3.74% | +3.90% |
| `moderation/long/ru/middle` | master / compact | +3.63% | 199.7417 | 207.1338 | +3.77% | +3.68% | +3.83% |
| `moderation/long/ru/end` | master / compact | +3.89% | 215.2996 | 223.1920 | +3.69% | +3.08% | +3.78% |
| `str_contains/en/middle` | master / compact | +0.81% | 0.4145 | 0.4199 | +1.24% | +0.80% | +1.66% |
| `substr_count/en/absent` | master / compact | -0.93% | 0.9315 | 0.9257 | -0.73% | -0.86% | +0.62% |
| `substr_count/en/repeated` | master / compact | -2.03% | 0.6214 | 0.6151 | -0.90% | -1.04% | -0.05% |
| `str_replace/en/repeated` | master / compact | -3.14% | 1.2917 | 1.2778 | -1.15% | -1.57% | -1.01% |
| `explode/en/end` | master / compact | -1.20% | 0.8487 | 0.8422 | -0.69% | -1.07% | -0.68% |
| `explode/en/repeated` | master / compact | -9.50% | 0.7409 | 0.6697 | -9.65% | -10.47% | -4.99% |
| `strpos/en/64k/end` | master / compact | -0.86% | 12.0143 | 11.9946 | -0.18% | -0.33% | -0.07% |
| `documents/ireplace/receipt/equal` | master / compact | -8.31% | 0.6504 | 0.5978 | -8.07% | -8.21% | -7.80% |
| `documents/stream/mail_delivery/closing` | master / compact | -0.98% | 0.7621 | 0.7556 | -0.87% | -0.96% | -0.82% |
| `documents/repeated/str_replace/23` | compact / compact | -0.04% | 6.8717 | 6.7895 | -0.77% | -1.73% | +0.71% |
| `mb_strstr/zh/middle` | master / compact | -0.56% | 5.2480 | 5.2354 | -0.19% | -0.25% | +0.19% |

## Intel clang20

| Case | A / B | Primary Δ time | Repeat A µs | Repeat B µs | Repeat Δ time | Min Δ | Max Δ |
|---|---|---:|---:|---:|---:|---:|---:|
| `moderation/medium/zh/middle` | master / compact | -2.22% | 6.7656 | 6.7310 | -0.52% | -0.66% | -0.28% |
| `explode/en/repeated` † | master / compact | -9.41% | 0.7366 | 0.6818 | -8.36% | -11.07% | +5.95% |
| `documents/search/log_long/absent` | master / compact | +0.69% | 15.0185 | 15.1118 | +0.66% | +0.43% | +0.78% |
| `documents/ireplace/receipt/shorter` | master / compact | +4.27% | 1.0836 | 1.1278 | +4.09% | +3.44% | +4.28% |
| `documents/ireplace/receipt/equal` | master / compact | +3.73% | 0.6164 | 0.6386 | +3.64% | +3.49% | +3.97% |
| `documents/ireplace/receipt/longer` | master / compact | +4.32% | 1.0841 | 1.1267 | +4.06% | +3.87% | +4.40% |
| `controls/haystack-1024/absent` | master / compact | -1.75% | 0.2145 | 0.2108 | -1.72% | -1.77% | -1.60% |
| `controls/needle-32/origin` † | master / compact | -13.17% | 0.0336 | 0.0296 | -11.53% | -18.10% | -8.41% |
