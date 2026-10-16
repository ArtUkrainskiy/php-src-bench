| call | master, CPU cycles per call (start) | start | end |
|---|--:|--:|--:|
| `mb_substr($s, 0, 10)`, English (1.00 B/char), 31-byte title | 200 | 0% (−1 … +1) | +1% (−1 … +1) |
| `mb_substr($s, $half, 20)`, English (1.00 B/char), 1 KB | 1,380 | +1% (−2 … +5) | 0% (0 … +3) |
| `mb_substr($s, $half, 20)`, English (1.00 B/char), 64 KB | 64,474 | −2% (−5 … +3) | +1% (0 … +2) |
| `mb_substr($s, 0, 10)`, Spanish (1.00 B/char), 37-byte title | 213 | 0% (−1 … +7) | 0% (0 … +1) |
| `mb_substr($s, $half, 20)`, Spanish (1.04 B/char), 1 KB | 1,651 | 0% (−3 … +1) | 0% (0 … 0) |
| `mb_substr($s, $half, 20)`, Spanish (1.03 B/char), 64 KB | 88,465 | 0% (−1 … +7) | 0% (0 … +3) |
| `mb_substr($s, 0, 10)`, Russian (1.81 B/char), 49-byte title | 279 | −1% (−2 … +4) | 0% (0 … +3) |
| `mb_substr($s, $half, 20)`, Russian (1.78 B/char), 1 KB | 1,740 | −1% (−3 … +1) | 0% (−1 … +2) |
| `mb_substr($s, $half, 20)`, Russian (1.77 B/char), 64 KB | 163,240 | 0% (0 … +1) | 0% (−2 … +2) |
| `mb_substr($s, 0, 10)`, Arabic (1.75 B/char), 56-byte title | 298 | 0% (−2 … +1) | −1% (−2 … +1) |
| `mb_substr($s, $half, 20)`, Arabic (1.74 B/char), 1 KB | 1,723 | +2% (0 … +7) | +3% (−2 … +7) |
| `mb_substr($s, $half, 20)`, Arabic (1.76 B/char), 64 KB | 160,934 | −1% (−2 … −1) | −1% (−1 … 0) |
| `mb_substr($s, 0, 10)`, Hindi (2.61 B/char), 94-byte title | 472 | 0% (−1 … 0) | +2% (0 … +4) |
| `mb_substr($s, $half, 20)`, Hindi (2.54 B/char), 1 KB | 2,150 | −1% (−2 … +5) | 0% (−1 … +5) |
| `mb_substr($s, $half, 20)`, Hindi (2.54 B/char), 64 KB | 178,735 | 0% (0 … +2) | 0% (−1 … +1) |
| `mb_substr($s, 0, 10)`, Chinese (3.00 B/char), 54-byte title | 386 | −1% (−2 … 0) | 0% (−2 … +8) |
| `mb_substr($s, $half, 20)`, Chinese (2.89 B/char), 1 KB | 2,823 | +1% (+1 … +1) | 0% (0 … 0) |
| `mb_substr($s, $half, 20)`, Chinese (2.89 B/char), 64 KB | 119,270 | 0% (−1 … +1) | 0% (−2 … +2) |
| `mb_substr($s, 0, 10)`, Japanese (3.00 B/char), 63-byte title | 407 | 0% (−1 … +3) | 0% (0 … +1) |
| `mb_substr($s, $half, 20)`, Japanese (2.91 B/char), 1 KB | 2,735 | 0% (−1 … +1) | 0% (−1 … +1) |
| `mb_substr($s, $half, 20)`, Japanese (2.88 B/char), 64 KB | 122,546 | 0% (0 … +4) | 0% (0 … +6) |
| `mb_substr($s, 0, 10)`, Korean (2.33 B/char), 49-byte title | 358 | 0% (−1 … +1) | −1% (−2 … −1) |
| `mb_substr($s, $half, 20)`, Korean (2.24 B/char), 1 KB | 3,036 | 0% (−2 … +4) | +1% (0 … +2) |
| `mb_substr($s, $half, 20)`, Korean (2.25 B/char), 64 KB | 144,443 | −1% (−1 … +1) | 0% (0 … +4) |
| `mb_substr($s, 0, 10)`, English with emoji (1.30 B/char), 26-byte title | 174 | +1% (0 … +3) | +1% (−1 … +6) |
| `mb_substr($s, $half, 20)`, English with emoji (1.39 B/char), 1 KB | 1,987 | 0% (−3 … +28) | 0% (−1 … +1) |
| `mb_substr($s, $half, 20)`, English with emoji (1.43 B/char), 64 KB | 148,477 | 0% (−1 … +5) | 0% (0 … +3) |
| `mb_substr($s, -20)`, English (1.00 B/char), 1 KB | 2,319 | 0% (0 … +14) | 0% (0 … +3) |
| `mb_substr($s, 0, $half)`, English (1.00 B/char), 1 KB | 2,107 | +1% (0 … +4) | +1% (−1 … +6) |
| `mb_strpos($s, $needle, $half)`, English (1.00 B/char), 1 KB | 6,304 | 0% (−1 … +2) | 0% (0 … +1) |
| `mb_substr($s, -20)`, English (1.00 B/char), 64 KB | 134,860 | 0% (−1 … 0) | 0% (−1 … 0) |
| `mb_strpos($s, $needle, $half)`, English (1.00 B/char), 64 KB | 385,316 | 0% (−1 … 0) | 0% (−1 … +1) |
| `mb_substr($s, 0, 10)`, English (1.00 B/char), 31-byte title, without the flag | 200 | 0% (0 … +1) | +2% (−1 … +5) |
| `mb_substr($s, $half, 20)`, English (1.00 B/char), 1 KB, without the flag | 1,355 | 0% (0 … +4) | 0% (−2 … +3) |
| `mb_substr($s, $half, 20)`, Chinese (2.89 B/char), 1 KB, without the flag | 2,837 | 0% (0 … +1) | −1% (−2 … 0) |
