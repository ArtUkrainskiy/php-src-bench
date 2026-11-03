# Input length: full results

[Methods, returned results and exact comparators](README.md#operations-and-comparators).

128 distinct literal keys, four different saved strings of each exact length, one string per operation. PCRE caches are warm; the prepared column reuses an object, while one-shot includes its full lifetime. A sample averages complete cycles of all four strings; the displayed time is the median of 15 samples. Units are µs per operation. `Prepared` measures a call on an existing object; `One-shot` directly measures construction, one call and destruction together. They are separate measurements, not an arithmetic sum.

The controlled English inputs reorder authored paragraphs; long documents repeat them. This is not a production trace. Unique-result counts and replacement counts vary with length, so the cases include both scanning and natural output costs. Exact texts and counts are in the [corpus](../../corpus/multi-pattern-length/README.md).

`1` means a directly observed single-string batch win with at least a 2% paired-median margin, including construction and destruction. This is an observation, not statistical confidence. `~N` values are **estimates**, not directly established minima. The model includes warm construction and one destruction, divided by the difference in prepared median operation time. It chooses the first integer above that quotient. Nonpositive differences show a dash; positive differences below 2% show `close`. The 2% cutoff is a noise heuristic, not confidence. [Direct batch measurements](LENGTH-PAYBACK.md) check selected nearby sizes; they do not prove a minimum.

## gcc15

| Method | Input | PHP built-ins µs | PCRE µs | Prepared µs | One-shot µs | Strings to beat PHP | Strings to beat PCRE |
|---|---:|---:|---:|---:|---:|---:|---:|
| `Matcher::matches()` (no match) | 128 B | 3.351 | 4.693 | 0.316 | 58.275 | ~19 | ~14 |
| `Matcher::matches()` (no match) | 4 KiB | 121.892 | 142.626 | 6.978 | 65.950 | 1 | 1 |
| `Matcher::matches()` (no match) | 16 KiB | 497.911 | 571.130 | 27.241 | 86.576 | 1 | 1 |
| `Matcher::getMatchedKeywords()` | 512 B | 17.842 | 20.329 | 1.707 | 47.486 | ~3 | ~3 |
| `Matcher::getMatchedKeywords()` | 4 KiB | 105.104 | 64.442 | 12.469 | 60.862 | 1 | 1 |
| `Matcher::getMatchedKeywords()` | 16 KiB | 207.546 | 103.328 | 40.338 | 91.136 | 1 | 1 |
| `Replacer::replace()` | 512 B | 38.278 | 12.880 | 1.566 | 46.389 | ~2 | ~4 |
| `Replacer::replace()` | 4 KiB | 359.125 | 98.547 | 12.016 | 59.369 | 1 | 1 |
| `Replacer::replace()` | 16 KiB | 1438.517 | 401.335 | 46.766 | 94.740 | 1 | 1 |

### All methods and counters

| Task | Input | Method | µs | CPU cycles | Instructions |
|---|---:|---|---:|---:|---:|
| Moderation: no match | 128 B | `contains_loop` | 3.351 | 14751.6 | 48731.9 |
| Moderation: no match | 128 B | `preg_match` | 4.693 | 21516.9 | 94934.3 |
| Moderation: no match | 128 B | `matcher` | 0.316 | 1435.4 | 3725.7 |
| Moderation: start | 128 B | `contains_loop` | 1.655 | 7749.1 | 25176.0 |
| Moderation: start | 128 B | `preg_match` | 0.913 | 4153.1 | 17108.5 |
| Moderation: start | 128 B | `matcher` | 0.141 | 630.9 | 1853.2 |
| Moderation: middle | 128 B | `contains_loop` | 1.697 | 7694.4 | 25128.8 |
| Moderation: middle | 128 B | `preg_match` | 2.977 | 13657.1 | 61928.0 |
| Moderation: middle | 128 B | `matcher` | 0.231 | 1033.5 | 2895.0 |
| Moderation: end | 128 B | `contains_loop` | 1.705 | 7672.4 | 24831.5 |
| Moderation: end | 128 B | `preg_match` | 4.267 | 19569.7 | 87163.3 |
| Moderation: end | 128 B | `matcher` | 0.292 | 1330.0 | 3655.5 |
| Moderation: no match | 4 KiB | `contains_loop` | 121.892 | 573940.2 | 802892.9 |
| Moderation: no match | 4 KiB | `preg_match` | 142.626 | 655801.8 | 3081410.3 |
| Moderation: no match | 4 KiB | `matcher` | 6.978 | 32587.7 | 73803.5 |
| Moderation: start | 4 KiB | `contains_loop` | 58.742 | 275803.8 | 404044.4 |
| Moderation: start | 4 KiB | `preg_match` | 0.905 | 4124.0 | 17108.5 |
| Moderation: start | 4 KiB | `matcher` | 0.141 | 633.5 | 1853.3 |
| Moderation: middle | 4 KiB | `contains_loop` | 58.739 | 276964.8 | 405700.8 |
| Moderation: middle | 4 KiB | `preg_match` | 72.055 | 331594.5 | 1559649.1 |
| Moderation: middle | 4 KiB | `matcher` | 3.582 | 16722.0 | 37995.7 |
| Moderation: end | 4 KiB | `contains_loop` | 58.995 | 278542.2 | 407871.5 |
| Moderation: end | 4 KiB | `preg_match` | 142.326 | 654276.7 | 3075598.4 |
| Moderation: end | 4 KiB | `matcher` | 6.984 | 32658.6 | 73760.2 |
| Moderation: no match | 16 KiB | `contains_loop` | 497.911 | 2345474.2 | 3067868.5 |
| Moderation: no match | 16 KiB | `preg_match` | 571.130 | 2625598.8 | 12365862.1 |
| Moderation: no match | 16 KiB | `matcher` | 27.241 | 127339.0 | 290736.7 |
| Moderation: start | 16 KiB | `contains_loop` | 246.539 | 1159090.9 | 1538834.8 |
| Moderation: start | 16 KiB | `preg_match` | 0.904 | 4115.4 | 17108.5 |
| Moderation: start | 16 KiB | `matcher` | 0.140 | 637.0 | 1853.3 |
| Moderation: middle | 16 KiB | `contains_loop` | 250.282 | 1173325.9 | 1547668.3 |
| Moderation: middle | 16 KiB | `preg_match` | 286.303 | 1315642.7 | 6201991.4 |
| Moderation: middle | 16 KiB | `matcher` | 13.776 | 64458.0 | 146459.6 |
| Moderation: end | 16 KiB | `contains_loop` | 250.721 | 1181907.5 | 1556565.5 |
| Moderation: end | 16 KiB | `preg_match` | 571.762 | 2623189.2 | 12361331.4 |
| Moderation: end | 16 KiB | `matcher` | 27.296 | 127520.3 | 290673.5 |
| Moderation: no match | 64 KiB | `contains_loop` | 1969.564 | 9259737.0 | 12123914.8 |
| Moderation: no match | 64 KiB | `preg_match` | 2285.126 | 10488830.8 | 49453963.5 |
| Moderation: no match | 64 KiB | `matcher` | 108.947 | 508791.6 | 1158765.1 |
| Moderation: start | 64 KiB | `contains_loop` | 985.328 | 4629976.6 | 6078283.2 |
| Moderation: start | 64 KiB | `preg_match` | 0.906 | 4127.6 | 17108.5 |
| Moderation: start | 64 KiB | `matcher` | 0.141 | 632.3 | 1853.3 |
| Moderation: middle | 64 KiB | `contains_loop` | 989.023 | 4660650.6 | 6112588.8 |
| Moderation: middle | 64 KiB | `preg_match` | 1141.479 | 5246168.8 | 24743133.5 |
| Moderation: middle | 64 KiB | `matcher` | 54.681 | 255440.9 | 580478.0 |
| Moderation: end | 64 KiB | `contains_loop` | 995.156 | 4690799.5 | 6147257.3 |
| Moderation: end | 64 KiB | `preg_match` | 2284.242 | 10489853.8 | 49447443.8 |
| Moderation: end | 64 KiB | `matcher` | 109.147 | 509589.0 | 1158708.3 |
| List matching support terms | 512 B | `strpos_unique` | 17.842 | 81206.3 | 207209.8 |
| List matching support terms | 512 B | `preg_each_unique` | 20.329 | 91562.3 | 279699.5 |
| List matching support terms | 512 B | `matcher` | 1.707 | 7857.7 | 19958.1 |
| Replace terms with help URLs | 512 B | `strtr` | 38.278 | 176655.7 | 530033.7 |
| Replace terms with help URLs | 512 B | `preg_replace_callback` | 12.880 | 59125.3 | 264954.6 |
| Replace terms with help URLs | 512 B | `replacer` | 1.566 | 7242.1 | 19894.5 |
| List matching support terms | 4 KiB | `strpos_unique` | 105.104 | 493767.7 | 970939.3 |
| List matching support terms | 4 KiB | `preg_each_unique` | 64.442 | 293495.9 | 972806.9 |
| List matching support terms | 4 KiB | `matcher` | 12.469 | 57019.9 | 130523.7 |
| Replace terms with help URLs | 4 KiB | `strtr` | 359.125 | 1648170.2 | 4256069.5 |
| Replace terms with help URLs | 4 KiB | `preg_replace_callback` | 98.547 | 452387.5 | 2094338.0 |
| Replace terms with help URLs | 4 KiB | `replacer` | 12.016 | 55338.8 | 144579.7 |
| List matching support terms | 16 KiB | `strpos_unique` | 207.546 | 976068.2 | 1588712.8 |
| List matching support terms | 16 KiB | `preg_each_unique` | 103.328 | 475554.0 | 1414200.4 |
| List matching support terms | 16 KiB | `matcher` | 40.338 | 188008.4 | 423185.3 |
| Replace terms with help URLs | 16 KiB | `strtr` | 1438.517 | 6638237.8 | 17049160.4 |
| Replace terms with help URLs | 16 KiB | `preg_replace_callback` | 401.335 | 1792664.7 | 8371436.9 |
| Replace terms with help URLs | 16 KiB | `replacer` | 46.766 | 216377.5 | 572086.7 |
| List matching support terms | 64 KiB | `strpos_unique` | 609.708 | 2873803.1 | 4071050.3 |
| List matching support terms | 64 KiB | `preg_each_unique` | 250.019 | 1151327.9 | 3206329.9 |
| List matching support terms | 64 KiB | `matcher` | 151.759 | 705813.6 | 1594457.5 |
| Replace terms with help URLs | 64 KiB | `strtr` | 5753.284 | 26518885.1 | 68135122.2 |
| Replace terms with help URLs | 64 KiB | `preg_replace_callback` | 1562.615 | 7153903.9 | 33435426.7 |
| Replace terms with help URLs | 64 KiB | `replacer` | 186.878 | 866166.3 | 2286244.9 |

### A/A elapsed controls

| Stage | Task | Time Δ |
|---|---|---:|
| before | Moderation: no match | -0.045% |
| before | Replace terms with help URLs | +0.033% |
| after | Moderation: no match | +0.120% |
| after | Replace terms with help URLs | -0.315% |

## clang21

| Method | Input | PHP built-ins µs | PCRE µs | Prepared µs | One-shot µs | Strings to beat PHP | Strings to beat PCRE |
|---|---:|---:|---:|---:|---:|---:|---:|
| `Matcher::matches()` (no match) | 128 B | 3.699 | 4.523 | 0.334 | 56.991 | ~17 | ~14 |
| `Matcher::matches()` (no match) | 4 KiB | 117.484 | 136.487 | 8.011 | 64.691 | 1 | 1 |
| `Matcher::matches()` (no match) | 16 KiB | 482.454 | 547.493 | 31.457 | 89.050 | 1 | 1 |
| `Matcher::getMatchedKeywords()` | 512 B | 18.068 | 20.152 | 1.786 | 45.538 | ~3 | ~3 |
| `Matcher::getMatchedKeywords()` | 4 KiB | 101.394 | 63.591 | 12.654 | 60.016 | 1 | 1 |
| `Matcher::getMatchedKeywords()` | 16 KiB | 199.215 | 102.015 | 41.693 | 90.653 | 1 | 1 |
| `Replacer::replace()` | 512 B | 38.996 | 13.922 | 1.587 | 45.149 | ~2 | ~4 |
| `Replacer::replace()` | 4 KiB | 361.649 | 108.050 | 12.352 | 58.486 | 1 | 1 |
| `Replacer::replace()` | 16 KiB | 1457.565 | 430.688 | 46.832 | 94.292 | 1 | 1 |

### All methods and counters

| Task | Input | Method | µs | CPU cycles | Instructions |
|---|---:|---|---:|---:|---:|
| Moderation: no match | 128 B | `contains_loop` | 3.699 | 16328.0 | 47649.6 |
| Moderation: no match | 128 B | `preg_match` | 4.523 | 20545.4 | 94940.4 |
| Moderation: no match | 128 B | `matcher` | 0.334 | 1539.8 | 4107.0 |
| Moderation: start | 128 B | `contains_loop` | 1.881 | 8252.5 | 24665.0 |
| Moderation: start | 128 B | `preg_match` | 0.856 | 3907.0 | 17116.5 |
| Moderation: start | 128 B | `matcher` | 0.133 | 607.3 | 1927.5 |
| Moderation: middle | 128 B | `contains_loop` | 1.883 | 8235.7 | 24608.3 |
| Moderation: middle | 128 B | `preg_match` | 2.840 | 12969.2 | 61936.0 |
| Moderation: middle | 128 B | `matcher` | 0.234 | 1059.5 | 3135.0 |
| Moderation: end | 128 B | `contains_loop` | 1.861 | 8094.1 | 24311.5 |
| Moderation: end | 128 B | `preg_match` | 4.084 | 18694.1 | 87171.3 |
| Moderation: end | 128 B | `matcher` | 0.308 | 1399.6 | 4020.7 |
| Moderation: no match | 4 KiB | `contains_loop` | 117.484 | 552870.9 | 758591.7 |
| Moderation: no match | 4 KiB | `preg_match` | 136.487 | 626136.3 | 3081413.1 |
| Moderation: no match | 4 KiB | `matcher` | 8.011 | 37388.0 | 85615.5 |
| Moderation: start | 4 KiB | `contains_loop` | 56.357 | 264466.0 | 381193.7 |
| Moderation: start | 4 KiB | `preg_match` | 0.848 | 3858.6 | 17116.5 |
| Moderation: start | 4 KiB | `matcher` | 0.134 | 610.2 | 1927.5 |
| Moderation: middle | 4 KiB | `contains_loop` | 56.575 | 266244.0 | 382818.2 |
| Moderation: middle | 4 KiB | `preg_match` | 68.896 | 316164.7 | 1559657.4 |
| Moderation: middle | 4 KiB | `matcher` | 4.071 | 18982.1 | 43965.9 |
| Moderation: end | 4 KiB | `contains_loop` | 56.842 | 267255.5 | 384959.0 |
| Moderation: end | 4 KiB | `preg_match` | 136.182 | 624408.1 | 3075607.0 |
| Moderation: end | 4 KiB | `matcher` | 8.021 | 37412.5 | 85565.4 |
| Moderation: no match | 16 KiB | `contains_loop` | 482.454 | 2267056.1 | 2922798.2 |
| Moderation: no match | 16 KiB | `preg_match` | 547.493 | 2505063.6 | 12365850.8 |
| Moderation: no match | 16 KiB | `matcher` | 31.457 | 146826.2 | 337948.2 |
| Moderation: start | 16 KiB | `contains_loop` | 238.519 | 1118599.5 | 1464029.7 |
| Moderation: start | 16 KiB | `preg_match` | 0.847 | 3853.3 | 17116.5 |
| Moderation: start | 16 KiB | `matcher` | 0.134 | 612.3 | 1927.5 |
| Moderation: middle | 16 KiB | `contains_loop` | 240.850 | 1131558.3 | 1472760.5 |
| Moderation: middle | 16 KiB | `preg_match` | 273.474 | 1255091.0 | 6201997.5 |
| Moderation: middle | 16 KiB | `matcher` | 15.828 | 73987.7 | 170130.2 |
| Moderation: end | 16 KiB | `contains_loop` | 242.561 | 1140489.1 | 1481517.9 |
| Moderation: end | 16 KiB | `preg_match` | 545.854 | 2502563.2 | 12361365.5 |
| Moderation: end | 16 KiB | `matcher` | 31.538 | 147519.5 | 337870.5 |
| Moderation: no match | 64 KiB | `contains_loop` | 1903.438 | 8939815.2 | 11574584.0 |
| Moderation: no match | 64 KiB | `preg_match` | 2182.794 | 10008625.2 | 49453957.0 |
| Moderation: no match | 64 KiB | `matcher` | 125.836 | 587573.9 | 1347640.9 |
| Moderation: start | 64 KiB | `contains_loop` | 951.595 | 4462852.9 | 5795501.4 |
| Moderation: start | 64 KiB | `preg_match` | 0.841 | 3874.1 | 17116.5 |
| Moderation: start | 64 KiB | `matcher` | 0.134 | 609.1 | 1927.5 |
| Moderation: middle | 64 KiB | `contains_loop` | 955.163 | 4490798.8 | 5829313.2 |
| Moderation: middle | 64 KiB | `preg_match` | 1090.553 | 5004546.5 | 24743137.7 |
| Moderation: middle | 64 KiB | `matcher` | 62.919 | 293814.7 | 674975.5 |
| Moderation: end | 64 KiB | `contains_loop` | 962.167 | 4520760.6 | 5863377.3 |
| Moderation: end | 64 KiB | `preg_match` | 2182.140 | 10008157.1 | 49447450.4 |
| Moderation: end | 64 KiB | `matcher` | 125.988 | 587780.0 | 1347571.2 |
| List matching support terms | 512 B | `strpos_unique` | 18.068 | 82977.4 | 207892.4 |
| List matching support terms | 512 B | `preg_each_unique` | 20.152 | 91808.2 | 287510.2 |
| List matching support terms | 512 B | `matcher` | 1.786 | 8250.6 | 21904.0 |
| Replace terms with help URLs | 512 B | `strtr` | 38.996 | 179805.9 | 542908.3 |
| Replace terms with help URLs | 512 B | `preg_replace_callback` | 13.922 | 64012.3 | 264417.2 |
| Replace terms with help URLs | 512 B | `replacer` | 1.587 | 7277.9 | 21280.2 |
| List matching support terms | 4 KiB | `strpos_unique` | 101.394 | 476412.6 | 954790.8 |
| List matching support terms | 4 KiB | `preg_each_unique` | 63.591 | 292508.6 | 996878.6 |
| List matching support terms | 4 KiB | `matcher` | 12.654 | 58715.6 | 146046.2 |
| Replace terms with help URLs | 4 KiB | `strtr` | 361.649 | 1664349.2 | 4358812.1 |
| Replace terms with help URLs | 4 KiB | `preg_replace_callback` | 108.050 | 495614.6 | 2090268.8 |
| Replace terms with help URLs | 4 KiB | `replacer` | 12.352 | 55794.6 | 155545.1 |
| List matching support terms | 16 KiB | `strpos_unique` | 199.215 | 931650.0 | 1533276.5 |
| List matching support terms | 16 KiB | `preg_each_unique` | 102.015 | 468869.5 | 1438625.7 |
| List matching support terms | 16 KiB | `matcher` | 41.693 | 194024.2 | 483327.0 |
| Replace terms with help URLs | 16 KiB | `strtr` | 1457.565 | 6723950.5 | 17460776.6 |
| Replace terms with help URLs | 16 KiB | `preg_replace_callback` | 430.688 | 1971373.5 | 8355428.7 |
| Replace terms with help URLs | 16 KiB | `replacer` | 46.832 | 216901.5 | 615801.8 |
| List matching support terms | 64 KiB | `strpos_unique` | 575.723 | 2712105.7 | 3855637.7 |
| List matching support terms | 64 KiB | `preg_each_unique` | 246.493 | 1142677.5 | 3230596.8 |
| List matching support terms | 64 KiB | `matcher` | 156.822 | 729756.5 | 1833006.6 |
| Replace terms with help URLs | 64 KiB | `strtr` | 5829.945 | 26854926.8 | 69778955.4 |
| Replace terms with help URLs | 64 KiB | `preg_replace_callback` | 1719.485 | 7860330.6 | 33371565.8 |
| Replace terms with help URLs | 64 KiB | `replacer` | 189.748 | 873966.3 | 2460903.4 |

### A/A elapsed controls

| Stage | Task | Time Δ |
|---|---|---:|
| before | Moderation: no match | +0.186% |
| before | Replace terms with help URLs | +0.001% |
| after | Moderation: no match | +0.340% |
| after | Replace terms with help URLs | -0.011% |

[Raw GCC samples and counters](data/length-gcc15.json) · [Raw Clang samples and counters](data/length-clang21.json) · [Capture audit](data/length-capture-audit.json) · [Reproduce](REPRODUCE.md#fixed-length-and-pure-construction-series).
