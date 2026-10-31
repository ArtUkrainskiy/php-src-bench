# Old and current AMD series

The 13 October and 31 October raw runs are both recalculated with paired ratios. Each column compares the PR with its own master. The old run also had other host load. Other commits separate the two masters, so this does not isolate the effect of #24145 alone. Negative = fewer cycles (faster).

| call | master, CPU cycles per call (GCC 15 before) | GCC 15 before | GCC 15 now | clang 21 before | clang 21 now |
|---|--:|--:|--:|--:|--:|
| Cyrillic, 4 KiB | 45,290 | −28% | −22% | −21% | −21% |
| CJK, 4 KiB | 33,628 | −31% | −14% | −16% | −18% |
| Emoji, 4 KiB | 32,423 | −13% | −8% | −16% | −12% |
| Cyrillic, unescaped Unicode, 4 KiB | 63,250 | −20% | −15% | −28% | −30% |
| CJK, unescaped Unicode, 4 KiB | 44,772 | −19% | −10% | −28% | −22% |
| Emoji, unescaped Unicode, 4 KiB | 32,853 | −25% | −19% | −27% | −20% |
| ASCII, 4 KiB | 9,439 | +1% | +5% | −1% | 0% |
| ASCII, 64 KiB | 153,330 | −3% | +5% | +2% | 0% |
| HTML, 4 KiB | 18,870 | +4% | +4% | −1% | 0% |
| Quotes only, 4 KiB | 35,104 | −7% | +12% | 0% | −2% |
| A newline every 40 bytes, 4 KiB | 11,075 | −2% | +7% | +2% | 0% |
| 1,000 arrays of 10 fields | 1,115,359 | −2% | −2% | −1% | −1% |
