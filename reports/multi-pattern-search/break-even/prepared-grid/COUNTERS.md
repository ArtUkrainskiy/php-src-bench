# Cycles and instructions

Five alternating 0/N pairs per implementation. † means at least one pair failed quality checks.

| Input | Implementation | Cycles/job | Instructions/job |
|---|---|---:|---:|
| comments.all.n8.b128.single | Matcher::matchAll() prepared | 1666.1 | 5322.0 |
| comments.all.n8.b128.single | strpos() loop | 2311.7 | 8680.0 |
| comments.all.n8.b128.single | preg_match_all() [literal] | 5463.6 | 20289.0 |
| comments.all.n8.b128.single | preg_match_all() [prefix] | 5359.9† | 20437.2† |
| comments.any.n16.b128.absent | Matcher::matches() prepared | 1353.9 | 4623.0 |
| comments.any.n16.b128.absent | strpos() loop | 2739.0 | 10682.0 |
| comments.any.n16.b128.absent | preg_match() [literal] | 1900.9 | 8014.0 |
| comments.any.n16.b128.absent | preg_match() [prefix] | 1689.1 | 7031.0 |
| comments.any.n16.b128.absent | str_contains() loop | 2127.9 | 8180.0 |
| comments.count.n8.b128.single | Matcher::countMatches() prepared | 1408.8† | 4630.0† |
| comments.count.n8.b128.single | strpos() loop | 1803.8† | 6712.0† |
| comments.count.n8.b128.single | preg_match_all() [literal] | 3248.9 | 11768.0 |
| comments.count.n8.b128.single | preg_match_all() [prefix] | 3177.2 | 11915.9 |
| comments.count.n8.b128.single | substr_count()/strpos() loop | 1459.1† | 5966.0† |
| comments.replace.n16.b128.single | Replacer::replace() prepared | 1527.4† | 5228.0† |
| comments.replace.n16.b128.single | strtr() | 3999.9 | 20818.1 |
| comments.replace.n16.b128.single | preg_replace_callback() [literal] | 2276.4 | 9094.0 |
| comments.replace.n16.b128.single | preg_replace_callback() [prefix] | 2017.8† | 8192.0† |
| comments.replace.n16.b128.single | str_replace() | 2012.8 | 7979.0 |
| comments.unique.n8.b128.single | Matcher::getMatchedKeywords() prepared | 1459.0† | 5572.0† |
| comments.unique.n8.b128.single | strpos() loop | 2295.4 | 8672.0 |
| comments.unique.n8.b128.single | preg_match_all() [literal] | 5795.0† | 21592.1† |
| comments.unique.n8.b128.single | preg_match_all() [prefix] | 5713.4 | 21740.0 |
| technical.all.n16.b1024.single | Matcher::matchAll() prepared | 9519.9 | 18723.0 |
| technical.all.n16.b1024.single | strpos() loop | 15712.3 | 33668.8 |
| technical.all.n16.b1024.single | preg_match_all() [literal] | 16666.8† | 72907.1† |
| technical.all.n16.b1024.single | preg_match_all() [prefix] | 14742.7 | 67966.8 |
| technical.all.n16.b128.single | Matcher::matchAll() prepared | 1680.0 | 5223.0 |
| technical.all.n16.b128.single | strpos() loop | 3268.9 | 12814.0 |
| technical.all.n16.b128.single | preg_match_all() [literal] | 7760.1 | 30083.9 |
| technical.all.n16.b128.single | preg_match_all() [prefix] | 7631.5 | 30169.9 |
| technical.all.n16.b256.single | Matcher::matchAll() prepared | 2436.8 | 7203.0 |
| technical.all.n16.b256.single | strpos() loop | 3979.1 | 15392.1 |
| technical.all.n16.b256.single | preg_match_all() [literal] | 9302.0 | 36967.9 |
| technical.all.n16.b256.single | preg_match_all() [prefix] | 8867.9 | 36271.0 |
| technical.all.n16.b4096.single | Matcher::matchAll() prepared | 49042.8 | 64083.8 |
| technical.all.n16.b4096.single | strpos() loop | 53427.2 | 90040.1 |
| technical.all.n16.b4096.single | preg_match_all() [literal] | 44896.1† | 214871.9† |
| technical.all.n16.b4096.single | preg_match_all() [prefix] | 41410.9 | 212687.3 |
| technical.all.n32.b1024.single | Matcher::matchAll() prepared | 9036.2 | 19272.0 |
| technical.all.n32.b1024.single | strpos() loop | 29485.8 | 63062.9 |
| technical.all.n32.b1024.single | preg_match_all() [literal] | 36008.5 | 162754.7 |
| technical.all.n32.b1024.single | preg_match_all() [prefix] | 31571.9† | 158446.3† |
| technical.all.n32.b128.single | Matcher::matchAll() prepared | 1662.7 | 5286.0 |
| technical.all.n32.b128.single | strpos() loop | 5024.6 | 20303.0 |
| technical.all.n32.b128.single | preg_match_all() [literal] | 10605.7 | 42044.0 |
| technical.all.n32.b128.single | preg_match_all() [prefix] | 10238.6 | 42228.1 |
| technical.all.n32.b256.single | Matcher::matchAll() prepared | 2406.7† | 7320.0† |
| technical.all.n32.b256.single | strpos() loop | 6369.4 | 25370.2 |
| technical.all.n32.b256.single | preg_match_all() [literal] | 14472.9 | 59825.1 |
| technical.all.n32.b256.single | preg_match_all() [prefix] | 13623.5† | 59310.1† |
| technical.all.n32.b4096.single | Matcher::matchAll() prepared | 42784.3 | 65730.0 |
| technical.all.n32.b4096.single | strpos() loop | 104470.7 | 184180.1 |
| technical.all.n32.b4096.single | preg_match_all() [literal] | 159021.8 | 556318.0 |
| technical.all.n32.b4096.single | preg_match_all() [prefix] | 119236.8 | 556729.1 |
| technical.all.n48.b1024.single | Matcher::matchAll() prepared | 8450.4 | 19446.1 |
| technical.all.n48.b1024.single | strpos() loop | 44365.2 | 91382.5 |
| technical.all.n48.b1024.single | preg_match_all() [literal] | 46068.3 | 229239.3 |
| technical.all.n48.b1024.single | preg_match_all() [prefix] | 46477.8† | 229371.1† |
| technical.all.n48.b128.single | Matcher::matchAll() prepared | 1643.3† | 5304.0† |
| technical.all.n48.b128.single | strpos() loop | 6734.7 | 27206.0 |
| technical.all.n48.b128.single | preg_match_all() [literal] | 14040.9 | 56412.4 |
| technical.all.n48.b128.single | preg_match_all() [prefix] | 14190.9 | 56718.2 |
| technical.all.n48.b256.single | Matcher::matchAll() prepared | 2416.9† | 7346.9† |
| technical.all.n48.b256.single | strpos() loop | 8299.2 | 33632.2 |
| technical.all.n48.b256.single | preg_match_all() [literal] | 18919.8 | 81334.4 |
| technical.all.n48.b256.single | preg_match_all() [prefix] | 19294.6 | 81671.7 |
| technical.all.n48.b4096.single | Matcher::matchAll() prepared | 42044.1 | 66191.9 |
| technical.all.n48.b4096.single | strpos() loop | 159457.9 | 270498.5 |
| technical.all.n48.b4096.single | preg_match_all() [literal] | 180788.3† | 791636.4† |
| technical.all.n48.b4096.single | preg_match_all() [prefix] | 215880.4 | 791078.0 |
| technical.all.n8.b1024.single | Matcher::matchAll() prepared | 10580.8 | 18255.0 |
| technical.all.n8.b1024.single | strpos() loop | 7837.4 | 18166.9 |
| technical.all.n8.b1024.single | preg_match_all() [literal] | 10715.8† | 41758.0† |
| technical.all.n8.b1024.single | preg_match_all() [prefix] | 9851.7 | 42086.0 |
| technical.all.n8.b128.single | Matcher::matchAll() prepared | 1679.2 | 5205.0 |
| technical.all.n8.b128.single | strpos() loop | 2402.1† | 9061.0† |
| technical.all.n8.b128.single | preg_match_all() [literal] | 5591.2 | 21168.0 |
| technical.all.n8.b128.single | preg_match_all() [prefix] | 5536.0 | 21356.0 |
| technical.all.n8.b256.single | Matcher::matchAll() prepared | 2445.7 | 7149.0 |
| technical.all.n8.b256.single | strpos() loop | 2515.6 | 9544.1 |
| technical.all.n8.b256.single | preg_match_all() [literal] | 6426.2 | 24136.0 |
| technical.all.n8.b256.single | preg_match_all() [prefix] | 6257.2† | 24339.0† |
| technical.all.n8.b4096.single | Matcher::matchAll() prepared | 52590.1 | 62471.9 |
| technical.all.n8.b4096.single | strpos() loop | 24056.4 | 42587.9 |
| technical.all.n8.b4096.single | preg_match_all() [literal] | 26511.5 | 107042.3 |
| technical.all.n8.b4096.single | preg_match_all() [prefix] | 22841.4 | 107740.0 |
| technical.any.n16.b1024.absent | Matcher::matches() prepared | 10262.3 | 17943.0 |
| technical.any.n16.b1024.absent | strpos() loop | 14978.3 | 31177.0 |
| technical.any.n16.b1024.absent | preg_match() [literal] | 7500.5 | 40045.0 |
| technical.any.n16.b1024.absent | preg_match() [prefix] | 6082.7 | 31425.0 |
| technical.any.n16.b1024.absent | str_contains() loop | 14347.6 | 28644.9 |
| technical.any.n16.b128.absent | Matcher::matches() prepared | 1378.5 | 4443.0 |
| technical.any.n16.b128.absent | strpos() loop | 2682.0 | 10339.0 |
| technical.any.n16.b128.absent | preg_match() [literal] | 1900.7 | 8047.0 |
| technical.any.n16.b128.absent | preg_match() [prefix] | 1736.7 | 7192.0 |
| technical.any.n16.b128.absent | str_contains() loop | 2083.3† | 7856.0† |
| technical.any.n16.b256.absent | Matcher::matches() prepared | 2013.5 | 6423.0 |
| technical.any.n16.b256.absent | strpos() loop | 3320.3 | 12718.0 |
| technical.any.n16.b256.absent | preg_match() [literal] | 2850.6 | 13324.1 |
| technical.any.n16.b256.absent | preg_match() [prefix] | 2370.4 | 10966.0 |
| technical.any.n16.b256.absent | str_contains() loop | 2738.2† | 10195.0† |
| technical.any.n16.b4096.absent | Matcher::matches() prepared | 49190.8† | 63312.1† |
| technical.any.n16.b4096.absent | strpos() loop | 52853.1 | 87622.9 |
| technical.any.n16.b4096.absent | preg_match() [literal] | 26394.2† | 146813.4† |
| technical.any.n16.b4096.absent | preg_match() [prefix] | 20742.7 | 111995.0 |
| technical.any.n16.b4096.absent | str_contains() loop | 52268.9† | 84854.4† |
| technical.any.n32.b1024.absent | Matcher::matches() prepared | 9646.5† | 18491.8† |
| technical.any.n32.b1024.absent | strpos() loop | 28905.1 | 60657.4 |
| technical.any.n32.b1024.absent | preg_match() [literal] | 14169.9 | 79632.0 |
| technical.any.n32.b1024.absent | preg_match() [prefix] | 8758.7 | 46640.1 |
| technical.any.n32.b1024.absent | str_contains() loop | 27908.9† | 56023.2† |
| technical.any.n32.b128.absent | Matcher::matches() prepared | 1416.8 | 4515.0 |
| technical.any.n32.b128.absent | strpos() loop | 4426.1 | 17838.0 |
| technical.any.n32.b128.absent | preg_match() [literal] | 2870.7 | 12632.0 |
| technical.any.n32.b128.absent | preg_match() [prefix] | 2098.4† | 8952.0† |
| technical.any.n32.b128.absent | str_contains() loop | 3445.4 | 13538.0 |
| technical.any.n32.b256.absent | Matcher::matches() prepared | 1950.8 | 6540.0 |
| technical.any.n32.b256.absent | strpos() loop | 5640.8 | 22540.0 |
| technical.any.n32.b256.absent | preg_match() [literal] | 4807.3 | 23464.0 |
| technical.any.n32.b256.absent | preg_match() [prefix] | 3157.9 | 14766.0 |
| technical.any.n32.b256.absent | str_contains() loop | 4828.6 | 18145.1 |
| technical.any.n32.b4096.absent | Matcher::matches() prepared | 42264.2 | 64958.9 |
| technical.any.n32.b4096.absent | strpos() loop | 103776.1 | 182005.0 |
| technical.any.n32.b4096.absent | preg_match() [literal] | 58241.4 | 289017.5 |
| technical.any.n32.b4096.absent | preg_match() [prefix] | 29667.5 | 165718.9 |
| technical.any.n32.b4096.absent | str_contains() loop | 102745.7 | 176230.4 |
| technical.any.n48.b1024.absent | Matcher::matches() prepared | 8294.5 | 18666.0 |
| technical.any.n48.b1024.absent | strpos() loop | 43829.0 | 88980.0 |
| technical.any.n48.b1024.absent | preg_match() [literal] | 30112.2 | 137106.1 |
| technical.any.n48.b1024.absent | preg_match() [prefix] | 13615.2† | 69089.9† |
| technical.any.n48.b1024.absent | str_contains() loop | 42226.2 | 82513.4 |
| technical.any.n48.b128.absent | Matcher::matches() prepared | 1331.6 | 4542.0 |
| technical.any.n48.b128.absent | strpos() loop | 6116.9 | 24806.0 |
| technical.any.n48.b128.absent | preg_match() [literal] | 4303.7† | 18450.0† |
| technical.any.n48.b128.absent | preg_match() [prefix] | 2735.7 | 11388.0 |
| technical.any.n48.b128.absent | str_contains() loop | 4671.8 | 18710.0 |
| technical.any.n48.b256.absent | Matcher::matches() prepared | 1964.4 | 6567.0 |
| technical.any.n48.b256.absent | strpos() loop | 7647.2 | 30767.0 |
| technical.any.n48.b256.absent | preg_match() [literal] | 7388.0 | 34464.0 |
| technical.any.n48.b256.absent | preg_match() [prefix] | 4289.5† | 19290.0† |
| technical.any.n48.b256.absent | str_contains() loop | 6428.2† | 24553.0† |
| technical.any.n48.b4096.absent | Matcher::matches() prepared | 40895.6 | 65420.0 |
| technical.any.n48.b4096.absent | strpos() loop | 158852.8 | 268308.9 |
| technical.any.n48.b4096.absent | preg_match() [literal] | 120350.6 | 491605.6 |
| technical.any.n48.b4096.absent | preg_match() [prefix] | 44955.8 | 244969.8 |
| technical.any.n48.b4096.absent | str_contains() loop | 157308.5† | 260528.8† |
| technical.any.n8.b1024.absent | Matcher::matches() prepared | 10756.0 | 17471.0 |
| technical.any.n8.b1024.absent | strpos() loop | 7242.3 | 15775.9 |
| technical.any.n8.b1024.absent | preg_match() [literal] | 4594.5 | 20065.0 |
| technical.any.n8.b1024.absent | preg_match() [prefix] | 4762.0† | 19911.0† |
| technical.any.n8.b1024.absent | str_contains() loop | 6599.0 | 14160.0 |
| technical.any.n8.b128.absent | Matcher::matches() prepared | 1367.1 | 4421.0 |
| technical.any.n8.b128.absent | strpos() loop | 1789.7 | 6617.0 |
| technical.any.n8.b128.absent | preg_match() [literal] | 1529.9 | 6098.0 |
| technical.any.n8.b128.absent | preg_match() [prefix] | 1552.6 | 6030.0 |
| technical.any.n8.b128.absent | str_contains() loop | 1360.5† | 5034.0† |
| technical.any.n8.b256.absent | Matcher::matches() prepared | 1988.8 | 6365.0 |
| technical.any.n8.b256.absent | strpos() loop | 1873.3 | 7096.0 |
| technical.any.n8.b256.absent | preg_match() [literal] | 1932.1 | 8002.0 |
| technical.any.n8.b256.absent | preg_match() [prefix] | 1945.5† | 7876.0† |
| technical.any.n8.b256.absent | str_contains() loop | 1452.0 | 5505.0 |
| technical.any.n8.b4096.absent | Matcher::matches() prepared | 51742.4 | 61697.2 |
| technical.any.n8.b4096.absent | strpos() loop | 23575.2 | 40154.2 |
| technical.any.n8.b4096.absent | preg_match() [literal] | 15166.0 | 66716.2 |
| technical.any.n8.b4096.absent | preg_match() [prefix] | 15489.0 | 65916.1 |
| technical.any.n8.b4096.absent | str_contains() loop | 23121.3 | 38429.6 |
| technical.count.n16.b1024.single | Matcher::countMatches() prepared | 6062.6† | 18035.1† |
| technical.count.n16.b1024.single | strpos() loop | 15250.7 | 31701.1 |
| technical.count.n16.b1024.single | preg_match_all() [literal] | 13296.0 | 60942.1 |
| technical.count.n16.b1024.single | preg_match_all() [prefix] | 11492.2 | 56002.4 |
| technical.count.n16.b1024.single | substr_count()/strpos() loop | 15124.7 | 31536.0 |
| technical.count.n16.b128.single | Matcher::countMatches() prepared | 1389.3 | 4535.0 |
| technical.count.n16.b128.single | strpos() loop | 2791.8 | 10846.0 |
| technical.count.n16.b128.single | preg_match_all() [literal] | 4532.9 | 18119.1 |
| technical.count.n16.b128.single | preg_match_all() [prefix] | 4497.0† | 18205.0† |
| technical.count.n16.b128.single | substr_count()/strpos() loop | 2504.7 | 10636.0 |
| technical.count.n16.b256.single | Matcher::countMatches() prepared | 3324.7† | 6515.0† |
| technical.count.n16.b256.single | strpos() loop | 5326.9† | 13424.0† |
| technical.count.n16.b256.single | preg_match_all() [literal] | 7497.6† | 25003.1† |
| technical.count.n16.b256.single | preg_match_all() [prefix] | 5666.9† | 24306.0† |
| technical.count.n16.b256.single | substr_count()/strpos() loop | 3310.8 | 13214.0 |
| technical.count.n16.b4096.single | Matcher::countMatches() prepared | 22572.6† | 63394.7† |
| technical.count.n16.b4096.single | strpos() loop | 53068.5 | 88083.2 |
| technical.count.n16.b4096.single | preg_match_all() [literal] | 41324.4 | 202907.0 |
| technical.count.n16.b4096.single | preg_match_all() [prefix] | 38168.7 | 200722.1 |
| technical.count.n16.b4096.single | substr_count()/strpos() loop | 52835.0 | 87918.6 |
| technical.count.n32.b1024.single | Matcher::countMatches() prepared | 5834.6 | 18584.0 |
| technical.count.n32.b1024.single | strpos() loop | 29079.7 | 61109.2 |
| technical.count.n32.b1024.single | preg_match_all() [literal] | 32344.9 | 149929.2 |
| technical.count.n32.b1024.single | preg_match_all() [prefix] | 27941.8 | 145620.2 |
| technical.count.n32.b1024.single | substr_count()/strpos() loop | 29369.8 | 62036.2 |
| technical.count.n32.b128.single | Matcher::countMatches() prepared | 1389.0 | 4598.0 |
| technical.count.n32.b128.single | strpos() loop | 4552.6 | 18335.0 |
| technical.count.n32.b128.single | preg_match_all() [literal] | 7307.1 | 29218.0 |
| technical.count.n32.b128.single | preg_match_all() [prefix] | 6628.0 | 29402.1 |
| technical.count.n32.b128.single | substr_count()/strpos() loop | 4364.2 | 19197.0 |
| technical.count.n32.b256.single | Matcher::countMatches() prepared | 2065.8 | 6632.0 |
| technical.count.n32.b256.single | strpos() loop | 5893.5 | 23402.0 |
| technical.count.n32.b256.single | preg_match_all() [literal] | 11045.5 | 46999.0 |
| technical.count.n32.b256.single | preg_match_all() [prefix] | 9891.9 | 46484.0 |
| technical.count.n32.b256.single | substr_count()/strpos() loop | 5944.2 | 24264.0 |
| technical.count.n32.b4096.single | Matcher::countMatches() prepared | 21912.8 | 65041.5 |
| technical.count.n32.b4096.single | strpos() loop | 104062.6 | 182253.8 |
| technical.count.n32.b4096.single | preg_match_all() [literal] | 147715.1 | 543491.5 |
| technical.count.n32.b4096.single | preg_match_all() [prefix] | 120036.8 | 543907.1 |
| technical.count.n32.b4096.single | substr_count()/strpos() loop | 104224.0 | 183178.9 |
| technical.count.n48.b1024.single | Matcher::countMatches() prepared | 5918.4 | 18766.0 |
| technical.count.n48.b1024.single | strpos() loop | 44141.7 | 89421.5 |
| technical.count.n48.b1024.single | preg_match_all() [literal] | 41605.4 | 212968.9 |
| technical.count.n48.b1024.single | preg_match_all() [prefix] | 42056.9 | 213101.2 |
| technical.count.n48.b1024.single | substr_count()/strpos() loop | 44417.7 | 91454.2 |
| technical.count.n48.b128.single | Matcher::countMatches() prepared | 1399.0† | 4616.0† |
| technical.count.n48.b128.single | strpos() loop | 6223.1 | 25238.0 |
| technical.count.n48.b128.single | preg_match_all() [literal] | 9419.9 | 40142.3 |
| technical.count.n48.b128.single | preg_match_all() [prefix] | 9742.7 | 40448.1 |
| technical.count.n48.b128.single | substr_count()/strpos() loop | 6042.8 | 27155.9 |
| technical.count.n48.b256.single | Matcher::countMatches() prepared | 2060.4 | 6659.0 |
| technical.count.n48.b256.single | strpos() loop | 7912.7† | 31663.0† |
| technical.count.n48.b256.single | preg_match_all() [literal] | 14160.4 | 65064.7 |
| technical.count.n48.b256.single | preg_match_all() [prefix] | 14716.9 | 65401.0 |
| technical.count.n48.b256.single | substr_count()/strpos() loop | 8044.2 | 33581.1 |
| technical.count.n48.b4096.single | Matcher::countMatches() prepared | 21057.6 | 65529.1 |
| technical.count.n48.b4096.single | strpos() loop | 159113.0† | 268577.2† |
| technical.count.n48.b4096.single | preg_match_all() [literal] | 173215.4 | 775369.7 |
| technical.count.n48.b4096.single | preg_match_all() [prefix] | 208501.1 | 774809.3 |
| technical.count.n48.b4096.single | substr_count()/strpos() loop | 159450.4 | 270608.7 |
| technical.count.n8.b1024.single | Matcher::countMatches() prepared | 6061.6† | 17563.0† |
| technical.count.n8.b1024.single | strpos() loop | 7353.3 | 16199.0 |
| technical.count.n8.b1024.single | preg_match_all() [literal] | 8514.7 | 33237.0 |
| technical.count.n8.b1024.single | preg_match_all() [prefix] | 7598.3 | 33565.1 |
| technical.count.n8.b1024.single | substr_count()/strpos() loop | 6935.6 | 15468.1 |
| technical.count.n8.b128.single | Matcher::countMatches() prepared | 1442.7 | 4513.0 |
| technical.count.n8.b128.single | strpos() loop | 1886.9 | 7093.0 |
| technical.count.n8.b128.single | preg_match_all() [literal] | 3429.0 | 12647.0 |
| technical.count.n8.b128.single | preg_match_all() [prefix] | 3358.1 | 12835.0 |
| technical.count.n8.b128.single | substr_count()/strpos() loop | 1561.9 | 6347.0 |
| technical.count.n8.b256.single | Matcher::countMatches() prepared | 2058.4 | 6457.0 |
| technical.count.n8.b256.single | strpos() loop | 1996.8 | 7576.0 |
| technical.count.n8.b256.single | preg_match_all() [literal] | 4203.3 | 15615.0 |
| technical.count.n8.b256.single | preg_match_all() [prefix] | 4047.4 | 15818.0 |
| technical.count.n8.b256.single | substr_count()/strpos() loop | 1648.8 | 6830.0 |
| technical.count.n8.b4096.single | Matcher::countMatches() prepared | 21540.4 | 61779.9 |
| technical.count.n8.b4096.single | strpos() loop | 23623.4 | 40620.1 |
| technical.count.n8.b4096.single | preg_match_all() [literal] | 23844.8† | 98521.2† |
| technical.count.n8.b4096.single | preg_match_all() [prefix] | 19961.6 | 99218.9 |
| technical.count.n8.b4096.single | substr_count()/strpos() loop | 23317.6† | 39888.9† |
| technical.replace.n16.b1024.single | Replacer::replace() prepared | 6228.7 | 20040.1 |
| technical.replace.n16.b1024.single | strtr() | 29458.0 | 174302.8 |
| technical.replace.n16.b1024.single | preg_replace_callback() [literal] | 8163.8 | 41113.0 |
| technical.replace.n16.b1024.single | preg_replace_callback() [prefix] | 6306.3 | 32605.1 |
| technical.replace.n16.b1024.single | str_replace() | 14001.3 | 28902.0 |
| technical.replace.n16.b128.single | Replacer::replace() prepared | 1501.7 | 5128.0 |
| technical.replace.n16.b128.single | strtr() | 3833.9 | 20035.9 |
| technical.replace.n16.b128.single | preg_replace_callback() [literal] | 2274.9† | 8985.0† |
| technical.replace.n16.b128.single | preg_replace_callback() [prefix] | 2040.0 | 8270.0 |
| technical.replace.n16.b128.single | str_replace() | 1907.0 | 7594.0 |
| technical.replace.n16.b256.single | Replacer::replace() prepared | 2319.5 | 7791.0 |
| technical.replace.n16.b256.single | strtr() | 9121.6 | 50051.2 |
| technical.replace.n16.b256.single | preg_replace_callback() [literal] | 3241.1† | 14566.0† |
| technical.replace.n16.b256.single | preg_replace_callback() [prefix] | 2671.7 | 12202.0 |
| technical.replace.n16.b256.single | str_replace() | 2634.8 | 10221.0 |
| technical.replace.n16.b4096.single | Replacer::replace() prepared | 25234.0 | 69031.1 |
| technical.replace.n16.b4096.single | strtr() | 160472.8 | 680147.4 |
| technical.replace.n16.b4096.single | preg_replace_callback() [literal] | 29293.8 | 148285.9 |
| technical.replace.n16.b4096.single | preg_replace_callback() [prefix] | 21207.6 | 113663.2 |
| technical.replace.n16.b4096.single | str_replace() | 51944.4 | 86398.6 |
| technical.replace.n32.b1024.single | Replacer::replace() prepared | 6161.4 | 20587.0 |
| technical.replace.n32.b1024.single | strtr() | 46080.6 | 258876.4 |
| technical.replace.n32.b1024.single | preg_replace_callback() [literal] | 16244.3 | 80349.0 |
| technical.replace.n32.b1024.single | preg_replace_callback() [prefix] | 9031.1 | 47683.2 |
| technical.replace.n32.b1024.single | str_replace() | 26885.1 | 55277.1 |
| technical.replace.n32.b128.single | Replacer::replace() prepared | 1521.9 | 5191.0 |
| technical.replace.n32.b128.single | strtr() | 5632.8 | 29085.0 |
| technical.replace.n32.b128.single | preg_replace_callback() [literal] | 3070.9 | 12950.0 |
| technical.replace.n32.b128.single | preg_replace_callback() [prefix] | 2355.8† | 9790.0† |
| technical.replace.n32.b128.single | str_replace() | 2907.0 | 12047.0 |
| technical.replace.n32.b256.single | Replacer::replace() prepared | 2322.5 | 7908.0 |
| technical.replace.n32.b256.single | strtr() | 12836.3 | 70375.0 |
| technical.replace.n32.b256.single | preg_replace_callback() [literal] | 5359.1† | 24609.0† |
| technical.replace.n32.b256.single | preg_replace_callback() [prefix] | 3453.2† | 15973.0† |
| technical.replace.n32.b256.single | str_replace() | 4288.9† | 17208.9† |
| technical.replace.n32.b4096.single | Replacer::replace() prepared | 24851.4 | 70678.2 |
| technical.replace.n32.b4096.single | strtr() | 277121.5 | 964358.8 |
| technical.replace.n32.b4096.single | preg_replace_callback() [literal] | 62507.3 | 290009.7 |
| technical.replace.n32.b4096.single | preg_replace_callback() [prefix] | 29263.5 | 167093.1 |
| technical.replace.n32.b4096.single | str_replace() | 102140.8 | 177593.4 |
| technical.replace.n48.b1024.single | Replacer::replace() prepared | 6176.2 | 20743.0 |
| technical.replace.n48.b1024.single | strtr() | 93174.3 | 476416.2 |
| technical.replace.n48.b1024.single | preg_replace_callback() [literal] | 29318.4 | 137527.1 |
| technical.replace.n48.b1024.single | preg_replace_callback() [prefix] | 14144.1 | 69994.1 |
| technical.replace.n48.b1024.single | str_replace() | 40255.4 | 80778.2 |
| technical.replace.n48.b128.single | Replacer::replace() prepared | 1523.5 | 5233.0 |
| technical.replace.n48.b128.single | strtr() | 8264.6 | 46799.1 |
| technical.replace.n48.b128.single | preg_replace_callback() [literal] | 4104.3 | 17947.0 |
| technical.replace.n48.b128.single | preg_replace_callback() [prefix] | 2861.4 | 11848.0 |
| technical.replace.n48.b128.single | str_replace() | 3825.9† | 16071.0† |
| technical.replace.n48.b256.single | Replacer::replace() prepared | 2346.7 | 7976.0 |
| technical.replace.n48.b256.single | strtr() | 19433.9 | 111399.0 |
| technical.replace.n48.b256.single | preg_replace_callback() [literal] | 7421.9 | 35569.1 |
| technical.replace.n48.b256.single | preg_replace_callback() [prefix] | 4528.8† | 20445.9† |
| technical.replace.n48.b256.single | str_replace() | 5611.7 | 22604.0 |
| technical.replace.n48.b4096.single | Replacer::replace() prepared | 24318.7 | 71621.6 |
| technical.replace.n48.b4096.single | strtr() | 504946.6 | 1739726.8 |
| technical.replace.n48.b4096.single | preg_replace_callback() [literal] | 121114.4† | 491778.6† |
| technical.replace.n48.b4096.single | preg_replace_callback() [prefix] | 51223.0 | 246046.4 |
| technical.replace.n48.b4096.single | str_replace() | 157299.2 | 261107.8 |
| technical.replace.n8.b1024.single | Replacer::replace() prepared | 6262.3 | 19572.0 |
| technical.replace.n8.b1024.single | strtr() | 7283.8† | 42131.9† |
| technical.replace.n8.b1024.single | preg_replace_callback() [literal] | 4806.3 | 21422.0 |
| technical.replace.n8.b1024.single | preg_replace_callback() [prefix] | 4917.0 | 21260.9 |
| technical.replace.n8.b1024.single | str_replace() | 6823.9 | 14837.0 |
| technical.replace.n8.b128.single | Replacer::replace() prepared | 1516.2 | 5110.0 |
| technical.replace.n8.b128.single | strtr() | 2071.6 | 9950.0 |
| technical.replace.n8.b128.single | preg_replace_callback() [literal] | 1807.7 | 7325.0 |
| technical.replace.n8.b128.single | preg_replace_callback() [prefix] | 1837.1 | 7278.0 |
| technical.replace.n8.b128.single | str_replace() | 1387.6 | 5308.0 |
| technical.replace.n8.b256.single | Replacer::replace() prepared | 2343.4 | 7737.0 |
| technical.replace.n8.b256.single | strtr() | 2965.6 | 14800.1 |
| technical.replace.n8.b256.single | preg_replace_callback() [literal] | 2205.0 | 9249.0 |
| technical.replace.n8.b256.single | preg_replace_callback() [prefix] | 2239.2 | 9116.0 |
| technical.replace.n8.b256.single | str_replace() | 1496.1 | 5840.0 |
| technical.replace.n8.b4096.single | Replacer::replace() prepared | 23388.4 | 67442.9 |
| technical.replace.n8.b4096.single | strtr() | 24074.1 | 141692.7 |
| technical.replace.n8.b4096.single | preg_replace_callback() [literal] | 15548.5 | 68698.8 |
| technical.replace.n8.b4096.single | preg_replace_callback() [prefix] | 15741.8 | 67786.8 |
| technical.replace.n8.b4096.single | str_replace() | 23522.0† | 40386.1† |
| technical.unique.n16.b1024.single | Matcher::getMatchedKeywords() prepared | 5770.6 | 21669.9 |
| technical.unique.n16.b1024.single | strpos() loop | 15733.7 | 33476.1 |
| technical.unique.n16.b1024.single | preg_match_all() [literal] | 17104.2 | 74142.2 |
| technical.unique.n16.b1024.single | preg_match_all() [prefix] | 15001.0 | 69202.1 |
| technical.unique.n16.b128.single | Matcher::getMatchedKeywords() prepared | 1478.5 | 5482.0 |
| technical.unique.n16.b128.single | strpos() loop | 3337.3 | 12770.0 |
| technical.unique.n16.b128.single | preg_match_all() [literal] | 8070.6 | 31319.0 |
| technical.unique.n16.b128.single | preg_match_all() [prefix] | 7886.7 | 31405.1 |
| technical.unique.n16.b256.single | Matcher::getMatchedKeywords() prepared | 2746.1† | 7846.0† |
| technical.unique.n16.b256.single | strpos() loop | 6928.7† | 15375.0† |
| technical.unique.n16.b256.single | preg_match_all() [literal] | 17502.3† | 38202.9† |
| technical.unique.n16.b256.single | preg_match_all() [prefix] | 16798.8† | 37506.0† |
| technical.unique.n16.b4096.single | Matcher::getMatchedKeywords() prepared | 40024.2 | 76245.8 |
| technical.unique.n16.b4096.single | strpos() loop | 53376.6 | 89617.2 |
| technical.unique.n16.b4096.single | preg_match_all() [literal] | 45626.8 | 216106.7 |
| technical.unique.n16.b4096.single | preg_match_all() [prefix] | 42038.1 | 213921.7 |
| technical.unique.n32.b1024.single | Matcher::getMatchedKeywords() prepared | 6821.9 | 22219.9 |
| technical.unique.n32.b1024.single | strpos() loop | 29618.7 | 62883.9 |
| technical.unique.n32.b1024.single | preg_match_all() [literal] | 36559.7 | 163973.0 |
| technical.unique.n32.b1024.single | preg_match_all() [prefix] | 32164.6 | 159664.8 |
| technical.unique.n32.b128.single | Matcher::getMatchedKeywords() prepared | 1472.8 | 5546.0 |
| technical.unique.n32.b128.single | strpos() loop | 5108.7 | 20259.0 |
| technical.unique.n32.b128.single | preg_match_all() [literal] | 10932.3 | 43262.1 |
| technical.unique.n32.b128.single | preg_match_all() [prefix] | 10674.0† | 43445.7† |
| technical.unique.n32.b256.single | Matcher::getMatchedKeywords() prepared | 2063.4 | 7964.0 |
| technical.unique.n32.b256.single | strpos() loop | 6420.2 | 25353.0 |
| technical.unique.n32.b256.single | preg_match_all() [literal] | 14789.4 | 61042.9 |
| technical.unique.n32.b256.single | preg_match_all() [prefix] | 13964.9 | 60527.9 |
| technical.unique.n32.b4096.single | Matcher::getMatchedKeywords() prepared | 38136.9 | 77894.2 |
| technical.unique.n32.b4096.single | strpos() loop | 104253.8 | 183785.7 |
| technical.unique.n32.b4096.single | preg_match_all() [literal] | 150854.1 | 557534.9 |
| technical.unique.n32.b4096.single | preg_match_all() [prefix] | 117181.2 | 557952.6 |
| technical.unique.n48.b1024.single | Matcher::getMatchedKeywords() prepared | 6173.0 | 22394.1 |
| technical.unique.n48.b1024.single | strpos() loop | 44298.2 | 91203.2 |
| technical.unique.n48.b1024.single | preg_match_all() [literal] | 46362.2 | 230388.0 |
| technical.unique.n48.b1024.single | preg_match_all() [prefix] | 46799.9 | 230521.2 |
| technical.unique.n48.b128.single | Matcher::getMatchedKeywords() prepared | 1448.6 | 5564.0 |
| technical.unique.n48.b128.single | strpos() loop | 6732.3 | 27162.0 |
| technical.unique.n48.b128.single | preg_match_all() [literal] | 14410.1 | 57562.0 |
| technical.unique.n48.b128.single | preg_match_all() [prefix] | 14510.1 | 57868.1 |
| technical.unique.n48.b256.single | Matcher::getMatchedKeywords() prepared | 2049.9† | 7991.0† |
| technical.unique.n48.b256.single | strpos() loop | 8331.3 | 33615.0 |
| technical.unique.n48.b256.single | preg_match_all() [literal] | 19142.2 | 82484.9 |
| technical.unique.n48.b256.single | preg_match_all() [prefix] | 19558.0 | 82821.0 |
| technical.unique.n48.b4096.single | Matcher::getMatchedKeywords() prepared | 36594.7 | 78355.2 |
| technical.unique.n48.b4096.single | strpos() loop | 159026.1 | 270093.1 |
| technical.unique.n48.b4096.single | preg_match_all() [literal] | 180781.9 | 792786.5 |
| technical.unique.n48.b4096.single | preg_match_all() [prefix] | 216330.5 | 792229.8 |
| technical.unique.n8.b1024.single | Matcher::getMatchedKeywords() prepared | 5658.4 | 21193.0 |
| technical.unique.n8.b1024.single | strpos() loop | 7767.3 | 17974.0 |
| technical.unique.n8.b1024.single | preg_match_all() [literal] | 11025.5 | 43061.0 |
| technical.unique.n8.b1024.single | preg_match_all() [prefix] | 10235.8 | 43388.9 |
| technical.unique.n8.b128.single | Matcher::getMatchedKeywords() prepared | 1478.4 | 5455.0 |
| technical.unique.n8.b128.single | strpos() loop | 2379.5 | 9017.0 |
| technical.unique.n8.b128.single | preg_match_all() [literal] | 5944.9 | 22471.1 |
| technical.unique.n8.b128.single | preg_match_all() [prefix] | 5868.6† | 22659.0† |
| technical.unique.n8.b256.single | Matcher::getMatchedKeywords() prepared | 2064.9 | 7783.0 |
| technical.unique.n8.b256.single | strpos() loop | 2516.3† | 9527.0† |
| technical.unique.n8.b256.single | preg_match_all() [literal] | 6748.0 | 25439.0 |
| technical.unique.n8.b256.single | preg_match_all() [prefix] | 6580.0† | 25642.1† |
| technical.unique.n8.b4096.single | Matcher::getMatchedKeywords() prepared | 43280.5 | 74625.9 |
| technical.unique.n8.b4096.single | strpos() loop | 23954.6 | 42154.0 |
| technical.unique.n8.b4096.single | preg_match_all() [literal] | 27190.4 | 108344.9 |
| technical.unique.n8.b4096.single | preg_match_all() [prefix] | 23448.9† | 109042.6† |
