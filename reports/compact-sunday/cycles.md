# CPU cycles and instructions

All changes are relative to master. A call is one complete listed operation; moderation includes all 12 searches. Each matrix includes master-against-master controls for the same cases. Counters were collected separately from elapsed time. Intel counters are diagnostic only because its elapsed A/A failed.

## amd-cycles

<!-- bench-table amd-cycles.json --header --full --compact-header --base-name master --labels amd-cycles-labels.txt -->
Machine: AMD Ryzen 9 5950X 16-Core Processor, CPU 15, kernel 7.0.0-38-generic.
Group gcc15: A = compact-base-gcc15 (cf1b5771a76 GCC 15.2, profile docker), B = compact-head-gcc15 (8d7babbc364 GCC 15.2, profile docker).
Group clang21: A = compact-base-clang21 (cf1b5771a76 clang 21.1, profile docker), B = compact-head-clang21 (8d7babbc364 clang 21.1, profile docker).
5 alternating passes per case, user-space cycles per call (perf stat, minus the empty loop), A against A at the start and the end.
Machine: turbo boost is on: thermal and frequency drift between rounds (sudo <recorded-path>/bench tune on).
negative = fewer cycles (faster)

Absolute cycles/call: master with GCC 15.2.

| call | master cycles | GCC 15.2 | clang 21.1 | Δ instr. |
|---|--:|--:|--:|--:|
| English moderation post | 14,154 | −10% (−12 … −7) | −10% (−10 … −9) | −6% … −2% |
| English moderation thread | 812,699 | −7% (−8 … −7) layout? | −8% (−8 … −8) layout? | 0% |
| Russian moderation post | 14,335 | −5% (−6 … −5) | −5% (−5 … −5) | −3% … −2% |
| Russian moderation thread | 1,044,263 | −4% (−4 … −3) layout? | −7% (−7 … −7) | −2% … 0% |
| Spanish moderation post | 13,543 | −9% (−9 … −9) | −10% (−10 … −10) | −6% … −2% |
| Spanish moderation thread | 837,103 | −7% (−7 … −7) layout? | −7% (−7 … −7) layout? | 0% |
| Arabic moderation post | 18,770 | −5% (−5 … −5) | −6% (−7 … −5) | −4% … −1% |
| Arabic moderation thread | 1,235,468 | −4% (−4 … −4) layout? | −5% (−6 … −5) layout? | 0% |
| Hindi moderation post | 12,517 | −7% (−7 … −6) | −7% (−7 … −5) | −5% … −3% |
| Hindi moderation thread | 848,940 | −4% (−4 … −4) layout? | −8% (−8 … −8) | −2% … 0% |
| Chinese moderation post | 10,968 | −10% (−13 … −9) | −11% (−13 … −11) | −8% … −3% |
| Chinese moderation thread | 711,035 | −7% (−8 … −7) layout? | −8% (−8 … −8) layout? | 0% |
| Japanese moderation post | 15,629 | −9% (−9 … −8) | −9% (−10 … −8) | −5% … −2% |
| Japanese moderation thread | 1,041,406 | −5% (−6 … −5) layout? | −6% (−7 … −6) layout? | 0% |
| Korean moderation post | 14,681 | −8% (−8 … −7) | −8% (−8 … −8) | −5% … −2% |
| Korean moderation thread | 898,174 | −5% (−6 … −5) layout? | −6% (−7 … −6) layout? | 0% |
| Mixed emoji moderation post | 12,787 | −9% (−10 … −8) | −10% (−10 … −10) | −6% … −2% |
| Mixed emoji moderation thread | 729,687 | −7% (−8 … −7) layout? | −8% (−8 … −7) layout? | 0% |
| Split fields on two pipes | 11,640 | 0% (−3 … +1) ~ | 0% (0 … +4) ~ | 0% |
| Split fields on `::` | 11,787 | −1% (−2 … +1) ~ | 0% (−5 … +2) ~ | 0% |
| Parse HTTP headers | 4,014 | +1% (−4 … +2) | −2% (−5 … +2) | 0% |
| Replace template placeholders | 33,070 | −16% (−17 … −14) | −14% (−15 … −14) | −18% … −6% |
| Count `{{order.id}}` slots | 4,709 | −16% (−17 … −15) | −15% (−17 … −14) | −18% … −7% |
| 9-byte search (no match) | 18,092 | −8% (−10 … −8) | −11% (−12 … −11) layout? | −1% … 0% |
| 32-byte early match (text) | 155 | +3% (−3 … +3) | +1% (−4 … +2) | +1% … +3% |
| 32-byte early match (repeated a) | 188 | −1% (−2 … +1) | −1% (−2 … +3) | +1% … +2% |

Control: master against itself.

Absolute cycles/call: master with GCC 15.2.

| call | master cycles | A/A start | A/A end |
|---|--:|--:|--:|
| English moderation post | 14,119 | 0% (0 … +1) | 0% (0 … 0) |
| English moderation thread | 812,098 | 0% (0 … 0) | 0% (−1 … 0) |
| Russian moderation post | 14,397 | 0% (−1 … +1) | 0% (−1 … 0) |
| Russian moderation thread | 1,044,441 | 0% (0 … 0) | 0% (0 … 0) |
| Spanish moderation post | 13,501 | 0% (0 … 0) | 0% (0 … +1) |
| Spanish moderation thread | 835,464 | 0% (0 … 0) | 0% (−1 … 0) |
| Arabic moderation post | 18,701 | 0% (−1 … +1) | 0% (0 … 0) |
| Arabic moderation thread | 1,235,243 | 0% (0 … +1) | 0% (−1 … +1) |
| Hindi moderation post | 12,530 | 0% (−1 … 0) | 0% (0 … 0) |
| Hindi moderation thread | 850,233 | 0% (−1 … +1) | 0% (0 … 0) |
| Chinese moderation post | 10,973 | 0% (−3 … 0) | 0% (0 … 0) |
| Chinese moderation thread | 712,477 | 0% (−1 … +1) | 0% (−1 … 0) |
| Japanese moderation post | 15,581 | 0% (−1 … 0) | 0% (0 … 0) |
| Japanese moderation thread | 1,042,836 | 0% (0 … 0) | 0% (0 … 0) |
| Korean moderation post | 14,701 | 0% (0 … +2) | 0% (−9 … 0) |
| Korean moderation thread | 898,309 | 0% (0 … +1) | 0% (0 … 0) |
| Mixed emoji moderation post | 12,748 | 0% (0 … 0) | 0% (−1 … +1) |
| Mixed emoji moderation thread | 730,119 | 0% (0 … 0) | 0% (−1 … 0) |
| Split fields on two pipes | 11,648 | +1% (−1 … +2) | 0% (−2 … +4) |
| Split fields on `::` | 11,560 | +1% (−2 … +3) | 0% (−4 … 0) |
| Parse HTTP headers | 4,005 | 0% (−1 … +1) | −1% (−1 … +1) |
| Replace template placeholders | 32,955 | 0% (−1 … +1) | 0% (−4 … 0) |
| Count `{{order.id}}` slots | 4,720 | 0% (0 … 0) | 0% (−1 … +1) |
| 9-byte search (no match) | 18,019 | 0% (−1 … +2) | 0% (−1 … +2) |
| 32-byte early match (text) | 155 | 0% (−3 … +4) | 0% (−3 … +4) |
| 32-byte early match (repeated a) | 187 | 0% (−1 … +1) | 0% (−1 … +2) |

~: the change is not larger than the A/A control of the same row: not evidence of a difference.

layout?: in every pass the cycles changed in the same direction, by 3% or more in the median, the instructions by less than 0.5%: the work is the same, so look for the cause (code placement, branch prediction) with `bench why` before reporting the row.
<!-- /bench-table -->

## intel-cycles

<!-- bench-table intel-cycles.json --header --full --compact-header --base-name master --labels intel-cycles-labels.txt -->
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

Absolute cycles/call: master with GCC 13.3.

| call | master cycles | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | Δ instr. |
|---|--:|--:|--:|--:|--:|--:|
| English moderation post | 12,954 | −4% (−4 … −3) | −3% (−4 … −1) | −7% (−13 … −6) | +2% (−1 … +4) | −10% … −6% |
| English moderation thread | 830,380 | +1% (0 … +1) | 0% (−1 … +1) ~ | +2% (−2 … +3) | −3% (−4 … −3) | −10% … 0% |
| Russian moderation post | 13,596 | −1% (−2 … +3) | −1% (−2 … 0) | −3% (−3 … −3) | −2% (−3 … −1) | −9% … −3% |
| Russian moderation thread | 1,138,161 | +2% (−3 … +2) | −1% (−1 … +5) | 0% (−6 … +2) ~ | 0% (0 … +2) ~ | −10% … 0% |
| Spanish moderation post | 12,549 | −4% (−5 … −3) | 0% (−2 … 0) ~ | −6% (−6 … −5) | −4% (−7 … −2) | −10% … −6% |
| Spanish moderation thread | 845,860 | 0% (−2 … +7) ~ | 0% (−1 … +2) | +3% (+2 … +4) | −3% (−5 … −3) | −10% … 0% |
| Arabic moderation post | 18,565 | −2% (−3 … −1) | −1% (−2 … 0) | −3% (−3 … −2) | −2% (−2 … −1) | −6% … −4% |
| Arabic moderation thread | 1,379,783 | −2% (−3 … 0) | 0% (−2 … +2) | +2% (+2 … +3) | +2% (+1 … +6) | −5% … 0% |
| Hindi moderation post | 11,802 | −2% (−3 … −1) | −4% (−4 … −2) | −4% (−5 … −2) | −2% (−3 … 0) | −11% … −5% |
| Hindi moderation thread | 950,398 | 0% (0 … +3) ~ | −2% (−5 … −1) | +1% (+1 … +3) | −1% (−4 … +1) | −12% … 0% |
| Chinese moderation post | 9,870 | −5% (−6 … −2) | −6% (−8 … −4) | −8% (−18 … −8) | −2% (−6 … 0) | −11% … −8% |
| Chinese moderation thread | 728,877 | +1% (0 … +7) | 0% (−1 … 0) ~ | +4% (+4 … +5) | −3% (−3 … 0) | −11% … 0% |
| Japanese moderation post | 14,974 | −3% (−4 … −3) | −2% (−4 … −1) | −5% (−5 … −4) | 0% (−5 … +1) | −8% … −5% |
| Japanese moderation thread | 1,121,332 | +1% (0 … +1) | 0% (−1 … +1) ~ | +2% (0 … +2) | +3% (0 … +3) | −8% … 0% |
| Korean moderation post | 14,346 | −3% (−4 … +1) | −2% (−4 … −2) | −4% (−5 … −3) | −2% (−2 … −1) | −8% … −5% |
| Korean moderation thread | 946,343 | +1% (0 … +1) | −1% (−6 … 0) | +2% (+2 … +3) | −2% (−2 … 0) | −7% … 0% |
| Mixed emoji moderation post | 11,876 | −2% (−6 … −1) | −4% (−6 … −2) | −6% (−7 … −5) | −2% (−8 … −1) | −10% … −6% |
| Mixed emoji moderation thread | 754,712 | 0% (−1 … +2) | +1% (0 … +2) | +2% (−2 … +3) | −3% (−6 … −2) | −10% … 0% |
| Split fields on two pipes | 9,093 | 0% (−20 … +1) ~ | −1% (−2 … +1) ~ | +1% (−6 … +3) ~ | 0% (−3 … +29) ~ | 0% |
| Split fields on `::` | 8,885 | −2% (−4 … +4) | 0% (−1 … +4) ~ | +1% (−1 … +3) ~ | +1% (−2 … +3) ~ | 0% |
| Parse HTTP headers | 3,066 | 0% (−2 … +1) ~ | +2% (0 … +4) | +1% (0 … +1) ~ | +1% (−2 … +3) ~ | 0% |
| Replace template placeholders | 27,576 | −10% (−11 … −10) | −14% (−14 … −12) | −1% (−4 … +1) | −4% (−10 … −1) | −18% … −12% |
| Count `{{order.id}}` slots | 4,108 | −13% (−13 … −11) | −24% (−24 … −22) | −2% (−2 … −1) | −2% (−12 … −2) | −18% … −12% |
| 9-byte search (no match) | 18,315 | 0% (0 … +2) ~ | +1% (0 … +4) | 0% (−1 … 0) | 0% (−1 … 0) | −12% … −1% |
| 32-byte early match (text) | 155 | +18% (+17 … +19) | −13% (−16 … 0) | +34% (+31 … +36) layout? | +1% (0 … +2) | 0% … +2% |
| 32-byte early match (repeated a) | 154 | +21% (+20 … +21) layout? | +2% (+1 … +11) | +25% (+24 … +28) layout? | +2% (+1 … +3) | 0% … +1% |

Control: master against itself.

Absolute cycles/call: master with GCC 13.3.

| call | master cycles | A/A start | A/A end |
|---|--:|--:|--:|
| English moderation post | 12,939 | −1% (−9 … 0) | 0% (−1 … +1) |
| English moderation thread | 834,131 | 0% (0 … +1) | +1% (0 … +1) |
| Russian moderation post | 13,647 | 0% (−1 … 0) | +1% (−1 … +3) |
| Russian moderation thread | 1,134,890 | 0% (0 … +1) | +1% (−2 … +2) |
| Spanish moderation post | 12,556 | 0% (−2 … +1) | 0% (−1 … +1) |
| Spanish moderation thread | 847,345 | 0% (0 … +1) | 0% (−3 … +6) |
| Arabic moderation post | 18,578 | 0% (−1 … 0) | +1% (0 … +1) |
| Arabic moderation thread | 1,355,570 | 0% (0 … +1) | 0% (0 … +1) |
| Hindi moderation post | 11,843 | 0% (−1 … +1) | 0% (−3 … +1) |
| Hindi moderation thread | 945,438 | 0% (−2 … +1) | 0% (−2 … +1) |
| Chinese moderation post | 9,900 | −1% (−4 … +2) | 0% (−1 … 0) |
| Chinese moderation thread | 728,919 | 0% (0 … 0) | 0% (−1 … +1) |
| Japanese moderation post | 14,976 | 0% (−1 … +1) | 0% (−1 … 0) |
| Japanese moderation thread | 1,118,894 | 0% (−2 … +2) | 0% (0 … +1) |
| Korean moderation post | 14,423 | −1% (−3 … +1) | 0% (−1 … 0) |
| Korean moderation thread | 946,147 | 0% (0 … 0) | 0% (−1 … +1) |
| Mixed emoji moderation post | 11,901 | 0% (−1 … 0) | 0% (0 … +5) |
| Mixed emoji moderation thread | 749,656 | 0% (−1 … +1) | 0% (−7 … +1) |
| Split fields on two pipes | 8,904 | +4% (0 … +6) | +3% (0 … +36) |
| Split fields on `::` | 8,869 | +1% (0 … +7) | −2% (−29 … +4) |
| Parse HTTP headers | 3,067 | +1% (0 … +2) | 0% (−5 … 0) |
| Replace template placeholders | 27,493 | 0% (−3 … 0) | 0% (−1 … +1) |
| Count `{{order.id}}` slots | 4,089 | 0% (0 … +1) | +1% (−1 … +16) |
| 9-byte search (no match) | 18,345 | 0% (0 … +1) | 0% (−1 … +1) |
| 32-byte early match (text) | 154 | −1% (−4 … +4) | 0% (−18 … +31) |
| 32-byte early match (repeated a) | 154 | 0% (−3 … +2) | −1% (−37 … +1) |

~: the change is not larger than the A/A control of the same row: not evidence of a difference.

layout?: in every pass the cycles changed in the same direction, by 3% or more in the median, the instructions by less than 0.5%: the work is the same, so look for the cause (code placement, branch prediction) with `bench why` before reporting the row.
<!-- /bench-table -->

## early31-cycles

<!-- bench-table early31-cycles.json --header --full --compact-header --base-name master --labels early31-cycles-labels.txt -->
Machine: AMD Ryzen 9 5950X 16-Core Processor, CPU 15, kernel 7.0.0-38-generic.
Group gcc15: A = compact-base-gcc15 (cf1b5771a76 GCC 15.2, profile docker), B = compact-head-gcc15 (8d7babbc364 GCC 15.2, profile docker).
Group clang21: A = compact-base-clang21 (cf1b5771a76 clang 21.1, profile docker), B = compact-head-clang21 (8d7babbc364 clang 21.1, profile docker).
5 alternating passes per case, user-space cycles per call (perf stat, minus the empty loop), A against A at the start and the end.
Machine: turbo boost is on: thermal and frequency drift between rounds (sudo <recorded-path>/bench tune on).
negative = fewer cycles (faster)

Absolute cycles/call: master with GCC 15.2.

| call | master cycles | GCC 15.2 | clang 21.1 | Δ instr. |
|---|--:|--:|--:|--:|
| 31-byte early match | 152 | −19% (−21 … +3) | −14% (−20 … −11) | −19% … −7% |

Control: master against itself.

Absolute cycles/call: master with GCC 15.2.

| call | master cycles | A/A start | A/A end |
|---|--:|--:|--:|
| 31-byte early match | 152 | 0% (−1 … +3) | −1% (−2 … +6) |
<!-- /bench-table -->

