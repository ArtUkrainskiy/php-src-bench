A: base — PHP 8.6.0-dev, 100e8f353ea ext/uri: Preserve empty query and fragment in URL builders  
B: /work/other/php — PHP 8.6.0-dev, /work/other/php  
CPU 2 (13th Gen Intel(R) Core(TM) i7-13700H), governor powersave, turbo on, kernel 7.0.0-34-generic  
2 rounds × 5 samples × 5 ms, cc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0, configure --disable-all --disable-cgi --disable-phpdbg --enable-cli, CFLAGS -O2 -g -falign-functions=64 -falign-loops=32, 2026-10-05T19:28+00:00  
! A or B was not built by `bench build`: nothing checks that both have the same configure options and CFLAGS  

| case | bytes | A ns/op | ± | B ns/op | ± | B vs A |
|---|--:|--:|--:|--:|--:|--:|
| htmlspecialchars @ empty | 0 | 6.1 | 5.5% | 6.2 | 4.1% | 1.01× slower ? |
| htmlspecialchars @ word-8 | 8 | 52.8 | 1.0% | 32.5 | 1.4% | 1.63× faster ? |
| htmlspecialchars @ en-1k | 1042 | 4327 | 1.6% | 1756 | 0.3% | 2.46× faster ? |
| htmlspecialchars @ html-page-4k | 4096 | 15317 | 0.8% | 8234 | 1.1% | 1.86× faster ? |
| htmlspecialchars @ amp-1k | 1024 | 2399 | 0.7% | 1726 | 0.7% | 1.39× faster ? ≠out |
| htmlspecialchars cp1251 @ cp1251-1k | 1056 | 3443 | 1.7% | 3476 | 0.8% | 1.01× slower ? |
| htmlentities @ ru-1k | 1030 | 4589 | 0.9% | 3546 | 0.6% | 1.29× faster ? |
| synthetic @ B slower | 1042 | 1756 | 0.3% | 4327 | 1.6% | 2.46× slower ? |
| synthetic @ same instructions | 8 | 52.8 | 1.0% | 32.5 | 1.4% | 1.63× faster ? |

<sub>ns/op: median time of one evaluation, loop overhead subtracted; ±: spread of the samples (1.4826·MAD/median); B vs A: A time / B time; ✅/❌: every round of B was faster/slower than every round of A, by at least 1%; ~: rounds overlap, no clear difference; ?: no verdict with fewer than 4 rounds; ≠out: A and B returned different results</sub>
warning: outputs differ between A and B for: htmlspecialchars @ amp-1k
warning: 1 of 9 cases have a spread above 5%: wall times are unreliable (background load?), rerun on an idle machine or add --perf
