# Complete elapsed-time comparisons

Unit: µs per complete job. Lower is better. Δ is the median of paired per-pass changes; min/max are paired changes, not confidence intervals.

All measured alternatives are listed. Preparation and reuse are separate sections. Natural API result representations are retained; see [method](METHOD.md).

A dagger marks an original sample span above 10%; the [complete-case confirmation](CONFIRMATION.md) preserves both measurements.

## Everyday cases

### Product tasks

#### Dictionary preparation included

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.346 | 7.080 | +1945.3% | +1918.9% | +1957.6% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.269 | 7.080 | +457.7% | +452.7% | +459.7% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.282 | 6.896 | +2344.1% | +2319.3% | +2373.4% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.171 | 6.896 | +488.8% | +487.0% | +495.1% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.317 | 7.152 | +2156.8% | +2134.7% | +2202.3% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.331 | 7.152 | +437.5% | +435.9% | +443.2% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.289 | 7.172 | +2379.5% | +2316.7% | +2408.1% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.339 | 7.172 | +436.9% | +431.9% | +441.9% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.057 | 8.563 | +710.2% | +697.5% | +722.1% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2.179 | 8.563 | +293.2% | +286.3% | +298.5% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.599 | 7.518 | +1156.4% | +1147.0% | +1165.2% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.545 | 7.518 | +386.6% | +383.9% | +390.1% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.284 | 20.675 | +1510.2% | +1496.6% | +1514.0% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.694 | 20.675 | +1120.3% | +1112.8% | +1123.9% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.462 | 20.725 | +1317.6% | +1313.9% | +1321.7% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.348 | 20.725 | +1437.6% | +1433.4% | +1442.1% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 2.104 | 20.781 | +887.8% | +878.2% | +895.4% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.886 | 20.781 | +1002.6% | +995.2% | +1007.5% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.459 | 20.896 | +1331.9% | +1327.3% | +1337.5% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.925 | 20.896 | +985.2% | +976.4% | +988.5% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 3.613 | 23.086 | +538.3% | +537.1% | +540.6% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5.212 | 23.086 | +342.8% | +340.9% | +345.0% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 2.018 | 21.485 | +964.6% | +961.4% | +966.7% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2.790 | 21.485 | +670.2% | +666.9% | +672.8% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.355 | 17.398 | +4806.1% | +4778.2% | +4918.5% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.296 | 17.398 | +1242.3% | +1234.6% | +1252.2% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.297 | 17.389 | +5746.7% | +5670.5% | +5800.5% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.160 | 17.389 | +1398.9% | +1394.0% | +1406.5% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.383 | 17.509 | +4469.9% | +4442.9% | +4496.2% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.346 | 17.509 | +1201.1% | +1194.4% | +1204.4% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.325 | 17.476 | +5273.4% | +5199.6% | +5309.9% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.367 | 17.476 | +1177.6% | +1172.6% | +1182.3% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.588 | 19.032 | +1099.8% | +1089.3% | +1105.0% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2.674 | 19.032 | +612.1% | +609.7% | +614.7% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.946 | 18.078 | +1811.4% | +1790.7% | +1851.0% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.668 | 18.078 | +985.2% | +977.9% | +997.5% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 4.250 | 11.934 | +180.3% | +178.1% | +182.0% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 3.473 | 11.934 | +243.3% | +240.9% | +244.6% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 2.139 | 6.228 | +191.1% | +190.0% | +194.2% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 0.919 | 6.228 | +577.1% | +571.3% | +587.6% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 2.395 | 9.200 | +283.7% | +282.3% | +286.6% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 2.149 | 9.200 | +327.8% | +325.8% | +331.1% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 2.612 | 11.828 | +352.8% | +349.5% | +354.5% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 3.204 | 11.828 | +268.8% | +265.8% | +270.5% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | strtr() | 0.968 | 6.891 | +612.6% | +608.4% | +617.5% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | preg_replace_callback() | 4.108 | 6.891 | +67.7% | +67.0% | +71.8% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | str_replace() | 3.160 | 6.891 | +118.3% | +117.4% | +121.5% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | strtr() | 1.407 | 7.808 | +453.8% | +450.6% | +456.8% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | preg_replace_callback() | 5.187 | 7.808 | +50.5% | +49.8% | +52.2% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | str_replace() | 4.020 | 7.808 | +94.4% | +93.4% | +97.0% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 0.337 | 2.517 | +646.2% | +643.3% | +651.7% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 1.831 | 2.517 | +37.5% | +36.9% | +38.1% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 1.295 | 2.517 | +94.2% | +93.5% | +95.3% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 2.083 | 6.553 | +214.2% | +212.6% | +216.4% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 4.503 | 6.553 | +45.6% | +45.0% | +46.4% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 2.761 | 6.553 | +137.4% | +136.6% | +138.1% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 0.203 | 0.912 | +349.6% | +346.3% | +351.6% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 1.141 | 0.912 | -20.1% | -20.3% | -19.7% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 1.016 | 0.912 | -10.3% | -10.8% | -9.9% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 0.302 | 1.119 | +270.9% | +266.3% | +278.1% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 1.542 | 1.119 | -27.5% | -27.7% | -27.1% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 1.162 | 1.119 | -3.8% | -5.4% | -3.0% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | strtr() | 0.208 | 0.537 | +157.9% | +156.8% | +158.8% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace_callback() | 1.148 | 0.537 | -53.2% | -53.5% | -52.8% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | str_replace() | 0.840 | 0.537 | -36.1% | -36.5% | -35.8% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace() | 0.900 | 0.537 | -40.4% | -41.1% | -40.0% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 0.345 | 9.397 | +2627.5% | +2604.6% | +2645.8% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 2.339 | 9.397 | +302.2% | +299.3% | +305.9% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 1.450 | 9.397 | +549.2% | +540.6% | +554.9% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 0.425 | 10.065 | +2271.0% | +2259.6% | +2280.1% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 2.537 | 10.065 | +296.8% | +295.4% | +301.2% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 1.578 | 10.065 | +537.2% | +527.9% | +539.5% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 2.846 | 13.258 | +365.7% | +364.2% | +367.9% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 4.644 | 13.258 | +185.7% | +184.5% | +187.8% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 3.589 | 13.258 | +269.2% | +267.6% | +273.8% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 5.950 | 41.759 | +601.8% | +599.0% | +603.5% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 7.116 | 41.759 | +487.0% | +481.2% | +497.5% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 16.153 | 41.759 | +158.5% | +156.9% | +160.3% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 7.012 | 41.759 | +495.5% | +488.0% | +505.1% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 6.102 | 43.400 | +611.0% | +608.3% | +613.5% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 7.136 | 43.400 | +507.1% | +505.6% | +513.8% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 17.246 | 43.400 | +151.8% | +139.9% | +162.5% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 6.907 | 43.400 | +528.4% | +523.2% | +533.9% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 9.214 | 51.543 | +459.5% | +458.1% | +460.2% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 7.644 | 51.543 | +574.0% | +572.2% | +580.4% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 24.168 | 51.543 | +113.3% | +112.8% | +114.6% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 7.242 | 51.543 | +611.5% | +608.8% | +619.2% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 72.800 | 199.191 | +173.5% | +172.1% | +174.4% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 11.046 | 199.191 | +1702.5% | +1697.6% | +1708.8% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 151.358 | 199.191 | +31.5% | +30.8% | +32.1% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 10.546 | 199.191 | +1787.8% | +1776.4% | +1799.9% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 0.197 | 0.868 | +341.3% | +339.5% | +343.8% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 2.037 | 0.868 | -57.4% | -58.0% | -56.3% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 1.793 | 0.868 | -51.5% | -52.3% | -49.9% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 0.234 | 0.937 | +300.7% | +298.9% | +305.6% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 2.219 | 0.937 | -57.8% | -57.9% | -57.5% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 1.877 | 0.937 | -50.1% | -50.4% | -49.7% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 12.146 | 32.607 | +168.5% | +167.5% | +170.0% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | preg_match() per term | 22.083 | 32.607 | +47.6% | +46.9% | +48.3% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 10.185 | 31.370 | +207.8% | +203.8% | +209.8% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 31.776 | 31.370 | -1.2% | -2.9% | -0.4% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 14.928 | 32.595 | +118.2% | +116.7% | +119.9% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 47.644 | 32.595 | -31.7% | -31.8% | -31.2% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 29.479 | 35.888 | +21.8% | +21.3% | +22.3% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 34.951 | 35.888 | +2.7% | +1.8% | +3.7% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 234.858 | 48.320 | -79.4% | -79.5% | -79.4% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 98.512 | 48.320 | -51.0% | -51.2% | -50.7% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.367 | 6.519 | +1674.1% | +1650.9% | +1726.7% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.331 | 6.519 | +389.7% | +383.2% | +397.0% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.285 | 6.391 | +2140.8% | +2129.9% | +2151.5% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.267 | 6.391 | +404.4% | +398.4% | +423.0% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.310 | 6.708 | +2060.0% | +2014.8% | +2085.6% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.414 | 6.708 | +373.6% | +362.5% | +381.7% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.286 | 6.692 | +2236.1% | +2196.2% | +2302.3% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.402 | 6.692 | +378.0% | +370.5% | +380.4% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.087 | 8.323 | +665.7% | +662.4% | +671.9% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2.455 | 8.323 | +239.2% | +236.7% | +243.7% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.598 | 7.127 | +1091.3% | +1086.5% | +1099.4% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.655 | 7.127 | +330.8% | +326.2% | +333.6% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.331 | 19.801 | +1386.6% | +1382.0% | +1392.2% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.677 | 19.801 | +1079.8% | +1074.7% | +1086.6% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.474 | 19.612 | +1230.1% | +1226.7% | +1235.7% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.304 | 19.612 | +1404.3% | +1396.9% | +1410.8% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 2.138 | 19.801 | +825.8% | +824.2% | +827.2% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.888 | 19.801 | +948.5% | +945.4% | +963.1% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.479 | 19.986 | +1251.7% | +1245.1% | +1256.0% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.899 | 19.986 | +951.7% | +945.5% | +961.8% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 3.408 | 22.393 | +556.8% | +554.7% | +560.0% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5.246 | 22.393 | +326.7% | +325.5% | +328.6% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.929 | 20.636 | +969.8% | +965.9% | +972.3% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2.799 | 20.636 | +638.6% | +634.9% | +642.7% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.367 | 16.418 | +4369.0% | +4353.7% | +4383.4% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.326 | 16.418 | +1139.0% | +1134.3% | +1153.9% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.299 | 16.205 | +5311.1% | +5278.4% | +5340.5% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.189 | 16.205 | +1264.4% | +1257.3% | +1281.4% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.387 | 16.436 | +4142.7% | +4096.8% | +4187.4% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.384 | 16.436 | +1087.5% | +1071.4% | +1092.9% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.323 | 16.425 | +4981.2% | +4906.2% | +4991.5% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.383 | 16.425 | +1087.3% | +1083.2% | +1108.9% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.614 | 17.978 | +1013.5% | +1008.4% | +1017.1% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2.764 | 17.978 | +550.3% | +548.3% | +555.4% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.933 | 16.975 | +1719.9% | +1714.4% | +1725.9% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.725 | 16.975 | +884.7% | +879.2% | +893.1% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 3.949 | 12.073 | +205.7% | +203.0% | +207.0% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 3.274 | 12.073 | +268.7% | +265.5% | +280.7% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 1.981 | 5.894 | +197.1% | +196.0% | +200.4% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 0.867 | 5.894 | +579.5% | +575.1% | +589.1% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 2.213 | 9.155 | +313.3% | +311.0% | +317.0% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 2.054 | 9.155 | +344.7% | +342.5% | +347.4% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 2.411 | 12.015 | +398.2% | +394.2% | +400.8% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 3.116 | 12.015 | +286.0% | +282.7% | +287.1% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | strtr() | 0.867 | 6.624 | +662.8% | +656.0% | +669.4% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | preg_replace_callback() | 4.133 | 6.624 | +60.2% | +59.1% | +60.9% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | str_replace() | 3.039 | 6.624 | +118.0% | +116.8% | +118.8% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | strtr() | 1.286 | 7.669 | +496.5% | +491.0% | +501.7% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | preg_replace_callback() | 5.278 | 7.669 | +45.3% | +44.5% | +46.5% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | str_replace() | 3.915 | 7.669 | +95.8% | +95.2% | +96.6% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 0.298 | 2.449 | +721.3% | +718.3% | +728.5% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 1.855 | 2.449 | +31.7% | +30.3% | +33.0% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 1.308 | 2.449 | +87.3% | +85.8% | +88.5% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 1.907 | 6.661 | +249.3% | +246.5% | +250.5% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 4.538 | 6.661 | +46.8% | +45.6% | +47.9% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 2.684 | 6.661 | +148.2% | +147.1% | +149.6% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 0.171 | 0.885 | +416.1% | +414.2% | +423.7% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 1.074 | 0.885 | -17.6% | -18.1% | -17.3% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 0.970 | 0.885 | -8.7% | -9.1% | -8.0% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 0.268 | 1.086 | +304.9% | +302.1% | +309.0% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 1.519 | 1.086 | -28.6% | -29.1% | -27.8% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 1.137 | 1.086 | -4.5% | -5.0% | -3.9% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | strtr() | 0.196 | 0.528 | +169.0% | +165.1% | +171.0% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace_callback() | 1.071 | 0.528 | -50.7% | -51.1% | -50.5% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | str_replace() | 0.795 | 0.528 | -33.6% | -34.2% | -33.1% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace() | 0.853 | 0.528 | -38.1% | -38.4% | -37.6% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 0.312 | 9.009 | +2787.1% | +2718.3% | +2806.9% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 2.535 | 9.009 | +255.4% | +250.5% | +260.0% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 1.444 | 9.009 | +523.8% | +520.1% | +534.8% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 0.398 | 9.585 | +2310.9% | +2297.7% | +2317.5% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 2.784 | 9.585 | +244.2% | +235.3% | +246.0% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 1.583 | 9.585 | +505.9% | +502.7% | +508.5% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 2.685 | 12.870 | +378.8% | +376.7% | +392.7% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 4.967 | 12.870 | +159.4% | +158.0% | +168.2% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 3.593 | 12.870 | +258.3% | +256.6% | +267.8% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 5.377 | 42.308 | +686.1% | +681.9% | +689.0% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 6.207 | 42.308 | +581.5% | +579.1% | +590.9% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 15.087 | 42.308 | +180.6% | +179.5% | +182.5% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 6.078 | 42.308 | +596.2% | +593.4% | +604.6% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 5.548 | 43.120 | +675.8% | +666.5% | +679.0% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 6.422 | 43.120 | +571.0% | +568.4% | +572.4% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 15.789 | 43.120 | +173.0% | +171.8% | +174.2% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 6.193 | 43.120 | +595.4% | +592.4% | +598.8% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 8.367 | 51.548 | +515.9% | +509.4% | +517.2% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 6.861 | 51.548 | +651.1% | +649.2% | +652.9% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 22.793 | 51.548 | +126.2% | +124.5% | +127.0% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 6.441 | 51.548 | +699.7% | +695.4% | +701.8% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 66.151 | 209.258 | +216.3% | +211.5% | +216.9% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 10.155 | 209.258 | +1960.6% | +1942.0% | +1975.0% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 141.341 | 209.258 | +48.0% | +46.5% | +48.4% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 9.652 | 209.258 | +2068.5% | +2050.9% | +2078.4% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 0.163 | 0.834 | +410.9% | +407.9% | +412.5% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 2.031 | 0.834 | -58.9% | -59.3% | -58.8% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 1.779 | 0.834 | -53.1% | -53.7% | -52.4% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 0.202 | 0.908 | +349.3% | +347.5% | +351.7% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 2.225 | 0.908 | -59.2% | -59.4% | -58.8% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 1.831 | 0.908 | -50.4% | -51.0% | -50.3% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 12.385 | 30.973 | +150.1% | +148.5% | +151.4% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | preg_match() per term | 21.668 | 30.973 | +43.0% | +42.5% | +44.1% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 11.006 | 30.085 | +173.4% | +171.9% | +174.9% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 28.581 | 30.085 | +5.2% | +0.8% | +7.2% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 15.169 | 31.418 | +107.3% | +105.4% | +109.4% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 46.218 | 31.418 | -32.1% | -32.2% | -31.8% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 29.459 | 34.521 | +17.2% | +16.5% | +17.8% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 34.711 | 34.521 | -0.5% | -1.0% | +0.7% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 234.868 | 46.583 | -80.2% | -80.2% | -80.1% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 98.878 | 46.583 | -52.9% | -53.1% | -52.8% |

#### Dictionary already prepared

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.347 | 0.265 | -23.5% | -24.5% | -22.1% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.256 | 0.265 | +3.5% | +3.2% | +3.9% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.279 | 0.161 | -42.3% | -42.5% | -41.9% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.172 | 0.161 | -6.0% | -6.1% | -5.5% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.314 | 0.401 | +27.9% | +27.3% | +29.9% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.314 | 0.401 | +27.7% | +27.6% | +28.5% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.284 | 0.438 | +54.0% | +51.5% | +54.6% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.325 | 0.438 | +34.8% | +34.3% | +35.4% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.057 | 1.821 | +72.2% | +71.2% | +72.8% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.184 | 1.821 | +53.5% | +52.6% | +55.0% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.602 | 0.809 | +34.3% | +32.9% | +34.8% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.545 | 0.809 | +48.5% | +47.9% | +49.4% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.304 | 0.397 | -69.5% | -69.7% | -69.4% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.535 | 0.397 | -25.9% | -26.1% | -25.6% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.460 | 0.201 | -86.2% | -86.3% | -86.2% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.181 | 0.201 | +10.8% | +10.1% | +11.9% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 2.111 | 0.624 | -70.5% | -70.7% | -70.4% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.725 | 0.624 | -14.1% | -14.5% | -13.7% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.438 | 0.634 | -55.9% | -56.2% | -55.7% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.742 | 0.634 | -14.5% | -14.9% | -14.1% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 3.594 | 2.939 | -18.3% | -19.4% | -18.1% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 4.014 | 2.939 | -26.8% | -27.4% | -26.6% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 2.013 | 1.244 | -38.4% | -39.0% | -38.1% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.623 | 1.244 | -23.3% | -24.1% | -23.3% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.358 | 0.245 | -31.5% | -31.8% | -31.4% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.291 | 0.245 | -15.7% | -16.2% | -15.3% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.298 | 0.153 | -48.7% | -49.1% | -47.9% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.167 | 0.153 | -8.4% | -9.1% | -7.8% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.378 | 0.380 | +0.6% | -0.4% | +1.2% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.328 | 0.380 | +15.7% | +14.9% | +17.1% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.329 | 0.380 | +15.4% | +12.6% | +16.2% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.349 | 0.380 | +8.8% | +8.0% | +9.4% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.582 | 1.708 | +8.0% | +7.2% | +8.9% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.674 | 1.708 | +2.0% | +1.5% | +2.5% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.926 | 0.791 | -14.6% | -15.1% | -14.1% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.653 | 0.791 | +21.1% | +20.5% | +21.5% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 4.253 | 6.059 | +42.4% | +40.4% | +42.9% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 2.713 | 6.059 | +123.1% | +121.4% | +123.9% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 2.138 | 0.423 | -80.2% | -80.4% | -80.1% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 0.250 | 0.423 | +68.8% | +67.7% | +70.1% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 2.386 | 3.406 | +42.6% | +40.7% | +43.2% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 1.453 | 3.406 | +134.3% | +132.7% | +135.2% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 2.601 | 6.013 | +131.0% | +127.3% | +131.6% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 2.504 | 6.013 | +139.5% | +137.5% | +140.7% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 0.338 | 0.660 | +95.4% | +94.0% | +96.1% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 0.484 | 0.660 | +36.3% | +35.9% | +36.8% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 0.303 | 0.660 | +117.8% | +116.8% | +118.5% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 2.078 | 4.639 | +123.5% | +121.7% | +125.6% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 3.106 | 4.639 | +49.4% | +47.4% | +50.0% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 1.739 | 4.639 | +166.9% | +164.8% | +169.5% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 0.198 | 0.323 | +62.7% | +61.9% | +63.1% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 0.167 | 0.323 | +93.1% | +91.3% | +94.0% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 0.188 | 0.323 | +72.0% | +71.3% | +72.2% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 0.292 | 0.532 | +82.6% | +80.7% | +84.1% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 0.553 | 0.532 | -3.8% | -4.8% | -3.5% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 0.330 | 0.532 | +61.3% | +60.5% | +62.2% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | strtr() | 0.212 | 0.270 | +27.4% | +26.9% | +29.0% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace_callback() | 0.371 | 0.270 | -27.1% | -27.6% | -26.5% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | str_replace() | 0.219 | 0.270 | +23.5% | +23.1% | +25.3% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace() | 0.207 | 0.270 | +30.9% | +30.3% | +32.6% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 0.347 | 0.330 | -4.8% | -5.2% | -4.5% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 0.193 | 0.330 | +71.4% | +70.4% | +72.1% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 0.250 | 0.330 | +32.3% | +32.1% | +33.0% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 0.427 | 0.574 | +34.3% | +34.0% | +34.8% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 0.384 | 0.574 | +48.9% | +47.7% | +49.7% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 0.375 | 0.574 | +52.7% | +52.1% | +53.6% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 2.826 | 3.982 | +40.9% | +40.4% | +41.4% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 2.433 | 3.982 | +63.8% | +63.1% | +64.3% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 2.329 | 3.982 | +70.7% | +70.0% | +71.9% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 5.924 | 12.331 | +108.0% | +106.9% | +108.6% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 0.491 | 12.331 | +2411.7% | +2403.7% | +2428.4% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 11.279 | 12.331 | +9.4% | +8.7% | +9.6% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 0.467 | 12.331 | +2537.4% | +2522.1% | +2552.8% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 6.093 | 13.962 | +128.8% | +128.1% | +129.7% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 0.728 | 13.962 | +1816.9% | +1808.0% | +1822.6% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 11.988 | 13.962 | +16.4% | +15.7% | +16.8% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 0.582 | 13.962 | +2303.8% | +2285.3% | +2314.3% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 9.172 | 21.963 | +139.3% | +138.5% | +139.9% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 1.147 | 21.963 | +1811.7% | +1808.0% | +1819.8% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 19.537 | 21.963 | +12.2% | +11.7% | +12.5% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 0.818 | 21.963 | +2580.8% | +2565.6% | +2587.7% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 73.932 | 169.749 | +129.6% | +128.7% | +129.9% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 4.531 | 169.749 | +3644.4% | +3628.3% | +3650.3% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 146.805 | 169.749 | +15.7% | +14.9% | +15.9% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 4.114 | 169.749 | +4024.9% | +3999.2% | +4037.5% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 0.190 | 0.255 | +33.9% | +32.8% | +34.3% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 0.185 | 0.255 | +38.3% | +37.5% | +40.2% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 0.225 | 0.255 | +13.3% | +12.8% | +13.9% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 0.235 | 0.329 | +39.6% | +39.4% | +40.4% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 0.326 | 0.329 | +1.0% | +0.2% | +1.5% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 0.274 | 0.329 | +20.1% | +19.4% | +21.1% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 12.238 | 1.797 | -85.3% | -85.4% | -85.2% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | preg_match() per term | 14.855 | 1.797 | -87.9% | -87.9% | -87.9% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 10.233 | 1.253 | -87.7% | -87.9% | -87.6% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 17.292 | 1.253 | -92.7% | -93.0% | -92.6% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 14.947 | 2.152 | -85.6% | -85.7% | -85.5% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 34.247 | 2.152 | -93.7% | -93.8% | -93.7% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 29.439 | 1.725 | -94.1% | -94.2% | -94.1% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 9.131 | 1.725 | -81.1% | -81.1% | -81.1% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 234.649 | 13.030 | -94.4% | -94.5% | -94.4% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 71.824 | 13.030 | -81.9% | -81.9% | -81.8% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.362 | 0.273 | -24.2% | -24.6% | -22.1% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.253 | 0.273 | +8.0% | +6.2% | +10.4% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.282 | 0.156 | -44.7% | -45.2% | -44.3% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.155 | 0.156 | +0.4% | -2.7% | +1.3% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.310 | 0.419 | +35.1% | +33.9% | +36.4% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.310 | 0.419 | +34.9% | +33.3% | +36.0% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.287 | 0.458 | +60.2% | +59.0% | +61.2% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.322 | 0.458 | +42.1% | +38.3% | +45.2% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.086 | 1.979 | +82.2% | +81.3% | +82.7% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.392 | 1.979 | +41.7% | +40.4% | +43.5% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.597 | 0.862 | +44.3% | +43.0% | +45.1% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.564 | 0.862 | +52.9% | +51.5% | +54.3% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.318 | 0.414 | -68.6% | -68.8% | -68.4% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.525 | 0.414 | -21.1% | -21.5% | -20.9% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.470 | 0.197 | -86.6% | -86.6% | -86.5% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.160 | 0.197 | +23.7% | +22.1% | +25.1% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 2.134 | 0.660 | -69.1% | -69.3% | -69.0% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.723 | 0.660 | -8.8% | -9.9% | -8.4% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.480 | 0.674 | -54.5% | -54.9% | -54.2% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.731 | 0.674 | -7.8% | -8.5% | -7.2% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 3.391 | 3.202 | -5.6% | -6.6% | -5.3% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 4.079 | 3.202 | -21.6% | -22.2% | -21.4% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.921 | 1.340 | -30.2% | -31.0% | -30.0% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.630 | 1.340 | -17.9% | -18.3% | -17.4% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.384 | 0.253 | -33.9% | -34.4% | -32.5% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.283 | 0.253 | -10.5% | -11.4% | -9.9% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.297 | 0.150 | -49.4% | -49.9% | -47.8% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.156 | 0.150 | -3.2% | -5.1% | -0.7% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.383 | 0.399 | +4.3% | +3.1% | +4.7% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.328 | 0.399 | +21.8% | +19.1% | +24.0% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.327 | 0.396 | +21.2% | +20.3% | +22.0% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.343 | 0.396 | +15.4% | +13.7% | +17.9% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.612 | 1.857 | +15.2% | +14.3% | +15.8% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.726 | 1.857 | +7.6% | +6.8% | +9.0% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.954 | 0.845 | -11.5% | -12.2% | -11.2% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.687 | 0.845 | +23.0% | +21.4% | +27.0% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 3.947 | 6.619 | +67.5% | +65.2% | +68.2% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 2.586 | 6.619 | +155.7% | +153.2% | +158.9% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 1.971 | 0.440 | -77.7% | -77.9% | -77.5% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 0.227 | 0.440 | +93.7% | +92.5% | +94.7% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 2.205 | 3.720 | +68.4% | +66.0% | +69.1% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 1.405 | 3.720 | +164.7% | +162.3% | +165.6% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 2.402 | 6.577 | +173.4% | +169.8% | +175.1% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 2.471 | 6.577 | +166.2% | +163.8% | +171.5% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 0.297 | 0.681 | +129.1% | +128.0% | +129.9% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 0.492 | 0.681 | +38.7% | +37.7% | +39.6% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 0.286 | 0.681 | +138.2% | +136.5% | +139.0% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 1.893 | 4.864 | +157.0% | +154.2% | +158.6% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 3.306 | 4.864 | +47.2% | +45.6% | +47.8% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 1.683 | 4.864 | +188.9% | +187.6% | +193.5% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 0.170 | 0.352 | +107.0% | +99.6% | +109.8% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 0.161 | 0.352 | +118.2% | +116.3% | +120.5% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 0.174 | 0.352 | +101.7% | +99.1% | +103.5% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 0.269 | 0.551 | +104.1% | +100.5% | +106.0% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 0.557 | 0.551 | -1.3% | -2.3% | -0.8% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 0.320 | 0.551 | +71.7% | +70.4% | +72.8% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | strtr() | 0.187 | 0.265 | +41.7% | +40.8% | +42.4% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace_callback() | 0.368 | 0.265 | -28.1% | -28.5% | -27.5% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | str_replace() | 0.204 | 0.265 | +30.1% | +29.0% | +31.4% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace() | 0.198 | 0.265 | +33.9% | +32.7% | +34.4% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 0.312 | 0.357 | +14.6% | +14.1% | +15.5% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 0.184 | 0.357 | +94.7% | +93.8% | +99.1% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 0.243 | 0.357 | +47.0% | +46.3% | +48.1% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 0.402 | 0.606 | +50.9% | +49.9% | +51.7% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 0.399 | 0.606 | +51.9% | +50.9% | +52.7% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 0.373 | 0.606 | +62.6% | +61.2% | +64.2% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 2.691 | 4.286 | +59.4% | +58.7% | +59.9% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 2.539 | 4.286 | +68.9% | +67.8% | +69.5% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 2.332 | 4.286 | +83.7% | +82.7% | +84.8% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 5.379 | 14.359 | +166.8% | +165.2% | +167.6% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 0.480 | 14.359 | +2887.9% | +2855.0% | +2908.7% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 10.436 | 14.359 | +37.4% | +36.2% | +38.2% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 0.451 | 14.359 | +3084.7% | +3047.8% | +3100.2% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 5.551 | 15.143 | +172.7% | +171.7% | +173.2% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 0.718 | 15.143 | +2007.1% | +1998.2% | +2020.1% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 11.113 | 15.143 | +36.3% | +35.1% | +36.6% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 0.577 | 15.143 | +2522.6% | +2514.0% | +2541.9% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 8.368 | 23.277 | +177.9% | +175.8% | +178.5% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 1.161 | 23.277 | +1903.1% | +1893.4% | +1909.9% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 18.132 | 23.277 | +28.2% | +27.4% | +28.6% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 0.811 | 23.277 | +2767.0% | +2745.8% | +2781.5% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 67.274 | 180.669 | +168.5% | +167.4% | +168.8% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 4.581 | 180.669 | +3842.7% | +3825.1% | +3851.6% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 136.570 | 180.669 | +32.3% | +31.0% | +32.6% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 4.179 | 180.669 | +4222.0% | +4194.8% | +4236.2% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 0.163 | 0.271 | +66.2% | +63.0% | +67.0% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 0.179 | 0.271 | +51.7% | +49.6% | +54.9% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 0.205 | 0.271 | +32.4% | +29.2% | +33.1% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 0.202 | 0.333 | +64.7% | +62.6% | +70.2% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 0.318 | 0.333 | +4.5% | +3.4% | +7.9% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 0.253 | 0.333 | +31.2% | +30.2% | +36.1% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 12.950 | 1.969 | -84.8% | -85.1% | -84.7% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | preg_match() per term | 15.191 | 1.969 | -87.0% | -87.1% | -86.9% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 11.033 | 1.318 | -88.1% | -88.1% | -87.9% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 17.663 | 1.318 | -92.5% | -92.7% | -92.4% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 15.609 | 2.377 | -84.8% | -84.8% | -84.6% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 34.624 | 2.377 | -93.1% | -93.2% | -93.1% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 29.378 | 1.742 | -94.1% | -94.1% | -94.1% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 9.314 | 1.742 | -81.3% | -81.3% | -81.3% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 234.979 | 13.106 | -94.4% | -94.4% | -94.4% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 73.578 | 13.106 | -82.2% | -82.4% | -82.1% |

### Synthetic tasks

#### Dictionary preparation included

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 0.394 | 91.677 | +23141.1% | +23035.8% | +23302.7% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 19.322 | 91.677 | +373.8% | +369.7% | +380.0% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 18.977 | 91.677 | +383.0% | +380.0% | +389.0% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 0.311 | 16.371 | +5165.4% | +5148.5% | +5194.0% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 18.163 | 16.371 | -9.9% | -10.9% | -9.6% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 17.886 | 16.371 | -8.4% | -9.6% | -8.3% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | strtr() | 0.307 | 1.157 | +276.7% | +273.2% | +278.0% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace_callback() | 4.986 | 1.157 | -76.8% | -77.0% | -76.8% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace() | 4.173 | 1.157 | -72.3% | -72.5% | -72.2% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | strtr() | 0.257 | 0.663 | +158.4% | +153.2% | +160.2% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | preg_replace_callback() | 1.353 | 0.663 | -51.0% | -51.3% | -50.8% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 0.380 | 83.878 | +21992.0% | +21891.6% | +22054.7% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 19.862 | 83.878 | +322.6% | +317.9% | +324.6% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 19.541 | 83.878 | +329.3% | +323.5% | +331.4% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 0.291 | 14.014 | +4713.2% | +4619.6% | +4770.4% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 20.441 | 14.014 | -31.5% | -31.9% | -30.8% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 20.102 | 14.014 | -30.2% | -30.9% | -28.8% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | strtr() | 0.282 | 1.127 | +300.1% | +297.1% | +301.7% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace_callback() | 5.070 | 1.127 | -77.8% | -77.9% | -77.7% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace() | 4.158 | 1.127 | -72.9% | -73.1% | -72.8% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | strtr() | 0.232 | 0.655 | +182.6% | +181.2% | +184.0% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | preg_replace_callback() | 1.293 | 0.655 | -49.3% | -49.4% | -49.2% |

#### Dictionary already prepared

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 0.386 | 0.541 | +40.5% | +40.1% | +41.2% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 0.883 | 0.541 | -38.7% | -38.9% | -38.4% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 0.652 | 0.541 | -17.0% | -17.3% | -16.6% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 0.319 | 0.542 | +69.9% | +68.7% | +73.0% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 0.671 | 0.542 | -19.3% | -20.8% | -18.7% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 0.464 | 0.542 | +16.8% | +16.5% | +19.4% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | strtr() | 0.313 | 0.535 | +71.0% | +70.5% | +71.9% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace_callback() | 1.062 | 0.535 | -49.6% | -49.9% | -49.2% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace() | 0.332 | 0.535 | +61.5% | +61.1% | +63.0% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | strtr() | 0.258 | 0.263 | +1.8% | +1.4% | +2.2% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | preg_replace_callback() | 0.588 | 0.263 | -55.4% | -55.7% | -55.1% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 0.372 | 0.562 | +51.0% | +50.7% | +51.7% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 0.858 | 0.562 | -34.4% | -34.7% | -34.2% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 0.622 | 0.562 | -9.6% | -10.1% | -9.4% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 0.296 | 0.553 | +86.6% | +85.6% | +87.4% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 0.663 | 0.553 | -16.5% | -17.2% | -15.7% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 0.398 | 0.553 | +38.9% | +33.6% | +42.7% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | strtr() | 0.281 | 0.571 | +103.0% | +102.3% | +104.0% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace_callback() | 1.164 | 0.571 | -51.0% | -51.3% | -50.7% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace() | 0.322 | 0.571 | +77.1% | +76.7% | +78.3% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | strtr() | 0.231 | 0.288 | +24.5% | +24.1% | +25.2% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | preg_replace_callback() | 0.580 | 0.288 | -50.3% | -50.6% | -50.0% |

## Size series

### Product tasks

#### Dictionary preparation included

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 0.281 | 1.398 | +397.2% | +395.4% | +400.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 0.710 | 1.398 | +96.8% | +94.6% | +97.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | str_contains() loop | 0.206 | 1.244 | +502.4% | +498.4% | +509.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | preg_match() | 0.633 | 1.244 | +96.5% | +95.3% | +97.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | str_contains() loop | 0.243 | 1.466 | +503.1% | +501.5% | +513.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | preg_match() | 0.759 | 1.466 | +93.1% | +91.3% | +94.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | str_contains() loop | 0.214 | 1.524 | +607.6% | +592.3% | +616.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | preg_match() | 0.746 | 1.524 | +103.8% | +99.4% | +105.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 0.974 | 2.934 | +201.5% | +200.2% | +203.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 1.533 | 2.934 | +91.6% | +90.9% | +92.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | str_contains() loop | 0.390 | 1.881 | +382.5% | +380.9% | +384.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | preg_match() | 0.978 | 1.881 | +92.2% | +90.4% | +93.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 0.434 | 3.615 | +732.5% | +727.1% | +737.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 1.237 | 3.615 | +192.4% | +190.7% | +193.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | str_contains() loop | 0.276 | 3.483 | +1163.1% | +1137.9% | +1179.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | preg_match() | 1.031 | 3.483 | +237.8% | +235.3% | +238.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | str_contains() loop | 0.335 | 3.693 | +999.9% | +996.3% | +1023.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | preg_match() | 1.304 | 3.693 | +182.9% | +180.4% | +184.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | str_contains() loop | 0.297 | 3.714 | +1154.3% | +1145.7% | +1179.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | preg_match() | 1.332 | 3.714 | +177.3% | +174.7% | +180.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 1.570 | 5.080 | +223.8% | +219.0% | +226.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 3.499 | 5.080 | +45.4% | +42.8% | +46.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | str_contains() loop | 0.555 | 4.047 | +627.8% | +620.7% | +632.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | preg_match() | 1.735 | 4.047 | +133.0% | +131.4% | +134.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 0.786 | 10.546 | +1242.8% | +1237.9% | +1271.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 2.558 | 10.546 | +313.2% | +310.8% | +316.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | str_contains() loop | 0.479 | 10.409 | +2072.0% | +2043.2% | +2133.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | preg_match() | 1.954 | 10.409 | +432.2% | +430.5% | +438.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | str_contains() loop | 0.588 | 10.876 | +1750.0% | +1741.0% | +1756.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | preg_match() | 2.761 | 10.876 | +293.8% | +291.8% | +295.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | str_contains() loop | 0.475 | 10.581 | +2131.5% | +2116.2% | +2190.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | preg_match() | 2.789 | 10.581 | +279.4% | +278.1% | +281.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 3.522 | 12.344 | +250.5% | +248.5% | +252.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 8.371 | 12.344 | +47.4% | +46.9% | +48.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | str_contains() loop | 1.306 | 11.166 | +754.6% | +723.9% | +757.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | preg_match() | 4.192 | 11.166 | +166.3% | +164.5% | +167.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 1.457 | 21.533 | +1376.0% | +1342.9% | +1440.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 4.891 | 21.533 | +340.3% | +339.1% | +341.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | str_contains() loop | 0.868 | 21.360 | +2359.7% | +2303.0% | +2437.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | preg_match() | 3.631 | 21.360 | +489.0% | +483.3% | +493.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | str_contains() loop | 1.109 | 21.649 | +1851.8% | +1842.3% | +1863.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | preg_match() | 5.213 | 21.649 | +315.2% | +314.1% | +316.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | str_contains() loop | 0.908 | 21.689 | +2291.3% | +2279.2% | +2337.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | preg_match() | 5.402 | 21.689 | +301.7% | +299.4% | +303.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 6.895 | 23.005 | +234.3% | +232.3% | +234.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 17.000 | 23.005 | +35.3% | +34.9% | +35.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | str_contains() loop | 2.833 | 21.987 | +676.1% | +671.3% | +680.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | preg_match() | 8.503 | 21.987 | +158.6% | +158.1% | +159.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 2.870 | 47.788 | +1565.4% | +1517.4% | +1614.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 9.920 | 47.788 | +380.5% | +376.5% | +385.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | str_contains() loop | 1.665 | 47.438 | +2750.2% | +2728.8% | +2766.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | preg_match() | 6.902 | 47.438 | +587.2% | +586.6% | +591.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | str_contains() loop | 2.149 | 47.606 | +2114.5% | +2049.9% | +2164.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | preg_match() | 10.347 | 47.606 | +360.6% | +357.1% | +362.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | str_contains() loop | 1.713 | 47.736 | +2691.9% | +2660.7% | +2743.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | preg_match() | 10.850 | 47.736 | +339.2% | +337.0% | +342.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 13.418 | 48.206 | +259.5% | +256.9% | +261.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 34.743 | 48.206 | +38.8% | +38.2% | +39.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | str_contains() loop | 5.474 | 46.899 | +756.6% | +752.9% | +761.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | preg_match() | 17.059 | 46.899 | +174.9% | +173.6% | +175.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 6.749 | 90.183 | +1236.5% | +1214.9% | +1253.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 19.853 | 90.183 | +354.0% | +352.6% | +354.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | str_contains() loop | 3.482 | 90.119 | +2490.6% | +2438.1% | +2511.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | preg_match() | 14.180 | 90.119 | +536.2% | +528.8% | +547.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | str_contains() loop | 4.574 | 90.132 | +1867.9% | +1824.9% | +1895.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | preg_match() | 20.803 | 90.132 | +333.2% | +328.9% | +333.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | str_contains() loop | 3.614 | 90.194 | +2393.7% | +2346.4% | +2562.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | preg_match() | 21.700 | 90.194 | +315.6% | +314.3% | +316.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 30.017 | 91.713 | +205.5% | +203.1% | +206.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 68.710 | 91.713 | +33.4% | +33.2% | +33.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | str_contains() loop | 11.498 | 90.497 | +687.4% | +684.5% | +691.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | preg_match() | 33.833 | 90.497 | +167.3% | +166.7% | +168.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 16.077 | 165.833 | +932.1% | +925.9% | +934.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 48.315 | 165.833 | +243.2% | +241.7% | +244.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | str_contains() loop | 8.656 | 165.010 | +1807.8% | +1782.7% | +1855.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | preg_match() | 27.972 | 165.010 | +490.0% | +489.0% | +491.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | str_contains() loop | 11.584 | 165.892 | +1332.2% | +1324.4% | +1345.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | preg_match() | 55.309 | 165.892 | +200.0% | +197.5% | +200.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | str_contains() loop | 8.716 | 165.712 | +1802.4% | +1779.0% | +1846.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | preg_match() | 57.250 | 165.712 | +189.4% | +188.7% | +190.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 68.080 | 167.197 | +145.5% | +144.4% | +146.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 226.290 | 167.197 | -26.1% | -26.5% | -25.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | str_contains() loop | 25.079 | 165.785 | +560.9% | +555.6% | +565.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | preg_match() | 112.783 | 165.785 | +47.1% | +46.4% | +53.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 1.187 | 3.255 | +174.5% | +173.5% | +176.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | preg_match() per term | 2.150 | 3.255 | +51.6% | +51.1% | +52.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 0.959 | 3.177 | +231.2% | +230.0% | +233.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 2.394 | 3.177 | +32.7% | +32.1% | +33.3% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 1.464 | 3.319 | +126.8% | +125.4% | +128.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 3.766 | 3.319 | -11.9% | -12.3% | -11.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 2.199 | 5.439 | +147.2% | +145.9% | +148.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | preg_match() per term | 3.987 | 5.439 | +36.4% | +35.6% | +37.2% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 1.817 | 5.586 | +207.3% | +205.9% | +209.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 4.490 | 5.586 | +24.2% | +23.9% | +25.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 2.714 | 5.538 | +104.1% | +103.2% | +105.3% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 7.028 | 5.538 | -21.2% | -21.6% | -20.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 3.921 | 9.600 | +144.8% | +143.7% | +146.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | preg_match() per term | 7.649 | 9.600 | +25.4% | +25.1% | +26.1% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 3.323 | 9.527 | +185.9% | +184.9% | +188.6% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 8.518 | 9.527 | +11.7% | +11.2% | +12.3% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 5.018 | 9.926 | +97.4% | +94.8% | +99.0% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 13.168 | 9.926 | -24.6% | -24.9% | -24.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 7.860 | 21.477 | +173.1% | +171.5% | +174.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | preg_match() per term | 14.446 | 21.477 | +48.8% | +48.2% | +49.1% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 6.747 | 21.080 | +212.4% | +210.2% | +216.2% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 16.733 | 21.080 | +25.8% | +25.4% | +26.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 9.933 | 21.303 | +114.3% | +112.2% | +115.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 24.984 | 21.303 | -14.8% | -15.1% | -14.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 15.972 | 48.688 | +204.9% | +201.8% | +207.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | preg_match() per term | 28.768 | 48.688 | +69.2% | +68.3% | +70.1% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 13.938 | 49.716 | +256.7% | +254.5% | +259.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 49.666 | 49.716 | +0.0% | -0.6% | +0.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 19.148 | 49.362 | +157.9% | +155.8% | +159.8% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 66.233 | 49.362 | -25.5% | -26.0% | -25.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 32.171 | 109.206 | +239.5% | +238.3% | +240.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | preg_match() per term | 60.273 | 109.206 | +81.1% | +80.4% | +81.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 30.319 | 108.260 | +257.1% | +256.1% | +257.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 112.761 | 108.260 | -4.0% | -4.3% | -3.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 35.413 | 105.815 | +198.7% | +197.7% | +199.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 137.419 | 105.815 | -23.0% | -23.1% | -22.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 62.523 | 305.941 | +389.5% | +387.7% | +391.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | preg_match() per term | 135.378 | 305.941 | +126.1% | +125.6% | +126.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 60.930 | 303.777 | +398.6% | +396.0% | +405.1% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 238.069 | 303.777 | +27.7% | +27.2% | +29.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 66.329 | 304.825 | +359.7% | +358.4% | +360.6% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 275.451 | 304.825 | +10.7% | +10.4% | +11.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 4.432 | 3.707 | -16.3% | -17.5% | -14.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 2.260 | 3.707 | +64.0% | +62.7% | +65.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 35.059 | 12.058 | -65.6% | -66.1% | -65.3% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 6.468 | 12.058 | +86.5% | +84.9% | +87.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 7.913 | 6.568 | -17.1% | -18.0% | -16.4% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 5.285 | 6.568 | +24.3% | +23.4% | +26.0% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 62.602 | 15.398 | -75.4% | -75.5% | -75.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 18.862 | 15.398 | -18.4% | -18.6% | -16.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 16.769 | 11.741 | -30.0% | -30.4% | -29.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 10.628 | 11.741 | +10.3% | +7.8% | +10.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 133.637 | 21.198 | -84.1% | -84.2% | -84.1% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 36.785 | 21.198 | -42.4% | -42.5% | -42.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 31.154 | 24.363 | -21.8% | -22.0% | -21.6% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 23.111 | 24.363 | +5.4% | +5.2% | +6.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 248.701 | 35.031 | -85.9% | -86.0% | -85.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 71.273 | 35.031 | -50.8% | -51.2% | -50.6% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 37.993 | 52.396 | +37.9% | +36.5% | +38.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 47.099 | 52.396 | +11.0% | +8.6% | +13.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 303.644 | 63.106 | -79.2% | -79.4% | -79.0% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 123.129 | 63.106 | -48.7% | -48.9% | -48.4% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 41.643 | 105.458 | +153.2% | +152.8% | +153.6% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 116.729 | 105.458 | -9.6% | -9.9% | -6.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 332.242 | 116.937 | -64.8% | -64.9% | -64.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 271.947 | 116.937 | -57.0% | -57.1% | -57.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 42.505 | 280.263 | +559.2% | +558.5% | +560.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 273.277 | 280.263 | +2.5% | +2.2% | +6.0% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 340.039 | 308.233 | -9.4% | -9.5% | -9.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 710.263 | 308.233 | -56.6% | -56.8% | -56.3% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 0.291 | 1.353 | +365.6% | +363.4% | +367.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 0.683 | 1.353 | +98.2% | +97.0% | +99.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | str_contains() loop | 0.203 | 1.198 | +489.4% | +484.1% | +493.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | preg_match() | 0.605 | 1.198 | +97.9% | +97.2% | +100.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | str_contains() loop | 0.238 | 1.437 | +504.6% | +496.6% | +507.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | preg_match() | 0.715 | 1.437 | +100.9% | +100.4% | +102.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | str_contains() loop | 0.212 | 1.450 | +584.4% | +579.4% | +589.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | preg_match() | 0.712 | 1.450 | +104.1% | +102.4% | +105.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 0.961 | 3.039 | +216.2% | +215.3% | +218.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 1.490 | 3.039 | +103.9% | +103.0% | +105.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | str_contains() loop | 0.386 | 1.890 | +389.5% | +385.0% | +392.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | preg_match() | 0.922 | 1.890 | +104.9% | +103.8% | +106.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 0.455 | 3.462 | +663.7% | +638.7% | +668.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 1.233 | 3.462 | +181.0% | +175.9% | +185.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | str_contains() loop | 0.280 | 3.239 | +1056.2% | +1045.1% | +1071.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | preg_match() | 1.070 | 3.239 | +202.9% | +198.6% | +207.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | str_contains() loop | 0.335 | 3.503 | +950.2% | +933.8% | +964.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | preg_match() | 1.308 | 3.503 | +168.5% | +166.2% | +169.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | str_contains() loop | 0.296 | 3.577 | +1108.4% | +1085.8% | +1116.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | preg_match() | 1.310 | 3.577 | +172.8% | +171.4% | +174.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 1.621 | 5.011 | +209.2% | +208.0% | +211.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 3.447 | 5.011 | +45.2% | +44.2% | +46.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | str_contains() loop | 0.552 | 3.852 | +598.0% | +594.4% | +600.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | preg_match() | 1.723 | 3.852 | +123.9% | +118.4% | +124.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 0.829 | 9.892 | +1092.8% | +1088.0% | +1127.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 2.553 | 9.892 | +287.5% | +285.2% | +290.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | str_contains() loop | 0.497 | 9.712 | +1854.5% | +1836.0% | +1865.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | preg_match() | 1.951 | 9.712 | +400.3% | +393.2% | +403.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | str_contains() loop | 0.608 | 10.268 | +1590.5% | +1578.0% | +1597.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | preg_match() | 2.729 | 10.268 | +276.2% | +274.4% | +278.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | str_contains() loop | 0.510 | 9.993 | +1860.5% | +1838.3% | +1896.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | preg_match() | 2.777 | 9.993 | +259.8% | +256.6% | +261.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 3.659 | 11.811 | +223.0% | +221.4% | +223.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 8.219 | 11.811 | +43.6% | +43.0% | +44.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | str_contains() loop | 1.352 | 10.590 | +684.0% | +679.4% | +691.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | preg_match() | 4.198 | 10.590 | +152.4% | +151.7% | +153.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 1.557 | 20.686 | +1229.5% | +1221.1% | +1237.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 4.986 | 20.686 | +315.7% | +311.8% | +319.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | str_contains() loop | 0.937 | 20.284 | +2065.4% | +2053.3% | +2082.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | preg_match() | 3.650 | 20.284 | +455.7% | +453.8% | +460.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | str_contains() loop | 1.182 | 20.613 | +1645.9% | +1635.5% | +1682.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | preg_match() | 5.369 | 20.613 | +283.9% | +280.2% | +288.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | str_contains() loop | 0.988 | 20.558 | +1981.3% | +1971.9% | +2038.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | preg_match() | 5.597 | 20.558 | +267.9% | +266.4% | +269.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 7.227 | 22.107 | +206.2% | +204.0% | +208.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 17.595 | 22.107 | +25.5% | +24.9% | +26.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | str_contains() loop | 2.901 | 20.995 | +623.8% | +621.7% | +628.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | preg_match() | 8.821 | 20.995 | +138.1% | +137.1% | +140.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 3.238 | 44.924 | +1287.6% | +1261.3% | +1301.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 10.031 | 44.924 | +347.9% | +346.1% | +350.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | str_contains() loop | 1.753 | 44.355 | +2430.2% | +2418.0% | +2440.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | preg_match() | 7.249 | 44.355 | +511.5% | +501.7% | +518.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | str_contains() loop | 2.309 | 44.876 | +1843.0% | +1819.9% | +1854.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | preg_match() | 10.684 | 44.876 | +320.2% | +319.2% | +321.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | str_contains() loop | 1.792 | 44.835 | +2401.0% | +2392.1% | +2418.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | preg_match() | 10.876 | 44.835 | +312.2% | +311.4% | +314.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 14.132 | 45.453 | +221.6% | +219.7% | +222.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 33.684 | 45.453 | +34.9% | +34.8% | +35.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | str_contains() loop | 5.675 | 44.408 | +683.0% | +679.2% | +684.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | preg_match() | 16.864 | 44.408 | +163.5% | +161.9% | +165.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 7.679 | 86.337 | +1024.5% | +1000.1% | +1049.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 20.075 | 86.337 | +330.1% | +325.6% | +333.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | str_contains() loop | 3.948 | 86.289 | +2083.9% | +2069.4% | +2135.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | preg_match() | 14.557 | 86.289 | +492.3% | +490.1% | +496.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | str_contains() loop | 5.259 | 86.506 | +1545.1% | +1535.0% | +1585.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | preg_match() | 22.612 | 86.506 | +282.4% | +280.5% | +283.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | str_contains() loop | 3.988 | 86.258 | +2063.7% | +2012.0% | +2075.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | preg_match() | 23.000 | 86.258 | +275.2% | +273.3% | +275.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 30.735 | 88.371 | +187.6% | +185.3% | +188.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 80.405 | 88.371 | +9.9% | +9.2% | +10.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | str_contains() loop | 12.020 | 87.543 | +628.6% | +623.2% | +629.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | preg_match() | 33.957 | 87.543 | +157.9% | +156.9% | +160.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 17.685 | 158.689 | +797.4% | +772.6% | +799.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 50.060 | 158.689 | +217.0% | +215.2% | +219.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | str_contains() loop | 9.320 | 159.040 | +1606.9% | +1597.9% | +1627.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | preg_match() | 29.095 | 159.040 | +446.5% | +443.3% | +459.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | str_contains() loop | 12.706 | 160.719 | +1165.1% | +1162.5% | +1171.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | preg_match() | 53.915 | 160.719 | +198.3% | +197.3% | +198.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | str_contains() loop | 9.584 | 159.330 | +1562.5% | +1556.5% | +1598.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | preg_match() | 57.339 | 159.330 | +177.7% | +175.5% | +179.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 70.372 | 160.763 | +128.7% | +127.3% | +129.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 233.067 | 160.763 | -31.1% | -33.9% | -30.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | str_contains() loop | 25.553 | 159.855 | +525.3% | +522.0% | +529.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | preg_match() | 114.737 | 159.855 | +39.3% | +35.4% | +42.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 1.189 | 3.422 | +187.8% | +186.2% | +190.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | preg_match() per term | 2.046 | 3.422 | +67.2% | +66.5% | +67.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 0.985 | 3.135 | +218.5% | +216.8% | +222.1% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 2.294 | 3.135 | +36.7% | +34.9% | +37.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 1.451 | 3.387 | +133.5% | +131.9% | +135.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 3.617 | 3.387 | -6.3% | -7.1% | -5.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 2.187 | 5.296 | +142.3% | +140.3% | +143.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | preg_match() per term | 3.781 | 5.296 | +40.1% | +39.3% | +41.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 1.883 | 5.136 | +173.0% | +170.2% | +174.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 4.299 | 5.136 | +19.5% | +18.8% | +20.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 2.740 | 5.407 | +97.4% | +95.9% | +99.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 6.702 | 5.407 | -19.5% | -20.0% | -18.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 3.987 | 9.325 | +133.6% | +131.3% | +135.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | preg_match() per term | 7.374 | 9.325 | +26.3% | +24.5% | +27.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 3.418 | 8.987 | +163.0% | +160.0% | +165.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 8.201 | 8.987 | +9.7% | +9.1% | +10.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 5.256 | 9.653 | +83.5% | +81.9% | +84.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 12.862 | 9.653 | -25.0% | -25.4% | -24.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 8.496 | 20.576 | +142.0% | +141.4% | +143.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | preg_match() per term | 14.395 | 20.576 | +42.9% | +42.5% | +43.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 7.107 | 20.223 | +184.6% | +182.8% | +186.2% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 16.288 | 20.223 | +24.1% | +23.6% | +24.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 10.526 | 20.417 | +94.0% | +92.7% | +94.6% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 24.371 | 20.417 | -16.2% | -16.7% | -15.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 16.221 | 46.148 | +184.7% | +182.8% | +185.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | preg_match() per term | 28.268 | 46.148 | +63.4% | +62.6% | +64.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 14.840 | 47.015 | +216.7% | +214.0% | +218.9% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 48.466 | 47.015 | -3.0% | -4.0% | -2.8% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 19.864 | 46.540 | +134.2% | +133.2% | +141.6% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 64.556 | 46.540 | -27.9% | -28.5% | -27.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 32.944 | 105.422 | +219.8% | +218.4% | +220.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | preg_match() per term | 60.012 | 105.422 | +75.8% | +74.3% | +77.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 31.460 | 104.518 | +232.5% | +230.6% | +233.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 110.994 | 104.518 | -5.8% | -6.0% | -5.6% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 35.824 | 102.660 | +186.2% | +182.7% | +187.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 133.869 | 102.660 | -23.3% | -23.6% | -23.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 63.270 | 292.269 | +361.8% | +361.0% | +363.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | preg_match() per term | 132.057 | 292.269 | +121.2% | +120.2% | +122.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 61.878 | 292.738 | +373.1% | +370.9% | +374.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 232.903 | 292.738 | +25.7% | +25.6% | +25.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 67.108 | 292.354 | +335.5% | +331.9% | +336.8% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 268.521 | 292.354 | +8.9% | +7.6% | +9.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 4.343 | 3.710 | -14.5% | -15.7% | -13.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 2.188 | 3.710 | +69.5% | +68.9% | +70.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 34.348 | 12.877 | -62.5% | -63.0% | -61.3% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 6.458 | 12.877 | +99.4% | +98.5% | +99.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 7.887 | 6.355 | -19.5% | -19.9% | -19.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 5.146 | 6.355 | +23.5% | +22.9% | +24.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 62.308 | 15.569 | -75.0% | -75.1% | -74.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 18.500 | 15.569 | -15.8% | -16.4% | -14.4% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 16.722 | 11.152 | -33.4% | -33.7% | -32.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 10.439 | 11.152 | +6.8% | +6.2% | +7.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 133.113 | 21.123 | -84.2% | -84.3% | -84.1% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 36.729 | 21.123 | -42.5% | -43.0% | -42.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 31.324 | 23.369 | -25.4% | -25.5% | -24.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 22.785 | 23.369 | +2.6% | +2.2% | +4.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 250.230 | 34.052 | -86.4% | -86.4% | -86.3% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 70.845 | 34.052 | -52.0% | -52.3% | -51.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 38.501 | 49.294 | +28.0% | +27.7% | +28.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 47.117 | 49.294 | +4.6% | +4.3% | +5.3% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 307.146 | 60.122 | -80.4% | -80.5% | -80.3% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 129.887 | 60.122 | -53.7% | -53.9% | -53.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 42.149 | 101.300 | +140.4% | +139.9% | +141.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 108.814 | 101.300 | -6.9% | -7.4% | -6.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 336.815 | 112.678 | -66.5% | -66.7% | -66.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 262.055 | 112.678 | -57.0% | -57.3% | -56.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 43.089 | 267.681 | +521.4% | +518.9% | +522.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 260.801 | 267.681 | +2.7% | +2.4% | +4.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 343.591 | 293.572 | -14.6% | -15.0% | -14.3% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 741.988 | 293.572 | -60.4% | -61.3% | -60.1% |

#### Dictionary already prepared

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 0.282 | 0.266 | -6.0% | -6.5% | -5.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 0.236 | 0.266 | +12.4% | +12.0% | +13.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | str_contains() loop | 0.206 | 0.121 | -41.0% | -41.7% | -40.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | preg_match() | 0.163 | 0.121 | -25.5% | -26.0% | -24.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | str_contains() loop | 0.243 | 0.339 | +39.5% | +38.5% | +40.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | preg_match() | 0.279 | 0.339 | +21.3% | +21.0% | +21.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | str_contains() loop | 0.219 | 0.364 | +65.8% | +64.7% | +67.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | preg_match() | 0.272 | 0.364 | +33.6% | +32.8% | +36.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 0.937 | 1.818 | +94.0% | +92.5% | +94.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 1.063 | 1.818 | +71.0% | +70.5% | +71.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | str_contains() loop | 0.384 | 0.756 | +96.8% | +95.0% | +98.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | preg_match() | 0.496 | 0.756 | +52.7% | +51.9% | +53.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 0.444 | 0.266 | -40.2% | -41.0% | -39.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 0.347 | 0.266 | -23.0% | -23.9% | -22.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | str_contains() loop | 0.278 | 0.121 | -56.4% | -58.5% | -55.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | preg_match() | 0.167 | 0.121 | -27.4% | -27.7% | -26.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | str_contains() loop | 0.332 | 0.339 | +2.0% | +1.2% | +2.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | preg_match() | 0.409 | 0.339 | -17.3% | -17.7% | -16.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | str_contains() loop | 0.289 | 0.365 | +26.4% | +23.9% | +26.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | preg_match() | 0.429 | 0.365 | -14.8% | -16.6% | -14.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 1.572 | 1.817 | +15.4% | +14.9% | +15.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 2.580 | 1.817 | -29.6% | -29.9% | -29.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | str_contains() loop | 0.567 | 0.758 | +33.7% | +33.2% | +35.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | preg_match() | 0.850 | 0.758 | -10.8% | -11.3% | -10.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 0.780 | 0.267 | -65.8% | -66.0% | -65.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 0.754 | 0.267 | -64.6% | -64.7% | -64.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | str_contains() loop | 0.472 | 0.122 | -74.1% | -74.7% | -72.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | preg_match() | 0.182 | 0.122 | -32.7% | -33.9% | -27.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | str_contains() loop | 0.588 | 0.340 | -42.2% | -42.4% | -42.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | preg_match() | 0.952 | 0.340 | -64.3% | -64.4% | -64.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | str_contains() loop | 0.491 | 0.366 | -25.5% | -25.8% | -24.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | preg_match() | 0.989 | 0.366 | -63.0% | -63.2% | -62.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 3.518 | 1.819 | -48.3% | -48.8% | -48.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 6.563 | 1.819 | -72.3% | -72.4% | -72.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | str_contains() loop | 1.374 | 0.757 | -44.9% | -45.4% | -44.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | preg_match() | 2.420 | 0.757 | -68.7% | -68.8% | -68.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 1.406 | 0.271 | -80.7% | -80.9% | -80.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 1.482 | 0.271 | -81.7% | -81.8% | -81.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | str_contains() loop | 0.890 | 0.119 | -86.7% | -86.8% | -86.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | preg_match() | 0.217 | 0.119 | -45.2% | -45.5% | -45.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | str_contains() loop | 1.125 | 0.346 | -69.3% | -70.0% | -68.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | preg_match() | 1.847 | 0.346 | -81.3% | -81.3% | -81.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | str_contains() loop | 0.908 | 0.373 | -58.9% | -59.1% | -58.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | preg_match() | 1.983 | 0.373 | -81.2% | -81.2% | -81.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 6.837 | 1.837 | -73.1% | -73.3% | -73.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 13.533 | 1.837 | -86.4% | -86.5% | -86.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | str_contains() loop | 2.846 | 0.763 | -73.2% | -73.4% | -73.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | preg_match() | 5.050 | 0.763 | -84.9% | -85.0% | -84.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 2.920 | 0.276 | -90.6% | -90.9% | -90.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 2.975 | 0.276 | -90.7% | -90.8% | -90.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | str_contains() loop | 1.699 | 0.119 | -93.0% | -93.0% | -92.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | preg_match() | 0.273 | 0.119 | -56.3% | -56.9% | -55.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | str_contains() loop | 2.102 | 0.350 | -83.3% | -83.6% | -83.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | preg_match() | 3.657 | 0.350 | -90.4% | -90.5% | -90.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | str_contains() loop | 1.674 | 0.376 | -77.5% | -78.1% | -77.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | preg_match() | 3.956 | 0.376 | -90.5% | -90.5% | -90.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 13.351 | 1.851 | -86.1% | -86.2% | -86.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 27.811 | 1.851 | -93.3% | -93.4% | -93.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | str_contains() loop | 5.461 | 0.761 | -86.1% | -86.2% | -86.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | preg_match() | 10.320 | 0.761 | -92.6% | -92.7% | -92.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 6.760 | 0.294 | -95.6% | -95.8% | -95.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 6.079 | 0.294 | -95.2% | -95.2% | -95.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | str_contains() loop | 3.564 | 0.119 | -96.6% | -96.8% | -96.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | preg_match() | 0.391 | 0.119 | -69.5% | -69.6% | -69.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | str_contains() loop | 4.439 | 0.374 | -91.6% | -92.0% | -91.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | preg_match() | 7.232 | 0.374 | -94.8% | -94.8% | -94.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | str_contains() loop | 3.712 | 0.395 | -89.4% | -89.4% | -88.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | preg_match() | 7.854 | 0.395 | -95.0% | -95.0% | -94.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 30.008 | 1.934 | -93.6% | -93.6% | -93.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 55.000 | 1.934 | -96.5% | -96.5% | -96.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | str_contains() loop | 11.462 | 0.810 | -92.9% | -93.0% | -92.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | preg_match() | 20.401 | 0.810 | -96.0% | -96.0% | -96.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 16.203 | 0.313 | -98.1% | -98.1% | -98.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 20.267 | 0.313 | -98.5% | -98.5% | -98.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | str_contains() loop | 8.669 | 0.118 | -98.6% | -98.7% | -98.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | preg_match() | 0.657 | 0.118 | -82.0% | -82.5% | -81.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | str_contains() loop | 11.813 | 0.395 | -96.7% | -96.7% | -96.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | preg_match() | 22.684 | 0.395 | -98.3% | -98.3% | -98.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | str_contains() loop | 8.863 | 0.426 | -95.2% | -95.3% | -95.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | preg_match() | 28.092 | 0.426 | -98.5% | -98.5% | -98.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 67.982 | 2.043 | -97.0% | -97.0% | -97.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 194.352 | 2.043 | -98.9% | -99.0% | -98.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | str_contains() loop | 24.990 | 0.849 | -96.6% | -96.6% | -96.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | preg_match() | 67.443 | 0.849 | -98.7% | -98.8% | -98.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 1.184 | 1.149 | -2.9% | -3.2% | -2.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | preg_match() per term | 1.488 | 1.149 | -22.8% | -23.4% | -22.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 0.960 | 1.085 | +13.0% | +12.6% | +13.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 1.671 | 1.085 | -35.1% | -35.4% | -34.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 1.457 | 1.215 | -16.6% | -16.9% | -16.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 2.840 | 1.215 | -57.2% | -57.3% | -56.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 2.160 | 1.228 | -43.2% | -43.3% | -42.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | preg_match() per term | 2.737 | 1.228 | -55.1% | -55.3% | -54.9% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 1.794 | 1.089 | -39.3% | -39.6% | -39.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 3.130 | 1.089 | -65.2% | -65.4% | -65.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 2.711 | 1.322 | -51.2% | -51.5% | -50.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 5.234 | 1.322 | -74.7% | -74.9% | -74.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 3.907 | 1.356 | -65.3% | -65.4% | -65.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | preg_match() per term | 5.238 | 1.356 | -74.1% | -74.2% | -74.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 3.192 | 1.103 | -65.4% | -65.6% | -65.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 5.954 | 1.103 | -81.5% | -81.5% | -81.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 5.008 | 1.510 | -69.9% | -70.1% | -69.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 9.827 | 1.510 | -84.6% | -84.7% | -84.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 7.909 | 1.569 | -80.2% | -80.3% | -80.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | preg_match() per term | 9.853 | 1.569 | -84.1% | -84.1% | -83.9% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 6.739 | 1.182 | -82.4% | -82.7% | -82.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 11.521 | 1.182 | -89.8% | -89.8% | -89.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 9.921 | 1.911 | -80.7% | -80.8% | -80.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 18.269 | 1.911 | -89.5% | -89.6% | -89.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 15.961 | 1.886 | -88.2% | -88.3% | -87.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | preg_match() per term | 19.092 | 1.886 | -90.1% | -90.2% | -89.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 13.996 | 1.302 | -90.7% | -90.7% | -90.6% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 37.357 | 1.302 | -96.5% | -96.5% | -96.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 19.186 | 2.264 | -88.2% | -88.3% | -87.6% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 50.710 | 2.264 | -95.5% | -95.5% | -95.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 31.978 | 1.958 | -93.9% | -93.9% | -93.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | preg_match() per term | 39.282 | 1.958 | -95.0% | -95.0% | -94.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 30.248 | 1.361 | -95.5% | -95.5% | -95.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 89.290 | 1.361 | -98.5% | -98.5% | -98.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 35.367 | 2.318 | -93.4% | -93.5% | -93.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 107.636 | 2.318 | -97.8% | -97.9% | -97.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 62.095 | 2.110 | -96.6% | -96.6% | -96.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | preg_match() per term | 92.959 | 2.110 | -97.7% | -97.7% | -97.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 60.778 | 1.503 | -97.5% | -97.5% | -97.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 192.043 | 1.503 | -99.2% | -99.2% | -99.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 65.857 | 2.481 | -96.2% | -96.2% | -96.0% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 218.943 | 2.481 | -98.9% | -98.9% | -98.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 4.449 | 1.257 | -71.7% | -72.2% | -71.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 0.701 | 1.257 | +79.4% | +78.8% | +80.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 34.634 | 9.433 | -72.8% | -73.1% | -72.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 4.839 | 9.433 | +94.9% | +93.8% | +96.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 7.878 | 1.335 | -83.1% | -83.2% | -82.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 1.988 | 1.335 | -32.8% | -33.1% | -32.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 62.790 | 10.134 | -83.8% | -84.0% | -83.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 15.178 | 10.134 | -33.1% | -33.7% | -32.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 16.793 | 1.462 | -91.3% | -91.3% | -91.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 3.814 | 1.462 | -61.7% | -61.8% | -61.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 133.691 | 10.996 | -91.8% | -91.8% | -91.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 30.309 | 10.996 | -63.7% | -63.8% | -63.6% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 31.114 | 1.606 | -94.8% | -94.9% | -94.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 6.938 | 1.606 | -76.9% | -76.9% | -76.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 248.610 | 12.133 | -95.1% | -95.1% | -95.1% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 54.646 | 12.133 | -77.8% | -77.8% | -77.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 37.987 | 1.786 | -95.3% | -95.4% | -95.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 10.983 | 1.786 | -83.7% | -84.0% | -83.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 302.936 | 13.453 | -95.6% | -95.6% | -95.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 86.735 | 13.453 | -84.5% | -84.5% | -84.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 41.586 | 1.852 | -95.5% | -95.6% | -95.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 22.755 | 1.852 | -91.9% | -91.9% | -91.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 331.712 | 14.137 | -95.7% | -95.8% | -95.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 180.085 | 14.137 | -92.2% | -92.2% | -92.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 42.540 | 2.079 | -95.1% | -95.1% | -95.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 69.161 | 2.079 | -97.0% | -97.0% | -97.0% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 339.351 | 14.936 | -95.6% | -95.6% | -95.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 531.474 | 14.936 | -97.2% | -97.2% | -97.2% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 0.288 | 0.274 | -4.5% | -5.7% | -3.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 0.220 | 0.274 | +25.1% | +23.4% | +26.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | str_contains() loop | 0.205 | 0.116 | -43.0% | -44.8% | -42.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | preg_match() | 0.153 | 0.116 | -23.9% | -25.0% | -22.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | str_contains() loop | 0.237 | 0.356 | +50.2% | +48.8% | +52.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | preg_match() | 0.255 | 0.356 | +39.3% | +38.4% | +40.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | str_contains() loop | 0.213 | 0.379 | +77.1% | +75.7% | +79.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | preg_match() | 0.251 | 0.379 | +50.6% | +48.6% | +51.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 0.940 | 1.979 | +110.3% | +107.7% | +111.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 1.006 | 1.979 | +96.6% | +93.4% | +98.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | str_contains() loop | 0.386 | 0.810 | +110.0% | +108.0% | +111.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | preg_match() | 0.465 | 0.810 | +74.1% | +72.4% | +76.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 0.463 | 0.273 | -41.0% | -41.2% | -40.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 0.324 | 0.273 | -15.3% | -16.2% | -14.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | str_contains() loop | 0.287 | 0.115 | -60.0% | -60.4% | -59.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | preg_match() | 0.151 | 0.115 | -23.8% | -24.7% | -23.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | str_contains() loop | 0.328 | 0.359 | +9.5% | +8.5% | +10.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | preg_match() | 0.387 | 0.359 | -7.3% | -10.5% | -6.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | str_contains() loop | 0.304 | 0.385 | +26.8% | +26.2% | +27.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | preg_match() | 0.405 | 0.385 | -4.8% | -5.4% | -4.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 1.615 | 1.978 | +22.5% | +21.6% | +22.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 2.513 | 1.978 | -21.3% | -22.1% | -20.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | str_contains() loop | 0.553 | 0.810 | +46.4% | +45.7% | +47.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | preg_match() | 0.804 | 0.810 | +0.7% | +0.1% | +1.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 0.857 | 0.273 | -68.1% | -68.2% | -67.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 0.722 | 0.273 | -62.2% | -62.3% | -62.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | str_contains() loop | 0.514 | 0.115 | -77.7% | -78.3% | -77.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | preg_match() | 0.167 | 0.115 | -31.3% | -33.3% | -30.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | str_contains() loop | 0.608 | 0.357 | -41.1% | -41.4% | -40.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | preg_match() | 0.919 | 0.357 | -61.1% | -61.4% | -60.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | str_contains() loop | 0.503 | 0.379 | -24.5% | -24.9% | -23.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | preg_match() | 0.958 | 0.379 | -60.4% | -60.6% | -60.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 3.622 | 1.977 | -45.4% | -45.7% | -45.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 6.442 | 1.977 | -69.3% | -69.4% | -69.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | str_contains() loop | 1.349 | 0.809 | -40.0% | -40.3% | -39.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | preg_match() | 2.357 | 0.809 | -65.7% | -65.8% | -65.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 1.653 | 0.278 | -83.2% | -83.3% | -83.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 1.519 | 0.278 | -81.7% | -81.8% | -81.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | str_contains() loop | 0.917 | 0.113 | -87.7% | -88.0% | -87.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | preg_match() | 0.197 | 0.113 | -42.8% | -43.5% | -42.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | str_contains() loop | 1.178 | 0.365 | -69.1% | -69.1% | -69.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | preg_match() | 1.896 | 0.365 | -80.8% | -80.9% | -80.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | str_contains() loop | 0.974 | 0.387 | -60.2% | -60.4% | -59.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | preg_match() | 2.042 | 0.387 | -81.0% | -81.1% | -80.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 7.198 | 1.994 | -72.3% | -72.6% | -72.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 14.054 | 1.994 | -85.8% | -85.9% | -85.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | str_contains() loop | 2.902 | 0.814 | -71.9% | -72.1% | -71.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | preg_match() | 5.238 | 0.814 | -84.5% | -84.5% | -84.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 3.450 | 0.285 | -91.7% | -92.0% | -91.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 2.854 | 0.285 | -90.0% | -90.0% | -89.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | str_contains() loop | 1.807 | 0.112 | -93.8% | -93.8% | -93.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | preg_match() | 0.239 | 0.112 | -53.0% | -53.3% | -51.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | str_contains() loop | 2.219 | 0.371 | -83.3% | -83.6% | -83.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | preg_match() | 3.474 | 0.371 | -89.3% | -89.4% | -89.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | str_contains() loop | 1.869 | 0.392 | -79.0% | -79.2% | -79.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | preg_match() | 3.778 | 0.392 | -89.7% | -89.7% | -89.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 14.132 | 2.013 | -85.8% | -85.9% | -85.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 26.568 | 2.013 | -92.4% | -92.5% | -92.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | str_contains() loop | 5.541 | 0.813 | -85.3% | -85.4% | -85.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | preg_match() | 9.833 | 0.813 | -91.7% | -91.8% | -91.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 7.934 | 0.304 | -96.2% | -96.2% | -96.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 5.979 | 0.304 | -94.9% | -94.9% | -94.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | str_contains() loop | 3.916 | 0.115 | -97.1% | -97.1% | -97.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | preg_match() | 0.376 | 0.115 | -69.4% | -70.1% | -68.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | str_contains() loop | 5.157 | 0.399 | -92.3% | -92.5% | -92.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | preg_match() | 7.061 | 0.399 | -94.4% | -94.4% | -94.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | str_contains() loop | 3.901 | 0.414 | -89.4% | -89.6% | -89.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | preg_match() | 7.672 | 0.414 | -94.6% | -94.6% | -94.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 30.699 | 2.101 | -93.2% | -93.2% | -93.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 67.249 | 2.101 | -96.9% | -96.9% | -96.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | str_contains() loop | 11.744 | 0.866 | -92.6% | -92.7% | -92.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | preg_match() | 19.979 | 0.866 | -95.7% | -95.7% | -95.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 17.747 | 0.324 | -98.2% | -98.2% | -98.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 20.411 | 0.324 | -98.4% | -98.4% | -98.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | str_contains() loop | 9.537 | 0.115 | -98.8% | -98.8% | -98.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | preg_match() | 0.620 | 0.115 | -81.2% | -82.0% | -80.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | str_contains() loop | 12.322 | 0.419 | -96.6% | -96.6% | -96.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | preg_match() | 23.226† | 0.419 | -98.2% | -98.3% | -98.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | str_contains() loop | 9.636 | 0.444 | -95.4% | -95.4% | -95.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | preg_match() | 25.386 | 0.444 | -98.3% | -98.3% | -98.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 71.652 | 2.209 | -96.9% | -96.9% | -96.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 185.207 | 2.209 | -98.8% | -98.9% | -98.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | str_contains() loop | 26.359 | 0.906 | -96.6% | -96.6% | -96.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | preg_match() | 67.255 | 0.906 | -98.7% | -98.7% | -98.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 1.176 | 1.343 | +14.2% | +13.7% | +14.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | preg_match() per term | 1.463 | 1.343 | -8.2% | -8.7% | -8.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 0.985 | 1.155 | +17.1% | +15.9% | +17.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 1.671 | 1.155 | -30.9% | -31.2% | -30.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 1.467 | 1.397 | -4.8% | -5.8% | -4.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 2.828 | 1.397 | -50.6% | -50.7% | -50.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 2.283 | 1.429 | -37.3% | -38.0% | -35.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | preg_match() per term | 2.827 | 1.429 | -49.2% | -49.6% | -48.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 1.884 | 1.160 | -38.4% | -39.0% | -38.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 3.168 | 1.160 | -63.4% | -63.5% | -63.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 2.798 | 1.514 | -45.9% | -46.5% | -45.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 5.217 | 1.514 | -71.0% | -71.0% | -70.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 3.968 | 1.542 | -61.1% | -61.4% | -60.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | preg_match() per term | 5.272 | 1.542 | -70.8% | -70.9% | -70.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 3.390 | 1.175 | -65.3% | -65.5% | -65.1% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 5.944 | 1.175 | -80.2% | -80.3% | -80.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 5.249 | 1.710 | -67.4% | -67.7% | -67.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 9.825 | 1.710 | -82.6% | -82.6% | -82.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 8.181 | 1.732 | -78.8% | -78.9% | -78.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | preg_match() per term | 9.868 | 1.732 | -82.5% | -82.5% | -82.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 7.303 | 1.252 | -82.9% | -82.9% | -82.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 11.506 | 1.252 | -89.1% | -89.2% | -89.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 10.563 | 2.058 | -80.5% | -80.6% | -80.3% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 18.309 | 2.058 | -88.8% | -88.8% | -88.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 16.301 | 2.055 | -87.4% | -87.4% | -87.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | preg_match() per term | 19.088 | 2.055 | -89.2% | -89.3% | -89.1% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 14.896 | 1.377 | -90.8% | -90.8% | -90.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 37.532 | 1.377 | -96.3% | -96.3% | -96.3% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 19.805 | 2.514 | -87.3% | -87.4% | -87.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 51.319 | 2.514 | -95.1% | -95.1% | -95.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 32.852 | 2.112 | -93.6% | -93.6% | -93.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | preg_match() per term | 38.661 | 2.112 | -94.5% | -94.6% | -94.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 30.859 | 1.433 | -95.4% | -95.4% | -95.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 89.887 | 1.433 | -98.4% | -98.4% | -98.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 36.416 | 2.536 | -93.0% | -93.2% | -93.0% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 107.333 | 2.536 | -97.6% | -97.6% | -97.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 62.293 | 2.292 | -96.3% | -96.3% | -96.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | preg_match() per term | 93.300 | 2.292 | -97.5% | -97.6% | -97.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 61.758 | 1.586 | -97.4% | -97.4% | -97.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 191.992 | 1.586 | -99.2% | -99.2% | -99.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 67.481 | 2.698 | -96.0% | -96.0% | -96.0% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 218.991 | 2.698 | -98.8% | -98.8% | -98.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 4.263 | 1.357 | -68.2% | -68.5% | -67.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 0.699 | 1.357 | +94.5% | +93.1% | +96.0% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 33.810 | 10.309 | -69.5% | -70.0% | -69.3% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 4.924 | 10.309 | +109.3% | +108.5% | +110.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 7.902 | 1.407 | -82.2% | -82.3% | -82.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 1.990 | 1.407 | -29.4% | -29.6% | -29.1% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 62.679 | 10.693 | -82.9% | -83.1% | -82.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 15.223 | 10.693 | -29.8% | -30.0% | -29.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 16.776 | 1.502 | -91.0% | -91.1% | -91.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 3.818 | 1.502 | -60.7% | -60.8% | -60.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 133.045 | 11.363 | -91.5% | -91.5% | -91.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 29.910 | 11.363 | -62.0% | -62.1% | -61.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 31.261 | 1.633 | -94.8% | -94.8% | -94.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 6.887 | 1.633 | -76.3% | -76.4% | -76.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 249.861 | 12.345 | -95.1% | -95.1% | -95.0% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 54.566 | 12.345 | -77.4% | -77.5% | -77.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 38.414 | 1.778 | -95.4% | -95.4% | -95.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 11.881 | 1.778 | -85.0% | -85.1% | -84.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 306.588 | 13.567 | -95.6% | -95.6% | -95.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 94.085 | 13.567 | -85.6% | -85.6% | -85.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 42.097 | 1.873 | -95.6% | -95.6% | -95.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 22.092 | 1.873 | -91.5% | -91.6% | -91.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 336.576 | 14.358 | -95.7% | -95.7% | -95.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 202.324 | 14.358 | -92.9% | -92.9% | -92.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 42.954 | 2.005 | -95.3% | -95.3% | -95.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 67.445 | 2.005 | -97.0% | -97.0% | -97.0% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 342.755 | 15.214 | -95.6% | -95.6% | -95.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 554.760 | 15.214 | -97.3% | -97.3% | -97.2% |

### Control tasks

#### Dictionary preparation included

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | str_contains() loop | 0.345 | 6.996 | +1931.1% | +1898.3% | +1952.6% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | preg_match() | 1.271 | 6.996 | +450.3% | +435.7% | +455.8% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | strtr() | 72.681 | 199.365 | +174.3% | +173.2% | +175.1% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace_callback() | 10.853 | 199.365 | +1736.8% | +1728.9% | +1743.5% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | str_replace() | 151.353 | 199.365 | +31.5% | +30.9% | +32.2% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace() | 10.420 | 199.365 | +1811.9% | +1802.4% | +1820.8% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | str_contains() loop | 0.368 | 6.566 | +1687.4% | +1654.2% | +1757.3% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | preg_match() | 1.340 | 6.566 | +391.2% | +379.3% | +398.1% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | strtr() | 66.185 | 209.180 | +216.0% | +214.6% | +216.4% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace_callback() | 10.102 | 209.180 | +1969.1% | +1963.3% | +1975.2% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | str_replace() | 141.272 | 209.180 | +48.1% | +46.1% | +48.4% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace() | 9.642 | 209.180 | +2068.6% | +2055.1% | +2072.6% |

#### Dictionary already prepared

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | str_contains() loop | 0.342 | 0.266 | -22.1% | -23.8% | -20.2% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | preg_match() | 0.256 | 0.266 | +4.1% | +3.6% | +4.7% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | strtr() | 73.467 | 169.747 | +131.1% | +130.3% | +131.3% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace_callback() | 4.520 | 169.747 | +3654.6% | +3642.2% | +3664.1% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | str_replace() | 146.498 | 169.747 | +15.9% | +15.0% | +16.0% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace() | 4.135 | 169.747 | +4004.6% | +3985.4% | +4016.4% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | str_contains() loop | 0.356 | 0.273 | -23.0% | -23.7% | -22.3% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | preg_match() | 0.252 | 0.273 | +8.6% | +7.0% | +10.4% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | strtr() | 67.292 | 180.876 | +168.7% | +167.1% | +171.6% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace_callback() | 4.588 | 180.876 | +3836.0% | +3819.9% | +3879.7% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | str_replace() | 136.463 | 180.876 | +32.6% | +31.2% | +33.8% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace() | 4.185 | 180.876 | +4222.3% | +4193.6% | +4271.2% |
