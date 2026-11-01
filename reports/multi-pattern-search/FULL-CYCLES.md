# Complete CPU-cycle comparisons

Unit: cycles per complete job. Lower is better. Δ is the median of paired per-pass changes; min/max are paired changes, not confidence intervals.

All measured alternatives are listed. Preparation and reuse are separate sections. Natural API result representations are retained; see [method](METHOD.md).

## Everyday cases

### Product tasks

#### Dictionary preparation included

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1504.0 | 33496.7 | +2118.4% | +2106.7% | +2218.7% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5757.5 | 33496.7 | +481.8% | +472.7% | +507.7% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1231.3 | 32717.8 | +2558.7% | +2532.7% | +2664.2% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5327.4 | 32717.8 | +515.9% | +512.6% | +528.2% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1386.1 | 34071.8 | +2364.3% | +2308.6% | +2380.8% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 6028.8 | 34071.8 | +464.7% | +459.6% | +469.1% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1262.5 | 33947.8 | +2585.6% | +2559.7% | +2613.2% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 6074.6 | 33947.8 | +458.4% | +457.6% | +462.3% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4873.4 | 39460.9 | +710.5% | +688.7% | +718.1% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 10059.4 | 39460.9 | +292.7% | +288.3% | +296.9% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 2806.8 | 34798.6 | +1137.8% | +1116.0% | +1204.8% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 7084.1 | 34798.6 | +394.3% | +388.2% | +417.3% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 6059.4 | 94591.4 | +1464.6% | +1454.6% | +1497.5% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 7763.6 | 94591.4 | +1119.8% | +1116.6% | +1131.9% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 6797.0 | 93988.0 | +1285.2% | +1281.8% | +1290.1% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 6091.3 | 93988.0 | +1443.5% | +1439.9% | +1449.8% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 9742.4 | 97185.1 | +896.6% | +889.0% | +899.4% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 8647.0 | 97185.1 | +1024.1% | +1017.9% | +1027.1% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 6644.2 | 95659.1 | +1339.8% | +1315.9% | +1343.6% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 8735.0 | 95659.1 | +996.0% | +986.7% | +998.0% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 16865.6 | 106785.2 | +533.0% | +532.5% | +536.8% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 23766.3 | 106785.2 | +349.0% | +348.6% | +351.2% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 9483.6 | 98720.7 | +941.2% | +933.3% | +945.2% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 12788.5 | 98720.7 | +672.6% | +670.7% | +674.5% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1566.2 | 79969.4 | +5001.3% | +4739.2% | +5072.1% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5878.9 | 79969.4 | +1265.7% | +1256.7% | +1270.8% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1312.8 | 79656.2 | +5973.7% | +5874.8% | +6027.8% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5295.8 | 79656.2 | +1404.9% | +1399.2% | +1411.8% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1758.4 | 80850.7 | +4502.7% | +4445.4% | +4620.2% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 6081.7 | 80850.7 | +1229.4% | +1215.9% | +1236.5% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1487.4 | 80823.2 | +5384.8% | +5296.3% | +5479.5% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 6196.0 | 80823.2 | +1207.0% | +1196.8% | +1223.0% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 7393.7 | 87007.3 | +1078.2% | +1072.4% | +1081.0% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 12223.6 | 87007.3 | +612.8% | +611.3% | +617.3% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4465.4 | 82708.6 | +1752.2% | +1749.8% | +1768.4% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 7589.9 | 82708.6 | +989.8% | +987.4% | +1003.3% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 20037.8 | 55041.7 | +175.0% | +174.5% | +175.9% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 15414.6 | 55041.7 | +257.3% | +255.6% | +258.9% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 10038.9 | 28457.1 | +183.5% | +183.0% | +187.5% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 4230.3 | 28457.1 | +575.2% | +570.7% | +582.7% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 11249.6 | 42598.6 | +278.4% | +277.0% | +281.8% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 9848.5 | 42598.6 | +332.5% | +327.9% | +337.0% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 12263.2 | 54759.5 | +346.5% | +342.6% | +347.8% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 14708.3 | 54759.5 | +272.2% | +270.3% | +275.4% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | strtr() | 4340.3 | 32062.7 | +638.7% | +634.1% | +642.4% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | preg_replace_callback() | 18222.9 | 32062.7 | +75.7% | +74.8% | +76.2% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | str_replace() | 13799.8 | 32062.7 | +132.1% | +129.0% | +133.1% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | strtr() | 6451.8 | 36329.6 | +463.8% | +459.9% | +465.6% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | preg_replace_callback() | 23211.1 | 36329.6 | +56.8% | +55.8% | +57.1% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | str_replace() | 17738.1 | 36329.6 | +104.8% | +104.5% | +105.4% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 1508.8 | 11623.9 | +672.2% | +666.2% | +690.4% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 8338.8 | 11623.9 | +39.4% | +38.6% | +44.6% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 5956.7 | 11623.9 | +94.2% | +91.0% | +102.0% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 9384.2 | 30378.0 | +223.7% | +221.3% | +226.2% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 20355.1 | 30378.0 | +49.0% | +48.3% | +49.9% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 12686.9 | 30378.0 | +139.6% | +136.4% | +143.0% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 881.0 | 4133.0 | +368.8% | +367.3% | +394.8% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 5218.3 | 4133.0 | -21.0% | -21.4% | -16.2% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 4604.4 | 4133.0 | -10.5% | -10.9% | -5.8% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 1314.4 | 5134.5 | +290.6% | +285.0% | +292.3% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 7014.9 | 5134.5 | -26.8% | -27.2% | -26.5% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 5338.8 | 5134.5 | -3.7% | -4.5% | -3.4% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | strtr() | 938.9 | 2462.2 | +161.2% | +159.2% | +166.0% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace_callback() | 5170.5 | 2462.2 | -52.5% | -53.3% | -52.3% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | str_replace() | 3877.6 | 2462.2 | -36.6% | -37.0% | -34.2% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace() | 4047.9 | 2462.2 | -39.5% | -39.9% | -38.5% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 1551.7 | 42935.2 | +2670.5% | +2649.2% | +2690.6% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 10660.0 | 42935.2 | +305.3% | +300.5% | +307.9% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 6554.9 | 42935.2 | +555.0% | +549.7% | +559.9% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 1923.3 | 45752.0 | +2278.8% | +2246.9% | +2351.2% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 11592.5 | 45752.0 | +295.0% | +292.5% | +307.7% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 7188.1 | 45752.0 | +530.8% | +529.2% | +561.2% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 12830.0 | 59859.0 | +366.8% | +365.4% | +371.5% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 20984.9 | 59859.0 | +185.7% | +183.2% | +189.2% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 16160.3 | 59859.0 | +271.5% | +262.3% | +274.4% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 27205.8 | 194477.1 | +615.0% | +609.4% | +616.3% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 30755.2 | 194477.1 | +532.9% | +529.5% | +534.3% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 73009.6 | 194477.1 | +166.3% | +164.7% | +166.8% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 30277.2 | 194477.1 | +540.5% | +536.4% | +543.3% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 27893.2 | 201594.4 | +624.1% | +617.6% | +625.0% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 32182.1 | 201594.4 | +527.2% | +525.6% | +528.9% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 76689.8 | 201594.4 | +163.0% | +162.2% | +163.8% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 31164.7 | 201594.4 | +547.1% | +544.3% | +549.4% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 42018.8 | 238267.5 | +466.8% | +464.1% | +468.2% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 34191.9 | 238267.5 | +596.1% | +595.8% | +599.5% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 112342.4 | 238267.5 | +112.2% | +111.3% | +113.0% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 32324.8 | 238267.5 | +637.8% | +633.2% | +642.0% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 335115.6 | 929019.7 | +177.4% | +176.7% | +178.9% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 49691.7 | 929019.7 | +1767.6% | +1756.8% | +1774.4% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 712932.8 | 929019.7 | +30.3% | +29.8% | +30.3% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 47646.9 | 929019.7 | +1847.7% | +1826.7% | +1855.5% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 836.3 | 3919.6 | +368.9% | +368.1% | +372.1% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 9132.6 | 3919.6 | -57.1% | -57.7% | -56.7% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 7998.4 | 3919.6 | -51.0% | -52.0% | -50.3% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 1046.8 | 4268.0 | +310.8% | +305.2% | +333.4% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 9818.8 | 4268.0 | -56.6% | -57.3% | -53.4% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 8278.5 | 4268.0 | -48.1% | -48.6% | -45.0% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 57234.4 | 146461.7 | +155.9% | +152.6% | +164.4% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | preg_match() per term | 100740.9 | 146461.7 | +45.4% | +44.1% | +46.9% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 47052.4 | 144338.2 | +207.6% | +191.6% | +209.3% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 147591.4 | 144338.2 | -2.1% | -4.9% | -1.7% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 70467.1 | 148557.4 | +111.2% | +107.2% | +115.9% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 217212.8 | 148557.4 | -31.5% | -31.7% | -31.0% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 135338.5 | 164404.0 | +21.4% | +21.3% | +22.5% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 156996.9 | 164404.0 | +4.6% | +4.5% | +6.0% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 1080260.7 | 221896.2 | -79.5% | -79.5% | -79.2% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 447279.3 | 221896.2 | -50.4% | -50.6% | -49.8% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1535.6 | 30979.8 | +1927.3% | +1853.8% | +1938.2% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 6255.8 | 30979.8 | +396.5% | +378.1% | +400.8% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1236.1 | 30337.9 | +2359.9% | +2334.8% | +2380.5% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5857.2 | 30337.9 | +415.2% | +410.6% | +419.1% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1374.1 | 31633.2 | +2206.2% | +2170.0% | +2273.4% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 6563.5 | 31633.2 | +381.8% | +376.8% | +393.8% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1247.6 | 31787.9 | +2457.9% | +2436.7% | +2501.8% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 6503.6 | 31787.9 | +388.5% | +369.5% | +401.4% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4976.8 | 37682.9 | +658.9% | +655.6% | +663.9% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 11284.9 | 37682.9 | +233.2% | +228.1% | +236.2% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 2735.3 | 32398.2 | +1082.3% | +1071.5% | +1098.1% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 7736.1 | 32398.2 | +323.2% | +316.5% | +330.1% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 6091.3 | 90164.6 | +1377.9% | +1370.1% | +1389.0% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 7871.1 | 90164.6 | +1041.2% | +1030.2% | +1054.2% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 6867.7 | 89157.0 | +1197.0% | +1194.3% | +1204.8% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 6125.5 | 89157.0 | +1358.9% | +1339.1% | +1367.6% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 9974.0 | 92616.3 | +827.8% | +824.6% | +833.1% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 8680.8 | 92616.3 | +968.7% | +965.7% | +974.5% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 6858.3 | 91459.4 | +1233.6% | +1216.4% | +1236.3% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 8743.3 | 91459.4 | +944.5% | +938.4% | +949.6% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 15946.7 | 103537.4 | +547.0% | +546.1% | +553.2% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 24132.6 | 103537.4 | +329.5% | +326.8% | +331.6% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 9010.0 | 94792.3 | +952.6% | +946.3% | +955.1% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 12915.7 | 94792.3 | +636.2% | +631.1% | +637.1% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1621.8 | 74749.7 | +4509.1% | +4463.7% | +4569.8% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 6222.2 | 74749.7 | +1099.8% | +1098.1% | +1108.1% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1317.7 | 74923.3 | +5618.6% | +5548.5% | +5639.2% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5575.4 | 74923.3 | +1244.3% | +1234.2% | +1268.8% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1744.0 | 75876.1 | +4265.7% | +4232.6% | +4374.4% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 6346.7 | 75876.1 | +1095.5% | +1090.0% | +1102.7% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1464.5 | 75765.3 | +5072.0% | +4957.3% | +5105.5% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 6479.0 | 75765.3 | +1075.2% | +1059.2% | +1084.0% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 7509.2 | 82561.3 | +999.2% | +995.8% | +1003.0% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 12706.8 | 82561.3 | +550.6% | +546.2% | +553.9% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4414.3 | 77730.0 | +1662.7% | +1641.0% | +1673.7% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 7974.6 | 77730.0 | +874.5% | +872.8% | +882.8% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 18606.3 | 56052.4 | +201.1% | +200.7% | +202.6% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 14582.0 | 56052.4 | +285.0% | +283.0% | +286.5% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 9288.7 | 26864.2 | +189.2% | +187.1% | +193.1% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 3941.8 | 26864.2 | +582.4% | +576.7% | +589.6% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 10424.5 | 42300.7 | +305.6% | +304.1% | +310.1% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 9377.5 | 42300.7 | +351.8% | +345.9% | +354.0% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 11362.0 | 55808.3 | +391.2% | +389.6% | +393.9% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 14127.4 | 55808.3 | +295.1% | +293.9% | +295.7% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | strtr() | 3918.6 | 31339.9 | +695.5% | +689.5% | +706.1% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | preg_replace_callback() | 18649.8 | 31339.9 | +66.3% | +65.0% | +70.2% |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | str_replace() | 13772.4 | 31339.9 | +125.2% | +122.7% | +131.9% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | strtr() | 5949.1 | 35643.2 | +500.1% | +497.5% | +505.9% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | preg_replace_callback() | 23739.2 | 35643.2 | +50.2% | +49.6% | +51.9% |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | 10 | str_replace() | 17818.5 | 35643.2 | +100.8% | +98.7% | +102.2% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 1340.4 | 11267.6 | +739.9% | +730.9% | +744.4% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 8279.2 | 11267.6 | +36.2% | +33.3% | +37.7% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 5871.6 | 11267.6 | +91.2% | +88.9% | +93.1% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 8595.4 | 30844.8 | +259.0% | +254.8% | +261.6% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 20611.0 | 30844.8 | +50.3% | +49.2% | +51.3% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 12378.7 | 30844.8 | +149.5% | +147.8% | +153.6% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 751.2 | 4072.8 | +443.4% | +429.6% | +445.1% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 4890.5 | 4072.8 | -16.6% | -17.1% | -16.2% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 4369.9 | 4072.8 | -6.7% | -6.9% | -6.2% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 1218.9 | 4996.7 | +306.2% | +298.9% | +311.2% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 6781.9 | 4996.7 | -26.3% | -27.3% | -25.8% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 5126.5 | 4996.7 | -2.3% | -3.9% | -1.9% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | strtr() | 846.3 | 2386.1 | +180.4% | +178.3% | +183.8% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace_callback() | 4797.9 | 2386.1 | -50.4% | -50.8% | -50.1% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | str_replace() | 3529.5 | 2386.1 | -32.8% | -33.4% | -31.8% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace() | 3823.5 | 2386.1 | -37.8% | -38.2% | -37.3% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 1416.9 | 41236.8 | +2814.1% | +2795.3% | +2851.1% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 11779.2 | 41236.8 | +249.0% | +247.5% | +258.2% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 6473.6 | 41236.8 | +535.4% | +534.0% | +537.9% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 1803.1 | 43845.9 | +2332.5% | +2286.7% | +2373.3% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 12763.6 | 43845.9 | +242.1% | +240.0% | +252.7% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 7187.6 | 43845.9 | +507.5% | +504.3% | +513.3% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 12220.2 | 60090.5 | +391.4% | +384.4% | +398.5% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 22463.8 | 60090.5 | +169.6% | +164.6% | +172.2% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 16432.7 | 60090.5 | +264.6% | +238.5% | +271.2% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 24703.8 | 196951.1 | +696.5% | +658.4% | +702.2% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 27562.5 | 196951.1 | +613.9% | +612.2% | +618.4% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 69656.8 | 196951.1 | +182.7% | +182.2% | +183.0% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 27136.5 | 196951.1 | +625.8% | +624.8% | +626.8% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 25465.4 | 200364.5 | +687.4% | +680.7% | +688.3% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 28894.1 | 200364.5 | +593.2% | +590.5% | +593.6% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 72889.9 | 200364.5 | +174.8% | +172.6% | +175.9% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 27920.0 | 200364.5 | +617.6% | +609.8% | +623.3% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 38489.5 | 237944.6 | +518.2% | +517.2% | +520.1% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 30995.3 | 237944.6 | +667.8% | +657.7% | +670.2% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 105902.4 | 237944.6 | +124.7% | +124.4% | +125.6% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 29083.2 | 237944.6 | +718.9% | +715.8% | +721.9% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 306656.1 | 976121.1 | +218.1% | +214.3% | +220.0% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 46844.1 | 976121.1 | +1982.1% | +1966.0% | +1994.4% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 666378.4 | 976121.1 | +46.4% | +46.2% | +46.6% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 44490.4 | 976121.1 | +2095.0% | +2078.8% | +2110.5% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 728.1 | 3816.4 | +423.9% | +417.5% | +431.4% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 9309.7 | 3816.4 | -59.0% | -59.4% | -58.8% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 7858.1 | 3816.4 | -51.4% | -52.6% | -51.4% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 897.9 | 4099.5 | +356.5% | +353.5% | +357.1% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 9907.6 | 4099.5 | -58.4% | -59.0% | -58.3% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 8184.0 | 4099.5 | -49.9% | -50.5% | -49.4% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 58966.5 | 140551.3 | +139.3% | +138.1% | +139.9% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | preg_match() per term | 98623.4 | 140551.3 | +42.6% | +41.6% | +43.3% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 50942.3 | 138270.9 | +171.5% | +169.3% | +172.5% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 134930.0 | 138270.9 | +2.4% | +0.7% | +4.9% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 71472.2 | 142870.0 | +100.3% | +99.3% | +100.6% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 212735.9 | 142870.0 | -32.8% | -32.9% | -32.2% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 135127.9 | 157819.4 | +16.8% | +16.3% | +17.1% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 155413.4 | 157819.4 | +1.6% | +1.0% | +2.0% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 1078499.4 | 214633.3 | -80.1% | -80.1% | -80.1% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 451826.4 | 214633.3 | -52.4% | -52.8% | -52.3% |

#### Dictionary already prepared

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1470.4 | 1216.6 | -17.5% | -18.8% | -17.2% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1146.3 | 1216.6 | +6.0% | +5.4% | +7.0% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1236.7 | 720.8 | -41.9% | -43.1% | -40.9% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 761.2 | 720.8 | -5.1% | -7.3% | -4.8% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1380.8 | 1850.3 | +33.5% | +31.4% | +35.1% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1411.6 | 1850.3 | +30.9% | +30.5% | +32.2% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1272.5 | 2021.3 | +58.6% | +55.8% | +61.1% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1471.3 | 2021.3 | +37.0% | +33.3% | +37.6% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4973.0 | 8556.5 | +72.0% | +71.8% | +75.3% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 5410.4 | 8556.5 | +58.1% | +57.3% | +60.1% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 2743.5 | 3746.9 | +36.6% | +33.8% | +36.6% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2463.0 | 3746.9 | +52.2% | +51.8% | +52.7% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 5967.5 | 1834.4 | -69.3% | -69.9% | -68.8% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2428.9 | 1834.4 | -24.5% | -25.0% | -23.7% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 6761.1 | 910.2 | -86.5% | -86.7% | -86.4% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 793.7 | 910.2 | +14.6% | +13.4% | +15.6% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 9839.3 | 2903.5 | -70.5% | -70.6% | -70.2% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 3283.7 | 2903.5 | -11.9% | -12.2% | -11.1% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 6652.3 | 2960.2 | -55.6% | -56.2% | -55.4% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 3370.9 | 2960.2 | -12.4% | -12.9% | -11.9% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 16869.4 | 13804.8 | -18.2% | -18.3% | -18.1% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 18413.1 | 13804.8 | -25.0% | -25.3% | -24.8% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 9482.7 | 5821.8 | -38.6% | -44.5% | -38.4% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 7422.2 | 5821.8 | -21.5% | -21.8% | -21.5% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1552.8 | 1119.7 | -27.9% | -28.4% | -27.9% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1291.9 | 1119.7 | -13.5% | -16.6% | -12.6% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1329.0 | 682.2 | -48.0% | -49.0% | -47.8% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 741.1 | 682.2 | -8.1% | -8.7% | -6.6% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1720.0 | 1746.5 | +1.6% | -1.7% | +2.3% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1498.0 | 1746.5 | +16.4% | +14.4% | +18.3% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1491.2 | 1750.5 | +17.5% | +15.9% | +20.5% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1582.0 | 1750.5 | +10.7% | +9.3% | +11.6% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 7396.9 | 8034.1 | +8.7% | +7.6% | +9.4% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 7644.3 | 8034.1 | +5.2% | +4.4% | +5.6% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4298.6 | 3680.8 | -14.2% | -16.4% | -14.0% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2981.0 | 3680.8 | +23.4% | +23.3% | +23.7% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 20039.7 | 28499.6 | +42.2% | +42.0% | +42.3% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 12390.5 | 28499.6 | +130.0% | +129.1% | +130.5% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 10048.1 | 1954.2 | -80.6% | -80.6% | -80.5% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 1108.5 | 1954.2 | +76.3% | +75.2% | +76.6% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 11267.4 | 16014.5 | +42.1% | +36.4% | +42.4% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 6637.8 | 16014.5 | +141.3% | +140.6% | +141.7% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 12268.1 | 28280.8 | +130.5% | +130.1% | +130.6% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 11483.6 | 28280.8 | +146.2% | +145.3% | +146.8% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 1511.2 | 3016.2 | +99.9% | +98.4% | +101.8% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 2185.8 | 3016.2 | +38.2% | +37.1% | +39.1% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 1371.6 | 3016.2 | +120.1% | +119.3% | +124.6% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 9360.7 | 21543.1 | +130.4% | +129.8% | +131.2% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 14125.4 | 21543.1 | +52.8% | +50.9% | +53.4% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 7987.7 | 21543.1 | +169.4% | +165.1% | +174.6% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 882.9 | 1485.5 | +68.3% | +67.6% | +69.3% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 746.9 | 1485.5 | +99.5% | +97.7% | +100.2% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 839.0 | 1485.5 | +77.0% | +74.5% | +78.9% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 1316.4 | 2434.0 | +84.9% | +82.6% | +85.6% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 2486.2 | 2434.0 | -2.1% | -2.5% | -1.6% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 1479.8 | 2434.0 | +64.5% | +62.4% | +65.8% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | strtr() | 955.2 | 1202.3 | +25.9% | +24.2% | +27.5% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace_callback() | 1666.1 | 1202.3 | -27.9% | -28.2% | -27.3% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | str_replace() | 955.2 | 1202.3 | +25.9% | +25.1% | +27.1% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace() | 905.7 | 1202.3 | +32.6% | +31.9% | +33.7% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 1565.6 | 1505.2 | -3.9% | -4.3% | -2.2% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 851.1 | 1505.2 | +76.1% | +75.5% | +81.0% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 1145.0 | 1505.2 | +33.1% | +29.9% | +34.8% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 1925.5 | 2654.3 | +37.9% | +37.3% | +38.1% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 1759.2 | 2654.3 | +50.8% | +50.6% | +51.2% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 1712.8 | 2654.3 | +54.9% | +54.3% | +55.3% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 12885.5 | 18407.8 | +43.1% | +42.0% | +43.6% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 10997.5 | 18407.8 | +67.3% | +65.3% | +68.2% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 10716.6 | 18407.8 | +71.9% | +70.9% | +72.1% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 27156.5 | 57849.7 | +113.0% | +112.1% | +113.4% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 2218.7 | 57849.7 | +2507.5% | +2499.8% | +2511.9% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 53205.3 | 57849.7 | +8.7% | +8.6% | +8.8% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 2135.7 | 57849.7 | +2608.8% | +2606.0% | +2613.0% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 27939.7 | 65469.3 | +134.3% | +133.2% | +135.6% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 3333.5 | 65469.3 | +1863.2% | +1848.7% | +1870.2% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 56564.6 | 65469.3 | +15.7% | +15.7% | +15.9% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 2674.8 | 65469.3 | +2347.7% | +2271.5% | +2352.2% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 42051.8 | 102369.2 | +143.4% | +142.0% | +144.0% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 5210.4 | 102369.2 | +1864.6% | +1845.2% | +1873.6% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 92127.2 | 102369.2 | +11.1% | +5.5% | +11.1% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 3735.2 | 102369.2 | +2639.3% | +2627.2% | +2642.3% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 333847.6 | 793103.7 | +137.7% | +135.7% | +138.2% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 20773.5 | 793103.7 | +3714.0% | +3713.5% | +3730.9% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 692264.8 | 793103.7 | +14.6% | +14.5% | +14.6% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 18889.8 | 793103.7 | +4099.8% | +4008.1% | +4122.3% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 842.5 | 1163.0 | +38.1% | +37.6% | +38.4% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 825.0 | 1163.0 | +41.0% | +39.1% | +42.0% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 997.5 | 1163.0 | +16.5% | +15.4% | +17.0% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 1044.1 | 1488.5 | +42.1% | +41.7% | +43.4% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 1465.0 | 1488.5 | +1.7% | +0.7% | +1.8% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 1223.5 | 1488.5 | +21.7% | +20.3% | +22.7% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 55368.5 | 8312.9 | -85.0% | -85.7% | -84.9% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | preg_match() per term | 67357.8 | 8312.9 | -87.7% | -87.7% | -87.6% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 48819.5 | 5905.0 | -87.9% | -88.0% | -87.4% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 81771.5 | 5905.0 | -92.8% | -92.9% | -92.6% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 70201.8 | 9995.1 | -85.7% | -86.0% | -85.4% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 160096.9 | 9995.1 | -93.7% | -93.8% | -93.7% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 135438.1 | 8038.6 | -94.1% | -94.1% | -94.1% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 41669.0 | 8038.6 | -80.7% | -80.7% | -80.7% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 1080555.9 | 60769.0 | -94.4% | -94.4% | -94.3% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 329964.9 | 60769.0 | -81.6% | -81.6% | -81.3% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1532.2 | 1263.3 | -17.7% | -17.9% | -17.0% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1114.7 | 1263.3 | +13.4% | +12.2% | +13.9% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1230.8 | 703.1 | -43.0% | -44.0% | -42.3% |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 675.4 | 703.1 | +3.6% | +2.8% | +5.0% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1371.5 | 1931.9 | +40.5% | +39.6% | +41.3% |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1380.3 | 1931.9 | +39.9% | +39.3% | +40.0% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1261.2 | 2130.3 | +68.7% | +67.8% | +73.4% |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1443.7 | 2130.3 | +48.1% | +47.0% | +48.7% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4972.6 | 9305.5 | +87.2% | +85.5% | +87.5% |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 6187.1 | 9305.5 | +50.4% | +49.4% | +50.5% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 2735.3 | 4031.5 | +47.3% | +46.3% | +48.2% |
| [Check a detailed EN support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2553.7 | 4031.5 | +57.7% | +57.7% | +59.1% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 6093.6 | 1937.6 | -68.2% | -68.6% | -68.1% |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 2400.4 | 1937.6 | -19.3% | -19.4% | -19.0% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 6871.3 | 892.9 | -87.0% | -87.1% | -86.8% |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 692.9 | 892.9 | +28.6% | +27.8% | +31.3% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 9961.6 | 3079.4 | -69.1% | -69.1% | -68.8% |
| [Flag a short RU comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 3239.9 | 3079.4 | -4.9% | -5.0% | -4.6% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 6858.4 | 3145.0 | -54.1% | -54.3% | -54.1% |
| [Flag a short RU comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 3304.0 | 3145.0 | -4.9% | -5.3% | -4.6% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 15952.4 | 15055.1 | -5.6% | -5.7% | -5.5% |
| [Check a detailed RU support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 18718.1 | 15055.1 | -19.6% | -20.2% | -19.3% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 8996.7 | 6294.7 | -30.0% | -35.4% | -29.9% |
| [Check a detailed RU support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 7451.6 | 6294.7 | -15.5% | -15.7% | -15.4% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1616.8 | 1158.9 | -28.3% | -28.6% | -28.0% |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1254.9 | 1158.9 | -7.4% | -7.8% | -6.8% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1319.8 | 677.8 | -48.7% | -49.5% | -48.1% |
| [Flag a short ZH comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 671.0 | 677.8 | +0.5% | -0.6% | +1.3% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1749.5 | 1829.1 | +4.6% | -1.4% | +6.2% |
| [Flag a short ZH comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1450.8 | 1829.1 | +26.0% | +24.1% | +27.7% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 1472.3 | 1838.9 | +24.6% | +24.2% | +26.6% |
| [Flag a short ZH comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 1539.4 | 1838.9 | +20.0% | +19.0% | +20.8% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 7494.1 | 8730.5 | +16.5% | +16.2% | +17.0% |
| [Check a detailed ZH support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 7773.2 | 8730.5 | +12.3% | +11.9% | +12.6% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | str_contains() loop | 4421.8 | 3956.3 | -10.6% | -10.8% | -10.0% |
| [Check a detailed ZH support message: a promotional phrase is quoted](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | preg_match() | 3013.9 | 3956.3 | +31.0% | +30.2% | +31.5% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 18607.7 | 31156.0 | +67.4% | +66.3% | +67.5% |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 11693.2 | 31156.0 | +166.4% | +164.4% | +166.6% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 9284.9 | 2046.8 | -78.0% | -78.6% | -77.9% |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 1017.1 | 2046.8 | +101.3% | +100.8% | +102.9% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 10431.0 | 17445.2 | +67.3% | +63.9% | +67.4% |
| [Decide whether a request trace needs an alert: error in the middle record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 6454.9 | 17445.2 | +170.3% | +169.4% | +171.4% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | str_contains() loop | 11365.0 | 30893.5 | +171.8% | +171.5% | +171.9% |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | 8 | preg_match() | 11158.4 | 30893.5 | +176.9% | +176.2% | +177.8% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 1337.9 | 3105.8 | +132.2% | +129.1% | +132.6% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 2218.4 | 3105.8 | +39.6% | +39.4% | +45.2% |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 1318.5 | 3105.8 | +135.6% | +132.6% | +141.2% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | strtr() | 8569.2 | 22538.0 | +162.9% | +159.8% | +163.8% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | preg_replace_callback() | 14554.7 | 22538.0 | +56.1% | +53.2% | +58.7% |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | 6 | str_replace() | 7694.3 | 22538.0 | +193.3% | +183.7% | +200.6% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 758.4 | 1629.6 | +115.0% | +113.8% | +117.3% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 730.0 | 1629.6 | +122.5% | +120.0% | +127.1% |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 768.2 | 1629.6 | +111.5% | +111.4% | +113.7% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | strtr() | 1215.1 | 2489.4 | +104.2% | +101.2% | +105.6% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | preg_replace_callback() | 2498.1 | 2489.4 | -0.2% | -2.3% | +0.4% |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | str_replace() | 1439.7 | 2489.4 | +73.1% | +71.4% | +73.8% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | strtr() | 845.7 | 1209.1 | +43.4% | +40.4% | +45.8% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace_callback() | 1644.2 | 1209.1 | -26.3% | -27.2% | -24.4% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | str_replace() | 908.3 | 1209.1 | +33.6% | +29.9% | +36.2% |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 4 | preg_replace() | 891.7 | 1209.1 | +36.6% | +34.8% | +38.1% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 1411.4 | 1646.5 | +16.6% | +15.3% | +17.2% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 812.1 | 1646.5 | +102.8% | +94.3% | +107.0% |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 1088.9 | 1646.5 | +51.0% | +49.2% | +52.4% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 1812.4 | 2782.7 | +53.5% | +46.2% | +54.6% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 1798.9 | 2782.7 | +54.6% | +52.0% | +57.5% |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 1703.9 | 2782.7 | +63.2% | +62.6% | +64.2% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | strtr() | 12163.5 | 19905.3 | +63.6% | +62.9% | +64.0% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | preg_replace_callback() | 11499.3 | 19905.3 | +73.6% | +72.0% | +75.5% |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | 8 | str_replace() | 10690.6 | 19905.3 | +86.8% | +85.2% | +87.4% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 24667.8 | 67335.1 | +173.0% | +172.3% | +173.5% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 2163.1 | 67335.1 | +3010.8% | +2995.8% | +3017.6% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 49156.8 | 67335.1 | +36.9% | +35.7% | +37.1% |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 2060.3 | 67335.1 | +3169.8% | +3116.2% | +3190.6% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 25426.9 | 71202.8 | +180.0% | +179.9% | +180.2% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 3268.4 | 71202.8 | +2079.2% | +2068.3% | +2086.0% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 52363.6 | 71202.8 | +36.0% | +34.9% | +36.1% |
| [Mask one registered secret in a request log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 2592.1 | 71202.8 | +2645.8% | +2638.4% | +2661.3% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 38448.2 | 108882.3 | +183.2% | +182.0% | +183.3% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 5312.9 | 108882.3 | +1949.2% | +1934.5% | +1957.8% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 85459.3 | 108882.3 | +27.4% | +25.2% | +27.4% |
| [Mask three registered secrets in an incident log excerpt](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 3729.5 | 108882.3 | +2818.9% | +2796.6% | +2824.0% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | strtr() | 305471.6 | 846981.8 | +177.3% | +175.3% | +177.8% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace_callback() | 21067.3 | 846981.8 | +3920.3% | +3873.9% | +3945.9% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | str_replace() | 644040.9 | 846981.8 | +31.5% | +31.4% | +31.6% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | preg_replace() | 19144.0 | 846981.8 | +4324.5% | +4252.5% | +4344.5% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 722.5 | 1252.6 | +73.4% | +72.2% | +73.8% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 810.4 | 1252.6 | +54.6% | +42.8% | +57.4% |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 922.9 | 1252.6 | +35.9% | +35.3% | +36.1% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | strtr() | 905.3 | 1512.5 | +67.0% | +50.8% | +71.7% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | preg_replace_callback() | 1451.8 | 1512.5 | +4.3% | +3.9% | +8.0% |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | str_replace() | 1160.8 | 1512.5 | +31.0% | +30.2% | +33.8% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 58676.1 | 9115.2 | -84.5% | -84.6% | -84.3% |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | preg_match() per term | 68172.3 | 9115.2 | -86.6% | -86.7% | -86.4% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 50763.9 | 6226.3 | -87.7% | -87.8% | -87.6% |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 81860.6 | 6226.3 | -92.4% | -92.5% | -92.3% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | strpos() per term | 71333.1 | 10966.3 | -84.6% | -84.8% | -84.4% |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | PCRE lookahead per term | 161228.6 | 10966.3 | -93.2% | -93.3% | -93.1% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 135224.6 | 8143.7 | -94.0% | -94.0% | -93.9% |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 42671.0 | 8143.7 | -80.9% | -81.0% | -80.6% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | strtr() | 1078899.4 | 61630.2 | -94.3% | -94.3% | -94.3% |
| [Publish eight different help articles using one link glossary](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | preg_replace_callback() | 337724.0 | 61630.2 | -81.8% | -81.8% | -81.7% |

### Synthetic tasks

#### Dictionary preparation included

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 1744.4 | 423602.5 | +24310.8% | +23097.3% | +24867.6% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 85460.5 | 423602.5 | +395.8% | +375.3% | +402.9% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 83912.0 | 423602.5 | +407.0% | +388.0% | +412.1% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 1389.2 | 76197.8 | +5377.0% | +5332.3% | +5430.7% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 83409.6 | 76197.8 | -8.5% | -9.2% | -8.1% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 82235.8 | 76197.8 | -7.6% | -7.7% | -6.9% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | strtr() | 1383.0 | 5323.3 | +285.5% | +273.3% | +286.2% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace_callback() | 22324.5 | 5323.3 | -76.2% | -77.7% | -76.1% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace() | 18433.1 | 5323.3 | -71.2% | -71.4% | -70.7% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | strtr() | 1144.9 | 3017.9 | +163.8% | +163.6% | +164.2% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | preg_replace_callback() | 6241.5 | 3017.9 | -51.5% | -52.1% | -51.4% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 1684.4 | 385089.4 | +22775.5% | +22727.2% | +23102.4% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 92181.0 | 385089.4 | +316.5% | +306.9% | +318.7% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 91322.6 | 385089.4 | +322.6% | +313.8% | +327.3% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 1331.5 | 64788.6 | +4765.8% | +4675.5% | +4875.1% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 95538.2 | 64788.6 | -32.3% | -38.4% | -29.6% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 92383.1 | 64788.6 | -29.9% | -31.7% | -26.9% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | strtr() | 1269.3 | 5183.4 | +307.7% | +303.8% | +317.7% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace_callback() | 23014.3 | 5183.4 | -77.4% | -77.6% | -77.2% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace() | 18706.1 | 5183.4 | -72.3% | -72.4% | -71.7% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | strtr() | 1033.7 | 2992.0 | +189.5% | +186.4% | +193.6% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | preg_replace_callback() | 5844.3 | 2992.0 | -48.8% | -49.1% | -47.7% |

#### Dictionary already prepared

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 1761.7 | 2468.0 | +40.1% | +38.5% | +42.8% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 4074.2 | 2468.0 | -39.4% | -39.9% | -39.1% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 2984.0 | 2468.0 | -17.4% | -17.7% | -16.8% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 1407.0 | 2452.6 | +74.3% | +73.1% | +76.2% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 2934.3 | 2452.6 | -16.1% | -18.1% | -15.5% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 2044.1 | 2452.6 | +20.3% | +19.1% | +22.1% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | strtr() | 1389.4 | 2447.2 | +76.0% | +75.8% | +77.6% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace_callback() | 4790.9 | 2447.2 | -48.9% | -51.0% | -48.6% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace() | 1485.5 | 2447.2 | +64.7% | -15.5% | +66.5% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | strtr() | 1151.8 | 1178.6 | +2.7% | +1.9% | +4.3% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | preg_replace_callback() | 2632.9 | 1178.6 | -55.2% | -56.7% | -54.7% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 1679.1 | 2589.0 | +54.2% | +52.5% | +56.5% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 3983.1 | 2589.0 | -34.8% | -36.9% | -34.3% |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 2846.5 | 2589.0 | -8.9% | -11.9% | -8.5% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | strtr() | 1336.2 | 2558.7 | +91.6% | +88.1% | +92.8% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace_callback() | 3081.7 | 2558.7 | -17.1% | -17.4% | -13.7% |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | 64 | preg_replace() | 1866.6 | 2558.7 | +37.2% | +34.2% | +47.6% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | strtr() | 1268.2 | 2639.1 | +108.1% | +107.1% | +108.6% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace_callback() | 5413.3 | 2639.1 | -51.3% | -51.4% | -51.0% |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | 16 | preg_replace() | 1447.4 | 2639.1 | +82.3% | +81.8% | +84.4% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | strtr() | 1032.3 | 1319.1 | +28.3% | +27.6% | +29.2% |
| [Correctness control: regex punctuation and literal replacement bytes](../../corpus/multi-pattern-product/suites/synthetic.json) | 4 | preg_replace_callback() | 2618.6 | 1319.1 | -49.5% | -49.7% | -49.3% |

## Size series

### Product tasks

#### Dictionary preparation included

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 1239.6 | 6441.2 | +422.5% | +415.9% | +438.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 3261.1 | 6441.2 | +99.7% | +96.5% | +105.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | str_contains() loop | 900.2 | 5766.9 | +540.6% | +529.2% | +587.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | preg_match() | 2883.3 | 5766.9 | +100.6% | +96.8% | +114.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | str_contains() loop | 1065.4 | 6727.7 | +531.4% | +525.8% | +556.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | preg_match() | 3420.5 | 6727.7 | +97.0% | +95.8% | +105.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | str_contains() loop | 961.6 | 6884.1 | +617.6% | +612.4% | +620.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | preg_match() | 3401.4 | 6884.1 | +101.8% | +100.5% | +105.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 4343.6 | 13732.9 | +216.9% | +213.3% | +218.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 7050.7 | 13732.9 | +94.6% | +93.2% | +96.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | str_contains() loop | 1776.4 | 8741.4 | +393.7% | +391.1% | +396.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | preg_match() | 4437.5 | 8741.4 | +97.0% | +96.0% | +97.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 1911.7 | 16434.4 | +757.6% | +751.0% | +791.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 5699.3 | 16434.4 | +189.2% | +187.7% | +198.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | str_contains() loop | 1225.1 | 15816.8 | +1199.7% | +1183.8% | +1225.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | preg_match() | 4786.1 | 15816.8 | +231.7% | +229.6% | +237.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | str_contains() loop | 1472.8 | 16870.6 | +1045.2% | +1031.8% | +1083.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | preg_match() | 5973.4 | 16870.6 | +182.4% | +180.4% | +189.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | str_contains() loop | 1299.1 | 16922.5 | +1200.6% | +1180.0% | +1222.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | preg_match() | 6066.2 | 16922.5 | +179.0% | +177.9% | +182.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 7429.2 | 23340.9 | +218.9% | +210.9% | +220.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 15974.9 | 23340.9 | +46.3% | +44.7% | +49.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | str_contains() loop | 2593.3 | 18468.3 | +615.2% | +610.0% | +642.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | preg_match() | 8020.9 | 18468.3 | +130.3% | +127.9% | +139.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 3412.4 | 48746.8 | +1329.0% | +1314.7% | +1348.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 11496.1 | 48746.8 | +323.6% | +318.0% | +327.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | str_contains() loop | 2061.8 | 48455.5 | +2275.6% | +2204.0% | +2318.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | preg_match() | 8834.1 | 48455.5 | +449.7% | +447.7% | +458.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | str_contains() loop | 2584.8 | 49844.4 | +1824.5% | +1779.8% | +1851.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | preg_match() | 12426.5 | 49844.4 | +299.6% | +297.2% | +305.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | str_contains() loop | 2108.9 | 49278.2 | +2239.2% | +2164.4% | +2253.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | preg_match() | 12618.2 | 49278.2 | +290.5% | +287.1% | +294.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 16706.8 | 57429.6 | +243.6% | +242.7% | +252.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 38302.2 | 57429.6 | +49.9% | +49.2% | +54.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | str_contains() loop | 6220.8 | 52375.7 | +742.6% | +732.6% | +756.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | preg_match() | 19191.8 | 52375.7 | +172.8% | +171.3% | +177.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 6288.0 | 98250.4 | +1455.7% | +1451.8% | +1515.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 22184.4 | 98250.4 | +343.4% | +341.3% | +350.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | str_contains() loop | 3786.2 | 97357.8 | +2499.1% | +2454.1% | +2526.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | preg_match() | 16292.4 | 97357.8 | +496.3% | +495.4% | +505.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | str_contains() loop | 5030.6 | 98649.1 | +1866.8% | +1847.4% | +1896.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | preg_match() | 24033.6 | 98649.1 | +308.2% | +306.5% | +317.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | str_contains() loop | 3922.8 | 98472.8 | +2413.4% | +2351.2% | +2429.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | preg_match() | 24552.8 | 98472.8 | +301.3% | +295.5% | +301.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 31798.8 | 106442.2 | +234.1% | +225.5% | +235.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 77635.6 | 106442.2 | +37.1% | +37.1% | +39.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | str_contains() loop | 13047.4 | 101688.8 | +677.6% | +656.9% | +682.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | preg_match() | 38797.0 | 101688.8 | +161.6% | +158.4% | +162.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 12839.5 | 219127.9 | +1608.3% | +1573.4% | +1656.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 44860.5 | 219127.9 | +388.8% | +385.0% | +389.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | str_contains() loop | 7266.9 | 218342.1 | +2904.6% | +2874.4% | +3007.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | preg_match() | 31682.6 | 218342.1 | +587.0% | +580.6% | +598.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | str_contains() loop | 9611.7 | 218706.6 | +2177.8% | +2134.8% | +2251.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | preg_match() | 47551.3 | 218706.6 | +360.4% | +357.1% | +361.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | str_contains() loop | 7245.6 | 219487.6 | +2926.9% | +2910.6% | +2945.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | preg_match() | 49031.0 | 219487.6 | +348.5% | +341.3% | +348.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 64747.2 | 221037.6 | +241.4% | +239.4% | +259.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 158932.0 | 221037.6 | +39.0% | +38.4% | +40.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | str_contains() loop | 26280.9 | 215550.6 | +719.7% | +717.6% | +762.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | preg_match() | 78280.8 | 215550.6 | +175.6% | +174.7% | +179.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 31140.1 | 406082.7 | +1203.2% | +1157.1% | +1236.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 90156.2 | 406082.7 | +349.7% | +346.6% | +351.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | str_contains() loop | 15226.2 | 404056.3 | +2552.3% | +2392.6% | +2634.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | preg_match() | 63204.0 | 404056.3 | +539.9% | +537.9% | +543.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | str_contains() loop | 21840.3 | 406819.3 | +1758.0% | +1746.9% | +1911.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | preg_match() | 94873.6 | 406819.3 | +328.9% | +325.2% | +334.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | str_contains() loop | 15370.2 | 405779.2 | +2540.0% | +2331.7% | +2611.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | preg_match() | 98093.1 | 405779.2 | +314.6% | +310.0% | +315.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 139386.7 | 410466.1 | +194.4% | +181.5% | +195.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 313708.7 | 410466.1 | +30.9% | +30.5% | +31.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | str_contains() loop | 53437.9 | 406122.2 | +660.4% | +632.5% | +666.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | preg_match() | 155219.4 | 406122.2 | +162.0% | +161.2% | +162.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 74792.9 | 761690.1 | +913.1% | +893.9% | +924.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 231137.2 | 761690.1 | +230.9% | +224.7% | +247.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | str_contains() loop | 39049.3 | 759690.5 | +1850.0% | +1747.0% | +1857.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | preg_match() | 125258.1 | 759690.5 | +506.2% | +504.2% | +511.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | str_contains() loop | 55621.8 | 763040.8 | +1280.9% | +1265.4% | +1338.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | preg_match() | 247267.6 | 763040.8 | +210.9% | +194.2% | +213.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | str_contains() loop | 39646.1 | 762013.2 | +1827.6% | +1746.9% | +1831.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | preg_match() | 260244.9 | 762013.2 | +192.3% | +182.4% | +196.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 317454.9 | 769502.3 | +142.6% | +134.5% | +143.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 1115695.8 | 769502.3 | -30.9% | -34.1% | -27.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | str_contains() loop | 121745.0 | 763423.2 | +529.1% | +522.4% | +559.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | preg_match() | 489958.4 | 763423.2 | +55.3% | +48.6% | +63.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 5397.9 | 15024.0 | +178.3% | +176.0% | +185.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | preg_match() per term | 9715.8 | 15024.0 | +54.3% | +53.0% | +60.2% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 4418.5 | 14684.4 | +233.3% | +229.5% | +247.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 10800.7 | 14684.4 | +37.9% | +35.2% | +42.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 6727.0 | 15368.8 | +129.3% | +125.0% | +136.0% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 17209.0 | 15368.8 | -10.6% | -11.0% | -7.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 10062.8 | 25132.2 | +152.5% | +147.4% | +155.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | preg_match() per term | 18026.4 | 25132.2 | +38.2% | +37.7% | +43.2% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 8495.4 | 24756.3 | +191.2% | +187.7% | +202.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 20393.7 | 24756.3 | +21.8% | +21.2% | +22.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 12448.2 | 25928.2 | +108.3% | +107.1% | +109.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 31794.8 | 25928.2 | -17.8% | -19.5% | -17.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 17784.5 | 44744.4 | +151.4% | +143.7% | +156.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | preg_match() per term | 34588.7 | 44744.4 | +29.8% | +29.2% | +30.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 15339.6 | 43709.7 | +184.6% | +182.7% | +196.1% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 38555.1 | 43709.7 | +13.4% | +12.3% | +15.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 23141.4 | 45510.3 | +96.9% | +91.4% | +98.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 59782.1 | 45510.3 | -23.9% | -24.6% | -23.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 36242.5 | 97310.1 | +168.8% | +157.4% | +169.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | preg_match() per term | 66786.1 | 97310.1 | +45.7% | +40.8% | +49.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 31210.3 | 94918.0 | +204.6% | +203.8% | +208.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 75597.3 | 94918.0 | +26.7% | +22.4% | +27.0% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 46968.8 | 97545.4 | +110.7% | +105.9% | +115.3% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 113889.8 | 97545.4 | -14.1% | -14.4% | -13.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 75808.6 | 223548.0 | +195.5% | +194.3% | +196.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | preg_match() per term | 131919.4 | 223548.0 | +69.4% | +69.1% | +72.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 65160.5 | 220471.8 | +238.4% | +227.6% | +242.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 229769.7 | 220471.8 | -3.7% | -4.3% | -3.3% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 88352.2 | 225905.0 | +154.4% | +150.3% | +157.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 303310.8 | 225905.0 | -25.7% | -31.0% | -24.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 148018.8 | 478838.0 | +224.3% | +217.0% | +224.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | preg_match() per term | 277228.0 | 478838.0 | +73.1% | +71.1% | +74.9% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 143203.5 | 475238.7 | +232.8% | +229.4% | +236.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 522807.4 | 475238.7 | -8.9% | -9.3% | -8.8% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 164478.7 | 481672.4 | +193.4% | +188.3% | +193.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 627314.1 | 481672.4 | -23.2% | -24.2% | -22.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 287746.8 | 1395560.3 | +384.8% | +382.3% | +391.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | preg_match() per term | 620279.9 | 1395560.3 | +125.2% | +122.2% | +126.6% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 283004.4 | 1395545.8 | +389.5% | +384.5% | +393.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 1101800.5 | 1395545.8 | +26.5% | +25.6% | +27.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 307297.9 | 1405375.5 | +356.2% | +350.5% | +359.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 1268734.0 | 1405375.5 | +10.9% | +9.6% | +11.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 20699.1 | 17108.7 | -17.2% | -17.9% | -16.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 10231.1 | 17108.7 | +67.4% | +65.0% | +68.0% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 162609.3 | 56041.3 | -65.5% | -65.8% | -65.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 29789.3 | 56041.3 | +88.6% | +87.8% | +89.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 36862.2 | 29528.9 | -19.9% | -20.0% | -17.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 23713.9 | 29528.9 | +24.8% | +23.6% | +27.3% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 293180.0 | 70971.0 | -75.8% | -75.9% | -75.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 84699.2 | 70971.0 | -16.6% | -16.7% | -15.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 78020.8 | 53122.6 | -31.3% | -32.2% | -30.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 48234.2 | 53122.6 | +10.0% | +9.7% | +12.0% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 620314.6 | 97999.0 | -84.2% | -84.3% | -84.1% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 168056.2 | 97999.0 | -41.6% | -42.1% | -41.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 143522.8 | 112021.9 | -21.9% | -22.2% | -21.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 104087.7 | 112021.9 | +7.9% | +6.0% | +8.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 1144727.7 | 160796.1 | -86.0% | -86.0% | -85.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 324264.0 | 160796.1 | -50.4% | -50.5% | -50.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 175568.0 | 239060.3 | +35.6% | +34.5% | +36.4% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 211161.6 | 239060.3 | +13.3% | +12.2% | +14.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 1397908.3 | 291214.1 | -79.2% | -79.4% | -79.1% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 562196.7 | 291214.1 | -48.4% | -48.7% | -48.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 191725.9 | 486291.3 | +153.7% | +152.5% | +155.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 504331.4 | 486291.3 | -3.4% | -5.0% | -2.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 1531021.2 | 538189.9 | -64.9% | -64.9% | -64.8% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 1233252.3 | 538189.9 | -56.4% | -56.8% | -56.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 195896.6 | 1276418.7 | +551.6% | +546.9% | +555.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 1236594.9 | 1276418.7 | +3.3% | +1.7% | +5.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 1565865.7 | 1400326.0 | -10.6% | -10.8% | -10.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 3451675.9 | 1400326.0 | -59.4% | -59.6% | -57.5% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 1247.8 | 6196.3 | +396.3% | +394.2% | +398.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 3099.3 | 6196.3 | +101.0% | +98.1% | +101.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | str_contains() loop | 888.3 | 5450.4 | +512.6% | +508.8% | +552.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | preg_match() | 2736.8 | 5450.4 | +98.4% | +97.9% | +109.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | str_contains() loop | 1053.3 | 6579.9 | +526.2% | +519.1% | +533.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | preg_match() | 3256.7 | 6579.9 | +103.0% | +102.0% | +103.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | str_contains() loop | 949.0 | 6703.6 | +612.5% | +605.6% | +635.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | preg_match() | 3261.1 | 6703.6 | +108.4% | +104.9% | +112.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 4411.8 | 14244.3 | +222.9% | +220.9% | +223.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 6742.5 | 14244.3 | +110.5% | +109.1% | +112.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | str_contains() loop | 1760.4 | 8733.7 | +396.1% | +394.6% | +397.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | preg_match() | 4199.4 | 8733.7 | +108.0% | +107.6% | +109.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 1993.4 | 15699.3 | +682.5% | +676.2% | +709.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 5637.7 | 15699.3 | +178.8% | +175.8% | +181.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | str_contains() loop | 1250.7 | 14878.6 | +1104.0% | +993.3% | +1108.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | preg_match() | 4816.0 | 14878.6 | +209.9% | +206.6% | +212.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | str_contains() loop | 1493.2 | 16113.8 | +984.8% | +974.1% | +993.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | preg_match() | 5929.8 | 16113.8 | +172.6% | +171.7% | +174.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | str_contains() loop | 1311.2 | 16177.1 | +1138.4% | +1111.8% | +1146.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | preg_match() | 6001.9 | 16177.1 | +169.5% | +166.6% | +171.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 7472.4 | 23327.2 | +213.0% | +208.6% | +215.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 15699.2 | 23327.2 | +48.7% | +47.9% | +50.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | str_contains() loop | 2565.4 | 17788.5 | +593.8% | +588.8% | +607.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | preg_match() | 7858.8 | 17788.5 | +126.0% | +124.5% | +131.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 3675.9 | 46085.3 | +1148.6% | +1133.7% | +1188.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 11631.6 | 46085.3 | +296.1% | +290.4% | +299.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | str_contains() loop | 2159.4 | 45280.8 | +1996.9% | +1923.8% | +2013.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | preg_match() | 9077.2 | 45280.8 | +400.4% | +388.7% | +405.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | str_contains() loop | 2701.0 | 46711.2 | +1632.2% | +1588.0% | +1643.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | preg_match() | 12528.2 | 46711.2 | +273.3% | +272.4% | +275.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | str_contains() loop | 2248.4 | 46585.3 | +1968.3% | +1956.8% | +2007.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | preg_match() | 12781.0 | 46585.3 | +265.5% | +263.6% | +271.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 16908.3 | 55335.7 | +226.1% | +225.5% | +229.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 37905.1 | 55335.7 | +45.9% | +44.5% | +46.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | str_contains() loop | 6225.3 | 49724.0 | +698.9% | +693.1% | +703.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | preg_match() | 19257.2 | 49724.0 | +159.1% | +155.9% | +160.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 6833.4 | 93046.4 | +1261.6% | +1233.3% | +1270.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 22943.5 | 93046.4 | +305.5% | +304.3% | +307.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | str_contains() loop | 4063.4 | 92307.3 | +2170.3% | +2153.5% | +2198.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | preg_match() | 16735.4 | 92307.3 | +451.6% | +447.4% | +457.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | str_contains() loop | 5275.3 | 93222.1 | +1675.0% | +1655.3% | +1700.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | preg_match() | 24662.3 | 93222.1 | +279.2% | +275.9% | +283.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | str_contains() loop | 4217.5 | 93411.3 | +2113.0% | +2054.9% | +2117.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | preg_match() | 25333.5 | 93411.3 | +267.5% | +266.5% | +270.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 33524.8 | 102444.2 | +204.8% | +202.6% | +207.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 80615.7 | 102444.2 | +27.0% | +26.4% | +27.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | str_contains() loop | 13421.9 | 96635.6 | +619.9% | +619.3% | +623.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | preg_match() | 40010.8 | 96635.6 | +141.9% | +139.5% | +143.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 14374.6 | 204752.7 | +1323.8% | +1301.8% | +1355.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 44978.0 | 204752.7 | +355.0% | +353.1% | +358.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | str_contains() loop | 7768.5 | 203686.5 | +2522.0% | +2490.1% | +2571.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | preg_match() | 32711.0 | 203686.5 | +521.5% | +506.5% | +525.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | str_contains() loop | 10143.0 | 205831.0 | +1929.8% | +1920.5% | +1936.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | preg_match() | 47609.1 | 205831.0 | +331.9% | +330.2% | +333.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | str_contains() loop | 7960.0 | 206495.3 | +2486.2% | +2479.7% | +2502.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | preg_match() | 48895.5 | 206495.3 | +321.4% | +318.5% | +322.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 65949.0 | 208719.3 | +217.2% | +215.6% | +219.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 153637.2 | 208719.3 | +35.7% | +35.5% | +36.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | str_contains() loop | 26326.4 | 202278.1 | +668.0% | +664.1% | +681.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | preg_match() | 76991.9 | 202278.1 | +163.1% | +162.4% | +165.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 35267.8 | 388669.4 | +996.7% | +995.9% | +1003.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 90984.4 | 388669.4 | +327.2% | +296.2% | +332.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | str_contains() loop | 17259.1 | 386284.3 | +2137.1% | +2127.6% | +2158.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | preg_match() | 64373.9 | 386284.3 | +497.7% | +477.6% | +509.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | str_contains() loop | 23127.1 | 386555.0 | +1571.4% | +1563.7% | +1582.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | preg_match() | 98486.1 | 386555.0 | +292.4% | +275.6% | +303.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | str_contains() loop | 17679.0 | 388755.6 | +2095.8% | +2071.5% | +2116.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | preg_match() | 98617.3 | 388755.6 | +294.7% | +261.0% | +296.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 149984.0 | 394702.6 | +162.5% | +160.8% | +165.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 323173.7 | 394702.6 | +22.3% | +6.0% | +27.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | str_contains() loop | 55512.7 | 387352.1 | +599.2% | +596.4% | +602.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | preg_match() | 176542.1 | 387352.1 | +120.3% | +118.8% | +130.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 80389.6 | 728779.1 | +806.6% | +801.5% | +812.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 227755.1 | 728779.1 | +220.0% | +219.0% | +233.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | str_contains() loop | 43421.2 | 728461.9 | +1575.5% | +1565.7% | +1580.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | preg_match() | 127927.5 | 728461.9 | +469.7% | +455.5% | +483.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | str_contains() loop | 58340.6 | 727792.2 | +1146.5% | +1135.8% | +1153.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | preg_match() | 249326.6 | 727792.2 | +191.1% | +185.3% | +194.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | str_contains() loop | 43606.7 | 731381.8 | +1573.0% | +1567.0% | +1618.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | preg_match() | 262012.3 | 731381.8 | +178.4% | +171.2% | +187.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 335382.5 | 736223.3 | +119.3% | +116.6% | +119.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 1131641.3 | 736223.3 | -34.8% | -36.4% | -32.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | str_contains() loop | 123146.5 | 731132.6 | +492.9% | +490.4% | +499.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | preg_match() | 498227.2 | 731132.6 | +46.6% | +40.3% | +50.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 5399.3 | 15372.4 | +184.4% | +183.2% | +184.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | preg_match() per term | 9240.4 | 15372.4 | +66.0% | +64.7% | +68.1% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 4500.8 | 14494.3 | +222.2% | +218.5% | +224.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 10371.9 | 14494.3 | +39.5% | +38.3% | +41.3% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 6663.8 | 15707.4 | +135.6% | +134.8% | +138.8% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 16426.4 | 15707.4 | -4.4% | -5.0% | -4.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 10178.5 | 24392.8 | +140.0% | +138.7% | +143.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | preg_match() per term | 17131.7 | 24392.8 | +42.3% | +41.1% | +44.9% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 8635.7 | 23537.9 | +172.8% | +170.9% | +173.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 19700.2 | 23537.9 | +19.8% | +17.6% | +20.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 12668.2 | 25271.6 | +99.5% | +98.7% | +100.6% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 30530.8 | 25271.6 | -17.5% | -17.7% | -17.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 18656.2 | 43166.7 | +131.7% | +130.3% | +135.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | preg_match() per term | 33576.0 | 43166.7 | +28.1% | +27.9% | +30.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 15788.0 | 41427.2 | +162.4% | +161.4% | +165.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 37096.3 | 41427.2 | +11.7% | +10.2% | +13.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 23842.5 | 43837.0 | +83.9% | +81.9% | +84.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 57826.0 | 43837.0 | -24.1% | -25.2% | -23.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 38529.0 | 93117.4 | +141.6% | +139.8% | +143.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | preg_match() per term | 65236.3 | 93117.4 | +42.7% | +42.2% | +43.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 33956.8 | 90396.5 | +166.6% | +165.3% | +168.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 74198.4 | 90396.5 | +21.6% | +20.1% | +23.6% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 48245.8 | 94078.2 | +95.1% | +93.4% | +99.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 111390.5 | 94078.2 | -15.5% | -16.4% | -13.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 77225.0 | 211364.6 | +173.6% | +173.1% | +174.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | preg_match() per term | 127724.0 | 211364.6 | +65.1% | +64.6% | +66.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 68687.1 | 208373.0 | +203.4% | +202.5% | +204.2% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 223378.5 | 208373.0 | -7.0% | -7.9% | -6.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 91253.1 | 214511.4 | +135.1% | +133.7% | +136.8% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 294156.4 | 214511.4 | -27.0% | -28.5% | -26.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 152841.3 | 461238.3 | +202.3% | +200.0% | +202.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | preg_match() per term | 268682.5 | 461238.3 | +71.8% | +70.0% | +73.2% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 146170.3 | 458875.3 | +213.9% | +213.2% | +219.1% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 511034.2 | 458875.3 | -10.1% | -10.5% | -9.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 168390.3 | 463551.9 | +175.9% | +174.6% | +177.6% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 613979.4 | 463551.9 | -24.5% | -25.1% | -23.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 293711.6 | 1343370.1 | +357.4% | +356.6% | +359.0% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | preg_match() per term | 602007.8 | 1343370.1 | +123.1% | +122.1% | +125.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 290593.9 | 1340275.6 | +361.2% | +358.3% | +363.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 1076533.6 | 1340275.6 | +24.5% | +23.2% | +25.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 314609.2 | 1354838.4 | +331.0% | +329.5% | +331.1% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 1234754.3 | 1354838.4 | +9.8% | +8.8% | +9.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 20049.5 | 16894.3 | -15.6% | -16.0% | -14.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 9864.8 | 16894.3 | +71.9% | +70.2% | +72.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 157719.9 | 59813.3 | -62.1% | -62.7% | -61.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 29343.5 | 59813.3 | +103.9% | +103.0% | +104.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 36034.7 | 28333.5 | -21.2% | -23.1% | -20.5% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 23113.5 | 28333.5 | +22.7% | +18.8% | +23.3% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 288958.6 | 72508.2 | -74.9% | -75.1% | -74.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 83533.3 | 72508.2 | -13.3% | -14.1% | -12.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 77364.7 | 50270.0 | -34.9% | -35.3% | -34.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 47371.4 | 50270.0 | +5.9% | +5.2% | +6.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 616724.6 | 97393.1 | -84.2% | -84.3% | -84.1% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 167218.4 | 97393.1 | -41.7% | -42.4% | -41.4% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 144027.0 | 107517.7 | -25.4% | -25.6% | -25.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 101675.7 | 107517.7 | +5.7% | +4.8% | +6.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 1150370.7 | 157517.2 | -86.3% | -86.3% | -86.3% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 320879.6 | 157517.2 | -51.0% | -51.1% | -50.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 177116.9 | 225632.3 | +27.4% | +27.0% | +28.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 209815.6 | 225632.3 | +7.4% | -30.8% | +8.1% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 1414134.0 | 276488.4 | -80.4% | -80.6% | -80.3% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 589080.8 | 276488.4 | -53.1% | -53.3% | -52.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 193908.7 | 464447.3 | +139.4% | +139.2% | +142.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 483123.1 | 464447.3 | -3.4% | -3.9% | -2.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 1550856.9 | 518808.0 | -66.6% | -66.7% | -66.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 1202824.7 | 518808.0 | -57.0% | -60.3% | -56.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 198217.4 | 1225484.4 | +518.9% | +515.5% | +522.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 1165943.3 | 1225484.4 | +4.9% | +3.1% | +6.3% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 1582818.4 | 1349409.0 | -14.7% | -15.2% | -9.1% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 3305756.6 | 1349409.0 | -58.9% | -60.9% | -56.5% |

#### Dictionary already prepared

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 1229.3 | 1227.2 | -0.1% | -0.3% | +0.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 1061.9 | 1227.2 | +15.8% | +14.2% | +17.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | str_contains() loop | 902.3 | 549.0 | -39.3% | -39.8% | -37.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | preg_match() | 689.9 | 549.0 | -20.5% | -21.5% | -18.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | str_contains() loop | 1070.9 | 1558.0 | +45.6% | +44.3% | +47.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | preg_match() | 1232.7 | 1558.0 | +26.5% | +26.1% | +27.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | str_contains() loop | 960.2 | 1677.8 | +74.5% | +74.3% | +76.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | preg_match() | 1210.0 | 1677.8 | +38.5% | +37.1% | +39.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 4312.3 | 8562.8 | +98.7% | +95.4% | +99.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 4856.6 | 8562.8 | +76.4% | +76.2% | +76.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | str_contains() loop | 1782.0 | 3535.3 | +98.4% | +94.5% | +101.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | preg_match() | 2249.1 | 3535.3 | +57.0% | +56.0% | +57.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 1889.0 | 1233.8 | -34.7% | -36.4% | -34.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 1565.5 | 1233.8 | -21.3% | -22.4% | -20.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | str_contains() loop | 1228.4 | 546.7 | -55.9% | -56.2% | -55.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | preg_match() | 729.3 | 546.7 | -25.2% | -26.3% | -24.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | str_contains() loop | 1458.7 | 1567.7 | +7.0% | +4.8% | +8.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | preg_match() | 1848.9 | 1567.7 | -15.2% | -16.0% | -14.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | str_contains() loop | 1300.7 | 1676.4 | +29.3% | +28.7% | +30.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | preg_match() | 1939.1 | 1676.4 | -13.6% | -14.9% | -13.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 7412.2 | 8569.3 | +15.5% | +15.3% | +17.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 11838.5 | 8569.3 | -27.5% | -28.0% | -27.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | str_contains() loop | 2592.8 | 3535.0 | +36.1% | +34.9% | +39.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | preg_match() | 3909.2 | 3535.0 | -9.6% | -9.9% | -8.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 3377.8 | 1235.4 | -63.5% | -64.2% | -62.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 3447.1 | 1235.4 | -64.2% | -64.5% | -63.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | str_contains() loop | 2066.9 | 563.1 | -72.7% | -73.1% | -72.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | preg_match() | 791.9 | 563.1 | -29.1% | -30.3% | -27.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | str_contains() loop | 2625.5 | 1563.6 | -40.2% | -41.1% | -38.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | preg_match() | 4336.5 | 1563.6 | -63.9% | -64.0% | -63.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | str_contains() loop | 2133.3 | 1683.6 | -21.1% | -21.5% | -19.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | preg_match() | 4519.5 | 1683.6 | -62.8% | -63.0% | -62.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 16721.4 | 8573.3 | -48.7% | -49.5% | -48.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 30146.0 | 8573.3 | -71.6% | -71.6% | -71.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | str_contains() loop | 6236.8 | 3538.8 | -43.3% | -43.5% | -43.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | preg_match() | 11101.8 | 3538.8 | -68.1% | -68.2% | -68.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 6166.8 | 1245.1 | -79.8% | -80.7% | -79.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 6770.2 | 1245.1 | -81.6% | -81.7% | -81.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | str_contains() loop | 3811.3 | 551.7 | -85.4% | -85.8% | -85.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | preg_match() | 953.8 | 551.7 | -42.2% | -43.4% | -40.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | str_contains() loop | 5044.7 | 1597.0 | -68.3% | -68.4% | -67.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | preg_match() | 8432.0 | 1597.0 | -81.1% | -81.1% | -81.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | str_contains() loop | 3943.1 | 1711.0 | -56.4% | -57.8% | -56.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | preg_match() | 9058.7 | 1711.0 | -81.1% | -81.2% | -81.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 31858.2 | 8631.5 | -72.9% | -73.9% | -72.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 62209.3 | 8631.5 | -86.1% | -86.2% | -86.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | str_contains() loop | 13043.9 | 3570.9 | -72.6% | -73.4% | -72.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | preg_match() | 23161.4 | 3570.9 | -84.6% | -84.6% | -84.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 12356.0 | 1270.9 | -89.7% | -90.3% | -89.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 13639.9 | 1270.9 | -90.6% | -90.7% | -90.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | str_contains() loop | 7333.0 | 545.6 | -92.5% | -92.6% | -92.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | preg_match() | 1217.9 | 545.6 | -55.2% | -56.7% | -52.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | str_contains() loop | 9513.7 | 1619.8 | -83.0% | -83.4% | -82.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | preg_match() | 16721.0 | 1619.8 | -90.3% | -90.4% | -90.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | str_contains() loop | 7387.4 | 1740.4 | -76.3% | -77.4% | -76.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | preg_match() | 18118.3 | 1740.4 | -90.4% | -90.4% | -90.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 61989.9 | 8768.6 | -85.9% | -86.5% | -85.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 127555.6 | 8768.6 | -93.1% | -93.1% | -93.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | str_contains() loop | 25275.4 | 3597.0 | -85.8% | -86.3% | -85.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | preg_match() | 47342.2 | 3597.0 | -92.4% | -92.4% | -92.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 30937.6 | 1372.1 | -95.6% | -95.8% | -95.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 28007.3 | 1372.1 | -95.1% | -95.1% | -95.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | str_contains() loop | 15170.5 | 561.2 | -96.3% | -96.6% | -96.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | preg_match() | 1760.0 | 561.2 | -68.1% | -68.9% | -67.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | str_contains() loop | 21746.9 | 1744.0 | -92.0% | -92.1% | -91.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | preg_match() | 33145.4 | 1744.0 | -94.7% | -94.8% | -94.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | str_contains() loop | 16677.5 | 1842.6 | -89.0% | -89.0% | -88.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | preg_match() | 36010.9 | 1842.6 | -94.9% | -94.9% | -94.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 139074.8 | 9117.8 | -93.4% | -93.8% | -93.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 252011.1 | 9117.8 | -96.4% | -96.4% | -96.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | str_contains() loop | 52980.4 | 3785.5 | -92.9% | -93.2% | -92.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | preg_match() | 93557.5 | 3785.5 | -96.0% | -96.0% | -95.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 75890.1 | 1475.5 | -98.1% | -98.1% | -98.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 105476.7 | 1475.5 | -98.6% | -98.6% | -98.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | str_contains() loop | 40505.6 | 557.8 | -98.6% | -98.6% | -98.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | preg_match() | 3031.2 | 557.8 | -81.6% | -81.8% | -81.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | str_contains() loop | 53356.1 | 1864.2 | -96.5% | -96.7% | -96.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | preg_match() | 107327.9 | 1864.2 | -98.3% | -98.4% | -98.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | str_contains() loop | 41299.1 | 1990.9 | -95.2% | -95.2% | -94.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | preg_match() | 124251.5 | 1990.9 | -98.4% | -98.6% | -98.3% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 325922.8 | 9646.6 | -97.0% | -97.0% | -97.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 925435.1 | 9646.6 | -99.0% | -99.0% | -98.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | str_contains() loop | 116437.4 | 4023.9 | -96.6% | -96.7% | -96.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | preg_match() | 348370.9 | 4023.9 | -98.8% | -98.9% | -98.7% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 5436.2 | 5312.1 | -2.4% | -3.3% | -1.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | preg_match() per term | 6789.5 | 5312.1 | -21.8% | -21.8% | -21.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 4415.2 | 5084.0 | +15.1% | +13.5% | +15.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 7687.2 | 5084.0 | -33.9% | -34.6% | -33.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 6721.5 | 5625.4 | -16.3% | -17.5% | -15.3% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 12923.3 | 5625.4 | -56.5% | -56.7% | -56.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 9865.2 | 5673.2 | -42.4% | -44.5% | -42.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | preg_match() per term | 12367.8 | 5673.2 | -54.1% | -54.3% | -53.9% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 8504.8 | 5099.7 | -40.0% | -40.3% | -38.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 14465.0 | 5099.7 | -64.7% | -64.9% | -64.6% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 12409.3 | 6102.7 | -50.8% | -51.7% | -50.6% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 23778.6 | 6102.7 | -74.3% | -74.4% | -74.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 17887.1 | 6266.0 | -65.0% | -65.8% | -64.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | preg_match() per term | 23833.0 | 6266.0 | -73.7% | -74.1% | -73.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 14809.0 | 5183.1 | -65.0% | -66.3% | -64.9% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 27012.6 | 5183.1 | -80.8% | -80.9% | -80.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 23492.5 | 6962.4 | -70.4% | -70.5% | -69.6% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 44626.0 | 6962.4 | -84.4% | -84.5% | -84.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 36367.2 | 7225.2 | -80.2% | -80.8% | -79.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | preg_match() per term | 44608.5 | 7225.2 | -83.8% | -83.8% | -83.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 32387.8 | 5541.4 | -82.9% | -82.9% | -82.1% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 52412.1 | 5541.4 | -89.4% | -89.5% | -89.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 45997.2 | 8517.2 | -81.5% | -82.0% | -81.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 82477.5 | 8517.2 | -89.7% | -89.7% | -89.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 76010.7 | 8737.2 | -88.5% | -88.6% | -88.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | preg_match() per term | 87094.8 | 8737.2 | -90.0% | -90.1% | -89.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 64717.7 | 6139.0 | -90.5% | -90.8% | -90.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 170237.7 | 6139.0 | -96.4% | -96.4% | -96.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 90351.3 | 10671.5 | -88.1% | -88.4% | -87.5% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 232969.3 | 10671.5 | -95.4% | -95.5% | -95.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 148843.0 | 9045.4 | -93.9% | -94.0% | -93.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | preg_match() per term | 176565.1 | 9045.4 | -94.9% | -94.9% | -94.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 140902.5 | 6417.2 | -95.4% | -95.6% | -95.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 413438.7 | 6417.2 | -98.4% | -98.5% | -98.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 166493.2 | 10826.0 | -93.5% | -93.5% | -93.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 496087.9 | 10826.0 | -97.8% | -98.2% | -97.8% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 287175.3 | 9789.4 | -96.6% | -96.6% | -96.5% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | preg_match() per term | 426117.6 | 9789.4 | -97.7% | -97.7% | -97.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 282692.8 | 7056.4 | -97.5% | -97.5% | -97.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 894800.9 | 7056.4 | -99.2% | -99.2% | -99.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 305999.2 | 11607.7 | -96.2% | -96.3% | -96.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 1007311.5 | 11607.7 | -98.8% | -98.9% | -98.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 20618.7 | 5851.6 | -71.6% | -71.9% | -71.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 3195.9 | 5851.6 | +83.3% | +82.1% | +84.3% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 162598.5 | 44175.9 | -72.8% | -72.8% | -72.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 22350.8 | 44175.9 | +97.6% | +95.9% | +99.4% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 36882.4 | 6230.9 | -83.1% | -83.2% | -82.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 9036.8 | 6230.9 | -30.9% | -31.5% | -29.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 292845.4 | 47031.7 | -83.9% | -84.0% | -83.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 70122.6 | 47031.7 | -32.8% | -33.2% | -32.4% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 77469.1 | 6773.2 | -91.3% | -91.3% | -91.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 17493.0 | 6773.2 | -61.3% | -61.4% | -61.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 621157.7 | 51315.9 | -91.7% | -91.8% | -91.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 136504.1 | 51315.9 | -62.4% | -62.6% | -62.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 143483.2 | 7477.5 | -94.8% | -94.8% | -94.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 31795.0 | 7477.5 | -76.5% | -76.5% | -76.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 1144622.9 | 56746.4 | -95.0% | -95.1% | -95.0% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 250859.1 | 56746.4 | -77.4% | -77.4% | -77.4% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 175196.9 | 8365.0 | -95.2% | -95.3% | -95.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 50414.5 | 8365.0 | -83.5% | -83.6% | -83.0% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 1398874.4 | 62698.9 | -95.5% | -95.5% | -95.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 398494.9 | 62698.9 | -84.3% | -84.4% | -84.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 191766.6 | 8674.9 | -95.5% | -95.5% | -95.4% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 104439.5 | 8674.9 | -91.7% | -91.7% | -91.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 1530946.8 | 66420.4 | -95.7% | -95.7% | -95.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 830511.3 | 66420.4 | -92.0% | -92.1% | -91.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 195996.3 | 9183.1 | -95.3% | -95.3% | -95.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 311543.3 | 9183.1 | -97.0% | -97.1% | -96.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 1564669.2 | 70178.8 | -95.5% | -95.5% | -95.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 2453406.2 | 70178.8 | -97.1% | -97.2% | -97.1% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 1249.6 | 1262.8 | +1.1% | +0.2% | +1.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 988.2 | 1262.8 | +27.8% | +25.6% | +29.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | str_contains() loop | 885.7 | 503.3 | -43.2% | -43.5% | -42.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 8 | preg_match() | 623.1 | 503.3 | -19.3% | -20.4% | -18.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | str_contains() loop | 1050.7 | 1646.5 | +56.7% | +55.5% | +57.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 8 | preg_match() | 1137.5 | 1646.5 | +44.9% | +42.9% | +45.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | str_contains() loop | 940.4 | 1756.5 | +86.4% | +85.7% | +87.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 8 | preg_match() | 1117.0 | 1756.5 | +57.2% | +56.2% | +57.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | str_contains() loop | 4418.3 | 9301.1 | +110.5% | +107.1% | +111.1% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 8 | preg_match() | 4598.7 | 9301.1 | +102.2% | +101.8% | +102.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | str_contains() loop | 1756.5 | 3788.3 | +115.7% | +114.9% | +115.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 8 | preg_match() | 2090.2 | 3788.3 | +81.2% | +80.3% | +82.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 1986.8 | 1266.2 | -36.4% | -38.3% | -36.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 1455.8 | 1266.2 | -13.3% | -14.1% | -13.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | str_contains() loop | 1233.6 | 502.8 | -59.2% | -59.7% | -58.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 16 | preg_match() | 655.3 | 502.8 | -23.4% | -23.4% | -22.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | str_contains() loop | 1487.5 | 1652.8 | +11.0% | +8.2% | +12.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 16 | preg_match() | 1734.4 | 1652.8 | -4.0% | -7.0% | -3.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | str_contains() loop | 1305.0 | 1762.3 | +35.3% | +33.5% | +35.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 16 | preg_match() | 1802.0 | 1762.3 | -2.4% | -3.1% | -1.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | str_contains() loop | 7485.8 | 9304.2 | +24.3% | +23.6% | +24.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 16 | preg_match() | 11490.6 | 9304.2 | -19.1% | -19.3% | -18.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | str_contains() loop | 2578.1 | 3786.4 | +47.1% | +46.5% | +47.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 16 | preg_match() | 3663.1 | 3786.4 | +3.5% | +2.5% | +3.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 3638.9 | 1264.9 | -65.2% | -65.4% | -64.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 3297.8 | 1264.9 | -61.6% | -61.8% | -61.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | str_contains() loop | 2162.5 | 507.8 | -76.6% | -77.2% | -76.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 32 | preg_match() | 719.6 | 507.8 | -29.7% | -36.8% | -29.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | str_contains() loop | 2714.4 | 1654.0 | -38.9% | -39.7% | -38.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 32 | preg_match() | 4189.0 | 1654.0 | -60.5% | -61.7% | -59.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | str_contains() loop | 2230.6 | 1765.2 | -20.8% | -22.1% | -20.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 32 | preg_match() | 4383.3 | 1765.2 | -59.7% | -59.9% | -59.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | str_contains() loop | 16895.4 | 9312.8 | -44.8% | -45.1% | -44.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 32 | preg_match() | 29557.8 | 9312.8 | -68.5% | -68.6% | -68.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | str_contains() loop | 6223.8 | 3794.3 | -38.9% | -39.3% | -38.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 32 | preg_match() | 10822.3 | 3794.3 | -64.9% | -65.0% | -64.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 6867.7 | 1279.9 | -81.4% | -81.4% | -81.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 6927.0 | 1279.9 | -81.5% | -81.6% | -81.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | str_contains() loop | 4051.9 | 505.2 | -87.5% | -87.6% | -87.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 64 | preg_match() | 872.1 | 505.2 | -42.0% | -42.6% | -41.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | str_contains() loop | 5259.0 | 1683.9 | -67.9% | -68.2% | -67.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 64 | preg_match() | 8651.9 | 1683.9 | -80.6% | -80.6% | -80.4% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | str_contains() loop | 4246.3 | 1786.0 | -57.9% | -58.0% | -57.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 64 | preg_match() | 9323.0 | 1786.0 | -80.8% | -80.9% | -80.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | str_contains() loop | 33542.7 | 9350.7 | -72.1% | -72.1% | -72.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 64 | preg_match() | 64403.2 | 9350.7 | -85.5% | -85.5% | -85.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | str_contains() loop | 13391.8 | 3814.9 | -71.5% | -71.6% | -71.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 64 | preg_match() | 23965.5 | 3814.9 | -84.1% | -84.1% | -84.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 14356.2 | 1304.1 | -90.9% | -91.0% | -90.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 13003.3 | 1304.1 | -90.0% | -90.0% | -89.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | str_contains() loop | 7831.0 | 507.7 | -93.5% | -93.7% | -93.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 128 | preg_match() | 1058.5 | 507.7 | -51.9% | -52.8% | -51.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | str_contains() loop | 10272.1 | 1703.2 | -83.4% | -83.7% | -83.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 128 | preg_match() | 15895.2 | 1703.2 | -89.3% | -89.3% | -89.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | str_contains() loop | 8070.1 | 1816.0 | -77.5% | -78.0% | -77.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 128 | preg_match() | 17296.7 | 1816.0 | -89.5% | -89.5% | -89.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | str_contains() loop | 65670.3 | 9500.3 | -85.5% | -85.6% | -85.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 128 | preg_match() | 121846.4 | 9500.3 | -92.2% | -92.2% | -92.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | str_contains() loop | 26260.8 | 3830.4 | -85.4% | -85.5% | -85.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 128 | preg_match() | 45048.8 | 3830.4 | -91.5% | -91.5% | -91.5% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 35311.4 | 1409.7 | -96.0% | -96.0% | -95.9% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 27534.9 | 1409.7 | -94.9% | -95.8% | -94.7% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | str_contains() loop | 17283.7 | 505.8 | -97.1% | -97.1% | -97.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 256 | preg_match() | 1646.6 | 505.8 | -69.5% | -74.5% | -68.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | str_contains() loop | 23228.6 | 1836.2 | -92.1% | -92.2% | -92.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 256 | preg_match() | 32544.6 | 1836.2 | -94.3% | -95.4% | -94.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | str_contains() loop | 17716.8 | 1935.4 | -89.1% | -89.2% | -89.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 256 | preg_match() | 35138.6 | 1935.4 | -94.5% | -95.5% | -94.5% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | str_contains() loop | 149382.1 | 9880.4 | -93.4% | -93.4% | -93.4% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 256 | preg_match() | 272544.9 | 9880.4 | -96.4% | -96.8% | -96.0% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | str_contains() loop | 55545.0 | 4031.2 | -92.8% | -92.8% | -92.7% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 256 | preg_match() | 94544.5 | 4031.2 | -95.7% | -96.5% | -95.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 80357.1 | 1514.3 | -98.1% | -98.2% | -98.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 95058.1 | 1514.3 | -98.4% | -98.4% | -98.3% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | str_contains() loop | 43323.0 | 511.9 | -98.8% | -98.8% | -98.8% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match at start) | 512 | preg_match() | 2872.6 | 511.9 | -82.3% | -82.6% | -82.0% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | str_contains() loop | 58456.8 | 1955.0 | -96.7% | -96.7% | -96.6% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match in body) | 512 | preg_match() | 107352.7 | 1955.0 | -98.2% | -98.3% | -98.1% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | str_contains() loop | 43713.5 | 2067.3 | -95.3% | -95.5% | -95.2% |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) (Match near end) | 512 | preg_match() | 116849.9 | 2067.3 | -98.3% | -98.4% | -98.2% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | str_contains() loop | 334828.1 | 10392.4 | -96.9% | -96.9% | -96.9% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (No match) | 512 | preg_match() | 913811.9 | 10392.4 | -98.9% | -98.9% | -98.8% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | str_contains() loop | 123118.5 | 4239.7 | -96.6% | -96.6% | -96.6% |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) (Quoted matching term) | 512 | preg_match() | 320452.8 | 4239.7 | -98.7% | -98.8% | -98.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 5428.5 | 6228.1 | +14.6% | +14.5% | +16.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | preg_match() per term | 6692.1 | 6228.1 | -6.9% | -8.1% | -6.1% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 4479.6 | 5403.0 | +20.6% | +18.2% | +21.1% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 7573.4 | 5403.0 | -28.7% | -28.9% | -28.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | strpos() per term | 6683.7 | 6472.8 | -3.2% | -3.5% | -2.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | PCRE lookahead per term | 12865.3 | 6472.8 | -49.6% | -49.8% | -49.3% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 10199.8 | 6605.7 | -35.2% | -35.4% | -34.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | preg_match() per term | 12428.0 | 6605.7 | -46.9% | -46.9% | -46.2% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 8621.4 | 5420.9 | -37.1% | -37.5% | -36.9% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 14377.8 | 5420.9 | -62.3% | -62.5% | -62.3% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | strpos() per term | 12687.5 | 6958.0 | -45.2% | -45.2% | -45.0% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | PCRE lookahead per term | 23644.1 | 6958.0 | -70.6% | -70.7% | -70.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 18667.1 | 7130.6 | -61.8% | -62.1% | -61.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | preg_match() per term | 23772.2 | 7130.6 | -70.0% | -70.4% | -69.7% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 15758.9 | 5511.4 | -65.0% | -65.1% | -64.8% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 27260.5 | 5511.4 | -79.8% | -79.8% | -79.6% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | strpos() per term | 23960.3 | 7889.4 | -67.1% | -67.2% | -66.7% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | PCRE lookahead per term | 44425.0 | 7889.4 | -82.2% | -82.3% | -82.1% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 38654.5 | 8045.7 | -79.2% | -79.3% | -78.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | preg_match() per term | 44899.7 | 8045.7 | -82.1% | -82.1% | -82.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 33711.6 | 5858.6 | -82.6% | -82.7% | -82.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 52570.0 | 5858.6 | -88.9% | -88.9% | -88.8% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | strpos() per term | 48072.1 | 9480.2 | -80.3% | -80.5% | -80.3% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | PCRE lookahead per term | 82527.2 | 9480.2 | -88.5% | -88.6% | -88.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 76960.4 | 9504.6 | -87.7% | -87.7% | -87.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | preg_match() per term | 86711.8 | 9504.6 | -89.0% | -89.3% | -89.0% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 68345.7 | 6449.6 | -90.6% | -90.7% | -90.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 173537.5 | 6449.6 | -96.3% | -96.3% | -96.3% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | strpos() per term | 90965.8 | 11565.3 | -87.3% | -87.3% | -86.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | PCRE lookahead per term | 235191.5 | 11565.3 | -95.1% | -95.1% | -94.9% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 152556.5 | 9835.4 | -93.5% | -93.6% | -93.2% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | preg_match() per term | 179740.5 | 9835.4 | -94.5% | -94.6% | -94.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 145427.5 | 6745.7 | -95.4% | -95.4% | -95.3% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 417089.6 | 6745.7 | -98.4% | -98.4% | -98.4% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | strpos() per term | 168155.4 | 11897.6 | -93.0% | -93.0% | -92.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | PCRE lookahead per term | 494344.6 | 11897.6 | -97.6% | -97.6% | -97.6% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 293782.7 | 10545.4 | -96.4% | -96.5% | -96.4% |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | preg_match() per term | 429510.1 | 10545.4 | -97.5% | -97.6% | -97.5% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 288971.1 | 7393.4 | -97.4% | -97.5% | -97.4% |
| [Count support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 891600.3 | 7393.4 | -99.2% | -99.2% | -99.2% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | strpos() per term | 313254.0 | 12620.8 | -96.0% | -96.0% | -95.9% |
| [Locate support-term occurrences](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | PCRE lookahead per term | 1010997.6 | 12620.8 | -98.8% | -98.8% | -98.7% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 19866.6 | 6331.6 | -68.1% | -68.5% | -67.9% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 3230.9 | 6331.6 | +95.7% | +94.2% | +99.1% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | strtr() | 158060.6 | 48367.7 | -69.4% | -69.7% | -69.0% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | preg_replace_callback() | 22442.9 | 48367.7 | +116.0% | +114.1% | +116.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 36189.2 | 6561.1 | -81.8% | -82.1% | -81.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 8987.3 | 6561.1 | -27.0% | -28.0% | -26.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | strtr() | 290142.1 | 50095.0 | -82.7% | -82.8% | -82.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | preg_replace_callback() | 68958.4 | 50095.0 | -27.4% | -28.2% | -27.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 77050.4 | 6993.9 | -90.9% | -90.9% | -90.8% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 17510.4 | 6993.9 | -60.0% | -60.1% | -59.7% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | strtr() | 616548.6 | 53253.2 | -91.4% | -91.4% | -91.3% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | preg_replace_callback() | 137031.5 | 53253.2 | -61.2% | -61.2% | -61.1% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 144121.0 | 7652.0 | -94.7% | -94.7% | -94.6% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 31623.5 | 7652.0 | -75.9% | -75.9% | -75.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | strtr() | 1150853.7 | 58068.8 | -94.9% | -95.0% | -94.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | preg_replace_callback() | 249807.4 | 58068.8 | -76.7% | -76.9% | -76.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 177161.0 | 8402.8 | -95.3% | -95.3% | -95.2% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 54511.2 | 8402.8 | -84.6% | -85.0% | -84.5% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | strtr() | 1414031.7 | 63647.4 | -95.5% | -95.5% | -95.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | preg_replace_callback() | 431529.9 | 63647.4 | -85.3% | -85.3% | -85.0% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 194111.4 | 8810.9 | -95.5% | -95.5% | -95.4% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 101746.9 | 8810.9 | -91.3% | -91.4% | -91.2% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | strtr() | 1549995.3 | 67055.0 | -95.7% | -95.7% | -95.6% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | preg_replace_callback() | 809017.9 | 67055.0 | -91.7% | -91.8% | -91.6% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 198361.3 | 9377.6 | -95.3% | -95.3% | -95.3% |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 305587.7 | 9377.6 | -96.9% | -97.0% | -96.9% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | strtr() | 1582587.7 | 71337.0 | -95.5% | -95.5% | -95.4% |
| [Publish eight help articles](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | preg_replace_callback() | 2433117.4 | 71337.0 | -97.1% | -97.1% | -97.0% |

### Control tasks

#### Dictionary preparation included

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | str_contains() loop | 1507.2 | 33449.6 | +2144.0% | +2084.7% | +2185.9% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | preg_match() | 5754.8 | 33449.6 | +481.1% | +474.8% | +501.0% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | strtr() | 333693.2 | 928561.6 | +178.3% | +178.2% | +178.7% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace_callback() | 49850.7 | 928561.6 | +1762.7% | +1752.7% | +1770.1% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | str_replace() | 713401.6 | 928561.6 | +30.2% | +29.8% | +30.6% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace() | 47844.8 | 928561.6 | +1843.1% | +1837.2% | +1857.9% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | str_contains() loop | 1518.4 | 30890.4 | +1932.9% | +1895.1% | +1947.9% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | preg_match() | 6225.0 | 30890.4 | +395.4% | +382.4% | +398.4% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | strtr() | 305586.8 | 976066.4 | +219.4% | +218.8% | +219.7% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace_callback() | 46719.5 | 976066.4 | +1989.2% | +1985.0% | +1997.0% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | str_replace() | 665943.0 | 976066.4 | +46.6% | +46.2% | +46.8% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace() | 44522.1 | 976066.4 | +2091.4% | +2087.3% | +2101.2% |

#### Dictionary already prepared

##### gcc15

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | str_contains() loop | 1485.6 | 1227.4 | -17.3% | -17.9% | -15.9% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | preg_match() | 1142.6 | 1227.4 | +7.6% | +7.2% | +8.2% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | strtr() | 335181.9 | 793062.6 | +136.9% | +136.4% | +137.5% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace_callback() | 20898.2 | 793062.6 | +3698.5% | +3664.8% | +3719.0% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | str_replace() | 692334.1 | 793062.6 | +14.6% | +14.4% | +14.7% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace() | 19160.3 | 793062.6 | +4044.6% | +4014.2% | +4095.3% |

##### clang21

| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |
|---|---:|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | str_contains() loop | 1527.3 | 1266.5 | -17.1% | -17.7% | -16.5% |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | 12 | preg_match() | 1116.9 | 1266.5 | +13.8% | +13.2% | +14.0% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | strtr() | 305359.8 | 847148.0 | +177.6% | +176.8% | +178.2% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace_callback() | 20993.4 | 847148.0 | +3934.8% | +3859.8% | +3964.1% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | str_replace() | 644361.9 | 847148.0 | +31.5% | +31.2% | +31.6% |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-scaling/suites/controls.json) | 24 | preg_replace() | 18971.6 | 847148.0 | +4365.1% | +4221.5% | +4387.8% |
