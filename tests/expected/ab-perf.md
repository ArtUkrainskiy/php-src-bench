A: base — PHP 8.6.0-dev, 100e8f353ea ext/uri: Preserve empty query and fragment in URL builders  
B: dev — PHP 8.6.0-dev, 0e4d8e73a21 ext/standard: Add a fast path for ASCII in htmlspecialchars()  
CPU 2 (13th Gen Intel(R) Core(TM) i7-13700H), governor powersave, turbo on, kernel 7.0.0-34-generic  
4 rounds × 7 samples × 10 ms, cc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0, configure --disable-all --disable-cgi --disable-phpdbg --enable-cli, CFLAGS -O2 -g -falign-functions=64 -falign-loops=32, 2026-10-05T19:28+00:00  

| case | bytes | A ns/op | ± | B ns/op | ± | B vs A | A instr/op | B instr/op | instr B vs A |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| htmlspecialchars @ empty | 0 | 6.1 | 4.9% | 6.2 | 4.4% | +2% ~ | 120 | 120 | 0% |
| htmlspecialchars @ word-8 | 8 | 52.8 | 1.0% | 32.6 | 1.4% | −38% ✅ | 937 | 564 | −40% |
| htmlspecialchars @ en-1k | 1042 | 4308 | 0.9% | 1757 | 0.4% | −59% ✅ | 63144 | 10027 | −84% |
| htmlspecialchars @ html-page-4k | 4096 | 15294 | 1.0% | 8215 | 0.7% | −46% ✅ | 254925 | 69112 | −73% |
| htmlspecialchars @ amp-1k | 1024 | 2394 | 0.4% | 1721 | 0.5% | −28% ✅ | 49230 | 35073 | −29% |
| htmlspecialchars cp1251 @ cp1251-1k | 1056 | 3401 | 1.9% | 3455 | 1.3% | +2% ~ | 62074 | 46133 | −26% |
| htmlentities @ ru-1k | 1030 | 4582 | 1.2% | 3536 | 0.7% | −23% ✅ | 65113 | 55339 | −15% |
| synthetic @ B slower | 1042 | 1757 | 0.4% | 4308 | 0.9% | +145% ❌ | 10027 | 63144 | +530% |
| synthetic @ same instructions | 8 | 52.8 | 1.0% | 32.6 | 1.4% | −38% ✅ layout? | 937 | 937 | 0% |
| synthetic @ nothing to measure | 8 | 0.0 | 1.2% | 0.1 | 0.7% | ≈0 ~ | 0 | 0 | n/a |
| synthetic @ one disturbed round | 8 | 52.8 | 1.0% | 32.8 | 3.3% | −38% ~ | 937 | 564 | −40% |
| synthetic @ random result | 8 | 52.8 | 1.0% | 32.6 | 1.4% | −38% ✅ | 937 | 564 | −40% |
| synthetic @ different inputs | 8 | 52.8 | 1.0% | 32.6 | 1.4% | −38% ✅ ≠in | 937 | 564 | −40% |

<sub>ns/op: median time of one evaluation, loop overhead subtracted; ±: spread of the samples (1.4826·MAD/median); B vs A: change of B relative to A, negative = less time (faster); ✅/❌: every round of B was faster/slower than every round of A, by at least 1%; ~: rounds overlap, no clear difference; ≈0: too fast to compare; instr/op: instructions per evaluation; layout?: the time changed, the instruction count did not; the amount of work does not explain it (code placement? cache or branch behaviour?); ≠in: A and B got different inputs</sub>
warning: the result changes from call to call, so outputs cannot be compared: synthetic @ random result
warning: A and B measured different inputs (the suite builds them with a function that behaves differently), timings are not comparable: synthetic @ different inputs
warning: 1 case changed wall time with unchanged instruction counts (layout?): the amount of work is the same, so look for the cause before reporting it: compare `objdump -d` of the function in both builds and `perf stat -e branch-misses,cache-misses`
warning: 1 case has a round more than 10% slower than another round of the same build (something disturbed a process), so the ratio and mark are shaky; run again: synthetic @ one disturbed round
