| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | instructions |
|---|--:|--:|--:|--:|--:|--:|
| `mb_substr($s, 0, 10)`, English (1.00 B/char), 31-byte title | 200 | −33% (−35 … −32) | −21% (−25 … −19) | −46% (−49 … −46) | −47% (−51 … −44) | −43% … −38% |
| `mb_substr($s, $half, 20)`, English (1.00 B/char), 64 KB | 63,324 | −92% (−92 … −92) | −90% (−90 … −89) | −95% (−96 … −88) | −95% (−95 … −93) | −95% … −92% |
| `mb_substr($s, $half, 20)`, Hindi (2.54 B/char), 1 KB | 2,191 | −18% (−18 … −13) | −10% (−11 … −8) | −43% (−43 … −43) | −43% (−43 … −41) | −66% … −54% |
| `mb_substr($s, -20)`, English (1.00 B/char), 1 KB | 2,310 | −66% (−67 … −65) | −62% (−62 … −60) | −70% (−71 … −70) | −67% (−68 … −67) | −73% … −67% |
| `mb_substr($s, 0, 10)`, English (1.00 B/char), 31-byte title, without the flag | 199 | +4% (+3 … +5) | +3% (+3 … +4) | 0% (0 … +3) | +1% (+1 … +3) | +1% … +2% |
| `mb_substr($s, $half, 20)`, Chinese (2.89 B/char), 1 KB, without the flag | 2,841 | 0% (−1 … +2) | +1% (0 … +3) | 0% (0 … 0) | 0% (−1 … +3) | 0% |

Control: master against itself.

| call | master, CPU cycles per call (GCC 13.3) | A/A start | A/A end |
|---|--:|--:|--:|
| `mb_substr($s, 0, 10)`, English (1.00 B/char), 31-byte title | 200 | 0% (−1 … +1) | +1% (−1 … +1) |
| `mb_substr($s, $half, 20)`, English (1.00 B/char), 64 KB | 64,474 | −2% (−5 … +3) | +1% (0 … +2) |
| `mb_substr($s, $half, 20)`, Hindi (2.54 B/char), 1 KB | 2,150 | −1% (−2 … +5) | 0% (−1 … +5) |
| `mb_substr($s, -20)`, English (1.00 B/char), 1 KB | 2,319 | 0% (0 … +14) | 0% (0 … +3) |
| `mb_substr($s, 0, 10)`, English (1.00 B/char), 31-byte title, without the flag | 200 | 0% (0 … +1) | +2% (−1 … +5) |
| `mb_substr($s, $half, 20)`, Chinese (2.89 B/char), 1 KB, without the flag | 2,837 | 0% (0 … +1) | −1% (−2 … 0) |
