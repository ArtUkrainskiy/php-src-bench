# All observed elapsed increases over 1%

Elapsed time is primary. Cycles¹ come from a separate series; no simultaneous IPC is implied. Instructions are from the indicated elapsed run. Full tables retain original rows; primary tables use the documented Intel focus/quality policy. Increases include noisy and unclear rows, not only confirmed regressions.

## AMD / GCC 15.2

| Case | Stock, µs | ca89, µs | Elapsed change | Stock spread | ca89 spread | Elapsed result | Source |
|---|--:|--:|--:|--:|--:|--:|---|
| banlist12/en/comment/early | 0.0325 | 0.0334 | +2.93% | 4.27% | 0.67% | Noise | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/en/post/early | 0.0326 | 0.0338 | +3.76% | 3.17% | 1.87% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/ru/comment/early | 0.0322 | 0.0335 | +3.86% | 2.23% | 1.92% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/es/post/early | 0.0325 | 0.0329 | +1.27% | 4.20% | 0.70% | Noise | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| explode/pipe2/64k | 45.0716 | 45.7202 | +1.44% | 0.16% | 1.35% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| parse-records/4k | 9.4418 | 9.5843 | +1.51% | 0.73% | 0.44% | Slower | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| parse-query/4k | 26.0120 | 26.2823 | +1.04% | 0.12% | 0.17% | Slower | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| parse-http/small | 0.8447 | 0.8538 | +1.07% | 1.27% | 0.29% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| parse-http/body64k | 0.8381 | 0.8595 | +2.54% | 0.47% | 0.37% | Slower | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| log-filter/thread/late | 41.7024 | 42.1452 | +1.06% | 1.06% | 1.39% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banword/es/comment/absent | 0.0495 | 0.0505 | +1.96% | 0.27% | 1.47% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/ar/comment/early | 0.0330 | 0.0337 | +2.08% | 2.16% | 1.69% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/ar/thread/early | 0.0324 | 0.0331 | +2.18% | 1.86% | 1.09% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/zh/comment/early | 0.0331 | 0.0335 | +1.29% | 2.71% | 1.97% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/ja/comment/early | 0.0317 | 0.0332 | +4.80% | 0.96% | 1.39% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banword/ko/comment/absent | 0.1262 | 0.1277 | +1.12% | 0.08% | 1.05% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/emoji/thread/early | 0.0327 | 0.0337 | +3.33% | 1.89% | 0.81% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| explode-limit2/colon2/short | 0.0476 | 0.0485 | +2.08% | 0.76% | 0.67% | Slower | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| substr-count/colon2/short | 0.0409 | 0.0418 | +2.16% | 0.09% | 0.09% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| explode/colon2/absent | 0.0394 | 0.0406 | +3.12% | 0.41% | 3.77% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| explode/tab/64k | 37.5673 | 38.2193 | +1.74% | 1.65% | 1.71% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| explode/tab/1m | 665.2315 | 675.3657 | +1.52% | 0.25% | 0.44% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| explode/amp/64k | 37.5149 | 37.8937 | +1.01% | 1.07% | 1.92% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| parse-query/small | 1.8370 | 1.8630 | +1.41% | 0.61% | 0.26% | Slower | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| parse-query/64k | 415.6586 | 419.8497 | +1.01% | 0.62% | 0.27% | Slower | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| parse-http/cookie4k | 0.9931 | 1.0061 | +1.31% | 0.38% | 0.04% | Slower | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| find-http-end/incomplete | 0.0308 | 0.0312 | +1.32% | 0.02% | 2.78% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |

### Separate counters

| Case | Stock cycles¹ | ca89 cycles¹ | Cycle change¹ | Stock instructions | ca89 instructions | Instruction change |
|---|--:|--:|--:|--:|--:|--:|
| banlist12/en/comment/early | 146.59 | 150.17 | +2.90% | 536.00 | 536.00 | −0.00% |
| banlist12/en/post/early | 149.08 | 147.80 | −2.42% | 529.00 | 529.00 | +0.00% |
| banlist12/ru/comment/early | 143.33 | 143.63 | −1.63% | 527.00 | 527.00 | +0.00% |
| banlist12/es/post/early | 141.05 | 148.77 | +4.79% | 529.00 | 529.00 | +0.00% |
| explode/pipe2/64k | 207185.39 | 206010.76 | −0.57% | 705785.20 | 705785.33 | +0.00% |
| parse-records/4k | 43246.57 | 43000.58 | −0.75% | 156431.05 | 156431.05 | +0.00% |
| parse-query/4k | 117785.67 | 119095.99 | +0.46% | 438335.74 | 438335.74 | +0.00% |
| parse-http/small | 3793.06 | 3857.46 | +1.70% | 13253.00 | 13253.01 | +0.00% |
| parse-http/body64k | 3799.36 | 3864.24 | +1.60% | 13240.00 | 13240.01 | +0.00% |
| log-filter/thread/late | 195092.37 | 196032.31 | +0.43% | 492191.24 | 492191.36 | +0.00% |
| banword/es/comment/absent | — | — | — | 634.00 | 634.00 | −0.00% |
| banlist12/ar/comment/early | — | — | — | 527.00 | 527.00 | −0.00% |
| banlist12/ar/thread/early | — | — | — | 529.00 | 529.00 | −0.00% |
| banlist12/zh/comment/early | — | — | — | 527.00 | 527.00 | +0.00% |
| banlist12/ja/comment/early | — | — | — | 535.00 | 535.00 | +0.00% |
| banword/ko/comment/absent | — | — | — | 1350.00 | 1350.00 | −0.00% |
| banlist12/emoji/thread/early | — | — | — | 529.00 | 529.00 | −0.00% |
| explode-limit2/colon2/short | — | — | — | 910.00 | 910.00 | −0.00% |
| substr-count/colon2/short | — | — | — | 582.00 | 582.00 | −0.00% |
| explode/colon2/absent | — | — | — | 941.00 | 941.00 | −0.00% |
| explode/tab/64k | — | — | — | 595208.23 | 595208.23 | −0.00% |
| explode/tab/1m | — | — | — | 9376196.12 | 9376194.50 | −0.00% |
| explode/amp/64k | — | — | — | 586610.18 | 586610.36 | +0.00% |
| parse-query/small | — | — | — | 31229.01 | 31229.01 | −0.00% |
| parse-query/64k | — | — | — | 6897041.26 | 6897039.66 | −0.00% |
| parse-http/cookie4k | — | — | — | 16182.00 | 16182.01 | +0.00% |
| find-http-end/incomplete | — | — | — | 451.00 | 451.00 | −0.00% |

## AMD / Clang 21.1

| Case | Stock, µs | ca89, µs | Elapsed change | Stock spread | ca89 spread | Elapsed result | Source |
|---|--:|--:|--:|--:|--:|--:|---|
| banlist12/en/thread/early | 0.0302 | 0.0306 | +1.37% | 1.38% | 0.47% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/ar/post/early | 0.0302 | 0.0308 | +2.15% | 0.29% | 1.87% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| explode/pipe2/4k | 2.7138 | 2.8019 | +3.24% | 1.17% | 0.90% | Slower | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| explode/colon2/short | 0.1036 | 0.1047 | +1.14% | 0.25% | 0.52% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| parse-records/4k | 9.9516 | 10.0725 | +1.22% | 0.59% | 0.51% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| parse-query/4k | 27.2458 | 27.5487 | +1.11% | 0.85% | 0.83% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/ar/comment/early | 0.0304 | 0.0310 | +1.96% | 2.11% | 0.52% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/ar/thread/early | 0.0303 | 0.0306 | +1.20% | 1.08% | 0.63% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/zh/comment/early | 0.0296 | 0.0301 | +1.65% | 0.93% | 1.14% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| substr-count/pipe2/64k | 18.5621 | 18.8166 | +1.37% | 2.16% | 0.05% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| substr-count/crlf/short | 0.0459 | 0.0472 | +2.80% | 2.66% | 1.26% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| explode/crlf/absent | 0.0415 | 0.0420 | +1.18% | 0.05% | 0.93% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| explode/amp/4k | 2.1393 | 2.1943 | +2.57% | 1.00% | 1.17% | Noise | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| find-http-end/small | 0.0331 | 0.0340 | +2.68% | 1.15% | 4.91% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| log-filter/post/late | 0.7476 | 0.7584 | +1.43% | 0.97% | 0.27% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| document/html-phpnet/href="/64k | 0.0392 | 0.0396 | +1.07% | 0.48% | 1.09% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |

### Separate counters

| Case | Stock cycles¹ | ca89 cycles¹ | Cycle change¹ | Stock instructions | ca89 instructions | Instruction change |
|---|--:|--:|--:|--:|--:|--:|
| banlist12/en/thread/early | 131.12 | 132.39 | +0.19% | 541.00 | 541.00 | +0.00% |
| banlist12/ar/post/early | 132.51 | 132.70 | −0.09% | 541.00 | 541.00 | −0.00% |
| explode/pipe2/4k | 12567.90 | 12593.43 | −0.15% | 41512.02 | 41511.02 | −0.00% |
| explode/colon2/short | 474.58 | 471.61 | −1.16% | 1762.00 | 1762.00 | −0.00% |
| parse-records/4k | 45672.63 | 46102.39 | +0.62% | 150929.07 | 150929.07 | +0.00% |
| parse-query/4k | 123968.35 | 124373.12 | +0.33% | 425597.72 | 425597.71 | −0.00% |
| banlist12/ar/comment/early | — | — | — | 541.00 | 541.00 | −0.00% |
| banlist12/ar/thread/early | — | — | — | 541.00 | 541.00 | +0.00% |
| banlist12/zh/comment/early | — | — | — | 543.00 | 543.00 | −0.00% |
| substr-count/pipe2/64k | — | — | — | 195860.13 | 195860.14 | +0.00% |
| substr-count/crlf/short | — | — | — | 641.00 | 641.00 | +0.00% |
| explode/crlf/absent | — | — | — | 943.00 | 943.00 | −0.00% |
| explode/amp/4k | — | — | — | 37173.01 | 37173.02 | +0.00% |
| find-http-end/small | — | — | — | 470.00 | 470.00 | −0.00% |
| log-filter/post/late | — | — | — | 8761.01 | 8761.00 | −0.00% |
| document/html-phpnet/href="/64k | — | — | — | 483.00 | 483.00 | +0.00% |

## Intel / GCC 13.3

| Case | Stock, µs | ca89, µs | Elapsed change | Stock spread | ca89 spread | Elapsed result | Source |
|---|--:|--:|--:|--:|--:|--:|---|
| banlist12/ru/thread/clean | 302.4371 | 310.3364 | +2.61% | 0.24% | 0.36% | Slower | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/ru/thread/late | 302.3368 | 309.8942 | +2.50% | 0.20% | 0.21% | Slower | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/ar/thread/clean | 361.0349 | 370.3597 | +2.58% | 0.37% | 0.33% | Slower | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/ar/thread/late | 360.1934 | 370.3816 | +2.83% | 0.51% | 0.27% | Slower | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/ja/thread/clean | 299.6051 | 306.4130 | +2.27% | 0.33% | 0.34% | Slower | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/ja/thread/late | 300.2276 | 306.7343 | +2.17% | 0.43% | 0.24% | Slower | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/ko/thread/clean | 253.6660 | 259.2468 | +2.20% | 0.33% | 0.25% | Slower | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/ko/thread/late | 254.6328 | 259.9094 | +2.07% | 0.47% | 0.38% | Slower | [gcc13-full233](../data/intel/gcc13-full233.json) |
| explode-limit2/colon2/64k | 1.3229 | 1.3374 | +1.10% | 0.32% | 0.47% | Slower | [gcc13-full233](../data/intel/gcc13-full233.json) |
| explode-limit2/crlf/4k | 0.0943 | 0.0954 | +1.13% | 0.62% | 1.67% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| explode/comma/4k | 2.0251 | 2.0706 | +2.25% | 1.71% | 3.51% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| explode/tab/4k | 1.9630 | 1.9984 | +1.80% | 2.01% | 4.01% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| explode/amp/4k | 1.9321 | 1.9540 | +1.14% | 1.58% | 2.76% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| parse-http/small | 0.8135 | 0.8261 | +1.55% | 0.36% | 0.89% | Slower | [gcc13-full233](../data/intel/gcc13-full233.json) |
| parse-http/cookie4k | 0.9939 | 1.0100 | +1.62% | 0.78% | 0.33% | Slower | [gcc13-full233](../data/intel/gcc13-full233.json) |
| parse-http/body64k | 0.8087 | 0.8264 | +2.19% | 0.48% | 0.34% | Slower | [gcc13-full233](../data/intel/gcc13-full233.json) |
| log-contains/event/comment/early | 0.0113 | 0.0115 | +1.91% | 2.99% | 2.87% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| document/html-phpnet/data-cookieconsent=/4k | 0.8663 | 0.8779 | +1.35% | 0.09% | 0.55% | Slower | [gcc13-full233](../data/intel/gcc13-full233.json) |
| document/js-jquery.min/function/4k | 0.0111 | 0.0114 | +2.71% | 2.31% | 4.54% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| document/js-jquery.min/function/64k | 0.0111 | 0.0114 | +2.30% | 1.97% | 3.54% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |

### Separate counters

| Case | Stock cycles¹ | ca89 cycles¹ | Cycle change¹ | Stock instructions | ca89 instructions | Instruction change |
|---|--:|--:|--:|--:|--:|--:|
| banlist12/ru/thread/clean | 1145533.19 | 1175994.64 | +2.86% | 1260433.09 | 1259619.40 | −0.06% |
| banlist12/ru/thread/late | 1154597.90 | 1187603.11 | +2.86% | 1261353.67 | 1260525.13 | −0.07% |
| banlist12/ar/thread/clean | 1379039.50 | 1442653.14 | +3.52% | 1815690.54 | 1814288.32 | −0.08% |
| banlist12/ar/thread/late | — | — | — | 1816707.06 | 1815278.59 | −0.08% |
| banlist12/ja/thread/clean | 1137577.68 | 1164654.37 | +2.17% | 1405958.03 | 1404405.19 | −0.11% |
| banlist12/ja/thread/late | — | — | — | 1407059.32 | 1405481.29 | −0.11% |
| banlist12/ko/thread/clean | 968272.56 | 988209.07 | +2.11% | 1235852.51 | 1234448.08 | −0.11% |
| banlist12/ko/thread/late | — | — | — | 1236322.40 | 1234916.81 | −0.11% |
| explode-limit2/colon2/64k | — | — | — | 1232.18 | 1232.13 | −0.00% |
| explode-limit2/crlf/4k | — | — | — | 1146.01 | 1146.01 | +0.00% |
| explode/comma/4k | 8084.49 | 7727.46 | −2.63% | 39329.17 | 39329.19 | +0.00% |
| explode/tab/4k | — | — | — | 37931.22 | 37931.16 | −0.00% |
| explode/amp/4k | — | — | — | 38048.27 | 38048.16 | −0.00% |
| parse-http/small | 3084.07 | 3131.71 | +1.45% | 13469.06 | 13469.05 | −0.00% |
| parse-http/cookie4k | — | — | — | 15167.07 | 15167.04 | −0.00% |
| parse-http/body64k | 3101.29 | 3120.80 | +0.63% | 13465.08 | 13465.06 | −0.00% |
| log-contains/event/comment/early | — | — | — | 221.00 | 221.00 | +0.00% |
| document/html-phpnet/data-cookieconsent=/4k | — | — | — | 4659.13 | 4517.06 | −3.05% |
| document/js-jquery.min/function/4k | — | — | — | 223.00 | 223.00 | +0.00% |
| document/js-jquery.min/function/64k | — | — | — | 223.00 | 223.00 | +0.00% |

### Documented focus/quality selection

| Case | Stock, µs | ca89, µs | Elapsed change | Stock spread | ca89 spread | Elapsed result | Source |
|---|--:|--:|--:|--:|--:|--:|---|
| banlist12/ru/thread/clean | 302.2632 | 310.0164 | +2.57% | 0.09% | 0.21% | Slower | [gcc13-focus](../data/intel/gcc13-focus.json) |
| banlist12/ru/thread/late | 302.5665 | 310.3976 | +2.59% | 0.14% | 0.11% | Slower | [gcc13-focus](../data/intel/gcc13-focus.json) |
| banlist12/ar/thread/clean | 361.0349 | 370.3597 | +2.58% | 0.37% | 0.33% | Slower | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/ar/thread/late | 360.1934 | 370.3816 | +2.83% | 0.51% | 0.27% | Slower | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/ja/thread/clean | 299.6051 | 306.4130 | +2.27% | 0.33% | 0.34% | Slower | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/ja/thread/late | 300.2276 | 306.7343 | +2.17% | 0.43% | 0.24% | Slower | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/ko/thread/clean | 253.6660 | 259.2468 | +2.20% | 0.33% | 0.25% | Slower | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/ko/thread/late | 254.6328 | 259.9094 | +2.07% | 0.47% | 0.38% | Slower | [gcc13-full233](../data/intel/gcc13-full233.json) |
| explode-limit2/colon2/64k | 1.3229 | 1.3374 | +1.10% | 0.32% | 0.47% | Slower | [gcc13-full233](../data/intel/gcc13-full233.json) |
| explode-limit2/crlf/4k | 0.0943 | 0.0954 | +1.13% | 0.62% | 1.67% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| explode/comma/4k | 2.0251 | 2.0706 | +2.25% | 1.71% | 3.51% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| explode/tab/4k | 1.9630 | 1.9984 | +1.80% | 2.01% | 4.01% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| explode/amp/4k | 1.9321 | 1.9540 | +1.14% | 1.58% | 2.76% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| parse-http/small | 0.8050 | 0.8211 | +2.00% | 0.32% | 0.36% | Slower | [gcc13-focus](../data/intel/gcc13-focus.json) |
| parse-http/cookie4k | 0.9939 | 1.0100 | +1.62% | 0.78% | 0.33% | Slower | [gcc13-full233](../data/intel/gcc13-full233.json) |
| parse-http/body64k | 0.8063 | 0.8215 | +1.88% | 0.34% | 0.23% | Slower | [gcc13-focus](../data/intel/gcc13-focus.json) |
| log-contains/event/comment/early | 0.0113 | 0.0115 | +1.91% | 2.99% | 2.87% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| document/html-phpnet/data-cookieconsent=/4k | 0.8663 | 0.8779 | +1.35% | 0.09% | 0.55% | Slower | [gcc13-full233](../data/intel/gcc13-full233.json) |
| document/js-jquery.min/function/4k | 0.0111 | 0.0114 | +2.71% | 2.31% | 4.54% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| document/js-jquery.min/function/64k | 0.0111 | 0.0114 | +2.30% | 1.97% | 3.54% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |

### Separate counters

| Case | Stock cycles¹ | ca89 cycles¹ | Cycle change¹ | Stock instructions | ca89 instructions | Instruction change |
|---|--:|--:|--:|--:|--:|--:|
| banlist12/ru/thread/clean | 1145533.19 | 1175994.64 | +2.86% | 1260352.92 | 1259516.76 | −0.07% |
| banlist12/ru/thread/late | 1154597.90 | 1187603.11 | +2.86% | 1261261.04 | 1260427.80 | −0.07% |
| banlist12/ar/thread/clean | 1379039.50 | 1442653.14 | +3.52% | 1815690.54 | 1814288.32 | −0.08% |
| banlist12/ar/thread/late | — | — | — | 1816707.06 | 1815278.59 | −0.08% |
| banlist12/ja/thread/clean | 1137577.68 | 1164654.37 | +2.17% | 1405958.03 | 1404405.19 | −0.11% |
| banlist12/ja/thread/late | — | — | — | 1407059.32 | 1405481.29 | −0.11% |
| banlist12/ko/thread/clean | 968272.56 | 988209.07 | +2.11% | 1235852.51 | 1234448.08 | −0.11% |
| banlist12/ko/thread/late | — | — | — | 1236322.40 | 1234916.81 | −0.11% |
| explode-limit2/colon2/64k | — | — | — | 1232.18 | 1232.13 | −0.00% |
| explode-limit2/crlf/4k | — | — | — | 1146.01 | 1146.01 | +0.00% |
| explode/comma/4k | 8084.49 | 7727.46 | −2.63% | 39329.17 | 39329.19 | +0.00% |
| explode/tab/4k | — | — | — | 37931.22 | 37931.16 | −0.00% |
| explode/amp/4k | — | — | — | 38048.27 | 38048.16 | −0.00% |
| parse-http/small | 3084.07 | 3131.71 | +1.45% | 13469.01 | 13469.01 | −0.00% |
| parse-http/cookie4k | — | — | — | 15167.07 | 15167.04 | −0.00% |
| parse-http/body64k | 3101.29 | 3120.80 | +0.63% | 13465.02 | 13465.02 | +0.00% |
| log-contains/event/comment/early | — | — | — | 221.00 | 221.00 | +0.00% |
| document/html-phpnet/data-cookieconsent=/4k | — | — | — | 4659.13 | 4517.06 | −3.05% |
| document/js-jquery.min/function/4k | — | — | — | 223.00 | 223.00 | +0.00% |
| document/js-jquery.min/function/64k | — | — | — | 223.00 | 223.00 | +0.00% |

## Intel / GCC 14.2

| Case | Stock, µs | ca89, µs | Elapsed change | Stock spread | ca89 spread | Elapsed result | Source |
|---|--:|--:|--:|--:|--:|--:|---|
| banlist12/ar/thread/late | 359.5092 | 363.4974 | +1.11% | 0.87% | 0.75% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| substr-count/crlf/short | 0.0558 | 0.0573 | +2.81% | 2.62% | 1.99% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| explode/comma/4k | 1.9212 | 1.9575 | +1.89% | 2.31% | 1.90% | Noise | [gcc14-full233](../data/intel/gcc14-full233.json) |
| explode/amp/short | 0.0744 | 0.0752 | +1.15% | 1.03% | 3.78% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| explode/amp/4k | 1.9261 | 1.8991 | −1.40% | 4.14% | 5.33% | Noise | [gcc14-full233](../data/intel/gcc14-full233.json) |
| parse-records/4k | 9.3207 | 9.4469 | +1.35% | 0.70% | 0.82% | Slower | [gcc14-full233](../data/intel/gcc14-full233.json) |
| find-http-end/small | 0.0292 | 0.0296 | +1.10% | 0.36% | 1.74% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| log-contains/event/comment/early | 0.0139 | 0.0141 | +1.20% | 3.91% | 3.63% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| document/js-jquery.min/function/4k | 0.0133 | 0.0138 | +3.70% | 4.12% | 5.83% | Noise | [gcc14-full233](../data/intel/gcc14-full233.json) |
| document/js-jquery.min/function/64k | 0.0133 | 0.0136 | +2.19% | 5.45% | 3.08% | Noise | [gcc14-full233](../data/intel/gcc14-full233.json) |

### Separate counters

| Case | Stock cycles¹ | ca89 cycles¹ | Cycle change¹ | Stock instructions | ca89 instructions | Instruction change |
|---|--:|--:|--:|--:|--:|--:|
| banlist12/ar/thread/late | — | — | — | 1864762.13 | 1863313.26 | −0.08% |
| substr-count/crlf/short | — | — | — | 650.00 | 650.01 | +0.00% |
| explode/comma/4k | 7255.98 | 7437.67 | +2.50% | 39329.17 | 39329.14 | −0.00% |
| explode/amp/short | — | — | — | 1572.01 | 1572.01 | +0.00% |
| explode/amp/4k | — | — | — | 38048.17 | 38048.09 | −0.00% |
| parse-records/4k | 35123.37 | 35775.72 | +1.55% | 156341.75 | 156341.75 | −0.00% |
| find-http-end/small | — | — | — | 502.00 | 502.00 | −0.00% |
| log-contains/event/comment/early | — | — | — | 220.00 | 220.00 | −0.00% |
| document/js-jquery.min/function/4k | — | — | — | 222.00 | 222.00 | +0.00% |
| document/js-jquery.min/function/64k | — | — | — | 222.00 | 222.00 | +0.00% |

### Documented focus/quality selection

| Case | Stock, µs | ca89, µs | Elapsed change | Stock spread | ca89 spread | Elapsed result | Source |
|---|--:|--:|--:|--:|--:|--:|---|
| banlist12/ar/thread/late | 359.5092 | 363.4974 | +1.11% | 0.87% | 0.75% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| substr-count/crlf/short | 0.0558 | 0.0573 | +2.81% | 2.62% | 1.99% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| explode/comma/4k | 1.9580 | 1.9571 | −0.05% | 1.81% | 2.39% | Unclear | [gcc14-quality-recheck](../data/intel/gcc14-quality-recheck.json) |
| explode/amp/short | 0.0744 | 0.0752 | +1.15% | 1.03% | 3.78% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| explode/amp/4k | 1.9016 | 1.9615 | +3.15% | 2.39% | 4.51% | Noise | [gcc14-quality-recheck](../data/intel/gcc14-quality-recheck.json) |
| parse-records/4k | 9.3207 | 9.4469 | +1.35% | 0.70% | 0.82% | Slower | [gcc14-full233](../data/intel/gcc14-full233.json) |
| find-http-end/small | 0.0292 | 0.0296 | +1.10% | 0.36% | 1.74% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| log-contains/event/comment/early | 0.0139 | 0.0141 | +1.20% | 3.91% | 3.63% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| document/js-jquery.min/function/4k | 0.0139 | 0.0140 | +1.40% | 2.32% | 3.39% | Slower | [gcc14-quality-recheck](../data/intel/gcc14-quality-recheck.json) |
| document/js-jquery.min/function/64k | 0.0138 | 0.0139 | +0.45% | 2.63% | 3.37% | Unclear | [gcc14-quality-recheck](../data/intel/gcc14-quality-recheck.json) |

### Separate counters

| Case | Stock cycles¹ | ca89 cycles¹ | Cycle change¹ | Stock instructions | ca89 instructions | Instruction change |
|---|--:|--:|--:|--:|--:|--:|
| banlist12/ar/thread/late | — | — | — | 1864762.13 | 1863313.26 | −0.08% |
| substr-count/crlf/short | — | — | — | 650.00 | 650.01 | +0.00% |
| explode/comma/4k | 7255.98 | 7437.67 | +2.50% | 39329.04 | 39329.03 | −0.00% |
| explode/amp/short | — | — | — | 1572.01 | 1572.01 | +0.00% |
| explode/amp/4k | — | — | — | 38048.05 | 38048.04 | −0.00% |
| parse-records/4k | 35123.37 | 35775.72 | +1.55% | 156341.75 | 156341.75 | −0.00% |
| find-http-end/small | — | — | — | 502.00 | 502.00 | −0.00% |
| log-contains/event/comment/early | — | — | — | 220.00 | 220.00 | −0.00% |
| document/js-jquery.min/function/4k | — | — | — | 222.00 | 222.00 | +0.00% |
| document/js-jquery.min/function/64k | — | — | — | 222.00 | 222.00 | +0.00% |

## Intel / Clang 18.1

| Case | Stock, µs | ca89, µs | Elapsed change | Stock spread | ca89 spread | Elapsed result | Source |
|---|--:|--:|--:|--:|--:|--:|---|
| banword/ar/post/absent | 1.1922 | 1.2268 | +2.90% | 0.07% | 3.82% | Noise | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/zh/comment/early | 0.0393 | 0.0397 | +1.15% | 2.32% | 2.16% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/ja/thread/clean | 303.1972 | 308.4958 | +1.75% | 0.78% | 0.35% | Slower | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/ja/thread/late | 303.9483 | 308.2971 | +1.43% | 0.49% | 0.38% | Slower | [clang18-full233](../data/intel/clang18-full233.json) |
| banword/emoji/comment/absent | 0.0602 | 0.0609 | +1.05% | 7.75% | 8.32% | Noise | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/emoji/comment/late | 0.4594 | 0.4645 | +1.10% | 1.03% | 2.00% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| explode/pipe2/short | 0.0871 | 0.0887 | +1.88% | 2.76% | 3.17% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| explode-limit2/pipe2/short | 0.0524 | 0.0533 | +1.72% | 0.89% | 1.87% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| substr-count/pipe2/short | 0.0398 | 0.0404 | +1.44% | 1.08% | 1.80% | Slower | [clang18-full233](../data/intel/clang18-full233.json) |
| explode/pipe2/4k | 2.5269 | 2.5789 | +2.06% | 0.77% | 3.62% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| explode-limit2/colon2/short | 0.0521 | 0.0534 | +2.58% | 2.29% | 1.99% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| explode/colon2/absent | 0.0573 | 0.0591 | +3.17% | 0.48% | 1.72% | Slower | [clang18-full233](../data/intel/clang18-full233.json) |
| substr-count/crlf/short | 0.0593 | 0.0600 | +1.12% | 3.08% | 2.74% | Noise | [clang18-full233](../data/intel/clang18-full233.json) |
| str-replace/crlf/short | 0.1419 | 0.1435 | +1.10% | 1.64% | 2.90% | Noise | [clang18-full233](../data/intel/clang18-full233.json) |
| explode/comma/4k | 2.1561 | 2.1971 | +1.90% | 2.98% | 5.77% | Noise | [clang18-full233](../data/intel/clang18-full233.json) |
| explode/comma/absent | 0.0582 | 0.0590 | +1.36% | 2.86% | 2.65% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| explode/tab/1m | 749.3003 | 768.3172 | +2.54% | 1.09% | 2.54% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| explode/tab/absent | 0.0575 | 0.0582 | +1.23% | 1.49% | 1.58% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| explode/amp/1m | 754.2618 | 765.1310 | +1.44% | 1.64% | 2.30% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| render-template/small | 0.4259 | 0.4331 | +1.71% | 1.66% | 0.66% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| html-contains/link/64k | 0.0244 | 0.0247 | +1.28% | 2.40% | 2.06% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| log-filter/post/clean | 0.8500 | 0.8604 | +1.23% | 1.75% | 3.44% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| log-contains/event/thread/clean | 17.2490 | 18.0763 | +4.80% | 0.08% | 0.09% | Slower | [clang18-full233](../data/intel/clang18-full233.json) |
| log-contains/event/thread/late | 17.2235 | 18.0316 | +4.69% | 0.09% | 0.21% | Slower | [clang18-full233](../data/intel/clang18-full233.json) |
| document/html-phpnet/data-cookieconsent=/4k | 0.8802 | 0.8906 | +1.17% | 1.50% | 0.39% | Slower | [clang18-full233](../data/intel/clang18-full233.json) |
| document/js-jquery.min/function/64k | 0.0137 | 0.0139 | +1.43% | 1.97% | 2.57% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |

### Separate counters

| Case | Stock cycles¹ | ca89 cycles¹ | Cycle change¹ | Stock instructions | ca89 instructions | Instruction change |
|---|--:|--:|--:|--:|--:|--:|
| banword/ar/post/absent | — | — | — | 8144.16 | 8144.13 | −0.00% |
| banlist12/zh/comment/early | — | — | — | 692.02 | 692.01 | −0.00% |
| banlist12/ja/thread/clean | 1150419.25 | 1164748.89 | +1.47% | 1511972.91 | 1395857.17 | −7.68% |
| banlist12/ja/thread/late | — | — | — | 1513131.96 | 1396945.68 | −7.68% |
| banword/emoji/comment/absent | — | — | — | 613.01 | 613.01 | +0.00% |
| banlist12/emoji/comment/late | — | — | — | 6666.17 | 6666.16 | −0.00% |
| explode/pipe2/short | 328.62 | 329.82 | +0.04% | 1589.01 | 1589.01 | +0.00% |
| explode-limit2/pipe2/short | — | — | — | 942.01 | 942.01 | +0.00% |
| substr-count/pipe2/short | — | — | — | 565.00 | 565.00 | −0.00% |
| explode/pipe2/4k | 9672.51 | 9609.63 | −1.00% | 41554.11 | 41554.22 | +0.00% |
| explode-limit2/colon2/short | — | — | — | 934.01 | 934.01 | +0.00% |
| explode/colon2/absent | — | — | — | 984.01 | 984.01 | +0.00% |
| substr-count/crlf/short | — | — | — | 687.01 | 687.01 | +0.00% |
| str-replace/crlf/short | — | — | — | 1704.02 | 1704.01 | −0.00% |
| explode/comma/4k | 7945.58 | 7817.76 | −1.61% | 38436.27 | 38436.21 | −0.00% |
| explode/comma/absent | — | — | — | 958.00 | 958.00 | +0.00% |
| explode/tab/1m | — | — | — | 9070355.10 | 9070357.31 | +0.00% |
| explode/tab/absent | — | — | — | 962.01 | 962.00 | −0.00% |
| explode/amp/1m | — | — | — | 9074886.25 | 9074921.77 | +0.00% |
| render-template/small | — | — | — | 6032.12 | 6032.15 | +0.00% |
| html-contains/link/64k | — | — | — | 397.00 | 397.00 | +0.00% |
| log-filter/post/clean | — | — | — | 9443.05 | 9443.07 | +0.00% |
| log-contains/event/thread/clean | 65398.34 | 69843.68 | +6.80% | 128952.65 | 117648.99 | −8.77% |
| log-contains/event/thread/late | 67136.69 | 68245.00 | +4.93% | 128786.32 | 117500.63 | −8.76% |
| document/html-phpnet/data-cookieconsent=/4k | — | — | — | 5104.10 | 4465.08 | −12.52% |
| document/js-jquery.min/function/64k | — | — | — | 229.00 | 229.00 | +0.00% |

### Documented focus/quality selection

| Case | Stock, µs | ca89, µs | Elapsed change | Stock spread | ca89 spread | Elapsed result | Source |
|---|--:|--:|--:|--:|--:|--:|---|
| banword/ar/post/absent | 1.2091 | 1.2093 | +0.02% | 0.13% | 0.10% | Unclear | [clang18-quality-recheck](../data/intel/clang18-quality-recheck.json) |
| banlist12/zh/comment/early | 0.0393 | 0.0397 | +1.15% | 2.32% | 2.16% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/ja/thread/clean | 303.1972 | 308.4958 | +1.75% | 0.78% | 0.35% | Slower | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/ja/thread/late | 303.9483 | 308.2971 | +1.43% | 0.49% | 0.38% | Slower | [clang18-full233](../data/intel/clang18-full233.json) |
| banword/emoji/comment/absent | 0.0581 | 0.0582 | +0.20% | 2.65% | 3.32% | Unclear | [clang18-quality-recheck](../data/intel/clang18-quality-recheck.json) |
| banlist12/emoji/comment/late | 0.4594 | 0.4645 | +1.10% | 1.03% | 2.00% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| explode/pipe2/short | 0.0871 | 0.0887 | +1.88% | 2.76% | 3.17% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| explode-limit2/pipe2/short | 0.0524 | 0.0533 | +1.72% | 0.89% | 1.87% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| substr-count/pipe2/short | 0.0398 | 0.0404 | +1.44% | 1.08% | 1.80% | Slower | [clang18-full233](../data/intel/clang18-full233.json) |
| explode/pipe2/4k | 2.5269 | 2.5789 | +2.06% | 0.77% | 3.62% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| explode-limit2/colon2/short | 0.0521 | 0.0534 | +2.58% | 2.29% | 1.99% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| explode/colon2/absent | 0.0573 | 0.0591 | +3.17% | 0.48% | 1.72% | Slower | [clang18-full233](../data/intel/clang18-full233.json) |
| substr-count/crlf/short | 0.0594 | 0.0604 | +1.61% | 1.11% | 1.65% | Unclear | [clang18-quality-recheck](../data/intel/clang18-quality-recheck.json) |
| str-replace/crlf/short | 0.1419 | 0.1424 | +0.35% | 0.67% | 0.64% | Unclear | [clang18-quality-recheck](../data/intel/clang18-quality-recheck.json) |
| explode/comma/4k | 2.2031 | 2.1221 | −3.68% | 1.12% | 2.41% | Noise | [clang18-quality-recheck](../data/intel/clang18-quality-recheck.json) |
| explode/comma/absent | 0.0582 | 0.0590 | +1.36% | 2.86% | 2.65% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| explode/tab/1m | 749.3003 | 768.3172 | +2.54% | 1.09% | 2.54% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| explode/tab/absent | 0.0575 | 0.0582 | +1.23% | 1.49% | 1.58% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| explode/amp/1m | 754.2618 | 765.1310 | +1.44% | 1.64% | 2.30% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| render-template/small | 0.4259 | 0.4331 | +1.71% | 1.66% | 0.66% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| html-contains/link/64k | 0.0244 | 0.0247 | +1.28% | 2.40% | 2.06% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| log-filter/post/clean | 0.8500 | 0.8604 | +1.23% | 1.75% | 3.44% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| log-contains/event/thread/clean | 17.2550 | 17.8645 | +3.53% | 0.11% | 1.26% | Slower | [clang18-focus](../data/intel/clang18-focus.json) |
| log-contains/event/thread/late | 17.2360 | 17.9109 | +3.92% | 0.10% | 0.98% | Slower | [clang18-focus](../data/intel/clang18-focus.json) |
| document/html-phpnet/data-cookieconsent=/4k | 0.8802 | 0.8906 | +1.17% | 1.50% | 0.39% | Slower | [clang18-full233](../data/intel/clang18-full233.json) |
| document/js-jquery.min/function/64k | 0.0137 | 0.0139 | +1.43% | 1.97% | 2.57% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |

### Separate counters

| Case | Stock cycles¹ | ca89 cycles¹ | Cycle change¹ | Stock instructions | ca89 instructions | Instruction change |
|---|--:|--:|--:|--:|--:|--:|
| banword/ar/post/absent | — | — | — | 8144.01 | 8144.03 | +0.00% |
| banlist12/zh/comment/early | — | — | — | 692.02 | 692.01 | −0.00% |
| banlist12/ja/thread/clean | 1150419.25 | 1164748.89 | +1.47% | 1511972.91 | 1395857.17 | −7.68% |
| banlist12/ja/thread/late | — | — | — | 1513131.96 | 1396945.68 | −7.68% |
| banword/emoji/comment/absent | — | — | — | 613.00 | 613.00 | +0.00% |
| banlist12/emoji/comment/late | — | — | — | 6666.17 | 6666.16 | −0.00% |
| explode/pipe2/short | 328.62 | 329.82 | +0.04% | 1589.01 | 1589.01 | +0.00% |
| explode-limit2/pipe2/short | — | — | — | 942.01 | 942.01 | +0.00% |
| substr-count/pipe2/short | — | — | — | 565.00 | 565.00 | −0.00% |
| explode/pipe2/4k | 9672.51 | 9609.63 | −1.00% | 41554.11 | 41554.22 | +0.00% |
| explode-limit2/colon2/short | — | — | — | 934.01 | 934.01 | +0.00% |
| explode/colon2/absent | — | — | — | 984.01 | 984.01 | +0.00% |
| substr-count/crlf/short | — | — | — | 687.00 | 687.00 | −0.00% |
| str-replace/crlf/short | — | — | — | 1704.00 | 1704.00 | −0.00% |
| explode/comma/4k | 7945.58 | 7817.76 | −1.61% | 38436.02 | 38436.04 | +0.00% |
| explode/comma/absent | — | — | — | 958.00 | 958.00 | +0.00% |
| explode/tab/1m | — | — | — | 9070355.10 | 9070357.31 | +0.00% |
| explode/tab/absent | — | — | — | 962.01 | 962.00 | −0.00% |
| explode/amp/1m | — | — | — | 9074886.25 | 9074921.77 | +0.00% |
| render-template/small | — | — | — | 6032.12 | 6032.15 | +0.00% |
| html-contains/link/64k | — | — | — | 397.00 | 397.00 | +0.00% |
| log-filter/post/clean | — | — | — | 9443.05 | 9443.07 | +0.00% |
| log-contains/event/thread/clean | 65398.34 | 69843.68 | +6.80% | 128951.39 | 117648.21 | −8.77% |
| log-contains/event/thread/late | 67136.69 | 68245.00 | +4.93% | 128784.22 | 117499.34 | −8.76% |
| document/html-phpnet/data-cookieconsent=/4k | — | — | — | 5104.10 | 4465.08 | −12.52% |
| document/js-jquery.min/function/64k | — | — | — | 229.00 | 229.00 | +0.00% |

## Intel / Clang 20.1

| Case | Stock, µs | ca89, µs | Elapsed change | Stock spread | ca89 spread | Elapsed result | Source |
|---|--:|--:|--:|--:|--:|--:|---|
| banlist12/en/thread/clean | 218.5844 | 227.9387 | +4.28% | 0.24% | 0.21% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| banword/en/thread/absent | 13.2604 | 13.5620 | +2.27% | 0.53% | 3.75% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/en/thread/late | 218.2802 | 227.6828 | +4.31% | 0.25% | 0.13% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/es/thread/clean | 223.6120 | 234.1284 | +4.70% | 0.21% | 0.14% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/es/thread/late | 223.7286 | 234.0853 | +4.63% | 0.14% | 0.19% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/ar/thread/clean | 362.4159 | 369.3155 | +1.90% | 0.21% | 0.19% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/ar/thread/late | 362.0705 | 368.8158 | +1.86% | 0.23% | 0.24% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/hi/thread/clean | 255.3880 | 259.7681 | +1.72% | 0.99% | 1.44% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/hi/thread/late | 255.1912 | 260.6728 | +2.15% | 0.69% | 0.96% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/zh/thread/clean | 194.5178 | 205.1801 | +5.48% | 0.25% | 0.45% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/zh/thread/late | 194.2356 | 204.9184 | +5.50% | 0.13% | 0.25% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/ja/thread/clean | 301.3862 | 307.1255 | +1.90% | 0.23% | 0.29% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| banword/ja/thread/absent | 30.9054 | 31.2379 | +1.08% | 0.25% | 0.32% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/ja/thread/late | 301.7188 | 307.3289 | +1.86% | 0.24% | 0.22% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/ko/thread/clean | 250.6608 | 259.8044 | +3.65% | 0.23% | 0.31% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/ko/thread/late | 251.2605 | 260.8519 | +3.82% | 0.42% | 0.30% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| banword/emoji/comment/absent | 0.0603 | 0.0610 | +1.17% | 4.45% | 10.98% | Noise | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/emoji/thread/clean | 196.9602 | 203.6991 | +3.42% | 0.21% | 0.17% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/emoji/thread/late | 196.3243 | 203.6279 | +3.72% | 0.13% | 0.20% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| substr-count/pipe2/64k | 19.5504 | 19.8854 | +1.71% | 2.36% | 1.34% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| explode-limit2/colon2/short | 0.0477 | 0.0482 | +1.10% | 1.52% | 2.05% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| explode-limit2/colon2/4k | 0.0900 | 0.0922 | +2.44% | 0.87% | 0.63% | Noise | [clang20-full233](../data/intel/clang20-full233.json) |
| explode-limit2/crlf/4k | 0.0906 | 0.0926 | +2.28% | 0.94% | 0.43% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| explode/comma/short | 0.0886 | 0.0892 | +0.67% | 1.39% | 2.07% | Noise | [clang20-full233](../data/intel/clang20-full233.json) |
| explode/tab/short | 0.0905 | 0.0914 | +1.03% | 2.24% | 2.45% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| explode/tab/4k | 2.0309 | 2.1358 | +5.17% | 1.17% | 5.38% | Noise | [clang20-full233](../data/intel/clang20-full233.json) |
| parse-query/small | 1.8623 | 1.9040 | +2.24% | 1.46% | 1.63% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| parse-http/body64k | 0.7736 | 0.7788 | +0.68% | 0.50% | 0.78% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| render-template/small | 0.4157 | 0.4200 | +1.03% | 0.83% | 0.88% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| html-contains/optional-widget/64k | 13.2780 | 13.4728 | +1.47% | 0.21% | 0.22% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| log-contains/event/comment/early | 0.0109 | 0.0110 | +1.03% | 2.59% | 2.17% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| log-contains/event/post/clean | 0.2965 | 0.3106 | +4.77% | 0.09% | 0.16% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| log-contains/event/post/late | 0.2734 | 0.2869 | +4.92% | 0.13% | 0.10% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| document/html-phpnet/data-cookieconsent=/4k | 0.8814 | 0.8923 | +1.24% | 0.36% | 0.68% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| document/js-jquery.min/function/64k | 0.0112 | 0.0114 | +1.33% | 1.99% | 5.04% | Noise | [clang20-full233](../data/intel/clang20-full233.json) |
| document/js-jquery.min/sourceMappingURL=/64k | 13.4336 | 13.5860 | +1.13% | 0.12% | 0.40% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |

### Separate counters

| Case | Stock cycles¹ | ca89 cycles¹ | Cycle change¹ | Stock instructions | ca89 instructions | Instruction change |
|---|--:|--:|--:|--:|--:|--:|
| banlist12/en/thread/clean | 837245.44 | 863666.88 | +3.16% | 1194891.83 | 1076799.88 | −9.88% |
| banword/en/thread/absent | — | — | — | 98948.86 | 98949.70 | +0.00% |
| banlist12/en/thread/late | 902498.31 | 863247.37 | −4.34% | 1195372.55 | 1077227.03 | −9.88% |
| banlist12/es/thread/clean | 852356.11 | 887274.56 | +4.40% | 1197755.67 | 1082092.79 | −9.66% |
| banlist12/es/thread/late | — | — | — | 1198263.14 | 1082562.46 | −9.66% |
| banlist12/ar/thread/clean | 1377509.72 | 1427322.27 | +3.44% | 1882641.65 | 1786066.20 | −5.13% |
| banlist12/ar/thread/late | — | — | — | 1883667.11 | 1787041.96 | −5.13% |
| banlist12/hi/thread/clean | 971791.76 | 991843.08 | +2.30% | 1172860.18 | 1093779.29 | −6.74% |
| banlist12/hi/thread/late | 971278.06 | 1014542.19 | +3.99% | 1174097.53 | 1095129.16 | −6.73% |
| banlist12/zh/thread/clean | 742380.62 | 779811.05 | +5.04% | 955687.66 | 851621.89 | −10.89% |
| banlist12/zh/thread/late | — | — | — | 956019.45 | 851930.69 | −10.89% |
| banlist12/ja/thread/clean | 1142586.59 | 1139271.40 | −0.29% | 1511400.08 | 1395301.16 | −7.68% |
| banword/ja/thread/absent | — | — | — | 197157.67 | 177279.59 | −10.08% |
| banlist12/ja/thread/late | — | — | — | 1512549.52 | 1396360.73 | −7.68% |
| banlist12/ko/thread/clean | 955325.94 | 991497.21 | +3.49% | 1320475.09 | 1225955.91 | −7.16% |
| banlist12/ko/thread/late | — | — | — | 1320954.34 | 1226414.82 | −7.16% |
| banword/emoji/comment/absent | — | — | — | 596.01 | 596.01 | +0.00% |
| banlist12/emoji/thread/clean | 751070.50 | 772342.65 | +2.99% | 1082527.23 | 976931.11 | −9.75% |
| banlist12/emoji/thread/late | — | — | — | 1082944.27 | 977306.78 | −9.75% |
| substr-count/pipe2/64k | — | — | — | 195862.10 | 195861.78 | −0.00% |
| explode-limit2/colon2/short | — | — | — | 886.01 | 886.01 | −0.00% |
| explode-limit2/colon2/4k | — | — | — | 1098.01 | 1098.01 | +0.00% |
| explode-limit2/crlf/4k | — | — | — | 1098.01 | 1098.01 | −0.00% |
| explode/comma/short | 318.81 | 321.63 | +0.89% | 1720.01 | 1720.01 | +0.00% |
| explode/tab/short | — | — | — | 1727.01 | 1727.00 | −0.00% |
| explode/tab/4k | — | — | — | 37024.18 | 37024.17 | −0.00% |
| parse-query/small | — | — | — | 30327.56 | 30327.59 | +0.00% |
| parse-http/body64k | 2937.02 | 2962.24 | +0.95% | 12907.03 | 12907.06 | +0.00% |
| render-template/small | — | — | — | 6021.13 | 6021.15 | +0.00% |
| html-contains/optional-widget/64k | — | — | — | 73478.74 | 64519.23 | −12.19% |
| log-contains/event/comment/early | — | — | — | 214.00 | 214.00 | −0.00% |
| log-contains/event/post/clean | — | — | — | 2534.03 | 2291.03 | −9.59% |
| log-contains/event/post/late | — | — | — | 2367.02 | 2142.04 | −9.50% |
| document/html-phpnet/data-cookieconsent=/4k | — | — | — | 5087.06 | 4448.12 | −12.56% |
| document/js-jquery.min/function/64k | — | — | — | 212.00 | 212.00 | −0.00% |
| document/js-jquery.min/sourceMappingURL=/64k | — | — | — | 73834.41 | 64775.17 | −12.27% |

### Documented focus/quality selection

| Case | Stock, µs | ca89, µs | Elapsed change | Stock spread | ca89 spread | Elapsed result | Source |
|---|--:|--:|--:|--:|--:|--:|---|
| banlist12/en/thread/clean | 217.9654 | 227.5464 | +4.40% | 0.24% | 0.10% | Slower | [clang20-focus](../data/intel/clang20-focus.json) |
| banword/en/thread/absent | 13.2604 | 13.5620 | +2.27% | 0.53% | 3.75% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/en/thread/late | 218.0044 | 227.6592 | +4.43% | 0.15% | 0.14% | Slower | [clang20-focus](../data/intel/clang20-focus.json) |
| banlist12/es/thread/clean | 223.6120 | 234.1284 | +4.70% | 0.21% | 0.14% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/es/thread/late | 223.7286 | 234.0853 | +4.63% | 0.14% | 0.19% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/ar/thread/clean | 362.4159 | 369.3155 | +1.90% | 0.21% | 0.19% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/ar/thread/late | 362.0705 | 368.8158 | +1.86% | 0.23% | 0.24% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/hi/thread/clean | 255.2522 | 259.4026 | +1.63% | 0.53% | 0.64% | Slower | [clang20-focus](../data/intel/clang20-focus.json) |
| banlist12/hi/thread/late | 256.3210 | 259.7873 | +1.35% | 0.42% | 0.72% | Slower | [clang20-focus](../data/intel/clang20-focus.json) |
| banlist12/zh/thread/clean | 194.1849 | 204.7293 | +5.43% | 0.10% | 0.17% | Slower | [clang20-focus](../data/intel/clang20-focus.json) |
| banlist12/zh/thread/late | 194.1845 | 204.3285 | +5.22% | 0.17% | 0.40% | Slower | [clang20-focus](../data/intel/clang20-focus.json) |
| banlist12/ja/thread/clean | 301.3862 | 307.1255 | +1.90% | 0.23% | 0.29% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| banword/ja/thread/absent | 30.9054 | 31.2379 | +1.08% | 0.25% | 0.32% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/ja/thread/late | 301.7188 | 307.3289 | +1.86% | 0.24% | 0.22% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/ko/thread/clean | 250.6608 | 259.8044 | +3.65% | 0.23% | 0.31% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/ko/thread/late | 251.2605 | 260.8519 | +3.82% | 0.42% | 0.30% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| banword/emoji/comment/absent | 0.0618 | 0.0622 | +0.54% | 3.64% | 3.36% | Unclear | [clang20-quality-recheck](../data/intel/clang20-quality-recheck.json) |
| banlist12/emoji/thread/clean | 196.9602 | 203.6991 | +3.42% | 0.21% | 0.17% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/emoji/thread/late | 196.3243 | 203.6279 | +3.72% | 0.13% | 0.20% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| substr-count/pipe2/64k | 19.5504 | 19.8854 | +1.71% | 2.36% | 1.34% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| explode-limit2/colon2/short | 0.0477 | 0.0482 | +1.10% | 1.52% | 2.05% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| explode-limit2/colon2/4k | 0.0841 | 0.0839 | −0.26% | 1.39% | 1.28% | Unclear | [clang20-quality-recheck](../data/intel/clang20-quality-recheck.json) |
| explode-limit2/crlf/4k | 0.0906 | 0.0926 | +2.28% | 0.94% | 0.43% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| explode/comma/short | 0.0925 | 0.0940 | +1.55% | 1.53% | 5.96% | Noise | [clang20-quality-recheck](../data/intel/clang20-quality-recheck.json) |
| explode/tab/short | 0.0905 | 0.0914 | +1.03% | 2.24% | 2.45% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| explode/tab/4k | 2.0849 | 2.1609 | +3.64% | 2.98% | 2.01% | Unclear | [clang20-quality-recheck](../data/intel/clang20-quality-recheck.json) |
| parse-query/small | 1.8623 | 1.9040 | +2.24% | 1.46% | 1.63% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| parse-http/body64k | 0.7904 | 0.8001 | +1.24% | 2.81% | 2.96% | Unclear | [clang20-focus](../data/intel/clang20-focus.json) |
| render-template/small | 0.4157 | 0.4200 | +1.03% | 0.83% | 0.88% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| html-contains/optional-widget/64k | 13.2780 | 13.4728 | +1.47% | 0.21% | 0.22% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| log-contains/event/comment/early | 0.0109 | 0.0110 | +1.03% | 2.59% | 2.17% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| log-contains/event/post/clean | 0.2965 | 0.3106 | +4.77% | 0.09% | 0.16% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| log-contains/event/post/late | 0.2734 | 0.2869 | +4.92% | 0.13% | 0.10% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| document/html-phpnet/data-cookieconsent=/4k | 0.8814 | 0.8923 | +1.24% | 0.36% | 0.68% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| document/js-jquery.min/function/64k | 0.0117 | 0.0118 | +0.94% | 2.40% | 1.41% | Unclear | [clang20-quality-recheck](../data/intel/clang20-quality-recheck.json) |
| document/js-jquery.min/sourceMappingURL=/64k | 13.4336 | 13.5860 | +1.13% | 0.12% | 0.40% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |

### Separate counters

| Case | Stock cycles¹ | ca89 cycles¹ | Cycle change¹ | Stock instructions | ca89 instructions | Instruction change |
|---|--:|--:|--:|--:|--:|--:|
| banlist12/en/thread/clean | 837245.44 | 863666.88 | +3.16% | 1194834.97 | 1076727.68 | −9.88% |
| banword/en/thread/absent | — | — | — | 98948.86 | 98949.70 | +0.00% |
| banlist12/en/thread/late | 902498.31 | 863247.37 | −4.34% | 1195306.10 | 1077170.31 | −9.88% |
| banlist12/es/thread/clean | 852356.11 | 887274.56 | +4.40% | 1197755.67 | 1082092.79 | −9.66% |
| banlist12/es/thread/late | — | — | — | 1198263.14 | 1082562.46 | −9.66% |
| banlist12/ar/thread/clean | 1377509.72 | 1427322.27 | +3.44% | 1882641.65 | 1786066.20 | −5.13% |
| banlist12/ar/thread/late | — | — | — | 1883667.11 | 1787041.96 | −5.13% |
| banlist12/hi/thread/clean | 971791.76 | 991843.08 | +2.30% | 1172760.92 | 1093682.62 | −6.74% |
| banlist12/hi/thread/late | 971278.06 | 1014542.19 | +3.99% | 1173995.20 | 1095038.42 | −6.73% |
| banlist12/zh/thread/clean | 742380.62 | 779811.05 | +5.04% | 955628.66 | 851557.84 | −10.89% |
| banlist12/zh/thread/late | — | — | — | 955968.93 | 851864.23 | −10.89% |
| banlist12/ja/thread/clean | 1142586.59 | 1139271.40 | −0.29% | 1511400.08 | 1395301.16 | −7.68% |
| banword/ja/thread/absent | — | — | — | 197157.67 | 177279.59 | −10.08% |
| banlist12/ja/thread/late | — | — | — | 1512549.52 | 1396360.73 | −7.68% |
| banlist12/ko/thread/clean | 955325.94 | 991497.21 | +3.49% | 1320475.09 | 1225955.91 | −7.16% |
| banlist12/ko/thread/late | — | — | — | 1320954.34 | 1226414.82 | −7.16% |
| banword/emoji/comment/absent | — | — | — | 596.00 | 596.00 | +0.00% |
| banlist12/emoji/thread/clean | 751070.50 | 772342.65 | +2.99% | 1082527.23 | 976931.11 | −9.75% |
| banlist12/emoji/thread/late | — | — | — | 1082944.27 | 977306.78 | −9.75% |
| substr-count/pipe2/64k | — | — | — | 195862.10 | 195861.78 | −0.00% |
| explode-limit2/colon2/short | — | — | — | 886.01 | 886.01 | −0.00% |
| explode-limit2/colon2/4k | — | — | — | 1098.00 | 1098.00 | −0.00% |
| explode-limit2/crlf/4k | — | — | — | 1098.01 | 1098.01 | −0.00% |
| explode/comma/short | 318.81 | 321.63 | +0.89% | 1720.00 | 1720.00 | −0.00% |
| explode/tab/short | — | — | — | 1727.01 | 1727.00 | −0.00% |
| explode/tab/4k | — | — | — | 37024.02 | 37024.04 | +0.00% |
| parse-query/small | — | — | — | 30327.56 | 30327.59 | +0.00% |
| parse-http/body64k | 2937.02 | 2962.24 | +0.95% | 12907.01 | 12907.01 | +0.00% |
| render-template/small | — | — | — | 6021.13 | 6021.15 | +0.00% |
| html-contains/optional-widget/64k | — | — | — | 73478.74 | 64519.23 | −12.19% |
| log-contains/event/comment/early | — | — | — | 214.00 | 214.00 | −0.00% |
| log-contains/event/post/clean | — | — | — | 2534.03 | 2291.03 | −9.59% |
| log-contains/event/post/late | — | — | — | 2367.02 | 2142.04 | −9.50% |
| document/html-phpnet/data-cookieconsent=/4k | — | — | — | 5087.06 | 4448.12 | −12.56% |
| document/js-jquery.min/function/64k | — | — | — | 212.00 | 212.00 | −0.00% |
| document/js-jquery.min/sourceMappingURL=/64k | — | — | — | 73834.41 | 64775.17 | −12.27% |
