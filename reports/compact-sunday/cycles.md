# Separate hardware-counter series

Intel is diagnostic only: its elapsed A/A failed. Every matrix includes same-row cycle A/A. These are separate measurements from the elapsed series; they do not establish exact simultaneous IPC.

## amd-cycles

<!-- bench-table amd-cycles.json --header --full --compact-header --base-name Stock --labels amd-cycles-labels.txt -->
Machine: AMD Ryzen 9 5950X 16-Core Processor, CPU 15, kernel 7.0.0-38-generic.
Group gcc15: A = compact-base-gcc15 (cf1b5771a76 GCC 15.2, profile docker), B = compact-head-gcc15 (8d7babbc364 GCC 15.2, profile docker).
Group clang21: A = compact-base-clang21 (cf1b5771a76 clang 21.1, profile docker), B = compact-head-clang21 (8d7babbc364 clang 21.1, profile docker).
5 alternating passes per case, user-space cycles per call (perf stat, minus the empty loop), A against A at the start and the end.
Machine: turbo boost is on: thermal and frequency drift between rounds (sudo <recorded-path>/bench tune on).
negative = fewer cycles (faster)

Absolute cycles/call: Stock with GCC 15.2.

| call | Stock cycles | GCC 15.2 | clang 21.1 | Δ instr. |
|---|--:|--:|--:|--:|
| banlist12/en/post/clean | 14,154 | −10% (−12 … −7) | −10% (−10 … −9) | −6% … −2% |
| banlist12/en/thread/clean | 812,699 | −7% (−8 … −7) layout? | −8% (−8 … −8) layout? | 0% |
| banlist12/ru/post/clean | 14,335 | −5% (−6 … −5) | −5% (−5 … −5) | −3% … −2% |
| banlist12/ru/thread/clean | 1,044,263 | −4% (−4 … −3) layout? | −7% (−7 … −7) | −2% … 0% |
| banlist12/es/post/clean | 13,543 | −9% (−9 … −9) | −10% (−10 … −10) | −6% … −2% |
| banlist12/es/thread/clean | 837,103 | −7% (−7 … −7) layout? | −7% (−7 … −7) layout? | 0% |
| banlist12/ar/post/clean | 18,770 | −5% (−5 … −5) | −6% (−7 … −5) | −4% … −1% |
| banlist12/ar/thread/clean | 1,235,468 | −4% (−4 … −4) layout? | −5% (−6 … −5) layout? | 0% |
| banlist12/hi/post/clean | 12,517 | −7% (−7 … −6) | −7% (−7 … −5) | −5% … −3% |
| banlist12/hi/thread/clean | 848,940 | −4% (−4 … −4) layout? | −8% (−8 … −8) | −2% … 0% |
| banlist12/zh/post/clean | 10,968 | −10% (−13 … −9) | −11% (−13 … −11) | −8% … −3% |
| banlist12/zh/thread/clean | 711,035 | −7% (−8 … −7) layout? | −8% (−8 … −8) layout? | 0% |
| banlist12/ja/post/clean | 15,629 | −9% (−9 … −8) | −9% (−10 … −8) | −5% … −2% |
| banlist12/ja/thread/clean | 1,041,406 | −5% (−6 … −5) layout? | −6% (−7 … −6) layout? | 0% |
| banlist12/ko/post/clean | 14,681 | −8% (−8 … −7) | −8% (−8 … −8) | −5% … −2% |
| banlist12/ko/thread/clean | 898,174 | −5% (−6 … −5) layout? | −6% (−7 … −6) layout? | 0% |
| banlist12/emoji/post/clean | 12,787 | −9% (−10 … −8) | −10% (−10 … −10) | −6% … −2% |
| banlist12/emoji/thread/clean | 729,687 | −7% (−8 … −7) layout? | −8% (−8 … −7) layout? | 0% |
| explode/pipe2/4k | 11,640 | 0% (−3 … +1) ~ | 0% (0 … +4) ~ | 0% |
| explode/colon2/4k | 11,787 | −1% (−2 … +1) ~ | 0% (−5 … +2) ~ | 0% |
| parse-http/body64k | 4,014 | +1% (−4 … +2) | −2% (−5 … +2) | 0% |
| render-template/4k | 33,070 | −16% (−17 … −14) | −14% (−15 … −14) | −18% … −6% |
| count-template/4k | 4,709 | −16% (−17 … −15) | −15% (−17 … −14) | −18% … −7% |
| boundary/9/absent | 18,092 | −8% (−10 … −8) | −11% (−12 … −11) layout? | −1% … 0% |
| boundary/32/early-text (original label: 31) | 155 | +3% (−3 … +3) | +1% (−4 … +2) | +1% … +3% |
| boundary/32/early | 188 | −1% (−2 … +1) | −1% (−2 … +3) | +1% … +2% |

Control: Stock against itself.

Absolute cycles/call: Stock with GCC 15.2.

| call | Stock cycles | A/A start | A/A end |
|---|--:|--:|--:|
| banlist12/en/post/clean | 14,119 | 0% (0 … +1) | 0% (0 … 0) |
| banlist12/en/thread/clean | 812,098 | 0% (0 … 0) | 0% (−1 … 0) |
| banlist12/ru/post/clean | 14,397 | 0% (−1 … +1) | 0% (−1 … 0) |
| banlist12/ru/thread/clean | 1,044,441 | 0% (0 … 0) | 0% (0 … 0) |
| banlist12/es/post/clean | 13,501 | 0% (0 … 0) | 0% (0 … +1) |
| banlist12/es/thread/clean | 835,464 | 0% (0 … 0) | 0% (−1 … 0) |
| banlist12/ar/post/clean | 18,701 | 0% (−1 … +1) | 0% (0 … 0) |
| banlist12/ar/thread/clean | 1,235,243 | 0% (0 … +1) | 0% (−1 … +1) |
| banlist12/hi/post/clean | 12,530 | 0% (−1 … 0) | 0% (0 … 0) |
| banlist12/hi/thread/clean | 850,233 | 0% (−1 … +1) | 0% (0 … 0) |
| banlist12/zh/post/clean | 10,973 | 0% (−3 … 0) | 0% (0 … 0) |
| banlist12/zh/thread/clean | 712,477 | 0% (−1 … +1) | 0% (−1 … 0) |
| banlist12/ja/post/clean | 15,581 | 0% (−1 … 0) | 0% (0 … 0) |
| banlist12/ja/thread/clean | 1,042,836 | 0% (0 … 0) | 0% (0 … 0) |
| banlist12/ko/post/clean | 14,701 | 0% (0 … +2) | 0% (−9 … 0) |
| banlist12/ko/thread/clean | 898,309 | 0% (0 … +1) | 0% (0 … 0) |
| banlist12/emoji/post/clean | 12,748 | 0% (0 … 0) | 0% (−1 … +1) |
| banlist12/emoji/thread/clean | 730,119 | 0% (0 … 0) | 0% (−1 … 0) |
| explode/pipe2/4k | 11,648 | +1% (−1 … +2) | 0% (−2 … +4) |
| explode/colon2/4k | 11,560 | +1% (−2 … +3) | 0% (−4 … 0) |
| parse-http/body64k | 4,005 | 0% (−1 … +1) | −1% (−1 … +1) |
| render-template/4k | 32,955 | 0% (−1 … +1) | 0% (−4 … 0) |
| count-template/4k | 4,720 | 0% (0 … 0) | 0% (−1 … +1) |
| boundary/9/absent | 18,019 | 0% (−1 … +2) | 0% (−1 … +2) |
| boundary/32/early-text (original label: 31) | 155 | 0% (−3 … +4) | 0% (−3 … +4) |
| boundary/32/early | 187 | 0% (−1 … +1) | 0% (−1 … +2) |

~: the change is not larger than the A/A control of the same row: not evidence of a difference.

layout?: in every pass the cycles changed in the same direction, by 3% or more in the median, the instructions by less than 0.5%: the work is the same, so look for the cause (code placement, branch prediction) with `bench why` before reporting the row.
<!-- /bench-table -->

## intel-cycles

<!-- bench-table intel-cycles.json --header --full --compact-header --base-name Stock --labels intel-cycles-labels.txt -->
Machine: 13th Gen Intel(R) Core(TM) i7-13700H, CPU 2, kernel 7.0.0-38-generic.
Group gcc13: A = compact-base-gcc13 (cf1b5771a76 GCC 13.3, profile docker), B = compact-head-gcc13 (8d7babbc364 GCC 13.3, profile docker).
Group gcc14: A = compact-base-gcc14 (cf1b5771a76 GCC 14.2, profile docker), B = compact-head-gcc14 (8d7babbc364 GCC 14.2, profile docker).
Group clang18: A = compact-base-clang18 (cf1b5771a76 clang 18.1, profile docker), B = compact-head-clang18 (8d7babbc364 clang 18.1, profile docker).
Group clang20: A = compact-base-clang20 (cf1b5771a76 clang 20.1, profile docker), B = compact-head-clang20 (8d7babbc364 clang 20.1, profile docker).
5 alternating passes per case, user-space cycles per call (perf stat, minus the empty loop), A against A at the start and the end.
Machine: CPU governor is 'powersave': frequency scaling adds noise (sudo <recorded-path>/bench tune on).
Machine: turbo boost is on: thermal and frequency drift between rounds (sudo <recorded-path>/bench tune on).
Machine: load average is 3.4: other programs are competing for the CPU.
negative = fewer cycles (faster)

Absolute cycles/call: Stock with GCC 13.3.

| call | Stock cycles | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | Δ instr. |
|---|--:|--:|--:|--:|--:|--:|
| banlist12/en/post/clean | 12,954 | −4% (−4 … −3) | −3% (−4 … −1) | −7% (−13 … −6) | +2% (−1 … +4) | −10% … −6% |
| banlist12/en/thread/clean | 830,380 | +1% (0 … +1) | 0% (−1 … +1) ~ | +2% (−2 … +3) | −3% (−4 … −3) | −10% … 0% |
| banlist12/ru/post/clean | 13,596 | −1% (−2 … +3) | −1% (−2 … 0) | −3% (−3 … −3) | −2% (−3 … −1) | −9% … −3% |
| banlist12/ru/thread/clean | 1,138,161 | +2% (−3 … +2) | −1% (−1 … +5) | 0% (−6 … +2) ~ | 0% (0 … +2) ~ | −10% … 0% |
| banlist12/es/post/clean | 12,549 | −4% (−5 … −3) | 0% (−2 … 0) ~ | −6% (−6 … −5) | −4% (−7 … −2) | −10% … −6% |
| banlist12/es/thread/clean | 845,860 | 0% (−2 … +7) ~ | 0% (−1 … +2) | +3% (+2 … +4) | −3% (−5 … −3) | −10% … 0% |
| banlist12/ar/post/clean | 18,565 | −2% (−3 … −1) | −1% (−2 … 0) | −3% (−3 … −2) | −2% (−2 … −1) | −6% … −4% |
| banlist12/ar/thread/clean | 1,379,783 | −2% (−3 … 0) | 0% (−2 … +2) | +2% (+2 … +3) | +2% (+1 … +6) | −5% … 0% |
| banlist12/hi/post/clean | 11,802 | −2% (−3 … −1) | −4% (−4 … −2) | −4% (−5 … −2) | −2% (−3 … 0) | −11% … −5% |
| banlist12/hi/thread/clean | 950,398 | 0% (0 … +3) ~ | −2% (−5 … −1) | +1% (+1 … +3) | −1% (−4 … +1) | −12% … 0% |
| banlist12/zh/post/clean | 9,870 | −5% (−6 … −2) | −6% (−8 … −4) | −8% (−18 … −8) | −2% (−6 … 0) | −11% … −8% |
| banlist12/zh/thread/clean | 728,877 | +1% (0 … +7) | 0% (−1 … 0) ~ | +4% (+4 … +5) | −3% (−3 … 0) | −11% … 0% |
| banlist12/ja/post/clean | 14,974 | −3% (−4 … −3) | −2% (−4 … −1) | −5% (−5 … −4) | 0% (−5 … +1) | −8% … −5% |
| banlist12/ja/thread/clean | 1,121,332 | +1% (0 … +1) | 0% (−1 … +1) ~ | +2% (0 … +2) | +3% (0 … +3) | −8% … 0% |
| banlist12/ko/post/clean | 14,346 | −3% (−4 … +1) | −2% (−4 … −2) | −4% (−5 … −3) | −2% (−2 … −1) | −8% … −5% |
| banlist12/ko/thread/clean | 946,343 | +1% (0 … +1) | −1% (−6 … 0) | +2% (+2 … +3) | −2% (−2 … 0) | −7% … 0% |
| banlist12/emoji/post/clean | 11,876 | −2% (−6 … −1) | −4% (−6 … −2) | −6% (−7 … −5) | −2% (−8 … −1) | −10% … −6% |
| banlist12/emoji/thread/clean | 754,712 | 0% (−1 … +2) | +1% (0 … +2) | +2% (−2 … +3) | −3% (−6 … −2) | −10% … 0% |
| explode/pipe2/4k | 9,093 | 0% (−20 … +1) ~ | −1% (−2 … +1) ~ | +1% (−6 … +3) ~ | 0% (−3 … +29) ~ | 0% |
| explode/colon2/4k | 8,885 | −2% (−4 … +4) | 0% (−1 … +4) ~ | +1% (−1 … +3) ~ | +1% (−2 … +3) ~ | 0% |
| parse-http/body64k | 3,066 | 0% (−2 … +1) ~ | +2% (0 … +4) | +1% (0 … +1) ~ | +1% (−2 … +3) ~ | 0% |
| render-template/4k | 27,576 | −10% (−11 … −10) | −14% (−14 … −12) | −1% (−4 … +1) | −4% (−10 … −1) | −18% … −12% |
| count-template/4k | 4,108 | −13% (−13 … −11) | −24% (−24 … −22) | −2% (−2 … −1) | −2% (−12 … −2) | −18% … −12% |
| boundary/9/absent | 18,315 | 0% (0 … +2) ~ | +1% (0 … +4) | 0% (−1 … 0) | 0% (−1 … 0) | −12% … −1% |
| boundary/32/early-text (original label: 31) | 155 | +18% (+17 … +19) | −13% (−16 … 0) | +34% (+31 … +36) layout? | +1% (0 … +2) | 0% … +2% |
| boundary/32/early | 154 | +21% (+20 … +21) layout? | +2% (+1 … +11) | +25% (+24 … +28) layout? | +2% (+1 … +3) | 0% … +1% |

Control: Stock against itself.

Absolute cycles/call: Stock with GCC 13.3.

| call | Stock cycles | A/A start | A/A end |
|---|--:|--:|--:|
| banlist12/en/post/clean | 12,939 | −1% (−9 … 0) | 0% (−1 … +1) |
| banlist12/en/thread/clean | 834,131 | 0% (0 … +1) | +1% (0 … +1) |
| banlist12/ru/post/clean | 13,647 | 0% (−1 … 0) | +1% (−1 … +3) |
| banlist12/ru/thread/clean | 1,134,890 | 0% (0 … +1) | +1% (−2 … +2) |
| banlist12/es/post/clean | 12,556 | 0% (−2 … +1) | 0% (−1 … +1) |
| banlist12/es/thread/clean | 847,345 | 0% (0 … +1) | 0% (−3 … +6) |
| banlist12/ar/post/clean | 18,578 | 0% (−1 … 0) | +1% (0 … +1) |
| banlist12/ar/thread/clean | 1,355,570 | 0% (0 … +1) | 0% (0 … +1) |
| banlist12/hi/post/clean | 11,843 | 0% (−1 … +1) | 0% (−3 … +1) |
| banlist12/hi/thread/clean | 945,438 | 0% (−2 … +1) | 0% (−2 … +1) |
| banlist12/zh/post/clean | 9,900 | −1% (−4 … +2) | 0% (−1 … 0) |
| banlist12/zh/thread/clean | 728,919 | 0% (0 … 0) | 0% (−1 … +1) |
| banlist12/ja/post/clean | 14,976 | 0% (−1 … +1) | 0% (−1 … 0) |
| banlist12/ja/thread/clean | 1,118,894 | 0% (−2 … +2) | 0% (0 … +1) |
| banlist12/ko/post/clean | 14,423 | −1% (−3 … +1) | 0% (−1 … 0) |
| banlist12/ko/thread/clean | 946,147 | 0% (0 … 0) | 0% (−1 … +1) |
| banlist12/emoji/post/clean | 11,901 | 0% (−1 … 0) | 0% (0 … +5) |
| banlist12/emoji/thread/clean | 749,656 | 0% (−1 … +1) | 0% (−7 … +1) |
| explode/pipe2/4k | 8,904 | +4% (0 … +6) | +3% (0 … +36) |
| explode/colon2/4k | 8,869 | +1% (0 … +7) | −2% (−29 … +4) |
| parse-http/body64k | 3,067 | +1% (0 … +2) | 0% (−5 … 0) |
| render-template/4k | 27,493 | 0% (−3 … 0) | 0% (−1 … +1) |
| count-template/4k | 4,089 | 0% (0 … +1) | +1% (−1 … +16) |
| boundary/9/absent | 18,345 | 0% (0 … +1) | 0% (−1 … +1) |
| boundary/32/early-text (original label: 31) | 154 | −1% (−4 … +4) | 0% (−18 … +31) |
| boundary/32/early | 154 | 0% (−3 … +2) | −1% (−37 … +1) |

~: the change is not larger than the A/A control of the same row: not evidence of a difference.

layout?: in every pass the cycles changed in the same direction, by 3% or more in the median, the instructions by less than 0.5%: the work is the same, so look for the cause (code placement, branch prediction) with `bench why` before reporting the row.
<!-- /bench-table -->

## early31-cycles

<!-- bench-table early31-cycles.json --header --full --compact-header --base-name Stock --labels early31-cycles-labels.txt -->
Machine: AMD Ryzen 9 5950X 16-Core Processor, CPU 15, kernel 7.0.0-38-generic.
Group gcc15: A = compact-base-gcc15 (cf1b5771a76 GCC 15.2, profile docker), B = compact-head-gcc15 (8d7babbc364 GCC 15.2, profile docker).
Group clang21: A = compact-base-clang21 (cf1b5771a76 clang 21.1, profile docker), B = compact-head-clang21 (8d7babbc364 clang 21.1, profile docker).
5 alternating passes per case, user-space cycles per call (perf stat, minus the empty loop), A against A at the start and the end.
Machine: turbo boost is on: thermal and frequency drift between rounds (sudo <recorded-path>/bench tune on).
negative = fewer cycles (faster)

Absolute cycles/call: Stock with GCC 15.2.

| call | Stock cycles | GCC 15.2 | clang 21.1 | Δ instr. |
|---|--:|--:|--:|--:|
| boundary/31/early | 152 | −19% (−21 … +3) | −14% (−20 … −11) | −19% … −7% |

Control: Stock against itself.

Absolute cycles/call: Stock with GCC 15.2.

| call | Stock cycles | A/A start | A/A end |
|---|--:|--:|--:|
| boundary/31/early | 152 | 0% (−1 … +3) | −1% (−2 … +6) |
<!-- /bench-table -->

