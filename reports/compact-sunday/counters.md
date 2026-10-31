# Absolute cycles and instructions

Counters come from the separate five-pass series.

## Clang 21.1

| Case | master cycles | compact cycles | master instr. | compact instr. |
|---|--:|--:|--:|--:|
| English moderation post | 13286.69 | 11997.58 | 22238.51 | 21818.44 |
| English moderation thread | 768143.86 | 706359.54 | 1077145.38 | 1076724.16 |
| Russian moderation post | 13614.59 | 12923.16 | 25507.73 | 24916.68 |
| Spanish moderation post | 12863.32 | 11625.01 | 22251.52 | 21831.45 |
| Arabic moderation post | 18360.35 | 17303.75 | 32904.16 | 32484.16 |
| Hindi moderation post | 11948.22 | 11117.42 | 22334.62 | 21730.58 |
| Chinese moderation post | 10399.22 | 9210.37 | 17724.19 | 17262.26 |
| Chinese moderation thread | 678488.74 | 623298.09 | 852095.40 | 851631.50 |
| Japanese moderation post | 14967.51 | 13607.45 | 26684.80 | 26222.78 |
| Korean moderation post | 14098.56 | 12944.72 | 25026.65 | 24606.64 |
| Mixed emoji moderation post | 12147.90 | 10907.61 | 20486.38 | 20066.51 |
| Split fields on two pipes | 12292.84 | 12371.87 | 41533.40 | 41533.32 |
| Split fields on `::` | 12270.20 | 12341.11 | 41460.34 | 41460.32 |
| Parse HTTP headers | 3922.17 | 3790.42 | 12905.08 | 12905.09 |
| Replace template placeholders | 30606.61 | 26185.83 | 64605.94 | 60490.24 |
| Count `{{order.id}}` slots | 4415.47 | 3731.91 | 8964.13 | 8376.14 |
| 9-byte search (no match) | 16959.85 | 15062.85 | 25159.50 | 25117.47 |
| 32-byte early match (text) | 148.05 | 150.11 | 562.01 | 577.00 |
| 32-byte early match (repeated a) | 173.51 | 172.26 | 592.01 | 604.01 |
| 31-byte early match | 139.05 | 122.23 | 564.00 | 522.01 |

## GCC 15.2

| Case | master cycles | compact cycles | master instr. | compact instr. |
|---|--:|--:|--:|--:|
| English moderation post | 14153.85 | 12718.05 | 24833.37 | 23403.42 |
| English moderation thread | 812698.86 | 754920.32 | 1140947.24 | 1139518.19 |
| Russian moderation post | 14335.05 | 13603.18 | 28581.52 | 27600.56 |
| Spanish moderation post | 13543.43 | 12336.98 | 24793.37 | 23363.27 |
| Arabic moderation post | 18770.41 | 17870.98 | 35803.95 | 34373.97 |
| Hindi moderation post | 12516.51 | 11643.93 | 25623.45 | 24351.40 |
| Chinese moderation post | 10968.02 | 9881.00 | 20288.10 | 18715.06 |
| Chinese moderation thread | 711034.63 | 660811.34 | 908030.12 | 906453.02 |
| Japanese moderation post | 15629.13 | 14230.57 | 29556.63 | 27983.50 |
| Korean moderation post | 14680.89 | 13556.54 | 27600.51 | 26170.46 |
| Mixed emoji moderation post | 12786.81 | 11594.20 | 22991.29 | 21561.37 |
| Split fields on two pipes | 11640.33 | 11616.13 | 43971.36 | 43971.31 |
| Split fields on `::` | 11787.42 | 11676.66 | 43920.28 | 43920.32 |
| Parse HTTP headers | 4013.62 | 4042.10 | 13240.08 | 13240.09 |
| Replace template placeholders | 33069.94 | 27689.57 | 79496.46 | 65482.69 |
| Count `{{order.id}}` slots | 4709.48 | 3962.96 | 11082.13 | 9080.13 |
| 9-byte search (no match) | 18092.31 | 16553.95 | 26946.44 | 26803.50 |
| 32-byte early match (text) | 155.27 | 158.82 | 777.00 | 782.00 |
| 32-byte early match (repeated a) | 187.71 | 186.87 | 810.01 | 815.01 |
| 31-byte early match | 152.08 | 123.17 | 764.00 | 621.00 |
