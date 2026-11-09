# Cycles and instructions per job

Each median uses five alternating 0/N pairs after subtraction. Captures are separate from elapsed timing. † means at least one pair failed quality checks; [raw pairs](data/counters.json.gz) and [criteria](QUALITY.md) remain available.

| Input | Mode | Recipe | Cycles/job | Instructions/job |
|---|---|---|---:|---:|
| batch.references.all.b1 | batch | Matcher::matchAll() | 566595.7 | 1092145.5 |
| batch.references.all.b1 | batch | strpos() loop | 1738094.0 | 2428038.0 |
| batch.references.all.b1 | batch | preg_match_all() [literal] | 2792047.1 | 7232157.3 |
| batch.references.all.b1 | batch | preg_match_all() [prefix] | 2828673.2 | 7233547.2 |
| batch.references.all.b16 | batch | Matcher::matchAll() | 3520055.6† | 5166745.8† |
| batch.references.all.b16 | batch | strpos() loop | 13782267.3 | 20039124.2 |
| batch.references.all.b16 | batch | preg_match_all() [literal] | 20446281.3 | 56259518.5 |
| batch.references.all.b16 | batch | preg_match_all() [prefix] | 20800931.0† | 56273054.7† |
| batch.references.all.b4 | batch | Matcher::matchAll() | 1195340.3 | 2011679.9 |
| batch.references.all.b4 | batch | strpos() loop | 4517825.8 | 6162695.2 |
| batch.references.all.b4 | batch | preg_match_all() [literal] | 6635913.8 | 18738316.0 |
| batch.references.all.b4 | batch | preg_match_all() [prefix] | 6657865.2 | 18742859.0 |
| batch.references.count.b1 | batch | Matcher::countMatches() | 565219.5 | 1063218.2 |
| batch.references.count.b1 | batch | strpos() loop | 1693302.1 | 2250765.7 |
| batch.references.count.b1 | batch | preg_match_all() [literal] | 2711932.0 | 6989782.0 |
| batch.references.count.b1 | batch | preg_match_all() [prefix] | 2761868.0 | 6991230.9 |
| batch.references.count.b16 | batch | Matcher::countMatches() | 3391388.1 | 4644870.0 |
| batch.references.count.b16 | batch | strpos() loop | 12966249.4 | 16550118.9 |
| batch.references.count.b16 | batch | preg_match_all() [literal] | 19364795.0 | 51754382.2 |
| batch.references.count.b16 | batch | preg_match_all() [prefix] | 19603139.0 | 51767730.7 |
| batch.references.count.b4 | batch | Matcher::countMatches() | 1168369.7 | 1925458.7 |
| batch.references.count.b4 | batch | strpos() loop | 4395577.6† | 5657429.2† |
| batch.references.count.b4 | batch | preg_match_all() [literal] | 6468220.4 | 18071833.1 |
| batch.references.count.b4 | batch | preg_match_all() [prefix] | 6498358.9 | 18076449.2 |
| batch.references.unique.b1 | batch | Matcher::getMatchedKeywords() | 586539.2 | 1177412.0 |
| batch.references.unique.b1 | batch | strpos() loop | 1559086.2 | 2096638.4 |
| batch.references.unique.b1 | batch | preg_match_all() [literal] | 2772377.9 | 7126545.0 |
| batch.references.unique.b1 | batch | preg_match_all() [prefix] | 2808661.5† | 7127963.3† |
| batch.references.unique.b16 | batch | Matcher::getMatchedKeywords() | 3388977.9 | 5517254.9 |
| batch.references.unique.b16 | batch | strpos() loop | 12148892.3 | 15296500.9 |
| batch.references.unique.b16 | batch | preg_match_all() [literal] | 19989713.5 | 54073969.7 |
| batch.references.unique.b16 | batch | preg_match_all() [prefix] | 20294156.2 | 54088048.8 |
| batch.references.unique.b4 | batch | Matcher::getMatchedKeywords() | 1193425.7 | 2239838.3 |
| batch.references.unique.b4 | batch | strpos() loop | 4133422.9 | 5335031.0 |
| batch.references.unique.b4 | batch | preg_match_all() [literal] | 6602847.2 | 18495381.8 |
| batch.references.unique.b4 | batch | preg_match_all() [prefix] | 6616572.0 | 18500051.5 |
| batch.rewrite.replace.b1 | batch | Replacer::replace() | 487979.7 | 934766.7 |
| batch.rewrite.replace.b1 | batch | strtr() | 5233683.2 | 15609263.4 |
| batch.rewrite.replace.b1 | batch | preg_replace_callback() [literal] | 1217526.4 | 4441225.4 |
| batch.rewrite.replace.b1 | batch | preg_replace_callback() [prefix] | 814706.2 | 2231602.5 |
| batch.rewrite.replace.b1 | batch | str_replace() | 1913273.9 | 2457375.9 |
| batch.rewrite.replace.b16 | batch | Replacer::replace() | 3285568.9 | 4884207.4 |
| batch.rewrite.replace.b16 | batch | strtr() | 34637647.8 | 102268047.2 |
| batch.rewrite.replace.b16 | batch | preg_replace_callback() [literal] | 8235735.9† | 30126930.4† |
| batch.rewrite.replace.b16 | batch | preg_replace_callback() [prefix] | 6341498.2 | 15744691.9 |
| batch.rewrite.replace.b4 | batch | Replacer::replace() | 1049242.1† | 1880577.3† |
| batch.rewrite.replace.b4 | batch | strtr() | 11340690.0 | 34054732.4 |
| batch.rewrite.replace.b4 | batch | preg_replace_callback() [literal] | 2629566.7 | 9937561.3 |
| batch.rewrite.replace.b4 | batch | preg_replace_callback() [prefix] | 1978291.1 | 5168717.2 |
| batch.rewrite.replace.b4 | batch | str_replace() | 4802475.1 | 5971888.1 |
| batch.validation.any.b1 | batch | Matcher::matches() | 1116804.2 | 2107647.9 |
| batch.validation.any.b1 | batch | stripos() loop | 144763.9 | 509780.9 |
| batch.validation.any.b1 | batch | preg_match() [literal] | 682842.8 | 1317817.7 |
| batch.validation.any.b1 | batch | preg_match() [prefix] | 23590.6 | 120777.2 |
| batch.validation.any.b1 | batch | strtolower() + strpos() loop | 125237.3 | 379343.4 |
| batch.validation.any.b16 | batch | Matcher::matches() | 1152753.1 | 2195327.4 |
| batch.validation.any.b16 | batch | stripos() loop | 1745322.2 | 4822514.3 |
| batch.validation.any.b16 | batch | preg_match() [literal] | 6098741.1 | 11797811.5 |
| batch.validation.any.b16 | batch | preg_match() [prefix] | 266991.0 | 1106206.2 |
| batch.validation.any.b16 | batch | strtolower() + strpos() loop | 1552599.6 | 3620520.9 |
| batch.validation.any.b4 | batch | Matcher::matches() | 1133559.3 | 2137724.5 |
| batch.validation.any.b4 | batch | stripos() loop | 562028.4 | 1718984.0 |
| batch.validation.any.b4 | batch | preg_match() [literal] | 2790887.1 | 5388277.4 |
| batch.validation.any.b4 | batch | preg_match() [prefix] | 99983.5 | 490079.1 |
| batch.validation.any.b4 | batch | strtolower() + strpos() loop | 547206.5† | 1283457.7† |
| batch.validation.any.b64 | batch | Matcher::matches() | 1284441.2 | 2477073.1 |
| batch.validation.any.b64 | batch | stripos() loop | 7283821.3 | 19821501.6 |
| batch.validation.any.b64 | batch | preg_match() [literal] | 23540851.6 | 45450980.6 |
| batch.validation.any.b64 | batch | preg_match() [prefix] | 1211990.5† | 4261384.3† |
| batch.validation.any.b64 | batch | strtolower() + strpos() loop | 6418075.0† | 14856395.9† |
| batch.validation.unique.b1 | batch | Matcher::getMatchedKeywords() | 1112650.2 | 2109324.0 |
| batch.validation.unique.b1 | batch | stripos() loop | 144395.3 | 510516.0 |
| batch.validation.unique.b1 | batch | preg_match_all() [literal] | 229712.8 | 1049465.4 |
| batch.validation.unique.b1 | batch | preg_match_all() [prefix] | 120082.9 | 628897.7 |
| batch.validation.unique.b1 | batch | strtolower() + strpos() loop | 125652.8 | 380079.7 |
| batch.validation.unique.b16 | batch | Matcher::getMatchedKeywords() | 1176476.8 | 2239366.1 |
| batch.validation.unique.b16 | batch | stripos() loop | 2565985.5 | 6790327.1 |
| batch.validation.unique.b16 | batch | preg_match_all() [literal] | 3316590.7 | 12422994.7 |
| batch.validation.unique.b16 | batch | preg_match_all() [prefix] | 2741136.6 | 7540353.7 |
| batch.validation.unique.b16 | batch | strtolower() + strpos() loop | 2277947.9 | 5086564.3 |
| batch.validation.unique.b4 | batch | Matcher::getMatchedKeywords() | 1135801.8 | 2150750.0 |
| batch.validation.unique.b4 | batch | stripos() loop | 802599.4 | 2290795.3 |
| batch.validation.unique.b4 | batch | preg_match_all() [literal] | 1218678.6† | 4944272.5† |
| batch.validation.unique.b4 | batch | preg_match_all() [prefix] | 973148.3 | 2954048.2 |
| batch.validation.unique.b4 | batch | strtolower() + strpos() loop | 765938.3 | 1712975.1 |
| batch.validation.unique.b64 | batch | Matcher::getMatchedKeywords() | 1350669.1 | 2665713.3 |
| batch.validation.unique.b64 | batch | stripos() loop | 10376204.2 | 27185952.9 |
| batch.validation.unique.b64 | batch | preg_match_all() [literal] | 13636513.8 | 49788841.4 |
| batch.validation.unique.b64 | batch | preg_match_all() [prefix] | 11470314.8 | 30207957.6 |
| batch.validation.unique.b64 | batch | strtolower() + strpos() loop | 9306851.8 | 20447668.5 |
| comment.10.any | oneshot | Matcher::matches() | 1123171.4† | 2101336.1† |
| comment.10.any | oneshot | stripos() loop | 65865.5 | 267214.4 |
| comment.10.any | oneshot | preg_match() [literal] | 170860.0 | 327981.8 |
| comment.10.any | oneshot | preg_match() [prefix] | 7654.9 | 35021.0 |
| comment.10.any | oneshot | strtolower() + strpos() loop | 49014.8 | 202332.1 |
| comment.10.any | prepared | Matcher::matches() | 1417.8 | 5050.0 |
| comment.10.any | prepared | stripos() loop | 65788.8 | 267214.9 |
| comment.10.any | prepared | preg_match() [literal] | 170473.1 | 327976.6 |
| comment.10.any | prepared | preg_match() [prefix] | 7505.9 | 35021.0 |
| comment.10.any | prepared | strtolower() + strpos() loop | 49192.7 | 202331.9 |
| comment.10.unique | oneshot | Matcher::getMatchedKeywords() | 1112588.9 | 2102003.5 |
| comment.10.unique | oneshot | stripos() loop | 65451.0 | 267947.3 |
| comment.10.unique | oneshot | preg_match_all() [literal] | 67977.4 | 298701.2 |
| comment.10.unique | oneshot | preg_match_all() [prefix] | 41668.2 | 192971.3 |
| comment.10.unique | oneshot | strtolower() + strpos() loop | 49684.8† | 203072.9† |
| comment.10.unique | prepared | Matcher::getMatchedKeywords() | 1552.4† | 5704.0† |
| comment.10.unique | prepared | stripos() loop | 65787.1 | 267947.2 |
| comment.10.unique | prepared | preg_match_all() [literal] | 68023.2 | 298703.4 |
| comment.10.unique | prepared | preg_match_all() [prefix] | 41644.6 | 192971.1 |
| comment.10.unique | prepared | strtolower() + strpos() loop | 49838.8 | 203073.0 |
| comment.13.any | oneshot | Matcher::matches() | 1114865.7 | 2100858.1 |
| comment.13.any | oneshot | stripos() loop | 61159.6 | 245979.6 |
| comment.13.any | oneshot | preg_match() [literal] | 123316.0 | 241348.1 |
| comment.13.any | oneshot | preg_match() [prefix] | 6127.1 | 27500.0 |
| comment.13.any | oneshot | strtolower() + strpos() loop | 46445.3 | 187460.8 |
| comment.13.any | prepared | Matcher::matches() | 1316.3 | 4579.0 |
| comment.13.any | prepared | stripos() loop | 60905.8 | 245979.4 |
| comment.13.any | prepared | preg_match() [literal] | 123334.9 | 241348.1 |
| comment.13.any | prepared | preg_match() [prefix] | 6159.0† | 27500.0† |
| comment.13.any | prepared | strtolower() + strpos() loop | 45850.3 | 187461.4 |
| comment.13.unique | oneshot | Matcher::getMatchedKeywords() | 1109644.0 | 2101438.5 |
| comment.13.unique | oneshot | stripos() loop | 61102.2 | 246712.8 |
| comment.13.unique | oneshot | preg_match_all() [literal] | 52902.1† | 225933.3† |
| comment.13.unique | oneshot | preg_match_all() [prefix] | 33854.5 | 150947.2 |
| comment.13.unique | oneshot | strtolower() + strpos() loop | 46023.3 | 188186.7 |
| comment.13.unique | prepared | Matcher::getMatchedKeywords() | 1424.6 | 5146.0 |
| comment.13.unique | prepared | stripos() loop | 60495.7 | 246712.4 |
| comment.13.unique | prepared | preg_match_all() [literal] | 52793.6 | 225933.6 |
| comment.13.unique | prepared | preg_match_all() [prefix] | 33787.8 | 150946.0 |
| comment.13.unique | prepared | strtolower() + strpos() loop | 46287.8 | 188191.7 |
| comment.13909.any | oneshot | Matcher::matches() | 1117562.4 | 2107873.0 |
| comment.13909.any | oneshot | stripos() loop | 148835.6 | 519577.4 |
| comment.13909.any | oneshot | preg_match() [literal] | 687512.2† | 1321036.6† |
| comment.13909.any | oneshot | preg_match() [prefix] | 23865.8 | 121680.3 |
| comment.13909.any | oneshot | strtolower() + strpos() loop | 130350.1† | 390036.2† |
| comment.13909.any | prepared | Matcher::matches() | 4066.1 | 11582.0 |
| comment.13909.any | prepared | stripos() loop | 149390.5† | 519578.9† |
| comment.13909.any | prepared | preg_match() [literal] | 688134.1† | 1321039.6† |
| comment.13909.any | prepared | preg_match() [prefix] | 23940.8 | 121680.0 |
| comment.13909.any | prepared | strtolower() + strpos() loop | 130512.0 | 390035.7 |
| comment.13909.unique | oneshot | Matcher::getMatchedKeywords() | 1115228.6 | 2109539.9 |
| comment.13909.unique | oneshot | stripos() loop | 149107.1 | 520313.7 |
| comment.13909.unique | oneshot | preg_match_all() [literal] | 227075.8 | 1051029.8 |
| comment.13909.unique | oneshot | preg_match_all() [prefix] | 121717.1 | 631745.9 |
| comment.13909.unique | oneshot | strtolower() + strpos() loop | 130738.6 | 390768.9 |
| comment.13909.unique | prepared | Matcher::getMatchedKeywords() | 4250.6† | 13272.9† |
| comment.13909.unique | prepared | stripos() loop | 148565.0 | 520313.0 |
| comment.13909.unique | prepared | preg_match_all() [literal] | 226970.7† | 1051030.5† |
| comment.13909.unique | prepared | preg_match_all() [prefix] | 121605.3 | 631744.4 |
| comment.13909.unique | prepared | strtolower() + strpos() loop | 130978.3 | 390769.1 |
| comment.13918.any | oneshot | Matcher::matches() | 1120373.6 | 2103555.8 |
| comment.13918.any | oneshot | stripos() loop | 93821.9 | 353248.4 |
| comment.13918.any | oneshot | preg_match() [literal] | 348705.9 | 671562.8 |
| comment.13918.any | oneshot | preg_match() [prefix] | 13109.3† | 64743.1† |
| comment.13918.any | oneshot | strtolower() + strpos() loop | 76409.0† | 265797.9† |
| comment.13918.any | prepared | Matcher::matches() | 2476.8† | 7292.0† |
| comment.13918.any | prepared | stripos() loop | 94401.1 | 353248.5 |
| comment.13918.any | prepared | preg_match() [literal] | 348220.8† | 671566.7† |
| comment.13918.any | prepared | preg_match() [prefix] | 13075.1† | 64742.8† |
| comment.13918.any | prepared | strtolower() + strpos() loop | 76363.9 | 265798.2 |
| comment.13918.unique | oneshot | Matcher::getMatchedKeywords() | 1112221.0 | 2104586.6 |
| comment.13918.unique | oneshot | stripos() loop | 93609.3 | 353981.7 |
| comment.13918.unique | oneshot | preg_match_all() [literal] | 127322.4 | 575325.7 |
| comment.13918.unique | oneshot | preg_match_all() [prefix] | 70485.5 | 352122.0 |
| comment.13918.unique | oneshot | strtolower() + strpos() loop | 76068.1† | 266532.1† |
| comment.13918.unique | prepared | Matcher::getMatchedKeywords() | 2608.8† | 8300.0† |
| comment.13918.unique | prepared | stripos() loop | 94229.2† | 353981.5† |
| comment.13918.unique | prepared | preg_match_all() [literal] | 128988.2† | 575325.2† |
| comment.13918.unique | prepared | preg_match_all() [prefix] | 71842.5† | 352120.7† |
| comment.13918.unique | prepared | strtolower() + strpos() loop | 76078.9 | 266531.0 |
| comment.28.any | oneshot | Matcher::matches() | 1114006.7 | 2100509.0 |
| comment.28.any | oneshot | stripos() loop | 59079.4 | 236984.1 |
| comment.28.any | oneshot | preg_match() [literal] | 97896.0 | 191731.4 |
| comment.28.any | oneshot | preg_match() [prefix] | 5299.4 | 23253.9 |
| comment.28.any | oneshot | strtolower() + strpos() loop | 43010.8 | 180736.9 |
| comment.28.any | prepared | Matcher::matches() | 1212.3 | 4223.0 |
| comment.28.any | prepared | stripos() loop | 58567.8 | 236984.0 |
| comment.28.any | prepared | preg_match() [literal] | 98164.8 | 191730.4 |
| comment.28.any | prepared | preg_match() [prefix] | 5334.9† | 23254.0† |
| comment.28.any | prepared | strtolower() + strpos() loop | 43031.4 | 180737.7 |
| comment.28.unique | oneshot | Matcher::getMatchedKeywords() | 1111864.3 | 2101020.8 |
| comment.28.unique | oneshot | stripos() loop | 58888.0 | 237715.9 |
| comment.28.unique | oneshot | preg_match_all() [literal] | 48098.7 | 198256.1 |
| comment.28.unique | oneshot | preg_match_all() [prefix] | 31217.2 | 135736.1 |
| comment.28.unique | oneshot | strtolower() + strpos() loop | 43404.7 | 181477.0 |
| comment.28.unique | prepared | Matcher::getMatchedKeywords() | 1320.6 | 4739.0 |
| comment.28.unique | prepared | stripos() loop | 58431.8 | 237717.9 |
| comment.28.unique | prepared | preg_match_all() [literal] | 48068.1 | 198257.5 |
| comment.28.unique | prepared | preg_match_all() [prefix] | 30964.7 | 135736.1 |
| comment.28.unique | prepared | strtolower() + strpos() loop | 43399.2 | 181476.4 |
| comment.41696.any | oneshot | Matcher::matches() | 1122647.6† | 2107655.6† |
| comment.41696.any | oneshot | stripos() loop | 145066.7† | 509781.2† |
| comment.41696.any | oneshot | preg_match() [literal] | 683579.3 | 1317825.5 |
| comment.41696.any | oneshot | preg_match() [prefix] | 23842.5† | 120777.5† |
| comment.41696.any | oneshot | strtolower() + strpos() loop | 127161.5† | 379321.0† |
| comment.41696.any | prepared | Matcher::matches() | 4034.3 | 11366.0 |
| comment.41696.any | prepared | stripos() loop | 144501.9† | 509780.9† |
| comment.41696.any | prepared | preg_match() [literal] | 683951.3† | 1317849.2† |
| comment.41696.any | prepared | preg_match() [prefix] | 23656.1 | 120776.9 |
| comment.41696.any | prepared | strtolower() + strpos() loop | 125798.6† | 379324.1† |
| comment.41696.unique | oneshot | Matcher::getMatchedKeywords() | 1110065.0 | 2109296.9 |
| comment.41696.unique | oneshot | stripos() loop | 145028.6 | 510515.1 |
| comment.41696.unique | oneshot | preg_match_all() [literal] | 228640.1 | 1049467.8 |
| comment.41696.unique | oneshot | preg_match_all() [prefix] | 120273.6 | 628898.1 |
| comment.41696.unique | oneshot | strtolower() + strpos() loop | 126149.2† | 380056.7† |
| comment.41696.unique | prepared | Matcher::getMatchedKeywords() | 4248.9 | 13031.0 |
| comment.41696.unique | prepared | stripos() loop | 144838.8 | 510513.6 |
| comment.41696.unique | prepared | preg_match_all() [literal] | 229068.4† | 1049462.4† |
| comment.41696.unique | prepared | preg_match_all() [prefix] | 120609.4 | 628900.0 |
| comment.41696.unique | prepared | strtolower() + strpos() loop | 125861.7 | 380054.7 |
| comment.41698.any | oneshot | Matcher::matches() | 1111179.5 | 2105446.4 |
| comment.41698.any | oneshot | stripos() loop | 114242.2 | 421039.4 |
| comment.41698.any | oneshot | preg_match() [literal] | 493847.2 | 952602.0 |
| comment.41698.any | oneshot | preg_match() [prefix] | 17453.5 | 88563.1 |
| comment.41698.any | oneshot | strtolower() + strpos() loop | 97261.2 | 311808.5 |
| comment.41698.any | prepared | Matcher::matches() | 3144.6 | 9159.0 |
| comment.41698.any | prepared | stripos() loop | 114009.3† | 421039.4† |
| comment.41698.any | prepared | preg_match() [literal] | 495508.9 | 952606.3 |
| comment.41698.any | prepared | preg_match() [prefix] | 17449.9 | 88563.1 |
| comment.41698.any | prepared | strtolower() + strpos() loop | 97244.1 | 311808.7 |
| comment.41698.unique | oneshot | Matcher::getMatchedKeywords() | 1120005.8 | 2106748.3 |
| comment.41698.unique | oneshot | stripos() loop | 113560.5 | 421772.4 |
| comment.41698.unique | oneshot | preg_match_all() [literal] | 167007.8† | 761540.7† |
| comment.41698.unique | oneshot | preg_match_all() [prefix] | 90913.8 | 462466.3 |
| comment.41698.unique | oneshot | strtolower() + strpos() loop | 97869.7 | 312542.5 |
| comment.41698.unique | prepared | Matcher::getMatchedKeywords() | 3367.9† | 10470.1† |
| comment.41698.unique | prepared | stripos() loop | 114088.2 | 421772.6 |
| comment.41698.unique | prepared | preg_match_all() [literal] | 166846.5 | 761539.9 |
| comment.41698.unique | prepared | preg_match_all() [prefix] | 91400.2 | 462465.7 |
| comment.41698.unique | prepared | strtolower() + strpos() loop | 98138.7 | 312541.5 |
| comment.41704.any | oneshot | Matcher::matches() | 1111832.9 | 2101993.0 |
| comment.41704.any | oneshot | stripos() loop | 77086.0 | 296087.6 |
| comment.41704.any | oneshot | preg_match() [literal] | 220642.2 | 427655.4 |
| comment.41704.any | oneshot | preg_match() [prefix] | 9292.0 | 44089.8 |
| comment.41704.any | oneshot | strtolower() + strpos() loop | 60064.5 | 223582.8 |
| comment.41704.any | prepared | Matcher::matches() | 1901.6 | 5716.0 |
| comment.41704.any | prepared | stripos() loop | 77127.4 | 296086.2 |
| comment.41704.any | prepared | preg_match() [literal] | 221199.6 | 427655.2 |
| comment.41704.any | prepared | preg_match() [prefix] | 9002.8† | 44090.2† |
| comment.41704.any | prepared | strtolower() + strpos() loop | 60818.0 | 223594.9 |
| comment.41704.unique | oneshot | Matcher::getMatchedKeywords() | 1112465.0 | 2102757.6 |
| comment.41704.unique | oneshot | stripos() loop | 77261.8 | 296816.0 |
| comment.41704.unique | oneshot | preg_match_all() [literal] | 86875.9† | 385677.3† |
| comment.41704.unique | oneshot | preg_match_all() [prefix] | 50637.9 | 242593.5 |
| comment.41704.unique | oneshot | strtolower() + strpos() loop | 60482.5 | 224296.9 |
| comment.41704.unique | prepared | Matcher::getMatchedKeywords() | 2001.0 | 6469.0 |
| comment.41704.unique | prepared | stripos() loop | 77246.0 | 296813.7 |
| comment.41704.unique | prepared | preg_match_all() [literal] | 87229.1 | 385675.8 |
| comment.41704.unique | prepared | preg_match_all() [prefix] | 50700.4 | 242593.5 |
| comment.41704.unique | prepared | strtolower() + strpos() loop | 60316.8† | 224296.6† |
| comment.41710.any | oneshot | Matcher::matches() | 1112847.3 | 2100714.8 |
| comment.41710.any | oneshot | stripos() loop | 60400.7 | 245160.5 |
| comment.41710.any | oneshot | preg_match() [literal] | 120129.4† | 235338.1† |
| comment.41710.any | oneshot | preg_match() [prefix] | 6095.8 | 26842.0 |
| comment.41710.any | oneshot | strtolower() + strpos() loop | 44410.4 | 185817.8 |
| comment.41710.any | prepared | Matcher::matches() | 1363.6 | 4438.0 |
| comment.41710.any | prepared | stripos() loop | 60049.6† | 245161.4† |
| comment.41710.any | prepared | preg_match() [literal] | 120550.9 | 235336.1 |
| comment.41710.any | prepared | preg_match() [prefix] | 6060.7 | 26842.0 |
| comment.41710.any | prepared | strtolower() + strpos() loop | 44543.2† | 185818.3† |
| comment.41710.unique | oneshot | Matcher::getMatchedKeywords() | 1108487.8 | 2101276.7 |
| comment.41710.unique | oneshot | stripos() loop | 60276.6 | 245894.2 |
| comment.41710.unique | oneshot | preg_match_all() [literal] | 53253.5 | 227009.0 |
| comment.41710.unique | oneshot | preg_match_all() [prefix] | 34119.7 | 151435.1 |
| comment.41710.unique | oneshot | strtolower() + strpos() loop | 44824.6 | 186551.3 |
| comment.41710.unique | prepared | Matcher::getMatchedKeywords() | 1466.3 | 4987.0 |
| comment.41710.unique | prepared | stripos() loop | 60238.7 | 245893.2 |
| comment.41710.unique | prepared | preg_match_all() [literal] | 53233.8 | 227008.3 |
| comment.41710.unique | prepared | preg_match_all() [prefix] | 34181.9† | 151435.4† |
| comment.41710.unique | prepared | strtolower() + strpos() loop | 44836.2 | 186551.0 |
| comment.41719.any | oneshot | Matcher::matches() | 1112297.2 | 2101852.2 |
| comment.41719.any | oneshot | stripos() loop | 73487.8 | 289291.4 |
| comment.41719.any | oneshot | preg_match() [literal] | 220022.0 | 424565.3 |
| comment.41719.any | oneshot | preg_match() [prefix] | 8931.7 | 43327.8 |
| comment.41719.any | oneshot | strtolower() + strpos() loop | 55447.9 | 219916.2 |
| comment.41719.any | prepared | Matcher::matches() | 1780.0 | 5588.0 |
| comment.41719.any | prepared | stripos() loop | 73591.6 | 289291.8 |
| comment.41719.any | prepared | preg_match() [literal] | 219894.3 | 424569.8 |
| comment.41719.any | prepared | preg_match() [prefix] | 9045.0† | 43327.9† |
| comment.41719.any | prepared | strtolower() + strpos() loop | 55485.9 | 219915.9 |
| comment.41719.unique | oneshot | Matcher::getMatchedKeywords() | 1115949.3 | 2102614.7 |
| comment.41719.unique | oneshot | stripos() loop | 73609.7† | 290006.9† |
| comment.41719.unique | oneshot | preg_match_all() [literal] | 83684.1 | 367757.1 |
| comment.41719.unique | oneshot | preg_match_all() [prefix] | 49158.7 | 232644.5 |
| comment.41719.unique | oneshot | strtolower() + strpos() loop | 55909.9 | 220670.5 |
| comment.41719.unique | prepared | Matcher::getMatchedKeywords() | 1929.8 | 6324.0 |
| comment.41719.unique | prepared | stripos() loop | 74216.5 | 290040.4 |
| comment.41719.unique | prepared | preg_match_all() [literal] | 83902.3 | 367758.3 |
| comment.41719.unique | prepared | preg_match_all() [prefix] | 49105.7 | 232644.1 |
| comment.41719.unique | prepared | strtolower() + strpos() loop | 56051.2† | 220669.5† |
| comment.55617.any | oneshot | Matcher::matches() | 1118558.9 | 2117151.5 |
| comment.55617.any | oneshot | stripos() loop | 282087.6 | 898158.4 |
| comment.55617.any | oneshot | preg_match() [literal] | 1440569.9† | 2776558.7† |
| comment.55617.any | oneshot | preg_match() [prefix] | 48593.2 | 249216.8 |
| comment.55617.any | oneshot | strtolower() + strpos() loop | 267925.7 | 667116.8 |
| comment.55617.any | prepared | Matcher::matches() | 6844.5† | 20878.9† |
| comment.55617.any | prepared | stripos() loop | 282504.6† | 898160.4† |
| comment.55617.any | prepared | preg_match() [literal] | 1442044.7† | 2776563.3† |
| comment.55617.any | prepared | preg_match() [prefix] | 48461.4 | 249217.1 |
| comment.55617.any | prepared | strtolower() + strpos() loop | 267580.0† | 667114.1† |
| comment.55617.unique | oneshot | Matcher::getMatchedKeywords() | 1124057.4 | 2120415.5 |
| comment.55617.unique | oneshot | stripos() loop | 283404.1 | 898901.6 |
| comment.55617.unique | oneshot | preg_match_all() [literal] | 486320.6 | 2201205.9 |
| comment.55617.unique | oneshot | preg_match_all() [prefix] | 321614.5† | 1302527.6† |
| comment.55617.unique | oneshot | strtolower() + strpos() loop | 267490.2 | 667845.8 |
| comment.55617.unique | prepared | Matcher::getMatchedKeywords() | 7157.1 | 24133.1 |
| comment.55617.unique | prepared | stripos() loop | 281870.1 | 898892.6 |
| comment.55617.unique | prepared | preg_match_all() [literal] | 487746.4 | 2201216.1 |
| comment.55617.unique | prepared | preg_match_all() [prefix] | 321207.0 | 1302522.7 |
| comment.55617.unique | prepared | strtolower() + strpos() loop | 268299.3 | 667847.8 |
| comment.69493.any | oneshot | Matcher::matches() | 1115024.9 | 2100464.0 |
| comment.69493.any | oneshot | stripos() loop | 56656.8 | 232889.9 |
| comment.69493.any | oneshot | preg_match() [literal] | 97033.2† | 190026.1† |
| comment.69493.any | oneshot | preg_match() [prefix] | 5411.3† | 23253.1† |
| comment.69493.any | oneshot | strtolower() + strpos() loop | 43221.1 | 177931.2 |
| comment.69493.any | prepared | Matcher::matches() | 1182.9 | 4181.0 |
| comment.69493.any | prepared | stripos() loop | 57443.3 | 232890.6 |
| comment.69493.any | prepared | preg_match() [literal] | 97162.9 | 190025.9 |
| comment.69493.any | prepared | preg_match() [prefix] | 5462.6† | 23253.0† |
| comment.69493.any | prepared | strtolower() + strpos() loop | 42994.2 | 177930.9 |
| comment.69493.unique | oneshot | Matcher::getMatchedKeywords() | 1114198.1† | 2100975.1† |
| comment.69493.unique | oneshot | stripos() loop | 56730.2 | 233623.5 |
| comment.69493.unique | oneshot | preg_match_all() [literal] | 46476.9 | 190474.3 |
| comment.69493.unique | oneshot | preg_match_all() [prefix] | 30496.1 | 131102.0 |
| comment.69493.unique | oneshot | strtolower() + strpos() loop | 43182.8† | 178664.5† |
| comment.69493.unique | prepared | Matcher::getMatchedKeywords() | 1291.5† | 4694.0† |
| comment.69493.unique | prepared | stripos() loop | 57006.1† | 233622.9† |
| comment.69493.unique | prepared | preg_match_all() [literal] | 46385.4 | 190474.0 |
| comment.69493.unique | prepared | preg_match_all() [prefix] | 30463.4 | 131101.3 |
| comment.69493.unique | prepared | strtolower() + strpos() loop | 43227.0 | 178664.1 |
| comment.69503.any | oneshot | Matcher::matches() | 1111962.6 | 2101249.6 |
| comment.69503.any | oneshot | stripos() loop | 68013.4 | 271707.2 |
| comment.69503.any | oneshot | preg_match() [literal] | 166842.6 | 324788.7 |
| comment.69503.any | oneshot | preg_match() [prefix] | 7582.8 | 34436.0 |
| comment.69503.any | oneshot | strtolower() + strpos() loop | 51708.0 | 206687.3 |
| comment.69503.any | prepared | Matcher::matches() | 1657.7 | 4961.0 |
| comment.69503.any | prepared | stripos() loop | 68219.7 | 271706.7 |
| comment.69503.any | prepared | preg_match() [literal] | 167292.6† | 324789.3† |
| comment.69503.any | prepared | preg_match() [prefix] | 7520.8 | 34436.0 |
| comment.69503.any | prepared | strtolower() + strpos() loop | 51544.0 | 206687.4 |
| comment.69503.unique | oneshot | Matcher::getMatchedKeywords() | 1110478.3 | 2101883.6 |
| comment.69503.unique | oneshot | stripos() loop | 68671.5 | 272440.0 |
| comment.69503.unique | oneshot | preg_match_all() [literal] | 66564.1 | 292933.4 |
| comment.69503.unique | oneshot | preg_match_all() [prefix] | 41092.9 | 190685.2 |
| comment.69503.unique | oneshot | strtolower() + strpos() loop | 52195.7 | 207419.8 |
| comment.69503.unique | prepared | Matcher::getMatchedKeywords() | 1757.0 | 5603.0 |
| comment.69503.unique | prepared | stripos() loop | 68063.9 | 272441.6 |
| comment.69503.unique | prepared | preg_match_all() [literal] | 66470.5 | 292933.6 |
| comment.69503.unique | prepared | preg_match_all() [prefix] | 41116.4 | 190685.1 |
| comment.69503.unique | prepared | strtolower() + strpos() loop | 52231.8† | 207419.9† |
| comment.69522.any | oneshot | Matcher::matches() | 1113798.3 | 2104925.7 |
| comment.69522.any | oneshot | stripos() loop | 8129.8† | 26424.0† |
| comment.69522.any | oneshot | preg_match() [literal] | 453248.2 | 873964.4 |
| comment.69522.any | oneshot | preg_match() [prefix] | 15811.7† | 81442.0† |
| comment.69522.any | oneshot | strtolower() + strpos() loop | 7997.1 | 21834.0 |
| comment.69522.any | prepared | Matcher::matches() | 3065.4 | 8633.0 |
| comment.69522.any | prepared | stripos() loop | 8163.5 | 26424.1 |
| comment.69522.any | prepared | preg_match() [literal] | 452796.9 | 873965.9 |
| comment.69522.any | prepared | preg_match() [prefix] | 16195.4 | 81442.0 |
| comment.69522.any | prepared | strtolower() + strpos() loop | 7998.1 | 21834.2 |
| comment.69522.unique | oneshot | Matcher::getMatchedKeywords() | 1122565.8 | 2112283.0 |
| comment.69522.unique | oneshot | stripos() loop | 174218.7 | 596052.7 |
| comment.69522.unique | oneshot | preg_match_all() [literal] | 288760.6 | 1330521.2 |
| comment.69522.unique | oneshot | preg_match_all() [prefix] | 152821.2 | 794657.3 |
| comment.69522.unique | oneshot | strtolower() + strpos() loop | 155555.2 | 452094.0 |
| comment.69522.unique | prepared | Matcher::getMatchedKeywords() | 5424.0 | 16001.0 |
| comment.69522.unique | prepared | stripos() loop | 173881.2† | 596047.6† |
| comment.69522.unique | prepared | preg_match_all() [literal] | 289068.8 | 1330520.7 |
| comment.69522.unique | prepared | preg_match_all() [prefix] | 153057.7 | 794655.1 |
| comment.69522.unique | prepared | strtolower() + strpos() loop | 154924.3 | 452094.5 |
| comment.83414.any | oneshot | Matcher::matches() | 1113390.1 | 2103733.1 |
| comment.83414.any | oneshot | stripos() loop | 98667.2 | 361994.9 |
| comment.83414.any | oneshot | preg_match() [literal] | 355275.1 | 688151.7 |
| comment.83414.any | oneshot | preg_match() [prefix] | 13147.6† | 65926.1† |
| comment.83414.any | oneshot | strtolower() + strpos() loop | 77917.6 | 271860.6 |
| comment.83414.any | prepared | Matcher::matches() | 2603.2 | 7469.0 |
| comment.83414.any | prepared | stripos() loop | 99344.9 | 361995.1 |
| comment.83414.any | prepared | preg_match() [literal] | 356926.4 | 688147.1 |
| comment.83414.any | prepared | preg_match() [prefix] | 13050.0 | 65926.0 |
| comment.83414.any | prepared | strtolower() + strpos() loop | 77897.9 | 271861.1 |
| comment.83414.unique | oneshot | Matcher::getMatchedKeywords() | 1134317.5† | 2104786.8† |
| comment.83414.unique | oneshot | stripos() loop | 99270.7† | 362728.3† |
| comment.83414.unique | oneshot | preg_match_all() [literal] | 125622.6 | 570625.6 |
| comment.83414.unique | oneshot | preg_match_all() [prefix] | 70416.1 | 350874.8 |
| comment.83414.unique | oneshot | strtolower() + strpos() loop | 78292.2† | 272593.0† |
| comment.83414.unique | prepared | Matcher::getMatchedKeywords() | 2708.4 | 8511.0 |
| comment.83414.unique | prepared | stripos() loop | 99578.3 | 362729.4 |
| comment.83414.unique | prepared | preg_match_all() [literal] | 125639.9 | 570624.6 |
| comment.83414.unique | prepared | preg_match_all() [prefix] | 71418.8† | 350875.3† |
| comment.83414.unique | prepared | strtolower() + strpos() loop | 79225.5 | 272592.6 |
| comment.97301.any | oneshot | Matcher::matches() | 1111463.0† | 2101126.2† |
| comment.97301.any | oneshot | stripos() loop | 5625.5 | 18281.0 |
| comment.97301.any | oneshot | preg_match() [literal] | 139078.6 | 270239.4 |
| comment.97301.any | oneshot | preg_match() [prefix] | 6497.6 | 29522.0 |
| comment.97301.any | oneshot | strtolower() + strpos() loop | 5258.8 | 15398.0 |
| comment.97301.any | prepared | Matcher::matches() | 1448.3 | 4848.0 |
| comment.97301.any | prepared | stripos() loop | 5620.7 | 18281.0 |
| comment.97301.any | prepared | preg_match() [literal] | 139647.9 | 270242.1 |
| comment.97301.any | prepared | preg_match() [prefix] | 6505.3 | 29522.0 |
| comment.97301.any | prepared | strtolower() + strpos() loop | 5240.7 | 15398.1 |
| comment.97301.unique | oneshot | Matcher::getMatchedKeywords() | 1114262.0† | 2107786.7† |
| comment.97301.unique | oneshot | stripos() loop | 128740.2† | 450832.0† |
| comment.97301.unique | oneshot | preg_match_all() [literal] | 187625.4 | 850895.7 |
| comment.97301.unique | oneshot | preg_match_all() [prefix] | 101618.2 | 516795.6 |
| comment.97301.unique | oneshot | strtolower() + strpos() loop | 108585.6 | 336919.0 |
| comment.97301.unique | prepared | Matcher::getMatchedKeywords() | 3890.9 | 11495.0 |
| comment.97301.unique | prepared | stripos() loop | 128103.2 | 450830.9 |
| comment.97301.unique | prepared | preg_match_all() [literal] | 187405.5 | 850896.9 |
| comment.97301.unique | prepared | preg_match_all() [prefix] | 101603.0† | 516795.3† |
| comment.97301.unique | prepared | strtolower() + strpos() loop | 108720.1 | 336919.4 |
| document.basehttpserver.all | oneshot | Matcher::matchAll() | 232235.4 | 655948.3 |
| document.basehttpserver.all | oneshot | strpos() loop | 423287.8† | 713285.8† |
| document.basehttpserver.all | oneshot | preg_match_all() [literal] | 708474.9† | 2071233.7† |
| document.basehttpserver.all | oneshot | preg_match_all() [prefix] | 723775.5 | 2069742.1 |
| document.basehttpserver.all | prepared | Matcher::matchAll() | 115663.0 | 173559.2 |
| document.basehttpserver.all | prepared | strpos() loop | 422459.1 | 713290.0 |
| document.basehttpserver.all | prepared | preg_match_all() [literal] | 712422.2 | 2071229.9 |
| document.basehttpserver.all | prepared | preg_match_all() [prefix] | 724584.3 | 2069734.2 |
| document.basehttpserver.count | oneshot | Matcher::countMatches() | 228752.9† | 644900.0† |
| document.basehttpserver.count | oneshot | strpos() loop | 407932.0† | 650840.7† |
| document.basehttpserver.count | oneshot | preg_match_all() [literal] | 681743.8 | 1974464.0 |
| document.basehttpserver.count | oneshot | preg_match_all() [prefix] | 690000.7 | 1972969.4 |
| document.basehttpserver.count | prepared | Matcher::countMatches() | 89010.6 | 162434.4 |
| document.basehttpserver.count | prepared | strpos() loop | 407626.4 | 650840.9 |
| document.basehttpserver.count | prepared | preg_match_all() [literal] | 681304.5 | 1974461.3 |
| document.basehttpserver.count | prepared | preg_match_all() [prefix] | 693994.3 | 1972974.4 |
| document.basehttpserver.replace | oneshot | Replacer::replace() | 162171.0 | 480566.7 |
| document.basehttpserver.replace | oneshot | strtr() | 1357483.6 | 4278576.5 |
| document.basehttpserver.replace | oneshot | preg_replace_callback() [literal] | 322501.7 | 1229278.1 |
| document.basehttpserver.replace | oneshot | preg_replace_callback() [prefix] | 170056.2 | 623235.0 |
| document.basehttpserver.replace | oneshot | str_replace() | 431695.2† | 676524.5† |
| document.basehttpserver.replace | prepared | Replacer::replace() | 91366.2 | 177865.1 |
| document.basehttpserver.replace | prepared | strtr() | 1352327.7 | 4278553.0 |
| document.basehttpserver.replace | prepared | preg_replace_callback() [literal] | 326537.5 | 1229279.1 |
| document.basehttpserver.replace | prepared | preg_replace_callback() [prefix] | 168116.9 | 623239.7 |
| document.basehttpserver.replace | prepared | str_replace() | 431453.7 | 676530.3 |
| document.basehttpserver.unique | oneshot | Matcher::getMatchedKeywords() | 227579.8 | 677619.2 |
| document.basehttpserver.unique | oneshot | strpos() loop | 369376.2 | 597200.2 |
| document.basehttpserver.unique | oneshot | preg_match_all() [literal] | 704194.2 | 2040452.6 |
| document.basehttpserver.unique | oneshot | preg_match_all() [prefix] | 713829.2† | 2038954.1† |
| document.basehttpserver.unique | prepared | Matcher::getMatchedKeywords() | 104679.5 | 195149.6 |
| document.basehttpserver.unique | prepared | strpos() loop | 369715.7 | 597199.5 |
| document.basehttpserver.unique | prepared | preg_match_all() [literal] | 705324.9 | 2040459.0 |
| document.basehttpserver.unique | prepared | preg_match_all() [prefix] | 718517.4 | 2038951.7 |
| document.collections.all | oneshot | Matcher::matchAll() | 599878.7† | 1084994.9† |
| document.collections.all | oneshot | strpos() loop | 1766910.4 | 2331979.0 |
| document.collections.all | oneshot | preg_match_all() [literal] | 2693096.8 | 7396608.8 |
| document.collections.all | oneshot | preg_match_all() [prefix] | 2759636.4 | 7387433.2 |
| document.collections.all | prepared | Matcher::matchAll() | 477499.7† | 602494.2† |
| document.collections.all | prepared | strpos() loop | 1762087.1 | 2331976.8 |
| document.collections.all | prepared | preg_match_all() [literal] | 2685522.9 | 7396614.4 |
| document.collections.all | prepared | preg_match_all() [prefix] | 2761355.9 | 7387444.8 |
| document.collections.count | oneshot | Matcher::countMatches() | 579717.3 | 1078920.0 |
| document.collections.count | oneshot | strpos() loop | 1750249.1 | 2312403.0 |
| document.collections.count | oneshot | preg_match_all() [literal] | 2673348.8 | 7352340.3 |
| document.collections.count | oneshot | preg_match_all() [prefix] | 2743597.5 | 7343124.3 |
| document.collections.count | prepared | Matcher::countMatches() | 422923.5 | 596422.4 |
| document.collections.count | prepared | strpos() loop | 1750036.4 | 2312409.6 |
| document.collections.count | prepared | preg_match_all() [literal] | 2675351.3 | 7352361.3 |
| document.collections.count | prepared | preg_match_all() [prefix] | 2747102.5 | 7343078.7 |
| document.collections.replace | oneshot | Replacer::replace() | 513131.3 | 944569.0 |
| document.collections.replace | oneshot | strtr() | 5042528.7† | 14976109.7† |
| document.collections.replace | oneshot | preg_replace_callback() [literal] | 1168585.5 | 4269357.0 |
| document.collections.replace | oneshot | preg_replace_callback() [prefix] | 792165.3 | 2164540.2 |
| document.collections.replace | oneshot | str_replace() | 1890393.5 | 2452025.1 |
| document.collections.replace | prepared | Replacer::replace() | 441673.0† | 642045.5† |
| document.collections.replace | prepared | strtr() | 5049807.3 | 14976077.8 |
| document.collections.replace | prepared | preg_replace_callback() [literal] | 1169710.3 | 4269349.5 |
| document.collections.replace | prepared | preg_replace_callback() [prefix] | 796727.3 | 2164538.4 |
| document.collections.replace | prepared | str_replace() | 1887359.2 | 2452009.2 |
| document.collections.unique | oneshot | Matcher::getMatchedKeywords() | 605455.3 | 1204294.5 |
| document.collections.unique | oneshot | strpos() loop | 1649832.1 | 2195323.9 |
| document.collections.unique | oneshot | preg_match_all() [literal] | 2701699.0 | 7393851.5 |
| document.collections.unique | oneshot | preg_match_all() [prefix] | 2753279.8 | 7384636.2 |
| document.collections.unique | prepared | Matcher::getMatchedKeywords() | 461133.0 | 721797.7 |
| document.collections.unique | prepared | strpos() loop | 1658984.1 | 2195333.9 |
| document.collections.unique | prepared | preg_match_all() [literal] | 2700303.5 | 7393850.7 |
| document.collections.unique | prepared | preg_match_all() [prefix] | 2756117.6 | 7384638.9 |
| document.configparser.all | oneshot | Matcher::matchAll() | 359863.4 | 848513.5 |
| document.configparser.all | oneshot | strpos() loop | 894237.9 | 1573084.8 |
| document.configparser.all | oneshot | preg_match_all() [literal] | 1425946.9 | 4166181.3 |
| document.configparser.all | oneshot | preg_match_all() [prefix] | 1454807.0 | 4175901.5 |
| document.configparser.all | prepared | Matcher::matchAll() | 238275.4 | 366221.7 |
| document.configparser.all | prepared | strpos() loop | 891387.2 | 1573067.5 |
| document.configparser.all | prepared | preg_match_all() [literal] | 1425318.2† | 4166180.4† |
| document.configparser.all | prepared | preg_match_all() [prefix] | 1450470.9 | 4175911.2 |
| document.configparser.count | oneshot | Matcher::countMatches() | 336565.9 | 790740.6 |
| document.configparser.count | oneshot | strpos() loop | 813430.4 | 1214113.1 |
| document.configparser.count | oneshot | preg_match_all() [literal] | 1305386.2† | 3690407.3† |
| document.configparser.count | oneshot | preg_match_all() [prefix] | 1342370.4 | 3700122.5 |
| document.configparser.count | prepared | Matcher::countMatches() | 188574.7 | 308369.9 |
| document.configparser.count | prepared | strpos() loop | 810154.3† | 1214104.9† |
| document.configparser.count | prepared | preg_match_all() [literal] | 1308132.7† | 3690401.7† |
| document.configparser.count | prepared | preg_match_all() [prefix] | 1339229.1† | 3700129.0† |
| document.configparser.replace | oneshot | Replacer::replace() | 262996.2† | 645035.7† |
| document.configparser.replace | oneshot | strtr() | 2237423.3† | 7012636.5† |
| document.configparser.replace | oneshot | preg_replace_callback() [literal] | 563826.8 | 2109937.3 |
| document.configparser.replace | oneshot | preg_replace_callback() [prefix] | 340119.2† | 1134816.9† |
| document.configparser.replace | oneshot | str_replace() | 817300.5 | 1207605.0 |
| document.configparser.replace | prepared | Replacer::replace() | 195132.1 | 342617.1 |
| document.configparser.replace | prepared | strtr() | 2236894.5 | 7012595.4 |
| document.configparser.replace | prepared | preg_replace_callback() [literal] | 561504.6 | 2109928.0 |
| document.configparser.replace | prepared | preg_replace_callback() [prefix] | 339873.3 | 1134815.0 |
| document.configparser.replace | prepared | str_replace() | 816009.1 | 1207600.6 |
| document.configparser.unique | oneshot | Matcher::getMatchedKeywords() | 343250.9† | 851568.9† |
| document.configparser.unique | oneshot | strpos() loop | 757275.2 | 1104616.7 |
| document.configparser.unique | oneshot | preg_match_all() [literal] | 1373100.1 | 3935867.5 |
| document.configparser.unique | oneshot | preg_match_all() [prefix] | 1410498.4 | 3945571.1 |
| document.configparser.unique | prepared | Matcher::getMatchedKeywords() | 211543.6 | 369198.4 |
| document.configparser.unique | prepared | strpos() loop | 754819.9 | 1104604.4 |
| document.configparser.unique | prepared | preg_match_all() [literal] | 1374945.6 | 3935862.5 |
| document.configparser.unique | prepared | preg_match_all() [prefix] | 1408383.6 | 3945568.1 |
| document.cookie.all | oneshot | Matcher::matchAll() | 239622.0 | 682882.5 |
| document.cookie.all | oneshot | strpos() loop | 448485.9† | 959795.4† |
| document.cookie.all | oneshot | preg_match_all() [literal] | 713359.6 | 2324034.7 |
| document.cookie.all | oneshot | preg_match_all() [prefix] | 726600.9† | 2315949.1† |
| document.cookie.all | prepared | Matcher::matchAll() | 116396.0† | 200341.3† |
| document.cookie.all | prepared | strpos() loop | 448368.0 | 959788.2 |
| document.cookie.all | prepared | preg_match_all() [literal] | 709315.4† | 2324032.9† |
| document.cookie.all | prepared | preg_match_all() [prefix] | 728868.8 | 2315930.5 |
| document.cookie.count | oneshot | Matcher::countMatches() | 220931.1 | 630449.8 |
| document.cookie.count | oneshot | strpos() loop | 369314.8† | 602704.9† |
| document.cookie.count | oneshot | preg_match_all() [literal] | 608334.8† | 1891245.0† |
| document.cookie.count | oneshot | preg_match_all() [prefix] | 623129.9 | 1883165.9 |
| document.cookie.count | prepared | Matcher::countMatches() | 81382.0 | 147982.4 |
| document.cookie.count | prepared | strpos() loop | 368220.7 | 602707.8 |
| document.cookie.count | prepared | preg_match_all() [literal] | 605257.5 | 1891257.1 |
| document.cookie.count | prepared | preg_match_all() [prefix] | 627984.5 | 1883171.2 |
| document.cookie.replace | oneshot | Replacer::replace() | 145498.1 | 471091.3 |
| document.cookie.replace | oneshot | strtr() | 1102634.1† | 3607466.3† |
| document.cookie.replace | oneshot | preg_replace_callback() [literal] | 282167.6 | 1133383.7 |
| document.cookie.replace | oneshot | preg_replace_callback() [prefix] | 150717.5† | 622510.9† |
| document.cookie.replace | oneshot | str_replace() | 385897.5 | 611048.9 |
| document.cookie.replace | prepared | Replacer::replace() | 71625.6 | 168346.9 |
| document.cookie.replace | prepared | strtr() | 1105208.7† | 3607465.7† |
| document.cookie.replace | prepared | preg_replace_callback() [literal] | 282715.1 | 1133373.6 |
| document.cookie.replace | prepared | preg_replace_callback() [prefix] | 151824.8† | 622511.1† |
| document.cookie.replace | prepared | str_replace() | 386734.4 | 611048.5 |
| document.cookie.unique | oneshot | Matcher::getMatchedKeywords() | 217818.2† | 661616.2† |
| document.cookie.unique | oneshot | strpos() loop | 344882.2 | 543721.7 |
| document.cookie.unique | oneshot | preg_match_all() [literal] | 666786.8† | 2109719.8† |
| document.cookie.unique | oneshot | preg_match_all() [prefix] | 684278.4 | 2101641.7 |
| document.cookie.unique | prepared | Matcher::getMatchedKeywords() | 86353.8 | 179150.3 |
| document.cookie.unique | prepared | strpos() loop | 345331.7 | 543723.7 |
| document.cookie.unique | prepared | preg_match_all() [literal] | 668384.4 | 2109720.8 |
| document.cookie.unique | prepared | preg_match_all() [prefix] | 683129.6 | 2101632.3 |
| document.cookielib.all | oneshot | Matcher::matchAll() | 501707.2 | 1059561.6 |
| document.cookielib.all | oneshot | strpos() loop | 1521819.8 | 2910290.9 |
| document.cookielib.all | oneshot | preg_match_all() [literal] | 2322979.5 | 6849570.6 |
| document.cookielib.all | oneshot | preg_match_all() [prefix] | 2389109.7 | 6840273.0 |
| document.cookielib.all | prepared | Matcher::matchAll() | 373867.0† | 576814.1† |
| document.cookielib.all | prepared | strpos() loop | 1520782.9 | 2910296.9 |
| document.cookielib.all | prepared | preg_match_all() [literal] | 2331579.5 | 6849587.8 |
| document.cookielib.all | prepared | preg_match_all() [prefix] | 2397106.5† | 6840254.1† |
| document.cookielib.count | oneshot | Matcher::countMatches() | 455054.4 | 926334.4 |
| document.cookielib.count | oneshot | strpos() loop | 1260442.2 | 1758042.3 |
| document.cookielib.count | oneshot | preg_match_all() [literal] | 2007995.5 | 5486920.3 |
| document.cookielib.count | oneshot | preg_match_all() [prefix] | 2085189.2 | 5477677.3 |
| document.cookielib.count | prepared | Matcher::countMatches() | 295768.5 | 444029.1 |
| document.cookielib.count | prepared | strpos() loop | 1259792.8† | 1758046.0† |
| document.cookielib.count | prepared | preg_match_all() [literal] | 2016940.5 | 5486957.9 |
| document.cookielib.count | prepared | preg_match_all() [prefix] | 2082288.8† | 5477697.7† |
| document.cookielib.replace | oneshot | Replacer::replace() | 349754.2 | 798414.8 |
| document.cookielib.replace | oneshot | strtr() | 3693015.2 | 11094753.7 |
| document.cookielib.replace | oneshot | preg_replace_callback() [literal] | 912862.1† | 3397561.8† |
| document.cookielib.replace | oneshot | preg_replace_callback() [prefix] | 599321.5 | 1832202.6 |
| document.cookielib.replace | oneshot | str_replace() | 1369055.1 | 1823987.2 |
| document.cookielib.replace | prepared | Replacer::replace() | 287854.8† | 495953.4† |
| document.cookielib.replace | prepared | strtr() | 3707969.9 | 11094735.8 |
| document.cookielib.replace | prepared | preg_replace_callback() [literal] | 907599.4 | 3397564.3 |
| document.cookielib.replace | prepared | preg_replace_callback() [prefix] | 594312.4 | 1832203.6 |
| document.cookielib.replace | prepared | str_replace() | 1367701.4 | 1823998.6 |
| document.cookielib.unique | oneshot | Matcher::getMatchedKeywords() | 479430.2 | 1014312.5 |
| document.cookielib.unique | oneshot | strpos() loop | 1129882.3† | 1550902.1† |
| document.cookielib.unique | oneshot | preg_match_all() [literal] | 2140496.1 | 6002162.4 |
| document.cookielib.unique | oneshot | preg_match_all() [prefix] | 2220561.8 | 5992939.7 |
| document.cookielib.unique | prepared | Matcher::getMatchedKeywords() | 316650.4† | 532011.2† |
| document.cookielib.unique | prepared | strpos() loop | 1125520.0† | 1550870.1† |
| document.cookielib.unique | prepared | preg_match_all() [literal] | 2139748.0 | 6002211.1 |
| document.cookielib.unique | prepared | preg_match_all() [prefix] | 2210565.9 | 5992952.7 |
| document.httplib.all | oneshot | Matcher::matchAll() | 395862.3† | 947046.5† |
| document.httplib.all | oneshot | strpos() loop | 1237038.7 | 1846857.6 |
| document.httplib.all | oneshot | preg_match_all() [literal] | 1715661.9 | 6104895.8 |
| document.httplib.all | oneshot | preg_match_all() [prefix] | 1744611.3 | 6113072.7 |
| document.httplib.all | prepared | Matcher::matchAll() | 274825.0 | 464608.9 |
| document.httplib.all | prepared | strpos() loop | 1237474.8 | 1846841.5 |
| document.httplib.all | prepared | preg_match_all() [literal] | 1725260.9 | 6104897.6 |
| document.httplib.all | prepared | preg_match_all() [prefix] | 1747280.5 | 6113085.5 |
| document.httplib.count | oneshot | Matcher::countMatches() | 361254.3 | 932043.8 |
| document.httplib.count | oneshot | strpos() loop | 1215791.6 | 1773352.0 |
| document.httplib.count | oneshot | preg_match_all() [literal] | 1682223.3 | 5998783.9 |
| document.httplib.count | oneshot | preg_match_all() [prefix] | 1714184.3 | 6007009.9 |
| document.httplib.count | prepared | Matcher::countMatches() | 213370.3† | 449546.7† |
| document.httplib.count | prepared | strpos() loop | 1218110.6 | 1773334.3 |
| document.httplib.count | prepared | preg_match_all() [literal] | 1686501.2 | 5998790.3 |
| document.httplib.count | prepared | preg_match_all() [prefix] | 1714083.0 | 6006946.5 |
| document.httplib.replace | oneshot | Replacer::replace() | 284113.2 | 794620.1 |
| document.httplib.replace | oneshot | strtr() | 2386218.2 | 8234214.0 |
| document.httplib.replace | oneshot | preg_replace_callback() [literal] | 628048.5 | 2507056.3 |
| document.httplib.replace | oneshot | preg_replace_callback() [prefix] | 377049.7 | 1388217.7 |
| document.httplib.replace | oneshot | str_replace() | 1282165.9† | 1810441.2† |
| document.httplib.replace | prepared | Replacer::replace() | 208171.9 | 492094.2 |
| document.httplib.replace | prepared | strtr() | 2399373.7 | 8234221.2 |
| document.httplib.replace | prepared | preg_replace_callback() [literal] | 629510.5 | 2507053.0 |
| document.httplib.replace | prepared | preg_replace_callback() [prefix] | 378209.0 | 1388216.2 |
| document.httplib.replace | prepared | str_replace() | 1284250.3† | 1810466.0† |
| document.httplib.unique | oneshot | Matcher::getMatchedKeywords() | 376564.9 | 1045684.3 |
| document.httplib.unique | oneshot | strpos() loop | 1160871.9 | 1715909.5 |
| document.httplib.unique | oneshot | preg_match_all() [literal] | 1706083.6 | 6075906.1 |
| document.httplib.unique | oneshot | preg_match_all() [prefix] | 1744534.5 | 6084105.7 |
| document.httplib.unique | prepared | Matcher::getMatchedKeywords() | 240140.2 | 563184.9 |
| document.httplib.unique | prepared | strpos() loop | 1161450.1 | 1715912.0 |
| document.httplib.unique | prepared | preg_match_all() [literal] | 1708019.2 | 6075910.5 |
| document.httplib.unique | prepared | preg_match_all() [prefix] | 1741092.9 | 6084089.5 |
| document.pickle.all | oneshot | Matcher::matchAll() | 565258.1 | 1092147.6 |
| document.pickle.all | oneshot | strpos() loop | 1738396.8† | 2428364.6† |
| document.pickle.all | oneshot | preg_match_all() [literal] | 2785722.3 | 7232178.9 |
| document.pickle.all | oneshot | preg_match_all() [prefix] | 2832558.7 | 7233502.1 |
| document.pickle.all | prepared | Matcher::matchAll() | 444931.0 | 609795.9 |
| document.pickle.all | prepared | strpos() loop | 1742928.1 | 2428375.8 |
| document.pickle.all | prepared | preg_match_all() [literal] | 2779500.4 | 7232188.8 |
| document.pickle.all | prepared | preg_match_all() [prefix] | 2829525.5 | 7233560.1 |
| document.pickle.count | oneshot | Matcher::countMatches() | 567865.6 | 1063240.9 |
| document.pickle.count | oneshot | strpos() loop | 1685980.1 | 2250843.4 |
| document.pickle.count | oneshot | preg_match_all() [literal] | 2711120.9 | 6989841.8 |
| document.pickle.count | oneshot | preg_match_all() [prefix] | 2761978.7 | 6991236.4 |
| document.pickle.count | prepared | Matcher::countMatches() | 414206.4† | 580739.7† |
| document.pickle.count | prepared | strpos() loop | 1689431.2 | 2250847.3 |
| document.pickle.count | prepared | preg_match_all() [literal] | 2714341.1 | 6989831.6 |
| document.pickle.count | prepared | preg_match_all() [prefix] | 2766726.3 | 6991251.2 |
| document.pickle.replace | oneshot | Replacer::replace() | 472398.2 | 934770.6 |
| document.pickle.replace | oneshot | strtr() | 5210360.0 | 15609225.4 |
| document.pickle.replace | oneshot | preg_replace_callback() [literal] | 1220127.3 | 4441210.6 |
| document.pickle.replace | oneshot | preg_replace_callback() [prefix] | 817037.8 | 2231599.9 |
| document.pickle.replace | oneshot | str_replace() | 1913815.0 | 2457247.7 |
| document.pickle.replace | prepared | Replacer::replace() | 405358.1 | 632245.2 |
| document.pickle.replace | prepared | strtr() | 5223762.8 | 15609323.7 |
| document.pickle.replace | prepared | preg_replace_callback() [literal] | 1222672.7† | 4441210.6† |
| document.pickle.replace | prepared | preg_replace_callback() [prefix] | 816587.0 | 2231600.7 |
| document.pickle.replace | prepared | str_replace() | 1908048.7 | 2457276.5 |
| document.pickle.unique | oneshot | Matcher::getMatchedKeywords() | 588604.2 | 1177408.9 |
| document.pickle.unique | oneshot | strpos() loop | 1560664.0 | 2096608.4 |
| document.pickle.unique | oneshot | preg_match_all() [literal] | 2765750.4 | 7126538.5 |
| document.pickle.unique | oneshot | preg_match_all() [prefix] | 2817122.2 | 7128000.4 |
| document.pickle.unique | prepared | Matcher::getMatchedKeywords() | 449900.9 | 694904.1 |
| document.pickle.unique | prepared | strpos() loop | 1562089.3 | 2096615.9 |
| document.pickle.unique | prepared | preg_match_all() [literal] | 2761673.0† | 7126607.6† |
| document.pickle.unique | prepared | preg_match_all() [prefix] | 2815501.5 | 7127949.2 |
| document.queue.all | oneshot | Matcher::matchAll() | 206930.9 | 619914.2 |
| document.queue.all | oneshot | strpos() loop | 313467.8 | 631864.9 |
| document.queue.all | oneshot | preg_match_all() [literal] | 427466.4 | 1592301.8 |
| document.queue.all | oneshot | preg_match_all() [prefix] | 475063.6† | 1595127.4† |
| document.queue.all | prepared | Matcher::matchAll() | 86402.9 | 137608.3 |
| document.queue.all | prepared | strpos() loop | 313231.8 | 631870.8 |
| document.queue.all | prepared | preg_match_all() [literal] | 429622.8† | 1592303.0† |
| document.queue.all | prepared | preg_match_all() [prefix] | 474328.6 | 1595116.6 |
| document.queue.count | oneshot | Matcher::countMatches() | 181184.3 | 592371.8 |
| document.queue.count | oneshot | strpos() loop | 270664.4 | 450618.7 |
| document.queue.count | oneshot | preg_match_all() [literal] | 365560.5 | 1347137.1 |
| document.queue.count | oneshot | preg_match_all() [prefix] | 413798.8 | 1349945.9 |
| document.queue.count | prepared | Matcher::countMatches() | 43849.0 | 110024.9 |
| document.queue.count | prepared | strpos() loop | 270163.0 | 450616.5 |
| document.queue.count | prepared | preg_match_all() [literal] | 364904.2 | 1347127.7 |
| document.queue.count | prepared | preg_match_all() [prefix] | 412890.7† | 1349953.0† |
| document.queue.replace | oneshot | Replacer::replace() | 119745.8 | 425951.9 |
| document.queue.replace | oneshot | strtr() | 788616.6 | 2740625.0 |
| document.queue.replace | oneshot | preg_replace_callback() [literal] | 205840.4† | 835995.1† |
| document.queue.replace | oneshot | preg_replace_callback() [prefix] | 94921.3 | 446248.7 |
| document.queue.replace | oneshot | str_replace() | 273417.5 | 442066.0 |
| document.queue.replace | prepared | Replacer::replace() | 51153.1† | 123246.8† |
| document.queue.replace | prepared | strtr() | 781531.4 | 2740636.0 |
| document.queue.replace | prepared | preg_replace_callback() [literal] | 206386.5 | 835997.3 |
| document.queue.replace | prepared | preg_replace_callback() [prefix] | 95167.9† | 446248.0† |
| document.queue.replace | prepared | str_replace() | 273790.1 | 442066.8 |
| document.queue.unique | oneshot | Matcher::getMatchedKeywords() | 185498.0 | 615170.6 |
| document.queue.unique | oneshot | strpos() loop | 257089.1 | 414044.5 |
| document.queue.unique | oneshot | preg_match_all() [literal] | 401196.9 | 1471353.6 |
| document.queue.unique | oneshot | preg_match_all() [prefix] | 446972.5 | 1474246.1 |
| document.queue.unique | prepared | Matcher::getMatchedKeywords() | 60885.3 | 132817.4 |
| document.queue.unique | prepared | strpos() loop | 257218.1† | 414049.3† |
| document.queue.unique | prepared | preg_match_all() [literal] | 400622.1 | 1471426.2 |
| document.queue.unique | prepared | preg_match_all() [prefix] | 447834.1 | 1474244.1 |
| document.robotparser.all | oneshot | Matcher::matchAll() | 131141.7 | 521740.0 |
| document.robotparser.all | oneshot | strpos() loop | 87739.1 | 166117.3 |
| document.robotparser.all | oneshot | preg_match_all() [literal] | 92518.4 | 454199.2 |
| document.robotparser.all | oneshot | preg_match_all() [prefix] | 91919.8 | 454034.5 |
| document.robotparser.all | prepared | Matcher::matchAll() | 18157.0 | 39331.1 |
| document.robotparser.all | prepared | strpos() loop | 87794.2 | 166117.2 |
| document.robotparser.all | prepared | preg_match_all() [literal] | 92643.6† | 454199.5† |
| document.robotparser.all | prepared | preg_match_all() [prefix] | 91977.0 | 454035.4 |
| document.robotparser.count | oneshot | Matcher::countMatches() | 123365.9† | 518234.7† |
| document.robotparser.count | oneshot | strpos() loop | 85281.2 | 156518.9 |
| document.robotparser.count | oneshot | preg_match_all() [literal] | 84169.1 | 424577.3 |
| document.robotparser.count | oneshot | preg_match_all() [prefix] | 83168.7 | 424414.1 |
| document.robotparser.count | prepared | Matcher::countMatches() | 11879.4† | 35826.1† |
| document.robotparser.count | prepared | strpos() loop | 85382.9 | 156516.0 |
| document.robotparser.count | prepared | preg_match_all() [literal] | 84244.0 | 424578.3 |
| document.robotparser.count | prepared | preg_match_all() [prefix] | 83061.5 | 424414.9 |
| document.robotparser.replace | oneshot | Replacer::replace() | 81905.5 | 341804.0 |
| document.robotparser.replace | oneshot | strtr() | 205829.2 | 862778.1 |
| document.robotparser.replace | oneshot | preg_replace_callback() [literal] | 55776.4 | 255097.3 |
| document.robotparser.replace | oneshot | preg_replace_callback() [prefix] | 26761.4 | 133676.7 |
| document.robotparser.replace | oneshot | str_replace() | 85843.8 | 152466.2 |
| document.robotparser.replace | prepared | Replacer::replace() | 12245.9 | 39321.9 |
| document.robotparser.replace | prepared | strtr() | 206127.1 | 862777.6 |
| document.robotparser.replace | prepared | preg_replace_callback() [literal] | 55965.0 | 255097.9 |
| document.robotparser.replace | prepared | preg_replace_callback() [prefix] | 26804.8† | 133677.0† |
| document.robotparser.replace | prepared | str_replace() | 85740.2 | 152466.0 |
| document.robotparser.unique | oneshot | Matcher::getMatchedKeywords() | 125685.8 | 525419.3 |
| document.robotparser.unique | oneshot | strpos() loop | 82449.6 | 150911.4 |
| document.robotparser.unique | oneshot | preg_match_all() [literal] | 92386.7 | 454739.3 |
| document.robotparser.unique | oneshot | preg_match_all() [prefix] | 91790.3 | 454576.0 |
| document.robotparser.unique | prepared | Matcher::getMatchedKeywords() | 12980.4† | 43013.0† |
| document.robotparser.unique | prepared | strpos() loop | 82469.7 | 150912.6 |
| document.robotparser.unique | prepared | preg_match_all() [literal] | 92898.2† | 454739.1† |
| document.robotparser.unique | prepared | preg_match_all() [prefix] | 91973.6 | 454575.3 |
| document.simplehttpserver.all | oneshot | Matcher::matchAll() | 159292.3 | 567356.0 |
| document.simplehttpserver.all | oneshot | strpos() loop | 192306.5† | 360594.1† |
| document.simplehttpserver.all | oneshot | preg_match_all() [literal] | 238903.9 | 988675.6 |
| document.simplehttpserver.all | oneshot | preg_match_all() [prefix] | 279391.8 | 988786.1 |
| document.simplehttpserver.all | prepared | Matcher::matchAll() | 45360.9 | 84789.4 |
| document.simplehttpserver.all | prepared | strpos() loop | 192490.2 | 360593.5 |
| document.simplehttpserver.all | prepared | preg_match_all() [literal] | 238124.5 | 988677.6 |
| document.simplehttpserver.all | prepared | preg_match_all() [prefix] | 278221.1 | 988792.4 |
| document.simplehttpserver.count | oneshot | Matcher::countMatches() | 151057.0 | 556609.6 |
| document.simplehttpserver.count | oneshot | strpos() loop | 178642.9† | 306121.0† |
| document.simplehttpserver.count | oneshot | preg_match_all() [literal] | 212469.8 | 900847.7 |
| document.simplehttpserver.count | oneshot | preg_match_all() [prefix] | 251815.6 | 900963.2 |
| document.simplehttpserver.count | prepared | Matcher::countMatches() | 26315.8 | 74257.6 |
| document.simplehttpserver.count | prepared | strpos() loop | 178434.4 | 306122.4 |
| document.simplehttpserver.count | prepared | preg_match_all() [literal] | 212513.7 | 900850.4 |
| document.simplehttpserver.count | prepared | preg_match_all() [prefix] | 252414.4 | 900963.9 |
| document.simplehttpserver.replace | oneshot | Replacer::replace() | 98212.5† | 384636.8† |
| document.simplehttpserver.replace | oneshot | strtr() | 519088.5 | 1801173.2 |
| document.simplehttpserver.replace | oneshot | preg_replace_callback() [literal] | 124954.2 | 533463.0 |
| document.simplehttpserver.replace | oneshot | preg_replace_callback() [prefix] | 57919.8† | 279442.4† |
| document.simplehttpserver.replace | oneshot | str_replace() | 179144.4 | 301543.2 |
| document.simplehttpserver.replace | prepared | Replacer::replace() | 29955.1 | 82139.3 |
| document.simplehttpserver.replace | prepared | strtr() | 521028.9 | 1801176.7 |
| document.simplehttpserver.replace | prepared | preg_replace_callback() [literal] | 125010.5 | 533461.6 |
| document.simplehttpserver.replace | prepared | preg_replace_callback() [prefix] | 57482.8 | 279442.7 |
| document.simplehttpserver.replace | prepared | str_replace() | 179281.2† | 301541.8† |
| document.simplehttpserver.unique | oneshot | Matcher::getMatchedKeywords() | 155370.0 | 571512.0 |
| document.simplehttpserver.unique | oneshot | strpos() loop | 171360.6 | 290774.6 |
| document.simplehttpserver.unique | oneshot | preg_match_all() [literal] | 232562.1† | 962483.5† |
| document.simplehttpserver.unique | oneshot | preg_match_all() [prefix] | 275091.7 | 962594.9 |
| document.simplehttpserver.unique | prepared | Matcher::getMatchedKeywords() | 37574.3 | 89160.7 |
| document.simplehttpserver.unique | prepared | strpos() loop | 171114.4 | 290776.7 |
| document.simplehttpserver.unique | prepared | preg_match_all() [literal] | 231312.4 | 962475.0 |
| document.simplehttpserver.unique | prepared | preg_match_all() [prefix] | 272753.4 | 962595.4 |
| document.simplexmlrpcserver.all | oneshot | Matcher::matchAll() | 241468.0 | 679972.1 |
| document.simplexmlrpcserver.all | oneshot | strpos() loop | 469125.5 | 848398.0 |
| document.simplexmlrpcserver.all | oneshot | preg_match_all() [literal] | 768006.5 | 2308039.6 |
| document.simplexmlrpcserver.all | oneshot | preg_match_all() [prefix] | 787166.2† | 2305897.1† |
| document.simplexmlrpcserver.all | prepared | Matcher::matchAll() | 123312.5 | 197298.6 |
| document.simplexmlrpcserver.all | prepared | strpos() loop | 468679.6 | 848393.4 |
| document.simplexmlrpcserver.all | prepared | preg_match_all() [literal] | 766242.7 | 2308037.7 |
| document.simplexmlrpcserver.all | prepared | preg_match_all() [prefix] | 780174.6 | 2305897.7 |
| document.simplexmlrpcserver.count | oneshot | Matcher::countMatches() | 236590.4 | 657116.8 |
| document.simplexmlrpcserver.count | oneshot | strpos() loop | 433170.6 | 697867.2 |
| document.simplexmlrpcserver.count | oneshot | preg_match_all() [literal] | 709613.5 | 2108792.5 |
| document.simplexmlrpcserver.count | oneshot | preg_match_all() [prefix] | 723899.2 | 2106655.4 |
| document.simplexmlrpcserver.count | prepared | Matcher::countMatches() | 100409.1 | 174650.7 |
| document.simplexmlrpcserver.count | prepared | strpos() loop | 432518.4 | 697865.2 |
| document.simplexmlrpcserver.count | prepared | preg_match_all() [literal] | 710333.7† | 2108806.4† |
| document.simplexmlrpcserver.count | prepared | preg_match_all() [prefix] | 726256.9 | 2106648.1 |
| document.simplexmlrpcserver.replace | oneshot | Replacer::replace() | 163741.3 | 495136.6 |
| document.simplexmlrpcserver.replace | oneshot | strtr() | 1400994.7† | 4461354.7† |
| document.simplexmlrpcserver.replace | oneshot | preg_replace_callback() [literal] | 326819.0† | 1305776.2† |
| document.simplexmlrpcserver.replace | oneshot | preg_replace_callback() [prefix] | 168694.3 | 674623.9 |
| document.simplexmlrpcserver.replace | oneshot | str_replace() | 465466.5 | 740828.8 |
| document.simplexmlrpcserver.replace | prepared | Replacer::replace() | 92298.2 | 192437.4 |
| document.simplexmlrpcserver.replace | prepared | strtr() | 1374952.9 | 4461368.6 |
| document.simplexmlrpcserver.replace | prepared | preg_replace_callback() [literal] | 323600.2 | 1305777.5 |
| document.simplexmlrpcserver.replace | prepared | preg_replace_callback() [prefix] | 164897.5 | 674626.2 |
| document.simplexmlrpcserver.replace | prepared | str_replace() | 466306.6† | 740836.3† |
| document.simplexmlrpcserver.unique | oneshot | Matcher::getMatchedKeywords() | 233069.4 | 691433.6 |
| document.simplexmlrpcserver.unique | oneshot | strpos() loop | 389448.5 | 621937.2 |
| document.simplexmlrpcserver.unique | oneshot | preg_match_all() [literal] | 745490.5 | 2223098.6 |
| document.simplexmlrpcserver.unique | oneshot | preg_match_all() [prefix] | 762346.4 | 2220980.4 |
| document.simplexmlrpcserver.unique | prepared | Matcher::getMatchedKeywords() | 107751.4 | 208965.5 |
| document.simplexmlrpcserver.unique | prepared | strpos() loop | 390446.7 | 621944.5 |
| document.simplexmlrpcserver.unique | prepared | preg_match_all() [literal] | 746387.8† | 2223093.4† |
| document.simplexmlrpcserver.unique | prepared | preg_match_all() [prefix] | 762635.2 | 2220949.1 |
| document.socketserver.all | oneshot | Matcher::matchAll() | 386775.1 | 863529.4 |
| document.socketserver.all | oneshot | strpos() loop | 1031102.9† | 1591864.8† |
| document.socketserver.all | oneshot | preg_match_all() [literal] | 1637904.8† | 4547861.3† |
| document.socketserver.all | oneshot | preg_match_all() [prefix] | 1671916.4 | 4556944.4 |
| document.socketserver.all | prepared | Matcher::matchAll() | 260105.0 | 380966.5 |
| document.socketserver.all | prepared | strpos() loop | 1031883.7 | 1591859.4 |
| document.socketserver.all | prepared | preg_match_all() [literal] | 1640271.2 | 4547864.6 |
| document.socketserver.all | prepared | preg_match_all() [prefix] | 1683569.2 | 4556926.3 |
| document.socketserver.count | oneshot | Matcher::countMatches() | 373588.6 | 829993.9 |
| document.socketserver.count | oneshot | strpos() loop | 979361.3 | 1383276.0 |
| document.socketserver.count | oneshot | preg_match_all() [literal] | 1573482.8† | 4264608.4† |
| document.socketserver.count | oneshot | preg_match_all() [prefix] | 1600412.3 | 4273686.1 |
| document.socketserver.count | prepared | Matcher::countMatches() | 221908.8 | 347392.9 |
| document.socketserver.count | prepared | strpos() loop | 979427.0† | 1383276.2† |
| document.socketserver.count | prepared | preg_match_all() [literal] | 1563709.8† | 4264616.1† |
| document.socketserver.count | prepared | preg_match_all() [prefix] | 1608035.8 | 4273684.4 |
| document.socketserver.replace | oneshot | Replacer::replace() | 297794.4† | 686081.3† |
| document.socketserver.replace | oneshot | strtr() | 2959153.7 | 9072277.6 |
| document.socketserver.replace | oneshot | preg_replace_callback() [literal] | 702760.3 | 2625307.2 |
| document.socketserver.replace | oneshot | preg_replace_callback() [prefix] | 430767.0 | 1342179.3 |
| document.socketserver.replace | oneshot | str_replace() | 1052075.3 | 1455177.6 |
| document.socketserver.replace | prepared | Replacer::replace() | 225307.8 | 383387.4 |
| document.socketserver.replace | prepared | strtr() | 2953412.1 | 9072257.1 |
| document.socketserver.replace | prepared | preg_replace_callback() [literal] | 703720.0 | 2625301.6 |
| document.socketserver.replace | prepared | preg_replace_callback() [prefix] | 433013.8 | 1342173.6 |
| document.socketserver.replace | prepared | str_replace() | 1050084.0 | 1455167.4 |
| document.socketserver.unique | oneshot | Matcher::getMatchedKeywords() | 378385.0 | 899466.9 |
| document.socketserver.unique | oneshot | strpos() loop | 873642.2† | 1239069.0† |
| document.socketserver.unique | oneshot | preg_match_all() [literal] | 1608184.3 | 4414706.6 |
| document.socketserver.unique | oneshot | preg_match_all() [prefix] | 1650022.0 | 4423765.7 |
| document.socketserver.unique | prepared | Matcher::getMatchedKeywords() | 244240.2 | 416871.5 |
| document.socketserver.unique | prepared | strpos() loop | 871451.0 | 1239038.1 |
| document.socketserver.unique | prepared | preg_match_all() [literal] | 1611843.2† | 4414697.6† |
| document.socketserver.unique | prepared | preg_match_all() [prefix] | 1645164.5 | 4423787.3 |
| document.stringio.all | oneshot | Matcher::matchAll() | 157926.3 | 580223.2 |
| document.stringio.all | oneshot | strpos() loop | 206304.7 | 469167.0 |
| document.stringio.all | oneshot | preg_match_all() [literal] | 249180.1 | 1105895.6 |
| document.stringio.all | oneshot | preg_match_all() [prefix] | 278270.2 | 1113136.1 |
| document.stringio.all | prepared | Matcher::matchAll() | 44785.7† | 97924.2† |
| document.stringio.all | prepared | strpos() loop | 205949.8 | 469168.7 |
| document.stringio.all | prepared | preg_match_all() [literal] | 248495.9 | 1105895.8 |
| document.stringio.all | prepared | preg_match_all() [prefix] | 278180.8† | 1113141.2† |
| document.stringio.count | oneshot | Matcher::countMatches() | 143908.8† | 550107.9† |
| document.stringio.count | oneshot | strpos() loop | 166432.0 | 294153.2 |
| document.stringio.count | oneshot | preg_match_all() [literal] | 187100.1† | 862482.0† |
| document.stringio.count | oneshot | preg_match_all() [prefix] | 218805.9 | 869723.8 |
| document.stringio.count | prepared | Matcher::countMatches() | 22954.9† | 67555.1† |
| document.stringio.count | prepared | strpos() loop | 166682.5† | 294151.9† |
| document.stringio.count | prepared | preg_match_all() [literal] | 187135.6 | 862482.8 |
| document.stringio.count | prepared | preg_match_all() [prefix] | 218930.6 | 869722.8 |
| document.stringio.replace | oneshot | Replacer::replace() | 93858.4 | 379777.6 |
| document.stringio.replace | oneshot | strtr() | 430868.1 | 1557683.3 |
| document.stringio.replace | oneshot | preg_replace_callback() [literal] | 119288.8† | 499356.6† |
| document.stringio.replace | oneshot | preg_replace_callback() [prefix] | 58508.7† | 280897.3† |
| document.stringio.replace | oneshot | str_replace() | 160926.5 | 270967.1 |
| document.stringio.replace | prepared | Replacer::replace() | 25555.0 | 77222.6 |
| document.stringio.replace | prepared | strtr() | 429643.4 | 1557685.2 |
| document.stringio.replace | prepared | preg_replace_callback() [literal] | 119602.0 | 499357.1 |
| document.stringio.replace | prepared | preg_replace_callback() [prefix] | 58211.4 | 280897.7 |
| document.stringio.replace | prepared | str_replace() | 160973.4 | 270966.9 |
| document.stringio.unique | oneshot | Matcher::getMatchedKeywords() | 148855.1 | 563971.8 |
| document.stringio.unique | oneshot | strpos() loop | 158063.6† | 267600.9† |
| document.stringio.unique | oneshot | preg_match_all() [literal] | 225805.2 | 998741.3 |
| document.stringio.unique | oneshot | preg_match_all() [prefix] | 257330.1† | 1005983.8† |
| document.stringio.unique | prepared | Matcher::getMatchedKeywords() | 30925.2† | 81618.8† |
| document.stringio.unique | prepared | strpos() loop | 157955.5 | 267601.6 |
| document.stringio.unique | prepared | preg_match_all() [literal] | 225137.7 | 998742.5 |
| document.stringio.unique | prepared | preg_match_all() [prefix] | 255745.9† | 1005985.0† |
| document.thread.all | oneshot | Matcher::matchAll() | 189178.4 | 624727.7 |
| document.thread.all | oneshot | strpos() loop | 306147.8 | 633641.7 |
| document.thread.all | oneshot | preg_match_all() [literal] | 470827.9 | 1603444.6 |
| document.thread.all | oneshot | preg_match_all() [prefix] | 506067.8† | 1610300.8† |
| document.thread.all | prepared | Matcher::matchAll() | 73786.8 | 142426.4 |
| document.thread.all | prepared | strpos() loop | 306041.2† | 633642.1† |
| document.thread.all | prepared | preg_match_all() [literal] | 470778.6 | 1603440.9 |
| document.thread.all | prepared | preg_match_all() [prefix] | 507100.1 | 1610297.8 |
| document.thread.count | oneshot | Matcher::countMatches() | 179236.3 | 588451.8 |
| document.thread.count | oneshot | strpos() loop | 263232.0 | 446463.1 |
| document.thread.count | oneshot | preg_match_all() [literal] | 406932.1 | 1347235.7 |
| document.thread.count | oneshot | preg_match_all() [prefix] | 442003.7† | 1354092.2† |
| document.thread.count | prepared | Matcher::countMatches() | 46763.2 | 106100.8 |
| document.thread.count | prepared | strpos() loop | 263121.1 | 446464.2 |
| document.thread.count | prepared | preg_match_all() [literal] | 407536.0 | 1347233.2 |
| document.thread.count | prepared | preg_match_all() [prefix] | 449566.1† | 1354091.7† |
| document.thread.replace | oneshot | Replacer::replace() | 120596.3 | 422551.5 |
| document.thread.replace | oneshot | strtr() | 807090.4 | 2608087.4 |
| document.thread.replace | oneshot | preg_replace_callback() [literal] | 208123.1 | 813837.1 |
| document.thread.replace | oneshot | preg_replace_callback() [prefix] | 98526.7† | 440195.6† |
| document.thread.replace | prepared | Replacer::replace() | 52296.7 | 119845.5 |
| document.thread.replace | prepared | strtr() | 810218.6 | 2608120.3 |
| document.thread.replace | prepared | preg_replace_callback() [literal] | 208162.3 | 813836.6 |
| document.thread.replace | prepared | preg_replace_callback() [prefix] | 99882.5 | 440196.1 |
| document.thread.unique | oneshot | Matcher::getMatchedKeywords() | 180235.1 | 610101.3 |
| document.thread.unique | oneshot | strpos() loop | 243984.8† | 396957.1† |
| document.thread.unique | oneshot | preg_match_all() [literal] | 450615.9 | 1503929.0 |
| document.thread.unique | oneshot | preg_match_all() [prefix] | 481808.3† | 1510785.2† |
| document.thread.unique | prepared | Matcher::getMatchedKeywords() | 57154.2† | 127749.4† |
| document.thread.unique | prepared | strpos() loop | 243751.7 | 396952.4 |
| document.thread.unique | prepared | preg_match_all() [literal] | 448836.5 | 1503933.5 |
| document.thread.unique | prepared | preg_match_all() [prefix] | 479884.7 | 1510780.7 |
| document.urlparse.all | oneshot | Matcher::matchAll() | 295375.3† | 745065.0† |
| document.urlparse.all | oneshot | strpos() loop | 635014.8 | 1043590.9 |
| document.urlparse.all | oneshot | preg_match_all() [literal] | 1026229.6 | 3097917.1 |
| document.urlparse.all | oneshot | preg_match_all() [prefix] | 1036411.9 | 3095098.1 |
| document.urlparse.all | prepared | Matcher::matchAll() | 175550.0 | 262646.3 |
| document.urlparse.all | prepared | strpos() loop | 635012.6 | 1043592.3 |
| document.urlparse.all | prepared | preg_match_all() [literal] | 1032480.6 | 3097924.4 |
| document.urlparse.all | prepared | preg_match_all() [prefix] | 1041921.9† | 3095093.7† |
| document.urlparse.count | oneshot | Matcher::countMatches() | 272673.0 | 725553.9 |
| document.urlparse.count | oneshot | strpos() loop | 608787.4 | 940306.8 |
| document.urlparse.count | oneshot | preg_match_all() [literal] | 990898.5† | 2979172.5† |
| document.urlparse.count | oneshot | preg_match_all() [prefix] | 1002816.4 | 2976340.9 |
| document.urlparse.count | prepared | Matcher::countMatches() | 129161.3 | 243182.4 |
| document.urlparse.count | prepared | strpos() loop | 608322.7 | 940293.8 |
| document.urlparse.count | prepared | preg_match_all() [literal] | 993673.3 | 2979172.0 |
| document.urlparse.count | prepared | preg_match_all() [prefix] | 1004875.9 | 2976329.3 |
| document.urlparse.replace | oneshot | Replacer::replace() | 203432.5 | 569353.2 |
| document.urlparse.replace | oneshot | strtr() | 1820069.4 | 5756161.2 |
| document.urlparse.replace | oneshot | preg_replace_callback() [literal] | 438074.1 | 1689122.7 |
| document.urlparse.replace | oneshot | preg_replace_callback() [prefix] | 234505.1† | 878871.2† |
| document.urlparse.replace | oneshot | str_replace() | 632316.0 | 968186.0 |
| document.urlparse.replace | prepared | Replacer::replace() | 136977.5 | 266924.1 |
| document.urlparse.replace | prepared | strtr() | 1816267.4 | 5756174.0 |
| document.urlparse.replace | prepared | preg_replace_callback() [literal] | 437338.9 | 1689127.4 |
| document.urlparse.replace | prepared | preg_replace_callback() [prefix] | 233681.4 | 878871.3 |
| document.urlparse.replace | prepared | str_replace() | 633123.7 | 968178.4 |
| document.urlparse.unique | oneshot | Matcher::getMatchedKeywords() | 289217.2 | 777805.2 |
| document.urlparse.unique | oneshot | strpos() loop | 594741.5 | 905534.0 |
| document.urlparse.unique | oneshot | preg_match_all() [literal] | 1019136.3 | 3074531.5 |
| document.urlparse.unique | oneshot | preg_match_all() [prefix] | 1034064.3 | 3071706.1 |
| document.urlparse.unique | prepared | Matcher::getMatchedKeywords() | 159052.8 | 295435.4 |
| document.urlparse.unique | prepared | strpos() loop | 595335.8 | 905547.6 |
| document.urlparse.unique | prepared | preg_match_all() [literal] | 1019542.9 | 3074539.5 |
| document.urlparse.unique | prepared | preg_match_all() [prefix] | 1032056.7 | 3071713.9 |
| document.xmlrpclib.all | oneshot | Matcher::matchAll() | 377207.5 | 854519.8 |
| document.xmlrpclib.all | oneshot | strpos() loop | 980565.1† | 1555751.6† |
| document.xmlrpclib.all | oneshot | preg_match_all() [literal] | 1590548.5 | 4439422.8 |
| document.xmlrpclib.all | oneshot | preg_match_all() [prefix] | 1614288.2† | 4440821.0† |
| document.xmlrpclib.all | prepared | Matcher::matchAll() | 254846.6 | 371962.0 |
| document.xmlrpclib.all | prepared | strpos() loop | 982264.0 | 1555749.6 |
| document.xmlrpclib.all | prepared | preg_match_all() [literal] | 1584459.0 | 4439431.8 |
| document.xmlrpclib.all | prepared | preg_match_all() [prefix] | 1617738.9 | 4440838.0 |
| document.xmlrpclib.count | oneshot | Matcher::countMatches() | 374967.0† | 821838.1† |
| document.xmlrpclib.count | oneshot | strpos() loop | 927073.2 | 1336197.5 |
| document.xmlrpclib.count | oneshot | preg_match_all() [literal] | 1504747.6 | 4158796.2 |
| document.xmlrpclib.count | oneshot | preg_match_all() [prefix] | 1545103.7 | 4160161.4 |
| document.xmlrpclib.count | prepared | Matcher::countMatches() | 227775.6 | 339223.0 |
| document.xmlrpclib.count | prepared | strpos() loop | 926633.4 | 1336196.5 |
| document.xmlrpclib.count | prepared | preg_match_all() [literal] | 1501257.3 | 4158791.4 |
| document.xmlrpclib.count | prepared | preg_match_all() [prefix] | 1547013.5 | 4160218.3 |
| document.xmlrpclib.replace | oneshot | Replacer::replace() | 284376.0 | 675193.7 |
| document.xmlrpclib.replace | oneshot | strtr() | 2821652.0 | 8622068.6 |
| document.xmlrpclib.replace | oneshot | preg_replace_callback() [literal] | 666170.2† | 2507184.9† |
| document.xmlrpclib.replace | oneshot | preg_replace_callback() [prefix] | 415616.8 | 1294511.4 |
| document.xmlrpclib.replace | oneshot | str_replace() | 1029471.5 | 1459830.3 |
| document.xmlrpclib.replace | prepared | Replacer::replace() | 212081.3 | 372498.9 |
| document.xmlrpclib.replace | prepared | strtr() | 2822307.7 | 8622068.7 |
| document.xmlrpclib.replace | prepared | preg_replace_callback() [literal] | 669826.8 | 2507182.8 |
| document.xmlrpclib.replace | prepared | preg_replace_callback() [prefix] | 412992.0 | 1294517.0 |
| document.xmlrpclib.replace | prepared | str_replace() | 1030849.0 | 1459840.6 |
| document.xmlrpclib.unique | oneshot | Matcher::getMatchedKeywords() | 369788.4† | 891544.4† |
| document.xmlrpclib.unique | oneshot | strpos() loop | 853338.2 | 1228653.1 |
| document.xmlrpclib.unique | oneshot | preg_match_all() [literal] | 1557424.7 | 4309616.6 |
| document.xmlrpclib.unique | oneshot | preg_match_all() [prefix] | 1591584.3 | 4311009.8 |
| document.xmlrpclib.unique | prepared | Matcher::getMatchedKeywords() | 241579.4† | 408935.8† |
| document.xmlrpclib.unique | prepared | strpos() loop | 852694.0 | 1228650.9 |
| document.xmlrpclib.unique | prepared | preg_match_all() [literal] | 1553889.6† | 4309619.6† |
| document.xmlrpclib.unique | prepared | preg_match_all() [prefix] | 1587732.8 | 4311025.6 |
| email.account-deletion.html | oneshot | Replacer::replace() | 87295.6† | 224145.6† |
| email.account-deletion.html | oneshot | strtr() | 43772.9 | 265379.0 |
| email.account-deletion.html | oneshot | preg_replace_callback() [literal] | 5747.1 | 26003.0 |
| email.account-deletion.html | oneshot | preg_replace_callback() [prefix] | 5746.2 | 26021.0 |
| email.account-deletion.html | oneshot | str_replace() | 54727.9† | 82328.8† |
| email.account-deletion.html | oneshot | preg_replace_callback() [tokens] | 6489.4 | 26749.0 |
| email.account-deletion.txt | oneshot | Replacer::replace() | 7551.3 | 28748.0 |
| email.account-deletion.txt | oneshot | strtr() | 2094.1† | 10551.0† |
| email.account-deletion.txt | oneshot | preg_replace_callback() [literal] | 2481.7† | 10262.0† |
| email.account-deletion.txt | oneshot | preg_replace_callback() [prefix] | 2483.3 | 10275.0 |
| email.account-deletion.txt | oneshot | str_replace() | 1416.3 | 5519.0 |
| email.account-deletion.txt | oneshot | preg_replace_callback() [tokens] | 2608.8 | 10773.0 |
| email.email-verification.html | oneshot | Replacer::replace() | 86007.7 | 218237.3 |
| email.email-verification.html | oneshot | strtr() | 44121.5 | 260570.1 |
| email.email-verification.html | oneshot | preg_replace_callback() [literal] | 5703.4† | 26253.1† |
| email.email-verification.html | oneshot | preg_replace_callback() [prefix] | 5525.7 | 26273.0 |
| email.email-verification.html | oneshot | str_replace() | 58902.3 | 87055.2 |
| email.email-verification.html | oneshot | preg_replace_callback() [tokens] | 5928.6 | 24625.1 |
| email.email-verification.txt | oneshot | Replacer::replace() | 6749.0† | 26192.0† |
| email.email-verification.txt | oneshot | strtr() | 1692.3 | 8062.0 |
| email.email-verification.txt | oneshot | preg_replace_callback() [literal] | 2099.0 | 8441.0 |
| email.email-verification.txt | oneshot | preg_replace_callback() [prefix] | 2104.5† | 8455.0† |
| email.email-verification.txt | oneshot | str_replace() | 1369.4 | 5113.0 |
| email.email-verification.txt | oneshot | preg_replace_callback() [tokens] | 2190.8 | 8704.0 |
| email.magic-link.html | oneshot | Replacer::replace() | 82250.4 | 207859.5 |
| email.magic-link.html | oneshot | strtr() | 42151.0 | 253967.3 |
| email.magic-link.html | oneshot | preg_replace_callback() [literal] | 5595.8 | 24925.0 |
| email.magic-link.html | oneshot | preg_replace_callback() [prefix] | 5649.6 | 24952.0 |
| email.magic-link.html | oneshot | str_replace() | 56694.1† | 81201.1† |
| email.magic-link.html | oneshot | preg_replace_callback() [tokens] | 6380.1† | 26628.0† |
| email.magic-link.txt | oneshot | Replacer::replace() | 5706.2† | 21399.1† |
| email.magic-link.txt | oneshot | strtr() | 1552.6 | 7305.0 |
| email.magic-link.txt | oneshot | preg_replace_callback() [literal] | 1726.0 | 6732.0 |
| email.magic-link.txt | oneshot | preg_replace_callback() [prefix] | 1732.4 | 6741.0 |
| email.magic-link.txt | oneshot | str_replace() | 1113.1 | 3965.0 |
| email.magic-link.txt | oneshot | preg_replace_callback() [tokens] | 1803.1 | 6973.0 |
| email.new-sign-in.html | oneshot | Replacer::replace() | 132181.2 | 332216.7 |
| email.new-sign-in.html | oneshot | strtr() | 65348.5† | 392258.1† |
| email.new-sign-in.html | oneshot | preg_replace_callback() [literal] | 60080.1 | 57494.3 |
| email.new-sign-in.html | oneshot | preg_replace_callback() [prefix] | 60156.3 | 57488.2 |
| email.new-sign-in.html | oneshot | str_replace() | 219353.0 | 303128.0 |
| email.new-sign-in.html | oneshot | preg_replace_callback() [tokens] | 9178.4 | 37256.0 |
| email.new-sign-in.txt | oneshot | Replacer::replace() | 10740.4 | 42806.1 |
| email.new-sign-in.txt | oneshot | strtr() | 2493.3 | 12988.0 |
| email.new-sign-in.txt | oneshot | preg_replace_callback() [literal] | 4239.8 | 14411.0 |
| email.new-sign-in.txt | oneshot | preg_replace_callback() [prefix] | 4239.3† | 14423.0† |
| email.new-sign-in.txt | oneshot | str_replace() | 2556.1 | 9798.0 |
| email.new-sign-in.txt | oneshot | preg_replace_callback() [tokens] | 3348.3 | 14286.0 |
| email.one-time-code.html | oneshot | Replacer::replace() | 69229.0† | 181099.1† |
| email.one-time-code.html | oneshot | strtr() | 36873.9 | 222583.2 |
| email.one-time-code.html | oneshot | preg_replace_callback() [literal] | 5500.3 | 25525.1 |
| email.one-time-code.html | oneshot | preg_replace_callback() [prefix] | 5543.3† | 25552.0† |
| email.one-time-code.html | oneshot | str_replace() | 28145.6† | 44621.0† |
| email.one-time-code.html | oneshot | preg_replace_callback() [tokens] | 6113.7† | 24855.0† |
| email.one-time-code.txt | oneshot | Replacer::replace() | 5838.5† | 20800.1† |
| email.one-time-code.txt | oneshot | strtr() | 1887.8† | 8757.0† |
| email.one-time-code.txt | oneshot | preg_replace_callback() [literal] | 1758.0† | 6815.0† |
| email.one-time-code.txt | oneshot | preg_replace_callback() [prefix] | 1742.6† | 6824.0† |
| email.one-time-code.txt | oneshot | str_replace() | 1102.5† | 4060.0† |
| email.one-time-code.txt | oneshot | preg_replace_callback() [tokens] | 1830.7† | 6916.0† |
| email.password-reset.html | oneshot | Replacer::replace() | 91923.7† | 221791.3† |
| email.password-reset.html | oneshot | strtr() | 45621.4† | 267135.5† |
| email.password-reset.html | oneshot | preg_replace_callback() [literal] | 6969.7† | 30294.9† |
| email.password-reset.html | oneshot | preg_replace_callback() [prefix] | 6958.8† | 30406.0† |
| email.password-reset.html | oneshot | str_replace() | 62164.6† | 91928.0† |
| email.password-reset.html | oneshot | preg_replace_callback() [tokens] | 7523.1† | 28867.0† |
| email.password-reset.txt | oneshot | Replacer::replace() | 6769.9† | 25434.1† |
| email.password-reset.txt | oneshot | strtr() | 1829.8† | 8979.0† |
| email.password-reset.txt | oneshot | preg_replace_callback() [literal] | 2136.1 | 8619.0 |
| email.password-reset.txt | oneshot | preg_replace_callback() [prefix] | 2131.0† | 8636.0† |
| email.password-reset.txt | oneshot | str_replace() | 1335.7 | 5058.0 |
| email.password-reset.txt | oneshot | preg_replace_callback() [tokens] | 2201.9 | 8836.0 |
| email.payment-failed.html | oneshot | Replacer::replace() | 117878.2† | 292847.8† |
| email.payment-failed.html | oneshot | strtr() | 58696.9 | 354158.9 |
| email.payment-failed.html | oneshot | preg_replace_callback() [literal] | 71811.5 | 68533.4 |
| email.payment-failed.html | oneshot | preg_replace_callback() [prefix] | 71824.5 | 68445.3 |
| email.payment-failed.html | oneshot | str_replace() | 192803.5† | 271131.6† |
| email.payment-failed.html | oneshot | preg_replace_callback() [tokens] | 9387.1 | 39826.1 |
| email.payment-failed.txt | oneshot | Replacer::replace() | 10215.9 | 40355.1 |
| email.payment-failed.txt | oneshot | strtr() | 2510.9 | 13210.0 |
| email.payment-failed.txt | oneshot | preg_replace_callback() [literal] | 4668.5 | 17335.0 |
| email.payment-failed.txt | oneshot | preg_replace_callback() [prefix] | 4697.5† | 17356.1† |
| email.payment-failed.txt | oneshot | str_replace() | 2876.9 | 10709.0 |
| email.payment-failed.txt | oneshot | preg_replace_callback() [tokens] | 4001.3 | 17591.0 |
| email.receipt.html | oneshot | Replacer::replace() | 153709.5 | 413615.8 |
| email.receipt.html | oneshot | strtr() | 80933.4 | 489123.0 |
| email.receipt.html | oneshot | preg_replace_callback() [literal] | 11809.5 | 51104.9 |
| email.receipt.html | oneshot | preg_replace_callback() [prefix] | 11421.6† | 47732.1† |
| email.receipt.html | oneshot | str_replace() | 407244.8 | 555230.0 |
| email.receipt.html | oneshot | preg_replace_callback() [tokens] | 11772.7 | 49496.7 |
| email.receipt.txt | oneshot | Replacer::replace() | 14947.9† | 61135.0† |
| email.receipt.txt | oneshot | strtr() | 3092.5 | 16483.0 |
| email.receipt.txt | oneshot | preg_replace_callback() [literal] | 4880.7† | 21808.9† |
| email.receipt.txt | oneshot | preg_replace_callback() [prefix] | 4836.0 | 21770.0 |
| email.receipt.txt | oneshot | str_replace() | 5227.2 | 18518.0 |
| email.receipt.txt | oneshot | preg_replace_callback() [tokens] | 5179.6† | 23019.0† |
| email.subscription-renewal.html | oneshot | Replacer::replace() | 122423.0 | 315885.9 |
| email.subscription-renewal.html | oneshot | strtr() | 64147.4 | 386992.6 |
| email.subscription-renewal.html | oneshot | preg_replace_callback() [literal] | 56598.1 | 62763.3 |
| email.subscription-renewal.html | oneshot | preg_replace_callback() [prefix] | 56913.0 | 62774.8 |
| email.subscription-renewal.html | oneshot | str_replace() | 203449.5† | 285519.4† |
| email.subscription-renewal.html | oneshot | preg_replace_callback() [tokens] | 11047.0 | 46446.1 |
| email.subscription-renewal.txt | oneshot | Replacer::replace() | 10535.4 | 42386.9 |
| email.subscription-renewal.txt | oneshot | strtr() | 2659.8 | 13840.0 |
| email.subscription-renewal.txt | oneshot | preg_replace_callback() [literal] | 4536.6 | 18603.0 |
| email.subscription-renewal.txt | oneshot | preg_replace_callback() [prefix] | 4526.4 | 18629.0 |
| email.subscription-renewal.txt | oneshot | str_replace() | 2914.7 | 10828.0 |
| email.subscription-renewal.txt | oneshot | preg_replace_callback() [tokens] | 4408.9† | 19447.0† |
| email.team-invite.html | oneshot | Replacer::replace() | 91468.2 | 231976.0 |
| email.team-invite.html | oneshot | strtr() | 45804.6 | 271364.1 |
| email.team-invite.html | oneshot | preg_replace_callback() [literal] | 33272.2† | 42083.9† |
| email.team-invite.html | oneshot | preg_replace_callback() [prefix] | 33169.3 | 42116.0 |
| email.team-invite.html | oneshot | str_replace() | 114088.5 | 164887.8 |
| email.team-invite.html | oneshot | preg_replace_callback() [tokens] | 8605.9† | 37249.0† |
| email.team-invite.txt | oneshot | Replacer::replace() | 8359.4 | 33663.1 |
| email.team-invite.txt | oneshot | strtr() | 1939.3 | 9467.0 |
| email.team-invite.txt | oneshot | preg_replace_callback() [literal] | 3273.0 | 13449.0 |
| email.team-invite.txt | oneshot | preg_replace_callback() [prefix] | 3260.1† | 13466.0† |
| email.team-invite.txt | oneshot | str_replace() | 2200.5 | 8174.0 |
| email.team-invite.txt | oneshot | preg_replace_callback() [tokens] | 3287.3 | 14045.0 |
| email.usage-alert.html | oneshot | Replacer::replace() | 121944.4 | 307591.5 |
| email.usage-alert.html | oneshot | strtr() | 60827.8 | 364978.8 |
| email.usage-alert.html | oneshot | preg_replace_callback() [literal] | 75869.5 | 77443.4 |
| email.usage-alert.html | oneshot | preg_replace_callback() [prefix] | 75524.3† | 77350.2† |
| email.usage-alert.html | oneshot | str_replace() | 213726.3 | 304204.8 |
| email.usage-alert.html | oneshot | preg_replace_callback() [tokens] | 11304.9 | 47676.9 |
| email.usage-alert.txt | oneshot | Replacer::replace() | 10994.4 | 44152.1 |
| email.usage-alert.txt | oneshot | strtr() | 2458.5 | 12683.0 |
| email.usage-alert.txt | oneshot | preg_replace_callback() [literal] | 4362.5 | 15724.9 |
| email.usage-alert.txt | oneshot | preg_replace_callback() [prefix] | 4347.7 | 15748.0 |
| email.usage-alert.txt | oneshot | str_replace() | 3042.9† | 11158.0† |
| email.usage-alert.txt | oneshot | preg_replace_callback() [tokens] | 3663.5 | 15747.0 |
| email.welcome.html | oneshot | Replacer::replace() | 100297.9 | 234571.3 |
| email.welcome.html | oneshot | strtr() | 48138.4 | 287016.1 |
| email.welcome.html | oneshot | preg_replace_callback() [literal] | 4804.9† | 21710.0† |
| email.welcome.html | oneshot | preg_replace_callback() [prefix] | 4801.5 | 21722.0 |
| email.welcome.html | oneshot | str_replace() | 61894.7 | 90338.7 |
| email.welcome.html | oneshot | preg_replace_callback() [tokens] | 5449.8 | 21474.1 |
| email.welcome.txt | oneshot | Replacer::replace() | 7604.4† | 27435.9† |
| email.welcome.txt | oneshot | strtr() | 2432.5 | 12024.0 |
| email.welcome.txt | oneshot | preg_replace_callback() [literal] | 2183.0† | 8784.0† |
| email.welcome.txt | oneshot | preg_replace_callback() [prefix] | 2170.9 | 8796.0 |
| email.welcome.txt | oneshot | str_replace() | 1361.9 | 5389.0 |
| email.welcome.txt | oneshot | preg_replace_callback() [tokens] | 2242.2 | 9017.0 |
