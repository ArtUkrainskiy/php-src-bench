# PCRE first requests and warm-cache requests

All times are microseconds per complete job. Warm requests still build pattern strings and request-owned state. First requests run in fresh processes, with PHP startup outside the timer. They include first-use effects, preparation, query and release. These are not pure compilation measurements and are not paired with the warm-cache samples.

## Everyday cases

### gcc15

| Task | Substrings | PCRE method | Warm median | First median | First min | First max |
|---|---:|---|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.269 | 58.129 | 57.358 | 63.699 |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.171 | 57.107 | 56.706 | 62.727 |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.331 | 58.129 | 57.267 | 69.530 |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.339 | 57.808 | 55.273 | 65.342 |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2.179 | 59.331 | 57.608 | 63.429 |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.545 | 59.241 | 57.428 | 62.768 |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.694 | 66.274 | 63.990 | 69.039 |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.348 | 66.325 | 65.072 | 72.616 |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.886 | 66.685 | 65.413 | 72.335 |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.925 | 65.974 | 64.250 | 71.744 |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5.212 | 70.592 | 67.637 | 76.123 |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2.790 | 67.156 | 65.764 | 78.357 |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.296 | 58.259 | 57.388 | 61.686 |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.160 | 57.878 | 56.096 | 63.209 |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.346 | 57.097 | 56.096 | 60.153 |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.367 | 57.989 | 56.687 | 61.626 |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2.674 | 60.113 | 58.881 | 63.950 |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.668 | 59.481 | 57.457 | 64.120 |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 3.473 | 56.606 | 55.243 | 63.930 |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 0.919 | 53.560 | 52.248 | 60.533 |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 2.149 | 55.284 | 54.201 | 62.117 |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 3.204 | 56.917 | 55.174 | 62.428 |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | preg_replace_callback() | 4.108 | 74.660 | 72.476 | 87.294 |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | preg_replace_callback() | 5.187 | 69.180 | 66.515 | 78.797 |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 1.831 | 56.717 | 54.682 | 66.355 |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 4.503 | 62.167 | 60.223 | 75.531 |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 1.141 | 50.825 | 49.253 | 59.191 |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 1.542 | 53.901 | 52.529 | 63.389 |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace_callback() | 1.148 | 48.591 | 46.618 | 52.889 |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace() | 0.900 | 47.619 | 45.836 | 53.992 |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 2.339 | 66.665 | 64.431 | 76.463 |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 2.537 | 67.697 | 65.893 | 74.650 |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 4.644 | 71.304 | 69.420 | 77.195 |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 7.116 | 124.633 | 121.668 | 128.652 |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 7.012 | 123.301 | 120.586 | 126.357 |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 7.136 | 126.778 | 120.927 | 129.222 |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 6.907 | 125.445 | 121.097 | 127.830 |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 7.644 | 126.287 | 123.061 | 130.835 |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 7.242 | 124.504 | 121.928 | 132.739 |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 11.046 | 150.944 | 148.158 | 159.138 |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 10.546 | 150.172 | 147.156 | 155.893 |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 2.037 | 53.460 | 52.218 | 67.256 |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 2.219 | 55.304 | 53.400 | 67.467 |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | preg_match() per term | 22.083 | 493.657 | 485.200 | 503.344 |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 31.776 | 533.682 | 518.062 | 542.668 |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 47.644 | 688.421 | 672.302 | 703.820 |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 34.951 | 194.785 | 192.321 | 208.061 |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 98.512 | 264.827 | 261.070 | 272.641 |

### clang21

| Task | Substrings | PCRE method | Warm median | First median | First min | First max |
|---|---:|---|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.331 | 54.533 | 52.558 | 58.890 |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.267 | 53.690 | 52.088 | 62.517 |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.414 | 53.921 | 52.418 | 59.712 |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.402 | 54.352 | 51.877 | 61.956 |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2.455 | 55.904 | 54.051 | 65.343 |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.655 | 54.151 | 52.418 | 60.484 |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.677 | 62.958 | 61.174 | 70.673 |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.304 | 63.079 | 60.032 | 66.936 |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.888 | 62.678 | 60.674 | 72.977 |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.899 | 61.806 | 59.872 | 68.398 |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5.246 | 65.082 | 63.058 | 71.665 |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2.799 | 62.888 | 60.433 | 69.280 |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.326 | 53.210 | 52.208 | 61.045 |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.189 | 54.422 | 51.737 | 58.790 |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.384 | 55.434 | 51.737 | 62.237 |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.383 | 52.870 | 51.988 | 58.901 |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2.764 | 57.148 | 53.671 | 61.035 |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.725 | 55.595 | 52.939 | 60.824 |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 3.274 | 53.180 | 50.996 | 62.047 |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 0.867 | 49.433 | 47.720 | 60.244 |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 2.054 | 52.750 | 49.413 | 57.719 |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 3.116 | 52.640 | 50.665 | 61.867 |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | preg_replace_callback() | 4.133 | 69.300 | 65.123 | 79.680 |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | preg_replace_callback() | 5.278 | 62.378 | 60.114 | 73.980 |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 1.855 | 51.337 | 48.471 | 61.085 |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 4.538 | 54.744 | 52.489 | 63.821 |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 1.074 | 42.410 | 41.728 | 57.759 |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 1.519 | 46.347 | 44.294 | 62.387 |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace_callback() | 1.071 | 41.809 | 40.516 | 47.860 |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace() | 0.853 | 40.446 | 38.723 | 45.416 |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 2.535 | 60.625 | 56.527 | 74.600 |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 2.784 | 58.781 | 56.727 | 67.327 |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 4.967 | 64.111 | 61.375 | 76.414 |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 6.207 | 114.817 | 112.622 | 118.283 |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 6.078 | 111.601 | 109.847 | 117.251 |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 6.422 | 116.490 | 112.623 | 127.902 |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 6.193 | 113.524 | 111.209 | 118.053 |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 6.861 | 117.281 | 113.874 | 120.828 |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 6.441 | 114.055 | 111.210 | 118.393 |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 10.155 | 141.056 | 137.840 | 147.528 |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 9.652 | 139.372 | 136.277 | 143.491 |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 2.031 | 45.596 | 44.324 | 56.497 |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 2.225 | 47.900 | 46.798 | 57.960 |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | preg_match() per term | 21.668 | 434.189 | 423.489 | 438.207 |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 28.581 | 457.393 | 446.111 | 471.309 |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 46.218 | 596.445 | 588.901 | 614.068 |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 34.711 | 183.837 | 180.871 | 190.319 |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 98.878 | 256.564 | 250.883 | 260.772 |

## Size series

### gcc15

| Task | Substrings | PCRE method | Warm median | First median | First min | First max |
|---|---:|---|---:|---:|---:|---:|
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 0.710 | 47.449 | 46.196 | 51.166 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | preg_match() | 0.633 | 45.976 | 45.014 | 53.100 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | preg_match() | 0.759 | 48.240 | 46.517 | 53.921 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | preg_match() | 0.746 | 47.159 | 46.397 | 52.157 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 1.533 | 50.094 | 48.341 | 53.530 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | preg_match() | 0.978 | 48.160 | 46.136 | 53.070 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 1.237 | 54.743 | 53.280 | 62.367 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | preg_match() | 1.031 | 54.492 | 53.119 | 59.481 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | preg_match() | 1.304 | 56.085 | 53.981 | 62.157 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | preg_match() | 1.332 | 56.416 | 54.091 | 61.986 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 3.499 | 58.780 | 55.914 | 64.301 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | preg_match() | 1.735 | 56.145 | 54.672 | 61.796 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 2.558 | 75.311 | 73.428 | 81.593 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | preg_match() | 1.954 | 75.271 | 73.357 | 83.297 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | preg_match() | 2.761 | 77.185 | 74.129 | 84.679 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | preg_match() | 2.789 | 75.852 | 74.008 | 83.457 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 8.371 | 82.435 | 79.920 | 89.928 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | preg_match() | 4.192 | 77.125 | 74.589 | 84.809 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 4.891 | 113.543 | 110.287 | 117.410 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | preg_match() | 3.631 | 110.537 | 108.834 | 116.308 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | preg_match() | 5.213 | 115.066 | 110.788 | 116.729 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | preg_match() | 5.402 | 114.384 | 111.388 | 120.015 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 17.000 | 125.345 | 120.816 | 129.172 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | preg_match() | 8.503 | 116.879 | 114.705 | 122.039 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 9.920 | 187.351 | 184.696 | 193.473 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | preg_match() | 6.902 | 185.568 | 182.583 | 189.665 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | preg_match() | 10.347 | 190.216 | 185.929 | 199.865 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | preg_match() | 10.850 | 188.062 | 185.187 | 192.741 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 34.743 | 213.240 | 210.344 | 221.505 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | preg_match() | 17.059 | 196.969 | 194.505 | 202.329 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 19.853 | 337.823 | 331.080 | 350.407 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | preg_match() | 14.180 | 325.600 | 322.625 | 334.607 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | preg_match() | 20.803 | 338.665 | 335.108 | 344.335 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | preg_match() | 21.700 | 337.222 | 332.824 | 357.059 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 68.710 | 384.451 | 375.344 | 395.821 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | preg_match() | 33.833 | 347.001 | 339.326 | 360.476 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 48.315 | 645.269 | 638.747 | 650.629 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | preg_match() | 27.972 | 614.050 | 606.948 | 619.080 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | preg_match() | 55.309 | 643.125 | 629.851 | 653.785 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | preg_match() | 57.250 | 646.321 | 639.078 | 661.119 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 226.290 | 819.536 | 789.059 | 849.532 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | preg_match() | 112.783 | 688.691 | 678.361 | 709.971 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | preg_match() per term | 2.150 | 75.030 | 70.983 | 78.587 |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 2.394 | 82.615 | 75.812 | 96.661 |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 3.766 | 103.675 | 91.462 | 115.136 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | preg_match() per term | 3.987 | 111.890 | 106.951 | 120.175 |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 4.490 | 125.715 | 115.366 | 134.001 |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 7.028 | 158.728 | 143.599 | 169.779 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | preg_match() per term | 7.649 | 186.780 | 182.963 | 194.374 |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 8.518 | 202.720 | 199.605 | 212.959 |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 13.168 | 261.310 | 255.589 | 268.263 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | preg_match() per term | 14.446 | 334.517 | 327.084 | 338.295 |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 16.733 | 371.957 | 363.000 | 382.828 |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 24.984 | 475.852 | 465.112 | 497.783 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | preg_match() per term | 28.768 | 637.224 | 631.234 | 656.240 |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 49.666 | 687.969 | 677.931 | 702.046 |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 66.233 | 905.357 | 886.151 | 917.810 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | preg_match() per term | 60.273 | 1253.379 | 1238.993 | 1268.137 |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 112.761 | 1345.973 | 1327.789 | 1369.577 |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 137.419 | 1731.876 | 1707.821 | 1774.666 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | preg_match() per term | 135.378 | 2446.025 | 2418.302 | 2484.397 |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 238.069 | 2642.342 | 2608.499 | 2693.268 |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 275.451 | 3395.504 | 3337.676 | 3461.297 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 2.260 | 57.157 | 55.163 | 67.095 |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 6.468 | 64.310 | 63.128 | 71.333 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 5.285 | 72.697 | 68.608 | 76.824 |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 18.862 | 89.578 | 87.333 | 98.876 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 10.628 | 93.225 | 90.961 | 97.122 |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 36.785 | 124.233 | 121.227 | 132.198 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 23.111 | 145.242 | 140.914 | 151.444 |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 71.273 | 199.134 | 195.526 | 206.868 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 47.099 | 245.951 | 243.546 | 259.436 |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 123.129 | 332.824 | 325.681 | 335.950 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 116.729 | 474.209 | 468.388 | 505.547 |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 271.947 | 648.286 | 638.006 | 657.713 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 273.277 | 973.284 | 960.209 | 1005.955 |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 710.263 | 1459.715 | 1436.522 | 1497.046 |

### clang21

| Task | Substrings | PCRE method | Warm median | First median | First min | First max |
|---|---:|---|---:|---:|---:|---:|
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 0.683 | 43.622 | 41.257 | 47.780 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | preg_match() | 0.605 | 42.520 | 41.027 | 46.978 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | preg_match() | 0.715 | 42.269 | 41.348 | 52.368 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | preg_match() | 0.712 | 43.381 | 41.317 | 48.291 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 1.490 | 46.577 | 42.299 | 52.619 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | preg_match() | 0.922 | 44.634 | 41.999 | 54.432 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 1.233 | 51.376 | 49.503 | 59.271 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | preg_match() | 1.070 | 50.725 | 48.581 | 57.969 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | preg_match() | 1.308 | 49.804 | 48.611 | 61.024 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | preg_match() | 1.310 | 51.286 | 48.881 | 62.207 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 3.447 | 53.701 | 51.727 | 57.497 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | preg_match() | 1.723 | 52.899 | 50.385 | 58.499 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 2.553 | 69.931 | 67.116 | 72.967 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | preg_match() | 1.951 | 69.901 | 67.326 | 76.403 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | preg_match() | 2.729 | 70.241 | 68.528 | 77.826 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | preg_match() | 2.777 | 70.452 | 66.866 | 77.225 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 8.219 | 76.945 | 74.640 | 82.665 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | preg_match() | 4.198 | 71.163 | 70.001 | 82.635 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 4.986 | 110.668 | 106.790 | 115.967 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | preg_match() | 3.650 | 109.134 | 105.157 | 115.907 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | preg_match() | 5.369 | 111.369 | 107.201 | 121.368 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | preg_match() | 5.597 | 108.935 | 106.128 | 115.016 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 17.595 | 121.738 | 117.770 | 128.321 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | preg_match() | 8.821 | 115.166 | 112.080 | 120.416 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 10.031 | 181.500 | 179.336 | 185.467 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | preg_match() | 7.249 | 177.132 | 173.856 | 187.862 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | preg_match() | 10.684 | 183.003 | 180.408 | 188.203 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | preg_match() | 10.876 | 183.895 | 180.819 | 193.493 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 33.684 | 207.599 | 202.209 | 214.883 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | preg_match() | 16.864 | 189.104 | 184.686 | 200.015 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 20.075 | 326.142 | 320.741 | 333.215 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | preg_match() | 14.557 | 314.329 | 310.603 | 323.736 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | preg_match() | 22.612 | 320.220 | 314.860 | 331.151 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | preg_match() | 23.000 | 326.291 | 319.679 | 335.449 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 80.405 | 374.993 | 366.457 | 385.973 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | preg_match() | 33.957 | 340.939 | 333.225 | 347.772 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 50.060 | 619.250 | 609.772 | 632.555 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | preg_match() | 29.095 | 593.743 | 587.441 | 606.817 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | preg_match() | 53.915 | 611.215 | 599.193 | 622.647 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | preg_match() | 57.339 | 629.169 | 621.084 | 635.381 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 233.067 | 782.887 | 769.733 | 824.275 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | preg_match() | 114.737 | 668.743 | 659.606 | 687.128 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | preg_match() per term | 2.046 | 66.254 | 61.476 | 70.442 |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 2.294 | 71.063 | 65.433 | 81.243 |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 3.617 | 86.583 | 79.238 | 100.689 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | preg_match() per term | 3.781 | 97.963 | 92.744 | 107.501 |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 4.299 | 105.668 | 97.723 | 117.290 |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 6.702 | 135.093 | 120.877 | 146.475 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | preg_match() per term | 7.374 | 164.198 | 157.755 | 174.858 |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 8.201 | 177.473 | 172.483 | 183.133 |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 12.862 | 229.400 | 222.847 | 248.826 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | preg_match() per term | 14.395 | 292.127 | 281.928 | 296.436 |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 16.288 | 319.138 | 311.714 | 328.565 |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 24.371 | 416.721 | 403.927 | 425.348 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | preg_match() per term | 28.268 | 555.562 | 547.867 | 562.354 |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 48.466 | 592.962 | 580.347 | 611.567 |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 64.556 | 780.413 | 764.213 | 789.960 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | preg_match() per term | 60.012 | 1090.234 | 1074.363 | 1120.861 |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 110.994 | 1171.356 | 1153.261 | 1186.453 |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 133.869 | 1506.654 | 1485.695 | 1537.031 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | preg_match() per term | 132.057 | 2121.546 | 2105.566 | 2158.345 |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 232.903 | 2256.319 | 2246.120 | 2338.553 |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 268.521 | 2945.386 | 2888.389 | 3013.644 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 2.188 | 50.174 | 47.950 | 57.568 |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 6.458 | 57.387 | 55.824 | 67.206 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 5.146 | 63.479 | 60.003 | 74.690 |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 18.500 | 81.663 | 79.670 | 88.216 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 10.439 | 84.208 | 81.984 | 92.173 |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 36.729 | 118.342 | 113.834 | 129.012 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 22.785 | 136.406 | 132.098 | 142.477 |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 70.845 | 191.189 | 187.953 | 199.164 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 47.117 | 232.907 | 227.737 | 246.413 |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 129.887 | 326.653 | 320.782 | 334.548 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 108.814 | 455.274 | 450.746 | 462.578 |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 262.055 | 621.707 | 610.575 | 638.568 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 260.801 | 942.187 | 928.121 | 960.492 |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 741.988 | 1421.767 | 1398.344 | 1467.934 |
