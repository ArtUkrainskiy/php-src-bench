# var_export() without temporary strings (php-src PR #23189)

Review material for [php/php-src#23189](https://github.com/php/php-src/pull/23189) by kamil-tekiela, "ext/standard: Optimize var_export". PR head [`dc5f7958b20`](https://github.com/php/php-src/pull/23189/commits/dc5f7958b201605d67d72f5d68b5be8c15357583), merged onto master [`c65321c70f7`](https://github.com/php/php-src/commit/c65321c70f7) (conflict in `UPGRADING` only). Measured and checked on 14 October 2026.

On master, `var_export()` builds every indentation with `spprintf("%*c")` and escapes strings into temporary strings: values and array keys twice, with `php_addcslashes()` for `'` and `\` and then `php_str_to_str()` for NUL; property names once, with `php_addcslashes_str()`. The PR writes spaces with `memset()` and escapes in one function that first counts the escaped length (`php_var_export_compute_escaped_string_len()`), reserves it with `smart_str_extend()` and then writes byte by byte.

## Summary

- **32-bit: the escaped length overflows and the write runs past the buffer.** The count adds 11 per NUL without a check. On a 32-bit build, `var_export()` of 357,913,942 NUL bytes counts 4,294,967,304 = 8 (mod 2³²), reserves 8 bytes and crashes with a segmentation fault; master stops with "Possible integer overflow in memory allocation", because `php_str_to_str()` allocates through `zend_string_safe_alloc()`. [Details](#32-bit-overflow).
- **Small and medium values are much faster:** 15–68% fewer cycles for strings, arrays, nested config arrays and objects, on all four compilers: the temporary strings and `spprintf()` are gone.
- **Long strings get slower:** a 64 KB string with `'` or `\` after one word in eight takes 92–172% more cycles, a 1 KB string with NUL bytes 53–116% more, a 64 KB string with nothing to escape −6 … +126% depending on the compiler. Counting and writing are two passes with several compares per byte: 23–28 instructions per byte instead of master's 8–9 on the 64 KB string with quotes. [Details](#long-strings).
- **A one-pass variant** fixes both: a 256-byte class table (one for values and keys, one for property names, which keep NUL as is), a single loop that appends plain runs with `smart_str_appendl()` and the escapes after them, without the unchecked expanded-length calculation. It is faster than master in every case measured except a single int, on all four compilers: 23–75% fewer cycles, and −2 … +2% for the int (the master-against-master control: −1 … +2%), and the 32-bit case ends in "Out of memory" instead of a crash. [`one-pass-variant.diff`](one-pass-variant.diff).
- **Output** is the same as master with the PR and with the variant, on all four compilers, on 32-bit and under ASan/UBSan; the check catches six deliberate mutations of the PR.
- **Not measured:** AMD; real-world callers (the PHPStan result cache that mentioned this PR moved to `serialize()`).

## Results

Change in CPU cycles per `var_export($value, true)` call relative to master (negative = fewer cycles, faster). Intel i7-13700H, one column per compiler, median of five alternating runs; the second column is master's cost for scale.

### The PR

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 |
|---|--:|--:|--:|--:|--:|
| an int | 157 | −1% | 0% | +3% | −1% |
| a 10–20-byte string, nothing to escape | 302 | −34% | −40% | −36% | −34% |
| a 16–25-byte string with `'` and `\` | 342 | −16% | −15% | −16% | −21% |
| array of 10 mixed values | 5,925 | −57% | −57% | −57% | −57% |
| nested config array, 0.1–7.4 KB of output (median 2.4 KB) | 42,556 | −62% | −66% | −63% | −65% |
| 1,000 ints | 177,222 | −49% | −46% | −45% | −47% |
| 1,000 strings | 319,568 | −68% | −67% | −63% | −65% |
| 1,000 string keys and values | 511,363 | −68% | −67% | −63% | −61% |
| 100 objects (`\Pt::__set_state()`) | 234,876 | −41% | −42% | −40% | −41% |
| a 64 KB string, nothing to escape | 147,551 | −6% | +7% | +126% | +121% |
| a 64 KB string, `'` or `\` after one word in eight | 181,004 | +95% | +92% | +163% | +172% |
| a 1 KB string with NUL bytes after one word in four | 3,815 | +72% | +53% | +105% | +116% |

### The one-pass variant

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 |
|---|--:|--:|--:|--:|--:|
| an int | 155 | −2% | +1% | +1% | +2% |
| a 10–20-byte string, nothing to escape | 294 | −48% | −50% | −43% | −44% |
| a 16–25-byte string with `'` and `\` | 332 | −36% | −34% | −30% | −29% |
| array of 10 mixed values | 5,914 | −59% | −60% | −57% | −59% |
| nested config array, 0.1–7.4 KB of output (median 2.4 KB) | 42,449 | −71% | −70% | −70% | −70% |
| 1,000 ints | 176,321 | −48% | −47% | −46% | −48% |
| 1,000 strings | 318,269 | −72% | −72% | −69% | −68% |
| 1,000 string keys and values | 518,113 | −75% | −73% | −70% | −68% |
| 100 objects (`\Pt::__set_state()`) | 228,438 | −41% | −43% | −41% | −42% |
| a 64 KB string, nothing to escape | 146,372 | −50% | −51% | −38% | −38% |
| a 64 KB string, `'` or `\` after one word in eight | 181,129 | −29% | −33% | −24% | −23% |
| a 1 KB string with NUL bytes after one word in four | 3,870 | −53% | −54% | −47% | −49% |

With spread and instructions: [full tables](#full-tables).

## 32-bit overflow

`php_var_export_compute_escaped_string_len()` returns `len` plus 1 per `'` or `\` plus 11 per NUL in a `size_t`, without a check, and `php_var_export_append_escaped()` reserves exactly that with `smart_str_extend()`, then writes 12 bytes per NUL for every input byte. With a 32-bit `size_t`, 357,913,942 NUL bytes (341 MiB) give 12 × 357,913,942 = 4,294,967,304, which wraps to 8.

Built with `gcc -m32` (`PHP_INT_SIZE` = 4), `php -n -d memory_limit=-1`, `var_export(str_repeat("\0", 357913942), true)`:

| build | result |
|---|---|
| master | `Fatal error: Possible integer overflow in memory allocation (357913942 * 11 + 357913960)` |
| PR | segmentation fault (exit 139) |
| one-pass variant | `Fatal error: Out of memory (allocated 2012569600 bytes) (tried to allocate 1650462720 bytes)` |

Full output: [`overflow-32bit.txt`](overflow-32bit.txt). On 64-bit the same wrap needs more memory than exists. Quotes and backslashes alone add at most `len`, so they wrap only for `len` ≥ 2³¹. The variant computes no expanded length; it appends plain runs and escapes through `smart_str`, like the rest of `var_export()`, and with it this reproducer ends in "Out of memory".

## Long strings

Instructions per byte of a 64 KB string, median of five runs:

| | master | PR | variant |
|---|--:|--:|--:|
| nothing to escape, GCC 13.3 | 9.1 | 10.0 | 8.0 |
| nothing to escape, clang 20.1 | 8.1 | 12.0 | 7.0 |
| `'` or `\` after one word in eight, GCC 13.3 | 9.2 | 23.0 | 8.8 |
| `'` or `\` after one word in eight, clang 20.1 | 8.2 | 26.9 | 7.9 |

The PR reads every byte twice, and both loops test for `'`, `\` and NUL separately; the write loop stores one byte at a time. Master's `php_addcslashes()` does one table lookup per byte in a single pass and `php_str_to_str()` finds the next NUL with `php_memnstr()`, which is `memchr()` for a one-byte needle. The variant does one table lookup per byte and copies everything between two escapes at once.

An intermediate one-pass version tested `k == 0 || k == max_plain`, with `max_plain` 0 or 2 (NUL is not escaped in property names); clang 20 compiled it into two `sete` and an `or` per byte and was 30–51% slower than master on the 64 KB strings. Two tables, so that the loop tests `k == 0` only, removed that.

## Correctness

- [`difftest.php`](difftest.php) hashes `var_export(..., true)` of: every byte value alone and between letters, as value and as key (768); all strings of length 0–4 over `a`, `'`, `\`, NUL as values and keys, and as dynamic property names where valid (not empty, not starting with NUL) (1,023 of each kind run; invalid property names give an empty object); 64 KB and 1 KB strings of quotes, backslashes, NULs and their random mixes (12); nested arrays and objects with indentation, public/protected/private properties, enums, negative and huge integer keys, floats including `NAN`, `INF`, `-0.0` (4); 200,000 random nested arrays and objects of random strings, seed 7.
- Identical output ([`difftest-master.txt`](difftest-master.txt)) on master, the PR and the variant with all four compilers, under ASan/UBSan (clang 18.1, `USE_ZEND_ALLOC=0`, nothing on stderr) for the PR and the variant, and on 32-bit for master, the PR and the variant (a different expected output there, since `PHP_INT_MAX` differs): [`difftest-builds.txt`](difftest-builds.txt).
- [`mutate.py`](mutate.py) applies six mutations to the PR (11 → 10 for NUL, NUL in keys not escaped, `'` not escaped when written, length not counted, one space less, NUL escaped in property names); each one changes the output or crashes: [`mutate-output.txt`](mutate-output.txt).
- `ext/standard/tests/general_functions` and `ext/standard/tests/array` under ASan: 1,078 passed, 0 failed, 90 skipped, for the PR and for the variant.
- `buffer_append_spaces()` takes an `int` and is called with `level + 1`, `level + 2` and, under `level > 1`, `level - 1`. A level of −1 through the C API (`php_var_export_ex()` is `PHPAPI`) gives array elements a width of 0: the PR writes no space where `%*c` wrote one. A level of −2 or below gives a negative width, which becomes `SIZE_MAX` in `memset()`. In-tree callers pass 1 or more (`ext/zend_test` passes 3 and more).

## Method

- Machine: Intel i7-13700H, P-core CPU 2, governor `powersave`, turbo on, kernel 7.0.0-34. Compilers GCC 13.3.0, GCC 14.2.0, clang 18.1.3, clang 20.1.2.
- Builds: `bench build`, CLI only (`--disable-all`), with the compiler and linker flags of the official Docker image plus `-g`: `BENCH_CFLAGS='-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64'`, `LDFLAGS='-Wl,-O1 -pie'`, `--enable-werror`. The PR merged onto `c65321c70f7` (merge `a348d6b3f08`, `UPGRADING` from master); the variant is `2562b938601` on top of that merge. 32-bit builds: `gcc -m32 -O2 -g`, `LDFLAGS=-m32`.
- Metric: CPU cycles and instructions per call from `perf stat`, N calls minus the same process with 0 calls, divided by N ([`pairs-run.sh`](pairs-run.sh), cases in [`cases.php`](cases.php)). Five runs per case, master and the build alternating; the value is the median over runs of the build's cycles divided by the median of master's runs, written as a change in percent. Small values come from a pool of 64 (fixed seed); long strings are random words with the escaped characters at random places.
- Control: master against master in the same series, −1 … +2% over the twelve cases.
- Raw data: [`intel-docker-20261014.txt`](intel-docker-20261014.txt) (how it was run: [`runs.txt`](runs.txt)); groups `g13` … `c20` for the PR, suffix `o` for the variant, `aa` for the control. Tables: [`speedup-table.py`](speedup-table.py) with [`rows.txt`](rows.txt).

## Full tables

Change in CPU cycles per call relative to master (negative = fewer cycles, faster), median of five runs, in brackets the lowest and the highest run; last column: change in instructions, lowest and highest over the four compilers.

### The PR

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | instructions |
|---|--:|--:|--:|--:|--:|--:|
| an int | 157 | −1% (−1 … +3) | 0% (−1 … +1) | +3% (+1 … +3) | −1% (−1 … +1) | 0% |
| a 10–20-byte string, nothing to escape | 302 | −34% (−35 … −15) | −40% (−44 … −35) | −36% (−37 … −35) | −34% (−34 … −33) | −36% … −29% |
| a 16–25-byte string with `'` and `\` | 342 | −16% (−19 … −15) | −15% (−17 … −15) | −16% (−16 … −14) | −21% (−21 … −18) | −17% … −10% |
| array of 10 mixed values | 5,925 | −57% (−58 … −56) | −57% (−57 … −56) | −57% (−57 … −34) | −57% (−58 … −56) | −54% … −51% |
| nested config array, 0.1–7.4 KB of output (median 2.4 KB) | 42,556 | −62% (−65 … −61) | −66% (−68 … −66) | −63% (−64 … −63) | −65% (−66 … −64) | −70% … −67% |
| 1,000 ints | 177,222 | −49% (−49 … −47) | −46% (−47 … −45) | −45% (−47 … −45) | −47% (−51 … −44) | −52% … −49% |
| 1,000 strings | 319,568 | −68% (−69 … −68) | −67% (−70 … −66) | −63% (−64 … −63) | −65% (−66 … −61) | −70% … −67% |
| 1,000 string keys and values | 511,363 | −68% (−69 … −68) | −67% (−68 … −66) | −63% (−63 … −62) | −61% (−62 … −60) | −74% … −69% |
| 100 objects (`\Pt::__set_state()`) | 234,876 | −41% (−42 … −38) | −42% (−43 … −40) | −40% (−41 … −39) | −41% (−41 … −40) | −37% … −34% |
| a 64 KB string, nothing to escape | 147,551 | −6% (−7 … −5) | +7% (+6 … +16) | +126% (+125 … +127) | +121% (+118 … +125) | +10% … +64% |
| a 64 KB string, `'` or `\` after one word in eight | 181,004 | +95% (+94 … +98) | +92% (+91 … +93) | +163% (+162 … +164) | +172% (+169 … +174) | +149% … +227% |
| a 1 KB string with NUL bytes after one word in four | 3,815 | +72% (+72 … +74) | +53% (+51 … +58) | +105% (+104 … +106) | +116% (+115 … +117) | +64% … +109% |

### The one-pass variant

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | instructions |
|---|--:|--:|--:|--:|--:|--:|
| an int | 155 | −2% (−3 … +1) | +1% (−1 … +1) | +1% (−1 … +39) | +2% (+1 … +5) | 0% |
| a 10–20-byte string, nothing to escape | 294 | −48% (−50 … −48) | −50% (−51 … −46) | −43% (−43 … −43) | −44% (−45 … −43) | −40% … −37% |
| a 16–25-byte string with `'` and `\` | 332 | −36% (−37 … −32) | −34% (−35 … −29) | −30% (−31 … −27) | −29% (−29 … −13) | −28% … −24% |
| array of 10 mixed values | 5,914 | −59% (−60 … −59) | −60% (−61 … −60) | −57% (−58 … −56) | −59% (−60 … −58) | −55% … −53% |
| nested config array, 0.1–7.4 KB of output (median 2.4 KB) | 42,449 | −71% (−72 … −69) | −70% (−71 … −69) | −70% (−70 … −68) | −70% (−70 … −69) | −75% … −73% |
| 1,000 ints | 176,321 | −48% (−48 … −46) | −47% (−47 … −46) | −46% (−46 … −45) | −48% (−49 … −48) | −52% … −49% |
| 1,000 strings | 318,269 | −72% (−73 … −70) | −72% (−73 … −71) | −69% (−69 … −67) | −68% (−69 … −68) | −73% … −71% |
| 1,000 string keys and values | 518,113 | −75% (−75 … −68) | −73% (−73 … −72) | −70% (−70 … −69) | −68% (−69 … −67) | −77% … −76% |
| 100 objects (`\Pt::__set_state()`) | 228,438 | −41% (−42 … −37) | −43% (−43 … −42) | −41% (−41 … −40) | −42% (−42 … −39) | −37% … −35% |
| a 64 KB string, nothing to escape | 146,372 | −50% (−52 … −49) | −51% (−52 … −51) | −38% (−39 … −38) | −38% (−39 … −38) | −14% … −12% |
| a 64 KB string, `'` or `\` after one word in eight | 181,129 | −29% (−32 … −10) | −33% (−33 … −32) | −24% (−25 … −23) | −23% (−24 … −22) | −5% … −4% |
| a 1 KB string with NUL bytes after one word in four | 3,870 | −53% (−54 … −53) | −54% (−55 … −20) | −47% (−48 … −41) | −49% (−50 … −43) | −31% … −29% |
