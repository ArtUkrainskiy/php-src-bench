# Cycles and instructions

Five alternating 0/N pairs per implementation. † means at least one pair failed quality checks.

| Input | Implementation | Cycles/job | Instructions/job |
|---|---|---:|---:|
| comments.all.n8.b256.single | Matcher::matchAll() prepared | 2394.1† | 7230.0† |
| comments.all.n8.b256.single | Matcher::matchAll() oneshot | 17136.6 | 77334.2 |
| comments.all.n8.b256.single | strpos() loop | 2313.0 | 8839.0 |
| comments.all.n8.b256.single | preg_match_all() [literal] | 6042.5 | 22449.9 |
| comments.all.n8.b256.single | preg_match_all() [prefix] | 5851.4 | 22598.0 |
| comments.any.n16.b256.absent | Matcher::matches() prepared | 1959.8† | 6576.0† |
| comments.any.n16.b256.absent | Matcher::matches() oneshot | 41129.2 | 187490.8 |
| comments.any.n16.b256.absent | strpos() loop | 3583.3 | 12464.0 |
| comments.any.n16.b256.absent | preg_match() [literal] | 2545.5 | 12082.0 |
| comments.any.n16.b256.absent | preg_match() [prefix] | 2237.9 | 10063.0 |
| comments.any.n16.b256.absent | str_contains() loop | 3016.0 | 9918.0 |
| comments.count.n16.b256.single | Matcher::countMatches() prepared | 2049.8 | 6677.0 |
| comments.count.n16.b256.single | Matcher::countMatches() oneshot | 41484.7 | 187589.1 |
| comments.count.n16.b256.single | strpos() loop | 3711.7 | 12923.0 |
| comments.count.n16.b256.single | preg_match_all() [literal] | 5638.6 | 23940.1 |
| comments.count.n16.b256.single | preg_match_all() [prefix] | 5227.8 | 22435.0 |
| comments.count.n16.b256.single | substr_count()/strpos() loop | 3565.4 | 12713.0 |
| comments.replace.n16.b256.single | Replacer::replace() prepared | 2311.3† | 7781.0† |
| comments.replace.n16.b256.single | Replacer::replace() oneshot | 18640.9 | 82448.9 |
| comments.replace.n16.b256.single | strtr() | 7188.1 | 39757.9 |
| comments.replace.n16.b256.single | preg_replace_callback() [literal] | 2920.2 | 13040.0 |
| comments.replace.n16.b256.single | preg_replace_callback() [prefix] | 2517.9 | 11161.0 |
| comments.replace.n16.b256.single | str_replace() | 2715.6 | 9652.0 |
| comments.unique.n8.b256.single | Matcher::getMatchedKeywords() prepared | 2053.7 | 7868.0 |
| comments.unique.n8.b256.single | Matcher::getMatchedKeywords() oneshot | 16689.7 | 77970.0 |
| comments.unique.n8.b256.single | strpos() loop | 2301.4 | 8822.0 |
| comments.unique.n8.b256.single | preg_match_all() [literal] | 6358.0 | 23753.0 |
| comments.unique.n8.b256.single | preg_match_all() [prefix] | 6183.4 | 23901.0 |
| technical.all.n1.b256.single | Matcher::matchAll() prepared | 2317.2 | 6213.0 |
| technical.all.n1.b256.single | Matcher::matchAll() oneshot | 4127.6 | 12781.0 |
| technical.all.n1.b256.single | strpos() loop | 1669.6 | 6014.0 |
| technical.all.n1.b256.single | preg_match_all() [literal] | 2756.9 | 9948.0 |
| technical.all.n1.b256.single | preg_match_all() [prefix] | 2755.6 | 9948.0 |
| technical.all.n16.b256.single | Matcher::matchAll() prepared | 2451.3 | 7203.0 |
| technical.all.n16.b256.single | Matcher::matchAll() oneshot | 42510.1† | 188121.8† |
| technical.all.n16.b256.single | strpos() loop | 4060.7† | 15392.0† |
| technical.all.n16.b256.single | preg_match_all() [literal] | 9495.0† | 36968.2† |
| technical.all.n16.b256.single | preg_match_all() [prefix] | 9096.1† | 36271.0† |
| technical.all.n4.b256.single | Matcher::matchAll() prepared | 2556.2† | 6650.0† |
| technical.all.n4.b256.single | Matcher::matchAll() oneshot | 9480.1 | 39181.1 |
| technical.all.n4.b256.single | strpos() loop | 2050.6 | 7585.0 |
| technical.all.n4.b256.single | preg_match_all() [literal] | 4368.0 | 16595.0 |
| technical.all.n4.b256.single | preg_match_all() [prefix] | 4374.9 | 16595.0 |
| technical.all.n48.b256.single | Matcher::matchAll() prepared | 2452.7† | 7347.1† |
| technical.all.n48.b256.single | Matcher::matchAll() oneshot | 113798.2† | 490208.9† |
| technical.all.n48.b256.single | strpos() loop | 8405.9† | 33631.9† |
| technical.all.n48.b256.single | preg_match_all() [literal] | 19268.3† | 81335.1† |
| technical.all.n48.b256.single | preg_match_all() [prefix] | 19501.5† | 81671.1† |
| technical.all.n8.b256.single | Matcher::matchAll() prepared | 2486.7† | 7149.0† |
| technical.all.n8.b256.single | Matcher::matchAll() oneshot | 17332.9† | 77253.1† |
| technical.all.n8.b256.single | strpos() loop | 2578.6† | 9544.0† |
| technical.all.n8.b256.single | preg_match_all() [literal] | 6554.1† | 24136.0† |
| technical.all.n8.b256.single | preg_match_all() [prefix] | 6394.2† | 24339.0† |
| technical.any.n1.b256.absent | Matcher::matches() prepared | 1891.4 | 5361.0 |
| technical.any.n1.b256.absent | Matcher::matches() oneshot | 3653.1 | 11929.0 |
| technical.any.n1.b256.absent | strpos() loop | 1057.2 | 3556.0 |
| technical.any.n1.b256.absent | preg_match() [literal] | 1130.3 | 3902.0 |
| technical.any.n1.b256.absent | preg_match() [prefix] | 1127.1 | 3902.0 |
| technical.any.n1.b256.absent | str_contains() loop | 804.1 | 2764.0 |
| technical.any.n1.b256.absent | str_contains() | 729.5 | 2553.0 |
| technical.any.n16.b256.absent | Matcher::matches() prepared | 2020.4† | 6423.0† |
| technical.any.n16.b256.absent | Matcher::matches() oneshot | 41408.4† | 187337.9† |
| technical.any.n16.b256.absent | strpos() loop | 3338.5 | 12718.0 |
| technical.any.n16.b256.absent | preg_match() [literal] | 2847.3 | 13324.0 |
| technical.any.n16.b256.absent | preg_match() [prefix] | 2378.4 | 10966.0 |
| technical.any.n16.b256.absent | str_contains() loop | 2732.6 | 10195.0 |
| technical.any.n4.b256.absent | Matcher::matches() prepared | 2060.0 | 5829.0 |
| technical.any.n4.b256.absent | Matcher::matches() oneshot | 9000.6† | 38356.0† |
| technical.any.n4.b256.absent | strpos() loop | 1434.1 | 5197.0 |
| technical.any.n4.b256.absent | preg_match() [literal] | 1538.5 | 4417.0 |
| technical.any.n4.b256.absent | preg_match() [prefix] | 1515.1 | 4360.0 |
| technical.any.n4.b256.absent | str_contains() loop | 1115.3 | 4059.0 |
| technical.any.n48.b256.absent | Matcher::matches() prepared | 1983.8 | 6567.0 |
| technical.any.n48.b256.absent | Matcher::matches() oneshot | 113010.0 | 489428.6 |
| technical.any.n48.b256.absent | strpos() loop | 7638.0 | 30773.9 |
| technical.any.n48.b256.absent | preg_match() [literal] | 7393.4 | 34464.0 |
| technical.any.n48.b256.absent | preg_match() [prefix] | 4283.8† | 19290.1† |
| technical.any.n48.b256.absent | str_contains() loop | 6417.6 | 24560.0 |
| technical.any.n48.b256.early | Matcher::matches() prepared | 859.1 | 2896.0 |
| technical.any.n48.b256.early | Matcher::matches() oneshot | 110315.4 | 485758.6 |
| technical.any.n48.b256.early | strpos() loop | 4605.8 | 18224.0 |
| technical.any.n48.b256.early | preg_match() [literal] | 1303.1 | 4419.0 |
| technical.any.n48.b256.early | preg_match() [prefix] | 1276.1 | 4318.0 |
| technical.any.n48.b256.early | str_contains() loop | 3927.2 | 14580.0 |
| technical.any.n48.b256.late | Matcher::matches() prepared | 1919.4 | 6478.0 |
| technical.any.n48.b256.late | Matcher::matches() oneshot | 111552.9 | 489340.0 |
| technical.any.n48.b256.late | strpos() loop | 4496.1 | 18023.0 |
| technical.any.n48.b256.late | preg_match() [literal] | 7358.8 | 32821.0 |
| technical.any.n48.b256.late | preg_match() [prefix] | 4063.8 | 18409.0 |
| technical.any.n48.b256.late | str_contains() loop | 3846.9† | 14377.0† |
| technical.any.n48.b256.middle | Matcher::matches() prepared | 1369.5† | 4660.0† |
| technical.any.n48.b256.middle | Matcher::matches() oneshot | 110933.4 | 487521.6 |
| technical.any.n48.b256.middle | strpos() loop | 4489.2 | 17906.0 |
| technical.any.n48.b256.middle | preg_match() [literal] | 4286.7 | 18618.0 |
| technical.any.n48.b256.middle | preg_match() [prefix] | 2691.9 | 11340.0 |
| technical.any.n48.b256.middle | str_contains() loop | 3811.5 | 14270.0 |
| technical.any.n8.b256.absent | Matcher::matches() prepared | 1987.0 | 6369.0 |
| technical.any.n8.b256.absent | Matcher::matches() oneshot | 16613.5 | 76473.3 |
| technical.any.n8.b256.absent | strpos() loop | 1863.7 | 7096.0 |
| technical.any.n8.b256.absent | preg_match() [literal] | 1950.7 | 8002.0 |
| technical.any.n8.b256.absent | preg_match() [prefix] | 1939.3 | 7876.0 |
| technical.any.n8.b256.absent | str_contains() loop | 1457.4 | 5505.0 |
| technical.count.n1.b256.single | Matcher::countMatches() prepared | 1772.2 | 5525.0 |
| technical.count.n1.b256.single | Matcher::countMatches() oneshot | 3536.5 | 12091.0 |
| technical.count.n1.b256.single | strpos() loop | 1173.0 | 4046.0 |
| technical.count.n1.b256.single | preg_match_all() [literal] | 1593.1 | 5732.0 |
| technical.count.n1.b256.single | preg_match_all() [prefix] | 1598.3 | 5732.0 |
| technical.count.n1.b256.single | substr_count()/strpos() loop | 777.9 | 2829.0 |
| technical.count.n1.b256.single | substr_count() | 716.3 | 2564.0 |
| technical.count.n16.b256.single | Matcher::countMatches() prepared | 2073.0 | 6515.0 |
| technical.count.n16.b256.single | Matcher::countMatches() oneshot | 41862.0 | 187428.3 |
| technical.count.n16.b256.single | strpos() loop | 3519.4† | 13424.0† |
| technical.count.n16.b256.single | preg_match_all() [literal] | 5893.3 | 25003.0 |
| technical.count.n16.b256.single | preg_match_all() [prefix] | 5655.7 | 24306.0 |
| technical.count.n16.b256.single | substr_count()/strpos() loop | 3301.8 | 13214.0 |
| technical.count.n4.b256.single | Matcher::countMatches() prepared | 1989.8 | 5966.0 |
| technical.count.n4.b256.single | Matcher::countMatches() oneshot | 8882.4† | 38490.7† |
| technical.count.n4.b256.single | strpos() loop | 1546.4 | 5617.0 |
| technical.count.n4.b256.single | preg_match_all() [literal] | 2543.2 | 9796.0 |
| technical.count.n4.b256.single | preg_match_all() [prefix] | 2540.0 | 9796.0 |
| technical.count.n4.b256.single | substr_count()/strpos() loop | 1176.2 | 4611.0 |
| technical.count.n48.b256.single | Matcher::countMatches() prepared | 2062.1 | 6659.0 |
| technical.count.n48.b256.single | Matcher::countMatches() oneshot | 111234.3 | 489519.4 |
| technical.count.n48.b256.single | strpos() loop | 7876.1 | 31670.0 |
| technical.count.n48.b256.single | preg_match_all() [literal] | 14135.0 | 65065.1 |
| technical.count.n48.b256.single | preg_match_all() [prefix] | 14637.8 | 65401.0 |
| technical.count.n48.b256.single | substr_count()/strpos() loop | 8090.5 | 33588.0 |
| technical.count.n48.b4096.single | Matcher::countMatches() prepared | 21718.8 | 65529.1 |
| technical.count.n48.b4096.single | Matcher::countMatches() oneshot | 142583.9 | 548028.5 |
| technical.count.n48.b4096.single | strpos() loop | 158830.1 | 268543.1 |
| technical.count.n48.b4096.single | preg_match_all() [literal] | 170851.4 | 775368.0 |
| technical.count.n48.b4096.single | preg_match_all() [prefix] | 210589.4 | 774809.5 |
| technical.count.n48.b4096.single | substr_count()/strpos() loop | 159324.3 | 270576.7 |
| technical.count.n8.b256.single | Matcher::countMatches() prepared | 2061.1 | 6461.0 |
| technical.count.n8.b256.single | Matcher::countMatches() oneshot | 16631.3 | 76562.9 |
| technical.count.n8.b256.single | strpos() loop | 2006.3 | 7576.0 |
| technical.count.n8.b256.single | preg_match_all() [literal] | 4197.5 | 15614.9 |
| technical.count.n8.b256.single | preg_match_all() [prefix] | 4038.9 | 15818.1 |
| technical.count.n8.b256.single | substr_count()/strpos() loop | 1649.9 | 6830.0 |
| technical.replace.n1.b256.single | Replacer::replace() prepared | 2036.8† | 6633.0† |
| technical.replace.n1.b256.single | Replacer::replace() oneshot | 3835.6† | 12955.1† |
| technical.replace.n1.b256.single | strtr() | 952.8† | 3310.0† |
| technical.replace.n1.b256.single | preg_replace_callback() [literal] | 1491.6† | 5337.0† |
| technical.replace.n1.b256.single | preg_replace_callback() [prefix] | 1494.9† | 5337.0† |
| technical.replace.n1.b256.single | str_replace() | 1015.9† | 3561.0† |
| technical.replace.n16.b256.single | Replacer::replace() prepared | 2373.3† | 7787.1† |
| technical.replace.n16.b256.single | Replacer::replace() oneshot | 19054.2† | 82455.1† |
| technical.replace.n16.b256.single | strtr() | 9041.1† | 50051.0† |
| technical.replace.n16.b256.single | preg_replace_callback() [literal] | 3313.6† | 14566.0† |
| technical.replace.n16.b256.single | preg_replace_callback() [prefix] | 2737.7† | 12202.0† |
| technical.replace.n16.b256.single | str_replace() | 2675.6† | 10233.0† |
| technical.replace.n4.b256.single | Replacer::replace() prepared | 2245.3† | 7074.0† |
| technical.replace.n4.b256.single | Replacer::replace() oneshot | 6916.5† | 26600.0† |
| technical.replace.n4.b256.single | strtr() | 2389.3† | 11454.0† |
| technical.replace.n4.b256.single | preg_replace_callback() [literal] | 1813.7† | 5764.0† |
| technical.replace.n4.b256.single | preg_replace_callback() [prefix] | 1790.1† | 5714.0† |
| technical.replace.n4.b256.single | str_replace() | 1254.6† | 4596.0† |
| technical.replace.n48.b256.single | Replacer::replace() prepared | 2402.2† | 7976.0† |
| technical.replace.n48.b256.single | Replacer::replace() oneshot | 71948.0† | 310857.9† |
| technical.replace.n48.b256.single | strtr() | 19783.7† | 111398.8† |
| technical.replace.n48.b256.single | preg_replace_callback() [literal] | 7560.9† | 35569.2† |
| technical.replace.n48.b256.single | preg_replace_callback() [prefix] | 4608.3† | 20446.0† |
| technical.replace.n48.b256.single | str_replace() | 5665.5† | 22585.0† |
| technical.replace.n8.b256.single | Replacer::replace() prepared | 2380.6† | 7737.0† |
| technical.replace.n8.b256.single | Replacer::replace() oneshot | 13355.3† | 56236.0† |
| technical.replace.n8.b256.single | strtr() | 2972.0 | 14800.0 |
| technical.replace.n8.b256.single | preg_replace_callback() [literal] | 2197.9 | 9249.1 |
| technical.replace.n8.b256.single | preg_replace_callback() [prefix] | 2244.3 | 9116.0 |
| technical.replace.n8.b256.single | str_replace() | 1508.4 | 5840.0 |
| technical.unique.n1.b256.single | Matcher::getMatchedKeywords() prepared | 1340.8 | 5073.0 |
| technical.unique.n1.b256.single | Matcher::getMatchedKeywords() oneshot | 3185.7† | 11639.1† |
| technical.unique.n1.b256.single | strpos() loop | 1639.1 | 5997.0 |
| technical.unique.n1.b256.single | preg_match_all() [literal] | 3098.4 | 11336.0 |
| technical.unique.n1.b256.single | preg_match_all() [prefix] | 3088.6 | 11336.0 |
| technical.unique.n1.b256.single | strpos() + result list | 756.1 | 2623.0 |
| technical.unique.n16.b256.single | Matcher::getMatchedKeywords() prepared | 2081.9 | 7846.0 |
| technical.unique.n16.b256.single | Matcher::getMatchedKeywords() oneshot | 41386.7† | 188759.1† |
| technical.unique.n16.b256.single | strpos() loop | 4047.1 | 15375.0 |
| technical.unique.n16.b256.single | preg_match_all() [literal] | 9676.9 | 38203.1 |
| technical.unique.n16.b256.single | preg_match_all() [prefix] | 9084.5 | 37505.8 |
| technical.unique.n4.b256.single | Matcher::getMatchedKeywords() prepared | 2085.7 | 7294.1 |
| technical.unique.n4.b256.single | Matcher::getMatchedKeywords() oneshot | 9006.6† | 39819.0† |
| technical.unique.n4.b256.single | strpos() loop | 2056.0 | 7568.0 |
| technical.unique.n4.b256.single | preg_match_all() [literal] | 4741.5 | 17932.0 |
| technical.unique.n4.b256.single | preg_match_all() [prefix] | 4747.2 | 17932.0 |
| technical.unique.n48.b256.single | Matcher::getMatchedKeywords() prepared | 2050.8 | 7991.0 |
| technical.unique.n48.b256.single | Matcher::getMatchedKeywords() oneshot | 113294.9† | 490853.3† |
| technical.unique.n48.b256.single | strpos() loop | 8358.4 | 33622.2 |
| technical.unique.n48.b256.single | preg_match_all() [literal] | 19267.2 | 82484.9 |
| technical.unique.n48.b256.single | preg_match_all() [prefix] | 19476.1† | 82821.0† |
| technical.unique.n8.b256.single | Matcher::getMatchedKeywords() prepared | 2074.1 | 7787.0 |
| technical.unique.n8.b256.single | Matcher::getMatchedKeywords() oneshot | 16693.5 | 77888.6 |
| technical.unique.n8.b256.single | strpos() loop | 2523.5 | 9527.0 |
| technical.unique.n8.b256.single | preg_match_all() [literal] | 6756.0 | 25439.0 |
| technical.unique.n8.b256.single | preg_match_all() [prefix] | 6565.5† | 25642.1† |
