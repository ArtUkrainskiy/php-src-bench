# Build time and memory

- **Build time**: 21–58 µs per KiB of keys for `Str\Matcher` with GCC on the real and random-letter dictionaries below. The slow dictionaries at the end take up to 183 µs per KiB.
- **`Str\Replacer`** builds as fast as `Str\Matcher` on random keys and word lists (within 11% on either compiler). On 512 or more PHP names it takes 1.4–2.2 times as long with GCC: it also builds an automaton of the reversed keys to pick the longest match.
- **The last three rows** are dictionaries built to be slow.

## Build time, µs

| Dictionary | Keys, KiB | Matcher, GCC | Matcher, Clang | Replacer, GCC | Replacer, Clang |
|---|---:|---:|---:|---:|---:|
| random letters a–p, 8 keys | 0.1 | 2.2 | 2.16 | 2.11 | 2.08 |
| random letters a–p, 16 keys | 0.2 | 3.99 | 3.96 | 3.76 | 3.79 |
| random letters a–p, 32 keys | 0.4 | 7.62 | 7.48 | 7.48 | 7.53 |
| random letters a–p, 128 keys | 1.3 | 30.3 | 29.8 | 28.7 | 28.6 |
| random letters a–p, 1024 keys | 10 | 385 | 379 | 381 | 375 |
| PHP names, 8 keys | 0.2 | 3.46 | 3.48 | 3.94 | 4.01 |
| PHP names, 32 keys | 0.6 | 13.7 | 14 | 14.8 | 15.2 |
| PHP names, 128 keys | 2.6 | 59.4 | 58.9 | 70.2 | 65.6 |
| PHP names, 512 keys | 10 | 312 | 298 | 451 | 435 |
| PHP names, 2048 keys | 41 | 1,298 | 1,274 | 2,503 | 2,456 |
| PHP names, 8019 keys | 160 | 7,533 | 7,505 | 16,612 | 16,107 |
| LDNOOBW, 403 keys | 3.3 | 117 | 110 | 124 | 119 |
| crawler patterns, 1469 keys | 17 | 1,007 | 1,002 | 1,103 | 1,086 |
| PHP functions, 3345 keys | 56 | 1,640 | 1,613 | 3,121 | 3,081 |
| words (en), 128 keys | 0.9 | 30.1 | 32 | 28.5 | 29.7 |
| words (es), 128 keys | 1.0 | 34.2 | 35.6 | 36.6 | 37.7 |
| words (ru), 128 keys | 2.0 | 61.6 | 59.8 | 62.1 | 60.2 |
| words (zh), 128 keys | 0.9 | 45.5 | 44.4 | 45.2 | 45.9 |
| words (ja), 128 keys | 0.9 | 43.9 | 42.7 | 47.6 | 47.5 |
| words (ko), 128 keys | 1.2 | 33.5 | 34.9 | 31.6 | 32.6 |
| nested a, aa, …, 512 keys | 128 | 483 | 418 | 479 | 415 |
| 64-byte common prefix, 10000 keys | 674 | 2,961 | 2,522 | 46,203 | 47,270 |
| random bytes, 10000 keys | 117 | 21,473 | 22,004 | 20,180 | 20,875 |

Median time of `new Str\Matcher($keys)` or `new Str\Replacer($map)`, repeated for at least 200 ms on the same dictionary, so caches are warm. The value is the median of three processes. Destroying the object is outside the timer.
"Keys, KiB" is the total length of the keys.
Each dictionary is measured in a fresh process with only that dictionary loaded. `Str\Replacer` maps every key to its uppercase.

## Memory, KiB

| Dictionary | Keys, KiB | Matcher kept, KiB | Matcher peak, KiB | Replacer kept, KiB | Replacer peak, KiB |
|---|---:|---:|---:|---:|---:|
| random letters a–p, 8 keys | 0.1 | 4.8 | 7.8 | 4.1 | 7.8 |
| random letters a–p, 16 keys | 0.2 | 8.1 | 17 | 6.5 | 17 |
| random letters a–p, 32 keys | 0.4 | 21 | 34 | 15 | 34 |
| random letters a–p, 128 keys | 1.3 | 50 | 90 | 43 | 92 |
| random letters a–p, 1024 keys | 10 | 277 | 587 | 221 | 595 |
| PHP names, 8 keys | 0.2 | 8.6 | 13 | 7.4 | 13 |
| PHP names, 32 keys | 0.6 | 33 | 52 | 28 | 49 |
| PHP names, 128 keys | 2.6 | 91 | 155 | 87 | 168 |
| PHP names, 512 keys | 10 | 269 | 461 | 284 | 589 |
| PHP names, 2048 keys | 41 | 749 | 1,361 | 1,061 | 2,075 |
| PHP names, 8019 keys | 160 | 2,241 | 4,741 | 4,113 | 7,533 |
| LDNOOBW, 403 keys | 3.3 | 134 | 208 | 118 | 204 |
| crawler patterns, 1469 keys | 17 | 881 | 1,269 | 673 | 1,110 |
| PHP functions, 3345 keys | 56 | 809 | 1,537 | 1,149 | 2,381 |
| words (en), 128 keys | 0.9 | 70 | 94 | 58 | 89 |
| words (es), 128 keys | 1.0 | 78 | 103 | 67 | 100 |
| words (ru), 128 keys | 2.0 | 74 | 119 | 72 | 128 |
| words (zh), 128 keys | 0.9 | 78 | 96 | 82 | 105 |
| words (ja), 128 keys | 0.9 | 70 | 89 | 82 | 113 |
| words (ko), 128 keys | 1.2 | 70 | 98 | 59 | 92 |
| nested a, aa, …, 512 keys | 128 | 17 | 149 | 15 | 153 |
| 64-byte common prefix, 10000 keys | 674 | 389 | 762 | 10,889 | 37,121 |
| random bytes, 10000 keys | 117 | 22,013 | 25,345 | 21,265 | 25,453 |

- **Kept**: `memory_get_usage()` after the build minus before it, with GCC. Key and replacement strings are shared with the input array and are not counted.
- **Peak**: `memory_get_peak_usage()` during the build minus the usage before it.

Memory is counted by the Zend allocator, not as process RSS.

## The slow dictionaries

- **nested a, aa, …**: keys `a`, `aa`, … up to 512 `a`. Every key is a prefix of the next one.
- **64-byte common prefix**: 10,000 keys that share their first 64 bytes. Reversed, these keys share almost nothing, so the reversed automaton of `Str\Replacer` is large.
- **random bytes**: 10,000 keys of 12 random bytes. They share almost no prefixes, so the automaton has a state for almost every key byte, and its first levels are full 256-entry rows.
