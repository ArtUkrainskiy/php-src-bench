# Every implementation and A/A control

| Input | Implementation | Median, µs | Maximum deviation |
|---|---|---:|---:|
| comments.all.n8.b128.single | Matcher::matchAll() prepared | 0.490 | 4.05% |
| comments.all.n8.b128.single | prepared_aa | 0.489 | 4.11% |
| comments.all.n8.b128.single | strpos() loop | 0.710 | 3.86% |
| comments.all.n8.b128.single | preg_match_all() [literal] | 1.732 | 2.48% |
| comments.all.n8.b128.single | preg_match_all() [prefix] | 1.668 | 4.66% |
| comments.any.n16.b128.absent | Matcher::matches() prepared | 0.400 | 4.23% |
| comments.any.n16.b128.absent | prepared_aa | 0.398 | 2.72% |
| comments.any.n16.b128.absent | strpos() loop | 0.841 | 3.69% |
| comments.any.n16.b128.absent | preg_match() [literal] | 0.576 | 3.12% |
| comments.any.n16.b128.absent | preg_match() [prefix] | 0.522 | 2.44% |
| comments.any.n16.b128.absent | str_contains() loop | 0.650 | 2.82% |
| comments.count.n8.b128.single | Matcher::countMatches() prepared | 0.413 | 3.56% |
| comments.count.n8.b128.single | prepared_aa | 0.410 | 3.03% |
| comments.count.n8.b128.single | strpos() loop | 0.549 | 3.51% |
| comments.count.n8.b128.single | preg_match_all() [literal] | 0.991 | 2.23% |
| comments.count.n8.b128.single | preg_match_all() [prefix] | 0.954 | 3.55% |
| comments.count.n8.b128.single | substr_count()/strpos() loop | 0.456 | 3.43% |
| comments.replace.n16.b128.single | Replacer::replace() prepared | 0.447 | 4.01% |
| comments.replace.n16.b128.single | prepared_aa | 0.452 | 2.91% |
| comments.replace.n16.b128.single | strtr() | 1.247 | 3.46% |
| comments.replace.n16.b128.single | preg_replace_callback() [literal] | 0.689 | 3.61% |
| comments.replace.n16.b128.single | preg_replace_callback() [prefix] | 0.606 | 3.28% |
| comments.replace.n16.b128.single | str_replace() | 0.606 | 3.70% |
| comments.unique.n8.b128.single | Matcher::getMatchedKeywords() prepared | 0.441 | 4.79% |
| comments.unique.n8.b128.single | prepared_aa | 0.440 | 3.92% |
| comments.unique.n8.b128.single | strpos() loop | 0.721 | 3.88% |
| comments.unique.n8.b128.single | preg_match_all() [literal] | 1.845 | 2.45% |
| comments.unique.n8.b128.single | preg_match_all() [prefix] | 1.799 | 2.89% |
| technical.all.n16.b1024.single | Matcher::matchAll() prepared | 2.718 | 9.60% |
| technical.all.n16.b1024.single | prepared_aa | 2.665 | 5.15% |
| technical.all.n16.b1024.single | strpos() loop | 4.258 | 7.37% |
| technical.all.n16.b1024.single | preg_match_all() [literal] | 5.263 | 3.44% |
| technical.all.n16.b1024.single | preg_match_all() [prefix] | 4.910 | 4.75% |
| technical.all.n16.b128.single | Matcher::matchAll() prepared | 0.444 | 1.10% |
| technical.all.n16.b128.single | prepared_aa | 0.445 | 1.21% |
| technical.all.n16.b128.single | strpos() loop | 0.859 | 3.35% |
| technical.all.n16.b128.single | preg_match_all() [literal] | 2.043 | 0.63% |
| technical.all.n16.b128.single | preg_match_all() [prefix] | 1.991 | 1.44% |
| technical.all.n16.b256.single | Matcher::matchAll() prepared | 0.653 | 1.66% |
| technical.all.n16.b256.single | prepared_aa | 0.653 | 1.94% |
| technical.all.n16.b256.single | strpos() loop | 1.115 | 4.36% |
| technical.all.n16.b256.single | preg_match_all() [literal] | 2.724 | 3.48% |
| technical.all.n16.b256.single | preg_match_all() [prefix] | 2.600 | 3.72% |
| technical.all.n16.b4096.single | Matcher::matchAll() prepared | 12.979 | 4.33% |
| technical.all.n16.b4096.single | prepared_aa | 12.769 | 4.09% |
| technical.all.n16.b4096.single | strpos() loop | 14.141 | 2.69% |
| technical.all.n16.b4096.single | preg_match_all() [literal] | 13.525 | 8.11% |
| technical.all.n16.b4096.single | preg_match_all() [prefix] | 13.313 | 4.38% |
| technical.all.n32.b1024.single | Matcher::matchAll() prepared | 2.633 | 12.75% |
| technical.all.n32.b1024.single | prepared_aa | 2.466 | 16.08% |
| technical.all.n32.b1024.single | strpos() loop | 8.553 | 14.38% |
| technical.all.n32.b1024.single | preg_match_all() [literal] | 10.790 | 8.68% |
| technical.all.n32.b1024.single | preg_match_all() [prefix] | 10.562 | 10.20% |
| technical.all.n32.b128.single | Matcher::matchAll() prepared | 0.439 | 0.59% |
| technical.all.n32.b128.single | prepared_aa | 0.441 | 0.75% |
| technical.all.n32.b128.single | strpos() loop | 1.322 | 0.39% |
| technical.all.n32.b128.single | preg_match_all() [literal] | 2.790 | 9.23% |
| technical.all.n32.b128.single | preg_match_all() [prefix] | 2.824 | 1.09% |
| technical.all.n32.b256.single | Matcher::matchAll() prepared | 0.635 | 0.79% |
| technical.all.n32.b256.single | prepared_aa | 0.634 | 0.72% |
| technical.all.n32.b256.single | strpos() loop | 1.707 | 3.12% |
| technical.all.n32.b256.single | preg_match_all() [literal] | 4.029 | 3.11% |
| technical.all.n32.b256.single | preg_match_all() [prefix] | 4.021 | 4.89% |
| technical.all.n32.b4096.single | Matcher::matchAll() prepared | 11.407 | 2.86% |
| technical.all.n32.b4096.single | prepared_aa | 11.312 | 2.38% |
| technical.all.n32.b4096.single | strpos() loop | 27.558 | 1.82% |
| technical.all.n32.b4096.single | preg_match_all() [literal] | 43.248 | 5.00% |
| technical.all.n32.b4096.single | preg_match_all() [prefix] | 39.255 | 3.77% |
| technical.all.n48.b1024.single | Matcher::matchAll() prepared | 2.396 | 5.78% |
| technical.all.n48.b1024.single | prepared_aa | 2.345 | 5.06% |
| technical.all.n48.b1024.single | strpos() loop | 11.905 | 2.09% |
| technical.all.n48.b1024.single | preg_match_all() [literal] | 14.248 | 4.47% |
| technical.all.n48.b1024.single | preg_match_all() [prefix] | 14.851 | 1.55% |
| technical.all.n48.b128.single | Matcher::matchAll() prepared | 0.432 | 1.69% |
| technical.all.n48.b128.single | prepared_aa | 0.432 | 1.19% |
| technical.all.n48.b128.single | strpos() loop | 1.766 | 0.67% |
| technical.all.n48.b128.single | preg_match_all() [literal] | 3.712 | 0.62% |
| technical.all.n48.b128.single | preg_match_all() [prefix] | 3.699 | 0.89% |
| technical.all.n48.b256.single | Matcher::matchAll() prepared | 1.758 | 54.50% |
| technical.all.n48.b256.single | prepared_aa | 1.767 | 54.87% |
| technical.all.n48.b256.single | strpos() loop | 5.812 | 52.30% |
| technical.all.n48.b256.single | preg_match_all() [literal] | 14.092 | 54.42% |
| technical.all.n48.b256.single | preg_match_all() [prefix] | 14.564 | 54.48% |
| technical.all.n48.b4096.single | Matcher::matchAll() prepared | 11.400 | 4.12% |
| technical.all.n48.b4096.single | prepared_aa | 11.283 | 2.98% |
| technical.all.n48.b4096.single | strpos() loop | 42.553 | 2.27% |
| technical.all.n48.b4096.single | preg_match_all() [literal] | 52.897 | 7.28% |
| technical.all.n48.b4096.single | preg_match_all() [prefix] | 55.664 | 3.38% |
| technical.all.n8.b1024.single | Matcher::matchAll() prepared | 2.635 | 6.03% |
| technical.all.n8.b1024.single | prepared_aa | 2.578 | 6.57% |
| technical.all.n8.b1024.single | strpos() loop | 2.099 | 3.51% |
| technical.all.n8.b1024.single | preg_match_all() [literal] | 3.228 | 7.57% |
| technical.all.n8.b1024.single | preg_match_all() [prefix] | 2.871 | 3.22% |
| technical.all.n8.b128.single | Matcher::matchAll() prepared | 0.451 | 0.96% |
| technical.all.n8.b128.single | prepared_aa | 0.442 | 1.06% |
| technical.all.n8.b128.single | strpos() loop | 0.631 | 1.73% |
| technical.all.n8.b128.single | preg_match_all() [literal] | 1.473 | 1.20% |
| technical.all.n8.b128.single | preg_match_all() [prefix] | 1.439 | 0.44% |
| technical.all.n8.b256.single | Matcher::matchAll() prepared | 0.651 | 0.62% |
| technical.all.n8.b256.single | prepared_aa | 0.645 | 0.68% |
| technical.all.n8.b256.single | strpos() loop | 0.664 | 2.16% |
| technical.all.n8.b256.single | preg_match_all() [literal] | 1.701 | 2.66% |
| technical.all.n8.b256.single | preg_match_all() [prefix] | 1.616 | 0.74% |
| technical.all.n8.b4096.single | Matcher::matchAll() prepared | 14.039 | 2.49% |
| technical.all.n8.b4096.single | prepared_aa | 13.832 | 4.19% |
| technical.all.n8.b4096.single | strpos() loop | 6.368 | 1.83% |
| technical.all.n8.b4096.single | preg_match_all() [literal] | 7.346 | 7.28% |
| technical.all.n8.b4096.single | preg_match_all() [prefix] | 6.456 | 6.13% |
| technical.any.n16.b1024.absent | Matcher::matches() prepared | 2.617 | 4.39% |
| technical.any.n16.b1024.absent | prepared_aa | 2.581 | 11.01% |
| technical.any.n16.b1024.absent | strpos() loop | 3.954 | 1.29% |
| technical.any.n16.b1024.absent | preg_match() [literal] | 2.090 | 5.17% |
| technical.any.n16.b1024.absent | preg_match() [prefix] | 1.714 | 5.28% |
| technical.any.n16.b1024.absent | str_contains() loop | 3.798 | 1.27% |
| technical.any.n16.b128.absent | Matcher::matches() prepared | 0.363 | 1.22% |
| technical.any.n16.b128.absent | prepared_aa | 0.363 | 1.02% |
| technical.any.n16.b128.absent | strpos() loop | 0.705 | 0.90% |
| technical.any.n16.b128.absent | preg_match() [literal] | 0.503 | 3.24% |
| technical.any.n16.b128.absent | preg_match() [prefix] | 0.462 | 2.42% |
| technical.any.n16.b128.absent | str_contains() loop | 0.547 | 1.56% |
| technical.any.n16.b256.absent | Matcher::matches() prepared | 0.556 | 50.65% |
| technical.any.n16.b256.absent | prepared_aa | 0.561 | 42.05% |
| technical.any.n16.b256.absent | strpos() loop | 0.934 | 52.06% |
| technical.any.n16.b256.absent | preg_match() [literal] | 0.790 | 70.08% |
| technical.any.n16.b256.absent | preg_match() [prefix] | 0.654 | 75.65% |
| technical.any.n16.b256.absent | str_contains() loop | 0.751 | 60.55% |
| technical.any.n16.b4096.absent | Matcher::matches() prepared | 12.527 | 5.08% |
| technical.any.n16.b4096.absent | prepared_aa | 12.517 | 4.42% |
| technical.any.n16.b4096.absent | strpos() loop | 13.966 | 5.26% |
| technical.any.n16.b4096.absent | preg_match() [literal] | 7.829 | 8.32% |
| technical.any.n16.b4096.absent | preg_match() [prefix] | 6.171 | 5.91% |
| technical.any.n16.b4096.absent | str_contains() loop | 13.927 | 8.40% |
| technical.any.n32.b1024.absent | Matcher::matches() prepared | 2.415 | 6.74% |
| technical.any.n32.b1024.absent | prepared_aa | 2.368 | 7.59% |
| technical.any.n32.b1024.absent | strpos() loop | 7.705 | 2.80% |
| technical.any.n32.b1024.absent | preg_match() [literal] | 4.070 | 5.97% |
| technical.any.n32.b1024.absent | preg_match() [prefix] | 2.847 | 3.95% |
| technical.any.n32.b1024.absent | str_contains() loop | 7.472 | 1.78% |
| technical.any.n32.b128.absent | Matcher::matches() prepared | 0.375 | 0.76% |
| technical.any.n32.b128.absent | prepared_aa | 0.374 | 1.25% |
| technical.any.n32.b128.absent | strpos() loop | 1.164 | 0.51% |
| technical.any.n32.b128.absent | preg_match() [literal] | 0.754 | 1.27% |
| technical.any.n32.b128.absent | preg_match() [prefix] | 0.587 | 1.71% |
| technical.any.n32.b128.absent | str_contains() loop | 0.914 | 3.73% |
| technical.any.n32.b256.absent | Matcher::matches() prepared | 0.517 | 3.17% |
| technical.any.n32.b256.absent | prepared_aa | 0.519 | 4.38% |
| technical.any.n32.b256.absent | strpos() loop | 1.547 | 5.59% |
| technical.any.n32.b256.absent | preg_match() [literal] | 1.282 | 1.81% |
| technical.any.n32.b256.absent | preg_match() [prefix] | 0.926 | 3.02% |
| technical.any.n32.b256.absent | str_contains() loop | 1.317 | 3.87% |
| technical.any.n32.b4096.absent | Matcher::matches() prepared | 11.250 | 3.19% |
| technical.any.n32.b4096.absent | prepared_aa | 11.204 | 4.35% |
| technical.any.n32.b4096.absent | strpos() loop | 27.652 | 1.64% |
| technical.any.n32.b4096.absent | preg_match() [literal] | 16.802 | 6.61% |
| technical.any.n32.b4096.absent | preg_match() [prefix] | 9.780 | 4.93% |
| technical.any.n32.b4096.absent | str_contains() loop | 27.698 | 2.44% |
| technical.any.n48.b1024.absent | Matcher::matches() prepared | 2.367 | 7.91% |
| technical.any.n48.b1024.absent | prepared_aa | 2.282 | 6.18% |
| technical.any.n48.b1024.absent | strpos() loop | 11.858 | 2.53% |
| technical.any.n48.b1024.absent | preg_match() [literal] | 9.050 | 5.32% |
| technical.any.n48.b1024.absent | preg_match() [prefix] | 4.415 | 4.41% |
| technical.any.n48.b1024.absent | str_contains() loop | 11.434 | 3.70% |
| technical.any.n48.b128.absent | Matcher::matches() prepared | 0.352 | 0.90% |
| technical.any.n48.b128.absent | prepared_aa | 0.352 | 1.41% |
| technical.any.n48.b128.absent | strpos() loop | 1.599 | 1.13% |
| technical.any.n48.b128.absent | preg_match() [literal] | 1.132 | 1.74% |
| technical.any.n48.b128.absent | preg_match() [prefix] | 0.744 | 0.57% |
| technical.any.n48.b128.absent | str_contains() loop | 1.234 | 0.81% |
| technical.any.n48.b256.absent | Matcher::matches() prepared | 0.515 | 21.40% |
| technical.any.n48.b256.absent | prepared_aa | 0.514 | 2.81% |
| technical.any.n48.b256.absent | strpos() loop | 2.038 | 4.92% |
| technical.any.n48.b256.absent | preg_match() [literal] | 1.939 | 92.12% |
| technical.any.n48.b256.absent | preg_match() [prefix] | 1.185 | 36.74% |
| technical.any.n48.b256.absent | str_contains() loop | 1.692 | 20.15% |
| technical.any.n48.b4096.absent | Matcher::matches() prepared | 10.881 | 15.10% |
| technical.any.n48.b4096.absent | prepared_aa | 10.883 | 4.32% |
| technical.any.n48.b4096.absent | strpos() loop | 42.205 | 21.51% |
| technical.any.n48.b4096.absent | preg_match() [literal] | 34.042 | 15.49% |
| technical.any.n48.b4096.absent | preg_match() [prefix] | 15.445 | 11.53% |
| technical.any.n48.b4096.absent | str_contains() loop | 42.116 | 25.11% |
| technical.any.n8.b1024.absent | Matcher::matches() prepared | 2.946 | 25.28% |
| technical.any.n8.b1024.absent | prepared_aa | 3.005 | 9.96% |
| technical.any.n8.b1024.absent | strpos() loop | 1.964 | 21.03% |
| technical.any.n8.b1024.absent | preg_match() [literal] | 1.370 | 7.43% |
| technical.any.n8.b1024.absent | preg_match() [prefix] | 1.430 | 6.23% |
| technical.any.n8.b1024.absent | str_contains() loop | 1.803 | 27.51% |
| technical.any.n8.b128.absent | Matcher::matches() prepared | 0.364 | 1.06% |
| technical.any.n8.b128.absent | prepared_aa | 0.363 | 1.36% |
| technical.any.n8.b128.absent | strpos() loop | 0.471 | 1.45% |
| technical.any.n8.b128.absent | preg_match() [literal] | 0.402 | 0.83% |
| technical.any.n8.b128.absent | preg_match() [prefix] | 0.412 | 1.56% |
| technical.any.n8.b128.absent | str_contains() loop | 0.359 | 1.30% |
| technical.any.n8.b256.absent | Matcher::matches() prepared | 0.525 | 1.01% |
| technical.any.n8.b256.absent | prepared_aa | 0.521 | 0.63% |
| technical.any.n8.b256.absent | strpos() loop | 0.492 | 0.64% |
| technical.any.n8.b256.absent | preg_match() [literal] | 0.507 | 0.55% |
| technical.any.n8.b256.absent | preg_match() [prefix] | 0.512 | 0.78% |
| technical.any.n8.b256.absent | str_contains() loop | 0.379 | 1.44% |
| technical.any.n8.b4096.absent | Matcher::matches() prepared | 13.336 | 2.41% |
| technical.any.n8.b4096.absent | prepared_aa | 13.305 | 1.36% |
| technical.any.n8.b4096.absent | strpos() loop | 6.227 | 1.84% |
| technical.any.n8.b4096.absent | preg_match() [literal] | 4.181 | 4.67% |
| technical.any.n8.b4096.absent | preg_match() [prefix] | 4.246 | 4.38% |
| technical.any.n8.b4096.absent | str_contains() loop | 6.116 | 2.17% |
| technical.count.n16.b1024.single | Matcher::countMatches() prepared | 2.028 | 16.54% |
| technical.count.n16.b1024.single | prepared_aa | 2.056 | 12.75% |
| technical.count.n16.b1024.single | strpos() loop | 5.278 | 18.41% |
| technical.count.n16.b1024.single | preg_match_all() [literal] | 4.467 | 12.63% |
| technical.count.n16.b1024.single | preg_match_all() [prefix] | 4.135 | 9.74% |
| technical.count.n16.b1024.single | substr_count()/strpos() loop | 5.020 | 20.05% |
| technical.count.n16.b128.single | Matcher::countMatches() prepared | 0.369 | 0.53% |
| technical.count.n16.b128.single | prepared_aa | 0.367 | 0.73% |
| technical.count.n16.b128.single | strpos() loop | 0.736 | 1.18% |
| technical.count.n16.b128.single | preg_match_all() [literal] | 1.197 | 1.00% |
| technical.count.n16.b128.single | preg_match_all() [prefix] | 1.188 | 2.85% |
| technical.count.n16.b128.single | substr_count()/strpos() loop | 0.659 | 0.77% |
| technical.count.n16.b256.single | Matcher::countMatches() prepared | 0.597 | 8.76% |
| technical.count.n16.b256.single | prepared_aa | 0.576 | 12.69% |
| technical.count.n16.b256.single | strpos() loop | 1.015 | 8.28% |
| technical.count.n16.b256.single | preg_match_all() [literal] | 1.702 | 9.26% |
| technical.count.n16.b256.single | preg_match_all() [prefix] | 1.668 | 16.61% |
| technical.count.n16.b256.single | substr_count()/strpos() loop | 0.973 | 25.01% |
| technical.count.n16.b4096.single | Matcher::countMatches() prepared | 5.941 | 4.10% |
| technical.count.n16.b4096.single | prepared_aa | 5.920 | 8.06% |
| technical.count.n16.b4096.single | strpos() loop | 14.232 | 5.45% |
| technical.count.n16.b4096.single | preg_match_all() [literal] | 12.088 | 5.13% |
| technical.count.n16.b4096.single | preg_match_all() [prefix] | 11.953 | 6.35% |
| technical.count.n16.b4096.single | substr_count()/strpos() loop | 14.148 | 1.90% |
| technical.count.n32.b1024.single | Matcher::countMatches() prepared | 1.876 | 3.80% |
| technical.count.n32.b1024.single | prepared_aa | 1.866 | 4.59% |
| technical.count.n32.b1024.single | strpos() loop | 9.106 | 4.29% |
| technical.count.n32.b1024.single | preg_match_all() [literal] | 10.262 | 9.01% |
| technical.count.n32.b1024.single | preg_match_all() [prefix] | 9.854 | 2.62% |
| technical.count.n32.b1024.single | substr_count()/strpos() loop | 9.323 | 4.26% |
| technical.count.n32.b128.single | Matcher::countMatches() prepared | 0.368 | 1.67% |
| technical.count.n32.b128.single | prepared_aa | 0.368 | 0.88% |
| technical.count.n32.b128.single | strpos() loop | 1.196 | 1.07% |
| technical.count.n32.b128.single | preg_match_all() [literal] | 1.927 | 1.65% |
| technical.count.n32.b128.single | preg_match_all() [prefix] | 1.921 | 0.76% |
| technical.count.n32.b128.single | substr_count()/strpos() loop | 1.143 | 0.75% |
| technical.count.n32.b256.single | Matcher::countMatches() prepared | 0.547 | 1.42% |
| technical.count.n32.b256.single | prepared_aa | 0.545 | 1.17% |
| technical.count.n32.b256.single | strpos() loop | 1.553 | 3.42% |
| technical.count.n32.b256.single | preg_match_all() [literal] | 2.929 | 2.11% |
| technical.count.n32.b256.single | preg_match_all() [prefix] | 2.870 | 2.74% |
| technical.count.n32.b256.single | substr_count()/strpos() loop | 1.590 | 6.38% |
| technical.count.n32.b4096.single | Matcher::countMatches() prepared | 5.651 | 4.08% |
| technical.count.n32.b4096.single | prepared_aa | 5.650 | 3.98% |
| technical.count.n32.b4096.single | strpos() loop | 27.595 | 0.81% |
| technical.count.n32.b4096.single | preg_match_all() [literal] | 41.932 | 5.88% |
| technical.count.n32.b4096.single | preg_match_all() [prefix] | 36.613 | 4.21% |
| technical.count.n32.b4096.single | substr_count()/strpos() loop | 27.684 | 1.88% |
| technical.count.n48.b1024.single | Matcher::countMatches() prepared | 1.685 | 5.05% |
| technical.count.n48.b1024.single | prepared_aa | 1.699 | 5.98% |
| technical.count.n48.b1024.single | strpos() loop | 11.855 | 7.15% |
| technical.count.n48.b1024.single | preg_match_all() [literal] | 12.451 | 4.47% |
| technical.count.n48.b1024.single | preg_match_all() [prefix] | 13.388 | 2.93% |
| technical.count.n48.b1024.single | substr_count()/strpos() loop | 11.948 | 10.00% |
| technical.count.n48.b128.single | Matcher::countMatches() prepared | 0.370 | 2.58% |
| technical.count.n48.b128.single | prepared_aa | 0.368 | 21.70% |
| technical.count.n48.b128.single | strpos() loop | 1.651 | 5.28% |
| technical.count.n48.b128.single | preg_match_all() [literal] | 2.490 | 11.87% |
| technical.count.n48.b128.single | preg_match_all() [prefix] | 2.644 | 16.29% |
| technical.count.n48.b128.single | substr_count()/strpos() loop | 1.602 | 55.95% |
| technical.count.n48.b256.single | Matcher::countMatches() prepared | 0.710 | 6.22% |
| technical.count.n48.b256.single | prepared_aa | 0.705 | 5.80% |
| technical.count.n48.b256.single | strpos() loop | 2.689 | 5.33% |
| technical.count.n48.b256.single | preg_match_all() [literal] | 4.890 | 4.43% |
| technical.count.n48.b256.single | preg_match_all() [prefix] | 5.261 | 6.72% |
| technical.count.n48.b256.single | substr_count()/strpos() loop | 2.806 | 4.32% |
| technical.count.n48.b4096.single | Matcher::countMatches() prepared | 5.795 | 6.87% |
| technical.count.n48.b4096.single | prepared_aa | 5.803 | 5.12% |
| technical.count.n48.b4096.single | strpos() loop | 42.496 | 5.42% |
| technical.count.n48.b4096.single | preg_match_all() [literal] | 50.146 | 4.23% |
| technical.count.n48.b4096.single | preg_match_all() [prefix] | 54.236 | 4.97% |
| technical.count.n48.b4096.single | substr_count()/strpos() loop | 42.593 | 1.46% |
| technical.count.n8.b1024.single | Matcher::countMatches() prepared | 1.604 | 1.91% |
| technical.count.n8.b1024.single | prepared_aa | 1.608 | 3.01% |
| technical.count.n8.b1024.single | strpos() loop | 1.942 | 5.48% |
| technical.count.n8.b1024.single | preg_match_all() [literal] | 2.336 | 4.77% |
| technical.count.n8.b1024.single | preg_match_all() [prefix] | 2.053 | 3.79% |
| technical.count.n8.b1024.single | substr_count()/strpos() loop | 1.853 | 3.27% |
| technical.count.n8.b128.single | Matcher::countMatches() prepared | 0.380 | 1.38% |
| technical.count.n8.b128.single | prepared_aa | 0.381 | 1.20% |
| technical.count.n8.b128.single | strpos() loop | 0.497 | 0.66% |
| technical.count.n8.b128.single | preg_match_all() [literal] | 0.897 | 0.62% |
| technical.count.n8.b128.single | preg_match_all() [prefix] | 0.854 | 3.90% |
| technical.count.n8.b128.single | substr_count()/strpos() loop | 0.410 | 0.62% |
| technical.count.n8.b256.single | Matcher::countMatches() prepared | 0.542 | 0.71% |
| technical.count.n8.b256.single | prepared_aa | 0.543 | 0.73% |
| technical.count.n8.b256.single | strpos() loop | 0.526 | 0.63% |
| technical.count.n8.b256.single | preg_match_all() [literal] | 1.108 | 0.63% |
| technical.count.n8.b256.single | preg_match_all() [prefix] | 1.010 | 0.61% |
| technical.count.n8.b256.single | substr_count()/strpos() loop | 0.439 | 0.95% |
| technical.count.n8.b4096.single | Matcher::countMatches() prepared | 5.622 | 6.61% |
| technical.count.n8.b4096.single | prepared_aa | 5.674 | 6.48% |
| technical.count.n8.b4096.single | strpos() loop | 6.277 | 1.54% |
| technical.count.n8.b4096.single | preg_match_all() [literal] | 6.403 | 4.81% |
| technical.count.n8.b4096.single | preg_match_all() [prefix] | 5.487 | 5.78% |
| technical.count.n8.b4096.single | substr_count()/strpos() loop | 6.216 | 4.00% |
| technical.replace.n16.b1024.single | Replacer::replace() prepared | 1.732 | 4.87% |
| technical.replace.n16.b1024.single | prepared_aa | 1.767 | 3.99% |
| technical.replace.n16.b1024.single | strtr() | 9.285 | 3.82% |
| technical.replace.n16.b1024.single | preg_replace_callback() [literal] | 2.434 | 4.16% |
| technical.replace.n16.b1024.single | preg_replace_callback() [prefix] | 1.893 | 4.51% |
| technical.replace.n16.b1024.single | str_replace() | 3.733 | 2.32% |
| technical.replace.n16.b128.single | Replacer::replace() prepared | 0.398 | 1.11% |
| technical.replace.n16.b128.single | prepared_aa | 0.400 | 1.04% |
| technical.replace.n16.b128.single | strtr() | 1.020 | 1.95% |
| technical.replace.n16.b128.single | preg_replace_callback() [literal] | 0.623 | 2.14% |
| technical.replace.n16.b128.single | preg_replace_callback() [prefix] | 0.528 | 4.77% |
| technical.replace.n16.b128.single | str_replace() | 0.502 | 1.67% |
| technical.replace.n16.b256.single | Replacer::replace() prepared | 0.618 | 2.53% |
| technical.replace.n16.b256.single | prepared_aa | 0.616 | 1.90% |
| technical.replace.n16.b256.single | strtr() | 2.555 | 6.86% |
| technical.replace.n16.b256.single | preg_replace_callback() [literal] | 0.883 | 3.03% |
| technical.replace.n16.b256.single | preg_replace_callback() [prefix] | 0.735 | 4.04% |
| technical.replace.n16.b256.single | str_replace() | 0.727 | 3.53% |
| technical.replace.n16.b4096.single | Replacer::replace() prepared | 6.790 | 7.87% |
| technical.replace.n16.b4096.single | prepared_aa | 7.003 | 4.98% |
| technical.replace.n16.b4096.single | strtr() | 49.610 | 7.31% |
| technical.replace.n16.b4096.single | preg_replace_callback() [literal] | 8.776 | 6.19% |
| technical.replace.n16.b4096.single | preg_replace_callback() [prefix] | 6.224 | 6.09% |
| technical.replace.n16.b4096.single | str_replace() | 13.938 | 1.93% |
| technical.replace.n32.b1024.single | Replacer::replace() prepared | 1.841 | 7.26% |
| technical.replace.n32.b1024.single | prepared_aa | 1.864 | 4.25% |
| technical.replace.n32.b1024.single | strtr() | 15.864 | 8.41% |
| technical.replace.n32.b1024.single | preg_replace_callback() [literal] | 5.175 | 3.41% |
| technical.replace.n32.b1024.single | preg_replace_callback() [prefix] | 3.242 | 5.24% |
| technical.replace.n32.b1024.single | str_replace() | 7.540 | 3.88% |
| technical.replace.n32.b128.single | Replacer::replace() prepared | 0.398 | 0.61% |
| technical.replace.n32.b128.single | prepared_aa | 0.400 | 0.96% |
| technical.replace.n32.b128.single | strtr() | 1.473 | 2.28% |
| technical.replace.n32.b128.single | preg_replace_callback() [literal] | 0.808 | 0.83% |
| technical.replace.n32.b128.single | preg_replace_callback() [prefix] | 0.640 | 1.34% |
| technical.replace.n32.b128.single | str_replace() | 0.768 | 1.06% |
| technical.replace.n32.b256.single | Replacer::replace() prepared | 0.604 | 1.43% |
| technical.replace.n32.b256.single | prepared_aa | 0.608 | 0.84% |
| technical.replace.n32.b256.single | strtr() | 3.599 | 6.02% |
| technical.replace.n32.b256.single | preg_replace_callback() [literal] | 1.422 | 1.42% |
| technical.replace.n32.b256.single | preg_replace_callback() [prefix] | 1.001 | 2.94% |
| technical.replace.n32.b256.single | str_replace() | 1.159 | 2.87% |
| technical.replace.n32.b4096.single | Replacer::replace() prepared | 6.700 | 6.47% |
| technical.replace.n32.b4096.single | prepared_aa | 6.824 | 5.07% |
| technical.replace.n32.b4096.single | strtr() | 84.984 | 5.73% |
| technical.replace.n32.b4096.single | preg_replace_callback() [literal] | 18.279 | 4.34% |
| technical.replace.n32.b4096.single | preg_replace_callback() [prefix] | 9.425 | 6.69% |
| technical.replace.n32.b4096.single | str_replace() | 27.531 | 3.53% |
| technical.replace.n48.b1024.single | Replacer::replace() prepared | 1.714 | 4.29% |
| technical.replace.n48.b1024.single | prepared_aa | 1.768 | 2.53% |
| technical.replace.n48.b1024.single | strtr() | 28.616 | 11.00% |
| technical.replace.n48.b1024.single | preg_replace_callback() [literal] | 8.455 | 3.56% |
| technical.replace.n48.b1024.single | preg_replace_callback() [prefix] | 4.253 | 4.00% |
| technical.replace.n48.b1024.single | str_replace() | 10.833 | 1.81% |
| technical.replace.n48.b128.single | Replacer::replace() prepared | 0.400 | 1.06% |
| technical.replace.n48.b128.single | prepared_aa | 0.400 | 1.05% |
| technical.replace.n48.b128.single | strtr() | 2.163 | 3.43% |
| technical.replace.n48.b128.single | preg_replace_callback() [literal] | 1.079 | 0.39% |
| technical.replace.n48.b128.single | preg_replace_callback() [prefix] | 0.750 | 0.53% |
| technical.replace.n48.b128.single | str_replace() | 1.006 | 0.58% |
| technical.replace.n48.b256.single | Replacer::replace() prepared | 0.712 | 3.72% |
| technical.replace.n48.b256.single | prepared_aa | 0.713 | 3.52% |
| technical.replace.n48.b256.single | strtr() | 6.175 | 4.03% |
| technical.replace.n48.b256.single | preg_replace_callback() [literal] | 2.286 | 3.85% |
| technical.replace.n48.b256.single | preg_replace_callback() [prefix] | 1.425 | 4.33% |
| technical.replace.n48.b256.single | str_replace() | 1.778 | 4.25% |
| technical.replace.n48.b4096.single | Replacer::replace() prepared | 6.520 | 7.05% |
| technical.replace.n48.b4096.single | prepared_aa | 6.735 | 4.63% |
| technical.replace.n48.b4096.single | strtr() | 156.945 | 4.85% |
| technical.replace.n48.b4096.single | preg_replace_callback() [literal] | 35.259 | 2.36% |
| technical.replace.n48.b4096.single | preg_replace_callback() [prefix] | 14.857 | 5.01% |
| technical.replace.n48.b4096.single | str_replace() | 42.136 | 1.84% |
| technical.replace.n8.b1024.single | Replacer::replace() prepared | 1.655 | 2.46% |
| technical.replace.n8.b1024.single | prepared_aa | 1.678 | 3.69% |
| technical.replace.n8.b1024.single | strtr() | 2.181 | 4.03% |
| technical.replace.n8.b1024.single | preg_replace_callback() [literal] | 1.360 | 2.72% |
| technical.replace.n8.b1024.single | preg_replace_callback() [prefix] | 1.392 | 6.22% |
| technical.replace.n8.b1024.single | str_replace() | 1.813 | 2.20% |
| technical.replace.n8.b128.single | Replacer::replace() prepared | 0.396 | 2.88% |
| technical.replace.n8.b128.single | prepared_aa | 0.402 | 3.94% |
| technical.replace.n8.b128.single | strtr() | 0.546 | 9.35% |
| technical.replace.n8.b128.single | preg_replace_callback() [literal] | 0.475 | 1.77% |
| technical.replace.n8.b128.single | preg_replace_callback() [prefix] | 0.493 | 0.73% |
| technical.replace.n8.b128.single | str_replace() | 0.366 | 0.66% |
| technical.replace.n8.b256.single | Replacer::replace() prepared | 0.612 | 0.97% |
| technical.replace.n8.b256.single | prepared_aa | 0.611 | 1.27% |
| technical.replace.n8.b256.single | strtr() | 0.777 | 1.14% |
| technical.replace.n8.b256.single | preg_replace_callback() [literal] | 0.582 | 1.86% |
| technical.replace.n8.b256.single | preg_replace_callback() [prefix] | 0.588 | 2.82% |
| technical.replace.n8.b256.single | str_replace() | 0.396 | 1.33% |
| technical.replace.n8.b4096.single | Replacer::replace() prepared | 6.191 | 4.00% |
| technical.replace.n8.b4096.single | prepared_aa | 6.417 | 7.21% |
| technical.replace.n8.b4096.single | strtr() | 7.518 | 4.18% |
| technical.replace.n8.b4096.single | preg_replace_callback() [literal] | 4.486 | 3.00% |
| technical.replace.n8.b4096.single | preg_replace_callback() [prefix] | 4.467 | 5.10% |
| technical.replace.n8.b4096.single | str_replace() | 6.271 | 3.16% |
| technical.unique.n16.b1024.single | Matcher::getMatchedKeywords() prepared | 1.613 | 6.32% |
| technical.unique.n16.b1024.single | prepared_aa | 1.577 | 4.69% |
| technical.unique.n16.b1024.single | strpos() loop | 4.188 | 1.10% |
| technical.unique.n16.b1024.single | preg_match_all() [literal] | 4.918 | 5.47% |
| technical.unique.n16.b1024.single | preg_match_all() [prefix] | 4.660 | 3.07% |
| technical.unique.n16.b128.single | Matcher::getMatchedKeywords() prepared | 0.391 | 1.86% |
| technical.unique.n16.b128.single | prepared_aa | 0.389 | 0.97% |
| technical.unique.n16.b128.single | strpos() loop | 0.878 | 1.12% |
| technical.unique.n16.b128.single | preg_match_all() [literal] | 2.133 | 5.72% |
| technical.unique.n16.b128.single | preg_match_all() [prefix] | 2.115 | 1.66% |
| technical.unique.n16.b256.single | Matcher::getMatchedKeywords() prepared | 0.626 | 8.42% |
| technical.unique.n16.b256.single | prepared_aa | 0.623 | 10.44% |
| technical.unique.n16.b256.single | strpos() loop | 1.216 | 9.24% |
| technical.unique.n16.b256.single | preg_match_all() [literal] | 3.006 | 17.31% |
| technical.unique.n16.b256.single | preg_match_all() [prefix] | 2.925 | 11.64% |
| technical.unique.n16.b4096.single | Matcher::getMatchedKeywords() prepared | 11.310 | 2.70% |
| technical.unique.n16.b4096.single | prepared_aa | 10.990 | 7.63% |
| technical.unique.n16.b4096.single | strpos() loop | 14.267 | 5.28% |
| technical.unique.n16.b4096.single | preg_match_all() [literal] | 13.475 | 5.20% |
| technical.unique.n16.b4096.single | preg_match_all() [prefix] | 13.526 | 2.31% |
| technical.unique.n32.b1024.single | Matcher::getMatchedKeywords() prepared | 2.039 | 9.55% |
| technical.unique.n32.b1024.single | prepared_aa | 2.003 | 6.93% |
| technical.unique.n32.b1024.single | strpos() loop | 8.516 | 9.94% |
| technical.unique.n32.b1024.single | preg_match_all() [literal] | 11.085 | 6.62% |
| technical.unique.n32.b1024.single | preg_match_all() [prefix] | 10.970 | 7.31% |
| technical.unique.n32.b128.single | Matcher::getMatchedKeywords() prepared | 0.390 | 8.57% |
| technical.unique.n32.b128.single | prepared_aa | 0.388 | 7.60% |
| technical.unique.n32.b128.single | strpos() loop | 1.348 | 5.93% |
| technical.unique.n32.b128.single | preg_match_all() [literal] | 2.884 | 9.23% |
| technical.unique.n32.b128.single | preg_match_all() [prefix] | 2.930 | 14.17% |
| technical.unique.n32.b256.single | Matcher::getMatchedKeywords() prepared | 0.555 | 4.38% |
| technical.unique.n32.b256.single | prepared_aa | 0.555 | 2.86% |
| technical.unique.n32.b256.single | strpos() loop | 1.765 | 3.33% |
| technical.unique.n32.b256.single | preg_match_all() [literal] | 4.177 | 2.74% |
| technical.unique.n32.b256.single | preg_match_all() [prefix] | 4.166 | 3.47% |
| technical.unique.n32.b4096.single | Matcher::getMatchedKeywords() prepared | 10.501 | 3.35% |
| technical.unique.n32.b4096.single | prepared_aa | 10.351 | 4.75% |
| technical.unique.n32.b4096.single | strpos() loop | 27.750 | 3.84% |
| technical.unique.n32.b4096.single | preg_match_all() [literal] | 42.235 | 5.62% |
| technical.unique.n32.b4096.single | preg_match_all() [prefix] | 39.111 | 2.17% |
| technical.unique.n48.b1024.single | Matcher::getMatchedKeywords() prepared | 1.861 | 7.00% |
| technical.unique.n48.b1024.single | prepared_aa | 1.817 | 4.46% |
| technical.unique.n48.b1024.single | strpos() loop | 12.009 | 3.36% |
| technical.unique.n48.b1024.single | preg_match_all() [literal] | 14.236 | 7.44% |
| technical.unique.n48.b1024.single | preg_match_all() [prefix] | 15.024 | 3.91% |
| technical.unique.n48.b128.single | Matcher::getMatchedKeywords() prepared | 0.378 | 1.22% |
| technical.unique.n48.b128.single | prepared_aa | 0.379 | 1.07% |
| technical.unique.n48.b128.single | strpos() loop | 1.786 | 1.25% |
| technical.unique.n48.b128.single | preg_match_all() [literal] | 3.802 | 1.20% |
| technical.unique.n48.b128.single | preg_match_all() [prefix] | 3.808 | 0.66% |
| technical.unique.n48.b256.single | Matcher::getMatchedKeywords() prepared | 0.783 | 3.77% |
| technical.unique.n48.b256.single | prepared_aa | 0.780 | 5.45% |
| technical.unique.n48.b256.single | strpos() loop | 3.207 | 8.95% |
| technical.unique.n48.b256.single | preg_match_all() [literal] | 7.500 | 3.92% |
| technical.unique.n48.b256.single | preg_match_all() [prefix] | 7.553 | 5.74% |
| technical.unique.n48.b4096.single | Matcher::getMatchedKeywords() prepared | 10.234 | 4.47% |
| technical.unique.n48.b4096.single | prepared_aa | 9.995 | 14.18% |
| technical.unique.n48.b4096.single | strpos() loop | 42.680 | 1.75% |
| technical.unique.n48.b4096.single | preg_match_all() [literal] | 51.694 | 6.43% |
| technical.unique.n48.b4096.single | preg_match_all() [prefix] | 55.360 | 4.19% |
| technical.unique.n8.b1024.single | Matcher::getMatchedKeywords() prepared | 1.611 | 1.90% |
| technical.unique.n8.b1024.single | prepared_aa | 1.600 | 2.82% |
| technical.unique.n8.b1024.single | strpos() loop | 2.089 | 3.13% |
| technical.unique.n8.b1024.single | preg_match_all() [literal] | 3.242 | 3.32% |
| technical.unique.n8.b1024.single | preg_match_all() [prefix] | 2.934 | 4.65% |
| technical.unique.n8.b128.single | Matcher::getMatchedKeywords() prepared | 0.385 | 3.54% |
| technical.unique.n8.b128.single | prepared_aa | 0.388 | 1.05% |
| technical.unique.n8.b128.single | strpos() loop | 0.627 | 2.19% |
| technical.unique.n8.b128.single | preg_match_all() [literal] | 1.564 | 3.04% |
| technical.unique.n8.b128.single | preg_match_all() [prefix] | 1.536 | 1.86% |
| technical.unique.n8.b256.single | Matcher::getMatchedKeywords() prepared | 0.542 | 1.59% |
| technical.unique.n8.b256.single | prepared_aa | 0.540 | 0.88% |
| technical.unique.n8.b256.single | strpos() loop | 0.661 | 1.75% |
| technical.unique.n8.b256.single | preg_match_all() [literal] | 1.797 | 0.63% |
| technical.unique.n8.b256.single | preg_match_all() [prefix] | 1.726 | 0.93% |
| technical.unique.n8.b4096.single | Matcher::getMatchedKeywords() prepared | 11.965 | 6.94% |
| technical.unique.n8.b4096.single | prepared_aa | 11.670 | 4.07% |
| technical.unique.n8.b4096.single | strpos() loop | 6.412 | 1.46% |
| technical.unique.n8.b4096.single | preg_match_all() [literal] | 7.444 | 6.46% |
| technical.unique.n8.b4096.single | preg_match_all() [prefix] | 6.486 | 4.98% |
