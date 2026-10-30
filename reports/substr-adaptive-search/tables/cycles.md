# Complete primary cycle matrices

All 76 preselected product cases, every available compiler, original pass ranges and same-row A/A controls. AMD uses five passes; quiet Intel uses three. A/A is the first compiler of each machine, not each compiler. These cycles were measured separately from elapsed time.

## AMD

<!-- bench-table ../data/amd/cycles-reference.json --full --compact-header --base-name Stock -->
Absolute cycles/call: Stock with GCC 15.2.

| call | Stock cycles | GCC 15.2 | clang 21.1 | Δ instr. |
|---|--:|--:|--:|--:|
| banlist12/en/comment/clean @ moderation-en-comment-clean | 2,289 | +1% (−1 … +2) | 0% (−1 … +1) ~ | 0% |
| banlist12/en/comment/early @ moderation-en-comment-early | 147 | +3% (0 … +9) | 0% (0 … +1) ~ | 0% |
| banlist12/en/comment/late @ moderation-en-comment-late | 2,531 | 0% (0 … +1) ~ | 0% (−1 … 0) | 0% |
| banlist12/en/post/clean @ moderation-en-post-clean | 13,958 | −10% (−11 … −10) | −10% (−10 … −10) | −6% … −2% |
| banlist12/en/post/early @ moderation-en-post-early | 149 | −2% (−9 … +5) ~ | −1% (−22 … +1) ~ | 0% |
| banlist12/en/post/late @ moderation-en-post-late | 14,288 | −11% (−11 … −7) | −10% (−10 … −9) | −6% … −2% |
| banlist12/en/thread/clean @ moderation-en-thread-clean | 812,186 | −7% (−8 … −7) layout? | −8% (−8 … −8) layout? | 0% |
| banlist12/en/thread/early @ moderation-en-thread-early | 145 | −3% (−6 … +4) | 0% (0 … +1) ~ | 0% |
| banlist12/en/thread/late @ moderation-en-thread-late | 811,745 | −8% (−8 … −7) layout? | −8% (−9 … −8) layout? | 0% |
| banlist12/ru/comment/clean @ moderation-ru-comment-clean | 11,846 | 0% (0 … +1) ~ | 0% (0 … 0) ~ | 0% |
| banlist12/ru/comment/early @ moderation-ru-comment-early | 143 | −2% (−8 … +5) | +1% (−2 … +4) ~ | 0% |
| banlist12/ru/comment/late @ moderation-ru-comment-late | 12,799 | 0% (−1 … 0) ~ | 0% (0 … 0) ~ | 0% |
| banlist12/ru/post/clean @ moderation-ru-post-clean | 14,319 | −6% (−6 … −1) | −4% (−4 … −4) | −3% … −2% |
| banlist12/ru/post/early @ moderation-ru-post-early | 149 | −2% (−5 … +1) ~ | +1% (−2 … +5) ~ | 0% |
| banlist12/ru/post/late @ moderation-ru-post-late | 15,033 | −5% (−5 … −1) | −4% (−6 … −4) | −3% … −2% |
| banlist12/ru/thread/clean @ moderation-ru-thread-clean | 1,042,274 | −2% (−2 … −2) | −6% (−6 … −6) | 0% … +4% |
| banlist12/ru/thread/early @ moderation-ru-thread-early | 138 | +8% (−5 … +8) | 0% (−2 … +1) ~ | 0% |
| banlist12/ru/thread/late @ moderation-ru-thread-late | 1,018,428 | −1% (−2 … 0) | −5% (−5 … −5) | 0% … +4% |
| banlist12/es/comment/clean @ moderation-es-comment-clean | 2,658 | −1% (−2 … 0) | 0% (−1 … +1) ~ | 0% |
| banlist12/es/post/clean @ moderation-es-post-clean | 13,467 | −10% (−10 … −9) | −10% (−10 … −9) | −6% … −2% |
| banlist12/es/post/early @ moderation-es-post-early | 141 | +5% (−6 … +11) | 0% (−2 … +2) ~ | 0% |
| banlist12/es/thread/clean @ moderation-es-thread-clean | 834,909 | −7% (−7 … −6) layout? | −8% (−8 … −7) layout? | 0% |
| banlist12/ar/comment/clean @ moderation-ar-comment-clean | 9,669 | 0% (0 … +1) ~ | 0% (0 … +1) ~ | 0% |
| banlist12/ar/comment/late @ moderation-ar-comment-late | 10,947 | 0% (0 … +2) ~ | 0% (−1 … 0) | 0% |
| banlist12/ar/post/clean @ moderation-ar-post-clean | 18,605 | −5% (−5 … +17) | −5% (−5 … −5) | −4% … −1% |
| banlist12/ar/post/early @ moderation-ar-post-early | 148 | −3% (−8 … +2) | 0% (−3 … +2) ~ | 0% |
| banlist12/ar/thread/clean @ moderation-ar-thread-clean | 1,232,914 | −1% (−1 … −1) | −4% (−5 … −4) layout? | 0% |
| banlist12/hi/comment/clean @ moderation-hi-comment-clean | 13,728 | 0% (0 … 0) ~ | 0% (−1 … +2) ~ | 0% |
| banlist12/hi/comment/late @ moderation-hi-comment-late | 15,831 | 0% (−1 … +2) | 0% (−1 … +3) | 0% |
| banlist12/hi/post/clean @ moderation-hi-post-clean | 12,483 | −7% (−10 … −6) | −4% (−5 … −3) | −5% … −3% |
| banlist12/hi/post/early @ moderation-hi-post-early | 198 | −15% (−19 … −13) | −13% (−15 … +2) | −17% … −6% |
| banlist12/hi/thread/clean @ moderation-hi-thread-clean | 848,894 | 0% (−1 … 0) | −6% (−7 … −5) | 0% … +4% |
| banlist12/hi/thread/late @ moderation-hi-thread-late | 860,152 | −4% (−5 … −4) layout? | −10% (−10 … −9) | 0% … +4% |
| banlist12/zh/comment/clean @ moderation-zh-comment-clean | 2,560 | 0% (−2 … +2) ~ | 0% (−1 … +1) ~ | 0% |
| banlist12/zh/post/clean @ moderation-zh-post-clean | 10,923 | −10% (−11 … −10) | −12% (−12 … −11) | −8% … −3% |
| banlist12/zh/post/early @ moderation-zh-post-early | 187 | −12% (−20 … −12) | −12% (−18 … −10) | −18% … −6% |
| banlist12/zh/thread/clean @ moderation-zh-thread-clean | 709,216 | −6% (−7 … −6) layout? | −9% (−9 … −8) layout? | 0% |
| banlist12/ja/comment/clean @ moderation-ja-comment-clean | 6,346 | 0% (0 … +1) ~ | 0% (−1 … +1) | 0% |
| banlist12/ja/comment/late @ moderation-ja-comment-late | 7,201 | 0% (0 … +2) ~ | 0% (−2 … 0) ~ | 0% |
| banlist12/ja/post/clean @ moderation-ja-post-clean | 15,437 | −9% (−9 … −9) | −8% (−8 … −8) | −5% … −2% |
| banlist12/ja/post/early @ moderation-ja-post-early | 189 | −19% (−19 … −13) | −14% (−17 … −14) | −18% … −7% |
| banlist12/ja/thread/clean @ moderation-ja-thread-clean | 1,039,570 | −4% (−4 … −4) layout? | −6% (−7 … −6) layout? | 0% |
| banlist12/ko/comment/clean @ moderation-ko-comment-clean | 4,640 | −1% (−5 … 0) | 0% (−3 … +3) | 0% |
| banlist12/ko/post/clean @ moderation-ko-post-clean | 14,561 | −8% (−8 … −7) | −8% (−9 … −7) | −5% … −2% |
| banlist12/ko/post/early @ moderation-ko-post-early | 145 | −2% (−5 … +3) ~ | 0% (−2 … +2) ~ | 0% |
| banlist12/ko/thread/clean @ moderation-ko-thread-clean | 894,674 | −3% (−3 … −3) | −6% (−6 … −6) layout? | 0% |
| banlist12/emoji/comment/clean @ moderation-emoji-comment-clean | 1,797 | 0% (0 … +11) ~ | +2% (0 … +5) | 0% |
| banlist12/emoji/post/clean @ moderation-emoji-post-clean | 12,684 | −10% (−10 … −9) | −9% (−10 … −4) | −6% … −2% |
| banlist12/emoji/post/early @ moderation-emoji-post-early | 141 | +5% (−1 … +6) | −1% (−3 … 0) ~ | 0% |
| banlist12/emoji/thread/clean @ moderation-emoji-thread-clean | 728,138 | −7% (−8 … −7) layout? | −8% (−8 … −8) layout? | 0% |
| explode/pipe2/short @ delimiter-pipe2-short | 390 | −1% (−1 … 0) | −1% (−2 … +1) | 0% |
| explode/pipe2/4k @ delimiter-pipe2-4k | 11,540 | +1% (−1 … +3) | 0% (−5 … +6) ~ | 0% |
| explode/pipe2/64k @ delimiter-pipe2-64k | 207,185 | −1% (−1 … +2) | 0% (−3 … +1) ~ | 0% |
| explode/colon2/short @ delimiter-colon2-short | 457 | 0% (−1 … +3) ~ | −1% (−2 … +1) | 0% |
| explode/colon2/4k @ delimiter-colon2-4k | 11,638 | 0% (0 … +1) ~ | 0% (−1 … +2) ~ | 0% |
| explode/colon2/64k @ delimiter-colon2-64k | 204,678 | 0% (0 … +1) ~ | −1% (−2 … +1) ~ | 0% |
| explode/crlf/short @ delimiter-crlf-short | 516 | 0% (−2 … 0) | −1% (−4 … +2) | 0% |
| explode/crlf/4k @ delimiter-crlf-4k | 11,287 | 0% (−2 … +7) ~ | −1% (−6 … +1) ~ | 0% |
| explode/crlf/64k @ delimiter-crlf-64k | 206,168 | +1% (0 … +3) | +1% (−1 … +1) | 0% |
| explode/comma/short @ delimiter-comma-short | 425 | 0% (−1 … +4) ~ | 0% (−2 … +1) ~ | 0% |
| explode/comma/4k @ delimiter-comma-4k | 10,048 | 0% (−2 … +4) ~ | +1% (−1 … +6) ~ | 0% |
| explode/comma/64k @ delimiter-comma-64k | 173,725 | +1% (−2 … +3) | −1% (−1 … +2) | 0% |
| parse-records/4k @ records-4k | 43,247 | −1% (−1 … 0) | +1% (0 … +3) | 0% |
| parse-query/4k @ query-4k | 117,786 | 0% (0 … +2) | 0% (−1 … +1) | 0% |
| parse-http/small @ http-small | 3,793 | +2% (+1 … +3) | −2% (−3 … −1) | 0% |
| parse-http/body64k @ http-body64k | 3,799 | +2% (0 … +3) | −2% (−17 … −1) | 0% |
| scan-template/4k @ template-4k | 20,654 | 0% (0 … +2) ~ | 0% (−1 … +4) ~ | 0% |
| render-template/4k @ template-4k | 32,819 | −15% (−15 … −14) | −14% (−16 … −14) | −18% … −7% |
| log-contains/event/post/early @ logs-post-early | 123 | −26% (−29 … −24) | −13% (−21 … −11) | −25% … −10% |
| log-contains/level/post/early @ logs-post-early | 140 | −22% (−25 … −21) | −26% (−27 … −17) | −24% … −10% |
| log-contains/event/thread/clean @ logs-thread-clean | 63,244 | −8% (−8 … −8) layout? | −8% (−8 … −7) layout? | 0% |
| log-filter/thread/clean @ logs-thread-clean | 195,199 | +1% (−3 … +2) ~ | 0% (−1 … +2) ~ | 0% |
| log-contains/event/thread/early @ logs-thread-early | 124 | −25% (−27 … −18) | −17% (−20 … −11) | −25% … −10% |
| log-contains/level/thread/early @ logs-thread-early | 140 | −22% (−25 … −10) | −26% (−31 … −17) | −24% … −10% |
| log-contains/event/thread/late @ logs-thread-late | 63,137 | −8% (−8 … −7) layout? | −8% (−8 … −7) layout? | 0% |
| log-filter/thread/late @ logs-thread-late | 195,092 | 0% (0 … +2) ~ | −1% (−1 … +1) ~ | 0% |

Control: Stock against itself.

Absolute cycles/call: Stock with GCC 15.2.

| call | Stock cycles | A/A start | A/A end |
|---|--:|--:|--:|
| banlist12/en/comment/clean @ moderation-en-comment-clean | 2,289 | 0% (−1 … +2) | 0% (−2 … +2) |
| banlist12/en/comment/early @ moderation-en-comment-early | 146 | −3% (−5 … +3) | +1% (−5 … +8) |
| banlist12/en/comment/late @ moderation-en-comment-late | 2,539 | 0% (−3 … 0) | 0% (−3 … +1) |
| banlist12/en/post/clean @ moderation-en-post-clean | 14,020 | 0% (0 … 0) | −1% (−1 … +1) |
| banlist12/en/post/early @ moderation-en-post-early | 146 | +1% (−7 … +3) | +3% (−6 … +5) |
| banlist12/en/post/late @ moderation-en-post-late | 14,283 | 0% (0 … 0) | 0% (−2 … 0) |
| banlist12/en/thread/clean @ moderation-en-thread-clean | 810,692 | 0% (−1 … 0) | 0% (0 … 0) |
| banlist12/en/thread/early @ moderation-en-thread-early | 141 | +1% (−5 … +6) | −2% (−6 … −1) |
| banlist12/en/thread/late @ moderation-en-thread-late | 811,493 | 0% (0 … +1) | 0% (0 … 0) |
| banlist12/ru/comment/clean @ moderation-ru-comment-clean | 11,852 | 0% (0 … +1) | 0% (0 … +1) |
| banlist12/ru/comment/early @ moderation-ru-comment-early | 146 | +1% (−1 … +7) | −1% (−4 … +3) |
| banlist12/ru/comment/late @ moderation-ru-comment-late | 12,802 | 0% (0 … 0) | 0% (0 … 0) |
| banlist12/ru/post/clean @ moderation-ru-post-clean | 14,354 | 0% (−1 … +1) | 0% (0 … 0) |
| banlist12/ru/post/early @ moderation-ru-post-early | 145 | −3% (−8 … +4) | +2% (−7 … +9) |
| banlist12/ru/post/late @ moderation-ru-post-late | 15,002 | 0% (−1 … +1) | 0% (0 … 0) |
| banlist12/ru/thread/clean @ moderation-ru-thread-clean | 1,040,829 | 0% (0 … 0) | 0% (0 … 0) |
| banlist12/ru/thread/early @ moderation-ru-thread-early | 145 | −1% (−9 … +6) | −5% (−6 … 0) |
| banlist12/ru/thread/late @ moderation-ru-thread-late | 1,021,823 | 0% (−1 … 0) | 0% (0 … +1) |
| banlist12/es/comment/clean @ moderation-es-comment-clean | 2,617 | +1% (0 … +2) | 0% (−1 … +1) |
| banlist12/es/post/clean @ moderation-es-post-clean | 13,453 | 0% (−1 … 0) | 0% (−1 … 0) |
| banlist12/es/post/early @ moderation-es-post-early | 148 | 0% (−5 … +12) | +2% (−8 … +11) |
| banlist12/es/thread/clean @ moderation-es-thread-clean | 834,455 | 0% (0 … +1) | 0% (−1 … 0) |
| banlist12/ar/comment/clean @ moderation-ar-comment-clean | 9,662 | 0% (0 … +1) | 0% (−2 … 0) |
| banlist12/ar/comment/late @ moderation-ar-comment-late | 10,925 | 0% (0 … +4) | 0% (0 … 0) |
| banlist12/ar/post/clean @ moderation-ar-post-clean | 18,573 | 0% (0 … +1) | 0% (0 … +1) |
| banlist12/ar/post/early @ moderation-ar-post-early | 147 | +1% (−10 … +7) | 0% (−3 … +6) |
| banlist12/ar/thread/clean @ moderation-ar-thread-clean | 1,230,619 | 0% (0 … 0) | 0% (0 … 0) |
| banlist12/hi/comment/clean @ moderation-hi-comment-clean | 13,710 | 0% (0 … 0) | 0% (−1 … 0) |
| banlist12/hi/comment/late @ moderation-hi-comment-late | 15,846 | 0% (0 … +1) | 0% (0 … +1) |
| banlist12/hi/post/clean @ moderation-hi-post-clean | 12,475 | 0% (0 … 0) | 0% (0 … +5) |
| banlist12/hi/post/early @ moderation-hi-post-early | 193 | +2% (−3 … +6) | 0% (0 … +5) |
| banlist12/hi/thread/clean @ moderation-hi-thread-clean | 846,619 | 0% (−1 … 0) | 0% (0 … 0) |
| banlist12/hi/thread/late @ moderation-hi-thread-late | 858,375 | 0% (0 … 0) | 0% (0 … 0) |
| banlist12/zh/comment/clean @ moderation-zh-comment-clean | 2,550 | 0% (−1 … +1) | 0% (0 … +1) |
| banlist12/zh/post/clean @ moderation-zh-post-clean | 10,925 | 0% (0 … +3) | 0% (−1 … 0) |
| banlist12/zh/post/early @ moderation-zh-post-early | 193 | −3% (−6 … +5) | −1% (−3 … +3) |
| banlist12/zh/thread/clean @ moderation-zh-thread-clean | 707,995 | 0% (−1 … 0) | 0% (0 … 0) |
| banlist12/ja/comment/clean @ moderation-ja-comment-clean | 6,355 | 0% (−1 … 0) | 0% (−1 … 0) |
| banlist12/ja/comment/late @ moderation-ja-comment-late | 7,187 | 0% (0 … 0) | −1% (−2 … 0) |
| banlist12/ja/post/clean @ moderation-ja-post-clean | 15,422 | 0% (0 … 0) | 0% (0 … 0) |
| banlist12/ja/post/early @ moderation-ja-post-early | 187 | 0% (−3 … +5) | +1% (−3 … +4) |
| banlist12/ja/thread/clean @ moderation-ja-thread-clean | 1,037,203 | 0% (0 … 0) | 0% (−1 … 0) |
| banlist12/ko/comment/clean @ moderation-ko-comment-clean | 4,584 | 0% (−1 … +1) | 0% (−1 … +2) |
| banlist12/ko/post/clean @ moderation-ko-post-clean | 14,549 | 0% (−1 … 0) | 0% (−1 … +1) |
| banlist12/ko/post/early @ moderation-ko-post-early | 140 | +6% (−2 … +7) | +7% (−10 … +8) |
| banlist12/ko/thread/clean @ moderation-ko-thread-clean | 893,301 | 0% (0 … 0) | 0% (0 … 0) |
| banlist12/emoji/comment/clean @ moderation-emoji-comment-clean | 1,797 | 0% (0 … +3) | +1% (0 … +6) |
| banlist12/emoji/post/clean @ moderation-emoji-post-clean | 12,655 | 0% (0 … +1) | 0% (0 … 0) |
| banlist12/emoji/post/early @ moderation-emoji-post-early | 141 | +1% (−5 … +7) | +3% (−3 … +6) |
| banlist12/emoji/thread/clean @ moderation-emoji-thread-clean | 727,673 | 0% (0 … 0) | 0% (0 … +1) |
| explode/pipe2/short @ delimiter-pipe2-short | 389 | 0% (−1 … 0) | 0% (−1 … 0) |
| explode/pipe2/4k @ delimiter-pipe2-4k | 11,535 | +1% (−1 … +3) | 0% (−1 … +2) |
| explode/pipe2/64k @ delimiter-pipe2-64k | 206,230 | 0% (−1 … 0) | 0% (−1 … +10) |
| explode/colon2/short @ delimiter-colon2-short | 458 | 0% (−14 … +1) | 0% (0 … +6) |
| explode/colon2/4k @ delimiter-colon2-4k | 11,550 | +1% (−2 … +1) | 0% (−2 … 0) |
| explode/colon2/64k @ delimiter-colon2-64k | 203,666 | +1% (0 … +1) | 0% (−1 … +1) |
| explode/crlf/short @ delimiter-crlf-short | 515 | 0% (0 … +2) | 0% (−1 … 0) |
| explode/crlf/4k @ delimiter-crlf-4k | 11,256 | 0% (−2 … 0) | +1% (0 … +2) |
| explode/crlf/64k @ delimiter-crlf-64k | 205,663 | 0% (−1 … +1) | 0% (−2 … +4) |
| explode/comma/short @ delimiter-comma-short | 423 | 0% (−1 … 0) | 0% (0 … +2) |
| explode/comma/4k @ delimiter-comma-4k | 9,971 | +1% (−3 … +5) | 0% (−3 … +3) |
| explode/comma/64k @ delimiter-comma-64k | 173,555 | 0% (−26 … +3) | +1% (0 … +4) |
| parse-records/4k @ records-4k | 43,389 | −1% (−1 … +1) | −1% (−1 … +1) |
| parse-query/4k @ query-4k | 118,637 | 0% (−5 … +3) | 0% (−1 … 0) |
| parse-http/small @ http-small | 3,792 | +1% (−2 … +2) | +1% (0 … +1) |
| parse-http/body64k @ http-body64k | 3,775 | +1% (0 … +1) | 0% (−1 … +2) |
| scan-template/4k @ template-4k | 20,590 | +1% (0 … +2) | 0% (−2 … +2) |
| render-template/4k @ template-4k | 32,757 | 0% (−1 … +1) | 0% (−1 … 0) |
| log-contains/event/post/early @ logs-post-early | 126 | −3% (−3 … +2) | +1% (−1 … +3) |
| log-contains/level/post/early @ logs-post-early | 140 | 0% (−1 … 0) | 0% (0 … 0) |
| log-contains/event/thread/clean @ logs-thread-clean | 63,165 | 0% (0 … 0) | 0% (0 … +1) |
| log-filter/thread/clean @ logs-thread-clean | 195,789 | −1% (−3 … +2) | 0% (−2 … +1) |
| log-contains/event/thread/early @ logs-thread-early | 123 | 0% (−1 … +1) | +1% (0 … +3) |
| log-contains/level/thread/early @ logs-thread-early | 140 | 0% (0 … 0) | 0% (0 … +5) |
| log-contains/event/thread/late @ logs-thread-late | 63,097 | 0% (0 … 0) | 0% (−1 … +1) |
| log-filter/thread/late @ logs-thread-late | 192,781 | 0% (−2 … +2) | +2% (−3 … +2) |

~: the change is not larger than the A/A control of the same row: not evidence of a difference.

layout?: in every pass the cycles changed in the same direction, by 3% or more in the median, the instructions by less than 0.5%: the work is the same, so look for the cause (code placement, branch prediction) with `bench why` before reporting the row.
<!-- /bench-table -->

## Quiet Intel

<!-- bench-table ../data/intel/control-cycles.json --full --compact-header --base-name Stock -->
Absolute cycles/call: Stock with GCC 13.3.

| call | Stock cycles | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | Δ instr. |
|---|--:|--:|--:|--:|--:|--:|
| banlist12/en/comment/clean @ moderation-en-comment-clean | 1,885 | 0% (−2 … 0) ~ | 0% (0 … 0) ~ | 0% (−1 … 0) ~ | 0% (0 … 0) ~ | 0% |
| banlist12/en/comment/early @ moderation-en-comment-early | 115 | 0% (−1 … 0) ~ | 0% (0 … +1) ~ | −2% (−5 … −1) | 0% (−2 … +2) ~ | 0% |
| banlist12/en/comment/late @ moderation-en-comment-late | 2,069 | 0% (−1 … 0) | −1% (−1 … −1) | −1% (−1 … +1) | +1% (0 … +1) | 0% |
| banlist12/en/post/clean @ moderation-en-post-clean | 13,299 | −7% (−9 … −6) | −2% (−3 … −2) | 0% (0 … 0) ~ | −6% (−7 … −6) | −10% … −6% |
| banlist12/en/post/early @ moderation-en-post-early | 113 | −1% (−2 … 0) ~ | +1% (0 … +1) ~ | 0% (0 … +1) ~ | 0% (−2 … 0) ~ | 0% |
| banlist12/en/post/late @ moderation-en-post-late | 13,440 | −6% (−6 … −5) | −2% (−4 … −2) | 0% (0 … 0) ~ | −5% (−5 … −5) | −10% … −6% |
| banlist12/en/thread/clean @ moderation-en-thread-clean | 840,463 | −1% (−1 … 0) ~ | +1% (0 … +3) ~ | −3% (−3 … −3) | +3% (+3 … +3) | −10% … 0% |
| banlist12/en/thread/early @ moderation-en-thread-early | 111 | +1% (0 … +3) | 0% (0 … +1) ~ | 0% (−1 … +1) ~ | −1% (−2 … 0) | 0% |
| banlist12/en/thread/late @ moderation-en-thread-late | 843,968 | −1% (−7 … −1) ~ | −5% (−12 … +15) | −3% (−4 … −3) | −4% (−10 … +4) | −10% … 0% |
| banlist12/ru/comment/clean @ moderation-ru-comment-clean | 11,698 | 0% (−1 … +1) | 0% (0 … 0) ~ | 0% (0 … 0) | 0% (0 … +1) | 0% |
| banlist12/ru/comment/early @ moderation-ru-comment-early | 112 | 0% (−1 … +1) ~ | 0% (−1 … 0) ~ | −1% (−3 … +2) ~ | −1% (−2 … 0) ~ | 0% |
| banlist12/ru/comment/late @ moderation-ru-comment-late | 12,825 | +1% (−1 … +2) | 0% (−3 … 0) ~ | 0% (0 … 0) | 0% (0 … 0) | 0% |
| banlist12/ru/post/clean @ moderation-ru-post-clean | 13,675 | −3% (−4 … −2) | −3% (−3 … −2) | −3% (−3 … −2) | −2% (−3 … −2) | −9% … −3% |
| banlist12/ru/post/early @ moderation-ru-post-early | 113 | −1% (−5 … 0) | 0% (−1 … 0) | −1% (−2 … +1) | 0% (−1 … +1) | 0% |
| banlist12/ru/post/late @ moderation-ru-post-late | 14,379 | −3% (−4 … −2) | −3% (−4 … −3) | −3% (−3 … −3) | −2% (−3 … −1) | −9% … −3% |
| banlist12/ru/thread/clean @ moderation-ru-thread-clean | 1,145,533 | +3% (+2 … +3) | −2% (−4 … +1) ~ | −2% (−2 … −2) ~ | +1% (0 … +4) ~ | −5% … 0% |
| banlist12/ru/thread/early @ moderation-ru-thread-early | 112 | 0% (−1 … +1) ~ | +1% (0 … +1) ~ | −2% (−3 … +1) | 0% (−1 … +1) ~ | 0% |
| banlist12/ru/thread/late @ moderation-ru-thread-late | 1,154,598 | +3% (+2 … +6) | −2% (−3 … −1) | −2% (−2 … −1) | +1% (0 … +1) ~ | −5% … 0% |
| banlist12/es/comment/clean @ moderation-es-comment-clean | 2,161 | 0% (−2 … +1) ~ | 0% (0 … 0) ~ | 0% (0 … +42) | −1% (−1 … −1) | 0% |
| banlist12/es/post/clean @ moderation-es-post-clean | 12,473 | −4% (−5 … −3) | −5% (−8 … −3) | −6% (−6 … −5) | −2% (−3 … −2) | −10% … −6% |
| banlist12/es/post/early @ moderation-es-post-early | 112 | 0% (0 … 0) | +1% (0 … +1) | −3% (−3 … 0) | 0% (0 … +13) ~ | 0% |
| banlist12/es/thread/clean @ moderation-es-thread-clean | 861,311 | 0% (−2 … +1) ~ | +1% (0 … +2) ~ | −3% (−4 … −3) | +4% (+4 … +7) | −10% … 0% |
| banlist12/ar/comment/clean @ moderation-ar-comment-clean | 9,575 | +1% (0 … +1) ~ | 0% (0 … 0) ~ | 0% (−1 … 0) ~ | 0% (0 … 0) ~ | 0% |
| banlist12/ar/comment/late @ moderation-ar-comment-late | 10,949 | 0% (0 … 0) ~ | 0% (0 … 0) ~ | 0% (0 … 0) ~ | 0% (0 … 0) ~ | 0% |
| banlist12/ar/post/clean @ moderation-ar-post-clean | 18,645 | −3% (−3 … −2) | −2% (−3 … −2) | −2% (−7 … −1) | −2% (−2 … −2) | −6% … −4% |
| banlist12/ar/post/early @ moderation-ar-post-early | 112 | +1% (0 … +3) ~ | 0% (−1 … 0) ~ | 0% (−4 … +3) ~ | 0% (−1 … 0) ~ | 0% |
| banlist12/ar/thread/clean @ moderation-ar-thread-clean | 1,379,040 | +4% (+2 … +6) layout? | +2% (+1 … +2) | +1% (−4 … +2) | +3% (+1 … +4) | −5% … 0% |
| banlist12/hi/comment/clean @ moderation-hi-comment-clean | 13,960 | 0% (0 … 0) ~ | 0% (0 … 0) ~ | 0% (0 … 0) ~ | 0% (0 … +1) ~ | 0% |
| banlist12/hi/comment/late @ moderation-hi-comment-late | 16,031 | 0% (0 … +2) ~ | 0% (0 … 0) ~ | 0% (0 … 0) ~ | 0% (0 … 0) ~ | 0% |
| banlist12/hi/post/clean @ moderation-hi-post-clean | 11,869 | −3% (−3 … −3) | −3% (−4 … −1) | −4% (−4 … −4) | −2% (−2 … +4) | −11% … −5% |
| banlist12/hi/post/early @ moderation-hi-post-early | 192 | −12% (−13 … −12) | −17% (−17 … −16) | −10% (−11 … −9) | −5% (−6 … −2) | −16% … −5% |
| banlist12/hi/thread/clean @ moderation-hi-thread-clean | 989,592 | −1% (−5 … 0) ~ | +1% (0 … +1) ~ | −1% (−2 … +9) ~ | +2% (+1 … +3) ~ | −8% … 0% |
| banlist12/hi/thread/late @ moderation-hi-thread-late | 1,006,425 | −1% (−10 … +2) | 0% (0 … +8) | −1% (−10 … +9) | +4% (+2 … +7) | −8% … 0% |
| banlist12/zh/comment/clean @ moderation-zh-comment-clean | 2,148 | −1% (−1 … −1) | 0% (0 … +4) ~ | 0% (0 … 0) ~ | 0% (0 … +2) ~ | 0% |
| banlist12/zh/post/clean @ moderation-zh-post-clean | 9,943 | −6% (−6 … −6) | −4% (−6 … −4) | −8% (−8 … −8) | −3% (−3 … −3) | −11% … −8% |
| banlist12/zh/post/early @ moderation-zh-post-early | 182 | −17% (−17 … −16) | −18% (−18 … −17) | −6% (−7 … −6) | −3% (−4 … −2) | −17% … −6% |
| banlist12/zh/thread/clean @ moderation-zh-thread-clean | 857,139 | −1% (−12 … +14) | +3% (+1 … +16) layout? | −2% (−2 … +10) | +5% (−2 … +5) | −11% … 0% |
| banlist12/ja/comment/clean @ moderation-ja-comment-clean | 6,397 | 0% (0 … 0) ~ | 0% (0 … 0) ~ | 0% (0 … 0) ~ | 0% (0 … 0) ~ | 0% |
| banlist12/ja/comment/late @ moderation-ja-comment-late | 7,037 | 0% (0 … 0) ~ | 0% (−1 … 0) ~ | 0% (0 … 0) ~ | 0% (0 … 0) ~ | 0% |
| banlist12/ja/post/clean @ moderation-ja-post-clean | 14,955 | −3% (−4 … −3) | −4% (−6 … −2) | −5% (−5 … −5) | −3% (−3 … −3) | −8% … −5% |
| banlist12/ja/post/early @ moderation-ja-post-early | 172 | −16% (−17 … −15) | −19% (−19 … −19) | −3% (−5 … −1) | −10% (−12 … −10) | −18% … −6% |
| banlist12/ja/thread/clean @ moderation-ja-thread-clean | 1,137,578 | +2% (+2 … +3) ~ | +8% (0 … +11) | +1% (0 … +2) ~ | 0% (0 … 0) ~ | −8% … 0% |
| banlist12/ko/comment/clean @ moderation-ko-comment-clean | 3,793 | +1% (0 … +2) | 0% (−1 … 0) | 0% (0 … 0) ~ | 0% (0 … 0) ~ | 0% |
| banlist12/ko/post/clean @ moderation-ko-post-clean | 14,533 | −5% (−5 … −4) | −2% (−3 … 0) | −3% (−4 … −3) | −2% (−2 … −1) | −8% … −5% |
| banlist12/ko/post/early @ moderation-ko-post-early | 113 | 0% (0 … +1) ~ | 0% (0 … 0) ~ | −2% (−2 … +2) | +1% (0 … +1) ~ | 0% |
| banlist12/ko/thread/clean @ moderation-ko-thread-clean | 968,273 | +2% (+2 … +2) | 0% (−3 … +3) ~ | −1% (−1 … −1) ~ | +3% (+3 … +4) | −7% … 0% |
| banlist12/emoji/comment/clean @ moderation-emoji-comment-clean | 1,421 | 0% (−1 … +1) | 0% (−1 … +1) | 0% (0 … +1) ~ | 0% (−1 … +2) | 0% |
| banlist12/emoji/post/clean @ moderation-emoji-post-clean | 11,949 | −2% (−2 … −2) | −3% (−3 … −2) | −6% (−7 … −6) | −3% (−4 … −3) | −10% … −6% |
| banlist12/emoji/post/early @ moderation-emoji-post-early | 113 | +1% (−1 … +1) | 0% (0 … 0) ~ | 0% (−1 … +1) ~ | 0% (0 … +1) ~ | 0% |
| banlist12/emoji/thread/clean @ moderation-emoji-thread-clean | 755,177 | 0% (−9 … +13) ~ | −2% (−3 … 0) ~ | −2% (−2 … +13) ~ | +3% (+2 … +3) | −10% … 0% |
| explode/pipe2/short @ delimiter-pipe2-short | 325 | −1% (−1 … 0) ~ | 0% (−1 … +3) ~ | 0% (0 … +1) ~ | 0% (−1 … 0) ~ | 0% |
| explode/pipe2/4k @ delimiter-pipe2-4k | 9,489 | +1% (−2 … +1) ~ | −2% (−3 … +3) ~ | −1% (−2 … 0) ~ | −4% (−4 … 0) layout? | 0% |
| explode/pipe2/64k @ delimiter-pipe2-64k | 190,968 | −1% (−3 … 0) ~ | +1% (−2 … +2) ~ | −1% (−5 … 0) ~ | 0% (0 … +1) ~ | 0% |
| explode/colon2/short @ delimiter-colon2-short | 381 | −1% (−1 … 0) | 0% (−1 … +1) ~ | +1% (−1 … +4) | +1% (−1 … +2) | 0% |
| explode/colon2/4k @ delimiter-colon2-4k | 9,238 | 0% (−5 … +4) ~ | +1% (−4 … +4) ~ | 0% (−2 … +1) ~ | +1% (0 … +1) ~ | 0% |
| explode/colon2/64k @ delimiter-colon2-64k | 187,947 | 0% (−1 … +1) ~ | +1% (0 … +6) ~ | +1% (−1 … +1) ~ | 0% (0 … +3) ~ | 0% |
| explode/crlf/short @ delimiter-crlf-short | 427 | 0% (−1 … 0) ~ | −1% (−1 … −1) | 0% (−2 … +1) ~ | 0% (−1 … +1) ~ | 0% |
| explode/crlf/4k @ delimiter-crlf-4k | 9,223 | +1% (+1 … +2) | −2% (−2 … +1) | 0% (−1 … +1) ~ | 0% (−6 … +2) ~ | 0% |
| explode/crlf/64k @ delimiter-crlf-64k | 186,874 | −1% (−1 … 0) ~ | +1% (0 … +2) ~ | 0% (−13 … +5) ~ | −4% (−5 … +3) | 0% |
| explode/comma/short @ delimiter-comma-short | 334 | 0% (−2 … 0) ~ | 0% (−1 … 0) ~ | +4% (+1 … +14) layout? | +1% (+1 … +2) ~ | 0% |
| explode/comma/4k @ delimiter-comma-4k | 8,084 | −3% (−14 … 0) | +3% (0 … +4) | −2% (−6 … +24) ~ | +2% (−7 … +12) ~ | 0% |
| explode/comma/64k @ delimiter-comma-64k | 156,814 | −1% (−1 … +1) ~ | 0% (−1 … 0) ~ | 0% (−1 … +1) ~ | 0% (−1 … +1) ~ | 0% |
| parse-records/4k @ records-4k | 36,772 | −1% (−2 … 0) ~ | +2% (0 … +3) | +1% (0 … +2) ~ | −1% (−2 … +1) ~ | 0% |
| parse-query/4k @ query-4k | 96,493 | 0% (−1 … +1) ~ | 0% (−1 … +1) | 0% (−3 … 0) ~ | +1% (0 … +2) | 0% |
| parse-http/small @ http-small | 3,084 | +1% (+1 … +3) | −1% (−1 … −1) | −1% (−2 … 0) | +1% (0 … +2) | 0% |
| parse-http/body64k @ http-body64k | 3,101 | +1% (0 … +2) | 0% (−2 … +2) | +1% (−4 … +3) | +1% (+1 … +1) | 0% |
| scan-template/4k @ template-4k | 16,116 | 0% (−1 … 0) | 0% (−1 … 0) | 0% (−1 … +1) ~ | +1% (−1 … +2) | 0% |
| render-template/4k @ template-4k | 28,885 | −16% (−17 … −16) | −11% (−14 … −11) | −8% (−9 … −6) | −3% (−5 … −3) | −18% … −12% |
| log-contains/event/post/early @ logs-post-early | 136 | −27% (−27 … −27) | −21% (−24 … −18) | −5% (−6 … −5) | −9% (−10 … −8) | −25% … −12% |
| log-contains/level/post/early @ logs-post-early | 147 | −24% (−24 … −23) | −21% (−23 … −17) | −4% (−5 … +12) | −5% (−5 … −4) | −24% … −12% |
| log-contains/event/thread/clean @ logs-thread-clean | 72,698 | −11% (−13 … +9) | −2% (−4 … +2) | +7% (−2 … +8) | −1% (−5 … +6) | −9% … 0% |
| log-filter/thread/clean @ logs-thread-clean | 210,867 | +1% (−1 … +1) ~ | −4% (−4 … −3) layout? | +1% (0 … +3) ~ | −1% (−2 … +9) ~ | 0% |
| log-contains/event/thread/early @ logs-thread-early | 136 | −27% (−27 … −26) | −24% (−26 … −24) | −5% (−7 … −4) | −10% (−10 … −9) | −25% … −12% |
| log-contains/level/thread/early @ logs-thread-early | 148 | −24% (−24 … −24) | −20% (−21 … −18) | −4% (−4 … −4) | −6% (−7 … −6) | −24% … −12% |
| log-contains/event/thread/late @ logs-thread-late | 64,502 | +4% (−9 … +7) | +9% (−12 … +11) | +5% (0 … +14) | −2% (−4 … −1) | −9% … 0% |
| log-filter/thread/late @ logs-thread-late | 210,746 | 0% (−1 … 0) ~ | 0% (−1 … 0) ~ | 0% (−1 … 0) ~ | −2% (−4 … +2) | 0% |

Control: Stock against itself.

Absolute cycles/call: Stock with GCC 13.3.

| call | Stock cycles | A/A start | A/A end |
|---|--:|--:|--:|
| banlist12/en/comment/clean @ moderation-en-comment-clean | 1,902 | 0% (−1 … +3) | 0% (0 … 0) |
| banlist12/en/comment/early @ moderation-en-comment-early | 118 | −2% (−3 … −1) | −1% (−2 … +1) |
| banlist12/en/comment/late @ moderation-en-comment-late | 2,062 | 0% (0 … +1) | 0% (−1 … 0) |
| banlist12/en/post/clean @ moderation-en-post-clean | 13,214 | +1% (0 … +1) | 0% (0 … 0) |
| banlist12/en/post/early @ moderation-en-post-early | 112 | +2% (+1 … +2) | 0% (0 … +1) |
| banlist12/en/post/late @ moderation-en-post-late | 13,306 | 0% (−3 … +1) | 0% (0 … 0) |
| banlist12/en/thread/clean @ moderation-en-thread-clean | 862,796 | +1% (−13 … +12) | +1% (0 … +1) |
| banlist12/en/thread/early @ moderation-en-thread-early | 112 | 0% (0 … +2) | 0% (−2 … +2) |
| banlist12/en/thread/late @ moderation-en-thread-late | 842,650 | +2% (0 … +8) | 0% (−13 … 0) |
| banlist12/ru/comment/clean @ moderation-ru-comment-clean | 11,707 | 0% (−1 … +1) | 0% (0 … 0) |
| banlist12/ru/comment/early @ moderation-ru-comment-early | 114 | +3% (−5 … +12) | 0% (−1 … 0) |
| banlist12/ru/comment/late @ moderation-ru-comment-late | 12,838 | 0% (−1 … 0) | 0% (0 … 0) |
| banlist12/ru/post/clean @ moderation-ru-post-clean | 13,645 | 0% (0 … +2) | 0% (−1 … 0) |
| banlist12/ru/post/early @ moderation-ru-post-early | 112 | 0% (−1 … +1) | 0% (0 … +2) |
| banlist12/ru/post/late @ moderation-ru-post-late | 14,339 | 0% (0 … +1) | 0% (0 … +1) |
| banlist12/ru/thread/clean @ moderation-ru-thread-clean | 1,174,006 | −3% (−8 … −1) | +2% (0 … +5) |
| banlist12/ru/thread/early @ moderation-ru-thread-early | 113 | −1% (−2 … 0) | −1% (−2 … +1) |
| banlist12/ru/thread/late @ moderation-ru-thread-late | 1,152,446 | −1% (−6 … 0) | 0% (0 … +6) |
| banlist12/es/comment/clean @ moderation-es-comment-clean | 2,154 | 0% (−1 … +1) | 0% (0 … 0) |
| banlist12/es/post/clean @ moderation-es-post-clean | 12,546 | 0% (0 … 0) | 0% (0 … +1) |
| banlist12/es/post/early @ moderation-es-post-early | 113 | 0% (−2 … +2) | 0% (0 … +3) |
| banlist12/es/thread/clean @ moderation-es-thread-clean | 865,283 | −1% (−2 … 0) | 0% (0 … +1) |
| banlist12/ar/comment/clean @ moderation-ar-comment-clean | 9,560 | +1% (0 … +1) | 0% (0 … +1) |
| banlist12/ar/comment/late @ moderation-ar-comment-late | 10,856 | +1% (0 … +1) | 0% (0 … 0) |
| banlist12/ar/post/clean @ moderation-ar-post-clean | 18,657 | 0% (−1 … 0) | 0% (0 … 0) |
| banlist12/ar/post/early @ moderation-ar-post-early | 113 | −1% (−1 … +3) | +1% (−1 … +1) |
| banlist12/ar/thread/clean @ moderation-ar-thread-clean | 1,367,501 | +1% (0 … +7) | +1% (0 … +8) |
| banlist12/hi/comment/clean @ moderation-hi-comment-clean | 13,891 | +1% (0 … +1) | 0% (−1 … 0) |
| banlist12/hi/comment/late @ moderation-hi-comment-late | 16,057 | 0% (0 … 0) | +1% (0 … +2) |
| banlist12/hi/post/clean @ moderation-hi-post-clean | 11,845 | +1% (−2 … +2) | 0% (0 … +1) |
| banlist12/hi/post/early @ moderation-hi-post-early | 193 | +1% (0 … +2) | 0% (−2 … +1) |
| banlist12/hi/thread/clean @ moderation-hi-thread-clean | 986,380 | 0% (−10 … +1) | +3% (−9 … +9) |
| banlist12/hi/thread/late @ moderation-hi-thread-late | 978,857 | 0% (0 … +1) | 0% (0 … +1) |
| banlist12/zh/comment/clean @ moderation-zh-comment-clean | 2,128 | 0% (0 … +2) | 0% (−1 … +1) |
| banlist12/zh/post/clean @ moderation-zh-post-clean | 9,912 | +1% (0 … +1) | 0% (0 … 0) |
| banlist12/zh/post/early @ moderation-zh-post-early | 181 | 0% (−1 … 0) | 0% (0 … +2) |
| banlist12/zh/thread/clean @ moderation-zh-thread-clean | 758,216 | 0% (−1 … 0) | 0% (−1 … +5) |
| banlist12/ja/comment/clean @ moderation-ja-comment-clean | 6,403 | 0% (−1 … +1) | 0% (−11 … 0) |
| banlist12/ja/comment/late @ moderation-ja-comment-late | 7,081 | −1% (−1 … 0) | 0% (−1 … 0) |
| banlist12/ja/post/clean @ moderation-ja-post-clean | 14,991 | −1% (−1 … −1) | 0% (0 … 0) |
| banlist12/ja/post/early @ moderation-ja-post-early | 172 | 0% (−1 … 0) | 0% (−1 … +1) |
| banlist12/ja/thread/clean @ moderation-ja-thread-clean | 1,135,081 | +2% (0 … +11) | 0% (−1 … 0) |
| banlist12/ko/comment/clean @ moderation-ko-comment-clean | 3,779 | 0% (−1 … +2) | 0% (−1 … +1) |
| banlist12/ko/post/clean @ moderation-ko-post-clean | 14,484 | 0% (−2 … 0) | 0% (0 … +1) |
| banlist12/ko/post/early @ moderation-ko-post-early | 111 | +2% (0 … +2) | 0% (−1 … +1) |
| banlist12/ko/thread/clean @ moderation-ko-thread-clean | 971,061 | −1% (−11 … 0) | −1% (−3 … 0) |
| banlist12/emoji/comment/clean @ moderation-emoji-comment-clean | 1,410 | 0% (−1 … +1) | 0% (−1 … 0) |
| banlist12/emoji/post/clean @ moderation-emoji-post-clean | 11,947 | 0% (−1 … +1) | 0% (0 … 0) |
| banlist12/emoji/post/early @ moderation-emoji-post-early | 113 | −1% (−2 … 0) | 0% (−1 … +1) |
| banlist12/emoji/thread/clean @ moderation-emoji-thread-clean | 756,935 | +2% (0 … +5) | 0% (0 … 0) |
| explode/pipe2/short @ delimiter-pipe2-short | 328 | −1% (−1 … 0) | 0% (0 … +1) |
| explode/pipe2/4k @ delimiter-pipe2-4k | 9,505 | +3% (−3 … +4) | +1% (−1 … +5) |
| explode/pipe2/64k @ delimiter-pipe2-64k | 196,094 | −2% (−4 … −1) | −1% (−3 … +2) |
| explode/colon2/short @ delimiter-colon2-short | 378 | +1% (0 … +1) | −1% (−1 … 0) |
| explode/colon2/4k @ delimiter-colon2-4k | 9,197 | 0% (0 … +4) | −2% (−3 … 0) |
| explode/colon2/64k @ delimiter-colon2-64k | 190,770 | −3% (−4 … −2) | 0% (−2 … +1) |
| explode/crlf/short @ delimiter-crlf-short | 428 | 0% (−1 … 0) | −1% (−1 … 0) |
| explode/crlf/4k @ delimiter-crlf-4k | 9,308 | −1% (−2 … +1) | 0% (−2 … +1) |
| explode/crlf/64k @ delimiter-crlf-64k | 187,149 | −1% (−2 … +4) | +2% (−1 … +2) |
| explode/comma/short @ delimiter-comma-short | 330 | +1% (−1 … +1) | 0% (−2 … +1) |
| explode/comma/4k @ delimiter-comma-4k | 7,596 | +2% (+2 … +4) | +2% (−4 … +8) |
| explode/comma/64k @ delimiter-comma-64k | 165,918 | −3% (−8 … 0) | −1% (−5 … 0) |
| parse-records/4k @ records-4k | 36,892 | 0% (−1 … 0) | +1% (0 … +2) |
| parse-query/4k @ query-4k | 95,247 | 0% (0 … 0) | 0% (−1 … +1) |
| parse-http/small @ http-small | 3,101 | 0% (−2 … 0) | 0% (0 … 0) |
| parse-http/body64k @ http-body64k | 3,100 | 0% (−1 … +1) | 0% (−3 … 0) |
| scan-template/4k @ template-4k | 16,107 | 0% (0 … +1) | 0% (−1 … 0) |
| render-template/4k @ template-4k | 29,108 | 0% (−1 … 0) | +1% (+1 … +1) |
| log-contains/event/post/early @ logs-post-early | 136 | −1% (−3 … 0) | +1% (−2 … +2) |
| log-contains/level/post/early @ logs-post-early | 149 | 0% (−2 … +2) | −1% (−1 … 0) |
| log-contains/event/thread/clean @ logs-thread-clean | 64,437 | −1% (−1 … +1) | 0% (0 … +1) |
| log-filter/thread/clean @ logs-thread-clean | 210,056 | 0% (−1 … +1) | +1% (0 … +1) |
| log-contains/event/thread/early @ logs-thread-early | 136 | 0% (0 … +1) | 0% (−1 … 0) |
| log-contains/level/thread/early @ logs-thread-early | 148 | 0% (−1 … +1) | 0% (−5 … 0) |
| log-contains/event/thread/late @ logs-thread-late | 64,688 | 0% (−9 … +1) | 0% (−1 … 0) |
| log-filter/thread/late @ logs-thread-late | 210,048 | 0% (0 … +1) | −1% (−2 … +1) |

~: the change is not larger than the A/A control of the same row: not evidence of a difference.

layout?: in every pass the cycles changed in the same direction, by 3% or more in the median, the instructions by less than 0.5%: the work is the same, so look for the cause (code placement, branch prediction) with `bench why` before reporting the row.
<!-- /bench-table -->
