# Supplemental route measurements

Negative deltas mean that B costs less than A. Elapsed time is primary; counters are diagnostic.

## gcc15: ca89 → No gram4

| Case | A, µs | B, µs | Δ time | Δ cycles | Δ instr. | Spread A/B | Result |
|---|--:|--:|--:|--:|--:|--:|---|
| banlist12/en/post/clean | 2.6764 | 2.6791 | +0.10% | -0.00% | +0.09% | 0.2% / 0.2% | Unclear |
| banlist12/en/post/early | 0.0341 | 0.0338 | -0.81% | -0.51% | +0.00% | 0.6% / 1.1% | Unclear |
| explode/colon2/4k | 2.4950 | 2.5095 | +0.58% | -1.05% | +0.00% | 0.6% / 0.6% | Unclear |
| substr-count/colon2/4k | 1.0256 | 1.0257 | +0.00% | -0.01% | +0.00% | 0.0% / 0.1% | Unclear |
| str-replace/colon2/4k | 3.0940 | 3.0838 | -0.33% | -0.07% | +0.00% | 0.3% / 0.1% | Unclear |
| render-template/4k | 5.9937 | 5.9755 | -0.30% | -0.21% | +0.30% | 0.1% / 0.7% | Unclear |
| route/gram/selective/absent | 3.4371 | 2.5461 | -25.92% | -26.13% | -24.96% | 0.0% / 0.0% | Faster |
| route/gram/selective/late | 3.4398 | 2.6754 | -22.22% | -22.23% | -23.89% | 0.1% / 0.0% | Faster |
| route/gram/dense/absent | 2.8483 | 2.7111 | -4.82% | -5.04% | -4.39% | 0.0% / 0.0% | Faster |
| route/gram/changing/absent | 15.6866 | 10.1882 | -35.05% | -35.17% | -29.63% | 0.0% / 0.1% | Faster |
| route/twoway/periodic-memory | 26.2659 | 26.0653 | -0.76% | -2.59% | -0.44% | 1.0% / 1.1% | Unclear |
| gram-periodic/ascii/absent | 12.2889 | 31.3527 | +155.13% | +153.86% | +238.50% | 0.1% / 0.1% | Slower |
| gram-periodic/dna/absent | 12.2599 | 43.6577 | +256.10% | +254.57% | +370.11% | 0.0% / 0.0% | Slower |

## gcc15: ca89 → Scalar

| Case | A, µs | B, µs | Δ time | Δ cycles | Δ instr. | Spread A/B | Result |
|---|--:|--:|--:|--:|--:|--:|---|
| banlist12/en/post/clean | 2.6772 | 2.6931 | +0.59% | +0.41% | +0.00% | 0.3% / 0.1% | Unclear |
| banlist12/en/post/early | 0.0342 | 0.0341 | -0.31% | +1.08% | +0.00% | 1.3% / 2.4% | Unclear |
| explode/colon2/4k | 2.5130 | 2.4860 | -1.07% | -0.58% | +0.00% | 0.6% / 0.1% | Faster |
| substr-count/colon2/4k | 1.0257 | 1.0266 | +0.09% | -0.51% | +0.00% | 0.1% / 0.1% | Unclear |
| str-replace/colon2/4k | 3.0968 | 3.0924 | -0.14% | +0.27% | -0.00% | 0.3% / 0.3% | Unclear |
| render-template/4k | 5.9970 | 5.8821 | -1.92% | -1.17% | +0.00% | 0.3% / 0.4% | Faster |
| route/pair/ascii/absent | 0.8871 | 10.8806 | +1126.60% | +1137.20% | +1379.86% | 0.0% / 0.0% | Slower |
| route/pair/dna/absent | 0.8867 | 10.8771 | +1126.75% | +1141.45% | +1379.86% | 0.0% / 0.0% | Slower |
| route/pair/binary/absent | 0.8799 | 10.8754 | +1136.03% | +1151.70% | +1384.56% | 0.1% / 0.0% | Slower |
| route/gram/selective/absent | 3.4385 | 1.0030 | -70.83% | -70.29% | -64.36% | 0.0% / 0.1% | Faster |
| route/gram/selective/late | 3.4402 | 1.1368 | -66.95% | -66.50% | -63.33% | 0.1% / 0.0% | Faster |
| route/gram/dense/absent | 2.8495 | 1.2297 | -56.85% | -56.34% | -47.96% | 0.0% / 0.1% | Faster |
| route/gram/changing/absent | 15.6907 | 4.1333 | -73.66% | -73.14% | -65.03% | 0.0% / 0.0% | Faster |
| route/twoway/periodic-memory | 25.7742 | 21.8452 | -15.24% | -14.14% | -13.21% | 1.2% / 3.8% | Faster |
| route/threshold/8191 | 34.1475 | 34.1089 | -0.11% | +0.61% | -0.00% | 0.3% / 0.5% | Unclear |
| route/threshold/8192 | 0.5505 | 5.5334 | +905.16% | +910.79% | +1092.78% | 0.1% / 0.0% | Slower |
| gram-periodic/ascii/absent | 12.2885 | 28.6098 | +132.82% | +132.04% | +232.63% | 0.1% / 0.0% | Slower |
| gram-periodic/dna/absent | 12.2551 | 42.7565 | +248.89% | +246.81% | +383.21% | 0.0% / 0.0% | Slower |

## clang21: ca89 → No gram4

| Case | A, µs | B, µs | Δ time | Δ cycles | Δ instr. | Spread A/B | Result |
|---|--:|--:|--:|--:|--:|--:|---|
| banlist12/en/post/clean | 2.5426 | 2.5422 | -0.02% | +0.03% | -0.00% | 0.1% / 0.2% | Unclear |
| banlist12/en/post/early | 0.0334 | 0.0331 | -0.97% | +1.10% | +0.00% | 2.3% / 1.5% | Unclear |
| explode/colon2/4k | 2.7111 | 2.7310 | +0.74% | -0.51% | -0.00% | 0.2% / 0.8% | Unclear |
| substr-count/colon2/4k | 1.0461 | 1.0627 | +1.59% | -0.12% | +0.00% | 2.4% / 0.2% | Unclear |
| str-replace/colon2/4k | 3.1451 | 3.1263 | -0.60% | -0.17% | +0.00% | 1.8% / 1.6% | Unclear |
| render-template/4k | 5.5863 | 5.5703 | -0.29% | +0.62% | -0.00% | 0.4% / 0.6% | Unclear |
| route/gram/selective/absent | 3.4753 | 2.4778 | -28.70% | -30.72% | -35.68% | 0.0% / 0.2% | Faster |
| route/gram/selective/late | 3.5855 | 2.4744 | -30.99% | -30.01% | -34.69% | 0.1% / 2.4% | Faster |
| route/gram/dense/absent | 2.8753 | 2.8008 | -2.59% | -2.55% | -3.13% | 0.2% / 0.1% | Unclear |
| route/gram/changing/absent | 16.3126 | 10.3551 | -36.52% | -35.32% | -31.87% | 0.0% / 2.4% | Faster |
| route/twoway/periodic-memory | 23.2887 | 22.9036 | -1.65% | -0.05% | -0.30% | 0.3% / 0.7% | Unclear |
| gram-periodic/ascii/absent | 12.7708 | 34.0430 | +166.57% | +167.89% | +208.30% | 0.0% / 0.5% | Slower |
| gram-periodic/dna/absent | 12.5136 | 43.2905 | +245.95% | +251.81% | +325.11% | 2.6% / 0.0% | Slower |

## clang21: ca89 → Scalar

| Case | A, µs | B, µs | Δ time | Δ cycles | Δ instr. | Spread A/B | Result |
|---|--:|--:|--:|--:|--:|--:|---|
| banlist12/en/post/clean | 2.5380 | 2.5352 | -0.11% | -0.54% | -0.00% | 0.2% / 0.0% | Unclear |
| banlist12/en/post/early | 0.0327 | 0.0326 | -0.52% | +0.91% | -0.00% | 0.8% / 2.9% | Noise |
| explode/colon2/4k | 2.7166 | 2.7305 | +0.51% | -0.08% | -0.00% | 1.0% / 0.7% | Unclear |
| substr-count/colon2/4k | 1.0302 | 1.0449 | +1.43% | -0.30% | +0.00% | 0.1% / 2.5% | Unclear |
| str-replace/colon2/4k | 3.1297 | 3.2008 | +2.27% | -0.42% | -0.00% | 0.1% / 0.1% | Unclear |
| render-template/4k | 5.5718 | 5.5853 | +0.24% | -0.22% | +0.00% | 0.2% / 0.2% | Unclear |
| route/pair/ascii/absent | 1.2205 | 10.8853 | +791.88% | +802.77% | +777.55% | 0.5% / 0.1% | Slower |
| route/pair/dna/absent | 1.2238 | 10.8733 | +788.46% | +801.88% | +777.55% | 0.2% / 0.1% | Slower |
| route/pair/binary/absent | 1.2120 | 10.8613 | +796.15% | +800.88% | +779.36% | 0.2% / 0.0% | Slower |
| route/gram/selective/absent | 3.5767 | 1.0457 | -70.76% | -70.53% | -62.61% | 0.4% / 0.1% | Faster |
| route/gram/selective/late | 3.5885 | 1.0763 | -70.01% | -68.89% | -61.65% | 0.3% / 0.1% | Faster |
| route/gram/dense/absent | 2.8219 | 1.2722 | -54.92% | -55.25% | -37.86% | 2.7% / 0.0% | Faster |
| route/gram/changing/absent | 16.3163 | 4.1991 | -74.26% | -72.02% | -59.29% | 0.0% / 0.1% | Faster |
| route/twoway/periodic-memory | 23.0583 | 31.2367 | +35.47% | +31.68% | -8.01% | 1.4% / 0.1% | Slower |
| route/threshold/8191 | 35.0873 | 35.3154 | +0.65% | +1.83% | -0.00% | 0.4% / 1.2% | Unclear |
| route/threshold/8192 | 0.7391 | 5.5515 | +651.11% | +651.18% | +639.14% | 0.1% / 0.0% | Slower |
| gram-periodic/ascii/absent | 12.3336 | 33.8190 | +174.20% | +163.72% | +213.15% | 0.1% / 0.1% | Slower |
| gram-periodic/dna/absent | 12.7258 | 42.4883 | +233.88% | +234.11% | +346.79% | 0.1% / 0.0% | Slower |

## gcc15: Stock → ca89

| Case | A, µs | B, µs | Δ time | Δ cycles | Δ instr. | Spread A/B | Result |
|---|--:|--:|--:|--:|--:|--:|---|
| route/short9/absent | 3.8264 | 3.4415 | -10.06% | -9.74% | -0.53% | 0.1% / 0.2% | Faster |
| route/short9/early | 0.0231 | 0.0168 | -27.35% | -26.48% | -29.92% | 0.0% / 0.2% | Faster |
| route/short16/absent | 2.7885 | 2.5133 | -9.87% | -9.75% | -0.78% | 0.0% / 0.2% | Faster |
| route/short16/early | 0.0266 | 0.0209 | -21.34% | -25.34% | -25.13% | 0.1% / 2.0% | Faster |
| route/short31/absent | 1.3992 | 1.2393 | -11.43% | -11.69% | -1.26% | 0.1% / 0.2% | Faster |
| route/short31/early | 0.0344 | 0.0285 | -17.16% | -10.24% | -18.72% | 1.0% / 0.2% | Faster |
| route/long/ordinary-miss | 1.0349 | 1.0386 | +0.36% | -0.32% | +0.32% | 0.2% / 0.7% | Unclear |
| route/long/early | 0.0402 | 0.0423 | +5.19% | +6.14% | +3.33% | 0.0% / 0.6% | Slower |
| route/pair/ascii/absent | 68.7737 | 0.8871 | -98.71% | -98.74% | -98.91% | 0.0% / 0.1% | Faster |
| route/pair/dna/absent | 68.7918 | 0.8867 | -98.71% | -98.73% | -98.91% | 0.1% / 0.1% | Faster |
| route/pair/binary/absent | 68.7797 | 0.8798 | -98.72% | -98.75% | -98.91% | 0.0% / 0.0% | Faster |
| route/gram/selective/absent | 18.5564 | 3.4391 | -81.47% | -81.87% | -65.31% | 0.0% / 0.0% | Faster |
| route/gram/selective/late | 18.5920 | 3.4404 | -81.50% | -81.87% | -65.37% | 0.0% / 0.0% | Faster |
| route/gram/dense/absent | 19.4253 | 2.8501 | -85.33% | -85.58% | -76.15% | 0.1% / 0.0% | Noise |
| route/gram/changing/absent | 75.4335 | 15.7842 | -79.08% | -79.50% | -69.41% | 0.1% / 0.9% | Faster |
| route/twoway/periodic-memory | 151.4308 | 26.3816 | -82.58% | -83.39% | -84.77% | 0.6% / 1.0% | Faster |
| route/threshold/8191 | 32.5272 | 34.0976 | +4.83% | +5.46% | +0.00% | 1.5% / 1.1% | Slower |
| route/threshold/8192 | 34.3238 | 0.5510 | -98.39% | -98.42% | -98.62% | 0.0% / 0.1% | Faster |
| gram-periodic/ascii/absent | 76.7565 | 12.2857 | -83.99% | -84.19% | -75.45% | 0.2% / 0.0% | Faster |
| gram-periodic/dna/absent | 42.5055 | 12.2581 | -71.16% | -71.53% | -59.91% | 0.0% / 0.0% | Faster |
| route/long/early (repeat) | 0.0401 | 0.0421 | +5.01% | +6.14% | +3.33% | 0.2% / 0.2% | Slower |

## clang21: Stock → ca89

| Case | A, µs | B, µs | Δ time | Δ cycles | Δ instr. | Spread A/B | Result |
|---|--:|--:|--:|--:|--:|--:|---|
| route/short9/absent | 3.5199 | 3.1623 | -10.16% | -9.95% | -0.17% | 0.0% / 0.1% | Faster |
| route/short9/early | 0.0205 | 0.0148 | -28.02% | -28.09% | -12.46% | 0.1% / 4.7% | Faster |
| route/short16/absent | 2.5815 | 2.3087 | -10.57% | -10.43% | -0.25% | 0.0% / 0.0% | Faster |
| route/short16/early | 0.0250 | 0.0174 | -30.45% | -31.18% | -10.59% | 1.3% / 3.6% | Faster |
| route/short31/absent | 1.3091 | 1.1857 | -9.43% | -10.02% | -0.41% | 0.4% / 0.3% | Faster |
| route/short31/early | 0.0340 | 0.0268 | -21.24% | -29.95% | -7.62% | 0.4% / 7.2% | Noise |
| route/long/ordinary-miss | 0.9553 | 0.9536 | -0.18% | -0.42% | +7.19% | 0.0% / 0.1% | Unclear |
| route/long/early | 0.0388 | 0.0393 | +1.30% | +2.79% | +21.62% | 0.4% / 0.6% | Unclear |
| route/pair/ascii/absent | 118.3694 | 1.2158 | -98.97% | -98.99% | -98.25% | 0.0% / 0.2% | Faster |
| route/pair/dna/absent | 118.3667 | 1.2194 | -98.97% | -98.99% | -98.25% | 0.0% / 0.1% | Faster |
| route/pair/binary/absent | 118.3389 | 1.2127 | -98.98% | -98.99% | -98.25% | 0.0% / 0.5% | Faster |
| route/gram/selective/absent | 17.7853 | 3.5634 | -79.96% | -80.19% | -62.64% | 0.0% / 1.0% | Faster |
| route/gram/selective/late | 17.8165 | 3.5320 | -80.18% | -80.19% | -62.71% | 0.0% / 2.3% | Faster |
| route/gram/dense/absent | 17.9367 | 2.8222 | -84.27% | -84.15% | -78.02% | 0.0% / 2.7% | Faster |
| route/gram/changing/absent | 71.2386 | 16.3123 | -77.10% | -77.28% | -71.74% | 0.0% / 0.1% | Faster |
| route/twoway/periodic-memory | 244.7039 | 23.2346 | -90.51% | -90.38% | -85.46% | 0.1% / 0.4% | Faster |
| route/threshold/8191 | 59.0718 | 35.2589 | -40.31% | -38.35% | -0.50% | 0.0% / 1.6% | Faster |
| route/threshold/8192 | 59.0526 | 0.7378 | -98.75% | -98.77% | -97.87% | 0.0% / 0.3% | Faster |
| gram-periodic/ascii/absent | 70.9213 | 12.7811 | -81.98% | -82.23% | -74.11% | 0.0% / 0.0% | Faster |
| gram-periodic/dna/absent | 35.3003 | 12.3115 | -65.12% | -64.14% | -58.03% | 0.0% / 0.1% | Faster |
| route/long/early (repeat) | 0.0386 | 0.0391 | +1.33% | +2.79% | +21.62% | 0.2% / 0.1% | Unclear |

## Elapsed A/A controls

| Series | Case | A, µs | B, µs | Δ time | Spread A/B |
|---|---|--:|--:|--:|--:|
| aa-before-gcc15-0 | banlist12/en/post/early | 0.0345 | 0.0342 | -0.82% | 1.8% / 3.8% |
| aa-before-gcc15-1 | explode/colon2/4k | 2.5119 | 2.4996 | -0.49% | 0.3% / 0.2% |
| aa-before-clang21-0 | banlist12/en/post/early | 0.0324 | 0.0326 | +0.68% | 2.8% / 1.3% |
| aa-before-clang21-1 | explode/colon2/4k | 2.6966 | 2.7244 | +1.03% | 1.2% / 0.5% |
| aa-after-gcc15-0 | banlist12/en/post/early | 0.0344 | 0.0338 | -1.74% | 4.9% / 0.9% |
| aa-after-gcc15-1 | explode/colon2/4k | 2.5127 | 2.5170 | +0.17% | 1.3% / 0.3% |
| aa-after-clang21-0 | banlist12/en/post/early | 0.0321 | 0.0326 | +1.75% | 0.4% / 0.2% |
| aa-after-clang21-1 | explode/colon2/4k | 2.7332 | 2.7639 | +1.12% | 0.4% / 1.3% |
