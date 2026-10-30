# Primary product cases

Elapsed time is primary. Cycles¹ come from a separate series; no simultaneous IPC is implied. Instructions are from the indicated elapsed run. Full tables retain original rows; primary tables use the documented Intel focus/quality policy. Increases include noisy and unclear rows, not only confirmed regressions.

## AMD / GCC 15.2

| Case | Stock, µs | Change, µs | Δ time | Stock spread | Change spread | Result | Source |
|---|--:|--:|--:|--:|--:|--:|---|
| banlist12/en/comment/clean | 0.4995 | 0.5034 | +0.79% | 0.10% | 1.65% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/en/comment/early | 0.0325 | 0.0334 | +2.93% | 4.27% | 0.67% | Noise | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/en/comment/late | 0.5508 | 0.5526 | +0.31% | 0.24% | 0.04% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/en/post/clean | 2.9548 | 2.6760 | −9.43% | 0.05% | 0.13% | Faster | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/en/post/early | 0.0326 | 0.0338 | +3.76% | 3.17% | 1.87% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/en/post/late | 3.0155 | 2.8452 | −5.65% | 0.76% | 0.20% | Faster | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/en/thread/clean | 170.6972 | 158.9640 | −6.87% | 0.05% | 0.12% | Faster | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/en/thread/early | 0.0331 | 0.0332 | +0.14% | 1.36% | 0.46% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/en/thread/late | 170.9937 | 158.9175 | −7.06% | 0.15% | 0.09% | Faster | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/ru/comment/clean | 2.5697 | 2.5442 | −0.99% | 1.99% | 0.06% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/ru/comment/early | 0.0322 | 0.0335 | +3.86% | 2.23% | 1.92% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/ru/comment/late | 2.7381 | 2.7418 | +0.14% | 0.09% | 0.09% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/ru/post/clean | 3.0461 | 2.8732 | −5.68% | 0.09% | 0.29% | Faster | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/ru/post/early | 0.0327 | 0.0320 | −2.32% | 0.43% | 2.47% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/ru/post/late | 3.1922 | 3.0476 | −4.53% | 0.08% | 0.16% | Faster | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/ru/thread/clean | 222.3682 | 217.5858 | −2.15% | 0.01% | 0.06% | Faster | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/ru/thread/early | 0.0334 | 0.0337 | +0.82% | 0.16% | 1.88% | Noise | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/ru/thread/late | 221.4095 | 216.4181 | −2.25% | 0.07% | 0.02% | Faster | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/es/comment/clean | 0.5678 | 0.5677 | −0.02% | 0.19% | 0.10% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/es/post/clean | 2.8571 | 2.5900 | −9.35% | 0.07% | 0.18% | Faster | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/es/post/early | 0.0325 | 0.0329 | +1.27% | 4.20% | 0.70% | Noise | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/es/thread/clean | 176.5150 | 165.3601 | −6.32% | 0.06% | 0.08% | Faster | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/ar/comment/clean | 2.0706 | 2.0786 | +0.39% | 0.06% | 0.48% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/ar/comment/late | 2.3430 | 2.3414 | −0.07% | 0.19% | 0.02% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/ar/post/clean | 3.9494 | 3.7548 | −4.93% | 0.22% | 0.09% | Faster | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/ar/post/early | 0.0335 | 0.0327 | −2.30% | 0.96% | 1.86% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/ar/thread/clean | 262.3693 | 260.5388 | −0.70% | 0.04% | 0.01% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/hi/comment/clean | 2.9315 | 2.9364 | +0.16% | 0.07% | 0.06% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/hi/comment/late | 3.3807 | 3.3833 | +0.08% | 0.11% | 0.06% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/hi/post/clean | 2.6588 | 2.4771 | −6.83% | 0.05% | 0.36% | Faster | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/hi/post/early | 0.0454 | 0.0374 | −17.58% | 1.40% | 2.08% | Faster | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/hi/thread/clean | 180.3921 | 180.1696 | −0.12% | 0.01% | 0.04% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/hi/thread/late | 183.1207 | 175.5044 | −4.16% | 0.03% | 0.04% | Faster | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/zh/comment/clean | 0.5543 | 0.5595 | +0.94% | 0.19% | 1.55% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/zh/post/clean | 2.3121 | 2.0728 | −10.35% | 0.18% | 0.11% | Faster | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/zh/post/early | 0.0432 | 0.0359 | −16.90% | 2.35% | 1.27% | Faster | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/zh/thread/clean | 149.5724 | 141.4225 | −5.45% | 0.05% | 0.15% | Faster | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/ja/comment/clean | 1.3625 | 1.3637 | +0.09% | 0.38% | 0.06% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/ja/comment/late | 1.5495 | 1.5495 | −0.00% | 0.22% | 0.01% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/ja/post/clean | 3.2846 | 3.0208 | −8.03% | 0.36% | 0.20% | Faster | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/ja/post/early | 0.0417 | 0.0351 | −15.70% | 1.32% | 0.24% | Faster | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/ja/thread/clean | 220.7184 | 211.9774 | −3.96% | 0.05% | 0.11% | Faster | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/ko/comment/clean | 0.9811 | 0.9851 | +0.40% | 0.55% | 0.19% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/ko/post/clean | 3.1002 | 2.8682 | −7.48% | 0.08% | 0.07% | Faster | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/ko/post/early | 0.0330 | 0.0330 | −0.13% | 2.58% | 0.29% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/ko/thread/clean | 189.6802 | 185.0225 | −2.46% | 0.03% | 0.03% | Faster | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/emoji/comment/clean | 0.3937 | 0.3938 | +0.02% | 0.15% | 0.55% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/emoji/post/clean | 2.6880 | 2.4388 | −9.27% | 0.06% | 0.23% | Faster | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/emoji/post/early | 0.0329 | 0.0333 | +0.97% | 1.52% | 2.19% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| banlist12/emoji/thread/clean | 153.4300 | 142.6811 | −7.01% | 0.11% | 0.02% | Faster | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| explode/pipe2/short | 0.0853 | 0.0851 | −0.23% | 0.79% | 0.25% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| explode/pipe2/4k | 2.5081 | 2.5085 | +0.02% | 1.31% | 0.44% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| explode/pipe2/64k | 45.0716 | 45.7202 | +1.44% | 0.16% | 1.35% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| explode/colon2/short | 0.1004 | 0.0996 | −0.85% | 0.48% | 0.07% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| explode/colon2/4k | 2.5272 | 2.4989 | −1.12% | 0.41% | 0.08% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| explode/colon2/64k | 45.9080 | 45.4306 | −1.04% | 1.95% | 0.21% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| explode/crlf/short | 0.1129 | 0.1125 | −0.37% | 0.44% | 0.15% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| explode/crlf/4k | 2.4607 | 2.4325 | −1.15% | 0.34% | 1.46% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| explode/crlf/64k | 45.0050 | 45.0270 | +0.05% | 0.55% | 0.83% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| explode/comma/short | 0.0930 | 0.0926 | −0.46% | 0.52% | 0.67% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| explode/comma/4k | 2.1888 | 2.1952 | +0.29% | 0.06% | 1.95% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| explode/comma/64k | 38.4283 | 38.5214 | +0.24% | 1.56% | 0.35% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| parse-records/4k | 9.4418 | 9.5843 | +1.51% | 0.73% | 0.44% | Slower | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| parse-query/4k | 26.0120 | 26.2823 | +1.04% | 0.12% | 0.17% | Slower | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| parse-http/small | 0.8447 | 0.8538 | +1.07% | 1.27% | 0.29% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| parse-http/body64k | 0.8381 | 0.8595 | +2.54% | 0.47% | 0.37% | Slower | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| scan-template/4k | 4.5714 | 4.5635 | −0.17% | 0.12% | 0.73% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| render-template/4k | 7.0283 | 5.9951 | −14.70% | 0.18% | 0.63% | Faster | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| log-contains/event/post/early | 0.0267 | 0.0209 | −21.78% | 0.23% | 0.69% | Faster | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| log-contains/level/post/early | 0.0303 | 0.0235 | −22.42% | 0.14% | 1.57% | Faster | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| log-contains/event/thread/clean | 13.3864 | 12.3392 | −7.82% | 0.02% | 0.39% | Faster | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| log-filter/thread/clean | 42.0660 | 41.9510 | −0.27% | 0.58% | 1.02% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| log-contains/event/thread/early | 0.0268 | 0.0209 | −22.17% | 0.98% | 0.32% | Faster | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| log-contains/level/thread/early | 0.0303 | 0.0236 | −22.07% | 0.04% | 2.30% | Noise | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| log-contains/event/thread/late | 13.3624 | 12.3295 | −7.73% | 0.03% | 0.10% | Faster | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |
| log-filter/thread/late | 41.7024 | 42.1452 | +1.06% | 1.06% | 1.39% | Unclear | [gcc15-full233-1sec](../data/amd/gcc15-full233-1sec.json) |

### Separate counters

| Case | Stock cycles¹ | Change cycles¹ | Δ cycles¹ | Stock instr. | Change instr. | Δ instr. |
|---|--:|--:|--:|--:|--:|--:|
| banlist12/en/comment/clean | 2289.36 | 2299.47 | +1.25% | 7244.01 | 7244.01 | −0.00% |
| banlist12/en/comment/early | 146.59 | 150.17 | +2.90% | 536.00 | 536.00 | −0.00% |
| banlist12/en/comment/late | 2530.98 | 2543.03 | +0.12% | 7734.01 | 7734.01 | −0.00% |
| banlist12/en/post/clean | 13958.26 | 12559.43 | −10.08% | 24790.07 | 23360.07 | −5.77% |
| banlist12/en/post/early | 149.08 | 147.80 | −2.42% | 529.00 | 529.00 | +0.00% |
| banlist12/en/post/late | 14288.46 | 12774.41 | −10.60% | 25167.07 | 23737.08 | −5.68% |
| banlist12/en/thread/clean | 812185.51 | 752771.80 | −7.18% | 1140870.97 | 1139441.34 | −0.13% |
| banlist12/en/thread/early | 145.16 | 141.01 | −2.65% | 529.00 | 529.00 | −0.00% |
| banlist12/en/thread/late | 811745.06 | 751622.64 | −7.54% | 1141318.05 | 1139888.31 | −0.13% |
| banlist12/ru/comment/clean | 11846.34 | 11846.17 | −0.06% | 23680.07 | 23680.07 | −0.00% |
| banlist12/ru/comment/early | 143.33 | 143.63 | −1.63% | 527.00 | 527.00 | +0.00% |
| banlist12/ru/comment/late | 12799.15 | 12810.04 | +0.09% | 25732.07 | 25732.07 | −0.00% |
| banlist12/ru/post/clean | 14319.01 | 13479.96 | −5.66% | 28561.07 | 27592.07 | −3.39% |
| banlist12/ru/post/early | 149.29 | 141.98 | −1.65% | 529.00 | 529.00 | −0.00% |
| banlist12/ru/post/late | 15033.23 | 14327.26 | −4.70% | 29654.08 | 28685.08 | −3.27% |
| banlist12/ru/thread/clean | 1042274.37 | 1019318.70 | −2.20% | 1318347.77 | 1317481.02 | −0.07% |
| banlist12/ru/thread/early | 138.05 | 145.81 | +7.83% | 529.00 | 529.00 | −0.00% |
| banlist12/ru/thread/late | 1018428.28 | 1014237.45 | −0.54% | 1319279.78 | 1318418.11 | −0.07% |
| banlist12/es/comment/clean | 2657.60 | 2622.71 | −0.97% | 7862.01 | 7862.02 | +0.00% |
| banlist12/es/post/clean | 13467.33 | 12194.09 | −9.52% | 24774.06 | 23344.06 | −5.77% |
| banlist12/es/post/early | 141.05 | 148.77 | +4.79% | 529.00 | 529.00 | +0.00% |
| banlist12/es/thread/clean | 834909.06 | 779596.88 | −6.67% | 1145234.86 | 1143804.95 | −0.12% |
| banlist12/ar/comment/clean | 9668.73 | 9681.48 | +0.11% | 20136.05 | 20136.05 | +0.00% |
| banlist12/ar/comment/late | 10946.93 | 10958.13 | +0.07% | 22296.06 | 22296.06 | +0.00% |
| banlist12/ar/post/clean | 18605.14 | 17640.96 | −5.17% | 35704.10 | 34274.11 | −4.01% |
| banlist12/ar/post/early | 147.59 | 141.44 | −2.84% | 529.00 | 529.00 | −0.00% |
| banlist12/ar/thread/clean | 1232914.30 | 1222453.88 | −0.82% | 1863534.48 | 1862103.89 | −0.08% |
| banlist12/hi/comment/clean | 13727.58 | 13733.69 | +0.04% | 27800.08 | 27800.08 | +0.00% |
| banlist12/hi/comment/late | 15830.89 | 15875.02 | +0.42% | 31864.09 | 31864.08 | −0.00% |
| banlist12/hi/post/clean | 12482.72 | 11622.45 | −7.09% | 25622.07 | 24359.06 | −4.93% |
| banlist12/hi/post/early | 197.92 | 168.45 | −14.89% | 853.00 | 710.00 | −16.76% |
| banlist12/hi/thread/clean | 848893.78 | 846023.49 | −0.40% | 1114883.23 | 1113666.01 | −0.11% |
| banlist12/hi/thread/late | 860152.19 | 823659.75 | −4.33% | 1116064.92 | 1114851.31 | −0.11% |
| banlist12/zh/comment/clean | 2559.95 | 2564.52 | −0.10% | 7225.01 | 7225.01 | −0.00% |
| banlist12/zh/post/clean | 10923.13 | 9776.52 | −10.45% | 20261.05 | 18688.05 | −7.76% |
| banlist12/zh/post/early | 187.07 | 163.37 | −12.28% | 814.00 | 671.00 | −17.57% |
| banlist12/zh/thread/clean | 709216.05 | 667023.88 | −5.98% | 907958.12 | 906385.34 | −0.17% |
| banlist12/ja/comment/clean | 6346.04 | 6353.92 | +0.01% | 13928.03 | 13928.03 | −0.00% |
| banlist12/ja/comment/late | 7200.64 | 7211.72 | −0.00% | 15605.04 | 15605.04 | +0.00% |
| banlist12/ja/post/clean | 15436.55 | 14062.35 | −8.91% | 29519.08 | 27946.08 | −5.33% |
| banlist12/ja/post/early | 188.93 | 156.12 | −18.60% | 775.00 | 632.00 | −18.45% |
| banlist12/ja/thread/clean | 1039569.57 | 995417.96 | −4.33% | 1463032.48 | 1461459.28 | −0.11% |
| banlist12/ko/comment/clean | 4640.32 | 4570.12 | −1.45% | 10298.02 | 10298.03 | +0.00% |
| banlist12/ko/post/clean | 14560.87 | 13451.41 | −7.60% | 27546.07 | 26116.08 | −5.19% |
| banlist12/ko/post/early | 144.81 | 141.91 | −2.38% | 529.00 | 529.00 | +0.00% |
| banlist12/ko/thread/clean | 894673.52 | 869009.27 | −2.83% | 1282211.97 | 1280781.59 | −0.11% |
| banlist12/emoji/comment/clean | 1797.06 | 1799.93 | −0.18% | 5926.01 | 5926.01 | +0.00% |
| banlist12/emoji/post/clean | 12684.07 | 11479.33 | −9.60% | 22975.07 | 21545.06 | −6.22% |
| banlist12/emoji/post/early | 141.22 | 148.71 | +5.16% | 529.00 | 529.00 | −0.00% |
| banlist12/emoji/thread/clean | 728137.91 | 673892.70 | −7.43% | 1034952.44 | 1033522.36 | −0.14% |
| explode/pipe2/short | 389.96 | 387.34 | −0.99% | 1605.00 | 1605.00 | +0.00% |
| explode/pipe2/4k | 11540.01 | 11584.18 | +1.37% | 43947.02 | 43947.03 | +0.00% |
| explode/pipe2/64k | 207185.39 | 206010.76 | −0.57% | 705785.20 | 705785.33 | +0.00% |
| explode/colon2/short | 456.69 | 454.22 | −0.38% | 1838.00 | 1838.00 | +0.00% |
| explode/colon2/4k | 11638.09 | 11606.27 | −0.21% | 43896.02 | 43896.02 | −0.00% |
| explode/colon2/64k | 204678.22 | 206257.26 | −0.17% | 701794.34 | 701794.37 | +0.00% |
| explode/crlf/short | 515.72 | 514.78 | −0.22% | 2084.00 | 2084.00 | −0.00% |
| explode/crlf/4k | 11286.79 | 11221.91 | −0.04% | 42743.01 | 42743.02 | +0.00% |
| explode/crlf/64k | 206167.88 | 208318.93 | +1.04% | 703262.40 | 703262.31 | −0.00% |
| explode/comma/short | 424.74 | 424.13 | +0.02% | 1783.00 | 1783.00 | +0.00% |
| explode/comma/4k | 10047.78 | 10056.59 | −0.32% | 39743.01 | 39743.01 | −0.00% |
| explode/comma/64k | 173725.13 | 175440.82 | +0.73% | 591645.35 | 591645.23 | −0.00% |
| parse-records/4k | 43246.57 | 43000.58 | −0.75% | 156431.05 | 156431.05 | +0.00% |
| parse-query/4k | 117785.67 | 119095.99 | +0.46% | 438335.74 | 438335.74 | +0.00% |
| parse-http/small | 3793.06 | 3857.46 | +1.70% | 13253.00 | 13253.01 | +0.00% |
| parse-http/body64k | 3799.36 | 3864.24 | +1.60% | 13240.00 | 13240.01 | +0.00% |
| scan-template/4k | 20654.47 | 20671.04 | +0.26% | 68608.03 | 68608.04 | +0.00% |
| render-template/4k | 32818.86 | 28100.78 | −14.66% | 79416.12 | 65402.14 | −17.65% |
| log-contains/event/post/early | 122.86 | 92.31 | −25.55% | 568.00 | 425.00 | −25.18% |
| log-contains/level/post/early | 139.69 | 109.61 | −21.76% | 602.00 | 459.00 | −23.75% |
| log-contains/event/thread/clean | 63244.33 | 58260.73 | −7.78% | 123453.08 | 123310.08 | −0.12% |
| log-filter/thread/clean | 195199.20 | 195661.96 | +0.85% | 492445.26 | 492445.11 | −0.00% |
| log-contains/event/thread/early | 124.18 | 92.05 | −24.93% | 568.00 | 425.00 | −25.18% |
| log-contains/level/thread/early | 139.82 | 108.76 | −21.94% | 602.00 | 459.00 | −23.75% |
| log-contains/event/thread/late | 63136.74 | 58336.18 | −7.55% | 123289.09 | 123146.08 | −0.12% |
| log-filter/thread/late | 195092.37 | 196032.31 | +0.43% | 492191.24 | 492191.36 | +0.00% |

## AMD / Clang 21.1

| Case | Stock, µs | Change, µs | Δ time | Stock spread | Change spread | Result | Source |
|---|--:|--:|--:|--:|--:|--:|---|
| banlist12/en/comment/clean | 0.5138 | 0.5104 | −0.66% | 0.10% | 0.24% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/en/comment/early | 0.0306 | 0.0308 | +0.83% | 2.71% | 1.86% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/en/comment/late | 0.5565 | 0.5569 | +0.08% | 0.36% | 0.14% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/en/post/clean | 2.8101 | 2.5401 | −9.61% | 0.17% | 0.14% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/en/post/early | 0.0304 | 0.0304 | +0.09% | 1.70% | 2.06% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/en/post/late | 2.9564 | 2.6935 | −8.89% | 0.28% | 0.26% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/en/thread/clean | 161.8209 | 149.1975 | −7.80% | 0.21% | 0.14% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/en/thread/early | 0.0302 | 0.0306 | +1.37% | 1.38% | 0.47% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/en/thread/late | 161.7351 | 148.9411 | −7.91% | 0.05% | 0.24% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/ru/comment/clean | 2.5963 | 2.5880 | −0.32% | 0.23% | 0.10% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/ru/comment/early | 0.0307 | 0.0305 | −0.87% | 0.37% | 2.46% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/ru/comment/late | 2.7989 | 2.7982 | −0.02% | 0.18% | 0.06% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/ru/post/clean | 2.8605 | 2.7476 | −3.95% | 0.13% | 0.13% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/ru/post/early | 0.0311 | 0.0302 | −2.92% | 1.14% | 0.56% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/ru/post/late | 3.0406 | 2.9230 | −3.87% | 0.19% | 0.04% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/ru/thread/clean | 217.9945 | 205.6730 | −5.65% | 0.02% | 0.03% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/ru/thread/early | 0.0308 | 0.0305 | −0.96% | 1.93% | 2.50% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/ru/thread/late | 214.2920 | 201.9312 | −5.77% | 1.10% | 0.10% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/es/comment/clean | 0.5887 | 0.5904 | +0.29% | 0.26% | 0.09% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/es/post/clean | 2.7114 | 2.4480 | −9.72% | 0.44% | 0.83% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/es/post/early | 0.0305 | 0.0302 | −0.97% | 1.69% | 0.68% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/es/thread/clean | 168.8748 | 155.5341 | −7.90% | 0.02% | 0.03% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/ar/comment/clean | 2.1006 | 2.1087 | +0.38% | 0.09% | 0.16% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/ar/comment/late | 2.3850 | 2.3859 | +0.04% | 0.71% | 0.38% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/ar/post/clean | 3.8592 | 3.6704 | −4.89% | 0.63% | 0.05% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/ar/post/early | 0.0302 | 0.0308 | +2.15% | 0.29% | 1.87% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/ar/thread/clean | 262.5189 | 251.0290 | −4.38% | 0.05% | 0.03% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/hi/comment/clean | 2.9993 | 2.9872 | −0.40% | 0.78% | 0.30% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/hi/comment/late | 3.4450 | 3.4550 | +0.29% | 0.11% | 0.23% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/hi/post/clean | 2.4691 | 2.3515 | −4.76% | 0.06% | 0.26% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/hi/post/early | 0.0418 | 0.0357 | −14.56% | 1.22% | 0.20% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/hi/thread/clean | 175.0818 | 164.6450 | −5.96% | 0.07% | 0.03% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/hi/thread/late | 178.5123 | 161.7531 | −9.39% | 0.11% | 0.05% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/zh/comment/clean | 0.5810 | 0.5803 | −0.12% | 0.40% | 0.08% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/zh/post/clean | 2.1799 | 1.9261 | −11.64% | 0.21% | 0.04% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/zh/post/early | 0.0387 | 0.0330 | −14.58% | 0.65% | 1.15% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/zh/thread/clean | 144.1783 | 131.6223 | −8.71% | 0.24% | 0.18% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/ja/comment/clean | 1.4090 | 1.4069 | −0.16% | 0.94% | 0.25% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/ja/comment/late | 1.5845 | 1.5831 | −0.09% | 0.20% | 0.04% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/ja/post/clean | 3.1152 | 2.8773 | −7.64% | 0.11% | 0.09% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/ja/post/early | 0.0364 | 0.0319 | −12.45% | 1.00% | 0.37% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/ja/thread/clean | 215.7335 | 202.3800 | −6.19% | 0.05% | 0.03% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/ko/comment/clean | 1.0083 | 1.0102 | +0.19% | 0.34% | 0.20% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/ko/post/clean | 2.9588 | 2.7281 | −7.80% | 0.46% | 0.17% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/ko/post/early | 0.0307 | 0.0301 | −2.09% | 1.42% | 1.64% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/ko/thread/clean | 186.8928 | 175.8799 | −5.89% | 0.05% | 0.03% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/emoji/comment/clean | 0.3973 | 0.3966 | −0.18% | 0.15% | 0.25% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/emoji/post/clean | 2.5483 | 2.2975 | −9.84% | 0.12% | 0.13% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/emoji/post/early | 0.0306 | 0.0305 | −0.21% | 1.06% | 1.75% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| banlist12/emoji/thread/clean | 145.2888 | 133.9651 | −7.79% | 0.10% | 0.01% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| explode/pipe2/short | 0.0908 | 0.0916 | +0.92% | 0.46% | 0.66% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| explode/pipe2/4k | 2.7138 | 2.8019 | +3.24% | 1.17% | 0.90% | Slower | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| explode/pipe2/64k | 49.4154 | 49.2383 | −0.36% | 0.87% | 0.78% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| explode/colon2/short | 0.1036 | 0.1047 | +1.14% | 0.25% | 0.52% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| explode/colon2/4k | 2.7902 | 2.7557 | −1.23% | 1.41% | 0.48% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| explode/colon2/64k | 48.6755 | 49.0002 | +0.67% | 0.46% | 1.48% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| explode/crlf/short | 0.1194 | 0.1199 | +0.48% | 0.24% | 0.84% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| explode/crlf/4k | 2.6348 | 2.6547 | +0.76% | 1.00% | 0.38% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| explode/crlf/64k | 49.0810 | 48.9463 | −0.27% | 0.75% | 0.73% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| explode/comma/short | 0.0944 | 0.0941 | −0.31% | 1.12% | 0.76% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| explode/comma/4k | 2.2465 | 2.2148 | −1.41% | 1.24% | 0.78% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| explode/comma/64k | 38.0996 | 38.2129 | +0.30% | 0.97% | 1.70% | Noise | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| parse-records/4k | 9.9516 | 10.0725 | +1.22% | 0.59% | 0.51% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| parse-query/4k | 27.2458 | 27.5487 | +1.11% | 0.85% | 0.83% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| parse-http/small | 0.8478 | 0.8275 | −2.39% | 0.47% | 0.67% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| parse-http/body64k | 0.8440 | 0.8262 | −2.10% | 0.21% | 0.61% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| scan-template/4k | 4.3505 | 4.3489 | −0.04% | 0.23% | 0.59% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| render-template/4k | 6.5323 | 5.5867 | −14.48% | 0.09% | 0.79% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| log-contains/event/post/early | 0.0245 | 0.0218 | −11.04% | 1.35% | 0.11% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| log-contains/level/post/early | 0.0322 | 0.0254 | −20.92% | 0.56% | 5.89% | Noise | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| log-contains/event/thread/clean | 12.4447 | 11.4881 | −7.69% | 0.01% | 0.05% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| log-filter/thread/clean | 43.1143 | 42.9586 | −0.36% | 0.71% | 0.21% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| log-contains/event/thread/early | 0.0269 | 0.0219 | −18.67% | 2.73% | 0.09% | Noise | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| log-contains/level/thread/early | 0.0325 | 0.0270 | −16.93% | 1.14% | 8.32% | Noise | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| log-contains/event/thread/late | 12.4268 | 11.4687 | −7.71% | 0.03% | 0.05% | Faster | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |
| log-filter/thread/late | 43.2732 | 43.3940 | +0.28% | 0.79% | 0.63% | Unclear | [clang21-full233-1sec](../data/amd/clang21-full233-1sec.json) |

### Separate counters

| Case | Stock cycles¹ | Change cycles¹ | Δ cycles¹ | Stock instr. | Change instr. | Δ instr. |
|---|--:|--:|--:|--:|--:|--:|
| banlist12/en/comment/clean | 2355.18 | 2366.91 | +0.23% | 7166.01 | 7166.01 | +0.00% |
| banlist12/en/comment/early | 131.98 | 132.19 | +0.15% | 550.00 | 550.00 | +0.00% |
| banlist12/en/comment/late | 2562.85 | 2551.47 | −0.44% | 7662.01 | 7662.02 | +0.00% |
| banlist12/en/post/clean | 13252.81 | 11900.14 | −10.14% | 22195.07 | 21765.07 | −1.94% |
| banlist12/en/post/early | 136.34 | 132.77 | −1.04% | 541.00 | 541.00 | +0.00% |
| banlist12/en/post/late | 13361.53 | 12048.16 | −9.82% | 22571.07 | 22141.08 | −1.91% |
| banlist12/en/thread/clean | 767392.09 | 703846.69 | −8.06% | 1077061.04 | 1076630.90 | −0.04% |
| banlist12/en/thread/early | 131.12 | 132.39 | +0.19% | 541.00 | 541.00 | +0.00% |
| banlist12/en/thread/late | 767990.85 | 704471.24 | −8.31% | 1077504.07 | 1077074.35 | −0.04% |
| banlist12/ru/comment/clean | 12088.03 | 12071.28 | +0.01% | 23205.08 | 23205.08 | −0.00% |
| banlist12/ru/comment/early | 131.35 | 131.96 | +1.22% | 541.00 | 541.00 | −0.00% |
| banlist12/ru/comment/late | 13048.55 | 13056.23 | −0.03% | 25235.08 | 25235.08 | −0.00% |
| banlist12/ru/post/clean | 13456.34 | 12891.22 | −4.14% | 25487.09 | 24909.09 | −2.27% |
| banlist12/ru/post/early | 132.58 | 132.75 | +0.58% | 541.00 | 541.00 | −0.00% |
| banlist12/ru/post/late | 14250.62 | 13665.29 | −4.18% | 26539.09 | 25939.09 | −2.26% |
| banlist12/ru/thread/clean | 1022235.32 | 963610.19 | −5.73% | 1252230.01 | 1298537.62 | +3.70% |
| banlist12/ru/thread/early | 132.62 | 131.28 | +0.35% | 541.00 | 541.00 | −0.00% |
| banlist12/ru/thread/late | 997819.33 | 945681.72 | −5.31% | 1253132.07 | 1299580.23 | +3.71% |
| banlist12/es/comment/clean | 2737.03 | 2735.83 | −0.04% | 7762.02 | 7762.02 | +0.00% |
| banlist12/es/post/clean | 12782.97 | 11535.09 | −9.88% | 22232.06 | 21802.06 | −1.93% |
| banlist12/es/post/early | 131.64 | 132.85 | +0.09% | 541.00 | 541.00 | −0.00% |
| banlist12/es/thread/clean | 797138.35 | 734696.62 | −7.88% | 1082285.73 | 1081856.16 | −0.04% |
| banlist12/ar/comment/clean | 9824.25 | 9821.91 | +0.05% | 19616.06 | 19616.06 | −0.00% |
| banlist12/ar/comment/late | 11098.49 | 11078.28 | −0.30% | 21724.06 | 21724.06 | −0.00% |
| banlist12/ar/post/clean | 18165.74 | 17243.08 | −4.93% | 32804.10 | 32374.11 | −1.31% |
| banlist12/ar/post/early | 132.51 | 132.70 | −0.09% | 541.00 | 541.00 | −0.00% |
| banlist12/ar/thread/clean | 1231472.77 | 1175693.75 | −4.48% | 1786362.68 | 1785931.94 | −0.02% |
| banlist12/hi/comment/clean | 13966.67 | 13965.19 | −0.01% | 27093.09 | 27093.08 | −0.00% |
| banlist12/hi/comment/late | 16121.84 | 16201.79 | +0.28% | 31062.11 | 31062.11 | +0.00% |
| banlist12/hi/post/clean | 11597.41 | 11074.50 | −4.41% | 22333.07 | 21735.07 | −2.68% |
| banlist12/hi/post/early | 189.45 | 162.27 | −12.93% | 723.00 | 680.00 | −5.95% |
| banlist12/hi/thread/clean | 822405.10 | 771420.68 | −6.24% | 1052440.54 | 1093667.43 | +3.92% |
| banlist12/hi/thread/late | 837331.49 | 758044.48 | −9.53% | 1053579.82 | 1095020.88 | +3.93% |
| banlist12/zh/comment/clean | 2685.34 | 2685.94 | −0.10% | 7088.02 | 7088.02 | −0.00% |
| banlist12/zh/post/clean | 10376.58 | 9123.54 | −12.09% | 17697.05 | 17224.05 | −2.67% |
| banlist12/zh/post/early | 177.63 | 153.06 | −12.47% | 682.00 | 639.00 | −6.30% |
| banlist12/zh/thread/clean | 680255.52 | 621065.57 | −8.80% | 852018.99 | 851545.27 | −0.06% |
| banlist12/ja/comment/clean | 6539.69 | 6576.30 | +0.46% | 13657.04 | 13657.04 | +0.00% |
| banlist12/ja/comment/late | 7385.46 | 7392.70 | +0.06% | 15298.04 | 15298.04 | −0.00% |
| banlist12/ja/post/clean | 14676.99 | 13487.97 | −8.11% | 26647.08 | 26174.08 | −1.78% |
| banlist12/ja/post/early | 169.23 | 144.63 | −14.41% | 660.00 | 617.00 | −6.52% |
| banlist12/ja/thread/clean | 1014271.01 | 949229.36 | −6.41% | 1395122.01 | 1394649.13 | −0.03% |
| banlist12/ko/comment/clean | 4683.09 | 4685.57 | +0.44% | 10090.03 | 10090.03 | +0.00% |
| banlist12/ko/post/clean | 13893.10 | 12836.01 | −7.53% | 24972.08 | 24542.08 | −1.72% |
| banlist12/ko/post/early | 132.12 | 130.75 | −0.22% | 541.00 | 541.00 | −0.00% |
| banlist12/ko/thread/clean | 879912.42 | 826866.65 | −5.82% | 1225799.86 | 1225369.22 | −0.04% |
| banlist12/emoji/comment/clean | 1814.63 | 1825.11 | +1.98% | 5834.01 | 5834.01 | +0.00% |
| banlist12/emoji/post/clean | 12014.44 | 10913.85 | −9.16% | 20470.06 | 20040.06 | −2.10% |
| banlist12/emoji/post/early | 132.66 | 131.77 | −0.67% | 541.00 | 541.00 | −0.00% |
| banlist12/emoji/thread/clean | 689012.48 | 633886.74 | −7.99% | 977183.29 | 976753.59 | −0.04% |
| explode/pipe2/short | 414.88 | 411.47 | −0.68% | 1546.00 | 1546.00 | +0.00% |
| explode/pipe2/4k | 12567.90 | 12593.43 | −0.15% | 41512.02 | 41511.02 | −0.00% |
| explode/pipe2/64k | 226403.95 | 225842.75 | +0.30% | 664547.34 | 664547.49 | +0.00% |
| explode/colon2/short | 474.58 | 471.61 | −1.16% | 1762.00 | 1762.00 | −0.00% |
| explode/colon2/4k | 12473.72 | 12544.55 | +0.39% | 41438.02 | 41438.02 | +0.00% |
| explode/colon2/64k | 223829.75 | 223094.55 | −0.69% | 660739.34 | 660739.36 | +0.00% |
| explode/crlf/short | 546.01 | 544.39 | −1.48% | 1995.00 | 1995.00 | +0.00% |
| explode/crlf/4k | 12181.11 | 12236.95 | −0.79% | 40376.02 | 40376.03 | +0.00% |
| explode/crlf/64k | 224167.58 | 225239.09 | +1.05% | 662210.53 | 662210.49 | −0.00% |
| explode/comma/short | 427.81 | 427.45 | −0.00% | 1720.00 | 1720.00 | −0.00% |
| explode/comma/4k | 10115.35 | 10178.24 | +0.62% | 38391.02 | 38391.02 | +0.00% |
| explode/comma/64k | 173188.67 | 171960.70 | −0.89% | 572560.29 | 572560.28 | −0.00% |
| parse-records/4k | 45672.63 | 46102.39 | +0.62% | 150929.07 | 150929.07 | +0.00% |
| parse-query/4k | 123968.35 | 124373.12 | +0.33% | 425597.72 | 425597.71 | −0.00% |
| parse-http/small | 3859.31 | 3797.91 | −1.66% | 12918.00 | 12918.00 | +0.00% |
| parse-http/body64k | 3876.95 | 3780.27 | −2.49% | 12905.00 | 12905.01 | +0.00% |
| scan-template/4k | 19586.88 | 19597.90 | +0.10% | 67567.03 | 67567.03 | −0.00% |
| render-template/4k | 30454.38 | 26011.23 | −14.26% | 64532.14 | 60318.10 | −6.53% |
| log-contains/event/post/early | 114.52 | 100.15 | −12.55% | 419.00 | 376.00 | −10.26% |
| log-contains/level/post/early | 150.43 | 111.43 | −25.82% | 451.00 | 408.00 | −9.53% |
| log-contains/event/thread/clean | 58593.32 | 54096.92 | −7.73% | 117674.08 | 117631.12 | −0.04% |
| log-filter/thread/clean | 200480.71 | 200349.36 | +0.13% | 483484.35 | 483484.31 | −0.00% |
| log-contains/event/thread/early | 119.81 | 100.25 | −16.54% | 419.00 | 376.00 | −10.26% |
| log-contains/level/thread/early | 150.43 | 122.34 | −26.00% | 451.00 | 408.00 | −9.53% |
| log-contains/event/thread/late | 58539.22 | 54042.09 | −7.70% | 117525.07 | 117482.09 | −0.04% |
| log-filter/thread/late | 200163.37 | 199194.37 | −0.73% | 483235.35 | 483235.27 | −0.00% |

## Intel / GCC 13.3

| Case | Stock, µs | Change, µs | Δ time | Stock spread | Change spread | Result | Source |
|---|--:|--:|--:|--:|--:|--:|---|
| banlist12/en/comment/clean | 0.4985 | 0.4987 | +0.04% | 0.34% | 0.30% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/en/comment/early | 0.0298 | 0.0297 | −0.10% | 1.44% | 1.66% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/en/comment/late | 0.5445 | 0.5431 | −0.25% | 0.79% | 0.31% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/en/post/clean | 3.5138 | 3.2788 | −6.69% | 0.26% | 0.18% | Faster | [gcc13-focus](../data/intel/gcc13-focus.json) |
| banlist12/en/post/early | 0.0296 | 0.0296 | +0.16% | 1.11% | 1.20% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/en/post/late | 3.5340 | 3.3324 | −5.71% | 0.14% | 0.16% | Faster | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/en/thread/clean | 221.4401 | 217.9769 | −1.56% | 0.11% | 0.13% | Faster | [gcc13-focus](../data/intel/gcc13-focus.json) |
| banlist12/en/thread/early | 0.0296 | 0.0295 | −0.19% | 1.02% | 1.02% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/en/thread/late | 221.5374 | 218.2879 | −1.47% | 0.06% | 0.12% | Faster | [gcc13-focus](../data/intel/gcc13-focus.json) |
| banlist12/ru/comment/clean | 3.0879 | 3.0866 | −0.04% | 0.24% | 0.25% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/ru/comment/early | 0.0296 | 0.0298 | +0.74% | 0.92% | 1.75% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/ru/comment/late | 3.3939 | 3.3957 | +0.05% | 0.28% | 0.26% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/ru/post/clean | 3.5943 | 3.5051 | −2.48% | 0.07% | 0.09% | Faster | [gcc13-focus](../data/intel/gcc13-focus.json) |
| banlist12/ru/post/early | 0.0295 | 0.0296 | +0.22% | 0.83% | 0.91% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/ru/post/late | 3.7683 | 3.6824 | −2.28% | 0.12% | 0.24% | Faster | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/ru/thread/clean | 302.2632 | 310.0164 | +2.57% | 0.09% | 0.21% | Slower | [gcc13-focus](../data/intel/gcc13-focus.json) |
| banlist12/ru/thread/early | 0.0297 | 0.0297 | −0.01% | 1.16% | 0.78% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/ru/thread/late | 302.5665 | 310.3976 | +2.59% | 0.14% | 0.11% | Slower | [gcc13-focus](../data/intel/gcc13-focus.json) |
| banlist12/es/comment/clean | 0.5669 | 0.5675 | +0.09% | 0.48% | 0.31% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/es/post/clean | 3.3111 | 3.1648 | −4.42% | 0.13% | 0.10% | Faster | [gcc13-focus](../data/intel/gcc13-focus.json) |
| banlist12/es/post/early | 0.0294 | 0.0296 | +0.73% | 0.98% | 1.13% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/es/thread/clean | 227.3919 | 226.0118 | −0.61% | 0.18% | 0.32% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/ar/comment/clean | 2.5348 | 2.5358 | +0.04% | 0.22% | 0.16% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/ar/comment/late | 2.8754 | 2.8772 | +0.06% | 0.17% | 0.17% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/ar/post/clean | 4.9122 | 4.7890 | −2.51% | 0.06% | 0.08% | Faster | [gcc13-focus](../data/intel/gcc13-focus.json) |
| banlist12/ar/post/early | 0.0295 | 0.0297 | +0.66% | 0.53% | 0.85% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/ar/thread/clean | 361.0349 | 370.3597 | +2.58% | 0.37% | 0.33% | Slower | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/hi/comment/clean | 3.6865 | 3.6819 | −0.13% | 0.26% | 0.32% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/hi/comment/late | 4.2315 | 4.2341 | +0.06% | 0.14% | 0.20% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/hi/post/clean | 3.1412 | 3.0376 | −3.30% | 0.54% | 0.17% | Faster | [gcc13-focus](../data/intel/gcc13-focus.json) |
| banlist12/hi/post/early | 0.0509 | 0.0444 | −12.72% | 0.69% | 0.65% | Faster | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/hi/thread/clean | 259.3623 | 259.5434 | +0.07% | 0.28% | 0.45% | Unclear | [gcc13-focus](../data/intel/gcc13-focus.json) |
| banlist12/hi/thread/late | 259.1355 | 258.9391 | −0.08% | 0.39% | 0.51% | Unclear | [gcc13-focus](../data/intel/gcc13-focus.json) |
| banlist12/zh/comment/clean | 0.5630 | 0.5632 | +0.03% | 0.75% | 0.76% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/zh/post/clean | 2.6236 | 2.4783 | −5.54% | 0.12% | 0.34% | Faster | [gcc13-focus](../data/intel/gcc13-focus.json) |
| banlist12/zh/post/early | 0.0475 | 0.0397 | −16.43% | 0.49% | 0.85% | Faster | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/zh/thread/clean | 200.4114 | 199.1485 | −0.63% | 0.18% | 0.16% | Unclear | [gcc13-focus](../data/intel/gcc13-focus.json) |
| banlist12/ja/comment/clean | 1.6781 | 1.6854 | +0.43% | 0.52% | 0.33% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/ja/comment/late | 1.8562 | 1.8571 | +0.05% | 0.19% | 0.22% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/ja/post/clean | 3.9456 | 3.8052 | −3.56% | 0.09% | 0.08% | Faster | [gcc13-focus](../data/intel/gcc13-focus.json) |
| banlist12/ja/post/early | 0.0451 | 0.0383 | −15.02% | 0.79% | 0.98% | Faster | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/ja/thread/clean | 299.6051 | 306.4130 | +2.27% | 0.33% | 0.34% | Slower | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/ko/comment/clean | 1.0014 | 0.9964 | −0.50% | 1.13% | 0.84% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/ko/post/clean | 3.8034 | 3.6322 | −4.50% | 0.20% | 0.16% | Faster | [gcc13-focus](../data/intel/gcc13-focus.json) |
| banlist12/ko/post/early | 0.0297 | 0.0298 | +0.27% | 0.69% | 0.89% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/ko/thread/clean | 253.6660 | 259.2468 | +2.20% | 0.33% | 0.25% | Slower | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/emoji/comment/clean | 0.3754 | 0.3758 | +0.10% | 0.73% | 0.77% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/emoji/post/clean | 3.1488 | 3.0634 | −2.71% | 0.09% | 0.16% | Faster | [gcc13-focus](../data/intel/gcc13-focus.json) |
| banlist12/emoji/post/early | 0.0295 | 0.0296 | +0.09% | 1.08% | 0.49% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| banlist12/emoji/thread/clean | 198.8143 | 196.3446 | −1.24% | 0.19% | 0.24% | Faster | [gcc13-full233](../data/intel/gcc13-full233.json) |
| explode/pipe2/short | 0.0853 | 0.0852 | −0.03% | 0.69% | 1.34% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| explode/pipe2/4k | 2.5381 | 2.5293 | −0.35% | 0.84% | 1.22% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| explode/pipe2/64k | 50.1447 | 50.2790 | +0.27% | 0.72% | 0.74% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| explode/colon2/short | 0.0997 | 0.0990 | −0.70% | 0.70% | 0.95% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| explode/colon2/4k | 2.4388 | 2.4124 | −1.08% | 1.24% | 2.35% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| explode/colon2/64k | 49.7878 | 49.8327 | +0.09% | 1.19% | 0.69% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| explode/crlf/short | 0.1125 | 0.1125 | −0.02% | 0.73% | 0.98% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| explode/crlf/4k | 2.4908 | 2.4786 | −0.49% | 1.92% | 1.69% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| explode/crlf/64k | 49.7146 | 49.6828 | −0.06% | 1.59% | 1.48% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| explode/comma/short | 0.0871 | 0.0875 | +0.41% | 0.48% | 0.79% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| explode/comma/4k | 2.0251 | 2.0706 | +2.25% | 1.71% | 3.51% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| explode/comma/64k | 41.4531 | 41.3862 | −0.16% | 0.87% | 0.53% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| parse-records/4k | 9.6409 | 9.6413 | +0.00% | 2.11% | 0.41% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| parse-query/4k | 25.3009 | 25.4288 | +0.51% | 0.62% | 0.50% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| parse-http/small | 0.8050 | 0.8211 | +2.00% | 0.32% | 0.36% | Slower | [gcc13-focus](../data/intel/gcc13-focus.json) |
| parse-http/body64k | 0.8063 | 0.8215 | +1.88% | 0.34% | 0.23% | Slower | [gcc13-focus](../data/intel/gcc13-focus.json) |
| scan-template/4k | 4.2426 | 4.2254 | −0.41% | 0.71% | 0.86% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| render-template/4k | 7.6350 | 6.4390 | −15.66% | 0.98% | 1.10% | Faster | [gcc13-focus](../data/intel/gcc13-focus.json) |
| log-contains/event/post/early | 0.0357 | 0.0262 | −26.50% | 0.58% | 1.23% | Faster | [gcc13-full233](../data/intel/gcc13-full233.json) |
| log-contains/level/post/early | 0.0389 | 0.0295 | −24.21% | 0.65% | 1.35% | Faster | [gcc13-full233](../data/intel/gcc13-full233.json) |
| log-contains/event/thread/clean | 17.0451 | 17.0650 | +0.12% | 0.06% | 0.12% | Unclear | [gcc13-focus](../data/intel/gcc13-focus.json) |
| log-filter/thread/clean | 55.1193 | 55.4201 | +0.55% | 0.50% | 1.06% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |
| log-contains/event/thread/early | 0.0354 | 0.0259 | −26.82% | 0.41% | 2.00% | Faster | [gcc13-full233](../data/intel/gcc13-full233.json) |
| log-contains/level/thread/early | 0.0389 | 0.0296 | −23.88% | 0.48% | 1.33% | Faster | [gcc13-full233](../data/intel/gcc13-full233.json) |
| log-contains/event/thread/late | 17.0252 | 17.0166 | −0.05% | 0.09% | 0.14% | Unclear | [gcc13-focus](../data/intel/gcc13-focus.json) |
| log-filter/thread/late | 54.8762 | 55.2814 | +0.74% | 0.22% | 1.42% | Unclear | [gcc13-full233](../data/intel/gcc13-full233.json) |

### Separate counters

| Case | Stock cycles¹ | Change cycles¹ | Δ cycles¹ | Stock instr. | Change instr. | Δ instr. |
|---|--:|--:|--:|--:|--:|--:|
| banlist12/en/comment/clean | 1885.02 | 1892.38 | +0.18% | 7376.17 | 7376.19 | +0.00% |
| banlist12/en/comment/early | 114.69 | 114.28 | −0.36% | 556.01 | 556.01 | −0.00% |
| banlist12/en/comment/late | 2069.41 | 2058.09 | −0.33% | 7874.19 | 7874.21 | +0.00% |
| banlist12/en/post/clean | 13298.58 | 12411.43 | −6.50% | 23925.23 | 22505.23 | −5.94% |
| banlist12/en/post/early | 113.10 | 112.11 | −0.87% | 549.01 | 549.01 | +0.00% |
| banlist12/en/post/late | 13440.30 | 12685.48 | −6.05% | 24301.05 | 22881.29 | −5.84% |
| banlist12/en/thread/clean | 840462.66 | 833314.84 | −0.72% | 1082229.15 | 1080809.62 | −0.13% |
| banlist12/en/thread/early | 111.31 | 112.71 | +0.52% | 549.01 | 549.01 | −0.00% |
| banlist12/en/thread/late | 843967.90 | 835974.64 | −1.15% | 1082673.69 | 1081254.69 | −0.13% |
| banlist12/ru/comment/clean | 11698.18 | 11674.19 | −0.21% | 23807.32 | 23807.19 | −0.00% |
| banlist12/ru/comment/early | 112.31 | 112.97 | +0.43% | 547.01 | 547.01 | −0.00% |
| banlist12/ru/comment/late | 12825.40 | 12962.92 | +1.42% | 25866.32 | 25866.30 | −0.00% |
| banlist12/ru/post/clean | 13675.09 | 13215.04 | −3.36% | 27668.27 | 26706.24 | −3.48% |
| banlist12/ru/post/early | 112.86 | 112.42 | −0.85% | 549.01 | 549.01 | +0.00% |
| banlist12/ru/post/late | 14379.12 | 13897.18 | −2.94% | 28729.23 | 27767.34 | −3.35% |
| banlist12/ru/thread/clean | 1145533.19 | 1175994.64 | +2.86% | 1260352.92 | 1259516.76 | −0.07% |
| banlist12/ru/thread/early | 112.01 | 112.22 | −0.04% | 549.01 | 549.01 | −0.00% |
| banlist12/ru/thread/late | 1154597.90 | 1187603.11 | +2.86% | 1261261.04 | 1260427.80 | −0.07% |
| banlist12/es/comment/clean | 2160.99 | 2155.12 | −0.27% | 7995.18 | 7995.19 | +0.00% |
| banlist12/es/post/clean | 12472.51 | 11958.68 | −4.08% | 23952.23 | 22532.25 | −5.93% |
| banlist12/es/post/early | 112.27 | 112.45 | +0.46% | 549.01 | 549.01 | +0.00% |
| banlist12/es/thread/clean | 861311.27 | 858255.67 | −0.30% | 1087960.93 | 1086535.84 | −0.13% |
| banlist12/ar/comment/clean | 9575.12 | 9639.51 | +0.67% | 20276.91 | 20276.92 | +0.00% |
| banlist12/ar/comment/late | 10949.08 | 10930.61 | −0.17% | 22445.09 | 22445.08 | −0.00% |
| banlist12/ar/post/clean | 18644.64 | 18127.97 | −3.30% | 35009.35 | 33589.38 | −4.06% |
| banlist12/ar/post/early | 112.34 | 113.86 | +0.62% | 549.01 | 549.01 | +0.00% |
| banlist12/ar/thread/clean | 1379039.50 | 1442653.14 | +3.52% | 1815690.54 | 1814288.32 | −0.08% |
| banlist12/hi/comment/clean | 13959.98 | 13947.68 | −0.33% | 27934.40 | 27934.42 | +0.00% |
| banlist12/hi/comment/late | 16030.69 | 16050.34 | +0.12% | 32006.66 | 32006.48 | −0.00% |
| banlist12/hi/post/clean | 11868.55 | 11554.76 | −2.76% | 24722.25 | 23468.24 | −5.07% |
| banlist12/hi/post/early | 192.28 | 168.48 | −12.28% | 870.02 | 728.02 | −16.32% |
| banlist12/hi/thread/clean | 989591.96 | 976256.06 | −1.49% | 1054844.42 | 1053652.03 | −0.11% |
| banlist12/hi/thread/late | 1006425.07 | 985547.54 | −0.80% | 1055989.30 | 1054803.06 | −0.11% |
| banlist12/zh/comment/clean | 2147.89 | 2131.36 | −0.61% | 7357.19 | 7357.19 | −0.00% |
| banlist12/zh/post/clean | 9942.80 | 9352.86 | −5.89% | 19540.20 | 17978.17 | −7.99% |
| banlist12/zh/post/early | 181.97 | 150.53 | −17.28% | 831.01 | 689.01 | −17.09% |
| banlist12/zh/thread/clean | 857138.68 | 866715.36 | −0.70% | 856266.79 | 854707.05 | −0.18% |
| banlist12/ja/comment/clean | 6396.83 | 6394.29 | +0.02% | 14060.61 | 14060.61 | −0.00% |
| banlist12/ja/comment/late | 7037.12 | 7032.95 | −0.16% | 15704.73 | 15704.67 | −0.00% |
| banlist12/ja/post/clean | 14955.38 | 14441.95 | −3.25% | 28691.29 | 27129.28 | −5.44% |
| banlist12/ja/post/early | 172.34 | 144.30 | −16.38% | 792.01 | 650.01 | −17.93% |
| banlist12/ja/thread/clean | 1137577.68 | 1164654.37 | +2.17% | 1405958.03 | 1404405.19 | −0.11% |
| banlist12/ko/comment/clean | 3793.38 | 3828.53 | +1.01% | 10431.34 | 10431.34 | +0.00% |
| banlist12/ko/post/clean | 14533.06 | 13848.17 | −4.84% | 26866.23 | 25446.28 | −5.29% |
| banlist12/ko/post/early | 112.55 | 112.70 | −0.17% | 549.01 | 549.01 | +0.00% |
| banlist12/ko/thread/clean | 968272.56 | 988209.07 | +2.11% | 1235852.51 | 1234448.08 | −0.11% |
| banlist12/emoji/comment/clean | 1421.11 | 1415.58 | −0.48% | 6059.12 | 6059.13 | +0.00% |
| banlist12/emoji/post/clean | 11948.54 | 11677.73 | −2.33% | 22210.22 | 20790.22 | −6.39% |
| banlist12/emoji/post/early | 113.02 | 113.43 | +0.69% | 549.01 | 549.01 | +0.00% |
| banlist12/emoji/thread/clean | 755176.63 | 750416.15 | −0.38% | 982643.44 | 981222.58 | −0.14% |
| explode/pipe2/short | 325.04 | 323.15 | −0.51% | 1592.00 | 1592.01 | +0.00% |
| explode/pipe2/4k | 9488.72 | 9521.29 | +1.04% | 43407.33 | 43407.20 | −0.00% |
| explode/pipe2/64k | 190968.41 | 188865.44 | −1.38% | 697147.16 | 697149.15 | +0.00% |
| explode/colon2/short | 381.23 | 377.60 | −1.11% | 1822.01 | 1822.01 | +0.00% |
| explode/colon2/4k | 9238.26 | 9248.73 | +0.11% | 43356.23 | 43356.31 | +0.00% |
| explode/colon2/64k | 187946.88 | 187370.68 | −0.31% | 693220.19 | 693221.33 | +0.00% |
| explode/crlf/short | 427.23 | 426.51 | −0.17% | 2065.01 | 2065.01 | −0.00% |
| explode/crlf/4k | 9222.59 | 9317.03 | +1.27% | 42218.09 | 42218.19 | +0.00% |
| explode/crlf/64k | 186873.61 | 185164.45 | −1.26% | 694653.38 | 694655.89 | +0.00% |
| explode/comma/short | 334.33 | 333.13 | −0.36% | 1767.01 | 1767.00 | −0.00% |
| explode/comma/4k | 8084.49 | 7727.46 | −2.63% | 39329.17 | 39329.19 | +0.00% |
| explode/comma/64k | 156813.92 | 155896.30 | −0.59% | 582633.13 | 582635.11 | +0.00% |
| parse-records/4k | 36772.34 | 36232.34 | −0.52% | 156829.99 | 156829.60 | −0.00% |
| parse-query/4k | 96492.63 | 96226.29 | −0.28% | 445875.52 | 445874.96 | −0.00% |
| parse-http/small | 3084.07 | 3131.71 | +1.45% | 13469.01 | 13469.01 | −0.00% |
| parse-http/body64k | 3101.29 | 3120.80 | +0.63% | 13465.02 | 13465.02 | +0.00% |
| scan-template/4k | 16116.34 | 16013.18 | −0.37% | 71214.28 | 71214.27 | −0.00% |
| render-template/4k | 28885.37 | 24167.01 | −15.99% | 78018.42 | 64102.43 | −17.84% |
| log-contains/event/post/early | 136.38 | 99.33 | −26.98% | 568.00 | 426.00 | −25.00% |
| log-contains/level/post/early | 147.41 | 112.98 | −23.60% | 601.00 | 459.00 | −23.63% |
| log-contains/event/thread/clean | 72697.69 | 64674.26 | −11.04% | 117828.27 | 117686.29 | −0.12% |
| log-filter/thread/clean | 210867.34 | 209017.13 | +0.52% | 496040.94 | 496040.29 | −0.00% |
| log-contains/event/thread/early | 135.99 | 100.01 | −26.57% | 568.00 | 426.00 | −25.00% |
| log-contains/level/thread/early | 147.87 | 112.99 | −23.56% | 601.00 | 459.00 | −23.63% |
| log-contains/event/thread/late | 64502.46 | 67326.09 | +4.46% | 117674.31 | 117532.44 | −0.12% |
| log-filter/thread/late | 210745.98 | 208012.12 | −0.05% | 495785.55 | 495787.39 | +0.00% |

## Intel / GCC 14.2

| Case | Stock, µs | Change, µs | Δ time | Stock spread | Change spread | Result | Source |
|---|--:|--:|--:|--:|--:|--:|---|
| banlist12/en/comment/clean | 0.5058 | 0.5074 | +0.32% | 0.60% | 0.59% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/en/comment/early | 0.0312 | 0.0314 | +0.52% | 1.30% | 0.95% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/en/comment/late | 0.5518 | 0.5523 | +0.09% | 0.51% | 0.59% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/en/post/clean | 3.5770 | 3.4860 | −2.54% | 0.98% | 0.83% | Faster | [gcc14-focus](../data/intel/gcc14-focus.json) |
| banlist12/en/post/early | 0.0314 | 0.0313 | −0.42% | 1.48% | 1.61% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/en/post/late | 3.6145 | 3.5363 | −2.16% | 1.93% | 1.96% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/en/thread/clean | 219.7972 | 220.4274 | +0.29% | 0.18% | 0.46% | Unclear | [gcc14-focus](../data/intel/gcc14-focus.json) |
| banlist12/en/thread/early | 0.0314 | 0.0313 | −0.19% | 0.90% | 0.79% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/en/thread/late | 220.2629 | 220.4383 | +0.08% | 0.18% | 0.26% | Unclear | [gcc14-focus](../data/intel/gcc14-focus.json) |
| banlist12/ru/comment/clean | 3.0441 | 3.0436 | −0.02% | 0.31% | 0.42% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/ru/comment/early | 0.0315 | 0.0315 | −0.11% | 1.04% | 1.21% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/ru/comment/late | 3.4094 | 3.4095 | +0.00% | 0.09% | 0.16% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/ru/post/clean | 3.6223 | 3.5413 | −2.24% | 0.45% | 0.87% | Faster | [gcc14-focus](../data/intel/gcc14-focus.json) |
| banlist12/ru/post/early | 0.0313 | 0.0314 | +0.54% | 0.97% | 1.39% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/ru/post/late | 3.8075 | 3.7052 | −2.69% | 0.78% | 0.37% | Faster | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/ru/thread/clean | 310.9561 | 304.3250 | −2.13% | 0.22% | 0.28% | Faster | [gcc14-focus](../data/intel/gcc14-focus.json) |
| banlist12/ru/thread/early | 0.0315 | 0.0313 | −0.45% | 0.89% | 0.96% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/ru/thread/late | 311.1486 | 304.8168 | −2.03% | 0.17% | 0.31% | Faster | [gcc14-focus](../data/intel/gcc14-focus.json) |
| banlist12/es/comment/clean | 0.5635 | 0.5642 | +0.12% | 0.59% | 0.51% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/es/post/clean | 3.3812 | 3.1966 | −5.46% | 0.81% | 0.51% | Faster | [gcc14-focus](../data/intel/gcc14-focus.json) |
| banlist12/es/post/early | 0.0313 | 0.0312 | −0.20% | 0.90% | 1.09% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/es/thread/clean | 226.7860 | 227.2420 | +0.20% | 0.31% | 0.28% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/ar/comment/clean | 2.5349 | 2.5328 | −0.08% | 0.17% | 0.22% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/ar/comment/late | 2.8774 | 2.8790 | +0.06% | 0.15% | 0.18% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/ar/post/clean | 4.9415 | 4.8488 | −1.88% | 0.42% | 0.27% | Faster | [gcc14-focus](../data/intel/gcc14-focus.json) |
| banlist12/ar/post/early | 0.0314 | 0.0313 | −0.13% | 1.10% | 1.11% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/ar/thread/clean | 360.4829 | 361.6382 | +0.32% | 1.01% | 0.74% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/hi/comment/clean | 3.6768 | 3.6743 | −0.07% | 0.15% | 0.13% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/hi/comment/late | 4.2311 | 4.2260 | −0.12% | 0.17% | 0.17% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/hi/post/clean | 3.1497 | 3.0277 | −3.87% | 0.53% | 0.31% | Faster | [gcc14-focus](../data/intel/gcc14-focus.json) |
| banlist12/hi/post/early | 0.0475 | 0.0396 | −16.60% | 0.82% | 1.98% | Faster | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/hi/thread/clean | 257.8595 | 258.5133 | +0.25% | 0.35% | 0.23% | Unclear | [gcc14-focus](../data/intel/gcc14-focus.json) |
| banlist12/hi/thread/late | 258.5873 | 259.1161 | +0.20% | 0.44% | 0.32% | Unclear | [gcc14-focus](../data/intel/gcc14-focus.json) |
| banlist12/zh/comment/clean | 0.5612 | 0.5617 | +0.09% | 1.26% | 1.05% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/zh/post/clean | 2.6545 | 2.5015 | −5.77% | 0.21% | 0.69% | Faster | [gcc14-focus](../data/intel/gcc14-focus.json) |
| banlist12/zh/post/early | 0.0462 | 0.0380 | −17.77% | 0.79% | 1.76% | Faster | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/zh/thread/clean | 199.5184 | 199.9076 | +0.20% | 0.22% | 0.40% | Unclear | [gcc14-focus](../data/intel/gcc14-focus.json) |
| banlist12/ja/comment/clean | 1.6934 | 1.6936 | +0.01% | 0.17% | 0.25% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/ja/comment/late | 1.8470 | 1.8459 | −0.06% | 0.35% | 0.20% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/ja/post/clean | 4.0006 | 3.8729 | −3.19% | 0.85% | 0.83% | Faster | [gcc14-focus](../data/intel/gcc14-focus.json) |
| banlist12/ja/post/early | 0.0450 | 0.0367 | −18.35% | 1.37% | 1.41% | Faster | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/ja/thread/clean | 298.7526 | 298.4905 | −0.09% | 0.51% | 0.22% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/ko/comment/clean | 1.0006 | 0.9968 | −0.38% | 1.53% | 1.01% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/ko/post/clean | 3.8260 | 3.7381 | −2.30% | 0.98% | 0.56% | Faster | [gcc14-focus](../data/intel/gcc14-focus.json) |
| banlist12/ko/post/early | 0.0314 | 0.0313 | −0.37% | 0.90% | 1.45% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/ko/thread/clean | 254.2450 | 254.5846 | +0.13% | 0.25% | 0.35% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/emoji/comment/clean | 0.3846 | 0.3838 | −0.19% | 1.00% | 1.19% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/emoji/post/clean | 3.2012 | 3.0873 | −3.56% | 1.15% | 0.89% | Faster | [gcc14-focus](../data/intel/gcc14-focus.json) |
| banlist12/emoji/post/early | 0.0313 | 0.0313 | +0.03% | 0.84% | 0.93% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| banlist12/emoji/thread/clean | 197.9345 | 197.9140 | −0.01% | 0.28% | 0.27% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| explode/pipe2/short | 0.0798 | 0.0797 | −0.07% | 0.55% | 0.61% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| explode/pipe2/4k | 2.4345 | 2.4200 | −0.59% | 1.01% | 0.94% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| explode/pipe2/64k | 47.2009 | 47.0479 | −0.32% | 0.98% | 0.61% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| explode/colon2/short | 0.0925 | 0.0929 | +0.40% | 0.92% | 0.83% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| explode/colon2/4k | 2.4194 | 2.4270 | +0.32% | 0.53% | 0.92% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| explode/colon2/64k | 47.0601 | 47.0265 | −0.07% | 0.44% | 0.46% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| explode/crlf/short | 0.1047 | 0.1054 | +0.63% | 0.79% | 1.03% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| explode/crlf/4k | 2.4787 | 2.3668 | −4.51% | 1.61% | 0.77% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| explode/crlf/64k | 47.3335 | 47.4465 | +0.24% | 0.82% | 0.44% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| explode/comma/short | 0.0811 | 0.0809 | −0.27% | 0.65% | 0.49% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| explode/comma/4k | 1.9580 | 1.9571 | −0.05% | 1.81% | 2.39% | Unclear | [gcc14-quality-recheck](../data/intel/gcc14-quality-recheck.json) |
| explode/comma/64k | 40.5824 | 40.7395 | +0.39% | 0.40% | 0.46% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| parse-records/4k | 9.3207 | 9.4469 | +1.35% | 0.70% | 0.82% | Slower | [gcc14-full233](../data/intel/gcc14-full233.json) |
| parse-query/4k | 25.3014 | 25.2431 | −0.23% | 0.67% | 0.82% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| parse-http/small | 0.8016 | 0.7889 | −1.59% | 0.86% | 0.42% | Faster | [gcc14-focus](../data/intel/gcc14-focus.json) |
| parse-http/body64k | 0.8023 | 0.7905 | −1.48% | 0.93% | 0.44% | Unclear | [gcc14-focus](../data/intel/gcc14-focus.json) |
| scan-template/4k | 4.2197 | 4.2096 | −0.24% | 0.75% | 0.38% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| render-template/4k | 7.3918 | 6.4248 | −13.08% | 1.40% | 0.88% | Faster | [gcc14-focus](../data/intel/gcc14-focus.json) |
| log-contains/event/post/early | 0.0348 | 0.0284 | −18.49% | 2.52% | 4.48% | Faster | [gcc14-full233](../data/intel/gcc14-full233.json) |
| log-contains/level/post/early | 0.0390 | 0.0331 | −15.09% | 2.55% | 3.60% | Faster | [gcc14-full233](../data/intel/gcc14-full233.json) |
| log-contains/event/thread/clean | 17.6087 | 17.2725 | −1.91% | 0.49% | 0.50% | Faster | [gcc14-focus](../data/intel/gcc14-focus.json) |
| log-filter/thread/clean | 55.7685 | 55.5561 | −0.38% | 0.61% | 0.54% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |
| log-contains/event/thread/early | 0.0345 | 0.0283 | −18.05% | 1.41% | 3.46% | Faster | [gcc14-full233](../data/intel/gcc14-full233.json) |
| log-contains/level/thread/early | 0.0392 | 0.0330 | −15.79% | 3.88% | 3.86% | Faster | [gcc14-quality-recheck](../data/intel/gcc14-quality-recheck.json) |
| log-contains/event/thread/late | 17.2852 | 17.2126 | −0.42% | 0.34% | 0.26% | Unclear | [gcc14-focus](../data/intel/gcc14-focus.json) |
| log-filter/thread/late | 55.6882 | 55.5160 | −0.31% | 0.47% | 0.66% | Unclear | [gcc14-full233](../data/intel/gcc14-full233.json) |

### Separate counters

| Case | Stock cycles¹ | Change cycles¹ | Δ cycles¹ | Stock instr. | Change instr. | Δ instr. |
|---|--:|--:|--:|--:|--:|--:|
| banlist12/en/comment/clean | 1919.21 | 1918.98 | +0.01% | 7316.20 | 7316.20 | −0.00% |
| banlist12/en/comment/early | 121.50 | 121.93 | +0.25% | 551.01 | 551.01 | +0.00% |
| banlist12/en/comment/late | 2100.65 | 2085.90 | −0.71% | 7814.19 | 7814.16 | −0.00% |
| banlist12/en/post/clean | 13508.69 | 13224.22 | −1.73% | 24859.24 | 23439.21 | −5.71% |
| banlist12/en/post/early | 118.20 | 118.57 | +0.53% | 544.01 | 544.01 | −0.00% |
| banlist12/en/post/late | 13721.79 | 13395.99 | −2.45% | 25245.18 | 23825.30 | −5.62% |
| banlist12/en/thread/clean | 840113.03 | 847245.43 | +0.75% | 1141027.89 | 1139609.67 | −0.12% |
| banlist12/en/thread/early | 119.08 | 119.21 | −0.15% | 544.01 | 544.01 | +0.00% |
| banlist12/en/thread/late | 890680.92 | 843097.91 | −5.34% | 1141484.12 | 1140065.53 | −0.12% |
| banlist12/ru/comment/clean | 11537.77 | 11530.47 | −0.03% | 23747.24 | 23747.14 | −0.00% |
| banlist12/ru/comment/early | 119.68 | 119.17 | −0.13% | 542.01 | 542.01 | −0.00% |
| banlist12/ru/comment/late | 12905.69 | 12902.35 | −0.08% | 25806.29 | 25806.25 | −0.00% |
| banlist12/ru/post/clean | 13802.54 | 13406.16 | −3.29% | 28602.27 | 27644.30 | −3.35% |
| banlist12/ru/post/early | 119.22 | 119.22 | +0.19% | 544.01 | 544.01 | +0.00% |
| banlist12/ru/post/late | 14521.22 | 14046.58 | −3.32% | 29704.52 | 28746.36 | −3.23% |
| banlist12/ru/thread/clean | 1178244.19 | 1155638.93 | −1.92% | 1318217.79 | 1317371.46 | −0.06% |
| banlist12/ru/thread/early | 118.13 | 119.23 | +0.69% | 544.01 | 544.01 | −0.00% |
| banlist12/ru/thread/late | 1179264.80 | 1154199.44 | −2.13% | 1319157.21 | 1318317.78 | −0.06% |
| banlist12/es/comment/clean | 2132.61 | 2137.64 | −0.09% | 7935.19 | 7935.20 | +0.00% |
| banlist12/es/post/clean | 12682.53 | 11955.80 | −5.39% | 24851.23 | 23431.23 | −5.71% |
| banlist12/es/post/early | 118.24 | 118.98 | +0.55% | 544.01 | 544.01 | −0.00% |
| banlist12/es/thread/clean | 863798.12 | 877466.30 | +0.68% | 1145529.92 | 1144110.06 | −0.12% |
| banlist12/ar/comment/clean | 9587.91 | 9578.36 | −0.10% | 20216.92 | 20216.91 | −0.00% |
| banlist12/ar/comment/late | 10889.20 | 10912.76 | +0.20% | 22384.94 | 22384.91 | −0.00% |
| banlist12/ar/post/clean | 18699.12 | 18313.78 | −2.13% | 35753.40 | 34333.32 | −3.97% |
| banlist12/ar/post/early | 119.71 | 119.27 | −0.37% | 544.01 | 544.01 | −0.00% |
| banlist12/ar/thread/clean | 1355954.95 | 1376428.55 | +1.51% | 1863739.42 | 1862319.25 | −0.08% |
| banlist12/hi/comment/clean | 13904.33 | 13911.31 | +0.24% | 27874.28 | 27874.50 | +0.00% |
| banlist12/hi/comment/late | 16024.66 | 16001.32 | −0.15% | 31946.73 | 31946.43 | −0.00% |
| banlist12/hi/post/clean | 11915.22 | 11569.62 | −3.23% | 25683.22 | 24432.24 | −4.87% |
| banlist12/hi/post/early | 181.51 | 151.89 | −16.55% | 867.02 | 725.02 | −16.38% |
| banlist12/hi/thread/clean | 970583.81 | 984437.54 | +0.72% | 1114961.50 | 1113760.63 | −0.11% |
| banlist12/hi/thread/late | 978939.87 | 983261.40 | +0.44% | 1116149.27 | 1114955.06 | −0.11% |
| banlist12/zh/comment/clean | 2121.75 | 2123.93 | +0.10% | 7297.19 | 7297.20 | +0.00% |
| banlist12/zh/post/clean | 10031.17 | 9644.74 | −3.81% | 20323.16 | 18761.20 | −7.69% |
| banlist12/zh/post/early | 176.14 | 145.76 | −17.63% | 828.01 | 686.01 | −17.15% |
| banlist12/zh/thread/clean | 754511.83 | 809705.79 | +3.40% | 908032.50 | 906467.96 | −0.17% |
| banlist12/ja/comment/clean | 6408.15 | 6410.55 | +0.04% | 14000.60 | 14000.61 | +0.00% |
| banlist12/ja/comment/late | 7008.06 | 6983.77 | −0.35% | 15644.63 | 15644.61 | −0.00% |
| banlist12/ja/post/clean | 15270.45 | 14654.04 | −4.04% | 29581.27 | 28019.31 | −5.28% |
| banlist12/ja/post/early | 173.83 | 141.28 | −18.72% | 789.01 | 647.02 | −18.00% |
| banlist12/ja/thread/clean | 1144286.06 | 1251950.42 | +8.19% | 1463735.16 | 1462174.07 | −0.11% |
| banlist12/ko/comment/clean | 3787.22 | 3771.87 | −0.41% | 10371.38 | 10371.31 | −0.00% |
| banlist12/ko/post/clean | 14401.16 | 14259.41 | −1.74% | 27630.25 | 26210.27 | −5.14% |
| banlist12/ko/post/early | 118.75 | 118.64 | −0.02% | 544.01 | 544.01 | +0.00% |
| banlist12/ko/thread/clean | 998141.68 | 994744.55 | −0.34% | 1282858.63 | 1281443.51 | −0.11% |
| banlist12/emoji/comment/clean | 1460.70 | 1455.32 | −0.37% | 5999.12 | 5999.15 | +0.00% |
| banlist12/emoji/post/clean | 12158.37 | 11835.18 | −2.66% | 23044.23 | 21624.23 | −6.16% |
| banlist12/emoji/post/early | 118.94 | 118.72 | −0.18% | 544.01 | 544.01 | +0.00% |
| banlist12/emoji/thread/clean | 769610.78 | 754130.82 | −2.01% | 1035183.38 | 1033769.46 | −0.14% |
| explode/pipe2/short | 304.20 | 305.66 | +0.48% | 1592.01 | 1592.01 | +0.00% |
| explode/pipe2/4k | 9417.16 | 9201.13 | −2.46% | 43407.12 | 43407.22 | +0.00% |
| explode/pipe2/64k | 177836.81 | 179295.52 | +1.20% | 697158.43 | 697158.18 | −0.00% |
| explode/colon2/short | 351.76 | 352.74 | +0.28% | 1822.01 | 1822.00 | −0.00% |
| explode/colon2/4k | 9135.75 | 9146.20 | +0.95% | 43356.15 | 43356.20 | +0.00% |
| explode/colon2/64k | 176821.50 | 178795.51 | +1.12% | 693228.69 | 693232.26 | +0.00% |
| explode/crlf/short | 400.70 | 396.08 | −1.14% | 2065.01 | 2065.00 | −0.00% |
| explode/crlf/4k | 8989.96 | 8894.52 | −1.99% | 42218.19 | 42218.25 | +0.00% |
| explode/crlf/64k | 177060.68 | 178379.32 | +1.37% | 694664.78 | 694666.46 | +0.00% |
| explode/comma/short | 307.32 | 307.60 | −0.16% | 1767.01 | 1767.01 | −0.00% |
| explode/comma/4k | 7255.98 | 7437.67 | +2.50% | 39329.04 | 39329.03 | −0.00% |
| explode/comma/64k | 155728.73 | 155707.48 | −0.43% | 582640.22 | 582640.10 | −0.00% |
| parse-records/4k | 35123.37 | 35775.72 | +1.55% | 156341.75 | 156341.75 | −0.00% |
| parse-query/4k | 96173.47 | 96125.94 | +0.37% | 444196.93 | 444197.79 | +0.00% |
| parse-http/small | 3022.71 | 3001.88 | −1.04% | 13363.01 | 13363.02 | +0.00% |
| parse-http/body64k | 3041.40 | 3026.95 | −0.47% | 13359.01 | 13359.01 | −0.00% |
| scan-template/4k | 15951.23 | 15868.54 | −0.42% | 70187.15 | 70187.28 | +0.00% |
| render-template/4k | 27876.69 | 24721.46 | −11.30% | 79166.39 | 65250.38 | −17.58% |
| log-contains/event/post/early | 134.75 | 106.66 | −21.30% | 573.00 | 431.00 | −24.78% |
| log-contains/level/post/early | 152.66 | 120.61 | −21.00% | 607.00 | 465.00 | −23.39% |
| log-contains/event/thread/clean | 66959.59 | 67516.26 | −2.23% | 123459.34 | 123317.50 | −0.11% |
| log-filter/thread/clean | 218703.81 | 210374.72 | −3.87% | 494031.00 | 494030.43 | −0.00% |
| log-contains/event/thread/early | 138.63 | 103.92 | −24.30% | 573.00 | 431.00 | −24.78% |
| log-contains/level/thread/early | 150.74 | 120.80 | −19.69% | 607.00 | 465.00 | −23.39% |
| log-contains/event/thread/late | 65894.64 | 71940.03 | +9.43% | 123294.30 | 123152.38 | −0.12% |
| log-filter/thread/late | 210450.35 | 209512.22 | −0.31% | 493779.95 | 493778.91 | −0.00% |

## Intel / Clang 18.1

| Case | Stock, µs | Change, µs | Δ time | Stock spread | Change spread | Result | Source |
|---|--:|--:|--:|--:|--:|--:|---|
| banlist12/en/comment/clean | 0.5299 | 0.5289 | −0.18% | 0.74% | 0.45% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/en/comment/early | 0.0398 | 0.0389 | −2.32% | 3.68% | 2.79% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/en/comment/late | 0.5688 | 0.5689 | +0.02% | 0.43% | 0.42% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/en/post/clean | 3.4900 | 3.4963 | +0.18% | 0.15% | 0.06% | Unclear | [clang18-focus](../data/intel/clang18-focus.json) |
| banlist12/en/post/early | 0.0397 | 0.0395 | −0.34% | 3.85% | 2.83% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/en/post/late | 3.5538 | 3.5442 | −0.27% | 0.50% | 0.15% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/en/thread/clean | 226.0742 | 217.4341 | −3.82% | 0.13% | 0.14% | Faster | [clang18-focus](../data/intel/clang18-focus.json) |
| banlist12/en/thread/early | 0.0395 | 0.0387 | −2.11% | 3.34% | 1.93% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/en/thread/late | 226.2447 | 217.6477 | −3.80% | 0.13% | 0.19% | Faster | [clang18-focus](../data/intel/clang18-focus.json) |
| banlist12/ru/comment/clean | 3.0798 | 3.0801 | +0.01% | 0.23% | 0.38% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/ru/comment/early | 0.0396 | 0.0394 | −0.50% | 3.69% | 3.01% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/ru/comment/late | 3.4206 | 3.4229 | +0.07% | 0.12% | 0.26% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/ru/post/clean | 3.7192 | 3.6137 | −2.84% | 0.20% | 0.30% | Faster | [clang18-focus](../data/intel/clang18-focus.json) |
| banlist12/ru/post/early | 0.0396 | 0.0390 | −1.60% | 4.43% | 2.76% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/ru/post/late | 3.8764 | 3.7599 | −3.01% | 0.20% | 0.28% | Faster | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/ru/thread/clean | 311.1181 | 305.6158 | −1.77% | 0.14% | 0.12% | Faster | [clang18-focus](../data/intel/clang18-focus.json) |
| banlist12/ru/thread/early | 0.0392 | 0.0391 | −0.31% | 3.40% | 2.44% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/ru/thread/late | 311.5055 | 305.8425 | −1.82% | 0.17% | 0.08% | Faster | [clang18-focus](../data/intel/clang18-focus.json) |
| banlist12/es/comment/clean | 0.5779 | 0.5754 | −0.43% | 0.68% | 0.68% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/es/post/clean | 3.3705 | 3.1791 | −5.68% | 0.09% | 0.12% | Faster | [clang18-focus](../data/intel/clang18-focus.json) |
| banlist12/es/post/early | 0.0392 | 0.0383 | −2.36% | 3.64% | 1.87% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/es/thread/clean | 231.9562 | 223.2037 | −3.77% | 0.24% | 0.22% | Faster | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/ar/comment/clean | 2.5628 | 2.5651 | +0.09% | 0.20% | 0.32% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/ar/comment/late | 2.8450 | 2.8475 | +0.09% | 0.19% | 0.38% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/ar/post/clean | 4.9597 | 4.8490 | −2.23% | 0.13% | 0.08% | Faster | [clang18-focus](../data/intel/clang18-focus.json) |
| banlist12/ar/post/early | 0.0407 | 0.0405 | −0.41% | 2.60% | 2.16% | Unclear | [clang18-quality-recheck](../data/intel/clang18-quality-recheck.json) |
| banlist12/ar/thread/clean | 370.7867 | 372.3374 | +0.42% | 0.43% | 0.61% | Unclear | [clang18-quality-recheck](../data/intel/clang18-quality-recheck.json) |
| banlist12/hi/comment/clean | 3.6349 | 3.6297 | −0.14% | 0.27% | 0.21% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/hi/comment/late | 4.3019 | 4.3048 | +0.07% | 0.21% | 0.41% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/hi/post/clean | 3.1477 | 3.0281 | −3.80% | 0.13% | 0.12% | Faster | [clang18-focus](../data/intel/clang18-focus.json) |
| banlist12/hi/post/early | 0.0484 | 0.0441 | −8.97% | 1.05% | 1.94% | Faster | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/hi/thread/clean | 257.4148 | 254.3987 | −1.17% | 0.48% | 0.17% | Faster | [clang18-focus](../data/intel/clang18-focus.json) |
| banlist12/hi/thread/late | 256.9256 | 254.9467 | −0.77% | 0.48% | 0.18% | Unclear | [clang18-focus](../data/intel/clang18-focus.json) |
| banlist12/zh/comment/clean | 0.5630 | 0.5636 | +0.11% | 0.74% | 0.58% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/zh/post/clean | 2.7009 | 2.4852 | −7.98% | 0.08% | 0.07% | Faster | [clang18-focus](../data/intel/clang18-focus.json) |
| banlist12/zh/post/early | 0.0466 | 0.0441 | −5.39% | 1.43% | 2.06% | Faster | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/zh/thread/clean | 198.7861 | 193.8668 | −2.47% | 0.18% | 0.17% | Faster | [clang18-focus](../data/intel/clang18-focus.json) |
| banlist12/ja/comment/clean | 1.6819 | 1.6909 | +0.54% | 0.22% | 0.20% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/ja/comment/late | 1.8716 | 1.8731 | +0.08% | 0.30% | 0.47% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/ja/post/clean | 4.0227 | 3.8399 | −4.54% | 0.08% | 0.15% | Faster | [clang18-focus](../data/intel/clang18-focus.json) |
| banlist12/ja/post/early | 0.0433 | 0.0416 | −3.97% | 2.23% | 2.54% | Faster | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/ja/thread/clean | 303.1972 | 308.4958 | +1.75% | 0.78% | 0.35% | Slower | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/ko/comment/clean | 1.1460 | 1.1470 | +0.09% | 0.36% | 0.54% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/ko/post/clean | 3.7714 | 3.6216 | −3.97% | 0.11% | 0.07% | Faster | [clang18-focus](../data/intel/clang18-focus.json) |
| banlist12/ko/post/early | 0.0401 | 0.0394 | −1.55% | 1.22% | 2.09% | Unclear | [clang18-quality-recheck](../data/intel/clang18-quality-recheck.json) |
| banlist12/ko/thread/clean | 255.7706 | 253.5957 | −0.85% | 0.28% | 0.28% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/emoji/comment/clean | 0.4335 | 0.4345 | +0.24% | 0.98% | 2.81% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/emoji/post/clean | 3.1371 | 2.9618 | −5.59% | 0.17% | 0.06% | Faster | [clang18-focus](../data/intel/clang18-focus.json) |
| banlist12/emoji/post/early | 0.0384 | 0.0387 | +0.66% | 2.26% | 2.06% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| banlist12/emoji/thread/clean | 202.3667 | 196.4695 | −2.91% | 0.21% | 0.25% | Faster | [clang18-full233](../data/intel/clang18-full233.json) |
| explode/pipe2/short | 0.0871 | 0.0887 | +1.88% | 2.76% | 3.17% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| explode/pipe2/4k | 2.5269 | 2.5789 | +2.06% | 0.77% | 3.62% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| explode/pipe2/64k | 49.9422 | 49.8238 | −0.24% | 0.27% | 0.64% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| explode/colon2/short | 0.1033 | 0.1031 | −0.19% | 1.39% | 2.19% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| explode/colon2/4k | 2.5552 | 2.4963 | −2.31% | 0.89% | 1.24% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| explode/colon2/64k | 49.5764 | 49.6967 | +0.24% | 0.81% | 1.41% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| explode/crlf/short | 0.1165 | 0.1173 | +0.65% | 2.71% | 2.01% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| explode/crlf/4k | 2.4999 | 2.4446 | −2.21% | 4.36% | 2.00% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| explode/crlf/64k | 49.9138 | 49.7415 | −0.35% | 0.84% | 0.55% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| explode/comma/short | 0.0972 | 0.0955 | −1.75% | 1.78% | 2.44% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| explode/comma/4k | 2.2031 | 2.1221 | −3.68% | 1.12% | 2.41% | Noise | [clang18-quality-recheck](../data/intel/clang18-quality-recheck.json) |
| explode/comma/64k | 41.8868 | 41.4621 | −1.01% | 1.88% | 1.31% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| parse-records/4k | 10.5792 | 10.5142 | −0.61% | 1.99% | 1.39% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| parse-query/4k | 30.6200 | 30.4641 | −0.51% | 1.23% | 1.28% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| parse-http/small | 0.8955 | 0.8887 | −0.76% | 0.49% | 0.56% | Unclear | [clang18-focus](../data/intel/clang18-focus.json) |
| parse-http/body64k | 0.9032 | 0.8960 | −0.80% | 1.89% | 1.39% | Unclear | [clang18-focus](../data/intel/clang18-focus.json) |
| scan-template/4k | 4.8341 | 4.8571 | +0.47% | 0.37% | 0.78% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| render-template/4k | 6.8738 | 6.2907 | −8.48% | 1.29% | 0.59% | Faster | [clang18-focus](../data/intel/clang18-focus.json) |
| log-contains/event/post/early | 0.0250 | 0.0234 | −6.31% | 1.17% | 1.01% | Faster | [clang18-full233](../data/intel/clang18-full233.json) |
| log-contains/level/post/early | 0.0279 | 0.0270 | −3.24% | 1.34% | 1.36% | Faster | [clang18-full233](../data/intel/clang18-full233.json) |
| log-contains/event/thread/clean | 17.2550 | 17.8645 | +3.53% | 0.11% | 1.26% | Slower | [clang18-focus](../data/intel/clang18-focus.json) |
| log-filter/thread/clean | 57.2203 | 57.2166 | −0.01% | 0.51% | 0.68% | Unclear | [clang18-quality-recheck](../data/intel/clang18-quality-recheck.json) |
| log-contains/event/thread/early | 0.0248 | 0.0235 | −5.20% | 2.88% | 1.14% | Faster | [clang18-full233](../data/intel/clang18-full233.json) |
| log-contains/level/thread/early | 0.0275 | 0.0270 | −1.69% | 3.71% | 1.32% | Unclear | [clang18-full233](../data/intel/clang18-full233.json) |
| log-contains/event/thread/late | 17.2360 | 17.9109 | +3.92% | 0.10% | 0.98% | Slower | [clang18-focus](../data/intel/clang18-focus.json) |
| log-filter/thread/late | 57.1323 | 57.1180 | −0.02% | 0.36% | 0.44% | Unclear | [clang18-quality-recheck](../data/intel/clang18-quality-recheck.json) |

### Separate counters

| Case | Stock cycles¹ | Change cycles¹ | Δ cycles¹ | Stock instr. | Change instr. | Δ instr. |
|---|--:|--:|--:|--:|--:|--:|
| banlist12/en/comment/clean | 2012.15 | 2010.22 | +0.04% | 7728.19 | 7728.18 | −0.00% |
| banlist12/en/comment/early | 155.08 | 151.91 | −2.04% | 699.01 | 699.02 | +0.00% |
| banlist12/en/comment/late | 2154.09 | 2166.19 | −0.53% | 8239.20 | 8239.23 | +0.00% |
| banlist12/en/post/clean | 13251.61 | 13226.21 | −0.18% | 24712.26 | 22334.25 | −9.62% |
| banlist12/en/post/early | 150.13 | 150.52 | +0.44% | 690.02 | 690.01 | −0.00% |
| banlist12/en/post/late | 13442.50 | 13426.19 | +0.04% | 25128.40 | 22726.39 | −9.56% |
| banlist12/en/thread/clean | 858198.24 | 830414.84 | −3.24% | 1195397.96 | 1077290.29 | −9.88% |
| banlist12/en/thread/early | 151.75 | 150.05 | −0.09% | 690.02 | 690.01 | −0.00% |
| banlist12/en/thread/late | 858460.59 | 830210.37 | −3.27% | 1195882.23 | 1077747.57 | −9.88% |
| banlist12/ru/comment/clean | 11638.54 | 11657.38 | +0.11% | 23762.05 | 23762.24 | +0.00% |
| banlist12/ru/comment/early | 151.12 | 150.67 | −0.52% | 690.01 | 690.02 | +0.00% |
| banlist12/ru/comment/late | 12978.03 | 12947.15 | −0.24% | 25806.30 | 25806.44 | +0.00% |
| banlist12/ru/post/clean | 14133.09 | 13763.23 | −2.62% | 27973.28 | 26494.25 | −5.29% |
| banlist12/ru/post/early | 150.13 | 149.23 | −1.09% | 690.01 | 690.01 | +0.00% |
| banlist12/ru/post/late | 14640.94 | 14246.54 | −2.69% | 29133.57 | 27606.58 | −5.24% |
| banlist12/ru/thread/clean | 1180958.93 | 1159889.49 | −1.66% | 1368410.15 | 1296458.91 | −5.26% |
| banlist12/ru/thread/early | 152.19 | 150.60 | −1.75% | 690.02 | 690.02 | −0.00% |
| banlist12/ru/thread/late | 1180164.65 | 1159358.89 | −1.75% | 1369390.72 | 1297408.78 | −5.26% |
| banlist12/es/comment/clean | 2182.55 | 2189.38 | +0.31% | 8325.21 | 8325.24 | +0.00% |
| banlist12/es/post/clean | 12764.28 | 12057.57 | −5.56% | 24687.21 | 22379.23 | −9.35% |
| banlist12/es/post/early | 151.25 | 146.93 | −3.19% | 690.01 | 690.02 | +0.00% |
| banlist12/es/thread/clean | 880530.44 | 848640.95 | −3.31% | 1198317.58 | 1082646.56 | −9.65% |
| banlist12/ar/comment/clean | 9692.67 | 9701.03 | −0.00% | 20186.97 | 20186.87 | −0.00% |
| banlist12/ar/comment/late | 10780.14 | 10767.81 | −0.18% | 22309.97 | 22309.97 | −0.00% |
| banlist12/ar/post/clean | 18844.09 | 18372.09 | −2.37% | 34923.35 | 32923.40 | −5.73% |
| banlist12/ar/post/early | 150.46 | 150.85 | +0.26% | 690.00 | 690.00 | −0.00% |
| banlist12/ar/thread/clean | 1406545.31 | 1421291.75 | +1.05% | 1883085.00 | 1786514.11 | −5.13% |
| banlist12/hi/comment/clean | 13772.23 | 13784.72 | −0.01% | 27657.45 | 27657.46 | +0.00% |
| banlist12/hi/comment/late | 16288.82 | 16292.13 | −0.04% | 31641.76 | 31641.87 | +0.00% |
| banlist12/hi/post/clean | 11955.99 | 11478.46 | −3.90% | 24894.24 | 23097.25 | −7.22% |
| banlist12/hi/post/early | 189.08 | 171.10 | −10.02% | 876.02 | 829.02 | −5.37% |
| banlist12/hi/thread/clean | 980993.07 | 966350.48 | −1.49% | 1173324.64 | 1084442.04 | −7.58% |
| banlist12/hi/thread/late | 978277.89 | 967971.12 | −0.62% | 1174575.58 | 1085626.89 | −7.57% |
| banlist12/zh/comment/clean | 2126.68 | 2125.11 | −0.08% | 7650.20 | 7650.20 | +0.00% |
| banlist12/zh/post/clean | 10242.90 | 9413.94 | −8.12% | 19908.15 | 17787.18 | −10.65% |
| banlist12/zh/post/early | 182.97 | 169.97 | −6.37% | 835.02 | 788.02 | −5.63% |
| banlist12/zh/thread/clean | 756961.16 | 738733.66 | −2.32% | 956193.83 | 852119.23 | −10.88% |
| banlist12/ja/comment/clean | 6380.57 | 6367.52 | −0.18% | 14219.66 | 14219.69 | +0.00% |
| banlist12/ja/comment/late | 7083.46 | 7089.46 | +0.08% | 15834.67 | 15834.73 | +0.00% |
| banlist12/ja/post/clean | 15273.74 | 14533.92 | −4.84% | 29066.28 | 26737.29 | −8.01% |
| banlist12/ja/post/early | 165.49 | 162.97 | −2.83% | 813.02 | 766.02 | −5.78% |
| banlist12/ja/thread/clean | 1150419.25 | 1164748.89 | +1.47% | 1511972.91 | 1395857.17 | −7.68% |
| banlist12/ko/comment/clean | 4341.14 | 4338.63 | −0.19% | 10653.42 | 10653.37 | −0.00% |
| banlist12/ko/post/clean | 14485.55 | 13975.16 | −3.49% | 27164.28 | 25126.27 | −7.50% |
| banlist12/ko/post/early | 152.40 | 150.20 | −1.65% | 690.00 | 690.00 | −0.00% |
| banlist12/ko/thread/clean | 969473.61 | 962758.85 | −0.76% | 1321034.89 | 1226529.08 | −7.15% |
| banlist12/emoji/comment/clean | 1634.70 | 1634.97 | −0.06% | 6397.14 | 6397.14 | +0.00% |
| banlist12/emoji/post/clean | 11920.23 | 11233.18 | −5.86% | 22787.24 | 20609.21 | −9.56% |
| banlist12/emoji/post/early | 152.26 | 151.66 | −0.25% | 690.01 | 690.01 | +0.00% |
| banlist12/emoji/thread/clean | 767455.17 | 861833.36 | −1.84% | 1083085.70 | 977484.79 | −9.75% |
| explode/pipe2/short | 328.62 | 329.82 | +0.04% | 1589.01 | 1589.01 | +0.00% |
| explode/pipe2/4k | 9672.51 | 9609.63 | −1.00% | 41554.11 | 41554.22 | +0.00% |
| explode/pipe2/64k | 195121.32 | 187565.99 | −0.94% | 664589.34 | 664587.55 | −0.00% |
| explode/colon2/short | 376.72 | 380.95 | +1.12% | 1805.00 | 1805.01 | +0.00% |
| explode/colon2/4k | 9644.42 | 9494.36 | −0.31% | 41481.23 | 41481.21 | −0.00% |
| explode/colon2/64k | 183671.88 | 184456.55 | +0.57% | 660796.33 | 660798.64 | +0.00% |
| explode/crlf/short | 423.34 | 423.58 | −0.27% | 2038.01 | 2038.01 | −0.00% |
| explode/crlf/4k | 9333.68 | 9284.24 | −0.46% | 40419.23 | 40419.13 | −0.00% |
| explode/crlf/64k | 187270.37 | 188882.01 | −0.01% | 662252.01 | 662248.08 | −0.00% |
| explode/comma/short | 338.61 | 386.42 | +4.46% | 1767.01 | 1767.01 | −0.00% |
| explode/comma/4k | 7945.58 | 7817.76 | −1.61% | 38436.02 | 38436.04 | +0.00% |
| explode/comma/64k | 155873.19 | 156500.70 | +0.19% | 569548.67 | 569548.60 | −0.00% |
| parse-records/4k | 38690.55 | 39037.00 | +0.90% | 157818.33 | 157819.15 | +0.00% |
| parse-query/4k | 112610.42 | 112932.94 | +0.16% | 462021.19 | 462022.49 | +0.00% |
| parse-http/small | 3409.47 | 3389.72 | −1.01% | 14049.01 | 14049.01 | −0.00% |
| parse-http/body64k | 3406.34 | 3425.65 | +0.93% | 14045.02 | 14045.01 | −0.00% |
| scan-template/4k | 18517.36 | 18482.42 | +0.10% | 75655.37 | 75655.42 | +0.00% |
| render-template/4k | 25910.18 | 24102.33 | −8.22% | 68031.33 | 59915.39 | −11.93% |
| log-contains/event/post/early | 95.92 | 90.76 | −5.38% | 448.00 | 393.00 | −12.28% |
| log-contains/level/post/early | 107.80 | 103.51 | −3.68% | 482.00 | 425.00 | −11.83% |
| log-contains/event/thread/clean | 65398.34 | 69843.68 | +6.80% | 128951.39 | 117648.21 | −8.77% |
| log-filter/thread/clean | 215528.83 | 217819.46 | +0.71% | 499326.42 | 499326.33 | −0.00% |
| log-contains/event/thread/early | 95.90 | 90.66 | −5.46% | 448.00 | 393.00 | −12.28% |
| log-contains/level/thread/early | 107.09 | 103.04 | −3.78% | 482.00 | 425.00 | −11.83% |
| log-contains/event/thread/late | 67136.69 | 68245.00 | +4.93% | 128784.22 | 117499.34 | −8.76% |
| log-filter/thread/late | 216771.41 | 215830.39 | −0.24% | 499094.43 | 499094.33 | −0.00% |

## Intel / Clang 20.1

| Case | Stock, µs | Change, µs | Δ time | Stock spread | Change spread | Result | Source |
|---|--:|--:|--:|--:|--:|--:|---|
| banlist12/en/comment/clean | 0.4901 | 0.4904 | +0.06% | 0.59% | 0.40% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/en/comment/early | 0.0274 | 0.0274 | +0.06% | 1.45% | 1.07% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/en/comment/late | 0.5335 | 0.5325 | −0.19% | 0.68% | 0.38% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/en/post/clean | 3.5143 | 3.2694 | −6.97% | 0.12% | 0.18% | Faster | [clang20-focus](../data/intel/clang20-focus.json) |
| banlist12/en/post/early | 0.0276 | 0.0275 | −0.37% | 1.93% | 1.17% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/en/post/late | 3.5673 | 3.3875 | −5.04% | 0.19% | 0.26% | Faster | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/en/thread/clean | 217.9654 | 227.5464 | +4.40% | 0.24% | 0.10% | Slower | [clang20-focus](../data/intel/clang20-focus.json) |
| banlist12/en/thread/early | 0.0279 | 0.0278 | −0.25% | 2.50% | 1.24% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/en/thread/late | 218.0044 | 227.6592 | +4.43% | 0.15% | 0.14% | Slower | [clang20-focus](../data/intel/clang20-focus.json) |
| banlist12/ru/comment/clean | 3.0449 | 3.0418 | −0.10% | 0.39% | 0.28% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/ru/comment/early | 0.0278 | 0.0275 | −1.15% | 3.48% | 1.10% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/ru/comment/late | 3.4218 | 3.4215 | −0.01% | 0.10% | 0.16% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/ru/post/clean | 3.6367 | 3.5565 | −2.20% | 0.11% | 0.04% | Faster | [clang20-focus](../data/intel/clang20-focus.json) |
| banlist12/ru/post/early | 0.0279 | 0.0275 | −1.27% | 2.40% | 0.83% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/ru/post/late | 3.8093 | 3.7361 | −1.92% | 0.21% | 0.09% | Faster | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/ru/thread/clean | 307.6727 | 308.9855 | +0.43% | 0.15% | 0.11% | Unclear | [clang20-focus](../data/intel/clang20-focus.json) |
| banlist12/ru/thread/early | 0.0276 | 0.0278 | +0.65% | 1.38% | 2.07% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/ru/thread/late | 307.8938 | 309.3196 | +0.46% | 0.13% | 0.15% | Unclear | [clang20-focus](../data/intel/clang20-focus.json) |
| banlist12/es/comment/clean | 0.5542 | 0.5536 | −0.11% | 0.54% | 0.59% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/es/post/clean | 3.2250 | 3.1406 | −2.62% | 0.13% | 0.11% | Faster | [clang20-focus](../data/intel/clang20-focus.json) |
| banlist12/es/post/early | 0.0275 | 0.0274 | −0.42% | 1.58% | 0.93% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/es/thread/clean | 223.6120 | 234.1284 | +4.70% | 0.21% | 0.14% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/ar/comment/clean | 2.5301 | 2.5324 | +0.09% | 0.27% | 0.27% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/ar/comment/late | 2.7961 | 2.7996 | +0.13% | 0.18% | 0.29% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/ar/post/clean | 4.9067 | 4.8025 | −2.12% | 0.10% | 0.06% | Faster | [clang20-focus](../data/intel/clang20-focus.json) |
| banlist12/ar/post/early | 0.0276 | 0.0274 | −0.58% | 1.15% | 0.77% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/ar/thread/clean | 362.4159 | 369.3155 | +1.90% | 0.21% | 0.19% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/hi/comment/clean | 3.6083 | 3.6046 | −0.10% | 0.21% | 0.21% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/hi/comment/late | 4.2784 | 4.2786 | +0.01% | 0.16% | 0.11% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/hi/post/clean | 3.0972 | 3.0178 | −2.56% | 0.17% | 0.06% | Faster | [clang20-focus](../data/intel/clang20-focus.json) |
| banlist12/hi/post/early | 0.0394 | 0.0376 | −4.67% | 1.33% | 1.33% | Faster | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/hi/thread/clean | 255.2522 | 259.4026 | +1.63% | 0.53% | 0.64% | Slower | [clang20-focus](../data/intel/clang20-focus.json) |
| banlist12/hi/thread/late | 256.3210 | 259.7873 | +1.35% | 0.42% | 0.72% | Slower | [clang20-focus](../data/intel/clang20-focus.json) |
| banlist12/zh/comment/clean | 0.5462 | 0.5461 | −0.02% | 0.84% | 0.62% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/zh/post/clean | 2.5133 | 2.4401 | −2.92% | 0.13% | 0.16% | Unclear | [clang20-focus](../data/intel/clang20-focus.json) |
| banlist12/zh/post/early | 0.0374 | 0.0359 | −4.07% | 1.52% | 1.02% | Faster | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/zh/thread/clean | 194.1849 | 204.7293 | +5.43% | 0.10% | 0.17% | Slower | [clang20-focus](../data/intel/clang20-focus.json) |
| banlist12/ja/comment/clean | 1.6477 | 1.6487 | +0.06% | 0.39% | 0.46% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/ja/comment/late | 1.8508 | 1.8492 | −0.09% | 0.24% | 0.21% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/ja/post/clean | 3.8932 | 3.7855 | −2.77% | 0.10% | 0.10% | Faster | [clang20-focus](../data/intel/clang20-focus.json) |
| banlist12/ja/post/early | 0.0367 | 0.0326 | −11.13% | 0.79% | 1.36% | Faster | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/ja/thread/clean | 301.3862 | 307.1255 | +1.90% | 0.23% | 0.29% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/ko/comment/clean | 1.1036 | 1.1041 | +0.05% | 0.13% | 0.11% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/ko/post/clean | 3.6491 | 3.5842 | −1.78% | 0.11% | 0.15% | Faster | [clang20-focus](../data/intel/clang20-focus.json) |
| banlist12/ko/post/early | 0.0275 | 0.0276 | +0.27% | 1.11% | 0.77% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/ko/thread/clean | 250.6608 | 259.8044 | +3.65% | 0.23% | 0.31% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/emoji/comment/clean | 0.3887 | 0.3900 | +0.33% | 1.28% | 1.02% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/emoji/post/clean | 2.9998 | 2.9069 | −3.10% | 0.09% | 0.10% | Faster | [clang20-focus](../data/intel/clang20-focus.json) |
| banlist12/emoji/post/early | 0.0275 | 0.0275 | −0.31% | 0.43% | 0.94% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| banlist12/emoji/thread/clean | 196.9602 | 203.6991 | +3.42% | 0.21% | 0.17% | Slower | [clang20-full233](../data/intel/clang20-full233.json) |
| explode/pipe2/short | 0.0865 | 0.0865 | +0.01% | 0.60% | 0.80% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| explode/pipe2/4k | 2.6594 | 2.6088 | −1.90% | 2.99% | 1.52% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| explode/pipe2/64k | 51.1262 | 50.9482 | −0.35% | 0.52% | 0.97% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| explode/colon2/short | 0.1011 | 0.0999 | −1.22% | 2.70% | 1.61% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| explode/colon2/4k | 2.6650 | 2.6492 | −0.59% | 3.46% | 1.01% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| explode/colon2/64k | 50.4398 | 50.6123 | +0.34% | 0.78% | 0.64% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| explode/crlf/short | 0.1140 | 0.1144 | +0.32% | 1.57% | 1.74% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| explode/crlf/4k | 2.5878 | 2.5502 | −1.45% | 2.28% | 2.20% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| explode/crlf/64k | 51.1302 | 51.0999 | −0.06% | 0.53% | 0.60% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| explode/comma/short | 0.0925 | 0.0940 | +1.55% | 1.53% | 5.96% | Noise | [clang20-quality-recheck](../data/intel/clang20-quality-recheck.json) |
| explode/comma/4k | 2.1478 | 2.1367 | −0.52% | 1.08% | 2.59% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| explode/comma/64k | 41.3550 | 41.3997 | +0.11% | 0.78% | 0.99% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| parse-records/4k | 9.9132 | 9.9712 | +0.59% | 0.80% | 1.84% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| parse-query/4k | 26.7763 | 26.9735 | +0.74% | 1.05% | 2.59% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| parse-http/small | 0.7861 | 0.7823 | −0.48% | 2.04% | 1.24% | Unclear | [clang20-focus](../data/intel/clang20-focus.json) |
| parse-http/body64k | 0.7904 | 0.8001 | +1.24% | 2.81% | 2.96% | Unclear | [clang20-focus](../data/intel/clang20-focus.json) |
| scan-template/4k | 4.1448 | 4.1311 | −0.33% | 0.95% | 0.64% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| render-template/4k | 6.3480 | 6.3211 | −0.42% | 0.55% | 1.36% | Unclear | [clang20-focus](../data/intel/clang20-focus.json) |
| log-contains/event/post/early | 0.0253 | 0.0224 | −11.34% | 0.59% | 1.76% | Faster | [clang20-full233](../data/intel/clang20-full233.json) |
| log-contains/level/post/early | 0.0272 | 0.0255 | −6.54% | 1.34% | 0.93% | Faster | [clang20-full233](../data/intel/clang20-full233.json) |
| log-contains/event/thread/clean | 17.4655 | 17.2431 | −1.27% | 0.09% | 0.07% | Faster | [clang20-focus](../data/intel/clang20-focus.json) |
| log-filter/thread/clean | 54.9737 | 55.0191 | +0.08% | 0.27% | 0.14% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |
| log-contains/event/thread/early | 0.0252 | 0.0224 | −11.16% | 0.47% | 1.31% | Faster | [clang20-full233](../data/intel/clang20-full233.json) |
| log-contains/level/thread/early | 0.0273 | 0.0255 | −6.69% | 1.75% | 1.44% | Faster | [clang20-full233](../data/intel/clang20-full233.json) |
| log-contains/event/thread/late | 17.4413 | 17.2184 | −1.28% | 0.09% | 0.07% | Faster | [clang20-focus](../data/intel/clang20-focus.json) |
| log-filter/thread/late | 55.0636 | 55.0474 | −0.03% | 0.26% | 0.46% | Unclear | [clang20-full233](../data/intel/clang20-full233.json) |

### Separate counters

| Case | Stock cycles¹ | Change cycles¹ | Δ cycles¹ | Stock instr. | Change instr. | Δ instr. |
|---|--:|--:|--:|--:|--:|--:|
| banlist12/en/comment/clean | 1857.68 | 1855.82 | −0.07% | 7165.20 | 7165.20 | −0.00% |
| banlist12/en/comment/early | 107.07 | 106.99 | −0.08% | 550.01 | 550.01 | +0.00% |
| banlist12/en/comment/late | 2018.57 | 2036.09 | +1.12% | 7661.21 | 7661.18 | −0.00% |
| banlist12/en/post/clean | 13290.88 | 12455.75 | −6.28% | 24149.22 | 21771.24 | −9.85% |
| banlist12/en/post/early | 106.25 | 104.91 | −0.47% | 541.01 | 541.01 | −0.00% |
| banlist12/en/post/late | 13529.11 | 12871.72 | −4.90% | 24550.25 | 22148.26 | −9.78% |
| banlist12/en/thread/clean | 837245.44 | 863666.88 | +3.16% | 1194834.97 | 1076727.68 | −9.88% |
| banlist12/en/thread/early | 106.08 | 105.17 | −1.15% | 541.01 | 541.01 | +0.00% |
| banlist12/en/thread/late | 902498.31 | 863247.37 | −4.34% | 1195306.10 | 1077170.31 | −9.88% |
| banlist12/ru/comment/clean | 11528.25 | 11555.91 | +0.14% | 23199.14 | 23199.36 | +0.00% |
| banlist12/ru/comment/early | 105.19 | 103.86 | −1.30% | 541.01 | 541.01 | −0.00% |
| banlist12/ru/comment/late | 12958.33 | 12953.26 | −0.13% | 25228.55 | 25228.43 | −0.00% |
| banlist12/ru/post/clean | 13835.92 | 13454.17 | −2.47% | 27410.27 | 24888.29 | −9.20% |
| banlist12/ru/post/early | 105.27 | 105.63 | +0.42% | 541.01 | 541.01 | −0.00% |
| banlist12/ru/post/late | 14409.43 | 14170.63 | −1.72% | 28555.44 | 25919.68 | −9.23% |
| banlist12/ru/thread/clean | 1167268.42 | 1172048.30 | +0.68% | 1367847.17 | 1298349.90 | −5.08% |
| banlist12/ru/thread/early | 104.95 | 104.74 | −0.20% | 541.01 | 541.01 | +0.00% |
| banlist12/ru/thread/late | 1168120.81 | 1174891.41 | +0.58% | 1368814.31 | 1299387.90 | −5.07% |
| banlist12/es/comment/clean | 2118.28 | 2103.09 | −0.72% | 7762.21 | 7762.23 | +0.00% |
| banlist12/es/post/clean | 12201.76 | 11913.54 | −2.36% | 24124.23 | 21816.24 | −9.57% |
| banlist12/es/post/early | 105.15 | 105.17 | +0.03% | 541.01 | 541.01 | +0.00% |
| banlist12/es/thread/clean | 852356.11 | 887274.56 | +4.40% | 1197755.67 | 1082092.79 | −9.66% |
| banlist12/ar/comment/clean | 9581.36 | 9577.63 | +0.03% | 19623.92 | 19623.99 | +0.00% |
| banlist12/ar/comment/late | 10594.55 | 10583.58 | −0.15% | 21732.16 | 21732.08 | −0.00% |
| banlist12/ar/post/clean | 18592.90 | 18201.37 | −2.14% | 34360.38 | 32360.39 | −5.82% |
| banlist12/ar/post/early | 105.66 | 105.16 | −0.47% | 541.01 | 541.01 | +0.00% |
| banlist12/ar/thread/clean | 1377509.72 | 1427322.27 | +3.44% | 1882641.65 | 1786066.20 | −5.13% |
| banlist12/hi/comment/clean | 13597.74 | 13650.15 | +0.42% | 27094.56 | 27094.53 | −0.00% |
| banlist12/hi/comment/late | 16187.47 | 16201.84 | +0.05% | 31063.87 | 31063.77 | −0.00% |
| banlist12/hi/post/clean | 11756.05 | 11489.72 | −2.24% | 24331.26 | 21735.28 | −10.67% |
| banlist12/hi/post/early | 148.99 | 141.43 | −5.08% | 727.02 | 680.02 | −6.46% |
| banlist12/hi/thread/clean | 971791.76 | 991843.08 | +2.30% | 1172760.92 | 1093682.62 | −6.74% |
| banlist12/hi/thread/late | 971278.06 | 1014542.19 | +3.99% | 1173995.20 | 1095038.42 | −6.73% |
| banlist12/zh/comment/clean | 2055.54 | 2069.26 | +0.31% | 7087.21 | 7087.20 | −0.00% |
| banlist12/zh/post/clean | 9522.77 | 9238.76 | −2.98% | 19345.19 | 17224.21 | −10.96% |
| banlist12/zh/post/early | 141.50 | 137.79 | −2.62% | 686.01 | 639.02 | −6.85% |
| banlist12/zh/thread/clean | 742380.62 | 779811.05 | +5.04% | 955628.66 | 851557.84 | −10.89% |
| banlist12/ja/comment/clean | 6240.55 | 6248.79 | −0.04% | 13656.64 | 13656.63 | −0.00% |
| banlist12/ja/comment/late | 7001.36 | 7006.35 | +0.06% | 15256.77 | 15256.72 | −0.00% |
| banlist12/ja/post/clean | 14788.85 | 14337.09 | −3.05% | 28503.30 | 26174.29 | −8.17% |
| banlist12/ja/post/early | 138.73 | 123.50 | −10.17% | 664.01 | 617.01 | −7.08% |
| banlist12/ja/thread/clean | 1142586.59 | 1139271.40 | −0.29% | 1511400.08 | 1395301.16 | −7.68% |
| banlist12/ko/comment/clean | 4183.46 | 4184.40 | +0.12% | 10090.38 | 10090.41 | +0.00% |
| banlist12/ko/post/clean | 14022.44 | 13781.60 | −1.66% | 26601.28 | 24563.27 | −7.66% |
| banlist12/ko/post/early | 105.02 | 105.66 | +0.71% | 541.01 | 541.01 | −0.00% |
| banlist12/ko/thread/clean | 955325.94 | 991497.21 | +3.49% | 1320475.09 | 1225955.91 | −7.16% |
| banlist12/emoji/comment/clean | 1486.89 | 1479.87 | −0.48% | 5834.13 | 5834.14 | +0.00% |
| banlist12/emoji/post/clean | 11403.75 | 11018.01 | −3.34% | 22224.24 | 20046.22 | −9.80% |
| banlist12/emoji/post/early | 105.28 | 105.11 | −0.04% | 541.01 | 541.01 | +0.00% |
| banlist12/emoji/thread/clean | 751070.50 | 772342.65 | +2.99% | 1082527.23 | 976931.11 | −9.75% |
| explode/pipe2/short | 329.05 | 327.38 | −0.11% | 1546.01 | 1546.01 | −0.00% |
| explode/pipe2/4k | 10296.11 | 9933.14 | −3.53% | 41511.16 | 41511.22 | +0.00% |
| explode/pipe2/64k | 192726.61 | 192968.07 | +0.28% | 664532.72 | 664535.15 | +0.00% |
| explode/colon2/short | 376.77 | 380.47 | +0.98% | 1762.01 | 1762.01 | +0.00% |
| explode/colon2/4k | 9825.92 | 9941.29 | +0.87% | 41438.22 | 41438.22 | −0.00% |
| explode/colon2/64k | 189331.14 | 190041.09 | +0.38% | 660743.37 | 660745.30 | +0.00% |
| explode/crlf/short | 432.31 | 432.18 | −0.03% | 1995.01 | 1995.01 | +0.00% |
| explode/crlf/4k | 9477.78 | 9497.84 | −0.31% | 40376.20 | 40376.22 | +0.00% |
| explode/crlf/64k | 199755.77 | 190993.26 | −4.39% | 662199.25 | 662197.38 | −0.00% |
| explode/comma/short | 318.81 | 321.63 | +0.89% | 1720.00 | 1720.00 | −0.00% |
| explode/comma/4k | 7519.21 | 7638.07 | +1.58% | 38391.21 | 38391.27 | +0.00% |
| explode/comma/64k | 156218.91 | 156034.94 | −0.14% | 569502.45 | 569502.37 | −0.00% |
| parse-records/4k | 36899.23 | 36783.73 | −1.09% | 150929.78 | 150929.80 | +0.00% |
| parse-query/4k | 98676.95 | 99910.22 | +0.76% | 425597.70 | 425597.34 | −0.00% |
| parse-http/small | 2933.98 | 2967.99 | +1.33% | 12911.01 | 12911.01 | −0.00% |
| parse-http/body64k | 2937.02 | 2962.24 | +0.95% | 12907.01 | 12907.01 | +0.00% |
| scan-template/4k | 15692.50 | 15736.12 | +0.54% | 67567.18 | 67567.32 | +0.00% |
| render-template/4k | 24703.89 | 23638.90 | −3.16% | 68044.43 | 59928.39 | −11.93% |
| log-contains/event/post/early | 95.68 | 86.99 | −8.76% | 431.00 | 376.00 | −12.76% |
| log-contains/level/post/early | 104.70 | 99.83 | −4.99% | 465.00 | 408.00 | −12.26% |
| log-contains/event/thread/clean | 66092.40 | 65427.08 | −1.22% | 128934.26 | 117631.32 | −8.77% |
| log-filter/thread/clean | 208853.40 | 207700.47 | −0.55% | 483489.45 | 483486.93 | −0.00% |
| log-contains/event/thread/early | 95.58 | 86.41 | −9.52% | 431.00 | 376.00 | −12.76% |
| log-contains/level/thread/early | 105.40 | 98.71 | −6.34% | 465.00 | 408.00 | −12.26% |
| log-contains/event/thread/late | 68207.25 | 66817.95 | −2.04% | 128767.31 | 117482.32 | −8.76% |
| log-filter/thread/late | 207826.93 | 210225.59 | −1.64% | 483239.99 | 483240.93 | +0.00% |
