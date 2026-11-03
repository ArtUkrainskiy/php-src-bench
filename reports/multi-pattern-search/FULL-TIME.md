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
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.343 | 6.345 | +1750.7% | +1745.2% | +1760.3% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.261 | 6.345 | +403.4% | +401.8% | +406.8% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.281 | 6.199 | +2106.4% | +2083.3% | +2126.9% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.161 | 6.199 | +433.3% | +426.2% | +437.9% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.308 | 6.393 | +1976.1% | +1961.7% | +1981.2% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.315 | 6.393 | +385.9% | +385.1% | +387.5% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.286 | 6.401 | +2136.4% | +2119.6% | +2179.5% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.333 | 6.401 | +380.2% | +377.9% | +381.4% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.055 | 7.483 | +609.0% | +607.1% | +611.6% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2.208 | 7.483 | +239.5% | +235.8% | +241.1% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.605 | 6.705 | +1008.8% | +1002.2% | +1014.1% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.560 | 6.705 | +329.6% | +328.0% | +332.6% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.285 | 10.987 | +754.7% | +748.4% | +758.9% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.705 | 10.987 | +544.2% | +541.4% | +547.1% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.455 | 10.801 | +641.9% | +639.3% | +645.3% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.349 | 10.801 | +700.6% | +695.9% | +704.3% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 2.096 | 11.095 | +429.3% | +427.5% | +430.6% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.890 | 11.095 | +487.6% | +479.9% | +491.9% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.436 | 11.093 | +672.5% | +669.8% | +676.0% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.909 | 11.093 | +481.2% | +473.8% | +485.9% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 3.620 | 12.859 | +255.3% | +254.3% | +256.0% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5.195 | 12.859 | +147.6% | +145.2% | +148.2% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 2.018 | 11.606 | +474.7% | +472.4% | +476.4% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2.790 | 11.606 | +315.9% | +313.7% | +317.3% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.361 | 11.036 | +2959.6% | +2938.2% | +3020.0% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.282 | 11.036 | +760.8% | +755.5% | +764.4% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.298 | 10.990 | +3594.0% | +3581.7% | +3616.6% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.151 | 10.990 | +855.7% | +852.2% | +860.3% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.376 | 11.120 | +2857.8% | +2847.1% | +2874.7% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.327 | 11.120 | +738.3% | +735.2% | +740.9% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.325 | 11.083 | +3307.5% | +3294.6% | +3344.2% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.347 | 11.083 | +722.4% | +720.2% | +730.4% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.582 | 11.745 | +642.5% | +640.2% | +646.9% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2.671 | 11.745 | +339.6% | +336.0% | +341.3% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.949 | 11.238 | +1084.9% | +1080.7% | +1114.7% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.685 | 11.238 | +566.9% | +562.7% | +568.2% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 4.259 | 8.005 | +87.9% | +87.4% | +88.4% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 3.494 | 8.005 | +129.1% | +127.6% | +129.8% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 2.140 | 5.608 | +161.9% | +161.1% | +162.9% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 0.938 | 5.608 | +497.6% | +494.7% | +500.8% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 2.398 | 6.904 | +187.8% | +187.2% | +189.5% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 2.142 | 6.904 | +222.2% | +221.2% | +223.8% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 2.609 | 8.043 | +208.1% | +207.1% | +208.8% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 3.197 | 8.043 | +151.5% | +149.4% | +152.3% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | strtr() | 0.962 | 4.800 | +399.5% | +394.4% | +402.4% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | preg_replace_callback() | 4.020 | 4.800 | +19.2% | +18.9% | +20.5% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | str_replace() | 3.090 | 4.800 | +55.2% | +54.6% | +56.5% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | strtr() | 1.403 | 5.562 | +296.5% | +295.1% | +297.1% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | preg_replace_callback() | 5.084 | 5.562 | +9.4% | +9.2% | +10.4% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | str_replace() | 3.935 | 5.562 | +41.3% | +40.7% | +42.3% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 0.335 | 2.048 | +510.6% | +505.8% | +516.2% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 1.837 | 2.048 | +11.4% | +11.1% | +11.8% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 1.290 | 2.048 | +58.8% | +57.6% | +59.3% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 2.085 | 5.239 | +151.4% | +150.1% | +152.8% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 4.503 | 5.239 | +16.5% | +15.8% | +16.9% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 2.768 | 5.239 | +89.7% | +87.6% | +90.4% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 0.198 | 1.526 | +671.9% | +666.0% | +681.4% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 1.122 | 1.526 | +35.9% | +35.2% | +36.7% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 0.993 | 1.526 | +53.6% | +52.5% | +54.2% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 0.296 | 1.703 | +474.2% | +471.3% | +479.3% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 1.543 | 1.703 | +10.4% | +9.8% | +12.0% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 1.164 | 1.703 | +46.5% | +45.2% | +48.0% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | strtr() | 0.209 | 0.923 | +340.3% | +338.0% | +343.4% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace_callback() | 1.128 | 0.923 | -18.1% | -18.7% | -17.9% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | str_replace() | 0.836 | 0.923 | +10.6% | +9.8% | +11.6% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace() | 0.887 | 0.923 | +4.1% | +3.3% | +5.0% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 0.345 | 7.809 | +2165.5% | +2155.0% | +2174.9% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 2.331 | 7.809 | +234.9% | +233.4% | +237.0% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 1.435 | 7.809 | +445.0% | +442.5% | +452.1% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 0.426 | 8.031 | +1781.9% | +1769.3% | +1793.7% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 2.523 | 8.031 | +218.3% | +214.7% | +220.3% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 1.588 | 8.031 | +405.1% | +402.1% | +407.9% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 2.838 | 11.071 | +290.8% | +287.6% | +292.1% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 4.642 | 11.071 | +138.5% | +137.6% | +142.1% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 3.581 | 11.071 | +209.2% | +207.5% | +213.4% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 5.926 | 25.404 | +328.7% | +327.6% | +329.3% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 6.821 | 25.404 | +272.3% | +271.2% | +273.5% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 15.754 | 25.404 | +61.2% | +60.6% | +61.7% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 6.711 | 25.404 | +278.3% | +276.6% | +280.4% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 6.075 | 26.576 | +337.1% | +335.8% | +338.7% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 7.122 | 26.576 | +272.5% | +271.0% | +274.8% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 16.560 | 26.576 | +60.5% | +59.4% | +61.0% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 6.928 | 26.576 | +283.2% | +281.3% | +285.6% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 9.168 | 32.843 | +258.2% | +256.8% | +258.9% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 7.649 | 32.843 | +329.1% | +322.5% | +334.3% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 24.146 | 32.843 | +36.1% | +35.0% | +36.7% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 7.223 | 32.843 | +354.8% | +345.7% | +359.6% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 72.363 | 152.875 | +111.1% | +110.2% | +112.8% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 10.782 | 152.875 | +1318.4% | +1311.4% | +1328.0% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 151.393 | 152.875 | +0.9% | +0.5% | +1.2% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 10.311 | 152.875 | +1383.2% | +1371.4% | +1393.7% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 0.193 | 1.469 | +660.8% | +655.3% | +675.8% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 2.010 | 1.469 | -26.8% | -27.4% | -25.0% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 1.779 | 1.469 | -17.4% | -18.4% | -14.7% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 0.235 | 1.550 | +560.9% | +555.8% | +570.8% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 2.169 | 1.550 | -28.5% | -28.9% | -27.3% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 1.841 | 1.550 | -15.8% | -16.2% | -14.1% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 12.204 | 33.238 | +172.3% | +169.4% | +174.2% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | preg_match() per term | 22.162 | 33.238 | +50.0% | +48.7% | +51.3% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 10.189 | 33.028 | +223.8% | +220.6% | +227.1% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 31.121 | 33.028 | +6.0% | +4.8% | +8.8% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 15.344 | 33.438 | +117.4% | +116.1% | +119.3% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 47.078 | 33.438 | -29.0% | -29.3% | -28.7% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 29.423 | 32.968 | +12.0% | +11.3% | +12.5% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 35.597 | 32.968 | -7.1% | -8.0% | -5.5% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 234.652 | 43.329 | -81.5% | -81.6% | -81.4% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 98.183 | 43.329 | -55.9% | -56.0% | -55.7% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.368 | 5.961 | +1521.6% | +1516.8% | +1584.5% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.329 | 5.961 | +348.6% | +334.7% | +352.2% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.288 | 6.178 | +2046.3% | +2022.4% | +2063.0% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.259 | 6.178 | +389.7% | +375.6% | +405.7% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.310 | 6.071 | +1855.9% | +1837.5% | +1875.5% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.376 | 6.071 | +341.1% | +330.3% | +344.5% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.283 | 6.090 | +2050.8% | +2017.0% | +2109.1% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.444 | 6.090 | +321.7% | +309.3% | +326.7% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.089 | 7.261 | +566.3% | +564.8% | +568.1% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2.454 | 7.261 | +195.7% | +193.2% | +199.8% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.597 | 6.401 | +972.1% | +965.9% | +974.1% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.645 | 6.401 | +289.0% | +286.7% | +291.3% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.356 | 10.314 | +660.5% | +656.6% | +669.8% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.711 | 10.314 | +503.4% | +491.1% | +508.3% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.509 | 10.277 | +581.2% | +577.6% | +582.8% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.311 | 10.277 | +683.4% | +680.3% | +692.8% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 2.147 | 10.499 | +389.2% | +388.0% | +390.6% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.871 | 10.499 | +461.3% | +456.2% | +465.0% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.470 | 10.466 | +611.4% | +602.3% | +614.6% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.887 | 10.466 | +453.7% | +446.3% | +457.0% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 3.405 | 12.510 | +267.4% | +266.2% | +269.0% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5.235 | 12.510 | +138.9% | +137.5% | +140.1% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.929 | 11.000 | +469.9% | +468.1% | +472.1% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2.787 | 11.000 | +294.4% | +292.2% | +296.0% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.375 | 10.643 | +2735.4% | +2716.2% | +2756.1% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.352 | 10.643 | +686.9% | +682.0% | +698.8% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.298 | 10.881 | +3546.5% | +3520.4% | +3592.9% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.196 | 10.881 | +809.5% | +790.9% | +816.6% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.373 | 10.728 | +2778.3% | +2749.2% | +2787.5% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.389 | 10.728 | +671.9% | +666.4% | +674.5% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.327 | 10.766 | +3184.9% | +3151.6% | +3215.8% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.381 | 10.766 | +680.0% | +675.3% | +687.5% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.615 | 11.228 | +595.2% | +592.5% | +598.9% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2.753 | 11.228 | +307.9% | +305.0% | +309.9% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.938 | 10.902 | +1062.6% | +1057.4% | +1070.0% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.737 | 10.902 | +526.5% | +522.2% | +539.1% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 3.983 | 7.732 | +94.0% | +92.5% | +95.3% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 3.202 | 7.732 | +141.3% | +139.1% | +142.5% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 1.975 | 5.280 | +167.0% | +165.9% | +168.0% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 0.862 | 5.280 | +512.5% | +508.3% | +517.6% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 2.220 | 6.380 | +187.4% | +184.4% | +189.8% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 2.045 | 6.380 | +212.2% | +209.8% | +214.4% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 2.439 | 7.647 | +213.6% | +211.8% | +215.0% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 3.120 | 7.647 | +145.2% | +141.9% | +146.7% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | strtr() | 0.865 | 4.271 | +393.2% | +386.7% | +396.4% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | preg_replace_callback() | 4.120 | 4.271 | +3.8% | +3.2% | +4.1% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | str_replace() | 3.024 | 4.271 | +41.3% | +39.6% | +41.8% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | strtr() | 1.301 | 5.040 | +286.5% | +283.1% | +291.9% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | preg_replace_callback() | 5.211 | 5.040 | -3.4% | -4.5% | -2.4% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | str_replace() | 3.934 | 5.040 | +28.1% | +26.9% | +29.7% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 0.301 | 1.887 | +526.9% | +523.8% | +535.5% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 1.843 | 1.887 | +2.3% | +1.8% | +2.8% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 1.292 | 1.887 | +46.0% | +44.7% | +46.5% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 1.892 | 4.444 | +134.5% | +132.3% | +137.3% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 4.575 | 4.444 | -2.9% | -4.1% | -1.9% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 2.719 | 4.444 | +63.3% | +61.6% | +64.8% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 0.170 | 1.458 | +759.7% | +755.5% | +766.3% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 1.076 | 1.458 | +35.9% | +34.5% | +37.5% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 0.970 | 1.458 | +50.0% | +47.3% | +52.5% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 0.271 | 1.643 | +505.7% | +498.4% | +514.6% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 1.516 | 1.643 | +7.9% | +7.4% | +10.1% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 1.124 | 1.643 | +46.1% | +45.4% | +48.6% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | strtr() | 0.196 | 0.759 | +286.5% | +284.6% | +292.4% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace_callback() | 1.078 | 0.759 | -29.7% | -30.0% | -29.2% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | str_replace() | 0.790 | 0.759 | -3.9% | -5.0% | -2.9% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace() | 0.860 | 0.759 | -11.8% | -12.2% | -10.7% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 0.311 | 7.343 | +2259.5% | +2216.6% | +2282.1% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 2.531 | 7.343 | +190.5% | +186.8% | +193.0% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 1.443 | 7.343 | +408.8% | +405.3% | +412.9% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 0.401 | 7.577 | +1787.5% | +1778.7% | +1794.1% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 2.822 | 7.577 | +168.4% | +166.0% | +171.1% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 1.766 | 7.577 | +329.0% | +314.5% | +342.7% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 2.727 | 10.162 | +273.2% | +271.4% | +277.1% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 4.985 | 10.162 | +103.8% | +101.8% | +106.2% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 3.593 | 10.162 | +182.7% | +181.5% | +185.1% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 5.372 | 20.399 | +279.4% | +278.2% | +280.9% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 6.104 | 20.399 | +234.2% | +232.5% | +237.7% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 14.983 | 20.399 | +36.1% | +35.6% | +36.5% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 5.987 | 20.399 | +240.5% | +239.2% | +244.6% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 5.537 | 21.836 | +294.3% | +291.5% | +295.1% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 6.376 | 21.836 | +242.3% | +241.0% | +245.3% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 15.727 | 21.836 | +38.7% | +37.9% | +39.3% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 6.145 | 21.836 | +255.3% | +253.8% | +258.0% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 8.389 | 26.541 | +216.3% | +213.8% | +217.9% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 6.944 | 26.541 | +282.5% | +281.1% | +286.7% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 22.833 | 26.541 | +16.2% | +15.3% | +17.0% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 6.521 | 26.541 | +306.9% | +305.4% | +311.7% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 66.159 | 110.524 | +67.0% | +66.3% | +67.6% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 10.187 | 110.524 | +986.7% | +978.2% | +989.8% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 141.774 | 110.524 | -22.0% | -22.4% | -21.7% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 9.681 | 110.524 | +1042.9% | +1032.9% | +1047.4% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 0.161 | 1.427 | +784.1% | +763.1% | +791.3% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 2.055 | 1.427 | -30.5% | -30.9% | -30.1% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 1.750 | 1.427 | -18.4% | -19.0% | -17.9% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 0.202 | 1.497† | +640.0% | +624.1% | +713.7% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 2.161 | 1.497† | -30.9% | -32.4% | -24.2% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 1.837 | 1.497† | -18.3% | -20.2% | -16.1% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 12.467 | 31.842 | +155.8% | +153.8% | +157.1% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | preg_match() per term | 21.605 | 31.842 | +47.2% | +45.2% | +48.6% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 10.977 | 31.514 | +187.0% | +184.3% | +190.3% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 29.480 | 31.514 | +6.8% | +5.9% | +11.6% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 15.137 | 32.723 | +116.1% | +115.2% | +119.6% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 46.196 | 32.723 | -29.1% | -29.6% | -28.6% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 29.441 | 32.127 | +9.2% | +8.7% | +9.5% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 34.386 | 32.127 | -6.6% | -7.0% | -5.7% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 235.303 | 42.723 | -81.8% | -81.9% | -81.8% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 99.166 | 42.723 | -56.9% | -57.1% | -56.7% |

#### Dictionary already prepared

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.348 | 0.234 | -32.9% | -33.3% | -32.2% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.255 | 0.234 | -8.6% | -8.9% | -6.9% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.282 | 0.146 | -48.2% | -49.1% | -47.3% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.171 | 0.146 | -14.5% | -15.4% | -14.0% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.309 | 0.314 | +1.6% | +1.0% | +2.3% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.312 | 0.314 | +0.7% | +0.4% | +1.0% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.293 | 0.342 | +16.6% | +16.3% | +20.1% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.328 | 0.342 | +4.3% | +3.0% | +6.0% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.064 | 1.325 | +24.5% | +24.0% | +25.1% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.190 | 1.325 | +11.6% | +10.5% | +12.8% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.598 | 0.601 | +0.4% | -0.1% | +1.4% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.541 | 0.601 | +11.1% | +10.0% | +12.0% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.296 | 0.337 | -74.0% | -74.1% | -73.9% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.537 | 0.337 | -37.2% | -37.4% | -36.9% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.456 | 0.172 | -88.2% | -88.2% | -88.0% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.178 | 0.172 | -3.2% | -3.8% | -2.2% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 2.099 | 0.467 | -77.8% | -77.9% | -77.7% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.733 | 0.467 | -36.3% | -36.6% | -35.8% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.443 | 0.460 | -68.2% | -68.3% | -68.0% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.739 | 0.460 | -37.8% | -38.2% | -37.5% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 3.602 | 2.276 | -36.9% | -37.4% | -36.5% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 4.017 | 2.276 | -43.3% | -43.6% | -43.1% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 2.014 | 0.981 | -51.3% | -51.7% | -51.0% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.630 | 0.981 | -39.7% | -40.2% | -39.2% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.352 | 0.181 | -48.5% | -48.9% | -47.8% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.287 | 0.181 | -36.8% | -37.0% | -36.6% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.297 | 0.148 | -50.1% | -51.5% | -49.8% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.167 | 0.148 | -11.6% | -12.2% | -11.3% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.384 | 0.235 | -38.9% | -39.5% | -38.4% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.339 | 0.235 | -30.7% | -32.3% | -30.0% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.325 | 0.232 | -28.8% | -29.5% | -28.6% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.347 | 0.232 | -33.4% | -34.3% | -33.1% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.583 | 0.759 | -52.0% | -52.2% | -51.7% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.681 | 0.759 | -54.8% | -55.4% | -54.1% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.930 | 0.396 | -57.5% | -58.3% | -57.3% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.674 | 0.396 | -41.2% | -42.9% | -40.2% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 4.264 | 2.659 | -37.7% | -38.0% | -37.3% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 2.778 | 2.659 | -4.2% | -4.6% | -3.7% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 2.141 | 0.254 | -88.1% | -88.2% | -88.0% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 0.251 | 0.254 | +1.6% | +0.5% | +2.4% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 2.393 | 1.531 | -36.1% | -36.6% | -35.7% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 1.448 | 1.531 | +5.7% | +4.7% | +6.3% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 2.608 | 2.644 | +1.4% | +0.8% | +1.9% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 2.582 | 2.644 | +2.5% | +1.5% | +3.1% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 0.337 | 0.549 | +63.0% | +61.3% | +63.9% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 0.485 | 0.549 | +13.2% | +12.4% | +13.7% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 0.306 | 0.549 | +79.4% | +78.6% | +80.0% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 2.084 | 3.746 | +79.5% | +77.5% | +82.1% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 3.099 | 3.746 | +20.9% | +20.1% | +21.8% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 1.759 | 3.746 | +113.2% | +111.2% | +114.3% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 0.200 | 0.259 | +29.6% | +28.9% | +30.7% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 0.170 | 0.259 | +52.3% | +52.0% | +52.7% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 0.190 | 0.259 | +36.7% | +36.0% | +37.0% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 0.295 | 0.420 | +42.4% | +41.8% | +42.8% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 0.557 | 0.420 | -24.7% | -24.9% | -23.9% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 0.330 | 0.420 | +27.2% | +26.6% | +27.5% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | strtr() | 0.212 | 0.242 | +14.3% | +13.3% | +14.6% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace_callback() | 0.375 | 0.242 | -35.4% | -35.6% | -35.3% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | str_replace() | 0.218 | 0.242 | +11.1% | +10.2% | +11.4% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace() | 0.207 | 0.242 | +16.8% | +16.5% | +17.5% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 0.346 | 0.296 | -14.3% | -14.9% | -13.4% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 0.194 | 0.296 | +53.1% | +51.7% | +54.7% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 0.250 | 0.296 | +18.5% | +17.9% | +19.5% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 0.426 | 0.479 | +12.4% | +12.0% | +12.7% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 0.388 | 0.479 | +23.3% | +23.0% | +23.6% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 0.378 | 0.479 | +26.8% | +25.6% | +27.2% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 2.831 | 3.136 | +10.9% | +10.2% | +11.2% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 2.400 | 3.136 | +30.5% | +30.1% | +31.4% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 2.325 | 3.136 | +35.0% | +34.1% | +35.3% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 5.958 | 10.433 | +75.1% | +73.4% | +76.8% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 0.493 | 10.433 | +2015.2% | +2007.8% | +2031.0% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 11.280 | 10.433 | -7.5% | -8.1% | -7.3% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 0.471 | 10.433 | +2111.3% | +2099.8% | +2135.3% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 6.100 | 11.434 | +87.4% | +86.6% | +88.4% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 0.728 | 11.434 | +1469.2% | +1462.5% | +1481.6% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 12.013 | 11.434 | -4.8% | -5.3% | -4.3% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 0.585 | 11.434 | +1856.5% | +1844.0% | +1877.5% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 9.252 | 17.782 | +92.1% | +91.4% | +92.6% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 1.143 | 17.782 | +1455.1% | +1449.0% | +1459.2% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 19.567 | 17.782 | -9.2% | -9.7% | -8.7% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 0.815 | 17.782 | +2081.7% | +2064.5% | +2094.7% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 72.800 | 137.312 | +88.6% | +87.6% | +89.3% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 4.341 | 137.312 | +3059.3% | +3046.3% | +3070.8% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 146.896 | 137.312 | -6.6% | -7.2% | -6.3% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 3.946 | 137.312 | +3378.7% | +3355.2% | +3392.1% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 0.190 | 0.215 | +13.0% | +12.6% | +13.4% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 0.186 | 0.215 | +15.4% | +14.8% | +16.0% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 0.225 | 0.215 | -4.6% | -4.8% | -4.2% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 0.235 | 0.275 | +17.3% | +16.9% | +17.9% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 0.330 | 0.275 | -16.7% | -17.0% | -16.3% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 0.273 | 0.275 | +0.8% | +0.3% | +1.3% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 12.264 | 1.499 | -87.8% | -87.9% | -87.7% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | preg_match() per term | 14.961 | 1.499 | -90.0% | -90.0% | -90.0% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 10.280 | 1.006 | -90.2% | -90.3% | -90.1% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 17.844 | 1.006 | -94.4% | -94.5% | -94.3% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 15.145 | 1.805 | -88.1% | -88.4% | -88.0% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 34.594 | 1.805 | -94.8% | -94.8% | -94.7% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 29.424 | 1.437 | -95.1% | -95.1% | -95.1% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 9.079 | 1.437 | -84.2% | -84.2% | -84.1% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 234.706 | 11.050 | -95.3% | -95.3% | -95.3% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 71.887 | 11.050 | -84.6% | -84.7% | -84.6% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.365 | 0.243 | -33.5% | -34.2% | -31.2% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.251 | 0.243 | -3.6% | -5.0% | -1.7% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.282 | 0.141 | -50.1% | -50.9% | -48.9% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.155 | 0.141 | -9.2% | -12.1% | -7.8% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.312 | 0.325 | +4.0% | +3.3% | +4.6% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.310 | 0.325 | +4.9% | +4.1% | +5.7% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.288 | 0.359 | +24.8% | +24.1% | +27.3% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.322 | 0.359 | +11.5% | +9.5% | +12.3% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.087 | 1.492 | +37.3% | +36.7% | +38.4% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.376 | 1.492 | +8.4% | +7.6% | +10.3% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.603 | 0.658 | +9.2% | +8.7% | +9.6% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.564 | 0.658 | +16.9% | +15.2% | +17.4% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.310 | 0.354 | -72.9% | -73.1% | -72.6% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.526 | 0.354 | -32.6% | -32.9% | -31.8% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.478 | 0.166 | -88.8% | -88.8% | -88.7% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.159 | 0.166 | +4.3% | +3.4% | +5.6% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 2.158 | 0.490 | -77.3% | -77.3% | -77.2% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.712 | 0.490 | -31.2% | -31.8% | -30.9% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.482 | 0.491 | -66.8% | -67.0% | -66.6% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.730 | 0.491 | -32.7% | -33.4% | -32.3% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 3.388 | 2.536 | -25.2% | -25.7% | -24.6% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 4.075 | 2.536 | -37.8% | -38.2% | -37.4% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.923 | 1.047 | -45.6% | -46.0% | -45.3% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.630 | 1.047 | -35.8% | -36.1% | -35.5% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.378 | 0.169 | -55.5% | -55.8% | -54.2% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.284 | 0.169 | -40.5% | -41.6% | -39.0% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.297 | 0.139 | -53.5% | -53.8% | -53.0% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.153 | 0.139 | -9.7% | -11.5% | -9.0% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.391 | 0.228 | -41.6% | -42.3% | -40.9% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.325 | 0.228 | -30.1% | -31.6% | -28.5% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.330 | 0.227 | -30.9% | -31.5% | -30.5% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.346 | 0.227 | -34.2% | -35.6% | -32.7% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1.608 | 0.751 | -53.3% | -53.6% | -52.6% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1.732 | 0.751 | -56.2% | -57.1% | -55.9% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 0.939 | 0.389 | -58.5% | -58.8% | -58.1% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 0.679 | 0.389 | -42.7% | -43.7% | -40.7% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 4.111 | 2.389 | -41.9% | -42.3% | -41.6% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 2.619 | 2.389 | -8.5% | -9.6% | -7.0% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 1.977 | 0.214 | -89.2% | -89.2% | -89.0% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 0.228 | 0.214 | -6.1% | -7.2% | -4.6% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 2.241 | 1.321 | -41.1% | -41.4% | -40.8% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 1.453 | 1.321 | -9.0% | -10.0% | -8.2% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 2.418 | 2.287 | -5.5% | -6.0% | -5.0% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 2.473 | 2.287 | -7.5% | -8.6% | -5.4% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 0.298 | 0.438 | +47.0% | +45.8% | +48.1% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 0.493 | 0.438 | -11.3% | -12.5% | -9.9% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 0.295 | 0.438 | +48.2% | +46.5% | +49.8% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 1.903 | 2.939 | +54.5% | +52.6% | +55.8% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 3.197 | 2.939 | -8.2% | -9.1% | -6.9% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 1.688 | 2.939 | +73.9% | +71.9% | +76.4% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 0.174 | 0.173 | -0.1% | -2.5% | +0.6% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 0.161 | 0.173 | +7.5% | +6.7% | +8.5% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 0.172 | 0.173 | +0.5% | -1.3% | +1.8% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 0.272 | 0.307 | +13.2% | +10.4% | +14.4% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 0.552 | 0.307 | -44.4% | -46.5% | -43.5% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 0.313 | 0.307 | -1.9% | -7.1% | -0.5% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | strtr() | 0.188 | 0.188 | +0.0% | -1.7% | +1.3% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace_callback() | 0.367 | 0.188 | -48.7% | -49.3% | -48.1% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | str_replace() | 0.205 | 0.188 | -8.2% | -9.5% | -7.2% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace() | 0.195 | 0.188 | -3.4% | -4.9% | -2.1% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 0.312 | 0.249 | -20.2% | -20.9% | -19.6% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 0.187 | 0.249 | +33.6% | +32.5% | +34.1% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 0.237 | 0.249 | +5.0% | +3.5% | +5.8% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 0.398 | 0.412 | +3.3% | +2.1% | +4.2% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 0.392 | 0.412 | +5.3% | +4.1% | +6.1% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 0.376 | 0.412 | +9.3% | +8.6% | +10.1% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 2.702 | 2.745 | +1.5% | +0.5% | +2.7% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 2.533 | 2.745 | +8.2% | +7.1% | +9.4% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 2.324 | 2.745 | +17.8% | +16.7% | +19.1% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 5.375 | 6.542 | +21.7% | +20.8% | +23.6% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 0.479 | 6.542 | +1273.3% | +1249.8% | +1286.0% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 10.466 | 6.542 | -37.5% | -37.9% | -36.6% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 0.454 | 6.542 | +1342.0% | +1322.0% | +1359.6% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 5.540 | 7.884 | +42.2% | +41.0% | +43.6% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 0.714 | 7.884 | +1002.9% | +994.2% | +1017.1% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 11.153 | 7.884 | -29.3% | -30.0% | -28.6% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 0.567 | 7.884 | +1291.1% | +1273.3% | +1306.4% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 8.407 | 12.500 | +48.8% | +46.6% | +49.6% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 1.168 | 12.500 | +970.0% | +955.9% | +976.3% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 18.182 | 12.500 | -31.3% | -32.3% | -30.8% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 0.819 | 12.500 | +1427.9% | +1404.9% | +1438.5% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 66.188 | 95.870 | +44.8% | +43.6% | +45.6% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 4.441 | 95.870 | +2059.9% | +2048.3% | +2070.2% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 137.212 | 95.870 | -30.2% | -30.4% | -29.9% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 3.999 | 95.870 | +2298.1% | +2280.7% | +2314.9% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 0.164 | 0.153 | -6.9% | -8.0% | -6.1% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 0.175 | 0.153 | -12.7% | -13.9% | -12.1% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 0.203 | 0.153 | -24.7% | -25.7% | -24.4% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 0.213 | 0.227 | +6.5% | +3.7% | +9.8% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 0.325 | 0.227 | -30.0% | -31.5% | -28.1% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 0.265 | 0.227 | -13.8% | -16.3% | -11.8% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 12.445 | 1.531 | -87.7% | -87.7% | -87.6% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | preg_match() per term | 14.811 | 1.531 | -89.7% | -89.7% | -89.6% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 10.611 | 1.079 | -89.8% | -90.5% | -89.8% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 17.785 | 1.079 | -93.9% | -94.4% | -93.8% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 15.657 | 2.011 | -87.1% | -87.2% | -87.1% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 35.611 | 2.011 | -94.4% | -94.4% | -94.3% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 29.429 | 1.452 | -95.1% | -95.1% | -95.1% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 9.293 | 1.452 | -84.4% | -84.4% | -84.3% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 235.289 | 11.092 | -95.3% | -95.3% | -95.3% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 73.794 | 11.092 | -85.0% | -85.0% | -84.9% |

### Synthetic tasks

#### Dictionary preparation included

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 0.381 | 86.830 | +22701.3% | +22672.9% | +22764.6% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 18.763 | 86.830 | +362.9% | +361.6% | +369.5% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 18.419 | 86.830 | +371.5% | +370.1% | +376.8% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 0.310 | 17.307 | +5491.7% | +5469.0% | +5531.4% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 18.635 | 17.307 | -7.1% | -8.1% | -4.8% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 18.348 | 17.307 | -5.6% | -5.9% | -4.4% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | strtr() | 0.307 | 1.348 | +340.1% | +337.0% | +343.4% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace_callback() | 4.926 | 1.348 | -72.7% | -72.8% | -72.4% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace() | 4.124 | 1.348 | -67.2% | -67.4% | -67.0% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | strtr() | 0.254 | 1.036 | +307.3% | +305.5% | +309.2% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | preg_replace_callback() | 1.353 | 1.036 | -23.4% | -24.0% | -23.1% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 0.372 | 82.482 | +22066.6% | +22021.5% | +22112.2% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 19.590 | 82.482 | +320.9% | +317.3% | +325.6% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 19.333 | 82.482 | +326.8% | +321.9% | +331.8% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 0.295 | 15.933 | +5302.1% | +5277.7% | +5331.3% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 19.957 | 15.933 | -20.2% | -20.5% | -19.8% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 19.681 | 15.933 | -19.0% | -19.4% | -18.7% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | strtr() | 0.277 | 1.332 | +381.1% | +377.1% | +383.5% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace_callback() | 5.043 | 1.332 | -73.5% | -73.8% | -73.4% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace() | 4.124 | 1.332 | -67.6% | -67.9% | -67.5% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | strtr() | 0.232 | 0.993 | +327.9% | +324.0% | +332.4% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | preg_replace_callback() | 1.300 | 0.993 | -23.5% | -24.2% | -23.1% |

#### Dictionary already prepared

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 0.386 | 0.457 | +18.4% | +18.2% | +18.9% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 0.885 | 0.457 | -48.4% | -48.5% | -48.2% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 0.650 | 0.457 | -29.8% | -30.0% | -29.5% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 0.313 | 0.456 | +45.6% | +44.9% | +46.3% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 0.652 | 0.456 | -30.1% | -31.5% | -28.8% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 0.451 | 0.456 | +1.2% | +0.3% | +2.9% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | strtr() | 0.309 | 0.470 | +52.0% | +51.5% | +52.5% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace_callback() | 1.059 | 0.470 | -55.7% | -55.8% | -55.6% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace() | 0.331 | 0.470 | +42.1% | +41.6% | +42.3% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | strtr() | 0.261 | 0.241 | -7.8% | -8.1% | -6.1% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | preg_replace_callback() | 0.588 | 0.241 | -59.1% | -59.2% | -58.5% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 0.372 | 0.407 | +9.2% | +8.5% | +10.3% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 0.872 | 0.407 | -53.4% | -53.7% | -52.8% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 0.633 | 0.407 | -35.8% | -36.3% | -35.2% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 0.298 | 0.404 | +35.7% | +34.6% | +39.5% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 0.656 | 0.404 | -38.5% | -38.9% | -36.2% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 0.400 | 0.404 | +1.1% | -1.2% | +6.2% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | strtr() | 0.279 | 0.496 | +77.4% | +76.3% | +81.1% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace_callback() | 1.167 | 0.496 | -57.6% | -58.0% | -56.3% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace() | 0.320 | 0.496 | +54.7% | +54.2% | +58.1% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | strtr() | 0.233 | 0.194 | -16.7% | -17.2% | -16.2% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | preg_replace_callback() | 0.581 | 0.194 | -66.6% | -66.8% | -66.5% |

## Size series

### Product tasks

#### Dictionary preparation included

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 0.280 | 2.377 | +748.5% | +737.9% | +760.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 0.713 | 2.377 | +233.3% | +230.1% | +234.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | str_contains() loop | 0.202 | 2.450 | +1110.0% | +1072.8% | +1146.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | preg_match() | 0.651 | 2.450 | +275.0% | +265.7% | +287.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | str_contains() loop | 0.236 | 2.421 | +925.7% | +918.8% | +936.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | preg_match() | 0.770 | 2.421 | +214.6% | +212.4% | +219.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | str_contains() loop | 0.218 | 2.429 | +1014.4% | +1008.3% | +1024.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | preg_match() | 0.757 | 2.429 | +220.8% | +218.5% | +222.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 0.932 | 3.015 | +223.3% | +222.2% | +224.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 1.548 | 3.015 | +94.8% | +94.2% | +95.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | str_contains() loop | 0.384 | 2.579 | +571.4% | +569.8% | +573.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | preg_match() | 0.978 | 2.579 | +163.8% | +163.3% | +164.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 0.439 | 5.203 | +1085.6% | +1061.0% | +1100.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 1.246 | 5.203 | +317.4% | +315.3% | +321.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | str_contains() loop | 0.282 | 5.086 | +1700.4% | +1688.1% | +1746.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | preg_match() | 1.040 | 5.086 | +388.6% | +382.7% | +390.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | str_contains() loop | 0.333 | 5.270 | +1480.3% | +1475.2% | +1491.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | preg_match() | 1.303 | 5.270 | +304.7% | +303.9% | +307.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | str_contains() loop | 0.297 | 5.449 | +1734.0% | +1723.7% | +1771.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | preg_match() | 1.322 | 5.449 | +312.4% | +310.8% | +314.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 1.606 | 5.773 | +259.5% | +257.2% | +268.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 3.497 | 5.773 | +65.0% | +64.3% | +65.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | str_contains() loop | 0.568 | 5.334 | +839.8% | +833.6% | +848.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | preg_match() | 1.799 | 5.334 | +196.6% | +189.5% | +203.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 0.784 | 12.839 | +1537.9% | +1498.0% | +1572.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 2.524 | 12.839 | +408.8% | +407.1% | +410.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | str_contains() loop | 0.473 | 12.552 | +2552.1% | +2498.5% | +2574.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | preg_match() | 1.932 | 12.552 | +549.7% | +540.5% | +556.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | str_contains() loop | 0.573 | 12.769 | +2125.7% | +2093.6% | +2165.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | preg_match() | 2.702 | 12.769 | +372.6% | +370.8% | +374.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | str_contains() loop | 0.487 | 12.786 | +2528.3% | +2516.3% | +2594.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | preg_match() | 2.782 | 12.786 | +359.7% | +357.3% | +362.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 3.521 | 13.839 | +293.2% | +290.6% | +294.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 8.338 | 13.839 | +66.0% | +65.5% | +66.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | str_contains() loop | 1.309 | 13.073 | +898.8% | +867.5% | +903.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | preg_match() | 4.247 | 13.073 | +207.5% | +206.3% | +209.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 1.486 | 26.274 | +1667.0% | +1608.0% | +1702.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 4.893 | 26.274 | +436.6% | +434.5% | +438.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | str_contains() loop | 0.870 | 26.089 | +2900.2% | +2887.5% | +2964.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | preg_match() | 3.615 | 26.089 | +622.0% | +619.6% | +624.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | str_contains() loop | 1.091 | 26.319 | +2313.0% | +2303.8% | +2327.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | preg_match() | 5.325 | 26.319 | +394.8% | +393.3% | +396.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | str_contains() loop | 0.917 | 26.166 | +2753.0% | +2725.0% | +2785.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | preg_match() | 5.355 | 26.166 | +388.9% | +387.7% | +390.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 6.877 | 27.300 | +297.1% | +295.3% | +299.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 17.049 | 27.300 | +60.1% | +59.6% | +60.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | str_contains() loop | 2.835 | 26.526 | +836.0% | +831.2% | +846.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | preg_match() | 8.543 | 26.526 | +210.8% | +209.2% | +215.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 3.066 | 58.269 | +1808.5% | +1765.7% | +1901.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 9.877 | 58.269 | +489.5% | +479.5% | +521.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | str_contains() loop | 1.658 | 58.473 | +3421.1% | +3320.4% | +3514.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | preg_match() | 7.049 | 58.473 | +727.6% | +714.5% | +742.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | str_contains() loop | 2.122 | 57.947 | +2629.9% | +2594.1% | +2661.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | preg_match() | 10.412 | 57.947 | +456.9% | +447.8% | +459.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | str_contains() loop | 1.684 | 58.869 | +3396.4% | +3325.2% | +3472.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | preg_match() | 10.815 | 58.869 | +444.0% | +434.4% | +449.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 13.477 | 59.757 | +342.6% | +339.0% | +356.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 34.901 | 59.757 | +71.1% | +70.4% | +76.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | str_contains() loop | 5.446 | 58.466 | +973.6% | +967.5% | +981.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | preg_match() | 17.142 | 58.466 | +241.1% | +238.7% | +243.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 6.946 | 152.716 | +2101.3% | +2083.9% | +2124.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 19.905 | 152.716 | +667.6% | +661.6% | +675.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | str_contains() loop | 3.529 | 152.237 | +4212.0% | +4121.6% | +4331.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | preg_match() | 14.176 | 152.237 | +973.9% | +964.6% | +976.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | str_contains() loop | 4.640 | 153.093 | +3195.6% | +3152.3% | +3312.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | preg_match() | 20.822 | 153.093 | +634.9% | +633.5% | +639.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | str_contains() loop | 3.810 | 152.779 | +3912.4% | +3876.9% | +4186.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | preg_match() | 21.693 | 152.779 | +604.3% | +602.5% | +614.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 30.087 | 154.924 | +415.0% | +412.6% | +417.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 68.546 | 154.924 | +126.0% | +125.5% | +126.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | str_contains() loop | 11.470 | 153.393 | +1237.0% | +1233.1% | +1245.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | preg_match() | 34.020 | 153.393 | +350.9% | +349.5% | +352.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 16.053 | 295.062 | +1738.8% | +1711.8% | +1744.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 49.053 | 295.062 | +501.1% | +500.1% | +506.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | str_contains() loop | 8.704 | 295.204 | +3289.6% | +3273.0% | +3352.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | preg_match() | 27.670 | 295.204 | +966.5% | +961.4% | +980.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | str_contains() loop | 11.574 | 294.838 | +2449.9% | +2412.3% | +2479.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | preg_match() | 53.368 | 294.838 | +452.9% | +451.0% | +454.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | str_contains() loop | 8.667 | 294.903 | +3305.8% | +3265.9% | +3331.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | preg_match() | 53.440 | 294.903 | +451.8% | +449.8% | +455.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 68.197 | 295.950 | +334.4% | +332.6% | +335.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 233.702 | 295.950 | +26.7% | +24.6% | +27.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | str_contains() loop | 25.208 | 295.349 | +1072.0% | +1069.2% | +1082.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | preg_match() | 105.639 | 295.349 | +179.5% | +178.4% | +180.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 1.172 | 3.104 | +164.8% | +163.5% | +165.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | preg_match() per term | 2.136 | 3.104 | +45.3% | +44.6% | +46.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 0.959 | 3.045 | +217.8% | +216.3% | +219.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 2.365 | 3.045 | +28.8% | +28.0% | +29.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 1.458 | 3.129 | +114.6% | +113.8% | +115.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 3.765 | 3.129 | -16.9% | -17.1% | -16.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 2.165 | 5.075 | +134.5% | +133.0% | +135.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | preg_match() per term | 3.940 | 5.075 | +28.9% | +28.1% | +29.2% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 1.799 | 4.878 | +171.1% | +170.2% | +172.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 4.479 | 4.878 | +8.9% | +8.6% | +9.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 2.736 | 5.089 | +86.0% | +84.5% | +88.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 7.012 | 5.089 | -27.4% | -27.7% | -27.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 3.902 | 10.109 | +158.9% | +158.1% | +160.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | preg_match() per term | 7.576 | 10.109 | +33.3% | +33.1% | +33.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 3.195 | 9.030 | +182.9% | +181.2% | +183.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 8.322 | 9.030 | +8.6% | +8.1% | +8.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 5.176 | 9.427 | +81.9% | +81.1% | +86.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 13.219 | 9.427 | -28.7% | -29.0% | -28.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 7.966 | 20.066 | +152.1% | +150.7% | +153.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | preg_match() per term | 14.764 | 20.066 | +35.9% | +34.5% | +36.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 6.760 | 19.337 | +186.0% | +184.5% | +188.2% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 16.394 | 19.337 | +18.1% | +17.7% | +18.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 10.032 | 20.108 | +100.4% | +97.9% | +101.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 24.957 | 20.108 | -19.4% | -19.8% | -19.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 16.370 | 47.354 | +189.1% | +187.1% | +190.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | preg_match() per term | 28.618 | 47.354 | +65.5% | +63.9% | +66.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 14.250 | 47.142 | +231.1% | +226.7% | +237.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 49.375 | 47.142 | -4.6% | -5.1% | -3.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 19.077 | 48.032 | +151.9% | +149.5% | +153.3% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 66.015 | 48.032 | -27.3% | -27.7% | -26.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 31.955 | 134.225 | +319.9% | +317.9% | +321.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | preg_match() per term | 60.688 | 134.225 | +121.0% | +120.1% | +122.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 30.313 | 133.896 | +341.8% | +340.3% | +343.1% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 113.576 | 133.896 | +17.8% | +17.4% | +18.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 35.323 | 135.162 | +282.4% | +281.6% | +284.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 135.781 | 135.162 | -0.5% | -0.8% | -0.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 61.675 | 362.329 | +487.3% | +485.5% | +488.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | preg_match() per term | 134.538 | 362.329 | +169.3% | +168.5% | +169.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 60.819 | 353.678 | +481.3% | +480.3% | +483.2% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 238.058 | 353.678 | +48.6% | +48.2% | +49.0% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 65.807 | 356.366 | +441.6% | +440.6% | +442.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 275.499 | 356.366 | +29.4% | +29.0% | +29.6% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 4.463 | 3.603 | -19.3% | -20.4% | -18.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 2.262 | 3.603 | +59.4% | +57.5% | +59.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 34.699 | 11.025 | -68.2% | -68.8% | -67.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 6.470 | 11.025 | +70.2% | +69.5% | +71.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 7.893 | 6.168 | -21.9% | -22.4% | -21.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 5.383 | 6.168 | +14.7% | +14.1% | +15.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 62.801 | 14.123 | -77.5% | -77.6% | -77.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 18.641 | 14.123 | -24.3% | -24.7% | -24.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 16.843 | 10.672 | -36.8% | -37.1% | -36.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 10.735 | 10.672 | -1.1% | -1.6% | -0.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 133.789 | 19.233 | -85.6% | -85.6% | -85.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 37.026 | 19.233 | -48.0% | -48.1% | -48.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 31.181 | 20.033 | -35.8% | -35.9% | -35.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 23.194 | 20.033 | -13.6% | -13.8% | -11.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 248.587 | 29.567 | -88.1% | -88.1% | -88.1% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 71.056 | 29.567 | -58.4% | -58.5% | -58.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 38.064 | 46.884 | +23.1% | +22.0% | +23.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 47.387 | 46.884 | -1.1% | -1.7% | -0.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 303.461 | 60.375 | -80.1% | -80.2% | -80.0% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 123.556 | 60.375 | -51.1% | -51.3% | -50.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 41.730 | 115.259 | +176.3% | +174.3% | +179.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 113.529 | 115.259 | +1.5% | +0.8% | +2.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 332.546 | 131.304 | -60.5% | -60.7% | -60.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 270.081 | 131.304 | -51.4% | -52.1% | -51.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 42.546 | 292.481 | +587.1% | +585.4% | +588.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 264.934 | 292.481 | +10.4% | +10.2% | +10.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 339.594 | 309.953 | -8.7% | -8.9% | -8.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 760.028 | 309.953 | -59.2% | -59.5% | -59.1% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 0.288 | 2.381 | +730.7% | +723.0% | +750.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 0.680 | 2.381 | +250.1% | +248.4% | +259.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | str_contains() loop | 0.203 | 2.318 | +1044.8% | +1029.6% | +1055.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | preg_match() | 0.600 | 2.318 | +287.0% | +284.9% | +290.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | str_contains() loop | 0.237 | 2.439 | +928.6% | +912.6% | +946.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | preg_match() | 0.708 | 2.439 | +244.7% | +239.9% | +247.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | str_contains() loop | 0.212 | 2.452 | +1057.8% | +1049.2% | +1067.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | preg_match() | 0.728 | 2.452 | +236.5% | +234.6% | +239.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 0.942 | 2.940 | +212.0% | +210.8% | +213.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 1.461 | 2.940 | +101.3% | +99.9% | +102.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | str_contains() loop | 0.384 | 2.551 | +564.3% | +557.3% | +572.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | preg_match() | 0.924 | 2.551 | +176.2% | +173.9% | +178.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 0.459 | 5.000 | +988.3% | +963.2% | +991.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 1.262 | 5.000 | +296.7% | +290.9% | +301.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | str_contains() loop | 0.286 | 4.919 | +1622.5% | +1612.4% | +1668.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | preg_match() | 1.067 | 4.919 | +362.0% | +355.5% | +364.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | str_contains() loop | 0.336 | 5.082 | +1412.6% | +1402.1% | +1421.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | preg_match() | 1.297 | 5.082 | +291.9% | +286.0% | +296.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | str_contains() loop | 0.303 | 5.105 | +1584.1% | +1569.3% | +1592.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | preg_match() | 1.350 | 5.105 | +278.3% | +272.5% | +286.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 1.621 | 5.618 | +246.5% | +245.1% | +247.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 3.426 | 5.618 | +64.1% | +63.2% | +64.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | str_contains() loop | 0.559 | 5.235 | +836.9% | +826.7% | +839.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | preg_match() | 1.740 | 5.235 | +201.1% | +198.9% | +202.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 0.866 | 12.537 | +1348.6% | +1344.9% | +1392.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 2.561 | 12.537 | +389.7% | +384.5% | +391.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | str_contains() loop | 0.499 | 12.111 | +2326.4% | +2317.6% | +2340.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | preg_match() | 2.016 | 12.111 | +500.5% | +498.1% | +508.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | str_contains() loop | 0.609 | 12.233 | +1907.4% | +1895.2% | +1953.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | preg_match() | 2.743 | 12.233 | +346.3% | +343.2% | +353.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | str_contains() loop | 0.503 | 12.380 | +2361.0% | +2347.0% | +2367.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | preg_match() | 2.742 | 12.380 | +351.6% | +347.0% | +352.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 3.670 | 13.643 | +271.9% | +269.1% | +277.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 8.269 | 13.643 | +65.0% | +64.2% | +66.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | str_contains() loop | 1.320 | 12.584 | +854.6% | +847.7% | +865.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | preg_match() | 4.179 | 12.584 | +201.3% | +199.6% | +204.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 1.567 | 25.620 | +1535.4% | +1528.8% | +1592.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 5.033 | 25.620 | +408.5% | +401.7% | +412.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | str_contains() loop | 0.930 | 25.486 | +2640.7% | +2622.9% | +2649.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | preg_match() | 3.710 | 25.486 | +586.3% | +580.2% | +609.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | str_contains() loop | 1.159 | 25.738 | +2120.1% | +2118.0% | +2124.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | preg_match() | 5.357 | 25.738 | +380.9% | +374.8% | +383.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | str_contains() loop | 0.970 | 25.910 | +2572.7% | +2562.7% | +2580.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | preg_match() | 5.604 | 25.910 | +362.9% | +360.6% | +367.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 7.013 | 26.918 | +283.5% | +281.5% | +285.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 17.544 | 26.918 | +53.4% | +52.9% | +53.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | str_contains() loop | 2.857 | 26.002 | +809.6% | +806.3% | +812.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | preg_match() | 8.753 | 26.002 | +196.9% | +195.9% | +198.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 3.282 | 56.921 | +1634.1% | +1618.5% | +1661.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 10.033 | 56.921 | +467.4% | +463.0% | +473.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | str_contains() loop | 1.745 | 56.575 | +3139.9% | +3096.0% | +3149.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | preg_match() | 7.449 | 56.575 | +658.6% | +649.8% | +679.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | str_contains() loop | 2.220 | 56.228 | +2433.3% | +2415.7% | +2453.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | preg_match() | 10.603 | 56.228 | +430.3% | +424.9% | +445.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | str_contains() loop | 1.837 | 57.177 | +3008.0% | +2940.4% | +3048.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | preg_match() | 10.888 | 57.177 | +425.2% | +415.5% | +429.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 14.183 | 58.871 | +314.7% | +311.8% | +318.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 33.657 | 58.871 | +74.8% | +73.6% | +75.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | str_contains() loop | 5.531 | 57.254 | +935.9% | +929.3% | +942.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | preg_match() | 16.846 | 57.254 | +239.9% | +237.7% | +241.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 7.770 | 149.700 | +1827.3% | +1819.1% | +1861.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 20.214 | 149.700 | +640.6% | +632.9% | +650.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | str_contains() loop | 3.872 | 150.366 | +3780.0% | +3755.1% | +3812.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | preg_match() | 14.319 | 150.366 | +950.1% | +933.2% | +961.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | str_contains() loop | 5.285 | 150.085 | +2737.1% | +2713.7% | +2801.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | preg_match() | 22.804 | 150.085 | +557.7% | +550.4% | +562.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | str_contains() loop | 3.998 | 150.059 | +3648.6% | +3614.5% | +3695.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | preg_match() | 21.798 | 150.059 | +588.2% | +576.5% | +593.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 30.896 | 153.226 | +396.1% | +393.3% | +398.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 73.149 | 153.226 | +109.1% | +98.7% | +115.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | str_contains() loop | 11.650 | 150.268 | +1189.7% | +1186.0% | +1195.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | preg_match() | 34.202 | 150.268 | +340.1% | +338.7% | +343.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 17.434 | 293.707 | +1585.5% | +1573.7% | +1593.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 50.212 | 293.707 | +484.9% | +482.5% | +487.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | str_contains() loop | 9.531 | 292.175 | +2964.2% | +2954.5% | +2975.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | preg_match() | 29.281 | 292.175 | +897.3% | +891.4% | +901.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | str_contains() loop | 12.667 | 293.464 | +2216.6% | +2203.1% | +2225.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | preg_match() | 54.969 | 293.464 | +433.8% | +430.1% | +437.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | str_contains() loop | 9.538 | 293.552 | +2977.4% | +2963.0% | +3086.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | preg_match() | 57.627 | 293.552 | +409.6% | +406.4% | +411.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 71.708 | 303.130 | +322.9% | +320.8% | +323.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 233.298 | 303.130 | +29.9% | +29.2% | +30.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | str_contains() loop | 25.623 | 292.653 | +1041.5% | +1035.8% | +1051.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | preg_match() | 111.171 | 292.653 | +163.3% | +156.4% | +166.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 1.178 | 3.022 | +156.8% | +156.0% | +157.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | preg_match() per term | 2.011 | 3.022 | +50.5% | +49.5% | +51.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 0.996 | 2.887 | +189.7% | +188.8% | +191.6% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 2.257 | 2.887 | +28.0% | +27.7% | +28.6% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 1.446 | 3.284 | +127.1% | +125.5% | +128.0% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 3.597 | 3.284 | -8.7% | -9.0% | -8.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 2.192 | 4.848 | +121.2% | +120.6% | +122.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | preg_match() per term | 3.932 | 4.848 | +23.3% | +22.8% | +23.9% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 1.872 | 4.679 | +150.0% | +149.3% | +151.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 4.259 | 4.679 | +9.9% | +9.2% | +10.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 2.790 | 5.091 | +82.5% | +81.4% | +83.3% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 6.739 | 5.091 | -24.4% | -24.6% | -24.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 4.073 | 9.180 | +125.3% | +120.7% | +126.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | preg_match() per term | 7.428 | 9.180 | +23.5% | +21.2% | +23.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 3.415 | 8.658 | +153.3% | +152.1% | +155.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 8.202 | 8.658 | +5.5% | +4.7% | +7.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 5.258 | 9.141 | +74.0% | +73.1% | +75.3% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 12.662 | 9.141 | -27.8% | -28.3% | -27.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 8.192 | 19.083 | +132.8% | +131.3% | +134.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | preg_match() per term | 14.306 | 19.083 | +33.4% | +31.2% | +34.9% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 7.257 | 18.662 | +157.2% | +154.7% | +158.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 16.479 | 18.662 | +13.2% | +12.6% | +14.0% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 10.290 | 19.517 | +89.7% | +88.7% | +90.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 24.292 | 19.517 | -19.6% | -20.1% | -19.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 16.790 | 46.074 | +174.6% | +171.0% | +176.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | preg_match() per term | 27.920 | 46.074 | +65.1% | +64.0% | +66.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 14.357 | 45.894 | +219.9% | +216.1% | +223.2% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 48.732 | 45.894 | -5.7% | -6.6% | -5.0% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 19.863 | 45.654 | +129.9% | +128.8% | +131.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 64.418 | 45.654 | -29.2% | -29.7% | -28.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 32.932 | 129.482 | +293.1% | +292.0% | +294.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | preg_match() per term | 59.825 | 129.482 | +116.4% | +110.7% | +117.2% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 31.261 | 128.693 | +311.6% | +308.8% | +312.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 109.740 | 128.693 | +17.3% | +16.9% | +17.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 36.242 | 130.384 | +259.7% | +258.2% | +261.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 133.507 | 130.384 | -2.3% | -3.1% | -1.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 63.028 | 348.421 | +453.0% | +451.7% | +454.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | preg_match() per term | 131.120 | 348.421 | +165.9% | +165.0% | +166.9% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 61.660 | 347.195 | +463.0% | +459.8% | +464.9% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 231.790 | 347.195 | +49.8% | +49.5% | +50.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 66.977 | 349.338 | +421.7% | +419.8% | +422.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 268.343 | 349.338 | +30.2% | +29.8% | +30.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 4.318 | 3.479 | -19.4% | -20.3% | -18.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 2.188 | 3.479 | +59.0% | +58.4% | +59.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 34.040 | 10.508 | -69.2% | -69.7% | -68.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 6.410 | 10.508 | +63.9% | +63.5% | +64.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 7.861 | 5.940 | -24.5% | -24.8% | -23.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 5.085 | 5.940 | +16.6% | +15.6% | +17.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 62.761 | 13.716 | -78.2% | -78.3% | -78.0% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 18.434 | 13.716 | -25.5% | -25.9% | -24.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 16.754 | 10.145 | -39.5% | -39.6% | -39.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 10.482 | 10.145 | -3.2% | -3.4% | -2.0% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 133.367 | 18.878 | -85.8% | -85.9% | -85.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 36.551 | 18.878 | -48.3% | -48.6% | -48.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 31.365 | 19.495 | -37.8% | -38.1% | -37.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 22.563 | 19.495 | -13.5% | -13.8% | -12.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 249.928 | 28.919 | -88.4% | -88.5% | -88.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 70.469 | 28.919 | -59.0% | -59.2% | -58.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 38.490 | 45.110 | +17.2% | +16.4% | +18.6% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 47.048 | 45.110 | -4.1% | -5.0% | -2.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 307.487 | 58.276 | -81.0% | -81.1% | -81.0% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 129.183 | 58.276 | -54.8% | -55.0% | -54.6% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 42.219 | 112.640 | +166.6% | +162.9% | +167.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 107.227 | 112.640 | +4.7% | +3.4% | +6.0% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 336.553 | 129.027 | -61.7% | -61.8% | -61.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 261.552 | 129.027 | -50.7% | -51.0% | -50.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 43.034 | 288.989 | +571.4% | +567.5% | +573.4% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 265.663 | 288.989 | +8.7% | +8.2% | +9.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 343.415 | 306.901 | -10.7% | -10.8% | -10.3% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 718.674 | 306.901 | -57.3% | -57.4% | -57.0% |

#### Dictionary already prepared

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 0.287 | 0.188 | -34.6% | -34.8% | -33.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 0.239 | 0.188 | -21.4% | -21.6% | -21.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | str_contains() loop | 0.205 | 0.128 | -37.2% | -38.5% | -36.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | preg_match() | 0.161 | 0.128 | -20.1% | -20.6% | -19.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | str_contains() loop | 0.237 | 0.212 | -10.6% | -11.1% | -10.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | preg_match() | 0.278 | 0.212 | -23.6% | -24.0% | -22.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | str_contains() loop | 0.218 | 0.221 | +1.6% | +0.7% | +3.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | preg_match() | 0.275 | 0.221 | -19.9% | -20.2% | -19.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 0.935 | 0.811 | -13.3% | -13.8% | -12.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 1.066 | 0.811 | -23.9% | -24.6% | -23.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | str_contains() loop | 0.390 | 0.374 | -4.2% | -5.2% | -3.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | preg_match() | 0.497 | 0.374 | -24.7% | -25.3% | -24.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 0.438 | 0.189 | -56.8% | -57.3% | -56.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 0.349 | 0.189 | -45.8% | -46.0% | -45.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | str_contains() loop | 0.281 | 0.127 | -54.8% | -57.0% | -54.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | preg_match() | 0.165 | 0.127 | -23.2% | -23.7% | -22.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | str_contains() loop | 0.336 | 0.217 | -35.3% | -35.7% | -35.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | preg_match() | 0.422 | 0.217 | -48.5% | -48.9% | -47.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | str_contains() loop | 0.295 | 0.228 | -22.9% | -23.1% | -22.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | preg_match() | 0.447 | 0.228 | -49.1% | -50.1% | -47.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 1.578 | 0.771 | -51.1% | -51.5% | -50.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 2.583 | 0.771 | -70.1% | -70.3% | -69.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | str_contains() loop | 0.563 | 0.367 | -34.7% | -35.2% | -34.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | preg_match() | 0.852 | 0.367 | -56.9% | -57.2% | -56.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 0.758 | 0.235 | -68.9% | -69.1% | -68.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 0.754 | 0.235 | -68.8% | -68.9% | -68.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | str_contains() loop | 0.474 | 0.126 | -73.4% | -73.5% | -73.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | preg_match() | 0.179 | 0.126 | -29.8% | -30.5% | -28.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | str_contains() loop | 0.574 | 0.271 | -52.7% | -53.5% | -52.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | preg_match() | 0.952 | 0.271 | -71.5% | -71.7% | -71.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | str_contains() loop | 0.484 | 0.283 | -41.7% | -44.6% | -41.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | preg_match() | 0.993 | 0.283 | -71.6% | -71.8% | -71.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 3.520 | 1.361 | -61.3% | -61.6% | -61.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 6.558 | 1.361 | -79.3% | -79.3% | -79.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | str_contains() loop | 1.307 | 0.576 | -55.9% | -56.2% | -55.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | preg_match() | 2.423 | 0.576 | -76.2% | -76.3% | -76.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 1.433 | 0.237 | -83.5% | -84.0% | -83.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 1.485 | 0.237 | -84.1% | -84.1% | -84.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | str_contains() loop | 0.874 | 0.128 | -85.3% | -85.4% | -84.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | preg_match() | 0.213 | 0.128 | -40.0% | -40.2% | -39.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | str_contains() loop | 1.106 | 0.275 | -75.1% | -75.2% | -75.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | preg_match() | 1.859 | 0.275 | -85.2% | -85.2% | -85.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | str_contains() loop | 0.907 | 0.286 | -68.4% | -68.8% | -68.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | preg_match() | 1.982 | 0.286 | -85.6% | -85.6% | -85.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 6.871 | 1.373 | -80.0% | -80.1% | -79.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 13.545 | 1.373 | -89.9% | -89.9% | -89.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | str_contains() loop | 2.826 | 0.576 | -79.6% | -79.7% | -79.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | preg_match() | 5.063 | 0.576 | -88.6% | -88.7% | -88.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 2.951 | 0.244 | -91.8% | -92.0% | -91.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 2.983 | 0.244 | -91.8% | -91.8% | -91.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | str_contains() loop | 1.646 | 0.127 | -92.3% | -92.4% | -92.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | preg_match() | 0.269 | 0.127 | -53.0% | -53.2% | -52.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | str_contains() loop | 2.133 | 0.282 | -86.8% | -87.1% | -86.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | preg_match() | 3.655 | 0.282 | -92.3% | -92.3% | -92.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | str_contains() loop | 1.673 | 0.294 | -82.4% | -82.6% | -82.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | preg_match() | 3.959 | 0.294 | -92.6% | -92.6% | -92.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 13.367 | 1.391 | -89.6% | -89.7% | -89.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 27.840 | 1.391 | -95.0% | -95.0% | -95.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | str_contains() loop | 5.445 | 0.576 | -89.4% | -89.5% | -89.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | preg_match() | 10.324 | 0.576 | -94.4% | -94.4% | -94.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 6.888 | 0.251 | -96.4% | -96.6% | -96.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 6.061 | 0.251 | -95.9% | -95.9% | -95.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | str_contains() loop | 3.474 | 0.128 | -96.3% | -96.5% | -96.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | preg_match() | 0.391 | 0.128 | -67.3% | -67.5% | -67.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | str_contains() loop | 4.525 | 0.290 | -93.6% | -93.7% | -93.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | preg_match() | 7.233 | 0.290 | -96.0% | -96.0% | -96.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | str_contains() loop | 3.545 | 0.300 | -91.5% | -91.8% | -91.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | preg_match() | 7.873 | 0.300 | -96.2% | -96.2% | -96.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 29.885 | 1.424 | -95.2% | -95.3% | -95.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 54.955 | 1.424 | -97.4% | -97.4% | -97.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | str_contains() loop | 11.504 | 0.586 | -94.9% | -94.9% | -94.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | preg_match() | 20.409 | 0.586 | -97.1% | -97.1% | -97.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 16.192 | 0.257 | -98.4% | -98.4% | -98.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 19.433 | 0.257 | -98.7% | -98.7% | -98.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | str_contains() loop | 8.705 | 0.127 | -98.5% | -98.6% | -98.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | preg_match() | 0.649 | 0.127 | -80.5% | -80.5% | -80.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | str_contains() loop | 11.623 | 0.299 | -97.4% | -97.4% | -97.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | preg_match() | 22.569 | 0.299 | -98.7% | -98.7% | -98.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | str_contains() loop | 8.940 | 0.311 | -96.5% | -96.6% | -96.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | preg_match() | 26.872 | 0.311 | -98.8% | -98.8% | -98.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 67.916 | 1.487 | -97.8% | -97.8% | -97.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 186.281 | 1.487 | -99.2% | -99.2% | -99.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | str_contains() loop | 25.043 | 0.592 | -97.6% | -97.6% | -97.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | preg_match() | 74.502 | 0.592 | -99.2% | -99.2% | -99.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 1.212 | 0.906 | -25.2% | -25.6% | -24.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | preg_match() per term | 1.551 | 0.906 | -41.5% | -41.9% | -41.2% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 0.962 | 0.837 | -13.1% | -13.8% | -11.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 1.677 | 0.837 | -50.1% | -50.6% | -49.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 1.462 | 0.936 | -36.0% | -36.4% | -35.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 2.853 | 0.936 | -67.2% | -67.3% | -66.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 2.183 | 1.109 | -49.2% | -49.4% | -48.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | preg_match() per term | 2.762 | 1.109 | -59.9% | -60.0% | -59.6% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 1.801 | 0.903 | -50.0% | -50.4% | -49.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 3.178 | 0.903 | -71.7% | -71.8% | -71.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 2.699 | 1.111 | -58.8% | -59.0% | -58.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 5.216 | 1.111 | -78.7% | -78.8% | -78.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 3.925 | 1.195 | -69.5% | -69.6% | -69.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | preg_match() per term | 5.274 | 1.195 | -77.3% | -77.5% | -77.2% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 3.204 | 0.918 | -71.4% | -71.6% | -71.2% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 5.844 | 0.918 | -84.3% | -84.4% | -84.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 5.075 | 1.277 | -74.8% | -75.3% | -74.6% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 9.911 | 1.277 | -87.1% | -87.2% | -87.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 7.850 | 1.332 | -83.0% | -83.1% | -83.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | preg_match() per term | 9.763 | 1.332 | -86.4% | -86.4% | -86.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 6.719 | 0.958 | -85.8% | -85.9% | -85.6% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 11.528 | 0.958 | -91.7% | -91.7% | -91.6% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 9.980 | 1.554 | -84.4% | -84.6% | -84.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 18.268 | 1.554 | -91.5% | -91.5% | -91.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 16.051 | 1.546 | -90.4% | -90.4% | -90.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | preg_match() per term | 18.958 | 1.546 | -91.8% | -91.9% | -91.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 14.007 | 1.039 | -92.6% | -92.6% | -92.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 37.025 | 1.039 | -97.2% | -97.2% | -97.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 19.082 | 1.957 | -89.7% | -89.8% | -89.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 50.951 | 1.957 | -96.2% | -96.2% | -96.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 31.938 | 1.582 | -95.0% | -95.1% | -95.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | preg_match() per term | 39.566 | 1.582 | -96.0% | -96.0% | -96.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 30.415 | 1.047 | -96.6% | -96.6% | -96.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 89.267 | 1.047 | -98.8% | -98.8% | -98.8% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 35.401 | 1.946 | -94.5% | -94.5% | -94.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 107.060 | 1.946 | -98.2% | -98.2% | -98.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 61.891 | 1.670 | -97.3% | -97.3% | -97.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | preg_match() per term | 93.074 | 1.670 | -98.2% | -98.2% | -98.2% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 60.868 | 1.088 | -98.2% | -98.2% | -98.2% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 192.298 | 1.088 | -99.4% | -99.4% | -99.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 65.807 | 2.038 | -96.9% | -96.9% | -96.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 219.057 | 2.038 | -99.1% | -99.1% | -99.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 4.464 | 1.144 | -74.3% | -74.6% | -74.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 0.713 | 1.144 | +60.6% | +59.3% | +63.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 34.559 | 8.501 | -75.4% | -75.8% | -75.0% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 4.860 | 8.501 | +75.0% | +74.4% | +76.6% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 7.945 | 1.208 | -84.8% | -84.9% | -84.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 1.997 | 1.208 | -39.5% | -39.7% | -38.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 62.690 | 9.005 | -85.6% | -85.7% | -85.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 15.187 | 9.005 | -40.7% | -40.9% | -40.4% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 16.772 | 1.307 | -92.2% | -92.2% | -92.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 3.813 | 1.307 | -65.7% | -65.9% | -65.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 133.674 | 9.704 | -92.7% | -92.8% | -92.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 29.754 | 9.704 | -67.4% | -67.5% | -67.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 31.144 | 1.390 | -95.5% | -95.6% | -95.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 6.925 | 1.390 | -79.9% | -80.0% | -79.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 248.619 | 10.259 | -95.9% | -95.9% | -95.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 54.564 | 10.259 | -81.2% | -81.3% | -81.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 37.992 | 1.464 | -96.1% | -96.2% | -96.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 11.006 | 1.464 | -86.7% | -86.8% | -86.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 303.345 | 10.964 | -96.4% | -96.4% | -96.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 87.042 | 10.964 | -87.4% | -87.4% | -87.4% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 41.684 | 1.545 | -96.3% | -96.3% | -96.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 22.734 | 1.545 | -93.2% | -93.2% | -93.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 332.189 | 11.352 | -96.6% | -96.6% | -96.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 181.095 | 11.352 | -93.7% | -93.8% | -93.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 42.519 | 1.595 | -96.2% | -96.3% | -96.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 68.420 | 1.595 | -97.7% | -97.7% | -97.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 339.313 | 11.880 | -96.5% | -96.5% | -96.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 521.449 | 11.880 | -97.7% | -97.7% | -97.7% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 0.291 | 0.170 | -41.4% | -43.1% | -40.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 0.220 | 0.170 | -22.6% | -23.2% | -21.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | str_contains() loop | 0.203 | 0.111 | -45.1% | -46.0% | -43.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | preg_match() | 0.144 | 0.111 | -23.2% | -24.4% | -21.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | str_contains() loop | 0.238 | 0.190 | -20.1% | -21.2% | -18.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | preg_match() | 0.254 | 0.190 | -25.1% | -26.0% | -23.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | str_contains() loop | 0.215 | 0.200 | -7.0% | -7.4% | -5.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | preg_match() | 0.254 | 0.200 | -21.1% | -21.6% | -19.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 0.959 | 0.757 | -21.1% | -21.5% | -20.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 1.010 | 0.757 | -25.1% | -26.4% | -24.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | str_contains() loop | 0.385 | 0.333 | -13.6% | -13.8% | -12.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | preg_match() | 0.460 | 0.333 | -27.5% | -27.8% | -27.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 0.460 | 0.174 | -62.0% | -62.3% | -61.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 0.325 | 0.174 | -46.2% | -46.7% | -45.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | str_contains() loop | 0.286 | 0.113 | -60.9% | -61.4% | -59.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | preg_match() | 0.153 | 0.113 | -26.3% | -27.9% | -24.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | str_contains() loop | 0.343 | 0.196 | -42.5% | -43.5% | -41.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | preg_match() | 0.392 | 0.196 | -50.1% | -50.6% | -48.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | str_contains() loop | 0.297 | 0.209 | -29.6% | -30.2% | -28.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | preg_match() | 0.407 | 0.209 | -48.6% | -49.0% | -47.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 1.639 | 0.773 | -52.8% | -53.2% | -52.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 2.515 | 0.773 | -69.3% | -69.5% | -68.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | str_contains() loop | 0.563 | 0.355 | -36.9% | -37.4% | -36.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | preg_match() | 0.805 | 0.355 | -55.8% | -56.1% | -55.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 0.842 | 0.244 | -71.0% | -71.2% | -70.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 0.724 | 0.244 | -66.3% | -66.5% | -66.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | str_contains() loop | 0.493 | 0.113 | -77.2% | -77.5% | -76.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | preg_match() | 0.166 | 0.113 | -32.4% | -33.4% | -30.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | str_contains() loop | 0.601 | 0.283 | -52.9% | -53.1% | -52.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | preg_match() | 0.919 | 0.283 | -69.2% | -69.3% | -69.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | str_contains() loop | 0.515 | 0.301 | -41.6% | -41.9% | -40.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | preg_match() | 0.964 | 0.301 | -68.8% | -69.0% | -68.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 3.664 | 1.546 | -57.8% | -58.0% | -57.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 6.430 | 1.546 | -76.0% | -76.0% | -75.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | str_contains() loop | 1.347 | 0.629 | -53.3% | -53.5% | -52.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | preg_match() | 2.358 | 0.629 | -73.3% | -73.4% | -73.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 1.597 | 0.245 | -84.7% | -84.7% | -84.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 1.518 | 0.245 | -83.8% | -83.9% | -83.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | str_contains() loop | 0.920 | 0.110 | -88.0% | -88.1% | -87.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | preg_match() | 0.198 | 0.110 | -44.1% | -44.9% | -43.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | str_contains() loop | 1.159 | 0.284 | -75.5% | -75.6% | -74.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | preg_match() | 1.895 | 0.284 | -85.0% | -85.1% | -84.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | str_contains() loop | 0.975 | 0.300 | -69.3% | -69.4% | -69.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | preg_match() | 2.045 | 0.300 | -85.3% | -85.4% | -85.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 7.001 | 1.557 | -77.7% | -77.8% | -77.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 14.052 | 1.557 | -88.9% | -88.9% | -88.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | str_contains() loop | 2.849 | 0.631 | -77.9% | -77.9% | -77.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | preg_match() | 5.235 | 0.631 | -87.9% | -88.0% | -87.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 3.353 | 0.251 | -92.5% | -92.7% | -92.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 2.850 | 0.251 | -91.2% | -91.3% | -91.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | str_contains() loop | 1.799 | 0.113 | -93.7% | -93.8% | -93.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | preg_match() | 0.242 | 0.113 | -53.2% | -53.7% | -52.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | str_contains() loop | 2.274 | 0.294 | -87.2% | -87.2% | -87.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | preg_match() | 3.482 | 0.294 | -91.6% | -91.7% | -91.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | str_contains() loop | 1.931 | 0.307 | -84.1% | -84.4% | -83.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | preg_match() | 3.811 | 0.307 | -91.9% | -92.0% | -91.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 13.583 | 1.585 | -88.3% | -88.4% | -88.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 26.589 | 1.585 | -94.0% | -94.1% | -94.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | str_contains() loop | 5.511 | 0.629 | -88.6% | -88.6% | -88.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | preg_match() | 9.839 | 0.629 | -93.6% | -93.6% | -93.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 7.943 | 0.256 | -96.8% | -96.9% | -96.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 5.980 | 0.256 | -95.7% | -95.7% | -95.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | str_contains() loop | 4.033 | 0.112 | -97.2% | -97.3% | -97.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | preg_match() | 0.368 | 0.112 | -69.6% | -69.9% | -69.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | str_contains() loop | 4.979 | 0.301 | -93.9% | -94.1% | -93.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | preg_match() | 7.063 | 0.301 | -95.7% | -95.8% | -95.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | str_contains() loop | 3.867 | 0.315 | -91.9% | -92.0% | -91.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | preg_match() | 7.677 | 0.315 | -95.9% | -95.9% | -95.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 30.776 | 1.610 | -94.8% | -94.8% | -94.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 54.112 | 1.610 | -97.0% | -97.0% | -97.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | str_contains() loop | 11.569 | 0.634 | -94.5% | -94.5% | -94.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | preg_match() | 19.953 | 0.634 | -96.8% | -96.8% | -96.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 17.177 | 0.264 | -98.5% | -98.5% | -98.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 21.827 | 0.264 | -98.8% | -98.8% | -98.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | str_contains() loop | 9.498 | 0.113 | -98.8% | -98.8% | -98.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | preg_match() | 0.642 | 0.113 | -82.5% | -82.8% | -82.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | str_contains() loop | 12.464 | 0.307 | -97.5% | -97.5% | -97.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | preg_match() | 22.768 | 0.307 | -98.7% | -98.7% | -98.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | str_contains() loop | 9.524 | 0.325 | -96.6% | -96.6% | -96.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | preg_match() | 24.276 | 0.325 | -98.7% | -98.7% | -98.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 70.178 | 1.653 | -97.6% | -97.7% | -97.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 201.871 | 1.653 | -99.2% | -99.2% | -99.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | str_contains() loop | 26.503 | 0.638 | -97.6% | -97.6% | -97.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | preg_match() | 66.308 | 0.638 | -99.0% | -99.0% | -99.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 1.185 | 0.941 | -20.6% | -21.0% | -20.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | preg_match() per term | 1.520 | 0.941 | -38.1% | -38.3% | -37.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 0.960 | 0.853 | -11.1% | -11.5% | -10.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 1.670 | 0.853 | -48.9% | -49.2% | -48.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 1.469 | 1.147 | -21.9% | -22.9% | -21.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 2.810 | 1.147 | -59.2% | -59.3% | -59.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 2.230 | 1.098 | -50.8% | -51.0% | -50.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | preg_match() per term | 2.720 | 1.098 | -59.6% | -59.9% | -59.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 1.880 | 0.945 | -49.7% | -50.0% | -49.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 3.167 | 0.945 | -70.1% | -70.4% | -70.0% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 2.790 | 1.312 | -53.0% | -53.3% | -52.8% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 5.196 | 1.312 | -74.8% | -74.9% | -74.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 3.996 | 1.195 | -70.1% | -70.3% | -69.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | preg_match() per term | 5.304 | 1.195 | -77.5% | -77.6% | -77.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 3.410 | 0.970 | -71.6% | -71.7% | -71.2% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 5.940 | 0.970 | -83.7% | -83.7% | -83.6% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 5.273 | 1.468 | -72.2% | -72.4% | -71.6% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 9.793 | 1.468 | -85.0% | -85.0% | -84.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 8.393 | 1.344 | -84.0% | -84.0% | -83.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | preg_match() per term | 9.921 | 1.344 | -86.5% | -86.5% | -86.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 7.333 | 1.026 | -86.0% | -86.1% | -85.9% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 11.486 | 1.026 | -91.1% | -91.1% | -91.0% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 10.192 | 1.757 | -82.8% | -83.0% | -82.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 18.218 | 1.757 | -90.3% | -90.4% | -90.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 16.414 | 1.612 | -90.2% | -90.2% | -90.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | preg_match() per term | 18.994 | 1.612 | -91.5% | -91.5% | -91.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 14.762 | 1.101 | -92.5% | -92.6% | -92.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 37.404 | 1.101 | -97.1% | -97.1% | -97.0% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 19.443 | 2.118 | -89.1% | -89.2% | -89.0% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 51.138 | 2.118 | -95.9% | -95.9% | -95.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 32.505 | 1.632 | -95.0% | -95.0% | -94.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | preg_match() per term | 40.055 | 1.632 | -95.9% | -95.9% | -95.9% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 30.792 | 1.123 | -96.4% | -96.4% | -96.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 89.810 | 1.123 | -98.7% | -98.8% | -98.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 36.144 | 2.144 | -94.1% | -94.2% | -94.0% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 108.663 | 2.144 | -98.0% | -98.0% | -98.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 62.470 | 1.722 | -97.2% | -97.3% | -97.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | preg_match() per term | 93.350 | 1.722 | -98.2% | -98.2% | -98.1% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 61.554 | 1.186 | -98.1% | -98.2% | -98.1% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 192.303 | 1.186 | -99.4% | -99.4% | -99.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 67.220 | 2.252 | -96.7% | -96.7% | -96.6% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 218.645 | 2.252 | -99.0% | -99.0% | -99.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 4.300 | 1.066 | -75.2% | -75.7% | -74.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 0.692 | 1.066 | +53.8% | +52.8% | +54.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 34.043 | 8.020 | -76.4% | -76.7% | -75.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 4.860 | 8.020 | +65.1% | +64.7% | +65.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 7.873 | 1.178 | -85.0% | -85.2% | -85.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 1.975 | 1.178 | -40.4% | -40.9% | -39.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 62.443 | 8.855 | -85.8% | -85.9% | -85.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 15.211 | 8.855 | -41.8% | -42.0% | -40.6% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 16.761 | 1.282 | -92.4% | -92.4% | -92.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 3.837 | 1.282 | -66.6% | -66.7% | -66.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 133.171 | 9.635 | -92.8% | -92.8% | -92.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 29.894 | 9.635 | -67.8% | -67.9% | -67.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 31.370 | 1.389 | -95.6% | -95.6% | -95.6% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 6.902 | 1.389 | -79.9% | -80.0% | -79.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 249.846 | 10.439 | -95.8% | -95.8% | -95.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 54.636 | 10.439 | -80.9% | -80.9% | -80.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 38.437 | 1.491 | -96.1% | -96.1% | -96.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 11.898 | 1.491 | -87.5% | -87.5% | -87.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 306.968 | 11.567 | -96.2% | -96.2% | -96.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 94.062 | 11.567 | -87.7% | -87.8% | -87.6% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 42.231 | 1.580 | -96.3% | -96.3% | -96.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 22.063 | 1.580 | -92.8% | -92.9% | -92.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 336.792 | 11.705 | -96.5% | -96.5% | -96.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 177.347 | 11.705 | -93.4% | -93.4% | -93.4% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 43.006 | 1.639 | -96.2% | -96.2% | -96.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 64.761 | 1.639 | -97.5% | -97.5% | -97.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 343.148 | 12.254 | -96.4% | -96.4% | -96.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 556.088 | 12.254 | -97.8% | -97.8% | -97.8% |

### Control tasks

#### Dictionary preparation included

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | str_contains() loop | 0.346 | 6.303 | +1723.1% | +1715.2% | +1766.7% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | preg_match() | 1.328 | 6.303 | +374.5% | +371.0% | +376.7% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | strtr() | 72.368 | 152.826 | +111.0% | +110.3% | +111.8% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace_callback() | 10.782 | 152.826 | +1317.5% | +1307.6% | +1331.6% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | str_replace() | 151.575 | 152.826 | +0.8% | +0.2% | +1.2% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace() | 10.317 | 152.826 | +1381.4% | +1369.7% | +1400.4% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | str_contains() loop | 0.352 | 5.949 | +1587.8% | +1559.3% | +1594.8% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | preg_match() | 1.355 | 5.949 | +339.3% | +334.2% | +345.8% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | strtr() | 66.060 | 110.820 | +67.8% | +66.9% | +68.5% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace_callback() | 10.068 | 110.820 | +1000.7% | +995.6% | +1006.6% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | str_replace() | 141.699 | 110.820 | -21.7% | -22.2% | -21.4% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace() | 9.589 | 110.820 | +1055.9% | +1048.3% | +1062.2% |

#### Dictionary already prepared

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | str_contains() loop | 0.335 | 0.235 | -30.1% | -31.7% | -29.5% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | preg_match() | 0.255 | 0.235 | -7.9% | -8.6% | -7.5% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | strtr() | 72.341 | 137.670 | +90.2% | +89.3% | +90.5% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace_callback() | 4.391 | 137.670 | +3030.3% | +3014.9% | +3040.1% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | str_replace() | 146.825 | 137.670 | -6.2% | -6.7% | -6.1% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace() | 3.994 | 137.670 | +3346.2% | +3322.5% | +3352.1% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | str_contains() loop | 0.356 | 0.241 | -32.1% | -32.6% | -31.5% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | preg_match() | 0.251 | 0.241 | -3.7% | -4.6% | -2.8% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | strtr() | 66.164 | 96.077 | +45.3% | +44.7% | +45.8% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace_callback() | 4.383 | 96.077 | +2093.1% | +2078.4% | +2099.9% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | str_replace() | 141.100 | 96.077 | -32.0% | -32.3% | -31.6% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace() | 3.968 | 96.077 | +2324.7% | +2307.5% | +2334.8% |
