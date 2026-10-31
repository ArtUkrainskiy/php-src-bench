# Search-control counters

All inputs are 4096 bytes. Negative means fewer cycles relative to master.
Each case has five paired passes and same-case A/A controls.

<!-- bench-table search-counters.json --header --full --compact-header --base-name master --labels search-labels.txt -->
Machine: AMD Ryzen 9 5950X 16-Core Processor, CPU 15, kernel 7.0.0-38-generic.
Group clang21: A = compact-base-clang21 (cf1b5771a76 clang 21.1, profile docker), B = compact-head-clang21 (8d7babbc364 clang 21.1, profile docker).
Group gcc15: A = compact-base-gcc15 (cf1b5771a76 GCC 15.2, profile docker), B = compact-head-gcc15 (8d7babbc364 GCC 15.2, profile docker).
5 alternating passes per case, user-space cycles per call (perf stat, minus the empty loop), A against A at the start and the end.
Machine: turbo boost is on: thermal and frequency drift between rounds (sudo <recorded-path>/bench tune on).
negative = fewer cycles (faster)

Absolute cycles/call: master with clang 21.1.

| call | master cycles | clang 21.1 | GCC 15.2 | Δ instr. |
|---|--:|--:|--:|--:|
| strpos, no match, 8 B | 4,861 | −1% (−2 … +1) ~ | 0% (0 … 0) ~ | 0% |
| strpos, match at 0, 8 B | 44 | +2% (0 … +3) | 0% (−2 … +2) ~ | 0% |
| strpos, match at end, 8 B | 4,841 | 0% (0 … 0) ~ | 0% (0 … 0) ~ | 0% |
| strpos, repeated prefix, 8 B | 73,356 | 0% (0 … +1) | 0% (0 … 0) | 0% |
| strpos, no match, 9 B | 5,103 | −11% (−11 … −10) | −11% (−11 … −10) | −2% … −1% |
| strpos, match at 0, 9 B | 94 | −41% (−43 … −34) | −32% (−33 … −30) | −32% … −13% |
| strpos, match at end, 9 B | 5,121 | −11% (−11 … −10) | −9% (−10 … −9) | −2% … −1% |
| strpos, repeated prefix, 9 B | 35,631 | −4% (−5 … −4) layout? | −2% (−7 … +8) | 0% |
| strpos, no match, 16 B | 2,834 | −11% (−11 … −11) | −9% (−9 … −9) | −3% … −1% |
| strpos, match at 0, 16 B | 99 | −26% (−30 … −24) | −28% (−29 … −28) | −26% … −11% |
| strpos, match at end, 16 B | 2,858 | −10% (−11 … −10) | −9% (−10 … −9) | −3% … −1% |
| strpos, repeated prefix, 16 B | 49,321 | −3% (−12 … +5) | 0% (−1 … +3) ~ | 0% |
| strpos, no match, 24 B | 2,344 | −10% (−10 … −10) | −10% (−10 … −9) | −4% … −1% |
| strpos, match at 0, 24 B | 117 | −21% (−31 … −20) | −24% (−39 … −14) | −22% … −9% |
| strpos, match at end, 24 B | 2,377 | −10% (−10 … −9) | −10% (−10 … −9) | −4% … −1% |
| strpos, repeated prefix, 24 B | 66,064 | −3% (−6 … +1) | +2% (0 … +4) ~ | 0% |
| strpos, no match, 31 B | 2,339 | −10% (−10 … −9) | −10% (−24 … −10) | −4% … −1% |
| strpos, match at 0, 31 B | 135 | −23% (−27 … −18) | −22% (−22 … −12) | −19% … −8% |
| strpos, match at end, 31 B | 2,392 | −11% (−27 … −10) | −10% (−10 … −10) | −4% … −1% |
| strpos, repeated prefix, 31 B | 82,723 | −3% (−11 … +4) ~ | +1% (−2 … +5) ~ | 0% |
| strpos, no match, 32 B | 2,374 | +2% (+1 … +2) | −1% (−1 … −1) | −6% … 0% |
| strpos, match at 0, 32 B | 137 | +1% (−5 … +1) | 0% (−1 … +4) ~ | +1% … +3% |
| strpos, match at end, 32 B | 2,424 | +2% (+1 … +2) | −1% (−2 … 0) | −5% … 0% |
| strpos, repeated prefix, 32 B | 83,704 | −3% (−5 … −2) | −1% (−2 … −1) | 0% |
| strpos, no match, 33 B | 1,776 | +1% (0 … +1) | −1% (−1 … −1) | −5% … 0% |
| strpos, match at 0, 33 B | 139 | +1% (0 … +2) | +10% (+1 … +11) | +1% … +3% |
| strpos, match at end, 33 B | 1,846 | 0% (0 … +1) ~ | 0% (−1 … +1) | −5% … 0% |
| strpos, repeated prefix, 33 B | 82,587 | +3% (−22 … +7) ~ | +6% (+5 … +11) ~ layout? | 0% |
| strpos, no match, 48 B | 3,758 | 0% (0 … +1) | 0% (−1 … 0) | −6% … 0% |
| strpos, match at 0, 48 B | 167 | 0% (0 … +2) ~ | +5% (+2 … +14) | +1% … +3% |
| strpos, match at end, 48 B | 3,833 | +1% (0 … +1) | −1% (−12 … −1) | −6% … 0% |
| strpos, repeated prefix, 48 B | 113,225 | +1% (−1 … +34) ~ | −2% (−2 … −1) | 0% |
| strpos, no match, 64 B | 1,766 | +1% (+1 … +2) | −1% (−1 … −1) | −5% … 0% |
| strpos, match at 0, 64 B | 197 | +2% (+1 … +2) | 0% (−6 … +8) ~ | 0% … +3% |
| strpos, match at end, 64 B | 1,906 | +1% (0 … +1) | 0% (−1 … 0) | −4% … 0% |
| strpos, repeated prefix, 64 B | 190,579 | −23% (−24 … −18) layout? | +31% (+31 … +32) layout? | 0% |
| strpos, no match, 128 B | 806 | +1% (0 … +2) ~ | +1% (0 … +2) | −1% … 0% |
| strpos, match at 0, 128 B | 333 | 0% (0 … +2) ~ | 0% (0 … 0) ~ | 0% … +3% |
| strpos, match at end, 128 B | 1,095 | −3% (−9 … +1) | −1% (−4 … +2) | −1% … 0% |
| strpos, repeated prefix, 128 B | 311,746 | +1% (0 … +1) | +3% (+2 … +4) | 0% |
| strpos, no match, 254 B | 675 | +1% (0 … +2) ~ | −1% (−1 … 0) ~ | 0% … +2% |
| strpos, match at 0, 254 B | 574 | +2% (−22 … +5) | 0% (0 … 0) ~ | 0% … +3% |
| strpos, match at end, 254 B | 990 | 0% (−1 … +2) ~ | −4% (−6 … −3) layout? | 0% … +1% |
| strpos, repeated prefix, 254 B | 545,621 | 0% (−3 … +3) ~ | +1% (+1 … +2) | 0% |
| strpos, no match, 255 B | 695 | +2% (0 … +3) | 0% (0 … +1) ~ | 0% … +2% |
| strpos, match at 0, 255 B | 565 | +4% (+2 … +6) | 0% (0 … 0) | 0% … +3% |
| strpos, match at end, 255 B | 1,133 | 0% (−2 … +2) ~ | −4% (−5 … −1) layout? | 0% … +1% |
| strpos, repeated prefix, 255 B | 548,358 | +1% (−1 … +29) | +1% (+1 … +3) | 0% |
| strpos, no match, 256 B | 1,139 | 0% (−3 … +1) ~ | −1% (−1 … +5) | 0% |
| strpos, match at 0, 256 B | 593 | −1% (−1 … +1) ~ | 0% (0 … 0) ~ | 0% … +3% |
| strpos, match at end, 256 B | 1,476 | 0% (−24 … +3) ~ | −2% (−5 … −1) | 0% |
| strpos, repeated prefix, 256 B | 550,107 | +1% (0 … +5) | +1% (0 … +1) | 0% |
| substr_count, repeated matches, 9 B | 7,234 | −24% (−31 … −21) | −27% (−28 … −26) | −32% … −13% |
| str_replace, repeated matches, 9 B | 15,749 | −22% (−31 … −18) | −26% (−28 … −21) | −30% … −11% |
| substr_count, repeated matches, 16 B | 6,609 | −17% (−19 … −16) | −26% (−27 … −25) | −28% … −12% |
| str_replace, repeated matches, 16 B | 13,824 | −17% (−19 … −14) | −21% (−25 … −21) | −26% … −11% |
| substr_count, repeated matches, 31 B | 6,012 | −13% (−26 … −12) | −10% (−10 … −4) | −21% … −8% |
| str_replace, repeated matches, 31 B | 12,773 | −6% (−14 … −5) | −14% (−14 … −6) | −20% … −8% |

Control: master against itself.

Absolute cycles/call: master with clang 21.1.

| call | master cycles | A/A start | A/A end |
|---|--:|--:|--:|
| strpos, no match, 8 B | 4,832 | +1% (0 … +2) | 0% (0 … +2) |
| strpos, match at 0, 8 B | 44 | −1% (−1 … 0) | 0% (−1 … +2) |
| strpos, match at end, 8 B | 4,839 | 0% (0 … +1) | 0% (0 … +2) |
| strpos, repeated prefix, 8 B | 73,414 | 0% (0 … 0) | 0% (−1 … +1) |
| strpos, no match, 9 B | 5,105 | 0% (0 … 0) | 0% (0 … 0) |
| strpos, match at 0, 9 B | 85 | 0% (−6 … +12) | 0% (0 … +2) |
| strpos, match at end, 9 B | 5,123 | 0% (0 … 0) | 0% (0 … 0) |
| strpos, repeated prefix, 9 B | 35,646 | 0% (0 … +1) | 0% (0 … 0) |
| strpos, no match, 16 B | 2,836 | 0% (−1 … +1) | 0% (0 … 0) |
| strpos, match at 0, 16 B | 100 | 0% (−1 … 0) | 0% (−3 … +7) |
| strpos, match at end, 16 B | 2,857 | 0% (0 … 0) | 0% (0 … 0) |
| strpos, repeated prefix, 16 B | 49,199 | 0% (−1 … +1) | 0% (−5 … +1) |
| strpos, no match, 24 B | 2,355 | 0% (−1 … 0) | 0% (−1 … +3) |
| strpos, match at 0, 24 B | 117 | 0% (−1 … +2) | 0% (0 … 0) |
| strpos, match at end, 24 B | 2,377 | 0% (0 … 0) | 0% (−1 … +1) |
| strpos, repeated prefix, 24 B | 67,493 | −3% (−15 … +2) | +1% (−11 … +16) |
| strpos, no match, 31 B | 2,337 | 0% (0 … +1) | 0% (−1 … 0) |
| strpos, match at 0, 31 B | 135 | 0% (−6 … 0) | 0% (−1 … 0) |
| strpos, match at end, 31 B | 2,386 | 0% (0 … +1) | 0% (0 … 0) |
| strpos, repeated prefix, 31 B | 81,279 | 0% (−3 … +13) | +3% (−5 … +19) |
| strpos, no match, 32 B | 2,372 | 0% (0 … 0) | 0% (0 … 0) |
| strpos, match at 0, 32 B | 136 | 0% (−2 … +1) | +1% (0 … +10) |
| strpos, match at end, 32 B | 2,424 | 0% (0 … 0) | 0% (0 … 0) |
| strpos, repeated prefix, 32 B | 81,890 | +1% (0 … +18) | 0% (−8 … +5) |
| strpos, no match, 33 B | 1,777 | 0% (−1 … 0) | 0% (0 … +4) |
| strpos, match at 0, 33 B | 139 | 0% (0 … 0) | 0% (−1 … +2) |
| strpos, match at end, 33 B | 1,845 | 0% (0 … +1) | 0% (0 … +2) |
| strpos, repeated prefix, 33 B | 84,909 | +7% (−8 … +8) | +2% (−5 … +7) |
| strpos, no match, 48 B | 3,753 | 0% (0 … 0) | 0% (0 … 0) |
| strpos, match at 0, 48 B | 167 | 0% (0 … 0) | 0% (0 … +2) |
| strpos, match at end, 48 B | 3,833 | 0% (0 … 0) | 0% (0 … 0) |
| strpos, repeated prefix, 48 B | 111,385 | 0% (0 … +4) | −1% (−6 … 0) |
| strpos, no match, 64 B | 1,770 | 0% (0 … +1) | 0% (0 … 0) |
| strpos, match at 0, 64 B | 197 | 0% (0 … +1) | 0% (0 … +1) |
| strpos, match at end, 64 B | 1,905 | 0% (−1 … +1) | 0% (−1 … 0) |
| strpos, repeated prefix, 64 B | 193,015 | −2% (−13 … 0) | 0% (−3 … +2) |
| strpos, no match, 128 B | 797 | +1% (−1 … +2) | +1% (−1 … +9) |
| strpos, match at 0, 128 B | 331 | +1% (−1 … +6) | 0% (−1 … +2) |
| strpos, match at end, 128 B | 1,091 | 0% (−1 … +2) | 0% (−1 … +1) |
| strpos, repeated prefix, 128 B | 311,840 | 0% (−9 … 0) | 0% (−3 … +1) |
| strpos, no match, 254 B | 676 | −1% (−2 … +1) | −1% (−60 … +2) |
| strpos, match at 0, 254 B | 573 | 0% (0 … +10) | 0% (−3 … +3) |
| strpos, match at end, 254 B | 987 | 0% (−3 … +2) | 0% (−5 … +34) |
| strpos, repeated prefix, 254 B | 545,402 | +1% (0 … +2) | 0% (−1 … 0) |
| strpos, no match, 255 B | 698 | −1% (−14 … +1) | −2% (−2 … 0) |
| strpos, match at 0, 255 B | 576 | 0% (−3 … +3) | 0% (0 … 0) |
| strpos, match at end, 255 B | 1,109 | 0% (−2 … +3) | −1% (−2 … +2) |
| strpos, repeated prefix, 255 B | 548,283 | 0% (−3 … 0) | 0% (0 … 0) |
| strpos, no match, 256 B | 1,136 | 0% (−1 … +1) | 0% (−1 … +1) |
| strpos, match at 0, 256 B | 593 | 0% (0 … +2) | +3% (0 … +3) |
| strpos, match at end, 256 B | 1,491 | −1% (−7 … +1) | 0% (−3 … +6) |
| strpos, repeated prefix, 256 B | 550,470 | 0% (−3 … 0) | 0% (−2 … 0) |
| substr_count, repeated matches, 9 B | 7,228 | 0% (−8 … +3) | 0% (0 … +10) |
| str_replace, repeated matches, 9 B | 15,894 | −1% (−6 … +1) | −1% (−6 … +1) |
| substr_count, repeated matches, 16 B | 6,667 | 0% (−2 … +1) | +1% (0 … +2) |
| str_replace, repeated matches, 16 B | 13,809 | 0% (−1 … +2) | 0% (0 … +1) |
| substr_count, repeated matches, 31 B | 6,024 | 0% (−2 … +4) | +1% (0 … +2) |
| str_replace, repeated matches, 31 B | 12,725 | 0% (−2 … 0) | −1% (−1 … 0) |

~: the change is not larger than the A/A control of the same row: not evidence of a difference.

layout?: in every pass the cycles changed in the same direction, by 3% or more in the median, the instructions by less than 0.5%: the work is the same, so look for the cause (code placement, branch prediction) with `bench why` before reporting the row.
<!-- /bench-table -->
