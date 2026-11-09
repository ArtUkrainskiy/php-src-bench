# Timings: every implementation and A/A control

Native A/A runs the same code with a separate object. Deviation is the largest absolute sample deviation from the implementation's median. The quality column applies to the complete input/mode comparison; [flags](QUALITY.md).

| Input | Mode | Recipe | Median, µs/job | Maximum deviation | Comparison qualified |
|---|---|---|---:|---:|---|
| [comment.13.any](inputs/cases/comment.13.any.json) | prepared | Matcher::matches() | 0.343 | 0.98% | yes |
| [comment.13.any](inputs/cases/comment.13.any.json) | prepared | stripos() loop | 16.140 | 4.96% | yes |
| [comment.13.any](inputs/cases/comment.13.any.json) | prepared | preg_match() [literal] | 32.674 | 0.50% | yes |
| [comment.13.any](inputs/cases/comment.13.any.json) | prepared | preg_match() [prefix] | 1.685 | 1.77% | yes |
| [comment.13.any](inputs/cases/comment.13.any.json) | prepared | strtolower() + strpos() loop | 12.095 | 1.06% | yes |
| [comment.13.any](inputs/cases/comment.13.any.json) | prepared | Native A/A control | 0.344 | 1.84% | yes |
| [comment.13.any](inputs/cases/comment.13.any.json) | oneshot | Matcher::matches() | 295.515 | 0.41% | yes |
| [comment.13.any](inputs/cases/comment.13.any.json) | oneshot | stripos() loop | 16.092 | 1.03% | yes |
| [comment.13.any](inputs/cases/comment.13.any.json) | oneshot | preg_match() [literal] | 32.486 | 0.77% | yes |
| [comment.13.any](inputs/cases/comment.13.any.json) | oneshot | preg_match() [prefix] | 1.678 | 1.21% | yes |
| [comment.13.any](inputs/cases/comment.13.any.json) | oneshot | strtolower() + strpos() loop | 12.041 | 0.78% | yes |
| [comment.13.any](inputs/cases/comment.13.any.json) | oneshot | Native A/A control | 295.041 | 0.74% | yes |
| [comment.13.unique](inputs/cases/comment.13.unique.json) | prepared | Matcher::getMatchedKeywords() | 0.372 | 0.80% | yes |
| [comment.13.unique](inputs/cases/comment.13.unique.json) | prepared | stripos() loop | 16.002 | 0.32% | yes |
| [comment.13.unique](inputs/cases/comment.13.unique.json) | prepared | preg_match_all() [literal] | 13.929 | 0.74% | yes |
| [comment.13.unique](inputs/cases/comment.13.unique.json) | prepared | preg_match_all() [prefix] | 8.852 | 0.48% | yes |
| [comment.13.unique](inputs/cases/comment.13.unique.json) | prepared | strtolower() + strpos() loop | 12.254 | 0.79% | yes |
| [comment.13.unique](inputs/cases/comment.13.unique.json) | prepared | Native A/A control | 0.372 | 1.66% | yes |
| [comment.13.unique](inputs/cases/comment.13.unique.json) | oneshot | Matcher::getMatchedKeywords() | 299.053 | 0.97% | yes |
| [comment.13.unique](inputs/cases/comment.13.unique.json) | oneshot | stripos() loop | 16.035 | 0.58% | yes |
| [comment.13.unique](inputs/cases/comment.13.unique.json) | oneshot | preg_match_all() [literal] | 13.935 | 0.62% | yes |
| [comment.13.unique](inputs/cases/comment.13.unique.json) | oneshot | preg_match_all() [prefix] | 8.871 | 0.66% | yes |
| [comment.13.unique](inputs/cases/comment.13.unique.json) | oneshot | strtolower() + strpos() loop | 12.179 | 0.40% | yes |
| [comment.13.unique](inputs/cases/comment.13.unique.json) | oneshot | Native A/A control | 299.470 | 0.96% | yes |
| [comment.41710.any](inputs/cases/comment.41710.any.json) | prepared | Matcher::matches() | 0.359 | 2.48% | yes |
| [comment.41710.any](inputs/cases/comment.41710.any.json) | prepared | stripos() loop | 16.026 | 0.59% | yes |
| [comment.41710.any](inputs/cases/comment.41710.any.json) | prepared | preg_match() [literal] | 31.738 | 0.42% | yes |
| [comment.41710.any](inputs/cases/comment.41710.any.json) | prepared | preg_match() [prefix] | 1.665 | 1.79% | yes |
| [comment.41710.any](inputs/cases/comment.41710.any.json) | prepared | strtolower() + strpos() loop | 11.916 | 3.01% | yes |
| [comment.41710.any](inputs/cases/comment.41710.any.json) | prepared | Native A/A control | 0.360 | 1.27% | yes |
| [comment.41710.any](inputs/cases/comment.41710.any.json) | oneshot | Matcher::matches() | 294.977 | 0.59% | yes |
| [comment.41710.any](inputs/cases/comment.41710.any.json) | oneshot | stripos() loop | 15.901 | 0.49% | yes |
| [comment.41710.any](inputs/cases/comment.41710.any.json) | oneshot | preg_match() [literal] | 31.768 | 1.21% | yes |
| [comment.41710.any](inputs/cases/comment.41710.any.json) | oneshot | preg_match() [prefix] | 1.681 | 1.84% | yes |
| [comment.41710.any](inputs/cases/comment.41710.any.json) | oneshot | strtolower() + strpos() loop | 11.916 | 0.84% | yes |
| [comment.41710.any](inputs/cases/comment.41710.any.json) | oneshot | Native A/A control | 295.233 | 0.42% | yes |
| [comment.41710.unique](inputs/cases/comment.41710.unique.json) | prepared | Matcher::getMatchedKeywords() | 0.385 | 0.88% | yes |
| [comment.41710.unique](inputs/cases/comment.41710.unique.json) | prepared | stripos() loop | 15.868 | 1.30% | yes |
| [comment.41710.unique](inputs/cases/comment.41710.unique.json) | prepared | preg_match_all() [literal] | 14.031 | 0.55% | yes |
| [comment.41710.unique](inputs/cases/comment.41710.unique.json) | prepared | preg_match_all() [prefix] | 8.962 | 0.40% | yes |
| [comment.41710.unique](inputs/cases/comment.41710.unique.json) | prepared | strtolower() + strpos() loop | 11.839 | 0.67% | yes |
| [comment.41710.unique](inputs/cases/comment.41710.unique.json) | prepared | Native A/A control | 0.385 | 0.75% | yes |
| [comment.41710.unique](inputs/cases/comment.41710.unique.json) | oneshot | Matcher::getMatchedKeywords() | 295.870 | 0.74% | yes |
| [comment.41710.unique](inputs/cases/comment.41710.unique.json) | oneshot | stripos() loop | 15.860 | 0.59% | yes |
| [comment.41710.unique](inputs/cases/comment.41710.unique.json) | oneshot | preg_match_all() [literal] | 14.016 | 0.50% | yes |
| [comment.41710.unique](inputs/cases/comment.41710.unique.json) | oneshot | preg_match_all() [prefix] | 8.941 | 0.50% | yes |
| [comment.41710.unique](inputs/cases/comment.41710.unique.json) | oneshot | strtolower() + strpos() loop | 11.858 | 0.96% | yes |
| [comment.41710.unique](inputs/cases/comment.41710.unique.json) | oneshot | Native A/A control | 296.144 | 0.94% | yes |
| [comment.28.any](inputs/cases/comment.28.any.json) | prepared | Matcher::matches() | 0.318 | 1.22% | yes |
| [comment.28.any](inputs/cases/comment.28.any.json) | prepared | stripos() loop | 15.491 | 0.73% | yes |
| [comment.28.any](inputs/cases/comment.28.any.json) | prepared | preg_match() [literal] | 25.898 | 0.81% | yes |
| [comment.28.any](inputs/cases/comment.28.any.json) | prepared | preg_match() [prefix] | 1.461 | 1.06% | yes |
| [comment.28.any](inputs/cases/comment.28.any.json) | prepared | strtolower() + strpos() loop | 11.345 | 0.92% | yes |
| [comment.28.any](inputs/cases/comment.28.any.json) | prepared | Native A/A control | 0.319 | 1.08% | yes |
| [comment.28.any](inputs/cases/comment.28.any.json) | oneshot | Matcher::matches() | 295.676 | 0.88% | yes |
| [comment.28.any](inputs/cases/comment.28.any.json) | oneshot | stripos() loop | 15.372 | 0.94% | yes |
| [comment.28.any](inputs/cases/comment.28.any.json) | oneshot | preg_match() [literal] | 25.883 | 0.47% | yes |
| [comment.28.any](inputs/cases/comment.28.any.json) | oneshot | preg_match() [prefix] | 1.457 | 4.70% | yes |
| [comment.28.any](inputs/cases/comment.28.any.json) | oneshot | strtolower() + strpos() loop | 11.372 | 1.05% | yes |
| [comment.28.any](inputs/cases/comment.28.any.json) | oneshot | Native A/A control | 295.302 | 0.54% | yes |
| [comment.28.unique](inputs/cases/comment.28.unique.json) | prepared | Matcher::getMatchedKeywords() | 0.347 | 2.07% | yes |
| [comment.28.unique](inputs/cases/comment.28.unique.json) | prepared | stripos() loop | 15.343 | 1.52% | yes |
| [comment.28.unique](inputs/cases/comment.28.unique.json) | prepared | preg_match_all() [literal] | 12.686 | 2.25% | yes |
| [comment.28.unique](inputs/cases/comment.28.unique.json) | prepared | preg_match_all() [prefix] | 8.165 | 3.22% | yes |
| [comment.28.unique](inputs/cases/comment.28.unique.json) | prepared | strtolower() + strpos() loop | 11.492 | 1.49% | yes |
| [comment.28.unique](inputs/cases/comment.28.unique.json) | prepared | Native A/A control | 0.348 | 1.16% | yes |
| [comment.28.unique](inputs/cases/comment.28.unique.json) | oneshot | Matcher::getMatchedKeywords() | 295.702 | 0.70% | yes |
| [comment.28.unique](inputs/cases/comment.28.unique.json) | oneshot | stripos() loop | 15.634 | 1.87% | yes |
| [comment.28.unique](inputs/cases/comment.28.unique.json) | oneshot | preg_match_all() [literal] | 12.666 | 1.48% | yes |
| [comment.28.unique](inputs/cases/comment.28.unique.json) | oneshot | preg_match_all() [prefix] | 8.171 | 0.58% | yes |
| [comment.28.unique](inputs/cases/comment.28.unique.json) | oneshot | strtolower() + strpos() loop | 11.492 | 0.83% | yes |
| [comment.28.unique](inputs/cases/comment.28.unique.json) | oneshot | Native A/A control | 296.417 | 0.85% | yes |
| [comment.69493.any](inputs/cases/comment.69493.any.json) | prepared | Matcher::matches() | 0.310 | 1.81% | yes |
| [comment.69493.any](inputs/cases/comment.69493.any.json) | prepared | stripos() loop | 14.891 | 0.95% | yes |
| [comment.69493.any](inputs/cases/comment.69493.any.json) | prepared | preg_match() [literal] | 25.906 | 1.42% | yes |
| [comment.69493.any](inputs/cases/comment.69493.any.json) | prepared | preg_match() [prefix] | 1.476 | 0.77% | yes |
| [comment.69493.any](inputs/cases/comment.69493.any.json) | prepared | strtolower() + strpos() loop | 11.447 | 0.48% | yes |
| [comment.69493.any](inputs/cases/comment.69493.any.json) | prepared | Native A/A control | 0.310 | 1.17% | yes |
| [comment.69493.any](inputs/cases/comment.69493.any.json) | oneshot | Matcher::matches() | 294.861 | 1.49% | yes |
| [comment.69493.any](inputs/cases/comment.69493.any.json) | oneshot | stripos() loop | 14.809 | 0.48% | yes |
| [comment.69493.any](inputs/cases/comment.69493.any.json) | oneshot | preg_match() [literal] | 25.673 | 1.10% | yes |
| [comment.69493.any](inputs/cases/comment.69493.any.json) | oneshot | preg_match() [prefix] | 1.475 | 0.59% | yes |
| [comment.69493.any](inputs/cases/comment.69493.any.json) | oneshot | strtolower() + strpos() loop | 11.397 | 0.61% | yes |
| [comment.69493.any](inputs/cases/comment.69493.any.json) | oneshot | Native A/A control | 294.996 | 0.54% | yes |
| [comment.69493.unique](inputs/cases/comment.69493.unique.json) | prepared | Matcher::getMatchedKeywords() | 0.337 | 0.59% | yes |
| [comment.69493.unique](inputs/cases/comment.69493.unique.json) | prepared | stripos() loop | 14.904 | 1.32% | yes |
| [comment.69493.unique](inputs/cases/comment.69493.unique.json) | prepared | preg_match_all() [literal] | 12.260 | 1.16% | yes |
| [comment.69493.unique](inputs/cases/comment.69493.unique.json) | prepared | preg_match_all() [prefix] | 7.989 | 0.54% | yes |
| [comment.69493.unique](inputs/cases/comment.69493.unique.json) | prepared | strtolower() + strpos() loop | 11.430 | 0.78% | yes |
| [comment.69493.unique](inputs/cases/comment.69493.unique.json) | prepared | Native A/A control | 0.338 | 0.93% | yes |
| [comment.69493.unique](inputs/cases/comment.69493.unique.json) | oneshot | Matcher::getMatchedKeywords() | 295.781 | 1.87% | yes |
| [comment.69493.unique](inputs/cases/comment.69493.unique.json) | oneshot | stripos() loop | 14.884 | 1.11% | yes |
| [comment.69493.unique](inputs/cases/comment.69493.unique.json) | oneshot | preg_match_all() [literal] | 12.250 | 0.44% | yes |
| [comment.69493.unique](inputs/cases/comment.69493.unique.json) | oneshot | preg_match_all() [prefix] | 7.972 | 0.36% | yes |
| [comment.69493.unique](inputs/cases/comment.69493.unique.json) | oneshot | strtolower() + strpos() loop | 11.437 | 0.56% | yes |
| [comment.69493.unique](inputs/cases/comment.69493.unique.json) | oneshot | Native A/A control | 296.191 | 0.94% | yes |
| [comment.41719.any](inputs/cases/comment.41719.any.json) | prepared | Matcher::matches() | 0.467 | 0.67% | yes |
| [comment.41719.any](inputs/cases/comment.41719.any.json) | prepared | stripos() loop | 19.352 | 0.56% | yes |
| [comment.41719.any](inputs/cases/comment.41719.any.json) | prepared | preg_match() [literal] | 58.517 | 0.66% | yes |
| [comment.41719.any](inputs/cases/comment.41719.any.json) | prepared | preg_match() [prefix] | 2.522 | 1.76% | yes |
| [comment.41719.any](inputs/cases/comment.41719.any.json) | prepared | strtolower() + strpos() loop | 14.625 | 1.36% | yes |
| [comment.41719.any](inputs/cases/comment.41719.any.json) | prepared | Native A/A control | 0.469 | 1.46% | yes |
| [comment.41719.any](inputs/cases/comment.41719.any.json) | oneshot | Matcher::matches() | 296.010 | 0.70% | yes |
| [comment.41719.any](inputs/cases/comment.41719.any.json) | oneshot | stripos() loop | 19.527 | 0.70% | yes |
| [comment.41719.any](inputs/cases/comment.41719.any.json) | oneshot | preg_match() [literal] | 58.120 | 0.67% | yes |
| [comment.41719.any](inputs/cases/comment.41719.any.json) | oneshot | preg_match() [prefix] | 2.499 | 1.82% | yes |
| [comment.41719.any](inputs/cases/comment.41719.any.json) | oneshot | strtolower() + strpos() loop | 14.681 | 1.11% | yes |
| [comment.41719.any](inputs/cases/comment.41719.any.json) | oneshot | Native A/A control | 296.414 | 0.82% | yes |
| [comment.41719.unique](inputs/cases/comment.41719.unique.json) | prepared | Matcher::getMatchedKeywords() | 0.507 | 0.77% | yes |
| [comment.41719.unique](inputs/cases/comment.41719.unique.json) | prepared | stripos() loop | 19.687 | 0.59% | yes |
| [comment.41719.unique](inputs/cases/comment.41719.unique.json) | prepared | preg_match_all() [literal] | 22.612 | 0.96% | yes |
| [comment.41719.unique](inputs/cases/comment.41719.unique.json) | prepared | preg_match_all() [prefix] | 12.856 | 0.68% | yes |
| [comment.41719.unique](inputs/cases/comment.41719.unique.json) | prepared | strtolower() + strpos() loop | 14.801 | 1.33% | yes |
| [comment.41719.unique](inputs/cases/comment.41719.unique.json) | prepared | Native A/A control | 0.508 | 1.26% | yes |
| [comment.41719.unique](inputs/cases/comment.41719.unique.json) | oneshot | Matcher::getMatchedKeywords() | 296.384 | 44.01% | no |
| [comment.41719.unique](inputs/cases/comment.41719.unique.json) | oneshot | stripos() loop | 19.469 | 34.56% | no |
| [comment.41719.unique](inputs/cases/comment.41719.unique.json) | oneshot | preg_match_all() [literal] | 22.098 | 0.68% | no |
| [comment.41719.unique](inputs/cases/comment.41719.unique.json) | oneshot | preg_match_all() [prefix] | 12.807 | 0.89% | no |
| [comment.41719.unique](inputs/cases/comment.41719.unique.json) | oneshot | strtolower() + strpos() loop | 14.760 | 1.40% | no |
| [comment.41719.unique](inputs/cases/comment.41719.unique.json) | oneshot | Native A/A control | 296.292 | 0.96% | no |
| [comment.69503.any](inputs/cases/comment.69503.any.json) | prepared | Matcher::matches() | 0.434 | 1.34% | yes |
| [comment.69503.any](inputs/cases/comment.69503.any.json) | prepared | stripos() loop | 17.729 | 0.66% | yes |
| [comment.69503.any](inputs/cases/comment.69503.any.json) | prepared | preg_match() [literal] | 44.005 | 0.45% | yes |
| [comment.69503.any](inputs/cases/comment.69503.any.json) | prepared | preg_match() [prefix] | 2.064 | 1.70% | yes |
| [comment.69503.any](inputs/cases/comment.69503.any.json) | prepared | strtolower() + strpos() loop | 13.540 | 1.20% | yes |
| [comment.69503.any](inputs/cases/comment.69503.any.json) | prepared | Native A/A control | 0.436 | 0.76% | yes |
| [comment.69503.any](inputs/cases/comment.69503.any.json) | oneshot | Matcher::matches() | 296.028 | 0.89% | yes |
| [comment.69503.any](inputs/cases/comment.69503.any.json) | oneshot | stripos() loop | 17.729 | 0.98% | yes |
| [comment.69503.any](inputs/cases/comment.69503.any.json) | oneshot | preg_match() [literal] | 44.040 | 0.49% | yes |
| [comment.69503.any](inputs/cases/comment.69503.any.json) | oneshot | preg_match() [prefix] | 2.055 | 2.81% | yes |
| [comment.69503.any](inputs/cases/comment.69503.any.json) | oneshot | strtolower() + strpos() loop | 13.526 | 2.44% | yes |
| [comment.69503.any](inputs/cases/comment.69503.any.json) | oneshot | Native A/A control | 296.055 | 0.86% | yes |
| [comment.69503.unique](inputs/cases/comment.69503.unique.json) | prepared | Matcher::getMatchedKeywords() | 0.461 | 1.08% | yes |
| [comment.69503.unique](inputs/cases/comment.69503.unique.json) | prepared | stripos() loop | 17.803 | 0.73% | yes |
| [comment.69503.unique](inputs/cases/comment.69503.unique.json) | prepared | preg_match_all() [literal] | 17.536 | 0.57% | yes |
| [comment.69503.unique](inputs/cases/comment.69503.unique.json) | prepared | preg_match_all() [prefix] | 10.736 | 0.45% | yes |
| [comment.69503.unique](inputs/cases/comment.69503.unique.json) | prepared | strtolower() + strpos() loop | 13.780 | 0.92% | yes |
| [comment.69503.unique](inputs/cases/comment.69503.unique.json) | prepared | Native A/A control | 0.462 | 0.90% | yes |
| [comment.69503.unique](inputs/cases/comment.69503.unique.json) | oneshot | Matcher::getMatchedKeywords() | 295.271 | 0.65% | yes |
| [comment.69503.unique](inputs/cases/comment.69503.unique.json) | oneshot | stripos() loop | 17.844 | 0.71% | yes |
| [comment.69503.unique](inputs/cases/comment.69503.unique.json) | oneshot | preg_match_all() [literal] | 17.574 | 0.64% | yes |
| [comment.69503.unique](inputs/cases/comment.69503.unique.json) | oneshot | preg_match_all() [prefix] | 10.766 | 0.49% | yes |
| [comment.69503.unique](inputs/cases/comment.69503.unique.json) | oneshot | strtolower() + strpos() loop | 13.709 | 1.09% | yes |
| [comment.69503.unique](inputs/cases/comment.69503.unique.json) | oneshot | Native A/A control | 294.902 | 1.61% | yes |
| [comment.41704.any](inputs/cases/comment.41704.any.json) | prepared | Matcher::matches() | 0.500 | 0.77% | yes |
| [comment.41704.any](inputs/cases/comment.41704.any.json) | prepared | stripos() loop | 20.256 | 0.62% | yes |
| [comment.41704.any](inputs/cases/comment.41704.any.json) | prepared | preg_match() [literal] | 58.662 | 0.83% | yes |
| [comment.41704.any](inputs/cases/comment.41704.any.json) | prepared | preg_match() [prefix] | 2.571 | 1.86% | yes |
| [comment.41704.any](inputs/cases/comment.41704.any.json) | prepared | strtolower() + strpos() loop | 15.910 | 1.18% | yes |
| [comment.41704.any](inputs/cases/comment.41704.any.json) | prepared | Native A/A control | 0.500 | 0.47% | yes |
| [comment.41704.any](inputs/cases/comment.41704.any.json) | oneshot | Matcher::matches() | 296.981 | 0.60% | yes |
| [comment.41704.any](inputs/cases/comment.41704.any.json) | oneshot | stripos() loop | 20.406 | 1.02% | yes |
| [comment.41704.any](inputs/cases/comment.41704.any.json) | oneshot | preg_match() [literal] | 58.274 | 0.96% | yes |
| [comment.41704.any](inputs/cases/comment.41704.any.json) | oneshot | preg_match() [prefix] | 2.583 | 1.38% | yes |
| [comment.41704.any](inputs/cases/comment.41704.any.json) | oneshot | strtolower() + strpos() loop | 15.812 | 0.74% | yes |
| [comment.41704.any](inputs/cases/comment.41704.any.json) | oneshot | Native A/A control | 296.549 | 0.85% | yes |
| [comment.41704.unique](inputs/cases/comment.41704.unique.json) | prepared | Matcher::getMatchedKeywords() | 0.534 | 2.07% | yes |
| [comment.41704.unique](inputs/cases/comment.41704.unique.json) | prepared | stripos() loop | 20.394 | 1.95% | yes |
| [comment.41704.unique](inputs/cases/comment.41704.unique.json) | prepared | preg_match_all() [literal] | 22.998 | 2.51% | yes |
| [comment.41704.unique](inputs/cases/comment.41704.unique.json) | prepared | preg_match_all() [prefix] | 13.255 | 2.55% | yes |
| [comment.41704.unique](inputs/cases/comment.41704.unique.json) | prepared | strtolower() + strpos() loop | 15.940 | 2.05% | yes |
| [comment.41704.unique](inputs/cases/comment.41704.unique.json) | prepared | Native A/A control | 0.535 | 0.65% | yes |
| [comment.41704.unique](inputs/cases/comment.41704.unique.json) | oneshot | Matcher::getMatchedKeywords() | 296.328 | 2.01% | yes |
| [comment.41704.unique](inputs/cases/comment.41704.unique.json) | oneshot | stripos() loop | 20.311 | 1.31% | yes |
| [comment.41704.unique](inputs/cases/comment.41704.unique.json) | oneshot | preg_match_all() [literal] | 23.018 | 2.52% | yes |
| [comment.41704.unique](inputs/cases/comment.41704.unique.json) | oneshot | preg_match_all() [prefix] | 13.251 | 3.56% | yes |
| [comment.41704.unique](inputs/cases/comment.41704.unique.json) | oneshot | strtolower() + strpos() loop | 15.912 | 1.89% | yes |
| [comment.41704.unique](inputs/cases/comment.41704.unique.json) | oneshot | Native A/A control | 295.832 | 0.76% | yes |
| [comment.10.any](inputs/cases/comment.10.any.json) | prepared | Matcher::matches() | 0.372 | 0.60% | yes |
| [comment.10.any](inputs/cases/comment.10.any.json) | prepared | stripos() loop | 17.135 | 0.77% | yes |
| [comment.10.any](inputs/cases/comment.10.any.json) | prepared | preg_match() [literal] | 45.351 | 3.13% | yes |
| [comment.10.any](inputs/cases/comment.10.any.json) | prepared | preg_match() [prefix] | 2.108 | 0.78% | yes |
| [comment.10.any](inputs/cases/comment.10.any.json) | prepared | strtolower() + strpos() loop | 12.954 | 1.34% | yes |
| [comment.10.any](inputs/cases/comment.10.any.json) | prepared | Native A/A control | 0.371 | 0.61% | yes |
| [comment.10.any](inputs/cases/comment.10.any.json) | oneshot | Matcher::matches() | 295.451 | 0.84% | yes |
| [comment.10.any](inputs/cases/comment.10.any.json) | oneshot | stripos() loop | 17.130 | 1.58% | yes |
| [comment.10.any](inputs/cases/comment.10.any.json) | oneshot | preg_match() [literal] | 45.123 | 0.49% | yes |
| [comment.10.any](inputs/cases/comment.10.any.json) | oneshot | preg_match() [prefix] | 2.110 | 2.16% | yes |
| [comment.10.any](inputs/cases/comment.10.any.json) | oneshot | strtolower() + strpos() loop | 12.905 | 1.25% | yes |
| [comment.10.any](inputs/cases/comment.10.any.json) | oneshot | Native A/A control | 295.784 | 0.84% | yes |
| [comment.10.unique](inputs/cases/comment.10.unique.json) | prepared | Matcher::getMatchedKeywords() | 0.408 | 0.71% | yes |
| [comment.10.unique](inputs/cases/comment.10.unique.json) | prepared | stripos() loop | 17.162 | 1.33% | yes |
| [comment.10.unique](inputs/cases/comment.10.unique.json) | prepared | preg_match_all() [literal] | 17.938 | 0.42% | yes |
| [comment.10.unique](inputs/cases/comment.10.unique.json) | prepared | preg_match_all() [prefix] | 10.955 | 0.44% | yes |
| [comment.10.unique](inputs/cases/comment.10.unique.json) | prepared | strtolower() + strpos() loop | 13.097 | 0.91% | yes |
| [comment.10.unique](inputs/cases/comment.10.unique.json) | prepared | Native A/A control | 0.408 | 0.71% | yes |
| [comment.10.unique](inputs/cases/comment.10.unique.json) | oneshot | Matcher::getMatchedKeywords() | 298.035 | 0.69% | yes |
| [comment.10.unique](inputs/cases/comment.10.unique.json) | oneshot | stripos() loop | 17.247 | 0.91% | yes |
| [comment.10.unique](inputs/cases/comment.10.unique.json) | oneshot | preg_match_all() [literal] | 17.954 | 0.87% | yes |
| [comment.10.unique](inputs/cases/comment.10.unique.json) | oneshot | preg_match_all() [prefix] | 10.955 | 0.38% | yes |
| [comment.10.unique](inputs/cases/comment.10.unique.json) | oneshot | strtolower() + strpos() loop | 13.119 | 0.91% | yes |
| [comment.10.unique](inputs/cases/comment.10.unique.json) | oneshot | Native A/A control | 298.940 | 0.48% | yes |
| [comment.41698.any](inputs/cases/comment.41698.any.json) | prepared | Matcher::matches() | 0.826 | 0.29% | yes |
| [comment.41698.any](inputs/cases/comment.41698.any.json) | prepared | stripos() loop | 30.013 | 1.04% | yes |
| [comment.41698.any](inputs/cases/comment.41698.any.json) | prepared | preg_match() [literal] | 130.388 | 0.50% | yes |
| [comment.41698.any](inputs/cases/comment.41698.any.json) | prepared | preg_match() [prefix] | 4.908 | 1.14% | yes |
| [comment.41698.any](inputs/cases/comment.41698.any.json) | prepared | strtolower() + strpos() loop | 25.602 | 0.60% | yes |
| [comment.41698.any](inputs/cases/comment.41698.any.json) | prepared | Native A/A control | 0.825 | 0.31% | yes |
| [comment.41698.any](inputs/cases/comment.41698.any.json) | oneshot | Matcher::matches() | 297.329 | 1.37% | yes |
| [comment.41698.any](inputs/cases/comment.41698.any.json) | oneshot | stripos() loop | 29.932 | 0.89% | yes |
| [comment.41698.any](inputs/cases/comment.41698.any.json) | oneshot | preg_match() [literal] | 130.505 | 3.54% | yes |
| [comment.41698.any](inputs/cases/comment.41698.any.json) | oneshot | preg_match() [prefix] | 4.909 | 2.27% | yes |
| [comment.41698.any](inputs/cases/comment.41698.any.json) | oneshot | strtolower() + strpos() loop | 25.661 | 1.60% | yes |
| [comment.41698.any](inputs/cases/comment.41698.any.json) | oneshot | Native A/A control | 296.972 | 0.96% | yes |
| [comment.41698.unique](inputs/cases/comment.41698.unique.json) | prepared | Matcher::getMatchedKeywords() | 0.885 | 2.02% | yes |
| [comment.41698.unique](inputs/cases/comment.41698.unique.json) | prepared | stripos() loop | 30.121 | 1.57% | yes |
| [comment.41698.unique](inputs/cases/comment.41698.unique.json) | prepared | preg_match_all() [literal] | 43.983 | 2.09% | yes |
| [comment.41698.unique](inputs/cases/comment.41698.unique.json) | prepared | preg_match_all() [prefix] | 23.719 | 1.20% | yes |
| [comment.41698.unique](inputs/cases/comment.41698.unique.json) | prepared | strtolower() + strpos() loop | 25.844 | 1.12% | yes |
| [comment.41698.unique](inputs/cases/comment.41698.unique.json) | prepared | Native A/A control | 0.885 | 1.81% | yes |
| [comment.41698.unique](inputs/cases/comment.41698.unique.json) | oneshot | Matcher::getMatchedKeywords() | 295.979 | 2.30% | yes |
| [comment.41698.unique](inputs/cases/comment.41698.unique.json) | oneshot | stripos() loop | 30.571 | 3.15% | yes |
| [comment.41698.unique](inputs/cases/comment.41698.unique.json) | oneshot | preg_match_all() [literal] | 44.263 | 1.75% | yes |
| [comment.41698.unique](inputs/cases/comment.41698.unique.json) | oneshot | preg_match_all() [prefix] | 23.802 | 2.74% | yes |
| [comment.41698.unique](inputs/cases/comment.41698.unique.json) | oneshot | strtolower() + strpos() loop | 25.879 | 1.92% | yes |
| [comment.41698.unique](inputs/cases/comment.41698.unique.json) | oneshot | Native A/A control | 296.522 | 0.67% | yes |
| [comment.97301.any](inputs/cases/comment.97301.any.json) | prepared | Matcher::matches() | 0.378 | 2.70% | yes |
| [comment.97301.any](inputs/cases/comment.97301.any.json) | prepared | stripos() loop | 1.479 | 2.06% | yes |
| [comment.97301.any](inputs/cases/comment.97301.any.json) | prepared | preg_match() [literal] | 36.876 | 3.32% | yes |
| [comment.97301.any](inputs/cases/comment.97301.any.json) | prepared | preg_match() [prefix] | 1.792 | 3.69% | yes |
| [comment.97301.any](inputs/cases/comment.97301.any.json) | prepared | strtolower() + strpos() loop | 1.379 | 0.43% | yes |
| [comment.97301.any](inputs/cases/comment.97301.any.json) | prepared | Native A/A control | 0.379 | 2.26% | yes |
| [comment.97301.any](inputs/cases/comment.97301.any.json) | oneshot | Matcher::matches() | 295.502 | 0.85% | yes |
| [comment.97301.any](inputs/cases/comment.97301.any.json) | oneshot | stripos() loop | 1.484 | 1.91% | yes |
| [comment.97301.any](inputs/cases/comment.97301.any.json) | oneshot | preg_match() [literal] | 36.881 | 3.11% | yes |
| [comment.97301.any](inputs/cases/comment.97301.any.json) | oneshot | preg_match() [prefix] | 1.793 | 4.23% | yes |
| [comment.97301.any](inputs/cases/comment.97301.any.json) | oneshot | strtolower() + strpos() loop | 1.382 | 1.73% | yes |
| [comment.97301.any](inputs/cases/comment.97301.any.json) | oneshot | Native A/A control | 296.052 | 2.05% | yes |
| [comment.97301.unique](inputs/cases/comment.97301.unique.json) | prepared | Matcher::getMatchedKeywords() | 1.023 | 1.92% | yes |
| [comment.97301.unique](inputs/cases/comment.97301.unique.json) | prepared | stripos() loop | 33.835 | 1.39% | yes |
| [comment.97301.unique](inputs/cases/comment.97301.unique.json) | prepared | preg_match_all() [literal] | 49.716 | 3.16% | yes |
| [comment.97301.unique](inputs/cases/comment.97301.unique.json) | prepared | preg_match_all() [prefix] | 26.563 | 3.01% | yes |
| [comment.97301.unique](inputs/cases/comment.97301.unique.json) | prepared | strtolower() + strpos() loop | 28.654 | 1.74% | yes |
| [comment.97301.unique](inputs/cases/comment.97301.unique.json) | prepared | Native A/A control | 1.023 | 1.70% | yes |
| [comment.97301.unique](inputs/cases/comment.97301.unique.json) | oneshot | Matcher::getMatchedKeywords() | 296.577 | 2.06% | yes |
| [comment.97301.unique](inputs/cases/comment.97301.unique.json) | oneshot | stripos() loop | 34.040 | 1.59% | yes |
| [comment.97301.unique](inputs/cases/comment.97301.unique.json) | oneshot | preg_match_all() [literal] | 49.926 | 2.11% | yes |
| [comment.97301.unique](inputs/cases/comment.97301.unique.json) | oneshot | preg_match_all() [prefix] | 26.603 | 0.86% | yes |
| [comment.97301.unique](inputs/cases/comment.97301.unique.json) | oneshot | strtolower() + strpos() loop | 28.632 | 1.67% | yes |
| [comment.97301.unique](inputs/cases/comment.97301.unique.json) | oneshot | Native A/A control | 296.495 | 2.20% | yes |
| [comment.83414.any](inputs/cases/comment.83414.any.json) | prepared | Matcher::matches() | 0.685 | 2.45% | yes |
| [comment.83414.any](inputs/cases/comment.83414.any.json) | prepared | stripos() loop | 26.053 | 1.55% | yes |
| [comment.83414.any](inputs/cases/comment.83414.any.json) | prepared | preg_match() [literal] | 94.052 | 3.48% | yes |
| [comment.83414.any](inputs/cases/comment.83414.any.json) | prepared | preg_match() [prefix] | 3.683 | 2.46% | yes |
| [comment.83414.any](inputs/cases/comment.83414.any.json) | prepared | strtolower() + strpos() loop | 20.541 | 0.96% | yes |
| [comment.83414.any](inputs/cases/comment.83414.any.json) | prepared | Native A/A control | 0.686 | 0.66% | yes |
| [comment.83414.any](inputs/cases/comment.83414.any.json) | oneshot | Matcher::matches() | 295.693 | 1.81% | yes |
| [comment.83414.any](inputs/cases/comment.83414.any.json) | oneshot | stripos() loop | 26.030 | 0.68% | yes |
| [comment.83414.any](inputs/cases/comment.83414.any.json) | oneshot | preg_match() [literal] | 93.904 | 4.33% | yes |
| [comment.83414.any](inputs/cases/comment.83414.any.json) | oneshot | preg_match() [prefix] | 3.675 | 4.80% | yes |
| [comment.83414.any](inputs/cases/comment.83414.any.json) | oneshot | strtolower() + strpos() loop | 20.512 | 1.56% | yes |
| [comment.83414.any](inputs/cases/comment.83414.any.json) | oneshot | Native A/A control | 295.771 | 1.63% | yes |
| [comment.83414.unique](inputs/cases/comment.83414.unique.json) | prepared | Matcher::getMatchedKeywords() | 0.714 | 0.65% | yes |
| [comment.83414.unique](inputs/cases/comment.83414.unique.json) | prepared | stripos() loop | 26.051 | 0.39% | yes |
| [comment.83414.unique](inputs/cases/comment.83414.unique.json) | prepared | preg_match_all() [literal] | 33.164 | 0.66% | yes |
| [comment.83414.unique](inputs/cases/comment.83414.unique.json) | prepared | preg_match_all() [prefix] | 18.328 | 1.21% | yes |
| [comment.83414.unique](inputs/cases/comment.83414.unique.json) | prepared | strtolower() + strpos() loop | 20.852 | 1.55% | yes |
| [comment.83414.unique](inputs/cases/comment.83414.unique.json) | prepared | Native A/A control | 0.718 | 1.15% | yes |
| [comment.83414.unique](inputs/cases/comment.83414.unique.json) | oneshot | Matcher::getMatchedKeywords() | 296.121 | 1.25% | yes |
| [comment.83414.unique](inputs/cases/comment.83414.unique.json) | oneshot | stripos() loop | 26.119 | 1.28% | yes |
| [comment.83414.unique](inputs/cases/comment.83414.unique.json) | oneshot | preg_match_all() [literal] | 33.222 | 2.09% | yes |
| [comment.83414.unique](inputs/cases/comment.83414.unique.json) | oneshot | preg_match_all() [prefix] | 18.287 | 0.57% | yes |
| [comment.83414.unique](inputs/cases/comment.83414.unique.json) | oneshot | strtolower() + strpos() loop | 20.798 | 1.62% | yes |
| [comment.83414.unique](inputs/cases/comment.83414.unique.json) | oneshot | Native A/A control | 295.659 | 2.14% | yes |
| [comment.13918.any](inputs/cases/comment.13918.any.json) | prepared | Matcher::matches() | 0.649 | 0.33% | yes |
| [comment.13918.any](inputs/cases/comment.13918.any.json) | prepared | stripos() loop | 24.854 | 1.46% | yes |
| [comment.13918.any](inputs/cases/comment.13918.any.json) | prepared | preg_match() [literal] | 92.313 | 3.14% | yes |
| [comment.13918.any](inputs/cases/comment.13918.any.json) | prepared | preg_match() [prefix] | 3.649 | 3.21% | yes |
| [comment.13918.any](inputs/cases/comment.13918.any.json) | prepared | strtolower() + strpos() loop | 19.893 | 2.10% | yes |
| [comment.13918.any](inputs/cases/comment.13918.any.json) | prepared | Native A/A control | 0.651 | 0.56% | yes |
| [comment.13918.any](inputs/cases/comment.13918.any.json) | oneshot | Matcher::matches() | 296.354 | 0.69% | yes |
| [comment.13918.any](inputs/cases/comment.13918.any.json) | oneshot | stripos() loop | 24.910 | 0.89% | yes |
| [comment.13918.any](inputs/cases/comment.13918.any.json) | oneshot | preg_match() [literal] | 92.015 | 0.79% | yes |
| [comment.13918.any](inputs/cases/comment.13918.any.json) | oneshot | preg_match() [prefix] | 3.673 | 0.69% | yes |
| [comment.13918.any](inputs/cases/comment.13918.any.json) | oneshot | strtolower() + strpos() loop | 20.201 | 13.12% | yes |
| [comment.13918.any](inputs/cases/comment.13918.any.json) | oneshot | Native A/A control | 297.296 | 1.16% | yes |
| [comment.13918.unique](inputs/cases/comment.13918.unique.json) | prepared | Matcher::getMatchedKeywords() | 0.680 | 0.51% | yes |
| [comment.13918.unique](inputs/cases/comment.13918.unique.json) | prepared | stripos() loop | 24.718 | 0.94% | yes |
| [comment.13918.unique](inputs/cases/comment.13918.unique.json) | prepared | preg_match_all() [literal] | 33.569 | 0.52% | yes |
| [comment.13918.unique](inputs/cases/comment.13918.unique.json) | prepared | preg_match_all() [prefix] | 18.485 | 0.78% | yes |
| [comment.13918.unique](inputs/cases/comment.13918.unique.json) | prepared | strtolower() + strpos() loop | 20.130 | 1.05% | yes |
| [comment.13918.unique](inputs/cases/comment.13918.unique.json) | prepared | Native A/A control | 0.682 | 0.46% | yes |
| [comment.13918.unique](inputs/cases/comment.13918.unique.json) | oneshot | Matcher::getMatchedKeywords() | 296.000 | 0.78% | no |
| [comment.13918.unique](inputs/cases/comment.13918.unique.json) | oneshot | stripos() loop | 24.878 | 4.79% | no |
| [comment.13918.unique](inputs/cases/comment.13918.unique.json) | oneshot | preg_match_all() [literal] | 33.516 | 1.32% | no |
| [comment.13918.unique](inputs/cases/comment.13918.unique.json) | oneshot | preg_match_all() [prefix] | 18.503 | 0.80% | no |
| [comment.13918.unique](inputs/cases/comment.13918.unique.json) | oneshot | strtolower() + strpos() loop | 20.154 | 4.08% | no |
| [comment.13918.unique](inputs/cases/comment.13918.unique.json) | oneshot | Native A/A control | 296.203 | 5.35% | no |
| [comment.41696.any](inputs/cases/comment.41696.any.json) | prepared | Matcher::matches() | 1.062 | 0.35% | yes |
| [comment.41696.any](inputs/cases/comment.41696.any.json) | prepared | stripos() loop | 38.477 | 0.44% | yes |
| [comment.41696.any](inputs/cases/comment.41696.any.json) | prepared | preg_match() [literal] | 180.514 | 0.43% | yes |
| [comment.41696.any](inputs/cases/comment.41696.any.json) | prepared | preg_match() [prefix] | 6.576 | 1.50% | yes |
| [comment.41696.any](inputs/cases/comment.41696.any.json) | prepared | strtolower() + strpos() loop | 32.964 | 0.58% | yes |
| [comment.41696.any](inputs/cases/comment.41696.any.json) | prepared | Native A/A control | 1.064 | 0.38% | yes |
| [comment.41696.any](inputs/cases/comment.41696.any.json) | oneshot | Matcher::matches() | 297.146 | 1.10% | yes |
| [comment.41696.any](inputs/cases/comment.41696.any.json) | oneshot | stripos() loop | 38.168 | 0.66% | yes |
| [comment.41696.any](inputs/cases/comment.41696.any.json) | oneshot | preg_match() [literal] | 180.567 | 0.55% | yes |
| [comment.41696.any](inputs/cases/comment.41696.any.json) | oneshot | preg_match() [prefix] | 6.611 | 0.90% | yes |
| [comment.41696.any](inputs/cases/comment.41696.any.json) | oneshot | strtolower() + strpos() loop | 33.115 | 0.97% | yes |
| [comment.41696.any](inputs/cases/comment.41696.any.json) | oneshot | Native A/A control | 297.521 | 0.79% | yes |
| [comment.41696.unique](inputs/cases/comment.41696.unique.json) | prepared | Matcher::getMatchedKeywords() | 1.117 | 0.77% | yes |
| [comment.41696.unique](inputs/cases/comment.41696.unique.json) | prepared | stripos() loop | 38.334 | 0.77% | yes |
| [comment.41696.unique](inputs/cases/comment.41696.unique.json) | prepared | preg_match_all() [literal] | 60.765 | 0.74% | yes |
| [comment.41696.unique](inputs/cases/comment.41696.unique.json) | prepared | preg_match_all() [prefix] | 31.312 | 1.29% | yes |
| [comment.41696.unique](inputs/cases/comment.41696.unique.json) | prepared | strtolower() + strpos() loop | 33.020 | 0.65% | yes |
| [comment.41696.unique](inputs/cases/comment.41696.unique.json) | prepared | Native A/A control | 1.119 | 0.32% | yes |
| [comment.41696.unique](inputs/cases/comment.41696.unique.json) | oneshot | Matcher::getMatchedKeywords() | 296.404 | 0.87% | yes |
| [comment.41696.unique](inputs/cases/comment.41696.unique.json) | oneshot | stripos() loop | 38.214 | 0.71% | yes |
| [comment.41696.unique](inputs/cases/comment.41696.unique.json) | oneshot | preg_match_all() [literal] | 60.594 | 0.70% | yes |
| [comment.41696.unique](inputs/cases/comment.41696.unique.json) | oneshot | preg_match_all() [prefix] | 31.336 | 1.31% | yes |
| [comment.41696.unique](inputs/cases/comment.41696.unique.json) | oneshot | strtolower() + strpos() loop | 33.151 | 0.84% | yes |
| [comment.41696.unique](inputs/cases/comment.41696.unique.json) | oneshot | Native A/A control | 296.318 | 0.77% | yes |
| [comment.55617.any](inputs/cases/comment.55617.any.json) | prepared | Matcher::matches() | 1.798 | 0.89% | yes |
| [comment.55617.any](inputs/cases/comment.55617.any.json) | prepared | stripos() loop | 74.492 | 0.94% | yes |
| [comment.55617.any](inputs/cases/comment.55617.any.json) | prepared | preg_match() [literal] | 380.179 | 0.88% | yes |
| [comment.55617.any](inputs/cases/comment.55617.any.json) | prepared | preg_match() [prefix] | 13.623 | 1.76% | yes |
| [comment.55617.any](inputs/cases/comment.55617.any.json) | prepared | strtolower() + strpos() loop | 70.389 | 0.51% | yes |
| [comment.55617.any](inputs/cases/comment.55617.any.json) | prepared | Native A/A control | 1.800 | 0.79% | yes |
| [comment.55617.any](inputs/cases/comment.55617.any.json) | oneshot | Matcher::matches() | 297.608 | 0.79% | yes |
| [comment.55617.any](inputs/cases/comment.55617.any.json) | oneshot | stripos() loop | 74.549 | 0.65% | yes |
| [comment.55617.any](inputs/cases/comment.55617.any.json) | oneshot | preg_match() [literal] | 381.843 | 0.57% | yes |
| [comment.55617.any](inputs/cases/comment.55617.any.json) | oneshot | preg_match() [prefix] | 13.741 | 1.61% | yes |
| [comment.55617.any](inputs/cases/comment.55617.any.json) | oneshot | strtolower() + strpos() loop | 70.469 | 1.24% | yes |
| [comment.55617.any](inputs/cases/comment.55617.any.json) | oneshot | Native A/A control | 297.496 | 3.20% | yes |
| [comment.55617.unique](inputs/cases/comment.55617.unique.json) | prepared | Matcher::getMatchedKeywords() | 1.883 | 1.64% | yes |
| [comment.55617.unique](inputs/cases/comment.55617.unique.json) | prepared | stripos() loop | 74.523 | 0.88% | yes |
| [comment.55617.unique](inputs/cases/comment.55617.unique.json) | prepared | preg_match_all() [literal] | 129.186 | 0.72% | yes |
| [comment.55617.unique](inputs/cases/comment.55617.unique.json) | prepared | preg_match_all() [prefix] | 84.867 | 1.78% | yes |
| [comment.55617.unique](inputs/cases/comment.55617.unique.json) | prepared | strtolower() + strpos() loop | 70.805 | 0.71% | yes |
| [comment.55617.unique](inputs/cases/comment.55617.unique.json) | prepared | Native A/A control | 1.886 | 0.49% | yes |
| [comment.55617.unique](inputs/cases/comment.55617.unique.json) | oneshot | Matcher::getMatchedKeywords() | 301.131 | 0.69% | yes |
| [comment.55617.unique](inputs/cases/comment.55617.unique.json) | oneshot | stripos() loop | 74.823 | 0.67% | yes |
| [comment.55617.unique](inputs/cases/comment.55617.unique.json) | oneshot | preg_match_all() [literal] | 128.732 | 0.83% | yes |
| [comment.55617.unique](inputs/cases/comment.55617.unique.json) | oneshot | preg_match_all() [prefix] | 85.166 | 1.68% | yes |
| [comment.55617.unique](inputs/cases/comment.55617.unique.json) | oneshot | strtolower() + strpos() loop | 70.742 | 1.26% | yes |
| [comment.55617.unique](inputs/cases/comment.55617.unique.json) | oneshot | Native A/A control | 301.774 | 0.90% | yes |
| [comment.69522.any](inputs/cases/comment.69522.any.json) | prepared | Matcher::matches() | 0.806 | 0.57% | yes |
| [comment.69522.any](inputs/cases/comment.69522.any.json) | prepared | stripos() loop | 2.145 | 0.69% | yes |
| [comment.69522.any](inputs/cases/comment.69522.any.json) | prepared | preg_match() [literal] | 120.021 | 1.29% | yes |
| [comment.69522.any](inputs/cases/comment.69522.any.json) | prepared | preg_match() [prefix] | 4.439 | 1.44% | yes |
| [comment.69522.any](inputs/cases/comment.69522.any.json) | prepared | strtolower() + strpos() loop | 2.119 | 0.35% | yes |
| [comment.69522.any](inputs/cases/comment.69522.any.json) | prepared | Native A/A control | 0.808 | 0.80% | yes |
| [comment.69522.any](inputs/cases/comment.69522.any.json) | oneshot | Matcher::matches() | 298.750 | 0.63% | yes |
| [comment.69522.any](inputs/cases/comment.69522.any.json) | oneshot | stripos() loop | 2.141 | 0.89% | yes |
| [comment.69522.any](inputs/cases/comment.69522.any.json) | oneshot | preg_match() [literal] | 119.825 | 1.50% | yes |
| [comment.69522.any](inputs/cases/comment.69522.any.json) | oneshot | preg_match() [prefix] | 4.505 | 2.36% | yes |
| [comment.69522.any](inputs/cases/comment.69522.any.json) | oneshot | strtolower() + strpos() loop | 2.118 | 0.92% | yes |
| [comment.69522.any](inputs/cases/comment.69522.any.json) | oneshot | Native A/A control | 298.315 | 0.86% | yes |
| [comment.69522.unique](inputs/cases/comment.69522.unique.json) | prepared | Matcher::getMatchedKeywords() | 1.432 | 0.82% | yes |
| [comment.69522.unique](inputs/cases/comment.69522.unique.json) | prepared | stripos() loop | 45.951 | 0.77% | yes |
| [comment.69522.unique](inputs/cases/comment.69522.unique.json) | prepared | preg_match_all() [literal] | 76.263 | 1.41% | yes |
| [comment.69522.unique](inputs/cases/comment.69522.unique.json) | prepared | preg_match_all() [prefix] | 39.595 | 1.79% | yes |
| [comment.69522.unique](inputs/cases/comment.69522.unique.json) | prepared | strtolower() + strpos() loop | 41.844 | 0.73% | yes |
| [comment.69522.unique](inputs/cases/comment.69522.unique.json) | prepared | Native A/A control | 1.435 | 1.50% | yes |
| [comment.69522.unique](inputs/cases/comment.69522.unique.json) | oneshot | Matcher::getMatchedKeywords() | 297.598 | 0.78% | yes |
| [comment.69522.unique](inputs/cases/comment.69522.unique.json) | oneshot | stripos() loop | 46.035 | 0.87% | yes |
| [comment.69522.unique](inputs/cases/comment.69522.unique.json) | oneshot | preg_match_all() [literal] | 76.452 | 1.15% | yes |
| [comment.69522.unique](inputs/cases/comment.69522.unique.json) | oneshot | preg_match_all() [prefix] | 39.698 | 1.42% | yes |
| [comment.69522.unique](inputs/cases/comment.69522.unique.json) | oneshot | strtolower() + strpos() loop | 41.980 | 0.80% | yes |
| [comment.69522.unique](inputs/cases/comment.69522.unique.json) | oneshot | Native A/A control | 296.953 | 0.81% | yes |
| [comment.13909.any](inputs/cases/comment.13909.any.json) | prepared | Matcher::matches() | 1.072 | 1.24% | yes |
| [comment.13909.any](inputs/cases/comment.13909.any.json) | prepared | stripos() loop | 39.315 | 0.67% | yes |
| [comment.13909.any](inputs/cases/comment.13909.any.json) | prepared | preg_match() [literal] | 181.355 | 0.88% | yes |
| [comment.13909.any](inputs/cases/comment.13909.any.json) | prepared | preg_match() [prefix] | 6.715 | 1.53% | yes |
| [comment.13909.any](inputs/cases/comment.13909.any.json) | prepared | strtolower() + strpos() loop | 34.345 | 0.33% | yes |
| [comment.13909.any](inputs/cases/comment.13909.any.json) | prepared | Native A/A control | 1.072 | 4.74% | yes |
| [comment.13909.any](inputs/cases/comment.13909.any.json) | oneshot | Matcher::matches() | 297.333 | 0.92% | yes |
| [comment.13909.any](inputs/cases/comment.13909.any.json) | oneshot | stripos() loop | 39.331 | 1.59% | yes |
| [comment.13909.any](inputs/cases/comment.13909.any.json) | oneshot | preg_match() [literal] | 181.373 | 0.91% | yes |
| [comment.13909.any](inputs/cases/comment.13909.any.json) | oneshot | preg_match() [prefix] | 6.747 | 1.18% | yes |
| [comment.13909.any](inputs/cases/comment.13909.any.json) | oneshot | strtolower() + strpos() loop | 34.416 | 1.01% | yes |
| [comment.13909.any](inputs/cases/comment.13909.any.json) | oneshot | Native A/A control | 297.565 | 0.81% | yes |
| [comment.13909.unique](inputs/cases/comment.13909.unique.json) | prepared | Matcher::getMatchedKeywords() | 1.121 | 0.50% | yes |
| [comment.13909.unique](inputs/cases/comment.13909.unique.json) | prepared | stripos() loop | 39.354 | 0.43% | yes |
| [comment.13909.unique](inputs/cases/comment.13909.unique.json) | prepared | preg_match_all() [literal] | 60.173 | 0.89% | yes |
| [comment.13909.unique](inputs/cases/comment.13909.unique.json) | prepared | preg_match_all() [prefix] | 31.609 | 0.60% | yes |
| [comment.13909.unique](inputs/cases/comment.13909.unique.json) | prepared | strtolower() + strpos() loop | 34.325 | 0.61% | yes |
| [comment.13909.unique](inputs/cases/comment.13909.unique.json) | prepared | Native A/A control | 1.127 | 0.50% | yes |
| [comment.13909.unique](inputs/cases/comment.13909.unique.json) | oneshot | Matcher::getMatchedKeywords() | 297.680 | 0.86% | yes |
| [comment.13909.unique](inputs/cases/comment.13909.unique.json) | oneshot | stripos() loop | 39.368 | 1.26% | yes |
| [comment.13909.unique](inputs/cases/comment.13909.unique.json) | oneshot | preg_match_all() [literal] | 60.035 | 0.60% | yes |
| [comment.13909.unique](inputs/cases/comment.13909.unique.json) | oneshot | preg_match_all() [prefix] | 31.685 | 2.87% | yes |
| [comment.13909.unique](inputs/cases/comment.13909.unique.json) | oneshot | strtolower() + strpos() loop | 34.307 | 6.73% | yes |
| [comment.13909.unique](inputs/cases/comment.13909.unique.json) | oneshot | Native A/A control | 297.580 | 1.14% | yes |
| [document.pickle.unique](inputs/cases/document.pickle.unique.json) | prepared | Matcher::getMatchedKeywords() | 119.394 | 0.96% | yes |
| [document.pickle.unique](inputs/cases/document.pickle.unique.json) | prepared | strpos() loop | 413.699 | 0.45% | yes |
| [document.pickle.unique](inputs/cases/document.pickle.unique.json) | prepared | preg_match_all() [literal] | 730.598 | 0.67% | yes |
| [document.pickle.unique](inputs/cases/document.pickle.unique.json) | prepared | preg_match_all() [prefix] | 757.155 | 0.54% | yes |
| [document.pickle.unique](inputs/cases/document.pickle.unique.json) | prepared | Native A/A control | 119.374 | 0.94% | yes |
| [document.pickle.unique](inputs/cases/document.pickle.unique.json) | oneshot | Matcher::getMatchedKeywords() | 155.945 | 0.95% | yes |
| [document.pickle.unique](inputs/cases/document.pickle.unique.json) | oneshot | strpos() loop | 413.135 | 0.37% | yes |
| [document.pickle.unique](inputs/cases/document.pickle.unique.json) | oneshot | preg_match_all() [literal] | 729.638 | 0.59% | yes |
| [document.pickle.unique](inputs/cases/document.pickle.unique.json) | oneshot | preg_match_all() [prefix] | 756.360 | 8.80% | yes |
| [document.pickle.unique](inputs/cases/document.pickle.unique.json) | oneshot | Native A/A control | 156.019 | 0.69% | yes |
| [document.pickle.count](inputs/cases/document.pickle.count.json) | prepared | Matcher::countMatches() | 111.651 | 2.35% | yes |
| [document.pickle.count](inputs/cases/document.pickle.count.json) | prepared | strpos() loop | 450.149 | 0.80% | yes |
| [document.pickle.count](inputs/cases/document.pickle.count.json) | prepared | preg_match_all() [literal] | 719.722 | 0.41% | yes |
| [document.pickle.count](inputs/cases/document.pickle.count.json) | prepared | preg_match_all() [prefix] | 744.389 | 0.89% | yes |
| [document.pickle.count](inputs/cases/document.pickle.count.json) | prepared | Native A/A control | 111.978 | 3.46% | yes |
| [document.pickle.count](inputs/cases/document.pickle.count.json) | oneshot | Matcher::countMatches() | 148.767 | 1.58% | yes |
| [document.pickle.count](inputs/cases/document.pickle.count.json) | oneshot | strpos() loop | 448.949 | 0.36% | yes |
| [document.pickle.count](inputs/cases/document.pickle.count.json) | oneshot | preg_match_all() [literal] | 716.772 | 0.90% | yes |
| [document.pickle.count](inputs/cases/document.pickle.count.json) | oneshot | preg_match_all() [prefix] | 740.453 | 0.38% | yes |
| [document.pickle.count](inputs/cases/document.pickle.count.json) | oneshot | Native A/A control | 149.346 | 1.25% | yes |
| [document.pickle.all](inputs/cases/document.pickle.all.json) | prepared | Matcher::matchAll() | 118.258 | 1.82% | yes |
| [document.pickle.all](inputs/cases/document.pickle.all.json) | prepared | strpos() loop | 462.443 | 0.28% | yes |
| [document.pickle.all](inputs/cases/document.pickle.all.json) | prepared | preg_match_all() [literal] | 735.228 | 0.73% | yes |
| [document.pickle.all](inputs/cases/document.pickle.all.json) | prepared | preg_match_all() [prefix] | 763.703 | 8.39% | yes |
| [document.pickle.all](inputs/cases/document.pickle.all.json) | prepared | Native A/A control | 118.039 | 0.95% | yes |
| [document.pickle.all](inputs/cases/document.pickle.all.json) | oneshot | Matcher::matchAll() | 149.283 | 1.29% | yes |
| [document.pickle.all](inputs/cases/document.pickle.all.json) | oneshot | strpos() loop | 463.257 | 0.69% | yes |
| [document.pickle.all](inputs/cases/document.pickle.all.json) | oneshot | preg_match_all() [literal] | 736.552 | 0.55% | yes |
| [document.pickle.all](inputs/cases/document.pickle.all.json) | oneshot | preg_match_all() [prefix] | 764.642 | 0.49% | yes |
| [document.pickle.all](inputs/cases/document.pickle.all.json) | oneshot | Native A/A control | 149.741 | 3.46% | yes |
| [document.pickle.replace](inputs/cases/document.pickle.replace.json) | prepared | Replacer::replace() | 107.187 | 4.47% | yes |
| [document.pickle.replace](inputs/cases/document.pickle.replace.json) | prepared | strtr() | 1384.048 | 0.89% | yes |
| [document.pickle.replace](inputs/cases/document.pickle.replace.json) | prepared | preg_replace_callback() [literal] | 323.701 | 1.30% | yes |
| [document.pickle.replace](inputs/cases/document.pickle.replace.json) | prepared | preg_replace_callback() [prefix] | 234.382 | 4.06% | yes |
| [document.pickle.replace](inputs/cases/document.pickle.replace.json) | prepared | str_replace() | 508.387 | 3.89% | yes |
| [document.pickle.replace](inputs/cases/document.pickle.replace.json) | prepared | Native A/A control | 107.696 | 4.51% | yes |
| [document.pickle.replace](inputs/cases/document.pickle.replace.json) | oneshot | Replacer::replace() | 126.648 | 3.69% | yes |
| [document.pickle.replace](inputs/cases/document.pickle.replace.json) | oneshot | strtr() | 1381.034 | 0.87% | yes |
| [document.pickle.replace](inputs/cases/document.pickle.replace.json) | oneshot | preg_replace_callback() [literal] | 321.256 | 1.09% | yes |
| [document.pickle.replace](inputs/cases/document.pickle.replace.json) | oneshot | preg_replace_callback() [prefix] | 234.267 | 4.72% | yes |
| [document.pickle.replace](inputs/cases/document.pickle.replace.json) | oneshot | str_replace() | 509.077 | 0.65% | yes |
| [document.pickle.replace](inputs/cases/document.pickle.replace.json) | oneshot | Native A/A control | 127.142 | 2.00% | yes |
| [document.urlparse.unique](inputs/cases/document.urlparse.unique.json) | prepared | Matcher::getMatchedKeywords() | 42.038 | 1.29% | yes |
| [document.urlparse.unique](inputs/cases/document.urlparse.unique.json) | prepared | strpos() loop | 157.176 | 1.82% | yes |
| [document.urlparse.unique](inputs/cases/document.urlparse.unique.json) | prepared | preg_match_all() [literal] | 270.543 | 2.15% | yes |
| [document.urlparse.unique](inputs/cases/document.urlparse.unique.json) | prepared | preg_match_all() [prefix] | 281.059 | 0.57% | yes |
| [document.urlparse.unique](inputs/cases/document.urlparse.unique.json) | prepared | Native A/A control | 41.977 | 1.41% | yes |
| [document.urlparse.unique](inputs/cases/document.urlparse.unique.json) | oneshot | Matcher::getMatchedKeywords() | 76.393 | 1.04% | yes |
| [document.urlparse.unique](inputs/cases/document.urlparse.unique.json) | oneshot | strpos() loop | 157.294 | 0.53% | yes |
| [document.urlparse.unique](inputs/cases/document.urlparse.unique.json) | oneshot | preg_match_all() [literal] | 269.441 | 1.43% | yes |
| [document.urlparse.unique](inputs/cases/document.urlparse.unique.json) | oneshot | preg_match_all() [prefix] | 280.875 | 0.70% | yes |
| [document.urlparse.unique](inputs/cases/document.urlparse.unique.json) | oneshot | Native A/A control | 76.330 | 1.06% | yes |
| [document.urlparse.count](inputs/cases/document.urlparse.count.json) | prepared | Matcher::countMatches() | 33.957 | 0.92% | yes |
| [document.urlparse.count](inputs/cases/document.urlparse.count.json) | prepared | strpos() loop | 161.179 | 0.67% | yes |
| [document.urlparse.count](inputs/cases/document.urlparse.count.json) | prepared | preg_match_all() [literal] | 262.758 | 0.74% | yes |
| [document.urlparse.count](inputs/cases/document.urlparse.count.json) | prepared | preg_match_all() [prefix] | 272.437 | 0.40% | yes |
| [document.urlparse.count](inputs/cases/document.urlparse.count.json) | prepared | Native A/A control | 34.012 | 0.47% | yes |
| [document.urlparse.count](inputs/cases/document.urlparse.count.json) | oneshot | Matcher::countMatches() | 72.157 | 0.78% | yes |
| [document.urlparse.count](inputs/cases/document.urlparse.count.json) | oneshot | strpos() loop | 161.164 | 0.56% | yes |
| [document.urlparse.count](inputs/cases/document.urlparse.count.json) | oneshot | preg_match_all() [literal] | 262.379 | 0.58% | yes |
| [document.urlparse.count](inputs/cases/document.urlparse.count.json) | oneshot | preg_match_all() [prefix] | 273.322 | 0.55% | yes |
| [document.urlparse.count](inputs/cases/document.urlparse.count.json) | oneshot | Native A/A control | 72.238 | 0.97% | yes |
| [document.urlparse.all](inputs/cases/document.urlparse.all.json) | prepared | Matcher::matchAll() | 46.389 | 0.39% | yes |
| [document.urlparse.all](inputs/cases/document.urlparse.all.json) | prepared | strpos() loop | 167.650 | 0.54% | yes |
| [document.urlparse.all](inputs/cases/document.urlparse.all.json) | prepared | preg_match_all() [literal] | 271.885 | 0.76% | yes |
| [document.urlparse.all](inputs/cases/document.urlparse.all.json) | prepared | preg_match_all() [prefix] | 282.288 | 0.65% | yes |
| [document.urlparse.all](inputs/cases/document.urlparse.all.json) | prepared | Native A/A control | 46.389 | 0.49% | yes |
| [document.urlparse.all](inputs/cases/document.urlparse.all.json) | oneshot | Matcher::matchAll() | 77.518 | 1.13% | yes |
| [document.urlparse.all](inputs/cases/document.urlparse.all.json) | oneshot | strpos() loop | 167.722 | 0.67% | yes |
| [document.urlparse.all](inputs/cases/document.urlparse.all.json) | oneshot | preg_match_all() [literal] | 271.303 | 0.77% | yes |
| [document.urlparse.all](inputs/cases/document.urlparse.all.json) | oneshot | preg_match_all() [prefix] | 282.976 | 0.45% | yes |
| [document.urlparse.all](inputs/cases/document.urlparse.all.json) | oneshot | Native A/A control | 77.645 | 2.23% | yes |
| [document.urlparse.replace](inputs/cases/document.urlparse.replace.json) | prepared | Replacer::replace() | 36.024 | 1.65% | yes |
| [document.urlparse.replace](inputs/cases/document.urlparse.replace.json) | prepared | strtr() | 480.596 | 0.92% | yes |
| [document.urlparse.replace](inputs/cases/document.urlparse.replace.json) | prepared | preg_replace_callback() [literal] | 116.093 | 1.15% | yes |
| [document.urlparse.replace](inputs/cases/document.urlparse.replace.json) | prepared | preg_replace_callback() [prefix] | 62.881 | 1.43% | yes |
| [document.urlparse.replace](inputs/cases/document.urlparse.replace.json) | prepared | str_replace() | 168.387 | 1.15% | yes |
| [document.urlparse.replace](inputs/cases/document.urlparse.replace.json) | prepared | Native A/A control | 36.095 | 1.22% | yes |
| [document.urlparse.replace](inputs/cases/document.urlparse.replace.json) | oneshot | Replacer::replace() | 53.691 | 0.71% | yes |
| [document.urlparse.replace](inputs/cases/document.urlparse.replace.json) | oneshot | strtr() | 479.951 | 0.92% | yes |
| [document.urlparse.replace](inputs/cases/document.urlparse.replace.json) | oneshot | preg_replace_callback() [literal] | 115.445 | 1.26% | yes |
| [document.urlparse.replace](inputs/cases/document.urlparse.replace.json) | oneshot | preg_replace_callback() [prefix] | 62.363 | 1.80% | yes |
| [document.urlparse.replace](inputs/cases/document.urlparse.replace.json) | oneshot | str_replace() | 168.066 | 0.62% | yes |
| [document.urlparse.replace](inputs/cases/document.urlparse.replace.json) | oneshot | Native A/A control | 53.820 | 0.89% | yes |
| [document.httplib.unique](inputs/cases/document.httplib.unique.json) | prepared | Matcher::getMatchedKeywords() | 63.304 | 0.32% | yes |
| [document.httplib.unique](inputs/cases/document.httplib.unique.json) | prepared | strpos() loop | 308.065 | 0.79% | yes |
| [document.httplib.unique](inputs/cases/document.httplib.unique.json) | prepared | preg_match_all() [literal] | 453.028 | 0.45% | yes |
| [document.httplib.unique](inputs/cases/document.httplib.unique.json) | prepared | preg_match_all() [prefix] | 472.933 | 0.82% | yes |
| [document.httplib.unique](inputs/cases/document.httplib.unique.json) | prepared | Native A/A control | 63.354 | 0.45% | yes |
| [document.httplib.unique](inputs/cases/document.httplib.unique.json) | oneshot | Matcher::getMatchedKeywords() | 99.658 | 0.78% | yes |
| [document.httplib.unique](inputs/cases/document.httplib.unique.json) | oneshot | strpos() loop | 308.407 | 0.90% | yes |
| [document.httplib.unique](inputs/cases/document.httplib.unique.json) | oneshot | preg_match_all() [literal] | 452.795 | 0.60% | yes |
| [document.httplib.unique](inputs/cases/document.httplib.unique.json) | oneshot | preg_match_all() [prefix] | 473.395 | 0.50% | yes |
| [document.httplib.unique](inputs/cases/document.httplib.unique.json) | oneshot | Native A/A control | 99.667 | 0.69% | yes |
| [document.httplib.count](inputs/cases/document.httplib.count.json) | prepared | Matcher::countMatches() | 56.306 | 1.13% | yes |
| [document.httplib.count](inputs/cases/document.httplib.count.json) | prepared | strpos() loop | 323.112 | 0.41% | yes |
| [document.httplib.count](inputs/cases/document.httplib.count.json) | prepared | preg_match_all() [literal] | 445.508 | 0.84% | yes |
| [document.httplib.count](inputs/cases/document.httplib.count.json) | prepared | preg_match_all() [prefix] | 465.392 | 0.54% | yes |
| [document.httplib.count](inputs/cases/document.httplib.count.json) | prepared | Native A/A control | 56.364 | 0.67% | yes |
| [document.httplib.count](inputs/cases/document.httplib.count.json) | oneshot | Matcher::countMatches() | 95.431 | 1.02% | yes |
| [document.httplib.count](inputs/cases/document.httplib.count.json) | oneshot | strpos() loop | 323.420 | 0.40% | yes |
| [document.httplib.count](inputs/cases/document.httplib.count.json) | oneshot | preg_match_all() [literal] | 445.416 | 0.88% | yes |
| [document.httplib.count](inputs/cases/document.httplib.count.json) | oneshot | preg_match_all() [prefix] | 465.428 | 0.30% | yes |
| [document.httplib.count](inputs/cases/document.httplib.count.json) | oneshot | Native A/A control | 95.668 | 0.78% | yes |
| [document.httplib.all](inputs/cases/document.httplib.all.json) | prepared | Matcher::matchAll() | 72.674 | 0.64% | yes |
| [document.httplib.all](inputs/cases/document.httplib.all.json) | prepared | strpos() loop | 329.088 | 0.66% | yes |
| [document.httplib.all](inputs/cases/document.httplib.all.json) | prepared | preg_match_all() [literal] | 454.102 | 0.39% | yes |
| [document.httplib.all](inputs/cases/document.httplib.all.json) | prepared | preg_match_all() [prefix] | 473.356 | 0.70% | yes |
| [document.httplib.all](inputs/cases/document.httplib.all.json) | prepared | Native A/A control | 72.659 | 0.55% | yes |
| [document.httplib.all](inputs/cases/document.httplib.all.json) | oneshot | Matcher::matchAll() | 103.964 | 0.85% | yes |
| [document.httplib.all](inputs/cases/document.httplib.all.json) | oneshot | strpos() loop | 329.785 | 0.58% | yes |
| [document.httplib.all](inputs/cases/document.httplib.all.json) | oneshot | preg_match_all() [literal] | 455.775 | 0.55% | yes |
| [document.httplib.all](inputs/cases/document.httplib.all.json) | oneshot | preg_match_all() [prefix] | 475.170 | 0.51% | yes |
| [document.httplib.all](inputs/cases/document.httplib.all.json) | oneshot | Native A/A control | 104.074 | 1.01% | yes |
| [document.httplib.replace](inputs/cases/document.httplib.replace.json) | prepared | Replacer::replace() | 56.716 | 2.91% | yes |
| [document.httplib.replace](inputs/cases/document.httplib.replace.json) | prepared | strtr() | 631.618 | 4.78% | yes |
| [document.httplib.replace](inputs/cases/document.httplib.replace.json) | prepared | preg_replace_callback() [literal] | 166.220 | 2.17% | yes |
| [document.httplib.replace](inputs/cases/document.httplib.replace.json) | prepared | preg_replace_callback() [prefix] | 105.776 | 1.31% | yes |
| [document.httplib.replace](inputs/cases/document.httplib.replace.json) | prepared | str_replace() | 341.618 | 0.72% | yes |
| [document.httplib.replace](inputs/cases/document.httplib.replace.json) | prepared | Native A/A control | 56.730 | 2.47% | yes |
| [document.httplib.replace](inputs/cases/document.httplib.replace.json) | oneshot | Replacer::replace() | 74.796 | 1.05% | yes |
| [document.httplib.replace](inputs/cases/document.httplib.replace.json) | oneshot | strtr() | 631.679 | 0.92% | yes |
| [document.httplib.replace](inputs/cases/document.httplib.replace.json) | oneshot | preg_replace_callback() [literal] | 165.460 | 0.78% | yes |
| [document.httplib.replace](inputs/cases/document.httplib.replace.json) | oneshot | preg_replace_callback() [prefix] | 105.572 | 1.20% | yes |
| [document.httplib.replace](inputs/cases/document.httplib.replace.json) | oneshot | str_replace() | 342.250 | 0.58% | yes |
| [document.httplib.replace](inputs/cases/document.httplib.replace.json) | oneshot | Native A/A control | 74.695 | 1.10% | yes |
| [document.simplexmlrpcserver.unique](inputs/cases/document.simplexmlrpcserver.unique.json) | prepared | Matcher::getMatchedKeywords() | 28.445 | 0.52% | yes |
| [document.simplexmlrpcserver.unique](inputs/cases/document.simplexmlrpcserver.unique.json) | prepared | strpos() loop | 103.152 | 0.70% | yes |
| [document.simplexmlrpcserver.unique](inputs/cases/document.simplexmlrpcserver.unique.json) | prepared | preg_match_all() [literal] | 198.553 | 0.71% | yes |
| [document.simplexmlrpcserver.unique](inputs/cases/document.simplexmlrpcserver.unique.json) | prepared | preg_match_all() [prefix] | 208.852 | 0.70% | yes |
| [document.simplexmlrpcserver.unique](inputs/cases/document.simplexmlrpcserver.unique.json) | prepared | Native A/A control | 28.435 | 0.61% | yes |
| [document.simplexmlrpcserver.unique](inputs/cases/document.simplexmlrpcserver.unique.json) | oneshot | Matcher::getMatchedKeywords() | 61.574 | 1.26% | yes |
| [document.simplexmlrpcserver.unique](inputs/cases/document.simplexmlrpcserver.unique.json) | oneshot | strpos() loop | 103.159 | 0.67% | yes |
| [document.simplexmlrpcserver.unique](inputs/cases/document.simplexmlrpcserver.unique.json) | oneshot | preg_match_all() [literal] | 198.413 | 1.25% | yes |
| [document.simplexmlrpcserver.unique](inputs/cases/document.simplexmlrpcserver.unique.json) | oneshot | preg_match_all() [prefix] | 210.466 | 0.70% | yes |
| [document.simplexmlrpcserver.unique](inputs/cases/document.simplexmlrpcserver.unique.json) | oneshot | Native A/A control | 61.508 | 0.92% | yes |
| [document.simplexmlrpcserver.count](inputs/cases/document.simplexmlrpcserver.count.json) | prepared | Matcher::countMatches() | 26.484 | 1.21% | yes |
| [document.simplexmlrpcserver.count](inputs/cases/document.simplexmlrpcserver.count.json) | prepared | strpos() loop | 114.633 | 0.60% | yes |
| [document.simplexmlrpcserver.count](inputs/cases/document.simplexmlrpcserver.count.json) | prepared | preg_match_all() [literal] | 188.316 | 1.04% | yes |
| [document.simplexmlrpcserver.count](inputs/cases/document.simplexmlrpcserver.count.json) | prepared | preg_match_all() [prefix] | 199.625 | 0.75% | yes |
| [document.simplexmlrpcserver.count](inputs/cases/document.simplexmlrpcserver.count.json) | prepared | Native A/A control | 26.520 | 1.90% | yes |
| [document.simplexmlrpcserver.count](inputs/cases/document.simplexmlrpcserver.count.json) | oneshot | Matcher::countMatches() | 63.551 | 1.04% | yes |
| [document.simplexmlrpcserver.count](inputs/cases/document.simplexmlrpcserver.count.json) | oneshot | strpos() loop | 114.560 | 0.30% | yes |
| [document.simplexmlrpcserver.count](inputs/cases/document.simplexmlrpcserver.count.json) | oneshot | preg_match_all() [literal] | 187.994 | 1.04% | yes |
| [document.simplexmlrpcserver.count](inputs/cases/document.simplexmlrpcserver.count.json) | oneshot | preg_match_all() [prefix] | 199.301 | 0.67% | yes |
| [document.simplexmlrpcserver.count](inputs/cases/document.simplexmlrpcserver.count.json) | oneshot | Native A/A control | 63.633 | 0.90% | yes |
| [document.simplexmlrpcserver.all](inputs/cases/document.simplexmlrpcserver.all.json) | prepared | Matcher::matchAll() | 32.635 | 2.29% | yes |
| [document.simplexmlrpcserver.all](inputs/cases/document.simplexmlrpcserver.all.json) | prepared | strpos() loop | 124.213 | 0.89% | yes |
| [document.simplexmlrpcserver.all](inputs/cases/document.simplexmlrpcserver.all.json) | prepared | preg_match_all() [literal] | 203.162 | 0.96% | yes |
| [document.simplexmlrpcserver.all](inputs/cases/document.simplexmlrpcserver.all.json) | prepared | preg_match_all() [prefix] | 214.831 | 0.50% | yes |
| [document.simplexmlrpcserver.all](inputs/cases/document.simplexmlrpcserver.all.json) | prepared | Native A/A control | 32.612 | 1.15% | yes |
| [document.simplexmlrpcserver.all](inputs/cases/document.simplexmlrpcserver.all.json) | oneshot | Matcher::matchAll() | 64.474 | 3.03% | yes |
| [document.simplexmlrpcserver.all](inputs/cases/document.simplexmlrpcserver.all.json) | oneshot | strpos() loop | 124.220 | 0.62% | yes |
| [document.simplexmlrpcserver.all](inputs/cases/document.simplexmlrpcserver.all.json) | oneshot | preg_match_all() [literal] | 202.791 | 0.90% | yes |
| [document.simplexmlrpcserver.all](inputs/cases/document.simplexmlrpcserver.all.json) | oneshot | preg_match_all() [prefix] | 213.784 | 0.63% | yes |
| [document.simplexmlrpcserver.all](inputs/cases/document.simplexmlrpcserver.all.json) | oneshot | Native A/A control | 64.423 | 0.65% | yes |
| [document.simplexmlrpcserver.replace](inputs/cases/document.simplexmlrpcserver.replace.json) | prepared | Replacer::replace() | 24.471 | 4.15% | yes |
| [document.simplexmlrpcserver.replace](inputs/cases/document.simplexmlrpcserver.replace.json) | prepared | strtr() | 362.674 | 0.60% | yes |
| [document.simplexmlrpcserver.replace](inputs/cases/document.simplexmlrpcserver.replace.json) | prepared | preg_replace_callback() [literal] | 85.161 | 0.49% | yes |
| [document.simplexmlrpcserver.replace](inputs/cases/document.simplexmlrpcserver.replace.json) | prepared | preg_replace_callback() [prefix] | 45.182 | 2.18% | yes |
| [document.simplexmlrpcserver.replace](inputs/cases/document.simplexmlrpcserver.replace.json) | prepared | str_replace() | 123.337 | 0.50% | yes |
| [document.simplexmlrpcserver.replace](inputs/cases/document.simplexmlrpcserver.replace.json) | prepared | Native A/A control | 24.511 | 3.78% | yes |
| [document.simplexmlrpcserver.replace](inputs/cases/document.simplexmlrpcserver.replace.json) | oneshot | Replacer::replace() | 42.622 | 2.44% | yes |
| [document.simplexmlrpcserver.replace](inputs/cases/document.simplexmlrpcserver.replace.json) | oneshot | strtr() | 363.301 | 0.99% | yes |
| [document.simplexmlrpcserver.replace](inputs/cases/document.simplexmlrpcserver.replace.json) | oneshot | preg_replace_callback() [literal] | 85.439 | 6.77% | yes |
| [document.simplexmlrpcserver.replace](inputs/cases/document.simplexmlrpcserver.replace.json) | oneshot | preg_replace_callback() [prefix] | 45.277 | 3.29% | yes |
| [document.simplexmlrpcserver.replace](inputs/cases/document.simplexmlrpcserver.replace.json) | oneshot | str_replace() | 123.197 | 0.46% | yes |
| [document.simplexmlrpcserver.replace](inputs/cases/document.simplexmlrpcserver.replace.json) | oneshot | Native A/A control | 42.512 | 1.65% | yes |
| [document.cookielib.unique](inputs/cases/document.cookielib.unique.json) | prepared | Matcher::getMatchedKeywords() | 83.877 | 4.10% | yes |
| [document.cookielib.unique](inputs/cases/document.cookielib.unique.json) | prepared | strpos() loop | 298.059 | 2.21% | yes |
| [document.cookielib.unique](inputs/cases/document.cookielib.unique.json) | prepared | preg_match_all() [literal] | 569.709 | 0.74% | yes |
| [document.cookielib.unique](inputs/cases/document.cookielib.unique.json) | prepared | preg_match_all() [prefix] | 594.624 | 0.62% | yes |
| [document.cookielib.unique](inputs/cases/document.cookielib.unique.json) | prepared | Native A/A control | 83.851 | 1.15% | yes |
| [document.cookielib.unique](inputs/cases/document.cookielib.unique.json) | oneshot | Matcher::getMatchedKeywords() | 125.850 | 3.66% | yes |
| [document.cookielib.unique](inputs/cases/document.cookielib.unique.json) | oneshot | strpos() loop | 298.366 | 1.50% | yes |
| [document.cookielib.unique](inputs/cases/document.cookielib.unique.json) | oneshot | preg_match_all() [literal] | 568.524 | 1.69% | yes |
| [document.cookielib.unique](inputs/cases/document.cookielib.unique.json) | oneshot | preg_match_all() [prefix] | 592.978 | 0.79% | yes |
| [document.cookielib.unique](inputs/cases/document.cookielib.unique.json) | oneshot | Native A/A control | 126.010 | 0.70% | yes |
| [document.cookielib.count](inputs/cases/document.cookielib.count.json) | prepared | Matcher::countMatches() | 77.040 | 1.82% | yes |
| [document.cookielib.count](inputs/cases/document.cookielib.count.json) | prepared | strpos() loop | 332.897 | 0.60% | yes |
| [document.cookielib.count](inputs/cases/document.cookielib.count.json) | prepared | preg_match_all() [literal] | 528.725 | 0.53% | yes |
| [document.cookielib.count](inputs/cases/document.cookielib.count.json) | prepared | preg_match_all() [prefix] | 551.866 | 0.69% | yes |
| [document.cookielib.count](inputs/cases/document.cookielib.count.json) | prepared | Native A/A control | 76.907 | 2.50% | yes |
| [document.cookielib.count](inputs/cases/document.cookielib.count.json) | oneshot | Matcher::countMatches() | 118.711 | 2.03% | yes |
| [document.cookielib.count](inputs/cases/document.cookielib.count.json) | oneshot | strpos() loop | 333.142 | 2.14% | yes |
| [document.cookielib.count](inputs/cases/document.cookielib.count.json) | oneshot | preg_match_all() [literal] | 530.791 | 0.56% | yes |
| [document.cookielib.count](inputs/cases/document.cookielib.count.json) | oneshot | preg_match_all() [prefix] | 554.172 | 3.56% | yes |
| [document.cookielib.count](inputs/cases/document.cookielib.count.json) | oneshot | Native A/A control | 118.951 | 1.53% | yes |
| [document.cookielib.all](inputs/cases/document.cookielib.all.json) | prepared | Matcher::matchAll() | 98.968 | 4.11% | no |
| [document.cookielib.all](inputs/cases/document.cookielib.all.json) | prepared | strpos() loop | 404.061 | 3.90% | no |
| [document.cookielib.all](inputs/cases/document.cookielib.all.json) | prepared | preg_match_all() [literal] | 622.417 | 4.58% | no |
| [document.cookielib.all](inputs/cases/document.cookielib.all.json) | prepared | preg_match_all() [prefix] | 648.927 | 4.21% | no |
| [document.cookielib.all](inputs/cases/document.cookielib.all.json) | prepared | Native A/A control | 98.642 | 2.07% | no |
| [document.cookielib.all](inputs/cases/document.cookielib.all.json) | oneshot | Matcher::matchAll() | 132.583 | 8.80% | no |
| [document.cookielib.all](inputs/cases/document.cookielib.all.json) | oneshot | strpos() loop | 403.943 | 3.54% | no |
| [document.cookielib.all](inputs/cases/document.cookielib.all.json) | oneshot | preg_match_all() [literal] | 620.752 | 5.14% | no |
| [document.cookielib.all](inputs/cases/document.cookielib.all.json) | oneshot | preg_match_all() [prefix] | 647.508 | 5.79% | no |
| [document.cookielib.all](inputs/cases/document.cookielib.all.json) | oneshot | Native A/A control | 132.628 | 4.80% | no |
| [document.cookielib.replace](inputs/cases/document.cookielib.replace.json) | prepared | Replacer::replace() | 74.117 | 2.34% | yes |
| [document.cookielib.replace](inputs/cases/document.cookielib.replace.json) | prepared | strtr() | 978.412 | 0.59% | yes |
| [document.cookielib.replace](inputs/cases/document.cookielib.replace.json) | prepared | preg_replace_callback() [literal] | 241.007 | 0.60% | yes |
| [document.cookielib.replace](inputs/cases/document.cookielib.replace.json) | prepared | preg_replace_callback() [prefix] | 167.670 | 1.22% | yes |
| [document.cookielib.replace](inputs/cases/document.cookielib.replace.json) | prepared | str_replace() | 363.472 | 0.81% | yes |
| [document.cookielib.replace](inputs/cases/document.cookielib.replace.json) | prepared | Native A/A control | 75.094 | 4.09% | yes |
| [document.cookielib.replace](inputs/cases/document.cookielib.replace.json) | oneshot | Replacer::replace() | 92.268 | 1.62% | yes |
| [document.cookielib.replace](inputs/cases/document.cookielib.replace.json) | oneshot | strtr() | 977.854 | 0.61% | yes |
| [document.cookielib.replace](inputs/cases/document.cookielib.replace.json) | oneshot | preg_replace_callback() [literal] | 241.522 | 0.61% | yes |
| [document.cookielib.replace](inputs/cases/document.cookielib.replace.json) | oneshot | preg_replace_callback() [prefix] | 166.368 | 1.64% | yes |
| [document.cookielib.replace](inputs/cases/document.cookielib.replace.json) | oneshot | str_replace() | 364.203 | 0.65% | yes |
| [document.cookielib.replace](inputs/cases/document.cookielib.replace.json) | oneshot | Native A/A control | 92.359 | 0.77% | yes |
| [document.configparser.unique](inputs/cases/document.configparser.unique.json) | prepared | Matcher::getMatchedKeywords() | 55.691 | 1.18% | yes |
| [document.configparser.unique](inputs/cases/document.configparser.unique.json) | prepared | strpos() loop | 199.258 | 0.75% | yes |
| [document.configparser.unique](inputs/cases/document.configparser.unique.json) | prepared | preg_match_all() [literal] | 364.691 | 0.88% | yes |
| [document.configparser.unique](inputs/cases/document.configparser.unique.json) | prepared | preg_match_all() [prefix] | 386.545 | 0.45% | yes |
| [document.configparser.unique](inputs/cases/document.configparser.unique.json) | prepared | Native A/A control | 55.779 | 1.01% | yes |
| [document.configparser.unique](inputs/cases/document.configparser.unique.json) | oneshot | Matcher::getMatchedKeywords() | 91.196 | 0.65% | yes |
| [document.configparser.unique](inputs/cases/document.configparser.unique.json) | oneshot | strpos() loop | 199.166 | 0.81% | yes |
| [document.configparser.unique](inputs/cases/document.configparser.unique.json) | oneshot | preg_match_all() [literal] | 364.246 | 0.90% | yes |
| [document.configparser.unique](inputs/cases/document.configparser.unique.json) | oneshot | preg_match_all() [prefix] | 387.964 | 0.39% | yes |
| [document.configparser.unique](inputs/cases/document.configparser.unique.json) | oneshot | Native A/A control | 91.165 | 1.35% | yes |
| [document.configparser.count](inputs/cases/document.configparser.count.json) | prepared | Matcher::countMatches() | 50.054 | 0.69% | yes |
| [document.configparser.count](inputs/cases/document.configparser.count.json) | prepared | strpos() loop | 214.594 | 0.61% | yes |
| [document.configparser.count](inputs/cases/document.configparser.count.json) | prepared | preg_match_all() [literal] | 345.299 | 1.10% | yes |
| [document.configparser.count](inputs/cases/document.configparser.count.json) | prepared | preg_match_all() [prefix] | 367.215 | 0.75% | yes |
| [document.configparser.count](inputs/cases/document.configparser.count.json) | prepared | Native A/A control | 49.973 | 1.09% | yes |
| [document.configparser.count](inputs/cases/document.configparser.count.json) | oneshot | Matcher::countMatches() | 88.761 | 1.01% | yes |
| [document.configparser.count](inputs/cases/document.configparser.count.json) | oneshot | strpos() loop | 214.279 | 0.73% | yes |
| [document.configparser.count](inputs/cases/document.configparser.count.json) | oneshot | preg_match_all() [literal] | 345.683 | 0.51% | yes |
| [document.configparser.count](inputs/cases/document.configparser.count.json) | oneshot | preg_match_all() [prefix] | 367.278 | 0.35% | yes |
| [document.configparser.count](inputs/cases/document.configparser.count.json) | oneshot | Native A/A control | 89.136 | 0.89% | yes |
| [document.configparser.all](inputs/cases/document.configparser.all.json) | prepared | Matcher::matchAll() | 62.947 | 1.37% | yes |
| [document.configparser.all](inputs/cases/document.configparser.all.json) | prepared | strpos() loop | 235.497 | 0.58% | yes |
| [document.configparser.all](inputs/cases/document.configparser.all.json) | prepared | preg_match_all() [literal] | 380.559 | 1.87% | yes |
| [document.configparser.all](inputs/cases/document.configparser.all.json) | prepared | preg_match_all() [prefix] | 401.050 | 0.71% | yes |
| [document.configparser.all](inputs/cases/document.configparser.all.json) | prepared | Native A/A control | 62.999 | 0.76% | yes |
| [document.configparser.all](inputs/cases/document.configparser.all.json) | oneshot | Matcher::matchAll() | 95.746 | 4.98% | yes |
| [document.configparser.all](inputs/cases/document.configparser.all.json) | oneshot | strpos() loop | 236.038 | 0.85% | yes |
| [document.configparser.all](inputs/cases/document.configparser.all.json) | oneshot | preg_match_all() [literal] | 379.441 | 0.48% | yes |
| [document.configparser.all](inputs/cases/document.configparser.all.json) | oneshot | preg_match_all() [prefix] | 399.892 | 0.57% | yes |
| [document.configparser.all](inputs/cases/document.configparser.all.json) | oneshot | Native A/A control | 95.971 | 1.70% | yes |
| [document.configparser.replace](inputs/cases/document.configparser.replace.json) | prepared | Replacer::replace() | 49.481 | 6.77% | no |
| [document.configparser.replace](inputs/cases/document.configparser.replace.json) | prepared | strtr() | 591.632 | 0.47% | no |
| [document.configparser.replace](inputs/cases/document.configparser.replace.json) | prepared | preg_replace_callback() [literal] | 148.010 | 0.87% | no |
| [document.configparser.replace](inputs/cases/document.configparser.replace.json) | prepared | preg_replace_callback() [prefix] | 93.240 | 1.87% | no |
| [document.configparser.replace](inputs/cases/document.configparser.replace.json) | prepared | str_replace() | 216.141 | 0.68% | no |
| [document.configparser.replace](inputs/cases/document.configparser.replace.json) | prepared | Native A/A control | 49.404 | 4.75% | no |
| [document.configparser.replace](inputs/cases/document.configparser.replace.json) | oneshot | Replacer::replace() | 69.504 | 1.03% | yes |
| [document.configparser.replace](inputs/cases/document.configparser.replace.json) | oneshot | strtr() | 590.988 | 1.13% | yes |
| [document.configparser.replace](inputs/cases/document.configparser.replace.json) | oneshot | preg_replace_callback() [literal] | 148.051 | 0.60% | yes |
| [document.configparser.replace](inputs/cases/document.configparser.replace.json) | oneshot | preg_replace_callback() [prefix] | 93.288 | 1.92% | yes |
| [document.configparser.replace](inputs/cases/document.configparser.replace.json) | oneshot | str_replace() | 216.400 | 0.69% | yes |
| [document.configparser.replace](inputs/cases/document.configparser.replace.json) | oneshot | Native A/A control | 69.740 | 1.03% | yes |
| [document.cookie.unique](inputs/cases/document.cookie.unique.json) | prepared | Matcher::getMatchedKeywords() | 22.645 | 0.99% | yes |
| [document.cookie.unique](inputs/cases/document.cookie.unique.json) | prepared | strpos() loop | 91.055 | 0.60% | yes |
| [document.cookie.unique](inputs/cases/document.cookie.unique.json) | prepared | preg_match_all() [literal] | 177.190 | 0.76% | yes |
| [document.cookie.unique](inputs/cases/document.cookie.unique.json) | prepared | preg_match_all() [prefix] | 186.969 | 0.65% | yes |
| [document.cookie.unique](inputs/cases/document.cookie.unique.json) | prepared | Native A/A control | 22.678 | 0.84% | yes |
| [document.cookie.unique](inputs/cases/document.cookie.unique.json) | oneshot | Matcher::getMatchedKeywords() | 56.803 | 1.17% | yes |
| [document.cookie.unique](inputs/cases/document.cookie.unique.json) | oneshot | strpos() loop | 91.089 | 0.51% | yes |
| [document.cookie.unique](inputs/cases/document.cookie.unique.json) | oneshot | preg_match_all() [literal] | 177.558 | 1.26% | yes |
| [document.cookie.unique](inputs/cases/document.cookie.unique.json) | oneshot | preg_match_all() [prefix] | 187.706 | 1.38% | yes |
| [document.cookie.unique](inputs/cases/document.cookie.unique.json) | oneshot | Native A/A control | 56.834 | 1.14% | yes |
| [document.cookie.count](inputs/cases/document.cookie.count.json) | prepared | Matcher::countMatches() | 21.425 | 2.21% | yes |
| [document.cookie.count](inputs/cases/document.cookie.count.json) | prepared | strpos() loop | 97.163 | 0.57% | yes |
| [document.cookie.count](inputs/cases/document.cookie.count.json) | prepared | preg_match_all() [literal] | 159.977 | 0.68% | yes |
| [document.cookie.count](inputs/cases/document.cookie.count.json) | prepared | preg_match_all() [prefix] | 170.605 | 0.48% | yes |
| [document.cookie.count](inputs/cases/document.cookie.count.json) | prepared | Native A/A control | 21.455 | 4.07% | yes |
| [document.cookie.count](inputs/cases/document.cookie.count.json) | oneshot | Matcher::countMatches() | 57.924 | 0.72% | yes |
| [document.cookie.count](inputs/cases/document.cookie.count.json) | oneshot | strpos() loop | 97.340 | 0.61% | yes |
| [document.cookie.count](inputs/cases/document.cookie.count.json) | oneshot | preg_match_all() [literal] | 160.208 | 0.90% | yes |
| [document.cookie.count](inputs/cases/document.cookie.count.json) | oneshot | preg_match_all() [prefix] | 171.452 | 0.52% | yes |
| [document.cookie.count](inputs/cases/document.cookie.count.json) | oneshot | Native A/A control | 57.864 | 0.94% | yes |
| [document.cookie.all](inputs/cases/document.cookie.all.json) | prepared | Matcher::matchAll() | 30.636 | 1.13% | yes |
| [document.cookie.all](inputs/cases/document.cookie.all.json) | prepared | strpos() loop | 118.556 | 0.75% | yes |
| [document.cookie.all](inputs/cases/document.cookie.all.json) | prepared | preg_match_all() [literal] | 189.654 | 0.90% | yes |
| [document.cookie.all](inputs/cases/document.cookie.all.json) | prepared | preg_match_all() [prefix] | 199.901 | 2.06% | yes |
| [document.cookie.all](inputs/cases/document.cookie.all.json) | prepared | Native A/A control | 30.607 | 1.10% | yes |
| [document.cookie.all](inputs/cases/document.cookie.all.json) | oneshot | Matcher::matchAll() | 62.983 | 1.39% | yes |
| [document.cookie.all](inputs/cases/document.cookie.all.json) | oneshot | strpos() loop | 118.377 | 0.97% | yes |
| [document.cookie.all](inputs/cases/document.cookie.all.json) | oneshot | preg_match_all() [literal] | 189.644 | 0.48% | yes |
| [document.cookie.all](inputs/cases/document.cookie.all.json) | oneshot | preg_match_all() [prefix] | 199.924 | 0.63% | yes |
| [document.cookie.all](inputs/cases/document.cookie.all.json) | oneshot | Native A/A control | 63.103 | 0.67% | yes |
| [document.cookie.replace](inputs/cases/document.cookie.replace.json) | prepared | Replacer::replace() | 20.240 | 7.59% | no |
| [document.cookie.replace](inputs/cases/document.cookie.replace.json) | prepared | strtr() | 292.552 | 6.03% | no |
| [document.cookie.replace](inputs/cases/document.cookie.replace.json) | prepared | preg_replace_callback() [literal] | 74.993 | 5.66% | no |
| [document.cookie.replace](inputs/cases/document.cookie.replace.json) | prepared | preg_replace_callback() [prefix] | 40.767 | 4.56% | no |
| [document.cookie.replace](inputs/cases/document.cookie.replace.json) | prepared | str_replace() | 102.230 | 2.52% | no |
| [document.cookie.replace](inputs/cases/document.cookie.replace.json) | prepared | Native A/A control | 20.343 | 7.90% | no |
| [document.cookie.replace](inputs/cases/document.cookie.replace.json) | oneshot | Replacer::replace() | 37.940 | 1.19% | yes |
| [document.cookie.replace](inputs/cases/document.cookie.replace.json) | oneshot | strtr() | 292.532 | 1.18% | yes |
| [document.cookie.replace](inputs/cases/document.cookie.replace.json) | oneshot | preg_replace_callback() [literal] | 74.665 | 1.15% | yes |
| [document.cookie.replace](inputs/cases/document.cookie.replace.json) | oneshot | preg_replace_callback() [prefix] | 40.651 | 4.59% | yes |
| [document.cookie.replace](inputs/cases/document.cookie.replace.json) | oneshot | str_replace() | 102.220 | 1.21% | yes |
| [document.cookie.replace](inputs/cases/document.cookie.replace.json) | oneshot | Native A/A control | 37.984 | 1.73% | yes |
| [document.stringio.unique](inputs/cases/document.stringio.unique.json) | prepared | Matcher::getMatchedKeywords() | 8.084 | 45.49% | no |
| [document.stringio.unique](inputs/cases/document.stringio.unique.json) | prepared | strpos() loop | 41.917 | 0.66% | no |
| [document.stringio.unique](inputs/cases/document.stringio.unique.json) | prepared | preg_match_all() [literal] | 60.167 | 2.21% | no |
| [document.stringio.unique](inputs/cases/document.stringio.unique.json) | prepared | preg_match_all() [prefix] | 62.407 | 1.95% | no |
| [document.stringio.unique](inputs/cases/document.stringio.unique.json) | prepared | Native A/A control | 8.093 | 23.95% | no |
| [document.stringio.unique](inputs/cases/document.stringio.unique.json) | oneshot | Matcher::getMatchedKeywords() | 39.708 | 14.46% | no |
| [document.stringio.unique](inputs/cases/document.stringio.unique.json) | oneshot | strpos() loop | 41.913 | 0.67% | no |
| [document.stringio.unique](inputs/cases/document.stringio.unique.json) | oneshot | preg_match_all() [literal] | 60.620 | 1.54% | no |
| [document.stringio.unique](inputs/cases/document.stringio.unique.json) | oneshot | preg_match_all() [prefix] | 62.686 | 1.59% | no |
| [document.stringio.unique](inputs/cases/document.stringio.unique.json) | oneshot | Native A/A control | 39.867 | 1.04% | no |
| [document.stringio.count](inputs/cases/document.stringio.count.json) | prepared | Matcher::countMatches() | 5.995 | 2.13% | yes |
| [document.stringio.count](inputs/cases/document.stringio.count.json) | prepared | strpos() loop | 43.909 | 0.57% | yes |
| [document.stringio.count](inputs/cases/document.stringio.count.json) | prepared | preg_match_all() [literal] | 49.438 | 1.38% | yes |
| [document.stringio.count](inputs/cases/document.stringio.count.json) | prepared | preg_match_all() [prefix] | 51.973 | 1.72% | yes |
| [document.stringio.count](inputs/cases/document.stringio.count.json) | prepared | Native A/A control | 5.970 | 3.81% | yes |
| [document.stringio.count](inputs/cases/document.stringio.count.json) | oneshot | Matcher::countMatches() | 37.427 | 1.62% | yes |
| [document.stringio.count](inputs/cases/document.stringio.count.json) | oneshot | strpos() loop | 43.920 | 0.25% | yes |
| [document.stringio.count](inputs/cases/document.stringio.count.json) | oneshot | preg_match_all() [literal] | 49.378 | 1.30% | yes |
| [document.stringio.count](inputs/cases/document.stringio.count.json) | oneshot | preg_match_all() [prefix] | 51.650 | 1.70% | yes |
| [document.stringio.count](inputs/cases/document.stringio.count.json) | oneshot | Native A/A control | 37.666 | 1.95% | yes |
| [document.stringio.all](inputs/cases/document.stringio.all.json) | prepared | Matcher::matchAll() | 11.868 | 1.16% | yes |
| [document.stringio.all](inputs/cases/document.stringio.all.json) | prepared | strpos() loop | 54.557 | 0.37% | yes |
| [document.stringio.all](inputs/cases/document.stringio.all.json) | prepared | preg_match_all() [literal] | 66.113 | 1.46% | yes |
| [document.stringio.all](inputs/cases/document.stringio.all.json) | prepared | preg_match_all() [prefix] | 68.145 | 1.43% | yes |
| [document.stringio.all](inputs/cases/document.stringio.all.json) | prepared | Native A/A control | 11.911 | 1.41% | yes |
| [document.stringio.all](inputs/cases/document.stringio.all.json) | oneshot | Matcher::matchAll() | 41.432 | 1.22% | yes |
| [document.stringio.all](inputs/cases/document.stringio.all.json) | oneshot | strpos() loop | 54.457 | 0.73% | yes |
| [document.stringio.all](inputs/cases/document.stringio.all.json) | oneshot | preg_match_all() [literal] | 65.996 | 2.00% | yes |
| [document.stringio.all](inputs/cases/document.stringio.all.json) | oneshot | preg_match_all() [prefix] | 67.869 | 1.26% | yes |
| [document.stringio.all](inputs/cases/document.stringio.all.json) | oneshot | Native A/A control | 41.525 | 1.00% | yes |
| [document.stringio.replace](inputs/cases/document.stringio.replace.json) | prepared | Replacer::replace() | 6.539 | 6.57% | no |
| [document.stringio.replace](inputs/cases/document.stringio.replace.json) | prepared | strtr() | 116.259 | 4.18% | no |
| [document.stringio.replace](inputs/cases/document.stringio.replace.json) | prepared | preg_replace_callback() [literal] | 31.900 | 0.80% | no |
| [document.stringio.replace](inputs/cases/document.stringio.replace.json) | prepared | preg_replace_callback() [prefix] | 15.289 | 2.96% | no |
| [document.stringio.replace](inputs/cases/document.stringio.replace.json) | prepared | str_replace() | 42.519 | 0.35% | no |
| [document.stringio.replace](inputs/cases/document.stringio.replace.json) | prepared | Native A/A control | 6.589 | 2.92% | no |
| [document.stringio.replace](inputs/cases/document.stringio.replace.json) | oneshot | Replacer::replace() | 24.573 | 1.85% | yes |
| [document.stringio.replace](inputs/cases/document.stringio.replace.json) | oneshot | strtr() | 113.988 | 4.34% | yes |
| [document.stringio.replace](inputs/cases/document.stringio.replace.json) | oneshot | preg_replace_callback() [literal] | 31.691 | 1.37% | yes |
| [document.stringio.replace](inputs/cases/document.stringio.replace.json) | oneshot | preg_replace_callback() [prefix] | 15.285 | 2.41% | yes |
| [document.stringio.replace](inputs/cases/document.stringio.replace.json) | oneshot | str_replace() | 42.503 | 0.60% | yes |
| [document.stringio.replace](inputs/cases/document.stringio.replace.json) | oneshot | Native A/A control | 24.687 | 1.89% | yes |
| [document.xmlrpclib.unique](inputs/cases/document.xmlrpclib.unique.json) | prepared | Matcher::getMatchedKeywords() | 63.324 | 0.83% | yes |
| [document.xmlrpclib.unique](inputs/cases/document.xmlrpclib.unique.json) | prepared | strpos() loop | 224.910 | 0.58% | yes |
| [document.xmlrpclib.unique](inputs/cases/document.xmlrpclib.unique.json) | prepared | preg_match_all() [literal] | 412.436 | 0.77% | yes |
| [document.xmlrpclib.unique](inputs/cases/document.xmlrpclib.unique.json) | prepared | preg_match_all() [prefix] | 426.537 | 0.44% | yes |
| [document.xmlrpclib.unique](inputs/cases/document.xmlrpclib.unique.json) | prepared | Native A/A control | 63.425 | 0.76% | yes |
| [document.xmlrpclib.unique](inputs/cases/document.xmlrpclib.unique.json) | oneshot | Matcher::getMatchedKeywords() | 97.900 | 1.73% | yes |
| [document.xmlrpclib.unique](inputs/cases/document.xmlrpclib.unique.json) | oneshot | strpos() loop | 225.165 | 0.56% | yes |
| [document.xmlrpclib.unique](inputs/cases/document.xmlrpclib.unique.json) | oneshot | preg_match_all() [literal] | 412.064 | 0.72% | yes |
| [document.xmlrpclib.unique](inputs/cases/document.xmlrpclib.unique.json) | oneshot | preg_match_all() [prefix] | 428.501 | 1.56% | yes |
| [document.xmlrpclib.unique](inputs/cases/document.xmlrpclib.unique.json) | oneshot | Native A/A control | 97.847 | 1.30% | yes |
| [document.xmlrpclib.count](inputs/cases/document.xmlrpclib.count.json) | prepared | Matcher::countMatches() | 60.171 | 1.56% | yes |
| [document.xmlrpclib.count](inputs/cases/document.xmlrpclib.count.json) | prepared | strpos() loop | 245.330 | 0.87% | yes |
| [document.xmlrpclib.count](inputs/cases/document.xmlrpclib.count.json) | prepared | preg_match_all() [literal] | 396.822 | 1.70% | yes |
| [document.xmlrpclib.count](inputs/cases/document.xmlrpclib.count.json) | prepared | preg_match_all() [prefix] | 415.022 | 1.60% | yes |
| [document.xmlrpclib.count](inputs/cases/document.xmlrpclib.count.json) | prepared | Native A/A control | 60.097 | 1.14% | yes |
| [document.xmlrpclib.count](inputs/cases/document.xmlrpclib.count.json) | oneshot | Matcher::countMatches() | 98.697 | 1.32% | yes |
| [document.xmlrpclib.count](inputs/cases/document.xmlrpclib.count.json) | oneshot | strpos() loop | 245.228 | 0.45% | yes |
| [document.xmlrpclib.count](inputs/cases/document.xmlrpclib.count.json) | oneshot | preg_match_all() [literal] | 396.692 | 2.56% | yes |
| [document.xmlrpclib.count](inputs/cases/document.xmlrpclib.count.json) | oneshot | preg_match_all() [prefix] | 414.727 | 1.83% | yes |
| [document.xmlrpclib.count](inputs/cases/document.xmlrpclib.count.json) | oneshot | Native A/A control | 98.717 | 2.13% | yes |
| [document.xmlrpclib.all](inputs/cases/document.xmlrpclib.all.json) | prepared | Matcher::matchAll() | 67.289 | 1.61% | yes |
| [document.xmlrpclib.all](inputs/cases/document.xmlrpclib.all.json) | prepared | strpos() loop | 259.413 | 1.18% | yes |
| [document.xmlrpclib.all](inputs/cases/document.xmlrpclib.all.json) | prepared | preg_match_all() [literal] | 420.031 | 1.20% | yes |
| [document.xmlrpclib.all](inputs/cases/document.xmlrpclib.all.json) | prepared | preg_match_all() [prefix] | 436.377 | 2.03% | yes |
| [document.xmlrpclib.all](inputs/cases/document.xmlrpclib.all.json) | prepared | Native A/A control | 67.271 | 1.85% | yes |
| [document.xmlrpclib.all](inputs/cases/document.xmlrpclib.all.json) | oneshot | Matcher::matchAll() | 99.607 | 2.80% | yes |
| [document.xmlrpclib.all](inputs/cases/document.xmlrpclib.all.json) | oneshot | strpos() loop | 260.023 | 0.96% | yes |
| [document.xmlrpclib.all](inputs/cases/document.xmlrpclib.all.json) | oneshot | preg_match_all() [literal] | 418.552 | 1.63% | yes |
| [document.xmlrpclib.all](inputs/cases/document.xmlrpclib.all.json) | oneshot | preg_match_all() [prefix] | 435.042 | 1.82% | yes |
| [document.xmlrpclib.all](inputs/cases/document.xmlrpclib.all.json) | oneshot | Native A/A control | 99.488 | 2.65% | yes |
| [document.xmlrpclib.replace](inputs/cases/document.xmlrpclib.replace.json) | prepared | Replacer::replace() | 57.610 | 4.95% | yes |
| [document.xmlrpclib.replace](inputs/cases/document.xmlrpclib.replace.json) | prepared | strtr() | 747.017 | 1.18% | yes |
| [document.xmlrpclib.replace](inputs/cases/document.xmlrpclib.replace.json) | prepared | preg_replace_callback() [literal] | 177.526 | 1.89% | yes |
| [document.xmlrpclib.replace](inputs/cases/document.xmlrpclib.replace.json) | prepared | preg_replace_callback() [prefix] | 113.840 | 2.28% | yes |
| [document.xmlrpclib.replace](inputs/cases/document.xmlrpclib.replace.json) | prepared | str_replace() | 272.263 | 0.53% | yes |
| [document.xmlrpclib.replace](inputs/cases/document.xmlrpclib.replace.json) | prepared | Native A/A control | 57.379 | 4.64% | yes |
| [document.xmlrpclib.replace](inputs/cases/document.xmlrpclib.replace.json) | oneshot | Replacer::replace() | 75.972 | 2.90% | yes |
| [document.xmlrpclib.replace](inputs/cases/document.xmlrpclib.replace.json) | oneshot | strtr() | 744.598 | 1.06% | yes |
| [document.xmlrpclib.replace](inputs/cases/document.xmlrpclib.replace.json) | oneshot | preg_replace_callback() [literal] | 176.743 | 2.00% | yes |
| [document.xmlrpclib.replace](inputs/cases/document.xmlrpclib.replace.json) | oneshot | preg_replace_callback() [prefix] | 114.586 | 1.02% | yes |
| [document.xmlrpclib.replace](inputs/cases/document.xmlrpclib.replace.json) | oneshot | str_replace() | 272.374 | 0.75% | yes |
| [document.xmlrpclib.replace](inputs/cases/document.xmlrpclib.replace.json) | oneshot | Native A/A control | 76.489 | 3.00% | yes |
| [document.thread.unique](inputs/cases/document.thread.unique.json) | prepared | Matcher::getMatchedKeywords() | 14.817 | 2.47% | yes |
| [document.thread.unique](inputs/cases/document.thread.unique.json) | prepared | strpos() loop | 64.315 | 0.52% | yes |
| [document.thread.unique](inputs/cases/document.thread.unique.json) | prepared | preg_match_all() [literal] | 119.050 | 3.76% | yes |
| [document.thread.unique](inputs/cases/document.thread.unique.json) | prepared | preg_match_all() [prefix] | 125.266 | 2.93% | yes |
| [document.thread.unique](inputs/cases/document.thread.unique.json) | prepared | Native A/A control | 14.958 | 2.69% | yes |
| [document.thread.unique](inputs/cases/document.thread.unique.json) | oneshot | Matcher::getMatchedKeywords() | 47.996 | 1.07% | yes |
| [document.thread.unique](inputs/cases/document.thread.unique.json) | oneshot | strpos() loop | 64.294 | 0.65% | yes |
| [document.thread.unique](inputs/cases/document.thread.unique.json) | oneshot | preg_match_all() [literal] | 119.288 | 1.90% | yes |
| [document.thread.unique](inputs/cases/document.thread.unique.json) | oneshot | preg_match_all() [prefix] | 125.408 | 0.87% | yes |
| [document.thread.unique](inputs/cases/document.thread.unique.json) | oneshot | Native A/A control | 48.171 | 1.88% | yes |
| [document.thread.count](inputs/cases/document.thread.count.json) | prepared | Matcher::countMatches() | 12.424 | 2.48% | yes |
| [document.thread.count](inputs/cases/document.thread.count.json) | prepared | strpos() loop | 69.397 | 0.91% | yes |
| [document.thread.count](inputs/cases/document.thread.count.json) | prepared | preg_match_all() [literal] | 107.058 | 3.09% | yes |
| [document.thread.count](inputs/cases/document.thread.count.json) | prepared | preg_match_all() [prefix] | 113.863 | 2.42% | yes |
| [document.thread.count](inputs/cases/document.thread.count.json) | prepared | Native A/A control | 12.350 | 1.89% | yes |
| [document.thread.count](inputs/cases/document.thread.count.json) | oneshot | Matcher::countMatches() | 47.364 | 1.44% | yes |
| [document.thread.count](inputs/cases/document.thread.count.json) | oneshot | strpos() loop | 69.400 | 0.93% | yes |
| [document.thread.count](inputs/cases/document.thread.count.json) | oneshot | preg_match_all() [literal] | 107.135 | 2.82% | yes |
| [document.thread.count](inputs/cases/document.thread.count.json) | oneshot | preg_match_all() [prefix] | 113.473 | 2.90% | yes |
| [document.thread.count](inputs/cases/document.thread.count.json) | oneshot | Native A/A control | 47.474 | 2.06% | yes |
| [document.thread.all](inputs/cases/document.thread.all.json) | prepared | Matcher::matchAll() | 19.380 | 6.29% | no |
| [document.thread.all](inputs/cases/document.thread.all.json) | prepared | strpos() loop | 80.655 | 0.67% | no |
| [document.thread.all](inputs/cases/document.thread.all.json) | prepared | preg_match_all() [literal] | 125.189 | 1.86% | no |
| [document.thread.all](inputs/cases/document.thread.all.json) | prepared | preg_match_all() [prefix] | 131.223 | 2.62% | no |
| [document.thread.all](inputs/cases/document.thread.all.json) | prepared | Native A/A control | 19.392 | 11.71% | no |
| [document.thread.all](inputs/cases/document.thread.all.json) | oneshot | Matcher::matchAll() | 50.327 | 2.81% | yes |
| [document.thread.all](inputs/cases/document.thread.all.json) | oneshot | strpos() loop | 80.576 | 1.34% | yes |
| [document.thread.all](inputs/cases/document.thread.all.json) | oneshot | preg_match_all() [literal] | 125.101 | 2.38% | yes |
| [document.thread.all](inputs/cases/document.thread.all.json) | oneshot | preg_match_all() [prefix] | 130.892 | 0.88% | yes |
| [document.thread.all](inputs/cases/document.thread.all.json) | oneshot | Native A/A control | 50.470 | 3.53% | yes |
| [document.thread.replace](inputs/cases/document.thread.replace.json) | prepared | Replacer::replace() | 13.626 | 7.16% | no |
| [document.thread.replace](inputs/cases/document.thread.replace.json) | prepared | strtr() | 215.896 | 2.63% | no |
| [document.thread.replace](inputs/cases/document.thread.replace.json) | prepared | preg_replace_callback() [literal] | 55.279 | 1.53% | no |
| [document.thread.replace](inputs/cases/document.thread.replace.json) | prepared | preg_replace_callback() [prefix] | 27.128 | 5.12% | no |
| [document.thread.replace](inputs/cases/document.thread.replace.json) | prepared | Native A/A control | 13.618 | 1.82% | no |
| [document.thread.replace](inputs/cases/document.thread.replace.json) | oneshot | Replacer::replace() | 31.551 | 3.19% | no |
| [document.thread.replace](inputs/cases/document.thread.replace.json) | oneshot | strtr() | 216.101 | 2.07% | no |
| [document.thread.replace](inputs/cases/document.thread.replace.json) | oneshot | preg_replace_callback() [literal] | 55.437 | 1.12% | no |
| [document.thread.replace](inputs/cases/document.thread.replace.json) | oneshot | preg_replace_callback() [prefix] | 26.811 | 6.87% | no |
| [document.thread.replace](inputs/cases/document.thread.replace.json) | oneshot | Native A/A control | 31.372 | 2.24% | no |
| [document.simplehttpserver.unique](inputs/cases/document.simplehttpserver.unique.json) | prepared | Matcher::getMatchedKeywords() | 9.907 | 1.90% | yes |
| [document.simplehttpserver.unique](inputs/cases/document.simplehttpserver.unique.json) | prepared | strpos() loop | 45.072 | 0.58% | yes |
| [document.simplehttpserver.unique](inputs/cases/document.simplehttpserver.unique.json) | prepared | preg_match_all() [literal] | 61.083 | 1.91% | yes |
| [document.simplehttpserver.unique](inputs/cases/document.simplehttpserver.unique.json) | prepared | preg_match_all() [prefix] | 65.982 | 1.26% | yes |
| [document.simplehttpserver.unique](inputs/cases/document.simplehttpserver.unique.json) | prepared | Native A/A control | 9.946 | 3.30% | yes |
| [document.simplehttpserver.unique](inputs/cases/document.simplehttpserver.unique.json) | oneshot | Matcher::getMatchedKeywords() | 41.386 | 1.49% | yes |
| [document.simplehttpserver.unique](inputs/cases/document.simplehttpserver.unique.json) | oneshot | strpos() loop | 45.131 | 0.42% | yes |
| [document.simplehttpserver.unique](inputs/cases/document.simplehttpserver.unique.json) | oneshot | preg_match_all() [literal] | 61.073 | 1.32% | yes |
| [document.simplehttpserver.unique](inputs/cases/document.simplehttpserver.unique.json) | oneshot | preg_match_all() [prefix] | 64.668 | 1.22% | yes |
| [document.simplehttpserver.unique](inputs/cases/document.simplehttpserver.unique.json) | oneshot | Native A/A control | 41.258 | 1.75% | yes |
| [document.simplehttpserver.count](inputs/cases/document.simplehttpserver.count.json) | prepared | Matcher::countMatches() | 6.787 | 3.45% | yes |
| [document.simplehttpserver.count](inputs/cases/document.simplehttpserver.count.json) | prepared | strpos() loop | 47.201 | 0.46% | yes |
| [document.simplehttpserver.count](inputs/cases/document.simplehttpserver.count.json) | prepared | preg_match_all() [literal] | 56.240 | 13.63% | yes |
| [document.simplehttpserver.count](inputs/cases/document.simplehttpserver.count.json) | prepared | preg_match_all() [prefix] | 61.402 | 1.43% | yes |
| [document.simplehttpserver.count](inputs/cases/document.simplehttpserver.count.json) | prepared | Native A/A control | 6.796 | 4.15% | yes |
| [document.simplehttpserver.count](inputs/cases/document.simplehttpserver.count.json) | oneshot | Matcher::countMatches() | 39.839 | 1.51% | yes |
| [document.simplehttpserver.count](inputs/cases/document.simplehttpserver.count.json) | oneshot | strpos() loop | 47.204 | 0.45% | yes |
| [document.simplehttpserver.count](inputs/cases/document.simplehttpserver.count.json) | oneshot | preg_match_all() [literal] | 56.217 | 2.73% | yes |
| [document.simplehttpserver.count](inputs/cases/document.simplehttpserver.count.json) | oneshot | preg_match_all() [prefix] | 61.384 | 1.05% | yes |
| [document.simplehttpserver.count](inputs/cases/document.simplehttpserver.count.json) | oneshot | Native A/A control | 39.905 | 1.34% | yes |
| [document.simplehttpserver.all](inputs/cases/document.simplehttpserver.all.json) | prepared | Matcher::matchAll() | 11.856 | 7.33% | no |
| [document.simplehttpserver.all](inputs/cases/document.simplehttpserver.all.json) | prepared | strpos() loop | 50.959 | 3.15% | no |
| [document.simplehttpserver.all](inputs/cases/document.simplehttpserver.all.json) | prepared | preg_match_all() [literal] | 62.987 | 10.04% | no |
| [document.simplehttpserver.all](inputs/cases/document.simplehttpserver.all.json) | prepared | preg_match_all() [prefix] | 67.755 | 8.52% | no |
| [document.simplehttpserver.all](inputs/cases/document.simplehttpserver.all.json) | prepared | Native A/A control | 11.904 | 2.10% | no |
| [document.simplehttpserver.all](inputs/cases/document.simplehttpserver.all.json) | oneshot | Matcher::matchAll() | 41.549 | 6.37% | no |
| [document.simplehttpserver.all](inputs/cases/document.simplehttpserver.all.json) | oneshot | strpos() loop | 50.891 | 2.56% | no |
| [document.simplehttpserver.all](inputs/cases/document.simplehttpserver.all.json) | oneshot | preg_match_all() [literal] | 63.156 | 10.21% | no |
| [document.simplehttpserver.all](inputs/cases/document.simplehttpserver.all.json) | oneshot | preg_match_all() [prefix] | 67.728 | 7.46% | no |
| [document.simplehttpserver.all](inputs/cases/document.simplehttpserver.all.json) | oneshot | Native A/A control | 41.271 | 3.72% | no |
| [document.simplehttpserver.replace](inputs/cases/document.simplehttpserver.replace.json) | prepared | Replacer::replace() | 8.036 | 4.10% | yes |
| [document.simplehttpserver.replace](inputs/cases/document.simplehttpserver.replace.json) | prepared | strtr() | 142.005 | 3.70% | yes |
| [document.simplehttpserver.replace](inputs/cases/document.simplehttpserver.replace.json) | prepared | preg_replace_callback() [literal] | 33.198 | 1.49% | yes |
| [document.simplehttpserver.replace](inputs/cases/document.simplehttpserver.replace.json) | prepared | preg_replace_callback() [prefix] | 15.677 | 4.86% | yes |
| [document.simplehttpserver.replace](inputs/cases/document.simplehttpserver.replace.json) | prepared | str_replace() | 47.307 | 0.88% | yes |
| [document.simplehttpserver.replace](inputs/cases/document.simplehttpserver.replace.json) | prepared | Native A/A control | 8.043 | 3.20% | yes |
| [document.simplehttpserver.replace](inputs/cases/document.simplehttpserver.replace.json) | oneshot | Replacer::replace() | 25.615 | 8.19% | no |
| [document.simplehttpserver.replace](inputs/cases/document.simplehttpserver.replace.json) | oneshot | strtr() | 140.942 | 3.62% | no |
| [document.simplehttpserver.replace](inputs/cases/document.simplehttpserver.replace.json) | oneshot | preg_replace_callback() [literal] | 33.336 | 1.85% | no |
| [document.simplehttpserver.replace](inputs/cases/document.simplehttpserver.replace.json) | oneshot | preg_replace_callback() [prefix] | 15.741 | 3.82% | no |
| [document.simplehttpserver.replace](inputs/cases/document.simplehttpserver.replace.json) | oneshot | str_replace() | 47.327 | 0.34% | no |
| [document.simplehttpserver.replace](inputs/cases/document.simplehttpserver.replace.json) | oneshot | Native A/A control | 25.711 | 7.48% | no |
| [document.socketserver.unique](inputs/cases/document.socketserver.unique.json) | prepared | Matcher::getMatchedKeywords() | 64.099 | 1.83% | yes |
| [document.socketserver.unique](inputs/cases/document.socketserver.unique.json) | prepared | strpos() loop | 230.677 | 0.49% | yes |
| [document.socketserver.unique](inputs/cases/document.socketserver.unique.json) | prepared | preg_match_all() [literal] | 428.038 | 1.43% | yes |
| [document.socketserver.unique](inputs/cases/document.socketserver.unique.json) | prepared | preg_match_all() [prefix] | 448.587 | 4.21% | yes |
| [document.socketserver.unique](inputs/cases/document.socketserver.unique.json) | prepared | Native A/A control | 64.014 | 4.11% | yes |
| [document.socketserver.unique](inputs/cases/document.socketserver.unique.json) | oneshot | Matcher::getMatchedKeywords() | 98.884 | 1.18% | yes |
| [document.socketserver.unique](inputs/cases/document.socketserver.unique.json) | oneshot | strpos() loop | 229.145 | 0.69% | yes |
| [document.socketserver.unique](inputs/cases/document.socketserver.unique.json) | oneshot | preg_match_all() [literal] | 423.314 | 0.80% | yes |
| [document.socketserver.unique](inputs/cases/document.socketserver.unique.json) | oneshot | preg_match_all() [prefix] | 445.023 | 0.48% | yes |
| [document.socketserver.unique](inputs/cases/document.socketserver.unique.json) | oneshot | Native A/A control | 99.083 | 2.09% | yes |
| [document.socketserver.count](inputs/cases/document.socketserver.count.json) | prepared | Matcher::countMatches() | 58.272 | 2.58% | yes |
| [document.socketserver.count](inputs/cases/document.socketserver.count.json) | prepared | strpos() loop | 258.290 | 0.55% | yes |
| [document.socketserver.count](inputs/cases/document.socketserver.count.json) | prepared | preg_match_all() [literal] | 415.223 | 1.30% | yes |
| [document.socketserver.count](inputs/cases/document.socketserver.count.json) | prepared | preg_match_all() [prefix] | 432.882 | 0.93% | yes |
| [document.socketserver.count](inputs/cases/document.socketserver.count.json) | prepared | Native A/A control | 58.582 | 0.77% | yes |
| [document.socketserver.count](inputs/cases/document.socketserver.count.json) | oneshot | Matcher::countMatches() | 97.658 | 0.68% | yes |
| [document.socketserver.count](inputs/cases/document.socketserver.count.json) | oneshot | strpos() loop | 258.148 | 0.59% | yes |
| [document.socketserver.count](inputs/cases/document.socketserver.count.json) | oneshot | preg_match_all() [literal] | 413.549 | 1.42% | yes |
| [document.socketserver.count](inputs/cases/document.socketserver.count.json) | oneshot | preg_match_all() [prefix] | 434.759 | 0.97% | yes |
| [document.socketserver.count](inputs/cases/document.socketserver.count.json) | oneshot | Native A/A control | 97.567 | 0.64% | yes |
| [document.socketserver.all](inputs/cases/document.socketserver.all.json) | prepared | Matcher::matchAll() | 68.618 | 0.43% | yes |
| [document.socketserver.all](inputs/cases/document.socketserver.all.json) | prepared | strpos() loop | 272.469 | 0.47% | yes |
| [document.socketserver.all](inputs/cases/document.socketserver.all.json) | prepared | preg_match_all() [literal] | 434.565 | 1.11% | yes |
| [document.socketserver.all](inputs/cases/document.socketserver.all.json) | prepared | preg_match_all() [prefix] | 453.576 | 1.67% | yes |
| [document.socketserver.all](inputs/cases/document.socketserver.all.json) | prepared | Native A/A control | 68.769 | 1.17% | yes |
| [document.socketserver.all](inputs/cases/document.socketserver.all.json) | oneshot | Matcher::matchAll() | 100.356 | 1.22% | yes |
| [document.socketserver.all](inputs/cases/document.socketserver.all.json) | oneshot | strpos() loop | 272.536 | 0.35% | yes |
| [document.socketserver.all](inputs/cases/document.socketserver.all.json) | oneshot | preg_match_all() [literal] | 437.068 | 0.98% | yes |
| [document.socketserver.all](inputs/cases/document.socketserver.all.json) | oneshot | preg_match_all() [prefix] | 453.883 | 0.35% | yes |
| [document.socketserver.all](inputs/cases/document.socketserver.all.json) | oneshot | Native A/A control | 100.352 | 1.54% | yes |
| [document.socketserver.replace](inputs/cases/document.socketserver.replace.json) | prepared | Replacer::replace() | 59.987 | 4.21% | yes |
| [document.socketserver.replace](inputs/cases/document.socketserver.replace.json) | prepared | strtr() | 783.426 | 0.78% | yes |
| [document.socketserver.replace](inputs/cases/document.socketserver.replace.json) | prepared | preg_replace_callback() [literal] | 185.823 | 11.24% | yes |
| [document.socketserver.replace](inputs/cases/document.socketserver.replace.json) | prepared | preg_replace_callback() [prefix] | 120.330 | 1.46% | yes |
| [document.socketserver.replace](inputs/cases/document.socketserver.replace.json) | prepared | str_replace() | 277.410 | 0.52% | yes |
| [document.socketserver.replace](inputs/cases/document.socketserver.replace.json) | prepared | Native A/A control | 59.915 | 3.66% | yes |
| [document.socketserver.replace](inputs/cases/document.socketserver.replace.json) | oneshot | Replacer::replace() | 77.730 | 0.83% | yes |
| [document.socketserver.replace](inputs/cases/document.socketserver.replace.json) | oneshot | strtr() | 782.315 | 0.95% | yes |
| [document.socketserver.replace](inputs/cases/document.socketserver.replace.json) | oneshot | preg_replace_callback() [literal] | 186.477 | 1.35% | yes |
| [document.socketserver.replace](inputs/cases/document.socketserver.replace.json) | oneshot | preg_replace_callback() [prefix] | 120.251 | 1.80% | yes |
| [document.socketserver.replace](inputs/cases/document.socketserver.replace.json) | oneshot | str_replace() | 277.577 | 0.95% | yes |
| [document.socketserver.replace](inputs/cases/document.socketserver.replace.json) | oneshot | Native A/A control | 77.941 | 2.96% | yes |
| [document.queue.unique](inputs/cases/document.queue.unique.json) | prepared | Matcher::getMatchedKeywords() | 16.158 | 0.77% | yes |
| [document.queue.unique](inputs/cases/document.queue.unique.json) | prepared | strpos() loop | 67.890 | 0.69% | yes |
| [document.queue.unique](inputs/cases/document.queue.unique.json) | prepared | preg_match_all() [literal] | 106.211 | 13.83% | yes |
| [document.queue.unique](inputs/cases/document.queue.unique.json) | prepared | preg_match_all() [prefix] | 111.741 | 1.20% | yes |
| [document.queue.unique](inputs/cases/document.queue.unique.json) | prepared | Native A/A control | 16.192 | 2.15% | yes |
| [document.queue.unique](inputs/cases/document.queue.unique.json) | oneshot | Matcher::getMatchedKeywords() | 48.746 | 0.98% | yes |
| [document.queue.unique](inputs/cases/document.queue.unique.json) | oneshot | strpos() loop | 67.935 | 0.24% | yes |
| [document.queue.unique](inputs/cases/document.queue.unique.json) | oneshot | preg_match_all() [literal] | 106.065 | 1.81% | yes |
| [document.queue.unique](inputs/cases/document.queue.unique.json) | oneshot | preg_match_all() [prefix] | 111.845 | 1.94% | yes |
| [document.queue.unique](inputs/cases/document.queue.unique.json) | oneshot | Native A/A control | 48.806 | 1.20% | yes |
| [document.queue.count](inputs/cases/document.queue.count.json) | prepared | Matcher::countMatches() | 11.457 | 1.86% | yes |
| [document.queue.count](inputs/cases/document.queue.count.json) | prepared | strpos() loop | 71.324 | 0.69% | yes |
| [document.queue.count](inputs/cases/document.queue.count.json) | prepared | preg_match_all() [literal] | 97.161 | 11.84% | yes |
| [document.queue.count](inputs/cases/document.queue.count.json) | prepared | preg_match_all() [prefix] | 102.328 | 3.03% | yes |
| [document.queue.count](inputs/cases/document.queue.count.json) | prepared | Native A/A control | 11.563 | 2.39% | yes |
| [document.queue.count](inputs/cases/document.queue.count.json) | oneshot | Matcher::countMatches() | 47.270 | 1.13% | yes |
| [document.queue.count](inputs/cases/document.queue.count.json) | oneshot | strpos() loop | 71.341 | 0.42% | yes |
| [document.queue.count](inputs/cases/document.queue.count.json) | oneshot | preg_match_all() [literal] | 96.642 | 1.26% | yes |
| [document.queue.count](inputs/cases/document.queue.count.json) | oneshot | preg_match_all() [prefix] | 102.728 | 0.87% | yes |
| [document.queue.count](inputs/cases/document.queue.count.json) | oneshot | Native A/A control | 47.216 | 1.35% | yes |
| [document.queue.all](inputs/cases/document.queue.all.json) | prepared | Matcher::matchAll() | 22.846 | 0.52% | yes |
| [document.queue.all](inputs/cases/document.queue.all.json) | prepared | strpos() loop | 82.622 | 0.50% | yes |
| [document.queue.all](inputs/cases/document.queue.all.json) | prepared | preg_match_all() [literal] | 112.993 | 1.08% | yes |
| [document.queue.all](inputs/cases/document.queue.all.json) | prepared | preg_match_all() [prefix] | 119.530 | 1.06% | yes |
| [document.queue.all](inputs/cases/document.queue.all.json) | prepared | Native A/A control | 22.873 | 0.33% | yes |
| [document.queue.all](inputs/cases/document.queue.all.json) | oneshot | Matcher::matchAll() | 54.320 | 1.21% | yes |
| [document.queue.all](inputs/cases/document.queue.all.json) | oneshot | strpos() loop | 82.701 | 0.38% | yes |
| [document.queue.all](inputs/cases/document.queue.all.json) | oneshot | preg_match_all() [literal] | 113.248 | 1.10% | yes |
| [document.queue.all](inputs/cases/document.queue.all.json) | oneshot | preg_match_all() [prefix] | 119.889 | 0.98% | yes |
| [document.queue.all](inputs/cases/document.queue.all.json) | oneshot | Native A/A control | 54.237 | 1.36% | yes |
| [document.queue.replace](inputs/cases/document.queue.replace.json) | prepared | Replacer::replace() | 13.534 | 2.38% | yes |
| [document.queue.replace](inputs/cases/document.queue.replace.json) | prepared | strtr() | 207.978 | 1.26% | yes |
| [document.queue.replace](inputs/cases/document.queue.replace.json) | prepared | preg_replace_callback() [literal] | 54.871 | 0.90% | yes |
| [document.queue.replace](inputs/cases/document.queue.replace.json) | prepared | preg_replace_callback() [prefix] | 25.241 | 3.30% | yes |
| [document.queue.replace](inputs/cases/document.queue.replace.json) | prepared | str_replace() | 72.199 | 0.44% | yes |
| [document.queue.replace](inputs/cases/document.queue.replace.json) | prepared | Native A/A control | 13.504 | 2.65% | yes |
| [document.queue.replace](inputs/cases/document.queue.replace.json) | oneshot | Replacer::replace() | 31.645 | 1.12% | yes |
| [document.queue.replace](inputs/cases/document.queue.replace.json) | oneshot | strtr() | 207.365 | 1.13% | yes |
| [document.queue.replace](inputs/cases/document.queue.replace.json) | oneshot | preg_replace_callback() [literal] | 55.002 | 0.80% | yes |
| [document.queue.replace](inputs/cases/document.queue.replace.json) | oneshot | preg_replace_callback() [prefix] | 25.388 | 4.83% | yes |
| [document.queue.replace](inputs/cases/document.queue.replace.json) | oneshot | str_replace() | 72.182 | 0.42% | yes |
| [document.queue.replace](inputs/cases/document.queue.replace.json) | oneshot | Native A/A control | 31.661 | 2.47% | yes |
| [document.basehttpserver.unique](inputs/cases/document.basehttpserver.unique.json) | prepared | Matcher::getMatchedKeywords() | 27.631 | 1.19% | yes |
| [document.basehttpserver.unique](inputs/cases/document.basehttpserver.unique.json) | prepared | strpos() loop | 97.619 | 0.22% | yes |
| [document.basehttpserver.unique](inputs/cases/document.basehttpserver.unique.json) | prepared | preg_match_all() [literal] | 187.275 | 0.94% | yes |
| [document.basehttpserver.unique](inputs/cases/document.basehttpserver.unique.json) | prepared | preg_match_all() [prefix] | 196.676 | 0.63% | yes |
| [document.basehttpserver.unique](inputs/cases/document.basehttpserver.unique.json) | prepared | Native A/A control | 27.593 | 0.70% | yes |
| [document.basehttpserver.unique](inputs/cases/document.basehttpserver.unique.json) | oneshot | Matcher::getMatchedKeywords() | 60.035 | 1.53% | yes |
| [document.basehttpserver.unique](inputs/cases/document.basehttpserver.unique.json) | oneshot | strpos() loop | 97.766 | 4.81% | yes |
| [document.basehttpserver.unique](inputs/cases/document.basehttpserver.unique.json) | oneshot | preg_match_all() [literal] | 187.026 | 1.55% | yes |
| [document.basehttpserver.unique](inputs/cases/document.basehttpserver.unique.json) | oneshot | preg_match_all() [prefix] | 196.943 | 0.48% | yes |
| [document.basehttpserver.unique](inputs/cases/document.basehttpserver.unique.json) | oneshot | Native A/A control | 60.033 | 2.12% | yes |
| [document.basehttpserver.count](inputs/cases/document.basehttpserver.count.json) | prepared | Matcher::countMatches() | 23.440 | 0.62% | yes |
| [document.basehttpserver.count](inputs/cases/document.basehttpserver.count.json) | prepared | strpos() loop | 107.733 | 0.80% | yes |
| [document.basehttpserver.count](inputs/cases/document.basehttpserver.count.json) | prepared | preg_match_all() [literal] | 179.415 | 0.81% | yes |
| [document.basehttpserver.count](inputs/cases/document.basehttpserver.count.json) | prepared | preg_match_all() [prefix] | 191.326 | 0.44% | yes |
| [document.basehttpserver.count](inputs/cases/document.basehttpserver.count.json) | prepared | Native A/A control | 23.446 | 1.02% | yes |
| [document.basehttpserver.count](inputs/cases/document.basehttpserver.count.json) | oneshot | Matcher::countMatches() | 59.976 | 0.94% | yes |
| [document.basehttpserver.count](inputs/cases/document.basehttpserver.count.json) | oneshot | strpos() loop | 107.866 | 0.58% | yes |
| [document.basehttpserver.count](inputs/cases/document.basehttpserver.count.json) | oneshot | preg_match_all() [literal] | 179.586 | 0.50% | yes |
| [document.basehttpserver.count](inputs/cases/document.basehttpserver.count.json) | oneshot | preg_match_all() [prefix] | 190.935 | 0.34% | yes |
| [document.basehttpserver.count](inputs/cases/document.basehttpserver.count.json) | oneshot | Native A/A control | 60.195 | 0.91% | yes |
| [document.basehttpserver.all](inputs/cases/document.basehttpserver.all.json) | prepared | Matcher::matchAll() | 30.410 | 0.40% | yes |
| [document.basehttpserver.all](inputs/cases/document.basehttpserver.all.json) | prepared | strpos() loop | 111.837 | 0.72% | yes |
| [document.basehttpserver.all](inputs/cases/document.basehttpserver.all.json) | prepared | preg_match_all() [literal] | 188.043 | 1.98% | yes |
| [document.basehttpserver.all](inputs/cases/document.basehttpserver.all.json) | prepared | preg_match_all() [prefix] | 198.130 | 0.79% | yes |
| [document.basehttpserver.all](inputs/cases/document.basehttpserver.all.json) | prepared | Native A/A control | 30.466 | 0.57% | yes |
| [document.basehttpserver.all](inputs/cases/document.basehttpserver.all.json) | oneshot | Matcher::matchAll() | 60.774 | 1.84% | yes |
| [document.basehttpserver.all](inputs/cases/document.basehttpserver.all.json) | oneshot | strpos() loop | 111.884 | 0.34% | yes |
| [document.basehttpserver.all](inputs/cases/document.basehttpserver.all.json) | oneshot | preg_match_all() [literal] | 188.929 | 0.90% | yes |
| [document.basehttpserver.all](inputs/cases/document.basehttpserver.all.json) | oneshot | preg_match_all() [prefix] | 200.008 | 0.81% | yes |
| [document.basehttpserver.all](inputs/cases/document.basehttpserver.all.json) | oneshot | Native A/A control | 60.809 | 0.67% | yes |
| [document.basehttpserver.replace](inputs/cases/document.basehttpserver.replace.json) | prepared | Replacer::replace() | 24.352 | 3.74% | yes |
| [document.basehttpserver.replace](inputs/cases/document.basehttpserver.replace.json) | prepared | strtr() | 357.397 | 0.71% | yes |
| [document.basehttpserver.replace](inputs/cases/document.basehttpserver.replace.json) | prepared | preg_replace_callback() [literal] | 85.325 | 1.29% | yes |
| [document.basehttpserver.replace](inputs/cases/document.basehttpserver.replace.json) | prepared | preg_replace_callback() [prefix] | 45.568 | 3.19% | yes |
| [document.basehttpserver.replace](inputs/cases/document.basehttpserver.replace.json) | prepared | str_replace() | 114.341 | 0.59% | yes |
| [document.basehttpserver.replace](inputs/cases/document.basehttpserver.replace.json) | prepared | Native A/A control | 24.299 | 4.13% | yes |
| [document.basehttpserver.replace](inputs/cases/document.basehttpserver.replace.json) | oneshot | Replacer::replace() | 41.902 | 0.78% | yes |
| [document.basehttpserver.replace](inputs/cases/document.basehttpserver.replace.json) | oneshot | strtr() | 357.173 | 1.50% | yes |
| [document.basehttpserver.replace](inputs/cases/document.basehttpserver.replace.json) | oneshot | preg_replace_callback() [literal] | 85.556 | 2.02% | yes |
| [document.basehttpserver.replace](inputs/cases/document.basehttpserver.replace.json) | oneshot | preg_replace_callback() [prefix] | 46.774 | 4.58% | yes |
| [document.basehttpserver.replace](inputs/cases/document.basehttpserver.replace.json) | oneshot | str_replace() | 114.079 | 0.41% | yes |
| [document.basehttpserver.replace](inputs/cases/document.basehttpserver.replace.json) | oneshot | Native A/A control | 42.028 | 1.26% | yes |
| [document.collections.unique](inputs/cases/document.collections.unique.json) | prepared | Matcher::getMatchedKeywords() | 121.421 | 3.29% | yes |
| [document.collections.unique](inputs/cases/document.collections.unique.json) | prepared | strpos() loop | 437.982 | 0.30% | yes |
| [document.collections.unique](inputs/cases/document.collections.unique.json) | prepared | preg_match_all() [literal] | 711.497 | 0.64% | yes |
| [document.collections.unique](inputs/cases/document.collections.unique.json) | prepared | preg_match_all() [prefix] | 743.411 | 0.61% | yes |
| [document.collections.unique](inputs/cases/document.collections.unique.json) | prepared | Native A/A control | 121.423 | 1.35% | yes |
| [document.collections.unique](inputs/cases/document.collections.unique.json) | oneshot | Matcher::getMatchedKeywords() | 159.740 | 0.48% | yes |
| [document.collections.unique](inputs/cases/document.collections.unique.json) | oneshot | strpos() loop | 438.256 | 0.57% | yes |
| [document.collections.unique](inputs/cases/document.collections.unique.json) | oneshot | preg_match_all() [literal] | 715.375 | 0.80% | yes |
| [document.collections.unique](inputs/cases/document.collections.unique.json) | oneshot | preg_match_all() [prefix] | 742.889 | 0.81% | yes |
| [document.collections.unique](inputs/cases/document.collections.unique.json) | oneshot | Native A/A control | 160.232 | 0.51% | yes |
| [document.collections.count](inputs/cases/document.collections.count.json) | prepared | Matcher::countMatches() | 110.862 | 1.03% | yes |
| [document.collections.count](inputs/cases/document.collections.count.json) | prepared | strpos() loop | 465.301 | 0.48% | yes |
| [document.collections.count](inputs/cases/document.collections.count.json) | prepared | preg_match_all() [literal] | 708.490 | 0.69% | yes |
| [document.collections.count](inputs/cases/document.collections.count.json) | prepared | preg_match_all() [prefix] | 740.251 | 9.02% | yes |
| [document.collections.count](inputs/cases/document.collections.count.json) | prepared | Native A/A control | 111.415 | 0.87% | yes |
| [document.collections.count](inputs/cases/document.collections.count.json) | oneshot | Matcher::countMatches() | 152.189 | 0.87% | yes |
| [document.collections.count](inputs/cases/document.collections.count.json) | oneshot | strpos() loop | 466.372 | 0.76% | yes |
| [document.collections.count](inputs/cases/document.collections.count.json) | oneshot | preg_match_all() [literal] | 711.397 | 0.82% | yes |
| [document.collections.count](inputs/cases/document.collections.count.json) | oneshot | preg_match_all() [prefix] | 737.409 | 0.46% | yes |
| [document.collections.count](inputs/cases/document.collections.count.json) | oneshot | Native A/A control | 152.124 | 1.12% | yes |
| [document.collections.all](inputs/cases/document.collections.all.json) | prepared | Matcher::matchAll() | 125.967 | 0.29% | yes |
| [document.collections.all](inputs/cases/document.collections.all.json) | prepared | strpos() loop | 468.548 | 0.37% | yes |
| [document.collections.all](inputs/cases/document.collections.all.json) | prepared | preg_match_all() [literal] | 711.663 | 0.89% | yes |
| [document.collections.all](inputs/cases/document.collections.all.json) | prepared | preg_match_all() [prefix] | 744.560 | 0.60% | yes |
| [document.collections.all](inputs/cases/document.collections.all.json) | prepared | Native A/A control | 126.007 | 0.68% | yes |
| [document.collections.all](inputs/cases/document.collections.all.json) | oneshot | Matcher::matchAll() | 158.273 | 1.92% | yes |
| [document.collections.all](inputs/cases/document.collections.all.json) | oneshot | strpos() loop | 468.094 | 0.43% | yes |
| [document.collections.all](inputs/cases/document.collections.all.json) | oneshot | preg_match_all() [literal] | 713.409 | 8.93% | yes |
| [document.collections.all](inputs/cases/document.collections.all.json) | oneshot | preg_match_all() [prefix] | 743.077 | 0.95% | yes |
| [document.collections.all](inputs/cases/document.collections.all.json) | oneshot | Native A/A control | 158.581 | 0.52% | yes |
| [document.collections.replace](inputs/cases/document.collections.replace.json) | prepared | Replacer::replace() | 118.071 | 4.97% | yes |
| [document.collections.replace](inputs/cases/document.collections.replace.json) | prepared | strtr() | 1330.839 | 0.42% | yes |
| [document.collections.replace](inputs/cases/document.collections.replace.json) | prepared | preg_replace_callback() [literal] | 308.317 | 1.25% | yes |
| [document.collections.replace](inputs/cases/document.collections.replace.json) | prepared | preg_replace_callback() [prefix] | 224.880 | 1.16% | yes |
| [document.collections.replace](inputs/cases/document.collections.replace.json) | prepared | str_replace() | 503.833 | 0.84% | yes |
| [document.collections.replace](inputs/cases/document.collections.replace.json) | prepared | Native A/A control | 117.336 | 3.62% | yes |
| [document.collections.replace](inputs/cases/document.collections.replace.json) | oneshot | Replacer::replace() | 136.365 | 3.83% | yes |
| [document.collections.replace](inputs/cases/document.collections.replace.json) | oneshot | strtr() | 1330.355 | 0.58% | yes |
| [document.collections.replace](inputs/cases/document.collections.replace.json) | oneshot | preg_replace_callback() [literal] | 308.923 | 0.33% | yes |
| [document.collections.replace](inputs/cases/document.collections.replace.json) | oneshot | preg_replace_callback() [prefix] | 225.173 | 0.84% | yes |
| [document.collections.replace](inputs/cases/document.collections.replace.json) | oneshot | str_replace() | 502.786 | 0.45% | yes |
| [document.collections.replace](inputs/cases/document.collections.replace.json) | oneshot | Native A/A control | 136.582 | 4.01% | yes |
| [document.robotparser.unique](inputs/cases/document.robotparser.unique.json) | prepared | Matcher::getMatchedKeywords() | 3.387 | 3.42% | yes |
| [document.robotparser.unique](inputs/cases/document.robotparser.unique.json) | prepared | strpos() loop | 21.780 | 0.39% | yes |
| [document.robotparser.unique](inputs/cases/document.robotparser.unique.json) | prepared | preg_match_all() [literal] | 24.473 | 0.88% | yes |
| [document.robotparser.unique](inputs/cases/document.robotparser.unique.json) | prepared | preg_match_all() [prefix] | 25.532 | 0.60% | yes |
| [document.robotparser.unique](inputs/cases/document.robotparser.unique.json) | prepared | Native A/A control | 3.389 | 4.28% | yes |
| [document.robotparser.unique](inputs/cases/document.robotparser.unique.json) | oneshot | Matcher::getMatchedKeywords() | 33.159 | 1.48% | yes |
| [document.robotparser.unique](inputs/cases/document.robotparser.unique.json) | oneshot | strpos() loop | 21.801 | 0.44% | yes |
| [document.robotparser.unique](inputs/cases/document.robotparser.unique.json) | oneshot | preg_match_all() [literal] | 24.382 | 12.50% | yes |
| [document.robotparser.unique](inputs/cases/document.robotparser.unique.json) | oneshot | preg_match_all() [prefix] | 25.505 | 0.62% | yes |
| [document.robotparser.unique](inputs/cases/document.robotparser.unique.json) | oneshot | Native A/A control | 33.404 | 1.72% | yes |
| [document.robotparser.count](inputs/cases/document.robotparser.count.json) | prepared | Matcher::countMatches() | 3.176 | 3.62% | yes |
| [document.robotparser.count](inputs/cases/document.robotparser.count.json) | prepared | strpos() loop | 22.491 | 0.33% | yes |
| [document.robotparser.count](inputs/cases/document.robotparser.count.json) | prepared | preg_match_all() [literal] | 22.147 | 0.45% | yes |
| [document.robotparser.count](inputs/cases/document.robotparser.count.json) | prepared | preg_match_all() [prefix] | 23.233 | 0.74% | yes |
| [document.robotparser.count](inputs/cases/document.robotparser.count.json) | prepared | Native A/A control | 3.159 | 3.59% | yes |
| [document.robotparser.count](inputs/cases/document.robotparser.count.json) | oneshot | Matcher::countMatches() | 32.475 | 1.92% | no |
| [document.robotparser.count](inputs/cases/document.robotparser.count.json) | oneshot | strpos() loop | 22.525 | 0.41% | no |
| [document.robotparser.count](inputs/cases/document.robotparser.count.json) | oneshot | preg_match_all() [literal] | 22.152 | 0.78% | no |
| [document.robotparser.count](inputs/cases/document.robotparser.count.json) | oneshot | preg_match_all() [prefix] | 23.193 | 0.92% | no |
| [document.robotparser.count](inputs/cases/document.robotparser.count.json) | oneshot | Native A/A control | 32.676 | 16.02% | no |
| [document.robotparser.all](inputs/cases/document.robotparser.all.json) | prepared | Matcher::matchAll() | 4.720 | 5.07% | no |
| [document.robotparser.all](inputs/cases/document.robotparser.all.json) | prepared | strpos() loop | 23.158 | 0.42% | no |
| [document.robotparser.all](inputs/cases/document.robotparser.all.json) | prepared | preg_match_all() [literal] | 24.617 | 0.75% | no |
| [document.robotparser.all](inputs/cases/document.robotparser.all.json) | prepared | preg_match_all() [prefix] | 25.535 | 0.85% | no |
| [document.robotparser.all](inputs/cases/document.robotparser.all.json) | prepared | Native A/A control | 4.825 | 4.90% | no |
| [document.robotparser.all](inputs/cases/document.robotparser.all.json) | oneshot | Matcher::matchAll() | 33.802 | 1.79% | yes |
| [document.robotparser.all](inputs/cases/document.robotparser.all.json) | oneshot | strpos() loop | 23.170 | 0.30% | yes |
| [document.robotparser.all](inputs/cases/document.robotparser.all.json) | oneshot | preg_match_all() [literal] | 24.524 | 1.03% | yes |
| [document.robotparser.all](inputs/cases/document.robotparser.all.json) | oneshot | preg_match_all() [prefix] | 25.587 | 0.63% | yes |
| [document.robotparser.all](inputs/cases/document.robotparser.all.json) | oneshot | Native A/A control | 33.962 | 2.02% | yes |
| [document.robotparser.replace](inputs/cases/document.robotparser.replace.json) | prepared | Replacer::replace() | 3.136 | 1.13% | yes |
| [document.robotparser.replace](inputs/cases/document.robotparser.replace.json) | prepared | strtr() | 56.631 | 5.89% | yes |
| [document.robotparser.replace](inputs/cases/document.robotparser.replace.json) | prepared | preg_replace_callback() [literal] | 14.838 | 1.47% | yes |
| [document.robotparser.replace](inputs/cases/document.robotparser.replace.json) | prepared | preg_replace_callback() [prefix] | 7.211 | 1.52% | yes |
| [document.robotparser.replace](inputs/cases/document.robotparser.replace.json) | prepared | str_replace() | 22.675 | 0.43% | yes |
| [document.robotparser.replace](inputs/cases/document.robotparser.replace.json) | prepared | Native A/A control | 3.146 | 1.61% | yes |
| [document.robotparser.replace](inputs/cases/document.robotparser.replace.json) | oneshot | Replacer::replace() | 21.166 | 1.17% | yes |
| [document.robotparser.replace](inputs/cases/document.robotparser.replace.json) | oneshot | strtr() | 54.713 | 6.99% | yes |
| [document.robotparser.replace](inputs/cases/document.robotparser.replace.json) | oneshot | preg_replace_callback() [literal] | 14.625 | 1.70% | yes |
| [document.robotparser.replace](inputs/cases/document.robotparser.replace.json) | oneshot | preg_replace_callback() [prefix] | 7.271 | 0.56% | yes |
| [document.robotparser.replace](inputs/cases/document.robotparser.replace.json) | oneshot | str_replace() | 22.667 | 0.56% | yes |
| [document.robotparser.replace](inputs/cases/document.robotparser.replace.json) | oneshot | Native A/A control | 21.141 | 1.04% | yes |
| [email.account-deletion.html](inputs/cases/email.account-deletion.html.json) | oneshot | Replacer::replace() | 23.021 | 1.21% | yes |
| [email.account-deletion.html](inputs/cases/email.account-deletion.html.json) | oneshot | strtr() | 11.608 | 1.43% | yes |
| [email.account-deletion.html](inputs/cases/email.account-deletion.html.json) | oneshot | preg_replace_callback() [literal] | 1.515 | 0.36% | yes |
| [email.account-deletion.html](inputs/cases/email.account-deletion.html.json) | oneshot | preg_replace_callback() [prefix] | 1.517 | 0.49% | yes |
| [email.account-deletion.html](inputs/cases/email.account-deletion.html.json) | oneshot | str_replace() | 14.464 | 0.77% | yes |
| [email.account-deletion.html](inputs/cases/email.account-deletion.html.json) | oneshot | preg_replace_callback() [tokens] | 1.714 | 0.69% | yes |
| [email.account-deletion.html](inputs/cases/email.account-deletion.html.json) | oneshot | Native A/A control | 23.020 | 0.64% | yes |
| [email.account-deletion.txt](inputs/cases/email.account-deletion.txt.json) | oneshot | Replacer::replace() | 1.989 | 0.50% | yes |
| [email.account-deletion.txt](inputs/cases/email.account-deletion.txt.json) | oneshot | strtr() | 0.544 | 1.14% | yes |
| [email.account-deletion.txt](inputs/cases/email.account-deletion.txt.json) | oneshot | preg_replace_callback() [literal] | 0.650 | 0.52% | yes |
| [email.account-deletion.txt](inputs/cases/email.account-deletion.txt.json) | oneshot | preg_replace_callback() [prefix] | 0.648 | 0.55% | yes |
| [email.account-deletion.txt](inputs/cases/email.account-deletion.txt.json) | oneshot | str_replace() | 0.371 | 1.12% | yes |
| [email.account-deletion.txt](inputs/cases/email.account-deletion.txt.json) | oneshot | preg_replace_callback() [tokens] | 0.687 | 1.02% | yes |
| [email.account-deletion.txt](inputs/cases/email.account-deletion.txt.json) | oneshot | Native A/A control | 1.990 | 0.61% | yes |
| [email.email-verification.html](inputs/cases/email.email-verification.html.json) | oneshot | Replacer::replace() | 22.373 | 1.22% | yes |
| [email.email-verification.html](inputs/cases/email.email-verification.html.json) | oneshot | strtr() | 11.446 | 0.76% | yes |
| [email.email-verification.html](inputs/cases/email.email-verification.html.json) | oneshot | preg_replace_callback() [literal] | 1.478 | 0.83% | yes |
| [email.email-verification.html](inputs/cases/email.email-verification.html.json) | oneshot | preg_replace_callback() [prefix] | 1.453 | 0.78% | yes |
| [email.email-verification.html](inputs/cases/email.email-verification.html.json) | oneshot | str_replace() | 15.529 | 1.02% | yes |
| [email.email-verification.html](inputs/cases/email.email-verification.html.json) | oneshot | preg_replace_callback() [tokens] | 1.553 | 0.92% | yes |
| [email.email-verification.html](inputs/cases/email.email-verification.html.json) | oneshot | Native A/A control | 22.454 | 0.81% | yes |
| [email.email-verification.txt](inputs/cases/email.email-verification.txt.json) | oneshot | Replacer::replace() | 1.782 | 0.48% | yes |
| [email.email-verification.txt](inputs/cases/email.email-verification.txt.json) | oneshot | strtr() | 0.441 | 0.52% | yes |
| [email.email-verification.txt](inputs/cases/email.email-verification.txt.json) | oneshot | preg_replace_callback() [literal] | 0.552 | 13.89% | yes |
| [email.email-verification.txt](inputs/cases/email.email-verification.txt.json) | oneshot | preg_replace_callback() [prefix] | 0.549 | 0.40% | yes |
| [email.email-verification.txt](inputs/cases/email.email-verification.txt.json) | oneshot | str_replace() | 0.355 | 0.76% | yes |
| [email.email-verification.txt](inputs/cases/email.email-verification.txt.json) | oneshot | preg_replace_callback() [tokens] | 0.573 | 0.39% | yes |
| [email.email-verification.txt](inputs/cases/email.email-verification.txt.json) | oneshot | Native A/A control | 1.785 | 0.46% | yes |
| [email.magic-link.html](inputs/cases/email.magic-link.html.json) | oneshot | Replacer::replace() | 21.660 | 1.66% | yes |
| [email.magic-link.html](inputs/cases/email.magic-link.html.json) | oneshot | strtr() | 11.100 | 1.21% | yes |
| [email.magic-link.html](inputs/cases/email.magic-link.html.json) | oneshot | preg_replace_callback() [literal] | 1.477 | 1.26% | yes |
| [email.magic-link.html](inputs/cases/email.magic-link.html.json) | oneshot | preg_replace_callback() [prefix] | 1.472 | 2.30% | yes |
| [email.magic-link.html](inputs/cases/email.magic-link.html.json) | oneshot | str_replace() | 14.983 | 0.36% | yes |
| [email.magic-link.html](inputs/cases/email.magic-link.html.json) | oneshot | preg_replace_callback() [tokens] | 1.669 | 6.72% | yes |
| [email.magic-link.html](inputs/cases/email.magic-link.html.json) | oneshot | Native A/A control | 21.653 | 1.02% | yes |
| [email.magic-link.txt](inputs/cases/email.magic-link.txt.json) | oneshot | Replacer::replace() | 1.495 | 1.07% | yes |
| [email.magic-link.txt](inputs/cases/email.magic-link.txt.json) | oneshot | strtr() | 0.408 | 1.06% | yes |
| [email.magic-link.txt](inputs/cases/email.magic-link.txt.json) | oneshot | preg_replace_callback() [literal] | 0.452 | 11.35% | yes |
| [email.magic-link.txt](inputs/cases/email.magic-link.txt.json) | oneshot | preg_replace_callback() [prefix] | 0.453 | 0.63% | yes |
| [email.magic-link.txt](inputs/cases/email.magic-link.txt.json) | oneshot | str_replace() | 0.281 | 1.31% | yes |
| [email.magic-link.txt](inputs/cases/email.magic-link.txt.json) | oneshot | preg_replace_callback() [tokens] | 0.474 | 19.29% | yes |
| [email.magic-link.txt](inputs/cases/email.magic-link.txt.json) | oneshot | Native A/A control | 1.495 | 0.62% | yes |
| [email.new-sign-in.html](inputs/cases/email.new-sign-in.html.json) | oneshot | Replacer::replace() | 34.629 | 0.65% | yes |
| [email.new-sign-in.html](inputs/cases/email.new-sign-in.html.json) | oneshot | strtr() | 17.074 | 2.19% | yes |
| [email.new-sign-in.html](inputs/cases/email.new-sign-in.html.json) | oneshot | preg_replace_callback() [literal] | 15.854 | 2.36% | yes |
| [email.new-sign-in.html](inputs/cases/email.new-sign-in.html.json) | oneshot | preg_replace_callback() [prefix] | 15.849 | 0.91% | yes |
| [email.new-sign-in.html](inputs/cases/email.new-sign-in.html.json) | oneshot | str_replace() | 58.163 | 0.62% | yes |
| [email.new-sign-in.html](inputs/cases/email.new-sign-in.html.json) | oneshot | preg_replace_callback() [tokens] | 2.411 | 1.44% | yes |
| [email.new-sign-in.html](inputs/cases/email.new-sign-in.html.json) | oneshot | Native A/A control | 34.709 | 0.54% | yes |
| [email.new-sign-in.txt](inputs/cases/email.new-sign-in.txt.json) | oneshot | Replacer::replace() | 2.855 | 0.83% | yes |
| [email.new-sign-in.txt](inputs/cases/email.new-sign-in.txt.json) | oneshot | strtr() | 0.659 | 1.12% | yes |
| [email.new-sign-in.txt](inputs/cases/email.new-sign-in.txt.json) | oneshot | preg_replace_callback() [literal] | 1.116 | 1.99% | yes |
| [email.new-sign-in.txt](inputs/cases/email.new-sign-in.txt.json) | oneshot | preg_replace_callback() [prefix] | 1.121 | 0.83% | yes |
| [email.new-sign-in.txt](inputs/cases/email.new-sign-in.txt.json) | oneshot | str_replace() | 0.677 | 0.72% | yes |
| [email.new-sign-in.txt](inputs/cases/email.new-sign-in.txt.json) | oneshot | preg_replace_callback() [tokens] | 0.873 | 0.67% | yes |
| [email.new-sign-in.txt](inputs/cases/email.new-sign-in.txt.json) | oneshot | Native A/A control | 2.855 | 0.84% | yes |
| [email.one-time-code.html](inputs/cases/email.one-time-code.html.json) | oneshot | Replacer::replace() | 18.180 | 0.87% | yes |
| [email.one-time-code.html](inputs/cases/email.one-time-code.html.json) | oneshot | strtr() | 9.840 | 1.38% | yes |
| [email.one-time-code.html](inputs/cases/email.one-time-code.html.json) | oneshot | preg_replace_callback() [literal] | 1.451 | 0.50% | yes |
| [email.one-time-code.html](inputs/cases/email.one-time-code.html.json) | oneshot | preg_replace_callback() [prefix] | 1.458 | 0.57% | yes |
| [email.one-time-code.html](inputs/cases/email.one-time-code.html.json) | oneshot | str_replace() | 7.400 | 0.52% | yes |
| [email.one-time-code.html](inputs/cases/email.one-time-code.html.json) | oneshot | preg_replace_callback() [tokens] | 1.637 | 0.37% | yes |
| [email.one-time-code.html](inputs/cases/email.one-time-code.html.json) | oneshot | Native A/A control | 18.138 | 0.80% | yes |
| [email.one-time-code.txt](inputs/cases/email.one-time-code.txt.json) | oneshot | Replacer::replace() | 1.522 | 0.57% | yes |
| [email.one-time-code.txt](inputs/cases/email.one-time-code.txt.json) | oneshot | strtr() | 0.476 | 1.43% | yes |
| [email.one-time-code.txt](inputs/cases/email.one-time-code.txt.json) | oneshot | preg_replace_callback() [literal] | 0.457 | 0.60% | yes |
| [email.one-time-code.txt](inputs/cases/email.one-time-code.txt.json) | oneshot | preg_replace_callback() [prefix] | 0.453 | 0.68% | yes |
| [email.one-time-code.txt](inputs/cases/email.one-time-code.txt.json) | oneshot | str_replace() | 0.280 | 1.81% | yes |
| [email.one-time-code.txt](inputs/cases/email.one-time-code.txt.json) | oneshot | preg_replace_callback() [tokens] | 0.475 | 15.54% | yes |
| [email.one-time-code.txt](inputs/cases/email.one-time-code.txt.json) | oneshot | Native A/A control | 1.521 | 0.66% | yes |
| [email.password-reset.html](inputs/cases/email.password-reset.html.json) | oneshot | Replacer::replace() | 23.674 | 0.77% | yes |
| [email.password-reset.html](inputs/cases/email.password-reset.html.json) | oneshot | strtr() | 11.763 | 0.52% | yes |
| [email.password-reset.html](inputs/cases/email.password-reset.html.json) | oneshot | preg_replace_callback() [literal] | 1.807 | 1.16% | yes |
| [email.password-reset.html](inputs/cases/email.password-reset.html.json) | oneshot | preg_replace_callback() [prefix] | 1.817 | 0.63% | yes |
| [email.password-reset.html](inputs/cases/email.password-reset.html.json) | oneshot | str_replace() | 16.349 | 1.01% | yes |
| [email.password-reset.html](inputs/cases/email.password-reset.html.json) | oneshot | preg_replace_callback() [tokens] | 1.976 | 15.35% | yes |
| [email.password-reset.html](inputs/cases/email.password-reset.html.json) | oneshot | Native A/A control | 23.743 | 1.27% | yes |
| [email.password-reset.txt](inputs/cases/email.password-reset.txt.json) | oneshot | Replacer::replace() | 1.759 | 1.87% | yes |
| [email.password-reset.txt](inputs/cases/email.password-reset.txt.json) | oneshot | strtr() | 0.481 | 1.63% | yes |
| [email.password-reset.txt](inputs/cases/email.password-reset.txt.json) | oneshot | preg_replace_callback() [literal] | 0.563 | 1.47% | yes |
| [email.password-reset.txt](inputs/cases/email.password-reset.txt.json) | oneshot | preg_replace_callback() [prefix] | 0.554 | 1.78% | yes |
| [email.password-reset.txt](inputs/cases/email.password-reset.txt.json) | oneshot | str_replace() | 0.355 | 0.88% | yes |
| [email.password-reset.txt](inputs/cases/email.password-reset.txt.json) | oneshot | preg_replace_callback() [tokens] | 0.588 | 1.61% | yes |
| [email.password-reset.txt](inputs/cases/email.password-reset.txt.json) | oneshot | Native A/A control | 1.764 | 1.19% | yes |
| [email.payment-failed.html](inputs/cases/email.payment-failed.html.json) | oneshot | Replacer::replace() | 30.834 | 1.02% | yes |
| [email.payment-failed.html](inputs/cases/email.payment-failed.html.json) | oneshot | strtr() | 15.562 | 1.95% | yes |
| [email.payment-failed.html](inputs/cases/email.payment-failed.html.json) | oneshot | preg_replace_callback() [literal] | 18.973 | 0.29% | yes |
| [email.payment-failed.html](inputs/cases/email.payment-failed.html.json) | oneshot | preg_replace_callback() [prefix] | 18.986 | 2.19% | yes |
| [email.payment-failed.html](inputs/cases/email.payment-failed.html.json) | oneshot | str_replace() | 51.122 | 0.76% | yes |
| [email.payment-failed.html](inputs/cases/email.payment-failed.html.json) | oneshot | preg_replace_callback() [tokens] | 2.453 | 0.74% | yes |
| [email.payment-failed.html](inputs/cases/email.payment-failed.html.json) | oneshot | Native A/A control | 30.906 | 0.67% | yes |
| [email.payment-failed.txt](inputs/cases/email.payment-failed.txt.json) | oneshot | Replacer::replace() | 2.692 | 2.84% | yes |
| [email.payment-failed.txt](inputs/cases/email.payment-failed.txt.json) | oneshot | strtr() | 0.657 | 0.76% | yes |
| [email.payment-failed.txt](inputs/cases/email.payment-failed.txt.json) | oneshot | preg_replace_callback() [literal] | 1.231 | 0.52% | yes |
| [email.payment-failed.txt](inputs/cases/email.payment-failed.txt.json) | oneshot | preg_replace_callback() [prefix] | 1.240 | 0.54% | yes |
| [email.payment-failed.txt](inputs/cases/email.payment-failed.txt.json) | oneshot | str_replace() | 0.759 | 0.91% | yes |
| [email.payment-failed.txt](inputs/cases/email.payment-failed.txt.json) | oneshot | preg_replace_callback() [tokens] | 1.035 | 0.80% | yes |
| [email.payment-failed.txt](inputs/cases/email.payment-failed.txt.json) | oneshot | Native A/A control | 2.694 | 1.01% | yes |
| [email.receipt.html](inputs/cases/email.receipt.html.json) | oneshot | Replacer::replace() | 40.266 | 0.68% | yes |
| [email.receipt.html](inputs/cases/email.receipt.html.json) | oneshot | strtr() | 21.453 | 2.21% | yes |
| [email.receipt.html](inputs/cases/email.receipt.html.json) | oneshot | preg_replace_callback() [literal] | 3.133 | 0.85% | yes |
| [email.receipt.html](inputs/cases/email.receipt.html.json) | oneshot | preg_replace_callback() [prefix] | 3.046 | 0.62% | yes |
| [email.receipt.html](inputs/cases/email.receipt.html.json) | oneshot | str_replace() | 107.694 | 0.69% | yes |
| [email.receipt.html](inputs/cases/email.receipt.html.json) | oneshot | preg_replace_callback() [tokens] | 3.143 | 0.48% | yes |
| [email.receipt.html](inputs/cases/email.receipt.html.json) | oneshot | Native A/A control | 40.220 | 0.67% | yes |
| [email.receipt.txt](inputs/cases/email.receipt.txt.json) | oneshot | Replacer::replace() | 3.937 | 0.47% | yes |
| [email.receipt.txt](inputs/cases/email.receipt.txt.json) | oneshot | strtr() | 0.812 | 0.75% | yes |
| [email.receipt.txt](inputs/cases/email.receipt.txt.json) | oneshot | preg_replace_callback() [literal] | 1.283 | 0.45% | yes |
| [email.receipt.txt](inputs/cases/email.receipt.txt.json) | oneshot | preg_replace_callback() [prefix] | 1.279 | 0.63% | yes |
| [email.receipt.txt](inputs/cases/email.receipt.txt.json) | oneshot | str_replace() | 1.386 | 0.34% | yes |
| [email.receipt.txt](inputs/cases/email.receipt.txt.json) | oneshot | preg_replace_callback() [tokens] | 1.352 | 0.97% | yes |
| [email.receipt.txt](inputs/cases/email.receipt.txt.json) | oneshot | Native A/A control | 3.935 | 0.62% | yes |
| [email.subscription-renewal.html](inputs/cases/email.subscription-renewal.html.json) | oneshot | Replacer::replace() | 32.214 | 0.67% | yes |
| [email.subscription-renewal.html](inputs/cases/email.subscription-renewal.html.json) | oneshot | strtr() | 16.811 | 3.06% | yes |
| [email.subscription-renewal.html](inputs/cases/email.subscription-renewal.html.json) | oneshot | preg_replace_callback() [literal] | 14.968 | 0.37% | yes |
| [email.subscription-renewal.html](inputs/cases/email.subscription-renewal.html.json) | oneshot | preg_replace_callback() [prefix] | 14.980 | 0.39% | yes |
| [email.subscription-renewal.html](inputs/cases/email.subscription-renewal.html.json) | oneshot | str_replace() | 53.860 | 0.96% | yes |
| [email.subscription-renewal.html](inputs/cases/email.subscription-renewal.html.json) | oneshot | preg_replace_callback() [tokens] | 2.909 | 0.68% | yes |
| [email.subscription-renewal.html](inputs/cases/email.subscription-renewal.html.json) | oneshot | Native A/A control | 32.279 | 0.51% | yes |
| [email.subscription-renewal.txt](inputs/cases/email.subscription-renewal.txt.json) | oneshot | Replacer::replace() | 2.782 | 1.03% | yes |
| [email.subscription-renewal.txt](inputs/cases/email.subscription-renewal.txt.json) | oneshot | strtr() | 0.707 | 0.70% | yes |
| [email.subscription-renewal.txt](inputs/cases/email.subscription-renewal.txt.json) | oneshot | preg_replace_callback() [literal] | 1.189 | 0.56% | yes |
| [email.subscription-renewal.txt](inputs/cases/email.subscription-renewal.txt.json) | oneshot | preg_replace_callback() [prefix] | 1.195 | 0.40% | yes |
| [email.subscription-renewal.txt](inputs/cases/email.subscription-renewal.txt.json) | oneshot | str_replace() | 0.771 | 0.43% | yes |
| [email.subscription-renewal.txt](inputs/cases/email.subscription-renewal.txt.json) | oneshot | preg_replace_callback() [tokens] | 1.149 | 0.50% | yes |
| [email.subscription-renewal.txt](inputs/cases/email.subscription-renewal.txt.json) | oneshot | Native A/A control | 2.784 | 0.96% | yes |
| [email.team-invite.html](inputs/cases/email.team-invite.html.json) | oneshot | Replacer::replace() | 24.153 | 1.37% | yes |
| [email.team-invite.html](inputs/cases/email.team-invite.html.json) | oneshot | strtr() | 11.986 | 1.47% | yes |
| [email.team-invite.html](inputs/cases/email.team-invite.html.json) | oneshot | preg_replace_callback() [literal] | 8.726 | 0.22% | yes |
| [email.team-invite.html](inputs/cases/email.team-invite.html.json) | oneshot | preg_replace_callback() [prefix] | 8.765 | 0.49% | yes |
| [email.team-invite.html](inputs/cases/email.team-invite.html.json) | oneshot | str_replace() | 30.049 | 1.35% | yes |
| [email.team-invite.html](inputs/cases/email.team-invite.html.json) | oneshot | preg_replace_callback() [tokens] | 2.323 | 1.07% | yes |
| [email.team-invite.html](inputs/cases/email.team-invite.html.json) | oneshot | Native A/A control | 24.152 | 0.86% | yes |
| [email.team-invite.txt](inputs/cases/email.team-invite.txt.json) | oneshot | Replacer::replace() | 2.217 | 0.86% | yes |
| [email.team-invite.txt](inputs/cases/email.team-invite.txt.json) | oneshot | strtr() | 0.511 | 0.65% | yes |
| [email.team-invite.txt](inputs/cases/email.team-invite.txt.json) | oneshot | preg_replace_callback() [literal] | 0.860 | 0.68% | yes |
| [email.team-invite.txt](inputs/cases/email.team-invite.txt.json) | oneshot | preg_replace_callback() [prefix] | 0.868 | 0.97% | yes |
| [email.team-invite.txt](inputs/cases/email.team-invite.txt.json) | oneshot | str_replace() | 0.571 | 0.67% | yes |
| [email.team-invite.txt](inputs/cases/email.team-invite.txt.json) | oneshot | preg_replace_callback() [tokens] | 0.852 | 1.33% | yes |
| [email.team-invite.txt](inputs/cases/email.team-invite.txt.json) | oneshot | Native A/A control | 2.218 | 0.52% | yes |
| [email.usage-alert.html](inputs/cases/email.usage-alert.html.json) | oneshot | Replacer::replace() | 32.174 | 0.87% | yes |
| [email.usage-alert.html](inputs/cases/email.usage-alert.html.json) | oneshot | strtr() | 16.069 | 1.86% | yes |
| [email.usage-alert.html](inputs/cases/email.usage-alert.html.json) | oneshot | preg_replace_callback() [literal] | 19.977 | 0.31% | yes |
| [email.usage-alert.html](inputs/cases/email.usage-alert.html.json) | oneshot | preg_replace_callback() [prefix] | 20.007 | 0.35% | yes |
| [email.usage-alert.html](inputs/cases/email.usage-alert.html.json) | oneshot | str_replace() | 56.516 | 0.49% | yes |
| [email.usage-alert.html](inputs/cases/email.usage-alert.html.json) | oneshot | preg_replace_callback() [tokens] | 2.986 | 0.82% | yes |
| [email.usage-alert.html](inputs/cases/email.usage-alert.html.json) | oneshot | Native A/A control | 32.110 | 0.62% | yes |
| [email.usage-alert.txt](inputs/cases/email.usage-alert.txt.json) | oneshot | Replacer::replace() | 2.930 | 4.09% | no |
| [email.usage-alert.txt](inputs/cases/email.usage-alert.txt.json) | oneshot | strtr() | 0.643 | 1.78% | no |
| [email.usage-alert.txt](inputs/cases/email.usage-alert.txt.json) | oneshot | preg_replace_callback() [literal] | 1.149 | 9.00% | no |
| [email.usage-alert.txt](inputs/cases/email.usage-alert.txt.json) | oneshot | preg_replace_callback() [prefix] | 1.155 | 7.98% | no |
| [email.usage-alert.txt](inputs/cases/email.usage-alert.txt.json) | oneshot | str_replace() | 0.804 | 1.84% | no |
| [email.usage-alert.txt](inputs/cases/email.usage-alert.txt.json) | oneshot | preg_replace_callback() [tokens] | 0.962 | 11.10% | no |
| [email.usage-alert.txt](inputs/cases/email.usage-alert.txt.json) | oneshot | Native A/A control | 2.931 | 6.29% | no |
| [email.welcome.html](inputs/cases/email.welcome.html.json) | oneshot | Replacer::replace() | 26.326 | 0.74% | yes |
| [email.welcome.html](inputs/cases/email.welcome.html.json) | oneshot | strtr() | 12.765 | 1.46% | yes |
| [email.welcome.html](inputs/cases/email.welcome.html.json) | oneshot | preg_replace_callback() [literal] | 1.264 | 0.75% | yes |
| [email.welcome.html](inputs/cases/email.welcome.html.json) | oneshot | preg_replace_callback() [prefix] | 1.260 | 0.41% | yes |
| [email.welcome.html](inputs/cases/email.welcome.html.json) | oneshot | str_replace() | 16.305 | 0.99% | yes |
| [email.welcome.html](inputs/cases/email.welcome.html.json) | oneshot | preg_replace_callback() [tokens] | 1.437 | 0.91% | yes |
| [email.welcome.html](inputs/cases/email.welcome.html.json) | oneshot | Native A/A control | 26.362 | 0.65% | yes |
| [email.welcome.txt](inputs/cases/email.welcome.txt.json) | oneshot | Replacer::replace() | 2.008 | 0.55% | yes |
| [email.welcome.txt](inputs/cases/email.welcome.txt.json) | oneshot | strtr() | 0.632 | 0.80% | yes |
| [email.welcome.txt](inputs/cases/email.welcome.txt.json) | oneshot | preg_replace_callback() [literal] | 0.579 | 0.77% | yes |
| [email.welcome.txt](inputs/cases/email.welcome.txt.json) | oneshot | preg_replace_callback() [prefix] | 0.567 | 0.68% | yes |
| [email.welcome.txt](inputs/cases/email.welcome.txt.json) | oneshot | str_replace() | 0.359 | 1.10% | yes |
| [email.welcome.txt](inputs/cases/email.welcome.txt.json) | oneshot | preg_replace_callback() [tokens] | 0.592 | 0.63% | yes |
| [email.welcome.txt](inputs/cases/email.welcome.txt.json) | oneshot | Native A/A control | 2.006 | 1.18% | yes |
| [batch.validation.any.b1](inputs/cases/batch.validation.any.b1.json) | batch | Matcher::matches() | 295.954 | 0.57% | yes |
| [batch.validation.any.b1](inputs/cases/batch.validation.any.b1.json) | batch | stripos() loop | 38.157 | 0.64% | yes |
| [batch.validation.any.b1](inputs/cases/batch.validation.any.b1.json) | batch | preg_match() [literal] | 180.480 | 0.74% | yes |
| [batch.validation.any.b1](inputs/cases/batch.validation.any.b1.json) | batch | preg_match() [prefix] | 6.610 | 1.06% | yes |
| [batch.validation.any.b1](inputs/cases/batch.validation.any.b1.json) | batch | strtolower() + strpos() loop | 32.997 | 0.70% | yes |
| [batch.validation.any.b1](inputs/cases/batch.validation.any.b1.json) | batch | Native A/A control | 296.413 | 0.43% | yes |
| [batch.validation.unique.b1](inputs/cases/batch.validation.unique.b1.json) | batch | Matcher::getMatchedKeywords() | 298.619 | 0.88% | yes |
| [batch.validation.unique.b1](inputs/cases/batch.validation.unique.b1.json) | batch | stripos() loop | 38.465 | 0.90% | yes |
| [batch.validation.unique.b1](inputs/cases/batch.validation.unique.b1.json) | batch | preg_match_all() [literal] | 60.947 | 1.72% | yes |
| [batch.validation.unique.b1](inputs/cases/batch.validation.unique.b1.json) | batch | preg_match_all() [prefix] | 31.455 | 1.25% | yes |
| [batch.validation.unique.b1](inputs/cases/batch.validation.unique.b1.json) | batch | strtolower() + strpos() loop | 33.161 | 0.62% | yes |
| [batch.validation.unique.b1](inputs/cases/batch.validation.unique.b1.json) | batch | Native A/A control | 298.273 | 1.19% | yes |
| [batch.validation.any.b4](inputs/cases/batch.validation.any.b4.json) | batch | Matcher::matches() | 301.606 | 14.20% | no |
| [batch.validation.any.b4](inputs/cases/batch.validation.any.b4.json) | batch | stripos() loop | 149.320 | 41.55% | no |
| [batch.validation.any.b4](inputs/cases/batch.validation.any.b4.json) | batch | preg_match() [literal] | 741.924 | 2.34% | no |
| [batch.validation.any.b4](inputs/cases/batch.validation.any.b4.json) | batch | preg_match() [prefix] | 28.047 | 1.92% | no |
| [batch.validation.any.b4](inputs/cases/batch.validation.any.b4.json) | batch | strtolower() + strpos() loop | 144.431 | 1.39% | no |
| [batch.validation.any.b4](inputs/cases/batch.validation.any.b4.json) | batch | Native A/A control | 301.138 | 1.15% | no |
| [batch.validation.unique.b4](inputs/cases/batch.validation.unique.b4.json) | batch | Matcher::getMatchedKeywords() | 304.377 | 0.91% | no |
| [batch.validation.unique.b4](inputs/cases/batch.validation.unique.b4.json) | batch | stripos() loop | 214.984 | 1.10% | no |
| [batch.validation.unique.b4](inputs/cases/batch.validation.unique.b4.json) | batch | preg_match_all() [literal] | 326.618 | 0.98% | no |
| [batch.validation.unique.b4](inputs/cases/batch.validation.unique.b4.json) | batch | preg_match_all() [prefix] | 260.054 | 1.41% | no |
| [batch.validation.unique.b4](inputs/cases/batch.validation.unique.b4.json) | batch | strtolower() + strpos() loop | 203.957 | 2.94% | no |
| [batch.validation.unique.b4](inputs/cases/batch.validation.unique.b4.json) | batch | Native A/A control | 305.305 | 3.23% | no |
| [batch.validation.any.b16](inputs/cases/batch.validation.any.b16.json) | batch | Matcher::matches() | 307.352 | 0.85% | yes |
| [batch.validation.any.b16](inputs/cases/batch.validation.any.b16.json) | batch | stripos() loop | 462.872 | 0.58% | yes |
| [batch.validation.any.b16](inputs/cases/batch.validation.any.b16.json) | batch | preg_match() [literal] | 1615.463 | 0.80% | yes |
| [batch.validation.any.b16](inputs/cases/batch.validation.any.b16.json) | batch | preg_match() [prefix] | 72.476 | 1.71% | yes |
| [batch.validation.any.b16](inputs/cases/batch.validation.any.b16.json) | batch | strtolower() + strpos() loop | 409.087 | 0.76% | yes |
| [batch.validation.any.b16](inputs/cases/batch.validation.any.b16.json) | batch | Native A/A control | 306.850 | 1.29% | yes |
| [batch.validation.unique.b16](inputs/cases/batch.validation.unique.b16.json) | batch | Matcher::getMatchedKeywords() | 312.351 | 0.81% | yes |
| [batch.validation.unique.b16](inputs/cases/batch.validation.unique.b16.json) | batch | stripos() loop | 679.779 | 0.55% | yes |
| [batch.validation.unique.b16](inputs/cases/batch.validation.unique.b16.json) | batch | preg_match_all() [literal] | 873.873 | 1.42% | yes |
| [batch.validation.unique.b16](inputs/cases/batch.validation.unique.b16.json) | batch | preg_match_all() [prefix] | 726.520 | 0.71% | yes |
| [batch.validation.unique.b16](inputs/cases/batch.validation.unique.b16.json) | batch | strtolower() + strpos() loop | 601.791 | 0.53% | yes |
| [batch.validation.unique.b16](inputs/cases/batch.validation.unique.b16.json) | batch | Native A/A control | 312.924 | 0.60% | yes |
| [batch.validation.any.b64](inputs/cases/batch.validation.any.b64.json) | batch | Matcher::matches() | 340.234 | 0.93% | yes |
| [batch.validation.any.b64](inputs/cases/batch.validation.any.b64.json) | batch | stripos() loop | 1934.656 | 0.65% | yes |
| [batch.validation.any.b64](inputs/cases/batch.validation.any.b64.json) | batch | preg_match() [literal] | 6225.493 | 0.39% | yes |
| [batch.validation.any.b64](inputs/cases/batch.validation.any.b64.json) | batch | preg_match() [prefix] | 328.861 | 0.56% | yes |
| [batch.validation.any.b64](inputs/cases/batch.validation.any.b64.json) | batch | strtolower() + strpos() loop | 1696.011 | 1.02% | yes |
| [batch.validation.any.b64](inputs/cases/batch.validation.any.b64.json) | batch | Native A/A control | 341.137 | 0.98% | yes |
| [batch.validation.unique.b64](inputs/cases/batch.validation.unique.b64.json) | batch | Matcher::getMatchedKeywords() | 357.304 | 1.39% | yes |
| [batch.validation.unique.b64](inputs/cases/batch.validation.unique.b64.json) | batch | stripos() loop | 2753.269 | 0.61% | yes |
| [batch.validation.unique.b64](inputs/cases/batch.validation.unique.b64.json) | batch | preg_match_all() [literal] | 3599.235 | 1.41% | yes |
| [batch.validation.unique.b64](inputs/cases/batch.validation.unique.b64.json) | batch | preg_match_all() [prefix] | 3012.912 | 0.30% | yes |
| [batch.validation.unique.b64](inputs/cases/batch.validation.unique.b64.json) | batch | strtolower() + strpos() loop | 2461.223 | 0.64% | yes |
| [batch.validation.unique.b64](inputs/cases/batch.validation.unique.b64.json) | batch | Native A/A control | 356.853 | 0.76% | yes |
| [batch.references.unique.b1](inputs/cases/batch.references.unique.b1.json) | batch | Matcher::getMatchedKeywords() | 154.219 | 0.72% | yes |
| [batch.references.unique.b1](inputs/cases/batch.references.unique.b1.json) | batch | strpos() loop | 413.443 | 0.45% | yes |
| [batch.references.unique.b1](inputs/cases/batch.references.unique.b1.json) | batch | preg_match_all() [literal] | 728.343 | 0.43% | yes |
| [batch.references.unique.b1](inputs/cases/batch.references.unique.b1.json) | batch | preg_match_all() [prefix] | 756.431 | 0.48% | yes |
| [batch.references.unique.b1](inputs/cases/batch.references.unique.b1.json) | batch | Native A/A control | 154.260 | 0.93% | yes |
| [batch.references.count.b1](inputs/cases/batch.references.count.b1.json) | batch | Matcher::countMatches() | 150.029 | 1.61% | yes |
| [batch.references.count.b1](inputs/cases/batch.references.count.b1.json) | batch | strpos() loop | 449.482 | 0.63% | yes |
| [batch.references.count.b1](inputs/cases/batch.references.count.b1.json) | batch | preg_match_all() [literal] | 717.420 | 0.46% | yes |
| [batch.references.count.b1](inputs/cases/batch.references.count.b1.json) | batch | preg_match_all() [prefix] | 742.263 | 0.60% | yes |
| [batch.references.count.b1](inputs/cases/batch.references.count.b1.json) | batch | Native A/A control | 150.128 | 0.91% | yes |
| [batch.references.all.b1](inputs/cases/batch.references.all.b1.json) | batch | Matcher::matchAll() | 148.757 | 5.01% | no |
| [batch.references.all.b1](inputs/cases/batch.references.all.b1.json) | batch | strpos() loop | 462.594 | 2.30% | no |
| [batch.references.all.b1](inputs/cases/batch.references.all.b1.json) | batch | preg_match_all() [literal] | 735.844 | 5.54% | no |
| [batch.references.all.b1](inputs/cases/batch.references.all.b1.json) | batch | preg_match_all() [prefix] | 762.200 | 4.58% | no |
| [batch.references.all.b1](inputs/cases/batch.references.all.b1.json) | batch | Native A/A control | 148.980 | 5.17% | no |
| [batch.rewrite.replace.b1](inputs/cases/batch.rewrite.replace.b1.json) | batch | Replacer::replace() | 122.920 | 1.72% | yes |
| [batch.rewrite.replace.b1](inputs/cases/batch.rewrite.replace.b1.json) | batch | strtr() | 1375.748 | 0.65% | yes |
| [batch.rewrite.replace.b1](inputs/cases/batch.rewrite.replace.b1.json) | batch | preg_replace_callback() [literal] | 320.192 | 1.25% | yes |
| [batch.rewrite.replace.b1](inputs/cases/batch.rewrite.replace.b1.json) | batch | preg_replace_callback() [prefix] | 233.945 | 4.48% | yes |
| [batch.rewrite.replace.b1](inputs/cases/batch.rewrite.replace.b1.json) | batch | str_replace() | 509.952 | 0.49% | yes |
| [batch.rewrite.replace.b1](inputs/cases/batch.rewrite.replace.b1.json) | batch | Native A/A control | 123.665 | 3.78% | yes |
| [batch.references.unique.b4](inputs/cases/batch.references.unique.b4.json) | batch | Matcher::getMatchedKeywords() | 315.984 | 0.27% | yes |
| [batch.references.unique.b4](inputs/cases/batch.references.unique.b4.json) | batch | strpos() loop | 1096.212 | 0.40% | yes |
| [batch.references.unique.b4](inputs/cases/batch.references.unique.b4.json) | batch | preg_match_all() [literal] | 1739.834 | 0.58% | yes |
| [batch.references.unique.b4](inputs/cases/batch.references.unique.b4.json) | batch | preg_match_all() [prefix] | 1779.880 | 1.68% | yes |
| [batch.references.unique.b4](inputs/cases/batch.references.unique.b4.json) | batch | Native A/A control | 316.563 | 0.44% | yes |
| [batch.references.count.b4](inputs/cases/batch.references.count.b4.json) | batch | Matcher::countMatches() | 308.602 | 0.62% | yes |
| [batch.references.count.b4](inputs/cases/batch.references.count.b4.json) | batch | strpos() loop | 1169.026 | 0.30% | yes |
| [batch.references.count.b4](inputs/cases/batch.references.count.b4.json) | batch | preg_match_all() [literal] | 1705.792 | 0.77% | yes |
| [batch.references.count.b4](inputs/cases/batch.references.count.b4.json) | batch | preg_match_all() [prefix] | 1742.115 | 0.24% | yes |
| [batch.references.count.b4](inputs/cases/batch.references.count.b4.json) | batch | Native A/A control | 308.851 | 0.88% | yes |
| [batch.references.all.b4](inputs/cases/batch.references.all.b4.json) | batch | Matcher::matchAll() | 316.252 | 0.59% | yes |
| [batch.references.all.b4](inputs/cases/batch.references.all.b4.json) | batch | strpos() loop | 1199.981 | 0.57% | yes |
| [batch.references.all.b4](inputs/cases/batch.references.all.b4.json) | batch | preg_match_all() [literal] | 1755.721 | 0.39% | yes |
| [batch.references.all.b4](inputs/cases/batch.references.all.b4.json) | batch | preg_match_all() [prefix] | 1798.026 | 0.53% | yes |
| [batch.references.all.b4](inputs/cases/batch.references.all.b4.json) | batch | Native A/A control | 316.351 | 0.72% | yes |
| [batch.rewrite.replace.b4](inputs/cases/batch.rewrite.replace.b4.json) | batch | Replacer::replace() | 275.989 | 0.87% | yes |
| [batch.rewrite.replace.b4](inputs/cases/batch.rewrite.replace.b4.json) | batch | strtr() | 2998.527 | 0.43% | yes |
| [batch.rewrite.replace.b4](inputs/cases/batch.rewrite.replace.b4.json) | batch | preg_replace_callback() [literal] | 697.119 | 1.35% | yes |
| [batch.rewrite.replace.b4](inputs/cases/batch.rewrite.replace.b4.json) | batch | preg_replace_callback() [prefix] | 549.788 | 0.81% | yes |
| [batch.rewrite.replace.b4](inputs/cases/batch.rewrite.replace.b4.json) | batch | str_replace() | 1280.331 | 0.32% | yes |
| [batch.rewrite.replace.b4](inputs/cases/batch.rewrite.replace.b4.json) | batch | Native A/A control | 277.103 | 1.08% | yes |
| [batch.references.unique.b16](inputs/cases/batch.references.unique.b16.json) | batch | Matcher::getMatchedKeywords() | 898.746 | 0.85% | no |
| [batch.references.unique.b16](inputs/cases/batch.references.unique.b16.json) | batch | strpos() loop | 3233.518 | 0.34% | no |
| [batch.references.unique.b16](inputs/cases/batch.references.unique.b16.json) | batch | preg_match_all() [literal] | 5372.671 | 1.46% | no |
| [batch.references.unique.b16](inputs/cases/batch.references.unique.b16.json) | batch | preg_match_all() [prefix] | 5514.946 | 1.03% | no |
| [batch.references.unique.b16](inputs/cases/batch.references.unique.b16.json) | batch | Native A/A control | 902.106 | 0.73% | no |
| [batch.references.count.b16](inputs/cases/batch.references.count.b16.json) | batch | Matcher::countMatches() | 897.036 | 0.64% | no |
| [batch.references.count.b16](inputs/cases/batch.references.count.b16.json) | batch | strpos() loop | 3456.451 | 0.50% | no |
| [batch.references.count.b16](inputs/cases/batch.references.count.b16.json) | batch | preg_match_all() [literal] | 5160.851 | 0.98% | no |
| [batch.references.count.b16](inputs/cases/batch.references.count.b16.json) | batch | preg_match_all() [prefix] | 5306.762 | 0.43% | no |
| [batch.references.count.b16](inputs/cases/batch.references.count.b16.json) | batch | Native A/A control | 895.891 | 1.09% | no |
| [batch.references.all.b16](inputs/cases/batch.references.all.b16.json) | batch | Matcher::matchAll() | 938.867 | 5.83% | no |
| [batch.references.all.b16](inputs/cases/batch.references.all.b16.json) | batch | strpos() loop | 3667.411 | 0.44% | no |
| [batch.references.all.b16](inputs/cases/batch.references.all.b16.json) | batch | preg_match_all() [literal] | 5497.537 | 0.79% | no |
| [batch.references.all.b16](inputs/cases/batch.references.all.b16.json) | batch | preg_match_all() [prefix] | 5628.988 | 0.74% | no |
| [batch.references.all.b16](inputs/cases/batch.references.all.b16.json) | batch | Native A/A control | 940.078 | 1.55% | no |
| [batch.rewrite.replace.b16](inputs/cases/batch.rewrite.replace.b16.json) | batch | Replacer::replace() | 866.177 | 0.32% | yes |
| [batch.rewrite.replace.b16](inputs/cases/batch.rewrite.replace.b16.json) | batch | strtr() | 9157.265 | 0.44% | yes |
| [batch.rewrite.replace.b16](inputs/cases/batch.rewrite.replace.b16.json) | batch | preg_replace_callback() [literal] | 2178.575 | 0.74% | yes |
| [batch.rewrite.replace.b16](inputs/cases/batch.rewrite.replace.b16.json) | batch | preg_replace_callback() [prefix] | 1770.753 | 0.32% | yes |
| [batch.rewrite.replace.b16](inputs/cases/batch.rewrite.replace.b16.json) | batch | Native A/A control | 865.574 | 0.43% | yes |
