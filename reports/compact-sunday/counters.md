# Absolute cycles and instructions

Counters come from the separate five-pass series.

## clang21

| Case | Stock cycles | Compact cycles | Stock instr. | Compact instr. |
|---|--:|--:|--:|--:|
| banlist12/en/post/clean | 13286.69 | 11997.58 | 22238.51 | 21818.44 |
| banlist12/en/thread/clean | 768143.86 | 706359.54 | 1077145.38 | 1076724.16 |
| banlist12/ru/post/clean | 13614.59 | 12923.16 | 25507.73 | 24916.68 |
| banlist12/es/post/clean | 12863.32 | 11625.01 | 22251.52 | 21831.45 |
| banlist12/ar/post/clean | 18360.35 | 17303.75 | 32904.16 | 32484.16 |
| banlist12/hi/post/clean | 11948.22 | 11117.42 | 22334.62 | 21730.58 |
| banlist12/zh/post/clean | 10399.22 | 9210.37 | 17724.19 | 17262.26 |
| banlist12/zh/thread/clean | 678488.74 | 623298.09 | 852095.40 | 851631.50 |
| banlist12/ja/post/clean | 14967.51 | 13607.45 | 26684.80 | 26222.78 |
| banlist12/ko/post/clean | 14098.56 | 12944.72 | 25026.65 | 24606.64 |
| banlist12/emoji/post/clean | 12147.90 | 10907.61 | 20486.38 | 20066.51 |
| explode/pipe2/4k | 12292.84 | 12371.87 | 41533.40 | 41533.32 |
| explode/colon2/4k | 12270.20 | 12341.11 | 41460.34 | 41460.32 |
| parse-http/body64k | 3922.17 | 3790.42 | 12905.08 | 12905.09 |
| render-template/4k | 30606.61 | 26185.83 | 64605.94 | 60490.24 |
| count-template/4k | 4415.47 | 3731.91 | 8964.13 | 8376.14 |
| boundary/9/absent | 16959.85 | 15062.85 | 25159.50 | 25117.47 |
| boundary/32/early-text (original label: 31) | 148.05 | 150.11 | 562.01 | 577.00 |
| boundary/32/early | 173.51 | 172.26 | 592.01 | 604.01 |
| boundary/31/early | 139.05 | 122.23 | 564.00 | 522.01 |

## gcc15

| Case | Stock cycles | Compact cycles | Stock instr. | Compact instr. |
|---|--:|--:|--:|--:|
| banlist12/en/post/clean | 14153.85 | 12718.05 | 24833.37 | 23403.42 |
| banlist12/en/thread/clean | 812698.86 | 754920.32 | 1140947.24 | 1139518.19 |
| banlist12/ru/post/clean | 14335.05 | 13603.18 | 28581.52 | 27600.56 |
| banlist12/es/post/clean | 13543.43 | 12336.98 | 24793.37 | 23363.27 |
| banlist12/ar/post/clean | 18770.41 | 17870.98 | 35803.95 | 34373.97 |
| banlist12/hi/post/clean | 12516.51 | 11643.93 | 25623.45 | 24351.40 |
| banlist12/zh/post/clean | 10968.02 | 9881.00 | 20288.10 | 18715.06 |
| banlist12/zh/thread/clean | 711034.63 | 660811.34 | 908030.12 | 906453.02 |
| banlist12/ja/post/clean | 15629.13 | 14230.57 | 29556.63 | 27983.50 |
| banlist12/ko/post/clean | 14680.89 | 13556.54 | 27600.51 | 26170.46 |
| banlist12/emoji/post/clean | 12786.81 | 11594.20 | 22991.29 | 21561.37 |
| explode/pipe2/4k | 11640.33 | 11616.13 | 43971.36 | 43971.31 |
| explode/colon2/4k | 11787.42 | 11676.66 | 43920.28 | 43920.32 |
| parse-http/body64k | 4013.62 | 4042.10 | 13240.08 | 13240.09 |
| render-template/4k | 33069.94 | 27689.57 | 79496.46 | 65482.69 |
| count-template/4k | 4709.48 | 3962.96 | 11082.13 | 9080.13 |
| boundary/9/absent | 18092.31 | 16553.95 | 26946.44 | 26803.50 |
| boundary/32/early-text (original label: 31) | 155.27 | 158.82 | 777.00 | 782.00 |
| boundary/32/early | 187.71 | 186.87 | 810.01 | 815.01 |
| boundary/31/early | 152.08 | 123.17 | 764.00 | 621.00 |

