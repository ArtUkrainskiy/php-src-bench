A: base — PHP 8.6.0-dev, 100e8f353ea ext/uri: Preserve empty query and fragment in URL builders  
CPU 2 (13th Gen Intel(R) Core(TM) i7-13700H), governor powersave, turbo on, kernel 7.0.0-34-generic  
4 rounds × 7 samples × 10 ms, cc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0, configure --disable-all --disable-cgi --disable-phpdbg --enable-cli, CFLAGS -O2 -g -falign-functions=64 -falign-loops=32, 2026-10-05T19:28+00:00  

| case | bytes | ns/op | ± |
|---|--:|--:|--:|
| htmlspecialchars @ empty | 0 | 6.1 | 4.9% |
| htmlspecialchars @ word-8 | 8 | 52.8 | 1.0% |
| htmlspecialchars @ en-1k | 1042 | 4308 | 0.9% |
| htmlspecialchars @ html-page-4k | 4096 | 15294 | 1.0% |
| htmlspecialchars @ amp-1k | 1024 | 2394 | 0.4% |
| htmlspecialchars cp1251 @ cp1251-1k | 1056 | 3401 | 1.9% |
| htmlentities @ ru-1k | 1030 | 4582 | 1.2% |
| synthetic @ B slower | 1042 | 1757 | 0.4% |
| synthetic @ same instructions | 8 | 52.8 | 1.0% |

<sub>ns/op: median time of one evaluation, loop overhead subtracted; ±: spread of the samples (1.4826·MAD/median)</sub>
