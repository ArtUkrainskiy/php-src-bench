# Construction and memory

Construction is a warm constructor, without a query or destruction. The constructor memory table uses the process before loading the dictionary as its baseline. PCRE cache memory is not compared here. “Dictionary + object” is the sum of retained components. Construction peak includes them and temporary buffers; other columns should not be added to it. Zend accounting, not RSS. All five fresh observations and 15 constructor samples are available in [memory.json](data/memory.json).

| Compiler / class / keys | Construction, µs | Dictionary, KiB | Additional object memory, KiB | Dictionary + object, KiB | Peak including dictionary, KiB |
|---|---:|---:|---:|---:|---:|
| gcc15 / Str\Matcher / 8 | 3.265 | 0.523 | 4.688 | 5.211 | 8.336 |
| gcc15 / Str\Matcher / 128 | 52.899 | 7.555 | 57.750 | 65.305 | 109.305 |
| gcc15 / Str\Matcher / 128 | 65.361 | 7.891 | 62.375 | 70.266 | 110.266 |
| gcc15 / Str\Matcher / 1024 | 757.965 | 60.055 | 324.859 | 384.914 | 652.914 |
| gcc15 / Str\Matcher / 10000 | 15502.977 | 650.680 | 2836.750 | 3487.430 | 5799.461 |
| gcc15 / Str\Replacer / 16 | 7.533 | 2.180 | 12.531 | 14.711 | 25.211 |
| gcc15 / Str\Replacer / 16 | 6.748 | 2.055 | 8.531 | 10.586 | 21.086 |
| gcc15 / Str\Replacer / 32 | 13.726 | 4.305 | 19.109 | 23.414 | 38.914 |
| gcc15 / Str\Replacer / 32 | 13.827 | 4.055 | 19.109 | 23.164 | 38.664 |
| gcc15 / Str\Replacer / 1 | 0.354 | 0.445 | 1.008 | 1.453 | 2.008 |
| gcc15 / Str\Replacer / 1 | 0.725 | 0.477 | 1.328 | 1.805 | 3.008 |
| gcc15 / Str\Replacer / 32 | 13.261 | 3.680 | 19.109 | 22.789 | 38.289 |
| gcc15 / Str\Replacer / 32 | 13.324 | 5.180 | 19.109 | 24.289 | 39.789 |
| gcc15 / Str\Replacer / 32 | 13.325 | 3.930 | 19.109 | 23.039 | 38.539 |
| gcc15 / Str\Replacer / 1000 | 314.796 | 127.492 | 224.750 | 352.242 | 736.242 |
| gcc15 / Str\Replacer / 10000 | 5857.735 | 1513.180 | 2048.750 | 3561.930 | 7109.961 |
| gcc15 / Str\Replacer / 10 | 2.909 | 1.617 | 3.812 | 5.430 | 13.523 |
| gcc15 / Str\Replacer / 128 | 113.072 | 21.391 | 79.375 | 100.766 | 156.766 |
| gcc15 / Str\Replacer / 64 | 62.188 | 11.969 | 55.875 | 67.844 | 179.844 |
| gcc15 / Str\Replacer / 24 | 15.446 | 3.555 | 19.625 | 23.180 | 44.180 |
| gcc15 / Str\Replacer / 1000 | 1333.123 | 133.805 | 396.750 | 530.555 | 1010.555 |
| gcc15 / Str\Replacer / 1000 | 1373.283 | 127.492 | 396.781 | 524.273 | 1004.273 |
| gcc15 / Str\Replacer / 10000 | 28552.834 | 1577.555 | 3186.250 | 4763.805 | 10954.367 |
| gcc15 / Str\Replacer / 10000 | 28869.130 | 1513.180 | 3202.750 | 4715.930 | 10889.992 |
| clang21 / Str\Matcher / 8 | 3.212 | 0.523 | 4.688 | 5.211 | 8.336 |
| clang21 / Str\Matcher / 128 | 51.826 | 7.555 | 57.750 | 65.305 | 109.305 |
| clang21 / Str\Matcher / 128 | 67.870 | 7.891 | 62.375 | 70.266 | 110.266 |
| clang21 / Str\Matcher / 1024 | 754.623 | 60.055 | 324.859 | 384.914 | 652.914 |
| clang21 / Str\Matcher / 10000 | 15752.852 | 650.680 | 2836.750 | 3487.430 | 5799.461 |
| clang21 / Str\Replacer / 16 | 7.864 | 2.180 | 12.531 | 14.711 | 25.211 |
| clang21 / Str\Replacer / 16 | 6.974 | 2.055 | 8.531 | 10.586 | 21.086 |
| clang21 / Str\Replacer / 32 | 14.417 | 4.305 | 19.109 | 23.414 | 38.914 |
| clang21 / Str\Replacer / 32 | 14.069 | 4.055 | 19.109 | 23.164 | 38.664 |
| clang21 / Str\Replacer / 1 | 0.338 | 0.445 | 1.008 | 1.453 | 2.008 |
| clang21 / Str\Replacer / 1 | 0.659 | 0.477 | 1.328 | 1.805 | 3.008 |
| clang21 / Str\Replacer / 32 | 13.830 | 3.680 | 19.109 | 22.789 | 38.289 |
| clang21 / Str\Replacer / 32 | 13.945 | 5.180 | 19.109 | 24.289 | 39.789 |
| clang21 / Str\Replacer / 32 | 13.983 | 3.930 | 19.109 | 23.039 | 38.539 |
| clang21 / Str\Replacer / 1000 | 313.130 | 127.492 | 224.750 | 352.242 | 736.242 |
| clang21 / Str\Replacer / 10000 | 5908.931 | 1513.180 | 2048.750 | 3561.930 | 7109.961 |
| clang21 / Str\Replacer / 10 | 2.799 | 1.617 | 3.812 | 5.430 | 13.523 |
| clang21 / Str\Replacer / 128 | 115.941 | 21.391 | 79.375 | 100.766 | 156.766 |
| clang21 / Str\Replacer / 64 | 60.046 | 11.969 | 55.875 | 67.844 | 179.844 |
| clang21 / Str\Replacer / 24 | 15.980 | 3.555 | 19.625 | 23.180 | 44.180 |
| clang21 / Str\Replacer / 1000 | 1381.920 | 133.805 | 396.750 | 530.555 | 1010.555 |
| clang21 / Str\Replacer / 1000 | 1423.383 | 127.492 | 396.781 | 524.273 | 1004.273 |
| clang21 / Str\Replacer / 10000 | 29170.876 | 1577.555 | 3186.250 | 4763.805 | 10954.367 |
| clang21 / Str\Replacer / 10000 | 29476.459 | 1513.180 | 3202.750 | 4715.930 | 10889.992 |
| gcc15 / Str\Matcher / 128 | 52.138 | 7.555 | 57.750 | 65.305 | 109.305 |
| clang21 / Str\Matcher / 128 | 52.055 | 7.555 | 57.750 | 65.305 | 109.305 |

## Temporary memory in replace()

The baseline includes the loaded text, dictionary, reference result and prepared Replacer. Allocated result memory includes buffer capacity and the string header and may exceed the length of its contents. Call peak includes the returned string and temporary buffers. The prepared object is not counted again in this peak. The measurement is of replace($text) without the count argument.

| Compiler | Input | Additional result memory, KiB | Call peak, KiB |
|---|---|---:|---:|
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | 0.000 | 0.000 |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | 0.000 | 0.000 |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | 8.000 | 8.250 |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | 8.000 | 8.250 |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | 8.000 | 8.250 |
| gcc15 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | 8.000 | 8.250 |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | 0.000 | 0.000 |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | 0.000 | 0.000 |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | 8.000 | 8.250 |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | 8.000 | 8.250 |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | 8.000 | 8.500 |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | 8.000 | 8.500 |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | 8.000 | 8.250 |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | 8.000 | 8.250 |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | 8.000 | 8.250 |
| gcc15 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | 8.000 | 8.250 |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 3856 B | 4.000 | 4.250 |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 4608 B | 8.000 | 8.250 |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 4000 B | 4.000 | 4.250 |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | 0.000 | 0.000 |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | 0.000 | 0.000 |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | 20.000 | 20.250 |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | 20.000 | 20.250 |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | 20.000 | 20.250 |
| gcc15 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | 20.000 | 20.250 |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | 0.000 | 0.000 |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | 0.000 | 0.000 |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | 20.000 | 20.250 |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | 20.000 | 20.250 |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | 20.000 | 20.500 |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | 20.000 | 20.500 |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | 20.000 | 20.250 |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | 20.000 | 20.250 |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | 20.000 | 20.250 |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | 20.000 | 20.250 |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16144 B | 16.000 | 16.250 |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 16896 B | 20.000 | 20.250 |
| gcc15 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16288 B | 16.000 | 16.250 |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100; keys {{…}} | 1028.000 | 1030.000 |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000; keys {{…}} | 1028.000 | 1044.000 |
| gcc15 | 820 B; dictionary of 10 keys; key lengths 13–20 B; replacements: 11; keys {{…}}; output 860 B | 4.000 | 4.250 |
| gcc15 | 7301 B; dictionary of 128 keys; key lengths 4–28 B; replacements: 4; output 7372 B | 8.000 | 8.250 |
| gcc15 | 8607 B; dictionary of 64 keys; key lengths 30–69 B; replacements: 9; output 8454 B | 12.000 | 12.250 |
| gcc15 | 69643 B; dictionary of 24 keys; key lengths 24 B; replacements: 3; one replacement value; output 69601 B | 68.000 | 68.250 |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 0 | 0.000 | 0.000 |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 10 | 1028.000 | 1028.250 |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 100 | 1028.000 | 1030.000 |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 500 | 1028.000 | 1036.000 |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 750 | 1028.000 | 1044.000 |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 1000 | 1028.000 | 1044.000 |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 0 | 0.000 | 0.000 |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 10 | 1028.000 | 1028.250 |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100 | 1028.000 | 1030.000 |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 500 | 1028.000 | 1036.000 |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 750 | 1028.000 | 1044.000 |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 1000 | 1028.000 | 1044.000 |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 0 | 0.000 | 0.000 |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 100 | 1028.000 | 1030.000 |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 1000 | 1028.000 | 1044.000 |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 5000 | 1028.000 | 1156.000 |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 7500 | 1028.000 | 1156.000 |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 10000 | 1028.000 | 1284.000 |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 0 | 0.000 | 0.000 |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 100 | 1028.000 | 1030.000 |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000 | 1028.000 | 1044.000 |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 5000 | 1028.000 | 1156.000 |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 7500 | 1028.000 | 1156.000 |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 10000 | 1028.000 | 1284.000 |
| gcc15 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 2 | 8.000 | 8.250 |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | 0.000 | 0.000 |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | 0.000 | 0.000 |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | 8.000 | 8.250 |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | 8.000 | 8.250 |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | 8.000 | 8.250 |
| clang21 | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | 8.000 | 8.250 |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | 0.000 | 0.000 |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | 0.000 | 0.000 |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | 8.000 | 8.250 |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | 8.000 | 8.250 |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | 8.000 | 8.500 |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | 8.000 | 8.500 |
| clang21 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | 8.000 | 8.250 |
| clang21 | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | 8.000 | 8.250 |
| clang21 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | 8.000 | 8.250 |
| clang21 | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | 8.000 | 8.250 |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 3856 B | 4.000 | 4.250 |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 4608 B | 8.000 | 8.250 |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 4000 B | 4.000 | 4.250 |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | 0.000 | 0.000 |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | 0.000 | 0.000 |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | 20.000 | 20.250 |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | 20.000 | 20.250 |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | 20.000 | 20.250 |
| clang21 | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | 20.000 | 20.250 |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | 0.000 | 0.000 |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | 0.000 | 0.000 |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | 20.000 | 20.250 |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | 20.000 | 20.250 |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | 20.000 | 20.500 |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | 20.000 | 20.500 |
| clang21 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | 20.000 | 20.250 |
| clang21 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | 20.000 | 20.250 |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | 20.000 | 20.250 |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | 20.000 | 20.250 |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16144 B | 16.000 | 16.250 |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 16896 B | 20.000 | 20.250 |
| clang21 | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16288 B | 16.000 | 16.250 |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100; keys {{…}} | 1028.000 | 1030.000 |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000; keys {{…}} | 1028.000 | 1044.000 |
| clang21 | 820 B; dictionary of 10 keys; key lengths 13–20 B; replacements: 11; keys {{…}}; output 860 B | 4.000 | 4.250 |
| clang21 | 7301 B; dictionary of 128 keys; key lengths 4–28 B; replacements: 4; output 7372 B | 8.000 | 8.250 |
| clang21 | 8607 B; dictionary of 64 keys; key lengths 30–69 B; replacements: 9; output 8454 B | 12.000 | 12.250 |
| clang21 | 69643 B; dictionary of 24 keys; key lengths 24 B; replacements: 3; one replacement value; output 69601 B | 68.000 | 68.250 |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 0 | 0.000 | 0.000 |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 10 | 1028.000 | 1028.250 |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 100 | 1028.000 | 1030.000 |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 500 | 1028.000 | 1036.000 |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 750 | 1028.000 | 1044.000 |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 1000 | 1028.000 | 1044.000 |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 0 | 0.000 | 0.000 |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 10 | 1028.000 | 1028.250 |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100 | 1028.000 | 1030.000 |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 500 | 1028.000 | 1036.000 |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 750 | 1028.000 | 1044.000 |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 1000 | 1028.000 | 1044.000 |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 0 | 0.000 | 0.000 |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 100 | 1028.000 | 1030.000 |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 1000 | 1028.000 | 1044.000 |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 5000 | 1028.000 | 1156.000 |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 7500 | 1028.000 | 1156.000 |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 10000 | 1028.000 | 1284.000 |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 0 | 0.000 | 0.000 |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 100 | 1028.000 | 1030.000 |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000 | 1028.000 | 1044.000 |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 5000 | 1028.000 | 1156.000 |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 7500 | 1028.000 | 1156.000 |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 10000 | 1028.000 | 1284.000 |
| clang21 | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 2 | 8.000 | 8.250 |
