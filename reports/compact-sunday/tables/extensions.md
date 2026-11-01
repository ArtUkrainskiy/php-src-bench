# All extension cases

[Report and interpretation](../README.md). Primary cohort only; no substitution from repeats.

Negative = less elapsed time, cycles or instructions. Time is µs per whole PHP operation; min/max are paired observed extrema, not confidence limits. † flags sample MAD >5% or process spread >10%; see [replications](repeats.md).

Absolute counts for both sides are in [CPU counts](cpu.md). Native paired ranges are in [AMD](counters-amd.md), [Intel core](counters-intel.md) and [Intel extensions](counters-intel-extensions.md).

## mb_strpos

### AMD gcc15

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_strpos/en/absent` | 0.9836 | 0.8941 | -9.14% | -9.64% | -8.93% | -9.38% | -2.08% |
| `mb_strpos/en/middle` | 0.5685 | 0.5214 | -8.30% | -8.36% | -8.16% | -8.02% | -2.67% |
| `mb_strpos/ru/absent` | 0.9429 | 0.8611 | -8.65% | -9.21% | -8.49% | -8.28% | -1.82% |
| `mb_strpos/ru/middle` | 0.5478 | 0.5091 | -7.05% | -7.27% | -7.00% | -7.05% | -2.48% |
| `mb_strpos/zh/absent` | 0.8751 | 0.7922 | -9.45% | -9.59% | -9.28% | -9.65% | -2.23% |
| `mb_strpos/zh/middle` | 0.5227 | 0.4765 | -8.86% | -8.96% | -8.65% | -8.35% | -2.78% |

### AMD clang21

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_strpos/en/absent` | 0.9202 | 0.8213 | -10.74% | -10.90% | -10.71% | -11.10% | -0.66% |
| `mb_strpos/en/middle` | 0.5312 | 0.4821 | -9.28% | -9.79% | -9.16% | -9.51% | -0.86% |
| `mb_strpos/ru/absent` | 0.8978 | 0.7954 | -11.39% | -11.62% | -11.37% | -11.54% | -0.58% |
| `mb_strpos/ru/middle` | 0.5197 | 0.4711 | -9.35% | -9.91% | -9.07% | -9.47% | -0.80% |
| `mb_strpos/zh/absent` | 0.8175 | 0.7276 | -10.97% | -11.11% | -10.85% | -11.16% | -0.71% |
| `mb_strpos/zh/middle` | 0.4920 | 0.4436 | -9.82% | -9.97% | -9.70% | -10.36% | -0.90% |

### Intel gcc13

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_strpos/en/absent` | 1.2129 | 1.1954 | -1.47% | -1.51% | -1.27% | -1.50% | -2.19% |
| `mb_strpos/en/middle` | 0.7064 | 0.6999 | -0.89% | -1.03% | -0.86% | -1.23% | -2.77% |
| `mb_strpos/ru/absent` | 1.1784 | 1.1666 | -1.00% | -1.06% | -0.76% | -0.72% | -1.90% |
| `mb_strpos/ru/middle` | 0.6726 | 0.6667 | -0.88% | -1.08% | -0.78% | -1.02% | -2.55% |
| `mb_strpos/zh/absent` | 1.0907 | 1.0734 | -1.64% | -1.68% | -1.51% | -1.81% | -2.35% |
| `mb_strpos/zh/middle` | 0.6493 | 0.6554 | +0.85% | +0.80% | +1.20% | +0.68% | -2.88% |

### Intel gcc14

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_strpos/en/absent` | 1.2214 | 1.2152 | -0.51% | -0.67% | -0.07% | +0.38% | -2.06% |
| `mb_strpos/en/middle` | 0.7183 | 0.7101 | -1.12% | -1.45% | -0.87% | -1.21% | -2.66% |
| `mb_strpos/ru/absent` | 1.1804 | 1.1703 | -0.86% | -1.68% | -0.35% | -0.82% | -1.81% |
| `mb_strpos/ru/middle` | 0.6653 | 0.6676 | +0.37% | +0.26% | +0.45% | +0.40% | -2.46% |
| `mb_strpos/zh/absent` | 1.0984 | 1.0842 | -1.29% | -1.31% | -0.98% | -1.74% | -2.21% |
| `mb_strpos/zh/middle` | 0.6711 | 0.6618 | -1.28% | -1.47% | -1.19% | -1.40% | -2.77% |

### Intel clang18

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_strpos/en/absent` | 1.2218 | 1.2026 | -1.51% | -1.81% | -1.24% | -1.20% | -11.99% |
| `mb_strpos/en/middle` | 0.6764 | 0.6713 | -0.71% | -0.82% | -0.64% | -0.46% | -8.67% |
| `mb_strpos/ru/absent` | 1.2300 | 1.2204 | -0.79% | -0.85% | -0.69% | -0.76% | -10.28% |
| `mb_strpos/ru/middle` | 0.6644 | 0.6616 | -0.40% | -1.09% | -0.28% | -0.30% | -7.64% |
| `mb_strpos/zh/absent` | 1.1040 | 1.0866 | -1.62% | -2.39% | -1.56% | -1.68% | -11.65% |
| `mb_strpos/zh/middle` | 0.6195 | 0.6121 | -1.10% | -1.30% | -1.00% | -1.00% | -8.22% |

### Intel clang20

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_strpos/en/absent` | 1.2170 | 1.1984 | -1.53% | -1.82% | -1.09% | -1.69% | -12.09% |
| `mb_strpos/en/middle` | 0.6838 | 0.6806 | -0.46% | -0.50% | -0.35% | -0.40% | -8.76% |
| `mb_strpos/ru/absent` | 1.2260 | 1.2141 | -0.97% | -1.09% | +0.56% | -0.88% | -10.36% |
| `mb_strpos/ru/middle` | 0.6789 | 0.6714 | -1.10% | -1.44% | -0.93% | -1.67% | -7.71% |
| `mb_strpos/zh/absent` | 1.1005 | 1.0808 | -1.80% | -1.98% | -1.67% | -1.59% | -11.75% |
| `mb_strpos/zh/middle` | 0.6265 | 0.6211 | -0.86% | -2.37% | -0.77% | -0.94% | -8.32% |

## mb_stripos

### AMD gcc15

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_stripos/en/absent` | 11.1636 | 11.1093 | -0.61% | -0.65% | +1.76% | -1.35% | -0.08% |
| `mb_stripos/en/middle` | 10.9434 | 10.9239 | -0.17% | -0.33% | +2.19% | +0.42% | -0.08% |
| `mb_stripos/ru/absent` † | 10.7117 | 10.5992 | -0.70% | -32.16% | +0.32% | -1.02% | -0.07% |
| `mb_stripos/ru/middle` | 10.5275 | 10.5236 | -0.11% | -0.84% | +0.36% | -0.16% | -0.07% |
| `mb_stripos/zh/absent` † | 9.5170 | 9.4803 | -0.35% | -1.52% | +39.39% | -0.65% | -0.08% |
| `mb_stripos/zh/middle` † | 9.3687 | 9.2956 | -0.91% | -28.89% | +37.83% | -0.23% | -0.08% |

### AMD clang21

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_stripos/en/absent` † | 8.3214 | 8.2422 | -0.96% | -10.94% | +10.14% | -0.99% | -0.03% |
| `mb_stripos/en/middle` † | 8.1083 | 8.0652 | -0.53% | -10.59% | +1.71% | -0.61% | -0.03% |
| `mb_stripos/ru/absent` | 10.4437 | 10.4093 | -0.25% | -0.50% | +3.49% | -1.16% | -0.02% |
| `mb_stripos/ru/middle` | 10.3539 | 10.3278 | +0.98% | -4.18% | +3.59% | -0.81% | -0.02% |
| `mb_stripos/zh/absent` | 10.0151 | 9.9466 | -0.49% | -0.83% | +2.72% | -0.58% | -0.02% |
| `mb_stripos/zh/middle` | 9.7925 | 9.7686 | +0.00% | -0.33% | +3.32% | -0.40% | -0.02% |

### Intel gcc13

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_stripos/en/absent` | 10.1674 | 10.2028 | +0.61% | -3.08% | +0.85% | -0.26% | -0.08% |
| `mb_stripos/en/middle` | 10.2307 | 10.2443 | -0.07% | -0.49% | +1.60% | +0.81% | -0.08% |
| `mb_stripos/ru/absent` | 10.5439 | 10.5007 | -0.44% | -0.84% | +0.81% | +0.14% | -0.07% |
| `mb_stripos/ru/middle` | 10.3223 | 10.3007 | -0.29% | -0.49% | +0.32% | +0.87% | -0.07% |
| `mb_stripos/zh/absent` | 9.7142 | 9.6990 | -0.10% | -0.48% | +0.46% | -0.32% | -0.08% |
| `mb_stripos/zh/middle` | 9.6276 | 9.6525 | -0.40% | -1.42% | +0.67% | -0.92% | -0.08% |

### Intel gcc14

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_stripos/en/absent` | 9.8994 | 9.9021 | +0.19% | -1.03% | +0.33% | -0.53% | -0.08% |
| `mb_stripos/en/middle` | 10.2348 | 10.1936 | -0.27% | -1.33% | +0.49% | -0.61% | -0.08% |
| `mb_stripos/ru/absent` | 10.5131 | 10.5123 | +0.01% | -3.04% | +0.30% | -0.99% | -0.07% |
| `mb_stripos/ru/middle` | 10.3874 | 10.3480 | -0.28% | -0.59% | +0.10% | -0.05% | -0.07% |
| `mb_stripos/zh/absent` | 9.6677 | 9.6350 | -0.47% | -1.34% | -0.34% | +0.18% | -0.08% |
| `mb_stripos/zh/middle` | 9.4854 | 9.4841 | -0.23% | -0.52% | +0.56% | +0.68% | -0.08% |

### Intel clang18

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_stripos/en/absent` | 8.8263 | 8.8676 | +0.57% | -0.94% | +1.20% | +0.07% | -0.43% |
| `mb_stripos/en/middle` | 8.8984 | 8.9659 | +0.80% | -0.61% | +1.55% | +0.43% | -0.23% |
| `mb_stripos/ru/absent` | 8.9439 | 8.9222 | -0.15% | -1.14% | +0.23% | +0.20% | -0.27% |
| `mb_stripos/ru/middle` | 8.6062 | 8.5949 | -0.16% | -0.70% | -0.09% | +0.44% | -0.15% |
| `mb_stripos/zh/absent` | 9.0263 | 8.9936 | -0.17% | -0.60% | -0.04% | +0.56% | -0.30% |
| `mb_stripos/zh/middle` | 9.1296 | 9.1721 | +0.38% | -0.87% | +0.71% | -0.23% | -0.16% |

### Intel clang20

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_stripos/en/absent` | 8.9981 | 8.9452 | +0.23% | -0.77% | +5.08% | +0.66% | -0.43% |
| `mb_stripos/en/middle` | 8.8636 | 8.9056 | +0.54% | -0.36% | +3.08% | +0.20% | -0.23% |
| `mb_stripos/ru/absent` | 8.7727 | 8.7586 | -0.16% | -0.25% | +1.02% | -0.95% | -0.27% |
| `mb_stripos/ru/middle` | 8.5728 | 8.5429 | -0.15% | -0.76% | -0.01% | +0.60% | -0.14% |
| `mb_stripos/zh/absent` | 9.3483 | 9.3232 | -0.10% | -0.75% | +0.71% | -0.01% | -0.28% |
| `mb_stripos/zh/middle` | 9.1749 | 9.2349 | +0.01% | -0.16% | +0.88% | +0.75% | -0.15% |

## mb_strstr

### AMD gcc15

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_strstr/en/absent` | 0.9830 | 0.8925 | -9.20% | -9.56% | -8.89% | -9.41% | -2.07% |
| `mb_strstr/en/middle` | 3.3341 | 3.2830 | -1.51% | -1.72% | -0.62% | -1.18% | -0.21% |
| `mb_strstr/ru/absent` | 0.9422 | 0.8611 | -8.60% | -8.73% | -8.56% | -8.76% | -1.82% |
| `mb_strstr/ru/middle` | 4.3976 | 4.3637 | -0.71% | -1.52% | -0.25% | +0.27% | -0.17% |
| `mb_strstr/zh/absent` | 0.8735 | 0.7911 | -9.45% | -9.57% | -9.36% | -9.55% | -2.23% |
| `mb_strstr/zh/middle` | 4.5445 | 4.4686 | -1.63% | -2.99% | -1.02% | -1.02% | -0.16% |

### AMD clang21

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_strstr/en/absent` † | 0.9194 | 0.8194 | -10.89% | -21.97% | -10.69% | -10.58% | -0.66% |
| `mb_strstr/en/middle` | 4.1484 | 4.0943 | -1.33% | -1.36% | +0.04% | -1.27% | -0.06% |
| `mb_strstr/ru/absent` | 0.8975 | 0.7948 | -11.49% | -11.55% | -11.36% | -11.54% | -0.58% |
| `mb_strstr/ru/middle` | 4.8107 | 4.7716 | -0.96% | -1.38% | +1.95% | -1.13% | -0.05% |
| `mb_strstr/zh/absent` † | 0.8176 | 0.7271 | -11.11% | -24.68% | -10.98% | -11.22% | -0.71% |
| `mb_strstr/zh/middle` | 5.2759 | 5.2145 | -1.16% | -1.78% | -0.92% | -0.87% | -0.04% |

### Intel gcc13

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_strstr/en/absent` | 1.2108 | 1.1954 | -1.26% | -1.36% | -1.08% | -1.50% | -2.19% |
| `mb_strstr/en/middle` | 3.5245 | 3.5256 | +0.04% | -0.30% | +0.05% | +0.30% | -0.20% |
| `mb_strstr/ru/absent` | 1.1773 | 1.1652 | -1.03% | -1.21% | -0.76% | -0.80% | -1.90% |
| `mb_strstr/ru/middle` | 4.9330 | 4.9225 | +0.02% | -0.46% | +0.09% | -1.33% | -0.16% |
| `mb_strstr/zh/absent` | 1.0900 | 1.0752 | -1.46% | -2.39% | -1.09% | -1.49% | -2.35% |
| `mb_strstr/zh/middle` | 5.5712 | 5.5973 | +0.47% | -0.01% | +1.70% | +0.34% | -0.16% |

### Intel gcc14

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_strstr/en/absent` | 1.2149 | 1.2155 | -0.02% | -0.17% | +0.91% | +0.57% | -2.06% |
| `mb_strstr/en/middle` | 3.5088 | 3.5161 | +0.02% | -0.15% | +0.24% | -0.19% | -0.20% |
| `mb_strstr/ru/absent` | 1.1828 | 1.1695 | -1.05% | -1.80% | -0.90% | -0.97% | -1.81% |
| `mb_strstr/ru/middle` | 4.4725 | 4.4658 | -0.48% | -0.60% | +0.09% | -0.85% | -0.16% |
| `mb_strstr/zh/absent` | 1.0920 | 1.0768 | -1.37% | -1.49% | -1.24% | -1.51% | -2.21% |
| `mb_strstr/zh/middle` | 5.4765 | 5.4543 | -0.38% | -1.78% | +0.11% | -0.27% | -0.16% |

### Intel clang18

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_strstr/en/absent` | 1.2180 | 1.2021 | -1.30% | -1.33% | -0.96% | -1.20% | -11.98% |
| `mb_strstr/en/middle` | 3.7817 | 3.7788 | -0.11% | -0.33% | +0.16% | -0.32% | -0.61% |
| `mb_strstr/ru/absent` | 1.2318 | 1.2200 | -0.79% | -1.06% | -0.63% | -0.66% | -10.27% |
| `mb_strstr/ru/middle` | 4.8461 | 4.8700 | +0.64% | +0.15% | +5.16% | +1.03% | -0.49% |
| `mb_strstr/zh/absent` | 1.1041 | 1.0883 | -1.36% | -1.53% | -1.20% | -1.53% | -11.64% |
| `mb_strstr/zh/middle` † | 5.9400 | 5.9393 | -0.56% | -0.95% | +4.11% | -0.67% | -0.46% |

### Intel clang20

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_strstr/en/absent` | 1.2162 | 1.2005 | -1.29% | -1.41% | -1.18% | -2.06% | -12.07% |
| `mb_strstr/en/middle` | 3.8673 | 3.8627 | -0.00% | -1.99% | +0.88% | -0.40% | -0.61% |
| `mb_strstr/ru/absent` | 1.2254 | 1.2152 | -0.83% | -0.97% | -0.60% | -0.71% | -10.35% |
| `mb_strstr/ru/middle` | 4.6670 | 4.6730 | -0.03% | -0.67% | +0.39% | +0.08% | -0.49% |
| `mb_strstr/zh/absent` | 1.1002 | 1.0841 | -1.37% | -1.74% | -1.22% | -1.65% | -11.73% |
| `mb_strstr/zh/middle` | 6.4947 | 6.5736 | +1.66% | -0.02% | +3.20% | +0.50% | -0.41% |

## mb_stristr

### AMD gcc15

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_stristr/en/absent` | 11.1768 | 11.1008 | -0.60% | -2.60% | -0.01% | -0.62% | -0.08% |
| `mb_stristr/en/middle` | 13.7096 | 13.6981 | -0.07% | -0.17% | -0.01% | -0.12% | -0.06% |
| `mb_stristr/ru/absent` † | 10.6700 | 10.6066 | -0.55% | -32.97% | +48.19% | +0.14% | -0.07% |
| `mb_stristr/ru/middle` | 14.6292 | 14.6277 | +0.52% | -0.13% | +1.16% | +0.05% | -0.05% |
| `mb_stristr/zh/absent` † | 9.5196 | 9.4653 | -0.85% | -29.71% | -0.25% | -1.08% | -0.08% |
| `mb_stristr/zh/middle` † | 13.3924 | 13.3446 | +0.37% | -1.17% | +28.53% | -0.15% | -0.05% |

### AMD clang21

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_stristr/en/absent` † | 8.3272 | 8.2508 | -0.92% | -5.14% | +10.31% | -1.26% | -0.03% |
| `mb_stristr/en/middle` | 11.7568 | 11.7072 | -0.28% | -2.10% | +1.28% | -0.82% | -0.02% |
| `mb_stristr/ru/absent` † | 10.4099 | 10.3805 | -0.38% | -4.34% | +10.25% | -0.44% | -0.02% |
| `mb_stristr/ru/middle` | 14.3939 | 14.7068 | +2.17% | -0.31% | +2.57% | -0.85% | -0.02% |
| `mb_stristr/zh/absent` | 10.0220 | 9.9546 | -0.67% | -4.01% | +2.90% | -0.45% | -0.02% |
| `mb_stristr/zh/middle` | 14.5902 | 14.5349 | -0.33% | -2.66% | +2.38% | -0.23% | -0.02% |

### Intel gcc13

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_stristr/en/absent` | 9.4898 | 9.5278 | +0.36% | +0.16% | +0.91% | +0.38% | -0.08% |
| `mb_stristr/en/middle` | 12.1266 | 12.1005 | -0.21% | -0.61% | +0.19% | +0.66% | -0.06% |
| `mb_stristr/ru/absent` | 10.5168 | 10.5279 | -0.06% | -0.53% | +0.12% | +1.15% | -0.07% |
| `mb_stristr/ru/middle` | 14.4345 | 14.0414 | +0.18% | -3.93% | +1.99% | +0.42% | -0.05% |
| `mb_stristr/zh/absent` | 11.2119 | 11.2356 | -0.49% | -0.71% | +1.23% | -0.24% | -0.08% |
| `mb_stristr/zh/middle` | 16.2183 | 16.2241 | -0.44% | -1.16% | +0.30% | -0.10% | -0.05% |

### Intel gcc14

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_stristr/en/absent` | 9.6012 | 9.5759 | -0.28% | -0.69% | +0.15% | -0.13% | -0.08% |
| `mb_stristr/en/middle` | 12.2183 | 12.1891 | -0.29% | -0.54% | -0.07% | +0.17% | -0.06% |
| `mb_stristr/ru/absent` | 10.5323 | 10.4864 | -0.36% | -3.12% | +0.55% | +0.28% | -0.07% |
| `mb_stristr/ru/middle` | 14.1467 | 14.1887 | -0.01% | -1.27% | +0.63% | +0.03% | -0.05% |
| `mb_stristr/zh/absent` | 11.2300 | 11.3713 | +1.06% | -1.29% | +4.85% | +0.30% | -0.08% |
| `mb_stristr/zh/middle` | 16.1364 | 16.0195 | -0.20% | -0.94% | +1.69% | +0.23% | -0.05% |

### Intel clang18

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_stristr/en/absent` | 8.2811 | 8.2972 | +0.14% | -0.29% | +0.42% | +0.49% | -0.43% |
| `mb_stristr/en/middle` | 10.9312 | 10.9645 | +0.30% | +0.25% | +0.74% | +0.43% | -0.16% |
| `mb_stristr/ru/absent` | 8.9515 | 8.8994 | -0.36% | -2.34% | +0.18% | +0.94% | -0.27% |
| `mb_stristr/ru/middle` | 13.0158 | 12.9655 | -0.25% | -0.93% | +1.05% | -1.02% | -0.10% |
| `mb_stristr/zh/absent` | 10.5078 | 10.5266 | +0.18% | -7.28% | +0.54% | -0.15% | -0.30% |
| `mb_stristr/zh/middle` | 15.8402 | 15.8077 | -0.65% | -1.34% | -0.21% | +0.00% | -0.11% |

### Intel clang20

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_stristr/en/absent` | 8.4556 | 8.4609 | -0.01% | -0.17% | +0.23% | +0.65% | -0.43% |
| `mb_stristr/en/middle` | 11.2986 | 11.2794 | -0.24% | -2.35% | -0.15% | -0.07% | -0.16% |
| `mb_stristr/ru/absent` | 8.7665 | 8.7506 | +0.03% | -2.41% | +2.55% | +0.71% | -0.27% |
| `mb_stristr/ru/middle` | 12.8140 | 12.7548 | -0.44% | -1.04% | +3.59% | -0.96% | -0.10% |
| `mb_stristr/zh/absent` | 10.6988 | 10.7358 | +0.38% | -0.62% | +0.92% | +0.19% | -0.28% |
| `mb_stristr/zh/middle` | 16.9697 | 16.9251 | -0.18% | -2.44% | +1.15% | +0.12% | -0.10% |

## mb_substr_count

### AMD gcc15

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_substr_count/en/absent` | 1.0027 | 0.9112 | -9.14% | -9.21% | -9.05% | -9.24% | -1.95% |
| `mb_substr_count/en/middle` | 1.0193 | 0.9178 | -9.88% | -9.98% | -9.60% | -9.64% | -3.69% |
| `mb_substr_count/ru/absent` | 0.9763 | 0.8959 | -8.23% | -8.35% | -8.15% | -8.73% | -1.66% |
| `mb_substr_count/ru/middle` | 1.0025 | 0.9195 | -8.24% | -8.57% | -8.08% | -8.29% | -3.12% |
| `mb_substr_count/zh/absent` | 0.8943 | 0.8100 | -9.42% | -9.83% | -9.21% | -9.45% | -2.07% |
| `mb_substr_count/zh/middle` | 0.9110 | 0.8215 | -9.89% | -10.97% | -9.56% | -9.88% | -3.92% |

### AMD clang21

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_substr_count/en/absent` | 0.9373 | 0.8412 | -10.32% | -10.62% | -10.19% | -10.69% | -0.62% |
| `mb_substr_count/en/middle` | 0.9509 | 0.8490 | -10.74% | -10.96% | -10.59% | -11.04% | -1.19% |
| `mb_substr_count/ru/absent` | 0.9313 | 0.8267 | -11.26% | -11.33% | -11.18% | -11.25% | -0.52% |
| `mb_substr_count/ru/middle` | 0.9543 | 0.8513 | -10.78% | -10.94% | -10.71% | -10.57% | -1.00% |
| `mb_substr_count/zh/absent` | 0.8394 | 0.7506 | -10.57% | -10.69% | -10.42% | -10.58% | -0.65% |
| `mb_substr_count/zh/middle` | 0.8552 | 0.7612 | -11.02% | -11.37% | -10.88% | -11.21% | -1.26% |

### Intel gcc13

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_substr_count/en/absent` | 1.2287 | 1.2204 | -0.64% | -0.91% | -0.45% | -0.40% | -2.05% |
| `mb_substr_count/en/middle` | 1.2383 | 1.2306 | -0.66% | -0.71% | -0.54% | -0.62% | -3.87% |
| `mb_substr_count/ru/absent` | 1.2072 | 1.1996 | -0.61% | -0.80% | -0.31% | -0.31% | -1.72% |
| `mb_substr_count/ru/middle` | 1.2131 | 1.2054 | -0.64% | -0.72% | -0.39% | -0.42% | -3.24% |
| `mb_substr_count/zh/absent` | 1.1109 | 1.1032 | -0.60% | -0.83% | -0.41% | -0.93% | -2.17% |
| `mb_substr_count/zh/middle` | 1.1150 | 1.1075 | -0.66% | -1.22% | -0.42% | -0.58% | -4.09% |

### Intel gcc14

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_substr_count/en/absent` | 1.2322 | 1.2427 | +0.73% | +0.59% | +0.95% | +0.62% | -1.94% |
| `mb_substr_count/en/middle` | 1.2422 | 1.2387 | -0.37% | -0.61% | +0.08% | -0.98% | -3.66% |
| `mb_substr_count/ru/absent` | 1.2264 | 1.2071 | -1.58% | -2.53% | -1.16% | -2.24% | -1.64% |
| `mb_substr_count/ru/middle` | 1.2355 | 1.2113 | -1.96% | -2.09% | -0.78% | -2.27% | -3.09% |
| `mb_substr_count/zh/absent` | 1.1174 | 1.1166 | -1.14% | -1.18% | -0.04% | -1.62% | -2.05% |
| `mb_substr_count/zh/middle` | 1.1184 | 1.1091 | -0.88% | -0.93% | -0.42% | -0.91% | -3.88% |

### Intel clang18

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_substr_count/en/absent` | 1.2349 | 1.2286 | -0.57% | -0.66% | -0.27% | -0.16% | -11.32% |
| `mb_substr_count/en/middle` | 1.2426 | 1.2365 | -0.49% | -0.59% | -0.33% | -0.57% | -11.55% |
| `mb_substr_count/ru/absent` | 1.2569 | 1.2519 | -0.40% | -0.53% | +0.28% | -0.47% | -9.41% |
| `mb_substr_count/ru/middle` | 1.2611 | 1.2559 | -0.41% | -5.36% | -0.30% | -0.40% | -9.53% |
| `mb_substr_count/zh/absent` | 1.1185 | 1.1122 | -0.56% | -0.73% | -0.49% | -0.59% | -10.84% |
| `mb_substr_count/zh/middle` | 1.1232 | 1.1170 | -0.60% | -0.69% | -0.39% | +0.13% | -11.12% |

### Intel clang20

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mb_substr_count/en/absent` | 1.2325 | 1.2275 | -0.43% | -0.52% | -0.07% | -0.41% | -11.39% |
| `mb_substr_count/en/middle` | 1.2409 | 1.2387 | -0.20% | -0.25% | -0.02% | -0.52% | -11.62% |
| `mb_substr_count/ru/absent` | 1.2564 | 1.2520 | -0.38% | -3.10% | -0.18% | +0.17% | -9.46% |
| `mb_substr_count/ru/middle` | 1.2585 | 1.2546 | -0.35% | -2.92% | -0.24% | -0.50% | -9.58% |
| `mb_substr_count/zh/absent` | 1.1311 | 1.1137 | -0.51% | -1.94% | -0.03% | -0.31% | -10.87% |
| `mb_substr_count/zh/middle` | 1.1259 | 1.1186 | -0.61% | -0.84% | -0.41% | -0.83% | -11.14% |

## grapheme_strpos

### AMD gcc15

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `grapheme_strpos/en/absent` | 2.2792 | 2.2313 | -2.10% | -2.33% | -1.62% | -1.66% | -0.38% |
| `grapheme_strpos/en/start` | 1.6165 | 1.6111 | -0.33% | -0.37% | -0.03% | -0.07% | -0.42% |
| `grapheme_strpos/en/middle` | 1.9107 | 1.8801 | -1.69% | -2.11% | -1.47% | -1.65% | -0.40% |
| `grapheme_strpos/en/end` | 2.2036 | 2.1471 | -2.40% | -4.50% | -2.29% | -2.69% | -0.38% |

### AMD clang21

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `grapheme_strpos/en/absent` | 1.9884 | 1.9408 | -2.22% | -9.34% | -1.81% | -1.13% | -0.10% |
| `grapheme_strpos/en/start` | 1.3626 | 1.3536 | -0.66% | -0.87% | -0.41% | -0.30% | -0.11% |
| `grapheme_strpos/en/middle` | 1.6347 | 1.6044 | -1.85% | -2.20% | -1.64% | -2.10% | -0.11% |
| `grapheme_strpos/en/end` | 1.9040 | 1.8472 | -2.99% | -3.13% | -2.82% | -3.58% | -0.10% |

### Intel gcc13

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `grapheme_strpos/en/absent` | 3.0265 | 3.0253 | -0.08% | -0.28% | +0.18% | +0.27% | -0.38% |
| `grapheme_strpos/en/start` | 2.3538 | 2.3466 | -0.27% | -0.61% | +0.17% | -0.56% | -0.42% |
| `grapheme_strpos/en/middle` | 2.6489 | 2.6042 | -1.59% | -2.10% | +1.47% | -0.54% | -0.40% |
| `grapheme_strpos/en/end` | 3.0465 | 3.0273 | -0.81% | -1.38% | -0.30% | -0.71% | -0.38% |

### Intel gcc14

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `grapheme_strpos/en/absent` | 3.0542 | 3.0559 | +0.03% | -0.79% | +0.63% | -0.03% | -0.38% |
| `grapheme_strpos/en/start` | 2.3560 | 2.3460 | -0.38% | -0.64% | +1.09% | -0.33% | -0.42% |
| `grapheme_strpos/en/middle` | 2.6814 | 2.6513 | -1.21% | -2.41% | +1.20% | +0.27% | -0.40% |
| `grapheme_strpos/en/end` | 3.0495 | 3.0374 | -0.17% | -1.05% | +0.20% | -1.02% | -0.37% |

### Intel clang18

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `grapheme_strpos/en/absent` | 2.4073 | 2.4054 | -0.10% | -0.25% | +0.27% | +0.95% | -1.31% |
| `grapheme_strpos/en/start` | 1.6874 | 1.6826 | -0.28% | -0.37% | +1.08% | +0.47% | -0.13% |
| `grapheme_strpos/en/middle` | 2.0508 | 2.0453 | -0.25% | -0.65% | -0.17% | -0.24% | -0.76% |
| `grapheme_strpos/en/end` | 2.4200 | 2.4172 | -0.14% | -0.29% | +0.42% | -0.53% | -1.32% |

### Intel clang20

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `grapheme_strpos/en/absent` | 2.7002 | 2.6638 | +0.12% | -4.39% | +2.06% | -3.51% | -1.32% |
| `grapheme_strpos/en/start` | 1.6816 | 1.6824 | +0.05% | -1.08% | +0.19% | -0.27% | -0.13% |
| `grapheme_strpos/en/middle` | 2.3169 | 2.3157 | +0.72% | -1.29% | +3.18% | +1.07% | -0.76% |
| `grapheme_strpos/en/end` | 2.7248 | 2.7292 | -0.42% | -0.56% | +2.01% | -0.61% | -1.32% |

## grapheme_stripos

### AMD gcc15

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `grapheme_stripos/en/absent` | 2.4759 | 2.4076 | -2.86% | -3.01% | -2.74% | -3.58% | -0.34% |
| `grapheme_stripos/en/start` | 1.7939 | 1.7859 | -0.43% | -0.65% | -0.04% | -0.77% | -0.38% |
| `grapheme_stripos/en/middle` | 2.0818 | 2.0500 | -1.52% | -1.64% | -0.95% | -1.46% | -0.36% |
| `grapheme_stripos/en/end` | 2.3763 | 2.3214 | -2.41% | -2.52% | -2.13% | -2.09% | -0.34% |

### AMD clang21

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `grapheme_stripos/en/absent` | 2.1957 | 2.1146 | -3.70% | -4.17% | -3.33% | -3.56% | -0.09% |
| `grapheme_stripos/en/start` | 1.5399 | 1.5299 | -0.52% | -0.78% | -0.43% | -1.48% | -0.10% |
| `grapheme_stripos/en/middle` | 1.8097 | 1.7779 | -1.73% | -1.89% | -1.62% | -1.69% | -0.10% |
| `grapheme_stripos/en/end` | 2.0790 | 2.0216 | -2.75% | -2.88% | -2.71% | -2.78% | -0.09% |

### Intel gcc13

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `grapheme_stripos/en/absent` | 3.2572 | 3.2505 | -0.24% | -0.42% | +0.02% | -0.41% | -0.35% |
| `grapheme_stripos/en/start` | 2.5446 | 2.5362 | -0.27% | -1.10% | +0.22% | +0.46% | -0.38% |
| `grapheme_stripos/en/middle` | 2.8445 | 2.8298 | -0.38% | -0.84% | -0.11% | -0.46% | -0.36% |
| `grapheme_stripos/en/end` | 3.2107 | 3.2105 | -0.17% | -0.78% | +0.32% | -0.75% | -0.35% |

### Intel gcc14

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `grapheme_stripos/en/absent` | 3.2609 | 3.2570 | -0.07% | -0.45% | +0.45% | +1.13% | -0.35% |
| `grapheme_stripos/en/start` | 2.5524 | 2.5423 | -0.44% | -2.75% | -0.23% | -0.65% | -0.38% |
| `grapheme_stripos/en/middle` | 2.8679 | 2.8746 | +0.57% | -0.56% | +1.54% | +0.40% | -0.36% |
| `grapheme_stripos/en/end` | 3.2327 | 3.2673 | +0.74% | +0.03% | +1.81% | +2.10% | -0.34% |

### Intel clang18

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `grapheme_stripos/en/absent` | 2.6244 | 2.6198 | -0.23% | -2.64% | +0.12% | -0.52% | -1.21% |
| `grapheme_stripos/en/start` | 1.9079 | 1.9066 | -0.15% | -0.40% | +0.13% | -1.11% | -0.12% |
| `grapheme_stripos/en/middle` | 2.2614 | 2.2667 | +0.10% | -0.10% | +0.65% | -0.82% | -0.70% |
| `grapheme_stripos/en/end` | 2.6432 | 2.6372 | -0.23% | -3.23% | +0.71% | -1.05% | -1.22% |

### Intel clang20

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `grapheme_stripos/en/absent` | 2.8706 | 2.8923 | +0.53% | -0.64% | +1.78% | +2.29% | -1.21% |
| `grapheme_stripos/en/start` | 2.0070 | 2.0200 | -0.05% | -2.19% | +3.02% | +1.05% | -0.12% |
| `grapheme_stripos/en/middle` | 2.5140 | 2.4984 | +0.27% | -2.81% | +1.97% | +0.74% | -0.70% |
| `grapheme_stripos/en/end` | 2.8233 | 2.8407 | +0.82% | -1.94% | +1.27% | -1.22% | -1.22% |

## grapheme_strstr

### AMD gcc15

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `grapheme_strstr/en/absent` | 2.1882 | 2.1341 | -2.48% | -2.60% | -2.09% | -2.66% | -0.38% |
| `grapheme_strstr/en/start` | 1.6678 | 1.6633 | -0.34% | -0.59% | -0.14% | -0.43% | -0.41% |
| `grapheme_strstr/en/middle` | 1.9432 | 1.9148 | -1.55% | -1.61% | -1.38% | -1.65% | -0.39% |
| `grapheme_strstr/en/end` | 2.2142 | 2.1602 | -2.42% | -2.64% | -2.05% | -2.61% | -0.37% |

### AMD clang21

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `grapheme_strstr/en/absent` | 1.9020 | 1.8419 | -3.16% | -3.20% | -3.06% | -2.36% | -0.10% |
| `grapheme_strstr/en/start` | 1.4186 | 1.4113 | -0.56% | -0.63% | -0.03% | +0.07% | -0.11% |
| `grapheme_strstr/en/middle` | 1.6681 | 1.6377 | -1.77% | -1.91% | -1.67% | -1.27% | -0.10% |
| `grapheme_strstr/en/end` | 1.9223 | 1.8620 | -3.14% | -3.40% | -2.68% | -3.52% | -0.10% |

### Intel gcc13

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `grapheme_strstr/en/absent` | 3.0738 | 3.0471 | -0.95% | -1.87% | -0.16% | -1.02% | -0.38% |
| `grapheme_strstr/en/start` | 2.4198 | 2.4087 | -0.89% | -1.13% | -0.32% | -0.17% | -0.41% |
| `grapheme_strstr/en/middle` | 2.8479 | 2.8167 | -0.79% | -1.57% | -0.68% | -1.43% | -0.39% |
| `grapheme_strstr/en/end` | 3.2765 | 3.2323 | -1.16% | -2.00% | -0.18% | -1.88% | -0.37% |

### Intel gcc14

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `grapheme_strstr/en/absent` | 3.0864 | 3.0744 | -0.11% | -1.16% | +0.61% | +0.76% | -0.38% |
| `grapheme_strstr/en/start` | 2.4317 | 2.4211 | -0.27% | -1.11% | +0.33% | -0.93% | -0.42% |
| `grapheme_strstr/en/middle` | 2.7627 | 2.7403 | +0.00% | -1.74% | +0.48% | -0.23% | -0.39% |
| `grapheme_strstr/en/end` | 3.1918 | 3.1825 | -0.13% | -0.53% | +0.89% | +1.24% | -0.37% |

### Intel clang18

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `grapheme_strstr/en/absent` | 2.3973 | 2.3946 | -0.29% | -1.15% | +0.06% | -0.28% | -1.31% |
| `grapheme_strstr/en/start` | 1.7431 | 1.7395 | -0.20% | -0.31% | -0.15% | -0.52% | -0.13% |
| `grapheme_strstr/en/middle` | 2.1708 | 2.1589 | -0.61% | -2.81% | -0.18% | +0.47% | -0.75% |
| `grapheme_strstr/en/end` | 2.5404 | 2.5159 | -0.68% | -1.52% | +0.15% | -0.38% | -1.31% |

### Intel clang20

| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `grapheme_strstr/en/absent` | 2.8649 | 2.8799 | -0.47% | -1.23% | +2.30% | +0.01% | -1.32% |
| `grapheme_strstr/en/start` | 1.7437 | 1.7443 | +0.03% | -0.46% | +0.24% | -0.87% | -0.13% |
| `grapheme_strstr/en/middle` | 2.5221 | 2.5983 | +1.95% | +0.24% | +8.16% | +2.08% | -0.75% |
| `grapheme_strstr/en/end` | 3.0164 | 3.0824 | +1.16% | -0.12% | +3.02% | -0.13% | -1.31% |
