| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | GCC 15.2 (AMD) | clang 21.1 (AMD) |
|---|--:|--:|--:|--:|--:|--:|--:|
| Cyrillic, 4 KiB | 35,063 | −19% | −28% | +12% | −22% | −22% | −14% |
| Cyrillic, unescaped Unicode, 4 KiB | 56,511 | −15% | −29% | −21% | −25% | −17% | −22% |
| CJK, 4 KiB | 22,791 | −7% | −11% | −20% | −19% | −24% | −21% |
| CJK, unescaped Unicode, 4 KiB | 25,056 | −11% | −11% | −13% | −15% | −18% | −20% |
| Emoji, 4 KiB | 25,041 | −10% | −9% | −14% | −9% | −7% | −11% |
| Emoji, unescaped Unicode, 4 KiB | 18,933 | −17% | −16% | −14% | −14% | −22% | −18% |
| French, 4 KiB | 24,467 | −4% | −3% | −1% | −17% | −15% | −8% |
| ASCII with random-position e acute, 4 KiB | 23,056 | −5% | −7% | −3% | −10% | −5% | −4% |
| ASCII with periodic e acute, unescaped Unicode, 4 KiB | 21,786 | −17% | +24% | −6% | −4% | −6% | −3% |
| ASCII, 16 bytes | 135 | +7% | −4% | 0% | +1% | +1% | +1% |
| ASCII, 4 KiB | 8,114 | +6% | 0% | 0% | 0% | +6% | +1% |
| ASCII, 64 KiB | 134,588 | +3% | 0% | 0% | 0% | +5% | 0% |
| HTML, 4 KiB | 28,450 | +5% | −1% | −1% | 0% | +4% | 0% |
| URLs, 4 KiB | 30,128 | +8% | +1% | −1% | 0% | −1% | −1% |
| Quotes only, 4 KiB | 25,683 | 0% | 0% | −1% | +1% | +12% | 0% |
| A newline every 40 bytes, 4 KiB | 22,313 | −33% | −21% | 0% | 0% | +7% | 0% |
| 1,000 arrays of 10 fields | 888,668 | +16% | −6% | +3% | −4% | −1% | 0% |
| 1,000 objects of 10 properties | 832,933 | +13% | +2% | +1% | +4% | 0% | 0% |
