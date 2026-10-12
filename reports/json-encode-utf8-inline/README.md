# json_encode(): inline UTF-8 decoding, scan position in a register

php-src change: branch [`json-utf8-2byte`](https://github.com/ArtUkrainskiy/php-src/commits/json-utf8-2byte), two commits on master [`bd6c637d071`](https://github.com/php/php-src/commit/bd6c637d071):

1. [`ca35c079a1f`](https://github.com/ArtUkrainskiy/php-src/commit/ca35c079a1f) "ext/standard: Add php_next_utf8_char_inline()".
2. [`9813f798db9`](https://github.com/ArtUkrainskiy/php-src/commit/9813f798db9) "ext/json: Keep the scan position of json_encode() in a register".

## Summary

The change has two parts: common UTF-8 is decoded inline instead of through two out-of-line calls, and `json_encode()`'s scan position stops being kept in memory.

With GCC 13, relative to master: Cyrillic 0.63 of the cycles, CJK 0.78, French 0.70, HTML 0.57, a quote every 16 bytes 0.44, ASCII 0.89–0.93, 1,000 records 0.94. Slower: a string in which every byte needs escaping, 1.08. With clang 18 the UTF-8 gain is the same, the ASCII gain is not there, and commit 2 is a trade-off. Output does not change.

## What changes and why it is faster

### 1. Common UTF-8 is decoded inline

**Before.** Every non-ASCII character in `json_encode()` went through two calls. `php_next_utf8_char()` lives in `html.c`, so it cannot be inlined into ext/json. Inside it, `get_next_char()` handles 14 charsets and was not inlined either, so each character also paid a `switch` on the charset, and the value, the new position and the status came back through memory. That is about 43 instructions per character (callgrind: 36 in `get_next_char()`, 7 in the wrapper).

**After.** A new static inline function, `php_next_utf8_char_inline()` in `ext/standard/html.h`, has the same contract as `php_next_utf8_char()`. At the call site it decodes ASCII and valid two- and three-byte sequences, with no call. Everything else (four-byte characters, every invalid or truncated sequence) goes to `php_next_utf8_char()`, which is unchanged and still exported. `json_encode()`, `utf8_decode()` and the xml extension's decoder use the new function.

**Why the shortcut is exact.** A lead byte C2..DF followed by a continuation byte 80..BF is always a valid shortest-form character: C0 and C1 are the only overlong two-byte leads. For three bytes the inline path checks the same two conditions as `get_next_char()`: the result is at least U+0800 (not overlong) and outside U+D800..U+DFFF (not a surrogate). Any other input runs the old code, so which bytes are rejected or skipped and the returned status stay exactly as before.

**Code layout.** `EXPECTED(c < 0xe0)` keeps the two-byte case on the straight path. Without it GCC 13 placed that case behind two extra taken jumps: Cyrillic ran the same instructions but took 20% more cycles.

### 2. `pos` moves from the stack to a register

`pos` is the length of the current run of bytes that need no escaping; the scan loop adds 1 for every such byte.

**Before.** `&pos` was passed to the UTF-8 decoder (after commit 1 it still reaches the out-of-line `php_next_utf8_char()`). A variable whose address goes to a function the compiler cannot see must have a place in memory. GCC kept `pos` in a stack slot for the whole function: the loop over plain bytes stored `pos` and loaded it back on every byte, and the address of the next byte depended on that load:

    add  $1, %rdx            ; pos++
    mov  %rdx, 0x38(%rsp)    ; store pos to the stack
    ...
    mov  0x38(%rsp), %rdx    ; load it back
    movzbl (%r14,%rdx), %ecx ; next byte

**After.** The decoder writes the character length into a separate local, `char_len`. Nothing takes the address of `pos` any more, so it stays in a register: 11 instructions per plain byte instead of 12, and no memory round trip on the path from one byte to the next. With GCC the gain is largest where runs of plain bytes are short and broken by escapes (HTML 0.57, a quote every 16 bytes 0.44 of master's cycles), smaller on long clean ASCII (0.89).

## Trade-offs

- **Slower with GCC:** a string in which every byte needs escaping, 1.08× cycles and +2 instructions per escaped byte. On the way back into the loop the compiler now resets the `pos` register to 0 and takes an extra jump, where master reloaded `pos` from the stack.
- **The commits are a pair.** Commit 1 brings the UTF-8 gain, commit 2 the ASCII and escape gain. With GCC, commit 2 alone makes Cyrillic 10% slower (measured on cd383dcc377). Commit 1 does not change the executed instructions for ASCII input; the cycle differences there are code-layout noise.
- **clang 18.** Commit 1 gives the same UTF-8 gain (Cyrillic 0.75, CJK 0.73 of clang master's cycles). Commit 2 matters less: clang already keeps the loop counter in a register and only stores `pos` on every byte without loading it back, so there is no load on the byte-to-byte path to remove. Commit 2 drops the store (8% fewer instructions on ASCII) without changing ASCII cycles; a string with every byte escaped goes to 0.85, while Cyrillic and 1,000 arrays lose 6% and 3% against commit 1 alone.
- **API.** `php_next_utf8_char()` and its exported symbol are unchanged. `php_next_utf8_char_inline()` is new; noted in UPGRADING.INTERNALS.
- **Other callers.** `utf8_decode()` (deprecated, still shipped) runs 2.2–2.8× fewer instructions on 4 KiB of Latin-1, Cyrillic or ASCII text. The xml extension's decoder uses the same path; not measured.
- **Size.** +704 bytes of code with GCC: `php_json_escape_string()` +260, `utf8_decode()` +224, the xml decoder +249.

## Machine and method

i7-13700H laptop, P-core 2 (`taskset -c 2`), governor powersave. Release builds from commits with `bench build` (`-O2 -g -falign-functions=64 -falign-loops=32`, `--enable-werror --with-libxml --enable-xml`), GCC 13.3 and clang 18.1.3 (`CC=clang`).

Each number is per `json_encode()` call: `perf stat` (`cpu_core` counters) over N calls minus the same process with 0 calls, divided by N. Cycles are the median over alternating runs: 3, then 5 more for rows whose first 3 differed by more than 5%. Cycles rather than nanoseconds: the laptop heats up to 86–91 °C in long runs and its clock moves, while cycle counts stay within a few percent.

Builds in the data files: `v3-base` = master `bd6c637d071`, `v3c1` = commit 1, `v3` = both commits; `clang-base`, `clang-c1`, `clang-v3` the same with clang.

## Results with GCC 13.3

Spread: the largest difference between runs of either build; rows above 5% are rough. Instructions are not affected by it.

| case | master instructions | master cycles | commit 1: instr. / cycles | both: instr. / cycles | spread | runs |
|---|---:|---:|---:|---:|---:|---:|
| ascii-16 | 766 | 142 | 1.00 / 0.94 | 0.98 / 0.89 | 6% | 3 |
| ascii-256 | 3,918 | 700 | 1.00 / 0.99 | 0.93 / 0.93 | 2% | 3 |
| ascii-4k | 49,876 | 8,596 | 1.00 / 1.00 | 0.92 / 0.89 | 3% | 3 |
| ascii-64k | 787,375 | 138,058 | 1.00 / 0.99 | 0.92 / 0.89 | 4% | 3 |
| html-4k | 83,386 | 29,221 | 0.99 / 1.01 | 0.98 / 0.57 | 6% | 3 |
| url-4k | 91,039 | 27,452 | 0.99 / 1.14 | 0.98 / 0.71 | 55% | 8 |
| url-4k-unescaped-slashes | 89,473 | 30,210 | 0.99 / 0.98 | 0.98 / 0.55 | 1% | 3 |
| esc-every-16 | 65,004 | 24,697 | 1.00 / 0.84 | 0.95 / 0.44 | 6% | 3 |
| esc-every-8 | 81,135 | 19,796 | 0.99 / 0.75 | 0.97 / 0.64 | 14% | 8 |
| esc-every-byte | 165,046 | 23,321 | 1.00 / 1.00 | 1.05 / 1.08 | 12% | 8 |
| newlines-every-40 | 55,593 | 15,502 | 1.00 / 1.12 | 0.93 / 0.61 | 4% | 3 |
| cyrillic-4k | 224,770 | 38,507 | 0.76 / 0.80 | 0.71 / 0.63 | 3% | 3 |
| cyrillic-4k-unescaped | 239,185 | 59,156 | 0.71 / 0.73 | 0.67 / 0.66 | 1% | 3 |
| cjk-4k | 170,494 | 25,259 | 0.78 / 0.79 | 0.74 / 0.78 | 12% | 8 |
| cjk-4k-unescaped | 180,892 | 26,352 | 0.81 / 0.86 | 0.76 / 0.80 | 3% | 3 |
| french-4k | 126,516 | 25,164 | 0.84 / 0.97 | 0.80 / 0.70 | 5% | 3 |
| french-4k-unescaped | 131,625 | 29,184 | 0.81 / 0.91 | 0.77 / 0.80 | 13% | 8 |
| ascii-rare-utf8-unescaped | 65,720 | 19,985 | 0.92 / 1.02 | 0.86 / 0.53 | 6% | 3 |
| api-1000-records | 4,850,224 | 900,022 | 1.00 / 0.98 | 0.97 / 0.94 | 7% | 3 |
| objects-1000-records | 4,684,610 | 857,853 | 1.00 / 0.99 | 0.97 / 0.94 | 2% | 3 |
| object-100-keys | 36,710 | 7,090 | 1.00 / 0.95 | 0.98 / 0.91 | 82% | 8 |

Cases are defined in [`cases.php`](cases.php), 4 KiB strings unless the name says otherwise. Raw data: [`cycles.txt`](cycles.txt) (`<build> <case> <cycles per call>`), [`instructions.txt`](instructions.txt) (`<case> <v3-base> <v3c1> <v3>`).

## Results with clang 18.1.3

Relative to master built with clang. Raw data: [`cycles-clang.txt`](cycles-clang.txt), [`instructions-clang.txt`](instructions-clang.txt).

| Вход | коммит 1, такты | оба, такты | оба, инструкции |
|---|---:|---:|---:|
| ascii-16 | 1.01 | 0.99 | 0.97 |
| ascii-256 | 1.06 | 1.06 | 0.93 |
| ascii-4k | 0.96 | 1.00 | 0.92 |
| ascii-64k | 0.99 | 1.01 | 0.92 |
| html-4k | 1.00 | 1.02 | 0.92 |
| url-4k | 1.00 | 1.00 | 0.92 |
| url-4k-unescaped-slashes | 1.00 | 0.96 | 0.92 |
| esc-every-16 | 1.00 | 1.00 | 0.92 |
| esc-every-8 | 1.01 | 0.88 | 0.93 |
| esc-every-byte | 1.00 | 0.85 | 0.88 |
| newlines-every-40 | 1.02 | 1.01 | 0.92 |
| cyrillic-4k | 0.75 | 0.79 | 0.77 |
| cyrillic-4k-unescaped | 0.76 | 0.78 | 0.78 |
| cjk-4k | 0.73 | 0.74 | 0.81 |
| cjk-4k-unescaped | 0.80 | 0.81 | 0.82 |
| french-4k | 0.81 | 0.80 | 0.84 |
| french-4k-unescaped | 0.84 | 0.86 | 0.84 |
| ascii-rare-utf8-unescaped | 0.93 | 0.93 | 0.88 |
| api-1000-records | 1.00 | 1.03 | 0.95 |
| objects-1000-records | 1.01 | 1.02 | 0.95 |
| object-100-keys | 1.01 | 1.00 | 0.96 |

## In an application

Symfony Demo's `/en/api/posts` (140 KB of JSON), GCC, CLI with opcache, kernel booted once, 30 warm-up requests, then `perf stat` over 200 requests minus 0, three alternating runs on `cd383dcc377`: `json_encode()` is 2.0M of 67.5M instructions per request (callgrind). With this change a request runs 0.2% fewer instructions and 1.0% fewer cycles by median; runs of the same build differ by up to 1.2%, so the cycle gain is within noise.

## Output verification

Against master, byte for byte and including `json_last_error()`, on the GCC and clang release builds and on a GCC debug build with ASan and UBSan (`--enable-debug --enable-address-sanitizer --enable-undefined-sanitizer`, `USE_ZEND_ALLOC=0`), where no sanitizer report appeared:

- [`pairs.php`](pairs.php): every pair of bytes, alone, inside ASCII and after 20 ASCII bytes, six flag sets;
- [`triples.php`](triples.php): every three-byte sequence with an E0..EF lead byte, alone and inside ASCII, six flag sets;
- [`positions.php`](positions.php): every byte value at every position of ASCII strings 1–24 bytes long, four flag sets;
- [`fuzz.php`](fuzz.php): 1,000,000 random strings (5 seeds × 200,000) of 0–300 bytes, as values and as keys, 11 flag sets;
- [`keys.php`](keys.php): literal keys, also ones that need escaping, through arrays, `stdClass` and declared properties, 10 flag sets;
- [`udecode.php`](udecode.php): `utf8_decode()` on all pairs and E0..EF triples;
- php-src tests `ext/json`, `ext/xml`, `ext/standard/tests/strings`: 838 passed on the GCC and clang release builds, 833 on the sanitizer build, none failed.

The new test `json_encode_utf8_sequences.phpt` fails if the overlong checks of the inline path are removed. A separate review compared the inline decoder with `get_next_char(cs_utf_8)` on every three-byte prefix, buffer lengths 0–6 and start cursors 0 and 1 (285 million calls): no difference in value, cursor or status.

## Not tested

aarch64, 32-bit and MSVC builds. The change has no width-dependent arithmetic.

## Appendix: together with other open PRs

Measured with GCC and the previous revision of this branch, which runs the same instructions (within 0.1%).

**php-src #24145** inlines `get_next_char()`, which also speeds up the out-of-line `php_next_utf8_char()`. The two merge without conflicts. Data: [`cycles-with-24145.txt`](cycles-with-24145.txt), [`instructions-with-24145.txt`](instructions-with-24145.txt) (`final-base` = master `897d2091cb4`, `v2` = this change, `hsc-only` = #24145, `hsc-both` = both).

| case | #24145 vs master, cycles | #24145 + this vs #24145, cycles |
|---|---:|---:|
| cyrillic-4k | 0.82 | 0.77 |
| cyrillic-4k-unescaped | 0.92 | 0.71 |
| cjk-4k | 0.90 | 0.87 |
| cjk-4k-unescaped | 0.89 | 0.89 |
| french-4k | 0.98 | 0.70 |
| ascii-4k | 1.01 | 0.90 |
| html-4k | 0.99 | 0.57 |
| api-1000-records | 1.03 | 0.93 |

**php-src #23682** (byte table for the scan) merges cleanly. **#23675** (SIMD scan) has one conflict: it moves the loop body into `php_json_escape_dirty_char()`, where this change applies unchanged; it was merged onto `80d2b997192`, slightly older than the other builds, and needs `ZEND_STATIC_ASSERT()` replaced by `static_assert()` to build on current master. Data: [`cycles-with-23682.txt`](cycles-with-23682.txt), [`cycles-with-23675.txt`](cycles-with-23675.txt) (`master2` = master, `utf8h` = this change, `23682` / `23675` the other PR, `23682mine` / `23675mine` the combination).

| cycles vs master | #23682 | this | both | #23675 | both |
|---|---:|---:|---:|---:|---:|
| ASCII | 0.78 | 0.89 | 0.70 | 0.22 | 0.22 |
| HTML | 0.81 | 0.56 | 0.53 | 0.21 | 0.22 |
| a quote in every byte | 1.00 | 1.09 | 0.92 | 1.20 | 1.22 |
| Cyrillic | 1.15 | 0.64 | 0.61 | 1.13 | 0.84 |
| CJK | 1.00 | 0.78 | 0.73 | 1.11 | 0.79 |
| French | 0.98 | 0.70 | 0.63 | 0.77 | 0.66 |
| 1,000 arrays | 0.99 | 0.95 | 0.90 | 0.93 | 1.02 |

## Reproduce

From the repository root, with php-src checked out next to it:

```sh
git -C ../php-src fetch https://github.com/ArtUkrainskiy/php-src.git json-utf8-2byte
E="--enable-werror --with-libxml --enable-xml"
BENCH_CONFIGURE_EXTRA="$E" ./bench build json-v3-base bd6c637d071
BENCH_CONFIGURE_EXTRA="$E" ./bench build json-v3c1 ca35c079a1f
BENCH_CONFIGURE_EXTRA="$E" ./bench build json-v3 9813f798db9
# clang: the same three with CC=clang and names json-clang-base, json-clang-c1, json-clang-v3
cd reports/json-encode-utf8-inline
./instructions.sh v3-base v3c1 v3           # instructions per call, one line per case
./cycles.sh out.txt v3-base v3c1 v3         # cycles, 3 alternating passes, prints ratios
for t in pairs triples positions udecode keys; do
  for b in v3-base v3; do echo "$b $t $(../../../php-builds/json-$b/sapi/cli/php -n $t.php | md5sum)"; done
done
../../../php-builds/json-v3/sapi/cli/php -n fuzz.php 200000 1   # compare with the same seed on v3-base
```

The scripts look for builds in `../php-builds/json-<name>` next to the repository, or in `$BENCH_BUILDS/json-<name>`.
