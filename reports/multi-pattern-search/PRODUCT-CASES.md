# Everyday application cases

All times are microseconds per complete job. String count, documents per job and preparation are shown separately. “Prototype” is Matcher for searches and Replacer for substitutions.

The existing reference is fixed across compilers; all alternatives and paired changes are in [full time results](FULL-TIME.md). These tasks have different dictionaries and inputs; their keyword counts do not define a size crossover.

## Presence checks

### Dictionary preparation included

| Task | Substrings | Documents | Existing method | Existing GCC | Prototype GCC | Existing Clang | Prototype Clang |
|---|---:|---:|---|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.346 | 7.080 | 0.367 | 6.519 |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.282 | 6.896 | 0.285 | 6.391 |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.317 | 7.152 | 0.310 | 6.708 |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.289 | 7.172 | 0.286 | 6.692 |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 1.057 | 8.563 | 1.087 | 8.323 |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.599 | 7.518 | 0.598 | 7.127 |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 1.284 | 20.675 | 1.331 | 19.801 |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 1.462 | 20.725 | 1.474 | 19.612 |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 2.104 | 20.781 | 2.138 | 19.801 |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 1.459 | 20.896 | 1.479 | 19.986 |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 3.613 | 23.086 | 3.408 | 22.393 |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 2.018 | 21.485 | 1.929 | 20.636 |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.355 | 17.398 | 0.367 | 16.418 |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.297 | 17.389 | 0.299 | 16.205 |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.383 | 17.509 | 0.387 | 16.436 |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.325 | 17.476 | 0.323 | 16.425 |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 1.588 | 19.032 | 1.614 | 17.978 |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.946 | 18.078 | 0.933 | 16.975 |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | 1 | str_contains() loop | 4.250 | 11.934 | 3.949 | 12.073 |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | 1 | str_contains() loop | 2.139 | 6.228 | 1.981 | 5.894 |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | 1 | str_contains() loop | 2.395 | 9.200 | 2.213 | 9.155 |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | 1 | str_contains() loop | 2.612 | 11.828 | 2.411 | 12.015 |

### Dictionary already prepared

| Task | Substrings | Documents | Existing method | Existing GCC | Prototype GCC | Existing Clang | Prototype Clang |
|---|---:|---:|---|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.347 | 0.265 | 0.362 | 0.273 |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.279 | 0.161 | 0.282 | 0.156 |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.314 | 0.401 | 0.310 | 0.419 |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.284 | 0.438 | 0.287 | 0.458 |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 1.057 | 1.821 | 1.086 | 1.979 |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.602 | 0.809 | 0.597 | 0.862 |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 1.304 | 0.397 | 1.318 | 0.414 |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 1.460 | 0.201 | 1.470 | 0.197 |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 2.111 | 0.624 | 2.134 | 0.660 |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 1.438 | 0.634 | 1.480 | 0.674 |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 3.594 | 2.939 | 3.391 | 3.202 |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 2.013 | 1.244 | 1.921 | 1.340 |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.358 | 0.245 | 0.384 | 0.253 |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.298 | 0.153 | 0.297 | 0.150 |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.378 | 0.380 | 0.383 | 0.399 |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.329 | 0.380 | 0.327 | 0.396 |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 1.582 | 1.708 | 1.612 | 1.857 |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.926 | 0.791 | 0.954 | 0.845 |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | 1 | str_contains() loop | 4.253 | 6.059 | 3.947 | 6.619 |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | 1 | str_contains() loop | 2.138 | 0.423 | 1.971 | 0.440 |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | 1 | str_contains() loop | 2.386 | 3.406 | 2.205 | 3.720 |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | 1 | str_contains() loop | 2.601 | 6.013 | 2.402 | 6.577 |

## Search results

### Dictionary preparation included

| Task | Substrings | Documents | Existing method | Existing GCC | Prototype GCC | Existing Clang | Prototype Clang |
|---|---:|---:|---|---:|---:|---:|---:|
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | 1 | strpos() per term | 12.146 | 32.607 | 12.385 | 30.973 |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | 1 | strpos() per term | 10.185 | 31.370 | 11.006 | 30.085 |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | 1 | strpos() per term | 14.928 | 32.595 | 15.169 | 31.418 |

### Dictionary already prepared

| Task | Substrings | Documents | Existing method | Existing GCC | Prototype GCC | Existing Clang | Prototype Clang |
|---|---:|---:|---|---:|---:|---:|---:|
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | 1 | strpos() per term | 12.238 | 1.797 | 12.950 | 1.969 |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | 1 | strpos() per term | 10.233 | 1.253 | 11.033 | 1.318 |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | 1 | strpos() per term | 14.947 | 2.152 | 15.609 | 2.377 |

## Literal replacement

### Dictionary preparation included

| Task | Substrings | Documents | Existing method | Existing GCC | Prototype GCC | Existing Clang | Prototype Clang |
|---|---:|---:|---|---:|---:|---:|---:|
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | 1 | strtr() | 0.968 | 6.891 | 0.867 | 6.624 |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | 2 | strtr() | 1.407 | 7.808 | 1.286 | 7.669 |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | 1 | strtr() | 0.337 | 2.517 | 0.298 | 2.449 |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | 8 | strtr() | 2.083 | 6.553 | 1.907 | 6.661 |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | 1 | strtr() | 0.203 | 0.912 | 0.171 | 0.885 |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | 1 | strtr() | 0.302 | 1.119 | 0.268 | 1.086 |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | 1 | strtr() | 0.208 | 0.537 | 0.196 | 0.528 |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | 1 | strtr() | 0.345 | 9.397 | 0.312 | 9.009 |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | 1 | strtr() | 0.425 | 10.065 | 0.398 | 9.585 |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | 8 | strtr() | 2.846 | 13.258 | 2.685 | 12.870 |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | 1 | strtr() | 5.950 | 41.759 | 5.377 | 42.308 |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | 1 | strtr() | 6.102 | 43.400 | 5.548 | 43.120 |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | 1 | strtr() | 9.214 | 51.543 | 8.367 | 51.548 |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | 1 | strtr() | 72.800 | 199.191 | 66.151 | 209.258 |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | 1 | strtr() | 0.197 | 0.868 | 0.163 | 0.834 |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | 1 | strtr() | 0.234 | 0.937 | 0.202 | 0.908 |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | 1 | strtr() | 29.479 | 35.888 | 29.459 | 34.521 |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | 8 | strtr() | 234.858 | 48.320 | 234.868 | 46.583 |

### Dictionary already prepared

| Task | Substrings | Documents | Existing method | Existing GCC | Prototype GCC | Existing Clang | Prototype Clang |
|---|---:|---:|---|---:|---:|---:|---:|
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | 1 | strtr() | 0.338 | 0.660 | 0.297 | 0.681 |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | 8 | strtr() | 2.078 | 4.639 | 1.893 | 4.864 |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | 1 | strtr() | 0.198 | 0.323 | 0.170 | 0.352 |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | 1 | strtr() | 0.292 | 0.532 | 0.269 | 0.551 |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | 1 | strtr() | 0.212 | 0.270 | 0.187 | 0.265 |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | 1 | strtr() | 0.347 | 0.330 | 0.312 | 0.357 |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | 1 | strtr() | 0.427 | 0.574 | 0.402 | 0.606 |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | 8 | strtr() | 2.826 | 3.982 | 2.691 | 4.286 |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | 1 | strtr() | 5.924 | 12.331 | 5.379 | 14.359 |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | 1 | strtr() | 6.093 | 13.962 | 5.551 | 15.143 |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | 1 | strtr() | 9.172 | 21.963 | 8.368 | 23.277 |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | 1 | strtr() | 73.932 | 169.749 | 67.274 | 180.669 |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | 1 | strtr() | 0.190 | 0.255 | 0.163 | 0.271 |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | 1 | strtr() | 0.235 | 0.329 | 0.202 | 0.333 |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | 1 | strtr() | 29.439 | 1.725 | 29.378 | 1.742 |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | 8 | strtr() | 234.649 | 13.030 | 234.979 | 13.106 |
