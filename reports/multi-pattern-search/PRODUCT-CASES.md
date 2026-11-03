# Everyday application cases

All times are microseconds per complete job. String count, documents per job and preparation are shown separately. “Prototype” is Matcher for searches and Replacer for substitutions.

The existing reference is fixed across compilers; all alternatives and paired changes are in [full time results](FULL-TIME.md). These tasks have different dictionaries and inputs; their keyword counts do not define a size crossover.

## Presence checks

### Dictionary preparation included

| Task | Substrings | Documents | Existing method | Existing GCC | Prototype GCC | Existing Clang | Prototype Clang |
|---|---:|---:|---|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.343 | 6.345 | 0.368 | 5.961 |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.281 | 6.199 | 0.288 | 6.178 |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.308 | 6.393 | 0.310 | 6.071 |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.286 | 6.401 | 0.283 | 6.090 |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 1.055 | 7.483 | 1.089 | 7.261 |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.605 | 6.705 | 0.597 | 6.401 |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 1.285 | 10.987 | 1.356 | 10.314 |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 1.455 | 10.801 | 1.509 | 10.277 |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 2.096 | 11.095 | 2.147 | 10.499 |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 1.436 | 11.093 | 1.470 | 10.466 |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 3.620 | 12.859 | 3.405 | 12.510 |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 2.018 | 11.606 | 1.929 | 11.000 |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.361 | 11.036 | 0.375 | 10.643 |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.298 | 10.990 | 0.298 | 10.881 |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.376 | 11.120 | 0.373 | 10.728 |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.325 | 11.083 | 0.327 | 10.766 |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 1.582 | 11.745 | 1.615 | 11.228 |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.949 | 11.238 | 0.938 | 10.902 |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | 1 | str_contains() loop | 4.259 | 8.005 | 3.983 | 7.732 |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | 1 | str_contains() loop | 2.140 | 5.608 | 1.975 | 5.280 |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | 1 | str_contains() loop | 2.398 | 6.904 | 2.220 | 6.380 |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | 1 | str_contains() loop | 2.609 | 8.043 | 2.439 | 7.647 |

### Dictionary already prepared

| Task | Substrings | Documents | Existing method | Existing GCC | Prototype GCC | Existing Clang | Prototype Clang |
|---|---:|---:|---|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.348 | 0.234 | 0.365 | 0.243 |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.282 | 0.146 | 0.282 | 0.141 |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.309 | 0.314 | 0.312 | 0.325 |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.293 | 0.342 | 0.288 | 0.359 |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 1.064 | 1.325 | 1.087 | 1.492 |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.598 | 0.601 | 0.603 | 0.658 |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 1.296 | 0.337 | 1.310 | 0.354 |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 1.456 | 0.172 | 1.478 | 0.166 |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 2.099 | 0.467 | 2.158 | 0.490 |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 1.443 | 0.460 | 1.482 | 0.491 |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 3.602 | 2.276 | 3.388 | 2.536 |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 2.014 | 0.981 | 1.923 | 1.047 |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.352 | 0.181 | 0.378 | 0.169 |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.297 | 0.148 | 0.297 | 0.139 |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.384 | 0.235 | 0.391 | 0.228 |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.325 | 0.232 | 0.330 | 0.227 |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 1.583 | 0.759 | 1.608 | 0.751 |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | 1 | str_contains() loop | 0.930 | 0.396 | 0.939 | 0.389 |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | 1 | str_contains() loop | 4.264 | 2.659 | 4.111 | 2.389 |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | 1 | str_contains() loop | 2.141 | 0.254 | 1.977 | 0.214 |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | 1 | str_contains() loop | 2.393 | 1.531 | 2.241 | 1.321 |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | 1 | str_contains() loop | 2.608 | 2.644 | 2.418 | 2.287 |

## Search results

### Dictionary preparation included

| Task | Substrings | Documents | Existing method | Existing GCC | Prototype GCC | Existing Clang | Prototype Clang |
|---|---:|---:|---|---:|---:|---:|---:|
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | 1 | strpos() per term | 12.204 | 33.238 | 12.467 | 31.842 |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | 1 | strpos() per term | 10.189 | 33.028 | 10.977 | 31.514 |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | 1 | strpos() per term | 15.344 | 33.438 | 15.137 | 32.723 |

### Dictionary already prepared

| Task | Substrings | Documents | Existing method | Existing GCC | Prototype GCC | Existing Clang | Prototype Clang |
|---|---:|---:|---|---:|---:|---:|---:|
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | 1 | strpos() per term | 12.264 | 1.499 | 12.445 | 1.531 |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | 1 | strpos() per term | 10.280 | 1.006 | 10.611 | 1.079 |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | 1 | strpos() per term | 15.145 | 1.805 | 15.657 | 2.011 |

## Literal replacement

### Dictionary preparation included

| Task | Substrings | Documents | Existing method | Existing GCC | Prototype GCC | Existing Clang | Prototype Clang |
|---|---:|---:|---|---:|---:|---:|---:|
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | 1 | strtr() | 0.962 | 4.800 | 0.865 | 4.271 |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | 2 | strtr() | 1.403 | 5.562 | 1.301 | 5.040 |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | 1 | strtr() | 0.335 | 2.048 | 0.301 | 1.887 |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | 8 | strtr() | 2.085 | 5.239 | 1.892 | 4.444 |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | 1 | strtr() | 0.198 | 1.526 | 0.170 | 1.458 |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | 1 | strtr() | 0.296 | 1.703 | 0.271 | 1.643 |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | 1 | strtr() | 0.209 | 0.923 | 0.196 | 0.759 |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | 1 | strtr() | 0.345 | 7.809 | 0.311 | 7.343 |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | 1 | strtr() | 0.426 | 8.031 | 0.401 | 7.577 |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | 8 | strtr() | 2.838 | 11.071 | 2.727 | 10.162 |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | 1 | strtr() | 5.926 | 25.404 | 5.372 | 20.399 |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | 1 | strtr() | 6.075 | 26.576 | 5.537 | 21.836 |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | 1 | strtr() | 9.168 | 32.843 | 8.389 | 26.541 |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | 1 | strtr() | 72.363 | 152.875 | 66.159 | 110.524 |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | 1 | strtr() | 0.193 | 1.469 | 0.161 | 1.427 |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | 1 | strtr() | 0.235 | 1.550 | 0.202 | 1.497 |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | 1 | strtr() | 29.423 | 32.968 | 29.441 | 32.127 |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | 8 | strtr() | 234.652 | 43.329 | 235.303 | 42.723 |

### Dictionary already prepared

| Task | Substrings | Documents | Existing method | Existing GCC | Prototype GCC | Existing Clang | Prototype Clang |
|---|---:|---:|---|---:|---:|---:|---:|
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | 1 | strtr() | 0.337 | 0.549 | 0.298 | 0.438 |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | 8 | strtr() | 2.084 | 3.746 | 1.903 | 2.939 |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | 1 | strtr() | 0.200 | 0.259 | 0.174 | 0.173 |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | 1 | strtr() | 0.295 | 0.420 | 0.272 | 0.307 |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | 1 | strtr() | 0.212 | 0.242 | 0.188 | 0.188 |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | 1 | strtr() | 0.346 | 0.296 | 0.312 | 0.249 |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | 1 | strtr() | 0.426 | 0.479 | 0.398 | 0.412 |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | 8 | strtr() | 2.831 | 3.136 | 2.702 | 2.745 |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | 1 | strtr() | 5.958 | 10.433 | 5.375 | 6.542 |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | 1 | strtr() | 6.100 | 11.434 | 5.540 | 7.884 |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | 1 | strtr() | 9.252 | 17.782 | 8.407 | 12.500 |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | 1 | strtr() | 72.800 | 137.312 | 66.188 | 95.870 |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | 1 | strtr() | 0.190 | 0.215 | 0.164 | 0.153 |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | 1 | strtr() | 0.235 | 0.275 | 0.213 | 0.227 |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | 1 | strtr() | 29.424 | 1.437 | 29.429 | 1.452 |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | 8 | strtr() | 234.706 | 11.050 | 235.289 | 11.092 |
