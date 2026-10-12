# json_encode(): decode common UTF-8 sequences inline

php-src change: [`ca35c079a1f`](https://github.com/ArtUkrainskiy/php-src/commit/ca35c079a1f) "ext/standard: Add php_next_utf8_char_inline()" on branch [`json-utf8-2byte`](https://github.com/ArtUkrainskiy/php-src/commits/json-utf8-2byte), on master [`bd6c637d071`](https://github.com/php/php-src/commit/bd6c637d071).

## Summary

`json_encode()`, `utf8_decode()` and the xml extension decode one character at a time with `php_next_utf8_char()`. This adds `php_next_utf8_char_inline()`, which decodes the common cases at the call site. Non-ASCII text in `json_encode()` gets faster with every compiler I tried: Cyrillic 0.74–0.80 of master's cycles, CJK 0.72–0.79.

ASCII runs the same instructions as master. With GCC three ASCII-heavy inputs are slower in cycles (see Trade-offs).

## What changes and why it is faster

**Before.** `php_next_utf8_char()` lives in `html.c`, so it cannot be inlined into ext/json. Inside it, `get_next_char()` handles 14 charsets and was not inlined either, so each character paid two calls and a `switch` on the charset, and the value, the new position and the status came back through memory: about 43 instructions per character in callgrind (36 in `get_next_char()`, 7 in the wrapper).

**After.** `php_next_utf8_char_inline()` in `ext/standard/html.h` has the same contract as `php_next_utf8_char()`. It decodes ASCII and valid two- and three-byte sequences without a call; everything else (four-byte characters, every invalid or truncated sequence) goes to `php_next_utf8_char()`, which is unchanged and still exported.

**Why the shortcut is exact.** A lead byte C2..DF followed by a continuation byte 80..BF is always a valid shortest-form character: C0 and C1 are the only overlong two-byte leads. For three bytes the inline path checks the same two conditions as `get_next_char()`: the result is at least U+0800 (not overlong) and outside U+D800..U+DFFF (not a surrogate). Any other input runs the old code, so which bytes are rejected or skipped and the returned status stay exactly as before.

`EXPECTED(c < 0xe0)` keeps the two-byte case on the straight path. Without it GCC 13 placed that case behind two extra taken jumps: Cyrillic ran the same instructions but took 20% more cycles.

## Trade-offs

- **Three ASCII-heavy inputs are slower with GCC** in my builds: URLs (1.11–1.16 of master's cycles), ASCII with an é every 31 bytes (1.00–1.13) and a newline every 40 bytes (1.10–1.24). The newline row is code placement: built with plain `-O2` instead of the aligned functions and loops I use, it is at 0.97–1.02. The other two stay slower with plain `-O2` (URLs 1.07–1.10, the é row 1.09–1.20). URLs run the same instructions as master and show no difference in branch or front-end counters; on the é input the new branch for the inline path adds about 80 mispredictions per call. With clang none of the three is slower.
- **#24145** makes `get_next_char()` always inline, which also speeds up the out-of-line `php_next_utf8_char()`. On top of it this PR still removes 14–20% of the instructions on non-ASCII text, but with GCC 13 the cycles change less: Cyrillic 0.98, Cyrillic with `JSON_UNESCAPED_UNICODE` 0.79, CJK 0.88 of #24145's cycles. Both together: Cyrillic 0.80, CJK 0.78 of master. The two merge without conflicts.
- **API.** `php_next_utf8_char()` and its exported symbol are unchanged; `php_next_utf8_char_inline()` is new (UPGRADING.INTERNALS).
- **Other callers.** `utf8_decode()` (deprecated, still shipped) runs 2.2–2.8× fewer instructions on 4 KiB of Latin-1, Cyrillic or ASCII text. The xml extension's decoder uses the same path; not measured.
- **Size.** +768 bytes of code with GCC 13: `php_json_escape_string()` +351, `utf8_decode()` +224, the xml decoder +249.

## Machine and method

i7-13700H laptop, P-core 2 (`taskset -c 2`), governor powersave. Release builds from commits with `bench build` (`-O2 -g -falign-functions=64 -falign-loops=32`, `--enable-werror --with-libxml --enable-xml`): GCC 13.3, GCC 14.2 (`CC=gcc-14`), clang 18.1 (`CC=clang`), clang 20.1 (`CC=clang-20`).

Each number is per `json_encode()` call: `perf stat` (`cpu_core` counters) over N calls minus the same process with 0 calls, divided by N. Cycles are the median over alternating runs of master and the change: 3 for every row, more where a row was measured again. Cycles rather than nanoseconds: the laptop heats up to 86–91 °C in long runs and its clock moves, while cycle counts stay within a few percent.

## Results

| input (4 KiB unless noted) | instructions | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 |
|---|---:|---:|---:|---:|---:|
| Cyrillic | 0.75–0.78 | 0.80 | 0.74 | 0.75 | 0.79 |
| Cyrillic, `JSON_UNESCAPED_UNICODE` | 0.69–0.79 | 0.73 | 0.71 | 0.76 | 0.73 |
| CJK | 0.77–0.81 | 0.79 | 0.78 | 0.72 | 0.75 |
| CJK, `JSON_UNESCAPED_UNICODE` | 0.79–0.82 | 0.86 | 0.79 | 0.80 | 0.80 |
| French | 0.84–0.86 | 0.96 | 0.93 | 0.81 | 0.81 |
| French, `JSON_UNESCAPED_UNICODE` | 0.80–0.87 | 0.91 | 0.85 | 0.84 | 0.81 |
| ASCII with an é every 31 bytes, `JSON_UNESCAPED_UNICODE` | 0.92–0.94 | 1.00 | 1.13 | 0.93 | 0.95 |
| ASCII, 16 bytes | 1.00 | 0.94 | 1.04 | 1.01 | 1.01 |
| ASCII, 256 bytes | 1.00 | 0.99 | 1.00 | 1.06 | 1.02 |
| ASCII, 4 KiB | 1.00 | 1.00 | 1.00 | 0.97 | 1.00 |
| ASCII, 64 KiB | 1.00 | 0.99 | 1.02 | 0.99 | 0.99 |
| HTML | 0.99–1.00 | 1.00 | 1.03 | 1.00 | 1.01 |
| URLs | 0.99–1.00 | 1.11 | 1.16 | 1.00 | 1.00 |
| URLs, `JSON_UNESCAPED_SLASHES` | 0.99–1.00 | 0.98 | 0.90 | 1.00 | 0.98 |
| a quote every 16 bytes | 1.00 | 0.83 | 0.83 | 1.00 | 1.00 |
| a quote every 8 bytes | 0.99–1.00 | 0.72 | 0.55 | 1.00 | 1.00 |
| a newline every 40 bytes | 1.00 | 1.10 | 1.24 | 1.00 | 1.00 |
| a quote in every byte | 1.00–1.02 | 1.00 | 1.00 | 1.00 | 1.00 |
| 1,000 arrays of 10 fields | 1.00 | 0.99 | 0.99 | 1.00 | 0.99 |
| 1,000 objects of 10 declared properties | 1.00 | 0.99 | 0.99 | 1.00 | 0.99 |
| an array with 100 keys | 1.00 | 0.95 | 0.99 | 1.00 | 1.00 |

Instructions per compiler, cycles and the spread between runs (the largest difference between runs of either build; rows above 5% are rough):

| case | GCC 13.3 instr. / cycles / spread | GCC 14.2 instr. / cycles / spread | clang 18.1 instr. / cycles / spread | clang 20.1 instr. / cycles / spread |
|---|---:|---:|---:|---:|
| cyrillic-4k | 0.76 / 0.80 / 25% | 0.75 / 0.74 / 12% | 0.78 / 0.75 / 9% | 0.77 / 0.79 / 14% |
| cyrillic-4k-unescaped | 0.71 / 0.73 / 2% | 0.69 / 0.71 / 2% | 0.79 / 0.76 / 1% | 0.79 / 0.73 / 3% |
| cjk-4k | 0.78 / 0.79 / 10% | 0.77 / 0.78 / 8% | 0.81 / 0.72 / 7% | 0.80 / 0.75 / 5% |
| cjk-4k-unescaped | 0.81 / 0.86 / 12% | 0.79 / 0.79 / 1% | 0.82 / 0.80 / 3% | 0.81 / 0.80 / 2% |
| french-4k | 0.84 / 0.96 / 5% | 0.84 / 0.93 / 6% | 0.86 / 0.81 / 6% | 0.86 / 0.81 / 41% |
| french-4k-unescaped | 0.81 / 0.91 / 3% | 0.80 / 0.85 / 4% | 0.87 / 0.84 / 2% | 0.87 / 0.81 / 3% |
| ascii-rare-utf8-unescaped | 0.92 / 1.00 / 15% | 0.92 / 1.13 / 35% | 0.94 / 0.93 / 6% | 0.94 / 0.95 / 42% |
| ascii-16 | 1.00 / 0.94 / 6% | 1.00 / 1.04 / 5% | 1.00 / 1.01 / 1% | 1.00 / 1.01 / 5% |
| ascii-256 | 1.00 / 0.99 / 1% | 1.00 / 1.00 / 3% | 1.00 / 1.06 / 1% | 1.00 / 1.02 / 2% |
| ascii-4k | 1.00 / 1.00 / 3% | 1.00 / 1.00 / 4% | 1.00 / 0.97 / 3% | 1.00 / 1.00 / 5% |
| ascii-64k | 1.00 / 0.99 / 4% | 1.00 / 1.02 / 2% | 1.00 / 0.99 / 1% | 1.00 / 0.99 / 2% |
| html-4k | 0.99 / 1.00 / 6% | 1.00 / 1.03 / 6% | 1.00 / 1.00 / 7% | 1.00 / 1.01 / 4% |
| url-4k | 0.99 / 1.11 / 48% | 1.00 / 1.16 / 7% | 1.00 / 1.00 / 8% | 1.00 / 1.00 / 6% |
| url-4k-unescaped-slashes | 0.99 / 0.98 / 2% | 1.00 / 0.90 / 4% | 1.00 / 1.00 / 1% | 1.00 / 0.98 / 2% |
| esc-every-16 | 1.00 / 0.83 / 10% | 1.00 / 0.83 / 10% | 1.00 / 1.00 / 49% | 1.00 / 1.00 / 5% |
| esc-every-8 | 0.99 / 0.72 / 26% | 1.00 / 0.55 / 17% | 1.00 / 1.00 / 7% | 1.00 / 1.00 / 7% |
| newlines-every-40 | 1.00 / 1.10 / 41% | 1.00 / 1.24 / 33% | 1.00 / 1.00 / 4% | 1.00 / 1.00 / 10% |
| esc-every-byte | 1.00 / 1.00 / 116% | 1.02 / 1.00 / 9% | 1.00 / 1.00 / 5% | 1.00 / 1.00 / 7% |
| api-1000-records | 1.00 / 0.99 / 8% | 1.00 / 0.99 / 8% | 1.00 / 1.00 / 5% | 1.00 / 0.99 / 16% |
| objects-1000-records | 1.00 / 0.99 / 8% | 1.00 / 0.99 / 5% | 1.00 / 1.00 / 6% | 1.00 / 0.99 / 82% |
| object-100-keys | 1.00 / 0.95 / 79% | 1.00 / 0.99 / 6% | 1.00 / 1.00 / 5% | 1.00 / 1.00 / 10% |

Cases are defined in [`cases.php`](cases.php), 4 KiB strings unless the name says otherwise. Raw data: [`cycles.txt`](cycles.txt) (`<compiler> <base|c1> <case> <cycles per call>`), [`instructions.txt`](instructions.txt) (`<compiler> <case> <master> <change>`).

## Output verification

Against master, byte for byte and including `json_last_error()`, with all four compilers and on a GCC debug build with ASan and UBSan (`--enable-debug --enable-address-sanitizer --enable-undefined-sanitizer`, `USE_ZEND_ALLOC=0`), where no sanitizer report appeared:

- [`pairs.php`](pairs.php): every pair of bytes, alone, inside ASCII and after 20 ASCII bytes, six flag sets;
- [`triples.php`](triples.php): every three-byte sequence with an E0..EF lead byte, alone and inside ASCII, six flag sets;
- [`positions.php`](positions.php): every byte value at every position of ASCII strings 1–24 bytes long, four flag sets;
- [`fuzz.php`](fuzz.php): 1,000,000 random strings (5 seeds × 200,000) of 0–300 bytes, as values and as keys, 11 flag sets;
- [`keys.php`](keys.php): literal keys, also ones that need escaping, through arrays, `stdClass` and declared properties, 10 flag sets;
- [`udecode.php`](udecode.php): `utf8_decode()` on all pairs and E0..EF triples;
- php-src tests `ext/json`, `ext/xml`, `ext/standard/tests/strings`: 838 passed with each compiler, 833 on the sanitizer build, none failed.

The new test `json_encode_utf8_sequences.phpt` fails if the overlong checks of the inline path are removed. A separate review compared the inline decoder with `get_next_char(cs_utf_8)` on every three-byte prefix, buffer lengths 0–6 and start cursors 0 and 1 (285 million calls): no difference in value, cursor or status.

## Not tested

aarch64, 32-bit and MSVC builds. The change has no width-dependent arithmetic.

## Appendix: the scan loop, a possible follow-up

Not part of this change. The scan for plain bytes in `php_json_escape_string()` is inside a large loop body, and how the compilers build it depends on the rest of the function. Moving it into a small always-inline function that returns the length of the plain run, with a 256-byte lookup table instead of `ZEND_BIT_TEST` (the table that php-src #23682 adds), gives these cycles relative to master together with this change ([`scan-split-cycles.txt`](scan-split-cycles.txt), builds `*-slut`); output identical under the same checks:

| | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 |
|---|---:|---:|---:|---:|
| ASCII, 4 KiB | 0.59 | 0.54 | 0.53 | 0.53 |
| HTML | 0.70 | 0.63 | 1.01 | 1.02 |
| a quote every 16 bytes | 0.30 | 0.29 | 0.81 | 0.69 |
| a newline every 40 bytes | 0.39 | 0.31 | 0.67 | 0.63 |
| Cyrillic | 0.65 | 0.70 | 0.66 | 0.61 |
| CJK | 0.78 | 0.73 | 0.59 | 0.58 |
| a quote in every byte | 1.00 | 1.03 | 0.85 | 0.84 |
| 1,000 arrays of 10 fields | 0.89 | 0.92 | 0.97 | 0.91 |

Without the table the same split is slower on GCC 13 (1.27 on ASCII): there GCC compiles the bit test to `shr %cl` + `test` instead of `bt`.

## Reproduce

From the repository root, with php-src checked out next to it:

```sh
git -C ../php-src fetch https://github.com/ArtUkrainskiy/php-src.git json-utf8-2byte
E="--enable-werror --with-libxml --enable-xml"
BENCH_CONFIGURE_EXTRA="$E" ./bench build json-v3-base bd6c637d071
BENCH_CONFIGURE_EXTRA="$E" ./bench build json-v3c1 ca35c079a1f
# other compilers: the same with CC=gcc-14, CC=clang, CC=clang-20 and other build names
cd reports/json-encode-utf8-inline
./instructions.sh v3-base v3c1              # instructions per call, one line per case
./cycles.sh out.txt v3-base v3c1            # cycles, 3 alternating passes, prints ratios
for t in pairs triples positions udecode keys; do
  for b in v3-base v3c1; do echo "$b $t $(../../../php-builds/json-$b/sapi/cli/php -n $t.php | md5sum)"; done
done
../../../php-builds/json-v3c1/sapi/cli/php -n fuzz.php 200000 1   # compare with the same seed on v3-base
```

The scripts look for builds in `../php-builds/json-<name>` next to the repository, or in `$BENCH_BUILDS/json-<name>`.
