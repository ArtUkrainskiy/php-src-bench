# Cycles and instructions

Five corrected N/0 pairs per method. Columns are medians per call; all pairs are saved in [counter-data.json.gz](data/counter-data.json.gz). † means at least one pair did not pass the checks. Invalid values are not removed and do not support comparative claims.

| Compiler | Method / input | Mode | Method | Cycles/call | Instructions/call | Quality |
|---|---|---|---|---:|---:|---|
| gcc15 | 128 B; dictionary of 8 keys; key lengths 12 B; no matches | prepared | `str_contains()` loop | 1250.2 | 4058.0 | checks passed |
| gcc15 | 128 B; dictionary of 8 keys; key lengths 12 B; no matches | prepared | `preg_match()` | 1326.1 | 5649.0 | checks passed |
| gcc15 | 128 B; dictionary of 8 keys; key lengths 12 B; no matches | prepared | Matcher::matches() | 850.9 | 2889.0 | checks passed |
| gcc15 | 128 B; dictionary of 8 keys; key lengths 12 B; no matches | oneshot | `str_contains()` loop | 1261.7 | 4058.0 | checks passed |
| gcc15 | 128 B; dictionary of 8 keys; key lengths 12 B; no matches | oneshot | `preg_match()` | 1330.8 | 5649.0 | checks passed |
| gcc15 | 128 B; dictionary of 8 keys; key lengths 12 B; no matches | oneshot | Matcher::matches() | 16084.5 | 61402.0 | checks passed |
| clang21 | 128 B; dictionary of 8 keys; key lengths 12 B; no matches | prepared | `str_contains()` loop | 1256.7 | 3950.0 | checks passed |
| clang21 | 128 B; dictionary of 8 keys; key lengths 12 B; no matches | prepared | `preg_match()` | 1295.8 | 5586.0 | checks passed |
| clang21 | 128 B; dictionary of 8 keys; key lengths 12 B; no matches | prepared | Matcher::matches() | 733.3 | 3040.0 | checks passed |
| clang21 | 128 B; dictionary of 8 keys; key lengths 12 B; no matches | oneshot | `str_contains()` loop | 1257.7 | 3950.0 | checks passed |
| clang21 | 128 B; dictionary of 8 keys; key lengths 12 B; no matches | oneshot | `preg_match()` | 1293.3 | 5586.0 | checks passed |
| clang21 | 128 B; dictionary of 8 keys; key lengths 12 B; no matches | oneshot | Matcher::matches() | 15467.2 | 65198.0 | checks passed |
| gcc15 | 128 B; dictionary of 128 keys; key lengths 12 B; no matches | prepared | `str_contains()` loop | 14252.8 | 47261.1 | checks passed |
| gcc15 | 128 B; dictionary of 128 keys; key lengths 12 B; no matches | prepared | `preg_match()` | 14092.7 | 64180.0 | checks passed |
| gcc15 | 128 B; dictionary of 128 keys; key lengths 12 B; no matches | prepared | Matcher::matches() | 849.6 | 2889.0 | checks passed |
| gcc15 | 128 B; dictionary of 128 keys; key lengths 12 B; no matches | oneshot | `str_contains()` loop | 14385.6 | 47262.9 | checks passed |
| gcc15 | 128 B; dictionary of 128 keys; key lengths 12 B; no matches | oneshot | `preg_match()` | 14041.4 | 64180.1 | checks passed |
| gcc15 | 128 B; dictionary of 128 keys; key lengths 12 B; no matches | oneshot | Matcher::matches() | 244468.1 | 775116.2 | checks passed |
| clang21 | 128 B; dictionary of 128 keys; key lengths 12 B; no matches | prepared | `str_contains()` loop | 15490.8 | 46213.0 | checks passed |
| clang21 | 128 B; dictionary of 128 keys; key lengths 12 B; no matches | prepared | `preg_match()` | 13936.7 | 64117.0 | checks passed |
| clang21 | 128 B; dictionary of 128 keys; key lengths 12 B; no matches | prepared | Matcher::matches() | 732.6 | 3040.0 | checks passed |
| clang21 | 128 B; dictionary of 128 keys; key lengths 12 B; no matches | oneshot | `str_contains()` loop | 15448.7 | 46218.2 | checks passed |
| clang21 | 128 B; dictionary of 128 keys; key lengths 12 B; no matches | oneshot | `preg_match()` | 13941.6 | 64117.0 | checks passed |
| clang21 | 128 B; dictionary of 128 keys; key lengths 12 B; no matches | oneshot | Matcher::matches() | 240371.1 | 818362.8 | checks passed |
| gcc15 | 1024 B; dictionary of 16 keys; key lengths 12 B; no matches | prepared | `str_contains()` loop | 18128.5 | 30987.1 | checks passed |
| gcc15 | 1024 B; dictionary of 16 keys; key lengths 12 B; no matches | prepared | `preg_match()` | 11237.1 | 52167.0 | checks passed |
| gcc15 | 1024 B; dictionary of 16 keys; key lengths 12 B; no matches | prepared | Matcher::matches() | 4668.7 | 14796.0 | checks passed |
| gcc15 | 1024 B; dictionary of 16 keys; key lengths 12 B; no matches | oneshot | `str_contains()` loop | 18162.7 | 30987.0 | checks passed |
| gcc15 | 1024 B; dictionary of 16 keys; key lengths 12 B; no matches | oneshot | `preg_match()` | 11214.2 | 52167.0 | checks passed |
| gcc15 | 1024 B; dictionary of 16 keys; key lengths 12 B; no matches | oneshot | Matcher::matches() | 33045.5 | 121846.0 | checks passed |
| clang21 | 1024 B; dictionary of 16 keys; key lengths 12 B; no matches | prepared | `str_contains()` loop | 16785.8 | 27080.0 | checks passed |
| clang21 | 1024 B; dictionary of 16 keys; key lengths 12 B; no matches | prepared | `preg_match()` | 12579.8 | 52104.0 | checks passed |
| clang21 | 1024 B; dictionary of 16 keys; key lengths 12 B; no matches | prepared | Matcher::matches() | 3969.4 | 16228.0 | checks passed |
| clang21 | 1024 B; dictionary of 16 keys; key lengths 12 B; no matches | oneshot | `str_contains()` loop | 16793.2 | 27080.1 | checks passed |
| clang21 | 1024 B; dictionary of 16 keys; key lengths 12 B; no matches | oneshot | `preg_match()` | 12492.7 | 52104.0 | checks passed |
| clang21 | 1024 B; dictionary of 16 keys; key lengths 12 B; no matches | oneshot | Matcher::matches() | 32552.2 | 129778.9 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; no matches | prepared | `str_contains()` loop | 563337.3 | 787687.0 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; no matches | prepared | `preg_match()` | 462275.8 | 2103394.1 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; no matches | prepared | Matcher::matches() | 17740.5 | 56070.0 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; no matches | oneshot | `str_contains()` loop | 562948.3 | 787688.1 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; no matches | oneshot | `preg_match()` | 462091.9 | 2103390.1 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; no matches | oneshot | Matcher::matches() | 272825.3 | 829068.2 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; no matches | prepared | `str_contains()` loop | 525421.8 | 720809.8 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; no matches | prepared | `preg_match()` | 461082.7 | 2103328.5 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; no matches | prepared | Matcher::matches() | 15811.4 | 62044.0 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; no matches | oneshot | `str_contains()` loop | 525407.7 | 720811.5 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; no matches | oneshot | `preg_match()` | 460808.5 | 2103329.2 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; no matches | oneshot | Matcher::matches() | 267828.1 | 878158.8 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 8, dictionary key #65 | prepared | `str_contains()` loop | 279952.6 | 395227.9 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 8, dictionary key #65 | prepared | `preg_match()` | 1905.2 | 7808.0 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 8, dictionary key #65 | prepared | Matcher::matches() | 531.3 | 1577.0 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 8, dictionary key #65 | oneshot | `str_contains()` loop | 279923.7 | 395228.0 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 8, dictionary key #65 | oneshot | `preg_match()` | 1909.3 | 7808.0 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 8, dictionary key #65 | oneshot | Matcher::matches() | 243789.8 | 774574.7 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 8, dictionary key #65 | prepared | `str_contains()` loop | 260914.3 | 361617.5 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 8, dictionary key #65 | prepared | `preg_match()` | 1865.1 | 7747.0 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 8, dictionary key #65 | prepared | Matcher::matches() | 491.9 | 1633.0 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 8, dictionary key #65 | oneshot | `str_contains()` loop | 260866.2 | 361615.7 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 8, dictionary key #65 | oneshot | `preg_match()` | 1875.3 | 7747.0 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 8, dictionary key #65 | oneshot | Matcher::matches() | 240537.7 | 817746.8 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 2042, dictionary key #65 | prepared | `str_contains()` loop | 281323.2 | 397787.8 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 2042, dictionary key #65 | prepared | `preg_match()` | 239644.7 | 1087021.1 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 2042, dictionary key #65 | prepared | Matcher::matches() | 9225.3 | 29108.0 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 2042, dictionary key #65 | oneshot | `str_contains()` loop | 281577.7 | 397786.9 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 2042, dictionary key #65 | oneshot | `preg_match()` | 239670.8 | 1087021.7 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 2042, dictionary key #65 | oneshot | Matcher::matches() | 256572.4 | 802103.1 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 2042, dictionary key #65 | prepared | `str_contains()` loop | 262033.5 | 364012.1 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 2042, dictionary key #65 | prepared | `preg_match()` | 238865.7 | 1086960.2 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 2042, dictionary key #65 | prepared | Matcher::matches() | 7806.9 | 32239.0 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 2042, dictionary key #65 | oneshot | `str_contains()` loop | 262051.3 | 364010.8 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 2042, dictionary key #65 | oneshot | `preg_match()` | 238940.3 | 1086957.9 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 2042, dictionary key #65 | oneshot | Matcher::matches() | 249491.6 | 848351.9 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 4076, dictionary key #65 | prepared | `str_contains()` loop | 283908.6 | 400840.8 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 4076, dictionary key #65 | prepared | `preg_match()` | 461319.2 | 2099738.2 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 4076, dictionary key #65 | prepared | Matcher::matches() | 17729.8 | 56063.0 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 4076, dictionary key #65 | oneshot | `str_contains()` loop | 284037.0 | 400839.6 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 4076, dictionary key #65 | oneshot | `preg_match()` | 461450.9 | 2099739.5 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 4076, dictionary key #65 | oneshot | Matcher::matches() | 274546.0 | 829061.0 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 4076, dictionary key #65 | prepared | `str_contains()` loop | 264243.3 | 366865.3 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 4076, dictionary key #65 | prepared | `preg_match()` | 460010.5 | 2099676.5 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 4076, dictionary key #65 | prepared | Matcher::matches() | 15525.1 | 62077.0 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 4076, dictionary key #65 | oneshot | `str_contains()` loop | 264380.3 | 366865.2 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 4076, dictionary key #65 | oneshot | `preg_match()` | 460411.2 | 2099676.0 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 4076, dictionary key #65 | oneshot | Matcher::matches() | 256512.4 | 878191.6 | checks passed |
| gcc15 | 16384 B; dictionary of 256 keys; key lengths 12 B; no matches | prepared | `str_contains()` loop | 4445485.7 | 5844433.5 | checks passed |
| gcc15 | 16384 B; dictionary of 256 keys; key lengths 12 B; no matches | prepared | `preg_match()` | 3243880.5 | 15391299.1 | checks passed |
| gcc15 | 16384 B; dictionary of 256 keys; key lengths 12 B; no matches | prepared | Matcher::matches() | 74879.3 | 215361.1 | checks passed |
| gcc15 | 16384 B; dictionary of 256 keys; key lengths 12 B; no matches | oneshot | `str_contains()` loop | 4444313.0 | 5844423.0 | checks passed |
| gcc15 | 16384 B; dictionary of 256 keys; key lengths 12 B; no matches | oneshot | `preg_match()` | 3472422.7 | 15391304.7 | checks passed |
| gcc15 | 16384 B; dictionary of 256 keys; key lengths 12 B; no matches | oneshot | Matcher::matches() | 952879.7 | 1688727.7 | checks passed |
| clang21 | 16384 B; dictionary of 256 keys; key lengths 12 B; no matches | prepared | `str_contains()` loop | 4159885.5 | 5430769.9 | checks passed |
| clang21 | 16384 B; dictionary of 256 keys; key lengths 12 B; no matches | prepared | `preg_match()` | 3218632.8 | 15391246.5 | checks passed |
| clang21 | 16384 B; dictionary of 256 keys; key lengths 12 B; no matches | prepared | Matcher::matches() | 59899.5 | 237568.5 | checks passed |
| clang21 | 16384 B; dictionary of 256 keys; key lengths 12 B; no matches | oneshot | `str_contains()` loop | 4163677.5 | 5430756.2 | checks passed |
| clang21 | 16384 B; dictionary of 256 keys; key lengths 12 B; no matches | oneshot | `preg_match()` | 3235246.8 | 15391242.3 | checks passed |
| clang21 | 16384 B; dictionary of 256 keys; key lengths 12 B; no matches | oneshot | Matcher::matches() | 963551.5 | 1790135.1 | checks passed |
| gcc15 | 32768 B; dictionary of 1024 keys; key lengths 12 B; no matches | prepared | `str_contains()` loop | 36266897.5 | 46729842.6 | checks passed |
| gcc15 | 32768 B; dictionary of 1024 keys; key lengths 12 B; no matches | prepared | `preg_match()` | 57095145.8 | 130502341.2 | checks passed |
| gcc15 | 32768 B; dictionary of 1024 keys; key lengths 12 B; no matches | prepared | Matcher::matches() | 364859.9 | 439280.2 | checks passed |
| gcc15 | 32768 B; dictionary of 1024 keys; key lengths 12 B; no matches | oneshot | `str_contains()` loop | 36293416.1 | 46730016.8 | checks passed |
| gcc15 | 32768 B; dictionary of 1024 keys; key lengths 12 B; no matches | oneshot | `preg_match()` | 58643692.3 | 130502486.5 | checks passed |
| gcc15 | 32768 B; dictionary of 1024 keys; key lengths 12 B; no matches | oneshot | Matcher::matches() | 3940340.4 | 5768129.2 | checks passed |
| clang21 | 32768 B; dictionary of 1024 keys; key lengths 12 B; no matches | prepared | `str_contains()` loop | 34066444.7 | 43552008.8 | checks passed |
| clang21 | 32768 B; dictionary of 1024 keys; key lengths 12 B; no matches | prepared | `preg_match()` | 56783222.5 | 130502304.7 | checks passed |
| clang21 | 32768 B; dictionary of 1024 keys; key lengths 12 B; no matches | prepared | Matcher::matches() | 348536.9 | 486843.7 | checks passed |
| clang21 | 32768 B; dictionary of 1024 keys; key lengths 12 B; no matches | oneshot | `str_contains()` loop | 34034226.6 | 43551938.3 | checks passed |
| clang21 | 32768 B; dictionary of 1024 keys; key lengths 12 B; no matches | oneshot | `preg_match()` | 53132335.8 | 130502243.3 | checks passed |
| clang21 | 32768 B; dictionary of 1024 keys; key lengths 12 B; no matches | oneshot | Matcher::matches() | 4050337.0 | 6045561.7 | checks passed |
| gcc15 | 65536 B; dictionary of 1024 keys; key lengths 12 B; no matches | prepared | `str_contains()` loop | 72488246.0 | 93142715.8 | checks passed |
| gcc15 | 65536 B; dictionary of 1024 keys; key lengths 12 B; no matches | prepared | `preg_match()` | 125024199.3 | 263885972.0 | checks passed |
| gcc15 | 65536 B; dictionary of 1024 keys; key lengths 12 B; no matches | prepared | Matcher::matches() | 835101.6 | 880117.3 | checks passed |
| gcc15 | 65536 B; dictionary of 1024 keys; key lengths 12 B; no matches | oneshot | `str_contains()` loop | 72514089.5 | 93142780.0 | checks passed |
| gcc15 | 65536 B; dictionary of 1024 keys; key lengths 12 B; no matches | oneshot | `preg_match()` | 91363991.7 | 263886315.3 | checks passed |
| gcc15 | 65536 B; dictionary of 1024 keys; key lengths 12 B; no matches | oneshot | Matcher::matches() | 4425172.5 | 6209182.2 | checks passed |
| clang21 | 65536 B; dictionary of 1024 keys; key lengths 12 B; no matches | prepared | `str_contains()` loop | 68000036.4 | 86931163.6 | checks passed |
| clang21 | 65536 B; dictionary of 1024 keys; key lengths 12 B; no matches | prepared | `preg_match()` | 114000972.3 | 263886232.7 | checks passed |
| clang21 | 65536 B; dictionary of 1024 keys; key lengths 12 B; no matches | prepared | Matcher::matches() | 813878.3 | 976244.3 | checks passed |
| clang21 | 65536 B; dictionary of 1024 keys; key lengths 12 B; no matches | oneshot | `str_contains()` loop | 68025746.4 | 86931127.4 | checks passed |
| clang21 | 65536 B; dictionary of 1024 keys; key lengths 12 B; no matches | oneshot | `preg_match()` | 112901444.7 | 263886418.7 | checks passed |
| clang21 | 65536 B; dictionary of 1024 keys; key lengths 12 B; no matches | oneshot | Matcher::matches() | 4509148.3 | 6535154.1 | checks passed |
| gcc15 | 65536 B; dictionary of 10000 keys; key lengths 12 B; no matches | prepared | `str_contains()` loop | — | — | Over 100 ms/call; elapsed observations retained |
| gcc15 | 65536 B; dictionary of 10000 keys; key lengths 12 B; no matches | prepared | `preg_match()` | — | — | Over 100 ms/call; elapsed observations retained |
| gcc15 | 65536 B; dictionary of 10000 keys; key lengths 12 B; no matches | prepared | Matcher::matches() | 836241.9 | 883068.4 | checks passed |
| gcc15 | 65536 B; dictionary of 10000 keys; key lengths 12 B; no matches | oneshot | `str_contains()` loop | — | — | Over 100 ms/call; elapsed observations retained |
| gcc15 | 65536 B; dictionary of 10000 keys; key lengths 12 B; no matches | oneshot | `preg_match()` | — | — | Over 100 ms/call; elapsed observations retained |
| gcc15 | 65536 B; dictionary of 10000 keys; key lengths 12 B; no matches | oneshot | Matcher::matches() | 67167720.8 | 51863752.8 | checks passed |
| clang21 | 65536 B; dictionary of 10000 keys; key lengths 12 B; no matches | prepared | `str_contains()` loop | — | — | Over 100 ms/call; elapsed observations retained |
| clang21 | 65536 B; dictionary of 10000 keys; key lengths 12 B; no matches | prepared | `preg_match()` | — | — | Over 100 ms/call; elapsed observations retained |
| clang21 | 65536 B; dictionary of 10000 keys; key lengths 12 B; no matches | prepared | Matcher::matches() | 815914.2 | 979475.5 | checks passed |
| clang21 | 65536 B; dictionary of 10000 keys; key lengths 12 B; no matches | oneshot | `str_contains()` loop | — | — | Over 100 ms/call; elapsed observations retained |
| clang21 | 65536 B; dictionary of 10000 keys; key lengths 12 B; no matches | oneshot | `preg_match()` | — | — | Over 100 ms/call; elapsed observations retained |
| clang21 | 65536 B; dictionary of 10000 keys; key lengths 12 B; no matches | oneshot | Matcher::matches() | 67616317.0 | 52870800.0 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 12 B; match: byte 4076, dictionary key #1 | prepared | `str_contains()` loop | 4689.9 | 7631.0 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 12 B; match: byte 4076, dictionary key #1 | prepared | `preg_match()` | 134465.9 | 465435.1 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 12 B; match: byte 4076, dictionary key #1 | prepared | Matcher::matches() | 17726.9 | 56063.1 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 12 B; match: byte 4076, dictionary key #1 | oneshot | `str_contains()` loop | 4690.1 | 7631.0 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 12 B; match: byte 4076, dictionary key #1 | oneshot | `preg_match()` | 134449.2 | 465435.1 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 12 B; match: byte 4076, dictionary key #1 | oneshot | Matcher::matches() | 73873.0 | 262807.1 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 12 B; match: byte 4076, dictionary key #1 | prepared | `str_contains()` loop | 4330.6 | 7055.0 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 12 B; match: byte 4076, dictionary key #1 | prepared | `preg_match()` | 129091.6 | 465373.8 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 12 B; match: byte 4076, dictionary key #1 | prepared | Matcher::matches() | 15519.4 | 62077.0 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 12 B; match: byte 4076, dictionary key #1 | oneshot | `str_contains()` loop | 4325.9 | 7055.0 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 12 B; match: byte 4076, dictionary key #1 | oneshot | `preg_match()` | 129104.7 | 465374.7 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 12 B; match: byte 4076, dictionary key #1 | oneshot | Matcher::matches() | 72302.5 | 281280.4 | checks passed |
| gcc15 | 4096 B; dictionary of 256 keys; key lengths 12 B; match: byte 4076, dictionary key #1 | prepared | `str_contains()` loop | 4690.8 | 7631.0 | checks passed |
| gcc15 | 4096 B; dictionary of 256 keys; key lengths 12 B; match: byte 4076, dictionary key #1 | prepared | `preg_match()` | 936670.7 | 4138234.2 | checks passed |
| gcc15 | 4096 B; dictionary of 256 keys; key lengths 12 B; match: byte 4076, dictionary key #1 | prepared | Matcher::matches() | 17735.5 | 56063.0 | checks passed |
| gcc15 | 4096 B; dictionary of 256 keys; key lengths 12 B; match: byte 4076, dictionary key #1 | oneshot | `str_contains()` loop | 4690.7 | 7631.0 | checks passed |
| gcc15 | 4096 B; dictionary of 256 keys; key lengths 12 B; match: byte 4076, dictionary key #1 | oneshot | `preg_match()` | 1028592.7 | 4138234.1 | checks passed |
| gcc15 | 4096 B; dictionary of 256 keys; key lengths 12 B; match: byte 4076, dictionary key #1 | oneshot | Matcher::matches() | 771128.9 | 1529629.1 | checks passed |
| clang21 | 4096 B; dictionary of 256 keys; key lengths 12 B; match: byte 4076, dictionary key #1 | prepared | `str_contains()` loop | 4333.5 | 7055.0 | checks passed |
| clang21 | 4096 B; dictionary of 256 keys; key lengths 12 B; match: byte 4076, dictionary key #1 | prepared | `preg_match()` | 868274.9 | 4138173.1 | checks passed |
| clang21 | 4096 B; dictionary of 256 keys; key lengths 12 B; match: byte 4076, dictionary key #1 | prepared | Matcher::matches() | 15538.9 | 62077.1 | checks passed |
| clang21 | 4096 B; dictionary of 256 keys; key lengths 12 B; match: byte 4076, dictionary key #1 | oneshot | `str_contains()` loop | 4330.0 | 7055.0 | checks passed |
| clang21 | 4096 B; dictionary of 256 keys; key lengths 12 B; match: byte 4076, dictionary key #1 | oneshot | `preg_match()` | 873526.5 | 4138174.5 | checks passed |
| clang21 | 4096 B; dictionary of 256 keys; key lengths 12 B; match: byte 4076, dictionary key #1 | oneshot | Matcher::matches() | 753071.4 | 1614910.2 | checks passed |
| gcc15 | 4096 B; dictionary of 10000 keys; key lengths 12 B; match: byte 8, dictionary key #1 | prepared | `str_contains()` loop | 546.0 | 1682.0 | checks passed |
| gcc15 | 4096 B; dictionary of 10000 keys; key lengths 12 B; match: byte 8, dictionary key #1 | prepared | `preg_match()` | 9357.3 | 23325.0 | checks passed |
| gcc15 | 4096 B; dictionary of 10000 keys; key lengths 12 B; match: byte 8, dictionary key #1 | prepared | Matcher::matches() | 551.2 | 1585.0 | checks passed |
| gcc15 | 4096 B; dictionary of 10000 keys; key lengths 12 B; match: byte 8, dictionary key #1 | oneshot | `str_contains()` loop | 545.0 | 1682.0 | checks passed |
| gcc15 | 4096 B; dictionary of 10000 keys; key lengths 12 B; match: byte 8, dictionary key #1 | oneshot | `preg_match()` | 9229.2 | 23325.0 | checks passed |
| gcc15 | 4096 B; dictionary of 10000 keys; key lengths 12 B; match: byte 8, dictionary key #1 | oneshot | Matcher::matches() | 65886912.2 | 50929177.0 | checks passed |
| clang21 | 4096 B; dictionary of 10000 keys; key lengths 12 B; match: byte 8, dictionary key #1 | prepared | `str_contains()` loop | 475.2 | 1489.0 | checks passed |
| clang21 | 4096 B; dictionary of 10000 keys; key lengths 12 B; match: byte 8, dictionary key #1 | prepared | `preg_match()` | 8419.2 | 23264.0 | checks passed |
| clang21 | 4096 B; dictionary of 10000 keys; key lengths 12 B; match: byte 8, dictionary key #1 | prepared | Matcher::matches() | 501.6 | 1639.0 | checks passed |
| clang21 | 4096 B; dictionary of 10000 keys; key lengths 12 B; match: byte 8, dictionary key #1 | oneshot | `str_contains()` loop | 476.9 | 1489.0 | checks passed |
| clang21 | 4096 B; dictionary of 10000 keys; key lengths 12 B; match: byte 8, dictionary key #1 | oneshot | `preg_match()` | 8409.4 | 23264.0 | checks passed |
| clang21 | 4096 B; dictionary of 10000 keys; key lengths 12 B; match: byte 8, dictionary key #1 | oneshot | Matcher::matches() | 66534602.0 | 51839753.6 | checks passed |
| gcc15 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 17647.9 | 58570.0 | checks passed |
| gcc15 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 22096.1 | 89952.0 | checks passed |
| gcc15 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::getMatchedKeywords() | 1104.8 | 3961.0 | checks passed |
| gcc15 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 17616.7 | 58577.1 | checks passed |
| gcc15 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 22058.2 | 89952.1 | checks passed |
| gcc15 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::getMatchedKeywords() | 246052.8 | 777637.5 | checks passed |
| clang21 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 19048.1 | 56098.0 | checks passed |
| clang21 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 21943.7 | 89772.1 | checks passed |
| clang21 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::getMatchedKeywords() | 962.1 | 4080.0 | checks passed |
| clang21 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 18131.4 | 56105.2 | checks passed |
| clang21 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 21935.2 | 89771.9 | checks passed |
| clang21 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::getMatchedKeywords() | 244200.3 | 820552.9 | checks passed |
| gcc15 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | `strpos()` loop | 1776671.5 | 4321644.5 | checks passed |
| gcc15 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | `preg_match_all()` | 2260409.2 | 4824797.1 | checks passed |
| gcc15 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | Matcher::getMatchedKeywords() | 1265.1 | 4232.0 | checks passed |
| gcc15 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | `strpos()` loop | 1778211.4 | 4321630.4 | checks passed |
| gcc15 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | `preg_match_all()` | 2257487.6 | 4824805.7 | checks passed |
| gcc15 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | Matcher::getMatchedKeywords() | 67068615.4 | 50935500.4 | checks passed |
| clang21 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | `strpos()` loop | 1792373.2 | 4133891.3 | checks passed |
| clang21 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | `preg_match_all()` | 2067452.7 | 4824596.9 | checks passed |
| clang21 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | Matcher::getMatchedKeywords() | 1155.1 | 4290.0 | checks passed |
| clang21 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | `strpos()` loop | 1792379.6 | 4133878.5 | checks passed |
| clang21 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | `preg_match_all()` | 2084264.1 | 4824613.8 | checks passed |
| clang21 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | Matcher::getMatchedKeywords() | 67520392.2 | 51846371.0 | checks passed |
| gcc15 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 1927903.3 | 4500055.7 | checks passed |
| gcc15 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 2476243.7 | 5505630.2 | checks passed |
| gcc15 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::getMatchedKeywords() | 1415.6 | 4709.0 | checks passed |
| gcc15 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 1927545.1 | 4500063.0 | checks passed |
| gcc15 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 2454459.9 | 5505631.8 | checks passed |
| gcc15 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::getMatchedKeywords() | 66132677.0 | 50933158.4 | checks passed |
| clang21 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 1987831.1 | 4306867.1 | checks passed |
| clang21 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 2310952.0 | 5505289.5 | checks passed |
| clang21 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::getMatchedKeywords() | 1302.0 | 4831.0 | checks passed |
| clang21 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 1986695.5 | 4306882.9 | checks passed |
| clang21 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 2328791.0 | 5505274.8 | checks passed |
| clang21 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::getMatchedKeywords() | 68171496.0 | 51844776.2 | checks passed |
| gcc15 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 151793.6 | 249078.1 | checks passed |
| gcc15 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 120663.8 | 543647.6 | checks passed |
| gcc15 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::getMatchedKeywords() | 5258.7 | 18520.0 | checks passed |
| gcc15 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 151871.6 | 249078.2 | checks passed |
| gcc15 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 120558.6 | 543647.1 | checks passed |
| gcc15 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::getMatchedKeywords() | 250465.1 | 792194.5 | checks passed |
| clang21 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 141657.1 | 218150.1 | checks passed |
| clang21 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 120732.5 | 543467.6 | checks passed |
| clang21 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::getMatchedKeywords() | 4141.9 | 19435.0 | checks passed |
| clang21 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 141707.0 | 218151.9 | checks passed |
| clang21 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 120641.7 | 543466.4 | checks passed |
| clang21 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::getMatchedKeywords() | 246867.4 | 835907.9 | checks passed |
| gcc15 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 32922.8 | 49970.0 | checks passed |
| gcc15 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 41487.9 | 175849.9 | checks passed |
| gcc15 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::getMatchedKeywords() | 19937.4 | 68974.0 | checks passed |
| gcc15 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 32925.1 | 49970.1 | checks passed |
| gcc15 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 41771.4 | 175849.9 | checks passed |
| gcc15 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::getMatchedKeywords() | 35139.5 | 127452.1 | checks passed |
| clang21 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 30665.5 | 45937.0 | checks passed |
| clang21 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 40591.0 | 175742.1 | checks passed |
| clang21 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::getMatchedKeywords() | 15790.1 | 72873.0 | checks passed |
| clang21 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 30637.0 | 45937.0 | checks passed |
| clang21 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 40571.5 | 175742.0 | checks passed |
| clang21 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::getMatchedKeywords() | 30637.1 | 134987.1 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | `strpos()` loop | 565386.7 | 794819.3 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | `preg_match_all()` | 464844.9 | 2159335.3 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | Matcher::getMatchedKeywords() | 19784.6 | 68569.0 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | `strpos()` loop | 565247.3 | 794822.7 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | `preg_match_all()` | 464502.4 | 2159335.4 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | Matcher::getMatchedKeywords() | 272235.9 | 840022.6 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | `strpos()` loop | 528956.1 | 728040.0 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | `preg_match_all()` | 465357.7 | 2159264.3 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | Matcher::getMatchedKeywords() | 16110.4 | 72420.0 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | `strpos()` loop | 528861.1 | 728040.0 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | `preg_match_all()` | 465626.1 | 2159266.3 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | Matcher::getMatchedKeywords() | 259837.5 | 886690.9 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 563956.6 | 793298.0 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 471074.2 | 2177006.9 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::getMatchedKeywords() | 19949.6 | 68989.0 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 563966.9 | 793293.3 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 470974.6 | 2177010.1 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::getMatchedKeywords() | 275083.6 | 840442.6 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 527981.5 | 726730.6 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 472079.1† | 2176827.8† | † |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::getMatchedKeywords() | 15824.4 | 72885.0 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 528035.9 | 726729.9 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 472311.6 | 2176829.1 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::getMatchedKeywords() | 263995.8 | 887156.0 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | prepared | `strpos()` loop | 561543.0 | 794307.6 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | prepared | `preg_match_all()` | 488817.8 | 2234369.7 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | prepared | Matcher::getMatchedKeywords() | 20358.6 | 70109.0 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | oneshot | `strpos()` loop | 561764.0 | 794309.4 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | oneshot | `preg_match_all()` | 488503.7 | 2234369.1 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | oneshot | Matcher::getMatchedKeywords() | 274590.4 | 841562.7 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | prepared | `strpos()` loop | 525202.0 | 728399.0 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | prepared | `preg_match_all()` | 490422.8 | 2234236.0 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | prepared | Matcher::getMatchedKeywords() | 16200.7 | 74178.1 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | oneshot | `strpos()` loop | 525040.5 | 728400.8 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | oneshot | `preg_match_all()` | 490016.8 | 2234237.7 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | oneshot | Matcher::getMatchedKeywords() | 270540.1 | 888450.7 | checks passed |
| gcc15 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 45643802.1 | 61907511.6 | checks passed |
| gcc15 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 65161038.6 | 162328580.2 | checks passed |
| gcc15 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::getMatchedKeywords() | 20546.2 | 69871.8 | checks passed |
| gcc15 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 45593784.0 | 61907675.7 | checks passed |
| gcc15 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 62837990.4 | 162328768.2 | checks passed |
| gcc15 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::getMatchedKeywords() | 67594431.8 | 50997460.8 | checks passed |
| clang21 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 42888389.0 | 56703768.1 | checks passed |
| clang21 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 63563725.8 | 162328518.2 | checks passed |
| clang21 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::getMatchedKeywords() | 16556.0 | 73795.0 | checks passed |
| clang21 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 42913985.3 | 56703826.1 | checks passed |
| clang21 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 63694464.8 | 162328542.6 | checks passed |
| clang21 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::getMatchedKeywords() | 67437269.2 | 51912943.8 | checks passed |
| gcc15 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 2200556.1 | 2924441.8 | checks passed |
| gcc15 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 1727654.2 | 8031124.6 | checks passed |
| gcc15 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::getMatchedKeywords() | 81433.5 | 265198.2 | checks passed |
| gcc15 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 2200770.8 | 2924444.2 | checks passed |
| gcc15 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 1728942.9 | 8031113.8 | checks passed |
| gcc15 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::getMatchedKeywords() | 511532.4 | 1036896.2 | checks passed |
| clang21 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 2059281.1 | 2718057.2 | checks passed |
| clang21 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 1732073.6 | 8030939.8 | checks passed |
| clang21 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::getMatchedKeywords() | 156643.6 | 278474.0 | checks passed |
| clang21 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 2058826.5 | 2718042.0 | checks passed |
| clang21 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 1733089.0 | 8030941.2 | checks passed |
| clang21 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::getMatchedKeywords() | 477997.8 | 1092991.3 | checks passed |
| gcc15 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 4464705.0 | 5811089.2 | checks passed |
| gcc15 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 3662843.8 | 17101924.7 | checks passed |
| gcc15 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::getMatchedKeywords() | 386810.7 | 537487.0 | checks passed |
| gcc15 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 4465389.0 | 5811116.2 | checks passed |
| gcc15 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 3663136.4 | 17101945.8 | checks passed |
| gcc15 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::getMatchedKeywords() | 777679.6 | 1311234.5 | checks passed |
| clang21 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 4183825.3 | 5415840.4 | checks passed |
| clang21 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 3670895.2 | 17101724.9 | checks passed |
| clang21 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::getMatchedKeywords() | 407635.0 | 568014.5 | checks passed |
| clang21 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 4184413.9 | 5415834.8 | checks passed |
| clang21 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 3671094.1 | 17101729.9 | checks passed |
| clang21 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::getMatchedKeywords() | 765543.8 | 1384557.6 | checks passed |
| gcc15 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 16; unique matched keys: 8 | prepared | `strpos()` loop | 143189.5 | 208299.9 | checks passed |
| gcc15 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 16; unique matched keys: 8 | prepared | `preg_match_all()` | 935990.6 | 2703729.1 | checks passed |
| gcc15 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 16; unique matched keys: 8 | prepared | Matcher::getMatchedKeywords() | 740324.4 | 857857.4 | checks passed |
| gcc15 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 16; unique matched keys: 8 | oneshot | `strpos()` loop | 143243.2 | 208299.1 | checks passed |
| gcc15 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 16; unique matched keys: 8 | oneshot | `preg_match_all()` | 935264.3 | 2703726.1 | checks passed |
| gcc15 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 16; unique matched keys: 8 | oneshot | Matcher::getMatchedKeywords() | 760619.0 | 916334.0 | checks passed |
| clang21 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 16; unique matched keys: 8 | prepared | `strpos()` loop | 134169.9 | 196054.5 | checks passed |
| clang21 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 16; unique matched keys: 8 | prepared | `preg_match_all()` | 946569.7 | 2704298.0 | checks passed |
| clang21 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 16; unique matched keys: 8 | prepared | Matcher::getMatchedKeywords() | 619968.3 | 907093.4 | checks passed |
| clang21 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 16; unique matched keys: 8 | oneshot | `strpos()` loop | 134055.1 | 196052.9 | checks passed |
| clang21 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 16; unique matched keys: 8 | oneshot | `preg_match_all()` | 945999.5 | 2704303.5 | checks passed |
| clang21 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 16; unique matched keys: 8 | oneshot | Matcher::getMatchedKeywords() | 638056.6 | 969209.3 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 8934300.8 | 11571098.8 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 7395891.4 | 34545422.5 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::getMatchedKeywords() | 881170.9 | 1076181.6 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 8937468.1 | 11571073.4 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 7395691.7 | 34545427.2 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::getMatchedKeywords() | 1269115.8 | 1849981.8 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 8369687.9 | 10798540.0 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 7409922.1 | 34545202.3 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::getMatchedKeywords() | 805024.3 | 1138591.0 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 8370620.5 | 10798617.6 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 7417437.6 | 34545240.6 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::getMatchedKeywords() | 1206870.1 | 1955199.0 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | prepared | `strpos()` loop | 564759.8 | 794345.8 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | prepared | `preg_match_all()` | 477633.8 | 2196041.8 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | prepared | Matcher::getMatchedKeywords() | 20093.3 | 69352.1 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | oneshot | `strpos()` loop | 564581.1 | 794343.5 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | oneshot | `preg_match_all()` | 477473.0 | 2196042.7 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | oneshot | Matcher::getMatchedKeywords() | 273368.1 | 840824.0 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | prepared | `strpos()` loop | 527436.6 | 727723.7 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | prepared | `preg_match_all()` | 478388.9 | 2196495.5 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | prepared | Matcher::getMatchedKeywords() | 15972.7 | 73397.9 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | oneshot | `strpos()` loop | 527368.7 | 727724.0 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | oneshot | `preg_match_all()` | 478291.9 | 2196495.0 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | oneshot | Matcher::getMatchedKeywords() | 262727.3 | 887687.5 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | prepared | `strpos()` loop | 8755274.6 | 11326979.2 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | prepared | `preg_match_all()` | 7765056.1 | 35782188.4 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | prepared | Matcher::getMatchedKeywords() | 881444.6 | 1085334.3 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | oneshot | `strpos()` loop | 8759952.5 | 11326975.7 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | oneshot | `preg_match_all()` | 7761010.1 | 35782200.0 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | oneshot | Matcher::getMatchedKeywords() | 1270155.6 | 1858824.1 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | prepared | `strpos()` loop | 8211215.6 | 10571633.7 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | prepared | `preg_match_all()` | 7788706.1 | 35779173.2 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | prepared | Matcher::getMatchedKeywords() | 812465.3 | 1151191.8 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | oneshot | `strpos()` loop | 8211524.4 | 10571706.0 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | oneshot | `preg_match_all()` | 7790409.0 | 35779185.2 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | oneshot | Matcher::getMatchedKeywords() | 1211390.4 | 1967509.0 | checks passed |
| gcc15 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 19832.3 | 63998.0 | checks passed |
| gcc15 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 19661.0 | 82674.0 | checks passed |
| gcc15 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::countMatches() | 1001.3 | 3017.0 | checks passed |
| gcc15 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 20367.9 | 64005.0 | checks passed |
| gcc15 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 19630.7 | 82674.0 | checks passed |
| gcc15 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::countMatches() | 245643.7 | 776690.3 | checks passed |
| clang21 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 20473.8 | 60014.0 | checks passed |
| clang21 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 19436.3 | 82367.0 | checks passed |
| clang21 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::countMatches() | 791.1 | 3010.0 | checks passed |
| clang21 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 20041.5 | 60021.0 | checks passed |
| clang21 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 19474.0 | 82367.1 | checks passed |
| clang21 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::countMatches() | 243359.6 | 819483.2 | checks passed |
| gcc15 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | `strpos()` loop | 1927052.2 | 4880950.6 | checks passed |
| gcc15 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | `preg_match_all()` | 1942179.0 | 4795310.9 | checks passed |
| gcc15 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | Matcher::countMatches() | 977.5 | 2874.0 | checks passed |
| gcc15 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | `strpos()` loop | 1943714.9 | 4880950.1 | checks passed |
| gcc15 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | `preg_match_all()` | 1831463.9 | 4795318.7 | checks passed |
| gcc15 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | Matcher::countMatches() | 67081219.4 | 50931318.4 | checks passed |
| clang21 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | `strpos()` loop | 1907123.7 | 4571528.1 | checks passed |
| clang21 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | `preg_match_all()` | 2146475.7 | 4795850.7 | checks passed |
| clang21 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | Matcher::countMatches() | 725.7 | 2829.0 | checks passed |
| clang21 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | `strpos()` loop | 1911000.2 | 4571526.7 | checks passed |
| clang21 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | `preg_match_all()` | 2090825.1 | 4795849.7 | checks passed |
| clang21 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | Matcher::countMatches() | 68191334.2 | 51842876.2 | checks passed |
| gcc15 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 153442.7 | 255637.7 | checks passed |
| gcc15 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 118581.7 | 528332.3 | checks passed |
| gcc15 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::countMatches() | 5732.4 | 14888.0 | checks passed |
| gcc15 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 154189.9 | 255637.2 | checks passed |
| gcc15 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 118442.3 | 528332.1 | checks passed |
| gcc15 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::countMatches() | 252183.1 | 788562.0 | checks passed |
| clang21 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 142720.1 | 222574.9 | checks passed |
| clang21 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 118192.3 | 528025.0 | checks passed |
| clang21 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::countMatches() | 4007.1 | 14831.0 | checks passed |
| clang21 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 142624.1 | 222574.2 | checks passed |
| clang21 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 118280.0 | 528024.9 | checks passed |
| clang21 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::countMatches() | 246319.9 | 831304.4 | checks passed |
| gcc15 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 34646.2 | 51716.2 | checks passed |
| gcc15 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 33335.7 | 150363.0 | checks passed |
| gcc15 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::countMatches() | 22086.3 | 56141.1 | checks passed |
| gcc15 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 34667.2 | 51716.0 | checks passed |
| gcc15 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 33501.2 | 150362.9 | checks passed |
| gcc15 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::countMatches() | 37324.9 | 114618.9 | checks passed |
| clang21 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 32170.3 | 47183.1 | checks passed |
| clang21 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 34278.1 | 150320.1 | checks passed |
| clang21 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::countMatches() | 15523.4 | 56039.0 | checks passed |
| clang21 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 32134.2 | 47183.1 | checks passed |
| clang21 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 34179.0 | 150320.0 | checks passed |
| clang21 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::countMatches() | 30368.3 | 118153.1 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | `strpos()` loop | 566678.6 | 801436.8 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | `preg_match_all()` | 463362.5 | 2120159.2 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | Matcher::countMatches() | 22049.3 | 56055.1 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | `strpos()` loop | 566706.0 | 801439.7 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | `preg_match_all()` | 462878.2 | 2120159.1 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | Matcher::countMatches() | 310419.6 | 827508.5 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | `strpos()` loop | 529352.1 | 732598.6 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | `preg_match_all()` | 463047.3 | 2120103.4 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | Matcher::countMatches() | 16063.3 | 55924.0 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | `strpos()` loop | 529122.8 | 732598.7 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | `preg_match_all()` | 462686.8 | 2120106.2 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | Matcher::countMatches() | 263690.1 | 870194.5 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 568060.8 | 801831.0 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 468186.2 | 2132946.5 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::countMatches() | 22090.6 | 56141.0 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 567419.8 | 801836.0 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 467845.5 | 2132946.2 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::countMatches() | 311441.3 | 827596.3 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 529517.0 | 732855.1 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 468116.0 | 2132639.2 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::countMatches() | 15527.0 | 56039.0 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 529606.3 | 732854.9 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 468131.5 | 2132639.9 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::countMatches() | 263096.2 | 870308.7 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | prepared | `strpos()` loop | 568585.9 | 805167.0 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | prepared | `preg_match_all()` | 483539.4 | 2176581.8 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | prepared | Matcher::countMatches() | 22097.2 | 56474.0 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | oneshot | `strpos()` loop | 568882.3 | 805166.6 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | oneshot | `preg_match_all()` | 482514.9 | 2176583.9 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | oneshot | Matcher::countMatches() | 312098.5 | 827927.9 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | prepared | `strpos()` loop | 530235.7 | 735615.7 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | prepared | `preg_match_all()` | 481689.4 | 2175626.1 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | prepared | Matcher::countMatches() | 15690.2 | 56472.0 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | oneshot | `strpos()` loop | 530290.3 | 735613.9 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | oneshot | `preg_match_all()` | 481749.1 | 2175629.1 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | oneshot | Matcher::countMatches() | 265530.8 | 870743.5 | checks passed |
| gcc15 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 45795040.1 | 62478708.9 | checks passed |
| gcc15 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 55997258.0 | 161553167.2 | checks passed |
| gcc15 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::countMatches() | 22117.7 | 56277.0 | checks passed |
| gcc15 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 45752870.6 | 62478958.9 | checks passed |
| gcc15 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 57589088.6 | 161553084.0 | checks passed |
| gcc15 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::countMatches() | 66546533.0 | 50983795.6 | checks passed |
| clang21 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 42959662.0 | 57114746.1 | checks passed |
| clang21 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 66184786.4 | 161552856.2 | checks passed |
| clang21 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::countMatches() | 15731.1 | 56198.0 | checks passed |
| clang21 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 42949645.7 | 57114607.4 | checks passed |
| clang21 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 65636218.0 | 161553007.8 | checks passed |
| clang21 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::countMatches() | 68139029.4† | 51895157.6† | † |
| gcc15 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 2204168.1 | 2933983.9 | checks passed |
| gcc15 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 1725025.0 | 7884114.0 | checks passed |
| gcc15 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::countMatches() | 179684.7 | 215486.0 | checks passed |
| gcc15 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 2205408.0 | 2933972.8 | checks passed |
| gcc15 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 1726036.3 | 7884128.7 | checks passed |
| gcc15 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::countMatches() | 545926.1 | 987182.8 | checks passed |
| clang21 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 2063035.1† | 2725110.3† | † |
| clang21 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 1725984.0 | 7883825.0 | checks passed |
| clang21 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::countMatches() | 159657.3 | 213930.1 | checks passed |
| clang21 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 2062636.2† | 2725110.5† | † |
| clang21 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 1725024.5† | 7883823.9† | † |
| clang21 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::countMatches() | 531798.4 | 1028447.2 | checks passed |
| gcc15 | 32768 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 271855.3 | 367028.6 | checks passed |
| gcc15 | 32768 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 424236.6 | 1151251.6 | checks passed |
| gcc15 | 32768 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::countMatches() | 450727.7 | 438622.8 | checks passed |
| gcc15 | 32768 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 271984.9 | 367029.2 | checks passed |
| gcc15 | 32768 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 424383.1 | 1151251.9 | checks passed |
| gcc15 | 32768 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::countMatches() | 469163.7 | 497101.4 | checks passed |
| clang21 | 32768 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 255130.8† | 341793.6† | † |
| clang21 | 32768 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 429173.6† | 1151210.1† | † |
| clang21 | 32768 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::countMatches() | 412133.5† | 437501.9† | † |
| clang21 | 32768 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 253846.2† | 341792.5† | † |
| clang21 | 32768 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 429841.7† | 1151210.8† | † |
| clang21 | 32768 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::countMatches() | 430593.2 | 499615.1 | checks passed |
| gcc15 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 4489813.1 | 5846310.5 | checks passed |
| gcc15 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 3653969.5 | 16795167.6 | checks passed |
| gcc15 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::countMatches() | 450581.9 | 438621.6 | checks passed |
| gcc15 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 4490189.0 | 5846316.0 | checks passed |
| gcc15 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 3652756.3 | 16795152.6 | checks passed |
| gcc15 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::countMatches() | 799066.2 | 1212370.6 | checks passed |
| clang21 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 4210137.3† | 5446942.3† | † |
| clang21 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 3651953.9 | 16794862.7 | checks passed |
| clang21 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::countMatches() | 406525.0† | 437500.8† | † |
| clang21 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 4212955.6† | 5446926.1† | † |
| clang21 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 3652190.8† | 16794853.5† | † |
| clang21 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::countMatches() | 772924.2 | 1254038.3 | checks passed |
| gcc15 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 546141.6 | 727290.1 | checks passed |
| gcc15 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 869024.1 | 2301947.6 | checks passed |
| gcc15 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::countMatches() | 934953.2 | 879010.4 | checks passed |
| gcc15 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 546059.9 | 727288.5 | checks passed |
| gcc15 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 870529.0 | 2301951.1 | checks passed |
| gcc15 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::countMatches() | 953437.0 | 937493.4 | checks passed |
| clang21 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 510455.8 | 678448.9 | checks passed |
| clang21 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 881868.1 | 2301909.8 | checks passed |
| clang21 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::countMatches() | 800979.4 | 877446.9 | checks passed |
| clang21 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 510535.2 | 678447.8 | checks passed |
| clang21 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 882705.3 | 2301904.2 | checks passed |
| clang21 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::countMatches() | 824285.3 | 939565.1 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 8976505.2 | 11630232.4 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 7378130.7 | 33931537.8 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::countMatches() | 935780.4 | 879017.1 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 8978205.0 | 11630227.3 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 7378779.6 | 33931632.1 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::countMatches() | 1283194.2 | 1652820.3 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 8417832.0 | 10852109.6 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 7385026.2 | 33931297.4 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::countMatches() | 799910.7 | 877450.2 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 8416305.8 | 10852110.1 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 7367680.1 | 33931240.3 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::countMatches() | 1204874.7 | 1694059.2 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | prepared | `strpos()` loop | 569226.8 | 805341.3 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | prepared | `preg_match_all()` | 471471.9 | 2145668.8 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | prepared | Matcher::countMatches() | 22133.7 | 56473.8 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | oneshot | `strpos()` loop | 568952.1 | 805342.0 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | oneshot | `preg_match_all()` | 471665.0 | 2145663.2 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | oneshot | Matcher::countMatches() | 308638.9 | 827946.6 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | prepared | `strpos()` loop | 530015.7 | 735777.0 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | prepared | `preg_match_all()` | 471780.7 | 2146226.8 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | prepared | Matcher::countMatches() | 15671.7 | 56472.0 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | oneshot | `strpos()` loop | 530473.2 | 735777.5 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | oneshot | `preg_match_all()` | 471875.6 | 2146227.6 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | oneshot | Matcher::countMatches() | 265427.9 | 870759.8 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | prepared | `strpos()` loop | 9021839.0 | 11701630.9 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | prepared | `preg_match_all()` | 7701997.3 | 34932428.2 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | prepared | Matcher::countMatches() | 934176.3 | 886777.0 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | oneshot | `strpos()` loop | 9023054.0 | 11701592.7 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | oneshot | `preg_match_all()` | 7692355.6 | 34932421.2 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | oneshot | Matcher::countMatches() | 1285721.3 | 1660266.3 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | prepared | `strpos()` loop | 8465239.4 | 10911726.4 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | prepared | `preg_match_all()` | 7695682.9 | 34917941.9 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | prepared | Matcher::countMatches() | 805771.2 | 887445.6 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | oneshot | `strpos()` loop | 8463347.6 | 10911661.4 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | oneshot | `preg_match_all()` | 7705036.1 | 34917936.4 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | oneshot | Matcher::countMatches() | 1207741.5 | 1703760.0 | checks passed |
| gcc15 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 20694.2 | 65758.1 | checks passed |
| gcc15 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 21632.4 | 88918.0 | checks passed |
| gcc15 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::matchAll() | 1221.8 | 3737.0 | checks passed |
| gcc15 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 20789.3 | 65764.9 | checks passed |
| gcc15 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 21611.0 | 88918.0 | checks passed |
| gcc15 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::matchAll() | 247091.9 | 777410.6 | checks passed |
| clang21 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 20674.5 | 61744.1 | checks passed |
| clang21 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 21452.0 | 88723.0 | checks passed |
| clang21 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::matchAll() | 1088.7 | 4207.0 | checks passed |
| clang21 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 20997.6 | 61751.0 | checks passed |
| clang21 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 21469.7 | 88723.0 | checks passed |
| clang21 | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::matchAll() | 242895.9 | 820680.7 | checks passed |
| gcc15 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | `strpos()` loop | 1932439.9 | 4881543.4 | checks passed |
| gcc15 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | `preg_match_all()` | 2193466.4 | 4824550.3 | checks passed |
| gcc15 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | Matcher::matchAll() | 967.0 | 2964.0 | checks passed |
| gcc15 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | `strpos()` loop | 1928507.9 | 4881502.8 | checks passed |
| gcc15 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | `preg_match_all()` | 2214607.2 | 4824553.2 | checks passed |
| gcc15 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | Matcher::matchAll() | 66371418.6 | 50931723.0 | checks passed |
| clang21 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | `strpos()` loop | 1907900.3 | 4572076.7 | checks passed |
| clang21 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | `preg_match_all()` | 2031557.7 | 4824339.4 | checks passed |
| clang21 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | Matcher::matchAll() | 839.6 | 3325.0 | checks passed |
| clang21 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | `strpos()` loop | 1908679.8 | 4572066.1 | checks passed |
| clang21 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | `preg_match_all()` | 2044644.8 | 4824337.4 | checks passed |
| clang21 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | Matcher::matchAll() | 66733342.2 | 51843517.8 | checks passed |
| gcc15 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 2122071.5 | 5060086.0 | checks passed |
| gcc15 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 2463457.0 | 5504609.0 | checks passed |
| gcc15 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::matchAll() | 1225.5 | 3737.0 | checks passed |
| gcc15 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 2121201.9 | 5060082.8 | checks passed |
| gcc15 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 2505450.5 | 5504626.2 | checks passed |
| gcc15 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::matchAll() | 66608516.8 | 50932494.8 | checks passed |
| clang21 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 2092943.9 | 4746346.6 | checks passed |
| clang21 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 2307627.7 | 5504228.9 | checks passed |
| clang21 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::matchAll() | 1084.6 | 4207.0 | checks passed |
| clang21 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 2085164.9 | 4746361.5 | checks passed |
| clang21 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 2298086.7 | 5504227.2 | checks passed |
| clang21 | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::matchAll() | 66958560.0 | 51844234.8 | checks passed |
| gcc15 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 153816.0 | 257397.1 | checks passed |
| gcc15 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 120180.3 | 542613.1 | checks passed |
| gcc15 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::matchAll() | 5798.3 | 15608.0 | checks passed |
| gcc15 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 153979.1 | 257396.4 | checks passed |
| gcc15 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 120136.2 | 542613.1 | checks passed |
| gcc15 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::matchAll() | 250555.5 | 789282.0 | checks passed |
| clang21 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 143256.5 | 224305.2 | checks passed |
| clang21 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 120177.5 | 542417.9 | checks passed |
| clang21 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::matchAll() | 4335.5 | 18989.0 | checks passed |
| clang21 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 143296.1 | 224303.8 | checks passed |
| clang21 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 120235.1 | 542417.8 | checks passed |
| clang21 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::matchAll() | 247640.2 | 835462.0 | checks passed |
| gcc15 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 35311.7 | 53476.0 | checks passed |
| gcc15 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 41160.1 | 174816.0 | checks passed |
| gcc15 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::matchAll() | 22039.2 | 56861.0 | checks passed |
| gcc15 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 35282.1 | 53476.0 | checks passed |
| gcc15 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 41226.1 | 174815.9 | checks passed |
| gcc15 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::matchAll() | 37153.3 | 115339.3 | checks passed |
| clang21 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 32751.3 | 48913.1 | checks passed |
| clang21 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 40178.9 | 174693.0 | checks passed |
| clang21 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::matchAll() | 16834.1 | 70788.1 | checks passed |
| clang21 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 32743.1 | 48913.2 | checks passed |
| clang21 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 40172.4 | 174693.1 | checks passed |
| clang21 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::matchAll() | 31679.5 | 132902.1 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | `strpos()` loop | 567163.2 | 801981.8 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | `preg_match_all()` | 464418.6 | 2159088.9 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | Matcher::matchAll() | 21786.3 | 56145.0 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | `strpos()` loop | 566937.6 | 801982.7 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | `preg_match_all()` | 464351.9 | 2159087.9 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | Matcher::matchAll() | 276436.5 | 827598.9 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | `strpos()` loop | 528671.3 | 733138.6 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | `preg_match_all()` | 465418.9 | 2159001.3 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | Matcher::matchAll() | 15534.9 | 70007.0 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | `strpos()` loop | 528560.3 | 733142.7 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | `preg_match_all()` | 465974.6 | 2159000.8 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | Matcher::matchAll() | 257578.7 | 884277.8 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 568272.6 | 803591.1 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 470780.7 | 2175973.9 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::matchAll() | 22058.8 | 56861.0 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 568261.4 | 803591.9 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 470557.2 | 2175973.7 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::matchAll() | 274133.5 | 828315.9 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 530162.1 | 734584.6 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 471458.9 | 2175779.4 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::matchAll() | 16403.1 | 70788.0 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 530144.8 | 734584.8 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 471472.1 | 2175779.4 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::matchAll() | 265443.7 | 885058.6 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | prepared | `strpos()` loop | 571231.7 | 812727.6 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | prepared | `preg_match_all()` | 487632.7 | 2232303.7 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | prepared | Matcher::matchAll() | 22661.7 | 58857.0 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | oneshot | `strpos()` loop | 571189.9 | 812727.3 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | oneshot | `preg_match_all()` | 487793.7 | 2232303.4 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | oneshot | Matcher::matchAll() | 274819.4 | 830310.9 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | prepared | `strpos()` loop | 532739.3 | 743335.4 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | prepared | `preg_match_all()` | 489022.0 | 2232059.3 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | prepared | Matcher::matchAll() | 17508.8 | 73055.1 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | oneshot | `strpos()` loop | 532608.4 | 743334.4 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | oneshot | `preg_match_all()` | 489223.9 | 2232062.9 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | oneshot | Matcher::matchAll() | 270168.1 | 887326.4 | checks passed |
| gcc15 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 45859412.0 | 62480564.1 | checks passed |
| gcc15 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 56951408.2 | 162327706.8 | checks passed |
| gcc15 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::matchAll() | 22300.6 | 56996.0 | checks passed |
| gcc15 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 45800189.7 | 62480263.7 | checks passed |
| gcc15 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 65573003.8 | 162328009.8 | checks passed |
| gcc15 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::matchAll() | 66581802.2 | 50984379.8 | checks passed |
| clang21 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 42947534.3 | 57116446.6 | checks passed |
| clang21 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 62733896.6 | 162327419.6 | checks passed |
| clang21 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::matchAll() | 17266.1 | 70946.0 | checks passed |
| clang21 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 42939450.6 | 57116614.6 | checks passed |
| clang21 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 65299952.8 | 162327447.4 | checks passed |
| clang21 | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::matchAll() | 66605001.0 | 51909940.0 | checks passed |
| gcc15 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 2205035.0 | 2935730.2 | checks passed |
| gcc15 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 1726978.2 | 8030077.7 | checks passed |
| gcc15 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::matchAll() | 88561.8 | 216206.1 | checks passed |
| gcc15 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 2205964.9 | 2935739.6 | checks passed |
| gcc15 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 1727715.9 | 8030077.0 | checks passed |
| gcc15 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::matchAll() | 521098.2 | 987902.6 | checks passed |
| clang21 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 2062658.9 | 2726849.7 | checks passed |
| clang21 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 1733435.2 | 8029892.7 | checks passed |
| clang21 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::matchAll() | 66366.9 | 266598.1 | checks passed |
| clang21 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 2062594.5 | 2726843.5 | checks passed |
| clang21 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 1733235.1 | 8029879.2 | checks passed |
| clang21 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::matchAll() | 502471.8 | 1081114.9 | checks passed |
| gcc15 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 4489755.5 | 5848063.5 | checks passed |
| gcc15 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 3660038.9 | 17100878.6 | checks passed |
| gcc15 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::matchAll() | 388940.8 | 439343.0 | checks passed |
| gcc15 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 4489901.3 | 5848083.2 | checks passed |
| gcc15 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 3659971.4 | 17100873.6 | checks passed |
| gcc15 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::matchAll() | 789612.7 | 1213093.3 | checks passed |
| clang21 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 4209450.7 | 5448628.3 | checks passed |
| clang21 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 3671228.3 | 17100683.6 | checks passed |
| clang21 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::matchAll() | 355803.1 | 549034.3 | checks passed |
| clang21 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 4212765.1 | 5448657.1 | checks passed |
| clang21 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 3669763.1 | 17100686.5 | checks passed |
| clang21 | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::matchAll() | 773762.8 | 1365571.6 | checks passed |
| gcc15 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | `strpos()` loop | 546061.3 | 727191.1 | checks passed |
| gcc15 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | `preg_match_all()` | 905382.1 | 2620185.8 | checks passed |
| gcc15 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | Matcher::matchAll() | 901189.2 | 878998.0 | checks passed |
| gcc15 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | `strpos()` loop | 546099.6 | 727186.0 | checks passed |
| gcc15 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | `preg_match_all()` | 905155.9 | 2620183.5 | checks passed |
| gcc15 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | Matcher::matchAll() | 923849.3 | 937474.7 | checks passed |
| clang21 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | `strpos()` loop | 510549.7 | 678510.6 | checks passed |
| clang21 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | `preg_match_all()` | 916209.6 | 2620094.7 | checks passed |
| clang21 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | prepared | Matcher::matchAll() | 835394.5 | 1101312.6 | checks passed |
| clang21 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | `strpos()` loop | 510461.3 | 678510.8 | checks passed |
| clang21 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | `preg_match_all()` | 915481.2 | 2620091.9 | checks passed |
| clang21 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | oneshot | Matcher::matchAll() | 856362.6 | 1163424.4 | checks passed |
| gcc15 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 546609.7 | 729050.9 | checks passed |
| gcc15 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 907713.6 | 2625287.6 | checks passed |
| gcc15 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::matchAll() | 901687.2 | 879734.5 | checks passed |
| gcc15 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 546657.7 | 729049.0 | checks passed |
| gcc15 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 907822.1 | 2625291.5 | checks passed |
| gcc15 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::matchAll() | 924647.3 | 938210.8 | checks passed |
| clang21 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 510746.8 | 680176.4 | checks passed |
| clang21 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 917604.0 | 2625169.2 | checks passed |
| clang21 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::matchAll() | 859587.7 | 1102123.1 | checks passed |
| clang21 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 510931.5 | 680173.2 | checks passed |
| clang21 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 916524.6 | 2625166.7 | checks passed |
| clang21 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::matchAll() | 879709.5 | 1164236.2 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 8979188.7 | 11631994.4 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 7392522.8 | 34544382.9 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::matchAll() | 901953.1 | 879741.6 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 8979001.8 | 11631992.1 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 7396878.8 | 34544336.1 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::matchAll() | 1295632.3 | 1653541.9 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `strpos()` loop | 8418927.9 | 10853865.1 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | `preg_match_all()` | 7421936.5 | 34544171.9 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | Matcher::matchAll() | 858826.7 | 1102121.3 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `strpos()` loop | 8420369.0 | 10853851.3 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | `preg_match_all()` | 7416274.6 | 34544168.4 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | Matcher::matchAll() | 1260887.5 | 1918734.3 | checks passed |
| gcc15 | 65536 B; dictionary of 1024 keys; key lengths 12 B; occurrences: 16; unique matched keys: 16 | prepared | `strpos()` loop | 72584029.8 | 93368456.8 | checks passed |
| gcc15 | 65536 B; dictionary of 1024 keys; key lengths 12 B; occurrences: 16; unique matched keys: 16 | prepared | `preg_match_all()` | 116539977.7 | 266964634.7 | checks passed |
| gcc15 | 65536 B; dictionary of 1024 keys; key lengths 12 B; occurrences: 16; unique matched keys: 16 | prepared | Matcher::matchAll() | 904952.3 | 891274.8 | checks passed |
| gcc15 | 65536 B; dictionary of 1024 keys; key lengths 12 B; occurrences: 16; unique matched keys: 16 | oneshot | `strpos()` loop | 72602383.0 | 93368393.8 | checks passed |
| gcc15 | 65536 B; dictionary of 1024 keys; key lengths 12 B; occurrences: 16; unique matched keys: 16 | oneshot | `preg_match_all()` | 116833646.7 | 266964017.7 | checks passed |
| gcc15 | 65536 B; dictionary of 1024 keys; key lengths 12 B; occurrences: 16; unique matched keys: 16 | oneshot | Matcher::matchAll() | 4473968.7 | 6216098.7 | checks passed |
| clang21 | 65536 B; dictionary of 1024 keys; key lengths 12 B; occurrences: 16; unique matched keys: 16 | prepared | `strpos()` loop | 68128633.6 | 87137620.8 | checks passed |
| clang21 | 65536 B; dictionary of 1024 keys; key lengths 12 B; occurrences: 16; unique matched keys: 16 | prepared | `preg_match_all()` | 108778882.3 | 266961687.0 | checks passed |
| clang21 | 65536 B; dictionary of 1024 keys; key lengths 12 B; occurrences: 16; unique matched keys: 16 | prepared | Matcher::matchAll() | 862151.2 | 1115244.7 | checks passed |
| clang21 | 65536 B; dictionary of 1024 keys; key lengths 12 B; occurrences: 16; unique matched keys: 16 | oneshot | `strpos()` loop | 68104762.6 | 87137668.2 | checks passed |
| clang21 | 65536 B; dictionary of 1024 keys; key lengths 12 B; occurrences: 16; unique matched keys: 16 | oneshot | `preg_match_all()` | 118236606.7 | 266961841.7 | checks passed |
| clang21 | 65536 B; dictionary of 1024 keys; key lengths 12 B; occurrences: 16; unique matched keys: 16 | oneshot | Matcher::matchAll() | 4526752.3 | 6668617.1 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | prepared | `strpos()` loop | 570889.9 | 811587.6 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | prepared | `preg_match_all()` | 477362.9 | 2196764.0 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | prepared | Matcher::matchAll() | 22633.4 | 58857.0 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | oneshot | `strpos()` loop | 571462.2 | 811584.6 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | oneshot | `preg_match_all()` | 477408.7 | 2196764.0 | checks passed |
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | oneshot | Matcher::matchAll() | 276121.2 | 830329.9 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | prepared | `strpos()` loop | 532298.7 | 742110.9 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | prepared | `preg_match_all()` | 478424.8 | 2197278.9 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | prepared | Matcher::matchAll() | 16709.0 | 73055.0 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | oneshot | `strpos()` loop | 532300.5 | 742109.6 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | oneshot | `preg_match_all()` | 478324.2 | 2197280.4 | checks passed |
| clang21 | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | oneshot | Matcher::matchAll() | 263922.7 | 887344.2 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | prepared | `strpos()` loop | 9097976.1 | 11974652.0 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | prepared | `preg_match_all()` | 7786972.8 | 35883701.3 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | prepared | Matcher::matchAll() | 916657.9 | 926560.8 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | oneshot | `strpos()` loop | 9097794.8 | 11974687.4 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | oneshot | `preg_match_all()` | 7783086.6 | 35883704.6 | checks passed |
| gcc15 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | oneshot | Matcher::matchAll() | 1305312.7 | 1698055.1 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | prepared | `strpos()` loop | 8539960.1 | 11196069.8 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | prepared | `preg_match_all()` | 7815164.0 | 35885672.9 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | prepared | Matcher::matchAll() | 874963.1 | 1155220.2 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | oneshot | `strpos()` loop | 8541626.3 | 11196023.4 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | oneshot | `preg_match_all()` | 7815650.7 | 35885678.0 | checks passed |
| clang21 | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | oneshot | Matcher::matchAll() | 1276870.0 | 1969541.6 | checks passed |
| gcc15 | 1393 B; dictionary of 128 keys; key lengths 3–30 B; no matches | prepared | `str_contains()` loop | 176001.9 | 299998.9 | checks passed |
| gcc15 | 1393 B; dictionary of 128 keys; key lengths 3–30 B; no matches | prepared | Matcher::matches() | 235407.0 | 1153477.3 | checks passed |
| gcc15 | 1393 B; dictionary of 128 keys; key lengths 3–30 B; no matches | prepared | Matcher::matches() | 11393.2 | 26013.0 | checks passed |
| gcc15 | 1393 B; dictionary of 128 keys; key lengths 3–30 B; no matches | oneshot | `str_contains()` loop | 175934.5 | 299990.6 | checks passed |
| gcc15 | 1393 B; dictionary of 128 keys; key lengths 3–30 B; no matches | oneshot | Matcher::matches() | 235399.9 | 1153477.3 | checks passed |
| gcc15 | 1393 B; dictionary of 128 keys; key lengths 3–30 B; no matches | oneshot | Matcher::matches() | 341082.0 | 885582.6 | checks passed |
| clang21 | 1393 B; dictionary of 128 keys; key lengths 3–30 B; no matches | prepared | `str_contains()` loop | 167073.9 | 276596.1 | checks passed |
| clang21 | 1393 B; dictionary of 128 keys; key lengths 3–30 B; no matches | prepared | Matcher::matches() | 233830.1 | 1153446.5 | checks passed |
| clang21 | 1393 B; dictionary of 128 keys; key lengths 3–30 B; no matches | prepared | Matcher::matches() | 12779.5 | 30070.0 | checks passed |
| clang21 | 1393 B; dictionary of 128 keys; key lengths 3–30 B; no matches | oneshot | `str_contains()` loop | 166810.1 | 276588.0 | checks passed |
| clang21 | 1393 B; dictionary of 128 keys; key lengths 3–30 B; no matches | oneshot | Matcher::matches() | 233934.1 | 1153446.3 | checks passed |
| clang21 | 1393 B; dictionary of 128 keys; key lengths 3–30 B; no matches | oneshot | Matcher::matches() | 344606.2 | 958286.6 | checks passed |
| gcc15 | 1337 B; dictionary of 128 keys; key lengths 3–30 B; match: byte 438, dictionary key #1 | prepared | `str_contains()` loop | 1037.8 | 2420.0 | checks passed |
| gcc15 | 1337 B; dictionary of 128 keys; key lengths 3–30 B; match: byte 438, dictionary key #1 | prepared | Matcher::matches() | 75868.5 | 374624.6 | checks passed |
| gcc15 | 1337 B; dictionary of 128 keys; key lengths 3–30 B; match: byte 438, dictionary key #1 | prepared | Matcher::matches() | 4042.4 | 9245.0 | checks passed |
| gcc15 | 1337 B; dictionary of 128 keys; key lengths 3–30 B; match: byte 438, dictionary key #1 | oneshot | `str_contains()` loop | 1041.7 | 2420.0 | checks passed |
| gcc15 | 1337 B; dictionary of 128 keys; key lengths 3–30 B; match: byte 438, dictionary key #1 | oneshot | Matcher::matches() | 75880.7 | 374624.5 | checks passed |
| gcc15 | 1337 B; dictionary of 128 keys; key lengths 3–30 B; match: byte 438, dictionary key #1 | oneshot | Matcher::matches() | 331166.4 | 868815.4 | checks passed |
| clang21 | 1337 B; dictionary of 128 keys; key lengths 3–30 B; match: byte 438, dictionary key #1 | prepared | `str_contains()` loop | 932.3 | 2179.0 | checks passed |
| clang21 | 1337 B; dictionary of 128 keys; key lengths 3–30 B; match: byte 438, dictionary key #1 | prepared | Matcher::matches() | 75423.5 | 374597.1 | checks passed |
| clang21 | 1337 B; dictionary of 128 keys; key lengths 3–30 B; match: byte 438, dictionary key #1 | prepared | Matcher::matches() | 4484.7 | 10567.0 | checks passed |
| clang21 | 1337 B; dictionary of 128 keys; key lengths 3–30 B; match: byte 438, dictionary key #1 | oneshot | `str_contains()` loop | 931.4 | 2179.0 | checks passed |
| clang21 | 1337 B; dictionary of 128 keys; key lengths 3–30 B; match: byte 438, dictionary key #1 | oneshot | Matcher::matches() | 75376.4 | 374597.0 | checks passed |
| clang21 | 1337 B; dictionary of 128 keys; key lengths 3–30 B; match: byte 438, dictionary key #1 | oneshot | Matcher::matches() | 334375.7 | 938779.8 | checks passed |
| gcc15 | 12828 B; dictionary of 128 keys; key lengths 4–28 B; occurrences: 23; unique matched keys: 12 | prepared | `strpos()` loop | 1438246.4 | 2025584.2 | checks passed |
| gcc15 | 12828 B; dictionary of 128 keys; key lengths 4–28 B; occurrences: 23; unique matched keys: 12 | prepared | `preg_match_all()` | 2113545.6 | 5971164.6 | checks passed |
| gcc15 | 12828 B; dictionary of 128 keys; key lengths 4–28 B; occurrences: 23; unique matched keys: 12 | prepared | Matcher::getMatchedKeywords() | 89423.5 | 247434.4 | checks passed |
| gcc15 | 12828 B; dictionary of 128 keys; key lengths 4–28 B; occurrences: 23; unique matched keys: 12 | oneshot | `strpos()` loop | 1438335.7 | 2025515.5 | checks passed |
| gcc15 | 12828 B; dictionary of 128 keys; key lengths 4–28 B; occurrences: 23; unique matched keys: 12 | oneshot | `preg_match_all()` | 2113711.0 | 5971163.3 | checks passed |
| gcc15 | 12828 B; dictionary of 128 keys; key lengths 4–28 B; occurrences: 23; unique matched keys: 12 | oneshot | Matcher::getMatchedKeywords() | 442488.6 | 1175529.2 | checks passed |
| clang21 | 12828 B; dictionary of 128 keys; key lengths 4–28 B; occurrences: 23; unique matched keys: 12 | prepared | `strpos()` loop | 1357954.9 | 1898225.0 | checks passed |
| clang21 | 12828 B; dictionary of 128 keys; key lengths 4–28 B; occurrences: 23; unique matched keys: 12 | prepared | `preg_match_all()` | 2116065.0 | 5972532.7 | checks passed |
| clang21 | 12828 B; dictionary of 128 keys; key lengths 4–28 B; occurrences: 23; unique matched keys: 12 | prepared | Matcher::getMatchedKeywords() | 63786.9 | 273449.0 | checks passed |
| clang21 | 12828 B; dictionary of 128 keys; key lengths 4–28 B; occurrences: 23; unique matched keys: 12 | oneshot | `strpos()` loop | 1356154.6 | 1898155.4 | checks passed |
| clang21 | 12828 B; dictionary of 128 keys; key lengths 4–28 B; occurrences: 23; unique matched keys: 12 | oneshot | `preg_match_all()` | 2114828.5 | 5972527.1 | checks passed |
| clang21 | 12828 B; dictionary of 128 keys; key lengths 4–28 B; occurrences: 23; unique matched keys: 12 | oneshot | Matcher::getMatchedKeywords() | 436687.1 | 1272064.6 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | prepared | `strtr()` | 35819.5 | 173926.1 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | prepared | `preg_replace_callback()` | 24747.0 | 131653.1 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | prepared | `preg_replace_callback()` | 24769.0 | 131688.0 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | prepared | Replacer::replace() | 26319.8 | 73275.2 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | oneshot | `strtr()` | 35819.5 | 173926.1 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | oneshot | `preg_replace_callback()` | 24747.0 | 131653.1 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | oneshot | `preg_replace_callback()` | 24769.0 | 131688.0 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | oneshot | Replacer::replace() | 61820.4 | 216605.1 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | prepared | `strtr()` | 32062.9 | 163389.1 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | prepared | `preg_replace_callback()` | 25024.8 | 131636.0 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | prepared | `preg_replace_callback()` | 25020.2 | 131674.0 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | prepared | Replacer::replace() | 24267.2 | 81378.8 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | oneshot | `strtr()` | 32062.9 | 163389.1 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | oneshot | `preg_replace_callback()` | 25024.8 | 131636.0 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | oneshot | `preg_replace_callback()` | 25020.2 | 131674.0 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | oneshot | Replacer::replace() | 60839.8 | 234535.9 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | prepared | `str_replace()` | 69149.1 | 99832.0 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | prepared | `preg_replace_callback()` | 25738.4 | 126760.1 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | prepared | `preg_replace_callback()` | 25752.0 | 126795.0 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | prepared | Replacer::replace() | 27480.8† | 73701.1† | † |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | oneshot | `str_replace()` | 69149.1 | 99832.0 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | oneshot | `preg_replace_callback()` | 25738.4 | 126760.1 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | oneshot | `preg_replace_callback()` | 25752.0 | 126795.0 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | oneshot | Replacer::replace() | 59251.6 | 198998.1 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | prepared | `str_replace()` | 64302.4 | 91722.3 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | prepared | `preg_replace_callback()` | 26661.7 | 126743.0 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | prepared | `preg_replace_callback()` | 26732.8 | 126780.9 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | prepared | Replacer::replace() | 26194.7 | 81820.0 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | oneshot | `str_replace()` | 64302.4 | 91722.3 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | oneshot | `preg_replace_callback()` | 26661.7 | 126743.0 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | oneshot | `preg_replace_callback()` | 26732.8 | 126780.9 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | oneshot | Replacer::replace() | 58660.1 | 216877.0 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | prepared | `strtr()` | 34710.2† | 168825.0† | † |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | prepared | `preg_replace_callback()` | 27739.0 | 139201.1 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | prepared | `preg_replace_callback()` | 27851.9 | 139236.1 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | prepared | Replacer::replace() | 27284.0 | 77018.0 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | oneshot | `strtr()` | 34710.2† | 168825.0† | † |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | oneshot | `preg_replace_callback()` | 27739.0 | 139201.1 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | oneshot | `preg_replace_callback()` | 27851.9 | 139236.1 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | oneshot | Replacer::replace() | 62667.7† | 219766.4† | † |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | prepared | `strtr()` | 31082.7 | 158373.0 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | prepared | `preg_replace_callback()` | 28418.6 | 138904.9 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | prepared | `preg_replace_callback()` | 28215.2 | 138943.0 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | prepared | Replacer::replace() | 25441.6 | 84991.1 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | oneshot | `strtr()` | 31082.7 | 158373.0 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | oneshot | `preg_replace_callback()` | 28418.6 | 138904.9 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | oneshot | `preg_replace_callback()` | 28215.2 | 138943.0 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | oneshot | Replacer::replace() | 61526.3 | 237571.9 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | prepared | `str_replace()` | 72042.3 | 109647.9 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | prepared | `preg_replace_callback()` | 28456.4 | 134184.1 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | prepared | `preg_replace_callback()` | 28532.5 | 134219.0 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | prepared | Replacer::replace() | 28182.8 | 76981.1 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | oneshot | `str_replace()` | 72042.3 | 109647.9 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | oneshot | `preg_replace_callback()` | 28456.4 | 134184.1 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | oneshot | `preg_replace_callback()` | 28532.5 | 134219.0 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | oneshot | Replacer::replace() | 60190.3 | 202835.0 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | prepared | `str_replace()` | 67252.6 | 100672.9 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | prepared | `preg_replace_callback()` | 29583.4 | 133885.0 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | prepared | `preg_replace_callback()` | 29493.0 | 133923.0 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | prepared | Replacer::replace() | 26997.8 | 84944.0 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | oneshot | `str_replace()` | 67252.6 | 100672.9 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | oneshot | `preg_replace_callback()` | 29583.4 | 133885.0 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | oneshot | `preg_replace_callback()` | 29493.0 | 133923.0 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | oneshot | Replacer::replace() | 59868.4 | 220556.0 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | prepared | `strtr()` | 33554.4 | 162582.0 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | prepared | `preg_replace_callback()` | 30358.8 | 146338.0 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | prepared | `preg_replace_callback()` | 30444.1 | 146373.0 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | prepared | Replacer::replace() | 27496.3 | 78709.1 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | oneshot | `strtr()` | 33554.4 | 162582.0 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | oneshot | `preg_replace_callback()` | 30358.8 | 146338.0 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | oneshot | `preg_replace_callback()` | 30444.1 | 146373.0 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | oneshot | Replacer::replace() | 63413.5 | 222068.8 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | prepared | `strtr()` | 29990.0 | 152253.0 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | prepared | `preg_replace_callback()` | 31438.8 | 145797.9 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | prepared | `preg_replace_callback()` | 31451.0 | 145836.0 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | prepared | Replacer::replace() | 25872.2 | 86554.1 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | oneshot | `strtr()` | 29990.0 | 152253.0 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | oneshot | `preg_replace_callback()` | 31438.8 | 145797.9 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | oneshot | `preg_replace_callback()` | 31451.0 | 145836.0 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | oneshot | Replacer::replace() | 62143.2 | 239744.0 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | prepared | `str_replace()` | 74843.3 | 115916.0 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | prepared | `preg_replace_callback()` | 30334.1 | 141256.9 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | prepared | `preg_replace_callback()` | 30660.7 | 141292.0 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | prepared | Replacer::replace() | 29236.5 | 79760.9 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | oneshot | `str_replace()` | 74843.3 | 115916.0 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | oneshot | `preg_replace_callback()` | 30334.1 | 141256.9 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | oneshot | `preg_replace_callback()` | 30660.7 | 141292.0 | checks passed |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | oneshot | Replacer::replace() | 60762.1 | 204429.2 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | prepared | `str_replace()` | 69850.7 | 106231.1 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | prepared | `preg_replace_callback()` | 32231.6 | 140714.0 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | prepared | `preg_replace_callback()` | 32192.6 | 140752.2 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | prepared | Replacer::replace() | 28387.2 | 87592.0 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | oneshot | `str_replace()` | 69850.7 | 106231.1 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | oneshot | `preg_replace_callback()` | 32231.6 | 140714.0 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | oneshot | `preg_replace_callback()` | 32192.6 | 140752.2 | checks passed |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | oneshot | Replacer::replace() | 60490.1 | 222022.9 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | prepared | `strtr()` | 54899.7 | 259453.1 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | prepared | `preg_replace_callback()` | 52760.9 | 241998.0 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | prepared | `preg_replace_callback()` | 52992.2 | 242032.9 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | prepared | Replacer::replace() | 27634.0 | 74191.1 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | oneshot | `strtr()` | 54899.7 | 259453.1 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | oneshot | `preg_replace_callback()` | 52760.9 | 241998.0 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | oneshot | `preg_replace_callback()` | 52992.2 | 242032.9 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | oneshot | Replacer::replace() | 92866.2 | 324304.3 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | prepared | `strtr()` | 50480.4 | 253484.8 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | prepared | `preg_replace_callback()` | 49101.1 | 241981.0 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | prepared | `preg_replace_callback()` | 48661.0 | 242019.4 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | prepared | Replacer::replace() | 26665.6 | 82269.1 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | oneshot | `strtr()` | 50480.4 | 253484.8 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | oneshot | `preg_replace_callback()` | 49101.1 | 241981.0 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | oneshot | `preg_replace_callback()` | 48661.0 | 242019.4 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | oneshot | Replacer::replace() | 93412.5 | 350475.8 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | prepared | `str_replace()` | 138767.5 | 196072.1 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | prepared | `preg_replace_callback()` | 38849.9† | 194924.0† | † |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | prepared | `preg_replace_callback()` | 38899.4 | 194959.2 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | prepared | Replacer::replace() | 27460.1 | 73824.1 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | oneshot | `str_replace()` | 138767.5 | 196072.1 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | oneshot | `preg_replace_callback()` | 38849.9† | 194924.0† | † |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | oneshot | `preg_replace_callback()` | 38899.4 | 194959.2 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | oneshot | Replacer::replace() | 89698.0 | 311295.5 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | prepared | `str_replace()` | 128709.5 | 179987.9 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | prepared | `preg_replace_callback()` | 37673.3 | 194907.1 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | prepared | `preg_replace_callback()` | 37503.5 | 194944.9 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | prepared | Replacer::replace() | 26192.9 | 81931.0 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | oneshot | `str_replace()` | 128709.5 | 179987.9 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | oneshot | `preg_replace_callback()` | 37673.3 | 194907.1 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | oneshot | `preg_replace_callback()` | 37503.5 | 194944.9 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | oneshot | Replacer::replace() | 91274.2 | 337485.4 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | prepared | `strtr()` | 50379.8 | 237625.9 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | prepared | `preg_replace_callback()` | 55468.7 | 242694.9 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | prepared | `preg_replace_callback()` | 55446.0 | 242730.2 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | prepared | Replacer::replace() | 28809.6 | 79555.9 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | oneshot | `strtr()` | 50379.8 | 237625.9 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | oneshot | `preg_replace_callback()` | 55468.7 | 242694.9 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | oneshot | `preg_replace_callback()` | 55446.0 | 242730.2 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | oneshot | Replacer::replace() | 93352.2 | 329611.6 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | prepared | `strtr()` | 46256.8 | 231326.9 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | prepared | `preg_replace_callback()` | 52563.7 | 242156.9 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | prepared | `preg_replace_callback()` | 52969.8 | 242195.1 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | prepared | Replacer::replace() | 28407.7 | 87373.0 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | oneshot | `strtr()` | 46256.8 | 231326.9 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | oneshot | `preg_replace_callback()` | 52563.7 | 242156.9 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | oneshot | `preg_replace_callback()` | 52969.8 | 242195.1 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | oneshot | Replacer::replace() | 95414.4 | 355525.8 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | prepared | `str_replace()` | 143456.0 | 211948.6 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | prepared | `preg_replace_callback()` | 43562.4 | 201201.4 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | prepared | `preg_replace_callback()` | 43365.8 | 201235.9 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | prepared | Replacer::replace() | 29126.4 | 79304.0 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | oneshot | `str_replace()` | 143456.0 | 211948.6 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | oneshot | `preg_replace_callback()` | 43562.4 | 201201.4 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | oneshot | `preg_replace_callback()` | 43365.8 | 201235.9 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | oneshot | Replacer::replace() | 91460.0 | 316718.3 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | prepared | `str_replace()` | 134950.1 | 194290.9 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | prepared | `preg_replace_callback()` | 42369.5 | 200660.0 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | prepared | `preg_replace_callback()` | 42311.3 | 200698.0 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | prepared | Replacer::replace() | 28135.5† | 87128.1† | † |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | oneshot | `str_replace()` | 134950.1 | 194290.9 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | oneshot | `preg_replace_callback()` | 42369.5 | 200660.0 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | oneshot | `preg_replace_callback()` | 42311.3 | 200698.0 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | oneshot | Replacer::replace() | 93453.7 | 342627.8 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | prepared | `strtr()` | 45215.0 | 212100.1 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | prepared | `preg_replace_callback()` | 55583.6 | 239154.0 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | prepared | `preg_replace_callback()` | 55721.8 | 239189.6 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | prepared | Replacer::replace() | 29552.7 | 83388.1 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | oneshot | `strtr()` | 45215.0 | 212100.1 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | oneshot | `preg_replace_callback()` | 55583.6 | 239154.0 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | oneshot | `preg_replace_callback()` | 55721.8 | 239189.6 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | oneshot | Replacer::replace() | 94394.9 | 334422.5 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | prepared | `strtr()` | 41169.4 | 205343.9 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | prepared | `preg_replace_callback()` | 53564.8 | 238143.1 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | prepared | `preg_replace_callback()` | 53869.2 | 238181.0 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | prepared | Replacer::replace() | 28943.3 | 90943.3 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | oneshot | `strtr()` | 41169.4 | 205343.9 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | oneshot | `preg_replace_callback()` | 53564.8 | 238143.1 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | oneshot | `preg_replace_callback()` | 53869.2 | 238181.0 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | oneshot | Replacer::replace() | 96496.7 | 360071.1 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | prepared | `str_replace()` | 148186.3 | 228672.6 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | prepared | `preg_replace_callback()` | 45990.0 | 205310.1 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | prepared | `preg_replace_callback()` | 46417.8 | 205344.9 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | prepared | Replacer::replace() | 30554.4 | 83206.1 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | oneshot | `str_replace()` | 148186.3 | 228672.6 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | oneshot | `preg_replace_callback()` | 45990.0 | 205310.1 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | oneshot | `preg_replace_callback()` | 46417.8 | 205344.9 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | oneshot | Replacer::replace() | 93030.2 | 321599.8 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | prepared | `str_replace()` | 138698.3 | 209518.7 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | prepared | `preg_replace_callback()` | 46025.2 | 204288.6 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | prepared | `preg_replace_callback()` | 46067.4 | 204327.1 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | prepared | Replacer::replace() | 29011.1 | 90775.1 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | oneshot | `str_replace()` | 138698.3 | 209518.7 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | oneshot | `preg_replace_callback()` | 46025.2 | 204288.6 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | oneshot | `preg_replace_callback()` | 46067.4 | 204327.1 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | oneshot | Replacer::replace() | 94684.1 | 347251.1 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | prepared | `strtr()` | 1822.6 | 5226.0 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | prepared | `str_replace()` | 1870.9 | 5455.0 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | prepared | `preg_replace()` | 1661.6 | 6418.0 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | prepared | `preg_replace()` | 1698.0† | 6475.0† | † |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | prepared | Replacer::replace() | 18616.6 | 54287.0 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | oneshot | `strtr()` | 1822.6 | 5226.0 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | oneshot | `str_replace()` | 1870.9 | 5455.0 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | oneshot | `preg_replace()` | 1661.6 | 6418.0 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | oneshot | `preg_replace()` | 1698.0† | 6475.0† | † |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | oneshot | Replacer::replace() | 20445.5 | 60307.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | prepared | `strtr()` | 1769.4 | 5034.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | prepared | `str_replace()` | 1798.3 | 5251.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | prepared | `preg_replace()` | 1619.8 | 6333.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | prepared | `preg_replace()` | 1665.9 | 6391.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | prepared | Replacer::replace() | 11382.6 | 62459.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | oneshot | `strtr()` | 1769.4 | 5034.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | oneshot | `str_replace()` | 1798.3 | 5251.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | oneshot | `preg_replace()` | 1619.8 | 6333.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | oneshot | `preg_replace()` | 1665.9 | 6391.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | oneshot | Replacer::replace() | 13215.5 | 68867.0 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | prepared | `strtr()` | 1860.1 | 5513.0 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | prepared | `str_replace()` | 1889.3 | 5734.0 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | prepared | `preg_replace()` | 1934.8 | 8277.0 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | prepared | `preg_replace()` | 1969.3 | 8334.0 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | prepared | Replacer::replace() | 18763.7 | 54904.1 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | oneshot | `strtr()` | 1860.1 | 5513.0 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | oneshot | `str_replace()` | 1889.3 | 5734.0 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | oneshot | `preg_replace()` | 1934.8 | 8277.0 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | oneshot | `preg_replace()` | 1969.3 | 8334.0 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | oneshot | Replacer::replace() | 20821.9 | 60924.1 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | prepared | `strtr()` | 1798.1 | 5306.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | prepared | `str_replace()` | 1825.9 | 5515.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | prepared | `preg_replace()` | 1894.6 | 8168.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | prepared | `preg_replace()` | 1926.5 | 8226.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | prepared | Replacer::replace() | 11654.0 | 63108.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | oneshot | `strtr()` | 1798.1 | 5306.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | oneshot | `str_replace()` | 1825.9 | 5515.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | oneshot | `preg_replace()` | 1894.6 | 8168.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | oneshot | `preg_replace()` | 1926.5 | 8226.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | oneshot | Replacer::replace() | 13405.6 | 69516.0 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | prepared | `strtr()` | 3753.7† | 6739.0† | † |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | prepared | `str_replace()` | 3818.5 | 6947.0 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | prepared | `preg_replace()` | 1617.3 | 6591.0 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | prepared | `preg_replace()` | 1647.2 | 6648.0 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | prepared | Replacer::replace() | 20879.4 | 62786.1 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | oneshot | `strtr()` | 3753.7† | 6739.0† | † |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | oneshot | `str_replace()` | 3818.5 | 6947.0 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | oneshot | `preg_replace()` | 1617.3 | 6591.0 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | oneshot | `preg_replace()` | 1647.2 | 6648.0 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | oneshot | Replacer::replace() | 24200.1 | 74805.1 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | prepared | `strtr()` | 3411.2 | 6087.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | prepared | `str_replace()` | 3414.0 | 6283.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | prepared | `preg_replace()` | 1579.6 | 6490.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | prepared | `preg_replace()` | 1601.1 | 6548.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | prepared | Replacer::replace() | 13406.8 | 70910.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | oneshot | `strtr()` | 3411.2 | 6087.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | oneshot | `str_replace()` | 3414.0 | 6283.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | oneshot | `preg_replace()` | 1579.6 | 6490.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | oneshot | `preg_replace()` | 1601.1 | 6548.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | oneshot | Replacer::replace() | 17387.1 | 83436.0 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | prepared | `strtr()` | 3960.8 | 8526.0 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | prepared | `str_replace()` | 4056.4 | 8734.0 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | prepared | `preg_replace()` | 2098.3 | 9152.0 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | prepared | `preg_replace()` | 2106.3 | 9209.0 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | prepared | Replacer::replace() | 21484.7 | 64636.1 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | oneshot | `strtr()` | 3960.8 | 8526.0 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | oneshot | `str_replace()` | 4056.4 | 8734.0 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | oneshot | `preg_replace()` | 2098.3 | 9152.0 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | oneshot | `preg_replace()` | 2106.3 | 9209.0 | checks passed |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | oneshot | Replacer::replace() | 24811.3 | 76655.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | prepared | `strtr()` | 3618.5 | 7388.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | prepared | `str_replace()` | 3631.0 | 7584.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | prepared | `preg_replace()` | 2059.3 | 8963.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | prepared | `preg_replace()` | 2078.1 | 9021.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | prepared | Replacer::replace() | 15014.8 | 72600.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | oneshot | `strtr()` | 3618.5 | 7388.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | oneshot | `str_replace()` | 3631.0 | 7584.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | oneshot | `preg_replace()` | 2059.3 | 8963.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | oneshot | `preg_replace()` | 2078.1 | 9021.0 | checks passed |
| clang21 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | oneshot | Replacer::replace() | 17594.6 | 85126.0 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 3856 B | prepared | `str_replace()` | 206889.2 | 308241.6 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 3856 B | prepared | `preg_replace()` | 36692.9 | 182290.2 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 3856 B | prepared | `preg_replace()` | 36676.2 | 182347.2 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 3856 B | prepared | Replacer::replace() | 29127.2 | 79199.0 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 3856 B | oneshot | `str_replace()` | 206889.2 | 308241.6 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 3856 B | oneshot | `preg_replace()` | 36692.9 | 182290.2 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 3856 B | oneshot | `preg_replace()` | 36676.2 | 182347.2 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 3856 B | oneshot | Replacer::replace() | 91349.8 | 316681.7 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 3856 B | prepared | `str_replace()` | 193565.0 | 281221.0 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 3856 B | prepared | `preg_replace()` | 35609.3 | 182229.0 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 3856 B | prepared | `preg_replace()` | 35625.8 | 182287.2 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 3856 B | prepared | Replacer::replace() | 28151.1 | 87038.1 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 3856 B | oneshot | `str_replace()` | 193565.0 | 281221.0 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 3856 B | oneshot | `preg_replace()` | 35609.3 | 182229.0 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 3856 B | oneshot | `preg_replace()` | 35625.8 | 182287.2 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 3856 B | oneshot | Replacer::replace() | 92763.1 | 342609.1 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 4608 B | prepared | `str_replace()` | 224199.7 | 329802.6 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 4608 B | prepared | `preg_replace_callback()` | 43018.3 | 201326.1 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 4608 B | prepared | `preg_replace_callback()` | 43386.5 | 201361.1 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 4608 B | prepared | Replacer::replace() | 29489.7 | 79934.0 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 4608 B | oneshot | `str_replace()` | 224199.7 | 329802.6 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 4608 B | oneshot | `preg_replace_callback()` | 43018.3 | 201326.1 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 4608 B | oneshot | `preg_replace_callback()` | 43386.5 | 201361.1 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 4608 B | oneshot | Replacer::replace() | 91555.3 | 317705.9 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 4608 B | prepared | `str_replace()` | 209755.8 | 301438.4 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 4608 B | prepared | `preg_replace_callback()` | 42451.2 | 200774.9 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 4608 B | prepared | `preg_replace_callback()` | 42530.8† | 200813.1† | † |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 4608 B | prepared | Replacer::replace() | 28426.7 | 87759.9 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 4608 B | oneshot | `str_replace()` | 209755.8 | 301438.4 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 4608 B | oneshot | `preg_replace_callback()` | 42451.2 | 200774.9 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 4608 B | oneshot | `preg_replace_callback()` | 42530.8† | 200813.1† | † |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 4608 B | oneshot | Replacer::replace() | 93526.1 | 343612.4 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 4000 B | prepared | `str_replace()` | 212209.3 | 313064.7 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 4000 B | prepared | `preg_replace()` | 37049.5 | 183962.1 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 4000 B | prepared | `preg_replace()` | 37121.7 | 184019.1 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 4000 B | prepared | Replacer::replace() | 29075.7 | 79171.0 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 4000 B | oneshot | `str_replace()` | 212209.3 | 313064.7 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 4000 B | oneshot | `preg_replace()` | 37049.5 | 183962.1 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 4000 B | oneshot | `preg_replace()` | 37121.7 | 184019.1 | checks passed |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 4000 B | oneshot | Replacer::replace() | 91830.8 | 316654.1 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 4000 B | prepared | `str_replace()` | 197429.1† | 285721.7† | † |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 4000 B | prepared | `preg_replace()` | 35616.0† | 183756.9† | † |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 4000 B | prepared | `preg_replace()` | 35728.7 | 183815.0 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 4000 B | prepared | Replacer::replace() | 28231.0 | 87009.8 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 4000 B | oneshot | `str_replace()` | 197429.1† | 285721.7† | † |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 4000 B | oneshot | `preg_replace()` | 35616.0† | 183756.9† | † |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 4000 B | oneshot | `preg_replace()` | 35728.7 | 183815.0 | checks passed |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 4000 B | oneshot | Replacer::replace() | 93074.7 | 342580.9 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | prepared | `strtr()` | 229876.5 | 689896.7 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | prepared | `preg_replace_callback()` | 149556.2 | 520998.2 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | prepared | `preg_replace_callback()` | 150801.8 | 521032.1 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | prepared | Replacer::replace() | 116900.0 | 293729.6 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | oneshot | `strtr()` | 229876.5 | 689896.7 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | oneshot | `preg_replace_callback()` | 149556.2 | 520998.2 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | oneshot | `preg_replace_callback()` | 150801.8 | 521032.1 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | oneshot | Replacer::replace() | 152869.3 | 437180.7 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | prepared | `strtr()` | 202910.3 | 647824.1 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | prepared | `preg_replace_callback()` | 149560.3 | 520981.0 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | prepared | `preg_replace_callback()` | 150618.4 | 521019.4 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | prepared | Replacer::replace() | 105205.8 | 326301.3 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | oneshot | `strtr()` | 202910.3 | 647824.1 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | oneshot | `preg_replace_callback()` | 149560.3 | 520981.0 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | oneshot | `preg_replace_callback()` | 150618.4 | 521019.4 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | oneshot | Replacer::replace() | 142234.3 | 479576.7 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | prepared | `str_replace()` | 278775.4 | 376315.4 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | prepared | `preg_replace_callback()` | 139942.5 | 500618.2 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | prepared | `preg_replace_callback()` | 139834.2 | 500653.1 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | prepared | Replacer::replace() | 118318.5 | 295654.4 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | oneshot | `str_replace()` | 278775.4 | 376315.4 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | oneshot | `preg_replace_callback()` | 139942.5 | 500618.2 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | oneshot | `preg_replace_callback()` | 139834.2 | 500653.1 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | oneshot | Replacer::replace() | 151044.6 | 420960.5 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | prepared | `str_replace()` | 260689.3 | 350154.3 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | prepared | `preg_replace_callback()` | 141655.4 | 500600.6 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | prepared | `preg_replace_callback()` | 142535.5 | 500638.6 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | prepared | Replacer::replace() | 113652.1 | 328302.4 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | oneshot | `str_replace()` | 260689.3 | 350154.3 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | oneshot | `preg_replace_callback()` | 141655.4 | 500600.6 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | oneshot | `preg_replace_callback()` | 142535.5 | 500638.6 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | oneshot | Replacer::replace() | 146270.8 | 463363.3 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | prepared | `strtr()` | 226679.4 | 687919.1 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | prepared | `preg_replace_callback()` | 150777.3 | 531093.8 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | prepared | `preg_replace_callback()` | 151942.7 | 531129.3 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | prepared | Replacer::replace() | 118196.8 | 300162.1 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | oneshot | `strtr()` | 226679.4 | 687919.1 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | oneshot | `preg_replace_callback()` | 150777.3 | 531093.8 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | oneshot | `preg_replace_callback()` | 151942.7 | 531129.3 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | oneshot | Replacer::replace() | 155256.9 | 443528.1 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | prepared | `strtr()` | 201355.6 | 645851.3 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | prepared | `preg_replace_callback()` | 154559.3 | 530782.3 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | prepared | `preg_replace_callback()` | 155602.6 | 530820.5 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | prepared | Replacer::replace() | 107662.3 | 332549.5 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | oneshot | `strtr()` | 201355.6 | 645851.3 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | oneshot | `preg_replace_callback()` | 154559.3 | 530782.3 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | oneshot | `preg_replace_callback()` | 155602.6 | 530820.5 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | oneshot | Replacer::replace() | 145082.0 | 485740.7 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | prepared | `str_replace()` | 286726.1 | 394652.5 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | prepared | `preg_replace_callback()` | 141150.1 | 511038.4 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | prepared | `preg_replace_callback()` | 141044.5 | 511073.4 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | prepared | Replacer::replace() | 120947.7 | 302888.1 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | oneshot | `str_replace()` | 286726.1 | 394652.5 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | oneshot | `preg_replace_callback()` | 141150.1 | 511038.4 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | oneshot | `preg_replace_callback()` | 141044.5 | 511073.4 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | oneshot | Replacer::replace() | 154193.1 | 427694.2 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | prepared | `str_replace()` | 267860.3 | 367418.5 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | prepared | `preg_replace_callback()` | 144075.6 | 510723.1 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | prepared | `preg_replace_callback()` | 144130.9 | 510761.2 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | prepared | Replacer::replace() | 115314.6 | 335337.8 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | oneshot | `str_replace()` | 267860.3 | 367418.5 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | oneshot | `preg_replace_callback()` | 144075.6 | 510723.1 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | oneshot | `preg_replace_callback()` | 144130.9 | 510761.2 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | oneshot | Replacer::replace() | 149052.9 | 469901.6 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | prepared | `strtr()` | 223334.5 | 681576.6 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | prepared | `preg_replace_callback()` | 151629.6 | 537213.8 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | prepared | `preg_replace_callback()` | 152780.8 | 537249.3 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | prepared | Replacer::replace() | 118268.1 | 302085.1 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | oneshot | `strtr()` | 223334.5 | 681576.6 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | oneshot | `preg_replace_callback()` | 151629.6 | 537213.8 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | oneshot | `preg_replace_callback()` | 152780.8 | 537249.3 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | oneshot | Replacer::replace() | 155506.3 | 445452.0 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | prepared | `strtr()` | 195980.0 | 639612.5 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | prepared | `preg_replace_callback()` | 155799.2 | 536657.5 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | prepared | `preg_replace_callback()` | 154192.6 | 536695.2 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | prepared | Replacer::replace() | 108102.9 | 334356.7 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | oneshot | `strtr()` | 195980.0 | 639612.5 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | oneshot | `preg_replace_callback()` | 155799.2 | 536657.5 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | oneshot | `preg_replace_callback()` | 154192.6 | 536695.2 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | oneshot | Replacer::replace() | 144865.0 | 487548.1 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | prepared | `str_replace()` | 292288.5 | 413074.3 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | prepared | `preg_replace_callback()` | 137648.6 | 515696.9 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | prepared | `preg_replace_callback()` | 137883.5 | 515732.1 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | prepared | Replacer::replace() | 121244.1 | 305037.6 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | oneshot | `str_replace()` | 292288.5 | 413074.3 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | oneshot | `preg_replace_callback()` | 137648.6 | 515696.9 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | oneshot | `preg_replace_callback()` | 137883.5 | 515732.1 | checks passed |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | oneshot | Replacer::replace() | 154300.1 | 429746.8 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | prepared | `str_replace()` | 274422.3 | 384873.1 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | prepared | `preg_replace_callback()` | 144375.4 | 515138.0 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | prepared | `preg_replace_callback()` | 144377.7 | 515176.5 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | prepared | Replacer::replace() | 115825.1 | 337357.5 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | oneshot | `str_replace()` | 274422.3 | 384873.1 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | oneshot | `preg_replace_callback()` | 144375.4 | 515138.0 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | oneshot | `preg_replace_callback()` | 144377.7 | 515176.5 | checks passed |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | oneshot | Replacer::replace() | 149043.4 | 471824.2 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | prepared | `strtr()` | 476768.2 | 1041053.9 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | prepared | `preg_replace_callback()` | 371338.6 | 971175.8 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | prepared | `preg_replace_callback()` | 370169.6 | 971210.9 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | prepared | Replacer::replace() | 119505.8 | 297080.1 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | oneshot | `strtr()` | 476768.2 | 1041053.9 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | oneshot | `preg_replace_callback()` | 371338.6 | 971175.8 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | oneshot | `preg_replace_callback()` | 370169.6 | 971210.9 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | oneshot | Replacer::replace() | 184673.3 | 547318.5 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | prepared | `strtr()` | 454503.7 | 1017862.9 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | prepared | `preg_replace_callback()` | 355501.8 | 971159.7 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | prepared | `preg_replace_callback()` | 357230.5 | 971196.8 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | prepared | Replacer::replace() | 115028.8 | 329608.6 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | oneshot | `strtr()` | 454503.7 | 1017862.9 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | oneshot | `preg_replace_callback()` | 355501.8 | 971159.7 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | oneshot | `preg_replace_callback()` | 357230.5 | 971196.8 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | oneshot | Replacer::replace() | 182979.4 | 597938.1 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | prepared | `str_replace()` | 556634.8 | 745578.0 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | prepared | `preg_replace_callback()` | 289516.1 | 774529.5 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | prepared | `preg_replace_callback()` | 290569.6 | 774566.1 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | prepared | Replacer::replace() | 119037.8 | 296099.9 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | oneshot | `str_replace()` | 556634.8 | 745578.0 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | oneshot | `preg_replace_callback()` | 289516.1 | 774529.5 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | oneshot | `preg_replace_callback()` | 290569.6 | 774566.1 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | oneshot | Replacer::replace() | 183571.9 | 533694.6 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | prepared | `str_replace()` | 519738.5 | 693488.6 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | prepared | `preg_replace_callback()` | 283317.0 | 774513.9 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | prepared | `preg_replace_callback()` | 284788.9 | 774552.2 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | prepared | Replacer::replace() | 113342.9 | 328709.3 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | oneshot | `str_replace()` | 519738.5 | 693488.6 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | oneshot | `preg_replace_callback()` | 283317.0 | 774513.9 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | oneshot | `preg_replace_callback()` | 284788.9 | 774552.2 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | oneshot | Replacer::replace() | 179820.0 | 584386.3 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | prepared | `strtr()` | 463966.5 | 1021592.3 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | prepared | `preg_replace_callback()` | 367880.9 | 971874.4 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | prepared | `preg_replace_callback()` | 367593.9 | 971909.3 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | prepared | Replacer::replace() | 121322.8 | 305366.7 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | oneshot | `strtr()` | 463966.5 | 1021592.3 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | oneshot | `preg_replace_callback()` | 367880.9 | 971874.4 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | oneshot | `preg_replace_callback()` | 367593.9 | 971909.3 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | oneshot | Replacer::replace() | 187087.1 | 555476.0 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | prepared | `strtr()` | 432318.3 | 997910.6 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | prepared | `preg_replace_callback()` | 353189.8 | 971320.8 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | prepared | `preg_replace_callback()` | 357108.6 | 971360.3 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | prepared | Replacer::replace() | 116948.1 | 337590.9 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | oneshot | `strtr()` | 432318.3 | 997910.6 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | oneshot | `preg_replace_callback()` | 353189.8 | 971320.8 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | oneshot | `preg_replace_callback()` | 357108.6 | 971360.3 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | oneshot | Replacer::replace() | 184347.7 | 605793.9 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | prepared | `str_replace()` | 566881.1 | 782153.7 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | prepared | `preg_replace_callback()` | 290631.9 | 779069.5 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | prepared | `preg_replace_callback()` | 288123.3 | 779105.9 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | prepared | Replacer::replace() | 121703.9 | 304556.1 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | oneshot | `str_replace()` | 566881.1 | 782153.7 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | oneshot | `preg_replace_callback()` | 290631.9 | 779069.5 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | oneshot | `preg_replace_callback()` | 288123.3 | 779105.9 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | oneshot | Replacer::replace() | 186547.6 | 542023.7 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | prepared | `str_replace()` | 534636.0 | 728031.7 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | prepared | `preg_replace_callback()` | 284547.4 | 778514.1 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | prepared | `preg_replace_callback()` | 283275.2 | 778551.8 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | prepared | Replacer::replace() | 115886.7 | 336837.6 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | oneshot | `str_replace()` | 534636.0 | 728031.7 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | oneshot | `preg_replace_callback()` | 284547.4 | 778514.1 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | oneshot | `preg_replace_callback()` | 283275.2 | 778551.8 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | oneshot | Replacer::replace() | 184661.8 | 592387.6 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | prepared | `strtr()` | 444916.5 | 995677.7 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | prepared | `preg_replace_callback()` | 361796.5 | 967756.9 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | prepared | `preg_replace_callback()` | 362299.3 | 967792.8 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | prepared | Replacer::replace() | 122921.1 | 310116.0 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | oneshot | `strtr()` | 444916.5 | 995677.7 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | oneshot | `preg_replace_callback()` | 361796.5 | 967756.9 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | oneshot | `preg_replace_callback()` | 362299.3 | 967792.8 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | oneshot | Replacer::replace() | 188351.8 | 560232.9 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | prepared | `strtr()` | 422271.5 | 971407.6 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | prepared | `preg_replace_callback()` | 350753.3 | 966732.7 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | prepared | `preg_replace_callback()` | 353924.2 | 966771.9 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | prepared | Replacer::replace() | 118331.3 | 342048.8 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | oneshot | `strtr()` | 422271.5 | 971407.6 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | oneshot | `preg_replace_callback()` | 350753.3 | 966732.7 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | oneshot | `preg_replace_callback()` | 353924.2 | 966771.9 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | oneshot | Replacer::replace() | 187703.0 | 610259.1 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | prepared | `str_replace()` | 583712.4 | 816583.3 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | prepared | `preg_replace_callback()` | 287025.1 | 784253.4 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | prepared | `preg_replace_callback()` | 290109.8 | 784289.7 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | prepared | Replacer::replace() | 123293.4 | 309224.0 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | oneshot | `str_replace()` | 583712.4 | 816583.3 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | oneshot | `preg_replace_callback()` | 287025.1 | 784253.4 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | oneshot | `preg_replace_callback()` | 290109.8 | 784289.7 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | oneshot | Replacer::replace() | 188667.1 | 546699.1 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | prepared | `str_replace()` | 546431.7 | 760531.1 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | prepared | `preg_replace_callback()` | 285166.5 | 783216.6 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | prepared | `preg_replace_callback()` | 287129.3 | 783258.1 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | prepared | Replacer::replace() | 117932.5 | 341229.0 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | oneshot | `str_replace()` | 546431.7 | 760531.1 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | oneshot | `preg_replace_callback()` | 285166.5 | 783216.6 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | oneshot | `preg_replace_callback()` | 287129.3 | 783258.1 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | oneshot | Replacer::replace() | 185980.0 | 596785.5 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | prepared | `strtr()` | 5897.0 | 15275.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | prepared | `str_replace()` | 5961.7 | 15532.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | prepared | `preg_replace()` | 5175.1 | 19441.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | prepared | `preg_replace()` | 5231.2 | 19498.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | prepared | Replacer::replace() | 144818.2 | 213337.6 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | oneshot | `strtr()` | 5897.0 | 15275.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | oneshot | `str_replace()` | 5961.7 | 15532.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | oneshot | `preg_replace()` | 5175.1 | 19441.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | oneshot | `preg_replace()` | 5231.2 | 19498.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | oneshot | Replacer::replace() | 147380.4 | 219360.3 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | prepared | `strtr()` | 5813.9 | 14737.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | prepared | `str_replace()` | 5871.0 | 14982.1 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | prepared | `preg_replace()` | 5126.4 | 19351.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | prepared | `preg_replace()` | 5129.7 | 19409.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | prepared | Replacer::replace() | 44823.8 | 246078.9 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | oneshot | `strtr()` | 5813.9 | 14737.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | oneshot | `str_replace()` | 5871.0 | 14982.1 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | oneshot | `preg_replace()` | 5126.4 | 19351.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | oneshot | `preg_replace()` | 5129.7 | 19409.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | oneshot | Replacer::replace() | 45868.5 | 252491.7 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | prepared | `strtr()` | 5944.6 | 15647.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | prepared | `str_replace()` | 6005.2 | 15912.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | prepared | `preg_replace()` | 5379.3 | 21273.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | prepared | `preg_replace()` | 5407.8 | 21330.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | prepared | Replacer::replace() | 145556.0 | 215800.8 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | oneshot | `strtr()` | 5944.6 | 15647.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | oneshot | `str_replace()` | 6005.2 | 15912.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | oneshot | `preg_replace()` | 5379.3 | 21273.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | oneshot | `preg_replace()` | 5407.8 | 21330.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | oneshot | Replacer::replace() | 146431.6 | 221173.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | prepared | `strtr()` | 5863.8 | 15087.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | prepared | `str_replace()` | 5901.0 | 15340.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | prepared | `preg_replace()` | 5261.0 | 21155.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | prepared | `preg_replace()` | 5278.5 | 21213.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | prepared | Replacer::replace() | 46709.6 | 248517.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | oneshot | `strtr()` | 5863.8 | 15087.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | oneshot | `str_replace()` | 5901.0 | 15340.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | oneshot | `preg_replace()` | 5261.0 | 21155.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | oneshot | `preg_replace()` | 5278.5 | 21213.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | oneshot | Replacer::replace() | 46648.8 | 254280.9 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | prepared | `strtr()` | 13222.0 | 19855.9 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | prepared | `str_replace()` | 13303.3 | 20064.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | prepared | `preg_replace_callback()` | 5149.3 | 18615.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | prepared | `preg_replace_callback()` | 5168.2 | 18615.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | prepared | `preg_replace_callback()` | 5177.7 | 18650.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | prepared | Replacer::replace() | 220514.5 | 247403.9 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | prepared | `preg_replace()` | 4651.8 | 17495.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | prepared | `preg_replace()` | 4646.1 | 17495.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | prepared | `preg_replace()` | 4668.8 | 17552.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | oneshot | `strtr()` | 13220.0 | 19855.9 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | oneshot | `str_replace()` | 13300.1 | 20064.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | oneshot | `preg_replace_callback()` | 5155.9 | 18615.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | oneshot | `preg_replace_callback()` | 5148.7 | 18615.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | oneshot | `preg_replace_callback()` | 5202.4 | 18650.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | oneshot | Replacer::replace() | 224825.5 | 259423.3 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | oneshot | `preg_replace()` | 4674.6 | 17495.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | oneshot | `preg_replace()` | 4641.2 | 17495.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | oneshot | `preg_replace()` | 4679.1 | 17552.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | prepared | `strtr()` | 12338.8 | 18413.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | prepared | `str_replace()` | 12398.7 | 18609.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | prepared | `preg_replace_callback()` | 5116.3 | 18551.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | prepared | `preg_replace_callback()` | 5105.5 | 18551.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | prepared | `preg_replace_callback()` | 5140.8 | 18589.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | prepared | Replacer::replace() | 56060.8 | 280091.8 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | prepared | `preg_replace()` | 4572.8 | 17391.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | prepared | `preg_replace()` | 4571.0 | 17391.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | prepared | `preg_replace()` | 4595.8 | 17449.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | oneshot | `strtr()` | 12347.7 | 18412.9 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | oneshot | `str_replace()` | 12409.1 | 18609.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | oneshot | `preg_replace_callback()` | 5126.6 | 18551.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | oneshot | `preg_replace_callback()` | 5136.1 | 18551.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | oneshot | `preg_replace_callback()` | 5157.2 | 18589.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | oneshot | Replacer::replace() | 59520.9 | 292617.5 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | oneshot | `preg_replace()` | 4582.4 | 17391.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | oneshot | `preg_replace()` | 4584.9 | 17391.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | oneshot | `preg_replace()` | 4596.5 | 17449.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | prepared | `strtr()` | 13861.6 | 22114.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | prepared | `str_replace()` | 13983.6 | 22322.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | prepared | `preg_replace()` | 4938.7 | 20176.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | prepared | `preg_replace()` | 4966.9 | 20233.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | prepared | Replacer::replace() | 220973.1 | 251136.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | oneshot | `strtr()` | 13861.6 | 22114.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | oneshot | `str_replace()` | 13983.6 | 22322.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | oneshot | `preg_replace()` | 4938.7 | 20176.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | oneshot | `preg_replace()` | 4966.9 | 20233.0 | checks passed |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | oneshot | Replacer::replace() | 223776.0 | 262496.3 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | prepared | `strtr()` | 13012.6 | 19996.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | prepared | `str_replace()` | 13105.3 | 20192.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | prepared | `preg_replace()` | 4886.4 | 19978.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | prepared | `preg_replace()` | 4894.1 | 20036.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | prepared | Replacer::replace() | 57060.3 | 283605.3 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | oneshot | `strtr()` | 13012.6 | 19996.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | oneshot | `str_replace()` | 13105.3 | 20192.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | oneshot | `preg_replace()` | 4886.4 | 19978.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | oneshot | `preg_replace()` | 4894.1 | 20036.0 | checks passed |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | oneshot | Replacer::replace() | 60164.1 | 295474.9 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16144 B | prepared | `str_replace()` | 840717.3 | 1156676.4 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16144 B | prepared | `preg_replace_callback()` | 291303.8 | 779531.4 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16144 B | prepared | `preg_replace_callback()` | 290544.9 | 779565.6 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16144 B | prepared | `preg_replace()` | 281203.5 | 760560.4 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16144 B | prepared | `preg_replace()` | 281416.5 | 760613.5 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16144 B | prepared | Replacer::replace() | 121656.8 | 304498.0 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16144 B | oneshot | `str_replace()` | 840717.3 | 1156676.4 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16144 B | oneshot | `preg_replace_callback()` | 291303.8 | 779531.4 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16144 B | oneshot | `preg_replace_callback()` | 290544.9 | 779565.6 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16144 B | oneshot | `preg_replace()` | 281203.5 | 760560.4 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16144 B | oneshot | `preg_replace()` | 281416.5 | 760613.5 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16144 B | oneshot | Replacer::replace() | 186469.3 | 541968.0 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16144 B | prepared | `str_replace()` | 783459.1 | 1074596.0 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16144 B | prepared | `preg_replace_callback()` | 284477.7 | 778975.3 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16144 B | prepared | `preg_replace_callback()` | 284297.7 | 779014.8 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16144 B | prepared | `preg_replace()` | 275897.1 | 760488.2 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16144 B | prepared | `preg_replace()` | 276456.6 | 760545.0 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16144 B | prepared | Replacer::replace() | 116575.9 | 336801.2 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16144 B | oneshot | `str_replace()` | 783459.1 | 1074596.0 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16144 B | oneshot | `preg_replace_callback()` | 284477.7 | 778975.3 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16144 B | oneshot | `preg_replace_callback()` | 284297.7 | 779014.8 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16144 B | oneshot | `preg_replace()` | 275897.1 | 760488.2 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16144 B | oneshot | `preg_replace()` | 276456.6 | 760545.0 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16144 B | oneshot | Replacer::replace() | 183323.1 | 592351.5 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 16896 B | prepared | `str_replace()` | 857829.2 | 1177317.7 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 16896 B | prepared | `preg_replace_callback()` | 289298.2 | 779088.8 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 16896 B | prepared | `preg_replace_callback()` | 289864.0 | 779123.6 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 16896 B | prepared | Replacer::replace() | 121354.1 | 304580.3 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 16896 B | oneshot | `str_replace()` | 857829.2 | 1177317.7 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 16896 B | oneshot | `preg_replace_callback()` | 289298.2 | 779088.8 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 16896 B | oneshot | `preg_replace_callback()` | 289864.0 | 779123.6 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 16896 B | oneshot | Replacer::replace() | 187382.5 | 542344.6 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 16896 B | prepared | `str_replace()` | 801970.0 | 1093937.0 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 16896 B | prepared | `preg_replace_callback()` | 283676.8 | 778533.1 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 16896 B | prepared | `preg_replace_callback()` | 284383.7 | 778569.8 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 16896 B | prepared | Replacer::replace() | 116272.0 | 336862.1 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 16896 B | oneshot | `str_replace()` | 801970.0 | 1093937.0 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 16896 B | oneshot | `preg_replace_callback()` | 283676.8 | 778533.1 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 16896 B | oneshot | `preg_replace_callback()` | 284383.7 | 778569.8 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 16896 B | oneshot | Replacer::replace() | 183001.5 | 592708.4 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16288 B | prepared | `str_replace()` | 845744.0 | 1162349.4 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16288 B | prepared | `preg_replace_callback()` | 289223.4 | 779141.4 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16288 B | prepared | `preg_replace_callback()` | 289256.9 | 779175.5 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16288 B | prepared | `preg_replace()` | 281613.9 | 761864.0 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16288 B | prepared | `preg_replace()` | 283155.5 | 761920.3 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16288 B | prepared | Replacer::replace() | 121298.5 | 304474.9 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16288 B | oneshot | `str_replace()` | 845744.0 | 1162349.4 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16288 B | oneshot | `preg_replace_callback()` | 289223.4 | 779141.4 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16288 B | oneshot | `preg_replace_callback()` | 289256.9 | 779175.5 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16288 B | oneshot | `preg_replace()` | 281613.9 | 761864.0 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16288 B | oneshot | `preg_replace()` | 283155.5 | 761920.3 | checks passed |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16288 B | oneshot | Replacer::replace() | 186761.3 | 541943.8 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16288 B | prepared | `str_replace()` | 789438.9 | 1079918.7 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16288 B | prepared | `preg_replace_callback()` | 284447.4 | 778585.3 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16288 B | prepared | `preg_replace_callback()` | 284401.9† | 778625.0† | † |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16288 B | prepared | `preg_replace()` | 276814.0 | 761649.6 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16288 B | prepared | `preg_replace()` | 275591.0 | 761707.7 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16288 B | prepared | Replacer::replace() | 116761.9 | 336778.0 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16288 B | oneshot | `str_replace()` | 789438.9 | 1079918.7 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16288 B | oneshot | `preg_replace_callback()` | 284447.4 | 778585.3 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16288 B | oneshot | `preg_replace_callback()` | 284401.9† | 778625.0† | † |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16288 B | oneshot | `preg_replace()` | 276814.0 | 761649.6 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16288 B | oneshot | `preg_replace()` | 275591.0 | 761707.7 | checks passed |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16288 B | oneshot | Replacer::replace() | 183957.5 | 592328.3 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100; keys {{…}} | prepared | `strtr()` | 3292823.3 | 17197985.1 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100; keys {{…}} | prepared | `preg_replace_callback()` | 339340.4 | 888362.1 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100; keys {{…}} | prepared | `preg_replace_callback()` | 332913.7 | 872404.1 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100; keys {{…}} | prepared | Replacer::replace() | 5344446.2 | 18513501.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100; keys {{…}} | oneshot | `strtr()` | 3292823.3 | 17197985.1 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100; keys {{…}} | oneshot | `preg_replace_callback()` | 339340.4 | 888362.1 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100; keys {{…}} | oneshot | `preg_replace_callback()` | 332913.7 | 872404.1 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100; keys {{…}} | oneshot | Replacer::replace() | 6855884.8 | 22439907.4 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100; keys {{…}} | prepared | `strtr()` | 2716720.4 | 13010887.8 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100; keys {{…}} | prepared | `preg_replace_callback()` | 339917.4† | 885308.6† | † |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100; keys {{…}} | prepared | `preg_replace_callback()` | 328661.9 | 869861.3 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100; keys {{…}} | prepared | Replacer::replace() | 4902056.7 | 20606762.3 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100; keys {{…}} | oneshot | `strtr()` | 2716720.4 | 13010887.8 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100; keys {{…}} | oneshot | `preg_replace_callback()` | 339917.4† | 885308.6† | † |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100; keys {{…}} | oneshot | `preg_replace_callback()` | 328661.9 | 869861.3 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100; keys {{…}} | oneshot | Replacer::replace() | 6364228.2 | 24565459.4 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000; keys {{…}} | prepared | `strtr()` | 3946820.1 | 18509058.6 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000; keys {{…}} | prepared | `preg_replace_callback()` | 10695261.2 | 22549770.8 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000; keys {{…}} | prepared | `preg_replace_callback()` | 893771.3 | 2336526.9 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000; keys {{…}} | prepared | Replacer::replace() | 5726535.0 | 18710219.5 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000; keys {{…}} | oneshot | `strtr()` | 3946820.1 | 18509058.6 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000; keys {{…}} | oneshot | `preg_replace_callback()` | 10695261.2 | 22549770.8 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000; keys {{…}} | oneshot | `preg_replace_callback()` | 893771.3 | 2336526.9 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000; keys {{…}} | oneshot | Replacer::replace() | 29900371.0 | 56187445.7 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000; keys {{…}} | prepared | `strtr()` | 3362916.6 | 14401465.1 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000; keys {{…}} | prepared | `preg_replace_callback()` | 10350431.6 | 22518484.0 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000; keys {{…}} | prepared | `preg_replace_callback()` | 936631.9 | 2312360.2 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000; keys {{…}} | prepared | Replacer::replace() | 5282451.9 | 20788192.6 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000; keys {{…}} | oneshot | `strtr()` | 3362916.6 | 14401465.1 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000; keys {{…}} | oneshot | `preg_replace_callback()` | 10350431.6 | 22518484.0 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000; keys {{…}} | oneshot | `preg_replace_callback()` | 936631.9 | 2312360.2 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000; keys {{…}} | oneshot | Replacer::replace() | 29764904.3 | 58657606.7 | checks passed |
| gcc15 | 820 B; dictionary of 10 keys; key lengths 13–20 B; replacements: 11; keys {{…}}; output 860 B | prepared | `strtr()` | 4160.1 | 19578.0 | checks passed |
| gcc15 | 820 B; dictionary of 10 keys; key lengths 13–20 B; replacements: 11; keys {{…}}; output 860 B | prepared | `preg_replace_callback()` | 7536.4 | 22384.1 | checks passed |
| gcc15 | 820 B; dictionary of 10 keys; key lengths 13–20 B; replacements: 11; keys {{…}}; output 860 B | prepared | `preg_replace_callback()` | 7514.7 | 22272.0 | checks passed |
| gcc15 | 820 B; dictionary of 10 keys; key lengths 13–20 B; replacements: 11; keys {{…}}; output 860 B | prepared | `preg_replace_callback()` | 7475.1 | 22307.0 | checks passed |
| gcc15 | 820 B; dictionary of 10 keys; key lengths 13–20 B; replacements: 11; keys {{…}}; output 860 B | prepared | `preg_replace_callback()` | 5939.8 | 21461.0 | checks passed |
| gcc15 | 820 B; dictionary of 10 keys; key lengths 13–20 B; replacements: 11; keys {{…}}; output 860 B | prepared | Replacer::replace() | 5053.6 | 18197.0 | checks passed |
| gcc15 | 820 B; dictionary of 10 keys; key lengths 13–20 B; replacements: 11; keys {{…}}; output 860 B | oneshot | `strtr()` | 4160.1 | 19578.0 | checks passed |
| gcc15 | 820 B; dictionary of 10 keys; key lengths 13–20 B; replacements: 11; keys {{…}}; output 860 B | oneshot | `preg_replace_callback()` | 7536.4 | 22384.1 | checks passed |
| gcc15 | 820 B; dictionary of 10 keys; key lengths 13–20 B; replacements: 11; keys {{…}}; output 860 B | oneshot | `preg_replace_callback()` | 7514.7 | 22272.0 | checks passed |
| gcc15 | 820 B; dictionary of 10 keys; key lengths 13–20 B; replacements: 11; keys {{…}}; output 860 B | oneshot | `preg_replace_callback()` | 7475.1 | 22307.0 | checks passed |
| gcc15 | 820 B; dictionary of 10 keys; key lengths 13–20 B; replacements: 11; keys {{…}}; output 860 B | oneshot | `preg_replace_callback()` | 5939.8 | 21461.0 | checks passed |
| gcc15 | 820 B; dictionary of 10 keys; key lengths 13–20 B; replacements: 11; keys {{…}}; output 860 B | oneshot | Replacer::replace() | 18908.7 | 71662.0 | checks passed |
| clang21 | 820 B; dictionary of 10 keys; key lengths 13–20 B; replacements: 11; keys {{…}}; output 860 B | prepared | `strtr()` | 3675.2 | 17012.0 | checks passed |
| clang21 | 820 B; dictionary of 10 keys; key lengths 13–20 B; replacements: 11; keys {{…}}; output 860 B | prepared | `preg_replace_callback()` | 7785.7 | 21995.0 | checks passed |
| clang21 | 820 B; dictionary of 10 keys; key lengths 13–20 B; replacements: 11; keys {{…}}; output 860 B | prepared | `preg_replace_callback()` | 7781.6 | 21883.0 | checks passed |
| clang21 | 820 B; dictionary of 10 keys; key lengths 13–20 B; replacements: 11; keys {{…}}; output 860 B | prepared | `preg_replace_callback()` | 7914.3 | 21921.0 | checks passed |
| clang21 | 820 B; dictionary of 10 keys; key lengths 13–20 B; replacements: 11; keys {{…}}; output 860 B | prepared | `preg_replace_callback()` | 5976.6 | 21123.0 | checks passed |
| clang21 | 820 B; dictionary of 10 keys; key lengths 13–20 B; replacements: 11; keys {{…}}; output 860 B | prepared | Replacer::replace() | 4647.9 | 19628.0 | checks passed |
| clang21 | 820 B; dictionary of 10 keys; key lengths 13–20 B; replacements: 11; keys {{…}}; output 860 B | oneshot | `strtr()` | 3675.2 | 17012.0 | checks passed |
| clang21 | 820 B; dictionary of 10 keys; key lengths 13–20 B; replacements: 11; keys {{…}}; output 860 B | oneshot | `preg_replace_callback()` | 7785.7 | 21995.0 | checks passed |
| clang21 | 820 B; dictionary of 10 keys; key lengths 13–20 B; replacements: 11; keys {{…}}; output 860 B | oneshot | `preg_replace_callback()` | 7781.6 | 21883.0 | checks passed |
| clang21 | 820 B; dictionary of 10 keys; key lengths 13–20 B; replacements: 11; keys {{…}}; output 860 B | oneshot | `preg_replace_callback()` | 7914.3 | 21921.0 | checks passed |
| clang21 | 820 B; dictionary of 10 keys; key lengths 13–20 B; replacements: 11; keys {{…}}; output 860 B | oneshot | `preg_replace_callback()` | 5976.6 | 21123.0 | checks passed |
| clang21 | 820 B; dictionary of 10 keys; key lengths 13–20 B; replacements: 11; keys {{…}}; output 860 B | oneshot | Replacer::replace() | 17931.5 | 74804.0 | checks passed |
| gcc15 | 7301 B; dictionary of 128 keys; key lengths 4–28 B; replacements: 4; output 7372 B | prepared | `strtr()` | 3913354.6 | 9826413.3 | checks passed |
| gcc15 | 7301 B; dictionary of 128 keys; key lengths 4–28 B; replacements: 4; output 7372 B | prepared | `preg_replace_callback()` | 217071.3 | 755943.9 | checks passed |
| gcc15 | 7301 B; dictionary of 128 keys; key lengths 4–28 B; replacements: 4; output 7372 B | prepared | `preg_replace_callback()` | 216760.0 | 755979.7 | checks passed |
| gcc15 | 7301 B; dictionary of 128 keys; key lengths 4–28 B; replacements: 4; output 7372 B | prepared | Replacer::replace() | 44063.8 | 136543.6 | checks passed |
| gcc15 | 7301 B; dictionary of 128 keys; key lengths 4–28 B; replacements: 4; output 7372 B | oneshot | `strtr()` | 3913354.6 | 9826413.3 | checks passed |
| gcc15 | 7301 B; dictionary of 128 keys; key lengths 4–28 B; replacements: 4; output 7372 B | oneshot | `preg_replace_callback()` | 217071.3 | 755943.9 | checks passed |
| gcc15 | 7301 B; dictionary of 128 keys; key lengths 4–28 B; replacements: 4; output 7372 B | oneshot | `preg_replace_callback()` | 216760.0 | 755979.7 | checks passed |
| gcc15 | 7301 B; dictionary of 128 keys; key lengths 4–28 B; replacements: 4; output 7372 B | oneshot | Replacer::replace() | 604432.6 | 1581168.6 | checks passed |
| clang21 | 7301 B; dictionary of 128 keys; key lengths 4–28 B; replacements: 4; output 7372 B | prepared | `strtr()` | 3955325.4 | 10069881.9 | checks passed |
| clang21 | 7301 B; dictionary of 128 keys; key lengths 4–28 B; replacements: 4; output 7372 B | prepared | `preg_replace_callback()` | 208263.0 | 755800.8 | checks passed |
| clang21 | 7301 B; dictionary of 128 keys; key lengths 4–28 B; replacements: 4; output 7372 B | prepared | `preg_replace_callback()` | 207326.7 | 755837.8 | checks passed |
| clang21 | 7301 B; dictionary of 128 keys; key lengths 4–28 B; replacements: 4; output 7372 B | prepared | Replacer::replace() | 33561.3 | 149854.1 | checks passed |
| clang21 | 7301 B; dictionary of 128 keys; key lengths 4–28 B; replacements: 4; output 7372 B | oneshot | `strtr()` | 3955325.4 | 10069881.9 | checks passed |
| clang21 | 7301 B; dictionary of 128 keys; key lengths 4–28 B; replacements: 4; output 7372 B | oneshot | `preg_replace_callback()` | 208263.0 | 755800.8 | checks passed |
| clang21 | 7301 B; dictionary of 128 keys; key lengths 4–28 B; replacements: 4; output 7372 B | oneshot | `preg_replace_callback()` | 207326.7 | 755837.8 | checks passed |
| clang21 | 7301 B; dictionary of 128 keys; key lengths 4–28 B; replacements: 4; output 7372 B | oneshot | Replacer::replace() | 613534.3 | 1717671.3 | checks passed |
| gcc15 | 8607 B; dictionary of 64 keys; key lengths 30–69 B; replacements: 9; output 8454 B | prepared | `str_replace()` | 285379.3 | 436321.3 | checks passed |
| gcc15 | 8607 B; dictionary of 64 keys; key lengths 30–69 B; replacements: 9; output 8454 B | prepared | `preg_replace_callback()` | 7036.5 | 26455.0 | checks passed |
| gcc15 | 8607 B; dictionary of 64 keys; key lengths 30–69 B; replacements: 9; output 8454 B | prepared | `preg_replace_callback()` | 7070.1 | 26490.0 | checks passed |
| gcc15 | 8607 B; dictionary of 64 keys; key lengths 30–69 B; replacements: 9; output 8454 B | prepared | Replacer::replace() | 55590.8 | 156874.9 | checks passed |
| gcc15 | 8607 B; dictionary of 64 keys; key lengths 30–69 B; replacements: 9; output 8454 B | oneshot | `str_replace()` | 285379.3 | 436321.3 | checks passed |
| gcc15 | 8607 B; dictionary of 64 keys; key lengths 30–69 B; replacements: 9; output 8454 B | oneshot | `preg_replace_callback()` | 7036.5 | 26455.0 | checks passed |
| gcc15 | 8607 B; dictionary of 64 keys; key lengths 30–69 B; replacements: 9; output 8454 B | oneshot | `preg_replace_callback()` | 7070.1 | 26490.0 | checks passed |
| gcc15 | 8607 B; dictionary of 64 keys; key lengths 30–69 B; replacements: 9; output 8454 B | oneshot | Replacer::replace() | 349800.3 | 1095090.0 | checks passed |
| clang21 | 8607 B; dictionary of 64 keys; key lengths 30–69 B; replacements: 9; output 8454 B | prepared | `str_replace()` | 265190.8 | 394432.0 | checks passed |
| clang21 | 8607 B; dictionary of 64 keys; key lengths 30–69 B; replacements: 9; output 8454 B | prepared | `preg_replace_callback()` | 7043.4 | 26247.0 | checks passed |
| clang21 | 8607 B; dictionary of 64 keys; key lengths 30–69 B; replacements: 9; output 8454 B | prepared | `preg_replace_callback()` | 7056.9 | 26285.0 | checks passed |
| clang21 | 8607 B; dictionary of 64 keys; key lengths 30–69 B; replacements: 9; output 8454 B | prepared | Replacer::replace() | 39932.3 | 172875.0 | checks passed |
| clang21 | 8607 B; dictionary of 64 keys; key lengths 30–69 B; replacements: 9; output 8454 B | oneshot | `str_replace()` | 265190.8 | 394432.0 | checks passed |
| clang21 | 8607 B; dictionary of 64 keys; key lengths 30–69 B; replacements: 9; output 8454 B | oneshot | `preg_replace_callback()` | 7043.4 | 26247.0 | checks passed |
| clang21 | 8607 B; dictionary of 64 keys; key lengths 30–69 B; replacements: 9; output 8454 B | oneshot | `preg_replace_callback()` | 7056.9 | 26285.0 | checks passed |
| clang21 | 8607 B; dictionary of 64 keys; key lengths 30–69 B; replacements: 9; output 8454 B | oneshot | Replacer::replace() | 312154.6 | 1100951.7 | checks passed |
| gcc15 | 69643 B; dictionary of 24 keys; key lengths 24 B; replacements: 3; one replacement value; output 69601 B | prepared | `strtr()` | 399669.8 | 1706798.6 | checks passed |
| gcc15 | 69643 B; dictionary of 24 keys; key lengths 24 B; replacements: 3; one replacement value; output 69601 B | prepared | `preg_replace()` | 18953.1 | 72163.0 | checks passed |
| gcc15 | 69643 B; dictionary of 24 keys; key lengths 24 B; replacements: 3; one replacement value; output 69601 B | prepared | `preg_replace()` | 18995.4 | 72219.9 | checks passed |
| gcc15 | 69643 B; dictionary of 24 keys; key lengths 24 B; replacements: 3; one replacement value; output 69601 B | prepared | Replacer::replace() | 351118.2 | 1011579.4 | checks passed |
| gcc15 | 69643 B; dictionary of 24 keys; key lengths 24 B; replacements: 3; one replacement value; output 69601 B | oneshot | `strtr()` | 399669.8 | 1706798.6 | checks passed |
| gcc15 | 69643 B; dictionary of 24 keys; key lengths 24 B; replacements: 3; one replacement value; output 69601 B | oneshot | `preg_replace()` | 18953.1 | 72163.0 | checks passed |
| gcc15 | 69643 B; dictionary of 24 keys; key lengths 24 B; replacements: 3; one replacement value; output 69601 B | oneshot | `preg_replace()` | 18995.4 | 72219.9 | checks passed |
| gcc15 | 69643 B; dictionary of 24 keys; key lengths 24 B; replacements: 3; one replacement value; output 69601 B | oneshot | Replacer::replace() | 423678.3 | 1280327.8 | checks passed |
| clang21 | 69643 B; dictionary of 24 keys; key lengths 24 B; replacements: 3; one replacement value; output 69601 B | prepared | `strtr()` | 351619.7 | 1454416.7 | checks passed |
| clang21 | 69643 B; dictionary of 24 keys; key lengths 24 B; replacements: 3; one replacement value; output 69601 B | prepared | `preg_replace()` | 18835.5 | 72061.0 | checks passed |
| clang21 | 69643 B; dictionary of 24 keys; key lengths 24 B; replacements: 3; one replacement value; output 69601 B | prepared | `preg_replace()` | 18849.4 | 72119.0 | checks passed |
| clang21 | 69643 B; dictionary of 24 keys; key lengths 24 B; replacements: 3; one replacement value; output 69601 B | prepared | Replacer::replace() | 243850.8 | 1150662.6 | checks passed |
| clang21 | 69643 B; dictionary of 24 keys; key lengths 24 B; replacements: 3; one replacement value; output 69601 B | oneshot | `strtr()` | 351619.7 | 1454416.7 | checks passed |
| clang21 | 69643 B; dictionary of 24 keys; key lengths 24 B; replacements: 3; one replacement value; output 69601 B | oneshot | `preg_replace()` | 18835.5 | 72061.0 | checks passed |
| clang21 | 69643 B; dictionary of 24 keys; key lengths 24 B; replacements: 3; one replacement value; output 69601 B | oneshot | `preg_replace()` | 18849.4 | 72119.0 | checks passed |
| clang21 | 69643 B; dictionary of 24 keys; key lengths 24 B; replacements: 3; one replacement value; output 69601 B | oneshot | Replacer::replace() | 314945.2† | 1436672.0† | † |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 0 | prepared | `strtr()` | 32924198.6 | 93666300.1 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 0 | prepared | `preg_replace_callback()` | 65594940.4 | 219694898.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 0 | prepared | Replacer::replace() | 6738326.1 | 15803675.3 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 0 | oneshot | `strtr()` | 32924198.6 | 93666300.1 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 0 | oneshot | `preg_replace_callback()` | 65594940.4 | 219694898.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 0 | oneshot | Replacer::replace() | 12919032.7 | 24220269.9 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 0 | prepared | `strtr()` | 31312678.8 | 93680959.6 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 0 | prepared | `preg_replace_callback()` | 63841661.2 | 219694835.4 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 0 | prepared | Replacer::replace() | 5433984.5 | 17900774.1 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 0 | oneshot | `strtr()` | 31312678.8 | 93680959.6 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 0 | oneshot | `preg_replace_callback()` | 63841661.2 | 219694835.4 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 0 | oneshot | Replacer::replace() | 12064820.6 | 27084421.2 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 10 | prepared | `strtr()` | 33622696.9 | 93843766.5 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 10 | prepared | `preg_replace_callback()` | 65927278.2 | 219817608.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 10 | prepared | Replacer::replace() | 6936423.5 | 15973042.3 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 10 | oneshot | `strtr()` | 33622696.9 | 93843766.5 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 10 | oneshot | `preg_replace_callback()` | 65927278.2 | 219817608.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 10 | oneshot | Replacer::replace() | 13205504.7 | 24389562.8 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 10 | prepared | `strtr()` | 31535287.1 | 93857546.0 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 10 | prepared | `preg_replace_callback()` | 65125605.2 | 219817195.6 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 10 | prepared | Replacer::replace() | 5609830.5 | 18069807.3 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 10 | oneshot | `strtr()` | 31535287.1 | 93857546.0 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 10 | oneshot | `preg_replace_callback()` | 65125605.2 | 219817195.6 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 10 | oneshot | Replacer::replace() | 12247165.4 | 27253391.7 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 100 | prepared | `strtr()` | 33574198.0 | 93653458.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 100 | prepared | `preg_replace_callback()` | 65035824.8 | 219389814.8 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 100 | prepared | Replacer::replace() | 6955351.9 | 16005775.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 100 | oneshot | `strtr()` | 33574198.0 | 93653458.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 100 | oneshot | `preg_replace_callback()` | 65035824.8 | 219389814.8 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 100 | oneshot | Replacer::replace() | 13258931.8 | 24421781.0 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 100 | prepared | `strtr()` | 31578015.4 | 93658616.6 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 100 | prepared | `preg_replace_callback()` | 63296747.2 | 219386790.0 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 100 | prepared | Replacer::replace() | 5677016.1 | 18099089.9 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 100 | oneshot | `strtr()` | 31578015.4 | 93658616.6 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 100 | oneshot | `preg_replace_callback()` | 63296747.2 | 219386790.0 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 100 | oneshot | Replacer::replace() | 12244036.2 | 27282123.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 500 | prepared | `strtr()` | 33760528.6 | 92789496.9 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 500 | prepared | `preg_replace_callback()` | 63500903.2 | 217264064.2 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 500 | prepared | Replacer::replace() | 7006486.8 | 16110237.9 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 500 | oneshot | `strtr()` | 33760528.6 | 92789496.9 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 500 | oneshot | `preg_replace_callback()` | 63500903.2 | 217264064.2 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 500 | oneshot | Replacer::replace() | 13211754.3 | 24527175.7 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 500 | prepared | `strtr()` | 31618026.2 | 92760563.8 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 500 | prepared | `preg_replace_callback()` | 65468923.4 | 217249699.8 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 500 | prepared | Replacer::replace() | 5828035.7 | 18194265.0 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 500 | oneshot | `strtr()` | 31618026.2 | 92760563.8 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 500 | oneshot | `preg_replace_callback()` | 65468923.4 | 217249699.8 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 500 | oneshot | Replacer::replace() | 12369828.1 | 27378117.7 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 750 | prepared | `strtr()` | 33223136.3 | 92214510.3 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 750 | prepared | `preg_replace_callback()` | 63519917.2 | 216144939.2 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 750 | prepared | Replacer::replace() | 7061524.3 | 16138358.1 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 750 | oneshot | `strtr()` | 33223136.3 | 92214510.3 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 750 | oneshot | `preg_replace_callback()` | 63519917.2 | 216144939.2 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 750 | oneshot | Replacer::replace() | 13283852.6 | 24545158.5 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 750 | prepared | `strtr()` | 31618081.8 | 92168107.0 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 750 | prepared | `preg_replace_callback()` | 64402340.2 | 216123196.6 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 750 | prepared | Replacer::replace() | 5836027.8 | 18218348.5 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 750 | oneshot | `strtr()` | 31618081.8 | 92168107.0 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 750 | oneshot | `preg_replace_callback()` | 64402340.2 | 216123196.6 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 750 | oneshot | Replacer::replace() | 12398534.9 | 27392223.8 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 1000 | prepared | `strtr()` | 32929943.3 | 91608984.2 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 1000 | prepared | `preg_replace_callback()` | 64277863.4 | 214884711.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 1000 | prepared | Replacer::replace() | 7117393.2 | 16182057.8 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 1000 | oneshot | `strtr()` | 32929943.3 | 91608984.2 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 1000 | oneshot | `preg_replace_callback()` | 64277863.4 | 214884711.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 1000 | oneshot | Replacer::replace() | 13447858.7 | 24588873.6 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 1000 | prepared | `strtr()` | 31055018.3 | 91544524.2 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 1000 | prepared | `preg_replace_callback()` | 63179787.8 | 214855606.4 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 1000 | prepared | Replacer::replace() | 5839170.3 | 18258104.4 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 1000 | oneshot | `strtr()` | 31055018.3 | 91544524.2 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 1000 | oneshot | `preg_replace_callback()` | 63179787.8 | 214855606.4 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 1000 | oneshot | Replacer::replace() | 12421293.7 | 27431887.1 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 0 | prepared | `strtr()` | 432144867.0 | 1237127904.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 0 | prepared | `preg_replace_callback()` | 64365486.2 | 219696823.6 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 0 | prepared | Replacer::replace() | 6726533.0 | 15803675.6 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 0 | oneshot | `strtr()` | 432144867.0 | 1237127904.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 0 | oneshot | `preg_replace_callback()` | 64365486.2 | 219696823.6 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 0 | oneshot | Replacer::replace() | 13031763.0 | 24222038.2 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 0 | prepared | `strtr()` | 428969235.0 | 1259290686.0 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 0 | prepared | `preg_replace_callback()` | 63400365.4 | 219696789.6 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 0 | prepared | Replacer::replace() | 5437197.1 | 17900813.1 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 0 | oneshot | `strtr()` | 428969235.0 | 1259290686.0 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 0 | oneshot | `preg_replace_callback()` | 63400365.4 | 219696789.6 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 0 | oneshot | Replacer::replace() | 12176333.6 | 27078511.2 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 10 | prepared | `strtr()` | 432056373.0 | 1236978340.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 10 | prepared | `preg_replace_callback()` | 61570676.2 | 219819774.8 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 10 | prepared | Replacer::replace() | 6962965.6 | 15973047.6 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 10 | oneshot | `strtr()` | 432056373.0 | 1236978340.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 10 | oneshot | `preg_replace_callback()` | 61570676.2 | 219819774.8 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 10 | oneshot | Replacer::replace() | 13415808.1 | 24391415.2 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 10 | prepared | `strtr()` | 428702409.0 | 1259132587.0 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 10 | prepared | `preg_replace_callback()` | 63032424.2 | 219819157.2 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 10 | prepared | Replacer::replace() | 5611672.6 | 18069806.4 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 10 | oneshot | `strtr()` | 428702409.0 | 1259132587.0 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 10 | oneshot | `preg_replace_callback()` | 63032424.2 | 219819157.2 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 10 | oneshot | Replacer::replace() | 12393146.6 | 27247415.4 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100 | prepared | `strtr()` | 434034235.0 | 1233765258.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100 | prepared | `preg_replace_callback()` | 63293954.6 | 219391947.8 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100 | prepared | Replacer::replace() | 6928018.2 | 16004657.5 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100 | oneshot | `strtr()` | 434034235.0 | 1233765258.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100 | oneshot | `preg_replace_callback()` | 63293954.6 | 219391947.8 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100 | oneshot | Replacer::replace() | 13448744.7 | 24424185.0 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100 | prepared | `strtr()` | 429803674.0 | 1255849307.0 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100 | prepared | `preg_replace_callback()` | 62972030.4 | 219389461.0 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100 | prepared | Replacer::replace() | 5709646.5 | 18097993.4 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100 | oneshot | `strtr()` | 429803674.0 | 1255849307.0 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100 | oneshot | `preg_replace_callback()` | 62972030.4 | 219389461.0 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100 | oneshot | Replacer::replace() | 12498696.0 | 27276835.1 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 500 | prepared | `strtr()` | 425693320.0 | 1218942192.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 500 | prepared | `preg_replace_callback()` | 62931383.6 | 217268979.6 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 500 | prepared | Replacer::replace() | 7124142.6 | 16112285.6 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 500 | oneshot | `strtr()` | 425693320.0 | 1218942192.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 500 | oneshot | `preg_replace_callback()` | 62931383.6 | 217268979.6 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 500 | oneshot | Replacer::replace() | 13577505.3 | 24530868.8 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 500 | prepared | `strtr()` | 427451700.0 | 1240725021.0 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 500 | prepared | `preg_replace_callback()` | 62119514.2 | 217254463.0 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 500 | prepared | Replacer::replace() | 5815161.6 | 18196301.9 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 500 | oneshot | `strtr()` | 427451700.0 | 1240725021.0 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 500 | oneshot | `preg_replace_callback()` | 62119514.2 | 217254463.0 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 500 | oneshot | Replacer::replace() | 12527438.4 | 27374204.2 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 750 | prepared | `strtr()` | 419122809.0 | 1210222626.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 750 | prepared | `preg_replace_callback()` | 66011468.8 | 216151012.8 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 750 | prepared | Replacer::replace() | 7187926.7 | 16140580.9 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 750 | oneshot | `strtr()` | 419122809.0 | 1210222626.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 750 | oneshot | `preg_replace_callback()` | 66011468.8 | 216151012.8 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 750 | oneshot | Replacer::replace() | 13540417.8 | 24549070.4 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 750 | prepared | `strtr()` | 425480297.0 | 1231830441.0 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 750 | prepared | `preg_replace_callback()` | 62352376.2 | 216129105.0 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 750 | prepared | Replacer::replace() | 5860677.9 | 18220556.4 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 750 | oneshot | `strtr()` | 425480297.0 | 1231830441.0 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 750 | oneshot | `preg_replace_callback()` | 62352376.2 | 216129105.0 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 750 | oneshot | Replacer::replace() | 12634362.7 | 27388446.6 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 1000 | prepared | `strtr()` | 421765352.0 | 1201002082.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 1000 | prepared | `preg_replace_callback()` | 65762128.0 | 214892228.4 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 1000 | prepared | Replacer::replace() | 7183713.7 | 16184218.6 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 1000 | oneshot | `strtr()` | 421765352.0 | 1201002082.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 1000 | oneshot | `preg_replace_callback()` | 65762128.0 | 214892228.4 | checks passed |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 1000 | oneshot | Replacer::replace() | 13545529.6 | 24594170.9 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 1000 | prepared | `strtr()` | 420012548.0 | 1222424415.0 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 1000 | prepared | `preg_replace_callback()` | 62243091.0 | 214863369.8 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 1000 | prepared | Replacer::replace() | 5961905.1 | 18260239.6 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 1000 | oneshot | `strtr()` | 420012548.0 | 1222424415.0 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 1000 | oneshot | `preg_replace_callback()` | 62243091.0 | 214863369.8 | checks passed |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 1000 | oneshot | Replacer::replace() | 12718416.0 | 27429545.5 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 0 | prepared | `strtr()` | 31138698.0 | 93234917.6 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 0 | prepared | `preg_replace_callback()` | — | — | Over 100 ms per call |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 0 | prepared | Replacer::replace() | 6968097.9 | 15949952.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 0 | oneshot | `strtr()` | 31138698.0 | 93234917.6 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 0 | oneshot | `preg_replace_callback()` | — | — | Over 100 ms per call |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 0 | oneshot | Replacer::replace() | 123163022.5 | 91584503.0 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 0 | prepared | `strtr()` | 29140505.0 | 92777364.7 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 0 | prepared | `preg_replace_callback()` | — | — | Over 100 ms per call |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 0 | prepared | Replacer::replace() | 5545563.6 | 18038475.2 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 0 | oneshot | `strtr()` | 29140505.0 | 92777364.7 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 0 | oneshot | `preg_replace_callback()` | — | — | Over 100 ms per call |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 0 | oneshot | Replacer::replace() | 122859382.5 | 99561355.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 100 | prepared | `strtr()` | 32245740.4 | 93281329.1 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 100 | prepared | `preg_replace_callback()` | — | — | Over 100 ms per call |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 100 | prepared | Replacer::replace() | 7168157.2 | 16180049.6 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 100 | oneshot | `strtr()` | 32245740.4 | 93281329.1 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 100 | oneshot | `preg_replace_callback()` | — | — | Over 100 ms per call |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 100 | oneshot | Replacer::replace() | 121833703.5 | 91812173.5 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 100 | prepared | `strtr()` | 29496757.5 | 92815832.0 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 100 | prepared | `preg_replace_callback()` | — | — | Over 100 ms per call |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 100 | prepared | Replacer::replace() | 5720977.7 | 18264817.8 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 100 | oneshot | `strtr()` | 29496757.5 | 92815832.0 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 100 | oneshot | `preg_replace_callback()` | — | — | Over 100 ms per call |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 100 | oneshot | Replacer::replace() | 130858828.5 | 99784320.5 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 1000 | prepared | `strtr()` | 31297369.8 | 91161317.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 1000 | prepared | `preg_replace_callback()` | — | — | Over 100 ms per call |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 1000 | prepared | Replacer::replace() | 7378027.9 | 16352344.8 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 1000 | oneshot | `strtr()` | 31297369.8 | 91161317.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 1000 | oneshot | `preg_replace_callback()` | — | — | Over 100 ms per call |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 1000 | oneshot | Replacer::replace() | 126059326.5 | 91916418.0 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 1000 | prepared | `strtr()` | 29321188.3 | 90641240.0 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 1000 | prepared | `preg_replace_callback()` | — | — | Over 100 ms per call |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 1000 | prepared | Replacer::replace() | 5912888.2 | 18420220.7 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 1000 | oneshot | `strtr()` | 29321188.3 | 90641240.0 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 1000 | oneshot | `preg_replace_callback()` | — | — | Over 100 ms per call |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 1000 | oneshot | Replacer::replace() | 124758559.5 | 99870683.5 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 5000 | prepared | `strtr()` | 28904546.7 | 81736620.7 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 5000 | prepared | `preg_replace_callback()` | — | — | Over 100 ms per call |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 5000 | prepared | Replacer::replace() | 8314533.6 | 17107135.9 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 5000 | oneshot | `strtr()` | 28904546.7 | 81736620.7 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 5000 | oneshot | `preg_replace_callback()` | — | — | Over 100 ms per call |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 5000 | oneshot | Replacer::replace() | 124608043.5 | 92651567.0 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 5000 | prepared | `strtr()` | 27614818.4 | 80990332.3 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 5000 | prepared | `preg_replace_callback()` | — | — | Over 100 ms per call |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 5000 | prepared | Replacer::replace() | 7106146.8 | 19113233.1 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 5000 | oneshot | `strtr()` | 27614818.4 | 80990332.3 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 5000 | oneshot | `preg_replace_callback()` | — | — | Over 100 ms per call |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 5000 | oneshot | Replacer::replace() | 123408847.5 | 100545396.5 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 7500 | prepared | `strtr()` | 28000110.1 | 76032633.3 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 7500 | prepared | `preg_replace_callback()` | — | — | Over 100 ms per call |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 7500 | prepared | Replacer::replace() | 9030973.3 | 17671951.1 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 7500 | oneshot | `strtr()` | 28000110.1 | 76032633.3 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 7500 | oneshot | `preg_replace_callback()` | — | — | Over 100 ms per call |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 7500 | oneshot | Replacer::replace() | 125554020.5 | 93225939.5 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 7500 | prepared | `strtr()` | 26446066.0 | 75153217.0 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 7500 | prepared | `preg_replace_callback()` | — | — | Over 100 ms per call |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 7500 | prepared | Replacer::replace() | 7962928.7 | 19639528.1 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 7500 | oneshot | `strtr()` | 26446066.0 | 75153217.0 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 7500 | oneshot | `preg_replace_callback()` | — | — | Over 100 ms per call |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 7500 | oneshot | Replacer::replace() | 129410679.0 | 101080626.5 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 10000 | prepared | `strtr()` | 27735174.6 | 70174501.4 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 10000 | prepared | `preg_replace_callback()` | — | — | Over 100 ms per call |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 10000 | prepared | Replacer::replace() | 9708424.3 | 18202330.3 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 10000 | oneshot | `strtr()` | 27735174.6 | 70174501.4 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 10000 | oneshot | `preg_replace_callback()` | — | — | Over 100 ms per call |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 10000 | oneshot | Replacer::replace() | 127820822.0 | 93755430.0 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 10000 | prepared | `strtr()` | 25461611.7 | 69150638.2 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 10000 | prepared | `preg_replace_callback()` | — | — | Over 100 ms per call |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 10000 | prepared | Replacer::replace() | 8718906.8 | 20131183.6 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 10000 | oneshot | `strtr()` | 25461611.7 | 69150638.2 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 10000 | oneshot | `preg_replace_callback()` | — | — | Over 100 ms per call |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 10000 | oneshot | Replacer::replace() | 125677081.5 | 101570445.5 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 0 | prepared | `strtr()` | 402033756.0 | 1227090670.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 0 | prepared | `preg_replace_callback()` | — | — | Over 100 ms per call |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 0 | prepared | Replacer::replace() | 6943913.9 | 16096298.6 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 0 | oneshot | `strtr()` | 402033756.0 | 1227090670.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 0 | oneshot | `preg_replace_callback()` | — | — | Over 100 ms per call |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 0 | oneshot | Replacer::replace() | 123081931.0 | 91941054.0 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 0 | prepared | `strtr()` | 412574245.0 | 1243000097.0 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 0 | prepared | `preg_replace_callback()` | — | — | Over 100 ms per call |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 0 | prepared | Replacer::replace() | 5542134.1 | 18176223.2 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 0 | oneshot | `strtr()` | 412574245.0 | 1243000097.0 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 0 | oneshot | `preg_replace_callback()` | — | — | Over 100 ms per call |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 0 | oneshot | Replacer::replace() | 122046583.5 | 99916535.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 100 | prepared | `strtr()` | 414298772.0 | 1223814971.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 100 | prepared | `preg_replace_callback()` | — | — | Over 100 ms per call |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 100 | prepared | Replacer::replace() | 7363727.1 | 16331246.4 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 100 | oneshot | `strtr()` | 414298772.0 | 1223814971.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 100 | oneshot | `preg_replace_callback()` | — | — | Over 100 ms per call |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 100 | oneshot | Replacer::replace() | 122982894.5 | 92180513.0 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 100 | prepared | `strtr()` | 405871414.0 | 1239666960.0 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 100 | prepared | `preg_replace_callback()` | — | — | Over 100 ms per call |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 100 | prepared | Replacer::replace() | 5788131.0 | 18407471.3 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 100 | oneshot | `strtr()` | 405871414.0 | 1239666960.0 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 100 | oneshot | `preg_replace_callback()` | — | — | Over 100 ms per call |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 100 | oneshot | Replacer::replace() | 124071788.0 | 100151442.5 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000 | prepared | `strtr()` | 408004067.0 | 1191214676.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000 | prepared | `preg_replace_callback()` | — | — | Over 100 ms per call |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000 | prepared | Replacer::replace() | 7497095.1 | 16499269.7 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000 | oneshot | `strtr()` | 408004067.0 | 1191214676.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000 | oneshot | `preg_replace_callback()` | — | — | Over 100 ms per call |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000 | oneshot | Replacer::replace() | 124262863.0 | 92247787.5 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000 | prepared | `strtr()` | 396121430.0 | 1206562643.0 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000 | prepared | `preg_replace_callback()` | — | — | Over 100 ms per call |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000 | prepared | Replacer::replace() | 6197313.1 | 18558953.2 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000 | oneshot | `strtr()` | 396121430.0 | 1206562643.0 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000 | oneshot | `preg_replace_callback()` | — | — | Over 100 ms per call |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000 | oneshot | Replacer::replace() | 126127275.0 | 100203122.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 5000 | prepared | `strtr()` | 350833697.0 | 1046083927.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 5000 | prepared | `preg_replace_callback()` | — | — | Over 100 ms per call |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 5000 | prepared | Replacer::replace() | 8833567.7 | 17239919.4 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 5000 | oneshot | `strtr()` | 350833697.0 | 1046083927.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 5000 | oneshot | `preg_replace_callback()` | — | — | Over 100 ms per call |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 5000 | oneshot | Replacer::replace() | 125365727.0 | 92988208.5 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 5000 | prepared | `strtr()` | 331125637.0 | 1059201909.0 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 5000 | prepared | `preg_replace_callback()` | — | — | Over 100 ms per call |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 5000 | prepared | Replacer::replace() | 7604184.6 | 19239087.6 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 5000 | oneshot | `strtr()` | 331125637.0 | 1059201909.0 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 5000 | oneshot | `preg_replace_callback()` | — | — | Over 100 ms per call |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 5000 | oneshot | Replacer::replace() | 127849449.0 | 100882840.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 7500 | prepared | `strtr()` | 337288178.0 | 958483074.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 7500 | prepared | `preg_replace_callback()` | — | — | Over 100 ms per call |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 7500 | prepared | Replacer::replace() | 9702022.1 | 17793593.6 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 7500 | oneshot | `strtr()` | 337288178.0 | 958483074.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 7500 | oneshot | `preg_replace_callback()` | — | — | Over 100 ms per call |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 7500 | oneshot | Replacer::replace() | 124574739.0 | 93554361.5 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 7500 | prepared | `strtr()` | 326726275.0 | 970254022.0 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 7500 | prepared | `preg_replace_callback()` | — | — | Over 100 ms per call |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 7500 | prepared | Replacer::replace() | 8739709.9 | 19754734.1 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 7500 | oneshot | `strtr()` | 326726275.0 | 970254022.0 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 7500 | oneshot | `preg_replace_callback()` | — | — | Over 100 ms per call |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 7500 | oneshot | Replacer::replace() | 125128324.0 | 101411143.5 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 10000 | prepared | `strtr()` | 306911371.0 | 867427236.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 10000 | prepared | `preg_replace_callback()` | — | — | Over 100 ms per call |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 10000 | prepared | Replacer::replace() | 10616184.2 | 18316975.7 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 10000 | oneshot | `strtr()` | 306911371.0 | 867427236.0 | checks passed |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 10000 | oneshot | `preg_replace_callback()` | — | — | Over 100 ms per call |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 10000 | oneshot | Replacer::replace() | 130385521.0 | 94103552.0 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 10000 | prepared | `strtr()` | 301202899.0 | 877797514.0 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 10000 | prepared | `preg_replace_callback()` | — | — | Over 100 ms per call |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 10000 | prepared | Replacer::replace() | 9762398.8 | 20240237.2 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 10000 | oneshot | `strtr()` | 301202899.0 | 877797514.0 | checks passed |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 10000 | oneshot | `preg_replace_callback()` | — | — | Over 100 ms per call |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 10000 | oneshot | Replacer::replace() | 129977455.0 | 101922124.0 | checks passed |

## Replacer: 1 KiB texts

| Compiler | Replacements | Method | Cycles/call | Instructions/call | Quality |
|---|---:|---|---:|---:|---|
| gcc15 | 0 | `strtr()` | 80524.1 | 357600.2 | checks passed |
| gcc15 | 0 | `str_replace()` | 35160.9 | 58714.7 | checks passed |
| gcc15 | 0 | `preg_replace_callback()` | 21370.5 | 90073.0 | checks passed |
| gcc15 | 0 | `preg_replace_callback()` | 9249.1 | 45685.1 | checks passed |
| gcc15 | 0 | `preg_replace_callback()` | 9318.1 | 45720.0 | checks passed |
| gcc15 | 0 | `Replacer::replace()` (prepared) | 6342.0 | 18721.0 | checks passed |
| gcc15 | 0 | `Replacer::replace()` (one-shot) | 68589.8 | 257347.2 | checks passed |
| gcc15 | 2 | `strtr()` | 77552.0 | 345164.2 | checks passed |
| gcc15 | 2 | `str_replace()` | 35242.3 | 59268.2 | checks passed |
| gcc15 | 2 | `preg_replace_callback()` | 21835.0 | 90484.0 | checks passed |
| gcc15 | 2 | `preg_replace_callback()` | 10275.5 | 47885.1 | checks passed |
| gcc15 | 2 | `preg_replace_callback()` | 10272.1 | 47920.0 | checks passed |
| gcc15 | 2 | `Replacer::replace()` (prepared) | 6665.2 | 20035.0 | † |
| gcc15 | 2 | `Replacer::replace()` (one-shot) | 68517.5 | 257519.1 | checks passed |
| clang21 | 0 | `strtr()` | 76445.6 | 361361.6 | checks passed |
| clang21 | 0 | `str_replace()` | 32797.9 | 51616.2 | checks passed |
| clang21 | 0 | `preg_replace_callback()` | 20923.4 | 90056.0 | checks passed |
| clang21 | 0 | `preg_replace_callback()` | 8960.5 | 45668.0 | checks passed |
| clang21 | 0 | `preg_replace_callback()` | 9017.6 | 45706.0 | checks passed |
| clang21 | 0 | `Replacer::replace()` (prepared) | 5882.9 | 20717.0 | checks passed |
| clang21 | 0 | `Replacer::replace()` (one-shot) | 70631.3 | 277413.2 | checks passed |
| clang21 | 2 | `strtr()` | 75196.1 | 348667.1 | checks passed |
| clang21 | 2 | `str_replace()` | 32760.9 | 52198.3 | checks passed |
| clang21 | 2 | `preg_replace_callback()` | 21399.8 | 90379.9 | checks passed |
| clang21 | 2 | `preg_replace_callback()` | 10210.1 | 47781.0 | checks passed |
| clang21 | 2 | `preg_replace_callback()` | 10236.0 | 47819.0 | checks passed |
| clang21 | 2 | `Replacer::replace()` (prepared) | 6277.0 | 21993.0 | checks passed |
| clang21 | 2 | `Replacer::replace()` (one-shot) | 70684.7 | 277558.2 | checks passed |
