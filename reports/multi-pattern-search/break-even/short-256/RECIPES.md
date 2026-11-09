# Timings: every implementation and A/A control

| Input | Implementation | Median, µs | Maximum deviation |
|---|---|---:|---:|
| comments.all.n8.b256.single | Matcher::matchAll() prepared | 0.629 | 0.76% |
| comments.all.n8.b256.single | prepared_aa | 0.629 | 0.70% |
| comments.all.n8.b256.single | Matcher::matchAll() oneshot | 4.498 | 2.73% |
| comments.all.n8.b256.single | oneshot_aa | 4.473 | 3.06% |
| comments.all.n8.b256.single | strpos() loop | 0.605 | 0.53% |
| comments.all.n8.b256.single | preg_match_all() [literal] | 1.589 | 0.97% |
| comments.all.n8.b256.single | preg_match_all() [prefix] | 1.505 | 1.75% |
| comments.any.n16.b256.absent | Matcher::matches() prepared | 0.512 | 4.53% |
| comments.any.n16.b256.absent | prepared_aa | 0.515 | 3.18% |
| comments.any.n16.b256.absent | Matcher::matches() oneshot | 10.831 | 0.61% |
| comments.any.n16.b256.absent | oneshot_aa | 10.855 | 0.60% |
| comments.any.n16.b256.absent | strpos() loop | 0.942 | 1.49% |
| comments.any.n16.b256.absent | preg_match() [literal] | 0.665 | 0.55% |
| comments.any.n16.b256.absent | preg_match() [prefix] | 0.588 | 0.54% |
| comments.any.n16.b256.absent | str_contains() loop | 0.790 | 2.03% |
| comments.count.n16.b256.single | Matcher::countMatches() prepared | 0.542 | 0.50% |
| comments.count.n16.b256.single | prepared_aa | 0.542 | 1.05% |
| comments.count.n16.b256.single | Matcher::countMatches() oneshot | 10.855 | 0.37% |
| comments.count.n16.b256.single | oneshot_aa | 10.862 | 0.36% |
| comments.count.n16.b256.single | strpos() loop | 0.972 | 1.75% |
| comments.count.n16.b256.single | preg_match_all() [literal] | 1.488 | 0.56% |
| comments.count.n16.b256.single | preg_match_all() [prefix] | 1.415 | 1.08% |
| comments.count.n16.b256.single | substr_count()/strpos() loop | 0.938 | 0.90% |
| comments.replace.n16.b256.single | Replacer::replace() prepared | 0.602 | 0.86% |
| comments.replace.n16.b256.single | prepared_aa | 0.600 | 1.09% |
| comments.replace.n16.b256.single | Replacer::replace() oneshot | 4.920 | 1.76% |
| comments.replace.n16.b256.single | oneshot_aa | 4.920 | 1.81% |
| comments.replace.n16.b256.single | strtr() | 1.946 | 3.37% |
| comments.replace.n16.b256.single | preg_replace_callback() [literal] | 0.770 | 1.33% |
| comments.replace.n16.b256.single | preg_replace_callback() [prefix] | 0.654 | 0.56% |
| comments.replace.n16.b256.single | str_replace() | 0.712 | 0.61% |
| comments.unique.n8.b256.single | Matcher::getMatchedKeywords() prepared | 0.536 | 2.26% |
| comments.unique.n8.b256.single | prepared_aa | 0.536 | 2.30% |
| comments.unique.n8.b256.single | Matcher::getMatchedKeywords() oneshot | 4.459 | 0.65% |
| comments.unique.n8.b256.single | oneshot_aa | 4.463 | 0.38% |
| comments.unique.n8.b256.single | strpos() loop | 0.605 | 1.04% |
| comments.unique.n8.b256.single | preg_match_all() [literal] | 1.672 | 0.29% |
| comments.unique.n8.b256.single | preg_match_all() [prefix] | 1.592 | 0.39% |
| technical.all.n1.b256.single | Matcher::matchAll() prepared | 0.608 | 0.74% |
| technical.all.n1.b256.single | prepared_aa | 0.608 | 0.63% |
| technical.all.n1.b256.single | Matcher::matchAll() oneshot | 1.084 | 0.78% |
| technical.all.n1.b256.single | oneshot_aa | 1.085 | 1.15% |
| technical.all.n1.b256.single | strpos() loop | 0.437 | 0.78% |
| technical.all.n1.b256.single | preg_match_all() [literal] | 0.720 | 1.59% |
| technical.all.n1.b256.single | preg_match_all() [prefix] | 0.721 | 1.56% |
| technical.all.n16.b256.single | Matcher::matchAll() prepared | 0.645 | 0.78% |
| technical.all.n16.b256.single | prepared_aa | 0.646 | 0.52% |
| technical.all.n16.b256.single | Matcher::matchAll() oneshot | 11.138 | 0.60% |
| technical.all.n16.b256.single | oneshot_aa | 11.140 | 0.27% |
| technical.all.n16.b256.single | strpos() loop | 1.048 | 0.73% |
| technical.all.n16.b256.single | preg_match_all() [literal] | 2.454 | 2.31% |
| technical.all.n16.b256.single | preg_match_all() [prefix] | 2.332 | 0.85% |
| technical.all.n4.b256.single | Matcher::matchAll() prepared | 0.665 | 1.39% |
| technical.all.n4.b256.single | prepared_aa | 0.663 | 0.82% |
| technical.all.n4.b256.single | Matcher::matchAll() oneshot | 2.607 | 2.55% |
| technical.all.n4.b256.single | oneshot_aa | 2.604 | 2.78% |
| technical.all.n4.b256.single | strpos() loop | 0.537 | 0.62% |
| technical.all.n4.b256.single | preg_match_all() [literal] | 1.151 | 1.74% |
| technical.all.n4.b256.single | preg_match_all() [prefix] | 1.153 | 0.56% |
| technical.all.n48.b256.single | Matcher::matchAll() prepared | 0.634 | 1.73% |
| technical.all.n48.b256.single | prepared_aa | 0.632 | 0.68% |
| technical.all.n48.b256.single | Matcher::matchAll() oneshot | 29.828 | 0.93% |
| technical.all.n48.b256.single | oneshot_aa | 29.736 | 1.13% |
| technical.all.n48.b256.single | strpos() loop | 2.190 | 1.06% |
| technical.all.n48.b256.single | preg_match_all() [literal] | 5.002 | 0.38% |
| technical.all.n48.b256.single | preg_match_all() [prefix] | 5.042 | 0.74% |
| technical.all.n8.b256.single | Matcher::matchAll() prepared | 0.644 | 0.80% |
| technical.all.n8.b256.single | prepared_aa | 0.645 | 0.58% |
| technical.all.n8.b256.single | Matcher::matchAll() oneshot | 4.518 | 1.12% |
| technical.all.n8.b256.single | oneshot_aa | 4.519 | 1.13% |
| technical.all.n8.b256.single | strpos() loop | 0.660 | 0.89% |
| technical.all.n8.b256.single | preg_match_all() [literal] | 1.694 | 0.77% |
| technical.all.n8.b256.single | preg_match_all() [prefix] | 1.623 | 0.88% |
| technical.any.n1.b256.absent | Matcher::matches() prepared | 0.488 | 0.54% |
| technical.any.n1.b256.absent | prepared_aa | 0.488 | 0.60% |
| technical.any.n1.b256.absent | Matcher::matches() oneshot | 0.962 | 0.56% |
| technical.any.n1.b256.absent | oneshot_aa | 0.962 | 0.60% |
| technical.any.n1.b256.absent | strpos() loop | 0.275 | 1.08% |
| technical.any.n1.b256.absent | preg_match() [literal] | 0.295 | 0.83% |
| technical.any.n1.b256.absent | preg_match() [prefix] | 0.295 | 0.99% |
| technical.any.n1.b256.absent | str_contains() loop | 0.209 | 1.56% |
| technical.any.n1.b256.absent | str_contains() | 0.190 | 1.37% |
| technical.any.n16.b256.absent | Matcher::matches() prepared | 0.529 | 0.86% |
| technical.any.n16.b256.absent | prepared_aa | 0.530 | 1.26% |
| technical.any.n16.b256.absent | Matcher::matches() oneshot | 10.890 | 0.88% |
| technical.any.n16.b256.absent | oneshot_aa | 10.891 | 0.71% |
| technical.any.n16.b256.absent | strpos() loop | 0.873 | 0.93% |
| technical.any.n16.b256.absent | preg_match() [literal] | 0.747 | 0.58% |
| technical.any.n16.b256.absent | preg_match() [prefix] | 0.629 | 0.65% |
| technical.any.n16.b256.absent | str_contains() loop | 0.721 | 1.08% |
| technical.any.n4.b256.absent | Matcher::matches() prepared | 0.539 | 1.20% |
| technical.any.n4.b256.absent | prepared_aa | 0.540 | 1.01% |
| technical.any.n4.b256.absent | Matcher::matches() oneshot | 2.440 | 3.69% |
| technical.any.n4.b256.absent | oneshot_aa | 2.444 | 3.45% |
| technical.any.n4.b256.absent | strpos() loop | 0.374 | 0.72% |
| technical.any.n4.b256.absent | preg_match() [literal] | 0.404 | 0.66% |
| technical.any.n4.b256.absent | preg_match() [prefix] | 0.397 | 0.79% |
| technical.any.n4.b256.absent | str_contains() loop | 0.290 | 1.65% |
| technical.any.n48.b256.absent | Matcher::matches() prepared | 0.513 | 0.47% |
| technical.any.n48.b256.absent | prepared_aa | 0.515 | 0.75% |
| technical.any.n48.b256.absent | Matcher::matches() oneshot | 29.311 | 0.93% |
| technical.any.n48.b256.absent | oneshot_aa | 29.292 | 0.71% |
| technical.any.n48.b256.absent | strpos() loop | 2.011 | 0.50% |
| technical.any.n48.b256.absent | preg_match() [literal] | 1.940 | 0.53% |
| technical.any.n48.b256.absent | preg_match() [prefix] | 1.181 | 0.80% |
| technical.any.n48.b256.absent | str_contains() loop | 1.677 | 1.17% |
| technical.any.n48.b256.early | Matcher::matches() prepared | 0.222 | 2.38% |
| technical.any.n48.b256.early | prepared_aa | 0.221 | 0.81% |
| technical.any.n48.b256.early | Matcher::matches() oneshot | 29.623 | 2.21% |
| technical.any.n48.b256.early | oneshot_aa | 29.592 | 0.67% |
| technical.any.n48.b256.early | strpos() loop | 1.208 | 0.75% |
| technical.any.n48.b256.early | preg_match() [literal] | 0.339 | 1.18% |
| technical.any.n48.b256.early | preg_match() [prefix] | 0.335 | 1.38% |
| technical.any.n48.b256.early | str_contains() loop | 1.032 | 1.55% |
| technical.any.n48.b256.late | Matcher::matches() prepared | 0.503 | 2.45% |
| technical.any.n48.b256.late | prepared_aa | 0.503 | 0.60% |
| technical.any.n48.b256.late | Matcher::matches() oneshot | 29.139 | 0.83% |
| technical.any.n48.b256.late | oneshot_aa | 29.214 | 0.83% |
| technical.any.n48.b256.late | strpos() loop | 1.183 | 4.32% |
| technical.any.n48.b256.late | preg_match() [literal] | 1.940 | 1.17% |
| technical.any.n48.b256.late | preg_match() [prefix] | 1.127 | 0.62% |
| technical.any.n48.b256.late | str_contains() loop | 1.002 | 2.30% |
| technical.any.n48.b256.middle | Matcher::matches() prepared | 0.359 | 1.08% |
| technical.any.n48.b256.middle | prepared_aa | 0.358 | 1.02% |
| technical.any.n48.b256.middle | Matcher::matches() oneshot | 28.831 | 2.76% |
| technical.any.n48.b256.middle | oneshot_aa | 28.793 | 2.03% |
| technical.any.n48.b256.middle | strpos() loop | 1.184 | 2.82% |
| technical.any.n48.b256.middle | preg_match() [literal] | 1.129 | 0.49% |
| technical.any.n48.b256.middle | preg_match() [prefix] | 0.735 | 1.19% |
| technical.any.n48.b256.middle | str_contains() loop | 0.999 | 2.10% |
| technical.any.n8.b256.absent | Matcher::matches() prepared | 0.521 | 0.61% |
| technical.any.n8.b256.absent | prepared_aa | 0.522 | 0.67% |
| technical.any.n8.b256.absent | Matcher::matches() oneshot | 4.376 | 1.90% |
| technical.any.n8.b256.absent | oneshot_aa | 4.371 | 0.55% |
| technical.any.n8.b256.absent | strpos() loop | 0.491 | 0.82% |
| technical.any.n8.b256.absent | preg_match() [literal] | 0.506 | 0.77% |
| technical.any.n8.b256.absent | preg_match() [prefix] | 0.514 | 0.83% |
| technical.any.n8.b256.absent | str_contains() loop | 0.377 | 0.71% |
| technical.count.n1.b256.single | Matcher::countMatches() prepared | 0.465 | 0.87% |
| technical.count.n1.b256.single | prepared_aa | 0.467 | 0.68% |
| technical.count.n1.b256.single | Matcher::countMatches() oneshot | 0.929 | 0.91% |
| technical.count.n1.b256.single | oneshot_aa | 0.927 | 1.93% |
| technical.count.n1.b256.single | strpos() loop | 0.307 | 0.63% |
| technical.count.n1.b256.single | preg_match_all() [literal] | 0.417 | 1.14% |
| technical.count.n1.b256.single | preg_match_all() [prefix] | 0.418 | 0.97% |
| technical.count.n1.b256.single | substr_count()/strpos() loop | 0.203 | 1.21% |
| technical.count.n1.b256.single | substr_count() | 0.185 | 1.09% |
| technical.count.n16.b256.single | Matcher::countMatches() prepared | 0.544 | 0.59% |
| technical.count.n16.b256.single | prepared_aa | 0.544 | 0.71% |
| technical.count.n16.b256.single | Matcher::countMatches() oneshot | 10.907 | 0.53% |
| technical.count.n16.b256.single | oneshot_aa | 10.892 | 0.59% |
| technical.count.n16.b256.single | strpos() loop | 0.924 | 0.60% |
| technical.count.n16.b256.single | preg_match_all() [literal] | 1.552 | 0.75% |
| technical.count.n16.b256.single | preg_match_all() [prefix] | 1.506 | 0.83% |
| technical.count.n16.b256.single | substr_count()/strpos() loop | 0.873 | 0.56% |
| technical.count.n4.b256.single | Matcher::countMatches() prepared | 0.523 | 1.09% |
| technical.count.n4.b256.single | prepared_aa | 0.524 | 1.41% |
| technical.count.n4.b256.single | Matcher::countMatches() oneshot | 2.334 | 1.47% |
| technical.count.n4.b256.single | oneshot_aa | 2.340 | 1.32% |
| technical.count.n4.b256.single | strpos() loop | 0.402 | 0.79% |
| technical.count.n4.b256.single | preg_match_all() [literal] | 0.667 | 0.81% |
| technical.count.n4.b256.single | preg_match_all() [prefix] | 0.666 | 0.56% |
| technical.count.n4.b256.single | substr_count()/strpos() loop | 0.306 | 0.65% |
| technical.count.n48.b256.single | Matcher::countMatches() prepared | 0.542 | 0.81% |
| technical.count.n48.b256.single | prepared_aa | 0.542 | 0.29% |
| technical.count.n48.b256.single | Matcher::countMatches() oneshot | 29.404 | 1.36% |
| technical.count.n48.b256.single | oneshot_aa | 29.359 | 1.09% |
| technical.count.n48.b256.single | strpos() loop | 2.069 | 1.35% |
| technical.count.n48.b256.single | preg_match_all() [literal] | 3.749 | 1.39% |
| technical.count.n48.b256.single | preg_match_all() [prefix] | 3.959 | 0.64% |
| technical.count.n48.b256.single | substr_count()/strpos() loop | 2.124 | 0.61% |
| technical.count.n48.b4096.single | Matcher::countMatches() prepared | 5.529 | 4.57% |
| technical.count.n48.b4096.single | prepared_aa | 5.549 | 2.48% |
| technical.count.n48.b4096.single | Matcher::countMatches() oneshot | 37.124 | 1.06% |
| technical.count.n48.b4096.single | oneshot_aa | 37.070 | 1.25% |
| technical.count.n48.b4096.single | strpos() loop | 41.962 | 0.29% |
| technical.count.n48.b4096.single | preg_match_all() [literal] | 45.532 | 1.63% |
| technical.count.n48.b4096.single | preg_match_all() [prefix] | 48.820 | 1.10% |
| technical.count.n48.b4096.single | substr_count()/strpos() loop | 42.059 | 0.26% |
| technical.count.n8.b256.single | Matcher::countMatches() prepared | 0.542 | 0.62% |
| technical.count.n8.b256.single | prepared_aa | 0.540 | 0.82% |
| technical.count.n8.b256.single | Matcher::countMatches() oneshot | 4.451 | 0.81% |
| technical.count.n8.b256.single | oneshot_aa | 4.463 | 0.88% |
| technical.count.n8.b256.single | strpos() loop | 0.525 | 0.64% |
| technical.count.n8.b256.single | preg_match_all() [literal] | 1.129 | 0.88% |
| technical.count.n8.b256.single | preg_match_all() [prefix] | 1.011 | 0.56% |
| technical.count.n8.b256.single | substr_count()/strpos() loop | 0.436 | 1.46% |
| technical.replace.n1.b256.single | Replacer::replace() prepared | 0.521 | 0.99% |
| technical.replace.n1.b256.single | prepared_aa | 0.521 | 0.87% |
| technical.replace.n1.b256.single | Replacer::replace() oneshot | 0.991 | 4.68% |
| technical.replace.n1.b256.single | oneshot_aa | 0.991 | 3.44% |
| technical.replace.n1.b256.single | strtr() | 0.243 | 2.20% |
| technical.replace.n1.b256.single | preg_replace_callback() [literal] | 0.384 | 0.50% |
| technical.replace.n1.b256.single | preg_replace_callback() [prefix] | 0.384 | 0.67% |
| technical.replace.n1.b256.single | str_replace() | 0.262 | 1.70% |
| technical.replace.n16.b256.single | Replacer::replace() prepared | 0.609 | 0.92% |
| technical.replace.n16.b256.single | prepared_aa | 0.609 | 1.08% |
| technical.replace.n16.b256.single | Replacer::replace() oneshot | 4.914 | 1.85% |
| technical.replace.n16.b256.single | oneshot_aa | 4.902 | 1.40% |
| technical.replace.n16.b256.single | strtr() | 2.331 | 4.27% |
| technical.replace.n16.b256.single | preg_replace_callback() [literal] | 0.854 | 0.59% |
| technical.replace.n16.b256.single | preg_replace_callback() [prefix] | 0.693 | 0.58% |
| technical.replace.n16.b256.single | str_replace() | 0.696 | 1.04% |
| technical.replace.n4.b256.single | Replacer::replace() prepared | 0.576 | 0.56% |
| technical.replace.n4.b256.single | prepared_aa | 0.576 | 0.99% |
| technical.replace.n4.b256.single | Replacer::replace() oneshot | 1.791 | 0.53% |
| technical.replace.n4.b256.single | oneshot_aa | 1.793 | 0.55% |
| technical.replace.n4.b256.single | strtr() | 0.607 | 1.04% |
| technical.replace.n4.b256.single | preg_replace_callback() [literal] | 0.468 | 1.17% |
| technical.replace.n4.b256.single | preg_replace_callback() [prefix] | 0.465 | 1.13% |
| technical.replace.n4.b256.single | str_replace() | 0.321 | 1.22% |
| technical.replace.n48.b256.single | Replacer::replace() prepared | 0.621 | 1.31% |
| technical.replace.n48.b256.single | prepared_aa | 0.612 | 0.69% |
| technical.replace.n48.b256.single | Replacer::replace() oneshot | 19.276 | 0.84% |
| technical.replace.n48.b256.single | oneshot_aa | 19.270 | 0.63% |
| technical.replace.n48.b256.single | strtr() | 5.028 | 1.66% |
| technical.replace.n48.b256.single | preg_replace_callback() [literal] | 1.974 | 0.97% |
| technical.replace.n48.b256.single | preg_replace_callback() [prefix] | 1.201 | 0.55% |
| technical.replace.n48.b256.single | str_replace() | 1.473 | 0.62% |
| technical.replace.n8.b256.single | Replacer::replace() prepared | 0.605 | 1.05% |
| technical.replace.n8.b256.single | prepared_aa | 0.605 | 1.45% |
| technical.replace.n8.b256.single | Replacer::replace() oneshot | 3.516 | 2.09% |
| technical.replace.n8.b256.single | oneshot_aa | 3.555 | 3.63% |
| technical.replace.n8.b256.single | strtr() | 0.772 | 1.10% |
| technical.replace.n8.b256.single | preg_replace_callback() [literal] | 0.578 | 0.75% |
| technical.replace.n8.b256.single | preg_replace_callback() [prefix] | 0.588 | 0.72% |
| technical.replace.n8.b256.single | str_replace() | 0.394 | 1.28% |
| technical.unique.n1.b256.single | Matcher::getMatchedKeywords() prepared | 0.346 | 0.96% |
| technical.unique.n1.b256.single | prepared_aa | 0.349 | 1.03% |
| technical.unique.n1.b256.single | Matcher::getMatchedKeywords() oneshot | 0.842 | 0.95% |
| technical.unique.n1.b256.single | oneshot_aa | 0.840 | 0.52% |
| technical.unique.n1.b256.single | strpos() loop | 0.427 | 0.88% |
| technical.unique.n1.b256.single | preg_match_all() [literal] | 0.817 | 0.73% |
| technical.unique.n1.b256.single | preg_match_all() [prefix] | 0.818 | 0.50% |
| technical.unique.n1.b256.single | strpos() + result list | 0.196 | 1.19% |
| technical.unique.n16.b256.single | Matcher::getMatchedKeywords() prepared | 0.547 | 0.81% |
| technical.unique.n16.b256.single | prepared_aa | 0.548 | 1.04% |
| technical.unique.n16.b256.single | Matcher::getMatchedKeywords() oneshot | 11.010 | 0.43% |
| technical.unique.n16.b256.single | oneshot_aa | 10.991 | 0.56% |
| technical.unique.n16.b256.single | strpos() loop | 1.062 | 0.51% |
| technical.unique.n16.b256.single | preg_match_all() [literal] | 2.546 | 0.68% |
| technical.unique.n16.b256.single | preg_match_all() [prefix] | 2.484 | 0.99% |
| technical.unique.n4.b256.single | Matcher::getMatchedKeywords() prepared | 0.544 | 0.90% |
| technical.unique.n4.b256.single | prepared_aa | 0.546 | 0.83% |
| technical.unique.n4.b256.single | Matcher::getMatchedKeywords() oneshot | 2.375 | 0.72% |
| technical.unique.n4.b256.single | oneshot_aa | 2.380 | 0.84% |
| technical.unique.n4.b256.single | strpos() loop | 0.540 | 0.57% |
| technical.unique.n4.b256.single | preg_match_all() [literal] | 1.247 | 0.82% |
| technical.unique.n4.b256.single | preg_match_all() [prefix] | 1.247 | 0.55% |
| technical.unique.n48.b256.single | Matcher::getMatchedKeywords() prepared | 0.533 | 0.84% |
| technical.unique.n48.b256.single | prepared_aa | 0.535 | 4.55% |
| technical.unique.n48.b256.single | Matcher::getMatchedKeywords() oneshot | 29.159 | 0.82% |
| technical.unique.n48.b256.single | oneshot_aa | 29.082 | 1.31% |
| technical.unique.n48.b256.single | strpos() loop | 2.218 | 0.76% |
| technical.unique.n48.b256.single | preg_match_all() [literal] | 5.148 | 0.68% |
| technical.unique.n48.b256.single | preg_match_all() [prefix] | 5.149 | 0.87% |
| technical.unique.n8.b256.single | Matcher::getMatchedKeywords() prepared | 0.543 | 0.96% |
| technical.unique.n8.b256.single | prepared_aa | 0.542 | 1.15% |
| technical.unique.n8.b256.single | Matcher::getMatchedKeywords() oneshot | 4.493 | 2.16% |
| technical.unique.n8.b256.single | oneshot_aa | 4.505 | 1.37% |
| technical.unique.n8.b256.single | strpos() loop | 0.662 | 0.93% |
| technical.unique.n8.b256.single | preg_match_all() [literal] | 1.774 | 0.77% |
| technical.unique.n8.b256.single | preg_match_all() [prefix] | 1.702 | 0.55% |
