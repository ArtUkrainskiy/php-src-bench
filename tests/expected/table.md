| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 |
|---|--:|--:|--:|--:|--:|
| `mb_substr($s, 0, 10)`, English (1.00 B/char), 31-byte title | 200 | −35% | −23% | −46% | −47% |
| `mb_substr($s, $half, 20)`, English (1.00 B/char), 64 KB | 63,324 | −92% | −90% | −95% | −95% |
| `mb_substr($s, $half, 20)`, Hindi (2.54 B/char), 1 KB | 2,191 | −16% | −10% | −43% | −43% |
| `mb_substr($s, -20)`, English (1.00 B/char), 1 KB | 2,310 | −66% | −62% | −70% | −67% |
| `mb_substr($s, 0, 10)`, English (1.00 B/char), 31-byte title, without the flag | 199 | +3% | +3% | 0% | +1% |
| `mb_substr($s, $half, 20)`, Chinese (2.89 B/char), 1 KB, without the flag | 2,841 | 0% | +2% | 0% | −1% |

Control: master against itself.

| call | master, CPU cycles per call (GCC 13.3) | A/A start | A/A end |
|---|--:|--:|--:|
| `mb_substr($s, 0, 10)`, English (1.00 B/char), 31-byte title | 200 | 0% | +1% |
| `mb_substr($s, $half, 20)`, English (1.00 B/char), 64 KB | 64,474 | −2% | +1% |
| `mb_substr($s, $half, 20)`, Hindi (2.54 B/char), 1 KB | 2,150 | +1% | +1% |
| `mb_substr($s, -20)`, English (1.00 B/char), 1 KB | 2,319 | 0% | +1% |
| `mb_substr($s, 0, 10)`, English (1.00 B/char), 31-byte title, without the flag | 200 | 0% | +1% |
| `mb_substr($s, $half, 20)`, Chinese (2.89 B/char), 1 KB, without the flag | 2,837 | 0% | −1% |
