# PCRE first requests and warm-cache requests

All times are microseconds per complete job. Warm requests still build pattern strings and request-owned state. First requests run in fresh processes, with PHP startup outside the timer. They include first-use effects, preparation, query and release. These are not pure compilation measurements and are not paired with the warm-cache samples.

## Everyday cases

### gcc15

| Task | Substrings | PCRE method | Warm median | First median | First min | First max |
|---|---:|---|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.261 | 61.505 | 59.131 | 68.378 |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.161 | 59.451 | 55.354 | 61.816 |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.315 | 58.901 | 56.065 | 67.938 |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.333 | 60.143 | 56.455 | 72.616 |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2.208 | 61.736 | 58.780 | 70.993 |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.560 | 62.738 | 57.708 | 68.058 |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.705 | 68.739 | 64.551 | 79.950 |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.349 | 68.688 | 64.701 | 74.119 |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.890 | 68.158 | 65.432 | 77.636 |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.909 | 69.260 | 65.433 | 75.892 |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5.195 | 71.845 | 68.057 | 78.777 |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2.790 | 71.764 | 65.934 | 79.438 |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.282 | 60.673 | 57.077 | 69.370 |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.151 | 60.093 | 56.576 | 68.288 |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.327 | 61.375 | 56.115 | 66.034 |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.347 | 63.048 | 57.167 | 65.774 |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2.671 | 60.424 | 57.497 | 67.226 |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.685 | 60.053 | 57.557 | 66.245 |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 3.494 | 58.199 | 55.003 | 68.038 |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 0.938 | 55.634 | 51.898 | 61.355 |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 2.142 | 58.179 | 54.732 | 62.567 |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 3.197 | 59.040 | 56.335 | 64.160 |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | preg_replace_callback() | 4.020 | 77.084 | 72.125 | 85.350 |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | preg_replace_callback() | 5.084 | 71.854 | 68.378 | 83.416 |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 1.837 | 59.892 | 56.626 | 67.106 |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 4.503 | 63.318 | 60.173 | 69.560 |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 1.122 | 51.888 | 49.553 | 64.721 |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 1.543 | 54.682 | 52.648 | 63.710 |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace_callback() | 1.128 | 51.347 | 48.872 | 57.698 |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace() | 0.887 | 50.014 | 45.896 | 55.153 |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 2.331 | 68.859 | 65.683 | 90.088 |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 2.523 | 70.863 | 66.905 | 85.069 |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 4.642 | 74.450 | 69.460 | 87.434 |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 6.821 | 124.253 | 119.805 | 128.580 |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 6.711 | 124.664 | 118.442 | 128.381 |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 7.122 | 125.355 | 120.836 | 128.160 |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 6.928 | 124.663 | 118.732 | 130.655 |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 7.649 | 126.587 | 121.598 | 134.301 |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 7.223 | 126.287 | 123.491 | 130.244 |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 10.782 | 151.624 | 146.434 | 158.357 |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 10.311 | 150.622 | 147.927 | 157.324 |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 2.010 | 54.823 | 51.928 | 67.056 |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 2.169 | 57.618 | 53.931 | 63.519 |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | preg_match() per term | 22.162 | 496.781 | 485.890 | 506.368 |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 31.121 | 533.058 | 525.604 | 544.120 |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 47.078 | 685.003 | 675.786 | 705.010 |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 35.597 | 196.288 | 189.966 | 205.996 |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 98.183 | 268.694 | 261.150 | 275.836 |

### clang21

| Task | Substrings | PCRE method | Warm median | First median | First min | First max |
|---|---:|---|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.329 | 53.961 | 52.127 | 58.830 |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.259 | 54.001 | 52.138 | 58.119 |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.376 | 54.141 | 52.318 | 65.903 |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.444 | 56.175 | 52.027 | 60.664 |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2.454 | 54.512 | 53.080 | 63.790 |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.645 | 55.444 | 52.819 | 63.138 |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.711 | 61.906 | 59.060 | 70.513 |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.311 | 61.325 | 58.169 | 67.096 |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.871 | 62.177 | 60.744 | 71.965 |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.887 | 62.748 | 60.483 | 72.626 |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5.235 | 65.823 | 64.019 | 79.850 |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2.787 | 63.308 | 61.315 | 71.964 |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.352 | 53.560 | 51.627 | 60.894 |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.196 | 52.658 | 51.827 | 60.243 |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.389 | 54.582 | 52.989 | 62.387 |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.381 | 54.231 | 51.616 | 60.023 |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2.753 | 56.596 | 53.981 | 67.096 |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.737 | 54.292 | 52.439 | 65.312 |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 3.202 | 52.950 | 50.685 | 59.842 |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 0.862 | 48.981 | 47.269 | 52.829 |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 2.045 | 50.745 | 48.762 | 59.741 |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 3.120 | 51.757 | 50.274 | 59.752 |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | preg_replace_callback() | 4.120 | 66.856 | 63.790 | 79.289 |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | preg_replace_callback() | 5.211 | 63.108 | 60.273 | 76.383 |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 1.843 | 49.192 | 47.509 | 63.600 |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 4.575 | 55.123 | 52.288 | 62.738 |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 1.076 | 43.471 | 41.528 | 53.831 |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 1.516 | 45.455 | 44.153 | 54.703 |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace_callback() | 1.078 | 41.177 | 39.764 | 45.886 |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace() | 0.860 | 39.714 | 38.202 | 48.641 |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 2.531 | 58.469 | 56.676 | 67.106 |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 2.822 | 59.622 | 57.888 | 68.839 |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 4.985 | 63.198 | 60.944 | 73.287 |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 6.104 | 113.893 | 110.987 | 116.879 |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 5.987 | 114.114 | 109.124 | 117.531 |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 6.376 | 114.985 | 111.328 | 121.828 |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 6.145 | 114.134 | 111.479 | 122.951 |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 6.944 | 115.787 | 113.843 | 123.791 |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 6.521 | 115.506 | 111.379 | 117.751 |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 10.187 | 142.016 | 137.758 | 147.736 |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 9.681 | 140.172 | 137.096 | 150.832 |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 2.055 | 46.708 | 44.544 | 59.381 |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 2.161 | 47.800 | 46.237 | 60.082 |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | preg_match() per term | 21.605 | 427.961 | 420.968 | 452.658 |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 29.480 | 457.237 | 444.934 | 475.762 |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 46.196 | 595.165 | 584.445 | 609.692 |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 34.386 | 183.975 | 180.659 | 201.928 |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 99.166 | 253.525 | 249.758 | 261.440 |

## Size series

### gcc15

| Task | Substrings | PCRE method | Warm median | First median | First min | First max |
|---|---:|---|---:|---:|---:|---:|
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 0.713 | 48.421 | 45.686 | 54.492 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | preg_match() | 0.651 | 49.242 | 45.184 | 53.600 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | preg_match() | 0.770 | 49.764 | 47.709 | 54.923 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | preg_match() | 0.757 | 49.733 | 46.928 | 54.722 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 1.548 | 51.437 | 48.661 | 55.774 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | preg_match() | 0.978 | 50.063 | 46.066 | 54.592 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 1.246 | 57.839 | 53.571 | 62.216 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | preg_match() | 1.040 | 57.287 | 52.970 | 66.064 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | preg_match() | 1.303 | 56.927 | 54.231 | 62.086 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | preg_match() | 1.322 | 58.420 | 55.815 | 68.198 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 3.497 | 60.463 | 56.746 | 67.337 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | preg_match() | 1.799 | 58.780 | 54.342 | 65.522 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 2.524 | 78.307 | 74.459 | 81.011 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | preg_match() | 1.932 | 76.633 | 73.187 | 83.396 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | preg_match() | 2.702 | 79.008 | 74.800 | 84.628 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | preg_match() | 2.782 | 78.426 | 75.161 | 83.557 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 8.338 | 81.943 | 77.976 | 89.768 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | preg_match() | 4.247 | 79.129 | 74.049 | 84.588 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 4.893 | 115.316 | 112.952 | 118.051 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | preg_match() | 3.615 | 111.749 | 106.950 | 119.954 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | preg_match() | 5.325 | 115.436 | 112.030 | 122.209 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | preg_match() | 5.355 | 116.909 | 114.204 | 120.195 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 17.049 | 127.548 | 124.062 | 136.926 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | preg_match() | 8.543 | 119.483 | 118.011 | 128.380 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 9.877 | 191.359 | 185.397 | 199.364 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | preg_match() | 7.049 | 187.902 | 181.410 | 190.216 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | preg_match() | 10.412 | 193.152 | 188.222 | 204.714 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | preg_match() | 10.815 | 190.717 | 185.628 | 200.426 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 34.901 | 216.696 | 210.203 | 225.432 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | preg_match() | 17.142 | 198.682 | 196.809 | 209.071 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 19.905 | 336.030 | 332.323 | 341.720 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | preg_match() | 14.176 | 328.254 | 323.787 | 337.472 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | preg_match() | 20.822 | 337.602 | 330.298 | 344.615 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | preg_match() | 21.693 | 339.286 | 332.773 | 345.457 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 68.546 | 383.979 | 371.175 | 394.118 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | preg_match() | 34.020 | 345.718 | 341.319 | 362.288 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 49.053 | 637.925 | 627.947 | 662.461 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | preg_match() | 27.670 | 622.896 | 614.380 | 632.254 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | preg_match() | 53.368 | 644.127 | 629.208 | 657.631 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | preg_match() | 53.440 | 652.963 | 644.377 | 663.522 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 233.702 | 826.899 | 784.920 | 864.810 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | preg_match() | 105.639 | 677.750 | 667.440 | 697.427 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | preg_match() per term | 2.136 | 76.604 | 69.420 | 81.794 |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 2.365 | 85.841 | 77.315 | 102.602 |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 3.765 | 104.576 | 91.742 | 121.227 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | preg_match() per term | 3.940 | 112.541 | 106.208 | 116.879 |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 4.479 | 128.892 | 114.474 | 140.793 |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 7.012 | 156.303 | 142.437 | 170.920 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | preg_match() per term | 7.576 | 188.293 | 182.322 | 196.468 |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 8.322 | 207.959 | 205.054 | 215.744 |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 13.219 | 267.481 | 255.047 | 279.895 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | preg_match() per term | 14.764 | 331.972 | 328.165 | 340.618 |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 16.394 | 375.022 | 367.628 | 389.410 |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 24.957 | 480.010 | 475.361 | 493.184 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | preg_match() per term | 28.618 | 636.462 | 627.836 | 650.188 |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 49.375 | 694.140 | 683.771 | 721.010 |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 66.015 | 901.047 | 882.923 | 927.587 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | preg_match() per term | 60.688 | 1248.609 | 1236.235 | 1271.511 |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 113.576 | 1345.941 | 1325.242 | 1418.076 |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 135.781 | 1745.590 | 1722.376 | 1765.637 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | preg_match() per term | 134.538 | 2438.657 | 2421.505 | 2479.775 |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 238.058 | 2652.318 | 2611.891 | 2696.701 |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 275.499 | 3391.372 | 3351.788 | 3437.608 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 2.262 | 60.984 | 55.604 | 67.366 |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 6.470 | 68.919 | 62.948 | 73.939 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 5.383 | 74.239 | 70.331 | 77.735 |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 18.641 | 92.985 | 87.394 | 98.164 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 10.735 | 95.289 | 92.263 | 102.231 |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 37.026 | 127.449 | 124.703 | 132.668 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 23.194 | 147.195 | 141.866 | 156.433 |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 71.056 | 205.876 | 200.155 | 214.822 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 47.387 | 249.267 | 243.135 | 259.747 |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 123.556 | 333.965 | 328.345 | 343.723 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 113.529 | 482.764 | 477.985 | 496.620 |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 270.081 | 646.752 | 633.817 | 653.463 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 264.934 | 982.210 | 967.663 | 1006.064 |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 760.028 | 1459.864 | 1436.680 | 1568.749 |

### clang21

| Task | Substrings | PCRE method | Warm median | First median | First min | First max |
|---|---:|---|---:|---:|---:|---:|
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 0.680 | 43.982 | 41.337 | 47.810 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | preg_match() | 0.600 | 42.600 | 41.438 | 50.936 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | preg_match() | 0.708 | 43.442 | 41.628 | 48.320 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | preg_match() | 0.728 | 44.303 | 41.197 | 49.904 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 1.461 | 44.142 | 42.459 | 49.002 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | preg_match() | 0.924 | 44.754 | 41.969 | 49.653 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 1.262 | 51.086 | 49.653 | 55.544 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | preg_match() | 1.067 | 49.883 | 48.782 | 59.371 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | preg_match() | 1.297 | 51.957 | 49.383 | 55.304 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | preg_match() | 1.350 | 51.026 | 49.693 | 60.193 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 3.426 | 53.810 | 51.566 | 64.732 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | preg_match() | 1.740 | 51.466 | 50.274 | 59.151 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 2.561 | 69.981 | 68.128 | 80.131 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | preg_match() | 2.016 | 69.249 | 67.958 | 77.395 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | preg_match() | 2.743 | 69.720 | 67.948 | 82.374 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | preg_match() | 2.742 | 71.555 | 68.939 | 77.234 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 8.269 | 76.172 | 73.608 | 79.399 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | preg_match() | 4.179 | 71.764 | 69.561 | 79.589 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 5.033 | 110.036 | 107.441 | 114.384 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | preg_match() | 3.710 | 107.512 | 102.442 | 114.143 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | preg_match() | 5.357 | 108.733 | 105.978 | 111.790 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | preg_match() | 5.604 | 110.948 | 106.861 | 115.276 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 17.544 | 123.442 | 119.444 | 127.088 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | preg_match() | 8.753 | 115.085 | 110.106 | 120.826 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 10.033 | 184.115 | 181.280 | 196.378 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | preg_match() | 7.449 | 176.010 | 173.074 | 184.686 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | preg_match() | 10.603 | 183.354 | 179.256 | 191.709 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | preg_match() | 10.888 | 184.776 | 182.131 | 191.960 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 33.657 | 209.994 | 205.424 | 216.315 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | preg_match() | 16.846 | 187.281 | 183.794 | 197.330 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 20.214 | 326.361 | 319.578 | 335.188 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | preg_match() | 14.319 | 318.446 | 313.337 | 323.196 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | preg_match() | 22.804 | 326.201 | 319.198 | 332.814 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | preg_match() | 21.798 | 328.966 | 322.694 | 334.988 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 73.149 | 374.913 | 366.145 | 384.170 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | preg_match() | 34.202 | 340.608 | 333.545 | 346.789 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 50.212 | 619.922 | 609.912 | 630.672 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | preg_match() | 29.281 | 594.714 | 587.902 | 616.415 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | preg_match() | 54.969 | 609.582 | 604.171 | 627.495 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | preg_match() | 57.627 | 619.551 | 610.183 | 628.597 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 233.298 | 782.926 | 764.232 | 812.412 |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | preg_match() | 111.171 | 663.613 | 651.440 | 689.862 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | preg_match() per term | 2.011 | 65.412 | 61.736 | 72.766 |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 2.257 | 73.367 | 65.423 | 82.845 |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 3.597 | 89.037 | 78.257 | 104.446 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | preg_match() per term | 3.932 | 96.060 | 93.154 | 103.414 |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 4.259 | 108.584 | 98.885 | 115.706 |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 6.739 | 138.669 | 123.771 | 151.674 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | preg_match() per term | 7.428 | 161.452 | 157.145 | 176.441 |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 8.202 | 177.573 | 174.076 | 183.884 |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 12.662 | 229.099 | 219.662 | 238.527 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | preg_match() per term | 14.306 | 290.193 | 284.784 | 300.443 |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 16.479 | 318.206 | 307.586 | 327.424 |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 24.292 | 414.637 | 403.465 | 438.051 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | preg_match() per term | 27.920 | 551.613 | 540.963 | 567.243 |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 48.732 | 595.094 | 582.872 | 606.316 |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 64.418 | 783.748 | 770.794 | 803.505 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | preg_match() per term | 59.825 | 1088.288 | 1075.544 | 1109.108 |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 109.740 | 1162.757 | 1154.342 | 1193.175 |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 133.507 | 1504.568 | 1470.133 | 1552.487 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | preg_match() per term | 131.120 | 2131.943 | 2117.907 | 2174.332 |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 231.790 | 2273.568 | 2234.636 | 2340.142 |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 268.343 | 2958.481 | 2911.574 | 3019.015 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 2.188 | 49.002 | 47.439 | 55.764 |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 6.410 | 57.066 | 54.412 | 62.938 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 5.085 | 63.149 | 59.982 | 67.877 |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 18.434 | 82.805 | 80.050 | 92.002 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 10.482 | 85.319 | 83.115 | 96.040 |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 36.551 | 118.883 | 114.494 | 125.054 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 22.563 | 135.564 | 130.945 | 145.362 |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 70.469 | 193.492 | 187.701 | 200.366 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 47.048 | 234.770 | 231.012 | 240.301 |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 129.183 | 328.225 | 321.372 | 332.192 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 107.227 | 459.170 | 445.544 | 478.957 |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 261.552 | 621.304 | 613.840 | 640.570 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 265.663 | 935.732 | 918.680 | 961.261 |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 718.674 | 1414.039 | 1390.604 | 1466.838 |
