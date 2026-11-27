# Full tables of the grapheme_ascii_check() report

All 174 calls of [`grapheme.php`](grapheme.php) in the main series of the [report](README.md). Change in CPU cycles per call against master (negative = fewer cycles, faster), the median over 15 passes and, in brackets, the lowest and the highest pass. The last column is the change in instructions over the three groups, the master-against-master group included.

## Main series

<!-- bench-table series.json --full --header -->
Machine: AMD Ryzen 9 5950X 16-Core Processor, CPU 15, kernel 7.0.0-42-generic.
Group gcc15: A = k10-base-gcc15 (abab936a395 GCC 15.2, profile docker), B = k10-gcc15 (903ef2198a0 GCC 15.2, profile docker).
Group clang21: A = k10-base-clang21 (abab936a395 clang 21.1, profile docker), B = k10-clang21 (903ef2198a0 clang 21.1, profile docker).
Group clang21-aa: A = k10-base-clang21 (abab936a395 clang 21.1, profile docker), B = k10-base-clang21 (abab936a395 clang 21.1, profile docker).
15 alternating passes per case, user-space cycles per call (perf stat, minus the empty loop), A against A at the start and the end.
Machine: turbo boost is on: thermal and frequency drift between rounds (sudo ./bench tune on).
negative = fewer cycles (faster)

| call | master, CPU cycles per call (GCC 15.2 (gcc15)) | GCC 15.2 (gcc15) | clang 21.1 (clang21) | clang 21.1 (clang21-aa) | instructions |
|---|--:|--:|--:|--:|--:|
| grapheme_strlen($s) @ ASCII 1 B | 36 | +11% (+6 … +29) | +5% (−5 … +68) | +1% (−3 … +6) | 0% … +3% |
| grapheme_strlen($s) @ ASCII 2 B | 35 | +14% (−3 … +18) | +3% (−6 … +11) | 0% (−7 … +13) ~ | 0% … +4% |
| grapheme_strlen($s) @ ASCII 3 B | 37 | +4% (−12 … +20) | +1% (−6 … +13) | +1% (−6 … +12) | 0% … +5% |
| grapheme_strlen($s) @ ASCII 4 B | 42 | +1% (−3 … +16) | 0% (−7 … +55) | −1% (−6 … +7) | 0% … +6% |
| grapheme_strlen($s) @ ASCII 5 B | 44 | −2% (−9 … +5) | 0% (−8 … +18) ~ | +4% (−7 … +14) | 0% … +7% |
| grapheme_strlen($s) @ ASCII 8 B | 47 | −1% (−13 … +2) ~ | −2% (−8 … +7) | 0% (−8 … +2) ~ | 0% … +9% |
| grapheme_strlen($s) @ ASCII 9 B | 52 | −22% (−35 … −13) | −23% (−28 … −18) | 0% (−6 … +9) ~ | −20% … 0% |
| grapheme_strlen($s) @ ASCII 10 B | 54 | −24% (−30 … −17) | −23% (−27 … −21) | 0% (−7 … +6) ~ | −19% … 0% |
| grapheme_strlen($s) @ ASCII 16 B | 66 | −27% (−29 … −22) | −24% (−27 … −19) | 0% (−10 … +4) | −14% … 0% |
| grapheme_strlen($s) @ ASCII 64 B | 179 | −63% (−66 … −63) | −61% (−62 … −54) | 0% (−2 … +2) | −51% … 0% |
| grapheme_strlen($s) @ ASCII 256 B | 561 | −75% (−75 … −74) | −75% (−75 … −74) | 0% (−1 … +1) ~ | −68% … 0% |
| grapheme_strlen($s) @ ASCII 1 KB | 2,100 | −78% (−78 … −76) | −78% (−79 … −77) | 0% (0 … 0) ~ | −73% … 0% |
| grapheme_strlen($s) @ ASCII 4 KB | 8,262 | −80% (−80 … −79) | −80% (−81 … −80) | 0% (0 … 0) | −75% … 0% |
| grapheme_strlen($s) @ ASCII 1 KB, CR LF every 80 B | 63,581 | 0% (−2 … +2) | 0% (−4 … +3) ~ | 0% (−2 … +1) ~ | 0% |
| grapheme_strlen($s) @ ASCII 1 KB, lone CR every 80 B | 2,101 | −78% (−78 … −77) | −81% (−81 … −80) | 0% (0 … 0) ~ | −73% … 0% |
| grapheme_strlen($s) @ ASCII 1 KB, "é" first | 63,255 | 0% (−1 … +9) ~ | 0% (−3 … +24) | 0% (−4 … +5) ~ | 0% |
| grapheme_strlen($s) @ ASCII 16 B, "é" last | 2,244 | −3% (−4 … 0) | 0% (−3 … +2) | 0% (−1 … +1) | 0% |
| grapheme_strlen($s) @ ASCII 64 B, "é" last | 5,193 | −4% (−6 … −3) | −2% (−14 … +5) | 0% (−1 … +3) | −2% … 0% |
| grapheme_strlen($s) @ ASCII 256 B, "é" last | 17,275 | −3% (−16 … +13) | −2% (−14 … 0) | 0% (−1 … +7) ~ | −2% … 0% |
| grapheme_strlen($s) @ ASCII 1 KB, "é" last | 65,310 | −3% (−4 … +3) | −2% (−4 … +3) | 0% (−4 … +2) ~ | −2% … 0% |
| grapheme_strlen($s) @ ASCII 4 KB, "é" last | 257,050 | −3% (−6 … −2) | −3% (−28 … +1) | 0% (0 … +39) | −2% … 0% |
| grapheme_strlen($s) @ Chinese 16 B | 1,563 | −4% (−4 … −3) layout? | +4% (+3 … +4) layout? | 0% (−2 … +4) | 0% |
| grapheme_strlen($s) @ Chinese 64 B | 2,636 | −2% (−4 … +1) | +1% (0 … +2) | 0% (−2 … +3) ~ | 0% |
| grapheme_strlen($s) @ Chinese 256 B | 7,354 | −1% (−5 … +8) | 0% (−18 … +2) | 0% (−1 … +1) ~ | 0% |
| grapheme_strlen($s) @ Chinese 1 KB | 26,549 | 0% (−1 … +5) | +1% (−5 … +8) | 0% (−11 … +4) ~ | 0% |
| grapheme_strlen($s) @ Chinese 4 KB | 99,628 | 0% (−1 … +2) | 0% (−2 … +3) | 0% (−1 … +4) ~ | 0% |
| grapheme_strlen($s) @ Spanish 256 B | 16,110 | 0% (−2 … +1) | 0% (−2 … +2) | 0% (−3 … +9) | 0% |
| grapheme_strlen($s) @ Russian 256 B | 10,397 | −1% (−3 … +2) | 0% (−5 … 0) | −1% (−3 … 0) | 0% |
| grapheme_strlen($s) @ Japanese 256 B | 7,520 | −1% (−2 … +1) | +1% (−2 … +7) | 0% (−2 … +46) ~ | 0% |
| grapheme_strlen($s) @ Korean 256 B | 8,346 | 0% (−8 … +11) | +1% (−7 … +5) | 0% (−5 … +7) | 0% |
| grapheme_strlen($s) @ English 256 B, ’ every 170 B | 16,925 | −1% (−6 … +17) | 0% (−5 … +2) | 0% (−3 … +16) ~ | −1% … 0% |
| grapheme_strlen($s) @ English 1 KB, ’ every 170 B | 63,018 | 0% (−3 … +6) | 0% (−2 … +3) | 0% (−6 … +7) | 0% |
| grapheme_strlen($s) @ English 4 KB, ’ every 170 B | 247,041 | 0% (−27 … 0) | 0% (−1 … +4) | 0% (−2 … +1) ~ | 0% |
| grapheme_strlen($s) @ emoji and text 256 B | 11,890 | 0% (−3 … +13) | 0% (−2 … +5) ~ | 0% (−4 … +3) | 0% |
| grapheme_substr($s, 0, 8) @ ASCII 1 B | 99 | −9% (−20 … −4) | 0% (−17 … +16) ~ | 0% (−4 … +13) | 0% … +2% |
| grapheme_substr($s, 0, 8) @ ASCII 2 B | 102 | −10% (−18 … +6) | 0% (−9 … +3) ~ | −1% (−14 … +5) | 0% … +2% |
| grapheme_substr($s, 0, 8) @ ASCII 3 B | 103 | −11% (−24 … +4) | −2% (−7 … +3) | −1% (−14 … +16) | 0% … +3% |
| grapheme_substr($s, 0, 8) @ ASCII 4 B | 102 | −10% (−22 … −6) | −1% (−14 … +18) | −1% (−8 … +8) | 0% … +3% |
| grapheme_substr($s, 0, 8) @ ASCII 5 B | 104 | −11% (−18 … +10) | −1% (−9 … +4) ~ | −1% (−15 … +9) ~ | 0% … +4% |
| grapheme_substr($s, 0, 8) @ ASCII 8 B | 102 | −5% (−15 … +8) | −5% (−15 … +1) ~ | +1% (−3 … +16) ~ | 0% … +5% |
| grapheme_substr($s, 0, 8) @ ASCII 9 B | 106 | −13% (−25 … −2) | −14% (−22 … −10) | 0% (−5 … +8) ~ | −9% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 10 B | 104 | −14% (−17 … −10) | −12% (−17 … +6) | +1% (−6 … +5) ~ | −9% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 16 B | 116 | −14% (−19 … −12) | −16% (−20 … −5) | −1% (−8 … +9) ~ | −8% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 64 B | 227 | −49% (−50 … −43) | −49% (−50 … −40) | 0% (−4 … +6) ~ | −39% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 256 B | 611 | −69% (−70 … −66) | −69% (−69 … −69) | 0% (−2 … +1) | −63% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 1 KB | 2,150 | −76% (−76 … −74) | −77% (−77 … −76) | 0% (0 … 0) ~ | −72% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 4 KB | 8,311 | −79% (−79 … −79) | −80% (−80 … −80) | 0% (0 … 0) ~ | −74% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 1 KB, CR LF every 80 B | 7,715 | −2% (−5 … −1) | −1% (−1 … +1) | 0% (−1 … +2) | −2% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 1 KB, lone CR every 80 B | 2,149 | −76% (−76 … −75) | −79% (−79 … −78) | 0% (0 … 0) | −72% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 1 KB, "é" first | 7,609 | 0% (−1 … +1) ~ | +1% (0 … +2) | 0% (−1 … +2) ~ | 0% |
| grapheme_substr($s, 0, 8) @ ASCII 16 B, "é" last | 2,073 | 0% (−5 … +1) ~ | 0% (−4 … +3) | 0% (−13 … +1) ~ | 0% |
| grapheme_substr($s, 0, 8) @ ASCII 64 B, "é" last | 2,448 | −5% (−6 … −2) | −3% (−8 … 0) | 0% (−1 … +5) ~ | −4% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 256 B, "é" last | 3,913 | −12% (−14 … −9) | −10% (−11 … −8) | 0% (−2 … +8) ~ | −11% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 1 KB, "é" last | 9,681 | −17% (−18 … −16) | −16% (−18 … −15) | 0% (−1 … 0) | −18% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 4 KB, "é" last | 32,868 | −20% (−20 … −20) | −20% (−20 … −20) | 0% (0 … 0) ~ | −21% … 0% |
| grapheme_substr($s, 0, 8) @ Chinese 16 B | 1,763 | 0% (−1 … 0) | +1% (+1 … +2) | 0% (0 … +1) ~ | 0% |
| grapheme_substr($s, 0, 8) @ Chinese 64 B | 2,327 | 0% (−1 … +2) | +1% (−3 … +7) | 0% (−2 … +1) ~ | 0% |
| grapheme_substr($s, 0, 8) @ Chinese 256 B | 3,143 | +1% (−6 … +1) | +1% (0 … +35) | 0% (−2 … +1) ~ | 0% |
| grapheme_substr($s, 0, 8) @ Chinese 1 KB | 6,377 | 0% (−1 … +1) | +1% (−1 … +2) | 0% (−1 … 0) | 0% |
| grapheme_substr($s, 0, 8) @ Chinese 4 KB | 19,064 | 0% (0 … +4) | 0% (−5 … 0) | 0% (0 … 0) ~ | 0% |
| grapheme_substr($s, 0, 8) @ Spanish 256 B | 3,373 | −2% (−4 … +1) | +2% (−1 … +3) | 0% (−2 … +1) ~ | 0% |
| grapheme_substr($s, 0, 8) @ Russian 256 B | 3,306 | 0% (0 … +4) | 0% (0 … +3) | 0% (−2 … +1) | 0% |
| grapheme_substr($s, 0, 8) @ Japanese 256 B | 3,102 | 0% (−1 … +3) | +2% (+1 … +4) | 0% (−1 … +1) ~ | 0% |
| grapheme_substr($s, 0, 8) @ Korean 256 B | 3,140 | −1% (−1 … +3) | +2% (−7 … +3) | 0% (−1 … 0) ~ | 0% |
| grapheme_substr($s, 0, 8) @ English 256 B, ’ every 170 B | 3,663 | −8% (−13 … −5) | −5% (−7 … −3) | +1% (−3 … +2) | −6% … 0% |
| grapheme_substr($s, 0, 8) @ English 1 KB, ’ every 170 B | 7,956 | −4% (−6 … +1) | −2% (−17 … −1) | 0% (−1 … +1) ~ | −3% … 0% |
| grapheme_substr($s, 0, 8) @ English 4 KB, ’ every 170 B | 25,238 | −1% (−2 … +1) | 0% (−1 … +5) | 0% (−1 … 0) ~ | −1% … 0% |
| grapheme_substr($s, 0, 8) @ emoji and text 256 B | 3,606 | −1% (−1 … 0) | 0% (−1 … +2) ~ | 0% (−2 … +1) | 0% |
| grapheme_strpos($s, 'zz') @ ASCII 1 B | 56 | +13% (+10 … +25) | +15% (+4 … +19) | 0% (−7 … +14) ~ | 0% … +9% |
| grapheme_strpos($s, 'zz') @ ASCII 2 B | 69 | +11% (+3 … +19) | +10% (0 … +14) | 0% (−6 … +2) ~ | 0% … +8% |
| grapheme_strpos($s, 'zz') @ ASCII 3 B | 74 | +6% (+1 … +14) | +5% (−2 … +11) | −1% (−5 … +39) | 0% … +8% |
| grapheme_strpos($s, 'zz') @ ASCII 4 B | 73 | +6% (0 … +9) | +8% (−1 … +11) | +2% (−7 … +7) | 0% … +9% |
| grapheme_strpos($s, 'zz') @ ASCII 5 B | 75 | +3% (−1 … +12) | +5% (+1 … +172) | −1% (−6 … +2) | 0% … +9% |
| grapheme_strpos($s, 'zz') @ ASCII 8 B | 81 | +3% (−4 … +10) | +2% (−7 … +7) ~ | −1% (−5 … +6) ~ | 0% … +10% |
| grapheme_strpos($s, 'zz') @ ASCII 9 B | 83 | −8% (−18 … −1) | −12% (−17 … −6) | +2% (−4 … +9) | −7% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 10 B | 88 | −11% (−18 … −5) | −9% (−18 … −3) | 0% (−6 … +5) | −6% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 16 B | 103 | −16% (−20 … −13) | −16% (−20 … −10) | −1% (−5 … +4) | −6% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 64 B | 226 | −49% (−52 … −49) | −50% (−53 … −49) | 0% (−2 … +2) ~ | −39% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 256 B | 638 | −67% (−67 … −66) | −67% (−67 … −65) | 0% (−1 … +1) | −60% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 1 KB | 2,349 | −69% (−70 … −68) | −70% (−70 … −69) | 0% (0 … 0) ~ | −67% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 4 KB | 9,333 | −70% (−71 … −70) | −71% (−71 … −71) | 0% (0 … 0) ~ | −69% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 1 KB, CR LF every 80 B | 112,860 | 0% (−1 … 0) | 0% (−1 … +1) | 0% (0 … 0) ~ | 0% |
| grapheme_strpos($s, 'zz') @ ASCII 1 KB, lone CR every 80 B | 2,349 | −69% (−70 … −68) | −73% (−73 … −72) | 0% (0 … 0) | −67% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 1 KB, "é" first | 112,784 | 0% (0 … 0) | 0% (0 … 0) | 0% (0 … 0) ~ | 0% |
| grapheme_strpos($s, 'zz') @ ASCII 16 B, "é" last | 6,187 | −1% (−3 … +3) | 0% (−2 … +4) ~ | 0% (−2 … +2) ~ | 0% |
| grapheme_strpos($s, 'zz') @ ASCII 64 B, "é" last | 11,365 | −1% (−3 … 0) | −1% (−3 … +1) | 0% (−1 … +1) ~ | −1% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 256 B, "é" last | 32,082 | −2% (−2 … −1) | −1% (−2 … −1) | 0% (−1 … +1) | −1% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 1 KB, "é" last | 114,841 | −1% (−2 … −1) | −1% (−30 … −1) | 0% (−1 … 0) | −2% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 4 KB, "é" last | 444,760 | −2% (−2 … −1) | −2% (−2 … −1) | 0% (−1 … 0) ~ | −2% … 0% |
| grapheme_strpos($s, 'zz') @ Chinese 16 B | 5,551 | 0% (−3 … 0) | −1% (−3 … +1) | 0% (−2 … +3) | 0% |
| grapheme_strpos($s, 'zz') @ Chinese 64 B | 8,703 | 0% (−2 … +4) ~ | +1% (−1 … +3) | 0% (−2 … +2) | 0% |
| grapheme_strpos($s, 'zz') @ Chinese 256 B | 21,681 | 0% (−1 … +1) ~ | +1% (−1 … +1) | 0% (−1 … +1) ~ | 0% |
| grapheme_strpos($s, 'zz') @ Chinese 1 KB | 72,936 | 0% (−1 … +1) | 0% (−1 … +1) | 0% (−1 … +1) | 0% |
| grapheme_strpos($s, 'zz') @ Chinese 4 KB | 281,234 | 0% (−1 … +1) | 0% (−1 … +3) ~ | 0% (−1 … +1) ~ | 0% |
| grapheme_strpos($s, 'zz') @ Spanish 256 B | 31,926 | 0% (−1 … +1) ~ | 0% (−1 … +1) ~ | 0% (−1 … 0) ~ | 0% |
| grapheme_strpos($s, 'zz') @ Russian 256 B | 20,924 | 0% (−1 … +2) | 0% (−1 … +1) | 0% (−2 … +1) ~ | 0% |
| grapheme_strpos($s, 'zz') @ Japanese 256 B | 14,932 | 0% (−12 … +1) ~ | 0% (−1 … +1) ~ | 0% (−1 … +1) ~ | 0% |
| grapheme_strpos($s, 'zz') @ Korean 256 B | 28,001 | 0% (−1 … +1) ~ | 0% (−1 … +1) ~ | 0% (−1 … +1) ~ | 0% |
| grapheme_strpos($s, 'zz') @ English 256 B, ’ every 170 B | 31,467 | −1% (−2 … 0) | −1% (−1 … 0) | 0% (−3 … +1) | −1% … 0% |
| grapheme_strpos($s, 'zz') @ English 1 KB, ’ every 170 B | 111,277 | 0% (−1 … +4) | 0% (−1 … 0) | 0% (−1 … +1) | 0% |
| grapheme_strpos($s, 'zz') @ English 4 KB, ’ every 170 B | 431,176 | 0% (−1 … 0) | 0% (−2 … 0) | 0% (−1 … 0) ~ | 0% |
| grapheme_strpos($s, 'zz') @ emoji and text 256 B | 25,054 | −1% (−12 … +1) | 0% (−1 … +1) | 0% (−1 … +1) ~ | 0% |
| grapheme_extract($s, 8) @ ASCII 1 B | 103 | +4% (+1 … +5) | +2% (−3 … +10) | 0% (−5 … +5) ~ | 0% … +1% |
| grapheme_extract($s, 8) @ ASCII 2 B | 106 | +2% (−1 … +5) | +2% (−16 … +10) | −1% (−9 … +18) | 0% … +2% |
| grapheme_extract($s, 8) @ ASCII 3 B | 108 | +3% (0 … +18) | +5% (−17 … +14) | −1% (−15 … +7) | 0% … +2% |
| grapheme_extract($s, 8) @ ASCII 4 B | 109 | +1% (−2 … +4) | +3% (−8 … +30) | +3% (−9 … +31) | 0% … +3% |
| grapheme_extract($s, 8) @ ASCII 5 B | 109 | +2% (+1 … +4) | +2% (−12 … +7) | 0% (−4 … +13) ~ | 0% … +3% |
| grapheme_extract($s, 8) @ ASCII 8 B | 113 | +2% (+2 … +3) | −5% (−14 … +78) | +1% (−7 … +5) | 0% … +5% |
| grapheme_extract($s, 8) @ ASCII 9 B | 114 | −4% (−6 … −3) | −13% (−18 … −7) | 0% (−4 … +3) ~ | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 10 B | 114 | −4% (−5 … −2) | −11% (−15 … −8) | +1% (−3 … +7) | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 16 B | 114 | −4% (−5 … −4) | −12% (−16 … −5) | −1% (−8 … +14) | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 64 B | 114 | −5% (−7 … −4) | −14% (−19 … −6) | 0% (−2 … +5) ~ | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 256 B | 114 | −5% (−5 … −4) | −14% (−17 … −10) | −1% (−5 … +5) | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 1 KB | 114 | −4% (−5 … −3) | −12% (−19 … −7) | 0% (−7 … +6) ~ | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 4 KB | 114 | −5% (−7 … −4) | −12% (−16 … −9) | 0% (−11 … +6) | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 1 KB, CR LF every 80 B | 114 | −4% (−6 … −3) | −11% (−16 … +36) | +1% (−4 … +3) | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 1 KB, lone CR every 80 B | 114 | −5% (−6 … −2) | −12% (−18 … −8) | +1% (−3 … +4) | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 1 KB, "é" first | 2,373 | 0% (−2 … +5) ~ | 0% (−21 … +3) ~ | 0% (−2 … +1) ~ | 0% |
| grapheme_extract($s, 8) @ ASCII 16 B, "é" last | 114 | −5% (−7 … −4) | −12% (−15 … −4) | 0% (−7 … +4) ~ | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 64 B, "é" last | 114 | −4% (−5 … −3) | −12% (−19 … +1) | −1% (−7 … +5) | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 256 B, "é" last | 114 | −4% (−8 … −3) | −13% (−16 … +6) | 0% (−6 … +12) | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 1 KB, "é" last | 115 | −5% (−6 … −3) | −13% (−17 … −7) | 0% (−5 … +12) | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 4 KB, "é" last | 114 | −5% (−8 … −2) | −11% (−18 … −6) | −1% (−5 … +5) | −10% … 0% |
| grapheme_extract($s, 8) @ Chinese 16 B | 1,791 | 0% (−4 … +1) | 0% (−1 … +2) | 0% (−1 … +3) ~ | 0% |
| grapheme_extract($s, 8) @ Chinese 64 B | 2,738 | 0% (−4 … +37) | 0% (−5 … +2) | 0% (−16 … +1) | 0% |
| grapheme_extract($s, 8) @ Chinese 256 B | 3,038 | 0% (−3 … +32) | 0% (−2 … +31) ~ | 0% (−3 … +3) ~ | 0% |
| grapheme_extract($s, 8) @ Chinese 1 KB | 3,042 | 0% (−4 … +3) | 0% (−1 … +2) | 0% (−3 … +26) | 0% |
| grapheme_extract($s, 8) @ Chinese 4 KB | 3,038 | 0% (−2 … +34) ~ | 0% (−2 … +1) | 0% (−1 … +2) ~ | 0% |
| grapheme_extract($s, 8) @ Spanish 256 B | 2,219 | 0% (−2 … +1) ~ | −2% (−5 … 0) | 0% (−5 … +4) | −1% … 0% |
| grapheme_extract($s, 8) @ Russian 256 B | 2,866 | 0% (−2 … +1) ~ | 0% (−1 … +3) | 0% (−25 … +2) ~ | 0% |
| grapheme_extract($s, 8) @ Japanese 256 B | 2,958 | 0% (−2 … +1) ~ | 0% (−1 … +1) ~ | 0% (−2 … +11) ~ | 0% |
| grapheme_extract($s, 8) @ Korean 256 B | 2,812 | 0% (−2 … +5) | 0% (−2 … +8) | 0% (−2 … +28) ~ | 0% |
| grapheme_extract($s, 8) @ English 256 B, ’ every 170 B | 114 | −4% (−11 … −4) | −12% (−18 … −8) | −1% (−7 … +5) | −10% … 0% |
| grapheme_extract($s, 8) @ English 1 KB, ’ every 170 B | 114 | −4% (−5 … −3) | −13% (−18 … −8) | +1% (−4 … +6) | −10% … 0% |
| grapheme_extract($s, 8) @ English 4 KB, ’ every 170 B | 114 | −5% (−11 … −4) | −13% (−17 … −10) | 0% (−4 … +4) ~ | −10% … 0% |
| grapheme_extract($s, 8) @ emoji and text 256 B | 2,368 | +1% (0 … +5) | 0% (−1 … +2) | 0% (−1 … +1) ~ | 0% |
| grapheme_strpos($s, 'x') @ ASCII 1 B | 66 | +13% (+5 … +19) | +10% (+3 … +16) | +1% (−7 … +9) | 0% … +7% |
| grapheme_strpos($s, 'x') @ ASCII 5 B | 74 | +6% (+1 … +15) | +4% (−4 … +10) | +1% (−3 … +7) | 0% … +9% |
| grapheme_strpos($s, 'x') @ ASCII 9 B | 82 | −9% (−16 … +1) | −13% (−18 … +3) | −1% (−6 … +7) | −9% … 0% |
| grapheme_strpos($s, 'x') @ ASCII 16 B | 99 | −15% (−19 … −10) | −20% (−25 … −15) | +1% (−7 … +7) ~ | −7% … 0% |
| grapheme_strpos($s, 'x') @ ASCII 64 B | 198 | −57% (−58 … −53) | −56% (−57 … −55) | 0% (−2 … +2) ~ | −45% … 0% |
| grapheme_strpos($s, 'x') @ ASCII 256 B | 582 | −73% (−74 … −72) | −73% (−73 … −72) | 0% (−1 … +1) ~ | −66% … 0% |
| grapheme_strpos($s, 'x') @ ASCII 1 KB | 2,121 | −77% (−77 … −76) | −78% (−78 … −77) | 0% (−1 … 0) | −72% … 0% |
| grapheme_strpos($s, 'x') @ ASCII 4 KB | 8,278 | −79% (−79 … −79) | −80% (−80 … −80) | 0% (0 … 0) ~ | −74% … 0% |
| grapheme_strstr($s, 'o') @ ASCII 1 B | 69 | +12% (+1 … +17) | +11% (+5 … +20) | 0% (−7 … +7) ~ | 0% … +3% |
| grapheme_strstr($s, 'o') @ ASCII 5 B | 77 | +4% (+3 … +11) | +6% (0 … +11) | 0% (−9 … +8) ~ | 0% … +5% |
| grapheme_strstr($s, 'o') @ ASCII 9 B | 82 | −10% (−11 … +1) | −12% (−19 … −7) | 0% (−5 … +10) ~ | −13% … 0% |
| grapheme_strstr($s, 'o') @ ASCII 16 B | 125 | −9% (−12 … −4) | −15% (−19 … −12) | +1% (−4 … +3) | −7% … 0% |
| grapheme_strstr($s, 'o') @ ASCII 64 B | 237 | −45% (−47 … −45) | −44% (−45 … −42) | 0% (−3 … +2) ~ | −39% … 0% |
| grapheme_strstr($s, 'o') @ ASCII 256 B | 624 | −67% (−68 … −65) | −67% (−68 … −66) | 0% (−1 … +1) | −62% … 0% |
| grapheme_strstr($s, 'o') @ ASCII 1 KB | 2,186 | −73% (−74 … −73) | −75% (−75 … −74) | 0% (−1 … +1) | −71% … 0% |
| grapheme_strstr($s, 'o') @ ASCII 4 KB | 8,491 | −77% (−78 … −77) | −78% (−78 … −78) | 0% (−1 … 0) ~ | −73% … 0% |
| grapheme_stripos($s, 'Z') @ ASCII 1 B | 142 | +4% (−1 … +7) | +1% (−4 … +8) | 0% (−6 … +4) | 0% … +2% |
| grapheme_stripos($s, 'Z') @ ASCII 5 B | 151 | +2% (0 … +8) | −1% (−18 … +2) ~ | 0% (−6 … +2) ~ | 0% … +3% |
| grapheme_stripos($s, 'Z') @ ASCII 9 B | 164 | −5% (−6 … +1) | −8% (−13 … −6) | 0% (−2 … +3) ~ | −6% … 0% |
| grapheme_stripos($s, 'Z') @ ASCII 16 B | 175 | −9% (−12 … −6) | −12% (−13 … −10) | 0% (−2 … +3) ~ | −5% … 0% |
| grapheme_stripos($s, 'Z') @ ASCII 64 B | 282 | −35% (−37 … −34) | −42% (−42 … −40) | 0% (−2 … +1) ~ | −32% … 0% |
| grapheme_stripos($s, 'Z') @ ASCII 256 B | 690 | −60% (−61 … −57) | −62% (−63 … −62) | 0% (−2 … +2) ~ | −55% … 0% |
| grapheme_stripos($s, 'Z') @ ASCII 1 KB | 2,341 | −68% (−69 … −68) | −69% (−71 … −68) | +1% (−2 … +1) | −65% … 0% |
| grapheme_stripos($s, 'Z') @ ASCII 4 KB | 9,026 | −72% (−73 … −72) | −73% (−74 … −73) | 0% (0 … 0) ~ | −67% … 0% |
| grapheme_strrpos($s, 'e') @ ASCII 1 B | 61 | +6% (−2 … +17) | +7% (+3 … +9) | 0% (−7 … +20) ~ | 0% … +6% |
| grapheme_strrpos($s, 'e') @ ASCII 5 B | 59 | +4% (−5 … +12) | +4% (−1 … +6) | 0% (−6 … +5) ~ | 0% … +6% |
| grapheme_strrpos($s, 'e') @ ASCII 9 B | 74 | −14% (−19 … −8) | −13% (−20 … −8) | +1% (−7 … +9) | −12% … 0% |
| grapheme_strrpos($s, 'e') @ ASCII 16 B | 95 | −16% (−19 … −11) | −10% (−12 … −6) | −2% (−9 … +3) | −8% … 0% |
| grapheme_strrpos($s, 'e') @ ASCII 64 B | 194 | −56% (−58 … −54) | −56% (−57 … −55) | 0% (−3 … +2) | −44% … 0% |
| grapheme_strrpos($s, 'e') @ ASCII 256 B | 592 | −72% (−72 … −71) | −71% (−72 … −71) | 0% (−1 … +1) ~ | −63% … 0% |
| grapheme_strrpos($s, 'e') @ ASCII 1 KB | 2,119 | −77% (−77 … −76) | −77% (−78 … −77) | 0% (0 … 0) ~ | −72% … 0% |
| grapheme_strrpos($s, 'e') @ ASCII 4 KB | 8,275 | −79% (−79 … −78) | −80% (−80 … −80) | 0% (0 … 0) ~ | −74% … 0% |
| grapheme_strlen(next string) @ ASCII, mixed lengths 1-24 B | 100 | −27% (−36 … −23) | −33% (−37 … −29) | 0% (−6 … +7) ~ | −14% … 0% |
| grapheme_strlen(next string) @ ASCII 1 KB, "é" at a random position | 64,897 | −2% (−6 … −1) | −2% (−8 … +2) | 0% (−4 … +4) ~ | −1% … 0% |
| grapheme_substr(next string, 0, 8) @ ASCII, mixed lengths 1-24 B | 159 | −9% (−15 … −7) | −8% (−10 … −6) | 0% (−3 … +9) ~ | −8% … 0% |
| grapheme_substr(next string, 0, 8) @ ASCII 1 KB, "é" at a random position | 8,773 | −9% (−10 … −5) | −9% (−11 … −8) | 0% (−1 … +1) ~ | −11% … 0% |
| grapheme_strpos(next string, 'zz') @ ASCII, mixed lengths 1-24 B | 144 | −11% (−14 … −7) | −12% (−17 … −8) | 0% (−8 … +7) ~ | −6% … 0% |
| grapheme_strpos(next string, 'zz') @ ASCII 1 KB, "é" at a random position | 113,931 | −1% (−1 … 0) | −1% (−1 … 0) | 0% (−1 … 0) | −1% … 0% |

Control: master against itself.

| call | master, CPU cycles per call (GCC 15.2) | A/A start | A/A end |
|---|--:|--:|--:|
| grapheme_strlen($s) @ ASCII 1 B | 33 | 0% (−10 … +9) | 0% (−16 … +19) |
| grapheme_strlen($s) @ ASCII 2 B | 37 | 0% (−8 … +19) | 0% (−8 … +19) |
| grapheme_strlen($s) @ ASCII 3 B | 40 | 0% (−8 … +11) | 0% (−15 … +16) |
| grapheme_strlen($s) @ ASCII 4 B | 42 | 0% (−15 … +8) | 0% (−15 … +12) |
| grapheme_strlen($s) @ ASCII 5 B | 44 | 0% (−7 … +16) | 0% (−14 … +8) |
| grapheme_strlen($s) @ ASCII 8 B | 50 | 0% (−8 … +7) | +2% (−8 … +9) |
| grapheme_strlen($s) @ ASCII 9 B | 49 | 0% (−12 … +13) | 0% (−12 … +13) |
| grapheme_strlen($s) @ ASCII 10 B | 54 | 0% (−11 … +6) | 0% (−11 … +6) |
| grapheme_strlen($s) @ ASCII 16 B | 66 | 0% (−5 … +6) | 0% (−6 … +6) |
| grapheme_strlen($s) @ ASCII 64 B | 176 | 0% (−2 … +3) | 0% (−3 … +2) |
| grapheme_strlen($s) @ ASCII 256 B | 563 | 0% (−1 … +1) | 0% (−1 … +2) |
| grapheme_strlen($s) @ ASCII 1 KB | 2,097 | 0% (0 … 0) | 0% (0 … 0) |
| grapheme_strlen($s) @ ASCII 4 KB | 8,243 | 0% (0 … 0) | 0% (−1 … 0) |
| grapheme_strlen($s) @ ASCII 1 KB, CR LF every 80 B | 63,450 | 0% (−6 … +3) | 0% (−8 … +2) |
| grapheme_strlen($s) @ ASCII 1 KB, lone CR every 80 B | 2,097 | 0% (0 … 0) | 0% (−1 … 0) |
| grapheme_strlen($s) @ ASCII 1 KB, "é" first | 63,039 | 0% (−4 … +7) | 0% (−2 … +3) |
| grapheme_strlen($s) @ ASCII 16 B, "é" last | 2,241 | 0% (−1 … +2) | 0% (−2 … +2) |
| grapheme_strlen($s) @ ASCII 64 B, "é" last | 5,178 | 0% (−19 … +1) | 0% (−3 … +30) |
| grapheme_strlen($s) @ ASCII 256 B, "é" last | 17,240 | +1% (−1 … +24) | 0% (−3 … +3) |
| grapheme_strlen($s) @ ASCII 1 KB, "é" last | 65,180 | 0% (−10 … +2) | 0% (−27 … +3) |
| grapheme_strlen($s) @ ASCII 4 KB, "é" last | 256,687 | 0% (−2 … +15) | 0% (−1 … +5) |
| grapheme_strlen($s) @ Chinese 16 B | 1,561 | 0% (−1 … 0) | 0% (−1 … +1) |
| grapheme_strlen($s) @ Chinese 64 B | 2,633 | 0% (−2 … +3) | 0% (−2 … +41) |
| grapheme_strlen($s) @ Chinese 256 B | 7,336 | 0% (−3 … +12) | 0% (−2 … +6) |
| grapheme_strlen($s) @ Chinese 1 KB | 26,488 | 0% (−2 … +52) | 0% (−3 … 0) |
| grapheme_strlen($s) @ Chinese 4 KB | 99,422 | 0% (−5 … +2) | 0% (−2 … +1) |
| grapheme_strlen($s) @ Spanish 256 B | 16,091 | 0% (−2 … +7) | 0% (−3 … +2) |
| grapheme_strlen($s) @ Russian 256 B | 10,369 | 0% (−3 … +3) | 0% (−3 … +2) |
| grapheme_strlen($s) @ Japanese 256 B | 7,501 | 0% (0 … +8) | 0% (−3 … +20) |
| grapheme_strlen($s) @ Korean 256 B | 8,333 | 0% (−8 … +20) | 0% (−8 … +3) |
| grapheme_strlen($s) @ English 256 B, ’ every 170 B | 16,952 | 0% (−13 … +19) | 0% (−4 … +3) |
| grapheme_strlen($s) @ English 1 KB, ’ every 170 B | 62,686 | 0% (−1 … +2) | 0% (−40 … +1) |
| grapheme_strlen($s) @ English 4 KB, ’ every 170 B | 246,456 | 0% (−8 … +6) | 0% (−1 … +1) |
| grapheme_strlen($s) @ emoji and text 256 B | 11,850 | 0% (−4 … +28) | 0% (−3 … +5) |
| grapheme_substr($s, 0, 8) @ ASCII 1 B | 99 | 0% (−7 … +19) | 0% (−13 … +12) |
| grapheme_substr($s, 0, 8) @ ASCII 2 B | 102 | 0% (−9 … +10) | 0% (−1 … +8) |
| grapheme_substr($s, 0, 8) @ ASCII 3 B | 103 | 0% (−7 … +22) | 0% (−6 … +5) |
| grapheme_substr($s, 0, 8) @ ASCII 4 B | 102 | 0% (−6 … +15) | +1% (−14 … +16) |
| grapheme_substr($s, 0, 8) @ ASCII 5 B | 103 | +6% (−6 … +13) | 0% (−12 … +39) |
| grapheme_substr($s, 0, 8) @ ASCII 8 B | 101 | 0% (−14 … +10) | +5% (−6 … +17) |
| grapheme_substr($s, 0, 8) @ ASCII 9 B | 102 | +1% (−11 … +10) | −1% (−12 … +13) |
| grapheme_substr($s, 0, 8) @ ASCII 10 B | 105 | −2% (−6 … +12) | +1% (−10 … +13) |
| grapheme_substr($s, 0, 8) @ ASCII 16 B | 116 | −1% (−6 … +2) | −1% (−7 … +4) |
| grapheme_substr($s, 0, 8) @ ASCII 64 B | 226 | +1% (−3 … +4) | 0% (−2 … +4) |
| grapheme_substr($s, 0, 8) @ ASCII 256 B | 610 | 0% (−1 … +1) | 0% (−1 … +1) |
| grapheme_substr($s, 0, 8) @ ASCII 1 KB | 2,146 | 0% (0 … 0) | 0% (0 … 0) |
| grapheme_substr($s, 0, 8) @ ASCII 4 KB | 8,292 | 0% (0 … 0) | 0% (−1 … 0) |
| grapheme_substr($s, 0, 8) @ ASCII 1 KB, CR LF every 80 B | 7,695 | 0% (−1 … +4) | 0% (−5 … +4) |
| grapheme_substr($s, 0, 8) @ ASCII 1 KB, lone CR every 80 B | 2,146 | 0% (0 … 0) | 0% (−1 … 0) |
| grapheme_substr($s, 0, 8) @ ASCII 1 KB, "é" first | 7,615 | 0% (−1 … +4) | 0% (−4 … +1) |
| grapheme_substr($s, 0, 8) @ ASCII 16 B, "é" last | 2,068 | 0% (−1 … +8) | 0% (−12 … +2) |
| grapheme_substr($s, 0, 8) @ ASCII 64 B, "é" last | 2,443 | 0% (0 … +2) | 0% (−2 … +1) |
| grapheme_substr($s, 0, 8) @ ASCII 256 B, "é" last | 3,916 | 0% (−6 … +1) | 0% (−6 … +1) |
| grapheme_substr($s, 0, 8) @ ASCII 1 KB, "é" last | 9,666 | 0% (−1 … +1) | 0% (−1 … +1) |
| grapheme_substr($s, 0, 8) @ ASCII 4 KB, "é" last | 32,791 | 0% (0 … 0) | 0% (−1 … 0) |
| grapheme_substr($s, 0, 8) @ Chinese 16 B | 1,759 | 0% (0 … 0) | 0% (−1 … +5) |
| grapheme_substr($s, 0, 8) @ Chinese 64 B | 2,321 | 0% (−1 … +5) | 0% (−1 … +1) |
| grapheme_substr($s, 0, 8) @ Chinese 256 B | 3,143 | 0% (−2 … +1) | 0% (−3 … +1) |
| grapheme_substr($s, 0, 8) @ Chinese 1 KB | 6,354 | 0% (−4 … +1) | 0% (−1 … 0) |
| grapheme_substr($s, 0, 8) @ Chinese 4 KB | 19,018 | 0% (−5 … 0) | 0% (−19 … +6) |
| grapheme_substr($s, 0, 8) @ Spanish 256 B | 3,366 | 0% (−1 … +19) | 0% (−2 … +2) |
| grapheme_substr($s, 0, 8) @ Russian 256 B | 3,299 | 0% (−1 … +3) | 0% (−1 … +1) |
| grapheme_substr($s, 0, 8) @ Japanese 256 B | 3,098 | 0% (−3 … +1) | 0% (−5 … +10) |
| grapheme_substr($s, 0, 8) @ Korean 256 B | 3,129 | 0% (0 … +1) | 0% (−1 … +2) |
| grapheme_substr($s, 0, 8) @ English 256 B, ’ every 170 B | 3,626 | 0% (−3 … +3) | 0% (−1 … +2) |
| grapheme_substr($s, 0, 8) @ English 1 KB, ’ every 170 B | 7,945 | 0% (−1 … +1) | 0% (−1 … +2) |
| grapheme_substr($s, 0, 8) @ English 4 KB, ’ every 170 B | 25,150 | 0% (0 … 0) | 0% (−1 … +1) |
| grapheme_substr($s, 0, 8) @ emoji and text 256 B | 3,599 | 0% (−5 … +1) | 0% (−1 … +1) |
| grapheme_strpos($s, 'zz') @ ASCII 1 B | 53 | 0% (−9 … +10) | 0% (−9 … +6) |
| grapheme_strpos($s, 'zz') @ ASCII 2 B | 72 | 0% (−4 … +8) | 0% (−8 … +5) |
| grapheme_strpos($s, 'zz') @ ASCII 3 B | 74 | 0% (−4 … +9) | 0% (−6 … +9) |
| grapheme_strpos($s, 'zz') @ ASCII 4 B | 76 | 0% (−8 … +4) | 0% (−8 … +9) |
| grapheme_strpos($s, 'zz') @ ASCII 5 B | 78 | 0% (−8 … +8) | 0% (−4 … +6) |
| grapheme_strpos($s, 'zz') @ ASCII 8 B | 81 | +3% (−6 … +8) | +2% (−12 … +6) |
| grapheme_strpos($s, 'zz') @ ASCII 9 B | 83 | 0% (−6 … +7) | −1% (−7 … +7) |
| grapheme_strpos($s, 'zz') @ ASCII 10 B | 85 | 0% (−3 … +7) | 0% (−8 … +7) |
| grapheme_strpos($s, 'zz') @ ASCII 16 B | 103 | 0% (−6 … +6) | 0% (−6 … +6) |
| grapheme_strpos($s, 'zz') @ ASCII 64 B | 226 | −1% (−3 … +4) | 0% (−2 … +2) |
| grapheme_strpos($s, 'zz') @ ASCII 256 B | 634 | 0% (−1 … +1) | 0% (−1 … +1) |
| grapheme_strpos($s, 'zz') @ ASCII 1 KB | 2,344 | 0% (0 … +4) | 0% (−1 … 0) |
| grapheme_strpos($s, 'zz') @ ASCII 4 KB | 9,307 | 0% (0 … 0) | 0% (−1 … 0) |
| grapheme_strpos($s, 'zz') @ ASCII 1 KB, CR LF every 80 B | 112,734 | 0% (−7 … 0) | 0% (−1 … 0) |
| grapheme_strpos($s, 'zz') @ ASCII 1 KB, lone CR every 80 B | 2,344 | 0% (0 … 0) | 0% (−1 … 0) |
| grapheme_strpos($s, 'zz') @ ASCII 1 KB, "é" first | 112,578 | 0% (0 … 0) | 0% (−1 … 0) |
| grapheme_strpos($s, 'zz') @ ASCII 16 B, "é" last | 6,216 | 0% (−2 … +2) | 0% (−3 … +3) |
| grapheme_strpos($s, 'zz') @ ASCII 64 B, "é" last | 11,332 | +1% (−1 … +2) | 0% (−1 … +3) |
| grapheme_strpos($s, 'zz') @ ASCII 256 B, "é" last | 32,014 | 0% (−1 … +1) | 0% (−1 … +1) |
| grapheme_strpos($s, 'zz') @ ASCII 1 KB, "é" last | 114,613 | 0% (0 … 0) | 0% (−1 … 0) |
| grapheme_strpos($s, 'zz') @ ASCII 4 KB, "é" last | 444,304 | 0% (−1 … 0) | 0% (−1 … 0) |
| grapheme_strpos($s, 'zz') @ Chinese 16 B | 5,508 | 0% (−3 … +4) | 0% (−5 … +3) |
| grapheme_strpos($s, 'zz') @ Chinese 64 B | 8,691 | 0% (−1 … +1) | 0% (−2 … +1) |
| grapheme_strpos($s, 'zz') @ Chinese 256 B | 21,683 | 0% (−2 … +1) | 0% (−4 … +1) |
| grapheme_strpos($s, 'zz') @ Chinese 1 KB | 72,917 | 0% (0 … +1) | 0% (−1 … +3) |
| grapheme_strpos($s, 'zz') @ Chinese 4 KB | 280,557 | 0% (−1 … +1) | 0% (−2 … +1) |
| grapheme_strpos($s, 'zz') @ Spanish 256 B | 31,887 | 0% (0 … 0) | 0% (0 … +1) |
| grapheme_strpos($s, 'zz') @ Russian 256 B | 20,938 | 0% (−1 … +1) | 0% (−1 … 0) |
| grapheme_strpos($s, 'zz') @ Japanese 256 B | 14,980 | 0% (−1 … +1) | +1% (−3 … +1) |
| grapheme_strpos($s, 'zz') @ Korean 256 B | 27,983 | 0% (−1 … +1) | 0% (−1 … 0) |
| grapheme_strpos($s, 'zz') @ English 256 B, ’ every 170 B | 31,424 | 0% (−1 … +2) | 0% (−1 … 0) |
| grapheme_strpos($s, 'zz') @ English 1 KB, ’ every 170 B | 111,140 | 0% (0 … 0) | 0% (−1 … 0) |
| grapheme_strpos($s, 'zz') @ English 4 KB, ’ every 170 B | 430,397 | 0% (0 … 0) | 0% (−1 … 0) |
| grapheme_strpos($s, 'zz') @ emoji and text 256 B | 25,048 | 0% (−1 … +2) | 0% (−1 … +1) |
| grapheme_extract($s, 8) @ ASCII 1 B | 103 | 0% (−2 … +3) | 0% (−2 … +2) |
| grapheme_extract($s, 8) @ ASCII 2 B | 107 | −1% (−2 … +2) | 0% (−2 … +2) |
| grapheme_extract($s, 8) @ ASCII 3 B | 107 | 0% (−4 … +2) | 0% (−2 … +2) |
| grapheme_extract($s, 8) @ ASCII 4 B | 109 | 0% (−2 … +4) | 0% (−1 … +4) |
| grapheme_extract($s, 8) @ ASCII 5 B | 109 | 0% (−3 … +2) | 0% (−2 … +3) |
| grapheme_extract($s, 8) @ ASCII 8 B | 113 | 0% (−1 … +1) | 0% (−1 … +1) |
| grapheme_extract($s, 8) @ ASCII 9 B | 114 | 0% (−3 … +1) | 0% (−1 … +1) |
| grapheme_extract($s, 8) @ ASCII 10 B | 114 | 0% (−1 … +1) | 0% (−1 … +1) |
| grapheme_extract($s, 8) @ ASCII 16 B | 114 | 0% (0 … +1) | 0% (−8 … +3) |
| grapheme_extract($s, 8) @ ASCII 64 B | 114 | 0% (−1 … +7) | 0% (−2 … +1) |
| grapheme_extract($s, 8) @ ASCII 256 B | 114 | 0% (−19 … +1) | 0% (−1 … +1) |
| grapheme_extract($s, 8) @ ASCII 1 KB | 114 | 0% (−2 … +5) | 0% (−1 … +1) |
| grapheme_extract($s, 8) @ ASCII 4 KB | 114 | 0% (−4 … +1) | 0% (−1 … +1) |
| grapheme_extract($s, 8) @ ASCII 1 KB, CR LF every 80 B | 114 | 0% (−14 … +7) | 0% (−1 … +2) |
| grapheme_extract($s, 8) @ ASCII 1 KB, lone CR every 80 B | 114 | 0% (−2 … +1) | 0% (−3 … 0) |
| grapheme_extract($s, 8) @ ASCII 1 KB, "é" first | 2,364 | 0% (−2 … +1) | 0% (−4 … +4) |
| grapheme_extract($s, 8) @ ASCII 16 B, "é" last | 114 | 0% (−1 … +1) | 0% (−1 … +10) |
| grapheme_extract($s, 8) @ ASCII 64 B, "é" last | 114 | 0% (−1 … +1) | 0% (−2 … +2) |
| grapheme_extract($s, 8) @ ASCII 256 B, "é" last | 114 | 0% (−1 … +1) | 0% (−2 … +1) |
| grapheme_extract($s, 8) @ ASCII 1 KB, "é" last | 114 | 0% (−1 … +3) | 0% (−1 … +3) |
| grapheme_extract($s, 8) @ ASCII 4 KB, "é" last | 114 | 0% (−1 … +1) | 0% (−3 … +1) |
| grapheme_extract($s, 8) @ Chinese 16 B | 1,788 | 0% (−31 … +5) | 0% (−5 … 0) |
| grapheme_extract($s, 8) @ Chinese 64 B | 2,730 | 0% (−1 … +3) | 0% (−1 … 0) |
| grapheme_extract($s, 8) @ Chinese 256 B | 3,031 | 0% (−7 … +2) | 0% (−2 … +1) |
| grapheme_extract($s, 8) @ Chinese 1 KB | 3,031 | 0% (−1 … +3) | 0% (−5 … +1) |
| grapheme_extract($s, 8) @ Chinese 4 KB | 3,031 | 0% (−1 … +4) | 0% (−2 … +2) |
| grapheme_extract($s, 8) @ Spanish 256 B | 2,213 | 0% (−2 … +3) | 0% (−1 … +6) |
| grapheme_extract($s, 8) @ Russian 256 B | 2,861 | 0% (−1 … +1) | 0% (−3 … +2) |
| grapheme_extract($s, 8) @ Japanese 256 B | 2,954 | 0% (−18 … +3) | 0% (−1 … +3) |
| grapheme_extract($s, 8) @ Korean 256 B | 2,806 | 0% (−2 … +3) | 0% (−2 … +1) |
| grapheme_extract($s, 8) @ English 256 B, ’ every 170 B | 114 | 0% (0 … +6) | 0% (−1 … +1) |
| grapheme_extract($s, 8) @ English 1 KB, ’ every 170 B | 114 | 0% (−1 … +1) | 0% (−2 … +2) |
| grapheme_extract($s, 8) @ English 4 KB, ’ every 170 B | 114 | 0% (−2 … +1) | 0% (−2 … +13) |
| grapheme_extract($s, 8) @ emoji and text 256 B | 2,370 | 0% (−8 … +10) | 0% (−1 … +2) |
| grapheme_strpos($s, 'x') @ ASCII 1 B | 66 | 0% (−10 … +10) | 0% (−11 … +12) |
| grapheme_strpos($s, 'x') @ ASCII 5 B | 74 | 0% (−5 … +9) | 0% (−8 … +9) |
| grapheme_strpos($s, 'x') @ ASCII 9 B | 81 | 0% (−4 … +8) | 0% (−7 … +8) |
| grapheme_strpos($s, 'x') @ ASCII 16 B | 99 | 0% (−7 … +7) | −2% (−8 … +6) |
| grapheme_strpos($s, 'x') @ ASCII 64 B | 198 | 0% (−3 … +2) | 0% (−3 … +2) |
| grapheme_strpos($s, 'x') @ ASCII 256 B | 582 | 0% (−2 … +1) | 0% (−1 … 0) |
| grapheme_strpos($s, 'x') @ ASCII 1 KB | 2,115 | 0% (0 … 0) | 0% (0 … 0) |
| grapheme_strpos($s, 'x') @ ASCII 4 KB | 8,261 | 0% (0 … 0) | 0% (0 … 0) |
| grapheme_strstr($s, 'o') @ ASCII 1 B | 69 | 0% (−5 … +10) | −1% (−8 … +11) |
| grapheme_strstr($s, 'o') @ ASCII 5 B | 77 | 0% (−11 … +6) | 0% (−8 … +8) |
| grapheme_strstr($s, 'o') @ ASCII 9 B | 85 | 0% (−7 … +4) | +3% (−7 … +7) |
| grapheme_strstr($s, 'o') @ ASCII 16 B | 128 | 0% (−5 … +3) | 0% (−5 … +8) |
| grapheme_strstr($s, 'o') @ ASCII 64 B | 237 | 0% (−4 … +4) | −1% (−3 … 0) |
| grapheme_strstr($s, 'o') @ ASCII 256 B | 622 | 0% (−3 … +1) | 0% (−1 … +1) |
| grapheme_strstr($s, 'o') @ ASCII 1 KB | 2,184 | 0% (−1 … 0) | 0% (0 … 0) |
| grapheme_strstr($s, 'o') @ ASCII 4 KB | 8,473 | 0% (0 … 0) | 0% (0 … 0) |
| grapheme_stripos($s, 'Z') @ ASCII 1 B | 140 | 0% (−4 … +5) | 0% (−4 … +5) |
| grapheme_stripos($s, 'Z') @ ASCII 5 B | 153 | 0% (−9 … +2) | −1% (−5 … +3) |
| grapheme_stripos($s, 'Z') @ ASCII 9 B | 164 | 0% (−4 … +2) | 0% (−4 … +7) |
| grapheme_stripos($s, 'Z') @ ASCII 16 B | 175 | 0% (−3 … +2) | +1% (−2 … +5) |
| grapheme_stripos($s, 'Z') @ ASCII 64 B | 282 | 0% (−2 … +1) | 0% (−2 … +2) |
| grapheme_stripos($s, 'Z') @ ASCII 256 B | 688 | 0% (−1 … +1) | 0% (−2 … +1) |
| grapheme_stripos($s, 'Z') @ ASCII 1 KB | 2,337 | 0% (0 … 0) | 0% (0 … +4) |
| grapheme_stripos($s, 'Z') @ ASCII 4 KB | 9,007 | 0% (0 … +1) | 0% (−1 … 0) |
| grapheme_strrpos($s, 'e') @ ASCII 1 B | 61 | 0% (−6 … +16) | +2% (−14 … +16) |
| grapheme_strrpos($s, 'e') @ ASCII 5 B | 59 | +2% (−13 … +16) | 0% (−5 … +11) |
| grapheme_strrpos($s, 'e') @ ASCII 9 B | 74 | 0% (−9 … +5) | −1% (−8 … +5) |
| grapheme_strrpos($s, 'e') @ ASCII 16 B | 97 | 0% (−8 … +6) | +2% (−6 … +10) |
| grapheme_strrpos($s, 'e') @ ASCII 64 B | 197 | 0% (−3 … +3) | 0% (−4 … +5) |
| grapheme_strrpos($s, 'e') @ ASCII 256 B | 589 | 0% (−1 … +1) | 0% (−1 … +2) |
| grapheme_strrpos($s, 'e') @ ASCII 1 KB | 2,116 | 0% (0 … 0) | 0% (−1 … 0) |
| grapheme_strrpos($s, 'e') @ ASCII 4 KB | 8,273 | 0% (0 … 0) | 0% (0 … 0) |
| grapheme_strlen(next string) @ ASCII, mixed lengths 1-24 B | 98 | +1% (−3 … +5) | 0% (−8 … +10) |
| grapheme_strlen(next string) @ ASCII 1 KB, "é" at a random position | 64,747 | 0% (−10 … +4) | −1% (−29 … +1) |
| grapheme_substr(next string, 0, 8) @ ASCII, mixed lengths 1-24 B | 158 | 0% (−1 … +6) | 0% (−3 … +3) |
| grapheme_substr(next string, 0, 8) @ ASCII 1 KB, "é" at a random position | 8,762 | 0% (−1 … +1) | 0% (−1 … +1) |
| grapheme_strpos(next string, 'zz') @ ASCII, mixed lengths 1-24 B | 144 | 0% (−3 … +3) | 0% (−9 … +7) |
| grapheme_strpos(next string, 'zz') @ ASCII 1 KB, "é" at a random position | 113,741 | 0% (0 … 0) | 0% (−1 … 0) |

~: within noise, the change is no larger than the difference between master and master on the same row.

layout?: in every pass the cycles changed in the same direction, by 3% or more in the median, the instructions by less than 0.5%: the work is the same, so look for the cause (code placement, branch prediction) with `bench why` before reporting the row.
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
