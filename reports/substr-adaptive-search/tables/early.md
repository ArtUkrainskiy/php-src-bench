# Quiet Intel early-match confirmations

Same ca89 candidate and reference. These supplementary boundary calls are not a production frequency distribution. All original elapsed results and noisy rows are retained.

## GCC 13.3

| Case | Stock, µs | ca89, µs | Elapsed change | Instruction change | Elapsed result |
|---|--:|--:|--:|--:|---|
| early-match/n31/h8191 | 0.0423 | 0.0345 | −18.45% | −19.27% | Faster |
| early-match/n31/h8192 | 0.0423 | 0.0345 | −18.52% | −19.27% | Faster |
| early-match/n31/h8193 | 0.0422 | 0.0345 | −18.17% | −19.27% | Faster |
| early-match/n32/h8191 | 0.0429 | 0.0425 | −0.89% | +1.07% | Unclear |
| early-match/n32/h8192 | 0.0430 | 0.0452 | +5.13% | +4.27% | Slower |
| early-match/n32/h8193 | 0.0430 | 0.0451 | +4.75% | +4.27% | Slower |
| early-match/n33/h8191 | 0.0462 | 0.0423 | −8.46% | +1.05% | Faster |
| early-match/n33/h8192 | 0.0465 | 0.0458 | −1.47% | +4.19% | Faster |
| early-match/n33/h8193 | 0.0466 | 0.0458 | −1.79% | +4.19% | Faster |
| early-match/n64/h8191 | 0.0745 | 0.0671 | −9.89% | +0.69% | Faster |
| early-match/n64/h8192 | 0.0737 | 0.0710 | −3.61% | +2.74% | Unclear |
| early-match/n64/h8193 | 0.0735 | 0.0708 | −3.70% | +2.74% | Faster |
| early-match/n256/h8191 | 0.1795 | 0.1728 | −3.72% | +0.22% | Faster |
| early-match/n256/h8192 | 0.1792 | 0.1801 | +0.53% | +0.87% | Unclear |
| early-match/n256/h8193 | 0.1791 | 0.1803 | +0.64% | +0.87% | Unclear |

[Native series](../data/intel/gcc13-early.json).

## GCC 14.2

| Case | Stock, µs | ca89, µs | Elapsed change | Instruction change | Elapsed result |
|---|--:|--:|--:|--:|---|
| early-match/n31/h8191 | 0.0357 | 0.0279 | −21.91% | −19.24% | Faster |
| early-match/n31/h8192 | 0.0359 | 0.0278 | −22.45% | −19.24% | Faster |
| early-match/n31/h8193 | 0.0361 | 0.0279 | −22.65% | −19.24% | Faster |
| early-match/n32/h8191 | 0.0370 | 0.0371 | +0.32% | +1.20% | Noise |
| early-match/n32/h8192 | 0.0371 | 0.0398 | +7.32% | +3.99% | Noise |
| early-match/n32/h8193 | 0.0392 | 0.0394 | +0.69% | +3.99% | Noise |
| early-match/n33/h8191 | 0.0396 | 0.0376 | −5.12% | +1.18% | Noise |
| early-match/n33/h8192 | 0.0417 | 0.0410 | −1.64% | +3.93% | Noise |
| early-match/n33/h8193 | 0.0387 | 0.0404 | +4.48% | +3.93% | Noise |
| early-match/n64/h8191 | 0.0641 | 0.0550 | −14.20% | +0.77% | Noise |
| early-match/n64/h8192 | 0.0640 | 0.0581 | −9.23% | +2.57% | Noise |
| early-match/n64/h8193 | 0.0645 | 0.0588 | −8.80% | +2.57% | Noise |
| early-match/n256/h8191 | 0.1703 | 0.1713 | +0.63% | +0.25% | Unclear |
| early-match/n256/h8192 | 0.1697 | 0.1754 | +3.32% | +0.82% | Slower |
| early-match/n256/h8193 | 0.1700 | 0.1752 | +3.06% | +0.82% | Slower |

[Native series](../data/intel/gcc14-early.json).

## Clang 18.1

| Case | Stock, µs | ca89, µs | Elapsed change | Instruction change | Elapsed result |
|---|--:|--:|--:|--:|---|
| early-match/n31/h8191 | 0.0294 | 0.0252 | −14.33% | −8.42% | Faster |
| early-match/n31/h8192 | 0.0294 | 0.0252 | −14.37% | −8.42% | Faster |
| early-match/n31/h8193 | 0.0293 | 0.0254 | −13.42% | −8.42% | Faster |
| early-match/n32/h8191 | 0.0374 | 0.0294 | −21.58% | +1.08% | Faster |
| early-match/n32/h8192 | 0.0369 | 0.0340 | −8.00% | +2.52% | Noise |
| early-match/n32/h8193 | 0.0363 | 0.0331 | −8.90% | +2.52% | Noise |
| early-match/n33/h8191 | 0.0354 | 0.0296 | −16.51% | +1.05% | Noise |
| early-match/n33/h8192 | 0.0324 | 0.0362 | +11.65% | +2.44% | Noise |
| early-match/n33/h8193 | 0.0324 | 0.0361 | +11.38% | +2.44% | Noise |
| early-match/n64/h8191 | 0.0441 | 0.0432 | −2.11% | +0.69% | Noise |
| early-match/n64/h8192 | 0.0441 | 0.0453 | +2.71% | +1.61% | Noise |
| early-match/n64/h8193 | 0.0439 | 0.0462 | +5.18% | +1.61% | Noise |
| early-match/n256/h8191 | 0.1365 | 0.1432 | +4.93% | +0.22% | Slower |
| early-match/n256/h8192 | 0.1363 | 0.1357 | −0.46% | +0.51% | Unclear |
| early-match/n256/h8193 | 0.1365 | 0.1358 | −0.50% | +0.51% | Unclear |

[Native series](../data/intel/clang18-early.json).

## Clang 20.1

| Case | Stock, µs | ca89, µs | Elapsed change | Instruction change | Elapsed result |
|---|--:|--:|--:|--:|---|
| early-match/n31/h8191 | 0.0295 | 0.0325 | +10.10% | −8.67% | Noise |
| early-match/n31/h8192 | 0.0299 | 0.0338 | +12.83% | −8.67% | Noise |
| early-match/n31/h8193 | 0.0312 | 0.0346 | +10.80% | −8.67% | Noise |
| early-match/n32/h8191 | 0.0326 | 0.0377 | +15.42% | +3.15% | Noise |
| early-match/n32/h8192 | 0.0329 | 0.0352 | +7.03% | +22.22% | Noise |
| early-match/n32/h8193 | 0.0334 | 0.0361 | +7.96% | +22.22% | Noise |
| early-match/n33/h8191 | 0.0339 | 0.0387 | +14.42% | +2.87% | Noise |
| early-match/n33/h8192 | 0.0334 | 0.0362 | +8.30% | +21.90% | Noise |
| early-match/n33/h8193 | 0.0334 | 0.0361 | +8.14% | +21.90% | Noise |
| early-match/n64/h8191 | 0.0479 | 0.0608 | +26.80% | +2.93% | Noise |
| early-match/n64/h8192 | 0.0471 | 0.0518 | +9.86% | +26.29% | Noise |
| early-match/n64/h8193 | 0.0486 | 0.0519 | +6.68% | +26.29% | Noise |
| early-match/n256/h8191 | 0.1591 | 0.1503 | −5.49% | +2.68% | Noise |
| early-match/n256/h8192 | 0.1580 | 0.1709 | +8.16% | +31.13% | Noise |
| early-match/n256/h8193 | 0.1589 | 0.1698 | +6.88% | +31.13% | Noise |

[Native series](../data/intel/clang20-early.json).
