# json_encode(): decode common UTF-8 sequences inline

php-src change: [`ca35c079a1f`](https://github.com/ArtUkrainskiy/php-src/commit/ca35c079a1f) "ext/standard: Add php_next_utf8_char_inline()" on branch [`json-utf8-2byte`](https://github.com/ArtUkrainskiy/php-src/commits/json-utf8-2byte), on master [`bd6c637d071`](https://github.com/php/php-src/commit/bd6c637d071).

## Summary

`json_encode()`, `utf8_decode()` and the xml extension decode one character at a time with `php_next_utf8_char()`. This adds `php_next_utf8_char_inline()`, which decodes the common cases at the call site. Non-ASCII text in `json_encode()` gets faster with all six compiler and CPU combinations I tried: Cyrillic 0.73–0.80 of master's cycles, CJK 0.70–0.78. Two ASCII-heavy inputs are 10–14% slower with GCC 13 and 14 on the Intel machine; that does not reproduce with clang or on AMD (see Trade-offs).

ASCII runs the same instructions as master. With GCC 13 and 14 on the Intel machine, URLs and ASCII with an occasional escaped é are 10–14% slower in cycles; this does not reproduce with clang 18, clang 20 or on AMD, and it comes from code layout that a follow-up removes (see Trade-offs).

## What changes and why it is faster

**Before.** `php_next_utf8_char()` lives in `html.c`, so it cannot be inlined into ext/json. Inside it, `get_next_char()` handles 14 charsets and was not inlined either, so each character paid two calls and a `switch` on the charset, and the value, the new position and the status came back through memory: about 43 instructions per character in callgrind (36 in `get_next_char()`, 7 in the wrapper).

**After.** `php_next_utf8_char_inline()` in `ext/standard/html.h` has the same contract as `php_next_utf8_char()`. It decodes ASCII and valid two- and three-byte sequences without a call; everything else (four-byte characters, every invalid or truncated sequence) goes to `php_next_utf8_char()`, which is unchanged and still exported.

**Why the shortcut is exact.** A lead byte C2..DF followed by a continuation byte 80..BF is always a valid shortest-form character: C0 and C1 are the only overlong two-byte leads. For three bytes the inline path checks the same two conditions as `get_next_char()`: the result is at least U+0800 (not overlong) and outside U+D800..U+DFFF (not a surrogate). Any other input runs the old code, so which bytes are rejected or skipped and the returned status stay exactly as before.

`EXPECTED(c < 0xe0)` keeps the two-byte case on the straight path. Without it GCC 13 placed that case behind two extra taken jumps: Cyrillic ran the same instructions but took 20% more cycles.

## Trade-offs

- **Two inputs are slower with GCC 13 and 14 on the Intel machine:** URLs (1.10 and 1.14) and ASCII with an occasional é escaped as `\u00e9` (1.12 and 1.13). Neither shows with clang 18/20 or on AMD (URLs 1.01–1.06, the é input 0.90–0.96). The loop over plain bytes is byte-for-byte the same as in master, at the same address; what changes is the layout GCC picks for the path that handles a special character: the flush of the pending plain run moved out of line, which adds a taken jump per special character. Hinting that branch in the source moves the slowdown to other inputs (a quote every 16 bytes 1.23 with GCC, a quote in every byte 1.33 with clang). Splitting the scan out of the loop and using a byte table removes it (see the appendix of the report).
- **A newline every 40 bytes** is at 1.07 and 1.28 with GCC 13 and 14 in my builds, and at 0.97–1.02 when built with plain `-O2` instead of the aligned functions and loops I use: code placement.
- **An é exactly every 31 bytes** measures between 0.92 and 1.27 depending on compiler and, with clang 20, on the process: branch predictors learn the period of that input. With the é at random positions and the same density it is 0.87–0.96 with `JSON_UNESCAPED_UNICODE` on all six builds.
- **#24145** makes `get_next_char()` always inline, which also speeds up the out-of-line `php_next_utf8_char()`. On top of it this PR still removes 14–20% of the instructions on non-ASCII text, but with GCC 13 the cycles change less: Cyrillic 0.98, Cyrillic with `JSON_UNESCAPED_UNICODE` 0.79, CJK 0.88 of #24145's cycles. Both together: Cyrillic 0.80, CJK 0.78 of master. The two merge without conflicts.
- **API.** `php_next_utf8_char()` and its exported symbol are unchanged; `php_next_utf8_char_inline()` is new (UPGRADING.INTERNALS).
- **Other callers.** `utf8_decode()` (deprecated, still shipped) runs 2.2–2.8× fewer instructions on 4 KiB of Latin-1, Cyrillic or ASCII text. The xml extension's decoder uses the same path; not measured.
- **Size.** +768 bytes of code with GCC 13: `php_json_escape_string()` +351, `utf8_decode()` +224, the xml decoder +249.

## Machine and method

- i7-13700H laptop, Ubuntu 24.04, P-core 2 (`taskset -c 2`), governor powersave: GCC 13.3, GCC 14.2 (`CC=gcc-14`), clang 18.1 (`CC=clang`), clang 20.1 (`CC=clang-20`).
- Ryzen 9 5950X desktop, Ubuntu 26.04, core 6 (`taskset -c 6`), governor powersave: GCC 15.2 and clang 21.1, the distribution defaults.

Release builds from commits with `bench build` (`-O2 -g -falign-functions=64 -falign-loops=32`, `--enable-werror --with-libxml --enable-xml`).

Each number is per `json_encode()` call: `perf stat` over N calls minus the same process with 0 calls, divided by N. One series per machine on 2026-10-13: 5 alternating runs of master and the change for every row, 9 more for rows whose first 5 differed by more than 15%. Cycles rather than nanoseconds: the laptop heats up to 86–91 °C in long runs and its clock moves, while cycle counts stay within a few percent.

## Results

| input (4 KiB unless noted) | instructions | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | GCC 15.2 (AMD) | clang 21.1 (AMD) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Cyrillic | 0.74–0.78 | 0.80 | 0.75 | 0.73 | 0.79 | 0.73 | 0.75 |
| Cyrillic, `JSON_UNESCAPED_UNICODE` | 0.69–0.79 | 0.74 | 0.72 | 0.79 | 0.73 | 0.81 | 0.78 |
| CJK | 0.76–0.81 | 0.78 | 0.78 | 0.73 | 0.75 | 0.70 | 0.75 |
| CJK, `JSON_UNESCAPED_UNICODE` | 0.79–0.82 | 0.84 | 0.77 | 0.83 | 0.81 | 0.84 | 0.67 |
| French | 0.83–0.86 | 0.96 | 0.90 | 0.83 | 0.80 | 0.82 | 0.85 |
| French, `JSON_UNESCAPED_UNICODE` | 0.80–0.87 | 0.91 | 0.85 | 0.83 | 0.81 | 0.88 | 0.83 |
| ASCII with an é every 31 bytes on average | 0.93–0.94 | 1.12 | 1.13 | 0.90 | 0.92 | 0.95 | 0.96 |
| ASCII with an é every 31 bytes on average, `JSON_UNESCAPED_UNICODE` | 0.92–0.94 | 0.94 | 0.96 | 0.91 | 0.87 | 0.93 | 0.90 |
| ASCII with an é exactly every 31 bytes, `JSON_UNESCAPED_UNICODE` | 0.92–0.94 | 1.03 | 1.15 | 0.92 | 1.11 | 0.92 | 0.94 |
| ASCII, 16 bytes | 1.00 | 0.99 | 1.03 | 0.99 | 1.00 | 1.00 | 0.99 |
| ASCII, 256 bytes | 1.00 | 0.99 | 1.00 | 1.05 | 1.01 | 1.02 | 0.99 |
| ASCII, 4 KiB | 1.00 | 0.99 | 1.00 | 0.96 | 1.00 | 1.00 | 1.00 |
| ASCII, 64 KiB | 1.00 | 1.00 | 1.00 | 1.00 | 1.01 | 1.00 | 1.00 |
| HTML | 0.99–1.00 | 0.99 | 1.03 | 1.00 | 0.99 | 1.06 | 1.00 |
| URLs | 0.99–1.00 | 1.10 | 1.14 | 1.01 | 1.01 | 1.01 | 1.06 |
| URLs, `JSON_UNESCAPED_SLASHES` | 0.99–1.00 | 1.00 | 0.90 | 1.00 | 1.00 | 1.01 | 0.97 |
| a quote every 16 bytes | 1.00 | 0.84 | 0.82 | 0.99 | 0.99 | 1.00 | 1.00 |
| a quote every 8 bytes | 0.99–1.00 | 0.74 | 0.55 | 0.99 | 1.00 | 1.02 | 0.99 |
| a newline every 40 bytes | 1.00 | 1.07 | 1.28 | 1.00 | 1.00 | 1.04 | 1.00 |
| a quote in every byte | 1.00–1.02 | 0.99 | 1.01 | 1.00 | 1.00 | 0.91 | 1.00 |
| 1,000 arrays of 10 fields | 1.00 | 0.97 | 0.99 | 0.99 | 0.99 | 0.98 | 1.00 |
| 1,000 objects of 10 declared properties | 1.00 | 0.97 | 1.00 | 0.99 | 1.01 | 0.99 | 1.00 |
| an array with 100 keys | 1.00 | 0.96 | 0.99 | 1.00 | 1.01 | 0.98 | 1.00 |

Instructions per compiler, cycles and the spread between runs (the largest difference between runs of either build; rows above 5% are rough):

| case | GCC 13.3 instr. / cycles / spread | GCC 14.2 instr. / cycles / spread | clang 18.1 instr. / cycles / spread | clang 20.1 instr. / cycles / spread | GCC 15.2 instr. / cycles / spread | clang 21.1 instr. / cycles / spread |
|---|---:|---:|---:|---:|---:|---:|
| cyrillic-4k | 0.76 / 0.80 / 5% | 0.75 / 0.75 / 21% | 0.78 / 0.73 / 6% | 0.77 / 0.79 / 4% | 0.74 / 0.73 / 3% | 0.77 / 0.75 / 3% |
| cyrillic-4k-unescaped | 0.71 / 0.74 / 6% | 0.69 / 0.72 / 4% | 0.79 / 0.79 / 6% | 0.79 / 0.73 / 16% | 0.69 / 0.81 / 2% | 0.79 / 0.78 / 6% |
| cjk-4k | 0.78 / 0.78 / 2% | 0.77 / 0.78 / 9% | 0.81 / 0.73 / 8% | 0.80 / 0.75 / 4% | 0.76 / 0.70 / 2% | 0.80 / 0.75 / 1% |
| cjk-4k-unescaped | 0.81 / 0.84 / 2% | 0.79 / 0.77 / 10% | 0.82 / 0.83 / 9% | 0.81 / 0.81 / 8% | 0.80 / 0.84 / 2% | 0.81 / 0.67 / 1% |
| french-4k | 0.84 / 0.96 / 5% | 0.84 / 0.90 / 7% | 0.86 / 0.83 / 8% | 0.86 / 0.80 / 4% | 0.83 / 0.82 / 1% | 0.86 / 0.85 / 2% |
| french-4k-unescaped | 0.81 / 0.91 / 2% | 0.80 / 0.85 / 13% | 0.87 / 0.83 / 6% | 0.87 / 0.81 / 7% | 0.80 / 0.88 / 7% | 0.87 / 0.83 / 2% |
| ascii-random-utf8 | 0.94 / 1.12 / 8% | 0.94 / 1.13 / 2% | 0.94 / 0.90 / 5% | 0.94 / 0.92 / 4% | 0.93 / 0.95 / 6% | 0.94 / 0.96 / 4% |
| ascii-random-utf8-unescaped | 0.92 / 0.94 / 32% | 0.92 / 0.96 / 7% | 0.94 / 0.91 / 3% | 0.94 / 0.87 / 4% | 0.92 / 0.93 / 3% | 0.94 / 0.90 / 5% |
| ascii-rare-utf8-unescaped | 0.92 / 1.03 / 11% | 0.92 / 1.15 / 17% | 0.94 / 0.92 / 4% | 0.94 / 1.11 / 31% | 0.92 / 0.92 / 7% | 0.94 / 0.94 / 2% |
| ascii-16 | 1.00 / 0.99 / 4% | 1.00 / 1.03 / 2% | 1.00 / 0.99 / 5% | 1.00 / 1.00 / 9% | 1.00 / 1.00 / 3% | 1.00 / 0.99 / 8% |
| ascii-256 | 1.00 / 0.99 / 2% | 1.00 / 1.00 / 1% | 1.00 / 1.05 / 4% | 1.00 / 1.01 / 2% | 1.00 / 1.02 / 2% | 1.00 / 0.99 / 13% |
| ascii-4k | 1.00 / 0.99 / 7% | 1.00 / 1.00 / 2% | 1.00 / 0.96 / 5% | 1.00 / 1.00 / 5% | 1.00 / 1.00 / 2% | 1.00 / 1.00 / 1% |
| ascii-64k | 1.00 / 1.00 / 18% | 1.00 / 1.00 / 1% | 1.00 / 1.00 / 10% | 1.00 / 1.01 / 7% | 1.00 / 1.00 / 2% | 1.00 / 1.00 / 1% |
| html-4k | 0.99 / 0.99 / 6% | 1.00 / 1.03 / 7% | 1.00 / 1.00 / 35% | 1.00 / 0.99 / 54% | 1.00 / 1.06 / 11% | 1.00 / 1.00 / 2% |
| url-4k | 0.99 / 1.10 / 5% | 1.00 / 1.14 / 5% | 1.00 / 1.01 / 8% | 1.00 / 1.01 / 3% | 1.00 / 1.01 / 6% | 1.00 / 1.06 / 9% |
| url-4k-unescaped-slashes | 0.99 / 1.00 / 4% | 1.00 / 0.90 / 6% | 1.00 / 1.00 / 5% | 1.00 / 1.00 / 3% | 1.00 / 1.01 / 10% | 1.00 / 0.97 / 46% |
| esc-every-16 | 1.00 / 0.84 / 3% | 1.00 / 0.82 / 3% | 1.00 / 0.99 / 49% | 1.00 / 0.99 / 6% | 1.00 / 1.00 / 3% | 1.00 / 1.00 / 7% |
| esc-every-8 | 0.99 / 0.74 / 12% | 1.00 / 0.55 / 8% | 1.00 / 0.99 / 10% | 1.00 / 1.00 / 10% | 1.00 / 1.02 / 16% | 1.00 / 0.99 / 2% |
| newlines-every-40 | 1.00 / 1.07 / 13% | 1.00 / 1.28 / 35% | 1.00 / 1.00 / 4% | 1.00 / 1.00 / 99% | 1.00 / 1.04 / 7% | 1.00 / 1.00 / 1% |
| esc-every-byte | 1.00 / 0.99 / 4% | 1.02 / 1.01 / 4% | 1.00 / 1.00 / 4% | 1.00 / 1.00 / 2% | 1.02 / 0.91 / 2% | 1.00 / 1.00 / 2% |
| api-1000-records | 1.00 / 0.97 / 3% | 1.00 / 0.99 / 3% | 1.00 / 0.99 / 3% | 1.00 / 0.99 / 5% | 1.00 / 0.98 / 2% | 1.00 / 1.00 / 2% |
| objects-1000-records | 1.00 / 0.97 / 2% | 1.00 / 1.00 / 1% | 1.00 / 0.99 / 3% | 1.00 / 1.01 / 4% | 1.00 / 0.99 / 37% | 1.00 / 1.00 / 1% |
| object-100-keys | 1.00 / 0.96 / 2% | 1.00 / 0.99 / 4% | 1.00 / 1.00 / 13% | 1.00 / 1.01 / 9% | 1.00 / 0.98 / 4% | 1.00 / 1.00 / 3% |

Cases are defined in [`cases.php`](cases.php), 4 KiB strings unless the name says otherwise. Raw data: [`cycles.txt`](cycles.txt), one line per run: `<compiler> <base|change> <case> <cycles per call> <instructions per call>`.

## Output verification

Against master, byte for byte and including `json_last_error()`, with all six compiler and CPU combinations and on a GCC debug build with ASan and UBSan (`--enable-debug --enable-address-sanitizer --enable-undefined-sanitizer`, `USE_ZEND_ALLOC=0`), where no sanitizer report appeared:

- [`pairs.php`](pairs.php): every pair of bytes, alone, inside ASCII and after 20 ASCII bytes, six flag sets;
- [`triples.php`](triples.php): every three-byte sequence with an E0..EF lead byte, alone and inside ASCII, six flag sets;
- [`positions.php`](positions.php): every byte value at every position of ASCII strings 1–24 bytes long, four flag sets;
- [`fuzz.php`](fuzz.php): 1,000,000 random strings (5 seeds × 200,000) of 0–300 bytes, as values and as keys, 11 flag sets;
- [`keys.php`](keys.php): literal keys, also ones that need escaping, through arrays, `stdClass` and declared properties, 10 flag sets;
- [`udecode.php`](udecode.php): `utf8_decode()` on all pairs and E0..EF triples;
- php-src tests `ext/json`, `ext/xml`, `ext/standard/tests/strings`: 838 passed on each Intel build, 833 on the sanitizer build, none failed.

The new test `json_encode_utf8_sequences.phpt` fails if the overlong checks of the inline path are removed. A separate review compared the inline decoder with `get_next_char(cs_utf_8)` on every three-byte prefix, buffer lengths 0–6 and start cursors 0 and 1 (285 million calls): no difference in value, cursor or status.

## Not tested

aarch64, 32-bit and MSVC builds. The change has no width-dependent arithmetic.

## Appendix: the scan loop, a possible follow-up

Not part of this change. The scan for plain bytes in `php_json_escape_string()` is inside a large loop body, and how the compilers build it depends on the rest of the function. Moving it into a small always-inline function that returns the length of the plain run, with a 256-byte lookup table instead of `ZEND_BIT_TEST` (the table that php-src #23682 adds), gives these cycles relative to master together with this change ([`scan-split-cycles.txt`](scan-split-cycles.txt), [`scan-split-random-cycles.txt`](scan-split-random-cycles.txt), builds `*-slut`); output identical under the same checks. It also removes the GCC slowdowns described under Trade-offs:

| | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 |
|---|---:|---:|---:|---:|
| ASCII, 4 KiB | 0.59 | 0.54 | 0.53 | 0.53 |
| HTML | 0.70 | 0.63 | 1.01 | 1.02 |
| URLs | 0.78 | 0.78 | 1.01 | 1.05 |
| ASCII with an é every 31 bytes on average | 0.31 | 0.31 | 0.69 | 0.59 |
| ASCII with an é every 31 bytes on average, `JSON_UNESCAPED_UNICODE` | 0.34 | 0.34 | 0.78 | 0.60 |
| a newline every 40 bytes | 0.39 | 0.34 | 0.67 | 0.62 |
| Cyrillic | 0.65 | 0.70 | 0.66 | 0.61 |
| CJK | 0.78 | 0.73 | 0.59 | 0.58 |
| a quote in every byte | 1.01 | 1.01 | 0.84 | 0.85 |
| 1,000 arrays of 10 fields | 0.89 | 0.92 | 0.97 | 0.91 |

Without the table the same split is slower on GCC 13 (1.27 on ASCII): there GCC compiles the bit test to `shr %cl` + `test` instead of `bt`. Every other change to the loop I tried (hints, a different loop exit, a loop over consecutive non-ASCII characters) moved slowdowns between inputs and compilers; the table is the part that makes the result independent of the compiler. php-src #23682 adds such a table, so this follow-up would use it.

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
