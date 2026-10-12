# json_encode(): inline UTF-8 decoding, scan position in a register

php-src change: branch [`json-utf8-2byte`](https://github.com/ArtUkrainskiy/php-src/commits/json-utf8-2byte), two commits on master [`897d2091cb4`](https://github.com/php/php-src/commit/897d2091cb4):

1. [`89659558c3c`](https://github.com/ArtUkrainskiy/php-src/commit/89659558c3c) "ext/standard: Decode common UTF-8 inline in php_next_utf8_char()". `php_next_utf8_char()` becomes a static inline function in `ext/standard/html.h` that decodes ASCII and valid two- and three-byte sequences itself; everything else, including every invalid sequence, goes to the former function, renamed `php_next_utf8_char_slow()`. Callers are `json_encode()`, `utf8_decode()` and the xml extension's decoder.
2. [`00ef789b361`](https://github.com/ArtUkrainskiy/php-src/commit/00ef789b361) "ext/json: Keep the scan position of json_encode() in a register". `json_encode()` decodes into a separate variable, so `&pos` no longer escapes and the loop over plain bytes keeps `pos` in a register instead of storing and reloading it per byte.

## Machine and method

i7-13700H laptop, pinned to P-core 2 (`taskset -c 2`), governor powersave. Release builds from commits with `bench build` (`-O2 -g -falign-functions=64 -falign-loops=32`, GCC 13.3, `--enable-werror --with-libxml --enable-xml`).

Each number is per `json_encode()` call: `perf stat` (`cpu_core` counters) over N calls minus the same process with 0 calls, divided by N, so start-up and input preparation cancel out. Three passes per case in alternating build order, median taken. N is chosen so a run takes about 50 ms. Cycles rather than nanoseconds: the laptop heats up to 86–91 °C in long runs and its clock moves, while cycle counts stay within a few percent.

Builds in the data files:

| name | commit |
|---|---|
| `final-base` | master `897d2091cb4` |
| `v2c1` | commit 1 only, `89659558c3c` |
| `v2` | both commits, `00ef789b361` |
| `hsc-only` | master + php-src #24145 (`get_next_char()` always inline, ASCII fast path in `htmlspecialchars()`) |
| `hsc-both` | this branch + #24145 |

## Summary

Relative to master, lower is better.

- **Non-ASCII text:** Cyrillic 0.63 of master's cycles, CJK 0.79, French 0.68; with `JSON_UNESCAPED_UNICODE` 0.65, 0.79, 0.80. Commit 1 gives this in instructions (the generic `get_next_char()` call was about 43 instructions per character in callgrind), commit 2 adds the register.
- **ASCII and escapes:** HTML 0.56, URLs 0.71, a quote every 16 bytes 0.44, every 8 bytes 0.50, plain ASCII 0.90–0.96. This is commit 2.
- **Records:** 1,000 arrays of 10 fields 0.95, 1,000 objects with 10 declared properties 0.94.
- **Slower:** a string in which every byte needs escaping, 1.09 (1.05 instructions): `pos` has to be reset to 0 in a register on the way back into the loop, where master reloaded it from the stack.
- **Each commit alone regresses something:** commit 1 alone has unchanged instructions on ASCII but cycles that move with code placement (0.60–1.12 on rows with identical instruction counts); commit 2 alone, measured earlier on `cd383dcc377`, made Cyrillic and the every-byte row 10% slower and a 100-key array 6% slower.
- **With #24145:** #24145 alone takes Cyrillic and CJK to 0.82 and 0.90 (it inlines `get_next_char()`, so `php_next_utf8_char_slow()` loses its charset switch). This branch on top of it: 0.77 and 0.87 of #24145. The two merge without conflicts.
- **`utf8_decode()`:** 2.2–2.8× fewer instructions on 4 KiB of Latin-1, Cyrillic or ASCII text (`udecode-bench.php`).

Rows where the two runs of a build differ by more than 5% (see the spread column) are rough; the instruction columns are not affected by that.

## Full table

| case | master instr | master cycles | commit 1 instr / cycles | both instr / cycles | spread master / both | #24145 instr / cycles | #24145 + this vs #24145, instr / cycles |
|---|---:|---:|---:|---:|---:|---:|---:|
| ascii-16 | 766 | 135 | 1.00 / 1.01 | 0.98 / 0.96 | 5% / 6% | 1.00 / 0.98 | 0.98 / 0.95 |
| ascii-256 | 3,918 | 703 | 1.00 / 1.04 | 0.93 / 0.92 | 3% / 32% | 1.00 / 1.10 | 0.93 / 0.83 |
| ascii-4k | 49,876 | 8,550 | 1.00 / 1.01 | 0.92 / 0.91 | 1% / 1% | 1.00 / 1.01 | 0.92 / 0.90 |
| ascii-64k | 787,681 | 137,393 | 1.00 / 1.00 | 0.92 / 0.90 | 1% / 2% | 1.00 / 1.00 | 0.92 / 0.90 |
| html-4k | 83,398 | 29,432 | 0.99 / 0.99 | 0.97 / 0.56 | 3% / 1% | 1.00 / 0.99 | 0.98 / 0.57 |
| url-4k | 91,022 | 27,362 | 0.99 / 1.11 | 0.98 / 0.71 | 1% / 1% | 1.00 / 1.00 | 0.98 / 0.71 |
| url-4k-unescaped-slashes | 89,556 | 30,435 | 0.99 / 0.99 | 0.98 / 0.56 | 4% / 3% | 1.00 / 0.99 | 0.98 / 0.56 |
| esc-every-16 | 65,002 | 24,845 | 1.00 / 0.83 | 0.95 / 0.44 | 3% / 3% | 1.00 / 0.99 | 0.95 / 0.44 |
| esc-every-8 | 81,104 | 24,816 | 0.99 / 0.60 | 0.97 / 0.50 | 4% / 2% | 1.00 / 0.85 | 0.97 / 0.59 |
| esc-every-byte | 165,030 | 23,538 | 1.00 / 0.99 | 1.05 / 1.09 | 0% / 1% | 1.00 / 0.99 | 1.05 / 1.09 |
| newlines-every-40 | 55,588 | 15,513 | 1.00 / 1.12 | 0.93 / 0.60 | 4% / 10% | 1.00 / 1.01 | 0.93 / 0.60 |
| cyrillic-4k | 224,687 | 38,961 | 0.76 / 0.80 | 0.71 / 0.63 | 10% / 1% | 0.88 / 0.82 | 0.80 / 0.77 |
| cyrillic-4k-unescaped | 239,213 | 59,440 | 0.71 / 0.74 | 0.67 / 0.65 | 1% / 1% | 0.89 / 0.92 | 0.75 / 0.71 |
| cjk-4k | 170,497 | 25,261 | 0.78 / 0.78 | 0.74 / 0.79 | 2% / 4% | 0.89 / 0.90 | 0.84 / 0.87 |
| cjk-4k-unescaped | 180,907 | 26,608 | 0.81 / 0.84 | 0.76 / 0.79 | 1% / 2% | 0.89 / 0.89 | 0.85 / 0.89 |
| french-4k | 126,432 | 25,772 | 0.84 / 0.95 | 0.80 / 0.68 | 2% / 2% | 0.93 / 0.98 | 0.86 / 0.70 |
| french-4k-unescaped | 131,548 | 29,473 | 0.81 / 0.92 | 0.77 / 0.80 | 3% / 1% | 0.93 / 0.94 | 0.83 / 0.84 |
| ascii-rare-utf8-unescaped | 65,728 | 20,388 | 0.92 / 0.98 | 0.86 / 0.52 | 12% / 5% | 0.97 / 1.08 | 0.88 / 0.47 |
| api-1000-records | 4,849,120 | 892,452 | 1.00 / 1.02 | 0.97 / 0.95 | 1% / 1% | 1.00 / 1.03 | 0.97 / 0.93 |
| objects-1000-records | 4,684,706 | 863,951 | 1.00 / 0.98 | 0.97 / 0.94 | 4% / 0% | 1.00 / 0.99 | 0.97 / 0.94 |
| object-100-keys | 36,722 | 7,158 | 1.00 / 0.94 | 0.98 / 0.89 | 41% / 3% | 1.00 / 0.97 | 0.98 / 0.93 |

Cases are defined in [`cases.php`](cases.php); 4 KiB strings unless the name says otherwise. Raw per-run data: [`cycles.txt`](cycles.txt) (`<build> <case> <cycles per call>`) and [`instructions.txt`](instructions.txt) (`<case>` then one column per build in the order of the table above).

## Together with other open PRs

Measured on master `cd383dcc377` with the same method and code that runs the same instructions as the commits above (within 0.1%). Raw data: [`cycles-with-23682.txt`](cycles-with-23682.txt), [`cycles-with-23675.txt`](cycles-with-23675.txt). In those files `master2` is master, `utf8h` this change, `23682` / `23675` the other PR alone and `23682mine` / `23675mine` the combination. #23675 there was merged onto `80d2b997192`, slightly older than the other builds; it needs `ZEND_STATIC_ASSERT()` replaced by `static_assert()` to build on current master.

| cycles vs master | #23682 | this | both | #23675 | both |
|---|---:|---:|---:|---:|---:|
| ASCII | 0.78 | 0.89 | 0.70 | 0.22 | 0.22 |
| HTML | 0.81 | 0.56 | 0.53 | 0.21 | 0.22 |
| a quote in every byte | 1.00 | 1.09 | 0.92 | 1.20 | 1.22 |
| Cyrillic | 1.15 | 0.64 | 0.61 | 1.13 | 0.84 |
| CJK | 1.00 | 0.78 | 0.73 | 1.11 | 0.79 |
| French | 0.98 | 0.70 | 0.63 | 0.77 | 0.66 |
| 1,000 arrays | 0.99 | 0.95 | 0.90 | 0.93 | 1.02 |

#23682 merges cleanly; with #23675 the only conflict is that it moves the loop body into `php_json_escape_dirty_char()`, where this change applies unchanged.

## In an application

Symfony Demo's `/en/api/posts` (140 KB of JSON), CLI with opcache, kernel booted once, 30 warm-up requests, then `perf stat` over 200 requests minus 0, three alternating runs on `cd383dcc377`: `json_encode()` is 2.0M of 67.5M instructions per request (callgrind). With this change a request runs 0.2% fewer instructions and 1.0% fewer cycles by median; runs of the same build differ by up to 1.2%, so the cycle gain is within noise.

## Output verification

All against master, byte for byte, on the release builds and on a debug build with ASan and UBSan (`--enable-debug --enable-address-sanitizer --enable-undefined-sanitizer`, `USE_ZEND_ALLOC=0`), where no sanitizer report appeared:

- [`pairs.php`](pairs.php): every pair of bytes, alone, inside ASCII and after 20 ASCII bytes, six flag sets;
- [`triples.php`](triples.php): every three-byte sequence with an E0..EF lead byte, alone and inside ASCII, six flag sets;
- [`positions.php`](positions.php): every byte value at every position of ASCII strings 1–24 bytes long, four flag sets;
- [`fuzz.php`](fuzz.php): 1,000,000 random strings (5 seeds × 200,000) of 0–300 bytes, as values and as keys, mixing escapes, two-, three- and four-byte characters, U+2028/2029, overlong and invalid sequences, 11 flag sets;
- [`keys.php`](keys.php): literal keys, also ones that need escaping, through arrays, `stdClass` and declared properties, 10 flag sets;
- [`udecode.php`](udecode.php): `utf8_decode()` on all pairs and E0..EF triples;
- php-src tests: `ext/json`, `ext/xml`, `ext/standard/tests/strings` (838 passed on the release build, 833 on the sanitizer build, none failed).

Each script prints one hash per flag set; the two builds must print the same lines. A separate review compared the inline decoder with `get_next_char(cs_utf_8)` over every 3-byte prefix, buffer lengths 0–6 and start cursors 0 and 1 (285 million calls): no difference in return value, cursor or status.

## Reproduce

From the repository root, with php-src checked out next to it:

```sh
git -C ../php-src fetch https://github.com/ArtUkrainskiy/php-src.git json-utf8-2byte
E="--enable-werror --with-libxml --enable-xml"
BENCH_CONFIGURE_EXTRA="$E" ./bench build json-final-base 897d2091cb4
BENCH_CONFIGURE_EXTRA="$E" ./bench build json-v2c1 89659558c3c
BENCH_CONFIGURE_EXTRA="$E" ./bench build json-v2 00ef789b361
cd reports/json-encode-utf8-inline
./instructions.sh final-base v2c1 v2          # instructions per call, one line per case
./cycles.sh out.txt final-base v2c1 v2        # cycles, 3 alternating passes, prints ratios
for t in pairs triples positions udecode keys; do
  for b in final-base v2; do echo "$b $t $(../../../php-builds/json-$b/sapi/cli/php -n $t.php | md5sum)"; done
done
../../../php-builds/json-v2/sapi/cli/php -n fuzz.php 200000 1   # compare with the same seed on final-base
```

The scripts look for builds in `../php-builds/json-<name>` next to the repository, or in `$BENCH_BUILDS/json-<name>`.
