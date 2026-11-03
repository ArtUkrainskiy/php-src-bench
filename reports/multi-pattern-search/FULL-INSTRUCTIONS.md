# Complete instruction comparisons

Unit: instructions per complete job. Lower is better. Δ is the median of paired per-pass changes; min/max are paired changes, not confidence intervals.

All measured alternatives are listed. Preparation and reuse are separate sections. Natural API result representations are retained; see [method](METHOD.md).

## Everyday cases

### Product tasks

#### Dictionary preparation included

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4796.1 | 110627.3 | +2206.6% | +2206.6% | +2206.6% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 19382.5 | 110627.3 | +470.8% | +470.8% | +470.8% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 3696.1 | 109651.4 | +2866.7% | +2866.7% | +2866.7% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 17306.6 | 109651.4 | +533.6% | +533.6% | +533.6% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4135.9 | 111521.6 | +2596.4% | +2596.4% | +2596.5% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 20736.5 | 111521.6 | +437.8% | +437.8% | +437.8% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 3802.0 | 111818.7 | +2841.0% | +2841.0% | +2841.1% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 21029.0 | 111818.7 | +431.7% | +431.7% | +431.7% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 13323.3 | 123052.1 | +823.6% | +823.6% | +823.6% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 41348.3 | 123052.1 | +197.6% | +197.6% | +197.6% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 7387.3 | 114842.2 | +1454.6% | +1454.6% | +1454.6% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 26913.0 | 114842.2 | +326.7% | +326.7% | +326.7% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 12995.8 | 195622.8 | +1405.3% | +1405.3% | +1405.3% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 26481.4 | 195622.8 | +638.7% | +638.7% | +638.7% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 13657.0 | 193842.4 | +1319.4% | +1319.4% | +1319.4% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 19028.2 | 193842.4 | +918.7% | +918.7% | +918.7% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 19324.4 | 197070.6 | +919.8% | +919.8% | +919.8% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 30665.6 | 197070.6 | +542.6% | +542.6% | +542.6% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 13525.9 | 197211.7 | +1358.0% | +1358.0% | +1358.0% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 30830.1 | 197211.7 | +539.7% | +539.7% | +539.7% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 32981.0 | 216295.1 | +555.8% | +555.8% | +555.8% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 99148.6 | 216295.1 | +118.2% | +118.2% | +118.2% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 18926.0 | 202471.4 | +969.8% | +969.8% | +969.8% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 49497.7 | 202471.4 | +309.1% | +309.1% | +309.1% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 5056.0 | 201579.3 | +3886.9% | +3886.9% | +3886.9% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 19058.3 | 201579.3 | +957.7% | +957.7% | +957.7% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 3912.4 | 200901.5 | +5035.0% | +5035.0% | +5035.0% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 16846.8 | 200901.5 | +1092.5% | +1092.5% | +1092.5% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4707.6 | 202416.9 | +4199.8% | +4199.7% | +4199.8% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 20258.5 | 202416.9 | +899.2% | +899.2% | +899.2% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4164.9 | 202407.6 | +4759.9% | +4759.9% | +4759.9% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 20447.5 | 202407.6 | +889.9% | +889.9% | +889.9% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 16476.0 | 211944.2 | +1186.4% | +1186.4% | +1186.4% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 42861.7 | 211944.2 | +394.5% | +394.5% | +394.5% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 9832.3 | 205470.6 | +1989.7% | +1989.7% | +1989.8% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 27222.7 | 205470.6 | +654.8% | +654.8% | +654.8% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 30278.4 | 131783.1 | +335.2% | +335.2% | +335.2% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 68761.7 | 131783.1 | +91.7% | +91.7% | +91.7% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 15714.2 | 96138.6 | +511.8% | +511.8% | +511.8% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 13870.4 | 96138.6 | +593.1% | +593.1% | +593.1% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 17331.3 | 114927.1 | +563.1% | +563.1% | +563.1% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 42520.3 | 114927.1 | +170.3% | +170.3% | +170.3% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 18676.5 | 131333.1 | +603.2% | +603.2% | +603.2% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 67658.5 | 131333.1 | +94.1% | +94.1% | +94.1% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | strtr() | 19756.1 | 77277.5 | +291.2% | +291.2% | +291.2% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | preg_replace_callback() | 57457.2 | 77277.5 | +34.5% | +34.5% | +34.5% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | str_replace() | 45005.5 | 77277.5 | +71.7% | +71.7% | +71.7% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | strtr() | 28370.1 | 87781.0 | +209.4% | +209.4% | +209.4% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | preg_replace_callback() | 74145.8 | 87781.0 | +18.4% | +18.4% | +18.4% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | str_replace() | 56082.2 | 87781.0 | +56.5% | +56.5% | +56.5% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 5724.9 | 33329.9 | +482.2% | +482.2% | +482.2% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 26086.6 | 33329.9 | +27.8% | +27.8% | +27.8% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 18493.9 | 33329.9 | +80.2% | +80.2% | +80.2% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 39520.0 | 78209.1 | +97.9% | +97.9% | +97.9% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 66873.9 | 78209.1 | +16.9% | +16.9% | +17.0% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 42862.0 | 78209.1 | +82.5% | +82.5% | +82.5% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 3389.0 | 24489.0 | +622.6% | +622.6% | +622.6% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 15773.0 | 24489.0 | +55.3% | +55.3% | +55.3% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 14864.0 | 24489.0 | +64.8% | +64.8% | +64.8% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 4972.0 | 26441.4 | +431.8% | +431.8% | +431.8% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 21679.4 | 26441.4 | +22.0% | +22.0% | +22.0% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 16615.9 | 26441.4 | +59.1% | +59.1% | +59.1% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | strtr() | 3208.3 | 11979.7 | +273.4% | +273.4% | +273.4% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace_callback() | 14728.5 | 11979.7 | -18.7% | -18.7% | -18.7% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | str_replace() | 11273.3 | 11979.7 | +6.3% | +6.3% | +6.3% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace() | 11936.8 | 11979.7 | +0.4% | +0.4% | +0.4% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 6031.0 | 138940.4 | +2203.8% | +2203.8% | +2203.8% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 33751.0 | 138940.4 | +311.7% | +311.7% | +311.7% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 21875.5 | 138940.4 | +535.1% | +535.1% | +535.1% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 7467.5 | 141343.1 | +1792.8% | +1792.8% | +1792.8% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 36514.2 | 141343.1 | +287.1% | +287.1% | +287.1% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 23266.8 | 141343.1 | +507.5% | +507.5% | +507.5% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 53503.0 | 179074.0 | +234.7% | +234.7% | +234.7% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 66594.1 | 179074.0 | +168.9% | +168.9% | +168.9% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 52946.0 | 179074.0 | +238.2% | +238.2% | +238.2% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 127752.9 | 329131.2 | +157.6% | +157.6% | +157.6% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 108596.0 | 329131.2 | +203.1% | +203.1% | +203.1% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 155798.0 | 329131.2 | +111.3% | +111.3% | +111.3% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 107800.0 | 329131.2 | +205.3% | +205.3% | +205.3% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 129996.0 | 354467.4 | +172.7% | +172.7% | +172.7% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 111502.4 | 354467.4 | +217.9% | +217.9% | +217.9% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 162156.9 | 354467.4 | +118.6% | +118.6% | +118.6% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 109462.3 | 354467.4 | +223.8% | +223.8% | +223.8% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 195156.7 | 442091.6 | +126.5% | +126.5% | +126.5% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 118382.0 | 442091.6 | +273.4% | +273.4% | +273.4% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 213697.6 | 442091.6 | +106.9% | +106.9% | +106.9% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 113943.5 | 442091.6 | +288.0% | +288.0% | +288.0% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 1529534.5 | 2004723.1 | +31.1% | +31.1% | +31.1% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 178692.5 | 2004723.1 | +1021.9% | +1021.9% | +1021.9% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 1020018.9 | 2004723.1 | +96.5% | +96.5% | +96.5% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 174254.0 | 2004723.1 | +1050.5% | +1050.5% | +1050.5% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 3050.8 | 24393.2 | +699.6% | +699.6% | +699.6% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 30970.3 | 24393.2 | -21.2% | -21.2% | -21.2% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 27907.0 | 24393.2 | -12.6% | -12.6% | -12.6% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 3737.8 | 25083.9 | +571.1% | +571.1% | +571.1% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 32790.7 | 25083.9 | -23.5% | -23.5% | -23.5% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 28415.0 | 25083.9 | -11.7% | -11.7% | -11.7% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 141235.8 | 491756.2 | +248.2% | +248.2% | +248.2% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | preg_match() per term | 301436.6 | 491756.2 | +63.1% | +63.1% | +63.1% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 109406.4 | 485472.4 | +343.7% | +343.7% | +343.7% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 333378.4 | 485472.4 | +45.6% | +45.6% | +45.6% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 173264.3 | 497703.3 | +187.3% | +187.3% | +187.3% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 523880.3 | 497703.3 | -5.0% | -5.0% | -5.0% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 387607.0 | 492100.9 | +27.0% | +27.0% | +27.0% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 598129.4 | 492100.9 | -17.7% | -17.7% | -17.7% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 3094328.3 | 604651.2 | -80.5% | -80.5% | -80.5% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 1858950.7 | 604651.2 | -67.5% | -67.5% | -67.5% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4711.2 | 112338.1 | +2284.5% | +2284.4% | +2284.5% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 18014.5 | 112338.1 | +523.6% | +523.6% | +523.6% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 3647.0 | 111236.2 | +2950.1% | +2950.0% | +2950.1% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 15940.6 | 111236.2 | +597.8% | +597.8% | +597.8% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4072.0 | 113414.3 | +2685.2% | +2685.2% | +2685.2% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 19370.5 | 113414.3 | +485.5% | +485.5% | +485.5% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 3757.9 | 113759.4 | +2927.2% | +2927.2% | +2927.2% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 19663.0 | 113759.4 | +478.5% | +478.5% | +478.5% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 13129.3 | 126792.1 | +865.7% | +865.7% | +865.7% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 39980.3 | 126792.1 | +217.1% | +217.1% | +217.1% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 7281.0 | 117278.9 | +1510.8% | +1510.7% | +1510.8% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 25547.0 | 117278.9 | +359.1% | +359.1% | +359.1% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 12748.9 | 198275.8 | +1455.2% | +1455.2% | +1455.2% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 25250.4 | 198275.8 | +685.2% | +685.2% | +685.2% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 13422.5 | 196271.6 | +1362.3% | +1362.3% | +1362.3% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 17799.2 | 196271.6 | +1002.7% | +1002.7% | +1002.7% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 18942.5 | 200043.9 | +956.1% | +956.1% | +956.1% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 29436.6 | 200043.9 | +579.6% | +579.6% | +579.6% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 13284.8 | 200195.9 | +1407.0% | +1406.9% | +1407.0% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 29601.1 | 200195.9 | +576.3% | +576.3% | +576.3% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 29582.7 | 222387.0 | +651.7% | +651.7% | +651.8% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 97917.7 | 222387.0 | +127.1% | +127.1% | +127.1% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 17307.0 | 206332.1 | +1092.2% | +1092.2% | +1092.2% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 48268.7 | 206332.1 | +327.5% | +327.5% | +327.5% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4961.6 | 208935.8 | +4111.0% | +4111.0% | +4111.0% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 18005.2 | 208935.8 | +1060.4% | +1060.4% | +1060.4% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 3851.8 | 208205.8 | +5305.5% | +5305.5% | +5305.5% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 15795.8 | 208205.8 | +1218.1% | +1218.1% | +1218.1% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4629.3 | 209941.7 | +4435.1% | +4435.1% | +4435.1% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 19207.5 | 209941.7 | +993.0% | +993.0% | +993.0% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4094.1 | 209929.7 | +5027.6% | +5027.5% | +5027.6% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 19396.5 | 209929.7 | +982.3% | +982.3% | +982.3% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 16126.0 | 220768.1 | +1269.0% | +1269.0% | +1269.0% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 41808.7 | 220768.1 | +428.0% | +428.0% | +428.0% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 9628.3 | 213441.1 | +2116.8% | +2116.8% | +2116.8% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 26171.7 | 213441.1 | +715.5% | +715.5% | +715.5% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 27342.0 | 138137.4 | +405.2% | +405.2% | +405.2% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 68126.8 | 138137.4 | +102.8% | +102.8% | +102.8% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 14214.8 | 98318.4 | +591.7% | +591.7% | +591.7% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 13237.4 | 98318.4 | +642.7% | +642.7% | +642.7% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 15724.3 | 119329.0 | +658.9% | +658.9% | +658.9% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 41887.4 | 119329.0 | +184.9% | +184.9% | +184.9% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 16981.0 | 137672.0 | +710.7% | +710.7% | +710.7% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 67025.5 | 137672.0 | +105.4% | +105.4% | +105.4% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | strtr() | 17229.1 | 80347.6 | +366.3% | +366.3% | +366.3% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | preg_replace_callback() | 55924.2 | 80347.6 | +43.7% | +43.7% | +43.7% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | str_replace() | 44910.7 | 80347.6 | +78.9% | +78.9% | +78.9% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | strtr() | 25248.1 | 91579.0 | +262.7% | +262.7% | +262.7% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | preg_replace_callback() | 72314.7 | 91579.0 | +26.6% | +26.6% | +26.6% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | str_replace() | 55630.6 | 91579.0 | +64.6% | +64.6% | +64.6% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 5105.2 | 34599.1 | +577.7% | +577.7% | +577.7% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 25365.9 | 34599.1 | +36.4% | +36.4% | +36.4% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 18617.6 | 34599.1 | +85.8% | +85.8% | +85.8% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 34569.0 | 82790.0 | +139.5% | +139.5% | +139.5% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 65526.0 | 82790.0 | +26.3% | +26.3% | +26.3% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 42522.0 | 82790.0 | +94.7% | +94.7% | +94.7% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 2992.0 | 26615.0 | +789.5% | +789.5% | +789.5% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 16001.0 | 26615.0 | +66.3% | +66.3% | +66.3% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 14989.0 | 26615.0 | +77.6% | +77.6% | +77.6% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 4397.0 | 28570.0 | +549.8% | +549.8% | +549.8% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 21781.9 | 28570.0 | +31.2% | +31.2% | +31.2% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 16643.9 | 28570.0 | +71.7% | +71.7% | +71.7% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | strtr() | 2978.3 | 12725.3 | +327.3% | +327.3% | +327.3% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace_callback() | 14715.2 | 12725.3 | -13.5% | -13.5% | -13.5% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | str_replace() | 11246.7 | 12725.3 | +13.1% | +13.1% | +13.1% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace() | 11943.7 | 12725.3 | +6.5% | +6.5% | +6.5% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 5846.5 | 140145.5 | +2297.1% | +2297.1% | +2297.1% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 31419.0 | 140145.5 | +346.1% | +346.1% | +346.1% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 22126.0 | 140145.5 | +533.4% | +533.4% | +533.4% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 7187.3 | 142686.9 | +1885.3% | +1885.3% | +1885.3% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 34114.9 | 142686.9 | +318.3% | +318.3% | +318.3% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 23453.1 | 142686.9 | +508.4% | +508.4% | +508.4% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 51261.0 | 183989.0 | +258.9% | +258.9% | +258.9% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 63905.0 | 183989.0 | +187.9% | +187.9% | +187.9% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 52455.0 | 183989.0 | +250.8% | +250.8% | +250.8% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 107590.0 | 348299.6 | +223.7% | +223.7% | +223.7% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 105257.0 | 348299.6 | +230.9% | +230.9% | +230.9% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 147599.1 | 348299.6 | +136.0% | +136.0% | +136.0% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 104421.1 | 348299.6 | +233.6% | +233.6% | +233.6% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 109704.2 | 370770.6 | +238.0% | +238.0% | +238.0% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 108122.8 | 370770.6 | +242.9% | +242.9% | +242.9% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 153055.2 | 370770.6 | +142.2% | +142.2% | +142.2% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 106066.3 | 370770.6 | +249.6% | +249.6% | +249.6% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 164580.4 | 464270.7 | +182.1% | +182.1% | +182.1% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 114937.6 | 464270.7 | +303.9% | +303.9% | +303.9% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 200274.3 | 464270.7 | +131.8% | +131.8% | +131.8% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 110520.8 | 464270.7 | +320.1% | +320.1% | +320.1% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 1285528.0 | 2171949.6 | +69.0% | +69.0% | +69.0% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 175249.2 | 2171949.6 | +1139.3% | +1139.3% | +1139.4% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 954193.2 | 2171949.6 | +127.6% | +127.6% | +127.6% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 170832.6 | 2171949.6 | +1171.4% | +1171.4% | +1171.4% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 2779.8 | 26365.3 | +848.5% | +848.5% | +848.5% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 31250.3 | 26365.3 | -15.6% | -15.6% | -15.6% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 28357.0 | 26365.3 | -7.0% | -7.0% | -7.0% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 3431.8 | 27043.7 | +688.0% | +688.0% | +688.0% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 33019.5 | 27043.7 | -18.1% | -18.1% | -18.1% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 28834.4 | 27043.7 | -6.2% | -6.2% | -6.2% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 141957.8 | 501980.0 | +253.6% | +253.6% | +253.6% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | preg_match() per term | 300389.5 | 501980.0 | +67.1% | +67.1% | +67.1% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 105319.3 | 494721.2 | +369.7% | +369.7% | +369.7% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 331142.1 | 494721.2 | +49.4% | +49.4% | +49.4% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 171824.1 | 510187.3 | +196.9% | +196.9% | +196.9% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 519099.1 | 510187.3 | -1.7% | -1.7% | -1.7% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 397024.3 | 518023.3 | +30.5% | +30.5% | +30.5% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 602056.3 | 518023.3 | -14.0% | -14.0% | -14.0% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 3169658.2 | 638860.6 | -79.8% | -79.8% | -79.8% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 1859844.1 | 638860.6 | -65.6% | -65.6% | -65.6% |

#### Dictionary already prepared

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4796.1 | 2799.2 | -41.6% | -41.6% | -41.6% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 4227.5 | 2799.2 | -33.8% | -33.8% | -33.8% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 3696.1 | 1823.4 | -50.7% | -50.7% | -50.7% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2151.6 | 1823.4 | -15.3% | -15.3% | -15.3% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4135.9 | 3693.6 | -10.7% | -10.7% | -10.7% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5581.5 | 3693.6 | -33.8% | -33.8% | -33.8% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 3802.0 | 3990.6 | +5.0% | +5.0% | +5.0% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5874.0 | 3990.6 | -32.1% | -32.1% | -32.1% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 13323.3 | 15224.0 | +14.3% | +14.3% | +14.3% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 26193.4 | 15224.0 | -41.9% | -41.9% | -41.9% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 7387.3 | 7014.0 | -5.1% | -5.1% | -5.1% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 11758.0 | 7014.0 | -40.3% | -40.3% | -40.3% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 12995.8 | 3847.6 | -70.4% | -70.4% | -70.4% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 9717.4 | 3847.6 | -60.4% | -60.4% | -60.4% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 13657.0 | 2067.5 | -84.9% | -84.9% | -84.9% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2264.3 | 2067.5 | -8.7% | -8.7% | -8.7% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 19324.4 | 5355.6 | -72.3% | -72.3% | -72.3% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 13901.6 | 5355.6 | -61.5% | -61.5% | -61.5% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 13525.9 | 5436.6 | -59.8% | -59.8% | -59.8% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 14066.1 | 5436.6 | -61.3% | -61.3% | -61.3% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 32981.0 | 24520.0 | -25.7% | -25.7% | -25.7% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 82384.7 | 24520.0 | -70.2% | -70.2% | -70.2% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 18926.0 | 10696.3 | -43.5% | -43.5% | -43.5% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 32733.7 | 10696.3 | -67.3% | -67.3% | -67.3% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 5056.0 | 2507.4 | -50.4% | -50.4% | -50.4% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 4369.2 | 2507.4 | -42.6% | -42.6% | -42.6% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 3912.4 | 1829.4 | -53.2% | -53.2% | -53.2% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2157.7 | 1829.4 | -15.2% | -15.2% | -15.2% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4707.6 | 3344.8 | -29.0% | -29.0% | -29.0% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5569.5 | 3344.8 | -39.9% | -39.9% | -39.9% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4164.9 | 3335.7 | -19.9% | -19.9% | -19.9% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5758.5 | 3335.7 | -42.1% | -42.1% | -42.1% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 16476.0 | 12872.3 | -21.9% | -21.9% | -21.9% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 28172.7 | 12872.3 | -54.3% | -54.3% | -54.3% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 9832.4 | 6398.3 | -34.9% | -34.9% | -34.9% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 12533.7 | 6398.3 | -49.0% | -49.0% | -49.0% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 30278.4 | 38973.1 | +28.7% | +28.7% | +28.7% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 59116.7 | 38973.1 | -34.1% | -34.1% | -34.1% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 15714.3 | 3328.5 | -78.8% | -78.8% | -78.8% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 4225.4 | 3328.5 | -21.2% | -21.2% | -21.2% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 17331.2 | 22117.1 | +27.6% | +27.6% | +27.6% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 32875.3 | 22117.1 | -32.7% | -32.7% | -32.7% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 18676.5 | 38523.0 | +106.3% | +106.3% | +106.3% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 58013.5 | 38523.0 | -33.6% | -33.6% | -33.6% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 5724.9 | 7359.9 | +28.6% | +28.6% | +28.6% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 6819.5 | 7359.9 | +7.9% | +7.9% | +7.9% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 4471.9 | 7359.9 | +64.6% | +64.6% | +64.6% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 39520.0 | 52239.0 | +32.2% | +32.2% | +32.2% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 47607.0 | 52239.0 | +9.7% | +9.7% | +9.7% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 28818.0 | 52239.0 | +81.3% | +81.3% | +81.3% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 3389.0 | 3118.0 | -8.0% | -8.0% | -8.0% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 2256.0 | 3118.0 | +38.2% | +38.2% | +38.2% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 3132.0 | 3118.0 | -0.4% | -0.4% | -0.4% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 4972.0 | 5070.4 | +2.0% | +2.0% | +2.0% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 8115.4 | 5070.4 | -37.5% | -37.5% | -37.5% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 4883.9 | 5070.4 | +3.8% | +3.8% | +3.8% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | strtr() | 3208.3 | 2957.8 | -7.8% | -7.8% | -7.8% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace_callback() | 5117.5 | 2957.8 | -42.2% | -42.2% | -42.2% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | str_replace() | 3041.8 | 2957.8 | -2.8% | -2.8% | -2.8% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace() | 2974.8 | 2957.8 | -0.6% | -0.6% | -0.6% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 6031.0 | 3888.5 | -35.5% | -35.5% | -35.5% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 2574.0 | 3888.5 | +51.1% | +51.1% | +51.1% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 3839.5 | 3888.5 | +1.3% | +1.3% | +1.3% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 7467.5 | 6327.0 | -15.3% | -15.3% | -15.3% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 5288.3 | 6327.0 | +19.6% | +19.6% | +19.6% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 5230.8 | 6327.0 | +21.0% | +21.0% | +21.0% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 53503.0 | 44022.1 | -17.7% | -17.7% | -17.7% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 35371.0 | 44022.1 | +24.5% | +24.5% | +24.5% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 34889.0 | 44022.1 | +26.2% | +26.2% | +26.2% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 127752.8 | 121257.3 | -5.1% | -5.1% | -5.1% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 8153.0 | 121257.3 | +1387.3% | +1387.3% | +1387.3% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 82907.0 | 121257.3 | +46.3% | +46.3% | +46.3% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 7963.0 | 121257.3 | +1422.8% | +1422.8% | +1422.8% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 129996.0 | 146593.3 | +12.8% | +12.8% | +12.8% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 11036.5 | 146593.3 | +1228.3% | +1228.3% | +1228.3% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 89265.8 | 146593.3 | +64.2% | +64.2% | +64.2% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 9625.3 | 146593.3 | +1423.0% | +1423.0% | +1423.0% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 195156.7 | 234217.7 | +20.0% | +20.0% | +20.0% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 17892.0 | 234217.7 | +1209.1% | +1209.1% | +1209.1% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 140806.6 | 234217.7 | +66.3% | +66.3% | +66.3% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 14130.5 | 234217.7 | +1557.5% | +1557.5% | +1557.5% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 1529534.8 | 1796814.8 | +17.5% | +17.5% | +17.5% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 78202.5 | 1796814.8 | +2197.6% | +2197.6% | +2197.6% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 947125.5 | 1796814.8 | +89.7% | +89.7% | +89.7% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 74417.0 | 1796814.8 | +2314.5% | +2314.5% | +2314.5% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 3050.8 | 2614.3 | -14.3% | -14.3% | -14.3% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 2640.3 | 2614.3 | -1.0% | -1.0% | -1.0% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 3832.0 | 2614.3 | -31.8% | -31.8% | -31.8% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 3737.8 | 3304.9 | -11.6% | -11.6% | -11.6% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 4413.6 | 3304.9 | -25.1% | -25.1% | -25.1% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 4340.0 | 3304.9 | -23.9% | -23.9% | -23.9% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 141236.2 | 16853.9 | -88.1% | -88.1% | -88.1% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | preg_match() per term | 200999.1 | 16853.9 | -91.6% | -91.6% | -91.6% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 109406.4 | 10149.6 | -90.7% | -90.7% | -90.7% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 227667.7 | 10149.6 | -95.5% | -95.5% | -95.5% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 173264.4 | 22185.4 | -87.2% | -87.2% | -87.2% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 381688.2 | 22185.4 | -94.2% | -94.2% | -94.2% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 387606.4 | 17126.8 | -95.6% | -95.6% | -95.6% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 181108.7 | 17126.8 | -90.5% | -90.5% | -90.5% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 3094325.6 | 130612.0 | -95.8% | -95.8% | -95.8% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 1441918.5 | 130612.0 | -90.9% | -90.9% | -90.9% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4711.3 | 3033.0 | -35.6% | -35.6% | -35.6% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 4233.5 | 3033.0 | -28.4% | -28.4% | -28.4% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 3647.0 | 1931.4 | -47.0% | -47.0% | -47.0% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2159.6 | 1931.4 | -10.6% | -10.6% | -10.6% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4072.0 | 4109.4 | +0.9% | +0.9% | +0.9% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5589.5 | 4109.4 | -26.5% | -26.5% | -26.5% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 3758.0 | 4454.4 | +18.5% | +18.5% | +18.5% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5882.0 | 4454.4 | -24.3% | -24.3% | -24.3% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 13129.3 | 17487.0 | +33.2% | +33.2% | +33.2% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 26199.4 | 17487.0 | -33.3% | -33.3% | -33.3% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 7281.0 | 7974.0 | +9.5% | +9.5% | +9.5% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 11766.0 | 7974.0 | -32.2% | -32.2% | -32.2% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 12748.9 | 4256.9 | -66.6% | -66.6% | -66.6% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 9723.4 | 4256.9 | -56.2% | -56.2% | -56.2% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 13422.5 | 2252.5 | -83.2% | -83.2% | -83.2% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2272.3 | 2252.5 | -0.9% | -0.9% | -0.9% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 18942.5 | 6083.9 | -67.9% | -67.9% | -67.9% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 13909.6 | 6083.9 | -56.3% | -56.3% | -56.3% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 13284.8 | 6176.9 | -53.5% | -53.5% | -53.5% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 14074.1 | 6176.9 | -56.1% | -56.1% | -56.1% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 29582.7 | 28368.0 | -4.1% | -4.1% | -4.1% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 82390.6 | 28368.0 | -65.6% | -65.6% | -65.6% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 17307.0 | 12313.0 | -28.9% | -28.9% | -28.9% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 32741.7 | 12313.0 | -62.4% | -62.4% | -62.4% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4961.6 | 2671.9 | -46.1% | -46.1% | -46.1% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 4375.2 | 2671.9 | -38.9% | -38.9% | -38.9% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 3851.7 | 1941.8 | -49.6% | -49.6% | -49.6% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2165.7 | 1941.8 | -10.3% | -10.3% | -10.3% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4629.3 | 3677.6 | -20.6% | -20.6% | -20.6% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5577.5 | 3677.6 | -34.1% | -34.1% | -34.1% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4094.1 | 3665.6 | -10.5% | -10.5% | -10.5% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5766.5 | 3665.6 | -36.4% | -36.4% | -36.4% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 16126.0 | 14504.0 | -10.1% | -10.1% | -10.1% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 28178.7 | 14504.0 | -48.5% | -48.5% | -48.5% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 9628.3 | 7177.0 | -25.5% | -25.5% | -25.5% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 12541.7 | 7177.0 | -42.8% | -42.8% | -42.8% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 27342.0 | 43417.5 | +58.8% | +58.8% | +58.8% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 59122.7 | 43417.5 | -26.6% | -26.6% | -26.6% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 14214.8 | 3598.5 | -74.7% | -74.7% | -74.7% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 4233.4 | 3598.5 | -15.0% | -15.0% | -15.0% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 15724.2 | 24609.0 | +56.5% | +56.5% | +56.5% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 32883.4 | 24609.0 | -25.2% | -25.2% | -25.2% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 16981.0 | 42952.1 | +152.9% | +152.9% | +152.9% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 58021.5 | 42952.1 | -26.0% | -26.0% | -26.0% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 5105.2 | 7829.1 | +53.4% | +53.4% | +53.4% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 6723.9 | 7829.1 | +16.4% | +16.4% | +16.4% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 4399.6 | 7829.1 | +77.9% | +77.9% | +78.0% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 34569.0 | 56020.0 | +62.1% | +62.1% | +62.1% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 46884.0 | 56020.0 | +19.5% | +19.5% | +19.5% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 28282.0 | 56020.0 | +98.1% | +98.1% | +98.1% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 2992.0 | 3317.0 | +10.9% | +10.9% | +10.9% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 2268.0 | 3317.0 | +46.3% | +46.3% | +46.3% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 3123.0 | 3317.0 | +6.2% | +6.2% | +6.2% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 4397.0 | 5272.0 | +19.9% | +19.9% | +19.9% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 8009.9 | 5272.0 | -34.2% | -34.2% | -34.2% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 4777.9 | 5272.0 | +10.3% | +10.3% | +10.3% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | strtr() | 2978.3 | 3043.3 | +2.2% | +2.2% | +2.2% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace_callback() | 5063.5 | 3043.3 | -39.9% | -39.9% | -39.9% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | str_replace() | 2970.3 | 3043.3 | +2.5% | +2.5% | +2.5% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace() | 2920.8 | 3043.3 | +4.2% | +4.2% | +4.2% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 5846.5 | 4254.5 | -27.2% | -27.2% | -27.2% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 2586.0 | 4254.5 | +64.5% | +64.5% | +64.5% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 3801.0 | 4254.5 | +11.9% | +11.9% | +11.9% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 7187.2 | 6833.9 | -4.9% | -4.9% | -4.9% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 5240.9 | 6833.9 | +30.4% | +30.4% | +30.4% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 5128.1 | 6833.9 | +33.3% | +33.3% | +33.3% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 51261.0 | 48097.9 | -6.2% | -6.2% | -6.2% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 35034.0 | 48097.9 | +37.3% | +37.3% | +37.3% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 34109.0 | 48097.9 | +41.0% | +41.0% | +41.0% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 107590.1 | 139107.2 | +29.3% | +29.3% | +29.3% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 8165.0 | 139107.2 | +1603.7% | +1603.7% | +1603.7% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 73065.0 | 139107.2 | +90.4% | +90.4% | +90.4% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 7927.0 | 139107.2 | +1654.9% | +1654.9% | +1654.9% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 109704.3 | 161578.5 | +47.3% | +47.3% | +47.3% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 11012.8 | 161578.5 | +1367.2% | +1367.2% | +1367.2% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 78521.6 | 161578.5 | +105.8% | +105.8% | +105.8% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 9572.3 | 161578.5 | +1588.0% | +1588.0% | +1588.0% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 164580.6 | 255079.3 | +55.0% | +55.0% | +55.0% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 17806.5 | 255079.3 | +1332.5% | +1332.5% | +1332.5% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 125740.3 | 255079.3 | +102.9% | +102.9% | +102.9% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 14047.7 | 255079.3 | +1715.8% | +1715.8% | +1715.8% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 1285529.4 | 1962714.6 | +52.7% | +52.7% | +52.7% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 78118.2 | 1962714.6 | +2412.5% | +2412.5% | +2412.5% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 879657.5 | 1962714.6 | +123.1% | +123.1% | +123.1% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 74338.6 | 1962714.6 | +2540.2% | +2540.2% | +2540.2% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 2779.8 | 2754.3 | -0.9% | -0.9% | -0.9% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 2652.3 | 2754.3 | +3.8% | +3.8% | +3.8% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 3839.0 | 2754.3 | -28.3% | -28.3% | -28.3% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 3431.7 | 3432.8 | +0.0% | +0.0% | +0.0% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 4382.5 | 3432.8 | -21.7% | -21.7% | -21.7% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 4316.4 | 3432.8 | -20.5% | -20.5% | -20.5% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 141957.9 | 18498.2 | -87.0% | -87.0% | -87.0% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | preg_match() per term | 206672.6 | 18498.2 | -91.0% | -91.0% | -91.0% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 105319.3 | 10817.1 | -89.7% | -89.7% | -89.7% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 232234.3 | 10817.1 | -95.3% | -95.3% | -95.3% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 171824.2 | 26107.5 | -84.8% | -84.8% | -84.8% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 386494.3 | 26107.5 | -93.2% | -93.2% | -93.2% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 397023.9 | 18311.3 | -95.4% | -95.4% | -95.4% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 180669.3 | 18311.3 | -89.9% | -89.9% | -89.9% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 3169658.4 | 140093.0 | -95.6% | -95.6% | -95.6% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 1438445.1 | 140093.0 | -90.3% | -90.3% | -90.3% |

### Synthetic tasks

#### Dictionary preparation included

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 7138.0 | 1293537.8 | +18021.8% | +18021.8% | +18021.9% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 301823.0 | 1293537.8 | +328.6% | +328.6% | +328.6% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 298454.4 | 1293537.8 | +333.4% | +333.4% | +333.4% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 5841.0 | 176429.0 | +2920.5% | +2920.5% | +2920.5% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 299444.0 | 176429.0 | -41.1% | -41.1% | -41.1% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 296050.0 | 176429.0 | -40.4% | -40.4% | -40.4% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | strtr() | 5017.0 | 18348.0 | +265.7% | +265.7% | +265.7% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace_callback() | 79321.0 | 18348.0 | -76.9% | -76.9% | -76.9% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace() | 66822.0 | 18348.0 | -72.5% | -72.5% | -72.5% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | strtr() | 4232.0 | 16859.0 | +298.4% | +298.4% | +298.4% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | preg_replace_callback() | 19093.0 | 16859.0 | -11.7% | -11.7% | -11.7% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 7032.0 | 1336112.2 | +18900.5% | +18900.4% | +18900.5% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 271268.1 | 1336112.2 | +392.5% | +392.5% | +392.5% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 267908.8 | 1336112.2 | +398.7% | +398.7% | +398.7% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 5680.0 | 182638.1 | +3115.5% | +3115.5% | +3115.5% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 268895.2 | 182638.1 | -32.1% | -32.1% | -32.1% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 265508.0 | 182638.1 | -31.2% | -31.2% | -31.2% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | strtr() | 4917.0 | 19213.0 | +290.7% | +290.7% | +290.7% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace_callback() | 80162.0 | 19213.0 | -76.0% | -76.0% | -76.0% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace() | 67962.0 | 19213.0 | -71.7% | -71.7% | -71.7% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | strtr() | 4071.0 | 18236.0 | +347.9% | +347.9% | +347.9% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | preg_replace_callback() | 18815.0 | 18236.0 | -3.1% | -3.1% | -3.1% |

#### Dictionary already prepared

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 7138.0 | 6648.0 | -6.9% | -6.9% | -6.9% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 11680.0 | 6648.0 | -43.1% | -43.1% | -43.1% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 8964.0 | 6648.0 | -25.8% | -25.8% | -25.8% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 5841.0 | 6663.0 | +14.1% | +14.1% | +14.1% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 9301.0 | 6663.0 | -28.4% | -28.4% | -28.4% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 6535.0 | 6663.0 | +2.0% | +2.0% | +2.0% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | strtr() | 5017.0 | 6442.0 | +28.4% | +28.4% | +28.4% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace_callback() | 17612.0 | 6442.0 | -63.4% | -63.4% | -63.4% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace() | 5766.0 | 6442.0 | +11.7% | +11.7% | +11.7% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | strtr() | 4232.0 | 3148.0 | -25.6% | -25.6% | -25.6% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | preg_replace_callback() | 9212.0 | 3148.0 | -65.8% | -65.8% | -65.8% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 7032.0 | 7096.0 | +0.9% | +0.9% | +0.9% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 11622.0 | 7096.0 | -38.9% | -38.9% | -38.9% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 8900.0 | 7096.0 | -20.3% | -20.3% | -20.3% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 5680.0 | 7109.0 | +25.2% | +25.2% | +25.2% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 9249.0 | 7109.0 | -23.1% | -23.1% | -23.1% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 6471.0 | 7109.0 | +9.9% | +9.9% | +9.9% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | strtr() | 4917.0 | 6883.0 | +40.0% | +40.0% | +40.0% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace_callback() | 17275.0 | 6883.0 | -60.2% | -60.2% | -60.2% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace() | 5712.0 | 6883.0 | +20.5% | +20.5% | +20.5% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | strtr() | 4071.0 | 3271.0 | -19.7% | -19.7% | -19.7% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | preg_replace_callback() | 9069.0 | 3271.0 | -63.9% | -63.9% | -63.9% |

## Size series

### Product tasks

#### Dictionary preparation included

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 3872.6 | 41508.8 | +971.9% | +971.8% | +971.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 10726.2 | 41508.8 | +287.0% | +287.0% | +287.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | str_contains() loop | 2751.6 | 40467.1 | +1370.7% | +1370.7% | +1370.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | preg_match() | 8915.9 | 40467.1 | +353.9% | +353.9% | +353.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | str_contains() loop | 3149.4 | 41913.9 | +1230.9% | +1230.9% | +1230.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | preg_match() | 11530.4 | 41913.9 | +263.5% | +263.5% | +263.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | str_contains() loop | 2880.0 | 42012.9 | +1358.8% | +1358.8% | +1358.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | preg_match() | 11496.4 | 42012.9 | +265.4% | +265.4% | +265.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 11354.7 | 52085.9 | +358.7% | +358.7% | +358.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 30088.7 | 52085.9 | +73.1% | +73.1% | +73.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | str_contains() loop | 5070.0 | 44725.0 | +782.2% | +782.1% | +782.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | preg_match() | 16759.7 | 44725.0 | +166.9% | +166.9% | +166.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 6239.6 | 89510.4 | +1334.5% | +1334.5% | +1334.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 19359.6 | 89510.4 | +362.4% | +362.4% | +362.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | str_contains() loop | 3895.9 | 88400.7 | +2169.1% | +2169.1% | +2169.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | preg_match() | 15774.9 | 88400.7 | +460.4% | +460.4% | +460.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | str_contains() loop | 4523.8 | 89935.3 | +1888.1% | +1888.0% | +1888.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | preg_match() | 20898.9 | 89935.3 | +330.3% | +330.3% | +330.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | str_contains() loop | 4063.9 | 90061.2 | +2116.1% | +2116.1% | +2116.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | preg_match() | 21262.9 | 90061.2 | +323.6% | +323.6% | +323.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 19277.7 | 100702.0 | +422.4% | +422.4% | +422.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 56005.3 | 100702.0 | +79.8% | +79.8% | +79.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | str_contains() loop | 7425.3 | 92906.1 | +1151.2% | +1151.2% | +1151.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | preg_match() | 30641.0 | 92906.1 | +203.2% | +203.2% | +203.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 11374.8 | 217030.8 | +1808.0% | +1808.0% | +1808.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 39938.3 | 217030.8 | +443.4% | +443.4% | +443.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | str_contains() loop | 6717.6 | 215810.8 | +3112.6% | +3112.6% | +3112.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | preg_match() | 30181.9 | 215810.8 | +615.0% | +615.0% | +615.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | str_contains() loop | 8064.8 | 216539.4 | +2585.0% | +2585.0% | +2585.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | preg_match() | 43674.8 | 216539.4 | +395.8% | +395.8% | +395.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | str_contains() loop | 6888.5 | 217653.7 | +3059.7% | +3059.7% | +3059.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | preg_match() | 44439.8 | 217653.7 | +389.8% | +389.8% | +389.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 40236.7 | 228624.7 | +468.2% | +468.2% | +468.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 135081.8 | 228624.7 | +69.2% | +69.2% | +69.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | str_contains() loop | 15927.4 | 219980.2 | +1281.1% | +1281.1% | +1281.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | preg_match() | 68478.2 | 219980.2 | +221.2% | +221.2% | +221.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 21321.3 | 421575.5 | +1877.3% | +1877.2% | +1877.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 84006.4 | 421575.5 | +401.8% | +401.8% | +401.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | str_contains() loop | 12522.5 | 420350.2 | +3256.8% | +3256.7% | +3256.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | preg_match() | 57018.8 | 420350.2 | +637.2% | +637.2% | +637.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | str_contains() loop | 15410.2 | 422044.2 | +2638.7% | +2638.6% | +2638.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | preg_match() | 93227.0 | 422044.2 | +352.7% | +352.7% | +352.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | str_contains() loop | 12941.3 | 422197.6 | +3162.4% | +3162.4% | +3162.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | preg_match() | 96124.4 | 422197.6 | +339.2% | +339.2% | +339.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 76126.0 | 434064.0 | +470.2% | +470.2% | +470.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 352981.3 | 434064.0 | +23.0% | +23.0% | +23.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | str_contains() loop | 32324.7 | 425399.8 | +1216.0% | +1216.0% | +1216.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | preg_match() | 165712.0 | 425399.8 | +156.7% | +156.7% | +156.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 40724.7 | 785826.4 | +1829.6% | +1829.6% | +1829.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 164403.8 | 785826.4 | +378.0% | +378.0% | +378.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | str_contains() loop | 23556.8 | 784594.0 | +3230.6% | +3230.6% | +3230.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | preg_match() | 110667.7 | 784594.0 | +609.0% | +609.0% | +609.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | str_contains() loop | 29162.2 | 786296.5 | +2596.3% | +2596.2% | +2596.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | preg_match() | 183491.9 | 786296.5 | +328.5% | +328.5% | +328.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | str_contains() loop | 24109.5 | 786449.5 | +3162.0% | +3162.0% | +3162.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | preg_match() | 188009.1 | 786449.5 | +318.3% | +318.3% | +318.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 146084.8 | 802103.4 | +449.1% | +449.1% | +449.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 701991.4 | 802103.4 | +14.3% | +14.3% | +14.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | str_contains() loop | 61610.7 | 793424.9 | +1187.8% | +1187.8% | +1187.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | preg_match() | 328867.3 | 793424.9 | +141.3% | +141.3% | +141.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 80770.6 | 1445258.6 | +1689.3% | +1689.3% | +1689.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 331215.4 | 1445258.6 | +336.4% | +336.3% | +336.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | str_contains() loop | 45764.5 | 1444026.0 | +3055.3% | +3055.3% | +3055.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | preg_match() | 216655.6 | 1444026.0 | +566.5% | +566.5% | +566.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | str_contains() loop | 57169.0 | 1445729.4 | +2428.9% | +2428.8% | +2428.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | preg_match() | 371240.3 | 1445729.4 | +289.4% | +289.4% | +289.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | str_contains() loop | 46922.1 | 1445882.1 | +2981.4% | +2981.4% | +2981.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | preg_match() | 379990.4 | 1445882.1 | +280.5% | +280.5% | +280.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 299086.7 | 1454984.1 | +386.5% | +386.5% | +386.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 1441219.1 | 1454984.1 | +1.0% | +1.0% | +1.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | str_contains() loop | 124819.1 | 1446279.0 | +1058.7% | +1058.7% | +1058.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | preg_match() | 671413.5 | 1446279.0 | +115.4% | +115.4% | +115.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 161151.5 | 2460347.1 | +1426.7% | +1426.6% | +1426.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 657989.1 | 2460347.1 | +273.9% | +273.9% | +273.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | str_contains() loop | 91032.1 | 2459102.7 | +2601.4% | +2601.4% | +2601.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | preg_match() | 425626.1 | 2459102.7 | +477.8% | +477.8% | +477.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | str_contains() loop | 114416.5 | 2460898.5 | +2050.8% | +2050.8% | +2050.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | preg_match() | 737423.3 | 2460898.5 | +233.7% | +233.7% | +233.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | str_contains() loop | 92862.6 | 2460979.6 | +2550.1% | +2550.1% | +2550.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | preg_match() | 754967.0 | 2460979.6 | +226.0% | +226.0% | +226.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 606320.2 | 2465474.0 | +306.6% | +306.6% | +306.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 2921232.3 | 2465474.0 | -15.6% | -15.6% | -15.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | str_contains() loop | 257000.7 | 2456702.2 | +855.9% | +855.9% | +855.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | preg_match() | 1346892.8 | 2456702.2 | +82.4% | +82.4% | +82.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 15059.6 | 50105.6 | +232.7% | +232.7% | +232.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | preg_match() per term | 29911.9 | 50105.6 | +67.5% | +67.5% | +67.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 12020.2 | 48085.1 | +300.0% | +300.0% | +300.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 33344.3 | 48085.1 | +44.2% | +44.2% | +44.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 18909.4 | 50051.8 | +164.7% | +164.7% | +164.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 53961.5 | 50051.8 | -7.2% | -7.2% | -7.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 27153.5 | 83020.1 | +205.7% | +205.7% | +205.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | preg_match() per term | 55511.6 | 83020.1 | +49.6% | +49.6% | +49.6% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 22022.4 | 80325.5 | +264.7% | +264.7% | +264.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 63435.5 | 80325.5 | +26.6% | +26.6% | +26.6% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 34878.2 | 83589.8 | +139.7% | +139.7% | +139.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 102098.9 | 83589.8 | -18.1% | -18.1% | -18.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 50244.7 | 150697.7 | +199.9% | +199.9% | +199.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | preg_match() per term | 106946.3 | 150697.7 | +40.9% | +40.9% | +40.9% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 39437.8 | 146963.1 | +272.6% | +272.6% | +272.6% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 118702.3 | 146963.1 | +23.8% | +23.8% | +23.8% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 65195.2 | 152516.1 | +133.9% | +133.9% | +133.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 192134.6 | 152516.1 | -20.6% | -20.6% | -20.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 95908.7 | 317882.8 | +231.4% | +231.4% | +231.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | preg_match() per term | 201910.5 | 317882.8 | +57.4% | +57.4% | +57.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 76834.0 | 312926.8 | +307.3% | +307.3% | +307.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 229752.1 | 312926.8 | +36.2% | +36.2% | +36.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 120489.7 | 321732.0 | +167.0% | +167.0% | +167.0% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 362031.9 | 321732.0 | -11.1% | -11.1% | -11.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 174359.5 | 670867.5 | +284.8% | +284.8% | +284.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | preg_match() per term | 386905.6 | 670867.5 | +73.4% | +73.4% | +73.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 141758.9 | 663875.5 | +368.3% | +368.3% | +368.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 433971.7 | 663875.5 | +53.0% | +53.0% | +53.0% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 210380.0 | 677766.8 | +222.2% | +222.2% | +222.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 661305.0 | 677766.8 | +2.5% | +2.5% | +2.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 306287.4 | 1311971.6 | +328.3% | +328.3% | +328.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | preg_match() per term | 718322.1 | 1311971.6 | +82.6% | +82.6% | +82.6% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 282283.6 | 1298567.6 | +360.0% | +360.0% | +360.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 860153.5 | 1298567.6 | +51.0% | +51.0% | +51.0% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 351655.4 | 1317824.4 | +274.7% | +274.7% | +274.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 1220530.0 | 1317824.4 | +8.0% | +8.0% | +8.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 562768.0 | 3152789.9 | +460.2% | +460.2% | +460.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | preg_match() per term | 1370392.7 | 3152789.9 | +130.1% | +130.1% | +130.1% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 556549.2 | 3145592.5 | +465.2% | +465.2% | +465.2% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 1690892.7 | 3145592.5 | +86.0% | +86.0% | +86.0% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 626825.5 | 3157765.7 | +403.8% | +403.8% | +403.8% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 2310721.1 | 3157765.7 | +36.7% | +36.7% | +36.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 75958.3 | 58097.4 | -23.5% | -23.5% | -23.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 31007.3 | 58097.4 | +87.4% | +87.4% | +87.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 601540.8 | 149956.1 | -75.1% | -75.1% | -75.1% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 81284.0 | 149956.1 | +84.5% | +84.5% | +84.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 114538.0 | 100032.9 | -12.7% | -12.7% | -12.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 80941.5 | 100032.9 | +23.6% | +23.6% | +23.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 909845.9 | 198890.0 | -78.1% | -78.1% | -78.1% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 283080.3 | 198890.0 | -29.7% | -29.7% | -29.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 204486.0 | 173360.4 | -15.2% | -15.2% | -15.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 170322.6 | 173360.4 | +1.8% | +1.8% | +1.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 1629545.9 | 278507.9 | -82.9% | -82.9% | -82.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 580497.5 | 278507.9 | -52.0% | -52.0% | -52.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 371102.5 | 328427.6 | -11.5% | -11.5% | -11.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 389981.6 | 328427.6 | -15.8% | -15.8% | -15.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 2962765.5 | 437913.1 | -85.2% | -85.2% | -85.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 1282915.3 | 437913.1 | -65.9% | -65.9% | -65.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 451012.6 | 647619.8 | +43.6% | +43.6% | +43.6% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 802861.4 | 647619.8 | -19.3% | -19.3% | -19.3% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 3601597.5 | 761665.0 | -78.9% | -78.9% | -78.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 2373332.3 | 761665.0 | -67.9% | -67.9% | -67.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 491702.3 | 1166111.7 | +137.2% | +137.2% | +137.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 1849223.7 | 1166111.7 | -36.9% | -36.9% | -36.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 3927383.7 | 1281941.1 | -67.4% | -67.4% | -67.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 4876855.0 | 1281941.1 | -73.7% | -73.7% | -73.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 504960.4 | 2532732.9 | +401.6% | +401.6% | +401.6% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 4035981.1 | 2532732.9 | -37.2% | -37.2% | -37.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 4033031.8 | 2652207.8 | -34.2% | -34.2% | -34.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 9921729.3 | 2652207.8 | -73.3% | -73.3% | -73.3% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 3807.5 | 42609.7 | +1019.1% | +1019.0% | +1019.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 10673.2 | 42609.7 | +299.2% | +299.2% | +299.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | str_contains() loop | 2716.3 | 41427.3 | +1425.2% | +1425.1% | +1425.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | preg_match() | 8864.9 | 41427.3 | +367.3% | +367.3% | +367.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | str_contains() loop | 3111.9 | 43070.9 | +1284.1% | +1284.0% | +1284.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | preg_match() | 11479.4 | 43070.9 | +275.2% | +275.2% | +275.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | str_contains() loop | 2843.5 | 43175.9 | +1418.4% | +1418.3% | +1418.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | preg_match() | 11445.4 | 43175.9 | +277.2% | +277.2% | +277.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 11288.4 | 54600.0 | +383.7% | +383.7% | +383.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 30035.6 | 54600.0 | +81.8% | +81.8% | +81.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | str_contains() loop | 5073.0 | 46254.0 | +811.8% | +811.8% | +811.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | preg_match() | 16708.7 | 46254.0 | +176.8% | +176.8% | +176.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 6116.6 | 91891.7 | +1402.3% | +1402.3% | +1402.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 19020.6 | 91891.7 | +383.1% | +383.1% | +383.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | str_contains() loop | 3833.1 | 90617.0 | +2264.1% | +2264.0% | +2264.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | preg_match() | 15437.9 | 90617.0 | +487.0% | +487.0% | +487.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | str_contains() loop | 4457.4 | 92377.7 | +1972.5% | +1972.5% | +1972.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | preg_match() | 20561.9 | 92377.7 | +349.3% | +349.3% | +349.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | str_contains() loop | 4000.5 | 92518.6 | +2212.7% | +2212.7% | +2212.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | preg_match() | 20925.9 | 92518.6 | +342.1% | +342.1% | +342.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 19069.3 | 104712.1 | +449.1% | +449.1% | +449.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 55666.3 | 104712.1 | +88.1% | +88.1% | +88.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | str_contains() loop | 7383.0 | 95786.0 | +1197.4% | +1197.4% | +1197.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | preg_match() | 30304.0 | 95786.0 | +216.1% | +216.1% | +216.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 11135.2 | 221930.7 | +1893.0% | +1893.0% | +1893.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 38877.3 | 221930.7 | +470.8% | +470.8% | +470.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | str_contains() loop | 6586.5 | 220509.0 | +3247.9% | +3247.9% | +3247.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | preg_match() | 29122.9 | 220509.0 | +657.2% | +657.2% | +657.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | str_contains() loop | 7925.5 | 221516.7 | +2695.0% | +2694.8% | +2695.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | preg_match() | 42615.7 | 221516.7 | +419.8% | +419.8% | +419.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | str_contains() loop | 6757.8 | 222653.7 | +3194.8% | +3194.8% | +3194.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | preg_match() | 43380.7 | 222653.7 | +413.3% | +413.3% | +413.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 39726.7 | 235549.0 | +492.9% | +492.9% | +492.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 134021.1 | 235549.0 | +75.8% | +75.8% | +75.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | str_contains() loop | 15769.3 | 225492.9 | +1329.9% | +1329.9% | +1330.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | preg_match() | 67419.3 | 225492.9 | +234.5% | +234.5% | +234.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 20820.4 | 430638.1 | +1968.3% | +1968.3% | +1968.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 81928.4 | 430638.1 | +425.6% | +425.6% | +425.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | str_contains() loop | 12254.9 | 429209.4 | +3402.4% | +3402.3% | +3402.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | preg_match() | 54942.9 | 429209.4 | +681.2% | +681.2% | +681.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | str_contains() loop | 15113.7 | 431182.9 | +2752.9% | +2752.9% | +2752.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | preg_match() | 91151.0 | 431182.9 | +373.0% | +373.0% | +373.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | str_contains() loop | 12676.8 | 431360.2 | +3302.8% | +3302.7% | +3302.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | preg_match() | 94048.5 | 431360.2 | +358.7% | +358.7% | +358.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 74945.4 | 445151.2 | +494.0% | +494.0% | +494.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 350903.4 | 445151.2 | +26.9% | +26.9% | +26.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | str_contains() loop | 31914.7 | 435070.8 | +1263.2% | +1263.2% | +1263.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | preg_match() | 163635.8 | 435070.8 | +165.9% | +165.9% | +165.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 39732.1 | 802141.3 | +1918.9% | +1918.9% | +1918.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 160263.7 | 802141.3 | +400.5% | +400.5% | +400.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | str_contains() loop | 23023.2 | 800704.2 | +3377.8% | +3377.8% | +3377.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | preg_match() | 106529.8 | 800704.2 | +651.6% | +651.6% | +651.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | str_contains() loop | 28575.1 | 802687.9 | +2709.0% | +2709.0% | +2709.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | preg_match() | 179354.2 | 802687.9 | +347.5% | +347.5% | +347.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | str_contains() loop | 23586.1 | 802863.9 | +3304.0% | +3304.0% | +3304.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | preg_match() | 183870.9 | 802863.9 | +336.6% | +336.6% | +336.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 143844.5 | 820422.3 | +470.4% | +470.4% | +470.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 697851.9 | 820422.3 | +17.6% | +17.6% | +17.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | str_contains() loop | 60704.9 | 810320.6 | +1234.9% | +1234.8% | +1234.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | preg_match() | 324729.5 | 810320.6 | +149.5% | +149.5% | +149.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 78773.7 | 1480444.0 | +1779.4% | +1779.3% | +1779.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 323336.3 | 1480444.0 | +357.9% | +357.9% | +357.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | str_contains() loop | 44685.1 | 1479003.7 | +3209.8% | +3209.8% | +3209.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | preg_match() | 208778.7 | 1479003.7 | +608.4% | +608.4% | +608.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | str_contains() loop | 55981.4 | 1480989.4 | +2545.5% | +2545.4% | +2545.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | preg_match() | 363363.2 | 1480989.4 | +307.6% | +307.6% | +307.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | str_contains() loop | 45836.7 | 1481164.1 | +3131.4% | +3131.4% | +3131.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | preg_match() | 372113.7 | 1481164.1 | +298.0% | +298.0% | +298.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 294258.3 | 1492231.3 | +407.1% | +407.1% | +407.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 1433342.7 | 1492231.3 | +4.1% | +4.1% | +4.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | str_contains() loop | 122887.4 | 1482104.8 | +1106.1% | +1106.1% | +1106.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | preg_match() | 663539.9 | 1482104.8 | +123.4% | +123.4% | +123.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 157149.0 | 2509696.2 | +1497.0% | +1496.8% | +1497.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 643273.9 | 2509696.2 | +290.1% | +290.1% | +290.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | str_contains() loop | 88900.2 | 2508238.9 | +2721.4% | +2721.4% | +2721.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | preg_match() | 410913.5 | 2508238.9 | +510.4% | +510.4% | +510.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | str_contains() loop | 112016.8 | 2510317.8 | +2141.0% | +2140.9% | +2141.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | preg_match() | 722710.6 | 2510317.8 | +247.3% | +247.3% | +247.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | str_contains() loop | 90696.5 | 2510420.4 | +2667.9% | +2667.9% | +2668.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | preg_match() | 740254.1 | 2510420.4 | +239.1% | +239.1% | +239.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 596603.1 | 2516885.9 | +321.9% | +321.9% | +321.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 2906510.7 | 2516885.9 | -13.4% | -13.4% | -13.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | str_contains() loop | 253052.5 | 2506654.7 | +890.6% | +890.6% | +890.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | preg_match() | 1332177.2 | 2506654.7 | +88.2% | +88.2% | +88.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 15125.8 | 51809.3 | +242.5% | +242.5% | +242.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | preg_match() per term | 29802.1 | 51809.3 | +73.8% | +73.8% | +73.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 11630.9 | 49002.3 | +321.3% | +321.3% | +321.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 33242.5 | 49002.3 | +47.4% | +47.4% | +47.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 18734.8 | 53854.0 | +187.5% | +187.5% | +187.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 53542.4 | 53854.0 | +0.6% | +0.6% | +0.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 27244.0 | 85285.6 | +213.0% | +213.0% | +213.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | preg_match() per term | 55316.6 | 85285.6 | +54.2% | +54.2% | +54.2% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 21230.3 | 81746.3 | +285.0% | +285.0% | +285.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 63189.0 | 81746.3 | +29.4% | +29.4% | +29.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 34549.1 | 88015.5 | +154.8% | +154.7% | +154.8% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 101328.2 | 88015.5 | -13.1% | -13.1% | -13.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 50564.4 | 154108.2 | +204.8% | +204.8% | +204.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | preg_match() per term | 106649.7 | 154108.2 | +44.5% | +44.5% | +44.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 38034.3 | 149495.2 | +293.1% | +293.1% | +293.1% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 118136.8 | 149495.2 | +26.5% | +26.5% | +26.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 64834.7 | 158130.4 | +143.9% | +143.9% | +143.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 190712.1 | 158130.4 | -17.1% | -17.1% | -17.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 96304.2 | 324791.4 | +237.3% | +237.3% | +237.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | preg_match() per term | 201153.5 | 324791.4 | +61.5% | +61.5% | +61.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 74014.8 | 318897.5 | +330.9% | +330.9% | +330.9% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 228314.6 | 318897.5 | +39.7% | +39.7% | +39.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 119479.4 | 330881.3 | +176.9% | +176.9% | +176.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 358854.4 | 330881.3 | -7.8% | -7.8% | -7.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 174678.6 | 682900.8 | +290.9% | +290.9% | +290.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | preg_match() per term | 384695.6 | 682900.8 | +77.5% | +77.5% | +77.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 136539.0 | 674919.8 | +394.3% | +394.3% | +394.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 430433.8 | 674919.8 | +56.8% | +56.8% | +56.8% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 208045.1 | 692093.6 | +232.7% | +232.7% | +232.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 654043.5 | 692093.6 | +5.8% | +5.8% | +5.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 303860.5 | 1321599.1 | +334.9% | +334.9% | +334.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | preg_match() per term | 710334.4 | 1321599.1 | +86.1% | +86.1% | +86.1% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 272397.7 | 1307200.0 | +379.9% | +379.9% | +379.9% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 850740.3 | 1307200.0 | +53.7% | +53.7% | +53.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 344702.2 | 1329756.1 | +285.8% | +285.8% | +285.8% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 1202106.6 | 1329756.1 | +10.6% | +10.6% | +10.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 555044.2 | 3166757.2 | +470.5% | +470.5% | +470.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | preg_match() per term | 1351743.3 | 3166757.2 | +134.3% | +134.3% | +134.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 537163.1 | 3158567.7 | +488.0% | +488.0% | +488.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 1670636.6 | 3158567.7 | +89.1% | +89.1% | +89.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 610406.7 | 3174035.6 | +420.0% | +420.0% | +420.0% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 2270769.0 | 3174035.6 | +39.8% | +39.8% | +39.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 76802.4 | 62063.1 | -19.2% | -19.2% | -19.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 30969.5 | 62063.1 | +100.4% | +100.4% | +100.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 608278.7 | 164271.2 | -73.0% | -73.0% | -73.0% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 80755.1 | 164271.2 | +103.4% | +103.4% | +103.4% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 116525.4 | 106636.7 | -8.5% | -8.5% | -8.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 81275.8 | 106636.7 | +31.2% | +31.2% | +31.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 925730.2 | 215220.9 | -76.8% | -76.8% | -76.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 282595.0 | 215220.9 | -23.8% | -23.8% | -23.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 210241.7 | 183752.9 | -12.6% | -12.6% | -12.6% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 170924.5 | 183752.9 | +7.5% | +7.5% | +7.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 1675553.4 | 297857.0 | -82.2% | -82.2% | -82.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 579704.9 | 297857.0 | -48.6% | -48.6% | -48.6% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 381689.5 | 348064.4 | -8.8% | -8.8% | -8.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 392136.2 | 348064.4 | -11.2% | -11.2% | -11.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 3047453.8 | 466109.7 | -84.7% | -84.7% | -84.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 1282860.3 | 466109.7 | -63.7% | -63.7% | -63.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 461945.4 | 680153.1 | +47.2% | +47.2% | +47.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 807923.9 | 680153.1 | -15.8% | -15.8% | -15.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 3689098.9 | 802523.1 | -78.2% | -78.2% | -78.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 2375166.3 | 802523.1 | -66.2% | -66.2% | -66.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 503419.0 | 1209304.5 | +140.2% | +140.2% | +140.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 1863015.9 | 1209304.5 | -35.1% | -35.1% | -35.1% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 4021107.9 | 1333385.9 | -66.8% | -66.8% | -66.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 4887390.0 | 1333385.9 | -72.7% | -72.7% | -72.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 517261.3 | 2621047.5 | +406.7% | +406.7% | +406.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 4068521.4 | 2621047.5 | -35.6% | -35.6% | -35.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 4131434.0 | 2748851.3 | -33.5% | -33.5% | -33.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 9950951.4 | 2748851.3 | -72.4% | -72.4% | -72.4% |

#### Dictionary already prepared

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 3872.6 | 2609.8 | -32.6% | -32.6% | -32.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 3823.2 | 2609.8 | -31.7% | -31.7% | -31.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | str_contains() loop | 2751.6 | 1568.1 | -43.0% | -43.0% | -43.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | preg_match() | 2012.9 | 1568.1 | -22.1% | -22.1% | -22.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | str_contains() loop | 3149.4 | 3014.9 | -4.3% | -4.3% | -4.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | preg_match() | 4627.4 | 3014.9 | -34.8% | -34.8% | -34.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | str_contains() loop | 2880.0 | 3113.9 | +8.1% | +8.1% | +8.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | preg_match() | 4593.4 | 3113.9 | -32.2% | -32.2% | -32.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 11354.7 | 13187.0 | +16.1% | +16.1% | +16.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 23185.7 | 13187.0 | -43.1% | -43.1% | -43.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | str_contains() loop | 5070.0 | 5826.0 | +14.9% | +14.9% | +14.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | preg_match() | 9856.7 | 5826.0 | -40.9% | -40.9% | -40.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 6239.6 | 2679.5 | -57.1% | -57.1% | -57.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 5686.6 | 2679.5 | -52.9% | -52.9% | -52.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | str_contains() loop | 3895.9 | 1569.7 | -59.7% | -59.7% | -59.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | preg_match() | 2101.9 | 1569.7 | -25.3% | -25.3% | -25.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | str_contains() loop | 4523.8 | 3104.2 | -31.4% | -31.4% | -31.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | preg_match() | 7225.9 | 3104.2 | -57.0% | -57.0% | -57.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | str_contains() loop | 4063.9 | 3230.2 | -20.5% | -20.5% | -20.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | preg_match() | 7589.9 | 3230.2 | -57.4% | -57.4% | -57.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 19277.7 | 13895.0 | -27.9% | -27.9% | -27.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 42332.3 | 13895.0 | -67.2% | -67.2% | -67.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | str_contains() loop | 7425.3 | 6099.0 | -17.9% | -17.9% | -17.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | preg_match() | 16968.0 | 6099.0 | -64.1% | -64.1% | -64.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 11374.7 | 2789.8 | -75.5% | -75.5% | -75.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 12076.2 | 2789.8 | -76.9% | -76.9% | -76.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | str_contains() loop | 6717.6 | 1569.7 | -76.6% | -76.6% | -76.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | preg_match() | 2319.9 | 1569.7 | -32.3% | -32.3% | -32.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | str_contains() loop | 8064.8 | 3259.5 | -59.6% | -59.6% | -59.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | preg_match() | 15812.7 | 3259.5 | -79.4% | -79.4% | -79.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | str_contains() loop | 6888.5 | 3412.5 | -50.5% | -50.5% | -50.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | preg_match() | 16577.8 | 3412.5 | -79.4% | -79.4% | -79.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 40236.7 | 15214.7 | -62.2% | -62.2% | -62.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 107220.1 | 15214.7 | -85.8% | -85.8% | -85.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | str_contains() loop | 15927.3 | 6570.0 | -58.8% | -58.8% | -58.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | preg_match() | 40616.3 | 6570.0 | -83.8% | -83.8% | -83.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 21321.2 | 2794.3 | -86.9% | -86.9% | -86.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 29696.3 | 2794.3 | -90.6% | -90.6% | -90.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | str_contains() loop | 12522.5 | 1569.1 | -87.5% | -87.5% | -87.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | preg_match() | 2708.8 | 1569.1 | -42.1% | -42.1% | -42.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | str_contains() loop | 15410.1 | 3263.4 | -78.8% | -78.8% | -78.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | preg_match() | 38917.0 | 3263.4 | -91.6% | -91.6% | -91.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | str_contains() loop | 12941.3 | 3416.4 | -73.6% | -73.6% | -73.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | preg_match() | 41814.5 | 3416.4 | -91.8% | -91.8% | -91.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 76125.9 | 15234.0 | -80.0% | -80.0% | -80.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 298671.3 | 15234.0 | -94.9% | -94.9% | -94.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | str_contains() loop | 32324.7 | 6570.0 | -79.7% | -79.7% | -79.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | preg_match() | 111402.0 | 6570.0 | -94.1% | -94.1% | -94.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 40725.1 | 2802.6 | -93.1% | -93.1% | -93.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 57230.7 | 2802.6 | -95.1% | -95.1% | -95.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | str_contains() loop | 23556.9 | 1569.8 | -93.3% | -93.3% | -93.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | preg_match() | 3494.7 | 1569.8 | -55.1% | -55.1% | -55.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | str_contains() loop | 29162.2 | 3272.4 | -88.8% | -88.8% | -88.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | preg_match() | 76319.0 | 3272.4 | -95.7% | -95.7% | -95.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | str_contains() loop | 24109.5 | 3425.4 | -85.8% | -85.8% | -85.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | preg_match() | 80836.0 | 3425.4 | -95.8% | -95.8% | -95.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 146084.7 | 15249.0 | -89.6% | -89.6% | -89.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 594818.7 | 15249.0 | -97.4% | -97.4% | -97.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | str_contains() loop | 61610.6 | 6570.0 | -89.3% | -89.3% | -89.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | preg_match() | 221694.2 | 6570.0 | -97.0% | -97.0% | -97.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 80770.4 | 2806.5 | -96.5% | -96.5% | -96.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 119580.2 | 2806.5 | -97.7% | -97.7% | -97.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | str_contains() loop | 45764.5 | 1569.8 | -96.6% | -96.6% | -96.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | preg_match() | 5020.6 | 1569.8 | -68.7% | -68.7% | -68.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | str_contains() loop | 57168.9 | 3276.2 | -94.3% | -94.3% | -94.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | preg_match() | 159605.1 | 3276.2 | -97.9% | -97.9% | -97.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | str_contains() loop | 46922.2 | 3429.2 | -92.7% | -92.7% | -92.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | preg_match() | 168355.5 | 3429.2 | -98.0% | -98.0% | -98.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 299086.3 | 15276.7 | -94.9% | -94.9% | -94.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 1229614.9 | 15276.7 | -98.8% | -98.8% | -98.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | str_contains() loop | 124819.0 | 6574.3 | -94.7% | -94.7% | -94.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | preg_match() | 459809.6 | 6574.3 | -98.6% | -98.6% | -98.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 161151.7 | 2821.4 | -98.2% | -98.2% | -98.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 240391.5 | 2821.4 | -98.8% | -98.8% | -98.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | str_contains() loop | 91032.2 | 1569.8 | -98.3% | -98.3% | -98.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | preg_match() | 8029.0 | 1569.8 | -80.4% | -80.4% | -80.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | str_contains() loop | 114417.1 | 3291.1 | -97.1% | -97.1% | -97.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | preg_match() | 319827.1 | 3291.1 | -99.0% | -99.0% | -99.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | str_contains() loop | 92862.4 | 3444.1 | -96.3% | -96.3% | -96.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | preg_match() | 337370.0 | 3444.1 | -99.0% | -99.0% | -99.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 606319.6 | 15381.7 | -97.5% | -97.5% | -97.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 2503654.6 | 15381.7 | -99.4% | -99.4% | -99.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | str_contains() loop | 257001.2 | 6604.3 | -97.4% | -97.4% | -97.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | preg_match() | 929316.8 | 6604.3 | -99.3% | -99.3% | -99.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 15059.6 | 11184.6 | -25.7% | -25.7% | -25.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | preg_match() per term | 21119.9 | 11184.6 | -47.0% | -47.0% | -47.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 12020.3 | 9164.1 | -23.8% | -23.8% | -23.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 24109.3 | 9164.1 | -62.0% | -62.0% | -62.0% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 18909.4 | 11130.8 | -41.1% | -41.1% | -41.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 41687.6 | 11130.8 | -73.3% | -73.3% | -73.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 27153.5 | 12065.2 | -55.6% | -55.6% | -55.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | preg_match() per term | 38374.6 | 12065.2 | -68.6% | -68.6% | -68.6% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 22022.4 | 9370.5 | -57.5% | -57.5% | -57.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 45417.5 | 9370.5 | -79.4% | -79.4% | -79.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 34878.3 | 12634.9 | -63.8% | -63.8% | -63.8% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 78002.9 | 12634.9 | -83.8% | -83.8% | -83.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 50244.6 | 13293.9 | -73.5% | -73.5% | -73.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | preg_match() per term | 73228.5 | 13293.9 | -81.8% | -81.8% | -81.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 39437.8 | 9559.1 | -75.8% | -75.8% | -75.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 83222.1 | 9559.1 | -88.5% | -88.5% | -88.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 65195.3 | 15160.0 | -76.7% | -76.7% | -76.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 144501.9 | 15160.0 | -89.5% | -89.5% | -89.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 95908.6 | 14877.8 | -84.5% | -84.5% | -84.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | preg_match() per term | 134652.7 | 14877.8 | -89.0% | -89.0% | -89.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 76834.1 | 9864.6 | -87.2% | -87.2% | -87.2% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 158969.0 | 9864.6 | -93.8% | -93.8% | -93.8% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 120489.6 | 18767.0 | -84.4% | -84.4% | -84.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 266932.9 | 18767.0 | -93.0% | -93.0% | -93.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 174359.3 | 17255.7 | -90.1% | -90.1% | -90.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | preg_match() per term | 251802.0 | 17255.7 | -93.1% | -93.1% | -93.1% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 141759.1 | 10262.7 | -92.8% | -92.8% | -92.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 291846.0 | 10262.7 | -96.5% | -96.5% | -96.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 210380.2 | 22967.1 | -89.1% | -89.1% | -89.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 470558.0 | 22967.1 | -95.1% | -95.1% | -95.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 306287.0 | 17457.3 | -94.3% | -94.3% | -94.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | preg_match() per term | 442261.6 | 17457.3 | -96.1% | -96.1% | -96.1% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 282284.0 | 10377.1 | -96.3% | -96.3% | -96.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 570094.3 | 10377.1 | -98.2% | -98.2% | -98.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 351655.7 | 23146.1 | -93.4% | -93.4% | -93.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 833260.9 | 23146.1 | -97.2% | -97.2% | -97.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 562768.7 | 17807.1 | -96.8% | -96.8% | -96.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | preg_match() per term | 816956.3 | 17807.1 | -97.8% | -97.8% | -97.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 556549.8 | 10637.6 | -98.1% | -98.1% | -98.1% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 1109518.9 | 10637.6 | -99.0% | -99.0% | -99.0% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 626826.3 | 23549.9 | -96.2% | -96.2% | -96.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 1535000.1 | 23549.9 | -98.5% | -98.5% | -98.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 75958.2 | 14067.9 | -81.5% | -81.5% | -81.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 8172.9 | 14067.9 | +72.1% | +72.1% | +72.1% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 601540.9 | 105889.0 | -82.4% | -82.4% | -82.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 58432.0 | 105889.0 | +81.2% | +81.2% | +81.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 114538.0 | 15053.9 | -86.9% | -86.9% | -86.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 29868.3 | 15053.9 | -49.6% | -49.6% | -49.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 909845.2 | 113836.9 | -87.5% | -87.5% | -87.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 231994.9 | 113836.9 | -50.9% | -50.9% | -50.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 204485.8 | 16112.4 | -92.1% | -92.1% | -92.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 59591.6 | 16112.4 | -73.0% | -73.0% | -73.0% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 1629546.5 | 122209.0 | -92.5% | -92.5% | -92.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 469765.6 | 122209.0 | -74.0% | -74.0% | -74.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 371102.3 | 16762.9 | -95.5% | -95.5% | -95.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 128552.6 | 16762.9 | -87.0% | -87.0% | -87.0% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 2962771.3 | 127221.2 | -95.7% | -95.7% | -95.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 1021468.2 | 127221.2 | -87.5% | -87.5% | -87.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 451012.3 | 17310.8 | -96.2% | -96.2% | -96.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 225350.8 | 17310.8 | -92.3% | -92.3% | -92.3% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 3601603.2 | 131644.1 | -96.3% | -96.3% | -96.3% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 1795856.0 | 131644.1 | -92.7% | -92.7% | -92.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 491702.7 | 17598.8 | -96.4% | -96.4% | -96.4% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 433517.7 | 17598.8 | -95.9% | -95.9% | -95.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 3927388.1 | 133683.9 | -96.6% | -96.6% | -96.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 3461191.8 | 133683.9 | -96.1% | -96.1% | -96.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 504961.1 | 17852.8 | -96.5% | -96.5% | -96.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 841865.6 | 17852.8 | -97.9% | -97.9% | -97.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 4033021.6 | 136612.1 | -96.6% | -96.6% | -96.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 6727977.7 | 136612.1 | -98.0% | -98.0% | -98.0% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 3807.5 | 2780.6 | -27.0% | -27.0% | -27.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 3829.3 | 2780.6 | -27.4% | -27.4% | -27.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | str_contains() loop | 2716.2 | 1598.3 | -41.2% | -41.2% | -41.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | preg_match() | 2020.9 | 1598.3 | -20.9% | -20.9% | -20.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | str_contains() loop | 3111.9 | 3241.9 | +4.2% | +4.2% | +4.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | preg_match() | 4635.4 | 3241.9 | -30.1% | -30.1% | -30.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | str_contains() loop | 2843.5 | 3346.9 | +17.7% | +17.7% | +17.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | preg_match() | 4601.4 | 3346.9 | -27.3% | -27.3% | -27.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 11288.3 | 14771.0 | +30.9% | +30.9% | +30.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 23191.7 | 14771.0 | -36.3% | -36.3% | -36.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | str_contains() loop | 5073.0 | 6425.0 | +26.7% | +26.7% | +26.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | preg_match() | 9864.7 | 6425.0 | -34.9% | -34.9% | -34.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 6116.6 | 2873.6 | -53.0% | -53.0% | -53.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 5692.6 | 2873.6 | -49.5% | -49.5% | -49.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | str_contains() loop | 3833.1 | 1599.0 | -58.3% | -58.3% | -58.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | preg_match() | 2109.9 | 1599.0 | -24.2% | -24.2% | -24.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | str_contains() loop | 4457.4 | 3359.6 | -24.6% | -24.6% | -24.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | preg_match() | 7233.9 | 3359.6 | -53.6% | -53.6% | -53.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | str_contains() loop | 4000.5 | 3500.6 | -12.5% | -12.5% | -12.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | preg_match() | 7597.9 | 3500.6 | -53.9% | -53.9% | -53.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 19069.3 | 15715.0 | -17.6% | -17.6% | -17.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 42338.3 | 15715.0 | -62.9% | -62.9% | -62.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | str_contains() loop | 7383.0 | 6789.0 | -8.0% | -8.0% | -8.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | preg_match() | 16976.0 | 6789.0 | -60.0% | -60.0% | -60.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 11135.3 | 3020.6 | -72.9% | -72.9% | -72.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 12082.3 | 3020.6 | -75.0% | -75.0% | -75.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | str_contains() loop | 6586.5 | 1599.0 | -75.7% | -75.7% | -75.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | preg_match() | 2327.9 | 1599.0 | -31.3% | -31.3% | -31.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | str_contains() loop | 7925.5 | 3566.6 | -55.0% | -55.0% | -55.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | preg_match() | 15820.8 | 3566.6 | -77.5% | -77.5% | -77.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | str_contains() loop | 6757.8 | 3743.6 | -44.6% | -44.6% | -44.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | preg_match() | 16585.8 | 3743.6 | -77.4% | -77.4% | -77.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 39726.7 | 17473.0 | -56.0% | -56.0% | -56.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 107226.0 | 17473.0 | -83.7% | -83.7% | -83.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | str_contains() loop | 15769.3 | 7417.0 | -53.0% | -53.0% | -53.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | preg_match() | 40624.3 | 7417.0 | -81.7% | -81.7% | -81.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 20820.4 | 3026.6 | -85.5% | -85.5% | -85.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 29702.3 | 3026.6 | -89.8% | -89.8% | -89.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | str_contains() loop | 12254.9 | 1598.4 | -87.0% | -87.0% | -87.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | preg_match() | 2716.7 | 1598.4 | -41.2% | -41.2% | -41.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | str_contains() loop | 15113.6 | 3572.0 | -76.4% | -76.4% | -76.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | preg_match() | 38925.0 | 3572.0 | -90.8% | -90.8% | -90.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | str_contains() loop | 12676.8 | 3749.0 | -70.4% | -70.4% | -70.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | preg_match() | 41822.5 | 3749.0 | -91.0% | -91.0% | -91.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 74945.4 | 17498.0 | -76.7% | -76.7% | -76.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 298677.7 | 17498.0 | -94.1% | -94.1% | -94.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | str_contains() loop | 31914.7 | 7417.0 | -76.8% | -76.8% | -76.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | preg_match() | 111410.0 | 7417.0 | -93.3% | -93.3% | -93.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 39732.3 | 3036.4 | -92.4% | -92.4% | -92.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 57236.7 | 3036.4 | -94.7% | -94.7% | -94.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | str_contains() loop | 23023.2 | 1599.0 | -93.1% | -93.1% | -93.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | preg_match() | 3502.8 | 1599.0 | -54.4% | -54.4% | -54.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | str_contains() loop | 28575.2 | 3582.4 | -87.5% | -87.5% | -87.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | preg_match() | 76327.0 | 3582.4 | -95.3% | -95.3% | -95.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | str_contains() loop | 23586.1 | 3759.4 | -84.1% | -84.1% | -84.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | preg_match() | 80844.0 | 3759.4 | -95.3% | -95.3% | -95.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 143844.3 | 17518.0 | -87.8% | -87.8% | -87.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 594824.3 | 17518.0 | -97.1% | -97.1% | -97.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | str_contains() loop | 60705.0 | 7417.0 | -87.8% | -87.8% | -87.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | preg_match() | 221702.5 | 7417.0 | -96.7% | -96.7% | -96.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 78773.5 | 3040.7 | -96.1% | -96.1% | -96.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 119586.0 | 3040.7 | -97.5% | -97.5% | -97.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | str_contains() loop | 44685.0 | 1599.0 | -96.4% | -96.4% | -96.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | preg_match() | 5028.6 | 1599.0 | -68.2% | -68.2% | -68.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | str_contains() loop | 55981.6 | 3586.8 | -93.6% | -93.6% | -93.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | preg_match() | 159613.2 | 3586.8 | -97.8% | -97.8% | -97.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | str_contains() loop | 45836.7 | 3763.8 | -91.8% | -91.8% | -91.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | preg_match() | 168363.5 | 3763.8 | -97.8% | -97.8% | -97.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 294258.6 | 17551.0 | -94.0% | -94.0% | -94.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 1229622.1 | 17551.0 | -98.6% | -98.6% | -98.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | str_contains() loop | 122887.2 | 7422.0 | -94.0% | -94.0% | -94.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | preg_match() | 459817.6 | 7422.0 | -98.4% | -98.4% | -98.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 157148.7 | 3058.8 | -98.1% | -98.1% | -98.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 240397.7 | 3058.8 | -98.7% | -98.7% | -98.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | str_contains() loop | 88900.2 | 1599.0 | -98.2% | -98.2% | -98.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | preg_match() | 8037.0 | 1599.0 | -80.1% | -80.1% | -80.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | str_contains() loop | 112016.6 | 3604.7 | -96.8% | -96.8% | -96.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | preg_match() | 319834.5 | 3604.7 | -98.9% | -98.9% | -98.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | str_contains() loop | 90696.5 | 3781.8 | -95.8% | -95.8% | -95.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | preg_match() | 337377.9 | 3781.8 | -98.9% | -98.9% | -98.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 596603.5 | 17680.4 | -97.0% | -97.0% | -97.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 2503656.9 | 17680.4 | -99.3% | -99.3% | -99.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | str_contains() loop | 253052.7 | 7462.0 | -97.1% | -97.1% | -97.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | preg_match() | 929325.5 | 7462.0 | -99.2% | -99.2% | -99.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 15125.8 | 12382.2 | -18.1% | -18.1% | -18.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | preg_match() per term | 21562.1 | 12382.2 | -42.6% | -42.6% | -42.6% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 11630.9 | 9575.3 | -17.7% | -17.7% | -17.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 24569.5 | 9575.3 | -61.0% | -61.0% | -61.0% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 18734.7 | 14427.0 | -23.0% | -23.0% | -23.0% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 42060.4 | 14427.0 | -65.7% | -65.7% | -65.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 27244.0 | 13364.6 | -50.9% | -50.9% | -50.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | preg_match() per term | 39279.6 | 13364.6 | -66.0% | -66.0% | -66.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 21230.3 | 9825.3 | -53.7% | -53.7% | -53.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 46287.0 | 9825.3 | -78.8% | -78.8% | -78.8% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 34549.1 | 16094.5 | -53.4% | -53.4% | -53.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 78807.0 | 16094.5 | -79.6% | -79.6% | -79.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 50564.4 | 14678.3 | -71.0% | -71.0% | -71.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | preg_match() per term | 75124.6 | 14678.3 | -80.5% | -80.5% | -80.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 38034.3 | 10065.1 | -73.5% | -73.5% | -73.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 84881.8 | 10065.1 | -88.1% | -88.1% | -88.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 64834.7 | 18742.3 | -71.1% | -71.1% | -71.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 146233.0 | 18742.3 | -87.2% | -87.2% | -87.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 96304.0 | 16394.5 | -83.0% | -83.0% | -83.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | preg_match() per term | 138395.5 | 16394.5 | -88.2% | -88.2% | -88.2% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 74015.0 | 10449.7 | -85.9% | -85.9% | -85.9% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 162095.7 | 10449.7 | -93.6% | -93.6% | -93.6% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 119479.3 | 22527.5 | -81.1% | -81.1% | -81.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 270174.0 | 22527.5 | -91.7% | -91.7% | -91.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 174679.2 | 18932.8 | -89.2% | -89.2% | -89.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | preg_match() per term | 258876.2 | 18932.8 | -92.7% | -92.7% | -92.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 136539.1 | 10950.9 | -92.0% | -92.0% | -92.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 297694.5 | 10950.9 | -96.3% | -96.3% | -96.3% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 208045.3 | 26941.7 | -87.1% | -87.1% | -87.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 476404.9 | 26941.7 | -94.3% | -94.3% | -94.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 303860.8 | 19146.7 | -93.7% | -93.7% | -93.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | preg_match() per term | 454278.4 | 19146.7 | -95.8% | -95.8% | -95.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 272397.9 | 11075.8 | -95.9% | -95.9% | -95.9% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 580851.5 | 11075.8 | -98.1% | -98.1% | -98.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 344702.2 | 27139.1 | -92.1% | -92.1% | -92.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 842393.4 | 27139.1 | -96.8% | -96.8% | -96.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 555045.8 | 19517.4 | -96.5% | -96.5% | -96.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | preg_match() per term | 838837.6 | 19517.4 | -97.7% | -97.7% | -97.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 537163.2 | 11342.4 | -97.9% | -97.9% | -97.9% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 1130076.6 | 11342.4 | -99.0% | -99.0% | -99.0% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 610407.9 | 27597.1 | -95.5% | -95.5% | -95.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 1550633.6 | 27597.1 | -98.2% | -98.2% | -98.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 76802.3 | 15547.0 | -79.8% | -79.8% | -79.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 8097.1 | 15547.0 | +92.0% | +92.0% | +92.0% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 608277.6 | 117718.0 | -80.6% | -80.6% | -80.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 57868.1 | 117718.0 | +103.4% | +103.4% | +103.4% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 116525.4 | 16440.8 | -85.9% | -85.9% | -85.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 29745.5 | 16440.8 | -44.7% | -44.7% | -44.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 925732.6 | 124953.0 | -86.5% | -86.5% | -86.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 231055.0 | 124953.0 | -45.9% | -45.9% | -45.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 210241.7 | 17395.0 | -91.7% | -91.7% | -91.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 59386.5 | 17395.0 | -70.7% | -70.7% | -70.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 1675554.4 | 132451.0 | -92.1% | -92.1% | -92.1% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 468166.6 | 132451.0 | -71.7% | -71.7% | -71.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 381690.1 | 17982.3 | -95.3% | -95.3% | -95.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 128231.0 | 17982.3 | -86.0% | -86.0% | -86.0% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 3047456.2 | 136989.0 | -95.5% | -95.5% | -95.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 1018937.7 | 136989.0 | -86.6% | -86.6% | -86.6% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 461945.5 | 18492.1 | -96.0% | -96.0% | -96.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 224882.9 | 18492.1 | -91.8% | -91.8% | -91.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 3689090.5 | 141131.9 | -96.2% | -96.2% | -96.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 1792154.3 | 141131.9 | -92.1% | -92.1% | -92.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 503418.1 | 18782.0 | -96.3% | -96.3% | -96.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 433047.8 | 18782.0 | -95.7% | -95.7% | -95.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 4021111.0 | 143187.0 | -96.4% | -96.4% | -96.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 3457472.1 | 143187.0 | -95.9% | -95.9% | -95.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 517260.9 | 19049.5 | -96.3% | -96.3% | -96.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 841388.3 | 19049.5 | -97.7% | -97.7% | -97.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 4131423.8 | 146159.2 | -96.5% | -96.5% | -96.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 6724197.6 | 146159.2 | -97.8% | -97.8% | -97.8% |

### Control tasks

#### Dictionary preparation included

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | str_contains() loop | 4796.1 | 110627.2 | +2206.6% | +2206.6% | +2206.6% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | preg_match() | 19382.5 | 110627.2 | +470.8% | +470.8% | +470.8% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | strtr() | 1529537.2 | 2004721.6 | +31.1% | +31.1% | +31.1% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace_callback() | 178692.5 | 2004721.6 | +1021.9% | +1021.9% | +1021.9% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | str_replace() | 1020021.7 | 2004721.6 | +96.5% | +96.5% | +96.5% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace() | 174254.2 | 2004721.6 | +1050.5% | +1050.5% | +1050.5% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | str_contains() loop | 4711.2 | 112338.0 | +2284.5% | +2284.4% | +2284.5% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | preg_match() | 18014.5 | 112338.0 | +523.6% | +523.6% | +523.6% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | strtr() | 1285528.2 | 2171949.6 | +69.0% | +69.0% | +69.0% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace_callback() | 175249.4 | 2171949.6 | +1139.3% | +1139.3% | +1139.4% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | str_replace() | 954193.4 | 2171949.6 | +127.6% | +127.6% | +127.6% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace() | 170832.6 | 2171949.6 | +1171.4% | +1171.4% | +1171.4% |

#### Dictionary already prepared

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | str_contains() loop | 4796.1 | 2799.3 | -41.6% | -41.6% | -41.6% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | preg_match() | 4227.5 | 2799.3 | -33.8% | -33.8% | -33.8% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | strtr() | 1529536.6 | 1796810.2 | +17.5% | +17.5% | +17.5% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace_callback() | 78202.5 | 1796810.2 | +2197.6% | +2197.6% | +2197.6% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | str_replace() | 947128.4 | 1796810.2 | +89.7% | +89.7% | +89.7% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace() | 74417.0 | 1796810.2 | +2314.5% | +2314.5% | +2314.5% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | str_contains() loop | 4711.3 | 3033.0 | -35.6% | -35.6% | -35.6% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | preg_match() | 4233.5 | 3033.0 | -28.4% | -28.4% | -28.4% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | strtr() | 1285528.0 | 1962712.7 | +52.7% | +52.7% | +52.7% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace_callback() | 78118.3 | 1962712.7 | +2412.5% | +2412.5% | +2412.5% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | str_replace() | 879660.5 | 1962712.7 | +123.1% | +123.1% | +123.1% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace() | 74338.5 | 1962712.7 | +2540.2% | +2540.2% | +2540.2% |
