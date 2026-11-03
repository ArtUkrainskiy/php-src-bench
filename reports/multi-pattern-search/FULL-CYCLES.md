# Complete CPU-cycle comparisons

Unit: cycles per complete job. Lower is better. Δ is the median of paired per-pass changes; min/max are paired changes, not confidence intervals.

All measured alternatives are listed. Preparation and reuse are separate sections. Natural API result representations are retained; see [method](METHOD.md).

## Everyday cases

### Product tasks

#### Dictionary preparation included

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1476.7 | 28933.8 | +1861.5% | +1819.2% | +1876.9% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5761.5 | 28933.8 | +401.9% | +399.2% | +403.0% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1224.2 | 28572.3 | +2232.5% | +2203.6% | +2331.4% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5338.5 | 28572.3 | +435.8% | +430.0% | +457.8% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1382.7 | 29241.7 | +2027.2% | +1994.5% | +2051.7% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 6021.9 | 29241.7 | +383.8% | +375.8% | +389.6% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1273.7 | 29443.6 | +2236.1% | +2188.2% | +2250.0% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 6092.5 | 29443.6 | +385.1% | +376.2% | +387.9% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4889.4 | 34101.8 | +598.6% | +585.8% | +601.9% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 10061.0 | 34101.8 | +239.2% | +236.3% | +241.2% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 2788.1 | 30732.3 | +1002.3% | +990.0% | +1029.7% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 7078.3 | 30732.3 | +334.8% | +330.4% | +339.3% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 5966.3 | 50340.8 | +737.7% | +708.1% | +753.5% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 7764.0 | 50340.8 | +547.0% | +543.7% | +552.4% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 6799.0 | 49261.1 | +627.1% | +623.4% | +644.8% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 6103.9 | 49261.1 | +707.6% | +704.6% | +725.2% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 9849.9 | 51087.8 | +423.0% | +411.9% | +428.9% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 8654.2 | 51087.8 | +489.9% | +484.2% | +501.9% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 6754.4 | 50777.7 | +658.7% | +649.6% | +661.2% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 8770.1 | 50777.7 | +479.2% | +476.3% | +487.6% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 16873.9 | 59297.8 | +251.4% | +248.2% | +253.2% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 23800.7 | 59297.8 | +148.8% | +148.4% | +150.7% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 9468.3 | 53320.0 | +463.5% | +459.0% | +475.7% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 12751.5 | 53320.0 | +318.6% | +315.1% | +326.2% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1570.7 | 50672.3 | +3144.1% | +3115.0% | +3220.4% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5890.5 | 50672.3 | +761.8% | +749.1% | +778.6% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1319.7 | 50426.9 | +3721.2% | +3713.7% | +3774.1% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5284.7 | 50426.9 | +853.7% | +845.6% | +859.1% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1753.7 | 50825.0 | +2806.4% | +2777.0% | +2877.8% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 6068.9 | 50825.0 | +736.6% | +727.6% | +744.5% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1495.9 | 51026.2 | +3311.2% | +3280.4% | +3403.2% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 6186.9 | 51026.2 | +724.2% | +721.4% | +743.7% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 7392.9 | 53329.6 | +623.9% | +618.4% | +628.7% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 12222.8 | 53329.6 | +336.3% | +335.0% | +340.7% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4395.3 | 51890.2 | +1080.6% | +1048.2% | +1117.5% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 7610.9 | 51890.2 | +584.6% | +576.0% | +591.5% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 20026.2 | 37053.0 | +84.5% | +80.8% | +87.3% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 15419.1 | 37053.0 | +140.3% | +139.4% | +142.6% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 10035.4 | 26016.6 | +159.2% | +155.1% | +170.3% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 4222.3 | 26016.6 | +516.2% | +505.1% | +543.6% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 11248.1 | 31704.0 | +181.8% | +181.1% | +183.9% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 9870.7 | 31704.0 | +221.8% | +220.2% | +224.5% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 12264.8 | 37031.3 | +200.7% | +198.1% | +203.4% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 14708.7 | 37031.3 | +151.1% | +150.5% | +153.6% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | strtr() | 4340.1 | 22060.6 | +408.4% | +405.2% | +411.0% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | preg_replace_callback() | 18245.2 | 22060.6 | +20.9% | +19.7% | +21.7% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | str_replace() | 13927.4 | 22060.6 | +58.2% | +56.8% | +59.4% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | strtr() | 6455.5 | 25576.7 | +297.1% | +286.2% | +299.1% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | preg_replace_callback() | 23138.5 | 25576.7 | +10.5% | +3.4% | +11.2% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | str_replace() | 17660.4 | 25576.7 | +44.6% | +41.5% | +45.8% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 1500.8 | 9399.2 | +526.4% | +517.0% | +533.3% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 8345.5 | 9399.2 | +12.9% | +11.5% | +13.2% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 5972.1 | 9399.2 | +57.5% | +56.6% | +58.4% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 9348.6 | 24150.9 | +159.7% | +157.4% | +182.6% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 20451.9 | 24150.9 | +18.7% | +17.7% | +29.2% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 12675.3 | 24150.9 | +91.9% | +89.7% | +107.5% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 876.1 | 6970.6 | +689.9% | +688.4% | +704.6% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 5228.9 | 6970.6 | +32.3% | +31.5% | +35.0% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 4605.2 | 6970.6 | +51.1% | +49.9% | +52.8% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 1308.5 | 7808.2 | +496.0% | +491.0% | +525.4% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 7029.1 | 7808.2 | +11.1% | +10.0% | +15.6% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 5344.2 | 7808.2 | +46.0% | +45.3% | +52.7% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | strtr() | 944.1 | 3617.5 | +281.9% | +263.9% | +300.3% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace_callback() | 5157.7 | 3617.5 | -29.6% | -30.5% | -26.7% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | str_replace() | 3855.8 | 3617.5 | -6.3% | -6.9% | -2.8% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace() | 4094.8 | 3617.5 | -12.1% | -12.4% | -7.1% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 1553.8 | 35973.0 | +2214.6% | +2200.7% | +2288.0% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 10620.5 | 35973.0 | +239.1% | +238.1% | +242.6% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 6540.9 | 35973.0 | +449.7% | +432.4% | +467.2% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 1916.4 | 36856.9 | +1824.6% | +1735.3% | +1875.5% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 11604.4 | 36856.9 | +217.6% | +215.9% | +226.1% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 7197.4 | 36856.9 | +412.1% | +406.8% | +422.4% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 12860.3 | 49387.4 | +283.8% | +282.7% | +289.6% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 20937.8 | 49387.4 | +135.6% | +133.0% | +139.1% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 16204.3 | 49387.4 | +206.0% | +202.2% | +211.9% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 27111.6 | 117820.8 | +334.2% | +326.3% | +337.8% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 30775.1 | 117820.8 | +282.8% | +279.9% | +287.0% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 73036.9 | 117820.8 | +61.4% | +60.6% | +62.0% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 30305.4 | 117820.8 | +288.5% | +287.6% | +290.1% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 27838.4 | 122580.5 | +340.2% | +336.8% | +347.0% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 32115.2 | 122580.5 | +282.9% | +279.3% | +287.9% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 76554.1 | 122580.5 | +60.3% | +60.0% | +62.6% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 31206.2 | 122580.5 | +293.6% | +290.3% | +294.4% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 42223.0 | 151982.3 | +260.5% | +259.5% | +264.2% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 34334.8 | 151982.3 | +344.5% | +339.9% | +347.9% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 112353.2 | 151982.3 | +35.1% | +34.8% | +37.0% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 32393.2 | 151982.3 | +369.2% | +367.4% | +376.6% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 335225.9 | 707048.9 | +110.9% | +109.8% | +111.8% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 50079.2 | 707048.9 | +1314.9% | +1305.2% | +1320.9% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 712904.4 | 707048.9 | -1.0% | -1.2% | -0.8% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 47986.4 | 707048.9 | +1375.0% | +1367.4% | +1389.7% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 836.0 | 6704.6 | +701.6% | +697.1% | +705.7% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 9136.4 | 6704.6 | -26.6% | -27.2% | -26.5% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 7964.0 | 6704.6 | -15.7% | -16.1% | -15.4% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 1029.6 | 7176.1 | +600.3% | +572.1% | +658.8% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 9801.8 | 7176.1 | -26.7% | -28.9% | -20.2% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 8262.2 | 7176.1 | -13.3% | -15.7% | -6.0% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 57650.2 | 153024.4 | +167.5% | +162.8% | +176.5% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | preg_match() per term | 100552.5 | 153024.4 | +52.3% | +50.3% | +54.2% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 49179.4 | 151213.5 | +205.6% | +201.6% | +223.0% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 146414.1 | 151213.5 | +2.6% | +1.0% | +4.7% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 70978.3 | 154119.9 | +116.7% | +115.0% | +119.2% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 217538.8 | 154119.9 | -29.2% | -29.5% | -28.7% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 135360.8 | 148065.6 | +9.4% | +8.7% | +10.2% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 157442.3 | 148065.6 | -6.5% | -7.9% | -5.0% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 1080365.1 | 197229.9 | -81.7% | -81.9% | -81.7% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 447384.7 | 197229.9 | -56.0% | -56.1% | -55.8% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1553.1 | 27391.6 | +1674.4% | +1649.8% | +1710.1% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 6200.2 | 27391.6 | +343.3% | +340.6% | +348.8% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1224.9 | 27430.2 | +2141.6% | +2086.6% | +2193.4% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5826.7 | 27430.2 | +370.8% | +359.4% | +393.4% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1371.3 | 28081.2 | +1942.7% | +1928.9% | +1968.3% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 6551.4 | 28081.2 | +330.5% | +318.1% | +333.3% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1250.6 | 27909.7 | +2150.6% | +2116.8% | +2159.6% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 6591.9 | 27909.7 | +323.7% | +313.5% | +334.1% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4976.0 | 33609.8 | +576.3% | +569.0% | +597.3% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 11344.5 | 33609.8 | +196.6% | +194.0% | +206.6% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 2736.2 | 29500.8 | +977.3% | +969.0% | +991.6% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 7632.9 | 29500.8 | +285.8% | +272.3% | +291.9% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 6103.4 | 47345.5 | +677.1% | +673.4% | +679.7% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 7831.7 | 47345.5 | +504.8% | +503.8% | +509.4% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 6860.3 | 46328.9 | +575.1% | +573.5% | +582.6% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 6138.5 | 46328.9 | +662.0% | +645.7% | +666.2% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 9990.1 | 47593.4 | +376.5% | +374.0% | +378.5% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 8699.6 | 47593.4 | +446.8% | +444.6% | +450.9% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 6870.3 | 47990.6 | +595.8% | +588.5% | +613.0% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 8730.7 | 47990.6 | +450.0% | +446.2% | +458.3% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 15932.8 | 57423.0 | +260.4% | +260.2% | +278.1% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 24112.9 | 57423.0 | +138.1% | +137.9% | +149.8% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 9003.7 | 50522.4 | +461.7% | +458.6% | +478.5% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 12913.8 | 50522.4 | +290.9% | +289.4% | +304.4% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1614.7 | 48748.0 | +2915.7% | +2869.7% | +2923.8% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 6173.8 | 48748.0 | +688.5% | +684.8% | +693.7% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1309.9 | 48458.8 | +3608.9% | +3583.2% | +3692.6% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5595.1 | 48458.8 | +766.9% | +760.8% | +790.8% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1734.5 | 49121.3 | +2712.6% | +2679.1% | +2743.3% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 6395.9 | 49121.3 | +667.8% | +664.1% | +670.3% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1474.2 | 49607.8 | +3268.0% | +3202.1% | +3353.4% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 6460.6 | 49607.8 | +667.9% | +660.6% | +683.4% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 7486.4 | 51845.6 | +590.7% | +586.8% | +600.2% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 12670.3 | 51845.6 | +311.0% | +305.0% | +312.9% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4407.9 | 49760.5 | +1029.3% | +1023.1% | +1068.4% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 7934.1 | 49760.5 | +529.5% | +523.1% | +543.9% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 18605.3 | 34352.0 | +84.5% | +83.3% | +85.0% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 14583.2 | 34352.0 | +135.1% | +133.8% | +136.4% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 9288.8 | 24207.4 | +160.7% | +159.0% | +166.0% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 3942.0 | 24207.4 | +516.5% | +504.5% | +524.7% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 10426.0 | 29332.0 | +181.3% | +179.7% | +182.9% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 9397.5 | 29332.0 | +211.9% | +209.4% | +213.0% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 11360.4 | 33978.5 | +199.1% | +196.0% | +199.9% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 14170.1 | 33978.5 | +139.8% | +136.7% | +141.2% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | strtr() | 3928.4 | 19631.2 | +399.7% | +389.3% | +412.1% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | preg_replace_callback() | 18738.4 | 19631.2 | +4.8% | +3.4% | +6.4% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | str_replace() | 13675.1 | 19631.2 | +43.5% | +41.3% | +45.7% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | strtr() | 5962.2 | 23046.9 | +287.2% | +276.5% | +292.0% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | preg_replace_callback() | 23795.2 | 23046.9 | -3.2% | -4.5% | -1.9% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | str_replace() | 17714.0 | 23046.9 | +29.9% | +28.6% | +31.6% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 1347.0 | 8799.3 | +552.6% | +551.7% | +617.2% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 8262.1 | 8799.3 | +6.7% | +5.5% | +14.8% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 5885.2 | 8799.3 | +49.7% | +49.0% | +62.8% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 8654.0 | 20351.7 | +135.7% | +134.5% | +136.8% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 20504.0 | 20351.7 | -0.5% | -2.2% | -0.4% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 12347.4 | 20351.7 | +64.7% | +62.1% | +66.2% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 751.6 | 6620.2 | +781.1% | +766.6% | +786.0% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 4860.4 | 6620.2 | +36.4% | +34.9% | +38.3% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 4360.5 | 6620.2 | +51.6% | +48.8% | +53.9% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 1220.1 | 7319.9 | +499.5% | +495.4% | +522.4% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 6788.0 | 7319.9 | +8.2% | +6.2% | +11.2% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 5160.5 | 7319.9 | +42.6% | +41.3% | +44.2% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | strtr() | 847.3 | 3425.9 | +304.8% | +297.0% | +307.5% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace_callback() | 4792.6 | 3425.9 | -28.4% | -29.8% | -27.9% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | str_replace() | 3535.2 | 3425.9 | -3.2% | -4.9% | -2.5% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace() | 3817.9 | 3425.9 | -10.3% | -10.6% | -9.8% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 1412.2 | 33532.5 | +2274.5% | +2256.6% | +2317.7% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 11630.1 | 33532.5 | +187.2% | +185.0% | +196.4% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 6474.5 | 33532.5 | +417.9% | +413.4% | +426.6% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 1803.1 | 34378.1 | +1807.2% | +1790.2% | +1878.5% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 12648.8 | 34378.1 | +171.6% | +170.3% | +186.1% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 7217.5 | 34378.1 | +377.9% | +375.3% | +396.0% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 12227.7 | 45458.0 | +272.4% | +268.8% | +274.6% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 22623.5 | 45458.0 | +100.9% | +98.7% | +103.4% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 16358.7 | 45458.0 | +178.4% | +176.9% | +180.4% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 24764.3 | 94155.4 | +280.1% | +278.0% | +284.0% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 27509.7 | 94155.4 | +243.7% | +235.3% | +244.7% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 69583.2 | 94155.4 | +35.4% | +31.8% | +36.1% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 26949.3 | 94155.4 | +249.3% | +245.9% | +250.6% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 25421.2 | 99765.0 | +292.4% | +291.9% | +332.6% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 28842.3 | 99765.0 | +246.9% | +243.6% | +284.1% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 72951.9 | 99765.0 | +36.7% | +36.4% | +52.0% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 27791.5 | 99765.0 | +259.1% | +257.1% | +298.6% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 38534.7 | 121169.9 | +213.9% | +212.3% | +218.1% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 30829.4 | 121169.9 | +292.7% | +291.4% | +295.5% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 105922.1 | 121169.9 | +14.5% | +13.7% | +14.9% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 29033.3 | 121169.9 | +317.1% | +313.3% | +319.2% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 305713.8 | 508073.7 | +66.2% | +65.8% | +66.7% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 46563.5 | 508073.7 | +990.9% | +970.0% | +996.1% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 665554.8 | 508073.7 | -23.6% | -23.8% | -23.4% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 44379.2 | 508073.7 | +1044.8% | +1041.9% | +1048.7% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 724.0 | 6477.9 | +795.8% | +782.2% | +803.5% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 9248.3 | 6477.9 | -30.0% | -30.5% | -29.1% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 7900.5 | 6477.9 | -18.0% | -18.4% | -17.0% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 898.6 | 6777.9 | +659.5% | +643.5% | +675.7% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 9926.2 | 6777.9 | -31.7% | -33.8% | -29.7% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 8148.0 | 6777.9 | -16.8% | -17.2% | -14.4% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 58704.0 | 146134.7 | +149.3% | +146.6% | +157.1% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | preg_match() per term | 98103.1 | 146134.7 | +48.6% | +48.0% | +53.0% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 50963.9 | 144898.1 | +185.0% | +180.9% | +186.0% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 134927.8 | 144898.1 | +7.0% | +4.7% | +10.1% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 71525.4 | 149463.8 | +109.3% | +107.3% | +110.3% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 213056.1 | 149463.8 | -29.9% | -30.2% | -29.3% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 135080.0 | 145178.8 | +7.5% | +7.2% | +8.5% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 154405.5 | 145178.8 | -5.9% | -7.0% | -5.1% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 1078230.5 | 195941.0 | -81.8% | -81.9% | -81.7% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 451005.6 | 195941.0 | -56.6% | -56.7% | -56.4% |

#### Dictionary already prepared

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1489.6 | 1067.0 | -28.5% | -29.7% | -28.2% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1151.3 | 1067.0 | -7.1% | -8.1% | -5.8% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1247.6 | 651.5 | -47.9% | -48.4% | -45.4% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 766.2 | 651.5 | -15.1% | -16.4% | -11.2% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1389.5 | 1421.7 | +2.3% | +1.0% | +3.1% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1412.9 | 1421.7 | +0.7% | -0.5% | +1.1% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1264.7 | 1553.6 | +22.7% | +22.3% | +24.6% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1476.6 | 1553.6 | +5.3% | +5.0% | +6.0% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4972.1 | 6159.9 | +23.9% | +22.8% | +26.5% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5414.2 | 6159.9 | +13.5% | +13.0% | +14.1% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 2786.7 | 2771.0 | -0.5% | -1.5% | +0.8% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2464.2 | 2771.0 | +12.6% | +12.3% | +12.8% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 6045.2 | 1547.4 | -74.3% | -74.5% | -73.9% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2432.1 | 1547.4 | -36.4% | -37.0% | -36.3% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 6759.8 | 775.2 | -88.5% | -88.7% | -88.2% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 792.8 | 775.2 | -1.4% | -2.9% | +0.1% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 9843.8 | 2133.2 | -78.3% | -78.4% | -78.1% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 3277.2 | 2133.2 | -34.9% | -35.0% | -34.8% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 6665.7 | 2113.4 | -68.4% | -68.8% | -68.3% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 3373.7 | 2113.4 | -37.4% | -37.7% | -36.9% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 16890.8 | 10595.7 | -37.3% | -38.9% | -37.1% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 18386.6 | 10595.7 | -42.4% | -42.5% | -42.2% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 9483.2 | 4545.6 | -52.1% | -52.2% | -51.7% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 7423.4 | 4545.6 | -38.8% | -39.1% | -38.4% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1558.8 | 807.6 | -48.2% | -48.9% | -48.0% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1298.5 | 807.6 | -37.6% | -38.2% | -37.0% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1324.3 | 653.8 | -50.7% | -51.2% | -50.4% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 744.3 | 653.8 | -12.2% | -12.6% | -10.4% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1720.4 | 1051.0 | -38.5% | -39.1% | -37.6% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1485.5 | 1051.0 | -29.3% | -29.5% | -28.7% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1465.5 | 1052.7 | -28.3% | -30.0% | -27.4% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1588.5 | 1052.7 | -33.1% | -34.3% | -32.7% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 7410.5 | 3489.7 | -52.7% | -53.1% | -52.5% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 7623.2 | 3489.7 | -54.2% | -54.6% | -54.0% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4400.5 | 1804.5 | -59.0% | -60.0% | -58.1% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2994.6 | 1804.5 | -39.6% | -41.8% | -39.4% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 20054.8 | 12266.6 | -38.8% | -39.0% | -38.7% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 12393.1 | 12266.6 | -1.0% | -1.2% | -0.8% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 10047.3 | 1138.3 | -88.7% | -88.7% | -88.7% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 1107.6 | 1138.3 | +2.6% | +1.4% | +2.8% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 11261.8 | 7064.9 | -37.3% | -39.5% | -37.2% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 6651.3 | 7064.9 | +6.3% | +5.4% | +6.6% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 12270.1 | 12228.9 | -0.2% | -0.5% | -0.0% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 11477.7 | 12228.9 | +6.5% | +6.2% | +7.0% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 1509.8 | 2495.4 | +65.2% | +63.8% | +67.4% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 2203.2 | 2495.4 | +13.1% | +6.2% | +14.8% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 1360.4 | 2495.4 | +83.8% | +82.1% | +84.3% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 9377.5 | 17176.2 | +82.6% | +79.8% | +84.0% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 14178.8 | 17176.2 | +21.4% | +20.6% | +22.3% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 7806.2 | 17176.2 | +119.6% | +118.2% | +121.5% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 888.4 | 1146.5 | +29.9% | +28.8% | +30.6% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 742.3 | 1146.5 | +54.7% | +52.5% | +56.4% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 836.1 | 1146.5 | +37.7% | +37.0% | +38.4% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 1314.8 | 1916.5 | +46.4% | +44.3% | +47.0% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 2509.3 | 1916.5 | -23.6% | -24.1% | -22.9% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 1483.0 | 1916.5 | +28.9% | +28.2% | +30.6% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | strtr() | 948.5 | 1081.0 | +14.2% | +13.1% | +14.8% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace_callback() | 1671.0 | 1081.0 | -35.1% | -35.6% | -34.9% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | str_replace() | 954.9 | 1081.0 | +13.3% | +12.8% | +14.0% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace() | 911.4 | 1081.0 | +18.9% | +17.3% | +19.4% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 1561.6 | 1361.0 | -12.7% | -15.3% | -10.5% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 853.8 | 1361.0 | +60.8% | +53.2% | +65.2% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 1114.1 | 1361.0 | +22.3% | +17.9% | +25.7% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 1929.3 | 2186.5 | +13.4% | +11.6% | +14.8% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 1767.2 | 2186.5 | +23.9% | +22.9% | +24.7% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 1709.5 | 2186.5 | +28.0% | +27.7% | +28.6% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 12857.2 | 14476.0 | +12.5% | +12.3% | +12.6% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 11014.6 | 14476.0 | +31.4% | +30.2% | +32.3% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 10548.5 | 14476.0 | +37.4% | +36.5% | +37.8% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 27163.3 | 48558.9 | +78.8% | +77.3% | +79.1% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 2218.6 | 48558.9 | +2089.8% | +2084.6% | +2092.6% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 53207.3 | 48558.9 | -8.7% | -8.8% | -8.7% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 2137.8 | 48558.9 | +2170.8% | +2170.4% | +2176.0% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 27879.2 | 52989.3 | +90.1% | +89.5% | +90.6% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 3346.7 | 52989.3 | +1485.3% | +1473.7% | +1487.1% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 56536.3 | 52989.3 | -6.3% | -6.3% | -6.1% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 2677.8 | 52989.3 | +1882.6% | +1874.3% | +1883.7% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 42032.1 | 82089.5 | +95.3% | +94.5% | +95.5% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 5231.5 | 82089.5 | +1468.9% | +1426.3% | +1476.8% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 92097.5 | 82089.5 | -10.9% | -10.9% | -10.8% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 3747.9 | 82089.5 | +2090.9% | +2077.8% | +2095.6% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 335016.4 | 638327.8 | +90.6% | +90.3% | +91.6% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 20984.9 | 638327.8 | +2941.6% | +2930.2% | +2978.8% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 692574.7 | 638327.8 | -7.8% | -8.2% | -7.8% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 18955.7 | 638327.8 | +3267.8% | +3259.6% | +3291.4% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 842.1 | 954.5 | +13.5% | +11.8% | +14.0% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 824.0 | 954.5 | +16.3% | +15.3% | +17.2% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 1001.0 | 954.5 | -4.4% | -5.2% | -4.1% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 1034.4 | 1233.0 | +18.8% | +18.1% | +21.4% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 1471.8 | 1233.0 | -16.2% | -17.3% | -14.7% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 1217.5 | 1233.0 | +1.3% | +0.4% | +2.2% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 57517.4 | 6876.6 | -88.0% | -88.1% | -87.4% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | preg_match() per term | 67820.5 | 6876.6 | -89.8% | -90.0% | -89.8% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 48846.2 | 4653.4 | -90.5% | -90.5% | -90.1% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 82595.2 | 4653.4 | -94.4% | -94.6% | -94.2% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 70453.4 | 8450.7 | -88.0% | -88.0% | -87.8% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 159758.0 | 8450.7 | -94.7% | -94.9% | -94.5% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 135504.0 | 6688.3 | -95.1% | -95.1% | -95.0% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 41731.3 | 6688.3 | -84.0% | -86.0% | -83.8% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 1080887.6 | 49944.6 | -95.4% | -95.4% | -95.4% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 329610.3 | 49944.6 | -84.8% | -84.9% | -84.8% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1531.3 | 1117.2 | -26.7% | -28.8% | -26.6% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1113.1 | 1117.2 | +0.6% | -0.5% | +1.5% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1233.3 | 631.1 | -48.8% | -50.0% | -47.9% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 680.8 | 631.1 | -7.4% | -8.6% | -5.6% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1382.4 | 1480.4 | +7.1% | +6.5% | +8.3% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1383.6 | 1480.4 | +6.9% | +6.4% | +7.4% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1241.4 | 1645.3 | +32.5% | +31.1% | +33.4% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1440.2 | 1645.3 | +14.1% | +13.7% | +14.7% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4978.8 | 6929.2 | +39.2% | +38.3% | +39.4% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 6200.7 | 6929.2 | +11.7% | +11.2% | +12.8% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 2739.2 | 3040.6 | +11.0% | +0.4% | +11.5% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2554.5 | 3040.6 | +18.9% | +18.0% | +19.5% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 6102.8 | 1639.0 | -73.2% | -73.2% | -72.8% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2394.0 | 1639.0 | -31.5% | -31.7% | -31.1% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 6876.6 | 757.5 | -89.0% | -89.0% | -88.8% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 689.0 | 757.5 | +9.6% | +9.1% | +10.6% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 9975.7 | 2256.9 | -77.4% | -77.5% | -77.1% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 3273.3 | 2256.9 | -31.0% | -31.7% | -30.5% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 6847.3 | 2255.2 | -67.1% | -67.6% | -67.0% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 3313.9 | 2255.2 | -31.9% | -32.3% | -31.7% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 15936.2 | 11805.1 | -25.9% | -26.1% | -25.8% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 18669.4 | 11805.1 | -36.8% | -37.3% | -36.6% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 9011.0 | 4871.1 | -46.0% | -46.2% | -45.8% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 7495.8 | 4871.1 | -35.0% | -35.3% | -34.6% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1624.2 | 754.4 | -53.6% | -54.3% | -53.2% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1260.0 | 754.4 | -40.0% | -40.6% | -39.7% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1333.5 | 630.6 | -52.6% | -53.0% | -52.1% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 673.7 | 630.6 | -6.0% | -9.1% | -5.9% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1749.8 | 1021.3 | -41.4% | -41.7% | -41.0% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1457.2 | 1021.3 | -30.0% | -30.3% | -29.1% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1463.4 | 1031.6 | -29.5% | -29.8% | -29.4% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1546.2 | 1031.6 | -33.2% | -33.5% | -31.8% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 7491.7 | 3430.8 | -54.2% | -54.4% | -53.9% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 7784.7 | 3430.8 | -56.0% | -56.1% | -55.6% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4415.6 | 1779.4 | -59.5% | -59.8% | -58.9% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 3028.8 | 1779.4 | -41.0% | -41.7% | -40.6% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 18609.4 | 10996.7 | -40.9% | -41.3% | -40.5% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 11679.0 | 10996.7 | -5.9% | -6.5% | -5.3% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 9290.8 | 975.5 | -89.5% | -89.7% | -89.4% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 1020.4 | 975.5 | -4.7% | -5.8% | -3.4% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 10422.7 | 6081.3 | -41.6% | -41.7% | -41.6% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 6446.4 | 6081.3 | -5.7% | -7.2% | -5.4% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 11360.6 | 10525.5 | -7.4% | -7.5% | -7.3% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 11223.9 | 10525.5 | -6.2% | -6.7% | -5.5% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 1341.7 | 1984.0 | +47.9% | +47.4% | +50.2% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 2219.9 | 1984.0 | -10.5% | -11.2% | -7.4% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 1314.4 | 1984.0 | +51.0% | +49.8% | +54.2% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 8578.3 | 13409.8 | +55.7% | +54.1% | +57.5% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 14204.9 | 13409.8 | -5.9% | -16.5% | -5.2% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 7629.6 | 13409.8 | +74.6% | +73.3% | +76.6% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 753.3 | 767.5 | +1.9% | +0.8% | +3.0% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 725.9 | 767.5 | +6.0% | +5.4% | +7.9% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 765.0 | 767.5 | +0.5% | -0.6% | +2.4% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 1218.7 | 1399.1 | +14.6% | +13.1% | +16.0% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 2489.1 | 1399.1 | -44.3% | -45.1% | -43.0% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 1443.6 | 1399.1 | -3.0% | -4.1% | -3.0% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | strtr() | 846.4 | 831.8 | -1.7% | -2.1% | -1.4% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace_callback() | 1633.5 | 831.8 | -49.2% | -49.3% | -48.6% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | str_replace() | 906.6 | 831.8 | -8.0% | -9.9% | -7.6% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace() | 881.2 | 831.8 | -5.3% | -6.7% | -2.5% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 1416.5 | 1132.7 | -20.0% | -21.9% | -19.6% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 822.9 | 1132.7 | +37.7% | +33.7% | +40.2% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 1087.9 | 1132.7 | +3.9% | +1.7% | +4.5% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 1813.2 | 1860.6 | +2.8% | +1.7% | +3.5% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 1761.0 | 1860.6 | +5.7% | +3.3% | +6.6% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 1706.3 | 1860.6 | +9.2% | +7.7% | +9.8% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 12274.1 | 12399.8 | +0.6% | -1.0% | +1.7% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 11488.6 | 12399.8 | +8.0% | +6.7% | +8.3% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 10672.3 | 12399.8 | +16.3% | +12.9% | +16.7% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 24675.9 | 30073.9 | +21.7% | +20.6% | +22.7% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 2166.3 | 30073.9 | +1284.9% | +1278.6% | +1294.9% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 49170.2 | 30073.9 | -38.8% | -39.3% | -38.7% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 2055.6 | 30073.9 | +1363.0% | +1351.8% | +1370.5% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 25459.1 | 36248.8 | +41.8% | +41.5% | +43.6% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 3283.6 | 36248.8 | +1001.0% | +988.6% | +1016.6% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 52371.5 | 36248.8 | -30.7% | -31.2% | -30.3% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 2610.4 | 36248.8 | +1290.7% | +1249.7% | +1298.9% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 38571.1 | 57259.8 | +48.7% | +47.5% | +50.6% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 5322.8 | 57259.8 | +974.7% | +966.2% | +988.8% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 85429.1 | 57259.8 | -33.0% | -33.4% | -32.3% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 3729.9 | 57259.8 | +1435.0% | +1421.7% | +1454.0% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 305279.5 | 442287.2 | +44.8% | +44.2% | +46.0% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 21106.3 | 442287.2 | +2004.9% | +1969.8% | +2009.5% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 644190.1 | 442287.2 | -31.4% | -31.8% | -30.8% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 19231.5 | 442287.2 | +2219.3% | +2176.0% | +2235.5% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 735.0 | 689.0 | -6.0% | -8.2% | -3.6% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 792.1 | 689.0 | -12.8% | -14.2% | -10.6% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 921.1 | 689.0 | -25.2% | -26.0% | -23.1% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 905.2 | 933.9 | +2.9% | +0.0% | +3.9% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 1445.0 | 933.9 | -35.1% | -36.2% | -34.7% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 1153.3 | 933.9 | -19.2% | -20.1% | -18.4% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 58899.0 | 7038.5 | -88.0% | -88.2% | -87.9% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | preg_match() per term | 68024.8 | 7038.5 | -89.6% | -89.9% | -89.5% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 50879.4 | 4969.5 | -90.2% | -90.8% | -90.2% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 81474.9 | 4969.5 | -93.9% | -94.2% | -93.8% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 71303.3 | 9195.4 | -87.1% | -87.2% | -86.5% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 161778.4 | 9195.4 | -94.3% | -94.4% | -93.9% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 135221.7 | 6726.1 | -95.0% | -95.0% | -95.0% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 42641.0 | 6726.1 | -84.2% | -84.3% | -84.2% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 1078780.7 | 51112.3 | -95.3% | -95.3% | -95.3% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 337323.9 | 51112.3 | -84.9% | -84.9% | -84.8% |

### Synthetic tasks

#### Dictionary preparation included

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 1722.7 | 399709.3 | +23070.1% | +22539.4% | +23164.0% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 85256.3 | 399709.3 | +369.2% | +365.1% | +370.2% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 83794.6 | 399709.3 | +377.2% | +372.0% | +378.0% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 1394.6 | 80654.9 | +5689.6% | +5608.1% | +5725.3% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 83427.8 | 80654.9 | -3.3% | -3.6% | -3.1% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 82523.7 | 80654.9 | -2.2% | -3.4% | -1.6% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | strtr() | 1384.6 | 6162.2 | +345.0% | +344.0% | +353.6% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace_callback() | 22161.7 | 6162.2 | -72.2% | -72.3% | -71.9% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace() | 18422.5 | 6162.2 | -66.4% | -67.1% | -66.0% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | strtr() | 1140.4 | 4765.3 | +316.6% | +314.4% | +320.1% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | preg_replace_callback() | 6258.5 | 4765.3 | -23.9% | -24.8% | -23.3% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 1675.1 | 380602.3 | +22625.2% | +22349.9% | +22786.7% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 93568.2 | 380602.3 | +306.8% | +298.7% | +318.3% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 93085.4 | 380602.3 | +310.1% | +304.3% | +319.8% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 1339.1 | 74364.9 | +5453.2% | +5263.7% | +5491.2% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 94986.2 | 74364.9 | -21.5% | -22.4% | -20.3% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 94078.7 | 74364.9 | -20.8% | -23.3% | -19.1% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | strtr() | 1265.3 | 6088.1 | +381.4% | +378.7% | +382.1% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace_callback() | 22921.1 | 6088.1 | -73.5% | -73.6% | -73.3% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace() | 18667.7 | 6088.1 | -67.5% | -67.6% | -67.3% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | strtr() | 1035.3 | 4566.1 | +338.8% | +337.4% | +348.1% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | preg_replace_callback() | 5832.1 | 4566.1 | -22.0% | -22.2% | -20.6% |

#### Dictionary already prepared

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 1742.1 | 2086.0 | +19.1% | +17.5% | +22.0% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 4065.8 | 2086.0 | -48.6% | -50.0% | -48.0% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 2986.1 | 2086.0 | -30.5% | -31.4% | -29.6% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 1418.3 | 2056.9 | +45.7% | +43.0% | +46.8% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 2965.5 | 2056.9 | -30.6% | -31.1% | -29.3% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 2030.8 | 2056.9 | +1.2% | +0.9% | +11.5% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | strtr() | 1397.0 | 2140.1 | +53.2% | +52.6% | +61.5% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace_callback() | 4843.9 | 2140.1 | -55.4% | -56.2% | -53.5% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace() | 1527.4 | 2140.1 | +39.8% | +33.0% | +53.9% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | strtr() | 1148.6 | 1071.1 | -6.8% | -7.1% | -5.3% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | preg_replace_callback() | 2635.9 | 1071.1 | -59.4% | -60.6% | -58.8% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 1659.3 | 1840.5 | +10.9% | +9.5% | +12.3% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 3980.5 | 1840.5 | -53.5% | -54.9% | -53.2% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 2909.1 | 1840.5 | -36.0% | -38.0% | -35.1% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 1310.3 | 1822.9 | +38.3% | +36.0% | +39.8% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 3075.3 | 1822.9 | -40.9% | -41.2% | -38.9% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 1807.0 | 1822.9 | +0.3% | -2.4% | +3.3% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | strtr() | 1270.2 | 2267.9 | +78.5% | +77.4% | +80.8% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace_callback() | 5379.0 | 2267.9 | -57.8% | -58.0% | -57.1% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace() | 1458.5 | 2267.9 | +55.8% | +42.9% | +57.5% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | strtr() | 1030.7 | 876.6 | -14.9% | -15.2% | -13.2% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | preg_replace_callback() | 2628.8 | 876.6 | -66.4% | -67.1% | -65.9% |

## Size series

### Product tasks

#### Dictionary preparation included

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 1238.8 | 10910.9 | +783.3% | +774.1% | +785.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 3250.7 | 10910.9 | +235.1% | +232.9% | +236.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | str_contains() loop | 902.0 | 10724.5 | +1088.9% | +1074.5% | +1190.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | preg_match() | 2889.9 | 10724.5 | +271.5% | +264.6% | +306.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | str_contains() loop | 1066.7 | 11021.6 | +932.4% | +913.3% | +941.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | preg_match() | 3420.8 | 11021.6 | +220.9% | +219.3% | +227.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | str_contains() loop | 957.4 | 11121.5 | +1063.6% | +1050.4% | +1171.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | preg_match() | 3411.0 | 11121.5 | +227.7% | +222.0% | +261.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 4385.5 | 13733.4 | +212.7% | +211.8% | +214.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 7031.4 | 13733.4 | +95.4% | +93.3% | +96.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | str_contains() loop | 1752.6 | 11723.6 | +571.0% | +558.9% | +588.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | preg_match() | 4448.1 | 11723.6 | +165.0% | +161.3% | +174.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 1900.0 | 23644.4 | +1137.8% | +1116.6% | +1146.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 5713.4 | 23644.4 | +313.5% | +311.0% | +315.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | str_contains() loop | 1221.5 | 23364.2 | +1812.0% | +1807.8% | +1853.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | preg_match() | 4798.2 | 23364.2 | +386.3% | +383.6% | +402.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | str_contains() loop | 1475.2 | 23891.8 | +1519.6% | +1502.8% | +1568.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | preg_match() | 5986.2 | 23891.8 | +299.1% | +295.0% | +303.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | str_contains() loop | 1299.8 | 23910.8 | +1743.2% | +1709.8% | +1781.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | preg_match() | 6082.8 | 23910.8 | +292.2% | +290.6% | +295.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 7396.0 | 26302.3 | +255.6% | +254.2% | +265.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 15994.0 | 26302.3 | +64.5% | +64.3% | +66.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | str_contains() loop | 2590.8 | 24606.3 | +845.2% | +840.6% | +855.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | preg_match() | 8047.5 | 24606.3 | +203.5% | +202.8% | +205.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 3453.9 | 58629.8 | +1591.9% | +1584.2% | +1659.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 11544.3 | 58629.8 | +407.8% | +405.4% | +410.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | str_contains() loop | 2075.2 | 58296.3 | +2709.3% | +2443.6% | +2764.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | preg_match() | 8822.6 | 58296.3 | +558.5% | +549.7% | +564.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | str_contains() loop | 2572.3 | 58462.0 | +2167.0% | +2123.3% | +2191.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | preg_match() | 12461.9 | 58462.0 | +369.4% | +366.5% | +372.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | str_contains() loop | 2113.6 | 58699.0 | +2677.2% | +2654.6% | +2750.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | preg_match() | 12555.8 | 58699.0 | +368.7% | +363.9% | +376.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 16244.3 | 63415.0 | +290.3% | +279.0% | +294.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 38342.4 | 63415.0 | +65.7% | +65.2% | +67.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | str_contains() loop | 6207.3 | 60771.0 | +871.8% | +839.3% | +922.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | preg_match() | 19221.9 | 60771.0 | +214.9% | +209.8% | +223.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 6204.3 | 121172.3 | +1826.3% | +1786.5% | +1888.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 22253.3 | 121172.3 | +446.6% | +435.8% | +448.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | str_contains() loop | 3784.2 | 119896.2 | +3049.6% | +3039.0% | +3133.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | preg_match() | 16243.1 | 119896.2 | +638.6% | +633.4% | +641.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | str_contains() loop | 4947.5 | 120894.9 | +2362.4% | +2289.1% | +2367.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | preg_match() | 23785.2 | 120894.9 | +408.9% | +405.9% | +412.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | str_contains() loop | 3908.3 | 120928.9 | +2996.5% | +2906.2% | +3019.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | preg_match() | 24564.8 | 120928.9 | +389.6% | +388.3% | +396.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 33074.7 | 126117.4 | +281.5% | +278.2% | +297.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 77641.6 | 126117.4 | +62.4% | +61.9% | +63.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | str_contains() loop | 13015.3 | 123201.0 | +836.4% | +812.3% | +876.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | preg_match() | 38777.7 | 123201.0 | +217.1% | +214.2% | +226.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 12874.1 | 271025.7 | +2011.0% | +1929.9% | +2117.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 44870.3 | 271025.7 | +504.0% | +497.5% | +516.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | str_contains() loop | 7082.2 | 268677.9 | +3684.4% | +3549.9% | +3828.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | preg_match() | 31877.2 | 268677.9 | +746.9% | +738.9% | +759.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | str_contains() loop | 9639.7 | 268716.4 | +2713.5% | +2655.2% | +2796.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | preg_match() | 47570.9 | 268716.4 | +467.8% | +461.9% | +470.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | str_contains() loop | 7527.6 | 269819.1 | +3501.1% | +3427.3% | +3601.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | preg_match() | 49022.1 | 269819.1 | +452.5% | +445.0% | +453.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 64787.5 | 277785.7 | +328.5% | +327.7% | +330.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 158954.6 | 277785.7 | +74.7% | +62.5% | +75.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | str_contains() loop | 26213.8 | 273154.7 | +945.7% | +931.2% | +986.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | preg_match() | 78267.4 | 273154.7 | +249.3% | +247.5% | +251.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 30569.0 | 707508.6 | +2214.5% | +2088.7% | +2257.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 90078.3 | 707508.6 | +686.7% | +680.8% | +688.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | str_contains() loop | 15017.8 | 706853.4 | +4606.8% | +4263.0% | +4634.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | preg_match() | 63050.0 | 706853.4 | +1021.7% | +1016.1% | +1026.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | str_contains() loop | 20281.1 | 707553.8 | +3388.7% | +3127.9% | +3494.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | preg_match() | 95019.7 | 707553.8 | +644.8% | +636.5% | +661.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | str_contains() loop | 15529.9 | 707650.2 | +4465.9% | +4149.4% | +4594.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | preg_match() | 98100.5 | 707650.2 | +622.1% | +615.0% | +625.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 138946.4 | 714198.5 | +414.0% | +390.7% | +437.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 313884.9 | 714198.5 | +127.7% | +126.6% | +137.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | str_contains() loop | 53136.8 | 707909.0 | +1232.2% | +1175.5% | +1238.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | preg_match() | 155013.8 | 707909.0 | +356.9% | +355.2% | +358.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 75356.4 | 1367180.4 | +1714.3% | +1694.8% | +1736.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 231118.6 | 1367180.4 | +491.5% | +473.3% | +519.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | str_contains() loop | 39195.2 | 1368328.1 | +3377.5% | +3326.4% | +3424.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | preg_match() | 124931.5 | 1368328.1 | +996.1% | +979.4% | +1012.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | str_contains() loop | 53358.8 | 1368546.7 | +2461.0% | +2370.3% | +2482.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | preg_match() | 252818.9 | 1368546.7 | +447.4% | +423.3% | +453.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | str_contains() loop | 39791.4 | 1367354.7 | +3335.4% | +3171.6% | +3386.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | preg_match() | 258273.5 | 1367354.7 | +429.9% | +413.8% | +436.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 317129.5 | 1368356.3 | +330.6% | +320.9% | +332.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 1118223.0 | 1368356.3 | +22.2% | +15.8% | +35.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | str_contains() loop | 116154.9 | 1363303.1 | +1074.4% | +1023.2% | +1083.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | preg_match() | 504875.5 | 1363303.1 | +169.8% | +157.6% | +182.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 5412.6 | 14329.3 | +164.5% | +157.2% | +174.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | preg_match() per term | 9741.5 | 14329.3 | +46.8% | +45.8% | +51.1% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 4452.7 | 13904.7 | +211.5% | +208.8% | +216.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 10795.4 | 13904.7 | +28.6% | +28.3% | +29.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 6721.5 | 14418.1 | +114.5% | +112.2% | +118.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 17058.5 | 14418.1 | -15.5% | -16.1% | -14.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 10003.0 | 23355.2 | +134.3% | +131.1% | +141.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | preg_match() per term | 17980.2 | 23355.2 | +29.6% | +29.0% | +33.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 8513.1 | 22442.9 | +163.6% | +161.4% | +175.2% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 20382.4 | 22442.9 | +10.9% | +9.2% | +13.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 12619.5 | 23634.1 | +89.6% | +85.0% | +92.0% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 31728.6 | 23634.1 | -25.6% | -26.3% | -24.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 17870.1 | 42699.5 | +138.6% | +135.2% | +140.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | preg_match() per term | 34882.8 | 42699.5 | +22.8% | +21.4% | +23.9% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 15105.6 | 41369.9 | +176.9% | +167.5% | +180.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 38321.6 | 41369.9 | +8.4% | +6.7% | +9.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 23023.3 | 43345.6 | +88.9% | +81.3% | +92.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 59889.4 | 43345.6 | -27.8% | -28.2% | -26.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 36298.0 | 90666.7 | +149.5% | +140.5% | +153.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | preg_match() per term | 66528.5 | 90666.7 | +36.5% | +35.8% | +37.2% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 31186.7 | 89097.5 | +185.2% | +184.7% | +187.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 75734.2 | 89097.5 | +17.5% | +17.0% | +18.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 45778.9 | 91771.5 | +100.7% | +95.5% | +101.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 113488.1 | 91771.5 | -19.3% | -19.4% | -18.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 75303.5 | 218633.6 | +190.0% | +188.1% | +205.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | preg_match() per term | 131553.6 | 218633.6 | +67.0% | +63.8% | +69.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 64970.6 | 215245.5 | +229.9% | +221.5% | +236.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 228881.9 | 215245.5 | -5.7% | -6.6% | -5.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 88587.8 | 220952.2 | +149.4% | +145.5% | +150.3% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 303209.2 | 220952.2 | -26.9% | -28.2% | -26.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 148466.8 | 623350.3 | +319.5% | +309.9% | +322.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | preg_match() per term | 278811.2 | 623350.3 | +124.6% | +122.6% | +127.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 141476.4 | 615323.2 | +334.4% | +327.7% | +335.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 521760.9 | 615323.2 | +18.1% | +17.6% | +18.6% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 164552.3 | 623595.4 | +278.1% | +267.5% | +279.6% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 627909.9 | 623595.4 | -0.7% | -1.1% | -0.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 290576.6 | 1631420.4 | +461.3% | +459.9% | +470.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | preg_match() per term | 622385.3 | 1631420.4 | +162.1% | +161.1% | +162.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 286163.5 | 1633541.7 | +470.4% | +468.9% | +478.6% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 1102133.9 | 1633541.7 | +48.1% | +48.0% | +48.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 310568.8 | 1637564.8 | +426.5% | +421.3% | +439.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 1269879.5 | 1637564.8 | +29.5% | +28.4% | +31.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 20753.2 | 16380.9 | -21.1% | -21.3% | -20.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 10202.8 | 16380.9 | +60.4% | +59.2% | +61.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 162407.2 | 50763.8 | -68.6% | -69.1% | -68.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 29722.4 | 50763.8 | +70.8% | +70.2% | +72.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 36865.1 | 28092.7 | -23.8% | -24.0% | -23.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 23678.2 | 28092.7 | +18.8% | +17.6% | +19.1% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 292914.4 | 64911.9 | -77.8% | -77.9% | -77.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 84609.0 | 64911.9 | -23.3% | -23.8% | -22.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 77841.3 | 49196.9 | -36.8% | -37.2% | -35.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 48543.1 | 49196.9 | +1.6% | +0.3% | +3.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 621404.1 | 88812.6 | -85.7% | -85.9% | -85.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 167844.9 | 88812.6 | -47.3% | -47.7% | -46.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 143451.3 | 91736.8 | -36.0% | -36.5% | -33.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 104259.4 | 91736.8 | -12.0% | -15.4% | -8.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 1144144.5 | 135057.0 | -88.2% | -88.2% | -87.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 324276.6 | 135057.0 | -58.4% | -58.5% | -56.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 175137.8 | 210989.2 | +20.5% | +19.8% | +24.4% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 213505.5 | 210989.2 | -1.0% | -3.2% | +2.0% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 1398395.7 | 273032.1 | -80.5% | -80.7% | -80.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 563036.6 | 273032.1 | -51.7% | -52.0% | -51.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 191621.3 | 529899.5 | +176.3% | +175.3% | +177.4% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 501876.1 | 529899.5 | +5.4% | +1.8% | +6.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 1529557.4 | 605674.6 | -60.4% | -60.5% | -60.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 1232614.1 | 605674.6 | -50.7% | -51.3% | -50.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 196034.6 | 1362596.4 | +595.4% | +589.6% | +596.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 1233907.8 | 1362596.4 | +10.1% | +7.3% | +13.3% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 1565617.9 | 1438086.9 | -8.1% | -8.4% | -7.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 3428196.5 | 1438086.9 | -57.9% | -59.3% | -57.7% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 1250.2 | 10941.5 | +775.1% | +764.2% | +827.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 3079.6 | 10941.5 | +253.7% | +252.5% | +278.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | str_contains() loop | 883.9 | 10675.1 | +1108.2% | +1095.7% | +1114.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | preg_match() | 2733.6 | 10675.1 | +289.1% | +285.1% | +293.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | str_contains() loop | 1051.3 | 11012.9 | +954.5% | +947.2% | +970.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | preg_match() | 3277.5 | 11012.9 | +237.3% | +226.0% | +244.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | str_contains() loop | 943.1 | 11074.4 | +1074.2% | +1062.2% | +1086.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | preg_match() | 3229.8 | 11074.4 | +242.5% | +240.1% | +243.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 4403.6 | 13524.0 | +208.5% | +205.1% | +216.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 6696.5 | 13524.0 | +101.9% | +100.8% | +107.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | str_contains() loop | 1764.2 | 11553.9 | +560.2% | +543.3% | +614.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | preg_match() | 4192.3 | 11553.9 | +176.3% | +171.5% | +200.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 2009.3 | 22955.3 | +1065.0% | +1029.8% | +1070.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 5651.7 | 22955.3 | +306.3% | +302.2% | +323.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | str_contains() loop | 1236.0 | 22856.7 | +1749.2% | +1719.0% | +1757.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | preg_match() | 4835.8 | 22856.7 | +372.7% | +365.7% | +378.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | str_contains() loop | 1503.3 | 22959.8 | +1429.2% | +1416.4% | +1456.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | preg_match() | 5885.1 | 22959.8 | +291.4% | +288.0% | +294.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | str_contains() loop | 1307.5 | 23005.8 | +1667.1% | +1623.5% | +1700.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | preg_match() | 5976.3 | 23005.8 | +285.1% | +283.4% | +296.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 7509.0 | 25636.5 | +242.2% | +237.1% | +245.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 15655.2 | 25636.5 | +64.1% | +62.4% | +65.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | str_contains() loop | 2564.5 | 23739.7 | +827.7% | +818.0% | +843.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | preg_match() | 7868.5 | 23739.7 | +200.4% | +190.7% | +204.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 3610.6 | 56568.3 | +1464.6% | +1423.8% | +1474.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 11733.2 | 56568.3 | +381.6% | +378.1% | +383.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | str_contains() loop | 2154.9 | 55798.9 | +2486.4% | +2431.9% | +2533.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | preg_match() | 9091.7 | 55798.9 | +513.7% | +494.1% | +525.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | str_contains() loop | 2713.7 | 56466.3 | +1962.0% | +1674.5% | +2021.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | preg_match() | 12585.8 | 56466.3 | +351.1% | +344.1% | +356.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | str_contains() loop | 2238.6 | 57297.5 | +2487.0% | +2439.9% | +2565.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | preg_match() | 12747.7 | 57297.5 | +350.4% | +345.9% | +369.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 16852.4 | 62415.8 | +270.4% | +269.2% | +272.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 37997.7 | 62415.8 | +64.1% | +64.0% | +65.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | str_contains() loop | 6228.2 | 58108.9 | +837.8% | +827.2% | +867.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | preg_match() | 19243.9 | 58108.9 | +202.0% | +199.9% | +212.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 6855.3 | 117009.5 | +1603.4% | +1590.8% | +1619.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 22914.0 | 117009.5 | +410.6% | +401.7% | +413.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | str_contains() loop | 4015.5 | 116579.1 | +2793.7% | +2717.0% | +2808.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | preg_match() | 16733.3 | 116579.1 | +596.3% | +590.1% | +597.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | str_contains() loop | 5270.4 | 117665.5 | +2132.6% | +2104.1% | +2160.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | preg_match() | 24641.4 | 117665.5 | +378.6% | +366.4% | +379.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | str_contains() loop | 4206.3 | 117243.9 | +2689.6% | +2643.9% | +2698.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | preg_match() | 25325.0 | 117243.9 | +362.5% | +356.7% | +367.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 33445.3 | 124428.9 | +273.9% | +267.8% | +287.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 80490.9 | 124428.9 | +54.3% | +53.2% | +61.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | str_contains() loop | 13441.9 | 119267.5 | +786.3% | +781.9% | +793.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | preg_match() | 39879.6 | 119267.5 | +199.9% | +194.0% | +200.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 14238.7 | 259492.9 | +1722.4% | +1713.0% | +1740.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 45535.4 | 259492.9 | +469.9% | +463.3% | +479.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | str_contains() loop | 7791.0 | 259783.7 | +3241.6% | +3178.3% | +3252.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | preg_match() | 32835.0 | 259783.7 | +694.3% | +679.0% | +702.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | str_contains() loop | 10165.0 | 260508.2 | +2466.9% | +2428.9% | +2557.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | preg_match() | 47810.7 | 260508.2 | +445.2% | +429.0% | +450.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | str_contains() loop | 8002.3 | 260751.9 | +3162.1% | +3130.0% | +3173.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | preg_match() | 49278.9 | 260751.9 | +430.8% | +425.3% | +432.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 65947.3 | 269012.1 | +309.6% | +305.1% | +311.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 153939.3 | 269012.1 | +75.0% | +73.2% | +75.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | str_contains() loop | 26346.2 | 265187.5 | +903.1% | +902.0% | +920.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | preg_match() | 76855.2 | 265187.5 | +245.6% | +242.1% | +251.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 35420.4 | 694229.6 | +1857.2% | +1846.7% | +1886.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 92004.4 | 694229.6 | +653.6% | +618.3% | +668.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | str_contains() loop | 17207.5 | 694827.8 | +3948.5% | +3919.1% | +3959.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | preg_match() | 64040.4 | 694827.8 | +985.9% | +976.1% | +995.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | str_contains() loop | 23207.2 | 695200.0 | +2902.1% | +2891.8% | +2931.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | preg_match() | 95625.7 | 695200.0 | +626.2% | +570.0% | +640.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | str_contains() loop | 17599.6 | 700314.9 | +3866.6% | +3807.3% | +3921.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | preg_match() | 100230.6 | 700314.9 | +599.2% | +552.1% | +610.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 149509.7 | 704045.0 | +370.9% | +358.1% | +375.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 311081.1 | 704045.0 | +126.4% | +113.1% | +129.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | str_contains() loop | 55641.6 | 697770.1 | +1151.2% | +1140.7% | +1162.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | preg_match() | 154705.4 | 697770.1 | +351.4% | +315.3% | +355.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 80209.1 | 1358598.4 | +1603.8% | +1585.3% | +1617.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 226858.4 | 1358598.4 | +497.8% | +492.2% | +520.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | str_contains() loop | 43185.7 | 1357178.0 | +3038.8% | +3026.7% | +3071.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | preg_match() | 129340.9 | 1357178.0 | +949.3% | +942.7% | +958.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | str_contains() loop | 58660.1 | 1358928.9 | +2215.5% | +2211.1% | +2226.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | preg_match() | 251389.3 | 1358928.9 | +443.4% | +420.6% | +459.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | str_contains() loop | 43666.8 | 1360273.2 | +3022.5% | +3002.3% | +3032.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | preg_match() | 261435.7 | 1360273.2 | +420.0% | +410.4% | +431.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 334809.3 | 1359531.4 | +306.3% | +305.0% | +307.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 1080335.8 | 1359531.4 | +25.7% | +19.0% | +27.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | str_contains() loop | 123741.1 | 1351731.7 | +998.2% | +982.2% | +1007.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | preg_match() | 501538.5 | 1351731.7 | +169.5% | +155.0% | +178.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 5422.2 | 13800.0 | +154.7% | +154.2% | +157.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | preg_match() per term | 9145.8 | 13800.0 | +50.3% | +47.4% | +52.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 4491.6 | 13326.1 | +196.7% | +193.4% | +198.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 10287.1 | 13326.1 | +29.4% | +29.2% | +29.6% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 6671.3 | 14782.9 | +121.8% | +120.7% | +133.8% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 16414.0 | 14782.9 | -9.7% | -10.4% | -5.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 10244.7 | 22237.9 | +117.3% | +115.9% | +122.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | preg_match() per term | 16992.4 | 22237.9 | +30.3% | +28.7% | +33.2% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 8642.1 | 21924.7 | +153.7% | +149.3% | +158.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 19691.0 | 21924.7 | +10.9% | +10.0% | +11.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 12705.0 | 23490.7 | +85.7% | +83.3% | +89.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 30663.2 | 23490.7 | -23.2% | -24.3% | -22.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 18659.3 | 40476.8 | +117.5% | +116.0% | +118.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | preg_match() per term | 33329.9 | 40476.8 | +21.3% | +20.6% | +23.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 15793.0 | 39795.9 | +151.0% | +149.6% | +153.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 37388.1 | 39795.9 | +7.1% | +5.0% | +7.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 23906.7 | 42117.3 | +76.3% | +73.7% | +77.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 57791.5 | 42117.3 | -27.3% | -28.1% | -26.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 38588.8 | 87745.2 | +127.2% | +126.4% | +139.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | preg_match() per term | 65167.3 | 87745.2 | +35.4% | +31.3% | +40.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 33839.6 | 85852.0 | +154.2% | +153.3% | +157.6% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 74395.0 | 85852.0 | +15.4% | +13.7% | +16.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 48089.6 | 89189.3 | +86.4% | +82.3% | +90.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 111067.7 | 89189.3 | -19.6% | -20.7% | -18.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 76826.3 | 207463.7 | +170.5% | +167.7% | +175.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | preg_match() per term | 126947.2 | 207463.7 | +63.7% | +58.7% | +64.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 68939.7 | 207317.9 | +199.3% | +194.9% | +208.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 222540.0 | 207317.9 | -8.0% | -8.3% | -6.6% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 91348.2 | 213370.1 | +132.9% | +129.8% | +135.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 294318.5 | 213370.1 | -27.9% | -28.5% | -26.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 152705.9 | 597863.9 | +290.8% | +290.0% | +294.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | preg_match() per term | 268981.7 | 597863.9 | +121.8% | +120.0% | +123.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 145285.8 | 591311.3 | +307.0% | +304.7% | +307.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 513276.1 | 591311.3 | +15.3% | +14.7% | +16.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 168206.7 | 599280.8 | +256.4% | +255.3% | +256.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 615420.6 | 599280.8 | -2.5% | -11.1% | -1.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 293846.4 | 1604431.1 | +446.6% | +444.8% | +449.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | preg_match() per term | 601117.0 | 1604431.1 | +166.8% | +164.5% | +169.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 290550.8 | 1608794.7 | +453.0% | +451.9% | +459.2% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 1077652.7 | 1608794.7 | +49.5% | +48.7% | +50.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 313848.4 | 1609045.9 | +411.3% | +397.6% | +416.6% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 1242180.0 | 1609045.9 | +29.8% | +23.6% | +31.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 19858.8 | 15859.6 | -20.1% | -22.1% | -19.6% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 9892.0 | 15859.6 | +60.1% | +59.8% | +61.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 157212.2 | 48430.4 | -69.1% | -69.7% | -68.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 29416.0 | 48430.4 | +64.6% | +63.8% | +67.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 36174.0 | 27078.9 | -24.9% | -25.1% | -23.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 23166.1 | 27078.9 | +17.4% | +16.2% | +18.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 289765.0 | 63105.0 | -78.2% | -78.3% | -77.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 83601.5 | 63105.0 | -24.7% | -26.1% | -23.6% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 77334.9 | 46709.6 | -39.6% | -39.8% | -38.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 47342.6 | 46709.6 | -1.6% | -2.2% | -0.3% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 616446.9 | 86629.6 | -85.9% | -86.1% | -85.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 167358.6 | 86629.6 | -48.2% | -48.9% | -47.6% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 144232.4 | 89142.4 | -38.1% | -39.0% | -37.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 102003.5 | 89142.4 | -12.5% | -13.6% | -11.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 1149581.5 | 133714.6 | -88.4% | -88.5% | -88.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 320721.5 | 133714.6 | -58.4% | -59.1% | -57.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 177229.7 | 208608.3 | +17.9% | +15.8% | +19.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 209370.0 | 208608.3 | -0.9% | -3.4% | +1.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 1413682.2 | 267485.0 | -81.1% | -81.2% | -81.0% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 588976.7 | 267485.0 | -54.6% | -55.0% | -54.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 193668.1 | 514587.0 | +165.8% | +163.4% | +167.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 482239.0 | 514587.0 | +6.4% | +6.1% | +7.3% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 1549010.2 | 592275.2 | -61.8% | -61.8% | -61.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 1192322.3 | 592275.2 | -50.5% | -54.7% | -50.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 198418.3 | 1339537.8 | +574.9% | +571.7% | +580.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 1174631.2 | 1339537.8 | +14.8% | +12.0% | +14.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 1582666.6 | 1415635.5 | -10.5% | -11.1% | -9.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 3342693.5 | 1415635.5 | -57.7% | -59.1% | -56.2% |

#### Dictionary already prepared

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 1225.5 | 850.0 | -30.9% | -31.0% | -29.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 1065.5 | 850.0 | -20.6% | -21.1% | -19.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | str_contains() loop | 903.2 | 569.3 | -37.0% | -37.6% | -34.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | preg_match() | 694.5 | 569.3 | -17.6% | -18.8% | -16.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | str_contains() loop | 1065.6 | 959.8 | -9.6% | -10.7% | -8.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | preg_match() | 1240.5 | 959.8 | -22.3% | -22.7% | -21.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | str_contains() loop | 963.3 | 1006.1 | +3.9% | +2.9% | +5.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | preg_match() | 1215.8 | 1006.1 | -17.7% | -18.2% | -16.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 4338.9 | 3752.4 | -13.6% | -14.6% | -12.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 4860.9 | 3752.4 | -22.8% | -23.3% | -22.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | str_contains() loop | 1755.2 | 1705.1 | -2.6% | -3.2% | -2.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | preg_match() | 2249.2 | 1705.1 | -24.0% | -24.3% | -23.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 1913.3 | 855.5 | -54.7% | -55.9% | -54.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 1571.8 | 855.5 | -45.7% | -46.5% | -44.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | str_contains() loop | 1219.9 | 578.9 | -53.0% | -53.4% | -52.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | preg_match() | 726.5 | 578.9 | -20.4% | -21.5% | -20.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | str_contains() loop | 1476.7 | 982.8 | -33.8% | -34.2% | -32.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | preg_match() | 1848.4 | 982.8 | -46.9% | -48.1% | -46.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | str_contains() loop | 1298.6 | 1032.3 | -20.4% | -22.4% | -19.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | preg_match() | 1944.7 | 1032.3 | -47.2% | -47.5% | -46.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 7310.3 | 3533.7 | -51.8% | -52.8% | -51.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 11823.7 | 3533.7 | -70.2% | -70.3% | -69.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | str_contains() loop | 2601.8 | 1668.0 | -35.4% | -36.2% | -34.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | preg_match() | 3897.8 | 1668.0 | -57.2% | -57.2% | -56.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 3328.5 | 1071.2 | -67.9% | -68.7% | -67.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 3439.0 | 1071.2 | -68.8% | -69.0% | -68.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | str_contains() loop | 2074.9 | 583.6 | -71.9% | -72.3% | -71.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | preg_match() | 789.6 | 583.6 | -26.3% | -28.4% | -24.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | str_contains() loop | 2615.7 | 1240.7 | -52.6% | -53.2% | -51.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | preg_match() | 4339.5 | 1240.7 | -71.4% | -71.7% | -70.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | str_contains() loop | 2129.0 | 1300.8 | -39.2% | -40.2% | -37.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | preg_match() | 4521.5 | 1300.8 | -71.1% | -71.4% | -71.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 16702.4 | 6332.0 | -62.0% | -62.2% | -61.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 30168.8 | 6332.0 | -79.0% | -79.0% | -79.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | str_contains() loop | 6059.3 | 2662.0 | -56.1% | -56.1% | -55.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | preg_match() | 11106.5 | 2662.0 | -76.0% | -76.1% | -75.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 6137.4 | 1082.2 | -82.4% | -82.5% | -82.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 6773.5 | 1082.2 | -84.0% | -84.1% | -83.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | str_contains() loop | 3825.3 | 579.7 | -84.9% | -85.3% | -84.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | preg_match() | 955.8 | 579.7 | -39.2% | -41.3% | -38.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | str_contains() loop | 4970.0 | 1257.3 | -74.7% | -75.3% | -74.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | preg_match() | 8440.6 | 1257.3 | -85.1% | -85.2% | -85.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | str_contains() loop | 3973.7 | 1317.8 | -67.0% | -67.8% | -66.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | preg_match() | 9072.4 | 1317.8 | -85.5% | -85.6% | -85.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 32922.9 | 6353.4 | -80.7% | -80.8% | -80.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 62017.0 | 6353.4 | -89.8% | -89.8% | -89.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | str_contains() loop | 13025.0 | 2665.0 | -79.5% | -80.3% | -79.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | preg_match() | 23152.1 | 2665.0 | -88.5% | -88.5% | -88.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 12334.3 | 1113.9 | -91.0% | -91.2% | -90.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 13679.5 | 1113.9 | -91.9% | -91.9% | -91.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | str_contains() loop | 7218.7 | 592.4 | -92.0% | -92.2% | -91.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | preg_match() | 1217.7 | 592.4 | -51.4% | -53.4% | -50.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | str_contains() loop | 9426.1 | 1291.8 | -86.3% | -86.9% | -86.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | preg_match() | 16709.5 | 1291.8 | -92.3% | -92.3% | -92.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | str_contains() loop | 7492.1 | 1349.9 | -81.8% | -82.6% | -81.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | preg_match() | 18128.7 | 1349.9 | -92.6% | -92.6% | -92.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 62269.6 | 6483.9 | -89.6% | -90.0% | -89.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 127606.5 | 6483.9 | -94.9% | -95.8% | -94.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | str_contains() loop | 25289.6 | 2666.5 | -89.5% | -89.8% | -89.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | preg_match() | 47319.9 | 2666.5 | -94.4% | -94.4% | -94.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 30559.3 | 1152.7 | -96.3% | -96.5% | -96.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 27992.6 | 1152.7 | -95.9% | -95.9% | -95.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | str_contains() loop | 15224.7 | 572.6 | -96.2% | -96.5% | -96.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | preg_match() | 1781.4 | 572.6 | -67.5% | -68.3% | -66.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | str_contains() loop | 21682.9 | 1338.4 | -93.8% | -94.0% | -93.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | preg_match() | 33163.3 | 1338.4 | -96.0% | -96.0% | -96.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | str_contains() loop | 15657.0 | 1384.6 | -91.2% | -91.7% | -91.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | preg_match() | 36003.9 | 1384.6 | -96.2% | -96.2% | -96.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 139642.2 | 6610.8 | -95.3% | -95.5% | -95.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 251973.3 | 6610.8 | -97.4% | -97.4% | -97.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | str_contains() loop | 55233.6 | 2688.2 | -95.1% | -95.2% | -94.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | preg_match() | 93638.2 | 2688.2 | -97.1% | -97.1% | -97.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 75835.8 | 1198.8 | -98.4% | -98.4% | -98.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 97355.4 | 1198.8 | -98.8% | -98.9% | -98.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | str_contains() loop | 39409.8 | 589.9 | -98.5% | -98.6% | -98.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | preg_match() | 2983.3 | 589.9 | -80.0% | -80.8% | -80.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | str_contains() loop | 53432.8 | 1384.1 | -97.4% | -97.5% | -97.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | preg_match() | 106921.3 | 1384.1 | -98.7% | -98.8% | -98.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | str_contains() loop | 39483.0 | 1427.5 | -96.4% | -96.5% | -96.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | preg_match() | 118034.3 | 1427.5 | -98.8% | -98.9% | -98.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 317235.1 | 6954.0 | -97.8% | -97.9% | -97.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 911382.0 | 6954.0 | -99.2% | -99.3% | -99.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | str_contains() loop | 116071.5 | 2767.5 | -97.6% | -97.7% | -97.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | preg_match() | 330568.6 | 2767.5 | -99.2% | -99.2% | -99.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 5403.3 | 4148.6 | -23.2% | -23.4% | -22.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | preg_match() per term | 6806.8 | 4148.6 | -39.0% | -39.1% | -38.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 4415.8 | 3827.2 | -13.3% | -14.3% | -13.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 7727.3 | 3827.2 | -50.5% | -51.0% | -49.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 6726.0 | 4302.1 | -35.9% | -36.3% | -35.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 12921.5 | 4302.1 | -66.8% | -67.0% | -66.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 10009.4 | 5113.6 | -48.9% | -49.6% | -48.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | preg_match() per term | 12388.2 | 5113.6 | -58.7% | -58.8% | -58.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 8295.1 | 4159.3 | -49.8% | -51.0% | -49.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 14425.4 | 4159.3 | -71.2% | -71.3% | -71.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 12649.5 | 5076.5 | -59.9% | -60.1% | -58.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 23817.3 | 5076.5 | -78.7% | -78.7% | -78.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 18266.6 | 5511.6 | -69.9% | -70.0% | -69.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | preg_match() per term | 23972.6 | 5511.6 | -77.0% | -77.4% | -77.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 14804.5 | 4237.1 | -71.5% | -72.5% | -71.2% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 26944.7 | 4237.1 | -84.3% | -84.6% | -84.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 23022.3 | 5883.2 | -74.5% | -74.9% | -74.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 44537.6 | 5883.2 | -86.8% | -86.9% | -86.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 35988.1 | 6112.8 | -83.0% | -83.7% | -82.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | preg_match() per term | 44567.7 | 6112.8 | -86.3% | -86.3% | -86.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 30988.1 | 4434.8 | -85.7% | -86.4% | -85.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 52703.0 | 4434.8 | -91.6% | -91.7% | -91.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 46906.7 | 7191.6 | -84.7% | -84.8% | -84.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 82537.8 | 7191.6 | -91.3% | -91.4% | -91.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 73325.4 | 7117.6 | -90.3% | -90.6% | -90.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | preg_match() per term | 87223.2 | 7117.6 | -91.9% | -91.9% | -91.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 66689.6 | 4797.4 | -92.8% | -92.8% | -92.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 169961.3 | 4797.4 | -97.2% | -97.2% | -97.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 88268.4 | 8869.9 | -89.9% | -90.0% | -89.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 233787.6 | 8869.9 | -96.2% | -96.2% | -96.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 151189.5 | 7310.7 | -95.1% | -95.2% | -95.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | preg_match() per term | 177582.4 | 7310.7 | -95.9% | -95.9% | -95.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 141388.4 | 4864.9 | -96.5% | -96.6% | -96.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 412170.3 | 4864.9 | -98.8% | -98.8% | -98.8% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 164219.3 | 9043.8 | -94.5% | -94.6% | -94.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 493761.4 | 9043.8 | -98.2% | -98.2% | -98.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 286850.7 | 7725.9 | -97.3% | -97.3% | -97.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | preg_match() per term | 426177.9 | 7725.9 | -98.2% | -98.2% | -98.2% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 282529.8 | 5078.9 | -98.2% | -98.2% | -98.2% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 893462.1 | 5078.9 | -99.4% | -99.4% | -99.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 310053.4 | 9471.3 | -96.9% | -96.9% | -96.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 1008710.3 | 9471.3 | -99.1% | -99.1% | -99.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 20678.8 | 5254.3 | -74.6% | -74.9% | -74.4% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 3186.7 | 5254.3 | +65.1% | +63.0% | +65.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 162843.3 | 39333.0 | -75.8% | -76.0% | -75.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 22348.7 | 39333.0 | +76.3% | +75.5% | +77.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 36878.1 | 5574.3 | -84.9% | -85.0% | -84.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 8982.1 | 5574.3 | -37.7% | -38.4% | -37.3% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 292127.4 | 41685.9 | -85.7% | -85.8% | -85.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 69605.3 | 41685.9 | -40.1% | -40.4% | -39.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 77997.5 | 5999.7 | -92.3% | -92.3% | -92.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 17466.9 | 5999.7 | -65.6% | -65.7% | -65.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 621968.4 | 44920.3 | -92.8% | -92.8% | -92.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 136487.0 | 44920.3 | -67.1% | -67.2% | -67.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 143638.1 | 6424.0 | -95.5% | -95.6% | -95.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 31796.3 | 6424.0 | -79.8% | -79.9% | -79.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 1145868.3 | 47478.0 | -95.9% | -95.9% | -95.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 250901.9 | 47478.0 | -81.1% | -81.1% | -81.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 175336.6 | 6766.9 | -96.1% | -96.1% | -96.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 50336.4 | 6766.9 | -86.5% | -86.7% | -86.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 1397761.7 | 50516.9 | -96.4% | -96.4% | -96.3% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 399102.8 | 50516.9 | -87.3% | -87.4% | -87.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 191617.6 | 7021.6 | -96.3% | -96.4% | -96.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 104559.9 | 7021.6 | -93.3% | -93.3% | -93.3% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 1530194.7 | 52749.9 | -96.6% | -96.6% | -96.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 830367.9 | 52749.9 | -93.7% | -93.7% | -93.6% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 195845.3 | 7343.8 | -96.3% | -96.3% | -96.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 316542.1 | 7343.8 | -97.7% | -97.7% | -97.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 1565013.2 | 54890.9 | -96.5% | -96.5% | -96.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 2437098.0 | 54890.9 | -97.7% | -97.8% | -97.7% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 1253.4 | 755.1 | -39.8% | -40.2% | -39.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 977.6 | 755.1 | -22.9% | -23.7% | -22.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | str_contains() loop | 886.3 | 480.5 | -45.8% | -45.9% | -44.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | preg_match() | 633.3 | 480.5 | -23.5% | -29.6% | -23.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | str_contains() loop | 1057.0 | 837.7 | -20.7% | -21.4% | -20.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | preg_match() | 1137.3 | 837.7 | -26.5% | -27.7% | -26.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | str_contains() loop | 942.3 | 880.8 | -6.5% | -7.3% | -5.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | preg_match() | 1119.7 | 880.8 | -21.3% | -22.3% | -20.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 4413.2 | 3468.2 | -21.4% | -21.9% | -20.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 4601.3 | 3468.2 | -24.6% | -24.8% | -24.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | str_contains() loop | 1765.5 | 1504.9 | -14.8% | -15.0% | -14.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | preg_match() | 2094.1 | 1504.9 | -28.3% | -29.1% | -27.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 1985.3 | 774.2 | -61.0% | -61.2% | -60.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 1465.0 | 774.2 | -47.1% | -47.2% | -46.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | str_contains() loop | 1254.9 | 484.5 | -60.9% | -61.7% | -59.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | preg_match() | 660.5 | 484.5 | -26.2% | -27.3% | -24.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | str_contains() loop | 1501.4 | 866.1 | -42.3% | -42.7% | -41.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | preg_match() | 1720.5 | 866.1 | -49.7% | -51.4% | -48.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | str_contains() loop | 1303.4 | 928.7 | -28.5% | -29.9% | -28.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | preg_match() | 1821.4 | 928.7 | -49.4% | -50.3% | -48.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 7483.9 | 3530.8 | -52.9% | -53.9% | -52.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 11549.6 | 3530.8 | -69.4% | -69.7% | -69.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | str_contains() loop | 2567.0 | 1604.5 | -37.5% | -38.0% | -36.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | preg_match() | 3661.4 | 1604.5 | -56.0% | -56.6% | -55.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 3640.6 | 1114.1 | -69.4% | -69.5% | -68.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 3297.4 | 1114.1 | -66.2% | -66.3% | -66.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | str_contains() loop | 2160.6 | 484.5 | -77.7% | -77.8% | -77.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | preg_match() | 722.5 | 484.5 | -32.6% | -33.4% | -31.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | str_contains() loop | 2711.7 | 1289.1 | -52.5% | -52.6% | -52.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | preg_match() | 4185.3 | 1289.1 | -69.2% | -69.3% | -69.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | str_contains() loop | 2228.7 | 1349.1 | -39.6% | -40.5% | -39.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | preg_match() | 4376.4 | 1349.1 | -69.2% | -69.2% | -69.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 16884.4 | 7176.0 | -57.5% | -58.1% | -57.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 29597.2 | 7176.0 | -75.8% | -75.8% | -75.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | str_contains() loop | 6218.3 | 2910.2 | -53.2% | -53.2% | -53.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | preg_match() | 10815.9 | 2910.2 | -73.1% | -73.1% | -73.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 6863.4 | 1121.2 | -83.7% | -83.7% | -83.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 6928.3 | 1121.2 | -83.8% | -83.9% | -83.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | str_contains() loop | 4050.8 | 483.3 | -88.1% | -88.1% | -87.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | preg_match() | 871.4 | 483.3 | -44.4% | -44.9% | -43.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | str_contains() loop | 5276.5 | 1301.7 | -75.4% | -75.6% | -75.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | preg_match() | 8644.7 | 1301.7 | -84.9% | -85.0% | -84.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | str_contains() loop | 4250.1 | 1359.7 | -68.0% | -68.1% | -67.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | preg_match() | 9313.5 | 1359.7 | -85.4% | -85.4% | -85.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 33372.0 | 7183.8 | -78.4% | -78.5% | -78.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 64393.8 | 7183.8 | -88.8% | -88.9% | -88.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | str_contains() loop | 13434.0 | 2910.2 | -78.3% | -78.4% | -78.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | preg_match() | 23936.8 | 2910.2 | -87.8% | -87.9% | -87.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 14334.2 | 1152.1 | -92.0% | -92.0% | -91.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 12994.6 | 1152.1 | -91.1% | -91.2% | -91.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | str_contains() loop | 7865.5 | 487.4 | -93.9% | -94.1% | -93.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | preg_match() | 1047.7 | 487.4 | -53.7% | -54.9% | -52.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | str_contains() loop | 10218.3 | 1325.7 | -87.0% | -87.3% | -86.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | preg_match() | 15851.6 | 1325.7 | -91.6% | -91.7% | -91.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | str_contains() loop | 8018.1 | 1391.7 | -82.7% | -82.7% | -82.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | preg_match() | 17229.1 | 1391.7 | -91.9% | -92.6% | -91.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 66176.0 | 7295.7 | -88.9% | -89.0% | -88.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 121934.1 | 7295.7 | -94.0% | -94.0% | -94.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | str_contains() loop | 26370.7 | 2909.6 | -89.0% | -89.0% | -88.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | preg_match() | 45051.2 | 2909.6 | -93.5% | -93.5% | -93.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 35383.1 | 1181.3 | -96.7% | -96.7% | -96.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 30712.5 | 1181.3 | -96.2% | -96.5% | -95.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | str_contains() loop | 17308.9 | 483.7 | -97.2% | -97.2% | -97.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | preg_match() | 1636.3 | 483.7 | -70.2% | -70.7% | -70.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | str_contains() loop | 23199.7 | 1365.5 | -94.1% | -94.2% | -94.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | preg_match() | 32359.3 | 1365.5 | -95.8% | -96.6% | -95.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | str_contains() loop | 17630.6 | 1427.4 | -91.9% | -91.9% | -91.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | preg_match() | 38694.1 | 1427.4 | -96.3% | -96.7% | -95.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 149257.5 | 7465.9 | -95.0% | -95.0% | -95.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 247139.7 | 7465.9 | -97.0% | -97.2% | -97.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | str_contains() loop | 55738.5 | 2922.4 | -94.7% | -94.8% | -94.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | preg_match() | 91715.9 | 2922.4 | -96.8% | -97.5% | -96.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 80045.7 | 1232.0 | -98.5% | -98.5% | -98.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 92679.3 | 1232.0 | -98.7% | -98.8% | -98.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | str_contains() loop | 43442.4 | 487.2 | -98.9% | -98.9% | -98.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | preg_match() | 2891.2 | 487.2 | -83.1% | -83.3% | -82.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | str_contains() loop | 58671.8 | 1407.6 | -97.6% | -97.7% | -97.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | preg_match() | 113365.3 | 1407.6 | -98.8% | -98.8% | -98.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | str_contains() loop | 43832.6 | 1476.9 | -96.6% | -96.6% | -96.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | preg_match() | 117380.9 | 1476.9 | -98.7% | -98.8% | -98.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 335794.5 | 7747.3 | -97.7% | -97.7% | -97.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 898972.3 | 7747.3 | -99.1% | -99.2% | -99.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | str_contains() loop | 123337.7 | 2986.2 | -97.6% | -97.6% | -97.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | preg_match() | 319023.8 | 2986.2 | -99.1% | -99.1% | -99.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 5409.6 | 4323.0 | -20.0% | -20.2% | -19.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | preg_match() per term | 6674.6 | 4323.0 | -35.2% | -35.5% | -35.1% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 4481.9 | 3948.3 | -11.8% | -12.9% | -11.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 7577.5 | 3948.3 | -47.9% | -48.3% | -47.6% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 6665.8 | 5275.6 | -21.0% | -21.7% | -20.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 12750.5 | 5275.6 | -58.7% | -59.0% | -58.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 10226.1 | 5043.5 | -50.7% | -52.7% | -49.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | preg_match() per term | 12237.3 | 5043.5 | -58.8% | -59.3% | -58.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 8612.8 | 4387.5 | -49.0% | -49.2% | -48.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 14411.1 | 4387.5 | -69.5% | -70.3% | -69.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 12672.4 | 6035.0 | -52.4% | -53.1% | +21.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 23614.9 | 6035.0 | -74.4% | -74.6% | -36.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 18732.8 | 5492.9 | -70.7% | -70.8% | -70.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | preg_match() per term | 23887.3 | 5492.9 | -77.0% | -77.1% | -76.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 15812.1 | 4480.3 | -71.7% | -72.1% | -71.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 27275.8 | 4480.3 | -83.6% | -83.9% | -83.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 23846.7 | 6765.8 | -71.6% | -71.7% | -71.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 44389.8 | 6765.8 | -84.7% | -84.9% | -84.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 38392.7 | 6186.9 | -84.0% | -84.2% | -83.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | preg_match() per term | 44734.4 | 6186.9 | -86.3% | -86.4% | -86.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 33638.1 | 4753.4 | -85.9% | -86.1% | -85.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 52744.9 | 4753.4 | -91.0% | -91.1% | -90.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 47983.7 | 8046.1 | -83.2% | -83.4% | -82.8% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 82240.7 | 8046.1 | -90.2% | -90.3% | -90.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 77035.0 | 7359.4 | -90.5% | -90.5% | -90.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | preg_match() per term | 87102.1 | 7359.4 | -91.6% | -91.6% | -91.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 68636.5 | 5100.1 | -92.6% | -92.6% | -92.6% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 174072.5 | 5100.1 | -97.1% | -97.1% | -97.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 91120.4 | 9674.2 | -89.4% | -89.5% | -89.3% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 236204.4 | 9674.2 | -95.9% | -96.0% | -95.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 152435.5 | 7529.7 | -95.1% | -95.1% | -94.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | preg_match() per term | 180237.1 | 7529.7 | -95.8% | -95.8% | -95.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 145128.0 | 5237.4 | -96.4% | -96.4% | -96.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 416961.0 | 5237.4 | -98.7% | -98.8% | -98.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 168543.0 | 9799.4 | -94.2% | -94.6% | -94.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 495161.3 | 9799.4 | -98.0% | -98.0% | -97.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 293855.6 | 8005.2 | -97.3% | -97.3% | -97.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | preg_match() per term | 431939.6 | 8005.2 | -98.1% | -98.2% | -98.1% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 289914.3 | 5520.2 | -98.1% | -98.2% | -98.1% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 892644.3 | 5520.2 | -99.4% | -99.4% | -99.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 313161.8 | 10318.8 | -96.7% | -96.7% | -96.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 1012288.8 | 10318.8 | -99.0% | -99.0% | -99.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 19976.4 | 4903.2 | -75.4% | -75.7% | -75.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 3203.9 | 4903.2 | +53.4% | +50.2% | +54.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 157214.3 | 37195.3 | -76.3% | -76.9% | -76.1% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 22343.7 | 37195.3 | +66.2% | +65.9% | +67.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 36061.9 | 5397.9 | -85.0% | -85.1% | -85.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 8965.5 | 5397.9 | -39.8% | -40.4% | -39.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 288704.4 | 40972.4 | -85.8% | -85.8% | -85.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 69106.9 | 40972.4 | -40.5% | -41.1% | -40.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 77417.1 | 5881.3 | -92.4% | -92.5% | -92.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 17511.6 | 5881.3 | -66.4% | -66.6% | -65.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 616066.2 | 44430.3 | -92.8% | -92.8% | -92.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 136991.2 | 44430.3 | -67.5% | -67.6% | -67.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 143863.0 | 6419.8 | -95.5% | -95.5% | -95.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 31693.5 | 6419.8 | -79.7% | -79.9% | -79.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 1149053.5 | 48205.5 | -95.8% | -95.8% | -95.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 249619.1 | 48205.5 | -80.7% | -80.7% | -80.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 177483.6 | 6913.8 | -96.1% | -96.1% | -96.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 54454.8 | 6913.8 | -87.3% | -87.3% | -87.1% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 1414056.6 | 52072.0 | -96.3% | -96.3% | -96.3% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 431788.4 | 52072.0 | -87.9% | -88.2% | -87.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 193861.8 | 7116.3 | -96.3% | -96.3% | -96.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 101452.4 | 7116.3 | -93.0% | -93.0% | -92.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 1547588.5 | 53651.0 | -96.5% | -96.5% | -96.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 809231.2 | 53651.0 | -93.4% | -93.4% | -93.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 198154.0 | 7572.8 | -96.2% | -96.2% | -96.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 307570.9 | 7572.8 | -97.6% | -97.7% | -97.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 1581122.1 | 56176.9 | -96.4% | -96.5% | -96.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 2466313.1 | 56176.9 | -97.7% | -97.8% | -97.6% |

### Control tasks

#### Dictionary preparation included

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | str_contains() loop | 1505.4 | 28876.2 | +1829.8% | +1802.7% | +1862.8% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | preg_match() | 5775.3 | 28876.2 | +400.0% | +394.0% | +404.2% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | strtr() | 334280.0 | 705944.7 | +111.1% | +110.0% | +112.4% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace_callback() | 50049.8 | 705944.7 | +1311.3% | +1297.8% | +1316.9% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | str_replace() | 712536.8 | 705944.7 | -1.0% | -1.1% | -0.7% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace() | 47576.5 | 705944.7 | +1382.9% | +1365.8% | +1389.2% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | str_contains() loop | 1535.5 | 27458.5 | +1690.7% | +1675.3% | +1723.0% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | preg_match() | 6237.3 | 27458.5 | +342.7% | +337.7% | +346.7% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | strtr() | 305938.9 | 506003.7 | +65.4% | +64.9% | +65.9% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace_callback() | 46360.6 | 506003.7 | +994.9% | +974.1% | +996.2% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | str_replace() | 665543.1 | 506003.7 | -23.9% | -24.3% | -23.7% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace() | 44494.3 | 506003.7 | +1038.4% | +1032.0% | +1042.3% |

#### Dictionary already prepared

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | str_contains() loop | 1486.4 | 1068.7 | -28.2% | -28.6% | -27.5% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | preg_match() | 1146.9 | 1068.7 | -6.9% | -7.6% | -6.6% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | strtr() | 333973.1 | 637385.0 | +90.8% | +89.7% | +91.0% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace_callback() | 20887.1 | 637385.0 | +2952.1% | +2936.9% | +2961.0% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | str_replace() | 692037.3 | 637385.0 | -8.0% | -8.0% | -7.9% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace() | 18996.3 | 637385.0 | +3250.2% | +3155.2% | +3272.4% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | str_contains() loop | 1527.7 | 1108.9 | -27.4% | -27.8% | -27.1% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | preg_match() | 1118.3 | 1108.9 | -1.0% | -5.6% | -0.3% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | strtr() | 305035.5 | 443710.9 | +45.5% | +44.9% | +47.0% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace_callback() | 20983.2 | 443710.9 | +2013.0% | +1991.6% | +2036.5% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | str_replace() | 644132.1 | 443710.9 | -31.1% | -31.3% | -30.5% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace() | 19098.1 | 443710.9 | +2222.8% | +2212.0% | +2241.3% |
