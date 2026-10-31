# Absolute diagnostic counters

Cycles come from a separate three-pass native `bench compare`; instructions below come from the one-second elapsed series.

## gcc15: ca89 → No gram4

| Case | A cycles | B cycles | A instr. | B instr. |
|---|--:|--:|--:|--:|
| banlist12/en/post/clean | 12632.99 | 12647.53 | 23402.06 | 23422.07 |
| banlist12/en/post/early | 155.45 | 154.77 | 529.00 | 529.00 |
| explode/colon2/4k | 11779.16 | 11655.73 | 43832.02 | 43832.02 |
| substr-count/colon2/4k | 4807.04 | 4793.44 | 12630.00 | 12630.01 |
| str-replace/colon2/4k | 14467.87 | 14466.58 | 34480.02 | 34480.03 |
| render-template/4k | 28206.98 | 28148.05 | 65539.12 | 65735.12 |
| route/gram/selective/absent | 15891.20 | 11738.99 | 60712.02 | 45559.02 |
| route/gram/selective/late | 15881.35 | 12351.71 | 60738.02 | 46227.02 |
| route/gram/dense/absent | 13125.99 | 12479.80 | 53395.03 | 51053.02 |
| route/gram/changing/absent | 72576.57 | 47076.03 | 264004.11 | 185773.11 |
| route/twoway/periodic-memory | 120919.28 | 117786.17 | 528654.16 | 526312.19 |
| gram-periodic/ascii/absent | 57052.44 | 144832.86 | 217761.09 | 737126.11 |
| gram-periodic/dna/absent | 56920.50 | 201837.33 | 217437.06 | 1022183.13 |

## gcc15: ca89 → Scalar

| Case | A cycles | B cycles | A instr. | B instr. |
|---|--:|--:|--:|--:|
| banlist12/en/post/clean | 12659.83 | 12704.95 | 23402.06 | 23402.07 |
| banlist12/en/post/early | 154.78 | 157.00 | 529.00 | 529.00 |
| explode/colon2/4k | 11751.64 | 11607.65 | 43832.02 | 43832.02 |
| substr-count/colon2/4k | 4826.17 | 4799.45 | 12630.01 | 12630.01 |
| str-replace/colon2/4k | 14477.06 | 14523.66 | 34480.04 | 34480.03 |
| render-template/4k | 28121.16 | 27762.19 | 65539.11 | 65539.11 |
| route/pair/ascii/absent | 4044.42 | 50037.60 | 18002.01 | 266405.01 |
| route/pair/dna/absent | 4030.33 | 50034.54 | 18002.01 | 266405.01 |
| route/pair/binary/absent | 3997.44 | 50042.41 | 17945.06 | 266405.07 |
| route/gram/selective/absent | 15899.98 | 4714.77 | 60712.01 | 21637.01 |
| route/gram/selective/late | 15882.68 | 5316.19 | 60738.01 | 22273.01 |
| route/gram/dense/absent | 13102.40 | 5727.16 | 53395.01 | 27789.01 |
| route/gram/changing/absent | 72411.23 | 19455.46 | 264004.05 | 92315.03 |
| route/twoway/periodic-memory | 119032.48 | 99977.58 | 528654.21 | 458808.16 |
| route/threshold/8191 | 156163.64 | 157142.80 | 820645.38 | 820645.27 |
| route/threshold/8192 | 2517.27 | 25444.29 | 11346.00 | 135333.01 |
| gram-periodic/ascii/absent | 57061.32 | 132404.66 | 217761.09 | 724338.14 |
| gram-periodic/dna/absent | 56927.98 | 197434.28 | 217437.11 | 1050678.09 |

## clang21: ca89 → No gram4

| Case | A cycles | B cycles | A instr. | B instr. |
|---|--:|--:|--:|--:|
| banlist12/en/post/clean | 11976.57 | 11964.68 | 21807.07 | 21807.06 |
| banlist12/en/post/early | 143.20 | 144.75 | 541.00 | 541.00 |
| explode/colon2/4k | 12616.44 | 12551.88 | 41377.03 | 41377.01 |
| substr-count/colon2/4k | 4988.82 | 4982.60 | 11872.01 | 11872.01 |
| str-replace/colon2/4k | 15038.47 | 15045.34 | 32575.02 | 32575.03 |
| render-template/4k | 26098.57 | 26259.12 | 60443.12 | 60443.12 |
| route/gram/selective/absent | 16551.91 | 11466.42 | 62250.02 | 40037.01 |
| route/gram/selective/late | 16566.84 | 11600.46 | 62277.02 | 40676.02 |
| route/gram/dense/absent | 13278.06 | 12969.44 | 47357.02 | 45875.01 |
| route/gram/changing/absent | 75807.43 | 48737.64 | 234547.09 | 159800.08 |
| route/twoway/periodic-memory | 108461.47 | 108354.56 | 499526.18 | 498044.13 |
| gram-periodic/ascii/absent | 59226.92 | 157859.26 | 221086.10 | 681608.12 |
| gram-periodic/dna/absent | 57072.69 | 200790.53 | 220656.09 | 938036.12 |

## clang21: ca89 → Scalar

| Case | A cycles | B cycles | A instr. | B instr. |
|---|--:|--:|--:|--:|
| banlist12/en/post/clean | 12024.89 | 11933.23 | 21807.07 | 21807.07 |
| banlist12/en/post/early | 142.05 | 143.34 | 541.00 | 541.00 |
| explode/colon2/4k | 12580.26 | 12536.14 | 41377.03 | 41377.02 |
| substr-count/colon2/4k | 4988.73 | 4973.96 | 11872.01 | 11872.01 |
| str-replace/colon2/4k | 14996.70 | 14653.47 | 32575.03 | 32575.02 |
| render-template/4k | 25986.46 | 26087.01 | 60443.11 | 60443.12 |
| route/pair/ascii/absent | 5568.59 | 50262.54 | 28627.01 | 251217.02 |
| route/pair/dna/absent | 5574.05 | 50264.59 | 28627.01 | 251217.02 |
| route/pair/binary/absent | 5580.49 | 50273.42 | 28568.09 | 251217.10 |
| route/gram/selective/absent | 16548.95 | 4901.88 | 62250.01 | 23277.01 |
| route/gram/selective/late | 16100.05 | 5041.23 | 62277.01 | 23886.01 |
| route/gram/dense/absent | 13300.38 | 5952.30 | 47357.01 | 29427.01 |
| route/gram/changing/absent | 71757.06 | 20118.51 | 234547.04 | 95490.04 |
| route/twoway/periodic-memory | 109184.37 | 143722.78 | 499526.18 | 459496.17 |
| route/threshold/8191 | 170010.58 | 173777.70 | 812280.28 | 812280.28 |
| route/threshold/8192 | 3418.11 | 25676.11 | 17363.01 | 128337.01 |
| gram-periodic/ascii/absent | 59263.08 | 156286.09 | 221086.09 | 692320.16 |
| gram-periodic/dna/absent | 59112.92 | 197532.28 | 220656.10 | 985878.16 |

## gcc15: Stock → ca89

| Case | A cycles | B cycles | A instr. | B instr. |
|---|--:|--:|--:|--:|
| route/short9/absent | 18096.15 | 16333.22 | 26946.02 | 26803.02 |
| route/short9/early | 99.05 | 72.83 | 478.00 | 335.00 |
| route/short16/absent | 13291.15 | 11995.75 | 18445.02 | 18302.02 |
| route/short16/early | 121.87 | 90.99 | 569.00 | 426.00 |
| route/short31/absent | 6613.25 | 5840.16 | 11344.01 | 11201.01 |
| route/short31/early | 152.66 | 137.02 | 764.00 | 621.00 |
| route/long/ordinary-miss | 4923.27 | 4907.40 | 7097.01 | 7120.01 |
| route/long/early | 186.20 | 197.63 | 810.00 | 837.00 |
| route/pair/ascii/absent | 319329.02 | 4027.57 | 1644127.08 | 18002.01 |
| route/pair/dna/absent | 319384.46 | 4045.62 | 1644127.07 | 18002.01 |
| route/pair/binary/absent | 319358.61 | 3999.58 | 1644127.13 | 17945.06 |
| route/gram/selective/absent | 87484.67 | 15864.12 | 174998.04 | 60712.03 |
| route/gram/selective/late | 87544.58 | 15874.88 | 175371.04 | 60738.02 |
| route/gram/dense/absent | 91071.43 | 13108.82 | 223862.04 | 53395.02 |
| route/gram/changing/absent | 353376.99 | 72417.18 | 862972.22 | 264004.13 |
| route/twoway/periodic-memory | 716800.09 | 119062.35 | 3470230.38 | 528654.20 |
| route/threshold/8191 | 150936.42 | 159884.99 | 820637.26 | 820645.33 |
| route/threshold/8192 | 159627.11 | 2522.85 | 820831.04 | 11346.00 |
| gram-periodic/ascii/absent | 361028.87 | 57028.30 | 886970.16 | 217761.10 |
| gram-periodic/dna/absent | 199957.23 | 56934.73 | 542345.13 | 217437.10 |
| route/long/early (repeat) | 186.20 | 197.63 | 810.00 | 837.00 |

## clang21: Stock → ca89

| Case | A cycles | B cycles | A instr. | B instr. |
|---|--:|--:|--:|--:|
| route/short9/absent | 16677.72 | 15018.94 | 25159.03 | 25116.02 |
| route/short9/early | 91.05 | 65.48 | 345.00 | 302.00 |
| route/short16/absent | 12277.54 | 10997.42 | 17078.02 | 17035.02 |
| route/short16/early | 114.23 | 78.78 | 406.00 | 363.00 |
| route/short31/absent | 6160.63 | 5543.61 | 10540.01 | 10497.01 |
| route/short31/early | 159.62 | 112.91 | 564.00 | 521.00 |
| route/long/ordinary-miss | 4538.94 | 4519.79 | 6442.01 | 6905.01 |
| route/long/early | 176.96 | 181.90 | 592.00 | 720.00 |
| route/pair/ascii/absent | 548093.18 | 5529.31 | 1635732.13 | 28627.01 |
| route/pair/dna/absent | 548092.52 | 5511.09 | 1635732.13 | 28627.01 |
| route/pair/binary/absent | 548094.96 | 5511.53 | 1635732.21 | 28568.09 |
| route/gram/selective/absent | 83701.86 | 16583.52 | 166618.03 | 62250.04 |
| route/gram/selective/late | 83849.77 | 16607.56 | 166996.04 | 62277.04 |
| route/gram/dense/absent | 83950.36 | 13303.48 | 215482.04 | 47357.02 |
| route/gram/changing/absent | 333432.10 | 75756.43 | 830016.18 | 234547.12 |
| route/twoway/periodic-memory | 1138921.85 | 109231.93 | 3435212.41 | 499526.21 |
| route/threshold/8191 | 274083.54 | 168959.80 | 816338.27 | 812280.27 |
| route/threshold/8192 | 273600.92 | 3377.64 | 816532.06 | 17363.01 |
| gram-periodic/ascii/absent | 333326.43 | 59241.29 | 854012.18 | 221086.11 |
| gram-periodic/dna/absent | 164772.17 | 59084.05 | 525754.13 | 220656.14 |
| route/long/early (repeat) | 176.96 | 181.90 | 592.00 | 720.00 |

