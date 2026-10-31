# json_encode(): decode valid UTF-8 inline

php-src change: [`63792a2d9f5`](https://github.com/ArtUkrainskiy/php-src/commit/63792a2d9f5) "ext/standard: Add php_next_utf8_char_inline()" on branch [`json-utf8-2byte`](https://github.com/ArtUkrainskiy/php-src/commits/json-utf8-2byte), on master [`bd6c637d071`](https://github.com/php/php-src/commit/bd6c637d071). php-src PR: [#24283](https://github.com/php/php-src/pull/24283).

The first version of the PR (`ca35c079a1f`) decoded two- and three-byte sequences only; four-byte characters went through the inline checks and then the old call, which made emoji 2–13% slower than master. The current version also decodes four-byte sequences inline. Raw data of the first version: [`cycles-two-three-byte.txt`](cycles-two-three-byte.txt).

## Summary

`json_encode()`, `utf8_decode()` and the xml extension decode one character at a time with `php_next_utf8_char()`. This adds `php_next_utf8_char_inline()`, which decodes valid UTF-8 at the call site and keeps the existing function as the fallback for invalid input and as the exported API.

Non-ASCII text in `json_encode()` gets faster across all six compiler/CPU configurations tested: Cyrillic takes 0.70–0.91 of master's cycles, CJK 0.68–0.84 and emoji 0.82–0.89. With GCC 13 and 14 on the Intel machine some ASCII-heavy inputs get slower at the same instruction count, from code placement; see Trade-offs.

## What changes and why it is faster

**Before.** `php_next_utf8_char()` lives in `html.c`, so it cannot be inlined into ext/json. Inside it, `get_next_char()` handles 14 charsets and was not inlined either, so each character paid two calls and a `switch` on the charset, and the value, the new position and the status came back through memory: about 43 instructions per non-ASCII character in callgrind (36 in `get_next_char()`, 7 in the wrapper).

**After.** `php_next_utf8_char_inline()` in `ext/standard/html.h` has the same contract as `php_next_utf8_char()`. It decodes ASCII and valid two-, three- and four-byte sequences without a call; every invalid or truncated sequence goes to `php_next_utf8_char()`, which is unchanged and still exported.

**Why the shortcut is exact.** A lead byte C2..DF followed by a continuation byte 80..BF is always a valid shortest-form character: C0 and C1 are the only overlong two-byte leads. For three bytes the inline path checks the same two conditions as `get_next_char()`: the result is at least U+0800 (not overlong) and outside U+D800..U+DFFF (not a surrogate). For four bytes it takes lead bytes F0..F4 only and checks that the result is in U+10000..U+10FFFF, as `get_next_char()` does. Any other input runs the old code, so which bytes are rejected or skipped and the returned status stay exactly as before.

`EXPECTED(c < 0xe0)` keeps the two-byte case on the straight path. Without it GCC 13 placed that case behind two extra taken jumps: Cyrillic ran the same instructions but took 20% more cycles.

## Trade-offs

- **Code placement with GCC 13 and 14 on the Intel machine.** Some inputs run the same instructions as master but take more cycles: a newline every 40 bytes (1.20 and 1.18), URLs (1.09 and 1.15), ASCII with an occasional é escaped as `\u00e9` (1.10 and 1.13), and with GCC 13 also 1,000 arrays (1.10), 1,000 objects (1.07) and English text with an emoji every few words (1.05, at 0.92 of the instructions). With clang 18 and 20 and on AMD these inputs are at 0.91–1.02. The generated loop over plain bytes is identical to master's and at the same address (objdump, GCC 13). `php_json_escape_string()` grows by 487 bytes, so `php_json_encode_zval()` and `php_json_encode_array()`, which follow it, move by 192 bytes; on the 1,000 arrays branch mispredictions go from 1.0 to 3.6–3.9 million per 3,000 calls, at every hot branch, including code this PR does not touch. Hinting branches in the source moved slowdowns of this kind to other inputs when I tried it on an earlier version. Splitting the scan out of the loop and using a byte table removed them for the two- and three-byte version (see the appendix).
- **An é exactly every 31 bytes** measured between 0.92 and 1.27 on the earlier version depending on compiler and process, consistent with the branch predictor learning the periodic pattern. The table uses é at random positions with the same density.
- **#24145** makes `get_next_char()` always inline, which also speeds up the out-of-line `php_next_utf8_char()`. Measured with the two- and three-byte version: on top of #24145 this PR still removes 14–20% of the instructions on non-ASCII text, but with GCC 13 the cycles change less (Cyrillic 0.98, Cyrillic with `JSON_UNESCAPED_UNICODE` 0.79, CJK 0.88 of #24145's cycles). The two merge without conflicts.
- **API.** `php_next_utf8_char()` and its exported symbol are unchanged; `php_next_utf8_char_inline()` is new (UPGRADING.INTERNALS).
- **Other callers.** `utf8_decode()` (deprecated, still shipped) runs 1.7–2.8× fewer instructions on 4 KiB of Latin-1, Cyrillic or ASCII text (GCC 13). The xml extension's decoder uses the same path; not measured.
- **Size.** +1,296 bytes of code with GCC 13: `php_json_escape_string()` +487, `utf8_decode()` +384, the xml decoder +425.

## Machine and method

- i7-13700H laptop, Ubuntu 24.04, P-core 2 (`taskset -c 2`), governor powersave: GCC 13.3, GCC 14.2 (`CC=gcc-14`), clang 18.1 (`CC=clang`), clang 20.1 (`CC=clang-20`).
- Ryzen 9 5950X desktop, Ubuntu 26.04, core 15 (`taskset -c 15`), governor powersave: GCC 15.2 and clang 21.1, the distribution defaults. Other load ran on the machine during the series, mostly on the other CCD; master measured against itself on core 15 stayed within 2% in medians, single runs within 19%.

Release builds from commits with `bench build` (`-O2 -g -falign-functions=64 -falign-loops=32`, `--enable-werror --with-libxml --enable-xml`).

Each number is per `json_encode()` call: `perf stat` over N calls minus the same process with 0 calls, divided by N. One series per machine on 2026-10-13: 5 alternating runs of master and the change for every row on the Intel machine, 15 on AMD. Cycles rather than nanoseconds: the laptop heats up in long runs and its clock moves, while cycle counts stay within a few percent.

## Results

Relative to master, lower is better. Release builds (`-O2`, x86-64, `--enable-werror`): GCC 13.3, GCC 14.2, clang 18.1 and clang 20.1 on an i7-13700H pinned to one P-core; GCC 15.2 and clang 21.1 on a Ryzen 9 5950X pinned to one core. Cycles and instructions per call from `perf stat` over N calls minus the same process with 0 calls; cycles are the median of alternating runs from one series per machine, 5 per row on the Intel machine and 15 on AMD, where other load was running on other cores (master against itself: medians within 2%). Instructions are given as a range over the six builds.

| input (4 KiB unless noted) | instructions | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | GCC 15.2 (AMD) | clang 21.1 (AMD) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Cyrillic | 0.74–0.77 | 0.72 | 0.79 | 0.76 | 0.91 | 0.70 | 0.80 |
| Cyrillic, `JSON_UNESCAPED_UNICODE` | 0.69–0.79 | 0.64 | 0.70 | 0.69 | 0.70 | 0.82 | 0.71 |
| CJK | 0.77–0.81 | 0.78 | 0.78 | 0.72 | 0.84 | 0.68 | 0.83 |
| CJK, `JSON_UNESCAPED_UNICODE` | 0.79–0.82 | 0.80 | 0.79 | 0.80 | 0.83 | 0.81 | 0.73 |
| French | 0.83–0.86 | 0.95 | 0.94 | 0.79 | 0.86 | 0.82 | 0.87 |
| French, `JSON_UNESCAPED_UNICODE` | 0.80–0.87 | 0.85 | 0.84 | 0.78 | 0.79 | 0.88 | 0.83 |
| emoji | 0.82–0.86 | 0.82 | 0.87 | 0.83 | 0.83 | 0.89 | 0.84 |
| emoji, `JSON_UNESCAPED_UNICODE` | 0.75–0.83 | 0.75 | 0.76 | 0.83 | 0.85 | 0.75 | 0.72 |
| English text with an emoji every few words | 0.92–0.94 | 1.05 | 0.96 | 0.91 | 0.91 | 0.97 | 0.94 |
| ASCII with an é every 31 bytes on average | 0.93–0.94 | 1.10 | 1.13 | 0.91 | 0.93 | 0.96 | 0.95 |
| ASCII with an é every 31 bytes on average, `JSON_UNESCAPED_UNICODE` | 0.92–0.94 | 0.96 | 0.96 | 0.93 | 0.90 | 0.94 | 0.92 |
| ASCII, 16 bytes | 1.00 | 1.00 | 1.00 | 1.01 | 1.00 | 1.00 | 1.04 |
| ASCII, 4 KiB | 1.00 | 1.01 | 1.00 | 1.00 | 0.99 | 1.01 | 0.99 |
| HTML | 0.99–1.00 | 1.00 | 1.05 | 0.98 | 0.99 | 1.05 | 1.00 |
| URLs | 0.99–1.00 | 1.09 | 1.15 | 0.99 | 1.00 | 0.99 | 1.00 |
| a quote every 16 bytes | 1.00 | 0.83 | 0.82 | 1.00 | 1.01 | 1.01 | 1.02 |
| a newline every 40 bytes | 1.00 | 1.20 | 1.18 | 1.00 | 1.00 | 1.00 | 1.02 |
| a quote in every byte | 1.00–1.02 | 1.00 | 1.00 | 1.00 | 1.00 | 0.92 | 1.00 |
| 1,000 arrays of 10 fields | 1.00 | 1.10 | 1.00 | 1.01 | 1.00 | 0.99 | 0.99 |
| 1,000 objects of 10 declared properties | 1.00 | 1.07 | 0.97 | 1.02 | 1.00 | 1.02 | 0.99 |

All 26 cases, with the spread between runs (largest (max − min) / median of master's or the change's runs):

| case | GCC 13.3 instr. / cycles / spread | GCC 14.2 instr. / cycles / spread | clang 18.1 instr. / cycles / spread | clang 20.1 instr. / cycles / spread | GCC 15.2 (AMD) instr. / cycles / spread | clang 21.1 (AMD) instr. / cycles / spread |
|---|---:|---:|---:|---:|---:|---:|
| cyrillic-4k | 0.75 / 0.72 / 9% | 0.75 / 0.79 / 2% | 0.77 / 0.76 / 6% | 0.77 / 0.91 / 4% | 0.74 / 0.70 / 61% | 0.77 / 0.80 / 20% |
| cyrillic-4k-unescaped | 0.69 / 0.64 / 3% | 0.69 / 0.70 / 2% | 0.79 / 0.69 / 2% | 0.79 / 0.70 / 2% | 0.69 / 0.82 / 22% | 0.79 / 0.71 / 14% |
| cjk-4k | 0.78 / 0.78 / 1% | 0.79 / 0.78 / 1% | 0.81 / 0.72 / 4% | 0.81 / 0.84 / 5% | 0.77 / 0.68 / 22% | 0.81 / 0.83 / 16% |
| cjk-4k-unescaped | 0.80 / 0.80 / 1% | 0.79 / 0.79 / 2% | 0.82 / 0.80 / 4% | 0.81 / 0.83 / 2% | 0.80 / 0.81 / 12% | 0.81 / 0.73 / 15% |
| french-4k | 0.84 / 0.95 / 4% | 0.84 / 0.94 / 1% | 0.86 / 0.79 / 1% | 0.86 / 0.86 / 3% | 0.83 / 0.82 / 37% | 0.86 / 0.87 / 38% |
| french-4k-unescaped | 0.80 / 0.85 / 3% | 0.80 / 0.84 / 7% | 0.87 / 0.78 / 3% | 0.87 / 0.79 / 1% | 0.80 / 0.88 / 23% | 0.87 / 0.83 / 27% |
| emoji-4k | 0.82 / 0.82 / 3% | 0.85 / 0.87 / 30% | 0.85 / 0.83 / 2% | 0.86 / 0.83 / 1% | 0.85 / 0.89 / 85% | 0.86 / 0.84 / 12% |
| emoji-4k-unescaped | 0.75 / 0.75 / 3% | 0.77 / 0.76 / 1% | 0.82 / 0.83 / 4% | 0.83 / 0.85 / 2% | 0.78 / 0.75 / 62% | 0.83 / 0.72 / 22% |
| emoji-text-4k | 0.92 / 1.05 / 8% | 0.93 / 0.96 / 3% | 0.93 / 0.91 / 2% | 0.94 / 0.91 / 1% | 0.93 / 0.97 / 25% | 0.94 / 0.94 / 38% |
| ascii-random-utf8 | 0.94 / 1.10 / 11% | 0.94 / 1.13 / 4% | 0.94 / 0.91 / 6% | 0.94 / 0.93 / 2% | 0.93 / 0.96 / 18% | 0.94 / 0.95 / 9% |
| ascii-random-utf8-unescaped | 0.92 / 0.96 / 13% | 0.92 / 0.96 / 5% | 0.94 / 0.93 / 2% | 0.94 / 0.90 / 11% | 0.92 / 0.94 / 16% | 0.94 / 0.92 / 14% |
| ascii-rare-utf8-unescaped | 0.92 / 1.08 / 10% | 0.92 / 1.05 / 21% | 0.94 / 0.98 / 7% | 0.94 / 0.92 / 6% | 0.92 / 0.94 / 15% | 0.94 / 0.92 / 18% |
| ascii-16 | 1.00 / 1.00 / 9% | 1.00 / 1.00 / 2% | 1.00 / 1.01 / 3% | 1.00 / 1.00 / 1% | 1.00 / 1.00 / 21% | 1.00 / 1.04 / 28% |
| ascii-256 | 1.00 / 1.00 / 1% | 1.00 / 0.99 / 1% | 1.00 / 0.99 / 1% | 1.00 / 1.02 / 2% | 1.00 / 0.99 / 19% | 1.00 / 0.96 / 14% |
| ascii-4k | 1.00 / 1.01 / 12% | 1.00 / 1.00 / 2% | 1.00 / 1.00 / 1% | 1.00 / 0.99 / 2% | 1.00 / 1.01 / 15% | 1.00 / 0.99 / 6% |
| ascii-64k | 1.00 / 1.00 / 1% | 1.00 / 1.01 / 2% | 1.00 / 0.99 / 2% | 1.00 / 1.00 / 3% | 1.00 / 0.98 / 18% | 1.00 / 1.01 / 27% |
| html-4k | 0.99 / 1.00 / 4% | 1.00 / 1.05 / 3% | 1.00 / 0.98 / 3% | 1.00 / 0.99 / 2% | 1.00 / 1.05 / 12% | 1.00 / 1.00 / 51% |
| url-4k | 0.99 / 1.09 / 2% | 1.00 / 1.15 / 3% | 1.00 / 0.99 / 3% | 1.00 / 1.00 / 4% | 1.00 / 0.99 / 135% | 1.00 / 1.00 / 15% |
| url-4k-unescaped-slashes | 0.99 / 1.03 / 2% | 1.00 / 0.91 / 6% | 1.00 / 0.98 / 6% | 1.00 / 0.97 / 108% | 1.00 / 1.08 / 60% | 1.00 / 0.95 / 44% |
| esc-every-16 | 1.00 / 0.83 / 4% | 1.00 / 0.82 / 16% | 1.00 / 1.00 / 1% | 1.00 / 1.01 / 1% | 1.00 / 1.01 / 19% | 1.00 / 1.02 / 18% |
| esc-every-8 | 0.99 / 0.76 / 21% | 1.00 / 0.55 / 4% | 1.00 / 1.00 / 2% | 1.00 / 1.00 / 2% | 1.00 / 1.05 / 13% | 1.00 / 1.00 / 17% |
| newlines-every-40 | 1.00 / 1.20 / 18% | 1.00 / 1.18 / 16% | 1.00 / 1.00 / 2% | 1.00 / 1.00 / 1% | 1.00 / 1.00 / 23% | 1.00 / 1.02 / 11% |
| esc-every-byte | 1.00 / 1.00 / 4% | 1.02 / 1.00 / 1% | 1.00 / 1.00 / 1% | 1.00 / 1.00 / 2% | 1.02 / 0.92 / 15% | 1.00 / 1.00 / 25% |
| api-1000-records | 1.00 / 1.10 / 55% | 1.00 / 1.00 / 2% | 1.00 / 1.01 / 1% | 1.00 / 1.00 / 1% | 1.00 / 0.99 / 9% | 1.00 / 0.99 / 13% |
| objects-1000-records | 1.00 / 1.07 / 3% | 1.00 / 0.97 / 6% | 1.00 / 1.02 / 3% | 1.00 / 1.00 / 4% | 1.00 / 1.02 / 16% | 1.00 / 0.99 / 10% |
| object-100-keys | 1.00 / 1.00 / 3% | 1.00 / 0.99 / 5% | 1.00 / 1.01 / 1% | 1.00 / 0.99 / 1% | 1.00 / 0.99 / 41% | 1.00 / 1.01 / 33% |

Cases are defined in [`cases.php`](cases.php), 4 KiB strings unless the name says otherwise. Raw data: [`cycles.txt`](cycles.txt), one line per run: `<compiler> <base|change> <case> <cycles per call> <instructions per call>`.

## Output verification

Against master, byte for byte and including `json_last_error()`, with all six compiler and CPU combinations and on a GCC debug build with ASan and UBSan (`--enable-debug --enable-address-sanitizer --enable-undefined-sanitizer`, `USE_ZEND_ALLOC=0`), where no sanitizer report appeared:

- [`pairs.php`](pairs.php): every pair of bytes, alone, inside ASCII and after 20 ASCII bytes, six flag sets;
- [`triples.php`](triples.php): every three-byte sequence with an E0..EF lead byte, alone and inside ASCII, six flag sets;
- [`quads.php`](quads.php): every four-byte sequence with an F0..FF lead byte, every second and third byte, the fourth byte at the continuation boundaries, alone, inside ASCII and truncated, three flag sets;
- [`positions.php`](positions.php): every byte value at every position of ASCII strings 1–24 bytes long, four flag sets;
- [`fuzz.php`](fuzz.php): random strings of 0–300 bytes, as values and as keys, 11 flag sets: 200,000 per Intel build and on the sanitizer build, 400,000 per AMD build;
- [`keys.php`](keys.php): literal keys, also ones that need escaping, through arrays, `stdClass` and declared properties, 10 flag sets;
- [`udecode.php`](udecode.php): `utf8_decode()` on all pairs and E0..EF triples;
- php-src tests `ext/json`, `ext/xml`, `ext/standard/tests/strings` pass on each Intel build and on the sanitizer build (833 passed there, none failed).

[`decoder-cmp/gen.py`](decoder-cmp/gen.py) builds a C program that compares `php_next_utf8_char_inline()` from `html.h` with the UTF-8 case of `get_next_char()` extracted from `html.c`: every sequence of one to four bytes with a lead byte 80..FF at every prefix length, at cursor 0 and after one ASCII byte, and every ASCII byte, 4.3 billion calls. No difference in value, cursor or status; with either range check of the four-byte path removed it reports differences. The new test `json_encode_utf8_sequences.phpt` fails if the overlong checks of the two- and three-byte paths are removed.

## Not tested

aarch64, 32-bit and MSVC builds. The change has no width-dependent arithmetic.

## Appendix: the scan loop, a possible follow-up

Not part of this change. The scan for plain bytes in `php_json_escape_string()` is inside a large loop body, and how the compilers build it depends on the rest of the function. Moving it into a small always-inline function that returns the length of the plain run, with a 256-byte lookup table instead of `ZEND_BIT_TEST` (the table that php-src #23682 adds), gave these cycles relative to master together with the earlier two- and three-byte version of this change ([`scan-split-cycles.txt`](scan-split-cycles.txt), [`scan-split-random-cycles.txt`](scan-split-random-cycles.txt), builds `*-slut`); output identical under the same checks. It removed the GCC slowdowns of that version:

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
BENCH_CONFIGURE_EXTRA="$E" ./bench build json-c4b 63792a2d9f5
# other compilers: the same with CC=gcc-14, CC=clang, CC=clang-20 and other build names
cd reports/json-encode-utf8-inline
./instructions.sh v3-base c4b              # instructions per call, one line per case
./cycles.sh out.txt v3-base c4b            # cycles, 3 alternating passes, prints ratios
for t in pairs triples quads positions udecode keys; do
  for b in v3-base c4b; do echo "$b $t $(../../../php-builds/json-$b/sapi/cli/php -n $t.php | md5sum)"; done
done
../../../php-builds/json-c4b/sapi/cli/php -n fuzz.php 200000 1   # compare with the same seed on v3-base
python3 decoder-cmp/gen.py ../../../php-src > /tmp/cmp.c && cc -O2 -o /tmp/cmp /tmp/cmp.c && /tmp/cmp
```

The scripts look for builds in `../php-builds/json-<name>` next to the repository, or in `$BENCH_BUILDS/json-<name>`.
