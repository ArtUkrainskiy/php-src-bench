# Full tables: date_format() builds the time zone offset only when used

Change in CPU cycles per call against master (negative = fewer cycles, faster). In each cell: the median over the passes, then the range over the passes. The last column is the range of the change in instructions over both compilers. Row names: the format, then the zone of the `DateTimeImmutable`. `date()` rows use a Unix timestamp and the default zone, UTC.

## Main series

All 58 calls of [`date.php`](date.php), 15 passes ([`series.json`](series.json)).

<!-- bench-table series.json --full -->
| call | master, CPU cycles per call (GCC 15.2) | GCC 15.2 | clang 21.1 | instructions |
|---|--:|--:|--:|--:|
| format('Y') @ UTC | 416 | −42% (−43 … −40) | −26% (−27 … −22) | −28% … −24% |
| format('Y') @ Europe/Madrid | 746 | −68% (−68 … −67) | −63% (−63 … −63) | −63% |
| format('Y') @ America/New_York | 721 | −67% (−67 … −66) | −62% (−62 … −62) | −61% |
| format('Y') @ offset +05:30 | 440 | −46% (−47 … −45) | −47% (−48 … −46) | −46% … −45% |
| format('Y') @ abbreviation EST | 350 | −32% (−33 … −30) | −21% (−21 … −19) | −23% … −19% |
| format('Y-m-d') @ UTC | 634 | −28% (−29 … −27) | −18% (−19 … −17) | −18% … −15% |
| format('Y-m-d') @ Europe/Madrid | 958 | −52% (−52 … −51) | −48% (−48 … −47) | −50% … −49% |
| format('Y-m-d') @ America/New_York | 923 | −51% (−51 … −49) | −47% (−48 … −45) | −48% |
| format('Y-m-d') @ offset +05:30 | 665 | −32% (−34 … −31) | −30% (−31 … −30) | −33% … −32% |
| format('Y-m-d') @ abbreviation EST | 578 | −22% (−23 … −20) | −15% (−16 … −14) | −14% … −12% |
| format('Y-m-d H:i:s') @ UTC | 1,039 | −17% (−17 … −15) | −9% (−12 … −8) | −12% … −10% |
| format('Y-m-d H:i:s') @ Europe/Madrid | 1,258 | −39% (−40 … −37) | −34% (−35 … −30) | −38% … −37% |
| format('Y-m-d H:i:s') @ America/New_York | 1,333 | −35% (−36 … −35) | −31% (−33 … −31) | −36% |
| format('Y-m-d H:i:s') @ offset +05:30 | 1,080 | −20% (−24 … −20) | −18% (−19 … −16) | −23% … −22% |
| format('Y-m-d H:i:s') @ abbreviation EST | 985 | −12% (−13 … −11) | −8% (−10 … −6) | −9% … −8% |
| format('H:i') @ UTC | 475 | −36% (−37 … −35) | −26% (−26 … −25) | −24% … −20% |
| format('H:i') @ Europe/Madrid | 814 | −62% (−63 … −59) | −60% (−61 … −60) | −58% |
| format('H:i') @ America/New_York | 788 | −61% (−62 … −61) | −59% (−59 … −58) | −57% … −56% |
| format('H:i') @ offset +05:30 | 504 | −40% (−40 … −38) | −37% (−38 … −37) | −40% |
| format('H:i') @ abbreviation EST | 419 | −28% (−29 … −25) | −22% (−22 … −21) | −19% … −16% |
| format('D, d M Y') @ UTC | 728 | −21% (−23 … −20) | −12% (−14 … −12) | −15% … −13% |
| format('D, d M Y') @ Europe/Madrid | 1,064 | −46% (−46 … −45) | −41% (−43 … −41) | −45% |
| format('D, d M Y') @ America/New_York | 1,030 | −44% (−45 … −43) | −41% (−42 … −40) | −43% |
| format('D, d M Y') @ offset +05:30 | 788 | −27% (−28 … −26) | −24% (−25 … −23) | −29% … −28% |
| format('D, d M Y') @ abbreviation EST | 688 | −16% (−19 … −15) | −10% (−12 … −8) | −12% … −10% |
| format('Y-m-d\TH:i:s.u') @ UTC | 1,110 | −17% (−19 … −16) | −7% (−8 … −5) | −10% … −9% |
| format('Y-m-d\TH:i:s.u') @ Europe/Madrid | 1,442 | −34% (−35 … −33) | −29% (−30 … −28) | −34% |
| format('Y-m-d\TH:i:s.u') @ America/New_York | 1,398 | −34% (−35 … −31) | −29% (−30 … −27) | −33% |
| format('Y-m-d\TH:i:s.u') @ offset +05:30 | 1,154 | −20% (−22 … −19) | −15% (−18 … −14) | −20% |
| format('Y-m-d\TH:i:s.u') @ abbreviation EST | 1,045 | −11% (−12 … −10) | −5% (−6 … −4) | −8% … −7% |
| format('U') @ UTC | 382 | −39% (−41 … −38) | −26% (−27 … −19) | −28% … −24% |
| format('U') @ Europe/Madrid | 733 | −68% (−69 … −68) | −65% (−65 … −63) | −64% … −63% |
| format('U') @ America/New_York | 708 | −67% (−69 … −64) | −63% (−64 … −63) | −62% … −61% |
| format('U') @ offset +05:30 | 428 | −45% (−46 … −40) | −46% (−47 … −46) | −46% … −45% |
| format('U') @ abbreviation EST | 342 | −32% (−32 … −31) | −20% (−22 … −20) | −22% … −20% |
| format('c') @ UTC | 812 | +1% (−5 … +2) | +8% (+7 … +9) layout? | 0% |
| format('c') @ Europe/Madrid | 1,125 | +2% (+1 … +9) | +5% (+5 … +8) layout? | 0% |
| format('c') @ America/New_York | 1,120 | 0% (−2 … +3) | +6% (+5 … +6) layout? | 0% |
| format('c') @ offset +05:30 | 832 | +6% (+6 … +10) layout? | +12% (+9 … +13) layout? | 0% |
| format('c') @ abbreviation EST | 747 | +3% (+2 … +4) | +5% (+3 … +8) layout? | 0% |
| format('Y-m-d\TH:i:sP') @ UTC | 1,221 | −2% (−5 … −1) | +4% (+3 … +5) layout? | 0% |
| format('Y-m-d\TH:i:sP') @ Europe/Madrid | 1,468 | −1% (−3 … +1) | +7% (+4 … +8) layout? | 0% |
| format('Y-m-d\TH:i:sP') @ America/New_York | 1,497 | −2% (−2 … +3) | +6% (+5 … +7) layout? | 0% |
| format('Y-m-d\TH:i:sP') @ offset +05:30 | 1,249 | −2% (−4 … +1) | +6% (+6 … +8) layout? | 0% |
| format('Y-m-d\TH:i:sP') @ abbreviation EST | 1,149 | −3% (−8 … −2) | +4% (0 … +5) | 0% |
| format('D, d M Y H:i:s O') @ UTC | 1,328 | −2% (−3 … +1) | +2% (−1 … +4) | 0% |
| format('D, d M Y H:i:s O') @ Europe/Madrid | 1,651 | −1% (−4 … +2) | +4% (+3 … +6) layout? | 0% |
| format('D, d M Y H:i:s O') @ America/New_York | 1,611 | 0% (−2 … +2) | +4% (+2 … +5) layout? | 0% |
| format('D, d M Y H:i:s O') @ offset +05:30 | 1,390 | 0% (−1 … +1) ~ | +6% (+4 … +8) layout? | 0% |
| format('D, d M Y H:i:s O') @ abbreviation EST | 1,260 | −1% (−4 … 0) | +2% (−1 … +3) | 0% |
| format('T') @ UTC | 338 | −3% (−4 … −2) layout? | −3% (−3 … 0) | 0% … +1% |
| format('T') @ Europe/Madrid | 681 | +1% (0 … +1) | −1% (−2 … 0) | 0% |
| format('T') @ America/New_York | 655 | +1% (−1 … +2) | −2% (−7 … −2) | 0% |
| format('T') @ offset +05:30 | 384 | +7% (−2 … +8) | +2% (0 … +3) | 0% … +1% |
| format('T') @ abbreviation EST | 287 | +3% (−5 … +4) | −2% (−4 … 0) | +1% |
| date('Y-m-d') @ timestamp | 866 | −17% (−19 … −11) | −10% (−11 … −8) | −13% … −11% |
| date('Y-m-d H:i:s') @ timestamp | 1,277 | −12% (−16 … −10) | −5% (−6 … −4) | −9% … −8% |
| date(DATE_ATOM) @ timestamp | 1,433 | −2% (−4 … −1) | +3% (0 … +4) | 0% |

Control: master against itself.

| call | master, CPU cycles per call (GCC 15.2) | A/A start | A/A end |
|---|--:|--:|--:|
| format('Y') @ UTC | 415 | 0% (−2 … +1) | 0% (−1 … +1) |
| format('Y') @ Europe/Madrid | 745 | 0% (−1 … +2) | 0% (0 … +2) |
| format('Y') @ America/New_York | 720 | 0% (−1 … +2) | 0% (−1 … +1) |
| format('Y') @ offset +05:30 | 439 | 0% (−10 … 0) | 0% (−2 … +2) |
| format('Y') @ abbreviation EST | 350 | 0% (−1 … +1) | 0% (−4 … 0) |
| format('Y-m-d') @ UTC | 624 | 0% (−1 … +1) | 0% (−1 … +4) |
| format('Y-m-d') @ Europe/Madrid | 956 | 0% (−1 … +1) | 0% (0 … +2) |
| format('Y-m-d') @ America/New_York | 923 | 0% (−1 … +1) | 0% (−1 … +2) |
| format('Y-m-d') @ offset +05:30 | 662 | +1% (−2 … +3) | 0% (−5 … +2) |
| format('Y-m-d') @ abbreviation EST | 579 | 0% (−1 … +1) | 0% (−1 … +1) |
| format('Y-m-d H:i:s') @ UTC | 1,034 | 0% (−1 … +1) | 0% (−1 … +1) |
| format('Y-m-d H:i:s') @ Europe/Madrid | 1,257 | 0% (−1 … +5) | 0% (0 … +1) |
| format('Y-m-d H:i:s') @ America/New_York | 1,332 | 0% (−1 … +1) | 0% (−5 … +1) |
| format('Y-m-d H:i:s') @ offset +05:30 | 1,080 | 0% (−2 … +3) | 0% (−3 … +4) |
| format('Y-m-d H:i:s') @ abbreviation EST | 986 | 0% (−3 … +1) | 0% (−3 … 0) |
| format('H:i') @ UTC | 486 | 0% (0 … +3) | 0% (−1 … +1) |
| format('H:i') @ Europe/Madrid | 816 | 0% (−2 … +1) | 0% (−3 … +1) |
| format('H:i') @ America/New_York | 791 | 0% (−1 … +1) | 0% (−3 … +1) |
| format('H:i') @ offset +05:30 | 506 | 0% (−1 … +1) | 0% (−1 … +1) |
| format('H:i') @ abbreviation EST | 414 | 0% (−1 … +2) | 0% (−1 … +1) |
| format('D, d M Y') @ UTC | 723 | 0% (−1 … +1) | 0% (−2 … +2) |
| format('D, d M Y') @ Europe/Madrid | 1,061 | 0% (−1 … +1) | 0% (−1 … +2) |
| format('D, d M Y') @ America/New_York | 1,031 | 0% (−1 … 0) | 0% (−1 … +1) |
| format('D, d M Y') @ offset +05:30 | 790 | −1% (−2 … 0) | 0% (−2 … +2) |
| format('D, d M Y') @ abbreviation EST | 684 | 0% (−1 … +2) | 0% (−1 … +2) |
| format('Y-m-d\TH:i:s.u') @ UTC | 1,106 | 0% (−1 … +1) | 0% (−1 … +1) |
| format('Y-m-d\TH:i:s.u') @ Europe/Madrid | 1,441 | 0% (−1 … +2) | 0% (0 … +2) |
| format('Y-m-d\TH:i:s.u') @ America/New_York | 1,398 | 0% (−2 … +5) | 0% (−3 … +1) |
| format('Y-m-d\TH:i:s.u') @ offset +05:30 | 1,148 | 0% (−1 … +3) | 0% (−2 … +3) |
| format('Y-m-d\TH:i:s.u') @ abbreviation EST | 1,051 | 0% (−2 … +1) | 0% (−1 … +2) |
| format('U') @ UTC | 380 | 0% (−3 … +1) | 0% (−5 … +5) |
| format('U') @ Europe/Madrid | 733 | 0% (−1 … +2) | 0% (−2 … +1) |
| format('U') @ America/New_York | 707 | 0% (−2 … +4) | 0% (−1 … +1) |
| format('U') @ offset +05:30 | 427 | 0% (0 … +4) | 0% (−3 … +1) |
| format('U') @ abbreviation EST | 342 | 0% (−1 … +4) | 0% (−1 … +4) |
| format('c') @ UTC | 807 | 0% (0 … 0) | 0% (−2 … +1) |
| format('c') @ Europe/Madrid | 1,124 | 0% (−1 … +4) | 0% (0 … +4) |
| format('c') @ America/New_York | 1,114 | 0% (0 … +1) | 0% (−1 … +1) |
| format('c') @ offset +05:30 | 832 | 0% (−1 … +1) | 0% (−2 … +1) |
| format('c') @ abbreviation EST | 746 | 0% (0 … +1) | 0% (−1 … +3) |
| format('Y-m-d\TH:i:sP') @ UTC | 1,218 | 0% (−2 … +1) | 0% (−1 … +1) |
| format('Y-m-d\TH:i:sP') @ Europe/Madrid | 1,468 | 0% (−1 … +1) | 0% (−1 … +1) |
| format('Y-m-d\TH:i:sP') @ America/New_York | 1,502 | 0% (−1 … +1) | 0% (−1 … +1) |
| format('Y-m-d\TH:i:sP') @ offset +05:30 | 1,253 | 0% (−2 … +3) | 0% (−1 … +4) |
| format('Y-m-d\TH:i:sP') @ abbreviation EST | 1,138 | +1% (−1 … +3) | 0% (−2 … +1) |
| format('D, d M Y H:i:s O') @ UTC | 1,321 | 0% (−2 … +1) | 0% (−1 … +2) |
| format('D, d M Y H:i:s O') @ Europe/Madrid | 1,638 | 0% (−1 … +2) | 0% (−1 … +1) |
| format('D, d M Y H:i:s O') @ America/New_York | 1,612 | 0% (−1 … +1) | 0% (−1 … +1) |
| format('D, d M Y H:i:s O') @ offset +05:30 | 1,385 | 0% (−4 … +2) | 0% (−2 … +3) |
| format('D, d M Y H:i:s O') @ abbreviation EST | 1,264 | 0% (−2 … +7) | 0% (−2 … +2) |
| format('T') @ UTC | 337 | 0% (−1 … +1) | 0% (−1 … +1) |
| format('T') @ Europe/Madrid | 683 | 0% (−1 … +1) | 0% (−3 … +1) |
| format('T') @ America/New_York | 653 | 0% (−3 … +1) | 0% (−1 … +1) |
| format('T') @ offset +05:30 | 383 | 0% (0 … +4) | 0% (−2 … +1) |
| format('T') @ abbreviation EST | 286 | 0% (−2 … +2) | 0% (−3 … +4) |
| date('Y-m-d') @ timestamp | 864 | 0% (−2 … +1) | 0% (−5 … +1) |
| date('Y-m-d H:i:s') @ timestamp | 1,270 | 0% (−1 … +1) | 0% (−1 … +1) |
| date(DATE_ATOM) @ timestamp | 1,427 | 0% (−4 … +3) | 0% (−1 … +2) |

~: within noise, the change is no larger than the difference between master and master on the same row.

layout?: in every pass the cycles changed in the same direction, by 3% or more in the median, the instructions by less than 0.5%: the work is the same, so look for the cause (code placement, branch prediction) with `bench why` before reporting the row.
<!-- /bench-table -->

## Aligned builds

Master and the change built with the flags of the main series plus `-falign-functions=64 -falign-loops=32` (`BENCH_CFLAGS` with `--profile docker`, so the link flags and `--enable-werror` are the same). Only to see how much of the cycles of these rows comes from where the code sits. Formats that print the time zone, and `format('Y')` on two zones, 15 passes ([`align-series.json`](align-series.json)). The load average was 9.1 at the start, from the builds of this series.

<!-- bench-table align-series.json --full -->
| call | master, CPU cycles per call (GCC 15.2) | GCC 15.2 | clang 21.1 | instructions |
|---|--:|--:|--:|--:|
| format('Y') @ UTC | 364 | −31% (−32 … −30) | −26% (−27 … −25) | −28% … −24% |
| format('Y') @ Europe/Madrid | 730 | −66% (−67 … −65) | −64% (−64 … −62) | −63% |
| format('c') @ UTC | 769 | 0% (−4 … +6) ~ | −5% (−7 … +4) | 0% |
| format('c') @ Europe/Madrid | 1,135 | −2% (−6 … +1) | −2% (−3 … +3) | 0% |
| format('c') @ America/New_York | 1,105 | −2% (−4 … +1) | −2% (−2 … 0) | 0% |
| format('c') @ offset +05:30 | 858 | 0% (−3 … +1) | −3% (−5 … +1) | 0% |
| format('c') @ abbreviation EST | 715 | +3% (+2 … +10) layout? | −3% (−4 … 0) | 0% |
| format('Y-m-d\TH:i:sP') @ UTC | 1,145 | +2% (0 … +3) | 0% (−1 … +1) ~ | 0% |
| format('Y-m-d\TH:i:sP') @ Europe/Madrid | 1,461 | +1% (0 … +7) | −1% (−2 … −1) | 0% |
| format('Y-m-d\TH:i:sP') @ America/New_York | 1,489 | +1% (−2 … +2) | +1% (−4 … +2) | 0% |
| format('Y-m-d\TH:i:sP') @ offset +05:30 | 1,233 | +3% (+1 … +4) | +2% (+1 … +3) | 0% |
| format('Y-m-d\TH:i:sP') @ abbreviation EST | 1,104 | +2% (+2 … +3) | 0% (−1 … +2) ~ | 0% |
| format('D, d M Y H:i:s O') @ UTC | 1,285 | +3% (0 … +7) | +1% (−1 … +3) | 0% |
| format('D, d M Y H:i:s O') @ Europe/Madrid | 1,652 | +2% (−1 … +4) | 0% (−3 … +1) | 0% |
| format('D, d M Y H:i:s O') @ America/New_York | 1,624 | +2% (−1 … +4) | +1% (−1 … +4) | 0% |
| format('D, d M Y H:i:s O') @ offset +05:30 | 1,371 | +5% (0 … +6) layout? | +2% (+1 … +6) | 0% |
| format('D, d M Y H:i:s O') @ abbreviation EST | 1,235 | +3% (+2 … +5) layout? | +2% (0 … +4) | 0% |
| format('T') @ UTC | 300 | +8% (+5 … +10) layout? | +2% (−3 … +4) | 0% … +1% |
| format('T') @ Europe/Madrid | 644 | +4% (+3 … +5) layout? | −2% (−3 … −1) | 0% |
| format('T') @ America/New_York | 614 | +4% (+2 … +5) layout? | −3% (−4 … +2) | 0% |
| format('T') @ offset +05:30 | 406 | 0% (−2 … +1) ~ | −3% (−4 … −3) | 0% … +1% |
| format('T') @ abbreviation EST | 260 | +7% (+1 … +29) | +3% (+1 … +19) | +1% |
| date(DATE_ATOM) @ timestamp | 1,426 | 0% (−1 … +1) ~ | −1% (−2 … 0) | 0% |

Control: master against itself.

| call | master, CPU cycles per call (GCC 15.2) | A/A start | A/A end |
|---|--:|--:|--:|
| format('Y') @ UTC | 363 | 0% (−1 … +2) | 0% (−3 … 0) |
| format('Y') @ Europe/Madrid | 731 | 0% (−1 … +1) | 0% (−1 … +1) |
| format('c') @ UTC | 769 | 0% (−1 … +6) | 0% (−7 … +6) |
| format('c') @ Europe/Madrid | 1,133 | 0% (−4 … +4) | 0% (−5 … +4) |
| format('c') @ America/New_York | 1,103 | 0% (−4 … +5) | 0% (−1 … +4) |
| format('c') @ offset +05:30 | 858 | 0% (−3 … +4) | 0% (−3 … +4) |
| format('c') @ abbreviation EST | 717 | 0% (−6 … +6) | 0% (−6 … +7) |
| format('Y-m-d\TH:i:sP') @ UTC | 1,144 | 0% (−1 … +1) | 0% (−1 … +1) |
| format('Y-m-d\TH:i:sP') @ Europe/Madrid | 1,458 | 0% (−1 … +2) | 0% (−2 … +1) |
| format('Y-m-d\TH:i:sP') @ America/New_York | 1,488 | 0% (−3 … +1) | 0% (−1 … +1) |
| format('Y-m-d\TH:i:sP') @ offset +05:30 | 1,232 | 0% (−2 … +3) | 0% (−2 … +3) |
| format('Y-m-d\TH:i:sP') @ abbreviation EST | 1,102 | 0% (−2 … +2) | 0% (−1 … +1) |
| format('D, d M Y H:i:s O') @ UTC | 1,284 | 0% (−1 … +3) | 0% (−3 … +2) |
| format('D, d M Y H:i:s O') @ Europe/Madrid | 1,653 | 0% (−2 … +1) | 0% (−2 … +1) |
| format('D, d M Y H:i:s O') @ America/New_York | 1,624 | 0% (−1 … +2) | 0% (−3 … +3) |
| format('D, d M Y H:i:s O') @ offset +05:30 | 1,370 | 0% (−2 … +3) | 0% (−2 … +1) |
| format('D, d M Y H:i:s O') @ abbreviation EST | 1,233 | 0% (−2 … +1) | 0% (−1 … +3) |
| format('T') @ UTC | 299 | 0% (−1 … +1) | 0% (−1 … +4) |
| format('T') @ Europe/Madrid | 644 | 0% (−1 … 0) | 0% (−2 … +3) |
| format('T') @ America/New_York | 615 | 0% (−1 … +3) | 0% (−1 … +3) |
| format('T') @ offset +05:30 | 405 | 0% (−1 … +1) | 0% (0 … +1) |
| format('T') @ abbreviation EST | 260 | 0% (−1 … +4) | 0% (0 … +1) |
| date(DATE_ATOM) @ timestamp | 1,424 | 0% (−21 … +1) | 0% (−2 … +1) |

~: within noise, the change is no larger than the difference between master and master on the same row.

layout?: in every pass the cycles changed in the same direction, by 3% or more in the median, the instructions by less than 0.5%: the work is the same, so look for the cause (code placement, branch prediction) with `bench why` before reporting the row.
<!-- /bench-table -->

## More paths

All 27 calls of [`date-extra.php`](date-extra.php), same builds as the main series, 15 passes ([`extra-series.json`](extra-series.json)). The column `clang21-aa` runs clang master against itself. The instructions column spans all three columns, so its 0% end comes from that control.

<!-- bench-table extra-series.json --full -->
| call | master, CPU cycles per call (GCC 15.2 (gcc15)) | GCC 15.2 (gcc15) | clang 21.1 (clang21) | clang 21.1 (clang21-aa) | instructions |
|---|--:|--:|--:|--:|--:|
| json_encode(100 dates) @ 100 dates UTC | 182,579 | −9% (−10 … −6) | −1% (−2 … 0) | 0% (−1 … +4) ~ | −6% … 0% |
| json_encode(100 dates) @ 100 dates Europe/Madrid | 218,476 | −22% (−23 … −21) | −20% (−21 … −19) | 0% (−3 … +1) | −22% … 0% |
| serialize(100 dates) @ 100 dates UTC | 194,702 | −9% (−11 … −8) | −1% (−2 … +1) | 0% (−2 … +1) | −6% … 0% |
| serialize(100 dates) @ 100 dates Europe/Madrid | 232,803 | −23% (−31 … −22) | −18% (−19 … −17) | 0% (−1 … +2) ~ | −24% … 0% |
| gmdate('Y-m-d H:i:s') @ timestamp | 892 | −3% (−5 … +1) | +8% (+5 … +9) layout? | 0% (−2 … +2) ~ | 0% |
| gmdate('c') @ timestamp | 639 | 0% (−7 … 0) ~ | +11% (+5 … +13) layout? | 0% (−1 … 0) ~ | 0% |
| gmdate('Y-m-d\\TH:i:sP') @ timestamp | 1,059 | −3% (−5 … −1) | +8% (+2 … +10) layout? | 0% (−2 … +4) | 0% |
| gmdate('D, d M Y H:i:s \\G\\M\\T') @ timestamp | 1,039 | −2% (−4 … 0) | +3% (+2 … +5) | 0% (−2 … +2) ~ | 0% |
| date('Y-m-d') @ timestamp | 1,541 | −31% (−32 … −29) | −28% (−28 … −27) | 0% (−1 … +1) ~ | −31% … 0% |
| date('Y-m-d H:i:s') @ timestamp | 1,947 | −25% (−25 … −24) | −21% (−22 … −20) | 0% (−1 … +1) ~ | −26% … 0% |
| date('Y-m-d\\TH:i:sP') @ timestamp | 2,111 | −1% (−1 … 0) | +3% (+2 … +4) layout? | 0% (−1 … +3) ~ | 0% |
| format('p') @ UTC | 334 | +3% (+1 … +5) | −1% (−2 … +12) | 0% (−3 … +1) | 0% … +1% |
| format('p') @ Europe/Madrid | 838 | −2% (−7 … −1) | +1% (0 … +4) | 0% (−1 … +1) ~ | 0% |
| format('p') @ offset +05:30 | 525 | +2% (+1 … +3) | +6% (+5 … +7) layout? | 0% (−1 … 0) ~ | 0% |
| format('p') @ abbreviation EST | 453 | −7% (−7 … +2) | 0% (−2 … +1) | 0% (−1 … +3) ~ | 0% … +1% |
| format('e') @ UTC | 339 | −39% (−40 … −39) | −33% (−34 … −29) | 0% (−1 … +1) ~ | −32% … 0% |
| format('e') @ Europe/Madrid | 687 | −69% (−69 … −68) | −68% (−68 … −67) | 0% (−1 … +1) ~ | −66% … 0% |
| format('e') @ offset +05:30 | 459 | +3% (+2 … +5) | +6% (+4 … +7) | 0% (−1 … +1) ~ | 0% … +1% |
| format('e') @ abbreviation EST | 291 | +1% (−1 … +4) | −2% (−5 … −1) | 0% (−1 … +1) | 0% … +1% |
| format('Y-m-d H:i:s T (P)') @ UTC | 1,405 | −4% (−15 … −2) layout? | +4% (+1 … +6) layout? | 0% (−3 … +2) ~ | 0% |
| format('Y-m-d H:i:s T (P)') @ Europe/Madrid | 1,664 | −1% (−3 … −1) | +7% (+2 … +8) layout? | 0% (−2 … +2) | 0% |
| format('Y-m-d H:i:s T (P)') @ offset +05:30 | 1,443 | −2% (−4 … +1) | +4% (+3 … +7) layout? | +1% (−2 … +3) | 0% |
| format('Y-m-d H:i:s T (P)') @ abbreviation EST | 1,345 | −3% (−4 … −1) layout? | +3% (+2 … +5) layout? | 0% (−2 … +2) ~ | 0% |
| format('P T e I Z') @ UTC | 869 | −5% (−8 … −4) layout? | +2% (0 … +3) | 0% (−2 … +3) ~ | 0% … +1% |
| format('P T e I Z') @ Europe/Madrid | 1,217 | −3% (−4 … −1) | +3% (+2 … +5) layout? | 0% (−2 … +6) | 0% |
| format('P T e I Z') @ offset +05:30 | 1,000 | −2% (−3 … −1) | +6% (+3 … +7) | 0% (−2 … +1) | 0% … +1% |
| format('P T e I Z') @ abbreviation EST | 817 | −3% (−5 … 0) layout? | +3% (0 … +6) | 0% (−1 … +2) | 0% … +1% |

Control: master against itself.

| call | master, CPU cycles per call (GCC 15.2) | A/A start | A/A end |
|---|--:|--:|--:|
| json_encode(100 dates) @ 100 dates UTC | 182,110 | 0% (−1 … +1) | 0% (−1 … +1) |
| json_encode(100 dates) @ 100 dates Europe/Madrid | 218,210 | 0% (−1 … +1) | 0% (−1 … +2) |
| serialize(100 dates) @ 100 dates UTC | 194,399 | 0% (−3 … +3) | 0% (−1 … +1) |
| serialize(100 dates) @ 100 dates Europe/Madrid | 232,507 | 0% (0 … +1) | 0% (−11 … +4) |
| gmdate('Y-m-d H:i:s') @ timestamp | 893 | 0% (−3 … +2) | −1% (−3 … 0) |
| gmdate('c') @ timestamp | 641 | 0% (−7 … +4) | 0% (−1 … +1) |
| gmdate('Y-m-d\\TH:i:sP') @ timestamp | 1,058 | 0% (−2 … +2) | 0% (−5 … +2) |
| gmdate('D, d M Y H:i:s \\G\\M\\T') @ timestamp | 1,042 | −1% (−1 … +1) | 0% (−1 … +2) |
| date('Y-m-d') @ timestamp | 1,537 | 0% (−1 … +1) | 0% (−1 … +1) |
| date('Y-m-d H:i:s') @ timestamp | 1,943 | 0% (−1 … +1) | 0% (−1 … +1) |
| date('Y-m-d\\TH:i:sP') @ timestamp | 2,113 | 0% (−1 … +1) | 0% (−1 … +1) |
| format('p') @ UTC | 334 | 0% (−4 … +1) | 0% (0 … 0) |
| format('p') @ Europe/Madrid | 837 | 0% (0 … +1) | 0% (−1 … +1) |
| format('p') @ offset +05:30 | 524 | 0% (−1 … 0) | 0% (0 … +3) |
| format('p') @ abbreviation EST | 453 | 0% (−1 … +2) | 0% (−12 … +20) |
| format('e') @ UTC | 339 | 0% (−1 … +1) | 0% (−1 … +1) |
| format('e') @ Europe/Madrid | 687 | 0% (−1 … +1) | 0% (−1 … +1) |
| format('e') @ offset +05:30 | 459 | 0% (−1 … +1) | 0% (−1 … +2) |
| format('e') @ abbreviation EST | 291 | 0% (−5 … +3) | 0% (−1 … +1) |
| format('Y-m-d H:i:s T (P)') @ UTC | 1,404 | 0% (−1 … +2) | 0% (−5 … +1) |
| format('Y-m-d H:i:s T (P)') @ Europe/Madrid | 1,666 | 0% (−1 … 0) | 0% (0 … +2) |
| format('Y-m-d H:i:s T (P)') @ offset +05:30 | 1,442 | 0% (−4 … +3) | 0% (−3 … +5) |
| format('Y-m-d H:i:s T (P)') @ abbreviation EST | 1,343 | 0% (−1 … +1) | 0% (−6 … 0) |
| format('P T e I Z') @ UTC | 858 | 0% (0 … +1) | 0% (−2 … +1) |
| format('P T e I Z') @ Europe/Madrid | 1,217 | 0% (−3 … +1) | 0% (−2 … +1) |
| format('P T e I Z') @ offset +05:30 | 998 | 0% (−1 … +1) | 0% (0 … +3) |
| format('P T e I Z') @ abbreviation EST | 821 | 0% (−2 … +1) | 0% (−2 … +2) |

~: within noise, the change is no larger than the difference between master and master on the same row.

layout?: in every pass the cycles changed in the same direction, by 3% or more in the median, the instructions by less than 0.5%: the work is the same, so look for the cause (code placement, branch prediction) with `bench why` before reporting the row.
<!-- /bench-table -->

## More paths, aligned builds

The same calls without serialization on the aligned builds of the section above, 15 passes ([`extra-align-series.json`](extra-align-series.json)).

<!-- bench-table extra-align-series.json --full -->
| call | master, CPU cycles per call (GCC 15.2 (gcc15)) | GCC 15.2 (gcc15) | clang 21.1 (clang21) | clang 21.1 (clang21-aa) | instructions |
|---|--:|--:|--:|--:|--:|
| gmdate('Y-m-d H:i:s') @ timestamp | 873 | +4% (+3 … +5) layout? | −2% (−3 … +1) | 0% (−3 … +2) ~ | 0% |
| gmdate('c') @ timestamp | 653 | 0% (−2 … +6) | −4% (−5 … 0) layout? | 0% (−1 … +5) ~ | 0% |
| gmdate('Y-m-d\\TH:i:sP') @ timestamp | 1,035 | +2% (+1 … +3) | −1% (−3 … 0) | 0% (−2 … +3) ~ | 0% |
| gmdate('D, d M Y H:i:s \\G\\M\\T') @ timestamp | 1,031 | +2% (−1 … +7) | 0% (−3 … +1) ~ | −1% (−2 … +2) | 0% |
| date('Y-m-d') @ timestamp | 1,532 | −28% (−29 … −27) | −30% (−30 … −29) | 0% (−1 … +1) ~ | −31% … 0% |
| date('Y-m-d H:i:s') @ timestamp | 1,938 | −21% (−22 … −20) | −23% (−24 … −21) | 0% (−1 … +1) ~ | −26% … 0% |
| date('Y-m-d\\TH:i:sP') @ timestamp | 2,116 | −1% (−2 … 0) | −2% (−3 … −1) | 0% (−1 … +1) ~ | 0% |
| format('p') @ UTC | 316 | +1% (−1 … +1) ~ | +2% (−1 … +9) | 0% (−1 … +4) ~ | 0% … +1% |
| format('p') @ Europe/Madrid | 805 | 0% (−2 … +1) | 0% (−1 … +2) ~ | 0% (0 … +1) | 0% |
| format('p') @ offset +05:30 | 541 | +8% (+6 … +9) layout? | −2% (−4 … −2) | 0% (−1 … +1) | 0% |
| format('p') @ abbreviation EST | 418 | +1% (0 … +2) | −3% (−5 … −1) | 0% (−1 … +3) ~ | 0% … +1% |
| format('e') @ UTC | 299 | −38% (−38 … −37) | −32% (−36 … −24) | 0% (−2 … +5) | −32% … 0% |
| format('e') @ Europe/Madrid | 661 | −70% (−70 … −66) | −71% (−71 … −70) | 0% (0 … +2) ~ | −66% … 0% |
| format('e') @ offset +05:30 | 474 | +5% (−5 … +6) | −5% (−6 … −2) | 0% (−1 … +1) | 0% … +1% |
| format('e') @ abbreviation EST | 260 | +8% (+6 … +9) | +4% (−3 … +8) | 0% (−5 … +9) ~ | 0% … +1% |
| format('Y-m-d H:i:s T (P)') @ UTC | 1,330 | +8% (+6 … +10) layout? | −1% (−2 … +1) | 0% (−1 … +2) ~ | 0% |
| format('Y-m-d H:i:s T (P)') @ Europe/Madrid | 1,655 | +5% (+2 … +7) layout? | −1% (−5 … 0) | 0% (−1 … +2) | 0% |
| format('Y-m-d H:i:s T (P)') @ offset +05:30 | 1,444 | +6% (+3 … +7) layout? | +3% (+1 … +5) layout? | 0% (−1 … +3) ~ | 0% |
| format('Y-m-d H:i:s T (P)') @ abbreviation EST | 1,291 | +8% (+6 … +9) layout? | +1% (−1 … +3) | +1% (−2 … +6) | 0% |
| format('P T e I Z') @ UTC | 793 | +4% (0 … +5) layout? | +2% (+1 … +4) | 0% (−1 … +1) ~ | 0% … +1% |
| format('P T e I Z') @ Europe/Madrid | 1,171 | +3% (+1 … +4) layout? | +3% (+1 … +4) | 0% (−1 … +2) ~ | 0% |
| format('P T e I Z') @ offset +05:30 | 988 | +5% (+3 … +6) layout? | +3% (−2 … +5) | 0% (−1 … 0) ~ | 0% … +1% |
| format('P T e I Z') @ abbreviation EST | 764 | +4% (+3 … +6) layout? | +5% (0 … +6) | 0% (−1 … +1) ~ | 0% … +1% |

Control: master against itself.

| call | master, CPU cycles per call (GCC 15.2) | A/A start | A/A end |
|---|--:|--:|--:|
| gmdate('Y-m-d H:i:s') @ timestamp | 875 | 0% (−1 … +1) | 0% (−1 … +2) |
| gmdate('c') @ timestamp | 650 | 0% (−7 … +7) | 0% (−7 … +7) |
| gmdate('Y-m-d\\TH:i:sP') @ timestamp | 1,036 | 0% (−1 … +31) | 0% (−2 … +3) |
| gmdate('D, d M Y H:i:s \\G\\M\\T') @ timestamp | 1,032 | 0% (−3 … +1) | 0% (−2 … +2) |
| date('Y-m-d') @ timestamp | 1,534 | 0% (−1 … +2) | 0% (−2 … +5) |
| date('Y-m-d H:i:s') @ timestamp | 1,932 | 0% (−1 … +2) | 0% (−1 … +2) |
| date('Y-m-d\\TH:i:sP') @ timestamp | 2,113 | 0% (−1 … +1) | 0% (0 … +1) |
| format('p') @ UTC | 314 | 0% (−3 … +2) | −1% (−5 … +1) |
| format('p') @ Europe/Madrid | 803 | 0% (−1 … +3) | 0% (−1 … +1) |
| format('p') @ offset +05:30 | 541 | 0% (−2 … +3) | 0% (−1 … +1) |
| format('p') @ abbreviation EST | 417 | 0% (−1 … +1) | 0% (−1 … +2) |
| format('e') @ UTC | 299 | 0% (−1 … +3) | 0% (−1 … +2) |
| format('e') @ Europe/Madrid | 658 | 0% (0 … +1) | 0% (−1 … +1) |
| format('e') @ offset +05:30 | 473 | 0% (−1 … +2) | 0% (−3 … +5) |
| format('e') @ abbreviation EST | 260 | 0% (−3 … +1) | 0% (−1 … +1) |
| format('Y-m-d H:i:s T (P)') @ UTC | 1,331 | 0% (−2 … +1) | 0% (−2 … +1) |
| format('Y-m-d H:i:s T (P)') @ Europe/Madrid | 1,655 | 0% (−2 … +1) | 0% (−1 … +4) |
| format('Y-m-d H:i:s T (P)') @ offset +05:30 | 1,440 | 0% (−3 … +1) | 0% (−2 … +1) |
| format('Y-m-d H:i:s T (P)') @ abbreviation EST | 1,292 | 0% (−1 … +31) | 0% (−2 … +2) |
| format('P T e I Z') @ UTC | 791 | 0% (−1 … +1) | 0% (−1 … +3) |
| format('P T e I Z') @ Europe/Madrid | 1,171 | 0% (0 … +1) | 0% (−1 … +1) |
| format('P T e I Z') @ offset +05:30 | 988 | 0% (−3 … +2) | 0% (−2 … +2) |
| format('P T e I Z') @ abbreviation EST | 758 | 0% (−1 … +4) | 0% (−1 … +6) |

~: within noise, the change is no larger than the difference between master and master on the same row.

layout?: in every pass the cycles changed in the same direction, by 3% or more in the median, the instructions by less than 0.5%: the work is the same, so look for the cause (code placement, branch prediction) with `bench why` before reporting the row.
<!-- /bench-table -->

## Earlier version: scan before the loop

The first version scanned the format before the loop and built the offset when it found a character that prints it. Same machine and flags, 15 passes ([`earlier-series.json`](earlier-series.json)). Not the code of the branch: in `earlier-series.json` the build names `k14off-*` stand for that earlier commit.

<!-- bench-table earlier-series.json --full -->
| call | master, CPU cycles per call (GCC 15.2) | GCC 15.2 | clang 21.1 | instructions |
|---|--:|--:|--:|--:|
| format('Y') @ UTC | 416 | −39% (−40 … −39) | −25% (−27 … −25) | −26% … −22% |
| format('Y') @ Europe/Madrid | 745 | −66% (−66 … −66) | −63% (−64 … −61) | −63% … −62% |
| format('Y') @ America/New_York | 722 | −65% (−66 … −65) | −62% (−62 … −61) | −61% … −60% |
| format('Y') @ offset +05:30 | 441 | −43% (−46 … −30) | −47% (−47 … −42) | −44% |
| format('Y') @ abbreviation EST | 350 | −28% (−29 … −27) | −20% (−21 … −19) | −21% … −18% |
| format('Y-m-d') @ UTC | 633 | −29% (−29 … −26) | −12% (−14 … −10) | −15% … −13% |
| format('Y-m-d') @ Europe/Madrid | 959 | −52% (−53 … −52) | −45% (−45 … −44) | −48% … −47% |
| format('Y-m-d') @ America/New_York | 926 | −51% (−52 … −51) | −44% (−44 … −42) | −46% |
| format('Y-m-d') @ offset +05:30 | 670 | −33% (−36 … −32) | −25% (−27 … −23) | −30% |
| format('Y-m-d') @ abbreviation EST | 584 | −23% (−24 … −21) | −9% (−11 … −7) | −11% … −9% |
| format('Y-m-d H:i:s') @ UTC | 1,036 | −15% (−18 … −14) | −5% (−6 … −1) | −8% … −7% |
| format('Y-m-d H:i:s') @ Europe/Madrid | 1,260 | −39% (−40 … −39) | −27% (−28 … −25) | −36% … −35% |
| format('Y-m-d H:i:s') @ America/New_York | 1,334 | −35% (−35 … −34) | −29% (−30 … −26) | −34% … −33% |
| format('Y-m-d H:i:s') @ offset +05:30 | 1,085 | −20% (−22 … −18) | −13% (−16 … −11) | −20% … −19% |
| format('Y-m-d H:i:s') @ abbreviation EST | 984 | −11% (−13 … −10) | −3% (−5 … −1) | −6% … −4% |
| format('H:i') @ UTC | 475 | −38% (−40 … −38) | −27% (−28 … −26) | −21% … −18% |
| format('H:i') @ Europe/Madrid | 814 | −64% (−64 … −63) | −61% (−62 … −59) | −57% |
| format('H:i') @ America/New_York | 790 | −63% (−64 … −62) | −59% (−60 … −59) | −55% |
| format('H:i') @ offset +05:30 | 508 | −42% (−43 … −41) | −39% (−39 … −37) | −39% … −38% |
| format('H:i') @ abbreviation EST | 415 | −30% (−31 … −30) | −23% (−24 … −22) | −17% … −14% |
| format('D, d M Y') @ UTC | 731 | −23% (−25 … −22) | −8% (−10 … −8) | −12% … −10% |
| format('D, d M Y') @ Europe/Madrid | 1,062 | −47% (−47 … −46) | −39% (−39 … −38) | −43% … −42% |
| format('D, d M Y') @ America/New_York | 1,029 | −45% (−46 … −41) | −38% (−38 … −36) | −41% |
| format('D, d M Y') @ offset +05:30 | 790 | −29% (−31 … −28) | −20% (−21 … −19) | −26% … −25% |
| format('D, d M Y') @ abbreviation EST | 687 | −19% (−20 … −18) | −5% (−7 … −3) | −8% … −7% |
| format('Y-m-d\TH:i:s.u') @ UTC | 1,107 | −17% (−19 … −16) | −2% (−4 … 0) | −7% … −5% |
| format('Y-m-d\TH:i:s.u') @ Europe/Madrid | 1,444 | −36% (−37 … −35) | −26% (−27 … −25) | −32% … −31% |
| format('Y-m-d\TH:i:s.u') @ America/New_York | 1,399 | −34% (−35 … −32) | −25% (−26 … −24) | −30% |
| format('Y-m-d\TH:i:s.u') @ offset +05:30 | 1,156 | −21% (−24 … −19) | −11% (−12 … −10) | −17% |
| format('Y-m-d\TH:i:s.u') @ abbreviation EST | 1,054 | −13% (−15 … −11) | 0% (−2 … +3) ~ | −4% … −3% |
| format('U') @ UTC | 395 | −42% (−42 … −38) | −30% (−31 … −29) | −26% … −23% |
| format('U') @ Europe/Madrid | 735 | −69% (−70 … −68) | −67% (−67 … −66) | −63% … −62% |
| format('U') @ America/New_York | 712 | −67% (−68 … −63) | −65% (−65 … −65) | −61% … −60% |
| format('U') @ offset +05:30 | 429 | −46% (−47 … −45) | −49% (−53 … −47) | −45% … −44% |
| format('U') @ abbreviation EST | 342 | −32% (−35 … −26) | −24% (−25 … −22) | −21% … −18% |
| format('c') @ UTC | 813 | −3% (−4 … −3) layout? | +4% (+3 … +5) layout? | 0% |
| format('c') @ Europe/Madrid | 1,129 | −1% (−3 … +2) | +2% (0 … +3) | 0% |
| format('c') @ America/New_York | 1,122 | −1% (−5 … −1) | +2% (0 … +5) | 0% |
| format('c') @ offset +05:30 | 833 | +3% (+2 … +7) | +6% (+2 … +8) layout? | 0% |
| format('c') @ abbreviation EST | 747 | 0% (−1 … 0) | +2% (+1 … +3) | 0% … +1% |
| format('Y-m-d\TH:i:sP') @ UTC | 1,222 | −6% (−7 … −3) | +6% (+5 … +8) | +3% |
| format('Y-m-d\TH:i:sP') @ Europe/Madrid | 1,472 | +1% (−1 … +5) | +7% (+5 … +8) | +2% |
| format('Y-m-d\TH:i:sP') @ America/New_York | 1,502 | −1% (−3 … +1) | +5% (−6 … +6) | +2% |
| format('Y-m-d\TH:i:sP') @ offset +05:30 | 1,254 | −3% (−6 … +2) | +7% (+6 … +12) | +2% … +3% |
| format('Y-m-d\TH:i:sP') @ abbreviation EST | 1,145 | −4% (−5 … 0) | +6% (+5 … +8) | +3% |
| format('D, d M Y H:i:s O') @ UTC | 1,332 | −4% (−5 … 0) | +5% (−3 … +7) | +3% |
| format('D, d M Y H:i:s O') @ Europe/Madrid | 1,640 | 0% (−1 … +3) | +5% (+4 … +7) | +2% … +3% |
| format('D, d M Y H:i:s O') @ America/New_York | 1,615 | 0% (−2 … +2) | +5% (+2 … +7) | +2% … +3% |
| format('D, d M Y H:i:s O') @ offset +05:30 | 1,392 | −3% (−5 … +1) | +10% (+9 … +14) | +3% |
| format('D, d M Y H:i:s O') @ abbreviation EST | 1,261 | −3% (−5 … 0) | +7% (+4 … +8) | +3% |
| format('T') @ UTC | 337 | −7% (−8 … −6) | +1% (−1 … +2) | +1% |
| format('T') @ Europe/Madrid | 683 | −1% (−2 … 0) | +1% (0 … +3) | 0% … +1% |
| format('T') @ America/New_York | 655 | −2% (−5 … +1) | 0% (−1 … 0) | 0% … +1% |
| format('T') @ offset +05:30 | 384 | +4% (+3 … +4) | +1% (0 … +2) | +1% |
| format('T') @ abbreviation EST | 287 | −4% (−7 … +2) | +2% (0 … +3) | +1% |
| date('Y-m-d') @ timestamp | 867 | −14% (−16 … −13) | −6% (−7 … −5) | −11% … −9% |
| date('Y-m-d H:i:s') @ timestamp | 1,278 | −6% (−7 … −5) | −1% (−5 … 0) | −6% … −5% |
| date(DATE_ATOM) @ timestamp | 1,430 | +1% (−4 … +3) | +5% (+3 … +7) | +2% … +3% |

Control: master against itself.

| call | master, CPU cycles per call (GCC 15.2) | A/A start | A/A end |
|---|--:|--:|--:|
| format('Y') @ UTC | 415 | 0% (−1 … +1) | 0% (−1 … +1) |
| format('Y') @ Europe/Madrid | 745 | 0% (0 … +1) | 0% (−1 … 0) |
| format('Y') @ America/New_York | 720 | 0% (−1 … +1) | 0% (0 … +3) |
| format('Y') @ offset +05:30 | 439 | 0% (−8 … +2) | 0% (−1 … +1) |
| format('Y') @ abbreviation EST | 350 | 0% (−2 … +4) | 0% (0 … +1) |
| format('Y-m-d') @ UTC | 621 | 0% (−1 … +1) | 0% (−1 … +1) |
| format('Y-m-d') @ Europe/Madrid | 955 | 0% (−1 … +1) | 0% (0 … +1) |
| format('Y-m-d') @ America/New_York | 922 | 0% (−1 … +1) | 0% (−1 … +1) |
| format('Y-m-d') @ offset +05:30 | 669 | 0% (−2 … +3) | 0% (−9 … +2) |
| format('Y-m-d') @ abbreviation EST | 579 | 0% (0 … +1) | 0% (−3 … +2) |
| format('Y-m-d H:i:s') @ UTC | 1,032 | 0% (0 … +1) | 0% (−1 … 0) |
| format('Y-m-d H:i:s') @ Europe/Madrid | 1,257 | 0% (−2 … +5) | 0% (−1 … +1) |
| format('Y-m-d H:i:s') @ America/New_York | 1,333 | 0% (−1 … 0) | 0% (−1 … +2) |
| format('Y-m-d H:i:s') @ offset +05:30 | 1,079 | 0% (−3 … +3) | 0% (−1 … +4) |
| format('Y-m-d H:i:s') @ abbreviation EST | 984 | 0% (−1 … +1) | 0% (−1 … +2) |
| format('H:i') @ UTC | 476 | 0% (−1 … +1) | 0% (−1 … 0) |
| format('H:i') @ Europe/Madrid | 814 | 0% (−1 … +3) | 0% (−1 … +2) |
| format('H:i') @ America/New_York | 791 | 0% (−1 … 0) | 0% (−4 … 0) |
| format('H:i') @ offset +05:30 | 508 | 0% (−1 … +1) | 0% (−1 … +1) |
| format('H:i') @ abbreviation EST | 418 | 0% (−2 … +2) | 0% (−1 … +1) |
| format('D, d M Y') @ UTC | 726 | 0% (−1 … +1) | 0% (−2 … +3) |
| format('D, d M Y') @ Europe/Madrid | 1,062 | 0% (−1 … +2) | 0% (−1 … +2) |
| format('D, d M Y') @ America/New_York | 1,028 | 0% (−1 … +1) | 0% (−2 … +1) |
| format('D, d M Y') @ offset +05:30 | 787 | 0% (−1 … +2) | 0% (−1 … +1) |
| format('D, d M Y') @ abbreviation EST | 689 | 0% (−1 … +1) | 0% (−1 … +1) |
| format('Y-m-d\TH:i:s.u') @ UTC | 1,113 | 0% (−1 … +1) | 0% (−1 … +1) |
| format('Y-m-d\TH:i:s.u') @ Europe/Madrid | 1,439 | 0% (−1 … +1) | 0% (−1 … +1) |
| format('Y-m-d\TH:i:s.u') @ America/New_York | 1,397 | 0% (−1 … +1) | 0% (−1 … +1) |
| format('Y-m-d\TH:i:s.u') @ offset +05:30 | 1,154 | 0% (−3 … +1) | 0% (−3 … +3) |
| format('Y-m-d\TH:i:s.u') @ abbreviation EST | 1,047 | 0% (−1 … +1) | 0% (−1 … +2) |
| format('U') @ UTC | 380 | −1% (−2 … +1) | 0% (−5 … +4) |
| format('U') @ Europe/Madrid | 734 | 0% (−1 … +1) | 0% (−1 … 0) |
| format('U') @ America/New_York | 706 | 0% (−1 … +2) | 0% (−1 … +1) |
| format('U') @ offset +05:30 | 428 | 0% (−1 … +4) | 0% (−9 … +3) |
| format('U') @ abbreviation EST | 342 | 0% (−4 … +6) | 0% (−1 … +2) |
| format('c') @ UTC | 811 | 0% (−3 … +1) | 0% (−5 … 0) |
| format('c') @ Europe/Madrid | 1,125 | 0% (−1 … +1) | 0% (−1 … +1) |
| format('c') @ America/New_York | 1,115 | 0% (−4 … +1) | 0% (0 … +1) |
| format('c') @ offset +05:30 | 831 | 0% (0 … +1) | 0% (−2 … 0) |
| format('c') @ abbreviation EST | 748 | 0% (−1 … +1) | 0% (−1 … +8) |
| format('Y-m-d\TH:i:sP') @ UTC | 1,216 | 0% (−1 … +2) | 0% (−2 … +1) |
| format('Y-m-d\TH:i:sP') @ Europe/Madrid | 1,470 | 0% (−1 … +1) | 0% (−1 … +1) |
| format('Y-m-d\TH:i:sP') @ America/New_York | 1,502 | 0% (−1 … +1) | 0% (−2 … +1) |
| format('Y-m-d\TH:i:sP') @ offset +05:30 | 1,248 | 0% (−2 … +3) | 0% (−3 … +2) |
| format('Y-m-d\TH:i:sP') @ abbreviation EST | 1,146 | 0% (−1 … +3) | 0% (−1 … +2) |
| format('D, d M Y H:i:s O') @ UTC | 1,324 | 0% (−2 … +1) | 0% (−9 … +10) |
| format('D, d M Y H:i:s O') @ Europe/Madrid | 1,645 | 0% (−1 … +1) | 0% (−1 … +3) |
| format('D, d M Y H:i:s O') @ America/New_York | 1,611 | 0% (−1 … +1) | 0% (−1 … +1) |
| format('D, d M Y H:i:s O') @ offset +05:30 | 1,385 | 0% (−1 … +1) | 0% (−2 … +2) |
| format('D, d M Y H:i:s O') @ abbreviation EST | 1,262 | 0% (−2 … +2) | 0% (−1 … +2) |
| format('T') @ UTC | 338 | 0% (−1 … +1) | 0% (−1 … +50) |
| format('T') @ Europe/Madrid | 682 | 0% (−1 … +1) | 0% (−1 … +3) |
| format('T') @ America/New_York | 654 | 0% (−2 … +2) | 0% (−1 … +1) |
| format('T') @ offset +05:30 | 383 | 0% (−2 … +4) | 0% (−1 … 0) |
| format('T') @ abbreviation EST | 287 | 0% (−3 … +1) | 0% (−11 … +1) |
| date('Y-m-d') @ timestamp | 863 | 0% (−1 … +2) | 0% (−1 … +1) |
| date('Y-m-d H:i:s') @ timestamp | 1,271 | 0% (−1 … +2) | 0% (−11 … +2) |
| date(DATE_ATOM) @ timestamp | 1,427 | 0% (−2 … +2) | 0% (−2 … +1) |

~: within noise, the change is no larger than the difference between master and master on the same row.

layout?: in every pass the cycles changed in the same direction, by 3% or more in the median, the instructions by less than 0.5%: the work is the same, so look for the cause (code placement, branch prediction) with `bench why` before reporting the row.
<!-- /bench-table -->
