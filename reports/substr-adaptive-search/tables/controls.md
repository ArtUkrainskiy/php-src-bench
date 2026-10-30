# Elapsed-time A/A controls

Each A/A pair runs the same binary on both sides. These selected controls do not cover all 233 cases. AMD includes six pilot cases at both durations; Intel has ten stock controls before and ten candidate controls after its series. Additional A/A for all originally usable AMD slower cases is in the main report and raw confirmation data.

## clang21-aa-1sec

| Case | A₁, µs | A₂, µs | Δ A/A | Spread A₁ / A₂ | Result |
|---|---:|---:|---:|---:|---|
| banlist12/en/post/clean | 2.8061 | 2.8050 | −0.04% | 0.12% / 0.06% | Unclear |
| banlist12/en/post/early | 0.0306 | 0.0312 | +2.04% | 1.80% / 1.80% | Unclear |
| banlist12/ru/thread/clean | 217.7306 | 217.5714 | −0.07% | 0.05% / 0.07% | Unclear |
| banlist12/hi/post/early | 0.0420 | 0.0420 | −0.08% | 0.36% / 1.09% | Unclear |
| parse-http/small | 0.8428 | 0.8449 | +0.25% | 0.23% / 0.06% | Unclear |
| render-template/4k | 6.4968 | 6.4994 | +0.04% | 0.46% / 0.30% | Unclear |

[clang21-aa-1sec.json](../data/amd/clang21-aa-1sec.json).

## clang21-aa-50ms

| Case | A₁, µs | A₂, µs | Δ A/A | Spread A₁ / A₂ | Result |
|---|---:|---:|---:|---:|---|
| banlist12/en/post/clean | 2.7957 | 2.7943 | −0.05% | 0.17% / 0.16% | Unclear |
| banlist12/en/post/early | 0.0307 | 0.0302 | −1.75% | 0.96% / 0.88% | Unclear |
| banlist12/ru/thread/clean | 217.4866 | 217.3488 | −0.06% | 0.10% / 0.05% | Unclear |
| banlist12/hi/post/early | 0.0425 | 0.0418 | −1.75% | 0.57% / 1.82% | Unclear |
| parse-http/small | 0.8480 | 0.8427 | −0.62% | 0.50% / 0.51% | Unclear |
| render-template/4k | 6.4964 | 6.4804 | −0.25% | 0.60% / 0.34% | Unclear |

[clang21-aa-50ms.json](../data/amd/clang21-aa-50ms.json).

## gcc15-aa-1sec

| Case | A₁, µs | A₂, µs | Δ A/A | Spread A₁ / A₂ | Result |
|---|---:|---:|---:|---:|---|
| banlist12/en/post/clean | 2.9632 | 2.9525 | −0.36% | 0.29% / 0.08% | Unclear |
| banlist12/en/post/early | 0.0323 | 0.0325 | +0.43% | 2.88% / 1.01% | Unclear |
| banlist12/ru/thread/clean | 221.8587 | 221.7740 | −0.04% | 0.17% / 0.06% | Unclear |
| banlist12/hi/post/early | 0.0446 | 0.0450 | +0.74% | 3.21% / 3.10% | Unclear |
| parse-http/small | 0.8319 | 0.8335 | +0.20% | 0.39% / 0.18% | Unclear |
| render-template/4k | 7.0111 | 7.0197 | +0.12% | 0.13% / 0.22% | Unclear |

[gcc15-aa-1sec.json](../data/amd/gcc15-aa-1sec.json).

## gcc15-aa-50ms

| Case | A₁, µs | A₂, µs | Δ A/A | Spread A₁ / A₂ | Result |
|---|---:|---:|---:|---:|---|
| banlist12/en/post/clean | 2.9565 | 2.9533 | −0.11% | 0.29% / 0.47% | Unclear |
| banlist12/en/post/early | 0.0330 | 0.0328 | −0.51% | 2.10% / 1.46% | Unclear |
| banlist12/ru/thread/clean | 221.1602 | 221.1399 | −0.01% | 0.06% / 0.05% | Unclear |
| banlist12/hi/post/early | 0.0447 | 0.0447 | +0.04% | 0.32% / 1.47% | Unclear |
| parse-http/small | 0.8338 | 0.8294 | −0.52% | 0.31% / 0.81% | Unclear |
| render-template/4k | 7.0133 | 6.9949 | −0.26% | 0.29% / 0.29% | Unclear |

[gcc15-aa-50ms.json](../data/amd/gcc15-aa-50ms.json).

## clang18-aa-after

| Case | A₁, µs | A₂, µs | Δ A/A | Spread A₁ / A₂ | Result |
|---|---:|---:|---:|---:|---|
| banlist12/en/comment/clean | 0.5272 | 0.5275 | +0.05% | 0.47% / 0.49% | Unclear |
| banlist12/en/post/clean | 3.4934 | 3.4938 | +0.01% | 0.08% / 0.11% | Unclear |
| banlist12/ru/thread/clean | 306.4665 | 306.2611 | −0.07% | 0.11% / 0.13% | Unclear |
| banlist12/es/comment/clean | 0.5782 | 0.5771 | −0.19% | 0.37% / 0.38% | Unclear |
| banlist12/hi/thread/clean | 254.3758 | 254.4609 | +0.03% | 0.20% / 0.18% | Unclear |
| banlist12/zh/thread/clean | 193.9388 | 193.8084 | −0.07% | 0.14% / 0.16% | Unclear |
| parse-http/small | 0.8946 | 0.8910 | −0.40% | 1.35% / 0.91% | Unclear |
| parse-http/body64k | 0.8976 | 0.8932 | −0.49% | 1.13% / 1.13% | Unclear |
| render-template/4k | 6.2335 | 6.2851 | +0.83% | 0.35% / 1.54% | Unclear |
| log-contains/event/thread/clean | 18.0222 | 17.9980 | −0.13% | 0.78% / 0.83% | Unclear |

[clang18-aa-after.json](../data/intel/clang18-aa-after.json).

## clang18-aa-before

| Case | A₁, µs | A₂, µs | Δ A/A | Spread A₁ / A₂ | Result |
|---|---:|---:|---:|---:|---|
| banlist12/en/comment/clean | 0.5285 | 0.5289 | +0.08% | 0.50% / 0.30% | Unclear |
| banlist12/en/post/clean | 3.4981 | 3.5002 | +0.06% | 0.31% / 0.32% | Unclear |
| banlist12/ru/thread/clean | 311.7305 | 311.8917 | +0.05% | 0.21% / 0.20% | Unclear |
| banlist12/es/comment/clean | 0.5790 | 0.5779 | −0.19% | 0.45% / 0.37% | Unclear |
| banlist12/hi/thread/clean | 257.4526 | 257.5477 | +0.04% | 0.68% / 0.48% | Unclear |
| banlist12/zh/thread/clean | 199.0333 | 198.9263 | −0.05% | 0.34% / 0.14% | Unclear |
| parse-http/small | 0.9086 | 0.9242 | +1.71% | 1.95% / 1.86% | Unclear |
| parse-http/body64k | 0.9141 | 0.9218 | +0.84% | 1.18% / 1.22% | Unclear |
| render-template/4k | 6.8697 | 6.8625 | −0.11% | 0.74% / 0.91% | Unclear |
| log-contains/event/thread/clean | 17.2596 | 17.2582 | −0.01% | 0.10% / 0.10% | Unclear |

[clang18-aa-before.json](../data/intel/clang18-aa-before.json).

## clang20-aa-after

| Case | A₁, µs | A₂, µs | Δ A/A | Spread A₁ / A₂ | Result |
|---|---:|---:|---:|---:|---|
| banlist12/en/comment/clean | 0.4906 | 0.4903 | −0.06% | 0.26% / 0.19% | Unclear |
| banlist12/en/post/clean | 3.2662 | 3.2642 | −0.06% | 0.23% / 0.21% | Unclear |
| banlist12/ru/thread/clean | 309.8275 | 309.8513 | +0.01% | 0.15% / 0.13% | Unclear |
| banlist12/es/comment/clean | 0.5570 | 0.5573 | +0.04% | 0.30% / 0.18% | Unclear |
| banlist12/hi/thread/clean | 259.5819 | 259.5312 | −0.02% | 0.81% / 0.70% | Unclear |
| banlist12/zh/thread/clean | 204.8060 | 204.9200 | +0.06% | 0.19% / 0.42% | Unclear |
| parse-http/small | 0.7932 | 0.8077 | +1.83% | 2.16% / 1.48% | Unclear |
| parse-http/body64k | 0.7949 | 0.8002 | +0.67% | 1.62% / 1.06% | Unclear |
| render-template/4k | 6.3211 | 6.2311 | −1.42% | 1.12% / 0.63% | Unclear |
| log-contains/event/thread/clean | 17.2465 | 17.2413 | −0.03% | 0.06% / 0.10% | Unclear |

[clang20-aa-after.json](../data/intel/clang20-aa-after.json).

## clang20-aa-before

| Case | A₁, µs | A₂, µs | Δ A/A | Spread A₁ / A₂ | Result |
|---|---:|---:|---:|---:|---|
| banlist12/en/comment/clean | 0.4905 | 0.4898 | −0.13% | 0.13% / 0.70% | Unclear |
| banlist12/en/post/clean | 3.5120 | 3.5111 | −0.02% | 0.14% / 0.09% | Unclear |
| banlist12/ru/thread/clean | 308.3490 | 308.4625 | +0.04% | 0.14% / 0.09% | Unclear |
| banlist12/es/comment/clean | 0.5590 | 0.5572 | −0.32% | 0.40% / 0.38% | Unclear |
| banlist12/hi/thread/clean | 255.9863 | 256.1079 | +0.05% | 0.47% / 0.38% | Unclear |
| banlist12/zh/thread/clean | 194.1577 | 194.2116 | +0.03% | 0.12% / 0.12% | Unclear |
| parse-http/small | 0.7820 | 0.7803 | −0.22% | 1.21% / 0.55% | Unclear |
| parse-http/body64k | 0.7851 | 0.7789 | −0.80% | 1.11% / 0.88% | Unclear |
| render-template/4k | 6.3371 | 6.3490 | +0.19% | 0.39% / 0.30% | Unclear |
| log-contains/event/thread/clean | 17.4694 | 17.4660 | −0.02% | 0.11% / 0.08% | Unclear |

[clang20-aa-before.json](../data/intel/clang20-aa-before.json).

## gcc13-aa-after

| Case | A₁, µs | A₂, µs | Δ A/A | Spread A₁ / A₂ | Result |
|---|---:|---:|---:|---:|---|
| banlist12/en/comment/clean | 0.4971 | 0.4983 | +0.23% | 0.17% / 0.28% | Unclear |
| banlist12/en/post/clean | 3.2751 | 3.2743 | −0.03% | 0.10% / 0.07% | Unclear |
| banlist12/ru/thread/clean | 310.7488 | 310.5928 | −0.05% | 0.14% / 0.13% | Unclear |
| banlist12/es/comment/clean | 0.5684 | 0.5684 | +0.01% | 0.34% / 0.19% | Unclear |
| banlist12/hi/thread/clean | 259.3436 | 259.6269 | +0.11% | 0.41% / 0.41% | Unclear |
| banlist12/zh/thread/clean | 199.0523 | 199.1138 | +0.03% | 0.22% / 0.35% | Unclear |
| parse-http/small | 0.8214 | 0.8237 | +0.28% | 0.28% / 0.33% | Unclear |
| parse-http/body64k | 0.8220 | 0.8205 | −0.18% | 0.57% / 0.37% | Unclear |
| render-template/4k | 6.4352 | 6.3874 | −0.74% | 0.92% / 0.47% | Unclear |
| log-contains/event/thread/clean | 17.0943 | 17.0867 | −0.04% | 0.19% / 0.17% | Unclear |

[gcc13-aa-after.json](../data/intel/gcc13-aa-after.json).

## gcc13-aa-before

| Case | A₁, µs | A₂, µs | Δ A/A | Spread A₁ / A₂ | Result |
|---|---:|---:|---:|---:|---|
| banlist12/en/comment/clean | 0.4977 | 0.4977 | −0.00% | 0.26% / 0.23% | Unclear |
| banlist12/en/post/clean | 3.4815 | 3.4823 | +0.02% | 0.11% / 0.09% | Unclear |
| banlist12/ru/thread/clean | 303.1449 | 303.1574 | +0.00% | 0.15% / 0.14% | Unclear |
| banlist12/es/comment/clean | 0.5679 | 0.5674 | −0.10% | 0.22% / 0.21% | Unclear |
| banlist12/hi/thread/clean | 259.6767 | 259.9468 | +0.10% | 0.33% / 0.46% | Unclear |
| banlist12/zh/thread/clean | 200.5461 | 200.5100 | −0.02% | 0.17% / 0.23% | Unclear |
| parse-http/small | 0.8078 | 0.8066 | −0.16% | 0.48% / 0.56% | Unclear |
| parse-http/body64k | 0.8065 | 0.8051 | −0.17% | 0.49% / 0.33% | Unclear |
| render-template/4k | 7.6436 | 7.6438 | +0.00% | 0.21% / 0.23% | Unclear |
| log-contains/event/thread/clean | 17.0418 | 17.0370 | −0.03% | 0.08% / 0.06% | Unclear |

[gcc13-aa-before.json](../data/intel/gcc13-aa-before.json).

## gcc14-aa-after

| Case | A₁, µs | A₂, µs | Δ A/A | Spread A₁ / A₂ | Result |
|---|---:|---:|---:|---:|---|
| banlist12/en/comment/clean | 0.5080 | 0.5072 | −0.16% | 0.34% / 0.42% | Unclear |
| banlist12/en/post/clean | 3.5024 | 3.4689 | −0.96% | 1.25% / 0.89% | Unclear |
| banlist12/ru/thread/clean | 304.6427 | 304.4904 | −0.05% | 0.36% / 0.31% | Unclear |
| banlist12/es/comment/clean | 0.5659 | 0.5659 | +0.00% | 0.16% / 0.43% | Unclear |
| banlist12/hi/thread/clean | 258.3130 | 258.3098 | −0.00% | 0.44% / 0.29% | Unclear |
| banlist12/zh/thread/clean | 200.2201 | 199.8547 | −0.18% | 0.21% / 0.24% | Unclear |
| parse-http/small | 0.8120 | 0.8038 | −1.01% | 1.78% / 1.54% | Unclear |
| parse-http/body64k | 0.8091 | 0.8057 | −0.43% | 0.75% / 0.97% | Unclear |
| render-template/4k | 6.4647 | 6.4402 | −0.38% | 1.21% / 0.66% | Unclear |
| log-contains/event/thread/clean | 17.2800 | 17.2736 | −0.04% | 0.36% / 0.16% | Unclear |

[gcc14-aa-after.json](../data/intel/gcc14-aa-after.json).

## gcc14-aa-before

| Case | A₁, µs | A₂, µs | Δ A/A | Spread A₁ / A₂ | Result |
|---|---:|---:|---:|---:|---|
| banlist12/en/comment/clean | 0.5064 | 0.5067 | +0.06% | 0.21% / 0.29% | Unclear |
| banlist12/en/post/clean | 3.5553 | 3.5585 | +0.09% | 0.74% / 0.52% | Unclear |
| banlist12/ru/thread/clean | 311.8389 | 311.9578 | +0.04% | 0.19% / 0.24% | Unclear |
| banlist12/es/comment/clean | 0.5650 | 0.5648 | −0.03% | 0.30% / 0.29% | Unclear |
| banlist12/hi/thread/clean | 257.5805 | 258.4494 | +0.34% | 0.53% / 0.32% | Unclear |
| banlist12/zh/thread/clean | 199.2980 | 199.3661 | +0.03% | 0.11% / 0.16% | Unclear |
| parse-http/small | 0.7946 | 0.7930 | −0.20% | 0.66% / 0.38% | Unclear |
| parse-http/body64k | 0.7931 | 0.7931 | −0.00% | 0.25% / 0.44% | Unclear |
| render-template/4k | 7.4106 | 7.4233 | +0.17% | 0.57% / 0.51% | Unclear |
| log-contains/event/thread/clean | 17.5777 | 17.5721 | −0.03% | 0.76% / 0.71% | Unclear |

[gcc14-aa-before.json](../data/intel/gcc14-aa-before.json).
