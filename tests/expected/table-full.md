| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | instructions |
|---|--:|--:|--:|--:|--:|--:|
| `mb_substr($s, 0, 10)`, English (1.00 B/char), 31-byte title | 200 | −35% (−37 … −33) | −23% (−24 … −21) | −46% (−49 … −45) | −47% (−51 … −44) | −43% … −38% |
| `mb_substr($s, $half, 20)`, English (1.00 B/char), 64 KB | 63,324 | −92% (−92 … −92) | −90% (−90 … −89) | −95% (−96 … −88) | −95% (−95 … −93) | −95% … −92% |
| `mb_substr($s, $half, 20)`, Hindi (2.54 B/char), 1 KB | 2,191 | −16% (−24 … −13) | −10% (−12 … −8) | −43% (−43 … −42) | −43% (−44 … −40) | −66% … −54% |
| `mb_substr($s, -20)`, English (1.00 B/char), 1 KB | 2,310 | −66% (−67 … −65) | −62% (−62 … −60) | −70% (−71 … −70) | −67% (−69 … −67) | −73% … −67% |
| `mb_substr($s, 0, 10)`, English (1.00 B/char), 31-byte title, without the flag | 199 | +3% (+1 … +6) | +3% (+2 … +5) | 0% (0 … +3) | +1% (−1 … +4) | +1% … +2% |
| `mb_substr($s, $half, 20)`, Chinese (2.89 B/char), 1 KB, without the flag | 2,841 | 0% (−2 … +2) | +2% (0 … +3) | 0% (−3 … 0) | −1% (−2 … +2) | 0% |

Control: master against itself.

| call | master, CPU cycles per call (GCC 13.3) | A/A start | A/A end |
|---|--:|--:|--:|
| `mb_substr($s, 0, 10)`, English (1.00 B/char), 31-byte title | 200 | 0% (−2 … +4) | +1% (−1 … +2) |
| `mb_substr($s, $half, 20)`, English (1.00 B/char), 64 KB | 64,474 | −2% (−3 … +1) | +1% (−4 … +2) |
| `mb_substr($s, $half, 20)`, Hindi (2.54 B/char), 1 KB | 2,150 | +1% (−3 … +4) | +1% (−3 … +7) |
| `mb_substr($s, -20)`, English (1.00 B/char), 1 KB | 2,319 | 0% (−2 … +14) | +1% (−3 … +4) |
| `mb_substr($s, 0, 10)`, English (1.00 B/char), 31-byte title, without the flag | 200 | 0% (0 … +2) | +1% (0 … +5) |
| `mb_substr($s, $half, 20)`, Chinese (2.89 B/char), 1 KB, without the flag | 2,837 | 0% (−2 … +1) | −1% (−1 … 0) |
