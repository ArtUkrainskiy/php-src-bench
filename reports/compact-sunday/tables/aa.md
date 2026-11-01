# A/A controls

[Interpretation](../README.md). Each row compares one unchanged binary with itself. This tests run-to-run variation; it does not measure compiler-to-compiler differences or prove immunity to code layout. The table shows elapsed-time controls; native counter controls accompany every suite in the counter tables.

## Disturbed native control

In Intel mbstring counters, aa2 / mb_strstr/zh/absent / pass 1 / side b ran after a 120-second idle wait expired (CPU 2 reported 17% busy). Exclude that pair from any quiet-control claim. Original observations are retained in [the series](../data/counters/intel-extensions-mbstring.json); [quality metadata](../data/counter-quality.json) identifies row 1741 (zero-based). The A/B rows were not the rows associated with that warning. A separate five-pair [A/A validation](../data/counters/intel-extensions-aa-validation.json) repeats that one case with the same GCC14 master binary.

The fresh validation median is -0.308% cycles and +0.00068% instructions. It is additional evidence, not a replacement observation in the original series.

## AMD gcc15

| Capture / control | Binary | Δ time | Min Δ | Max Δ |
|---|---|---:|---:|---:|
| `amd/aa-before-1-gcc15` | master | +0.01% | -0.08% | +0.61% |
| `amd/aa-before-2-gcc15` | master | -0.02% | -0.04% | +0.20% |
| `amd/aa-before-3-gcc15` | master | -0.00% | -0.18% | +0.19% |
| `amd/aa-before-4-gcc15` | master | -0.85% | -2.45% | +2.28% |
| `amd/head-aa-before-1-gcc15` | compact | +0.17% | +0.01% | +1.02% |
| `amd/head-aa-before-2-gcc15` | compact | +0.20% | -0.36% | +0.57% |
| `amd/aa-after-1-gcc15` | master | +0.01% | -0.33% | +0.47% |
| `amd/aa-after-2-gcc15` | master | -0.01% | -1.54% | +0.21% |
| `amd/aa-after-3-gcc15` | master | -0.04% | -0.65% | +0.01% |
| `amd/aa-after-4-gcc15` | master | +0.06% | -1.73% | +0.74% |
| `amd/head-aa-after-1-gcc15` | compact | +1.16% | -3.54% | +1.53% |
| `amd/head-aa-after-2-gcc15` | compact | +0.13% | -2.42% | +0.33% |

## AMD clang21

| Capture / control | Binary | Δ time | Min Δ | Max Δ |
|---|---|---:|---:|---:|
| `amd/aa-before-1-clang21` | master | +0.00% | -0.06% | +0.02% |
| `amd/aa-before-2-clang21` † | master | +0.11% | -16.61% | +0.41% |
| `amd/aa-before-3-clang21` | master | -0.03% | -0.10% | +0.21% |
| `amd/aa-before-4-clang21` | master | -0.39% | -0.68% | +0.10% |
| `amd/head-aa-before-1-clang21` | compact | +2.11% | -1.96% | +2.86% |
| `amd/head-aa-before-2-clang21` | compact | +0.81% | +0.22% | +2.11% |
| `amd/aa-after-1-clang21` | master | +0.01% | -0.04% | +0.10% |
| `amd/aa-after-2-clang21` | master | +0.02% | -0.35% | +0.35% |
| `amd/aa-after-3-clang21` | master | +0.02% | -0.16% | +0.09% |
| `amd/aa-after-4-clang21` | master | +0.91% | -1.56% | +1.15% |
| `amd/head-aa-after-1-clang21` | compact | -0.32% | -1.62% | +0.10% |
| `amd/head-aa-after-2-clang21` | compact | +1.04% | -0.09% | +1.12% |

## Intel gcc13

| Capture / control | Binary | Δ time | Min Δ | Max Δ |
|---|---|---:|---:|---:|
| `intel/aa-before-1-gcc13` | master | +0.06% | -0.04% | +0.08% |
| `intel/aa-before-2-gcc13` | master | +0.05% | -0.21% | +0.28% |
| `intel/head-aa-before-1-gcc13` | compact | +0.07% | -0.72% | +1.96% |
| `intel/head-aa-before-2-gcc13` | compact | +0.00% | -0.13% | +0.25% |
| `intel/aa-after-1-gcc13` | master | +0.01% | -0.10% | +0.06% |
| `intel/aa-after-2-gcc13` | master | +0.01% | -0.02% | +0.02% |
| `intel/head-aa-after-1-gcc13` | compact | +1.17% | -0.21% | +6.20% |
| `intel/head-aa-after-2-gcc13` | compact | -0.18% | -0.50% | +0.14% |
| `intel-extensions/aa-before-1-gcc13` | master | +0.07% | +0.01% | +0.34% |
| `intel-extensions/aa-before-2-gcc13` | master | -0.15% | -0.65% | +0.54% |
| `intel-extensions/aa-after-1-gcc13` | master | -0.03% | -0.12% | +0.03% |
| `intel-extensions/aa-after-2-gcc13` | master | +0.88% | -0.16% | +1.35% |

## Intel gcc14

| Capture / control | Binary | Δ time | Min Δ | Max Δ |
|---|---|---:|---:|---:|
| `intel/aa-before-1-gcc14` | master | -0.02% | -1.02% | +0.04% |
| `intel/aa-before-2-gcc14` | master | -0.00% | -0.02% | +0.72% |
| `intel/head-aa-before-1-gcc14` | compact | +0.13% | -2.90% | +2.54% |
| `intel/head-aa-before-2-gcc14` | compact | -0.09% | -1.16% | +0.22% |
| `intel/aa-after-1-gcc14` | master | -0.02% | -0.07% | +0.07% |
| `intel/aa-after-2-gcc14` | master | -0.01% | -0.08% | +0.02% |
| `intel/head-aa-after-1-gcc14` | compact | -0.17% | -0.56% | +0.59% |
| `intel/head-aa-after-2-gcc14` | compact | -0.07% | -0.14% | +0.13% |
| `intel-extensions/aa-before-1-gcc14` | master | -0.18% | -0.27% | -0.06% |
| `intel-extensions/aa-before-2-gcc14` | master | -0.69% | -1.83% | +0.00% |
| `intel-extensions/aa-after-1-gcc14` | master | -0.04% | -0.27% | +0.34% |
| `intel-extensions/aa-after-2-gcc14` | master | +0.22% | -0.62% | +1.06% |

## Intel clang18

| Capture / control | Binary | Δ time | Min Δ | Max Δ |
|---|---|---:|---:|---:|
| `intel/aa-before-1-clang18` | master | -0.02% | -0.12% | +0.09% |
| `intel/aa-before-2-clang18` | master | -0.03% | -1.23% | +0.08% |
| `intel/head-aa-before-1-clang18` | compact | -0.24% | -1.56% | +2.75% |
| `intel/head-aa-before-2-clang18` | compact | +0.26% | +0.03% | +1.76% |
| `intel/aa-after-1-clang18` | master | +0.02% | -0.03% | +0.07% |
| `intel/aa-after-2-clang18` | master | +0.04% | -0.05% | +0.06% |
| `intel/head-aa-after-1-clang18` | compact | -0.03% | -4.04% | +0.06% |
| `intel/head-aa-after-2-clang18` † | compact | -0.04% | -8.68% | +0.55% |
| `intel-extensions/aa-before-1-clang18` | master | +0.12% | -0.02% | +0.75% |
| `intel-extensions/aa-before-2-clang18` | master | -0.02% | -0.06% | +0.17% |
| `intel-extensions/aa-after-1-clang18` | master | +0.02% | -0.12% | +0.19% |
| `intel-extensions/aa-after-2-clang18` | master | +0.20% | -1.37% | +1.77% |

## Intel clang20

| Capture / control | Binary | Δ time | Min Δ | Max Δ |
|---|---|---:|---:|---:|
| `intel/aa-before-1-clang20` | master | +0.01% | -0.14% | +0.05% |
| `intel/aa-before-2-clang20` | master | +0.03% | -0.09% | +0.13% |
| `intel/head-aa-before-1-clang20` | compact | +0.50% | -0.29% | +1.62% |
| `intel/head-aa-before-2-clang20` | compact | -0.19% | -0.57% | +0.79% |
| `intel/aa-after-1-clang20` | master | -0.01% | -0.04% | +0.01% |
| `intel/aa-after-2-clang20` | master | +0.02% | -0.02% | +0.08% |
| `intel/head-aa-after-1-clang20` | compact | +0.31% | -0.21% | +0.82% |
| `intel/head-aa-after-2-clang20` | compact | +0.08% | -0.36% | +0.27% |
| `intel-extensions/aa-before-1-clang20` | master | -0.03% | -0.13% | +0.17% |
| `intel-extensions/aa-before-2-clang20` | master | +1.32% | -3.10% | +4.31% |
| `intel-extensions/aa-after-1-clang20` | master | +0.02% | -0.07% | +1.54% |
| `intel-extensions/aa-after-2-clang20` | master | +0.70% | -2.34% | +0.92% |
