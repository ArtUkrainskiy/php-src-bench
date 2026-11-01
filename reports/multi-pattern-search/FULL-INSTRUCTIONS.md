# Complete instruction comparisons

Unit: instructions per complete job. Lower is better. Δ is the median of paired per-pass changes; min/max are paired changes, not confidence intervals.

All measured alternatives are listed. Preparation and reuse are separate sections. Natural API result representations are retained; see [method](METHOD.md).

## Everyday cases

### Product tasks

#### Dictionary preparation included

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4796.1 | 124593.6 | +2497.8% | +2497.8% | +2497.8% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 19382.5 | 124593.6 | +542.8% | +542.8% | +542.8% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 3696.1 | 123839.3 | +3250.5% | +3250.5% | +3250.5% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 17306.6 | 123839.3 | +615.6% | +615.6% | +615.6% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4135.9 | 125205.9 | +2927.3% | +2927.3% | +2927.3% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 20736.5 | 125205.9 | +503.8% | +503.8% | +503.8% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 3802.0 | 125426.8 | +3199.0% | +3198.8% | +3199.0% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 21029.0 | 125426.8 | +496.4% | +496.4% | +496.4% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 13323.3 | 131261.4 | +885.2% | +885.2% | +885.2% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 41348.4 | 131261.4 | +217.5% | +217.5% | +217.5% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 7387.3 | 125783.6 | +1602.7% | +1602.7% | +1602.7% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 26913.0 | 125783.6 | +367.4% | +367.4% | +367.4% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 12995.8 | 361944.9 | +2685.1% | +2685.1% | +2685.1% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 26481.4 | 361944.9 | +1266.8% | +1266.8% | +1266.8% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 13657.0 | 360579.6 | +2540.3% | +2540.2% | +2540.3% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 19028.2 | 360579.6 | +1795.0% | +1795.0% | +1795.0% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 19324.4 | 365907.9 | +1793.5% | +1793.5% | +1793.5% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 30665.6 | 365907.9 | +1093.2% | +1093.2% | +1093.2% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 13525.9 | 363035.0 | +2584.0% | +2584.0% | +2584.0% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 30830.1 | 363035.0 | +1077.5% | +1077.5% | +1077.5% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 32981.0 | 376888.3 | +1042.7% | +1042.7% | +1042.7% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 99148.7 | 376888.3 | +280.1% | +280.1% | +280.1% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 18926.0 | 366815.8 | +1838.2% | +1838.1% | +1838.2% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 49497.7 | 366815.8 | +641.1% | +641.1% | +641.1% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 5056.1 | 302829.6 | +5889.4% | +5889.4% | +5889.4% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 19058.2 | 302829.6 | +1489.0% | +1489.0% | +1489.0% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 3912.4 | 302200.5 | +7624.2% | +7623.9% | +7624.2% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 16846.8 | 302200.5 | +1693.8% | +1693.8% | +1693.8% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4707.6 | 303433.5 | +6345.6% | +6345.5% | +6345.6% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 20258.5 | 303433.5 | +1397.8% | +1397.8% | +1397.8% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4164.9 | 303433.6 | +7185.5% | +7185.5% | +7185.5% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 20447.5 | 303433.6 | +1384.0% | +1384.0% | +1384.0% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 16476.0 | 311450.0 | +1790.3% | +1790.3% | +1790.3% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 42861.7 | 311450.0 | +626.6% | +626.6% | +626.6% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 9832.3 | 305923.1 | +3011.4% | +3011.4% | +3011.4% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 27222.7 | 305923.1 | +1023.8% | +1023.8% | +1023.8% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 30278.4 | 140649.0 | +364.5% | +364.5% | +364.5% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 68761.8 | 140649.0 | +104.5% | +104.5% | +104.5% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 15714.3 | 107376.7 | +583.3% | +583.3% | +583.3% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 13870.4 | 107376.7 | +674.1% | +674.1% | +674.1% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 17331.3 | 124887.7 | +620.6% | +620.6% | +620.6% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 42520.4 | 124887.7 | +193.7% | +193.7% | +193.7% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 18676.5 | 140190.4 | +650.6% | +650.6% | +650.6% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 67658.5 | 140190.4 | +107.2% | +107.2% | +107.2% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | strtr() | 19756.1 | 104955.5 | +431.3% | +431.3% | +431.3% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | preg_replace_callback() | 57457.2 | 104955.5 | +82.7% | +82.7% | +82.7% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | str_replace() | 45005.5 | 104955.5 | +133.2% | +133.2% | +133.2% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | strtr() | 28370.1 | 113323.0 | +299.4% | +299.4% | +299.4% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | preg_replace_callback() | 74145.9 | 113323.0 | +52.8% | +52.8% | +52.8% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | str_replace() | 56082.1 | 113323.0 | +102.1% | +102.1% | +102.1% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 5724.9 | 41087.4 | +617.7% | +617.7% | +617.7% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 26086.5 | 41087.4 | +57.5% | +57.5% | +57.5% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 18493.9 | 41087.4 | +122.2% | +122.2% | +122.2% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 39520.0 | 79925.1 | +102.2% | +102.2% | +102.2% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 66874.0 | 79925.1 | +19.5% | +19.5% | +19.5% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 42862.0 | 79925.1 | +86.5% | +86.5% | +86.5% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 3389.0 | 13421.0 | +296.0% | +296.0% | +296.0% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 15773.0 | 13421.0 | -14.9% | -14.9% | -14.9% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 14864.0 | 13421.0 | -9.7% | -9.7% | -9.7% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 4978.0 | 15378.9 | +208.9% | +208.9% | +208.9% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 21654.9 | 15378.9 | -29.0% | -29.0% | -29.0% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 16615.9 | 15378.9 | -7.4% | -7.4% | -7.4% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | strtr() | 3208.3 | 7440.8 | +131.9% | +131.9% | +131.9% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace_callback() | 14728.5 | 7440.8 | -49.5% | -49.5% | -49.5% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | str_replace() | 11273.2 | 7440.8 | -34.0% | -34.0% | -34.0% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace() | 11936.7 | 7440.8 | -37.7% | -37.7% | -37.7% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 6031.0 | 166914.1 | +2667.6% | +2667.6% | +2667.6% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 33751.0 | 166914.1 | +394.5% | +394.5% | +394.5% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 21875.5 | 166914.1 | +663.0% | +663.0% | +663.0% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 7467.5 | 171796.7 | +2200.6% | +2200.6% | +2200.6% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 36514.2 | 171796.7 | +370.5% | +370.5% | +370.5% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 23266.8 | 171796.7 | +638.4% | +638.4% | +638.4% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 53503.0 | 198935.1 | +271.8% | +271.8% | +271.8% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 66594.0 | 198935.1 | +198.7% | +198.7% | +198.7% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 52946.0 | 198935.1 | +275.7% | +275.7% | +275.7% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 127752.8 | 627476.1 | +391.2% | +391.2% | +391.2% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 108595.9 | 627476.1 | +477.8% | +477.8% | +477.8% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 155797.6 | 627476.1 | +302.8% | +302.7% | +302.8% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 107800.0 | 627476.1 | +482.1% | +482.1% | +482.1% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 129995.9 | 652728.5 | +402.1% | +402.1% | +402.1% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 111502.5 | 652728.5 | +485.4% | +485.4% | +485.4% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 162156.9 | 652728.5 | +302.5% | +302.5% | +302.5% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 109462.3 | 652728.5 | +496.3% | +496.3% | +496.3% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 195156.7 | 729834.2 | +274.0% | +274.0% | +274.0% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 118382.1 | 729834.2 | +516.5% | +516.5% | +516.5% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 213697.5 | 729834.2 | +241.5% | +241.5% | +241.5% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 113943.5 | 729834.2 | +540.5% | +540.5% | +540.5% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 1529535.7 | 2107813.4 | +37.8% | +37.8% | +37.8% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 178692.5 | 2107813.4 | +1079.6% | +1079.6% | +1079.6% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 1020019.8 | 2107813.4 | +106.6% | +106.6% | +106.6% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 174254.1 | 2107813.4 | +1109.6% | +1109.6% | +1109.6% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 3050.8 | 13747.7 | +350.6% | +350.6% | +350.6% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 30970.3 | 13747.7 | -55.6% | -55.6% | -55.6% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 27907.0 | 13747.7 | -50.7% | -50.7% | -50.7% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 3740.0 | 14435.0 | +286.0% | +286.0% | +286.0% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 32790.6 | 14435.0 | -56.0% | -56.0% | -56.0% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 28425.5 | 14435.0 | -49.2% | -49.2% | -49.2% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 141232.0 | 510628.1 | +261.6% | +261.6% | +261.6% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | preg_match() per term | 301436.8 | 510628.1 | +69.4% | +69.4% | +69.4% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 109402.5 | 501722.1 | +358.6% | +358.6% | +358.6% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 333378.1 | 501722.1 | +50.5% | +50.5% | +50.5% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 173260.5 | 516584.6 | +198.2% | +198.2% | +198.2% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 523881.8 | 516584.6 | -1.4% | -1.4% | -1.4% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 387604.3 | 572310.5 | +47.7% | +47.7% | +47.7% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 598129.8 | 572310.5 | -4.3% | -4.3% | -4.3% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 3094311.6 | 665292.0 | -78.5% | -78.5% | -78.5% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 1858950.6 | 665292.0 | -64.2% | -64.2% | -64.2% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4711.3 | 133735.9 | +2738.6% | +2738.6% | +2738.6% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 18014.5 | 133735.9 | +642.4% | +642.4% | +642.4% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 3647.0 | 132981.3 | +3546.3% | +3546.3% | +3546.3% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 15940.6 | 132981.3 | +734.2% | +734.2% | +734.2% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4072.0 | 134347.9 | +3199.3% | +3199.3% | +3199.3% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 19370.5 | 134347.9 | +593.6% | +593.6% | +593.6% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 3757.9 | 134568.9 | +3481.0% | +3480.9% | +3481.0% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 19663.0 | 134568.9 | +584.4% | +584.4% | +584.4% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 13129.3 | 140411.1 | +969.4% | +969.4% | +969.5% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 39980.4 | 140411.1 | +251.2% | +251.2% | +251.2% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 7281.0 | 134932.4 | +1753.2% | +1753.2% | +1753.2% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 25547.0 | 134932.4 | +428.2% | +428.2% | +428.2% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 12748.9 | 392834.9 | +2981.3% | +2981.3% | +2981.3% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 25250.4 | 392834.9 | +1455.8% | +1455.8% | +1455.8% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 13422.5 | 391469.3 | +2816.5% | +2816.5% | +2816.5% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 17799.2 | 391469.3 | +2099.4% | +2099.4% | +2099.4% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 18942.5 | 396781.2 | +1994.7% | +1994.7% | +1994.7% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 29436.6 | 396781.2 | +1247.9% | +1247.9% | +1247.9% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 13284.7 | 393924.2 | +2865.2% | +2865.2% | +2865.2% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 29601.1 | 393924.2 | +1230.8% | +1230.8% | +1230.8% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 29582.7 | 407777.6 | +1278.4% | +1278.4% | +1278.4% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 97917.7 | 407777.6 | +316.4% | +316.4% | +316.5% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 17307.0 | 397705.3 | +2197.9% | +2197.9% | +2197.9% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 48268.6 | 397705.3 | +723.9% | +723.9% | +723.9% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4961.7 | 329784.4 | +6546.5% | +6546.5% | +6546.6% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 18005.2 | 329784.4 | +1731.6% | +1731.6% | +1731.6% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 3851.8 | 329155.3 | +8445.6% | +8445.5% | +8445.6% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 15795.7 | 329155.3 | +1983.8% | +1983.8% | +1983.8% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4629.3 | 330388.3 | +7037.0% | +7036.8% | +7037.0% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 19207.5 | 330388.3 | +1620.1% | +1620.1% | +1620.1% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4094.1 | 330388.4 | +7969.8% | +7969.3% | +7969.8% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 19396.5 | 330388.4 | +1603.3% | +1603.3% | +1603.3% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 16126.0 | 338405.0 | +1998.5% | +1998.5% | +1998.5% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 41808.7 | 338405.0 | +709.4% | +709.4% | +709.4% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 9628.3 | 332878.0 | +3357.3% | +3357.3% | +3357.3% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 26171.7 | 332878.0 | +1171.9% | +1171.9% | +1171.9% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 27342.0 | 148960.0 | +444.8% | +444.8% | +444.8% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 68126.8 | 148960.0 | +118.7% | +118.7% | +118.7% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 14214.8 | 115687.8 | +713.9% | +713.9% | +713.9% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 13237.4 | 115687.8 | +773.9% | +773.9% | +773.9% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 15724.3 | 133198.8 | +747.1% | +747.1% | +747.1% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 41887.4 | 133198.8 | +218.0% | +218.0% | +218.0% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 16981.0 | 148501.3 | +774.5% | +774.5% | +774.5% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 67025.5 | 148501.3 | +121.6% | +121.6% | +121.6% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | strtr() | 17229.1 | 111887.5 | +549.4% | +549.4% | +549.4% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | preg_replace_callback() | 55924.1 | 111887.5 | +100.1% | +100.1% | +100.1% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | str_replace() | 44910.8 | 111887.5 | +149.1% | +149.1% | +149.1% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | strtr() | 25248.1 | 120516.0 | +377.3% | +377.3% | +377.3% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | preg_replace_callback() | 72314.7 | 120516.0 | +66.7% | +66.7% | +66.7% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | str_replace() | 55630.6 | 120516.0 | +116.6% | +116.6% | +116.6% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 5105.2 | 43820.7 | +758.3% | +758.3% | +758.3% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 25365.9 | 43820.7 | +72.8% | +72.8% | +72.8% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 18617.6 | 43820.7 | +135.4% | +135.4% | +135.4% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 34569.0 | 84102.0 | +143.3% | +143.3% | +143.3% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 65526.0 | 84102.0 | +28.3% | +28.3% | +28.3% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 42522.0 | 84102.0 | +97.8% | +97.8% | +97.8% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 2992.0 | 14337.0 | +379.2% | +379.2% | +379.2% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 16001.0 | 14337.0 | -10.4% | -10.4% | -10.4% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 14989.0 | 14337.0 | -4.3% | -4.4% | -4.3% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 4403.0 | 16281.3 | +269.8% | +269.8% | +269.8% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 21757.4 | 16281.3 | -25.2% | -25.2% | -25.2% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 16643.9 | 16281.3 | -2.2% | -2.2% | -2.2% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | strtr() | 2978.3 | 7860.8 | +163.9% | +163.9% | +163.9% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace_callback() | 14715.2 | 7860.8 | -46.6% | -46.6% | -46.6% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | str_replace() | 11246.8 | 7860.8 | -30.1% | -30.1% | -30.1% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace() | 11943.8 | 7860.8 | -34.2% | -34.2% | -34.2% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 5846.5 | 180186.1 | +2981.9% | +2981.9% | +2982.0% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 31419.0 | 180186.1 | +473.5% | +473.5% | +473.5% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 22126.0 | 180186.1 | +714.4% | +714.4% | +714.4% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 7187.2 | 185092.4 | +2475.3% | +2475.3% | +2475.3% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 34114.9 | 185092.4 | +442.6% | +442.6% | +442.6% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 23453.1 | 185092.4 | +689.2% | +689.2% | +689.2% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 51261.0 | 213970.6 | +317.4% | +317.4% | +317.4% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 63905.0 | 213970.6 | +234.8% | +234.8% | +234.8% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 52455.0 | 213970.6 | +307.9% | +307.9% | +307.9% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 107590.0 | 679881.1 | +531.9% | +531.9% | +531.9% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 105257.0 | 679881.1 | +545.9% | +545.9% | +545.9% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 147599.1 | 679881.1 | +360.6% | +360.6% | +360.6% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 104421.0 | 679881.1 | +551.1% | +551.1% | +551.1% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 109704.3 | 702130.6 | +540.0% | +540.0% | +540.0% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 108122.5 | 702130.6 | +549.4% | +549.4% | +549.4% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 153055.2 | 702130.6 | +358.7% | +358.7% | +358.7% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 106066.3 | 702130.6 | +562.0% | +562.0% | +562.0% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 164580.5 | 781355.6 | +374.8% | +374.8% | +374.8% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 114937.6 | 781355.6 | +579.8% | +579.8% | +579.8% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 200274.3 | 781355.6 | +290.1% | +290.1% | +290.1% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 110520.8 | 781355.6 | +607.0% | +607.0% | +607.0% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 1285529.0 | 2229942.1 | +73.5% | +73.5% | +73.5% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 175249.3 | 2229942.1 | +1172.4% | +1172.4% | +1172.4% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 954193.5 | 2229942.1 | +133.7% | +133.7% | +133.7% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 170832.5 | 2229942.1 | +1205.3% | +1205.3% | +1205.3% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 2779.8 | 14634.3 | +426.5% | +426.5% | +426.5% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 31250.2 | 14634.3 | -53.2% | -53.2% | -53.2% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 28357.0 | 14634.3 | -48.4% | -48.4% | -48.4% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 3434.0 | 15304.1 | +345.7% | +345.6% | +345.7% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 33019.5 | 15304.1 | -53.7% | -53.7% | -53.7% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 28844.9 | 15304.1 | -46.9% | -47.0% | -46.9% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 141953.9 | 548234.2 | +286.2% | +286.2% | +286.2% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | preg_match() per term | 300389.4 | 548234.2 | +82.5% | +82.5% | +82.5% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 105315.0 | 538925.3 | +411.7% | +411.7% | +411.7% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 331141.4 | 538925.3 | +62.7% | +62.7% | +62.7% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 171820.2 | 553710.8 | +222.3% | +222.3% | +222.3% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 519098.4 | 553710.8 | +6.7% | +6.7% | +6.7% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 397022.1 | 616102.8 | +55.2% | +55.2% | +55.2% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 602056.6 | 616102.8 | +2.3% | +2.3% | +2.3% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 3169640.6 | 711836.2 | -77.5% | -77.5% | -77.5% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 1859843.7 | 711836.2 | -61.7% | -61.7% | -61.7% |

#### Dictionary already prepared

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4796.1 | 2431.6 | -49.3% | -49.3% | -49.3% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 4227.5 | 2431.6 | -42.5% | -42.5% | -42.5% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 3696.1 | 1677.3 | -54.6% | -54.6% | -54.6% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2151.6 | 1677.3 | -22.0% | -22.0% | -22.0% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4135.9 | 3043.9 | -26.4% | -26.4% | -26.4% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5581.5 | 3043.9 | -45.5% | -45.5% | -45.5% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 3802.0 | 3264.9 | -14.1% | -14.1% | -14.1% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5874.0 | 3264.9 | -44.4% | -44.4% | -44.4% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 13323.3 | 11586.3 | -13.0% | -13.0% | -13.0% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 26193.3 | 11586.3 | -55.8% | -55.8% | -55.8% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 7387.3 | 5491.7 | -25.7% | -25.7% | -25.7% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 11758.0 | 5491.7 | -53.3% | -53.3% | -53.3% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 12995.8 | 3181.9 | -75.5% | -75.5% | -75.5% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 9717.4 | 3181.9 | -67.3% | -67.3% | -67.3% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 13657.0 | 1816.5 | -86.7% | -86.7% | -86.7% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2264.3 | 1816.5 | -19.8% | -19.8% | -19.8% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 19324.4 | 4206.9 | -78.2% | -78.2% | -78.2% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 13901.6 | 4206.9 | -69.7% | -69.7% | -69.7% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 13525.9 | 4271.9 | -68.4% | -68.4% | -68.4% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 14066.1 | 4271.9 | -69.6% | -69.6% | -69.6% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 32981.0 | 18125.3 | -45.0% | -45.0% | -45.0% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 82384.6 | 18125.3 | -78.0% | -78.0% | -78.0% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 18926.0 | 8052.7 | -57.5% | -57.5% | -57.5% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 32733.7 | 8052.7 | -75.4% | -75.4% | -75.4% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 5056.1 | 2311.4 | -54.3% | -54.3% | -54.3% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 4369.3 | 2311.4 | -47.1% | -47.1% | -47.1% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 3912.4 | 1682.1 | -57.0% | -57.0% | -57.0% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2157.8 | 1682.1 | -22.0% | -22.0% | -22.0% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4707.6 | 2915.5 | -38.1% | -38.1% | -38.1% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5569.5 | 2915.5 | -47.7% | -47.7% | -47.7% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4164.9 | 2915.5 | -30.0% | -30.0% | -30.0% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5758.5 | 2915.5 | -49.4% | -49.4% | -49.4% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 16476.0 | 10932.0 | -33.6% | -33.6% | -33.6% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 28172.7 | 10932.0 | -61.2% | -61.2% | -61.2% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 9832.3 | 5405.0 | -45.0% | -45.0% | -45.0% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 12533.7 | 5405.0 | -56.9% | -56.9% | -56.9% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 30278.5 | 36438.0 | +20.3% | +20.3% | +20.3% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 59116.8 | 36438.0 | -38.4% | -38.4% | -38.4% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 15714.2 | 3165.8 | -79.9% | -79.9% | -79.9% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 4225.4 | 3165.8 | -25.1% | -25.1% | -25.1% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 17331.2 | 20676.8 | +19.3% | +19.3% | +19.3% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 32875.4 | 20676.8 | -37.1% | -37.1% | -37.1% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 18676.5 | 35979.4 | +92.6% | +92.6% | +92.6% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 58013.5 | 35979.4 | -38.0% | -38.0% | -38.0% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 5724.9 | 6466.4 | +13.0% | +13.0% | +13.0% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 6819.5 | 6466.4 | -5.2% | -5.2% | -5.2% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 4471.9 | 6466.4 | +44.6% | +44.6% | +44.6% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 39520.0 | 45259.0 | +14.5% | +14.5% | +14.5% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 47607.0 | 45259.0 | -4.9% | -4.9% | -4.9% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 28818.0 | 45259.0 | +57.1% | +57.1% | +57.1% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 3389.0 | 3313.0 | -2.2% | -2.2% | -2.2% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 2256.0 | 3313.0 | +46.9% | +46.9% | +46.9% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 3132.0 | 3313.0 | +5.8% | +5.8% | +5.8% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 4978.0 | 5270.9 | +5.9% | +5.9% | +5.9% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 8115.4 | 5270.9 | -35.1% | -35.1% | -35.1% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 4883.9 | 5270.9 | +7.9% | +7.9% | +7.9% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | strtr() | 3208.3 | 3016.8 | -6.0% | -6.0% | -6.0% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace_callback() | 5117.5 | 3016.8 | -41.1% | -41.1% | -41.1% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | str_replace() | 3041.8 | 3016.8 | -0.8% | -0.8% | -0.8% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace() | 2974.8 | 3016.8 | +1.4% | +1.4% | +1.4% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 6031.0 | 3351.0 | -44.4% | -44.4% | -44.4% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 2574.0 | 3351.0 | +30.2% | +30.2% | +30.2% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 3839.5 | 3351.0 | -12.7% | -12.7% | -12.7% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 7467.5 | 5322.9 | -28.7% | -28.7% | -28.7% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 5288.3 | 5322.9 | +0.7% | +0.7% | +0.7% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 5230.8 | 5322.9 | +1.8% | +1.8% | +1.8% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 53503.0 | 35989.1 | -32.7% | -32.7% | -32.7% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 35371.0 | 35989.1 | +1.7% | +1.7% | +1.7% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 34889.0 | 35989.1 | +3.2% | +3.2% | +3.2% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 127752.8 | 103665.7 | -18.9% | -18.9% | -18.9% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 8153.0 | 103665.7 | +1171.5% | +1171.5% | +1171.5% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 82907.0 | 103665.7 | +25.0% | +25.0% | +25.0% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 7963.0 | 103665.7 | +1201.8% | +1201.8% | +1201.8% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 129996.0 | 128917.7 | -0.8% | -0.8% | -0.8% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 11036.5 | 128917.7 | +1068.1% | +1068.1% | +1068.1% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 89265.6 | 128917.7 | +44.4% | +44.4% | +44.4% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 9625.3 | 128917.7 | +1239.4% | +1239.4% | +1239.4% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 195156.9 | 205998.0 | +5.6% | +5.6% | +5.6% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 17892.0 | 205998.0 | +1051.3% | +1051.3% | +1051.5% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 140806.7 | 205998.0 | +46.3% | +46.3% | +46.3% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 14130.5 | 205998.0 | +1357.8% | +1357.8% | +1357.8% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 1529536.5 | 1585323.1 | +3.6% | +3.6% | +3.6% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 78202.5 | 1585323.1 | +1927.2% | +1927.2% | +1927.3% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 947127.9 | 1585323.1 | +67.4% | +67.4% | +67.4% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 74417.1 | 1585323.1 | +2030.3% | +2030.3% | +2030.3% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 3050.8 | 2747.8 | -9.9% | -9.9% | -9.9% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 2640.3 | 2747.8 | +4.1% | +4.1% | +4.1% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 3832.0 | 2747.8 | -28.3% | -28.3% | -28.3% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 3740.0 | 3435.0 | -8.2% | -8.2% | -8.2% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 4413.6 | 3435.0 | -22.2% | -22.2% | -22.2% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 4350.5 | 3435.0 | -21.0% | -21.0% | -21.0% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 141232.2 | 17387.8 | -87.7% | -87.7% | -87.7% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | preg_match() per term | 200999.2 | 17387.8 | -91.3% | -91.3% | -91.3% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 109402.3 | 8408.0 | -92.3% | -92.3% | -92.3% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 227667.4 | 8408.0 | -96.3% | -96.3% | -96.3% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 173260.6 | 22270.9 | -87.1% | -87.1% | -87.1% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 381689.2 | 22270.9 | -94.2% | -94.2% | -94.2% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 387604.7 | 13596.8 | -96.5% | -96.5% | -96.5% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 181108.6 | 13596.8 | -92.5% | -92.5% | -92.5% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 3094316.9 | 101644.0 | -96.7% | -96.7% | -96.7% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 1441916.9 | 101644.0 | -93.0% | -93.0% | -93.0% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4711.3 | 2448.6 | -48.0% | -48.0% | -48.0% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 4233.5 | 2448.6 | -42.2% | -42.2% | -42.2% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 3647.0 | 1694.3 | -53.5% | -53.5% | -53.5% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2159.6 | 1694.3 | -21.5% | -21.5% | -21.5% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4072.0 | 3060.9 | -24.8% | -24.8% | -24.8% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5589.5 | 3060.9 | -45.2% | -45.2% | -45.2% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 3757.9 | 3281.9 | -12.7% | -12.7% | -12.7% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5882.0 | 3281.9 | -44.2% | -44.2% | -44.2% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 13129.3 | 11603.4 | -11.6% | -11.6% | -11.6% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 26199.3 | 11603.4 | -55.7% | -55.7% | -55.7% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 7281.0 | 5508.7 | -24.3% | -24.3% | -24.3% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 11766.0 | 5508.7 | -53.2% | -53.2% | -53.2% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 12748.9 | 3198.9 | -74.9% | -74.9% | -74.9% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 9723.4 | 3198.9 | -67.1% | -67.1% | -67.1% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 13422.5 | 1833.5 | -86.3% | -86.3% | -86.3% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2272.3 | 1833.5 | -19.3% | -19.3% | -19.3% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 18942.5 | 4223.9 | -77.7% | -77.7% | -77.7% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 13909.6 | 4223.9 | -69.6% | -69.6% | -69.6% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 13284.7 | 4288.9 | -67.7% | -67.7% | -67.7% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 14074.1 | 4288.9 | -69.5% | -69.5% | -69.5% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 29582.7 | 18142.3 | -38.7% | -38.7% | -38.7% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 82390.7 | 18142.3 | -78.0% | -78.0% | -78.0% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 17307.0 | 8069.7 | -53.4% | -53.4% | -53.4% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 32741.7 | 8069.7 | -75.4% | -75.4% | -75.4% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4961.7 | 2328.4 | -53.1% | -53.1% | -53.1% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 4375.3 | 2328.4 | -46.8% | -46.8% | -46.8% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 3851.8 | 1699.1 | -55.9% | -55.9% | -55.9% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2165.8 | 1699.1 | -21.5% | -21.5% | -21.5% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4629.3 | 2932.5 | -36.7% | -36.7% | -36.7% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5577.5 | 2932.5 | -47.4% | -47.4% | -47.4% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4094.1 | 2932.5 | -28.4% | -28.4% | -28.4% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5766.5 | 2932.5 | -49.1% | -49.1% | -49.1% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 16126.0 | 10949.0 | -32.1% | -32.1% | -32.1% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 28178.7 | 10949.0 | -61.1% | -61.1% | -61.1% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 9628.3 | 5422.0 | -43.7% | -43.7% | -43.7% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 12541.7 | 5422.0 | -56.8% | -56.8% | -56.8% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 27342.0 | 36455.0 | +33.3% | +33.3% | +33.3% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 59122.7 | 36455.0 | -38.3% | -38.3% | -38.3% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 14214.8 | 3182.8 | -77.6% | -77.6% | -77.6% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 4233.4 | 3182.8 | -24.8% | -24.8% | -24.8% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 15724.3 | 20693.7 | +31.6% | +31.6% | +31.6% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 32883.4 | 20693.7 | -37.1% | -37.1% | -37.1% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 16981.0 | 35996.4 | +112.0% | +112.0% | +112.0% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 58021.5 | 35996.4 | -38.0% | -38.0% | -38.0% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 5105.3 | 6670.0 | +30.6% | +30.6% | +30.7% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 6723.9 | 6670.0 | -0.8% | -0.8% | -0.8% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 4399.6 | 6670.0 | +51.6% | +51.6% | +51.6% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 34569.0 | 46907.0 | +35.7% | +35.7% | +35.7% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 46884.1 | 46907.0 | +0.0% | +0.0% | +0.0% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 28282.0 | 46907.0 | +65.9% | +65.9% | +65.9% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 2992.0 | 3508.0 | +17.2% | +17.2% | +17.2% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 2268.0 | 3508.0 | +54.7% | +54.7% | +54.7% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 3123.0 | 3508.0 | +12.3% | +12.3% | +12.3% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 4403.0 | 5452.2 | +23.8% | +23.8% | +23.8% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 8009.9 | 5452.2 | -31.9% | -31.9% | -31.9% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 4777.9 | 5452.2 | +14.1% | +14.1% | +14.1% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | strtr() | 2978.3 | 3087.8 | +3.7% | +3.7% | +3.7% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace_callback() | 5063.3 | 3087.8 | -39.0% | -39.0% | -39.0% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | str_replace() | 2970.3 | 3087.8 | +4.0% | +4.0% | +4.0% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace() | 2920.8 | 3087.8 | +5.7% | +5.7% | +5.7% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 5846.5 | 3550.0 | -39.3% | -39.3% | -39.3% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 2586.0 | 3550.0 | +37.3% | +37.3% | +37.4% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 3801.0 | 3550.0 | -6.6% | -6.6% | -6.6% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 7187.2 | 5565.5 | -22.6% | -22.6% | -22.6% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 5240.9 | 5565.5 | +6.2% | +6.2% | +6.2% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 5128.1 | 5565.5 | +8.5% | +8.5% | +8.5% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 51261.0 | 37951.0 | -26.0% | -26.0% | -26.0% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 35034.0 | 37951.0 | +8.3% | +8.3% | +8.3% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 34109.0 | 37951.0 | +11.3% | +11.3% | +11.3% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 107590.0 | 114424.4 | +6.4% | +6.4% | +6.4% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 8165.0 | 114424.4 | +1301.4% | +1301.4% | +1301.4% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 73064.9 | 114424.4 | +56.6% | +56.6% | +56.6% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 7927.0 | 114424.4 | +1343.5% | +1343.5% | +1343.5% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 109704.4 | 136672.3 | +24.6% | +24.6% | +24.6% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 11012.8 | 136672.3 | +1141.0% | +1141.0% | +1141.0% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 78521.1 | 136672.3 | +74.1% | +74.1% | +74.1% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 9572.3 | 136672.3 | +1327.8% | +1327.8% | +1327.8% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 164580.5 | 215881.5 | +31.2% | +31.2% | +31.2% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 17806.5 | 215881.5 | +1112.4% | +1112.4% | +1112.6% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 125740.4 | 215881.5 | +71.7% | +71.7% | +71.7% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 14047.8 | 215881.5 | +1436.8% | +1436.8% | +1436.8% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 1285528.1 | 1665802.6 | +29.6% | +29.6% | +29.6% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 78118.3 | 1665802.6 | +2032.4% | +2032.4% | +2032.5% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 879658.8 | 1665802.6 | +89.4% | +89.4% | +89.4% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 74338.5 | 1665802.6 | +2140.8% | +2140.8% | +2140.8% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 2779.8 | 2883.3 | +3.7% | +3.7% | +3.7% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 2652.3 | 2883.3 | +8.7% | +8.7% | +8.7% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 3839.0 | 2883.3 | -24.9% | -24.9% | -24.9% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 3434.0 | 3553.1 | +3.5% | +3.5% | +3.5% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 4382.5 | 3553.1 | -18.9% | -18.9% | -18.9% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 4326.9 | 3553.1 | -17.9% | -17.9% | -17.9% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 141953.8 | 18228.1 | -87.2% | -87.2% | -87.2% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | preg_match() per term | 206672.6 | 18228.1 | -91.2% | -91.2% | -91.2% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 105315.3 | 8845.4 | -91.6% | -91.6% | -91.6% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 232234.4 | 8845.4 | -96.2% | -96.2% | -96.2% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 171819.9 | 22639.9 | -86.8% | -86.8% | -86.8% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 386494.2 | 22639.9 | -94.1% | -94.1% | -94.1% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 397021.8 | 13986.7 | -96.5% | -96.5% | -96.5% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 180669.2 | 13986.7 | -92.3% | -92.3% | -92.3% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 3169639.4 | 104792.0 | -96.7% | -96.7% | -96.7% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 1438444.7 | 104792.0 | -92.7% | -92.7% | -92.7% |

### Synthetic tasks

#### Dictionary preparation included

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 7138.0 | 1798268.7 | +25092.9% | +25092.8% | +25093.0% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 301823.2 | 1798268.7 | +495.8% | +495.8% | +495.8% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 298453.8 | 1798268.7 | +502.5% | +502.5% | +502.5% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 5841.0 | 229220.1 | +3824.3% | +3824.3% | +3824.3% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 299443.5 | 229220.1 | -23.5% | -23.5% | -23.5% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 296050.3 | 229220.1 | -22.6% | -22.6% | -22.6% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | strtr() | 5017.0 | 13600.0 | +171.1% | +171.1% | +171.1% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace_callback() | 79321.0 | 13600.0 | -82.9% | -82.9% | -82.9% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace() | 66822.1 | 13600.0 | -79.6% | -79.6% | -79.6% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | strtr() | 4232.0 | 10007.0 | +136.5% | +136.5% | +136.5% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | preg_replace_callback() | 19093.0 | 10007.0 | -47.6% | -47.6% | -47.6% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 7032.0 | 1939266.6 | +27477.7% | +27477.7% | +27477.8% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 271268.1 | 1939266.6 | +614.9% | +614.9% | +614.9% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 267909.1 | 1939266.6 | +623.9% | +623.9% | +623.9% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 5680.0 | 231429.0 | +3974.5% | +3974.5% | +3974.5% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 268895.1 | 231429.0 | -13.9% | -13.9% | -13.9% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 265508.0 | 231429.0 | -12.8% | -12.8% | -12.8% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | strtr() | 4917.0 | 13514.0 | +174.8% | +174.8% | +174.8% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace_callback() | 80161.9 | 13514.0 | -83.1% | -83.1% | -83.1% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace() | 67962.0 | 13514.0 | -80.1% | -80.1% | -80.1% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | strtr() | 4071.0 | 10662.0 | +161.9% | +161.9% | +161.9% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | preg_replace_callback() | 18815.0 | 10662.0 | -43.3% | -43.3% | -43.3% |

#### Dictionary already prepared

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 7138.0 | 5363.0 | -24.9% | -24.9% | -24.9% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 11680.0 | 5363.0 | -54.1% | -54.1% | -54.1% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 8964.0 | 5363.0 | -40.2% | -40.2% | -40.2% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 5841.0 | 5363.0 | -8.2% | -8.2% | -8.2% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 9301.0 | 5363.0 | -42.3% | -42.3% | -42.3% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 6535.0 | 5363.0 | -17.9% | -17.9% | -17.9% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | strtr() | 5017.0 | 5483.0 | +9.3% | +9.3% | +9.3% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace_callback() | 17612.0 | 5483.0 | -68.9% | -68.9% | -68.9% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace() | 5766.0 | 5483.0 | -4.9% | -4.9% | -4.9% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | strtr() | 4232.0 | 3057.0 | -27.8% | -27.8% | -27.8% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | preg_replace_callback() | 9212.0 | 3057.0 | -66.8% | -66.8% | -66.8% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 7032.0 | 5565.0 | -20.9% | -20.9% | -20.9% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 11622.0 | 5565.0 | -52.1% | -52.1% | -52.1% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 8900.0 | 5565.0 | -37.5% | -37.5% | -37.5% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 5680.0 | 5565.0 | -2.0% | -2.0% | -2.0% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 9249.0 | 5565.0 | -39.8% | -39.8% | -39.8% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 6471.0 | 5565.0 | -14.0% | -14.0% | -14.0% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | strtr() | 4917.0 | 5620.0 | +14.3% | +14.3% | +14.3% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace_callback() | 17275.0 | 5620.0 | -67.5% | -67.5% | -67.5% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace() | 5712.0 | 5620.0 | -1.6% | -1.6% | -1.6% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | strtr() | 4071.0 | 3132.0 | -23.1% | -23.1% | -23.1% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | preg_replace_callback() | 9069.0 | 3132.0 | -65.5% | -65.5% | -65.5% |

## Size series

### Product tasks

#### Dictionary preparation included

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 3872.6 | 23302.6 | +501.7% | +501.7% | +501.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 10726.2 | 23302.6 | +117.2% | +117.2% | +117.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | str_contains() loop | 2751.6 | 22413.4 | +714.5% | +714.5% | +714.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | preg_match() | 8915.9 | 22413.4 | +151.4% | +151.4% | +151.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | str_contains() loop | 3149.4 | 23650.0 | +650.9% | +650.9% | +650.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | preg_match() | 11530.4 | 23650.0 | +105.1% | +105.1% | +105.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | str_contains() loop | 2880.0 | 23767.0 | +725.2% | +725.2% | +725.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | preg_match() | 11496.4 | 23767.0 | +106.7% | +106.7% | +106.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 11352.7 | 32457.4 | +185.9% | +185.9% | +185.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 30088.7 | 32457.4 | +7.9% | +7.9% | +7.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | str_contains() loop | 5066.0 | 26089.6 | +415.0% | +415.0% | +415.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | preg_match() | 16759.6 | 26089.6 | +55.7% | +55.7% | +55.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 6239.6 | 62843.7 | +907.2% | +907.1% | +907.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 19359.6 | 62843.7 | +224.6% | +224.6% | +224.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | str_contains() loop | 3895.9 | 61954.3 | +1490.3% | +1490.2% | +1490.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | preg_match() | 15774.9 | 61954.3 | +292.7% | +292.7% | +292.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | str_contains() loop | 4523.8 | 63191.0 | +1296.9% | +1296.8% | +1296.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | preg_match() | 20898.9 | 63191.0 | +202.4% | +202.4% | +202.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | str_contains() loop | 4063.9 | 63308.0 | +1457.8% | +1457.8% | +1457.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | preg_match() | 21262.9 | 63308.0 | +197.7% | +197.7% | +197.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 19275.7 | 70982.3 | +268.2% | +268.2% | +268.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 56005.3 | 70982.3 | +26.7% | +26.7% | +26.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | str_contains() loop | 7421.3 | 64614.7 | +770.7% | +770.7% | +770.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | preg_match() | 30641.0 | 64614.7 | +110.9% | +110.9% | +110.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 11372.3 | 182319.7 | +1503.2% | +1503.2% | +1503.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 39938.3 | 182319.7 | +356.5% | +356.5% | +356.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | str_contains() loop | 6717.6 | 181430.4 | +2600.8% | +2600.8% | +2600.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | preg_match() | 30181.9 | 181430.4 | +501.1% | +501.1% | +501.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | str_contains() loop | 8064.7 | 183498.1 | +2175.3% | +2175.3% | +2175.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | preg_match() | 43674.8 | 183498.1 | +320.1% | +320.1% | +320.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | str_contains() loop | 6888.5 | 182784.1 | +2553.5% | +2553.5% | +2553.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | preg_match() | 44439.8 | 182784.1 | +311.3% | +311.3% | +311.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 40236.7 | 193352.6 | +380.5% | +380.5% | +380.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 135081.8 | 193352.6 | +43.1% | +43.1% | +43.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | str_contains() loop | 15927.3 | 186984.8 | +1074.0% | +1074.0% | +1074.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | preg_match() | 68478.4 | 186984.8 | +173.1% | +173.1% | +173.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 21321.3 | 361724.7 | +1596.5% | +1596.5% | +1596.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 84006.2 | 361724.7 | +330.6% | +330.6% | +330.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | str_contains() loop | 12523.2 | 360835.5 | +2781.3% | +2781.3% | +2781.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | preg_match() | 57018.8 | 360835.5 | +532.8% | +532.8% | +532.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | str_contains() loop | 15412.0 | 362072.5 | +2249.3% | +2249.3% | +2249.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | preg_match() | 93227.0 | 362072.5 | +288.4% | +288.4% | +288.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | str_contains() loop | 12943.1 | 362189.1 | +2698.3% | +2698.3% | +2698.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | preg_match() | 96124.3 | 362189.1 | +276.8% | +276.8% | +276.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 76143.7 | 372648.5 | +389.4% | +389.4% | +389.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 352981.4 | 372648.5 | +5.6% | +5.6% | +5.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | str_contains() loop | 32333.4 | 366280.8 | +1032.8% | +1032.8% | +1032.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | preg_match() | 165712.1 | 366280.8 | +121.0% | +121.0% | +121.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 40722.6 | 752210.1 | +1747.2% | +1747.1% | +1747.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 164403.7 | 752210.1 | +357.5% | +357.5% | +357.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | str_contains() loop | 23554.1 | 751319.8 | +3089.8% | +3089.8% | +3089.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | preg_match() | 110667.8 | 751319.8 | +578.9% | +578.9% | +578.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | str_contains() loop | 29162.3 | 752557.5 | +2480.6% | +2480.5% | +2480.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | preg_match() | 183491.9 | 752557.5 | +310.1% | +310.1% | +310.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | str_contains() loop | 24107.9 | 752674.2 | +3022.1% | +3022.1% | +3022.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | preg_match() | 188009.3 | 752674.2 | +300.3% | +300.3% | +300.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 146075.4 | 755020.5 | +416.9% | +416.9% | +416.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 701991.8 | 755020.5 | +7.6% | +7.6% | +7.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | str_contains() loop | 61607.4 | 748652.9 | +1115.2% | +1115.2% | +1115.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | preg_match() | 328867.3 | 748652.9 | +127.6% | +127.6% | +127.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 80769.3 | 1433937.4 | +1675.3% | +1675.3% | +1675.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 331215.2 | 1433937.4 | +332.9% | +332.9% | +332.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | str_contains() loop | 45763.7 | 1433049.7 | +3031.4% | +3031.4% | +3031.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | preg_match() | 216655.8 | 1433049.7 | +561.4% | +561.4% | +561.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | str_contains() loop | 57169.4 | 1434284.8 | +2408.8% | +2408.8% | +2408.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | preg_match() | 371240.2 | 1434284.8 | +286.3% | +286.3% | +286.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | str_contains() loop | 46922.4 | 1434403.4 | +2957.0% | +2956.9% | +2957.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | preg_match() | 379990.4 | 1434403.4 | +277.5% | +277.5% | +277.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 299095.6 | 1439766.5 | +381.4% | +381.4% | +381.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 1441218.3 | 1439766.5 | -0.1% | -0.1% | -0.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | str_contains() loop | 124814.6 | 1433398.6 | +1048.4% | +1048.4% | +1048.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | preg_match() | 671413.7 | 1433398.6 | +113.5% | +113.5% | +113.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 161144.1 | 2609532.8 | +1519.4% | +1519.4% | +1519.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 657989.4 | 2609532.8 | +296.6% | +296.6% | +296.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | str_contains() loop | 91036.6 | 2608646.9 | +2765.5% | +2765.5% | +2765.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | preg_match() | 425625.9 | 2608646.9 | +512.9% | +512.9% | +512.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | str_contains() loop | 114421.2 | 2609881.0 | +2180.9% | +2180.9% | +2181.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | preg_match() | 737422.8 | 2609881.0 | +253.9% | +253.9% | +253.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | str_contains() loop | 92867.5 | 2609997.8 | +2710.5% | +2710.4% | +2710.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | preg_match() | 754967.6 | 2609997.8 | +245.7% | +245.7% | +245.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 606321.5 | 2619267.0 | +332.0% | +332.0% | +332.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 2921221.8 | 2619267.0 | -10.3% | -10.3% | -10.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | str_contains() loop | 257023.9 | 2612898.8 | +916.6% | +916.6% | +916.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | preg_match() | 1346891.0 | 2612898.8 | +94.0% | +94.0% | +94.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 15058.1 | 51063.6 | +239.1% | +239.1% | +239.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | preg_match() per term | 29911.9 | 51063.6 | +70.7% | +70.7% | +70.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 12018.8 | 46906.0 | +290.3% | +290.3% | +290.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 33344.3 | 46906.0 | +40.7% | +40.7% | +40.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 18901.8 | 50675.3 | +168.1% | +168.1% | +168.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 53961.7 | 50675.3 | -6.1% | -6.1% | -6.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 27152.9 | 87928.8 | +223.8% | +223.8% | +223.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | preg_match() per term | 55511.7 | 87928.8 | +58.4% | +58.4% | +58.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 22021.8 | 84007.0 | +281.5% | +281.5% | +281.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 63435.6 | 84007.0 | +32.4% | +32.4% | +32.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 34877.6 | 89058.3 | +155.3% | +155.3% | +155.3% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 102098.9 | 89058.3 | -12.8% | -12.8% | -12.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 50241.4 | 158420.8 | +215.3% | +215.3% | +215.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | preg_match() per term | 106946.4 | 158420.8 | +48.1% | +48.1% | +48.1% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 39434.5 | 152515.1 | +286.8% | +286.8% | +286.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 118702.2 | 152515.1 | +28.5% | +28.5% | +28.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 65191.9 | 159810.0 | +145.1% | +145.1% | +145.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 192134.7 | 159810.0 | -16.8% | -16.8% | -16.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 95903.7 | 340557.8 | +255.1% | +255.1% | +255.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | preg_match() per term | 201910.6 | 340557.8 | +68.7% | +68.7% | +68.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 76829.2 | 332224.8 | +332.4% | +332.4% | +332.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 229752.4 | 332224.8 | +44.6% | +44.6% | +44.6% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 120484.7 | 342108.7 | +183.9% | +183.9% | +183.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 362032.1 | 342108.7 | -5.5% | -5.5% | -5.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 174352.5 | 769196.4 | +341.2% | +341.2% | +341.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | preg_match() per term | 386905.8 | 769196.4 | +98.8% | +98.8% | +98.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 141753.2 | 759918.2 | +436.1% | +436.1% | +436.1% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 433971.6 | 759918.2 | +75.1% | +75.1% | +75.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 210374.0 | 775686.4 | +268.7% | +268.7% | +268.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 661304.9 | 775686.4 | +17.3% | +17.3% | +17.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 306280.5 | 1647370.5 | +437.9% | +437.9% | +437.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | preg_match() per term | 718322.3 | 1647370.5 | +129.3% | +129.3% | +129.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 282277.6 | 1637983.4 | +480.3% | +480.3% | +480.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 860153.4 | 1637983.4 | +90.4% | +90.4% | +90.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 351649.1 | 1652590.5 | +370.0% | +370.0% | +370.0% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 1220529.2 | 1652590.5 | +35.4% | +35.4% | +35.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 562762.8 | 4727102.8 | +740.0% | +740.0% | +740.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | preg_match() per term | 1370389.7 | 4727102.8 | +244.9% | +244.9% | +244.9% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 556545.6 | 4717646.4 | +747.7% | +747.7% | +747.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 1690890.7 | 4717646.4 | +179.0% | +179.0% | +179.0% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 626820.8 | 4741208.6 | +656.4% | +656.4% | +656.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 2310725.1 | 4741208.6 | +105.2% | +105.2% | +105.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 75958.2 | 57986.9 | -23.7% | -23.7% | -23.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 31007.2 | 57986.9 | +87.0% | +87.0% | +87.0% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 601541.4 | 132893.2 | -77.9% | -77.9% | -77.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 81284.0 | 132893.2 | +63.5% | +63.5% | +63.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 114537.9 | 103900.4 | -9.3% | -9.3% | -9.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 80941.6 | 103900.4 | +28.4% | +28.4% | +28.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 909844.8 | 184272.1 | -79.7% | -79.7% | -79.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 283080.1 | 184272.1 | -34.9% | -34.9% | -34.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 204484.8 | 188303.8 | -7.9% | -7.9% | -7.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 170322.5 | 188303.8 | +10.6% | +10.6% | +10.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 1629539.6 | 274569.4 | -83.2% | -83.2% | -83.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 580497.0 | 274569.4 | -52.7% | -52.7% | -52.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 371102.3 | 389577.8 | +5.0% | +5.0% | +5.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 389981.9 | 389577.8 | -0.1% | -0.1% | -0.1% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 2962758.0 | 476176.5 | -83.9% | -83.9% | -83.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 1282917.2 | 476176.5 | -62.9% | -62.9% | -62.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 451009.8 | 813630.3 | +80.4% | +80.4% | +80.4% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 802861.6 | 813630.3 | +1.3% | +1.3% | +1.3% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 3601587.4 | 894050.1 | -75.2% | -75.2% | -75.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 2373333.0 | 894050.1 | -62.3% | -62.3% | -62.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 491700.6 | 1628816.7 | +231.3% | +231.3% | +231.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 1849226.7 | 1628816.7 | -11.9% | -11.9% | -11.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 3927370.7 | 1705919.3 | -56.6% | -56.6% | -56.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 4876854.1 | 1705919.3 | -65.0% | -65.0% | -65.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 504958.1 | 4360529.5 | +763.5% | +763.5% | +763.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 4035980.9 | 4360529.5 | +8.0% | +8.0% | +8.0% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 4033002.5 | 4485566.1 | +11.2% | +11.2% | +11.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 9921727.1 | 4485566.1 | -54.8% | -54.8% | -54.8% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 3807.5 | 24791.6 | +551.1% | +551.1% | +551.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 10673.3 | 24791.6 | +132.3% | +132.3% | +132.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | str_contains() loop | 2716.2 | 23902.4 | +780.0% | +780.0% | +780.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | preg_match() | 8864.9 | 23902.4 | +169.6% | +169.6% | +169.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | str_contains() loop | 3111.9 | 25139.0 | +707.8% | +707.8% | +707.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | preg_match() | 11479.4 | 25139.0 | +119.0% | +119.0% | +119.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | str_contains() loop | 2843.5 | 25256.0 | +788.2% | +788.2% | +788.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | preg_match() | 11445.4 | 25256.0 | +120.7% | +120.7% | +120.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 11286.3 | 33946.3 | +200.8% | +200.8% | +200.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 30035.7 | 33946.3 | +13.0% | +13.0% | +13.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | str_contains() loop | 5069.0 | 27578.6 | +444.1% | +444.0% | +444.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | preg_match() | 16708.7 | 27578.6 | +65.1% | +65.0% | +65.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 6116.6 | 67261.6 | +999.7% | +999.6% | +999.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 19020.6 | 67261.6 | +253.6% | +253.6% | +253.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | str_contains() loop | 3833.1 | 66372.4 | +1631.5% | +1631.5% | +1631.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | preg_match() | 15437.9 | 66372.4 | +329.9% | +329.9% | +329.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | str_contains() loop | 4457.4 | 67609.0 | +1416.8% | +1416.8% | +1416.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | preg_match() | 20561.9 | 67609.0 | +228.8% | +228.8% | +228.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | str_contains() loop | 4000.5 | 67726.0 | +1592.9% | +1592.9% | +1592.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | preg_match() | 20925.9 | 67726.0 | +223.6% | +223.6% | +223.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 19067.3 | 75401.4 | +295.4% | +295.4% | +295.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 55666.3 | 75401.4 | +35.5% | +35.5% | +35.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | str_contains() loop | 7379.0 | 69033.7 | +835.5% | +835.5% | +835.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | preg_match() | 30304.0 | 69033.7 | +127.8% | +127.8% | +127.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 11132.8 | 195924.7 | +1659.9% | +1659.8% | +1659.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 38877.3 | 195924.7 | +404.0% | +404.0% | +404.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | str_contains() loop | 6586.5 | 195035.4 | +2861.1% | +2861.1% | +2861.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | preg_match() | 29122.9 | 195035.4 | +569.7% | +569.7% | +569.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | str_contains() loop | 7925.5 | 197109.1 | +2387.0% | +2386.9% | +2387.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | preg_match() | 42615.8 | 197109.1 | +362.5% | +362.5% | +362.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | str_contains() loop | 6757.7 | 196388.9 | +2806.1% | +2806.1% | +2806.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | preg_match() | 43380.7 | 196388.9 | +352.7% | +352.7% | +352.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 39726.7 | 206975.3 | +421.0% | +421.0% | +421.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 134021.0 | 206975.3 | +54.4% | +54.4% | +54.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | str_contains() loop | 15769.3 | 200607.8 | +1172.1% | +1172.1% | +1172.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | preg_match() | 67419.3 | 200607.8 | +197.6% | +197.6% | +197.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 20820.4 | 389432.5 | +1770.4% | +1770.4% | +1770.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 81928.2 | 389432.5 | +375.3% | +375.3% | +375.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | str_contains() loop | 12255.6 | 388543.5 | +3070.3% | +3070.3% | +3070.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | preg_match() | 54942.8 | 388543.5 | +607.2% | +607.2% | +607.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | str_contains() loop | 15115.5 | 389780.1 | +2478.7% | +2478.6% | +2478.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | preg_match() | 91151.0 | 389780.1 | +327.6% | +327.6% | +327.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | str_contains() loop | 12678.6 | 389897.1 | +2975.2% | +2975.2% | +2975.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | preg_match() | 94048.5 | 389897.1 | +314.6% | +314.6% | +314.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 74963.0 | 400354.7 | +434.1% | +434.1% | +434.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 350903.4 | 400354.7 | +14.1% | +14.1% | +14.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | str_contains() loop | 31923.3 | 393987.7 | +1134.2% | +1134.2% | +1134.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | preg_match() | 163636.0 | 393987.7 | +140.8% | +140.8% | +140.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 39729.9 | 809819.2 | +1938.3% | +1938.3% | +1938.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 160263.8 | 809819.2 | +405.3% | +405.3% | +405.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | str_contains() loop | 23020.5 | 808929.1 | +3413.9% | +3413.9% | +3414.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | preg_match() | 106529.9 | 808929.1 | +659.3% | +659.3% | +659.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | str_contains() loop | 28575.2 | 810167.2 | +2735.2% | +2735.2% | +2735.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | preg_match() | 179354.2 | 810167.2 | +351.7% | +351.7% | +351.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | str_contains() loop | 23584.5 | 810284.3 | +3335.7% | +3335.6% | +3335.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | preg_match() | 183871.2 | 810284.3 | +340.7% | +340.7% | +340.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 143835.4 | 812595.3 | +464.9% | +464.9% | +465.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 697851.4 | 812595.3 | +16.4% | +16.4% | +16.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | str_contains() loop | 60701.7 | 806228.0 | +1228.2% | +1228.2% | +1228.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | preg_match() | 324729.4 | 806228.0 | +148.3% | +148.3% | +148.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 78772.6 | 1546841.7 | +1863.7% | +1863.7% | +1863.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 323336.4 | 1546841.7 | +378.4% | +378.4% | +378.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | str_contains() loop | 44684.2 | 1545951.3 | +3359.7% | +3359.7% | +3359.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | preg_match() | 208778.8 | 1545951.3 | +640.5% | +640.5% | +640.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | str_contains() loop | 55981.8 | 1547189.2 | +2663.7% | +2663.7% | +2663.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | preg_match() | 363363.1 | 1547189.2 | +325.8% | +325.8% | +325.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | str_contains() loop | 45836.9 | 1547305.0 | +3275.7% | +3275.7% | +3275.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | preg_match() | 372113.0 | 1547305.0 | +315.8% | +315.8% | +315.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 294268.4 | 1552685.5 | +427.6% | +427.6% | +427.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 1433342.8 | 1552685.5 | +8.3% | +8.3% | +8.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | str_contains() loop | 122882.9 | 1546316.8 | +1158.4% | +1158.4% | +1158.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | preg_match() | 663540.2 | 1546316.8 | +133.0% | +133.0% | +133.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 157140.9 | 2815548.9 | +1691.7% | +1691.7% | +1691.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 643273.4 | 2815548.9 | +337.7% | +337.7% | +337.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | str_contains() loop | 88904.4 | 2814658.6 | +3065.9% | +3065.9% | +3065.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | preg_match() | 410913.1 | 2814658.6 | +585.0% | +585.0% | +585.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | str_contains() loop | 112021.1 | 2815896.7 | +2413.7% | +2413.7% | +2413.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | preg_match() | 722710.4 | 2815896.7 | +289.6% | +289.6% | +289.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | str_contains() loop | 90701.6 | 2816013.7 | +3004.7% | +3004.7% | +3004.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | preg_match() | 740253.8 | 2816013.7 | +280.4% | +280.4% | +280.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 596602.3 | 2825279.8 | +373.6% | +373.6% | +373.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 2906508.0 | 2825279.8 | -2.8% | -2.8% | -2.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | str_contains() loop | 253075.6 | 2818911.2 | +1013.9% | +1013.9% | +1013.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | preg_match() | 1332176.5 | 2818911.2 | +111.6% | +111.6% | +111.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 15124.3 | 54620.2 | +261.1% | +261.1% | +261.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | preg_match() per term | 29802.1 | 54620.2 | +83.3% | +83.3% | +83.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 11629.4 | 50061.4 | +330.5% | +330.5% | +330.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 33242.5 | 50061.4 | +50.6% | +50.6% | +50.6% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 18727.1 | 53459.5 | +185.5% | +185.5% | +185.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 53542.4 | 53459.5 | -0.2% | -0.2% | -0.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 27243.4 | 94126.9 | +245.5% | +245.5% | +245.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | preg_match() per term | 55316.6 | 94126.9 | +70.2% | +70.2% | +70.2% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 21229.6 | 89791.4 | +323.0% | +323.0% | +323.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 63189.1 | 89791.4 | +42.1% | +42.1% | +42.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 34548.5 | 94518.6 | +173.6% | +173.6% | +173.6% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 101328.2 | 94518.6 | -6.7% | -6.7% | -6.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 50561.2 | 169429.2 | +235.1% | +235.1% | +235.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | preg_match() per term | 106649.5 | 169429.2 | +58.9% | +58.9% | +58.9% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 38031.1 | 163112.3 | +328.9% | +328.9% | +328.9% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 118136.7 | 163112.3 | +38.1% | +38.1% | +38.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 64831.4 | 170168.2 | +162.5% | +162.5% | +162.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 190712.0 | 170168.2 | -10.8% | -10.8% | -10.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 96299.1 | 365455.3 | +279.5% | +279.5% | +279.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | preg_match() per term | 201153.3 | 365455.3 | +81.7% | +81.7% | +81.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 74010.1 | 356714.3 | +382.0% | +382.0% | +382.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 228314.7 | 356714.3 | +56.2% | +56.2% | +56.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 119474.4 | 366447.1 | +206.7% | +206.7% | +206.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 358854.4 | 366447.1 | +2.1% | +2.1% | +2.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 174671.9 | 827252.4 | +373.6% | +373.6% | +373.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | preg_match() per term | 384696.1 | 827252.4 | +115.0% | +115.0% | +115.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 136533.2 | 817574.0 | +498.8% | +498.8% | +498.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 430433.9 | 817574.0 | +89.9% | +89.9% | +89.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 208039.3 | 833283.2 | +300.5% | +300.5% | +300.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 654043.3 | 833283.2 | +27.4% | +27.4% | +27.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 303853.4 | 1772794.3 | +483.4% | +483.4% | +483.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | preg_match() per term | 710334.6 | 1772794.3 | +149.6% | +149.6% | +149.6% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 272392.0 | 1763012.7 | +547.2% | +547.2% | +547.2% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 850739.9 | 1763012.7 | +107.2% | +107.2% | +107.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 344696.2 | 1777592.7 | +415.7% | +415.7% | +415.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 1202105.7 | 1777592.7 | +47.9% | +47.9% | +47.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 555040.1 | 5114452.7 | +821.5% | +821.5% | +821.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | preg_match() per term | 1351744.4 | 5114452.7 | +278.4% | +278.4% | +278.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 537159.5 | 5104595.1 | +850.3% | +850.3% | +850.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 1670634.2 | 5104595.1 | +205.5% | +205.5% | +205.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 610403.0 | 5128116.5 | +740.1% | +740.1% | +740.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 2270771.2 | 5128116.5 | +125.8% | +125.8% | +125.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 76802.3 | 62097.8 | -19.1% | -19.1% | -19.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 30969.5 | 62097.8 | +100.5% | +100.5% | +100.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 608277.9 | 141738.2 | -76.7% | -76.7% | -76.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 80755.0 | 141738.2 | +75.5% | +75.5% | +75.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 116525.4 | 111273.4 | -4.5% | -4.5% | -4.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 81275.8 | 111273.4 | +36.9% | +36.9% | +36.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 925733.7 | 195612.2 | -78.9% | -78.9% | -78.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 282595.1 | 195612.2 | -30.8% | -30.8% | -30.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 210240.6 | 201843.0 | -4.0% | -4.0% | -4.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 170924.5 | 201843.0 | +18.1% | +18.1% | +18.1% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 1675547.8 | 291342.1 | -82.6% | -82.6% | -82.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 579705.0 | 291342.1 | -49.7% | -49.7% | -49.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 381689.1 | 419104.6 | +9.8% | +9.8% | +9.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 392136.5 | 419104.6 | +6.9% | +6.9% | +6.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 3047445.1 | 508631.8 | -83.3% | -83.3% | -83.3% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 1282860.2 | 508631.8 | -60.4% | -60.4% | -60.4% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 461943.5 | 876157.9 | +89.7% | +89.7% | +89.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 807924.1 | 876157.9 | +8.4% | +8.4% | +8.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 3689074.3 | 959318.9 | -74.0% | -74.0% | -74.0% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 2375165.7 | 959318.9 | -59.6% | -59.6% | -59.6% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 503416.1 | 1754162.3 | +248.5% | +248.5% | +248.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 1863016.9 | 1754162.3 | -5.8% | -5.8% | -5.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 4021094.6 | 1833944.6 | -54.4% | -54.4% | -54.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 4887388.7 | 1833944.6 | -62.5% | -62.5% | -62.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 517259.1 | 4723145.4 | +813.1% | +813.1% | +813.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 4068514.5 | 4723145.4 | +16.1% | +16.1% | +16.1% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 4131405.0 | 4850847.8 | +17.4% | +17.4% | +17.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 9950952.4 | 4850847.8 | -51.3% | -51.3% | -51.3% |

#### Dictionary already prepared

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 3872.6 | 2431.6 | -37.2% | -37.2% | -37.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 3823.3 | 2431.6 | -36.4% | -36.4% | -36.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | str_contains() loop | 2751.6 | 1542.4 | -43.9% | -43.9% | -43.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | preg_match() | 2012.9 | 1542.4 | -23.4% | -23.4% | -23.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | str_contains() loop | 3149.4 | 2779.0 | -11.8% | -11.8% | -11.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | preg_match() | 4627.4 | 2779.0 | -39.9% | -39.9% | -39.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | str_contains() loop | 2880.0 | 2896.0 | +0.6% | +0.6% | +0.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | preg_match() | 4593.4 | 2896.0 | -37.0% | -37.0% | -37.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 11352.7 | 11586.3 | +2.1% | +2.1% | +2.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 23185.7 | 11586.3 | -50.0% | -50.0% | -50.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | str_contains() loop | 5066.0 | 5218.7 | +3.0% | +3.0% | +3.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | preg_match() | 9856.7 | 5218.7 | -47.1% | -47.1% | -47.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 6239.6 | 2431.6 | -61.0% | -61.0% | -61.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 5686.6 | 2431.6 | -57.2% | -57.2% | -57.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | str_contains() loop | 3895.9 | 1542.4 | -60.4% | -60.4% | -60.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | preg_match() | 2101.9 | 1542.4 | -26.6% | -26.6% | -26.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | str_contains() loop | 4523.8 | 2779.0 | -38.6% | -38.6% | -38.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | preg_match() | 7225.9 | 2779.0 | -61.5% | -61.5% | -61.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | str_contains() loop | 4063.9 | 2896.0 | -28.7% | -28.7% | -28.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | preg_match() | 7589.9 | 2896.0 | -61.8% | -61.8% | -61.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 19275.6 | 11586.3 | -39.9% | -39.9% | -39.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 42332.3 | 11586.3 | -72.6% | -72.6% | -72.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | str_contains() loop | 7421.3 | 5218.7 | -29.7% | -29.7% | -29.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | preg_match() | 16968.0 | 5218.7 | -69.2% | -69.2% | -69.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 11372.3 | 2431.6 | -78.6% | -78.6% | -78.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 12076.3 | 2431.6 | -79.9% | -79.9% | -79.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | str_contains() loop | 6717.6 | 1542.4 | -77.0% | -77.0% | -77.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | preg_match() | 2319.9 | 1542.4 | -33.5% | -33.5% | -33.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | str_contains() loop | 8064.7 | 2779.0 | -65.5% | -65.5% | -65.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | preg_match() | 15812.8 | 2779.0 | -82.4% | -82.4% | -82.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | str_contains() loop | 6888.5 | 2896.0 | -58.0% | -58.0% | -58.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | preg_match() | 16577.7 | 2896.0 | -82.5% | -82.5% | -82.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 40236.7 | 11586.3 | -71.2% | -71.2% | -71.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 107220.0 | 11586.3 | -89.2% | -89.2% | -89.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | str_contains() loop | 15927.3 | 5218.7 | -67.2% | -67.2% | -67.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | preg_match() | 40616.4 | 5218.7 | -87.2% | -87.2% | -87.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 21321.3 | 2431.6 | -88.6% | -88.6% | -88.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 29696.3 | 2431.6 | -91.8% | -91.8% | -91.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | str_contains() loop | 12523.3 | 1542.4 | -87.7% | -87.7% | -87.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | preg_match() | 2708.8 | 1542.4 | -43.1% | -43.1% | -43.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | str_contains() loop | 15412.0 | 2779.0 | -82.0% | -82.0% | -82.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | preg_match() | 38917.0 | 2779.0 | -92.9% | -92.9% | -92.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | str_contains() loop | 12943.1 | 2896.0 | -77.6% | -77.6% | -77.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | preg_match() | 41814.5 | 2896.0 | -93.1% | -93.1% | -93.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 76143.7 | 11586.4 | -84.8% | -84.8% | -84.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 298671.3 | 11586.4 | -96.1% | -96.1% | -96.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | str_contains() loop | 32333.4 | 5218.7 | -83.9% | -83.9% | -83.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | preg_match() | 111402.1 | 5218.7 | -95.3% | -95.3% | -95.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 40722.5 | 2431.6 | -94.0% | -94.0% | -94.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 57230.8 | 2431.6 | -95.8% | -95.8% | -95.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | str_contains() loop | 23554.1 | 1542.4 | -93.5% | -93.5% | -93.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | preg_match() | 3494.8 | 1542.4 | -55.9% | -55.9% | -55.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | str_contains() loop | 29162.3 | 2779.0 | -90.5% | -90.5% | -90.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | preg_match() | 76318.9 | 2779.0 | -96.4% | -96.4% | -96.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | str_contains() loop | 24107.9 | 2896.0 | -88.0% | -88.0% | -88.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | preg_match() | 80836.0 | 2896.0 | -96.4% | -96.4% | -96.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 146075.6 | 11586.3 | -92.1% | -92.1% | -92.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 594818.5 | 11586.3 | -98.1% | -98.1% | -98.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | str_contains() loop | 61607.3 | 5218.7 | -91.5% | -91.5% | -91.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | preg_match() | 221694.5 | 5218.7 | -97.6% | -97.6% | -97.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 80769.4 | 2431.6 | -97.0% | -97.0% | -97.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 119580.3 | 2431.6 | -98.0% | -98.0% | -98.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | str_contains() loop | 45763.7 | 1542.4 | -96.6% | -96.6% | -96.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | preg_match() | 5020.6 | 1542.4 | -69.3% | -69.3% | -69.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | str_contains() loop | 57169.2 | 2779.0 | -95.1% | -95.1% | -95.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | preg_match() | 159605.0 | 2779.0 | -98.3% | -98.3% | -98.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | str_contains() loop | 46922.4 | 2896.0 | -93.8% | -93.8% | -93.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | preg_match() | 168355.5 | 2896.0 | -98.3% | -98.3% | -98.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 299095.3 | 11586.3 | -96.1% | -96.1% | -96.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 1229615.5 | 11586.3 | -99.1% | -99.1% | -99.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | str_contains() loop | 124814.9 | 5218.7 | -95.8% | -95.8% | -95.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | preg_match() | 459809.6 | 5218.7 | -98.9% | -98.9% | -98.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 161144.0 | 2431.6 | -98.5% | -98.5% | -98.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 240391.4 | 2431.6 | -99.0% | -99.0% | -99.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | str_contains() loop | 91036.4 | 1542.4 | -98.3% | -98.3% | -98.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | preg_match() | 8029.0 | 1542.4 | -80.8% | -80.8% | -80.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | str_contains() loop | 114421.0 | 2779.0 | -97.6% | -97.6% | -97.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | preg_match() | 319826.6 | 2779.0 | -99.1% | -99.1% | -99.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | str_contains() loop | 92868.3 | 2896.0 | -96.9% | -96.9% | -96.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | preg_match() | 337370.0 | 2896.0 | -99.1% | -99.1% | -99.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 606321.0 | 11586.3 | -98.1% | -98.1% | -98.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 2503655.9 | 11586.3 | -99.5% | -99.5% | -99.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | str_contains() loop | 257023.7 | 5218.7 | -98.0% | -98.0% | -98.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | preg_match() | 929316.9 | 5218.7 | -99.4% | -99.4% | -99.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 15058.1 | 12565.6 | -16.6% | -16.6% | -16.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | preg_match() per term | 21119.9 | 12565.6 | -40.5% | -40.5% | -40.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 12018.8 | 8408.0 | -30.0% | -30.0% | -30.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 24109.2 | 8408.0 | -65.1% | -65.1% | -65.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 18901.8 | 12122.2 | -35.9% | -35.9% | -35.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 41687.6 | 12122.2 | -70.9% | -70.9% | -70.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 27152.9 | 13290.8 | -51.1% | -51.1% | -51.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | preg_match() per term | 38374.6 | 13290.8 | -65.4% | -65.4% | -65.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 22021.7 | 8408.0 | -61.8% | -61.8% | -61.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 45417.6 | 8408.0 | -81.5% | -81.5% | -81.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 34877.6 | 13423.4 | -61.5% | -61.5% | -61.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 78002.9 | 13423.4 | -82.8% | -82.8% | -82.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 50241.3 | 14349.9 | -71.4% | -71.4% | -71.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | preg_match() per term | 73228.4 | 14349.9 | -80.4% | -80.4% | -80.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 39434.6 | 8408.0 | -78.7% | -78.7% | -78.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 83222.2 | 8408.0 | -89.9% | -89.9% | -89.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 65191.8 | 15776.1 | -75.8% | -75.8% | -75.8% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 144501.5 | 15776.1 | -89.1% | -89.1% | -89.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 95903.8 | 15661.4 | -83.7% | -83.7% | -83.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | preg_match() per term | 134652.6 | 15661.4 | -88.4% | -88.4% | -88.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 76829.3 | 8408.0 | -89.1% | -89.1% | -89.1% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 158969.2 | 8408.0 | -94.7% | -94.7% | -94.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 120484.7 | 19106.2 | -84.1% | -84.1% | -84.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 266933.0 | 19106.2 | -92.8% | -92.8% | -92.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 174352.4 | 17685.9 | -89.9% | -89.9% | -89.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | preg_match() per term | 251801.7 | 17685.9 | -93.0% | -93.0% | -93.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 141753.2 | 8408.0 | -94.1% | -94.1% | -94.1% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 291843.8 | 8408.0 | -97.1% | -97.1% | -97.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 210374.2 | 22945.5 | -89.1% | -89.1% | -89.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 470557.1 | 22945.5 | -95.1% | -95.1% | -95.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 306280.4 | 17774.8 | -94.2% | -94.2% | -94.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | preg_match() per term | 442262.9 | 17774.8 | -96.0% | -96.0% | -96.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 282277.2 | 8408.0 | -97.0% | -97.0% | -97.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 570096.1 | 8408.0 | -98.5% | -98.5% | -98.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 351649.7 | 23015.4 | -93.5% | -93.5% | -93.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 833261.5 | 23015.4 | -97.2% | -97.2% | -97.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 562764.2 | 17867.8 | -96.8% | -96.8% | -96.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | preg_match() per term | 816956.5 | 17867.8 | -97.8% | -97.8% | -97.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 556544.6 | 8408.0 | -98.5% | -98.5% | -98.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 1109523.3 | 8408.0 | -99.2% | -99.2% | -99.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 626822.3 | 23158.0 | -96.3% | -96.3% | -96.3% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 1535000.7 | 23158.0 | -98.5% | -98.5% | -98.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 75958.3 | 11536.9 | -84.8% | -84.8% | -84.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 8172.9 | 11536.9 | +41.2% | +41.2% | +41.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 601541.1 | 85401.1 | -85.8% | -85.8% | -85.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 58432.0 | 85401.1 | +46.2% | +46.2% | +46.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 114538.2 | 12307.4 | -89.3% | -89.3% | -89.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 29868.2 | 12307.4 | -58.8% | -58.8% | -58.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 909847.1 | 92225.0 | -89.9% | -89.9% | -89.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 231995.0 | 92225.0 | -60.2% | -60.2% | -60.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 204484.9 | 13184.6 | -93.6% | -93.6% | -93.6% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 59591.7 | 13184.6 | -77.9% | -77.9% | -77.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 1629539.5 | 98787.0 | -93.9% | -93.9% | -93.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 469766.1 | 98787.0 | -79.0% | -79.0% | -79.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 371101.9 | 13477.8 | -96.4% | -96.4% | -96.4% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 128552.6 | 13477.8 | -89.5% | -89.5% | -89.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 2962760.8 | 101228.0 | -96.6% | -96.6% | -96.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 1021466.6 | 101228.0 | -90.1% | -90.1% | -90.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 451010.1 | 13605.6 | -97.0% | -97.0% | -97.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 225350.6 | 13605.6 | -94.0% | -94.0% | -94.0% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 3601589.4 | 101906.9 | -97.2% | -97.2% | -97.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 1795854.6 | 101906.9 | -94.3% | -94.3% | -94.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 491701.2 | 13650.1 | -97.2% | -97.2% | -97.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 433517.8 | 13650.1 | -96.9% | -96.9% | -96.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 3927370.0 | 102135.1 | -97.4% | -97.4% | -97.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 3461191.9 | 102135.1 | -97.0% | -97.0% | -97.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 504958.6 | 13670.9 | -97.3% | -97.3% | -97.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 841865.6 | 13670.9 | -98.4% | -98.4% | -98.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 4033009.2 | 102597.2 | -97.5% | -97.5% | -97.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 6727975.0 | 102597.2 | -98.5% | -98.5% | -98.5% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 3807.5 | 2448.6 | -35.7% | -35.7% | -35.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 3829.3 | 2448.6 | -36.1% | -36.1% | -36.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | str_contains() loop | 2716.3 | 1559.4 | -42.6% | -42.6% | -42.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | preg_match() | 2020.9 | 1559.4 | -22.8% | -22.8% | -22.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | str_contains() loop | 3111.9 | 2796.0 | -10.2% | -10.2% | -10.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | preg_match() | 4635.4 | 2796.0 | -39.7% | -39.7% | -39.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | str_contains() loop | 2843.5 | 2913.0 | +2.4% | +2.4% | +2.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | preg_match() | 4601.4 | 2913.0 | -36.7% | -36.7% | -36.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 11286.3 | 11603.3 | +2.8% | +2.8% | +2.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 23191.7 | 11603.3 | -50.0% | -50.0% | -50.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | str_contains() loop | 5069.0 | 5235.7 | +3.3% | +3.3% | +3.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | preg_match() | 9864.7 | 5235.7 | -46.9% | -46.9% | -46.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 6116.6 | 2448.6 | -60.0% | -60.0% | -60.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 5692.6 | 2448.6 | -57.0% | -57.0% | -57.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | str_contains() loop | 3833.1 | 1559.4 | -59.3% | -59.3% | -59.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | preg_match() | 2109.9 | 1559.4 | -26.1% | -26.1% | -26.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | str_contains() loop | 4457.4 | 2796.0 | -37.3% | -37.3% | -37.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | preg_match() | 7233.9 | 2796.0 | -61.3% | -61.3% | -61.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | str_contains() loop | 4000.5 | 2913.0 | -27.2% | -27.2% | -27.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | preg_match() | 7597.9 | 2913.0 | -61.7% | -61.7% | -61.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 19067.3 | 11603.4 | -39.1% | -39.1% | -39.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 42338.3 | 11603.4 | -72.6% | -72.6% | -72.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | str_contains() loop | 7379.0 | 5235.7 | -29.0% | -29.0% | -29.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | preg_match() | 16976.0 | 5235.7 | -69.2% | -69.2% | -69.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 11132.7 | 2448.6 | -78.0% | -78.0% | -78.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 12082.2 | 2448.6 | -79.7% | -79.7% | -79.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | str_contains() loop | 6586.5 | 1559.4 | -76.3% | -76.3% | -76.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | preg_match() | 2327.9 | 1559.4 | -33.0% | -33.0% | -33.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | str_contains() loop | 7925.5 | 2796.0 | -64.7% | -64.7% | -64.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | preg_match() | 15820.8 | 2796.0 | -82.3% | -82.3% | -82.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | str_contains() loop | 6757.7 | 2913.0 | -56.9% | -56.9% | -56.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | preg_match() | 16585.8 | 2913.0 | -82.4% | -82.4% | -82.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 39726.7 | 11603.3 | -70.8% | -70.8% | -70.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 107226.1 | 11603.3 | -89.2% | -89.2% | -89.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | str_contains() loop | 15769.3 | 5235.7 | -66.8% | -66.8% | -66.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | preg_match() | 40624.3 | 5235.7 | -87.1% | -87.1% | -87.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 20820.4 | 2448.6 | -88.2% | -88.2% | -88.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 29702.3 | 2448.6 | -91.8% | -91.8% | -91.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | str_contains() loop | 12255.6 | 1559.4 | -87.3% | -87.3% | -87.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | preg_match() | 2716.7 | 1559.4 | -42.6% | -42.6% | -42.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | str_contains() loop | 15115.5 | 2796.0 | -81.5% | -81.5% | -81.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | preg_match() | 38925.0 | 2796.0 | -92.8% | -92.8% | -92.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | str_contains() loop | 12678.6 | 2913.0 | -77.0% | -77.0% | -77.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | preg_match() | 41822.5 | 2913.0 | -93.0% | -93.0% | -93.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 74963.0 | 11603.3 | -84.5% | -84.5% | -84.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 298677.4 | 11603.3 | -96.1% | -96.1% | -96.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | str_contains() loop | 31923.4 | 5235.7 | -83.6% | -83.6% | -83.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | preg_match() | 111410.0 | 5235.7 | -95.3% | -95.3% | -95.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 39730.1 | 2448.6 | -93.8% | -93.8% | -93.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 57236.8 | 2448.6 | -95.7% | -95.7% | -95.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | str_contains() loop | 23020.5 | 1559.4 | -93.2% | -93.2% | -93.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | preg_match() | 3502.7 | 1559.4 | -55.5% | -55.5% | -55.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | str_contains() loop | 28575.3 | 2796.0 | -90.2% | -90.2% | -90.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | preg_match() | 76327.0 | 2796.0 | -96.3% | -96.3% | -96.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | str_contains() loop | 23584.5 | 2913.0 | -87.6% | -87.6% | -87.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | preg_match() | 80843.9 | 2913.0 | -96.4% | -96.4% | -96.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 143835.5 | 11603.4 | -91.9% | -91.9% | -91.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 594824.3 | 11603.4 | -98.0% | -98.0% | -98.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | str_contains() loop | 60701.6 | 5235.7 | -91.4% | -91.4% | -91.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | preg_match() | 221702.5 | 5235.7 | -97.6% | -97.6% | -97.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 78772.8 | 2448.6 | -96.9% | -96.9% | -96.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 119586.1 | 2448.6 | -98.0% | -98.0% | -98.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | str_contains() loop | 44684.1 | 1559.4 | -96.5% | -96.5% | -96.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | preg_match() | 5028.6 | 1559.4 | -69.0% | -69.0% | -69.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | str_contains() loop | 55982.0 | 2796.0 | -95.0% | -95.0% | -95.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | preg_match() | 159613.1 | 2796.0 | -98.2% | -98.2% | -98.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | str_contains() loop | 45836.9 | 2913.0 | -93.6% | -93.6% | -93.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | preg_match() | 168363.5 | 2913.0 | -98.3% | -98.3% | -98.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 294267.2 | 11603.3 | -96.1% | -96.1% | -96.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 1229622.4 | 11603.3 | -99.1% | -99.1% | -99.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | str_contains() loop | 122883.0 | 5235.7 | -95.7% | -95.7% | -95.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | preg_match() | 459817.8 | 5235.7 | -98.9% | -98.9% | -98.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 157141.3 | 2448.6 | -98.4% | -98.4% | -98.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 240397.8 | 2448.6 | -99.0% | -99.0% | -99.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | str_contains() loop | 88904.5 | 1559.4 | -98.2% | -98.2% | -98.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | preg_match() | 8037.0 | 1559.4 | -80.6% | -80.6% | -80.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | str_contains() loop | 112021.3 | 2796.0 | -97.5% | -97.5% | -97.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | preg_match() | 319834.5 | 2796.0 | -99.1% | -99.1% | -99.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | str_contains() loop | 90701.6 | 2913.0 | -96.8% | -96.8% | -96.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | preg_match() | 337378.0 | 2913.0 | -99.1% | -99.1% | -99.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 596602.9 | 11603.4 | -98.1% | -98.1% | -98.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 2503657.9 | 11603.4 | -99.5% | -99.5% | -99.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | str_contains() loop | 253075.3 | 5235.7 | -97.9% | -97.9% | -97.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | preg_match() | 929324.2 | 5235.7 | -99.4% | -99.4% | -99.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 15124.2 | 13404.2 | -11.4% | -11.4% | -11.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | preg_match() per term | 21562.1 | 13404.2 | -37.8% | -37.8% | -37.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 11629.4 | 8845.4 | -23.9% | -23.9% | -23.9% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 24569.5 | 8845.4 | -64.0% | -64.0% | -64.0% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 18727.1 | 12188.5 | -34.9% | -34.9% | -34.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 42060.4 | 12188.5 | -71.0% | -71.0% | -71.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 27243.4 | 14141.0 | -48.1% | -48.1% | -48.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | preg_match() per term | 39279.6 | 14141.0 | -64.0% | -64.0% | -64.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 21229.6 | 8845.4 | -58.3% | -58.3% | -58.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 46287.1 | 8845.4 | -80.9% | -80.9% | -80.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 34548.5 | 13534.5 | -60.8% | -60.8% | -60.8% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 78807.1 | 13534.5 | -82.8% | -82.8% | -82.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 50561.1 | 15200.2 | -69.9% | -69.9% | -69.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | preg_match() per term | 75124.6 | 15200.2 | -79.8% | -79.8% | -79.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 38031.0 | 8845.4 | -76.7% | -76.7% | -76.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 84881.8 | 8845.4 | -89.6% | -89.6% | -89.6% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 64831.4 | 15965.2 | -75.4% | -75.4% | -75.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 146233.1 | 15965.2 | -89.1% | -89.1% | -89.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 96299.4 | 16511.3 | -82.9% | -82.9% | -82.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | preg_match() per term | 138395.7 | 16511.3 | -88.1% | -88.1% | -88.1% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 74010.0 | 8845.4 | -88.0% | -88.0% | -88.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 162095.2 | 8845.4 | -94.5% | -94.5% | -94.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 119474.7 | 19390.1 | -83.8% | -83.8% | -83.8% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 270174.0 | 19390.1 | -92.8% | -92.8% | -92.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 174671.8 | 18523.8 | -89.4% | -89.4% | -89.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | preg_match() per term | 258875.8 | 18523.8 | -92.8% | -92.8% | -92.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 136533.2 | 8845.4 | -93.5% | -93.5% | -93.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 297694.8 | 8845.4 | -97.0% | -97.0% | -97.0% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 208039.4 | 23337.3 | -88.8% | -88.8% | -88.8% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 476404.7 | 23337.3 | -95.1% | -95.1% | -95.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 303854.3 | 18609.9 | -93.9% | -93.9% | -93.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | preg_match() per term | 454277.3 | 18609.9 | -95.9% | -95.9% | -95.9% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 272391.8 | 8845.4 | -96.8% | -96.8% | -96.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 580852.7 | 8845.4 | -98.5% | -98.5% | -98.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 344696.4 | 23409.7 | -93.2% | -93.2% | -93.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 842394.0 | 23409.7 | -97.2% | -97.2% | -97.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 555040.4 | 18703.2 | -96.6% | -96.6% | -96.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | preg_match() per term | 838838.2 | 18703.2 | -97.8% | -97.8% | -97.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 537159.2 | 8845.4 | -98.4% | -98.4% | -98.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 1130074.3 | 8845.4 | -99.2% | -99.2% | -99.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 610402.7 | 23557.5 | -96.1% | -96.1% | -96.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 1550632.3 | 23557.5 | -98.5% | -98.5% | -98.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 76802.3 | 12209.9 | -84.1% | -84.1% | -84.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 8097.1 | 12209.9 | +50.8% | +50.8% | +50.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 608278.8 | 90811.2 | -85.1% | -85.1% | -85.1% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 57868.1 | 90811.2 | +56.9% | +56.9% | +56.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 116525.3 | 12873.4 | -89.0% | -89.0% | -89.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 29745.5 | 12873.4 | -56.7% | -56.7% | -56.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 925731.7 | 96768.0 | -89.5% | -89.5% | -89.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 231055.0 | 96768.0 | -58.1% | -58.1% | -58.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 210240.7 | 13650.0 | -93.5% | -93.5% | -93.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 59386.5 | 13650.0 | -77.0% | -77.0% | -77.0% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 1675546.2 | 102491.0 | -93.9% | -93.9% | -93.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 468167.0 | 102491.0 | -78.1% | -78.1% | -78.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 381689.3 | 13891.6 | -96.4% | -96.4% | -96.4% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 128231.0 | 13891.6 | -89.2% | -89.2% | -89.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 3047446.0 | 104568.1 | -96.6% | -96.6% | -96.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 1018937.5 | 104568.1 | -89.7% | -89.7% | -89.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 461944.6 | 13994.0 | -97.0% | -97.0% | -97.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 224883.1 | 13994.0 | -93.8% | -93.8% | -93.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 3689071.0 | 105019.0 | -97.2% | -97.2% | -97.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 1792154.5 | 105019.0 | -94.1% | -94.1% | -94.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 503416.1 | 14038.0 | -97.2% | -97.2% | -97.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 433047.8 | 14038.0 | -96.8% | -96.8% | -96.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 4021090.9 | 105219.2 | -97.4% | -97.4% | -97.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 3457474.3 | 105219.2 | -97.0% | -97.0% | -97.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 517259.2 | 14055.4 | -97.3% | -97.3% | -97.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 841389.3 | 14055.4 | -98.3% | -98.3% | -98.3% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 4131404.9 | 105669.9 | -97.4% | -97.4% | -97.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 6724203.3 | 105669.9 | -98.4% | -98.4% | -98.4% |

### Control tasks

#### Dictionary preparation included

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | str_contains() loop | 4796.1 | 124593.7 | +2497.8% | +2497.7% | +2497.8% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | preg_match() | 19382.5 | 124593.7 | +542.8% | +542.8% | +542.8% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | strtr() | 1529535.4 | 2107808.2 | +37.8% | +37.8% | +37.8% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace_callback() | 178692.3 | 2107808.2 | +1079.6% | +1079.6% | +1079.6% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | str_replace() | 1020018.1 | 2107808.2 | +106.6% | +106.6% | +106.6% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace() | 174254.0 | 2107808.2 | +1109.6% | +1109.6% | +1109.6% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | str_contains() loop | 4711.3 | 133735.6 | +2738.6% | +2738.6% | +2738.6% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | preg_match() | 18014.5 | 133735.6 | +642.4% | +642.4% | +642.4% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | strtr() | 1285527.9 | 2229942.6 | +73.5% | +73.5% | +73.5% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace_callback() | 175249.4 | 2229942.6 | +1172.4% | +1172.4% | +1172.4% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | str_replace() | 954193.4 | 2229942.6 | +133.7% | +133.7% | +133.7% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace() | 170832.6 | 2229942.6 | +1205.3% | +1205.3% | +1205.3% |

#### Dictionary already prepared

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | str_contains() loop | 4796.1 | 2431.6 | -49.3% | -49.3% | -49.3% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | preg_match() | 4227.5 | 2431.6 | -42.5% | -42.5% | -42.5% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | strtr() | 1529534.8 | 1585324.3 | +3.6% | +3.6% | +3.6% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace_callback() | 78202.5 | 1585324.3 | +1927.2% | +1927.2% | +1927.3% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | str_replace() | 947127.0 | 1585324.3 | +67.4% | +67.4% | +67.4% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace() | 74417.0 | 1585324.3 | +2030.3% | +2030.3% | +2030.3% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | str_contains() loop | 4711.3 | 2448.6 | -48.0% | -48.0% | -48.0% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | preg_match() | 4233.5 | 2448.6 | -42.2% | -42.2% | -42.2% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | strtr() | 1285527.5 | 1665801.3 | +29.6% | +29.6% | +29.6% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace_callback() | 78118.3 | 1665801.3 | +2032.4% | +2032.4% | +2032.5% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | str_replace() | 879659.6 | 1665801.3 | +89.4% | +89.4% | +89.4% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace() | 74338.5 | 1665801.3 | +2140.8% | +2140.8% | +2140.8% |
