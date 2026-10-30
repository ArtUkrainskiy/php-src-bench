# Synthetic routing boundary grid

Supplementary guards, not a frequency distribution of everyday requests. These compare the same final candidate and base. Every original pass, A/A control and warning remains visible.

## amd-boundaries

<!-- bench-table ../data/stress/amd-boundaries.json --header --full -->
Machine: AMD Ryzen 9 5950X 16-Core Processor, CPU 15, kernel 7.0.0-38-generic.
Group gcc15: A = base-gcc15 (ef99f4248f1 GCC 15.2, profile docker), B = product-guard-gcc15 (ca89fb5fb96 GCC 15.2, profile docker).
Group clang21: A = base-clang21 (ef99f4248f1 clang 21.1, profile docker), B = product-guard-clang21 (ca89fb5fb96 clang 21.1, profile docker).
5 alternating passes per case, user-space cycles per call (perf stat, minus the empty loop), A against A at the start and the end.
Machine: turbo boost is on: thermal and frequency drift between rounds (sudo ./bench tune on).
negative = fewer cycles (faster)

| call | master, CPU cycles per call (GCC 15.2) | GCC 15.2 | clang 21.1 | instructions |
|---|--:|--:|--:|--:|
| dense-prefix/n31/h8191 @ dense-prefix/n31/h8191 | 157,884 | +2% (−1 … +7) | −41% (−42 … −38) layout? | 0% |
| periodic/n31/h8191 @ periodic/n31/h8191 | 84,020 | +11% (+6 … +17) layout? | −30% (−31 … −29) layout? | 0% |
| ordinary-miss/n31/h8191 @ ordinary-miss/n31/h8191 | 5,130 | −10% (−11 … −8) | −10% (−11 … −10) | −2% … −1% |
| early-match/n31/h8191 @ early-match/n31/h8191 | 148 | −24% (−26 … −22) | −36% (−43 … −21) | −19% … −8% |
| late-match/n31/h8191 @ late-match/n31/h8191 | 5,082 | −8% (−14 … −8) | −10% (−11 … −10) | −2% … −1% |
| dense-prefix/n31/h8192 @ dense-prefix/n31/h8192 | 145,106 | +8% (+7 … +16) layout? | −39% (−40 … −38) layout? | 0% |
| periodic/n31/h8192 @ periodic/n31/h8192 | 84,163 | +11% (+5 … +19) layout? | −30% (−32 … −29) layout? | 0% |
| ordinary-miss/n31/h8192 @ ordinary-miss/n31/h8192 | 5,131 | −11% (−19 … −8) | −10% (−11 … −10) | −2% … −1% |
| early-match/n31/h8192 @ early-match/n31/h8192 | 151 | −26% (−28 … −23) | −36% (−37 … −28) | −19% … −8% |
| late-match/n31/h8192 @ late-match/n31/h8192 | 5,283 | −14% (−14 … −10) | −10% (−11 … −9) | −2% … −1% |
| dense-prefix/n31/h8193 @ dense-prefix/n31/h8193 | 154,990 | 0% (−1 … +6) ~ | −41% (−42 … −39) layout? | 0% |
| periodic/n31/h8193 @ periodic/n31/h8193 | 84,368 | +10% (+7 … +16) layout? | −31% (−31 … −30) layout? | 0% |
| ordinary-miss/n31/h8193 @ ordinary-miss/n31/h8193 | 5,133 | −10% (−12 … −6) | −10% (−10 … −10) | −2% … −1% |
| early-match/n31/h8193 @ early-match/n31/h8193 | 149 | −25% (−29 … −22) | −29% (−36 … −26) | −19% … −8% |
| late-match/n31/h8193 @ late-match/n31/h8193 | 5,180 | −10% (−12 … −8) | −10% (−11 … −10) | −2% … −1% |
| dense-prefix/n31/h65536 @ dense-prefix/n31/h65536 | 1,157,924 | +11% (+4 … +17) layout? | −40% (−42 … −35) layout? | 0% |
| periodic/n31/h65536 @ periodic/n31/h65536 | 669,041 | +11% (+6 … +20) layout? | −32% (−33 … −29) layout? | 0% |
| ordinary-miss/n31/h65536 @ ordinary-miss/n31/h65536 | 39,837 | −10% (−11 … −8) layout? | −10% (−10 … −10) layout? | 0% |
| early-match/n31/h65536 @ early-match/n31/h65536 | 152 | −16% (−26 … −11) | −36% (−38 … −26) | −19% … −8% |
| late-match/n31/h65536 @ late-match/n31/h65536 | 39,832 | −10% (−14 … −8) layout? | −10% (−11 … −10) layout? | 0% |
| dense-prefix/n32/h8191 @ dense-prefix/n32/h8191 | 147,827 | +8% (+3 … +11) layout? | −36% (−38 … −35) layout? | 0% |
| periodic/n32/h8191 @ periodic/n32/h8191 | 73,107 | +5% (+4 … +10) layout? | −37% (−40 … −30) | −1% … 0% |
| ordinary-miss/n32/h8191 @ ordinary-miss/n32/h8191 | 5,142 | −1% (−4 … 0) ~ | +2% (+2 … +3) | −6% … 0% |
| early-match/n32/h8191 @ early-match/n32/h8191 | 151 | +1% (−1 … +3) | −9% (−12 … −9) | +1% … +4% |
| late-match/n32/h8191 @ late-match/n32/h8191 | 5,177 | +1% (−4 … +10) | +2% (+2 … +3) | −6% … 0% |
| dense-prefix/n32/h8192 @ dense-prefix/n32/h8192 | 159,378 | −98% (−100 … −98) | −99% (−99 … −99) | −99% … −98% |
| periodic/n32/h8192 @ periodic/n32/h8192 | 76,955 | −90% (−91 … −88) | −93% (−94 … −93) | −92% … −91% |
| ordinary-miss/n32/h8192 @ ordinary-miss/n32/h8192 | 5,139 | −1% (−2 … +1) | 0% (0 … +1) | 0% … +11% |
| early-match/n32/h8192 @ early-match/n32/h8192 | 150 | +3% (−4 … +6) | +1% (0 … +3) ~ | +4% … +23% |
| late-match/n32/h8192 @ late-match/n32/h8192 | 5,175 | −1% (−2 … 0) ~ | 0% (0 … +1) ~ | 0% … +12% |
| dense-prefix/n32/h8193 @ dense-prefix/n32/h8193 | 151,819 | n/a (instructions −99%) | −99% (−99 … −99) | −98% |
| periodic/n32/h8193 @ periodic/n32/h8193 | 71,871 | −88% (−90 … −85) | −93% (−94 … −93) | −92% … −91% |
| ordinary-miss/n32/h8193 @ ordinary-miss/n32/h8193 | 5,034 | 0% (−3 … +3) ~ | 0% (0 … +1) ~ | 0% … +11% |
| early-match/n32/h8193 @ early-match/n32/h8193 | 150 | +4% (+2 … +6) | +2% (0 … +3) ~ | +4% … +23% |
| late-match/n32/h8193 @ late-match/n32/h8193 | 5,198 | −3% (−3 … +1) | 0% (−2 … +1) | 0% … +12% |
| dense-prefix/n32/h65536 @ dense-prefix/n32/h65536 | 1,287,376 | n/a (instructions −99%) | −99% (−99 … −99) | −99% |
| periodic/n32/h65536 @ periodic/n32/h65536 | 619,360 | −90% (−92 … −88) | −94% (−94 … −94) | −93% |
| ordinary-miss/n32/h65536 @ ordinary-miss/n32/h65536 | 40,293 | −2% (−3 … +1) | +1% (0 … +1) | 0% … +11% |
| early-match/n32/h65536 @ early-match/n32/h65536 | 153 | +1% (0 … +3) | +2% (0 … +3) | +4% … +23% |
| late-match/n32/h65536 @ late-match/n32/h65536 | 40,215 | −1% (−2 … +1) | +1% (0 … +1) | 0% … +11% |
| dense-prefix/n33/h8191 @ dense-prefix/n33/h8191 | 163,643 | 0% (−1 … +1) ~ | −38% (−40 … −38) layout? | 0% |
| periodic/n33/h8191 @ periodic/n33/h8191 | 88,341 | +12% (+9 … +16) layout? | −28% (−30 … −27) | −1% … 0% |
| ordinary-miss/n33/h8191 @ ordinary-miss/n33/h8191 | 8,864 | −1% (−1 … +2) ~ | 0% (0 … 0) ~ | −7% … 0% |
| early-match/n33/h8191 @ early-match/n33/h8191 | 152 | +9% (+3 … +15) | −10% (−10 … −9) | +1% … +4% |
| late-match/n33/h8191 @ late-match/n33/h8191 | 8,902 | −1% (−3 … +1) ~ | 0% (−1 … 0) ~ | −7% … 0% |
| dense-prefix/n33/h8192 @ dense-prefix/n33/h8192 | 153,548 | n/a (instructions −99%) | −99% (−99 … −99) | −98% |
| periodic/n33/h8192 @ periodic/n33/h8192 | 88,499 | −89% (−92 … −87) | −94% (−94 … −94) | −92% |
| ordinary-miss/n33/h8192 @ ordinary-miss/n33/h8192 | 8,843 | +1% (−3 … +2) | −1% (−1 … 0) | 0% … +7% |
| early-match/n33/h8192 @ early-match/n33/h8192 | 153 | +4% (−1 … +6) | 0% (−2 … +5) ~ | +4% … +23% |
| late-match/n33/h8192 @ late-match/n33/h8192 | 8,863 | 0% (−1 … +1) ~ | −1% (−1 … 0) ~ | 0% … +8% |
| dense-prefix/n33/h8193 @ dense-prefix/n33/h8193 | 162,352 | n/a (instructions −99%) | −99% (−99 … −99) | −98% |
| periodic/n33/h8193 @ periodic/n33/h8193 | 90,031 | −90% (−90 … −88) | −94% (−94 … −93) | −92% |
| ordinary-miss/n33/h8193 @ ordinary-miss/n33/h8193 | 8,843 | −1% (−3 … +2) ~ | 0% (−1 … 0) ~ | 0% … +7% |
| early-match/n33/h8193 @ early-match/n33/h8193 | 156 | +2% (0 … +4) | −1% (−4 … +2) | +4% … +23% |
| late-match/n33/h8193 @ late-match/n33/h8193 | 8,897 | −3% (−5 … +2) | −1% (−1 … 0) ~ | 0% … +8% |
| dense-prefix/n33/h65536 @ dense-prefix/n33/h65536 | 1,231,559 | n/a (instructions −99%) | −99% (−99 … −99) | −99% |
| periodic/n33/h65536 @ periodic/n33/h65536 | 717,210 | −91% (−91 … −89) | −95% (−95 … −94) | −94% … −93% |
| ordinary-miss/n33/h65536 @ ordinary-miss/n33/h65536 | 71,292 | −1% (−3 … 0) | −1% (−1 … 0) | 0% … +7% |
| early-match/n33/h65536 @ early-match/n33/h65536 | 155 | +4% (0 … +7) | 0% (−2 … +2) ~ | +4% … +23% |
| late-match/n33/h65536 @ late-match/n33/h65536 | 70,164 | 0% (−3 … +2) | −1% (−1 … 0) | 0% … +7% |
| dense-prefix/n64/h8191 @ dense-prefix/n64/h8191 | 278,711 | +38% (+31 … +42) layout? | −49% (−49 … −46) layout? | 0% |
| periodic/n64/h8191 @ periodic/n64/h8191 | 140,928 | +3% (−1 … +9) | −51% (−52 … −46) layout? | 0% |
| ordinary-miss/n64/h8191 @ ordinary-miss/n64/h8191 | 2,064 | −1% (−3 … +3) | 0% (−1 … 0) ~ | −5% … 0% |
| early-match/n64/h8191 @ early-match/n64/h8191 | 227 | −2% (−12 … +2) ~ | −22% (−23 … −22) | +1% … +3% |
| late-match/n64/h8191 @ late-match/n64/h8191 | 2,221 | −1% (−4 … 0) | −3% (−3 … −2) | −4% … 0% |
| dense-prefix/n64/h8192 @ dense-prefix/n64/h8192 | 288,757 | n/a (instructions −99%) | −99% (−99 … −99) | −99% |
| periodic/n64/h8192 @ periodic/n64/h8192 | 143,341 | −93% (−97 … −91) | −97% (−97 … −97) | −96% … −95% |
| ordinary-miss/n64/h8192 @ ordinary-miss/n64/h8192 | 2,063 | −1% (−3 … +1) ~ | 0% (0 … +1) ~ | +1% … +7% |
| early-match/n64/h8192 @ early-match/n64/h8192 | 222 | +1% (−13 … +5) ~ | −5% (−7 … +6) | +2% … +27% |
| late-match/n64/h8192 @ late-match/n64/h8192 | 2,213 | −2% (−8 … +1) ~ | −1% (−19 … 0) ~ | +1% … +12% |
| dense-prefix/n64/h8193 @ dense-prefix/n64/h8193 | 278,424 | n/a (instructions −99%) | −99% (−99 … −99) | −99% |
| periodic/n64/h8193 @ periodic/n64/h8193 | 137,267 | −94% (−94 … −91) | −97% (−97 … −97) | −96% … −95% |
| ordinary-miss/n64/h8193 @ ordinary-miss/n64/h8193 | 2,021 | +1% (−2 … +4) ~ | +1% (0 … +7) ~ | +1% … +7% |
| early-match/n64/h8193 @ early-match/n64/h8193 | 221 | +2% (0 … +7) | −5% (−6 … −5) | +2% … +27% |
| late-match/n64/h8193 @ late-match/n64/h8193 | 2,202 | −3% (−6 … −2) | −1% (−2 … +2) ~ | +1% … +12% |
| dense-prefix/n64/h65536 @ dense-prefix/n64/h65536 | 2,363,123 | n/a (instructions −100%) | −99% (−100 … −99) | −99% |
| periodic/n64/h65536 @ periodic/n64/h65536 | 1,150,591 | −96% (−98 … −93) | −98% (−98 … −98) | −97% |
| ordinary-miss/n64/h65536 @ ordinary-miss/n64/h65536 | 15,059 | +1% (−2 … +2) ~ | 0% (0 … 0) ~ | 0% … +7% |
| early-match/n64/h65536 @ early-match/n64/h65536 | 226 | +2% (−8 … +3) ~ | −6% (−7 … −4) | +2% … +27% |
| late-match/n64/h65536 @ late-match/n64/h65536 | 15,433 | 0% (−1 … +2) ~ | −1% (−1 … 0) | 0% … +8% |
| dense-prefix/n256/h8191 @ dense-prefix/n256/h8191 | 1,151,495 | −1% (−1 … +3) | −46% (−47 … −44) layout? | 0% |
| periodic/n256/h8191 @ periodic/n256/h8191 | 563,806 | +2% (0 … +5) | −46% (−47 … −45) layout? | 0% |
| ordinary-miss/n256/h8191 @ ordinary-miss/n256/h8191 | 1,580 | −2% (−3 … +3) ~ | +4% (+2 … +4) | −1% … 0% |
| early-match/n256/h8191 @ early-match/n256/h8191 | 688 | +1% (0 … +2) | −29% (−30 … −27) | 0% … +3% |
| late-match/n256/h8191 @ late-match/n256/h8191 | 2,186 | 0% (−6 … +4) ~ | −3% (−11 … −2) | −1% … 0% |
| dense-prefix/n256/h8192 @ dense-prefix/n256/h8192 | 1,103,793 | n/a (instructions −99%) | −99% (−99 … −99) | −99% |
| periodic/n256/h8192 @ periodic/n256/h8192 | 560,042 | −95% (−98 … −95) | −98% (−99 … −98) | −98% |
| ordinary-miss/n256/h8192 @ ordinary-miss/n256/h8192 | 1,612 | −2% (−4 … 0) | +3% (−1 … +4) | +1% … +9% |
| early-match/n256/h8192 @ early-match/n256/h8192 | 687 | 0% (−2 … +3) ~ | −4% (−5 … −3) | +1% … +31% |
| late-match/n256/h8192 @ late-match/n256/h8192 | 2,199 | −1% (−3 … 0) ~ | +1% (+1 … +3) ~ | 0% … +23% |
| dense-prefix/n256/h8193 @ dense-prefix/n256/h8193 | 1,134,985 | n/a (instructions −99%) | −99% (−99 … −99) | −99% |
| periodic/n256/h8193 @ periodic/n256/h8193 | 563,033 | −98% (−100 … −96) | −98% (−99 … −98) | −98% |
| ordinary-miss/n256/h8193 @ ordinary-miss/n256/h8193 | 1,579 | 0% (−1 … +4) ~ | +3% (+2 … +3) | +1% … +9% |
| early-match/n256/h8193 @ early-match/n256/h8193 | 676 | +2% (0 … +5) | −4% (−6 … −4) | +1% … +31% |
| late-match/n256/h8193 @ late-match/n256/h8193 | 2,192 | −3% (−7 … −1) layout? | +1% (+1 … +2) | 0% … +23% |
| dense-prefix/n256/h65536 @ dense-prefix/n256/h65536 | 9,325,374 | n/a (instructions −100%) | −100% (−100 … −100) | −100% |
| periodic/n256/h65536 @ periodic/n256/h65536 | 4,679,578 | −99% (−99 … −97) | −99% (−99 … −99) | −99% |
| ordinary-miss/n256/h65536 @ ordinary-miss/n256/h65536 | 10,960 | 0% (−2 … +1) ~ | +2% (0 … +4) | 0% … +11% |
| early-match/n256/h65536 @ early-match/n256/h65536 | 686 | +1% (−1 … +2) | −3% (−4 … −3) | +1% … +31% |
| late-match/n256/h65536 @ late-match/n256/h65536 | 11,679 | −1% (−2 … +3) ~ | +2% (0 … +4) | 0% … +14% |
| late-density/n32/remaining4095/absent @ late-density/n32/remaining4095/absent | 127,755 | −31% (−35 … −23) | −13% (−14 … −10) | +3% … +51% |
| late-density/n32/remaining4095/match @ late-density/n32/remaining4095/match | 128,887 | −30% (−33 … −29) | −12% (−14 … −9) | +3% … +51% |
| late-density/n32/remaining4096/absent @ late-density/n32/remaining4096/absent | 131,172 | −33% (−34 … −28) | −12% (−13 … −9) | +3% … +51% |
| late-density/n32/remaining4096/match @ late-density/n32/remaining4096/match | 131,372 | −33% (−36 … −28) | −11% (−12 … −9) | +3% … +51% |
| late-density/n32/remaining4097/absent @ late-density/n32/remaining4097/absent | 131,729 | −34% (−34 … −32) | −9% (−14 … −7) | +3% … +51% |
| late-density/n32/remaining4097/match @ late-density/n32/remaining4097/match | 128,589 | −32% (−33 … −31) | −11% (−12 … −9) | +3% … +51% |
| late-density/n256/remaining4095/absent @ late-density/n256/remaining4095/absent | 967,221 | −40% (−45 … −38) layout? | −7% (−8 … −6) | 0% … +50% |
| late-density/n256/remaining4095/match @ late-density/n256/remaining4095/match | 985,177 | −43% (−46 … −40) layout? | −7% (−8 … −7) | 0% … +50% |
| late-density/n256/remaining4096/absent @ late-density/n256/remaining4096/absent | 956,770 | −41% (−45 … −39) layout? | −7% (−8 … −6) | 0% … +50% |
| late-density/n256/remaining4096/match @ late-density/n256/remaining4096/match | 952,080 | −41% (−43 … −37) layout? | −7% (−7 … −7) | 0% … +50% |
| late-density/n256/remaining4097/absent @ late-density/n256/remaining4097/absent | 956,455 | −39% (−42 … −38) layout? | −7% (−8 … −7) | 0% … +50% |
| late-density/n256/remaining4097/match @ late-density/n256/remaining4097/match | 972,039 | −42% (−45 … −40) layout? | −7% (−7 … −7) | 0% … +50% |

Control: master against itself.

| call | master, CPU cycles per call (GCC 15.2) | A/A start | A/A end |
|---|--:|--:|--:|
| dense-prefix/n31/h8191 @ dense-prefix/n31/h8191 | 154,702 | +1% (−2 … +4) | −1% (−2 … +1) |
| periodic/n31/h8191 @ periodic/n31/h8191 | 83,974 | 0% (0 … +4) | −2% (−2 … 0) |
| ordinary-miss/n31/h8191 @ ordinary-miss/n31/h8191 | 5,112 | 0% (−4 … +4) | 0% (−2 … +2) |
| early-match/n31/h8191 @ early-match/n31/h8191 | 149 | −2% (−4 … +2) | 0% (−2 … +2) |
| late-match/n31/h8191 @ late-match/n31/h8191 | 5,175 | 0% (0 … +2) | 0% (−2 … 0) |
| dense-prefix/n31/h8192 @ dense-prefix/n31/h8192 | 143,329 | 0% (−4 … +2) | 0% (−2 … +3) |
| periodic/n31/h8192 @ periodic/n31/h8192 | 84,114 | 0% (−2 … +2) | −1% (−2 … 0) |
| ordinary-miss/n31/h8192 @ ordinary-miss/n31/h8192 | 5,117 | 0% (0 … +2) | −2% (−2 … +2) |
| early-match/n31/h8192 @ early-match/n31/h8192 | 148 | 0% (−2 … 0) | 0% (−14 … +2) |
| late-match/n31/h8192 @ late-match/n31/h8192 | 5,164 | 0% (−2 … 0) | 0% (−2 … +2) |
| dense-prefix/n31/h8193 @ dense-prefix/n31/h8193 | 155,207 | 0% (−2 … +4) | −2% (−4 … +2) |
| periodic/n31/h8193 @ periodic/n31/h8193 | 84,037 | 0% (−4 … +2) | 0% (0 … +2) |
| ordinary-miss/n31/h8193 @ ordinary-miss/n31/h8193 | 5,124 | −2% (−4 … +2) | +2% (0 … +2) |
| early-match/n31/h8193 @ early-match/n31/h8193 | 148 | 0% (−2 … 0) | 0% (−3 … +2) |
| late-match/n31/h8193 @ late-match/n31/h8193 | 5,164 | 0% (−4 … +2) | 0% (−4 … +2) |
| dense-prefix/n31/h65536 @ dense-prefix/n31/h65536 | 1,169,618 | 0% (−4 … +4) | 0% (−1 … +2) |
| periodic/n31/h65536 @ periodic/n31/h65536 | 678,476 | 0% (−4 … +3) | 0% (−3 … +2) |
| ordinary-miss/n31/h65536 @ ordinary-miss/n31/h65536 | 39,823 | 0% (−2 … 0) | 0% (−2 … +4) |
| early-match/n31/h65536 @ early-match/n31/h65536 | 148 | 0% (−3 … +2) | 0% (−2 … +1) |
| late-match/n31/h65536 @ late-match/n31/h65536 | 39,848 | 0% (−4 … +2) | 0% (−2 … +2) |
| dense-prefix/n32/h8191 @ dense-prefix/n32/h8191 | 147,195 | 0% (−7 … +3) | −2% (−6 … +6) |
| periodic/n32/h8191 @ periodic/n32/h8191 | 71,657 | 0% (−1 … +4) | −2% (−5 … −1) |
| ordinary-miss/n32/h8191 @ ordinary-miss/n32/h8191 | 5,118 | +2% (−2 … +4) | 0% (−2 … +4) |
| early-match/n32/h8191 @ early-match/n32/h8191 | 150 | 0% (0 … +2) | 0% (−3 … +1) |
| late-match/n32/h8191 @ late-match/n32/h8191 | 5,184 | 0% (−4 … +2) | 0% (−2 … +2) |
| dense-prefix/n32/h8192 @ dense-prefix/n32/h8192 | 159,398 | 0% (−2 … +2) | 0% (−2 … +1) |
| periodic/n32/h8192 @ periodic/n32/h8192 | 77,915 | 0% (−2 … +2) | −1% (−4 … +2) |
| ordinary-miss/n32/h8192 @ ordinary-miss/n32/h8192 | 5,225 | 0% (−2 … +2) | 0% (0 … +2) |
| early-match/n32/h8192 @ early-match/n32/h8192 | 150 | +1% (−2 … +4) | −2% (−2 … 0) |
| late-match/n32/h8192 @ late-match/n32/h8192 | 5,283 | −2% (−2 … 0) | 0% (−2 … 0) |
| dense-prefix/n32/h8193 @ dense-prefix/n32/h8193 | 147,363 | 0% (−2 … +2) | +2% (−1 … +2) |
| periodic/n32/h8193 @ periodic/n32/h8193 | 72,571 | 0% (−4 … +1) | −2% (−4 … 0) |
| ordinary-miss/n32/h8193 @ ordinary-miss/n32/h8193 | 5,117 | 0% (−2 … +2) | +2% (−2 … +2) |
| early-match/n32/h8193 @ early-match/n32/h8193 | 153 | −2% (−4 … +2) | 0% (−3 … +2) |
| late-match/n32/h8193 @ late-match/n32/h8193 | 5,173 | 0% (0 … +2) | 0% (0 … +2) |
| dense-prefix/n32/h65536 @ dense-prefix/n32/h65536 | 1,290,278 | −3% (−3 … −1) | +2% (−3 … +4) |
| periodic/n32/h65536 @ periodic/n32/h65536 | 622,063 | 0% (−1 … +5) | +1% (0 … +2) |
| ordinary-miss/n32/h65536 @ ordinary-miss/n32/h65536 | 40,225 | 0% (0 … +2) | 0% (−2 … +2) |
| early-match/n32/h65536 @ early-match/n32/h65536 | 150 | 0% (0 … +1) | +1% (−2 … +1) |
| late-match/n32/h65536 @ late-match/n32/h65536 | 40,208 | 0% (0 … +2) | 0% (−1 … +2) |
| dense-prefix/n33/h8191 @ dense-prefix/n33/h8191 | 160,845 | 0% (−1 … +4) | 0% (−2 … +1) |
| periodic/n33/h8191 @ periodic/n33/h8191 | 88,245 | 0% (−2 … 0) | 0% (−4 … 0) |
| ordinary-miss/n33/h8191 @ ordinary-miss/n33/h8191 | 8,844 | 0% (−2 … +2) | −2% (−4 … 0) |
| early-match/n33/h8191 @ early-match/n33/h8191 | 153 | 0% (−2 … +2) | 0% (−16 … +2) |
| late-match/n33/h8191 @ late-match/n33/h8191 | 8,683 | +4% (0 … +4) | 0% (0 … +2) |
| dense-prefix/n33/h8192 @ dense-prefix/n33/h8192 | 152,366 | 0% (−4 … +6) | −2% (−3 … +6) |
| periodic/n33/h8192 @ periodic/n33/h8192 | 88,325 | −2% (−2 … +2) | 0% (−2 … +2) |
| ordinary-miss/n33/h8192 @ ordinary-miss/n33/h8192 | 8,829 | 0% (0 … 0) | 0% (−2 … +4) |
| early-match/n33/h8192 @ early-match/n33/h8192 | 152 | 0% (−4 … +3) | 0% (−3 … +2) |
| late-match/n33/h8192 @ late-match/n33/h8192 | 8,876 | +2% (−2 … +2) | −2% (−2 … 0) |
| dense-prefix/n33/h8193 @ dense-prefix/n33/h8193 | 163,772 | 0% (−1 … +3) | 0% (−3 … +2) |
| periodic/n33/h8193 @ periodic/n33/h8193 | 88,301 | 0% (−2 … +2) | 0% (−2 … +4) |
| ordinary-miss/n33/h8193 @ ordinary-miss/n33/h8193 | 8,658 | +2% (0 … +4) | 0% (0 … 0) |
| early-match/n33/h8193 @ early-match/n33/h8193 | 152 | 0% (0 … 0) | 0% (−2 … +2) |
| late-match/n33/h8193 @ late-match/n33/h8193 | 8,878 | 0% (−2 … +2) | +2% (−4 … +4) |
| dense-prefix/n33/h65536 @ dense-prefix/n33/h65536 | 1,247,130 | −1% (−2 … +6) | +1% (0 … +4) |
| periodic/n33/h65536 @ periodic/n33/h65536 | 711,796 | 0% (−3 … +2) | −1% (−2 … +1) |
| ordinary-miss/n33/h65536 @ ordinary-miss/n33/h65536 | 69,857 | 0% (−2 … +2) | +1% (0 … +2) |
| early-match/n33/h65536 @ early-match/n33/h65536 | 155 | 0% (−2 … +2) | 0% (−3 … +2) |
| late-match/n33/h65536 @ late-match/n33/h65536 | 69,851 | 0% (0 … +2) | 0% (−2 … +2) |
| dense-prefix/n64/h8191 @ dense-prefix/n64/h8191 | 277,228 | 0% (−3 … +3) | 0% (−5 … +3) |
| periodic/n64/h8191 @ periodic/n64/h8191 | 136,557 | +1% (−3 … +6) | 0% (−5 … +3) |
| ordinary-miss/n64/h8191 @ ordinary-miss/n64/h8191 | 2,055 | 0% (−2 … +3) | 0% (0 … +2) |
| early-match/n64/h8191 @ early-match/n64/h8191 | 221 | +10% (0 … +15) | −9% (−11 … +2) |
| late-match/n64/h8191 @ late-match/n64/h8191 | 2,219 | 0% (−3 … +3) | +1% (−2 … +3) |
| dense-prefix/n64/h8192 @ dense-prefix/n64/h8192 | 295,946 | −3% (−5 … 0) | 0% (−2 … +3) |
| periodic/n64/h8192 @ periodic/n64/h8192 | 142,227 | 0% (−3 … +4) | 0% (−3 … +5) |
| ordinary-miss/n64/h8192 @ ordinary-miss/n64/h8192 | 2,056 | 0% (−2 … +1) | −1% (−2 … +2) |
| early-match/n64/h8192 @ early-match/n64/h8192 | 222 | 0% (−11 … +10) | +2% (−11 … +15) |
| late-match/n64/h8192 @ late-match/n64/h8192 | 2,253 | −2% (−3 … +2) | 0% (−2 … +3) |
| dense-prefix/n64/h8193 @ dense-prefix/n64/h8193 | 280,250 | 0% (−4 … +3) | +4% (−3 … +6) |
| periodic/n64/h8193 @ periodic/n64/h8193 | 140,681 | −1% (−3 … +1) | 0% (−3 … +5) |
| ordinary-miss/n64/h8193 @ ordinary-miss/n64/h8193 | 2,069 | +1% (−2 … +4) | 0% (−1 … +4) |
| early-match/n64/h8193 @ early-match/n64/h8193 | 221 | 0% (0 … +14) | 0% (−5 … +9) |
| late-match/n64/h8193 @ late-match/n64/h8193 | 2,214 | −1% (−4 … +3) | +1% (−1 … +4) |
| dense-prefix/n64/h65536 @ dense-prefix/n64/h65536 | 2,365,777 | 0% (−5 … +3) | +2% (0 … +3) |
| periodic/n64/h65536 @ periodic/n64/h65536 | 1,155,609 | 0% (−5 … +3) | +1% (−2 … +5) |
| ordinary-miss/n64/h65536 @ ordinary-miss/n64/h65536 | 15,317 | +1% (−1 … +2) | −1% (−3 … +2) |
| early-match/n64/h65536 @ early-match/n64/h65536 | 221 | 0% (−5 … +14) | −2% (−8 … +2) |
| late-match/n64/h65536 @ late-match/n64/h65536 | 15,386 | 0% (−4 … +2) | 0% (0 … +2) |
| dense-prefix/n256/h8191 @ dense-prefix/n256/h8191 | 1,126,250 | 0% (−2 … +1) | 0% (−2 … +2) |
| periodic/n256/h8191 @ periodic/n256/h8191 | 561,944 | 0% (−2 … +4) | 0% (−2 … +2) |
| ordinary-miss/n256/h8191 @ ordinary-miss/n256/h8191 | 1,578 | −2% (−31 … 0) | 0% (−2 … +4) |
| early-match/n256/h8191 @ early-match/n256/h8191 | 688 | 0% (−2 … 0) | 0% (0 … +2) |
| late-match/n256/h8191 @ late-match/n256/h8191 | 2,187 | −2% (−2 … +2) | +2% (−3 … +2) |
| dense-prefix/n256/h8192 @ dense-prefix/n256/h8192 | 1,130,002 | −1% (−2 … +3) | 0% (−2 … +2) |
| periodic/n256/h8192 @ periodic/n256/h8192 | 558,471 | +2% (−3 … +2) | 0% (−2 … +2) |
| ordinary-miss/n256/h8192 @ ordinary-miss/n256/h8192 | 1,574 | 0% (−1 … +4) | −1% (−2 … +2) |
| early-match/n256/h8192 @ early-match/n256/h8192 | 686 | 0% (−2 … +2) | 0% (−2 … +2) |
| late-match/n256/h8192 @ late-match/n256/h8192 | 2,149 | +2% (−1 … +2) | 0% (−1 … +1) |
| dense-prefix/n256/h8193 @ dense-prefix/n256/h8193 | 1,127,999 | −1% (−3 … 0) | 0% (−2 … +1) |
| periodic/n256/h8193 @ periodic/n256/h8193 | 552,350 | +2% (+1 … +5) | 0% (−3 … +1) |
| ordinary-miss/n256/h8193 @ ordinary-miss/n256/h8193 | 1,549 | +2% (−2 … +2) | 0% (−2 … +12) |
| early-match/n256/h8193 @ early-match/n256/h8193 | 688 | 0% (−2 … +3) | 0% (−2 … +2) |
| late-match/n256/h8193 @ late-match/n256/h8193 | 2,172 | 0% (−4 … +2) | 0% (−2 … +2) |
| dense-prefix/n256/h65536 @ dense-prefix/n256/h65536 | 9,211,647 | +1% (0 … +3) | 0% (0 … +2) |
| periodic/n256/h65536 @ periodic/n256/h65536 | 4,631,650 | +1% (0 … +3) | 0% (−3 … +2) |
| ordinary-miss/n256/h65536 @ ordinary-miss/n256/h65536 | 10,974 | 0% (−1 … +2) | +1% (−1 … +2) |
| early-match/n256/h65536 @ early-match/n256/h65536 | 687 | 0% (−2 … +4) | 0% (0 … +5) |
| late-match/n256/h65536 @ late-match/n256/h65536 | 11,576 | −1% (−2 … +3) | −1% (−2 … 0) |
| late-density/n32/remaining4095/absent @ late-density/n32/remaining4095/absent | 130,984 | −1% (−2 … +1) | −1% (−3 … +4) |
| late-density/n32/remaining4095/match @ late-density/n32/remaining4095/match | 128,343 | +1% (−5 … +3) | 0% (−2 … +1) |
| late-density/n32/remaining4096/absent @ late-density/n32/remaining4096/absent | 130,242 | 0% (−6 … +2) | 0% (−4 … +3) |
| late-density/n32/remaining4096/match @ late-density/n32/remaining4096/match | 128,673 | −1% (−2 … +5) | 0% (−2 … +2) |
| late-density/n32/remaining4097/absent @ late-density/n32/remaining4097/absent | 131,059 | −2% (−30 … +2) | +4% (0 … +5) |
| late-density/n32/remaining4097/match @ late-density/n32/remaining4097/match | 129,904 | 0% (−3 … +2) | +1% (0 … +2) |
| late-density/n256/remaining4095/absent @ late-density/n256/remaining4095/absent | 953,959 | −3% (−4 … +4) | +2% (−1 … +3) |
| late-density/n256/remaining4095/match @ late-density/n256/remaining4095/match | 971,327 | −1% (−5 … +3) | −1% (−4 … +3) |
| late-density/n256/remaining4096/absent @ late-density/n256/remaining4096/absent | 947,723 | 0% (−1 … +6) | 0% (−6 … +3) |
| late-density/n256/remaining4096/match @ late-density/n256/remaining4096/match | 974,297 | −3% (−4 … +2) | +1% (−1 … +5) |
| late-density/n256/remaining4097/absent @ late-density/n256/remaining4097/absent | 945,580 | +1% (−3 … +5) | 0% (−2 … +4) |
| late-density/n256/remaining4097/match @ late-density/n256/remaining4097/match | 965,744 | 0% (−2 … +1) | 0% (−5 … +3) |

~: the change is not larger than the A/A control of the same row: not evidence of a difference.

layout?: in every pass the cycles changed in the same direction, by 3% or more in the median, the instructions by less than 0.5%: the work is the same, so look for the cause (code placement, branch prediction) with `bench why` before reporting the row.

n/a: under 20 cycles per call, the subtraction of the empty loop dominates; compare instructions.
<!-- /bench-table -->

## intel-boundaries

<!-- bench-table ../data/stress/intel-boundaries.json --header --full -->
Machine: 13th Gen Intel(R) Core(TM) i7-13700H, CPU 10, kernel 7.0.0-38-generic.
Group gcc13: A = base-gcc13 (ef99f4248f1 GCC 13.3, profile docker), B = product-guard-gcc13 (ca89fb5fb96 GCC 13.3, profile docker).
Group gcc14: A = base-gcc14 (ef99f4248f1 GCC 14.2, profile docker), B = product-guard-gcc14 (ca89fb5fb96 GCC 14.2, profile docker).
Group clang18: A = base-clang18 (ef99f4248f1 clang 18.1, profile docker), B = product-guard-clang18 (ca89fb5fb96 clang 18.1, profile docker).
Group clang20: A = base-clang20 (ef99f4248f1 clang 20.1, profile docker), B = product-guard-clang20 (ca89fb5fb96 clang 20.1, profile docker).
5 alternating passes per case, user-space cycles per call (perf stat, minus the empty loop), A against A at the start and the end.
Machine: CPU governor is 'powersave': frequency scaling adds noise (sudo ./bench tune on).
Machine: turbo boost is on: thermal and frequency drift between rounds (sudo ./bench tune on).
Machine: load average is 4.2: other programs are competing for the CPU.
Machine: CPU 10 is 14% busy with other processes: timings will be noisy (wait for it to finish).
negative = fewer cycles (faster)

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | instructions |
|---|--:|--:|--:|--:|--:|--:|
| dense-prefix/n31/h8191 @ dense-prefix/n31/h8191 | 132,198 | +102% (+95 … +104) layout? | −5% (−6 … 0) | +10% (+8 … +11) | +95% (+94 … +96) | −1% … 0% |
| periodic/n31/h8191 @ periodic/n31/h8191 | 82,206 | +70% (+67 … +73) layout? | −1% (−3 … +1) ~ | +43% (+32 … +47) | +105% (+93 … +115) | −2% … 0% |
| ordinary-miss/n31/h8191 @ ordinary-miss/n31/h8191 | 5,248 | −1% (−3 … −1) | −2% (−2 … −1) | −1% (−2 … +1) | 0% (−1 … +2) ~ | −12% … −2% |
| early-match/n31/h8191 @ early-match/n31/h8191 | 161 | −18% (−19 … −17) | −24% (−25 … −21) | −15% (−17 … −14) | +6% (0 … +9) | −19% … −8% |
| late-match/n31/h8191 @ late-match/n31/h8191 | 5,287 | 0% (−2 … +1) ~ | −2% (−2 … +1) | −1% (−1 … +2) | +2% (0 … +3) | −12% … −2% |
| dense-prefix/n31/h8192 @ dense-prefix/n31/h8192 | 133,714 | +101% (+98 … +106) layout? | −1% (−5 … +1) ~ | +8% (+6 … +11) | +92% (+90 … +97) | −1% … 0% |
| periodic/n31/h8192 @ periodic/n31/h8192 | 83,894 | +67% (+65 … +69) layout? | +1% (0 … +4) ~ | +42% (+30 … +52) | +107% (+101 … +111) | −2% … 0% |
| ordinary-miss/n31/h8192 @ ordinary-miss/n31/h8192 | 5,214 | −1% (−1 … 0) | −2% (−2 … 0) | 0% (−3 … 0) ~ | −2% (−3 … 0) | −12% … −2% |
| early-match/n31/h8192 @ early-match/n31/h8192 | 161 | −17% (−24 … −15) | −23% (−25 … −19) | −17% (−18 … −11) | +3% (−7 … +7) | −19% … −8% |
| late-match/n31/h8192 @ late-match/n31/h8192 | 5,301 | −3% (−3 … +1) | −1% (−3 … +1) | 0% (−1 … +1) ~ | 0% (−1 … +1) ~ | −12% … −2% |
| dense-prefix/n31/h8193 @ dense-prefix/n31/h8193 | 135,708 | +95% (+90 … +100) layout? | −5% (−6 … +1) | +10% (+8 … +11) | +95% (+85 … +105) | −1% … 0% |
| periodic/n31/h8193 @ periodic/n31/h8193 | 83,468 | +69% (+61 … +70) layout? | 0% (−2 … +3) ~ | +44% (+24 … +54) | +88% (+88 … +96) | −2% … 0% |
| ordinary-miss/n31/h8193 @ ordinary-miss/n31/h8193 | 5,176 | +2% (−2 … +78) | +1% (−2 … +2) ~ | −1% (−1 … 0) ~ | +2% (−6 … +3) | −12% … −2% |
| early-match/n31/h8193 @ early-match/n31/h8193 | 161 | −18% (−19 … −16) | −22% (−26 … −5) | −17% (−24 … −14) | +3% (−3 … +5) | −19% … −8% |
| late-match/n31/h8193 @ late-match/n31/h8193 | 5,238 | 0% (−2 … +2) ~ | 0% (−1 … +2) ~ | −1% (−1 … 0) | 0% (−3 … +2) ~ | −12% … −2% |
| dense-prefix/n31/h65536 @ dense-prefix/n31/h65536 | 1,086,894 | +98% (+95 … +103) layout? | 0% (−3 … +4) ~ | +10% (+6 … +12) | +96% (+94 … +100) | −1% … 0% |
| periodic/n31/h65536 @ periodic/n31/h65536 | 661,412 | +70% (+66 … +71) layout? | +2% (−1 … +3) | +41% (+33 … +57) | +86% (+83 … +96) | −2% … 0% |
| ordinary-miss/n31/h65536 @ ordinary-miss/n31/h65536 | 40,538 | 0% (−3 … +2) ~ | 0% (−2 … +2) ~ | 0% (0 … +1) ~ | −1% (−3 … +8) ~ | −12% … 0% |
| early-match/n31/h65536 @ early-match/n31/h65536 | 162 | −20% (−24 … −16) | −23% (−25 … −20) | −16% (−18 … −13) | +3% (+2 … +9) | −19% … −8% |
| late-match/n31/h65536 @ late-match/n31/h65536 | 40,812 | −1% (−2 … +2) ~ | 0% (−7 … +1) ~ | +1% (−2 … +4) ~ | +2% (−2 … +9) | −12% … 0% |
| dense-prefix/n32/h8191 @ dense-prefix/n32/h8191 | 141,575 | −1% (−6 … +2) ~ | −1% (−5 … +2) ~ | −1% (−3 … 0) ~ | +93% (+89 … +107) | −1% … 0% |
| periodic/n32/h8191 @ periodic/n32/h8191 | 66,608 | 0% (−1 … +1) ~ | +2% (−3 … +3) ~ | 0% (−2 … +3) ~ | +94% (+80 … +99) | −2% … 0% |
| ordinary-miss/n32/h8191 @ ordinary-miss/n32/h8191 | 5,224 | −1% (−2 … +1) ~ | 0% (−1 … +1) ~ | 0% (−1 … +1) ~ | +1% (−2 … +2) ~ | −16% … 0% |
| early-match/n32/h8191 @ early-match/n32/h8191 | 165 | −12% (−17 … −6) | +2% (0 … +4) | −22% (−23 … −13) | +15% (+10 … +33) | +1% … +3% |
| late-match/n32/h8191 @ late-match/n32/h8191 | 5,249 | 0% (−4 … +1) ~ | 0% (−3 … +1) ~ | 0% (−1 … 0) ~ | +1% (−2 … +3) | −16% … 0% |
| dense-prefix/n32/h8192 @ dense-prefix/n32/h8192 | 141,770 | n/a (instructions −99%) | −99% (−100 … −97) | −98% (−99 … −97) | −97% (−99 … −96) | −99% … −98% |
| periodic/n32/h8192 @ periodic/n32/h8192 | 67,444 | −89% (−90 … −87) | −90% (−90 … −89) | −89% (−89 … −88) | −90% (−94 … −87) | −92% … −91% |
| ordinary-miss/n32/h8192 @ ordinary-miss/n32/h8192 | 5,238 | −1% (−2 … 0) | −1% (−1 … 0) | 0% (−1 … 0) ~ | 0% (−5 … +1) | −1% … 0% |
| early-match/n32/h8192 @ early-match/n32/h8192 | 164 | +5% (+3 … +6) | +10% (+7 … +13) | −4% (−9 … +4) | +7% (+2 … +14) | +3% … +22% |
| late-match/n32/h8192 @ late-match/n32/h8192 | 5,253 | 0% (−1 … +2) ~ | 0% (−1 … +2) ~ | +1% (−1 … +2) | 0% (−1 … +1) ~ | 0% |
| dense-prefix/n32/h8193 @ dense-prefix/n32/h8193 | 139,732 | −97% (−98 … −97) | −98% (−99 … −98) | −97% (−98 … −97) | n/a (instructions −98%) | −99% … −98% |
| periodic/n32/h8193 @ periodic/n32/h8193 | 66,926 | −90% (−90 … −86) | −90% (−91 … −89) | −89% (−90 … −89) | −90% (−91 … −88) | −92% … −91% |
| ordinary-miss/n32/h8193 @ ordinary-miss/n32/h8193 | 5,249 | 0% (−4 … +1) ~ | 0% (0 … +1) ~ | 0% (−2 … +1) ~ | −1% (−3 … +1) | −1% … 0% |
| early-match/n32/h8193 @ early-match/n32/h8193 | 165 | +2% (0 … +5) | +5% (−20 … +10) | −7% (−11 … +3) | +4% (−1 … +6) | +3% … +22% |
| late-match/n32/h8193 @ late-match/n32/h8193 | 5,281 | +1% (0 … +2) | 0% (−2 … +1) ~ | +1% (−1 … +1) ~ | −1% (−1 … +3) | 0% |
| dense-prefix/n32/h65536 @ dense-prefix/n32/h65536 | 1,106,031 | n/a (instructions −99%) | −99% (−100 … −98) | −99% (−99 … −98) | −98% (−99 … −97) | −99% |
| periodic/n32/h65536 @ periodic/n32/h65536 | 534,642 | −91% (−91 … −89) | −92% (−92 … −91) | −92% (−92 … −89) | −91% (−92 … −89) | −93% |
| ordinary-miss/n32/h65536 @ ordinary-miss/n32/h65536 | 41,099 | 0% (−1 … +2) ~ | 0% (−1 … +1) ~ | +1% (0 … +3) | +1% (−1 … +15) | −1% … 0% |
| early-match/n32/h65536 @ early-match/n32/h65536 | 165 | +3% (+2 … +5) | +8% (+6 … +10) | −6% (−11 … 0) | +7% (+4 … +8) | +3% … +22% |
| late-match/n32/h65536 @ late-match/n32/h65536 | 41,055 | 0% (−1 … +2) ~ | 0% (−2 … +3) ~ | 0% (−1 … 0) ~ | −1% (−2 … +3) ~ | −1% … 0% |
| dense-prefix/n33/h8191 @ dense-prefix/n33/h8191 | 153,942 | −5% (−8 … −3) layout? | −3% (−5 … +2) | −2% (−5 … +4) ~ | +92% (+41 … +95) | −1% … 0% |
| periodic/n33/h8191 @ periodic/n33/h8191 | 87,019 | −2% (−4 … 0) | −1% (−5 … +2) ~ | −3% (−20 … +26) | +72% (+70 … +76) | −3% … 0% |
| ordinary-miss/n33/h8191 @ ordinary-miss/n33/h8191 | 8,941 | 0% (−2 … +2) ~ | 0% (−1 … 0) ~ | 0% (−3 … +1) ~ | +1% (−3 … +3) | −18% … 0% |
| early-match/n33/h8191 @ early-match/n33/h8191 | 177 | −17% (−22 … −16) | +4% (−2 … +9) | −20% (−23 … −15) | +12% (+8 … +14) | +1% … +3% |
| late-match/n33/h8191 @ late-match/n33/h8191 | 9,037 | −1% (−2 … +1) ~ | +2% (−1 … +3) | 0% (−2 … 0) ~ | +2% (−16 … +4) | −18% … 0% |
| dense-prefix/n33/h8192 @ dense-prefix/n33/h8192 | 159,650 | −98% (−99 … −98) | n/a (instructions −99%) | −98% (−99 … −97) | n/a (instructions −98%) | −99% … −98% |
| periodic/n33/h8192 @ periodic/n33/h8192 | 87,981 | −89% (−91 … −89) | −92% (−92 … −90) | n/a (instructions −92%) | −91% (−92 … −90) | −92% |
| ordinary-miss/n33/h8192 @ ordinary-miss/n33/h8192 | 8,970 | −1% (−1 … +2) | −1% (−4 … −1) | 0% (−2 … +1) ~ | −1% (−5 … +4) | −6% … 0% |
| early-match/n33/h8192 @ early-match/n33/h8192 | 177 | −2% (−2 … −2) ~ | +10% (+4 … +16) | +2% (−1 … +7) | +6% (+4 … +9) | +2% … +22% |
| late-match/n33/h8192 @ late-match/n33/h8192 | 9,001 | 0% (0 … +1) ~ | +1% (−1 … +2) ~ | 0% (−1 … +1) ~ | +2% (−4 … +4) | −5% … 0% |
| dense-prefix/n33/h8193 @ dense-prefix/n33/h8193 | 155,094 | −98% (−99 … −97) | −99% (−99 … −98) | n/a (instructions −98%) | n/a (instructions −98%) | −99% |
| periodic/n33/h8193 @ periodic/n33/h8193 | 87,533 | −91% (−91 … −89) | −92% (−95 … −91) | −92% (−92 … −91) | −90% (−92 … −88) | −92% |
| ordinary-miss/n33/h8193 @ ordinary-miss/n33/h8193 | 9,000 | 0% (−1 … +2) ~ | 0% (−1 … +2) ~ | 0% (0 … +1) ~ | +1% (−2 … +3) | −6% … 0% |
| early-match/n33/h8193 @ early-match/n33/h8193 | 176 | −2% (−3 … +3) | +10% (+5 … +18) | +4% (−9 … +10) | +6% (−21 … +8) | +2% … +22% |
| late-match/n33/h8193 @ late-match/n33/h8193 | 9,007 | −1% (−2 … +2) | 0% (−1 … +2) ~ | 0% (0 … +2) | 0% (−1 … +2) ~ | −5% … 0% |
| dense-prefix/n33/h65536 @ dense-prefix/n33/h65536 | 1,210,298 | −99% (−100 … −98) | n/a (instructions −99%) | −99% (−99 … −98) | n/a (instructions −99%) | −99% |
| periodic/n33/h65536 @ periodic/n33/h65536 | 704,247 | −92% (−93 … −91) | −92% (−93 … −92) | −93% (−95 … −92) | −92% (−93 … −91) | −94% … −93% |
| ordinary-miss/n33/h65536 @ ordinary-miss/n33/h65536 | 70,608 | 0% (−3 … +2) ~ | +1% (−2 … +3) ~ | −1% (−2 … +1) ~ | −1% (−2 … +2) ~ | −6% … 0% |
| early-match/n33/h65536 @ early-match/n33/h65536 | 177 | −2% (−5 … +1) | +10% (+8 … +12) | +3% (−3 … +7) | +5% (+3 … +20) | +2% … +22% |
| late-match/n33/h65536 @ late-match/n33/h65536 | 70,176 | +1% (−1 … +3) | +1% (−1 … +4) | 0% (0 … +1) ~ | 0% (−1 … +1) ~ | −6% … 0% |
| dense-prefix/n64/h8191 @ dense-prefix/n64/h8191 | 387,040 | −1% (−2 … +1) ~ | +1% (−8 … +1) ~ | +18% (+12 … +24) layout? | +43% (+35 … +50) | −1% … 0% |
| periodic/n64/h8191 @ periodic/n64/h8191 | 186,699 | 0% (−1 … 0) ~ | +1% (−3 … +3) ~ | +22% (−12 … +30) | +39% (+38 … +43) | −1% … 0% |
| ordinary-miss/n64/h8191 @ ordinary-miss/n64/h8191 | 2,095 | −1% (−3 … +2) ~ | +1% (0 … +2) ~ | +1% (−2 … +2) ~ | 0% (0 … +2) ~ | −15% … 0% |
| early-match/n64/h8191 @ early-match/n64/h8191 | 277 | −19% (−25 … −10) | +5% (+3 … +10) | −1% (−5 … 0) ~ | +26% (+23 … +30) | +1% … +3% |
| late-match/n64/h8191 @ late-match/n64/h8191 | 2,211 | −1% (−2 … 0) | 0% (−1 … +2) ~ | −1% (−1 … 0) ~ | +3% (−16 … +4) | −14% … 0% |
| dense-prefix/n64/h8192 @ dense-prefix/n64/h8192 | 386,079 | n/a (instructions −99%) | n/a (instructions −99%) | −98% (−100 … −97) | n/a (instructions −99%) | −99% |
| periodic/n64/h8192 @ periodic/n64/h8192 | 184,614 | −95% (−97 … −94) | −97% (−97 … −95) | −95% (−96 … −94) | −96% (−97 … −94) | −96% … −95% |
| ordinary-miss/n64/h8192 @ ordinary-miss/n64/h8192 | 2,107 | −1% (−4 … +2) | 0% (−1 … +2) ~ | 0% (−1 … +1) ~ | 0% (−7 … +3) ~ | −4% … +1% |
| early-match/n64/h8192 @ early-match/n64/h8192 | 283 | −5% (−6 … −1) | +3% (−4 … +11) | −1% (−7 … +5) ~ | +9% (+3 … +20) | +2% … +26% |
| late-match/n64/h8192 @ late-match/n64/h8192 | 2,216 | 0% (−2 … +4) ~ | −1% (−4 … 0) ~ | +1% (−1 … +1) ~ | 0% (0 … +4) ~ | 0% … +1% |
| dense-prefix/n64/h8193 @ dense-prefix/n64/h8193 | 387,403 | n/a (instructions −99%) | −99% (−100 … −97) | n/a (instructions −99%) | n/a (instructions −99%) | −99% |
| periodic/n64/h8193 @ periodic/n64/h8193 | 185,699 | −96% (−96 … −94) | −96% (−98 … −96) | −96% (−96 … −95) | −96% (−100 … −95) | −96% … −95% |
| ordinary-miss/n64/h8193 @ ordinary-miss/n64/h8193 | 2,096 | 0% (−6 … +3) ~ | 0% (−3 … +1) ~ | +1% (−1 … +8) | +2% (−4 … +3) | −4% … +1% |
| early-match/n64/h8193 @ early-match/n64/h8193 | 285 | −2% (−8 … 0) | +3% (−7 … +6) | +1% (−2 … +8) ~ | +3% (−22 … +8) | +2% … +26% |
| late-match/n64/h8193 @ late-match/n64/h8193 | 2,211 | +1% (0 … +5) ~ | 0% (−2 … +1) ~ | 0% (−2 … +1) ~ | 0% (−3 … +2) ~ | 0% … +1% |
| dense-prefix/n64/h65536 @ dense-prefix/n64/h65536 | 3,095,311 | n/a (instructions −100%) | n/a (instructions −100%) | −99% (−100 … −98) | n/a (instructions −99%) | −99% |
| periodic/n64/h65536 @ periodic/n64/h65536 | 1,520,351 | −97% (−98 … −96) | −97% (−98 … −96) | −97% (−98 … −96) | −97% (−99 … −96) | −97% |
| ordinary-miss/n64/h65536 @ ordinary-miss/n64/h65536 | 18,487 | −1% (−3 … +3) | 0% (0 … +1) ~ | 0% (−1 … +1) ~ | +1% (−3 … +1) | −6% … 0% |
| early-match/n64/h65536 @ early-match/n64/h65536 | 286 | −5% (−9 … −2) | +2% (+2 … +7) ~ | +1% (−6 … +7) ~ | +7% (+4 … +9) | +2% … +26% |
| late-match/n64/h65536 @ late-match/n64/h65536 | 18,781 | 0% (−2 … +2) ~ | +1% (−2 … +2) ~ | 0% (−1 … +1) ~ | 0% (0 … +3) ~ | −5% … 0% |
| dense-prefix/n256/h8191 @ dense-prefix/n256/h8191 | 1,159,628 | 0% (−2 … +2) ~ | 0% (−1 … +1) ~ | −3% (−4 … −2) | +11% (+9 … +32) layout? | 0% |
| periodic/n256/h8191 @ periodic/n256/h8191 | 571,652 | +1% (−2 … +3) | 0% (0 … +1) | −2% (−5 … −1) | +8% (+8 … +14) layout? | 0% |
| ordinary-miss/n256/h8191 @ ordinary-miss/n256/h8191 | 1,598 | −2% (−3 … −1) | +1% (−1 … +2) | 0% (−1 … +2) ~ | 0% (−5 … +2) ~ | −8% … 0% |
| early-match/n256/h8191 @ early-match/n256/h8191 | 686 | −5% (−5 … −2) layout? | +1% (0 … +4) | +5% (+3 … +9) layout? | −1% (−2 … 0) | 0% … +3% |
| late-match/n256/h8191 @ late-match/n256/h8191 | 2,018 | −2% (−8 … −1) | +2% (+1 … +3) | 0% (−5 … +1) ~ | 0% (−1 … +5) ~ | −6% … 0% |
| dense-prefix/n256/h8192 @ dense-prefix/n256/h8192 | 1,165,890 | n/a (instructions −99%) | n/a (instructions −99%) | n/a (instructions −99%) | −99% (−100 … −94) | −99% |
| periodic/n256/h8192 @ periodic/n256/h8192 | 568,926 | n/a (instructions −98%) | −98% (−98 … −97) | −98% (−99 … −97) | −97% (−98 … −95) | −98% |
| ordinary-miss/n256/h8192 @ ordinary-miss/n256/h8192 | 1,606 | −2% (−3 … +2) | −1% (−1 … +1) ~ | −2% (−55 … +1) | −2% (−2 … +1) | 0% … +2% |
| early-match/n256/h8192 @ early-match/n256/h8192 | 684 | 0% (−6 … +2) ~ | +3% (−63 … +177) | −2% (−63 … +4) | +12% (−33 … +16) | +1% … +31% |
| late-match/n256/h8192 @ late-match/n256/h8192 | 2,035 | −2% (−3 … −1) | +2% (−1 … +2) | −1% (−1 … 0) ~ | +3% (+1 … +58) | 0% … +17% |
| dense-prefix/n256/h8193 @ dense-prefix/n256/h8193 | 1,148,018 | n/a (instructions −99%) | n/a (instructions −99%) | −99% (−100 … −99) | n/a (instructions −99%) | −99% |
| periodic/n256/h8193 @ periodic/n256/h8193 | 578,584 | n/a (instructions −98%) | −98% (−100 … −97) | −98% (−99 … −96) | −99% (−100 … −97) | −98% |
| ordinary-miss/n256/h8193 @ ordinary-miss/n256/h8193 | 1,615 | −2% (−33 … +1) | 0% (0 … +1) ~ | −1% (−54 … +1) ~ | +1% (0 … +74) | 0% … +2% |
| early-match/n256/h8193 @ early-match/n256/h8193 | 681 | 0% (−2 … +1) ~ | +2% (+1 … +3) ~ | −1% (−1 … +2) ~ | +14% (+13 … +18) | +1% … +31% |
| late-match/n256/h8193 @ late-match/n256/h8193 | 1,992 | −1% (−2 … +1) ~ | +1% (0 … +1) ~ | 0% (−1 … +1) ~ | +5% (+4 … +10) | 0% … +17% |
| dense-prefix/n256/h65536 @ dense-prefix/n256/h65536 | 9,469,562 | −100% (−100 … −99) | −100% (−100 … −99) | n/a (instructions −100%) | n/a (instructions −100%) | −100% |
| periodic/n256/h65536 @ periodic/n256/h65536 | 4,725,203 | −99% (−99 … −98) | n/a (instructions −99%) | −99% (−99 … −98) | n/a (instructions −99%) | −99% |
| ordinary-miss/n256/h65536 @ ordinary-miss/n256/h65536 | 12,941 | 0% (0 … +3) ~ | 0% (−1 … +2) ~ | +1% (−2 … +2) | +1% (−1 … +2) | −1% … 0% |
| early-match/n256/h65536 @ early-match/n256/h65536 | 683 | +1% (−2 … +2) | +3% (+2 … +4) | −1% (−1 … 0) | +14% (+11 … +14) | +1% … +31% |
| late-match/n256/h65536 @ late-match/n256/h65536 | 13,350 | 0% (0 … +2) ~ | 0% (−1 … 0) ~ | 0% (−1 … +2) ~ | 0% (−1 … 0) ~ | 0% … +3% |
| late-density/n32/remaining4095/absent @ late-density/n32/remaining4095/absent | 70,878 | +117% (+112 … +125) | +10% (+10 … +18) | +22% (+18 … +29) | +29% (+29 … +32) | +3% … +49% |
| late-density/n32/remaining4095/match @ late-density/n32/remaining4095/match | 72,515 | +116% (+113 … +121) | +11% (+7 … +13) | +25% (+14 … +32) | +30% (+26 … +34) | +3% … +49% |
| late-density/n32/remaining4096/absent @ late-density/n32/remaining4096/absent | 70,829 | +122% (+115 … +124) | +10% (+9 … +14) | +22% (+17 … +24) | +26% (+24 … +31) | +3% … +49% |
| late-density/n32/remaining4096/match @ late-density/n32/remaining4096/match | 70,811 | +118% (+111 … +123) | +10% (+10 … +12) | +27% (+20 … +30) | +32% (+30 … +38) | +3% … +49% |
| late-density/n32/remaining4097/absent @ late-density/n32/remaining4097/absent | 71,157 | +116% (+110 … +120) | +10% (+8 … +13) | +24% (+18 … +24) | +29% (+26 … +32) | +3% … +49% |
| late-density/n32/remaining4097/match @ late-density/n32/remaining4097/match | 71,720 | +114% (+110 … +116) | +11% (+9 … +13) | +22% (+18 … +24) | +28% (+26 … +40) | +3% … +49% |
| late-density/n256/remaining4095/absent @ late-density/n256/remaining4095/absent | 561,484 | +11% (+9 … +15) layout? | 0% (−1 … +2) ~ | −2% (−3 … +1) | +25% (+24 … +25) | 0% … +50% |
| late-density/n256/remaining4095/match @ late-density/n256/remaining4095/match | 566,293 | +12% (+9 … +12) layout? | 0% (0 … +1) ~ | −1% (−3 … +1) | +22% (+21 … +25) | 0% … +50% |
| late-density/n256/remaining4096/absent @ late-density/n256/remaining4096/absent | 571,089 | +11% (+8 … +13) layout? | +1% (−1 … +5) | −3% (−3 … +4) | +23% (+22 … +26) | 0% … +50% |
| late-density/n256/remaining4096/match @ late-density/n256/remaining4096/match | 567,938 | +11% (+7 … +16) layout? | +1% (0 … +1) ~ | 0% (−4 … +2) ~ | +22% (+21 … +24) | 0% … +50% |
| late-density/n256/remaining4097/absent @ late-density/n256/remaining4097/absent | 557,601 | +11% (+9 … +14) layout? | +2% (+1 … +3) | −3% (−4 … 0) | +24% (+23 … +26) | 0% … +50% |
| late-density/n256/remaining4097/match @ late-density/n256/remaining4097/match | 567,406 | +10% (+9 … +13) layout? | 0% (−4 … +1) ~ | −1% (−4 … +3) | +22% (+22 … +22) | 0% … +50% |

Control: master against itself.

| call | master, CPU cycles per call (GCC 13.3) | A/A start | A/A end |
|---|--:|--:|--:|
| dense-prefix/n31/h8191 @ dense-prefix/n31/h8191 | 134,662 | +1% (−1 … +3) | −1% (−4 … +2) |
| periodic/n31/h8191 @ periodic/n31/h8191 | 82,320 | −1% (−1 … +3) | −2% (−2 … +3) |
| ordinary-miss/n31/h8191 @ ordinary-miss/n31/h8191 | 5,212 | 0% (−1 … +2) | 0% (−2 … +2) |
| early-match/n31/h8191 @ early-match/n31/h8191 | 160 | 0% (0 … +1) | 0% (0 … +2) |
| late-match/n31/h8191 @ late-match/n31/h8191 | 5,243 | +1% (−1 … +1) | 0% (−1 … +1) |
| dense-prefix/n31/h8192 @ dense-prefix/n31/h8192 | 133,013 | +2% (−1 … +3) | +1% (0 … +2) |
| periodic/n31/h8192 @ periodic/n31/h8192 | 82,802 | 0% (−1 … +2) | +1% (−2 … +3) |
| ordinary-miss/n31/h8192 @ ordinary-miss/n31/h8192 | 5,218 | 0% (−1 … +4) | +1% (−1 … +1) |
| early-match/n31/h8192 @ early-match/n31/h8192 | 161 | 0% (−1 … +1) | 0% (0 … +1) |
| late-match/n31/h8192 @ late-match/n31/h8192 | 5,263 | 0% (−1 … +2) | −1% (−10 … 0) |
| dense-prefix/n31/h8193 @ dense-prefix/n31/h8193 | 136,689 | −2% (−4 … +2) | +1% (−2 … +3) |
| periodic/n31/h8193 @ periodic/n31/h8193 | 83,003 | +1% (−3 … +2) | +1% (−1 … +4) |
| ordinary-miss/n31/h8193 @ ordinary-miss/n31/h8193 | 5,276 | −1% (−5 … +7) | −1% (−1 … +2) |
| early-match/n31/h8193 @ early-match/n31/h8193 | 161 | 0% (−2 … +1) | 0% (−3 … +3) |
| late-match/n31/h8193 @ late-match/n31/h8193 | 5,247 | +1% (0 … +2) | −1% (−4 … +3) |
| dense-prefix/n31/h65536 @ dense-prefix/n31/h65536 | 1,069,900 | 0% (−2 … +3) | +1% (−3 … +1) |
| periodic/n31/h65536 @ periodic/n31/h65536 | 662,115 | 0% (−4 … +4) | 0% (−2 … 0) |
| ordinary-miss/n31/h65536 @ ordinary-miss/n31/h65536 | 39,427 | +2% (−1 … +17) | +1% (−1 … +2) |
| early-match/n31/h65536 @ early-match/n31/h65536 | 160 | −2% (−2 … +5) | 0% (−4 … +1) |
| late-match/n31/h65536 @ late-match/n31/h65536 | 41,429 | −2% (−6 … +1) | +1% (−7 … +3) |
| dense-prefix/n32/h8191 @ dense-prefix/n32/h8191 | 137,659 | +1% (−2 … +8) | +1% (−3 … +9) |
| periodic/n32/h8191 @ periodic/n32/h8191 | 67,149 | −1% (−3 … 0) | −2% (−2 … 0) |
| ordinary-miss/n32/h8191 @ ordinary-miss/n32/h8191 | 5,296 | 0% (−2 … 0) | −1% (−2 … +2) |
| early-match/n32/h8191 @ early-match/n32/h8191 | 164 | +1% (−1 … +4) | −1% (−2 … +1) |
| late-match/n32/h8191 @ late-match/n32/h8191 | 5,288 | +1% (−2 … +5) | +1% (−2 … +2) |
| dense-prefix/n32/h8192 @ dense-prefix/n32/h8192 | 140,599 | +1% (−4 … +4) | +2% (−6 … +2) |
| periodic/n32/h8192 @ periodic/n32/h8192 | 67,521 | 0% (−2 … +2) | +1% (−1 … +3) |
| ordinary-miss/n32/h8192 @ ordinary-miss/n32/h8192 | 5,245 | 0% (−1 … +3) | 0% (−1 … +1) |
| early-match/n32/h8192 @ early-match/n32/h8192 | 164 | 0% (−2 … +2) | 0% (−1 … 0) |
| late-match/n32/h8192 @ late-match/n32/h8192 | 5,289 | +1% (−2 … +2) | 0% (−1 … +1) |
| dense-prefix/n32/h8193 @ dense-prefix/n32/h8193 | 139,224 | −1% (−1 … +3) | 0% (−1 … +1) |
| periodic/n32/h8193 @ periodic/n32/h8193 | 66,090 | 0% (−2 … +6) | −1% (−1 … +2) |
| ordinary-miss/n32/h8193 @ ordinary-miss/n32/h8193 | 5,203 | +1% (0 … +3) | −1% (−1 … +1) |
| early-match/n32/h8193 @ early-match/n32/h8193 | 164 | −1% (−2 … +4) | +1% (−1 … +3) |
| late-match/n32/h8193 @ late-match/n32/h8193 | 5,301 | −1% (−2 … 0) | 0% (−3 … +3) |
| dense-prefix/n32/h65536 @ dense-prefix/n32/h65536 | 1,108,894 | −1% (−3 … +3) | +1% (0 … +4) |
| periodic/n32/h65536 @ periodic/n32/h65536 | 526,149 | +2% (+1 … +4) | −1% (−2 … +1) |
| ordinary-miss/n32/h65536 @ ordinary-miss/n32/h65536 | 40,932 | +1% (0 … +3) | 0% (−2 … +3) |
| early-match/n32/h65536 @ early-match/n32/h65536 | 164 | +1% (−1 … +4) | 0% (−2 … +3) |
| late-match/n32/h65536 @ late-match/n32/h65536 | 41,216 | +1% (−3 … +2) | +1% (−1 … +2) |
| dense-prefix/n33/h8191 @ dense-prefix/n33/h8191 | 154,434 | +2% (−3 … +5) | 0% (−3 … +1) |
| periodic/n33/h8191 @ periodic/n33/h8191 | 87,237 | 0% (−6 … +3) | −2% (−2 … +2) |
| ordinary-miss/n33/h8191 @ ordinary-miss/n33/h8191 | 9,037 | 0% (−1 … +2) | −1% (−1 … +2) |
| early-match/n33/h8191 @ early-match/n33/h8191 | 179 | −3% (−6 … −1) | −2% (−2 … +3) |
| late-match/n33/h8191 @ late-match/n33/h8191 | 8,921 | +1% (−1 … +4) | −1% (−1 … +2) |
| dense-prefix/n33/h8192 @ dense-prefix/n33/h8192 | 156,233 | 0% (−3 … +1) | +2% (0 … +222) |
| periodic/n33/h8192 @ periodic/n33/h8192 | 88,785 | +1% (−6 … +5) | −1% (−2 … 0) |
| ordinary-miss/n33/h8192 @ ordinary-miss/n33/h8192 | 8,948 | 0% (−3 … +1) | 0% (−1 … +1) |
| early-match/n33/h8192 @ early-match/n33/h8192 | 180 | +2% (−7 … +4) | +1% (−3 … +1) |
| late-match/n33/h8192 @ late-match/n33/h8192 | 9,062 | −1% (−15 … 0) | −1% (−1 … 0) |
| dense-prefix/n33/h8193 @ dense-prefix/n33/h8193 | 157,208 | −2% (−5 … +1) | −1% (−2 … 0) |
| periodic/n33/h8193 @ periodic/n33/h8193 | 88,652 | 0% (−3 … +3) | 0% (−1 … +1) |
| ordinary-miss/n33/h8193 @ ordinary-miss/n33/h8193 | 8,998 | 0% (−1 … +2) | 0% (0 … +2) |
| early-match/n33/h8193 @ early-match/n33/h8193 | 179 | −2% (−4 … +1) | 0% (−2 … +3) |
| late-match/n33/h8193 @ late-match/n33/h8193 | 8,963 | 0% (−1 … +2) | 0% (−1 … +1) |
| dense-prefix/n33/h65536 @ dense-prefix/n33/h65536 | 1,202,293 | +1% (−4 … +3) | 0% (−2 … +3) |
| periodic/n33/h65536 @ periodic/n33/h65536 | 708,338 | −1% (−3 … +3) | +1% (−2 … +3) |
| ordinary-miss/n33/h65536 @ ordinary-miss/n33/h65536 | 70,929 | 0% (−2 … +1) | −1% (−2 … −1) |
| early-match/n33/h65536 @ early-match/n33/h65536 | 180 | −1% (−2 … −1) | 0% (−2 … +4) |
| late-match/n33/h65536 @ late-match/n33/h65536 | 71,208 | 0% (−2 … +2) | 0% (−1 … +2) |
| dense-prefix/n64/h8191 @ dense-prefix/n64/h8191 | 387,827 | −1% (−5 … +1) | −2% (−3 … 0) |
| periodic/n64/h8191 @ periodic/n64/h8191 | 188,873 | −1% (−3 … +1) | 0% (−1 … +3) |
| ordinary-miss/n64/h8191 @ ordinary-miss/n64/h8191 | 2,091 | +2% (−2 … +2) | 0% (−2 … +1) |
| early-match/n64/h8191 @ early-match/n64/h8191 | 280 | +1% (−5 … +5) | −2% (−6 … +3) |
| late-match/n64/h8191 @ late-match/n64/h8191 | 2,228 | −1% (−2 … +1) | 0% (−1 … +8) |
| dense-prefix/n64/h8192 @ dense-prefix/n64/h8192 | 380,045 | +2% (0 … +3) | +2% (0 … +2) |
| periodic/n64/h8192 @ periodic/n64/h8192 | 187,052 | 0% (−1 … +2) | 0% (−1 … +2) |
| ordinary-miss/n64/h8192 @ ordinary-miss/n64/h8192 | 2,089 | 0% (−3 … +2) | +1% (−1 … +1) |
| early-match/n64/h8192 @ early-match/n64/h8192 | 278 | −2% (−6 … +1) | +1% (−1 … +8) |
| late-match/n64/h8192 @ late-match/n64/h8192 | 2,232 | −1% (−2 … +1) | +1% (0 … +2) |
| dense-prefix/n64/h8193 @ dense-prefix/n64/h8193 | 387,758 | −1% (−2 … +1) | 0% (−1 … +2) |
| periodic/n64/h8193 @ periodic/n64/h8193 | 187,111 | 0% (−1 … +1) | +1% (0 … +2) |
| ordinary-miss/n64/h8193 @ ordinary-miss/n64/h8193 | 2,088 | 0% (−1 … +2) | 0% (−1 … +2) |
| early-match/n64/h8193 @ early-match/n64/h8193 | 278 | 0% (−1 … +2) | +2% (−6 … +4) |
| late-match/n64/h8193 @ late-match/n64/h8193 | 2,216 | 0% (−2 … +2) | +2% (−1 … +3) |
| dense-prefix/n64/h65536 @ dense-prefix/n64/h65536 | 3,119,795 | −1% (−3 … +3) | −1% (−4 … 0) |
| periodic/n64/h65536 @ periodic/n64/h65536 | 1,506,756 | 0% (−1 … +2) | 0% (−1 … 0) |
| ordinary-miss/n64/h65536 @ ordinary-miss/n64/h65536 | 18,621 | +1% (−1 … +1) | 0% (−2 … +1) |
| early-match/n64/h65536 @ early-match/n64/h65536 | 289 | −2% (−6 … +6) | −3% (−5 … +2) |
| late-match/n64/h65536 @ late-match/n64/h65536 | 18,673 | 0% (0 … +149) | +1% (−2 … +2) |
| dense-prefix/n256/h8191 @ dense-prefix/n256/h8191 | 1,152,834 | −1% (−2 … +1) | 0% (−2 … +1) |
| periodic/n256/h8191 @ periodic/n256/h8191 | 575,158 | 0% (−1 … +2) | 0% (−2 … +1) |
| ordinary-miss/n256/h8191 @ ordinary-miss/n256/h8191 | 1,595 | 0% (−1 … +2) | 0% (0 … +1) |
| early-match/n256/h8191 @ early-match/n256/h8191 | 679 | 0% (−1 … +2) | +1% (0 … +1) |
| late-match/n256/h8191 @ late-match/n256/h8191 | 2,043 | 0% (−2 … 0) | −1% (−2 … +17) |
| dense-prefix/n256/h8192 @ dense-prefix/n256/h8192 | 1,151,223 | +1% (−2 … +5) | 0% (−1 … +2) |
| periodic/n256/h8192 @ periodic/n256/h8192 | 579,298 | −1% (−1 … +2) | 0% (−2 … +5) |
| ordinary-miss/n256/h8192 @ ordinary-miss/n256/h8192 | 1,608 | +1% (0 … +1) | 0% (0 … +1) |
| early-match/n256/h8192 @ early-match/n256/h8192 | 676 | +1% (−1 … +3) | 0% (−2 … +1) |
| late-match/n256/h8192 @ late-match/n256/h8192 | 2,028 | 0% (−1 … +2) | −1% (−4 … +2) |
| dense-prefix/n256/h8193 @ dense-prefix/n256/h8193 | 1,158,775 | 0% (−1 … +2) | 0% (−1 … +7) |
| periodic/n256/h8193 @ periodic/n256/h8193 | 579,873 | −1% (−2 … +3) | +1% (−1 … +1) |
| ordinary-miss/n256/h8193 @ ordinary-miss/n256/h8193 | 1,612 | −1% (−2 … +1) | 0% (−9 … +2) |
| early-match/n256/h8193 @ early-match/n256/h8193 | 706 | −3% (−49 … +2) | +1% (−1 … +3) |
| late-match/n256/h8193 @ late-match/n256/h8193 | 1,996 | +1% (−1 … +2) | −1% (−3 … 0) |
| dense-prefix/n256/h65536 @ dense-prefix/n256/h65536 | 9,468,537 | 0% (0 … 0) | 0% (−1 … 0) |
| periodic/n256/h65536 @ periodic/n256/h65536 | 4,697,051 | +1% (−1 … +2) | +1% (−1 … +1) |
| ordinary-miss/n256/h65536 @ ordinary-miss/n256/h65536 | 13,103 | −1% (−8 … 0) | +1% (0 … +2) |
| early-match/n256/h65536 @ early-match/n256/h65536 | 681 | 0% (−2 … +2) | 0% (−1 … +19) |
| late-match/n256/h65536 @ late-match/n256/h65536 | 13,485 | −1% (−4 … +1) | 0% (−1 … +1) |
| late-density/n32/remaining4095/absent @ late-density/n32/remaining4095/absent | 71,811 | 0% (−1 … 0) | +1% (−1 … +2) |
| late-density/n32/remaining4095/match @ late-density/n32/remaining4095/match | 71,247 | 0% (−2 … 0) | 0% (−2 … +1) |
| late-density/n32/remaining4096/absent @ late-density/n32/remaining4096/absent | 71,892 | −1% (−2 … 0) | 0% (−1 … +1) |
| late-density/n32/remaining4096/match @ late-density/n32/remaining4096/match | 71,627 | 0% (−5 … +1) | 0% (−1 … +1) |
| late-density/n32/remaining4097/absent @ late-density/n32/remaining4097/absent | 71,962 | −1% (−2 … 0) | −1% (−3 … 0) |
| late-density/n32/remaining4097/match @ late-density/n32/remaining4097/match | 71,770 | −1% (−3 … +2) | −1% (−4 … +1) |
| late-density/n256/remaining4095/absent @ late-density/n256/remaining4095/absent | 563,969 | 0% (−2 … +5) | +1% (−1 … +10) |
| late-density/n256/remaining4095/match @ late-density/n256/remaining4095/match | 564,634 | 0% (−1 … +3) | 0% (−1 … +1) |
| late-density/n256/remaining4096/absent @ late-density/n256/remaining4096/absent | 563,438 | 0% (−2 … +3) | 0% (−1 … 0) |
| late-density/n256/remaining4096/match @ late-density/n256/remaining4096/match | 562,611 | +1% (0 … +3) | 0% (−1 … 0) |
| late-density/n256/remaining4097/absent @ late-density/n256/remaining4097/absent | 566,174 | +1% (−1 … +2) | −1% (−5 … +1) |
| late-density/n256/remaining4097/match @ late-density/n256/remaining4097/match | 565,110 | 0% (−3 … +4) | 0% (−2 … +1) |

~: the change is not larger than the A/A control of the same row: not evidence of a difference.

layout?: in every pass the cycles changed in the same direction, by 3% or more in the median, the instructions by less than 0.5%: the work is the same, so look for the cause (code placement, branch prediction) with `bench why` before reporting the row.

n/a: under 20 cycles per call, the subtraction of the empty loop dominates; compare instructions.
<!-- /bench-table -->
