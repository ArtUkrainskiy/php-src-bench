# Separate cycle and instruction diagnostics

These are presentation views of the two original series, not separate experiments. All groups use the original iteration counts calibrated from ca89 with GCC 15 (50 ms target, three passes). Cycle A/A always uses ca89 with GCC 15. Negative deltas mean less cost for B. These counters are separate from elapsed timing.

## main-nogram: ca89 → No gram4

<!-- bench-table cycle-views/main-nogram.json --full --compact-header --base-name ca89 -->
Absolute cycles/call: ca89 with GCC 15.2.

| call | ca89 cycles | GCC 15.2 | clang 21.1 | Δ instr. |
|---|--:|--:|--:|--:|
| banlist12/en/post/clean @ moderation-en-post-clean | 12,633 | 0% (0 … 0) ~ | 0% (0 … 0) ~ | 0% |
| banlist12/en/post/early @ moderation-en-post-early | 155 | −1% (−5 … 0) ~ | +1% (+1 … +1) ~ | 0% |
| banlist12/ru/post/clean @ moderation-ru-post-clean | 13,524 | 0% (0 … 0) ~ | 0% (0 … 0) ~ | 0% |
| banlist12/es/post/clean @ moderation-es-post-clean | 12,303 | 0% (0 … 0) ~ | 0% (−1 … 0) | 0% |
| banlist12/ar/post/clean @ moderation-ar-post-clean | 17,788 | 0% (0 … 0) ~ | 0% (0 … 0) | 0% |
| banlist12/hi/post/clean @ moderation-hi-post-clean | 11,693 | 0% (0 … 0) ~ | 0% (0 … +1) ~ | 0% |
| banlist12/hi/post/early @ moderation-hi-post-early | 174 | 0% (0 … +4) ~ | 0% (0 … 0) ~ | 0% |
| banlist12/zh/post/clean @ moderation-zh-post-clean | 9,854 | −1% (−1 … 0) | −1% (−1 … 0) | 0% |
| banlist12/ja/post/clean @ moderation-ja-post-clean | 14,239 | 0% (−1 … 0) ~ | 0% (0 … 0) ~ | 0% |
| banlist12/ko/post/clean @ moderation-ko-post-clean | 13,597 | 0% (0 … 0) ~ | 0% (0 … 0) ~ | 0% |
| banlist12/emoji/post/clean @ moderation-emoji-post-clean | 11,596 | 0% (0 … 0) ~ | −1% (−1 … 0) | 0% |
| explode/pipe2/4k @ delimiter-pipe2-4k | 11,590 | 0% (0 … +1) ~ | 0% (−1 … 0) ~ | 0% |
| explode/colon2/4k @ delimiter-colon2-4k | 11,779 | −1% (−3 … 0) | −1% (−2 … 0) | 0% |
| substr-count/colon2/4k @ delimiter-colon2-4k | 4,807 | 0% (−1 … 0) ~ | 0% (−1 … 0) ~ | 0% |
| str-replace/colon2/4k @ delimiter-colon2-4k | 14,468 | 0% (0 … +1) ~ | 0% (−2 … +3) ~ | 0% |
| parse-http/body64k @ http-body64k | 3,908 | 0% (0 … +1) ~ | −1% (−2 … 0) | 0% |
| render-template/4k @ template-4k | 28,207 | 0% (−1 … +1) ~ | +1% (−3 … +1) ~ | 0% |
| log-filter/thread/clean @ logs-thread-clean | 192,927 | +1% (−1 … +1) ~ | 0% (0 … +1) ~ | 0% |
| route/short9/absent @ route-141 | 16,346 | 0% (−1 … 0) | 0% (0 … 0) | 0% |
| route/short9/early @ route-142 | 74 | −1% (−2 … −1) ~ | −1% (−6 … +6) ~ | 0% … +1% |
| route/short16/absent @ route-143 | 11,992 | 0% (0 … 0) ~ | −1% (−1 … 0) | 0% |
| route/short16/early @ route-144 | 91 | +1% (0 … +1) ~ | 0% (−1 … +1) ~ | 0% |
| route/short31/absent @ route-145 | 5,843 | 0% (−1 … 0) | 0% (0 … +1) | 0% |
| route/short31/early @ route-146 | 129 | +1% (−1 … +3) ~ | −1% (−8 … −1) ~ | 0% |
| route/long/ordinary-miss @ route-147 | 4,906 | 0% (0 … 0) ~ | 0% (0 … +4) | 0% |
| route/long/early @ route-148 | 198 | 0% (0 … +1) | 0% (0 … +1) ~ | 0% |
| route/pair/ascii/absent @ route-149 | 4,043 | 0% (−1 … 0) | −1% (−4 … 0) | 0% |
| route/pair/dna/absent @ route-150 | 4,060 | 0% (−2 … +1) ~ | +3% (+1 … +9) layout? | 0% |
| route/pair/binary/absent @ route-151 | 4,012 | 0% (0 … +1) | 0% (0 … 0) ~ | 0% |
| route/gram/selective/absent @ route-152 | 15,891 | −26% (−26 … −26) | −31% (−33 … −29) | −36% … −25% |
| route/gram/selective/late @ route-153 | 15,881 | −22% (−22 … −22) | −30% (−30 … −28) | −35% … −24% |
| route/gram/dense/absent @ route-154 | 13,126 | −5% (−5 … −5) | −3% (−6 … +1) | −4% … −3% |
| route/gram/changing/absent @ route-155 | 72,577 | −35% (−35 … −35) | −35% (−36 … −32) | −32% … −30% |
| route/twoway/periodic-memory @ route-156 | 120,919 | −3% (−4 … +3) ~ | 0% (−2 … +1) ~ | 0% |
| route/threshold/8191 @ route-157 | 157,949 | −1% (−5 … +2) ~ | −3% (−9 … +4) | 0% |
| route/threshold/8192 @ route-158 | 2,532 | −1% (−3 … 0) ~ | 0% (0 … 0) ~ | 0% |

Control: ca89 against itself.

Absolute cycles/call: ca89 with GCC 15.2.

| call | ca89 cycles | A/A start | A/A end |
|---|--:|--:|--:|
| banlist12/en/post/clean @ moderation-en-post-clean | 12,679 | −1% (−1 … 0) | 0% (0 … 0) |
| banlist12/en/post/early @ moderation-en-post-early | 156 | −1% (−6 … 0) | −1% (−2 … −1) |
| banlist12/ru/post/clean @ moderation-ru-post-clean | 13,527 | 0% (0 … 0) | 0% (−1 … 0) |
| banlist12/es/post/clean @ moderation-es-post-clean | 12,290 | 0% (−1 … 0) | 0% (0 … 0) |
| banlist12/ar/post/clean @ moderation-ar-post-clean | 17,856 | 0% (0 … 0) | 0% (0 … 0) |
| banlist12/hi/post/clean @ moderation-hi-post-clean | 11,638 | 0% (0 … +1) | −1% (−2 … 0) |
| banlist12/hi/post/early @ moderation-hi-post-early | 174 | 0% (−3 … +2) | +2% (−3 … +3) |
| banlist12/zh/post/clean @ moderation-zh-post-clean | 9,872 | 0% (−1 … 0) | 0% (0 … 0) |
| banlist12/ja/post/clean @ moderation-ja-post-clean | 14,213 | 0% (0 … 0) | 0% (0 … 0) |
| banlist12/ko/post/clean @ moderation-ko-post-clean | 13,550 | 0% (0 … 0) | 0% (−1 … 0) |
| banlist12/emoji/post/clean @ moderation-emoji-post-clean | 11,556 | 0% (0 … 0) | 0% (0 … 0) |
| explode/pipe2/4k @ delimiter-pipe2-4k | 11,561 | 0% (−1 … +2) | −1% (−1 … −1) |
| explode/colon2/4k @ delimiter-colon2-4k | 11,604 | 0% (0 … +1) | 0% (−1 … 0) |
| substr-count/colon2/4k @ delimiter-colon2-4k | 4,826 | −1% (−1 … 0) | 0% (−1 … 0) |
| str-replace/colon2/4k @ delimiter-colon2-4k | 14,523 | 0% (−1 … 0) | 0% (0 … +1) |
| parse-http/body64k @ http-body64k | 3,897 | 0% (0 … +1) | 0% (0 … +6) |
| render-template/4k @ template-4k | 28,300 | −2% (−2 … +1) | 0% (−1 … +2) |
| log-filter/thread/clean @ logs-thread-clean | 195,308 | 0% (−2 … +1) | −1% (−1 … 0) |
| route/short9/absent @ route-141 | 16,313 | 0% (−1 … 0) | 0% (0 … 0) |
| route/short9/early @ route-142 | 74 | +1% (−1 … +3) | −4% (−5 … −1) |
| route/short16/absent @ route-143 | 11,969 | 0% (0 … 0) | 0% (0 … 0) |
| route/short16/early @ route-144 | 93 | −2% (−3 … +1) | 0% (−1 … 0) |
| route/short31/absent @ route-145 | 5,843 | 0% (−1 … 0) | 0% (0 … +1) |
| route/short31/early @ route-146 | 135 | −6% (−7 … +6) | +6% (−1 … +8) |
| route/long/ordinary-miss @ route-147 | 4,909 | 0% (0 … +1) | 0% (0 … 0) |
| route/long/early @ route-148 | 197 | 0% (−1 … +1) | 0% (0 … +1) |
| route/pair/ascii/absent @ route-149 | 4,056 | 0% (−1 … 0) | 0% (0 … +1) |
| route/pair/dna/absent @ route-150 | 4,093 | −2% (−2 … 0) | 0% (0 … 0) |
| route/pair/binary/absent @ route-151 | 4,017 | 0% (0 … +1) | 0% (0 … +1) |
| route/gram/selective/absent @ route-152 | 15,891 | 0% (0 … +4) | 0% (0 … 0) |
| route/gram/selective/late @ route-153 | 15,912 | 0% (−1 … 0) | 0% (0 … 0) |
| route/gram/dense/absent @ route-154 | 13,106 | 0% (0 … 0) | 0% (0 … 0) |
| route/gram/changing/absent @ route-155 | 72,533 | 0% (−1 … 0) | 0% (0 … 0) |
| route/twoway/periodic-memory @ route-156 | 125,948 | −6% (−7 … 0) | +4% (+4 … +12) |
| route/threshold/8191 @ route-157 | 160,557 | −1% (−3 … +1) | −1% (−2 … 0) |
| route/threshold/8192 @ route-158 | 2,524 | −1% (−2 … −1) | 0% (−1 … +1) |

~: the change is not larger than the A/A control of the same row: not evidence of a difference.

layout?: in every pass the cycles changed in the same direction, by 3% or more in the median, the instructions by less than 0.5%: the work is the same, so look for the cause (code placement, branch prediction) with `bench why` before reporting the row.
<!-- /bench-table -->

## main-scalar: ca89 → Scalar

<!-- bench-table cycle-views/main-scalar.json --full --compact-header --base-name ca89 -->
Absolute cycles/call: ca89 with GCC 15.2.

| call | ca89 cycles | GCC 15.2 | clang 21.1 | Δ instr. |
|---|--:|--:|--:|--:|
| banlist12/en/post/clean @ moderation-en-post-clean | 12,660 | 0% (0 … +1) ~ | −1% (−1 … 0) | 0% |
| banlist12/en/post/early @ moderation-en-post-early | 155 | +1% (−6 … +12) ~ | +1% (−1 … +6) ~ | 0% |
| banlist12/ru/post/clean @ moderation-ru-post-clean | 13,570 | 0% (0 … +1) ~ | 0% (−1 … 0) ~ | 0% |
| banlist12/es/post/clean @ moderation-es-post-clean | 12,260 | 0% (−1 … +1) ~ | 0% (−1 … 0) | 0% |
| banlist12/ar/post/clean @ moderation-ar-post-clean | 17,843 | 0% (−1 … +1) ~ | 0% (−1 … 0) | 0% |
| banlist12/hi/post/clean @ moderation-hi-post-clean | 11,701 | 0% (−1 … 0) ~ | 0% (0 … 0) ~ | 0% |
| banlist12/hi/post/early @ moderation-hi-post-early | 167 | +4% (−1 … +5) | 0% (−1 … +2) ~ | 0% |
| banlist12/zh/post/clean @ moderation-zh-post-clean | 9,841 | 0% (0 … +1) | 0% (−1 … 0) ~ | 0% |
| banlist12/ja/post/clean @ moderation-ja-post-clean | 14,233 | 0% (0 … +1) | 0% (0 … 0) ~ | 0% |
| banlist12/ko/post/clean @ moderation-ko-post-clean | 13,556 | 0% (0 … 0) ~ | 0% (0 … 0) ~ | 0% |
| banlist12/emoji/post/clean @ moderation-emoji-post-clean | 11,575 | 0% (0 … 0) ~ | 0% (−1 … +1) | 0% |
| explode/pipe2/4k @ delimiter-pipe2-4k | 11,560 | 0% (−1 … 0) ~ | 0% (0 … +2) ~ | 0% |
| explode/colon2/4k @ delimiter-colon2-4k | 11,752 | −1% (−2 … 0) | 0% (0 … +1) ~ | 0% |
| substr-count/colon2/4k @ delimiter-colon2-4k | 4,826 | −1% (−1 … 0) ~ | 0% (−3 … +2) ~ | 0% |
| str-replace/colon2/4k @ delimiter-colon2-4k | 14,477 | 0% (0 … +1) ~ | 0% (−4 … 0) | 0% |
| parse-http/body64k @ http-body64k | 3,899 | −1% (−2 … −1) | +1% (0 … +1) | 0% |
| render-template/4k @ template-4k | 28,121 | −1% (−2 … 0) ~ | 0% (−1 … +1) ~ | 0% |
| log-filter/thread/clean @ logs-thread-clean | 193,432 | −1% (−1 … +1) ~ | +1% (−2 … +2) ~ | 0% |
| route/short9/absent @ route-141 | 16,342 | +1% (+1 … +1) | 0% (0 … 0) | 0% |
| route/short9/early @ route-142 | 73 | +1% (−6 … +2) ~ | +7% (0 … +7) | 0% |
| route/short16/absent @ route-143 | 11,980 | +1% (−1 … +1) | 0% (0 … 0) ~ | 0% |
| route/short16/early @ route-144 | 91 | −1% (−1 … −1) ~ | +1% (0 … +5) ~ | 0% |
| route/short31/absent @ route-145 | 5,860 | +3% (+3 … +4) layout? | −1% (−1 … 0) | 0% |
| route/short31/early @ route-146 | 139 | −10% (−13 … +1) | +1% (−9 … +1) ~ | 0% |
| route/long/ordinary-miss @ route-147 | 4,909 | −1% (−2 … −1) | 0% (0 … +1) ~ | 0% |
| route/long/early @ route-148 | 198 | −6% (−6 … −3) | +1% (−1 … +4) | −1% … 0% |
| route/pair/ascii/absent @ route-149 | 4,044 | +1137% (+1128 … +1143) | +803% (+796 … +811) | +778% … +1380% |
| route/pair/dna/absent @ route-150 | 4,030 | +1141% (+1138 … +1142) | +802% (+786 … +812) | +778% … +1380% |
| route/pair/binary/absent @ route-151 | 3,997 | +1152% (+1152 … +1152) | +801% (+800 … +810) | +779% … +1384% |
| route/gram/selective/absent @ route-152 | 15,900 | −70% (−71 … −70) | −71% (−71 … −69) | −64% … −63% |
| route/gram/selective/late @ route-153 | 15,883 | −67% (−67 … −66) | −69% (−69 … −69) | −63% … −62% |
| route/gram/dense/absent @ route-154 | 13,102 | −56% (−56 … −56) | −55% (−55 … −54) | −48% … −38% |
| route/gram/changing/absent @ route-155 | 72,411 | −73% (−73 … −73) | −72% (−72 … −71) | −65% … −59% |
| route/twoway/periodic-memory @ route-156 | 119,032 | −14% (−23 … −7) | +32% (+31 … +32) | −13% … −8% |
| route/threshold/8191 @ route-157 | 156,164 | +1% (−2 … +1) ~ | +2% (0 … +7) | 0% |
| route/threshold/8192 @ route-158 | 2,517 | +911% (+907 … +926) | +651% (+648 … +663) | +639% … +1093% |

Control: ca89 against itself.

Absolute cycles/call: ca89 with GCC 15.2.

| call | ca89 cycles | A/A start | A/A end |
|---|--:|--:|--:|
| banlist12/en/post/clean @ moderation-en-post-clean | 12,679 | −1% (−1 … 0) | 0% (0 … 0) |
| banlist12/en/post/early @ moderation-en-post-early | 156 | −1% (−6 … 0) | −1% (−2 … −1) |
| banlist12/ru/post/clean @ moderation-ru-post-clean | 13,527 | 0% (0 … 0) | 0% (−1 … 0) |
| banlist12/es/post/clean @ moderation-es-post-clean | 12,290 | 0% (−1 … 0) | 0% (0 … 0) |
| banlist12/ar/post/clean @ moderation-ar-post-clean | 17,856 | 0% (0 … 0) | 0% (0 … 0) |
| banlist12/hi/post/clean @ moderation-hi-post-clean | 11,638 | 0% (0 … +1) | −1% (−2 … 0) |
| banlist12/hi/post/early @ moderation-hi-post-early | 174 | 0% (−3 … +2) | +2% (−3 … +3) |
| banlist12/zh/post/clean @ moderation-zh-post-clean | 9,872 | 0% (−1 … 0) | 0% (0 … 0) |
| banlist12/ja/post/clean @ moderation-ja-post-clean | 14,213 | 0% (0 … 0) | 0% (0 … 0) |
| banlist12/ko/post/clean @ moderation-ko-post-clean | 13,550 | 0% (0 … 0) | 0% (−1 … 0) |
| banlist12/emoji/post/clean @ moderation-emoji-post-clean | 11,556 | 0% (0 … 0) | 0% (0 … 0) |
| explode/pipe2/4k @ delimiter-pipe2-4k | 11,561 | 0% (−1 … +2) | −1% (−1 … −1) |
| explode/colon2/4k @ delimiter-colon2-4k | 11,604 | 0% (0 … +1) | 0% (−1 … 0) |
| substr-count/colon2/4k @ delimiter-colon2-4k | 4,826 | −1% (−1 … 0) | 0% (−1 … 0) |
| str-replace/colon2/4k @ delimiter-colon2-4k | 14,523 | 0% (−1 … 0) | 0% (0 … +1) |
| parse-http/body64k @ http-body64k | 3,897 | 0% (0 … +1) | 0% (0 … +6) |
| render-template/4k @ template-4k | 28,300 | −2% (−2 … +1) | 0% (−1 … +2) |
| log-filter/thread/clean @ logs-thread-clean | 195,308 | 0% (−2 … +1) | −1% (−1 … 0) |
| route/short9/absent @ route-141 | 16,313 | 0% (−1 … 0) | 0% (0 … 0) |
| route/short9/early @ route-142 | 74 | +1% (−1 … +3) | −4% (−5 … −1) |
| route/short16/absent @ route-143 | 11,969 | 0% (0 … 0) | 0% (0 … 0) |
| route/short16/early @ route-144 | 93 | −2% (−3 … +1) | 0% (−1 … 0) |
| route/short31/absent @ route-145 | 5,843 | 0% (−1 … 0) | 0% (0 … +1) |
| route/short31/early @ route-146 | 135 | −6% (−7 … +6) | +6% (−1 … +8) |
| route/long/ordinary-miss @ route-147 | 4,909 | 0% (0 … +1) | 0% (0 … 0) |
| route/long/early @ route-148 | 197 | 0% (−1 … +1) | 0% (0 … +1) |
| route/pair/ascii/absent @ route-149 | 4,056 | 0% (−1 … 0) | 0% (0 … +1) |
| route/pair/dna/absent @ route-150 | 4,093 | −2% (−2 … 0) | 0% (0 … 0) |
| route/pair/binary/absent @ route-151 | 4,017 | 0% (0 … +1) | 0% (0 … +1) |
| route/gram/selective/absent @ route-152 | 15,891 | 0% (0 … +4) | 0% (0 … 0) |
| route/gram/selective/late @ route-153 | 15,912 | 0% (−1 … 0) | 0% (0 … 0) |
| route/gram/dense/absent @ route-154 | 13,106 | 0% (0 … 0) | 0% (0 … 0) |
| route/gram/changing/absent @ route-155 | 72,533 | 0% (−1 … 0) | 0% (0 … 0) |
| route/twoway/periodic-memory @ route-156 | 125,948 | −6% (−7 … 0) | +4% (+4 … +12) |
| route/threshold/8191 @ route-157 | 160,557 | −1% (−3 … +1) | −1% (−2 … 0) |
| route/threshold/8192 @ route-158 | 2,524 | −1% (−2 … −1) | 0% (−1 … +1) |

~: the change is not larger than the A/A control of the same row: not evidence of a difference.

layout?: in every pass the cycles changed in the same direction, by 3% or more in the median, the instructions by less than 0.5%: the work is the same, so look for the cause (code placement, branch prediction) with `bench why` before reporting the row.
<!-- /bench-table -->

## main-stock: Stock → ca89

<!-- bench-table cycle-views/main-stock.json --full --compact-header --base-name Stock -->
Absolute cycles/call: Stock with GCC 15.2.

| call | Stock cycles | GCC 15.2 | clang 21.1 | Δ instr. |
|---|--:|--:|--:|--:|
| banlist12/en/post/clean @ moderation-en-post-clean | 14,071 | −10% (−11 … −10) | −9% (−10 … −9) | −6% … −2% |
| banlist12/en/post/early @ moderation-en-post-early | 144 | +8% (0 … +8) layout? | −1% (−2 … +1) ~ | 0% |
| banlist12/ru/post/clean @ moderation-ru-post-clean | 14,340 | −5% (−6 … −5) | −4% (−5 … −4) | −3% … −2% |
| banlist12/es/post/clean @ moderation-es-post-clean | 13,539 | −9% (−10 … −7) | −9% (−10 … −7) | −6% … −2% |
| banlist12/ar/post/clean @ moderation-ar-post-clean | 18,744 | −5% (−5 … −4) | −5% (−5 … −5) | −4% … −1% |
| banlist12/hi/post/clean @ moderation-hi-post-clean | 12,560 | −7% (−7 … −7) | −4% (−5 … −4) | −5% … −3% |
| banlist12/hi/post/early @ moderation-hi-post-early | 204 | −14% (−19 … −13) | −16% (−17 … −16) | −17% … −6% |
| banlist12/zh/post/clean @ moderation-zh-post-clean | 10,955 | −10% (−10 … −10) | −11% (−11 … −11) | −8% … −3% |
| banlist12/ja/post/clean @ moderation-ja-post-clean | 15,553 | −9% (−9 … −8) | −8% (−8 … −7) | −5% … −2% |
| banlist12/ko/post/clean @ moderation-ko-post-clean | 14,724 | −8% (−8 … −8) | −8% (−8 … −7) | −5% … −2% |
| banlist12/emoji/post/clean @ moderation-emoji-post-clean | 12,755 | −9% (−9 … −9) | −10% (−10 … −9) | −6% … −2% |
| explode/pipe2/4k @ delimiter-pipe2-4k | 11,592 | −1% (−2 … +1) ~ | +1% (0 … +1) ~ | 0% |
| explode/colon2/4k @ delimiter-colon2-4k | 11,657 | −1% (−5 … +1) | +1% (−1 … +2) | 0% |
| substr-count/colon2/4k @ delimiter-colon2-4k | 4,806 | 0% (0 … 0) ~ | 0% (−3 … +3) ~ | 0% |
| str-replace/colon2/4k @ delimiter-colon2-4k | 14,539 | −1% (−1 … 0) | 0% (−2 … +2) | 0% |
| parse-http/body64k @ http-body64k | 3,851 | +1% (+1 … +2) | −2% (−3 … −1) | 0% |
| render-template/4k @ template-4k | 33,035 | −15% (−16 … −14) | −14% (−15 … −14) | −18% … −7% |
| log-filter/thread/clean @ logs-thread-clean | 195,380 | +1% (0 … +3) ~ | +1% (−1 … +1) ~ | 0% |
| route/short9/absent @ route-141 | 18,096 | −10% (−13 … −9) | −10% (−10 … −10) layout? | −1% … 0% |
| route/short9/early @ route-142 | 99 | −26% (−27 … −25) | −28% (−29 … −25) | −30% … −12% |
| route/short16/absent @ route-143 | 13,291 | −10% (−10 … −10) | −10% (−11 … −10) layout? | −1% … 0% |
| route/short16/early @ route-144 | 122 | −25% (−26 … −24) | −31% (−31 … −28) | −25% … −11% |
| route/short31/absent @ route-145 | 6,613 | −12% (−12 … −11) | −10% (−10 … −10) layout? | −1% … 0% |
| route/short31/early @ route-146 | 153 | −10% (−18 … −5) | −30% (−36 … −19) | −19% … −8% |
| route/long/ordinary-miss @ route-147 | 4,923 | 0% (−1 … 0) | 0% (0 … 0) | 0% … +7% |
| route/long/early @ route-148 | 186 | +6% (+4 … +7) | +3% (+1 … +4) | +3% … +22% |
| route/pair/ascii/absent @ route-149 | 319,329 | −99% (−99 … −99) | −99% (−99 … −99) | −99% … −98% |
| route/pair/dna/absent @ route-150 | 319,384 | −99% (−99 … −99) | −99% (−99 … −99) | −99% … −98% |
| route/pair/binary/absent @ route-151 | 319,359 | −99% (−99 … −99) | −99% (−99 … −99) | −99% … −98% |
| route/gram/selective/absent @ route-152 | 87,485 | −82% (−82 … −82) | −80% (−81 … −80) | −65% … −63% |
| route/gram/selective/late @ route-153 | 87,545 | −82% (−82 … −82) | −80% (−81 … −80) | −65% … −63% |
| route/gram/dense/absent @ route-154 | 91,071 | −86% (−86 … −86) | −84% (−85 … −84) | −78% … −76% |
| route/gram/changing/absent @ route-155 | 353,377 | −80% (−80 … −79) | −77% (−78 … −77) | −72% … −69% |
| route/twoway/periodic-memory @ route-156 | 716,800 | −83% (−84 … −82) | −90% (−91 … −90) | −85% |
| route/threshold/8191 @ route-157 | 150,936 | +5% (+3 … +6) layout? | −38% (−39 … −36) layout? | 0% |
| route/threshold/8192 @ route-158 | 159,627 | −98% (−98 … −98) | −99% (−99 … −99) | −99% … −98% |

Control: Stock against itself.

Absolute cycles/call: Stock with GCC 15.2.

| call | Stock cycles | A/A start | A/A end |
|---|--:|--:|--:|
| banlist12/en/post/clean @ moderation-en-post-clean | 12,679 | −1% (−1 … 0) | 0% (0 … 0) |
| banlist12/en/post/early @ moderation-en-post-early | 156 | −1% (−6 … 0) | −1% (−2 … −1) |
| banlist12/ru/post/clean @ moderation-ru-post-clean | 13,527 | 0% (0 … 0) | 0% (−1 … 0) |
| banlist12/es/post/clean @ moderation-es-post-clean | 12,290 | 0% (−1 … 0) | 0% (0 … 0) |
| banlist12/ar/post/clean @ moderation-ar-post-clean | 17,856 | 0% (0 … 0) | 0% (0 … 0) |
| banlist12/hi/post/clean @ moderation-hi-post-clean | 11,638 | 0% (0 … +1) | −1% (−2 … 0) |
| banlist12/hi/post/early @ moderation-hi-post-early | 174 | 0% (−3 … +2) | +2% (−3 … +3) |
| banlist12/zh/post/clean @ moderation-zh-post-clean | 9,872 | 0% (−1 … 0) | 0% (0 … 0) |
| banlist12/ja/post/clean @ moderation-ja-post-clean | 14,213 | 0% (0 … 0) | 0% (0 … 0) |
| banlist12/ko/post/clean @ moderation-ko-post-clean | 13,550 | 0% (0 … 0) | 0% (−1 … 0) |
| banlist12/emoji/post/clean @ moderation-emoji-post-clean | 11,556 | 0% (0 … 0) | 0% (0 … 0) |
| explode/pipe2/4k @ delimiter-pipe2-4k | 11,561 | 0% (−1 … +2) | −1% (−1 … −1) |
| explode/colon2/4k @ delimiter-colon2-4k | 11,604 | 0% (0 … +1) | 0% (−1 … 0) |
| substr-count/colon2/4k @ delimiter-colon2-4k | 4,826 | −1% (−1 … 0) | 0% (−1 … 0) |
| str-replace/colon2/4k @ delimiter-colon2-4k | 14,523 | 0% (−1 … 0) | 0% (0 … +1) |
| parse-http/body64k @ http-body64k | 3,897 | 0% (0 … +1) | 0% (0 … +6) |
| render-template/4k @ template-4k | 28,300 | −2% (−2 … +1) | 0% (−1 … +2) |
| log-filter/thread/clean @ logs-thread-clean | 195,308 | 0% (−2 … +1) | −1% (−1 … 0) |
| route/short9/absent @ route-141 | 16,313 | 0% (−1 … 0) | 0% (0 … 0) |
| route/short9/early @ route-142 | 74 | +1% (−1 … +3) | −4% (−5 … −1) |
| route/short16/absent @ route-143 | 11,969 | 0% (0 … 0) | 0% (0 … 0) |
| route/short16/early @ route-144 | 93 | −2% (−3 … +1) | 0% (−1 … 0) |
| route/short31/absent @ route-145 | 5,843 | 0% (−1 … 0) | 0% (0 … +1) |
| route/short31/early @ route-146 | 135 | −6% (−7 … +6) | +6% (−1 … +8) |
| route/long/ordinary-miss @ route-147 | 4,909 | 0% (0 … +1) | 0% (0 … 0) |
| route/long/early @ route-148 | 197 | 0% (−1 … +1) | 0% (0 … +1) |
| route/pair/ascii/absent @ route-149 | 4,056 | 0% (−1 … 0) | 0% (0 … +1) |
| route/pair/dna/absent @ route-150 | 4,093 | −2% (−2 … 0) | 0% (0 … 0) |
| route/pair/binary/absent @ route-151 | 4,017 | 0% (0 … +1) | 0% (0 … +1) |
| route/gram/selective/absent @ route-152 | 15,891 | 0% (0 … +4) | 0% (0 … 0) |
| route/gram/selective/late @ route-153 | 15,912 | 0% (−1 … 0) | 0% (0 … 0) |
| route/gram/dense/absent @ route-154 | 13,106 | 0% (0 … 0) | 0% (0 … 0) |
| route/gram/changing/absent @ route-155 | 72,533 | 0% (−1 … 0) | 0% (0 … 0) |
| route/twoway/periodic-memory @ route-156 | 125,948 | −6% (−7 … 0) | +4% (+4 … +12) |
| route/threshold/8191 @ route-157 | 160,557 | −1% (−3 … +1) | −1% (−2 … 0) |
| route/threshold/8192 @ route-158 | 2,524 | −1% (−2 … −1) | 0% (−1 … +1) |

~: the change is not larger than the A/A control of the same row: not evidence of a difference.

layout?: in every pass the cycles changed in the same direction, by 3% or more in the median, the instructions by less than 0.5%: the work is the same, so look for the cause (code placement, branch prediction) with `bench why` before reporting the row.
<!-- /bench-table -->

## periodic-nogram: ca89 → No gram4

<!-- bench-table cycle-views/periodic-nogram.json --full --compact-header --base-name ca89 -->
Absolute cycles/call: ca89 with GCC 15.2.

| call | ca89 cycles | GCC 15.2 | clang 21.1 | Δ instr. |
|---|--:|--:|--:|--:|
| gram-periodic/ascii/absent @ periodic-ascii | 57,052 | +154% (+152 … +154) | +168% (+167 … +175) | +208% … +239% |
| gram-periodic/dna/absent @ periodic-dna | 56,921 | +255% (+254 … +255) | +252% (+251 … +252) | +325% … +370% |

Control: ca89 against itself.

Absolute cycles/call: ca89 with GCC 15.2.

| call | ca89 cycles | A/A start | A/A end |
|---|--:|--:|--:|
| gram-periodic/ascii/absent @ periodic-ascii | 57,181 | 0% (−1 … 0) | 0% (0 … 0) |
| gram-periodic/dna/absent @ periodic-dna | 57,028 | 0% (0 … +1) | −2% (−3 … 0) |
<!-- /bench-table -->

## periodic-scalar: ca89 → Scalar

<!-- bench-table cycle-views/periodic-scalar.json --full --compact-header --base-name ca89 -->
Absolute cycles/call: ca89 with GCC 15.2.

| call | ca89 cycles | GCC 15.2 | clang 21.1 | Δ instr. |
|---|--:|--:|--:|--:|
| gram-periodic/ascii/absent @ periodic-ascii | 57,061 | +132% (+130 … +133) | +164% (+163 … +173) | +213% … +233% |
| gram-periodic/dna/absent @ periodic-dna | 56,928 | +247% (+245 … +247) | +234% (+234 … +247) | +347% … +383% |

Control: ca89 against itself.

Absolute cycles/call: ca89 with GCC 15.2.

| call | ca89 cycles | A/A start | A/A end |
|---|--:|--:|--:|
| gram-periodic/ascii/absent @ periodic-ascii | 57,181 | 0% (−1 … 0) | 0% (0 … 0) |
| gram-periodic/dna/absent @ periodic-dna | 57,028 | 0% (0 … +1) | −2% (−3 … 0) |
<!-- /bench-table -->

## periodic-stock: Stock → ca89

<!-- bench-table cycle-views/periodic-stock.json --full --compact-header --base-name Stock -->
Absolute cycles/call: Stock with GCC 15.2.

| call | Stock cycles | GCC 15.2 | clang 21.1 | Δ instr. |
|---|--:|--:|--:|--:|
| gram-periodic/ascii/absent @ periodic-ascii | 361,029 | −84% (−84 … −84) | −82% (−82 … −82) | −75% … −74% |
| gram-periodic/dna/absent @ periodic-dna | 199,957 | −72% (−72 … −71) | −64% (−64 … −64) | −60% … −58% |

Control: Stock against itself.

Absolute cycles/call: Stock with GCC 15.2.

| call | Stock cycles | A/A start | A/A end |
|---|--:|--:|--:|
| gram-periodic/ascii/absent @ periodic-ascii | 57,181 | 0% (−1 … 0) | 0% (0 … 0) |
| gram-periodic/dna/absent @ periodic-dna | 57,028 | 0% (0 … +1) | −2% (−3 … 0) |
<!-- /bench-table -->
