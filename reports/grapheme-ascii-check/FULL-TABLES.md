# Full tables of the grapheme_ascii_check() report

All 111 calls of [`grapheme.php`](grapheme.php) in the main series of the [report](README.md). Change in CPU cycles per call against master (negative = fewer cycles, faster), the median over 15 passes and, in brackets, the lowest and the highest pass. The last column is the change in instructions over the three groups, the master-against-master group included.

## Main series

<!-- bench-table series.json --full --header -->
Machine: AMD Ryzen 9 5950X 16-Core Processor, CPU 15, kernel 7.0.0-42-generic.
Group gcc15: A = k10-base-gcc15 (abab936a395 GCC 15.2, profile docker), B = k10-gcc15 (5595f170c35 GCC 15.2, profile docker).
Group clang21: A = k10-base-clang21 (abab936a395 clang 21.1, profile docker), B = k10-clang21 (5595f170c35 clang 21.1, profile docker).
Group clang21-aa: A = k10-base-clang21 (abab936a395 clang 21.1, profile docker), B = k10-base-clang21 (abab936a395 clang 21.1, profile docker).
15 alternating passes per case, user-space cycles per call (perf stat, minus the empty loop), A against A at the start and the end.
Machine: turbo boost is on: thermal and frequency drift between rounds (sudo ./bench tune on).
Machine: load average is 2.6: other programs are competing for the CPU.
negative = fewer cycles (faster)

| call | master, CPU cycles per call (GCC 15.2 (gcc15)) | GCC 15.2 (gcc15) | clang 21.1 (clang21) | clang 21.1 (clang21-aa) | instructions |
|---|--:|--:|--:|--:|--:|
| grapheme_strlen($s) @ ASCII 1 B | 36 | +9% (0 … +16) | +4% (−5 … +9) | +3% (−8 … +9) | 0% … +3% |
| grapheme_strlen($s) @ ASCII 2 B | 38 | +5% (+5 … +6) | +3% (−3 … +9) | 0% (−7 … +7) | 0% … +4% |
| grapheme_strlen($s) @ ASCII 3 B | 40 | +3% (+2 … +12) | −4% (−8 … +5) | 0% (−9 … +18) | 0% … +5% |
| grapheme_strlen($s) @ ASCII 4 B | 42 | 0% (−3 … +10) ~ | −4% (−7 … +5) | 0% (−6 … +14) ~ | 0% … +6% |
| grapheme_strlen($s) @ ASCII 5 B | 44 | −2% (−3 … −2) | −5% (−8 … +10) | 0% (−8 … +45) | 0% … +7% |
| grapheme_strlen($s) @ ASCII 8 B | 50 | −6% (−14 … −6) | −8% (−32 … +8) | 0% (−11 … +7) | 0% … +9% |
| grapheme_strlen($s) @ ASCII 9 B | 52 | −23% (−29 … −17) | −25% (−29 … −20) | −6% (−8 … +8) | −20% … 0% |
| grapheme_strlen($s) @ ASCII 10 B | 54 | −24% (−25 … −5) | −26% (−27 … −14) | 0% (−12 … +6) | −19% … 0% |
| grapheme_strlen($s) @ ASCII 16 B | 69 | −28% (−34 … −28) | −27% (−28 … −23) | 0% (−4 … +11) ~ | −14% … 0% |
| grapheme_strlen($s) @ ASCII 80 B | 211 | −67% (−68 … −66) | −64% (−65 … −64) | 0% (−2 … +2) | −55% … 0% |
| grapheme_strlen($s) @ ASCII 2 KB | 4,157 | −79% (−79 … −79) | −80% (−80 … −80) | 0% (0 … 0) ~ | −74% … 0% |
| grapheme_strlen($s) @ ASCII 2 KB, CR LF every 80 B | 125,899 | +1% (−2 … +18) | +1% (−3 … +9) | 0% (−3 … +3) ~ | 0% |
| grapheme_strlen($s) @ ASCII 2 KB, lone CR every 80 B | 4,157 | −79% (−79 … −79) | −82% (−82 … −82) | 0% (0 … 0) | −74% … 0% |
| grapheme_strlen($s) @ ASCII 2 KB, "é" first | 125,225 | +1% (−51 … +4) | +1% (0 … +5) | 0% (−3 … +3) ~ | 0% |
| grapheme_strlen($s) @ ASCII 2 KB, "é" last | 129,355 | −2% (−5 … +1) | −1% (−3 … +4) | +1% (−5 … +5) | −2% … 0% |
| grapheme_strlen($s) @ Spanish 80 B | 5,847 | −1% (−7 … 0) | +1% (−1 … +4) | 0% (−2 … +1) ~ | 0% |
| grapheme_strlen($s) @ Russian 80 B | 4,141 | −1% (−8 … +13) | +1% (0 … +14) | 0% (−8 … +3) ~ | 0% |
| grapheme_strlen($s) @ Chinese 80 B | 3,067 | −2% (−6 … +9) | +1% (0 … +6) | 0% (−4 … +3) ~ | 0% |
| grapheme_strlen($s) @ Japanese 80 B | 3,215 | −2% (−3 … +1) | +1% (−2 … +2) | 0% (−2 … +1) | 0% |
| grapheme_strlen($s) @ Korean 80 B | 3,501 | −2% (−2 … −1) | +1% (−2 … +1) | 0% (−1 … +5) ~ | 0% |
| grapheme_strlen($s) @ emoji and text 80 B | 4,949 | −1% (−2 … +1) | +1% (−4 … +5) | 0% (−2 … +3) | 0% |
| grapheme_substr($s, 0, 8) @ ASCII 1 B | 99 | −9% (−17 … −6) | +2% (−4 … +6) | 0% (−14 … +16) ~ | 0% … +2% |
| grapheme_substr($s, 0, 8) @ ASCII 2 B | 102 | −10% (−18 … +25) | 0% (−11 … +16) | −2% (−38 … +13) | 0% … +2% |
| grapheme_substr($s, 0, 8) @ ASCII 3 B | 103 | −10% (−13 … +5) | 0% (−12 … +6) | 0% (−14 … +17) ~ | 0% … +3% |
| grapheme_substr($s, 0, 8) @ ASCII 4 B | 103 | −10% (−21 … −5) | −1% (−15 … +18) | 0% (−16 … +9) ~ | 0% … +3% |
| grapheme_substr($s, 0, 8) @ ASCII 5 B | 103 | −9% (−20 … +6) | −2% (−11 … +13) | −2% (−9 … +92) | 0% … +4% |
| grapheme_substr($s, 0, 8) @ ASCII 8 B | 102 | −5% (−14 … +6) | −1% (−11 … +18) ~ | 0% (−7 … +9) ~ | 0% … +5% |
| grapheme_substr($s, 0, 8) @ ASCII 9 B | 102 | −11% (−23 … 0) | −16% (−18 … −10) | 0% (−10 … +7) ~ | −9% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 10 B | 104 | −12% (−17 … −7) | −15% (−18 … −11) | −1% (−4 … +7) ~ | −9% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 16 B | 117 | −14% (−19 … −10) | −19% (−24 … +13) | 0% (−7 … +6) | −8% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 80 B | 258 | −53% (−54 … −47) | −53% (−54 … −52) | 0% (−6 … +4) | −44% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 2 KB | 4,201 | −78% (−78 … −77) | −79% (−79 … −79) | 0% (0 … 0) | −73% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 2 KB, CR LF every 80 B | 13,448 | −1% (−3 … +1) | −1% (−1 … 0) | 0% (0 … +1) ~ | −1% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 2 KB, lone CR every 80 B | 4,203 | −78% (−78 … −78) | −81% (−81 … −80) | 0% (0 … 0) | −73% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 2 KB, "é" first | 13,323 | 0% (−1 … +1) | 0% (−1 … +1) ~ | 0% (0 … +1) ~ | 0% |
| grapheme_substr($s, 0, 8) @ ASCII 2 KB, "é" last | 17,422 | −19% (−19 … −18) | −19% (−19 … −18) | 0% (−1 … 0) | −20% … 0% |
| grapheme_substr($s, 0, 8) @ Spanish 80 B | 2,397 | −2% (−4 … −1) | +2% (−1 … +4) | 0% (−3 … +1) | −1% … 0% |
| grapheme_substr($s, 0, 8) @ Russian 80 B | 2,439 | +1% (0 … +14) | +2% (−1 … +3) | 0% (−1 … +1) ~ | 0% |
| grapheme_substr($s, 0, 8) @ Chinese 80 B | 2,392 | 0% (−1 … +4) | 0% (−2 … +3) | 0% (−3 … +2) ~ | 0% |
| grapheme_substr($s, 0, 8) @ Japanese 80 B | 2,341 | +1% (0 … +1) | +1% (−7 … +4) | 0% (−2 … +16) ~ | 0% |
| grapheme_substr($s, 0, 8) @ Korean 80 B | 2,372 | +1% (−1 … +2) | +2% (+1 … +3) | 0% (−3 … +4) | 0% |
| grapheme_substr($s, 0, 8) @ emoji and text 80 B | 2,596 | 0% (−3 … 0) | +1% (0 … +7) | 0% (−2 … +1) ~ | 0% |
| grapheme_strpos($s, 'zz') @ ASCII 1 B | 56 | +12% (+7 … +15) | +11% (+3 … +21) | 0% (−48 … +14) ~ | 0% … +9% |
| grapheme_strpos($s, 'zz') @ ASCII 2 B | 72 | +7% (+2 … +12) | +8% (+2 … +13) | +1% (−9 … +7) | 0% … +8% |
| grapheme_strpos($s, 'zz') @ ASCII 3 B | 74 | +6% (+2 … +13) | +6% (0 … +11) | −1% (−5 … +3) | 0% … +8% |
| grapheme_strpos($s, 'zz') @ ASCII 4 B | 76 | +4% (0 … +9) | +5% (0 … +10) | 0% (−6 … +5) | 0% … +9% |
| grapheme_strpos($s, 'zz') @ ASCII 5 B | 78 | +3% (−1 … +4) | +7% (+1 … +10) | 0% (−5 … +7) | 0% … +9% |
| grapheme_strpos($s, 'zz') @ ASCII 8 B | 84 | 0% (−24 … +1) | +2% (−6 … +7) | +1% (−3 … +9) | 0% … +10% |
| grapheme_strpos($s, 'zz') @ ASCII 9 B | 86 | −10% (−13 … −4) | −11% (−18 … −9) | 0% (−5 … +6) | −7% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 10 B | 88 | −11% (−14 … −11) | −8% (−18 … +38) | 0% (−4 … +5) | −6% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 16 B | 103 | −17% (−19 … −13) | −14% (−18 … −12) | −1% (−7 … +4) | −6% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 80 B | 262 | −54% (−55 … −51) | −54% (−55 … −53) | −1% (−2 … +1) | −43% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 2 KB | 4,725 | −69% (−70 … −69) | −70% (−70 … −70) | 0% (0 … 0) ~ | −68% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 2 KB, CR LF every 80 B | 221,146 | 0% (−1 … 0) | 0% (0 … 0) | 0% (−1 … 0) | 0% |
| grapheme_strpos($s, 'zz') @ ASCII 2 KB, lone CR every 80 B | 4,725 | −69% (−70 … −69) | −73% (−73 … −73) | 0% (0 … 0) ~ | −69% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 2 KB, "é" first | 221,114 | 0% (−1 … 0) | 0% (0 … +1) | 0% (−1 … 0) ~ | 0% |
| grapheme_strpos($s, 'zz') @ ASCII 2 KB, "é" last | 224,971 | −1% (−2 … −1) | −1% (−2 … +52) | 0% (−8 … +1) | −2% … 0% |
| grapheme_strpos($s, 'zz') @ Spanish 80 B | 12,953 | 0% (−1 … 0) | 0% (−2 … +2) | 0% (−2 … +3) | 0% |
| grapheme_strpos($s, 'zz') @ Russian 80 B | 9,775 | 0% (−1 … +2) ~ | 0% (−2 … +2) | 0% (−2 … +1) ~ | 0% |
| grapheme_strpos($s, 'zz') @ Chinese 80 B | 9,641 | 0% (−2 … 0) ~ | 0% (−1 … +3) ~ | 0% (−2 … +1) | 0% |
| grapheme_strpos($s, 'zz') @ Japanese 80 B | 7,704 | +1% (−2 … +1) | 0% (−2 … +3) | 0% (−2 … +2) ~ | 0% |
| grapheme_strpos($s, 'zz') @ Korean 80 B | 11,887 | 0% (−1 … +2) | 0% (−2 … +4) | 0% (−3 … +2) | 0% |
| grapheme_strpos($s, 'zz') @ emoji and text 80 B | 11,523 | −1% (−2 … +2) | 0% (−2 … +2) | 0% (−2 … +2) | 0% |
| grapheme_extract($s, 8) @ ASCII 1 B | 104 | +4% (−5 … +10) | +3% (−8 … +14) | 0% (−7 … +7) ~ | 0% … +1% |
| grapheme_extract($s, 8) @ ASCII 2 B | 107 | +3% (+1 … +5) | +6% (−2 … +11) | −1% (−25 … +10) | 0% … +2% |
| grapheme_extract($s, 8) @ ASCII 3 B | 107 | +2% (+1 … +3) | +5% (−2 … +10) | +1% (−10 … +20) | 0% … +2% |
| grapheme_extract($s, 8) @ ASCII 4 B | 109 | +1% (−1 … +4) | +2% (−12 … +5) | +3% (−5 … +26) | 0% … +3% |
| grapheme_extract($s, 8) @ ASCII 5 B | 110 | +1% (−2 … +3) | 0% (−9 … +5) | −1% (−14 … +6) | 0% … +3% |
| grapheme_extract($s, 8) @ ASCII 8 B | 114 | +2% (−1 … +4) | −1% (−8 … +4) | 0% (−8 … +7) ~ | 0% … +5% |
| grapheme_extract($s, 8) @ ASCII 9 B | 115 | −5% (−5 … 0) | −12% (−15 … −9) | +1% (−6 … +8) | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 10 B | 115 | −5% (−5 … −1) | −12% (−15 … −6) | +1% (−32 … +5) | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 16 B | 115 | −6% (−14 … −2) | −14% (−19 … −4) | 0% (−5 … +8) | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 80 B | 115 | −5% (−6 … −4) | −13% (−18 … 0) | 0% (−6 … +6) ~ | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 2 KB | 115 | −5% (−7 … −3) | −13% (−18 … −8) | 0% (−3 … +75) | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 2 KB, CR LF every 80 B | 115 | −5% (−5 … −4) | −13% (−19 … −8) | 0% (−6 … +8) | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 2 KB, lone CR every 80 B | 115 | −5% (−8 … −4) | −14% (−17 … −11) | −1% (−7 … +9) | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 2 KB, "é" first | 2,372 | 0% (−11 … +2) ~ | −1% (−4 … +1) | 0% (−3 … 0) | 0% |
| grapheme_extract($s, 8) @ ASCII 2 KB, "é" last | 114 | −5% (−6 … −4) | −14% (−22 … −11) | 0% (−12 … +6) ~ | −10% … 0% |
| grapheme_extract($s, 8) @ Spanish 80 B | 2,216 | 0% (−3 … +1) | −2% (−3 … +1) | 0% (−3 … +1) ~ | −1% … 0% |
| grapheme_extract($s, 8) @ Russian 80 B | 2,869 | 0% (−2 … +2) ~ | 0% (−2 … +2) ~ | 0% (−2 … +2) | 0% |
| grapheme_extract($s, 8) @ Chinese 80 B | 2,880 | 0% (−7 … +5) | 0% (−2 … +9) | 0% (−4 … +5) | 0% |
| grapheme_extract($s, 8) @ Japanese 80 B | 2,875 | 0% (−3 … +4) | 0% (−1 … +2) ~ | 0% (−4 … +5) ~ | 0% |
| grapheme_extract($s, 8) @ Korean 80 B | 2,817 | 0% (−2 … +8) ~ | 0% (−2 … +1) ~ | 0% (−1 … +1) | 0% |
| grapheme_extract($s, 8) @ emoji and text 80 B | 2,376 | 0% (−8 … +6) | 0% (−5 … +1) | 0% (−3 … +6) ~ | 0% |
| grapheme_strpos($s, 'x') @ ASCII 1 B | 66 | +12% (+9 … +18) | +8% (0 … +15) | 0% (−6 … +9) | 0% … +7% |
| grapheme_strpos($s, 'x') @ ASCII 5 B | 74 | +5% (0 … +16) | +3% (−6 … +54) | +1% (−7 … +189) | 0% … +9% |
| grapheme_strpos($s, 'x') @ ASCII 9 B | 82 | −8% (−12 … −5) | −13% (−17 … −7) | 0% (−7 … +5) ~ | −9% … 0% |
| grapheme_strpos($s, 'x') @ ASCII 16 B | 99 | −15% (−18 … −12) | −18% (−21 … −15) | 0% (−4 … +19) | −7% … 0% |
| grapheme_strpos($s, 'x') @ ASCII 80 B | 231 | −60% (−62 … −60) | −60% (−61 … −59) | 0% (−2 … +2) ~ | −50% … 0% |
| grapheme_strpos($s, 'x') @ ASCII 2 KB | 4,176 | −78% (−79 … −78) | −79% (−79 … −78) | 0% (0 … 0) ~ | −74% … 0% |
| grapheme_strstr($s, 'o') @ ASCII 1 B | 69 | +9% (+4 … +14) | +10% (0 … +18) | −2% (−8 … +11) | 0% … +3% |
| grapheme_strstr($s, 'o') @ ASCII 5 B | 77 | +2% (−1 … +8) | +8% (−1 … +13) | 0% (−8 … +8) | 0% … +5% |
| grapheme_strstr($s, 'o') @ ASCII 9 B | 85 | −11% (−14 … −7) | −12% (−17 … −7) | 0% (−9 … +10) ~ | −13% … 0% |
| grapheme_strstr($s, 'o') @ ASCII 16 B | 128 | −12% (−14 … −8) | −15% (−20 … −13) | 0% (−3 … +7) | −7% … 0% |
| grapheme_strstr($s, 'o') @ ASCII 80 B | 271 | −50% (−51 … −47) | −49% (−49 … −48) | −1% (−2 … +3) | −43% … 0% |
| grapheme_strstr($s, 'o') @ ASCII 2 KB | 4,269 | −76% (−76 … −76) | −77% (−77 … −77) | 0% (0 … 0) ~ | −72% … 0% |
| grapheme_stripos($s, 'Z') @ ASCII 1 B | 142 | +4% (+1 … +5) | +2% (−3 … +25) | +1% (−12 … +5) | 0% … +2% |
| grapheme_stripos($s, 'Z') @ ASCII 5 B | 153 | +1% (−1 … +3) | 0% (−6 … +3) | −1% (−6 … +3) | 0% … +3% |
| grapheme_stripos($s, 'Z') @ ASCII 9 B | 164 | −6% (−6 … −3) | −8% (−10 … −5) | 0% (−2 … +4) | −6% … 0% |
| grapheme_stripos($s, 'Z') @ ASCII 16 B | 175 | −10% (−11 … −9) | −11% (−14 … −10) | +1% (−1 … +5) ~ | −5% … 0% |
| grapheme_stripos($s, 'Z') @ ASCII 80 B | 317 | −40% (−41 … −37) | −46% (−47 … −45) | 0% (−2 … +2) | −36% … 0% |
| grapheme_stripos($s, 'Z') @ ASCII 2 KB | 4,580 | −71% (−71 … −71) | −72% (−72 … −72) | 0% (0 … 0) | −66% … 0% |
| grapheme_strrpos($s, 'e') @ ASCII 1 B | 64 | +6% (+6 … +13) | +6% (+3 … +10) | 0% (−7 … +2) | 0% … +6% |
| grapheme_strrpos($s, 'e') @ ASCII 5 B | 62 | 0% (−9 … +6) | +5% (−25 … +6) | +1% (−5 … +6) | 0% … +6% |
| grapheme_strrpos($s, 'e') @ ASCII 9 B | 75 | −15% (−18 … −14) | −11% (−15 … −6) | +1% (−6 … +8) | −12% … 0% |
| grapheme_strrpos($s, 'e') @ ASCII 16 B | 98 | −17% (−19 … −14) | −11% (−15 … −7) | +1% (−6 … +9) | −8% … 0% |
| grapheme_strrpos($s, 'e') @ ASCII 80 B | 245 | −56% (−57 … −55) | −55% (−56 … −54) | +1% (−1 … +4) | −44% … 0% |
| grapheme_strrpos($s, 'e') @ ASCII 2 KB | 4,187 | −78% (−79 … −78) | −79% (−79 … −79) | 0% (0 … 0) | −73% … 0% |
| grapheme_strlen(next string) @ ASCII, mixed lengths 1-24 B | 100 | −28% (−32 … −23) | −33% (−41 … −26) | 0% (−4 … +8) ~ | −14% … 0% |
| grapheme_substr(next string, 0, 8) @ ASCII, mixed lengths 1-24 B | 159 | −8% (−9 … −6) | −7% (−9 … +40) | 0% (−2 … +2) ~ | −8% … 0% |
| grapheme_strpos(next string, 'zz') @ ASCII, mixed lengths 1-24 B | 145 | −12% (−17 … −5) | −13% (−14 … −10) | 0% (−5 … +1) ~ | −6% … 0% |

Control: master against itself.

| call | master, CPU cycles per call (GCC 15.2) | A/A start | A/A end |
|---|--:|--:|--:|
| grapheme_strlen($s) @ ASCII 1 B | 36 | 0% (−10 … +12) | 0% (−10 … 0) |
| grapheme_strlen($s) @ ASCII 2 B | 38 | 0% (−9 … +13) | 0% (−8 … +9) |
| grapheme_strlen($s) @ ASCII 3 B | 40 | 0% (−9 … +8) | 0% (−8 … +10) |
| grapheme_strlen($s) @ ASCII 4 B | 42 | 0% (−8 … +8) | 0% (−1 … +7) |
| grapheme_strlen($s) @ ASCII 5 B | 44 | 0% (−15 … +10) | 0% (−9 … +17) |
| grapheme_strlen($s) @ ASCII 8 B | 50 | 0% (−7 … +8) | 0% (−12 … 0) |
| grapheme_strlen($s) @ ASCII 9 B | 52 | 0% (−7 … +8) | 0% (0 … +6) |
| grapheme_strlen($s) @ ASCII 10 B | 54 | 0% (0 … +8) | 0% (0 … +1) |
| grapheme_strlen($s) @ ASCII 16 B | 69 | 0% (−6 … 0) | 0% (−6 … +6) |
| grapheme_strlen($s) @ ASCII 80 B | 211 | 0% (0 … +3) | 0% (0 … +1) |
| grapheme_strlen($s) @ ASCII 2 KB | 4,148 | 0% (0 … 0) | 0% (0 … 0) |
| grapheme_strlen($s) @ ASCII 2 KB, CR LF every 80 B | 125,489 | 0% (−1 … +27) | 0% (−31 … +2) |
| grapheme_strlen($s) @ ASCII 2 KB, lone CR every 80 B | 4,147 | 0% (0 … 0) | 0% (0 … 0) |
| grapheme_strlen($s) @ ASCII 2 KB, "é" first | 124,897 | 0% (−3 … +16) | 0% (−1 … +35) |
| grapheme_strlen($s) @ ASCII 2 KB, "é" last | 128,970 | 0% (−41 … +4) | 0% (−3 … +6) |
| grapheme_strlen($s) @ Spanish 80 B | 5,842 | 0% (−4 … +5) | 0% (−30 … +4) |
| grapheme_strlen($s) @ Russian 80 B | 4,119 | 0% (−4 … +29) | 0% (−2 … +10) |
| grapheme_strlen($s) @ Chinese 80 B | 3,061 | 0% (−5 … +1) | 0% (−2 … 0) |
| grapheme_strlen($s) @ Japanese 80 B | 3,207 | 0% (−2 … +1) | 0% (−2 … 0) |
| grapheme_strlen($s) @ Korean 80 B | 3,499 | 0% (−2 … +1) | 0% (−2 … +3) |
| grapheme_strlen($s) @ emoji and text 80 B | 4,926 | 0% (0 … +2) | 0% (−1 … +7) |
| grapheme_substr($s, 0, 8) @ ASCII 1 B | 99 | 0% (−4 … +16) | 0% (−11 … +4) |
| grapheme_substr($s, 0, 8) @ ASCII 2 B | 102 | 0% (−11 … +10) | 0% (−10 … +7) |
| grapheme_substr($s, 0, 8) @ ASCII 3 B | 103 | 0% (−11 … +15) | 0% (−8 … +14) |
| grapheme_substr($s, 0, 8) @ ASCII 4 B | 102 | −1% (−14 … +12) | 0% (−11 … +13) |
| grapheme_substr($s, 0, 8) @ ASCII 5 B | 103 | −1% (−13 … +14) | −1% (−12 … +13) |
| grapheme_substr($s, 0, 8) @ ASCII 8 B | 105 | −2% (−11 … +9) | −1% (−11 … +10) |
| grapheme_substr($s, 0, 8) @ ASCII 9 B | 109 | −6% (−12 … +8) | 0% (−11 … +13) |
| grapheme_substr($s, 0, 8) @ ASCII 10 B | 102 | +1% (−12 … +17) | 0% (−11 … +12) |
| grapheme_substr($s, 0, 8) @ ASCII 16 B | 116 | 0% (−7 … +7) | 0% (−6 … +4) |
| grapheme_substr($s, 0, 8) @ ASCII 80 B | 258 | 0% (−1 … +18) | 0% (−2 … +1) |
| grapheme_substr($s, 0, 8) @ ASCII 2 KB | 4,195 | 0% (0 … 0) | 0% (0 … 0) |
| grapheme_substr($s, 0, 8) @ ASCII 2 KB, CR LF every 80 B | 13,406 | 0% (−8 … +2) | 0% (−1 … +1) |
| grapheme_substr($s, 0, 8) @ ASCII 2 KB, lone CR every 80 B | 4,196 | 0% (0 … 0) | 0% (0 … 0) |
| grapheme_substr($s, 0, 8) @ ASCII 2 KB, "é" first | 13,313 | 0% (0 … 0) | 0% (0 … +24) |
| grapheme_substr($s, 0, 8) @ ASCII 2 KB, "é" last | 17,392 | 0% (0 … 0) | 0% (0 … +9) |
| grapheme_substr($s, 0, 8) @ Spanish 80 B | 2,404 | 0% (−1 … +1) | 0% (−5 … +2) |
| grapheme_substr($s, 0, 8) @ Russian 80 B | 2,432 | 0% (−6 … +2) | 0% (−7 … +2) |
| grapheme_substr($s, 0, 8) @ Chinese 80 B | 2,383 | 0% (−2 … +6) | 0% (−1 … +4) |
| grapheme_substr($s, 0, 8) @ Japanese 80 B | 2,339 | 0% (−1 … +2) | 0% (−4 … +1) |
| grapheme_substr($s, 0, 8) @ Korean 80 B | 2,367 | 0% (−1 … +1) | 0% (−4 … +1) |
| grapheme_substr($s, 0, 8) @ emoji and text 80 B | 2,591 | 0% (−2 … +1) | 0% (−3 … +1) |
| grapheme_strpos($s, 'zz') @ ASCII 1 B | 56 | 0% (−16 … +5) | 0% (−6 … +5) |
| grapheme_strpos($s, 'zz') @ ASCII 2 B | 72 | 0% (−5 … +4) | 0% (0 … +6) |
| grapheme_strpos($s, 'zz') @ ASCII 3 B | 74 | 0% (−3 … +4) | 0% (−5 … 0) |
| grapheme_strpos($s, 'zz') @ ASCII 4 B | 76 | 0% (−5 … +5) | 0% (−4 … +4) |
| grapheme_strpos($s, 'zz') @ ASCII 5 B | 78 | 0% (−2 … +9) | 0% (−1 … +9) |
| grapheme_strpos($s, 'zz') @ ASCII 8 B | 84 | 0% (−6 … +4) | 0% (−5 … +5) |
| grapheme_strpos($s, 'zz') @ ASCII 9 B | 86 | 0% (−3 … +4) | 0% (−5 … +8) |
| grapheme_strpos($s, 'zz') @ ASCII 10 B | 88 | 0% (−4 … +4) | 0% (−3 … 0) |
| grapheme_strpos($s, 'zz') @ ASCII 16 B | 103 | 0% (−3 … +6) | 0% (−4 … 0) |
| grapheme_strpos($s, 'zz') @ ASCII 80 B | 262 | 0% (−1 … +1) | 0% (−3 … +1) |
| grapheme_strpos($s, 'zz') @ ASCII 2 KB | 4,721 | 0% (−1 … 0) | 0% (0 … 0) |
| grapheme_strpos($s, 'zz') @ ASCII 2 KB, CR LF every 80 B | 220,725 | 0% (−1 … +4) | 0% (−1 … 0) |
| grapheme_strpos($s, 'zz') @ ASCII 2 KB, lone CR every 80 B | 4,712 | 0% (0 … 0) | 0% (−1 … 0) |
| grapheme_strpos($s, 'zz') @ ASCII 2 KB, "é" first | 220,705 | 0% (−1 … +2) | 0% (−1 … 0) |
| grapheme_strpos($s, 'zz') @ ASCII 2 KB, "é" last | 224,756 | 0% (0 … 0) | 0% (−1 … +1) |
| grapheme_strpos($s, 'zz') @ Spanish 80 B | 12,904 | 0% (−1 … +1) | 0% (−1 … +1) |
| grapheme_strpos($s, 'zz') @ Russian 80 B | 9,757 | 0% (−2 … +3) | 0% (−2 … +3) |
| grapheme_strpos($s, 'zz') @ Chinese 80 B | 9,627 | 0% (−2 … +3) | 0% (−2 … +4) |
| grapheme_strpos($s, 'zz') @ Japanese 80 B | 7,699 | 0% (−9 … +2) | 0% (−2 … +2) |
| grapheme_strpos($s, 'zz') @ Korean 80 B | 11,865 | 0% (−2 … +1) | 0% (−2 … +1) |
| grapheme_strpos($s, 'zz') @ emoji and text 80 B | 11,542 | 0% (−2 … +2) | 0% (−2 … +2) |
| grapheme_extract($s, 8) @ ASCII 1 B | 105 | −1% (−2 … +5) | 0% (−3 … +3) |
| grapheme_extract($s, 8) @ ASCII 2 B | 106 | +1% (−2 … +3) | 0% (−2 … +4) |
| grapheme_extract($s, 8) @ ASCII 3 B | 107 | 0% (−6 … +1) | 0% (−7 … +1) |
| grapheme_extract($s, 8) @ ASCII 4 B | 109 | 0% (−3 … +1) | 0% (−3 … +2) |
| grapheme_extract($s, 8) @ ASCII 5 B | 110 | 0% (−7 … +32) | 0% (−1 … +2) |
| grapheme_extract($s, 8) @ ASCII 8 B | 114 | 0% (−2 … +8) | 0% (−4 … +5) |
| grapheme_extract($s, 8) @ ASCII 9 B | 115 | 0% (0 … +5) | 0% (−4 … +5) |
| grapheme_extract($s, 8) @ ASCII 10 B | 114 | 0% (−3 … 0) | 0% (−5 … +8) |
| grapheme_extract($s, 8) @ ASCII 16 B | 114 | 0% (−1 … +1) | 0% (−3 … +1) |
| grapheme_extract($s, 8) @ ASCII 80 B | 114 | 0% (−1 … +1) | 0% (−1 … +1) |
| grapheme_extract($s, 8) @ ASCII 2 KB | 114 | 0% (−1 … +3) | 0% (−7 … +1) |
| grapheme_extract($s, 8) @ ASCII 2 KB, CR LF every 80 B | 114 | 0% (0 … +3) | 0% (−12 … +1) |
| grapheme_extract($s, 8) @ ASCII 2 KB, lone CR every 80 B | 114 | 0% (−1 … +1) | 0% (−1 … +1) |
| grapheme_extract($s, 8) @ ASCII 2 KB, "é" first | 2,365 | 0% (−1 … +6) | 0% (−2 … +4) |
| grapheme_extract($s, 8) @ ASCII 2 KB, "é" last | 114 | 0% (−1 … +1) | 0% (−3 … +1) |
| grapheme_extract($s, 8) @ Spanish 80 B | 2,211 | 0% (−1 … +10) | 0% (−1 … +20) |
| grapheme_extract($s, 8) @ Russian 80 B | 2,869 | 0% (−3 … +1) | 0% (−2 … +2) |
| grapheme_extract($s, 8) @ Chinese 80 B | 2,869 | 0% (0 … +3) | 0% (−1 … +1) |
| grapheme_extract($s, 8) @ Japanese 80 B | 2,858 | 0% (−1 … +1) | 0% (−3 … +2) |
| grapheme_extract($s, 8) @ Korean 80 B | 2,812 | 0% (−5 … +38) | 0% (−1 … +1) |
| grapheme_extract($s, 8) @ emoji and text 80 B | 2,365 | 0% (−1 … +1) | 0% (−2 … +2) |
| grapheme_strpos($s, 'x') @ ASCII 1 B | 66 | 0% (−4 … +5) | 0% (−5 … +6) |
| grapheme_strpos($s, 'x') @ ASCII 5 B | 74 | 0% (−5 … +4) | 0% (−8 … 0) |
| grapheme_strpos($s, 'x') @ ASCII 9 B | 82 | 0% (−5 … +4) | 0% (−5 … +4) |
| grapheme_strpos($s, 'x') @ ASCII 16 B | 99 | 0% (−3 … +7) | 0% (−3 … +4) |
| grapheme_strpos($s, 'x') @ ASCII 80 B | 230 | 0% (−2 … +2) | 0% (−2 … +3) |
| grapheme_strpos($s, 'x') @ ASCII 2 KB | 4,167 | 0% (0 … 0) | 0% (0 … 0) |
| grapheme_strstr($s, 'o') @ ASCII 1 B | 69 | 0% (−5 … +4) | 0% (−5 … +11) |
| grapheme_strstr($s, 'o') @ ASCII 5 B | 77 | 0% (−4 … +5) | 0% (−5 … +4) |
| grapheme_strstr($s, 'o') @ ASCII 9 B | 85 | 0% (−7 … +4) | 0% (−4 … +4) |
| grapheme_strstr($s, 'o') @ ASCII 16 B | 128 | 0% (−5 … +6) | 0% (−3 … +6) |
| grapheme_strstr($s, 'o') @ ASCII 80 B | 270 | 0% (−3 … +3) | 0% (−1 … +2) |
| grapheme_strstr($s, 'o') @ ASCII 2 KB | 4,259 | 0% (0 … 0) | 0% (0 … 0) |
| grapheme_stripos($s, 'Z') @ ASCII 1 B | 142 | 0% (−3 … +6) | 0% (−6 … 0) |
| grapheme_stripos($s, 'Z') @ ASCII 5 B | 153 | 0% (−3 … +5) | 0% (−5 … +2) |
| grapheme_stripos($s, 'Z') @ ASCII 9 B | 164 | 0% (−2 … +3) | 0% (−3 … +2) |
| grapheme_stripos($s, 'Z') @ ASCII 16 B | 175 | 0% (−4 … +2) | −1% (−3 … +4) |
| grapheme_stripos($s, 'Z') @ ASCII 80 B | 316 | 0% (−1 … +1) | 0% (−1 … +2) |
| grapheme_stripos($s, 'Z') @ ASCII 2 KB | 4,572 | 0% (0 … 0) | 0% (0 … 0) |
| grapheme_strrpos($s, 'e') @ ASCII 1 B | 64 | 0% (−3 … +5) | 0% (−5 … +7) |
| grapheme_strrpos($s, 'e') @ ASCII 5 B | 62 | 0% (−6 … +7) | 0% (−5 … +4) |
| grapheme_strrpos($s, 'e') @ ASCII 9 B | 74 | 0% (−5 … +4) | 0% (−5 … +5) |
| grapheme_strrpos($s, 'e') @ ASCII 16 B | 98 | 0% (−6 … +3) | 0% (−5 … +4) |
| grapheme_strrpos($s, 'e') @ ASCII 80 B | 245 | 0% (−2 … +2) | 0% (−2 … +3) |
| grapheme_strrpos($s, 'e') @ ASCII 2 KB | 4,178 | 0% (0 … 0) | 0% (0 … 0) |
| grapheme_strlen(next string) @ ASCII, mixed lengths 1-24 B | 99 | 0% (−35 … +10) | 0% (0 … +6) |
| grapheme_substr(next string, 0, 8) @ ASCII, mixed lengths 1-24 B | 158 | 0% (−3 … +2) | 0% (−2 … +2) |
| grapheme_strpos(next string, 'zz') @ ASCII, mixed lengths 1-24 B | 145 | 0% (−1 … +8) | 0% (−6 … +21) |

~: within noise, the change is no larger than the difference between master and master on the same row.
<!-- /bench-table -->

## Earlier versions

Each in its own series, on the 56 calls of [`earlier-grapheme.php`](earlier-grapheme.php), with the same master builds.

The first version: the 8-byte loop for bytes above 0x7f, then `memchr()` for each CR ([`earlier-memchr.diff`](earlier-memchr.diff), [`memchr-series.json`](memchr-series.json)).

<!-- bench-table memchr-series.json --full -->
| call | master, CPU cycles per call (GCC 15.2 (gcc15)) | GCC 15.2 (gcc15) | clang 21.1 (clang21) | clang 21.1 (clang21-aa) | instructions |
|---|--:|--:|--:|--:|--:|
| grapheme_strlen($s) @ ASCII 5 B | 38 | +29% (+12 … +39) | +23% (−41 … +32) | 0% (−8 … +8) ~ | 0% … +13% |
| grapheme_strlen($s) @ ASCII 10 B | 48 | −4% (−10 … +10) | −7% (−15 … +1) | 0% (−8 … +8) ~ | −16% … 0% |
| grapheme_strlen($s) @ ASCII 80 B | 208 | −69% (−71 … −69) | −72% (−73 … −71) | 0% (−3 … +2) ~ | −70% … 0% |
| grapheme_strlen($s) @ ASCII 2 KB | 4,150 | −87% (−88 … −86) | −91% (−91 … −91) | 0% (0 … 0) ~ | −90% … 0% |
| grapheme_strlen($s) @ ASCII 2 KB, CR LF every 80 B | 125,697 | 0% (−4 … +3) ~ | −1% (−27 … +9) | 0% (−3 … +8) ~ | 0% |
| grapheme_strlen($s) @ ASCII 2 KB, lone CR every 80 B | 4,146 | −75% (−76 … −75) | −81% (−82 … −81) | 0% (0 … 0) ~ | −84% … 0% |
| grapheme_strlen($s) @ ASCII 2 KB, "é" first | 125,254 | 0% (−3 … +5) | −1% (−2 … +3) | 0% (−28 … +17) | 0% |
| grapheme_strlen($s) @ ASCII 2 KB, "é" last | 130,196 | −3% (−9 … 0) | −4% (−8 … −3) | 0% (−3 … +5) ~ | −3% … 0% |
| grapheme_strlen($s) @ Spanish 80 B | 5,857 | −1% (−5 … 0) | −1% (−2 … +2) | 0% (−3 … 0) | 0% |
| grapheme_strlen($s) @ Russian 80 B | 4,132 | −1% (−3 … +13) | 0% (−2 … +2) | 0% (−1 … +14) ~ | 0% |
| grapheme_strlen($s) @ Chinese 80 B | 3,067 | −1% (−5 … +8) | 0% (−1 … +7) | +1% (−2 … +3) | 0% |
| grapheme_strlen($s) @ Japanese 80 B | 3,214 | −1% (−3 … +8) | −1% (−2 … +1) | 0% (−19 … 0) ~ | 0% |
| grapheme_strlen($s) @ Korean 80 B | 3,502 | −1% (−3 … 0) | 0% (−2 … +2) | 0% (−4 … +1) | 0% |
| grapheme_strlen($s) @ emoji and text 80 B | 4,941 | −1% (−2 … 0) | 0% (−2 … +2) | 0% (−2 … +2) ~ | 0% |
| grapheme_substr($s, 0, 8) @ ASCII 5 B | 101 | +3% (−10 … +25) | +11% (+8 … +20) | +1% (−7 … +8) | 0% … +6% |
| grapheme_substr($s, 0, 8) @ ASCII 10 B | 104 | −3% (−11 … +1) ~ | −2% (−6 … +3) ~ | 0% (−7 … +7) ~ | −8% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 80 B | 259 | −56% (−58 … −49) | −57% (−58 … −56) | 0% (−3 … +3) | −57% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 2 KB | 4,204 | −86% (−87 … −85) | −90% (−90 … −90) | 0% (0 … 0) ~ | −89% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 2 KB, CR LF every 80 B | 13,473 | +2% (−7 … +3) | +1% (0 … +12) | 0% (−1 … +1) ~ | 0% … +3% |
| grapheme_substr($s, 0, 8) @ ASCII 2 KB, lone CR every 80 B | 4,201 | −74% (−75 … −74) | −81% (−81 … −80) | 0% (0 … 0) ~ | −83% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 2 KB, "é" first | 13,347 | 0% (0 … 0) ~ | 0% (−1 … 0) | 0% (−1 … +1) ~ | 0% |
| grapheme_substr($s, 0, 8) @ ASCII 2 KB, "é" last | 17,429 | −21% (−22 … −21) | −22% (−23 … −14) | 0% (0 … +1) | −25% … 0% |
| grapheme_substr($s, 0, 8) @ Spanish 80 B | 2,398 | −2% (−3 … −1) | +2% (−1 … +5) | +1% (−3 … +3) | −1% … 0% |
| grapheme_substr($s, 0, 8) @ Russian 80 B | 2,439 | −1% (−10 … +1) | +2% (0 … +4) | 0% (0 … +16) | 0% |
| grapheme_substr($s, 0, 8) @ Chinese 80 B | 2,390 | 0% (−1 … +4) ~ | +1% (−1 … +15) | 0% (−3 … +3) ~ | 0% |
| grapheme_substr($s, 0, 8) @ Japanese 80 B | 2,344 | +1% (−1 … +3) | +1% (0 … +12) | 0% (−1 … +1) ~ | 0% |
| grapheme_substr($s, 0, 8) @ Korean 80 B | 2,375 | +1% (−2 … +2) | +2% (+1 … +5) | 0% (0 … +1) ~ | 0% |
| grapheme_substr($s, 0, 8) @ emoji and text 80 B | 2,597 | −2% (−7 … +2) | +1% (−4 … +2) | 0% (−1 … +1) ~ | 0% |
| grapheme_strpos($s, 'zz') @ ASCII 5 B | 75 | +31% (+24 … +38) | +21% (+16 … +38) | +4% (−5 … +11) | 0% … +17% |
| grapheme_strpos($s, 'zz') @ ASCII 10 B | 85 | +15% (+10 … +31) | +2% (−1 … +9) ~ | 0% (−6 … +8) ~ | −3% … +2% |
| grapheme_strpos($s, 'zz') @ ASCII 80 B | 258 | −51% (−54 … −50) | −51% (−52 … −50) | 0% (−4 … +4) ~ | −54% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 2 KB | 4,719 | −76% (−77 … −76) | −80% (−80 … −79) | 0% (−4 … 0) | −83% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 2 KB, CR LF every 80 B | 221,077 | 0% (0 … +1) | 0% (0 … +1) | 0% (−1 … +12) ~ | 0% |
| grapheme_strpos($s, 'zz') @ ASCII 2 KB, lone CR every 80 B | 4,718 | −66% (−67 … −65) | −72% (−72 … −72) | 0% (0 … 0) ~ | −78% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 2 KB, "é" first | 221,120 | 0% (0 … +3) | 0% (−1 … +1) | 0% (−1 … +1) | 0% |
| grapheme_strpos($s, 'zz') @ ASCII 2 KB, "é" last | 225,166 | −2% (−2 … 0) | −2% (−3 … −1) | 0% (−1 … +1) ~ | −2% … 0% |
| grapheme_strpos($s, 'zz') @ Spanish 80 B | 12,956 | −1% (−1 … +1) | 0% (−1 … +1) | 0% (−4 … +2) | 0% |
| grapheme_strpos($s, 'zz') @ Russian 80 B | 9,793 | −1% (−4 … +2) ~ | −1% (−2 … +1) ~ | 0% (−3 … +1) ~ | 0% |
| grapheme_strpos($s, 'zz') @ Chinese 80 B | 9,671 | −1% (−1 … +2) | 0% (−1 … +2) ~ | 0% (−2 … +2) ~ | 0% |
| grapheme_strpos($s, 'zz') @ Japanese 80 B | 7,782 | −1% (−2 … +1) | +2% (−1 … +3) | 0% (−2 … +2) ~ | 0% |
| grapheme_strpos($s, 'zz') @ Korean 80 B | 11,961 | 0% (−11 … +4) | 0% (−1 … +2) ~ | 0% (−3 … +2) | 0% |
| grapheme_strpos($s, 'zz') @ emoji and text 80 B | 11,557 | −1% (−3 … +1) ~ | 0% (−1 … +2) ~ | 0% (−1 … +2) ~ | 0% |
| grapheme_extract($s, 8) @ ASCII 5 B | 110 | +7% (+5 … +8) | +10% (+4 … +16) | 0% (−5 … +6) | 0% … +6% |
| grapheme_extract($s, 8) @ ASCII 10 B | 114 | 0% (−1 … +1) | −5% (−9 … +2) | +2% (−5 … +8) | −8% … 0% |
| grapheme_extract($s, 8) @ ASCII 80 B | 114 | 0% (−2 … +1) | −5% (−8 … −1) | 0% (−1 … +8) | −8% … 0% |
| grapheme_extract($s, 8) @ ASCII 2 KB | 114 | 0% (−3 … 0) | −4% (−9 … 0) | +1% (−7 … +5) | −8% … 0% |
| grapheme_extract($s, 8) @ ASCII 2 KB, CR LF every 80 B | 114 | 0% (−3 … +1) | −4% (−9 … +3) | 0% (−4 … +8) ~ | −8% … 0% |
| grapheme_extract($s, 8) @ ASCII 2 KB, lone CR every 80 B | 114 | 0% (−1 … +1) ~ | −5% (−6 … +2) | +3% (−4 … +13) | −8% … 0% |
| grapheme_extract($s, 8) @ ASCII 2 KB, "é" first | 2,367 | +1% (−3 … +3) | −1% (−4 … +3) | 0% (−17 … +2) ~ | 0% |
| grapheme_extract($s, 8) @ ASCII 2 KB, "é" last | 114 | 0% (−4 … +1) | −5% (−9 … −1) | 0% (−5 … +7) ~ | −8% … 0% |
| grapheme_extract($s, 8) @ Spanish 80 B | 2,220 | 0% (−10 … +2) | −2% (−4 … 0) | 0% (−1 … +2) | −1% … 0% |
| grapheme_extract($s, 8) @ Russian 80 B | 2,869 | +1% (−1 … +28) | −1% (−6 … +1) | 0% (−3 … +2) | 0% |
| grapheme_extract($s, 8) @ Chinese 80 B | 2,876 | +1% (0 … +2) | 0% (−2 … +2) | 0% (−2 … +5) ~ | 0% |
| grapheme_extract($s, 8) @ Japanese 80 B | 2,871 | +1% (0 … +8) | 0% (−2 … +2) ~ | 0% (−1 … +3) ~ | 0% |
| grapheme_extract($s, 8) @ Korean 80 B | 2,812 | +1% (0 … +8) | 0% (−3 … +7) ~ | 0% (−1 … +1) | 0% |
| grapheme_extract($s, 8) @ emoji and text 80 B | 2,373 | 0% (−1 … +3) | −1% (−1 … 0) | 0% (−1 … +3) | −1% … 0% |

Control: master against itself.

| call | master, CPU cycles per call (GCC 15.2) | A/A start | A/A end |
|---|--:|--:|--:|
| grapheme_strlen($s) @ ASCII 5 B | 41 | 0% (−8 … +13) | 0% (−10 … +17) |
| grapheme_strlen($s) @ ASCII 10 B | 51 | 0% (−6 … +7) | 0% (−6 … +18) |
| grapheme_strlen($s) @ ASCII 80 B | 208 | 0% (−1 … +3) | 0% (−2 … +1) |
| grapheme_strlen($s) @ ASCII 2 KB | 4,143 | 0% (0 … 0) | 0% (0 … 0) |
| grapheme_strlen($s) @ ASCII 2 KB, CR LF every 80 B | 126,753 | 0% (−5 … +4) | 0% (−2 … +4) |
| grapheme_strlen($s) @ ASCII 2 KB, lone CR every 80 B | 4,143 | 0% (0 … 0) | 0% (0 … 0) |
| grapheme_strlen($s) @ ASCII 2 KB, "é" first | 125,957 | 0% (−5 … +85) | 0% (−2 … +1) |
| grapheme_strlen($s) @ ASCII 2 KB, "é" last | 129,383 | 0% (−2 … +4) | 0% (−3 … +2) |
| grapheme_strlen($s) @ Spanish 80 B | 5,839 | 0% (−2 … +2) | 0% (−3 … +2) |
| grapheme_strlen($s) @ Russian 80 B | 4,128 | 0% (−4 … 0) | 0% (−2 … +6) |
| grapheme_strlen($s) @ Chinese 80 B | 3,058 | 0% (−1 … 0) | 0% (−2 … +2) |
| grapheme_strlen($s) @ Japanese 80 B | 3,212 | 0% (−2 … +20) | 0% (−16 … +1) |
| grapheme_strlen($s) @ Korean 80 B | 3,494 | 0% (−5 … +1) | 0% (−6 … +15) |
| grapheme_strlen($s) @ emoji and text 80 B | 4,929 | 0% (−2 … +3) | 0% (−9 … +6) |
| grapheme_substr($s, 0, 8) @ ASCII 5 B | 102 | +1% (−13 … +18) | 0% (−12 … +16) |
| grapheme_substr($s, 0, 8) @ ASCII 10 B | 103 | 0% (−9 … +24) | +4% (−7 … +27) |
| grapheme_substr($s, 0, 8) @ ASCII 80 B | 259 | 0% (−2 … +4) | 0% (−2 … +4) |
| grapheme_substr($s, 0, 8) @ ASCII 2 KB | 4,193 | 0% (0 … +1) | 0% (0 … 0) |
| grapheme_substr($s, 0, 8) @ ASCII 2 KB, CR LF every 80 B | 13,423 | 0% (−1 … +10) | 0% (0 … +1) |
| grapheme_substr($s, 0, 8) @ ASCII 2 KB, lone CR every 80 B | 4,195 | 0% (0 … 0) | 0% (0 … 0) |
| grapheme_substr($s, 0, 8) @ ASCII 2 KB, "é" first | 13,331 | 0% (−2 … +2) | 0% (0 … 0) |
| grapheme_substr($s, 0, 8) @ ASCII 2 KB, "é" last | 17,421 | 0% (−2 … +2) | 0% (0 … +1) |
| grapheme_substr($s, 0, 8) @ Spanish 80 B | 2,397 | 0% (−3 … +4) | 0% (−1 … +1) |
| grapheme_substr($s, 0, 8) @ Russian 80 B | 2,434 | 0% (−2 … +4) | 0% (−1 … +1) |
| grapheme_substr($s, 0, 8) @ Chinese 80 B | 2,383 | 0% (−1 … +1) | 0% (0 … +1) |
| grapheme_substr($s, 0, 8) @ Japanese 80 B | 2,343 | 0% (−2 … +1) | 0% (−3 … +3) |
| grapheme_substr($s, 0, 8) @ Korean 80 B | 2,369 | 0% (0 … +1) | 0% (−2 … +6) |
| grapheme_substr($s, 0, 8) @ emoji and text 80 B | 2,591 | 0% (−3 … +7) | 0% (−2 … +12) |
| grapheme_strpos($s, 'zz') @ ASCII 5 B | 75 | 0% (−9 … +8) | 0% (−9 … +13) |
| grapheme_strpos($s, 'zz') @ ASCII 10 B | 85 | 0% (−9 … +7) | −3% (−10 … +3) |
| grapheme_strpos($s, 'zz') @ ASCII 80 B | 260 | −1% (−4 … +2) | 0% (−3 … +2) |
| grapheme_strpos($s, 'zz') @ ASCII 2 KB | 4,712 | 0% (0 … 0) | 0% (0 … 0) |
| grapheme_strpos($s, 'zz') @ ASCII 2 KB, CR LF every 80 B | 220,613 | 0% (−2 … +1) | 0% (0 … +1) |
| grapheme_strpos($s, 'zz') @ ASCII 2 KB, lone CR every 80 B | 4,712 | 0% (0 … 0) | 0% (−1 … 0) |
| grapheme_strpos($s, 'zz') @ ASCII 2 KB, "é" first | 220,670 | 0% (0 … +1) | 0% (0 … 0) |
| grapheme_strpos($s, 'zz') @ ASCII 2 KB, "é" last | 224,773 | 0% (0 … 0) | 0% (−23 … +1) |
| grapheme_strpos($s, 'zz') @ Spanish 80 B | 12,935 | 0% (−1 … +1) | 0% (−1 … +2) |
| grapheme_strpos($s, 'zz') @ Russian 80 B | 9,717 | +1% (−1 … +2) | 0% (−1 … +2) |
| grapheme_strpos($s, 'zz') @ Chinese 80 B | 9,657 | 0% (−1 … +3) | 0% (−1 … +1) |
| grapheme_strpos($s, 'zz') @ Japanese 80 B | 7,753 | 0% (−2 … +2) | 0% (−1 … +2) |
| grapheme_strpos($s, 'zz') @ Korean 80 B | 11,907 | 0% (−1 … +2) | 0% (0 … +3) |
| grapheme_strpos($s, 'zz') @ emoji and text 80 B | 11,380 | +1% (−2 … +2) | 0% (−2 … +2) |
| grapheme_extract($s, 8) @ ASCII 5 B | 110 | 0% (−1 … +1) | 0% (−2 … +14) |
| grapheme_extract($s, 8) @ ASCII 10 B | 114 | 0% (−1 … +1) | 0% (−10 … +2) |
| grapheme_extract($s, 8) @ ASCII 80 B | 114 | 0% (−1 … +1) | 0% (−2 … +2) |
| grapheme_extract($s, 8) @ ASCII 2 KB | 114 | 0% (−17 … +7) | 0% (−1 … +1) |
| grapheme_extract($s, 8) @ ASCII 2 KB, CR LF every 80 B | 114 | 0% (−1 … +1) | 0% (−1 … +1) |
| grapheme_extract($s, 8) @ ASCII 2 KB, lone CR every 80 B | 114 | 0% (−4 … +3) | 0% (0 … +1) |
| grapheme_extract($s, 8) @ ASCII 2 KB, "é" first | 2,374 | 0% (−2 … +1) | 0% (−1 … +2) |
| grapheme_extract($s, 8) @ ASCII 2 KB, "é" last | 114 | 0% (−1 … +4) | 0% (−2 … +1) |
| grapheme_extract($s, 8) @ Spanish 80 B | 2,213 | 0% (−3 … +2) | 0% (−1 … +1) |
| grapheme_extract($s, 8) @ Russian 80 B | 2,864 | 0% (−2 … +2) | 0% (−6 … +4) |
| grapheme_extract($s, 8) @ Chinese 80 B | 2,869 | 0% (−22 … +5) | 0% (−21 … +2) |
| grapheme_extract($s, 8) @ Japanese 80 B | 2,860 | 0% (−1 … +1) | 0% (−3 … +1) |
| grapheme_extract($s, 8) @ Korean 80 B | 2,810 | 0% (−1 … +1) | 0% (−2 … +1) |
| grapheme_extract($s, 8) @ emoji and text 80 B | 2,367 | 0% (−2 … +3) | 0% (−2 … +2) |

~: within noise, the change is no larger than the difference between master and master on the same row.
<!-- /bench-table -->

The second version: a word with a CR is checked byte by byte inside the loop ([`earlier-inword.diff`](earlier-inword.diff), [`inword-series.json`](inword-series.json)).

<!-- bench-table inword-series.json --full -->
| call | master, CPU cycles per call (GCC 15.2 (gcc15)) | GCC 15.2 (gcc15) | clang 21.1 (clang21) | clang 21.1 (clang21-aa) | instructions |
|---|--:|--:|--:|--:|--:|
| grapheme_strlen($s) @ ASCII 5 B | 41 | −5% (−13 … +12) | +16% (+15 … +26) | 0% (−9 … +8) ~ | 0% … +18% |
| grapheme_strlen($s) @ ASCII 10 B | 51 | −23% (−33 … −12) | −16% (−20 … −11) | 0% (−10 … +8) ~ | −20% … 0% |
| grapheme_strlen($s) @ ASCII 80 B | 205 | −72% (−74 … −70) | −71% (−71 … −70) | 0% (−2 … +2) ~ | −64% … 0% |
| grapheme_strlen($s) @ ASCII 2 KB | 4,151 | −83% (−83 … −82) | −83% (−83 … −83) | 0% (0 … 0) | −78% … 0% |
| grapheme_strlen($s) @ ASCII 2 KB, CR LF every 80 B | 126,372 | +2% (−3 … +4) | −2% (−3 … +2) | 0% (−4 … +3) | 0% |
| grapheme_strlen($s) @ ASCII 2 KB, lone CR every 80 B | 4,152 | −76% (−77 … −74) | −79% (−79 … −79) | 0% (0 … 0) ~ | −69% … 0% |
| grapheme_strlen($s) @ ASCII 2 KB, "é" first | 125,110 | +2% (−4 … +3) | −1% (−3 … +10) | +1% (−4 … +8) | 0% |
| grapheme_strlen($s) @ ASCII 2 KB, "é" last | 129,680 | −1% (−4 … +7) | −4% (−7 … −2) | 0% (−2 … +1) ~ | −3% … 0% |
| grapheme_strlen($s) @ Spanish 80 B | 5,854 | 0% (−2 … +1) | −1% (−18 … 0) | 0% (−3 … +1) ~ | 0% |
| grapheme_strlen($s) @ Russian 80 B | 4,135 | 0% (−31 … +2) | 0% (−2 … +2) | 0% (−2 … +1) ~ | 0% |
| grapheme_strlen($s) @ Chinese 80 B | 3,070 | 0% (−1 … +2) | −1% (−3 … +5) | 0% (−13 … +2) ~ | 0% |
| grapheme_strlen($s) @ Japanese 80 B | 3,219 | 0% (−1 … +4) | −1% (−2 … +2) | 0% (0 … +1) | 0% |
| grapheme_strlen($s) @ Korean 80 B | 3,500 | +1% (0 … +2) | −1% (−2 … +2) | 0% (−2 … +3) ~ | 0% |
| grapheme_strlen($s) @ emoji and text 80 B | 4,955 | +1% (−8 … +11) | −1% (−12 … 0) | 0% (−4 … +2) ~ | 0% |
| grapheme_substr($s, 0, 8) @ ASCII 5 B | 103 | −10% (−18 … 0) | +9% (0 … +20) | +1% (−10 … +8) | 0% … +8% |
| grapheme_substr($s, 0, 8) @ ASCII 10 B | 106 | −13% (−23 … −8) | −3% (−9 … +2) | −1% (−10 … +7) ~ | −9% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 80 B | 257 | −57% (−58 … −53) | −57% (−60 … −53) | 0% (−3 … +2) ~ | −52% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 2 KB | 4,203 | −82% (−82 … −81) | −82% (−83 … −82) | 0% (0 … 0) ~ | −78% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 2 KB, CR LF every 80 B | 13,455 | −1% (−1 … 0) | −1% (−2 … +10) | 0% (−1 … 0) ~ | −1% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 2 KB, lone CR every 80 B | 4,202 | −75% (−76 … −74) | −78% (−78 … −78) | 0% (0 … 0) ~ | −69% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 2 KB, "é" first | 13,352 | 0% (−3 … 0) | 0% (−1 … 0) | 0% (−1 … 0) ~ | 0% |
| grapheme_substr($s, 0, 8) @ ASCII 2 KB, "é" last | 17,459 | −20% (−21 … −19) | −20% (−20 … −20) | 0% (−1 … +1) ~ | −21% … 0% |
| grapheme_substr($s, 0, 8) @ Spanish 80 B | 2,406 | −2% (−3 … 0) | +1% (−5 … +3) | 0% (−1 … +4) ~ | −1% … 0% |
| grapheme_substr($s, 0, 8) @ Russian 80 B | 2,437 | −1% (−4 … +5) | +1% (−8 … +5) | 0% (−2 … +8) ~ | 0% |
| grapheme_substr($s, 0, 8) @ Chinese 80 B | 2,390 | 0% (−3 … +4) | +2% (0 … +2) | 0% (−3 … +1) ~ | 0% |
| grapheme_substr($s, 0, 8) @ Japanese 80 B | 2,346 | 0% (−3 … +10) | +2% (+1 … +8) | 0% (−2 … +1) ~ | 0% |
| grapheme_substr($s, 0, 8) @ Korean 80 B | 2,374 | +1% (−1 … +2) | +3% (−2 … +8) | 0% (−1 … +1) ~ | 0% |
| grapheme_substr($s, 0, 8) @ emoji and text 80 B | 2,595 | −1% (−11 … +1) | 0% (−17 … +1) | 0% (−2 … +2) | 0% |
| grapheme_strpos($s, 'zz') @ ASCII 5 B | 75 | +1% (−3 … +6) ~ | +7% (0 … +16) | 0% (−4 … +5) ~ | 0% … +17% |
| grapheme_strpos($s, 'zz') @ ASCII 10 B | 85 | −12% (−13 … −5) | −9% (−13 … −6) | +1% (−3 … +6) ~ | −10% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 80 B | 258 | −57% (−59 … −55) | −59% (−61 … −58) | 0% (−2 … +2) ~ | −50% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 2 KB | 4,718 | −73% (−73 … −72) | −73% (−74 … −73) | 0% (0 … 0) ~ | −73% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 2 KB, CR LF every 80 B | 221,066 | 0% (0 … 0) | 0% (0 … +1) | 0% (−1 … +1) ~ | 0% |
| grapheme_strpos($s, 'zz') @ ASCII 2 KB, lone CR every 80 B | 4,718 | −67% (−67 … −65) | −70% (−71 … −70) | 0% (0 … +1) | −64% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 2 KB, "é" first | 221,117 | 0% (−1 … +1) | 0% (0 … +1) | 0% (0 … 0) ~ | 0% |
| grapheme_strpos($s, 'zz') @ ASCII 2 KB, "é" last | 225,224 | −2% (−2 … −1) | −1% (−11 … −1) | 0% (−1 … +1) | −2% … 0% |
| grapheme_strpos($s, 'zz') @ Spanish 80 B | 12,996 | 0% (−2 … +2) | 0% (−1 … +1) ~ | 0% (−1 … +1) ~ | 0% |
| grapheme_strpos($s, 'zz') @ Russian 80 B | 9,702 | 0% (−2 … +2) ~ | −1% (−2 … +1) | 0% (−2 … +2) ~ | 0% |
| grapheme_strpos($s, 'zz') @ Chinese 80 B | 9,698 | 0% (−2 … +2) | 0% (−1 … +3) | 0% (−2 … +1) ~ | 0% |
| grapheme_strpos($s, 'zz') @ Japanese 80 B | 7,782 | −1% (−3 … +1) | 0% (−1 … +2) ~ | 0% (−2 … +2) ~ | 0% |
| grapheme_strpos($s, 'zz') @ Korean 80 B | 11,948 | −1% (−2 … +1) | 0% (−2 … +1) | 0% (−1 … +1) ~ | 0% |
| grapheme_strpos($s, 'zz') @ emoji and text 80 B | 11,535 | −1% (−2 … +1) | 0% (−2 … +1) ~ | 0% (−1 … +1) ~ | 0% |
| grapheme_extract($s, 8) @ ASCII 5 B | 110 | +2% (+1 … +3) | +7% (+1 … +14) | 0% (−5 … +14) | 0% … +9% |
| grapheme_extract($s, 8) @ ASCII 10 B | 114 | −5% (−7 … −4) | −7% (−12 … +92) | 0% (−5 … +6) | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 80 B | 114 | −5% (−7 … −4) | −9% (−13 … −2) | 0% (−8 … +7) | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 2 KB | 114 | −5% (−7 … −4) | −7% (−13 … +11) | +1% (−12 … +7) | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 2 KB, CR LF every 80 B | 114 | −5% (−6 … −3) | −9% (−13 … −3) | −1% (−8 … +6) | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 2 KB, lone CR every 80 B | 115 | −5% (−6 … −4) | −9% (−13 … −4) | −1% (−8 … +7) | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 2 KB, "é" first | 2,370 | 0% (−2 … +4) ~ | −2% (−3 … +4) | 0% (−1 … +2) ~ | 0% |
| grapheme_extract($s, 8) @ ASCII 2 KB, "é" last | 115 | −5% (−7 … −4) | −8% (−13 … −4) | 0% (−8 … +7) | −10% … 0% |
| grapheme_extract($s, 8) @ Spanish 80 B | 2,217 | 0% (−20 … +5) | −2% (−3 … +3) | 0% (−5 … +5) ~ | −1% … 0% |
| grapheme_extract($s, 8) @ Russian 80 B | 2,864 | 0% (0 … +2) | −1% (−3 … 0) | 0% (−19 … +5) ~ | 0% |
| grapheme_extract($s, 8) @ Chinese 80 B | 2,879 | 0% (−2 … +4) | −1% (−2 … +33) | 0% (−1 … +1) | 0% |
| grapheme_extract($s, 8) @ Japanese 80 B | 2,870 | 0% (−6 … +2) | 0% (−2 … 0) | 0% (−1 … +1) ~ | 0% |
| grapheme_extract($s, 8) @ Korean 80 B | 2,818 | 0% (−3 … +8) | −1% (−2 … +2) | 0% (−2 … +4) ~ | 0% |
| grapheme_extract($s, 8) @ emoji and text 80 B | 2,368 | +1% (+1 … +10) | −1% (−4 … +1) | 0% (−1 … +1) ~ | 0% |

Control: master against itself.

| call | master, CPU cycles per call (GCC 15.2) | A/A start | A/A end |
|---|--:|--:|--:|
| grapheme_strlen($s) @ ASCII 5 B | 38 | 0% (0 … +13) | 0% (−8 … +13) |
| grapheme_strlen($s) @ ASCII 10 B | 51 | 0% (−8 … +5) | 0% (−6 … +6) |
| grapheme_strlen($s) @ ASCII 80 B | 208 | 0% (−2 … +3) | 0% (−3 … +3) |
| grapheme_strlen($s) @ ASCII 2 KB | 4,144 | 0% (0 … 0) | 0% (0 … 0) |
| grapheme_strlen($s) @ ASCII 2 KB, CR LF every 80 B | 125,529 | 0% (−1 … +2) | 0% (−2 … +4) |
| grapheme_strlen($s) @ ASCII 2 KB, lone CR every 80 B | 4,142 | 0% (0 … 0) | 0% (0 … 0) |
| grapheme_strlen($s) @ ASCII 2 KB, "é" first | 125,870 | 0% (−41 … +4) | 0% (−1 … +2) |
| grapheme_strlen($s) @ ASCII 2 KB, "é" last | 129,098 | 0% (−38 … +5) | 0% (−4 … +4) |
| grapheme_strlen($s) @ Spanish 80 B | 5,852 | 0% (−10 … +1) | 0% (−2 … +1) |
| grapheme_strlen($s) @ Russian 80 B | 4,123 | 0% (−1 … +4) | 0% (−9 … +10) |
| grapheme_strlen($s) @ Chinese 80 B | 3,061 | 0% (−1 … +6) | 0% (−1 … +1) |
| grapheme_strlen($s) @ Japanese 80 B | 3,211 | 0% (−20 … +94) | 0% (−5 … +8) |
| grapheme_strlen($s) @ Korean 80 B | 3,495 | 0% (−13 … +1) | 0% (−1 … +2) |
| grapheme_strlen($s) @ emoji and text 80 B | 4,935 | 0% (−4 … +5) | 0% (−3 … +3) |
| grapheme_substr($s, 0, 8) @ ASCII 5 B | 102 | +1% (−23 … +13) | +1% (−9 … +15) |
| grapheme_substr($s, 0, 8) @ ASCII 10 B | 105 | −1% (−15 … +13) | −1% (−19 … +18) |
| grapheme_substr($s, 0, 8) @ ASCII 80 B | 259 | −1% (−7 … +1) | +1% (−4 … +4) |
| grapheme_substr($s, 0, 8) @ ASCII 2 KB | 4,196 | 0% (0 … 0) | 0% (0 … 0) |
| grapheme_substr($s, 0, 8) @ ASCII 2 KB, CR LF every 80 B | 13,434 | 0% (0 … +1) | 0% (−1 … +1) |
| grapheme_substr($s, 0, 8) @ ASCII 2 KB, lone CR every 80 B | 4,195 | 0% (0 … 0) | 0% (0 … 0) |
| grapheme_substr($s, 0, 8) @ ASCII 2 KB, "é" first | 13,323 | 0% (−1 … 0) | 0% (−2 … 0) |
| grapheme_substr($s, 0, 8) @ ASCII 2 KB, "é" last | 17,446 | 0% (0 … +1) | 0% (0 … 0) |
| grapheme_substr($s, 0, 8) @ Spanish 80 B | 2,398 | 0% (−1 … +1) | 0% (−5 … +2) |
| grapheme_substr($s, 0, 8) @ Russian 80 B | 2,437 | 0% (−2 … +2) | 0% (−1 … +8) |
| grapheme_substr($s, 0, 8) @ Chinese 80 B | 2,385 | 0% (−3 … +1) | 0% (−1 … +8) |
| grapheme_substr($s, 0, 8) @ Japanese 80 B | 2,340 | 0% (−2 … +5) | 0% (−1 … 0) |
| grapheme_substr($s, 0, 8) @ Korean 80 B | 2,367 | 0% (−1 … +3) | 0% (−3 … +10) |
| grapheme_substr($s, 0, 8) @ emoji and text 80 B | 2,590 | 0% (−3 … +2) | 0% (−1 … +1) |
| grapheme_strpos($s, 'zz') @ ASCII 5 B | 75 | +4% (−8 … +10) | +1% (−8 … +5) |
| grapheme_strpos($s, 'zz') @ ASCII 10 B | 85 | +1% (−5 … +7) | 0% (−13 … +19) |
| grapheme_strpos($s, 'zz') @ ASCII 80 B | 257 | 0% (−4 … +40) | 0% (−2 … +4) |
| grapheme_strpos($s, 'zz') @ ASCII 2 KB | 4,709 | 0% (0 … 0) | 0% (0 … 0) |
| grapheme_strpos($s, 'zz') @ ASCII 2 KB, CR LF every 80 B | 220,524 | 0% (−1 … 0) | 0% (0 … 0) |
| grapheme_strpos($s, 'zz') @ ASCII 2 KB, lone CR every 80 B | 4,711 | 0% (0 … 0) | 0% (0 … 0) |
| grapheme_strpos($s, 'zz') @ ASCII 2 KB, "é" first | 220,629 | 0% (0 … 0) | 0% (0 … 0) |
| grapheme_strpos($s, 'zz') @ ASCII 2 KB, "é" last | 224,752 | 0% (−29 … +1) | 0% (0 … 0) |
| grapheme_strpos($s, 'zz') @ Spanish 80 B | 12,952 | 0% (−1 … +4) | 0% (−1 … +1) |
| grapheme_strpos($s, 'zz') @ Russian 80 B | 9,758 | 0% (−2 … +2) | 0% (−1 … +3) |
| grapheme_strpos($s, 'zz') @ Chinese 80 B | 9,631 | 0% (−1 … +2) | 0% (−1 … +1) |
| grapheme_strpos($s, 'zz') @ Japanese 80 B | 7,748 | +1% (−2 … +2) | 0% (−2 … +2) |
| grapheme_strpos($s, 'zz') @ Korean 80 B | 11,909 | 0% (−1 … +3) | 0% (−1 … +2) |
| grapheme_strpos($s, 'zz') @ emoji and text 80 B | 11,428 | +1% (−2 … +2) | 0% (−2 … +2) |
| grapheme_extract($s, 8) @ ASCII 5 B | 110 | 0% (−2 … +1) | 0% (−18 … +2) |
| grapheme_extract($s, 8) @ ASCII 10 B | 114 | 0% (−1 … +1) | 0% (−2 … +1) |
| grapheme_extract($s, 8) @ ASCII 80 B | 114 | 0% (−1 … +1) | 0% (−1 … +1) |
| grapheme_extract($s, 8) @ ASCII 2 KB | 114 | 0% (−3 … +1) | 0% (−2 … +1) |
| grapheme_extract($s, 8) @ ASCII 2 KB, CR LF every 80 B | 114 | 0% (−1 … +1) | 0% (−1 … 0) |
| grapheme_extract($s, 8) @ ASCII 2 KB, lone CR every 80 B | 114 | 0% (−3 … +2) | 0% (−3 … +14) |
| grapheme_extract($s, 8) @ ASCII 2 KB, "é" first | 2,365 | −1% (−2 … +1) | 0% (−4 … +1) |
| grapheme_extract($s, 8) @ ASCII 2 KB, "é" last | 114 | 0% (−1 … +2) | 0% (−3 … +1) |
| grapheme_extract($s, 8) @ Spanish 80 B | 2,212 | 0% (−2 … +3) | 0% (−4 … +13) |
| grapheme_extract($s, 8) @ Russian 80 B | 2,861 | 0% (−1 … +15) | 0% (−2 … +2) |
| grapheme_extract($s, 8) @ Chinese 80 B | 2,870 | 0% (−3 … +1) | 0% (−1 … 0) |
| grapheme_extract($s, 8) @ Japanese 80 B | 2,863 | 0% (−3 … +26) | 0% (−5 … +1) |
| grapheme_extract($s, 8) @ Korean 80 B | 2,807 | 0% (−3 … +1) | 0% (−6 … +1) |
| grapheme_extract($s, 8) @ emoji and text 80 B | 2,374 | 0% (−2 … +21) | 0% (−1 … +1) |

~: within noise, the change is no larger than the difference between master and master on the same row.
<!-- /bench-table -->

Back to the [report](README.md).
