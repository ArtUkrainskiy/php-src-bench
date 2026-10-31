# Elapsed time: stock → compact Sunday

One paired round, ten approximately one-second samples per version after at least three seconds warmup. Samples share one PHP process per version. Deltas are descriptive; this is not four independent paired rounds. Negative means lower cost.

## clang21

Observed A/A envelope: 0.30%. Interpretation floor: 2.00%.

| Case | Bytes | Stock µs | Compact µs | Δ time | Δ cycles | Δ instr. | Quality |
|---|--:|--:|--:|--:|--:|--:|---|
| banlist12/en/post/clean | 1081 | 2.8060 | 2.5239 | -10.05% | -9.62% | -1.89% | Observed |
| banlist12/en/thread/clean | 65548 | 161.4258 | 148.5095 | -8.00% | -7.99% | -0.04% | Observed |
| banlist12/ru/post/clean | 1041 | 2.8824 | 2.7330 | -5.19% | -5.16% | -2.32% | Observed |
| banlist12/es/post/clean | 1086 | 2.7112 | 2.4345 | -10.21% | -9.86% | -1.89% | Observed |
| banlist12/ar/post/clean | 1036 | 3.8715 | 3.6589 | -5.49% | -5.71% | -1.28% | Observed |
| banlist12/hi/post/clean | 1091 | 2.5331 | 2.3453 | -7.41% | -7.00% | -2.70% | Observed |
| banlist12/zh/post/clean | 1039 | 2.1935 | 1.9339 | -11.84% | -11.45% | -2.61% | Observed |
| banlist12/zh/thread/clean | 65620 | 143.5457 | 131.7750 | -8.20% | -8.22% | -0.05% | Observed |
| banlist12/ja/post/clean | 1069 | 3.1576 | 2.8807 | -8.77% | -9.26% | -1.73% | Observed |
| banlist12/ko/post/clean | 1098 | 2.9995 | 2.7558 | -8.12% | -8.25% | -1.68% | Observed |
| banlist12/emoji/post/clean | 1097 | 2.5714 | 2.3065 | -10.30% | -10.25% | -2.05% | Observed |
| explode/pipe2/4k | 4123 | 2.7295 | 2.6258 | -3.80% | +0.31% | -0.00% | Observed |
| explode/colon2/4k | 4099 | 2.6946 | 2.7033 | +0.32% | -0.49% | -0.00% | Near A/A |
| parse-http/body64k | 65848 | 0.8524 | 0.8262 | -3.07% | -1.81% | +0.00% | Observed |
| render-template/4k | 4250 | 6.4798 | 5.5455 | -14.42% | -14.44% | -6.37% | Observed |
| count-template/4k | 4250 | 0.9404 | 0.7944 | -15.53% | -15.29% | -6.56% | Observed |
| boundary/9/absent | 14400 | 3.5678 | 3.1581 | -11.48% | -11.19% | -0.17% | Observed |
| boundary/32/early-text (original label: 31) | 14439 | 0.0319 | 0.0320 | +0.48% | +1.07% | +2.67% | Near A/A |
| boundary/32/early | 16839 | 0.0373 | 0.0368 | -1.50% | -1.28% | +2.03% | Near A/A |
| boundary/31/early | 14438 | 0.0299 | 0.0266 | -10.92% | -13.73% | -7.45% | Observed |

## gcc15

Observed A/A envelope: 2.32%. Interpretation floor: 2.32%.

| Case | Bytes | Stock µs | Compact µs | Δ time | Δ cycles | Δ instr. | Quality |
|---|--:|--:|--:|--:|--:|--:|---|
| banlist12/en/post/clean | 1081 | 2.9496 | 2.6783 | -9.20% | -10.19% | -5.76% | Observed |
| banlist12/en/thread/clean | 65548 | 169.3483 | 157.9180 | -6.75% | -6.99% | -0.13% | Observed |
| banlist12/ru/post/clean | 1041 | 3.0331 | 2.8469 | -6.14% | -5.18% | -3.43% | Observed |
| banlist12/es/post/clean | 1086 | 2.8435 | 2.5977 | -8.65% | -8.85% | -5.77% | Observed |
| banlist12/ar/post/clean | 1036 | 3.9634 | 3.7680 | -4.93% | -4.79% | -3.99% | Observed |
| banlist12/hi/post/clean | 1091 | 2.6601 | 2.4853 | -6.57% | -6.95% | -4.96% | Observed |
| banlist12/zh/post/clean | 1039 | 2.3145 | 2.0789 | -10.18% | -9.91% | -7.75% | Observed |
| banlist12/zh/thread/clean | 65620 | 149.5828 | 139.0386 | -7.05% | -7.06% | -0.17% | Observed |
| banlist12/ja/post/clean | 1069 | 3.2940 | 3.1229 | -5.20% | -8.56% | -5.32% | Observed |
| banlist12/ko/post/clean | 1098 | 3.1239 | 2.8635 | -8.34% | -7.75% | -5.18% | Observed |
| banlist12/emoji/post/clean | 1097 | 2.6857 | 2.4525 | -8.68% | -9.06% | -6.22% | Observed |
| explode/pipe2/4k | 4123 | 2.5352 | 2.4895 | -1.80% | -0.25% | -0.00% | Near A/A |
| explode/colon2/4k | 4099 | 2.5143 | 2.5089 | -0.22% | -0.92% | +0.00% | Near A/A |
| parse-http/body64k | 65848 | 0.8704 | 0.8702 | -0.02% | +0.89% | +0.00% | Near A/A |
| render-template/4k | 4250 | 7.0374 | 5.9181 | -15.91% | -16.10% | -17.63% | Observed |
| count-template/4k | 4250 | 0.9989 | 0.8339 | -16.52% | -15.85% | -18.07% | Observed |
| boundary/9/absent | 14400 | 3.7974 | 3.4724 | -8.56% | -8.38% | -0.53% | Observed |
| boundary/32/early-text (original label: 31) | 14439 | 0.0346 | 0.0359 | +3.86% | +2.57% | +0.64% | Observed |
| boundary/32/early | 16839 | 0.0399 | 0.0411 | +2.99% | -0.51% | +0.62% | Observed |
| boundary/31/early | 14438 | 0.0338 | 0.0297 | -12.30% | -19.15% | -18.72% | Observed |

## Elapsed A/A

| Source | Compiler | A ns | B ns | Δ time | Quality |
|---|---|--:|--:|--:|---|
| amd/aa-after-clang21.json | clang21 | 31.763 | 31.840 | +0.24% | Observed |
| amd/aa-after-gcc15.json | gcc15 | 34.569 | 35.042 | +1.37% | Observed |
| amd/aa-before-clang21.json | clang21 | 31.666 | 31.570 | -0.30% | Observed |
| amd/aa-before-gcc15.json | gcc15 | 33.786 | 34.571 | +2.32% | Observed |
