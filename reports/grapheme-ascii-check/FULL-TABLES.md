# Full tables of the grapheme_ascii_check() report

All 159 calls of [`grapheme.php`](grapheme.php) in the main series of the [report](README.md). Change in CPU cycles per call against master (negative = fewer cycles, faster), the median over 15 passes and, in brackets, the lowest and the highest pass. The last column is the change in instructions over the three groups, the master-against-master group included.

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
| grapheme_strlen($s) @ ASCII 1 B | 36 | +9% (+8 … +13) | +4% (−4 … +64) | −2% (−10 … +9) | 0% … +3% |
| grapheme_strlen($s) @ ASCII 2 B | 38 | +6% (+5 … +14) | +5% (−5 … +8) | 0% (−11 … +9) | 0% … +4% |
| grapheme_strlen($s) @ ASCII 3 B | 40 | +2% (0 … +11) | −1% (−6 … +11) | 0% (−13 … +14) | 0% … +5% |
| grapheme_strlen($s) @ ASCII 4 B | 42 | 0% (−1 … +9) | −2% (−7 … +8) | +5% (−5 … +73) | 0% … +6% |
| grapheme_strlen($s) @ ASCII 5 B | 44 | −2% (−9 … −2) | −1% (−8 … +2) | −1% (−43 … +5) | 0% … +7% |
| grapheme_strlen($s) @ ASCII 8 B | 50 | −6% (−12 … −6) | −3% (−9 … +5) | 0% (−8 … +14) | 0% … +9% |
| grapheme_strlen($s) @ ASCII 9 B | 52 | −23% (−24 … −17) | −25% (−29 … −18) | +3% (−8 … +13) | −20% … 0% |
| grapheme_strlen($s) @ ASCII 10 B | 54 | −24% (−33 … −18) | −24% (−27 … −7) | 0% (−8 … +12) | −19% … 0% |
| grapheme_strlen($s) @ ASCII 16 B | 69 | −28% (−33 … −25) | −25% (−28 … −19) | 0% (−9 … +7) | −14% … 0% |
| grapheme_strlen($s) @ ASCII 64 B | 179 | −63% (−65 … −63) | −61% (−62 … −59) | 0% (−2 … +2) | −51% … 0% |
| grapheme_strlen($s) @ ASCII 256 B | 564 | −75% (−75 … −75) | −75% (−75 … −74) | 0% (−1 … +1) | −68% … 0% |
| grapheme_strlen($s) @ ASCII 1 KB | 2,105 | −77% (−78 … −77) | −78% (−78 … −78) | 0% (0 … 0) | −73% … 0% |
| grapheme_strlen($s) @ ASCII 4 KB | 8,264 | −80% (−81 … −79) | −80% (−81 … −80) | 0% (0 … +1) | −75% … 0% |
| grapheme_strlen($s) @ ASCII 1 KB, CR LF every 80 B | 63,529 | 0% (−3 … +5) ~ | 0% (−3 … +1) ~ | 0% (−4 … +1) ~ | 0% |
| grapheme_strlen($s) @ ASCII 1 KB, lone CR every 80 B | 2,103 | −77% (−78 … −77) | −80% (−81 … −80) | 0% (−1 … 0) | −73% … 0% |
| grapheme_strlen($s) @ ASCII 1 KB, "é" first | 63,221 | 0% (−4 … +9) | 0% (−2 … +6) | 0% (−5 … +3) ~ | 0% |
| grapheme_strlen($s) @ ASCII 16 B, "é" last | 2,244 | −3% (−4 … −1) | +1% (−1 … +4) | 0% (−2 … +1) ~ | 0% |
| grapheme_strlen($s) @ ASCII 64 B, "é" last | 5,186 | −3% (−4 … −1) | −2% (−3 … 0) | 0% (−1 … +3) | −2% … 0% |
| grapheme_strlen($s) @ ASCII 256 B, "é" last | 17,297 | −3% (−6 … −1) | −2% (−28 … −1) | 0% (−1 … +3) ~ | −2% … 0% |
| grapheme_strlen($s) @ ASCII 1 KB, "é" last | 65,214 | −2% (−3 … 0) | −2% (−4 … +10) | 0% (−2 … +2) ~ | −2% … 0% |
| grapheme_strlen($s) @ ASCII 4 KB, "é" last | 257,840 | −2% (−4 … +2) | −2% (−29 … −1) | 0% (−2 … +46) ~ | −2% … 0% |
| grapheme_strlen($s) @ Chinese 16 B | 1,564 | −4% (−4 … +7) | +4% (+3 … +5) layout? | 0% (−4 … +6) ~ | 0% |
| grapheme_strlen($s) @ Chinese 64 B | 2,638 | −2% (−4 … −1) | +1% (0 … +2) | 0% (−1 … +1) ~ | 0% |
| grapheme_strlen($s) @ Chinese 256 B | 7,350 | −1% (−2 … +3) | 0% (−1 … +2) | 0% (−5 … +2) | 0% |
| grapheme_strlen($s) @ Chinese 1 KB | 26,525 | 0% (−1 … +5) ~ | 0% (−3 … +4) | 0% (−2 … +18) | 0% |
| grapheme_strlen($s) @ Chinese 4 KB | 99,615 | 0% (0 … +4) ~ | 0% (−3 … +1) ~ | 0% (−3 … +11) ~ | 0% |
| grapheme_strlen($s) @ Spanish 256 B | 16,102 | 0% (−2 … +2) | 0% (−2 … +2) | 0% (−18 … +2) | 0% |
| grapheme_strlen($s) @ Russian 256 B | 10,386 | 0% (−1 … +1) ~ | 0% (−4 … +3) ~ | 0% (−9 … +2) ~ | 0% |
| grapheme_strlen($s) @ Japanese 256 B | 7,530 | −1% (−20 … +2) | 0% (−2 … +11) | 0% (−30 … +1) ~ | 0% |
| grapheme_strlen($s) @ Korean 256 B | 8,346 | 0% (−10 … +2) | +1% (−1 … +3) | 0% (−17 … +6) ~ | 0% |
| grapheme_strlen($s) @ emoji and text 256 B | 11,893 | −1% (−3 … 0) | 0% (−3 … +2) ~ | 0% (−2 … +4) ~ | 0% |
| grapheme_substr($s, 0, 8) @ ASCII 1 B | 99 | −9% (−17 … −4) | 0% (−14 … +5) | 0% (−6 … +13) ~ | 0% … +2% |
| grapheme_substr($s, 0, 8) @ ASCII 2 B | 102 | −10% (−20 … +5) | −1% (−8 … +20) | 0% (−11 … +15) | 0% … +2% |
| grapheme_substr($s, 0, 8) @ ASCII 3 B | 103 | −10% (−23 … −6) | −3% (−12 … +2) | +2% (−9 … +4) | 0% … +3% |
| grapheme_substr($s, 0, 8) @ ASCII 4 B | 103 | −10% (−20 … +13) | −3% (−14 … +5) | −1% (−10 … +7) ~ | 0% … +3% |
| grapheme_substr($s, 0, 8) @ ASCII 5 B | 103 | −9% (−20 … +6) | −3% (−10 … +11) | 0% (−13 … +8) ~ | 0% … +4% |
| grapheme_substr($s, 0, 8) @ ASCII 8 B | 100 | −4% (−34 … +9) | −6% (−12 … +11) | +1% (−6 … +6) | 0% … +5% |
| grapheme_substr($s, 0, 8) @ ASCII 9 B | 103 | −13% (−21 … −1) | −16% (−22 … +5) | +1% (−7 … +10) ~ | −9% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 10 B | 104 | −13% (−24 … −4) | −15% (−21 … 0) | 0% (−23 … +7) ~ | −9% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 16 B | 117 | −14% (−16 … −3) | −17% (−22 … −6) | −2% (−5 … +5) | −8% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 64 B | 226 | −48% (−50 … −42) | −50% (−52 … −43) | 0% (−3 … +3) | −39% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 256 B | 611 | −69% (−71 … −69) | −69% (−69 … −68) | 0% (−3 … +1) | −63% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 1 KB | 2,152 | −76% (−76 … −75) | −77% (−77 … −76) | 0% (−1 … 0) | −72% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 4 KB | 8,311 | −79% (−79 … −79) | −80% (−80 … −80) | 0% (0 … 0) ~ | −74% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 1 KB, CR LF every 80 B | 7,735 | −1% (−3 … +1) | −1% (−2 … 0) | 0% (−1 … +1) ~ | −2% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 1 KB, lone CR every 80 B | 2,152 | −76% (−76 … −75) | −79% (−79 … −78) | 0% (−1 … 0) | −72% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 1 KB, "é" first | 7,663 | 0% (−1 … +1) ~ | +1% (0 … +1) | 0% (−1 … +2) ~ | 0% |
| grapheme_substr($s, 0, 8) @ ASCII 16 B, "é" last | 2,074 | 0% (−2 … +1) ~ | −1% (−3 … +2) | 0% (−1 … +2) | 0% |
| grapheme_substr($s, 0, 8) @ ASCII 64 B, "é" last | 2,447 | −5% (−10 … 0) | −3% (−4 … −1) | 0% (−3 … +3) ~ | −4% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 256 B, "é" last | 3,905 | −11% (−15 … −9) | −9% (−33 … −7) | 0% (−2 … +1) ~ | −11% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 1 KB, "é" last | 9,681 | −17% (−18 … −16) | −17% (−18 … −16) | 0% (−3 … 0) | −18% … 0% |
| grapheme_substr($s, 0, 8) @ ASCII 4 KB, "é" last | 32,876 | −20% (−20 … −20) | −20% (−21 … −20) | 0% (0 … 0) ~ | −21% … 0% |
| grapheme_substr($s, 0, 8) @ Chinese 16 B | 1,762 | 0% (−3 … +2) | +1% (0 … +2) | 0% (0 … +1) ~ | 0% |
| grapheme_substr($s, 0, 8) @ Chinese 64 B | 2,327 | +1% (−1 … +5) | +1% (−1 … +4) | 0% (−1 … +4) ~ | 0% |
| grapheme_substr($s, 0, 8) @ Chinese 256 B | 3,148 | +1% (0 … +1) | +1% (0 … +2) | 0% (−1 … 0) ~ | 0% |
| grapheme_substr($s, 0, 8) @ Chinese 1 KB | 6,361 | 0% (−3 … +1) ~ | 0% (0 … +2) | 0% (0 … 0) ~ | 0% |
| grapheme_substr($s, 0, 8) @ Chinese 4 KB | 19,045 | 0% (−1 … +5) | 0% (−2 … +1) | 0% (0 … 0) ~ | 0% |
| grapheme_substr($s, 0, 8) @ Spanish 256 B | 3,381 | −1% (−4 … 0) | +1% (0 … +5) | 0% (−1 … +1) ~ | 0% |
| grapheme_substr($s, 0, 8) @ Russian 256 B | 3,304 | 0% (−2 … +1) | +1% (−2 … +1) | 0% (−1 … +2) | 0% |
| grapheme_substr($s, 0, 8) @ Japanese 256 B | 3,122 | 0% (−4 … +1) ~ | +2% (0 … +4) | 0% (−2 … +10) | 0% |
| grapheme_substr($s, 0, 8) @ Korean 256 B | 3,136 | 0% (−2 … +1) | +2% (+1 … +5) | 0% (−1 … +10) ~ | 0% |
| grapheme_substr($s, 0, 8) @ emoji and text 256 B | 3,606 | −1% (−2 … +2) | 0% (−1 … +1) | 0% (−3 … +1) ~ | 0% |
| grapheme_strpos($s, 'zz') @ ASCII 1 B | 56 | +13% (+7 … +15) | +12% (+5 … +22) | +6% (−8 … +35) | 0% … +9% |
| grapheme_strpos($s, 'zz') @ ASCII 2 B | 72 | +7% (+2 … +11) | +7% (−1 … +15) | −1% (−13 … +6) | 0% … +8% |
| grapheme_strpos($s, 'zz') @ ASCII 3 B | 74 | +6% (+1 … +9) | +7% (+2 … +12) | −1% (−12 … +8) | 0% … +8% |
| grapheme_strpos($s, 'zz') @ ASCII 4 B | 76 | +5% (−2 … +15) | +5% (−1 … +10) | +1% (−6 … +9) | 0% … +9% |
| grapheme_strpos($s, 'zz') @ ASCII 5 B | 78 | +3% (−2 … +8) | +5% (0 … +11) | +2% (−5 … +9) | 0% … +9% |
| grapheme_strpos($s, 'zz') @ ASCII 8 B | 84 | 0% (−4 … +6) | +2% (−2 … +8) | 0% (−5 … +10) | 0% … +10% |
| grapheme_strpos($s, 'zz') @ ASCII 9 B | 86 | −10% (−13 … −7) | −11% (−12 … −6) | −1% (−6 … +5) | −7% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 10 B | 88 | −11% (−14 … −4) | −10% (−16 … −5) | 0% (−5 … +3) | −6% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 16 B | 103 | −17% (−19 … −15) | −14% (−18 … −12) | 0% (−9 … +8) | −6% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 64 B | 226 | −50% (−51 … −49) | −50% (−51 … −43) | 0% (−2 … +3) | −39% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 256 B | 639 | −67% (−67 … −67) | −67% (−67 … −63) | 0% (−1 … +1) | −60% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 1 KB | 2,348 | −69% (−69 … −69) | −70% (−70 … −70) | 0% (0 … 0) ~ | −67% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 4 KB | 9,319 | −70% (−71 … −70) | −71% (−71 … −71) | 0% (0 … 0) | −69% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 1 KB, CR LF every 80 B | 113,026 | 0% (−1 … 0) | 0% (−1 … 0) | 0% (−1 … 0) | 0% |
| grapheme_strpos($s, 'zz') @ ASCII 1 KB, lone CR every 80 B | 2,349 | −69% (−69 … −69) | −73% (−73 … −72) | 0% (0 … 0) | −67% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 1 KB, "é" first | 112,803 | 0% (−1 … 0) | 0% (0 … 0) | 0% (−1 … +1) | 0% |
| grapheme_strpos($s, 'zz') @ ASCII 16 B, "é" last | 6,280 | −1% (−3 … +2) | +1% (−2 … +2) | 0% (−3 … +5) ~ | 0% |
| grapheme_strpos($s, 'zz') @ ASCII 64 B, "é" last | 11,427 | −2% (−2 … 0) | −1% (−2 … +1) | 0% (−2 … +2) | −1% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 256 B, "é" last | 32,038 | −2% (−2 … −1) | −1% (−2 … 0) | 0% (−1 … 0) ~ | −1% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 1 KB, "é" last | 114,849 | −1% (−2 … −1) | −2% (−2 … −1) | 0% (−1 … 0) ~ | −2% … 0% |
| grapheme_strpos($s, 'zz') @ ASCII 4 KB, "é" last | 444,985 | −1% (−2 … −1) | −1% (−2 … −1) | 0% (−1 … +1) | −2% … 0% |
| grapheme_strpos($s, 'zz') @ Chinese 16 B | 5,544 | 0% (−3 … +2) ~ | 0% (−3 … +2) ~ | 0% (−3 … +2) ~ | 0% |
| grapheme_strpos($s, 'zz') @ Chinese 64 B | 8,708 | 0% (−2 … 0) | +1% (−6 … +2) | 0% (−3 … +2) | 0% |
| grapheme_strpos($s, 'zz') @ Chinese 256 B | 21,673 | 0% (−1 … +1) | 0% (−13 … +2) | 0% (−2 … +1) ~ | 0% |
| grapheme_strpos($s, 'zz') @ Chinese 1 KB | 72,901 | 0% (−1 … +2) ~ | 0% (−2 … +1) ~ | 0% (−2 … +10) | 0% |
| grapheme_strpos($s, 'zz') @ Chinese 4 KB | 281,108 | 0% (−1 … +1) | 0% (−1 … +1) ~ | 0% (−1 … +1) ~ | 0% |
| grapheme_strpos($s, 'zz') @ Spanish 256 B | 31,957 | 0% (−1 … 0) | 0% (−1 … +1) | 0% (0 … 0) | 0% |
| grapheme_strpos($s, 'zz') @ Russian 256 B | 20,950 | 0% (−4 … +1) ~ | 0% (−1 … +1) ~ | 0% (−3 … +3) ~ | 0% |
| grapheme_strpos($s, 'zz') @ Japanese 256 B | 14,926 | 0% (−1 … +1) | 0% (−1 … +1) ~ | 0% (−1 … +15) ~ | 0% |
| grapheme_strpos($s, 'zz') @ Korean 256 B | 27,983 | 0% (−1 … +1) ~ | 0% (−2 … +1) ~ | 0% (−1 … +1) ~ | 0% |
| grapheme_strpos($s, 'zz') @ emoji and text 256 B | 25,057 | −1% (−1 … 0) | 0% (−1 … +1) ~ | 0% (−3 … +1) ~ | 0% |
| grapheme_extract($s, 8) @ ASCII 1 B | 104 | +4% (+2 … +5) | +4% (−3 … +8) | 0% (−10 … +8) ~ | 0% … +1% |
| grapheme_extract($s, 8) @ ASCII 2 B | 106 | +3% (−3 … +4) | +3% (−12 … +9) | 0% (−5 … +8) ~ | 0% … +2% |
| grapheme_extract($s, 8) @ ASCII 3 B | 107 | +2% (0 … +3) | 0% (−7 … +5) ~ | −1% (−10 … +7) | 0% … +2% |
| grapheme_extract($s, 8) @ ASCII 4 B | 109 | +2% (0 … +6) | +2% (−7 … +9) | 0% (−6 … +7) ~ | 0% … +3% |
| grapheme_extract($s, 8) @ ASCII 5 B | 110 | +1% (0 … +4) | 0% (−11 … +7) | −1% (−7 … +5) | 0% … +3% |
| grapheme_extract($s, 8) @ ASCII 8 B | 114 | +2% (+1 … +3) | −4% (−6 … +4) | 0% (−8 … +7) | 0% … +5% |
| grapheme_extract($s, 8) @ ASCII 9 B | 114 | −5% (−5 … −2) | −13% (−18 … −8) | −1% (−7 … +10) | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 10 B | 114 | −4% (−6 … −4) | −13% (−18 … −7) | 0% (−7 … +4) | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 16 B | 115 | −5% (−6 … −4) | −14% (−18 … −7) | +1% (−7 … +6) | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 64 B | 114 | −5% (−7 … −4) | −14% (−18 … −8) | +1% (−18 … +7) | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 256 B | 114 | −5% (−6 … 0) | −13% (−16 … −9) | −1% (−21 … +5) | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 1 KB | 114 | −4% (−5 … −2) | −11% (−18 … −1) | +2% (−7 … +4) | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 4 KB | 114 | −5% (−6 … +12) | −13% (−18 … −8) | +2% (−10 … +5) | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 1 KB, CR LF every 80 B | 114 | −4% (−5 … −3) | −12% (−15 … −4) | +1% (−5 … +7) | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 1 KB, lone CR every 80 B | 114 | −4% (−5 … −3) | −12% (−15 … −3) | −1% (−8 … +6) | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 1 KB, "é" first | 2,380 | 0% (−2 … +31) ~ | 0% (−3 … +2) ~ | 0% (−2 … +1) ~ | 0% |
| grapheme_extract($s, 8) @ ASCII 16 B, "é" last | 114 | −4% (−5 … 0) | −16% (−27 … −11) | −1% (−4 … +5) ~ | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 64 B, "é" last | 114 | −4% (−6 … −1) | −12% (−18 … −8) | +1% (−7 … +4) | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 256 B, "é" last | 115 | −5% (−5 … +4) | −14% (−16 … −8) | 0% (−4 … +4) ~ | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 1 KB, "é" last | 114 | −5% (−7 … −3) | −13% (−24 … −4) | +1% (−14 … +15) | −10% … 0% |
| grapheme_extract($s, 8) @ ASCII 4 KB, "é" last | 114 | −5% (−8 … −3) | −14% (−18 … −2) | 0% (−7 … +15) | −10% … 0% |
| grapheme_extract($s, 8) @ Chinese 16 B | 1,791 | −1% (−7 … +2) | 0% (−2 … +2) | 0% (−1 … +1) | 0% |
| grapheme_extract($s, 8) @ Chinese 64 B | 2,739 | 0% (−11 … +5) | 0% (−3 … +5) | 0% (−5 … +1) | 0% |
| grapheme_extract($s, 8) @ Chinese 256 B | 3,041 | 0% (−2 … +2) | 0% (−1 … +1) ~ | 0% (−1 … +12) ~ | 0% |
| grapheme_extract($s, 8) @ Chinese 1 KB | 3,036 | 0% (−1 … +2) ~ | 0% (−1 … +1) | 0% (−1 … +4) ~ | 0% |
| grapheme_extract($s, 8) @ Chinese 4 KB | 3,039 | 0% (−2 … +1) | 0% (−2 … +1) | 0% (−1 … +1) | 0% |
| grapheme_extract($s, 8) @ Spanish 256 B | 2,218 | 0% (−35 … +1) | −2% (−6 … +28) | 0% (−1 … +2) ~ | −1% … 0% |
| grapheme_extract($s, 8) @ Russian 256 B | 2,865 | 0% (−18 … +1) ~ | 0% (−1 … +2) ~ | 0% (−2 … +1) | 0% |
| grapheme_extract($s, 8) @ Japanese 256 B | 2,951 | 0% (−3 … +2) ~ | 0% (−1 … +6) | 0% (−2 … +4) | 0% |
| grapheme_extract($s, 8) @ Korean 256 B | 2,814 | 0% (−1 … +2) | 0% (−2 … +2) | 0% (−2 … +2) | 0% |
| grapheme_extract($s, 8) @ emoji and text 256 B | 2,370 | 0% (−2 … +5) | 0% (−19 … +1) | 0% (−2 … +20) | 0% |
| grapheme_strpos($s, 'x') @ ASCII 1 B | 66 | +13% (+11 … +24) | +8% (−15 … +14) | 0% (−8 … +11) ~ | 0% … +7% |
| grapheme_strpos($s, 'x') @ ASCII 5 B | 74 | +7% (0 … +14) | +4% (−2 … +10) | +4% (−5 … +11) | 0% … +9% |
| grapheme_strpos($s, 'x') @ ASCII 9 B | 82 | −9% (−12 … −3) | −14% (−17 … +1) | +1% (−9 … +5) | −9% … 0% |
| grapheme_strpos($s, 'x') @ ASCII 16 B | 99 | −15% (−32 … −12) | −19% (−20 … −15) | +1% (−5 … +8) | −7% … 0% |
| grapheme_strpos($s, 'x') @ ASCII 64 B | 198 | −57% (−59 … −56) | −57% (−57 … −56) | 0% (−2 … +3) | −45% … 0% |
| grapheme_strpos($s, 'x') @ ASCII 256 B | 583 | −73% (−74 … −71) | −73% (−73 … −73) | 0% (−1 … +1) ~ | −66% … 0% |
| grapheme_strpos($s, 'x') @ ASCII 1 KB | 2,123 | −77% (−77 … −76) | −78% (−78 … −77) | 0% (0 … 0) | −72% … 0% |
| grapheme_strpos($s, 'x') @ ASCII 4 KB | 8,282 | −79% (−79 … −79) | −80% (−80 … −80) | 0% (0 … 0) | −74% … 0% |
| grapheme_strstr($s, 'o') @ ASCII 1 B | 69 | +9% (+8 … +14) | +11% (+5 … +20) | +1% (−5 … +12) | 0% … +3% |
| grapheme_strstr($s, 'o') @ ASCII 5 B | 77 | +3% (−1 … +11) | +5% (0 … +12) | 0% (−10 … +10) | 0% … +5% |
| grapheme_strstr($s, 'o') @ ASCII 9 B | 85 | −10% (−11 … −6) | −12% (−18 … −6) | −1% (−7 … +9) | −13% … 0% |
| grapheme_strstr($s, 'o') @ ASCII 16 B | 128 | −11% (−12 … −7) | −15% (−20 … −12) | −1% (−2 … +5) | −7% … 0% |
| grapheme_strstr($s, 'o') @ ASCII 64 B | 236 | −46% (−47 … −45) | −44% (−45 … −41) | 0% (−3 … +4) | −39% … 0% |
| grapheme_strstr($s, 'o') @ ASCII 256 B | 622 | −67% (−67 … −65) | −66% (−67 … −64) | 0% (−1 … +1) | −62% … 0% |
| grapheme_strstr($s, 'o') @ ASCII 1 KB | 2,188 | −73% (−74 … −73) | −74% (−75 … −74) | 0% (0 … 0) ~ | −71% … 0% |
| grapheme_strstr($s, 'o') @ ASCII 4 KB | 8,496 | −77% (−77 … −77) | −78% (−78 … −78) | 0% (0 … 0) ~ | −73% … 0% |
| grapheme_stripos($s, 'Z') @ ASCII 1 B | 140 | +4% (+2 … +6) | +1% (−3 … +5) | 0% (−45 … +7) | 0% … +2% |
| grapheme_stripos($s, 'Z') @ ASCII 5 B | 151 | +2% (+1 … +4) | −1% (−5 … +3) | −1% (−18 … +4) | 0% … +3% |
| grapheme_stripos($s, 'Z') @ ASCII 9 B | 162 | −5% (−7 … +2) | −8% (−12 … −5) | 0% (−4 … +3) | −6% … 0% |
| grapheme_stripos($s, 'Z') @ ASCII 16 B | 174 | −10% (−16 … −8) | −12% (−15 … −9) | 0% (−3 … +4) ~ | −5% … 0% |
| grapheme_stripos($s, 'Z') @ ASCII 64 B | 280 | −36% (−38 … −36) | −42% (−43 … −41) | 0% (−3 … +20) | −32% … 0% |
| grapheme_stripos($s, 'Z') @ ASCII 256 B | 689 | −59% (−60 … −59) | −62% (−63 … −61) | 0% (−1 … +2) | −55% … 0% |
| grapheme_stripos($s, 'Z') @ ASCII 1 KB | 2,342 | −68% (−69 … −68) | −69% (−70 … −69) | 0% (−2 … +2) | −65% … 0% |
| grapheme_stripos($s, 'Z') @ ASCII 4 KB | 9,030 | −72% (−73 … −72) | −73% (−74 … −73) | 0% (−1 … 0) ~ | −67% … 0% |
| grapheme_strrpos($s, 'e') @ ASCII 1 B | 64 | +7% (0 … +11) | +5% (−3 … +9) | 0% (−27 … +14) | 0% … +6% |
| grapheme_strrpos($s, 'e') @ ASCII 5 B | 62 | 0% (−5 … +5) | +5% (−3 … +7) | +1% (−4 … +9) | 0% … +6% |
| grapheme_strrpos($s, 'e') @ ASCII 9 B | 75 | −15% (−19 … −12) | −11% (−15 … −8) | −1% (−5 … +5) ~ | −12% … 0% |
| grapheme_strrpos($s, 'e') @ ASCII 16 B | 99 | −17% (−19 … −15) | −10% (−15 … −8) | −1% (−5 … +1) | −8% … 0% |
| grapheme_strrpos($s, 'e') @ ASCII 64 B | 197 | −57% (−57 … −54) | −57% (−58 … −55) | 0% (−3 … +4) | −44% … 0% |
| grapheme_strrpos($s, 'e') @ ASCII 256 B | 593 | −72% (−72 … −72) | −71% (−71 … −71) | 0% (−1 … +2) | −63% … 0% |
| grapheme_strrpos($s, 'e') @ ASCII 1 KB | 2,121 | −77% (−77 … −77) | −78% (−78 … −77) | 0% (−1 … 0) ~ | −72% … 0% |
| grapheme_strrpos($s, 'e') @ ASCII 4 KB | 8,291 | −79% (−79 … −79) | −80% (−80 … −80) | 0% (0 … 0) | −74% … 0% |
| grapheme_strlen(next string) @ ASCII, mixed lengths 1-24 B | 100 | −29% (−35 … −25) | −31% (−35 … −30) | 0% (−33 … +4) | −14% … 0% |
| grapheme_substr(next string, 0, 8) @ ASCII, mixed lengths 1-24 B | 159 | −7% (−9 … −5) | −8% (−10 … −7) | 0% (−1 … +2) | −8% … 0% |
| grapheme_strpos(next string, 'zz') @ ASCII, mixed lengths 1-24 B | 145 | −11% (−16 … −5) | −12% (−16 … −8) | 0% (−4 … +5) ~ | −6% … 0% |

Control: master against itself.

| call | master, CPU cycles per call (GCC 15.2) | A/A start | A/A end |
|---|--:|--:|--:|
| grapheme_strlen($s) @ ASCII 1 B | 36 | 0% (−10 … 0) | 0% (−11 … 0) |
| grapheme_strlen($s) @ ASCII 2 B | 38 | 0% (0 … +8) | 0% (−8 … 0) |
| grapheme_strlen($s) @ ASCII 3 B | 40 | 0% (−10 … 0) | 0% (−2 … +10) |
| grapheme_strlen($s) @ ASCII 4 B | 42 | 0% (0 … +17) | 0% (−1 … 0) |
| grapheme_strlen($s) @ ASCII 5 B | 44 | 0% (−7 … +1) | 0% (−7 … +8) |
| grapheme_strlen($s) @ ASCII 8 B | 50 | 0% (−8 … +5) | 0% (−8 … 0) |
| grapheme_strlen($s) @ ASCII 9 B | 52 | 0% (−8 … +7) | 0% (0 … +4) |
| grapheme_strlen($s) @ ASCII 10 B | 54 | 0% (−7 … 0) | 0% (−7 … 0) |
| grapheme_strlen($s) @ ASCII 16 B | 69 | 0% (−4 … +6) | 0% (−5 … +5) |
| grapheme_strlen($s) @ ASCII 64 B | 179 | 0% (0 … +2) | 0% (−2 … +1) |
| grapheme_strlen($s) @ ASCII 256 B | 563 | 0% (0 … 0) | 0% (−1 … +1) |
| grapheme_strlen($s) @ ASCII 1 KB | 2,099 | 0% (0 … 0) | 0% (−1 … 0) |
| grapheme_strlen($s) @ ASCII 4 KB | 8,243 | 0% (0 … 0) | 0% (−1 … 0) |
| grapheme_strlen($s) @ ASCII 1 KB, CR LF every 80 B | 63,461 | 0% (−1 … +1) | 0% (−5 … 0) |
| grapheme_strlen($s) @ ASCII 1 KB, lone CR every 80 B | 2,099 | 0% (0 … 0) | 0% (−1 … 0) |
| grapheme_strlen($s) @ ASCII 1 KB, "é" first | 63,108 | 0% (−14 … +38) | 0% (−2 … +5) |
| grapheme_strlen($s) @ ASCII 16 B, "é" last | 2,241 | 0% (−3 … +1) | 0% (−7 … +1) |
| grapheme_strlen($s) @ ASCII 64 B, "é" last | 5,176 | 0% (−14 … +2) | 0% (−20 … +3) |
| grapheme_strlen($s) @ ASCII 256 B, "é" last | 17,228 | 0% (−2 … +14) | 0% (−19 … +6) |
| grapheme_strlen($s) @ ASCII 1 KB, "é" last | 65,130 | 0% (−5 … +3) | 0% (−2 … +5) |
| grapheme_strlen($s) @ ASCII 4 KB, "é" last | 257,917 | 0% (−27 … +4) | 0% (−4 … +2) |
| grapheme_strlen($s) @ Chinese 16 B | 1,561 | 0% (−6 … +2) | 0% (−1 … 0) |
| grapheme_strlen($s) @ Chinese 64 B | 2,631 | 0% (−1 … +1) | 0% (−10 … +4) |
| grapheme_strlen($s) @ Chinese 256 B | 7,339 | 0% (−15 … +1) | 0% (−3 … +6) |
| grapheme_strlen($s) @ Chinese 1 KB | 26,490 | 0% (−5 … +2) | 0% (−17 … +11) |
| grapheme_strlen($s) @ Chinese 4 KB | 99,411 | 0% (−1 … +4) | 0% (−17 … +4) |
| grapheme_strlen($s) @ Spanish 256 B | 16,074 | 0% (−2 … +2) | 0% (−2 … +2) |
| grapheme_strlen($s) @ Russian 256 B | 10,362 | +1% (−21 … +10) | 0% (−1 … +3) |
| grapheme_strlen($s) @ Japanese 256 B | 7,514 | 0% (−2 … +5) | 0% (−2 … +11) |
| grapheme_strlen($s) @ Korean 256 B | 8,323 | 0% (−1 … +3) | 0% (−2 … +1) |
| grapheme_strlen($s) @ emoji and text 256 B | 11,847 | 0% (−1 … +4) | 0% (−1 … +9) |
| grapheme_substr($s, 0, 8) @ ASCII 1 B | 99 | 0% (−1 … +36) | 0% (−11 … +4) |
| grapheme_substr($s, 0, 8) @ ASCII 2 B | 102 | 0% (−5 … +11) | 0% (−5 … +4) |
| grapheme_substr($s, 0, 8) @ ASCII 3 B | 103 | 0% (−11 … +8) | −1% (−7 … +11) |
| grapheme_substr($s, 0, 8) @ ASCII 4 B | 102 | 0% (−11 … +14) | +1% (−4 … +20) |
| grapheme_substr($s, 0, 8) @ ASCII 5 B | 103 | 0% (−15 … +9) | 0% (−8 … +14) |
| grapheme_substr($s, 0, 8) @ ASCII 8 B | 100 | 0% (−12 … +14) | −1% (−6 … +13) |
| grapheme_substr($s, 0, 8) @ ASCII 9 B | 103 | −1% (−13 … +17) | −1% (−10 … +9) |
| grapheme_substr($s, 0, 8) @ ASCII 10 B | 104 | 0% (−7 … +7) | −1% (−12 … +5) |
| grapheme_substr($s, 0, 8) @ ASCII 16 B | 116 | +1% (−7 … +7) | 0% (−3 … +16) |
| grapheme_substr($s, 0, 8) @ ASCII 64 B | 226 | 0% (−2 … +3) | 0% (−4 … +4) |
| grapheme_substr($s, 0, 8) @ ASCII 256 B | 610 | 0% (0 … +2) | 0% (−1 … +1) |
| grapheme_substr($s, 0, 8) @ ASCII 1 KB | 2,146 | 0% (0 … 0) | 0% (0 … 0) |
| grapheme_substr($s, 0, 8) @ ASCII 4 KB | 8,292 | 0% (0 … 0) | 0% (−1 … 0) |
| grapheme_substr($s, 0, 8) @ ASCII 1 KB, CR LF every 80 B | 7,727 | 0% (−2 … +1) | 0% (−1 … +1) |
| grapheme_substr($s, 0, 8) @ ASCII 1 KB, lone CR every 80 B | 2,147 | 0% (0 … 0) | 0% (0 … 0) |
| grapheme_substr($s, 0, 8) @ ASCII 1 KB, "é" first | 7,626 | 0% (−1 … +1) | 0% (−1 … +1) |
| grapheme_substr($s, 0, 8) @ ASCII 16 B, "é" last | 2,070 | 0% (−2 … +1) | 0% (−5 … +14) |
| grapheme_substr($s, 0, 8) @ ASCII 64 B, "é" last | 2,446 | 0% (0 … +5) | 0% (−1 … +1) |
| grapheme_substr($s, 0, 8) @ ASCII 256 B, "é" last | 3,905 | 0% (−3 … +2) | 0% (−3 … +3) |
| grapheme_substr($s, 0, 8) @ ASCII 1 KB, "é" last | 9,690 | 0% (−1 … +1) | 0% (−1 … +1) |
| grapheme_substr($s, 0, 8) @ ASCII 4 KB, "é" last | 32,825 | 0% (−6 … 0) | 0% (−1 … 0) |
| grapheme_substr($s, 0, 8) @ Chinese 16 B | 1,762 | 0% (−1 … +6) | 0% (0 … +5) |
| grapheme_substr($s, 0, 8) @ Chinese 64 B | 2,320 | 0% (−1 … +2) | 0% (−1 … +2) |
| grapheme_substr($s, 0, 8) @ Chinese 256 B | 3,144 | 0% (−1 … 0) | 0% (0 … +6) |
| grapheme_substr($s, 0, 8) @ Chinese 1 KB | 6,345 | 0% (0 … 0) | 0% (−1 … 0) |
| grapheme_substr($s, 0, 8) @ Chinese 4 KB | 19,012 | 0% (−1 … 0) | 0% (−6 … 0) |
| grapheme_substr($s, 0, 8) @ Spanish 256 B | 3,371 | 0% (−2 … +3) | 0% (−2 … +3) |
| grapheme_substr($s, 0, 8) @ Russian 256 B | 3,293 | 0% (−1 … +2) | 0% (−8 … +1) |
| grapheme_substr($s, 0, 8) @ Japanese 256 B | 3,118 | 0% (−3 … +30) | 0% (−1 … +6) |
| grapheme_substr($s, 0, 8) @ Korean 256 B | 3,132 | 0% (−4 … +6) | 0% (−2 … +1) |
| grapheme_substr($s, 0, 8) @ emoji and text 256 B | 3,604 | 0% (−1 … +13) | 0% (−3 … +1) |
| grapheme_strpos($s, 'zz') @ ASCII 1 B | 56 | 0% (−5 … +5) | 0% (−28 … +6) |
| grapheme_strpos($s, 'zz') @ ASCII 2 B | 72 | 0% (−4 … +10) | 0% (−4 … +6) |
| grapheme_strpos($s, 'zz') @ ASCII 3 B | 74 | 0% (−11 … +4) | 0% (−5 … +5) |
| grapheme_strpos($s, 'zz') @ ASCII 4 B | 76 | 0% (−5 … +4) | 0% (−5 … +6) |
| grapheme_strpos($s, 'zz') @ ASCII 5 B | 78 | 0% (−4 … +5) | 0% (−4 … +4) |
| grapheme_strpos($s, 'zz') @ ASCII 8 B | 84 | 0% (−4 … +10) | 0% (−6 … +4) |
| grapheme_strpos($s, 'zz') @ ASCII 9 B | 86 | 0% (−4 … +5) | 0% (−3 … +6) |
| grapheme_strpos($s, 'zz') @ ASCII 10 B | 88 | 0% (0 … +6) | 0% (−4 … +5) |
| grapheme_strpos($s, 'zz') @ ASCII 16 B | 103 | 0% (−3 … +3) | 0% (−6 … +3) |
| grapheme_strpos($s, 'zz') @ ASCII 64 B | 226 | 0% (−1 … +2) | 0% (−2 … +1) |
| grapheme_strpos($s, 'zz') @ ASCII 256 B | 637 | 0% (−1 … 0) | 0% (−1 … +1) |
| grapheme_strpos($s, 'zz') @ ASCII 1 KB | 2,344 | 0% (0 … 0) | 0% (−1 … 0) |
| grapheme_strpos($s, 'zz') @ ASCII 4 KB | 9,310 | 0% (0 … 0) | 0% (−1 … 0) |
| grapheme_strpos($s, 'zz') @ ASCII 1 KB, CR LF every 80 B | 112,695 | 0% (0 … 0) | 0% (−1 … +5) |
| grapheme_strpos($s, 'zz') @ ASCII 1 KB, lone CR every 80 B | 2,344 | 0% (0 … 0) | 0% (−1 … 0) |
| grapheme_strpos($s, 'zz') @ ASCII 1 KB, "é" first | 112,610 | 0% (0 … 0) | 0% (−1 … 0) |
| grapheme_strpos($s, 'zz') @ ASCII 16 B, "é" last | 6,190 | 0% (−2 … +2) | 0% (−2 … +20) |
| grapheme_strpos($s, 'zz') @ ASCII 64 B, "é" last | 11,409 | 0% (−2 … +1) | 0% (−1 … +1) |
| grapheme_strpos($s, 'zz') @ ASCII 256 B, "é" last | 32,006 | 0% (−1 … +1) | 0% (−1 … +1) |
| grapheme_strpos($s, 'zz') @ ASCII 1 KB, "é" last | 114,660 | 0% (0 … 0) | 0% (−1 … 0) |
| grapheme_strpos($s, 'zz') @ ASCII 4 KB, "é" last | 444,488 | 0% (0 … 0) | 0% (−1 … 0) |
| grapheme_strpos($s, 'zz') @ Chinese 16 B | 5,558 | 0% (−2 … +2) | 0% (−3 … +2) |
| grapheme_strpos($s, 'zz') @ Chinese 64 B | 8,676 | 0% (−2 … +1) | 0% (−2 … +2) |
| grapheme_strpos($s, 'zz') @ Chinese 256 B | 21,617 | 0% (−1 … +1) | 0% (−1 … +1) |
| grapheme_strpos($s, 'zz') @ Chinese 1 KB | 72,933 | 0% (−1 … +1) | 0% (−1 … +1) |
| grapheme_strpos($s, 'zz') @ Chinese 4 KB | 279,998 | 0% (−1 … +1) | 0% (−1 … +1) |
| grapheme_strpos($s, 'zz') @ Spanish 256 B | 31,868 | 0% (−1 … +1) | 0% (−1 … +1) |
| grapheme_strpos($s, 'zz') @ Russian 256 B | 20,931 | 0% (−16 … +2) | 0% (−1 … +1) |
| grapheme_strpos($s, 'zz') @ Japanese 256 B | 14,985 | 0% (−1 … +1) | 0% (−1 … +1) |
| grapheme_strpos($s, 'zz') @ Korean 256 B | 28,011 | 0% (−2 … +1) | 0% (−10 … +1) |
| grapheme_strpos($s, 'zz') @ emoji and text 256 B | 24,952 | 0% (−1 … +1) | 0% (−1 … +1) |
| grapheme_extract($s, 8) @ ASCII 1 B | 103 | 0% (−1 … 0) | 0% (−3 … +1) |
| grapheme_extract($s, 8) @ ASCII 2 B | 106 | −1% (−4 … +2) | 0% (−11 … +3) |
| grapheme_extract($s, 8) @ ASCII 3 B | 108 | 0% (−2 … +1) | 0% (−2 … +3) |
| grapheme_extract($s, 8) @ ASCII 4 B | 109 | 0% (−1 … +1) | 0% (−2 … +3) |
| grapheme_extract($s, 8) @ ASCII 5 B | 109 | 0% (−1 … +2) | 0% (−3 … +5) |
| grapheme_extract($s, 8) @ ASCII 8 B | 114 | 0% (−1 … +1) | 0% (−2 … +2) |
| grapheme_extract($s, 8) @ ASCII 9 B | 114 | 0% (−1 … +1) | 0% (−1 … 0) |
| grapheme_extract($s, 8) @ ASCII 10 B | 114 | 0% (−1 … +3) | 0% (−2 … +1) |
| grapheme_extract($s, 8) @ ASCII 16 B | 114 | 0% (−26 … +5) | 0% (0 … +1) |
| grapheme_extract($s, 8) @ ASCII 64 B | 114 | 0% (0 … +1) | 0% (−1 … +1) |
| grapheme_extract($s, 8) @ ASCII 256 B | 114 | 0% (−1 … +1) | 0% (−1 … 0) |
| grapheme_extract($s, 8) @ ASCII 1 KB | 114 | 0% (−4 … +2) | 0% (−1 … +1) |
| grapheme_extract($s, 8) @ ASCII 4 KB | 114 | 0% (−3 … +2) | 0% (−1 … +4) |
| grapheme_extract($s, 8) @ ASCII 1 KB, CR LF every 80 B | 114 | 0% (−1 … +2) | 0% (−2 … +3) |
| grapheme_extract($s, 8) @ ASCII 1 KB, lone CR every 80 B | 114 | 0% (−2 … +2) | 0% (−2 … +1) |
| grapheme_extract($s, 8) @ ASCII 1 KB, "é" first | 2,357 | +1% (0 … +4) | 0% (−3 … +3) |
| grapheme_extract($s, 8) @ ASCII 16 B, "é" last | 114 | +1% (−2 … +44) | 0% (−3 … +1) |
| grapheme_extract($s, 8) @ ASCII 64 B, "é" last | 114 | 0% (−2 … +13) | 0% (−1 … +1) |
| grapheme_extract($s, 8) @ ASCII 256 B, "é" last | 114 | 0% (−2 … +2) | 0% (−8 … +1) |
| grapheme_extract($s, 8) @ ASCII 1 KB, "é" last | 114 | 0% (0 … +7) | 0% (−5 … +1) |
| grapheme_extract($s, 8) @ ASCII 4 KB, "é" last | 114 | 0% (−1 … +1) | 0% (−2 … +1) |
| grapheme_extract($s, 8) @ Chinese 16 B | 1,785 | 0% (−3 … +5) | 0% (−1 … +1) |
| grapheme_extract($s, 8) @ Chinese 64 B | 2,731 | 0% (−2 … +1) | 0% (−1 … +1) |
| grapheme_extract($s, 8) @ Chinese 256 B | 3,029 | 0% (−1 … +4) | 0% (−10 … +1) |
| grapheme_extract($s, 8) @ Chinese 1 KB | 3,041 | 0% (−3 … +1) | 0% (−3 … +1) |
| grapheme_extract($s, 8) @ Chinese 4 KB | 3,029 | 0% (−2 … +1) | 0% (0 … +2) |
| grapheme_extract($s, 8) @ Spanish 256 B | 2,215 | 0% (−1 … +3) | 0% (−3 … +2) |
| grapheme_extract($s, 8) @ Russian 256 B | 2,861 | 0% (−1 … +2) | 0% (−4 … +1) |
| grapheme_extract($s, 8) @ Japanese 256 B | 2,946 | 0% (−2 … +1) | 0% (−1 … +2) |
| grapheme_extract($s, 8) @ Korean 256 B | 2,812 | 0% (−3 … +1) | 0% (−2 … 0) |
| grapheme_extract($s, 8) @ emoji and text 256 B | 2,371 | 0% (−1 … +1) | 0% (−4 … +3) |
| grapheme_strpos($s, 'x') @ ASCII 1 B | 66 | 0% (−5 … +6) | 0% (−9 … +5) |
| grapheme_strpos($s, 'x') @ ASCII 5 B | 74 | 0% (−4 … +4) | 0% (−5 … +5) |
| grapheme_strpos($s, 'x') @ ASCII 9 B | 82 | 0% (−5 … 0) | 0% (−1 … +5) |
| grapheme_strpos($s, 'x') @ ASCII 16 B | 99 | 0% (−4 … +7) | 0% (0 … +3) |
| grapheme_strpos($s, 'x') @ ASCII 64 B | 198 | 0% (−1 … 0) | 0% (−1 … +2) |
| grapheme_strpos($s, 'x') @ ASCII 256 B | 582 | 0% (−1 … +1) | 0% (−1 … +1) |
| grapheme_strpos($s, 'x') @ ASCII 1 KB | 2,118 | 0% (0 … 0) | 0% (−1 … 0) |
| grapheme_strpos($s, 'x') @ ASCII 4 KB | 8,264 | 0% (0 … 0) | 0% (−1 … 0) |
| grapheme_strstr($s, 'o') @ ASCII 1 B | 69 | 0% (−5 … +5) | 0% (0 … +9) |
| grapheme_strstr($s, 'o') @ ASCII 5 B | 77 | 0% (−4 … +4) | 0% (−7 … +4) |
| grapheme_strstr($s, 'o') @ ASCII 9 B | 85 | 0% (−11 … +5) | 0% (−4 … +4) |
| grapheme_strstr($s, 'o') @ ASCII 16 B | 128 | 0% (−3 … +2) | 0% (−3 … +2) |
| grapheme_strstr($s, 'o') @ ASCII 64 B | 236 | 0% (−4 … +3) | 0% (−3 … +2) |
| grapheme_strstr($s, 'o') @ ASCII 256 B | 622 | 0% (−1 … +1) | 0% (−1 … +1) |
| grapheme_strstr($s, 'o') @ ASCII 1 KB | 2,184 | 0% (0 … 0) | 0% (−1 … 0) |
| grapheme_strstr($s, 'o') @ ASCII 4 KB | 8,479 | 0% (0 … 0) | 0% (−1 … 0) |
| grapheme_stripos($s, 'Z') @ ASCII 1 B | 140 | 0% (−3 … +3) | 0% (−4 … +2) |
| grapheme_stripos($s, 'Z') @ ASCII 5 B | 151 | 0% (−2 … +4) | 0% (−2 … +3) |
| grapheme_stripos($s, 'Z') @ ASCII 9 B | 162 | 0% (−2 … +4) | 0% (−2 … 0) |
| grapheme_stripos($s, 'Z') @ ASCII 16 B | 174 | −1% (−2 … +2) | 0% (−4 … +2) |
| grapheme_stripos($s, 'Z') @ ASCII 64 B | 280 | 0% (−2 … +1) | 0% (−1 … +2) |
| grapheme_stripos($s, 'Z') @ ASCII 256 B | 688 | 0% (0 … +1) | 0% (−1 … +1) |
| grapheme_stripos($s, 'Z') @ ASCII 1 KB | 2,338 | 0% (0 … +1) | 0% (−1 … 0) |
| grapheme_stripos($s, 'Z') @ ASCII 4 KB | 9,013 | 0% (−1 … 0) | 0% (−1 … 0) |
| grapheme_strrpos($s, 'e') @ ASCII 1 B | 64 | 0% (−4 … +2) | 0% (−10 … +6) |
| grapheme_strrpos($s, 'e') @ ASCII 5 B | 62 | 0% (−40 … +12) | 0% (−11 … +5) |
| grapheme_strrpos($s, 'e') @ ASCII 9 B | 74 | 0% (−6 … +5) | −1% (−6 … +7) |
| grapheme_strrpos($s, 'e') @ ASCII 16 B | 98 | 0% (−4 … +4) | 0% (−7 … +4) |
| grapheme_strrpos($s, 'e') @ ASCII 64 B | 197 | 0% (−2 … +4) | 0% (−4 … +2) |
| grapheme_strrpos($s, 'e') @ ASCII 256 B | 592 | 0% (−1 … +1) | 0% (−1 … +1) |
| grapheme_strrpos($s, 'e') @ ASCII 1 KB | 2,117 | 0% (0 … 0) | 0% (−1 … 0) |
| grapheme_strrpos($s, 'e') @ ASCII 4 KB | 8,274 | 0% (0 … 0) | 0% (−1 … 0) |
| grapheme_strlen(next string) @ ASCII, mixed lengths 1-24 B | 99 | 0% (−9 … +10) | 0% (−1 … +10) |
| grapheme_substr(next string, 0, 8) @ ASCII, mixed lengths 1-24 B | 159 | 0% (−7 … +6) | 0% (−17 … +10) |
| grapheme_strpos(next string, 'zz') @ ASCII, mixed lengths 1-24 B | 145 | +1% (−4 … +8) | 0% (−7 … +8) |

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
