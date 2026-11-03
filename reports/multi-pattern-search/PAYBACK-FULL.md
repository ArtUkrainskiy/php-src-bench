# Direct batch times

Microseconds per complete batch. The candidate is built once for B jobs; native/PCRE setup is already prepared. Delta is the median paired time change; min/max are paired changes, not confidence intervals. See [interpretation and tested counts](AMORTIZATION.md).

## gcc15

| Task | Jobs | Existing method | Existing µs | Prepared API µs | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 1 | str_contains() loop | 0.369 | 6.416 | +1638.9% | +1600.0% | +1655.0% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 1 | preg_match() | 0.262 | 6.416 | +2348.9% | +2337.9% | +2369.2% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 285 | str_contains() loop | 89.603 | 60.286 | -32.8% | -33.9% | -31.2% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 285 | preg_match() | 57.414 | 60.286 | +5.0% | +4.4% | +5.3% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 345 | str_contains() loop | 106.265 | 71.505 | -32.8% | -34.7% | -31.9% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 345 | preg_match() | 69.187 | 71.505 | +3.3% | +2.7% | +4.4% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 690 | str_contains() loop | 213.282 | 136.015 | -36.2% | -37.5% | -35.8% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 690 | preg_match() | 139.663 | 136.015 | -2.6% | -3.0% | -0.9% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 1 | str_contains() loop | 1.303 | 11.035 | +747.2% | +741.2% | +752.4% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 1 | preg_match() | 0.529 | 11.035 | +1987.0% | +1980.4% | +1989.6% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 53 | str_contains() loop | 66.464 | 26.365 | -60.4% | -60.8% | -60.1% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 53 | preg_match() | 25.265 | 26.365 | +4.4% | +3.1% | +4.8% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 66 | str_contains() loop | 82.053 | 29.789 | -63.7% | -63.8% | -63.5% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 66 | preg_match() | 31.464 | 29.789 | -5.2% | -5.7% | -5.1% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 1 | str_contains() loop | 0.380 | 11.056 | +2808.3% | +2747.0% | +2837.2% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 1 | preg_match() | 0.292 | 11.056 | +3682.9% | +3661.5% | +3700.1% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 102 | str_contains() loop | 34.620 | 23.638 | -31.7% | -32.0% | -31.3% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 102 | preg_match() | 23.984 | 23.638 | -1.5% | -1.9% | -1.3% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 125 | str_contains() loop | 40.390 | 26.502 | -34.2% | -35.7% | -33.6% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 125 | preg_match() | 29.318 | 26.502 | -9.5% | -10.1% | -9.1% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 1 | str_contains() loop | 0.296 | 6.258 | +2011.9% | +1985.1% | +2040.5% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 1 | preg_match() | 0.174 | 6.258 | +3504.2% | +3469.7% | +3594.6% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 241 | str_contains() loop | 58.750 | 29.692 | -49.5% | -50.3% | -48.9% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 241 | preg_match() | 28.071 | 29.692 | +5.2% | +4.4% | +6.6% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 292 | str_contains() loop | 69.745 | 34.500 | -50.6% | -51.4% | -49.3% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 292 | preg_match() | 34.550 | 34.500 | -0.2% | -1.0% | +2.5% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 584 | str_contains() loop | 143.857 | 63.190 | -56.0% | -56.5% | -55.6% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 584 | preg_match() | 67.724 | 63.190 | -6.8% | -7.9% | -6.2% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 1 | str_contains() loop | 0.316 | 6.518 | +1966.9% | +1940.8% | +1986.4% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 1 | preg_match() | 0.316 | 6.518 | +1961.5% | +1954.8% | +1970.0% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 8 | str_contains() loop | 2.139 | 8.431 | +294.0% | +291.5% | +302.1% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 8 | preg_match() | 2.121 | 8.431 | +297.9% | +295.7% | +299.9% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 1 | str_contains() loop | 0.306 | 6.421 | +2000.0% | +1984.7% | +2035.8% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 1 | preg_match() | 0.334 | 6.421 | +1827.2% | +1817.9% | +1855.5% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 8 | str_contains() loop | 1.973 | 8.504 | +331.0% | +323.7% | +336.9% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 8 | preg_match() | 2.230 | 8.504 | +281.4% | +280.0% | +283.7% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 1 | str_contains() loop | 1.068 | 7.428 | +596.2% | +590.0% | +597.1% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 1 | preg_match() | 1.219 | 7.428 | +509.2% | +488.9% | +529.4% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 8 | str_contains() loop | 8.137 | 16.436 | +102.1% | +101.5% | +102.5% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 8 | preg_match() | 9.032 | 16.436 | +81.9% | +80.6% | +83.8% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 1 | strpos() per term | 10.199 | 32.700 | +220.9% | +218.2% | +224.7% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 1 | PCRE lookahead per term | 17.571 | 32.700 | +86.1% | +80.5% | +93.7% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 3 | strpos() per term | 30.483 | 34.772 | +14.1% | +13.0% | +15.3% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 3 | PCRE lookahead per term | 52.519 | 34.772 | -33.8% | -35.3% | -31.1% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 6 | strpos() per term | 63.366 | 37.802 | -40.5% | -41.0% | -39.9% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 6 | PCRE lookahead per term | 104.159 | 37.802 | -63.7% | -64.3% | -62.2% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 1 | strpos() per term | 12.134 | 33.092 | +172.6% | +170.0% | +174.9% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 1 | preg_match() per term | 14.826 | 33.092 | +123.1% | +122.3% | +123.5% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 2 | strpos() per term | 24.301 | 34.764 | +43.1% | +42.1% | +44.0% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 2 | preg_match() per term | 29.475 | 34.764 | +17.9% | +17.2% | +18.8% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 5 | strpos() per term | 60.033 | 39.631 | -34.0% | -34.7% | -33.3% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 5 | preg_match() per term | 73.552 | 39.631 | -46.1% | -46.6% | -45.6% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 1 | strpos() per term | 14.947 | 33.385 | +123.1% | +121.0% | +124.7% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 1 | PCRE lookahead per term | 34.553 | 33.385 | -3.4% | -4.3% | -1.3% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 2 | strpos() per term | 29.910 | 35.410 | +18.3% | +17.8% | +19.8% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 2 | PCRE lookahead per term | 69.522 | 35.410 | -49.1% | -49.5% | -48.5% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 5 | strpos() per term | 74.533 | 41.231 | -44.7% | -44.9% | -44.3% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 5 | PCRE lookahead per term | 168.787 | 41.231 | -75.5% | -75.9% | -75.1% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 1 | strtr() | 29.415 | 32.034 | +8.9% | +8.4% | +9.4% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 1 | preg_replace_callback() | 9.155 | 32.034 | +249.8% | +248.2% | +251.4% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 4 | strtr() | 117.595 | 37.671 | -68.0% | -68.1% | -67.9% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 4 | preg_replace_callback() | 36.227 | 37.671 | +4.0% | +3.7% | +4.2% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 7 | strtr() | 205.864 | 40.978 | -80.1% | -80.2% | -80.0% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 7 | preg_replace_callback() | 63.437 | 40.978 | -35.3% | -35.5% | -35.2% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 1 | strtr() | 0.302 | 1.726 | +471.9% | +463.6% | +474.6% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 1 | preg_replace_callback() | 0.563 | 1.726 | +206.4% | +203.9% | +207.8% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 1 | str_replace() | 0.343 | 1.726 | +403.5% | +397.3% | +404.7% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 2.033 | 4.242 | +108.9% | +107.5% | +110.1% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 3.998 | 4.242 | +6.4% | +5.4% | +6.8% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 2.249 | 4.242 | +88.6% | +86.5% | +91.2% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 1 | strtr() | 0.242 | 1.567 | +549.0% | +544.3% | +551.1% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 1 | preg_replace_callback() | 0.335 | 1.567 | +367.8% | +364.8% | +372.1% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 1 | str_replace() | 0.286 | 1.567 | +447.1% | +442.2% | +448.9% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 8 | strtr() | 1.554 | 3.107 | +100.3% | +98.5% | +103.5% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 8 | preg_replace_callback() | 2.227 | 3.107 | +40.1% | +38.9% | +42.1% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 8 | str_replace() | 1.792 | 3.107 | +73.8% | +72.4% | +77.0% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 1 | strtr() | 5.932 | 25.419 | +328.4% | +327.0% | +329.8% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 1 | preg_replace_callback() | 0.489 | 25.419 | +5095.0% | +5061.3% | +5112.1% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 1 | str_replace() | 11.309 | 25.419 | +124.8% | +124.0% | +125.5% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 1 | preg_replace() | 0.478 | 25.419 | +5213.2% | +5168.3% | +5247.7% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 8 | strtr() | 47.090 | 97.727 | +107.6% | +106.6% | +108.3% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 8 | preg_replace_callback() | 3.443 | 97.727 | +2737.9% | +2730.2% | +2747.8% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 8 | str_replace() | 89.866 | 97.727 | +8.8% | +8.2% | +9.1% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 8 | preg_replace() | 3.317 | 97.727 | +2848.7% | +2829.1% | +2858.8% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 1 | strtr() | 73.882 | 152.896 | +106.8% | +105.7% | +107.4% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 1 | preg_replace_callback() | 4.534 | 152.896 | +3271.4% | +3257.6% | +3278.0% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 1 | str_replace() | 147.461 | 152.896 | +3.7% | +3.0% | +3.9% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 1 | preg_replace() | 4.142 | 152.896 | +3591.4% | +3573.5% | +3606.4% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 8 | strtr() | 588.138 | 1117.406 | +90.0% | +88.9% | +90.4% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 8 | preg_replace_callback() | 36.149 | 1117.406 | +2991.0% | +2977.4% | +2996.4% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 8 | str_replace() | 1174.676 | 1117.406 | -4.8% | -5.5% | -4.5% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 8 | preg_replace() | 32.971 | 1117.406 | +3292.6% | +3263.1% | +3301.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 1 | str_contains() loop | 0.302 | 2.444 | +705.5% | +696.3% | +727.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 1 | preg_match() | 0.250 | 2.444 | +878.9% | +873.2% | +889.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 42 | str_contains() loop | 10.520 | 7.760 | -26.3% | -26.6% | -24.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 42 | preg_match() | 7.940 | 7.760 | -2.1% | -2.8% | -0.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 53 | str_contains() loop | 12.803 | 9.305 | -27.4% | -30.0% | -26.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 53 | preg_match() | 9.857 | 9.305 | -5.6% | -6.3% | -5.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 1 | str_contains() loop | 0.457 | 5.179 | +1032.7% | +997.9% | +1040.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 1 | preg_match() | 0.353 | 5.179 | +1368.8% | +1356.5% | +1374.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 31 | str_contains() loop | 12.378 | 9.163 | -25.9% | -28.2% | -25.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 31 | preg_match() | 9.281 | 9.163 | -1.2% | -1.6% | -0.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 40 | str_contains() loop | 16.395 | 10.257 | -37.5% | -37.7% | -35.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 40 | preg_match() | 11.906 | 10.257 | -13.9% | -14.3% | -13.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 1 | str_contains() loop | 0.783 | 13.151 | +1578.5% | +1556.7% | +1619.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 1 | preg_match() | 0.748 | 13.151 | +1656.8% | +1652.8% | +1662.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 24 | str_contains() loop | 19.031 | 17.833 | -6.3% | -6.5% | -6.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 24 | preg_match() | 16.744 | 17.833 | +6.4% | +5.7% | +6.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 31 | str_contains() loop | 24.120 | 18.551 | -23.1% | -23.2% | -22.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 31 | preg_match() | 21.623 | 18.551 | -14.2% | -14.5% | -14.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 1 | str_contains() loop | 1.493 | 26.337 | +1659.3% | +1598.0% | +1680.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 1 | preg_match() | 1.472 | 26.337 | +1689.5% | +1680.2% | +1696.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 21 | str_contains() loop | 30.650 | 30.985 | +1.0% | -1.7% | +1.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 21 | preg_match() | 29.933 | 30.985 | +3.6% | +3.0% | +4.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 28 | str_contains() loop | 42.492 | 31.701 | -25.3% | -25.9% | -23.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 28 | preg_match() | 39.983 | 31.701 | -20.7% | -20.9% | -20.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 1 | str_contains() loop | 3.056 | 58.411 | +1809.1% | +1789.7% | +1836.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 1 | preg_match() | 2.985 | 58.411 | +1858.6% | +1835.6% | +1877.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 21 | str_contains() loop | 64.459 | 62.443 | -3.1% | -5.0% | -0.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 21 | preg_match() | 61.028 | 62.443 | +2.3% | +2.0% | +2.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 28 | str_contains() loop | 85.977 | 63.864 | -25.7% | -26.3% | -24.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 28 | preg_match() | 80.774 | 63.864 | -21.0% | -21.6% | -20.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 1 | str_contains() loop | 7.080 | 152.615 | +2055.7% | +2028.6% | +2089.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 1 | preg_match() | 6.058 | 152.615 | +2419.4% | +2407.6% | +2426.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 26 | str_contains() loop | 173.622 | 158.762 | -8.5% | -12.0% | -7.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 26 | preg_match() | 156.035 | 158.762 | +1.7% | +1.5% | +2.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 34 | str_contains() loop | 230.942 | 160.192 | -30.6% | -31.3% | -30.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 34 | preg_match() | 202.523 | 160.192 | -20.9% | -21.2% | -20.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 1 | str_contains() loop | 16.423 | 294.350 | +1692.4% | +1676.7% | +1703.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 1 | preg_match() | 22.598 | 294.350 | +1203.9% | +1194.3% | +1227.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 18 | str_contains() loop | 294.844 | 298.387 | +1.1% | +0.7% | +3.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 18 | preg_match() | 396.322 | 298.387 | -24.7% | -25.1% | -22.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 24 | str_contains() loop | 401.906 | 300.095 | -25.3% | -25.7% | -24.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 24 | preg_match() | 508.512 | 300.095 | -41.0% | -41.3% | -40.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 1 | strpos() per term | 1.185 | 3.106 | +162.0% | +161.3% | +162.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 1 | preg_match() per term | 1.489 | 3.106 | +108.6% | +107.8% | +109.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 7 | strpos() per term | 7.912 | 8.318 | +5.1% | +4.8% | +5.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 7 | preg_match() per term | 10.034 | 8.318 | -17.1% | -17.5% | -16.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 11 | strpos() per term | 12.433 | 11.801 | -5.1% | -5.6% | -4.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 11 | preg_match() per term | 15.670 | 11.801 | -24.7% | -25.0% | -24.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 1 | strpos() per term | 2.170 | 5.098 | +135.0% | +133.9% | +205.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 1 | preg_match() per term | 2.748 | 5.098 | +85.7% | +84.0% | +142.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 3 | strpos() per term | 6.377 | 7.238 | +13.5% | +12.9% | +14.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 3 | preg_match() per term | 8.045 | 7.238 | -10.0% | -10.2% | -9.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 6 | strpos() per term | 12.725 | 10.487 | -17.6% | -17.8% | -17.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 6 | preg_match() per term | 15.896 | 10.487 | -34.0% | -34.3% | -33.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 1 | strpos() per term | 3.904 | 9.322 | +138.8% | +137.1% | +140.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 1 | preg_match() per term | 5.263 | 9.322 | +77.1% | +76.5% | +78.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 3 | strpos() per term | 11.582 | 11.679 | +1.0% | +0.5% | +1.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 3 | preg_match() per term | 15.501 | 11.679 | -24.6% | -25.0% | -24.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 6 | strpos() per term | 23.255 | 15.113 | -35.1% | -35.3% | -34.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 6 | preg_match() per term | 31.552 | 15.113 | -52.1% | -52.2% | -51.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 1 | strpos() per term | 7.968 | 19.738 | +147.4% | +146.5% | +149.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 1 | preg_match() per term | 9.874 | 19.738 | +99.8% | +99.2% | +101.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 2 | strpos() per term | 15.817 | 20.995 | +32.7% | +31.5% | +33.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 2 | preg_match() per term | 19.651 | 20.995 | +6.8% | +6.5% | +7.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 5 | strpos() per term | 39.118 | 26.110 | -33.3% | -33.7% | -32.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 5 | preg_match() per term | 48.585 | 26.110 | -46.2% | -46.5% | -46.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 1 | strpos() per term | 15.947 | 47.319 | +196.9% | +193.5% | +199.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 1 | preg_match() per term | 18.820 | 47.319 | +151.6% | +149.2% | +153.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 3 | strpos() per term | 47.599 | 52.292 | +9.9% | +8.0% | +11.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 3 | preg_match() per term | 56.877 | 52.292 | -8.1% | -9.0% | -7.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 6 | strpos() per term | 95.047 | 56.009 | -41.1% | -41.7% | -40.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 6 | preg_match() per term | 113.729 | 56.009 | -50.7% | -51.1% | -50.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 1 | strpos() per term | 32.015 | 134.558 | +320.0% | +318.5% | +322.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 1 | preg_match() per term | 38.820 | 134.558 | +246.6% | +243.8% | +248.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 4 | strpos() per term | 127.423 | 140.815 | +10.4% | +10.1% | +10.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 4 | preg_match() per term | 154.955 | 140.815 | -9.2% | -10.6% | -8.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 7 | strpos() per term | 223.589 | 147.040 | -34.3% | -34.6% | -33.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 7 | preg_match() per term | 265.546 | 147.040 | -44.6% | -44.9% | -44.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 1 | strpos() per term | 61.956 | 354.061 | +471.5% | +468.6% | +473.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 1 | preg_match() per term | 93.757 | 354.061 | +277.4% | +276.0% | +279.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 5 | strpos() per term | 308.780 | 365.449 | +18.4% | +17.9% | +18.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 5 | preg_match() per term | 463.274 | 365.449 | -21.1% | -21.3% | -20.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 9 | strpos() per term | 554.253 | 371.202 | -33.0% | -33.2% | -32.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 9 | preg_match() per term | 833.394 | 371.202 | -55.4% | -55.6% | -55.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 1 | strtr() | 4.478 | 3.589 | -19.9% | -20.7% | -18.6% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 1 | preg_replace_callback() | 0.700 | 3.589 | +413.1% | +410.3% | +415.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 34.785 | 11.487 | -67.0% | -67.7% | -66.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 5.232 | 11.487 | +119.6% | +119.0% | +120.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 1 | strtr() | 7.899 | 6.186 | -21.7% | -22.3% | -20.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 1 | preg_replace_callback() | 1.987 | 6.186 | +211.3% | +210.3% | +212.6% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 6 | strtr() | 47.075 | 11.972 | -74.6% | -74.7% | -74.4% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 6 | preg_replace_callback() | 11.501 | 11.972 | +4.1% | +2.9% | +4.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 10 | strtr() | 78.667 | 16.584 | -78.9% | -79.1% | -78.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 10 | preg_replace_callback() | 19.558 | 16.584 | -15.0% | -16.3% | -13.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 1 | strtr() | 16.827 | 10.523 | -37.4% | -37.6% | -37.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 1 | preg_replace_callback() | 3.814 | 10.523 | +175.9% | +174.8% | +178.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 3 | strtr() | 50.212 | 13.119 | -73.9% | -74.0% | -73.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 3 | preg_replace_callback() | 11.311 | 13.119 | +16.0% | +15.6% | +16.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 6 | strtr() | 100.881 | 16.908 | -83.2% | -83.3% | -83.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 6 | preg_replace_callback() | 22.525 | 16.908 | -24.9% | -25.2% | -24.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 1 | strtr() | 31.141 | 19.995 | -35.8% | -35.9% | -35.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 1 | preg_replace_callback() | 6.980 | 19.995 | +186.5% | +185.3% | +187.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 3 | strtr() | 93.363 | 22.720 | -75.7% | -75.7% | -75.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 3 | preg_replace_callback() | 20.771 | 22.720 | +9.4% | +9.0% | +10.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 6 | strtr() | 186.513 | 26.896 | -85.6% | -85.6% | -85.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 6 | preg_replace_callback() | 41.231 | 26.896 | -34.8% | -35.1% | -34.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 1 | strtr() | 38.014 | 46.040 | +21.0% | +19.9% | +22.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 1 | preg_replace_callback() | 11.014 | 46.040 | +318.6% | +314.0% | +324.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 4 | strtr() | 151.900 | 51.295 | -66.2% | -66.5% | -65.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 4 | preg_replace_callback() | 43.841 | 51.295 | +17.0% | +15.9% | +17.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 7 | strtr() | 265.969 | 55.908 | -79.0% | -79.2% | -78.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 7 | preg_replace_callback() | 76.728 | 55.908 | -27.1% | -28.0% | -26.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 1 | strtr() | 41.606 | 114.339 | +174.7% | +173.7% | +177.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 1 | preg_replace_callback() | 22.802 | 114.339 | +401.5% | +398.3% | +405.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 5 | strtr() | 207.881 | 123.676 | -40.5% | -40.7% | -40.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 5 | preg_replace_callback() | 113.451 | 123.676 | +9.0% | +8.8% | +9.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 9 | strtr() | 373.811 | 132.479 | -64.6% | -64.7% | -64.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 9 | preg_replace_callback() | 203.633 | 132.479 | -35.0% | -35.3% | -34.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 1 | strtr() | 42.491 | 294.290 | +592.7% | +591.6% | +595.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 1 | preg_replace_callback() | 68.651 | 294.290 | +328.7% | +327.7% | +331.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 7 | strtr() | 297.247 | 306.236 | +3.0% | +2.8% | +3.6% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 7 | preg_replace_callback() | 468.547 | 306.236 | -34.6% | -34.9% | -34.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 11 | strtr() | 466.663 | 315.624 | -32.4% | -32.5% | -32.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 11 | preg_replace_callback() | 733.430 | 315.624 | -57.0% | -57.2% | -56.9% |

## clang21

| Task | Jobs | Existing method | Existing µs | Prepared API µs | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 1 | str_contains() loop | 0.370 | 6.047 | +1533.5% | +1493.9% | +1544.3% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 1 | preg_match() | 0.256 | 6.047 | +2264.5% | +2235.0% | +2276.4% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 719 | str_contains() loop | 228.672 | 153.222 | -33.0% | -33.3% | -30.8% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 719 | preg_match() | 143.882 | 153.222 | +6.4% | +5.5% | +6.9% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 865 | str_contains() loop | 289.231 | 183.257 | -36.6% | -37.0% | -36.0% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 865 | preg_match() | 174.146 | 183.257 | +5.2% | +4.3% | +5.6% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 1024 | str_contains() loop | 313.051 | 215.356 | -31.2% | -33.2% | -31.0% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 1024 | preg_match() | 205.933 | 215.356 | +4.6% | +3.9% | +5.2% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 1 | str_contains() loop | 1.335 | 10.436 | +682.3% | +678.0% | +687.4% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 1 | preg_match() | 0.534 | 10.436 | +1854.8% | +1842.9% | +1879.4% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 58 | str_contains() loop | 74.818 | 28.320 | -62.2% | -62.4% | -61.5% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 58 | preg_match() | 27.784 | 28.320 | +1.8% | +0.5% | +2.7% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 72 | str_contains() loop | 91.297 | 32.769 | -64.1% | -64.2% | -63.9% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 72 | preg_match() | 34.640 | 32.769 | -5.4% | -6.4% | -5.0% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 1 | str_contains() loop | 0.386 | 10.679 | +2667.2% | +2579.8% | +2680.7% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 1 | preg_match() | 0.290 | 10.679 | +3588.3% | +3552.3% | +3622.5% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 90 | str_contains() loop | 30.852 | 21.873 | -29.1% | -29.3% | -28.7% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 90 | preg_match() | 21.356 | 21.873 | +2.4% | +1.9% | +3.8% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 111 | str_contains() loop | 38.133 | 24.587 | -35.4% | -35.7% | -35.2% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 111 | preg_match() | 26.333 | 24.587 | -6.6% | -7.0% | -5.9% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 1 | str_contains() loop | 0.294 | 6.401 | +2075.6% | +2057.5% | +2084.1% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 1 | preg_match() | 0.159 | 6.401 | +3917.6% | +3872.5% | +3938.9% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 406 | str_contains() loop | 101.262 | 46.108 | -54.4% | -54.8% | -54.2% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 406 | preg_match() | 44.564 | 46.108 | +3.4% | +3.1% | +4.2% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 490 | str_contains() loop | 122.385 | 54.325 | -55.6% | -56.0% | -55.4% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 490 | preg_match() | 52.792 | 54.325 | +2.9% | +2.6% | +3.2% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 980 | str_contains() loop | 243.743 | 103.131 | -57.7% | -57.8% | -57.5% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 980 | preg_match() | 106.562 | 103.131 | -3.3% | -4.5% | -2.2% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 1 | str_contains() loop | 0.323 | 6.181 | +1813.8% | +1799.6% | +1821.1% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 1 | preg_match() | 0.314 | 6.181 | +1871.9% | +1855.6% | +1880.2% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 8 | str_contains() loop | 2.215 | 8.200 | +270.1% | +267.4% | +271.2% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 8 | preg_match() | 2.139 | 8.200 | +283.4% | +279.9% | +285.9% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 1 | str_contains() loop | 0.302 | 6.118 | +1925.6% | +1897.1% | +1934.3% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 1 | preg_match() | 0.330 | 6.118 | +1752.7% | +1737.8% | +1770.6% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 8 | str_contains() loop | 2.004 | 8.480 | +323.2% | +322.1% | +324.6% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 8 | preg_match() | 2.278 | 8.480 | +272.4% | +268.9% | +277.3% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 1 | str_contains() loop | 1.087 | 7.255 | +567.5% | +562.1% | +572.1% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 1 | preg_match() | 1.367 | 7.255 | +432.5% | +422.0% | +438.3% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 8 | str_contains() loop | 8.442 | 17.551 | +107.8% | +106.3% | +108.9% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 8 | preg_match() | 10.614 | 17.551 | +65.5% | +63.8% | +68.9% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 1 | strpos() per term | 11.073 | 31.813 | +187.5% | +185.0% | +201.8% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 1 | PCRE lookahead per term | 17.822 | 31.813 | +78.2% | +72.6% | +84.4% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 3 | strpos() per term | 33.513 | 33.792 | +0.7% | -0.7% | +1.9% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 3 | PCRE lookahead per term | 52.682 | 33.792 | -35.8% | -36.2% | -34.1% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 6 | strpos() per term | 63.413 | 36.938 | -41.7% | -42.4% | -41.3% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 6 | PCRE lookahead per term | 105.109 | 36.938 | -64.9% | -65.9% | -63.6% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 1 | strpos() per term | 12.545 | 32.029 | +155.4% | +153.9% | +156.3% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 1 | preg_match() per term | 14.993 | 32.029 | +113.7% | +112.1% | +115.1% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 2 | strpos() per term | 24.814 | 33.401 | +34.8% | +33.3% | +35.7% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 2 | preg_match() per term | 30.243 | 33.401 | +10.7% | +9.5% | +11.3% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 5 | strpos() per term | 64.432 | 38.038 | -40.8% | -41.2% | -40.3% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 5 | preg_match() per term | 74.346 | 38.038 | -48.8% | -49.1% | -48.1% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 1 | strpos() per term | 15.814 | 32.413 | +105.3% | +102.7% | +108.8% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 1 | PCRE lookahead per term | 34.387 | 32.413 | -5.5% | -7.7% | -3.7% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 2 | strpos() per term | 30.244 | 34.935 | +15.5% | +14.0% | +16.3% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 2 | PCRE lookahead per term | 68.970 | 34.935 | -49.4% | -49.6% | -48.6% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 5 | strpos() per term | 78.564 | 41.144 | -47.7% | -48.1% | -47.3% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 5 | PCRE lookahead per term | 174.687 | 41.144 | -76.4% | -76.6% | -76.1% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 1 | strtr() | 29.427 | 31.780 | +8.0% | +7.7% | +8.3% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 1 | preg_replace_callback() | 9.321 | 31.780 | +241.0% | +239.6% | +242.2% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 3 | strtr() | 88.306 | 35.052 | -60.3% | -60.5% | -60.0% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 3 | preg_replace_callback() | 27.829 | 35.052 | +26.0% | +25.5% | +26.5% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 6 | strtr() | 176.186 | 39.402 | -77.6% | -77.7% | -77.6% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 6 | preg_replace_callback() | 55.618 | 39.402 | -29.1% | -29.5% | -28.9% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 1 | strtr() | 0.290 | 1.687 | +482.1% | +478.2% | +486.5% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 1 | preg_replace_callback() | 0.567 | 1.687 | +197.5% | +196.3% | +199.7% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 1 | str_replace() | 0.332 | 1.687 | +409.5% | +399.6% | +416.7% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 1.920 | 3.519 | +83.1% | +82.0% | +87.0% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 4.026 | 3.519 | -12.6% | -13.4% | -10.2% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 2.181 | 3.519 | +61.6% | +59.7% | +64.3% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 1 | strtr() | 0.227 | 1.517 | +568.1% | +560.0% | +579.7% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 1 | preg_replace_callback() | 0.320 | 1.517 | +373.5% | +367.6% | +377.0% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 1 | str_replace() | 0.270 | 1.517 | +462.4% | +455.4% | +464.2% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 8 | strtr() | 1.415 | 2.727 | +92.8% | +90.9% | +97.1% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 8 | preg_replace_callback() | 2.171 | 2.727 | +25.5% | +24.7% | +26.8% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 8 | str_replace() | 1.741 | 2.727 | +56.7% | +56.0% | +57.2% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 1 | strtr() | 5.399 | 20.479 | +279.2% | +275.5% | +280.5% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 1 | preg_replace_callback() | 0.474 | 20.479 | +4216.8% | +4170.1% | +4239.7% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 1 | str_replace() | 10.526 | 20.479 | +94.5% | +93.8% | +95.0% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 1 | preg_replace() | 0.471 | 20.479 | +4257.0% | +4181.7% | +4320.3% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 8 | strtr() | 42.909 | 65.960 | +53.8% | +52.4% | +54.9% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 8 | preg_replace_callback() | 3.508 | 65.960 | +1780.3% | +1766.4% | +1802.2% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 8 | str_replace() | 83.405 | 65.960 | -20.9% | -21.2% | -20.7% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 8 | preg_replace() | 3.324 | 65.960 | +1886.1% | +1870.0% | +1905.4% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 1 | strtr() | 67.347 | 110.836 | +64.6% | +63.7% | +65.2% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 1 | preg_replace_callback() | 4.542 | 110.836 | +2339.8% | +2328.0% | +2349.5% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 1 | str_replace() | 136.946 | 110.836 | -19.1% | -19.4% | -18.7% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 1 | preg_replace() | 4.125 | 110.836 | +2586.9% | +2572.0% | +2598.7% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 8 | strtr() | 538.011 | 791.396 | +47.1% | +46.4% | +47.5% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 8 | preg_replace_callback() | 36.342 | 791.396 | +2077.6% | +2069.3% | +2083.8% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 8 | str_replace() | 1095.765 | 791.396 | -27.8% | -27.9% | -27.6% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 8 | preg_replace() | 33.003 | 791.396 | +2297.7% | +2285.3% | +2309.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 1 | str_contains() loop | 0.299 | 2.379 | +696.6% | +686.0% | +703.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 1 | preg_match() | 0.225 | 2.379 | +957.7% | +953.0% | +963.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 44 | str_contains() loop | 11.099 | 7.815 | -29.7% | -30.1% | -27.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 44 | preg_match() | 7.515 | 7.815 | +4.0% | +3.8% | +4.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 55 | str_contains() loop | 13.394 | 9.173 | -31.5% | -31.8% | -31.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 55 | preg_match() | 9.441 | 9.173 | -2.9% | -3.3% | -2.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 1 | str_contains() loop | 0.483 | 4.990 | +933.0% | +917.8% | +939.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 1 | preg_match() | 0.333 | 4.990 | +1394.5% | +1382.0% | +1411.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 32 | str_contains() loop | 13.647 | 9.220 | -32.4% | -32.6% | -31.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 32 | preg_match() | 9.012 | 9.220 | +2.3% | +1.4% | +3.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 41 | str_contains() loop | 17.105 | 10.410 | -39.2% | -40.1% | -39.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 41 | preg_match() | 11.520 | 10.410 | -9.7% | -9.9% | -9.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 1 | str_contains() loop | 0.859 | 12.303 | +1332.7% | +1330.1% | +1337.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 1 | preg_match() | 0.724 | 12.303 | +1598.6% | +1589.4% | +1602.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 25 | str_contains() loop | 20.439 | 17.378 | -15.0% | -15.2% | -14.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 25 | preg_match() | 16.980 | 17.378 | +2.3% | +1.7% | +3.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 33 | str_contains() loop | 27.079 | 18.958 | -29.9% | -30.1% | -29.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 33 | preg_match() | 22.329 | 18.958 | -15.0% | -15.4% | -14.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 1 | str_contains() loop | 1.550 | 25.613 | +1552.0% | +1542.8% | +1560.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 1 | preg_match() | 1.513 | 25.613 | +1592.9% | +1586.3% | +1596.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 19 | str_contains() loop | 30.382 | 29.837 | -1.7% | -2.6% | -1.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 19 | preg_match() | 27.703 | 29.837 | +7.6% | +7.1% | +8.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 25 | str_contains() loop | 41.242 | 31.321 | -24.0% | -24.6% | -23.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 25 | preg_match() | 36.266 | 31.321 | -13.6% | -14.1% | -13.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 1 | str_contains() loop | 3.175 | 56.868 | +1686.1% | +1671.6% | +1723.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 1 | preg_match() | 2.850 | 56.868 | +1894.6% | +1874.3% | +1911.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 21 | str_contains() loop | 67.124 | 61.409 | -8.0% | -10.5% | -6.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 21 | preg_match() | 58.233 | 61.409 | +5.4% | +4.5% | +6.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 28 | str_contains() loop | 93.310 | 62.640 | -32.9% | -33.6% | -32.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 28 | preg_match() | 77.876 | 62.640 | -19.5% | -20.1% | -19.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 1 | str_contains() loop | 8.031 | 149.802 | +1764.1% | +1757.1% | +1793.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 1 | preg_match() | 5.971 | 149.802 | +2406.8% | +2401.5% | +2417.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 26 | str_contains() loop | 209.742 | 156.234 | -25.4% | -25.9% | -24.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 26 | preg_match() | 151.468 | 156.234 | +3.1% | +2.9% | +3.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 34 | str_contains() loop | 258.421 | 160.299 | -38.0% | -39.0% | -36.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 34 | preg_match() | 202.199 | 160.299 | -20.7% | -20.8% | -20.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 1 | str_contains() loop | 17.619 | 291.854 | +1557.0% | +1554.9% | +1563.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 1 | preg_match() | 20.196 | 291.854 | +1345.4% | +1340.5% | +1355.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 17 | str_contains() loop | 301.159 | 296.199 | -1.6% | -3.9% | -1.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 17 | preg_match() | 314.441 | 296.199 | -5.8% | -6.0% | -5.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 23 | str_contains() loop | 406.932 | 296.971 | -27.0% | -27.2% | -26.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 23 | preg_match() | 473.313 | 296.971 | -37.3% | -37.4% | -37.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 1 | strpos() per term | 1.184 | 3.078 | +159.8% | +158.8% | +160.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 1 | preg_match() per term | 1.475 | 3.078 | +108.8% | +107.2% | +110.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 9.149 | 9.473 | +3.5% | +3.0% | +3.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | preg_match() per term | 11.348 | 9.473 | -16.5% | -17.0% | -16.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 12 | strpos() per term | 13.659 | 13.010 | -4.7% | -5.3% | -4.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 12 | preg_match() per term | 17.009 | 13.010 | -23.6% | -24.4% | -23.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 1 | strpos() per term | 2.195 | 4.885 | +122.8% | +121.8% | +123.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 1 | preg_match() per term | 2.720 | 4.885 | +79.7% | +78.4% | +81.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 3 | strpos() per term | 6.624 | 7.062 | +6.7% | +6.1% | +7.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 3 | preg_match() per term | 8.040 | 7.062 | -12.2% | -12.8% | -11.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 6 | strpos() per term | 12.990 | 10.257 | -21.0% | -21.8% | -20.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 6 | preg_match() per term | 15.935 | 10.257 | -35.7% | -36.2% | -35.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 1 | strpos() per term | 4.098 | 8.900 | +117.1% | +116.2% | +118.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 1 | preg_match() per term | 5.279 | 8.900 | +68.7% | +67.9% | +69.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 2 | strpos() per term | 7.907 | 10.109 | +28.0% | +23.1% | +28.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 2 | preg_match() per term | 10.517 | 10.109 | -3.8% | -4.6% | -2.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 5 | strpos() per term | 19.700 | 13.764 | -30.1% | -30.5% | -29.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 5 | preg_match() per term | 26.210 | 13.764 | -47.6% | -48.0% | -47.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 1 | strpos() per term | 8.188 | 19.078 | +133.1% | +132.1% | +135.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 1 | preg_match() per term | 9.897 | 19.078 | +92.9% | +92.6% | +94.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 2 | strpos() per term | 16.407 | 20.508 | +25.0% | +24.3% | +25.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 2 | preg_match() per term | 19.742 | 20.508 | +3.9% | +3.0% | +4.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 5 | strpos() per term | 42.268 | 24.333 | -42.4% | -42.8% | -41.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 5 | preg_match() per term | 49.415 | 24.333 | -50.7% | -51.0% | -50.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 1 | strpos() per term | 16.315 | 45.707 | +180.8% | +177.4% | +182.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 1 | preg_match() per term | 18.934 | 45.707 | +141.3% | +137.9% | +142.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 3 | strpos() per term | 50.395 | 48.770 | -3.1% | -4.2% | -2.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 3 | preg_match() per term | 56.837 | 48.770 | -14.3% | -15.0% | -13.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 6 | strpos() per term | 98.356 | 54.717 | -44.4% | -45.0% | -43.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 6 | preg_match() per term | 116.463 | 54.717 | -53.1% | -53.5% | -52.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 1 | strpos() per term | 32.381 | 129.388 | +299.4% | +296.7% | +301.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 1 | preg_match() per term | 39.198 | 129.388 | +230.0% | +227.1% | +233.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 4 | strpos() per term | 129.420 | 135.522 | +4.8% | +4.1% | +5.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 4 | preg_match() per term | 153.504 | 135.522 | -11.7% | -12.2% | -10.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 7 | strpos() per term | 230.435 | 142.440 | -38.2% | -38.5% | -38.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 7 | preg_match() per term | 270.508 | 142.440 | -47.4% | -47.6% | -47.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 1 | strpos() per term | 62.480 | 346.442 | +454.7% | +453.2% | +455.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 1 | preg_match() per term | 92.071 | 346.442 | +276.4% | +275.1% | +277.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 5 | strpos() per term | 312.423 | 356.050 | +14.0% | +13.7% | +14.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 5 | preg_match() per term | 461.583 | 356.050 | -22.8% | -23.2% | -22.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 9 | strpos() per term | 560.511 | 365.316 | -34.9% | -35.0% | -34.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 9 | preg_match() per term | 839.438 | 365.316 | -56.5% | -56.6% | -56.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 1 | strtr() | 4.380 | 3.531 | -19.4% | -21.5% | -18.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 1 | preg_replace_callback() | 0.717 | 3.531 | +392.3% | +390.4% | +394.6% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 34.578 | 10.751 | -68.9% | -69.4% | -68.4% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 5.207 | 10.751 | +106.4% | +105.8% | +107.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 1 | strtr() | 7.844 | 6.023 | -23.2% | -23.7% | -22.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 1 | preg_replace_callback() | 2.008 | 6.023 | +200.0% | +198.5% | +201.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 5 | strtr() | 39.343 | 10.528 | -73.3% | -73.4% | -73.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 5 | preg_replace_callback() | 9.762 | 10.528 | +7.9% | +7.4% | +8.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 9 | strtr() | 70.424 | 15.103 | -78.5% | -78.7% | -78.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 9 | preg_replace_callback() | 17.360 | 15.103 | -12.8% | -13.9% | -11.4% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 1 | strtr() | 16.722 | 10.152 | -39.5% | -39.8% | -39.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 1 | preg_replace_callback() | 3.829 | 10.152 | +165.1% | +163.6% | +166.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 3 | strtr() | 50.017 | 12.770 | -74.5% | -74.7% | -74.4% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 3 | preg_replace_callback() | 11.383 | 12.770 | +12.2% | +11.5% | +12.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 6 | strtr() | 101.215 | 16.506 | -83.7% | -83.8% | -83.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 6 | preg_replace_callback() | 22.623 | 16.506 | -27.1% | -27.2% | -26.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 1 | strtr() | 31.268 | 19.537 | -37.5% | -37.7% | -37.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 1 | preg_replace_callback() | 6.919 | 19.537 | +182.3% | +181.5% | +183.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 3 | strtr() | 94.105 | 22.431 | -76.2% | -76.2% | -76.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 3 | preg_replace_callback() | 20.648 | 22.431 | +8.6% | +8.3% | +9.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 6 | strtr() | 187.646 | 26.458 | -85.9% | -86.0% | -85.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 6 | preg_replace_callback() | 41.117 | 26.458 | -35.6% | -35.8% | -35.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 1 | strtr() | 38.470 | 45.320 | +17.8% | +16.8% | +18.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 1 | preg_replace_callback() | 11.907 | 45.320 | +280.4% | +277.6% | +284.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 4 | strtr() | 153.706 | 50.446 | -67.2% | -67.5% | -66.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 4 | preg_replace_callback() | 47.355 | 50.446 | +6.6% | +5.8% | +8.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 7 | strtr() | 268.592 | 55.117 | -79.5% | -79.6% | -79.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 7 | preg_replace_callback() | 82.716 | 55.117 | -33.3% | -33.8% | -32.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 1 | strtr() | 42.190 | 111.387 | +164.1% | +162.9% | +165.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 1 | preg_replace_callback() | 22.276 | 111.387 | +400.1% | +398.0% | +402.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 5 | strtr() | 210.593 | 120.775 | -42.7% | -43.0% | -42.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 5 | preg_replace_callback() | 111.209 | 120.775 | +8.7% | +8.0% | +9.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 9 | strtr() | 378.159 | 129.422 | -65.7% | -66.1% | -65.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 9 | preg_replace_callback() | 225.704 | 129.422 | -42.7% | -43.0% | -42.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 1 | strtr() | 43.001 | 288.476 | +570.9% | +569.1% | +572.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 1 | preg_replace_callback() | 66.477 | 288.476 | +334.1% | +333.1% | +335.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 6 | strtr() | 257.465 | 299.788 | +16.5% | +16.2% | +17.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 6 | preg_replace_callback() | 396.423 | 299.788 | -24.3% | -24.7% | -23.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 10 | strtr() | 429.508 | 309.722 | -27.9% | -28.1% | -27.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 10 | preg_replace_callback() | 644.540 | 309.722 | -51.9% | -52.2% | -51.8% |
