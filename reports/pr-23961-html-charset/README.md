# html functions: UTF-8 first when resolving the charset (php-src PR #23961)

Review material for [php/php-src#23961](https://github.com/php/php-src/pull/23961) by nicolas-grekas, "ext/standard: Check for UTF-8 first when resolving the charset of html functions". PR head [`be56f2884e2`](https://github.com/php/php-src/pull/23961/commits/be56f2884e2dedfee9a644efee6939a38c8c6737), merged onto master [`c65321c70f7`](https://github.com/php/php-src/commit/c65321c70f7) (conflict in `NEWS` only). Measured and checked on 14 October 2026, together with the PRs it meets in `ext/standard/html.c`: [#23957](https://github.com/php/php-src/pull/23957) (`htmlspecialchars()` returns its input when nothing needs encoding), which the PR description builds on, and [#24145](https://github.com/php/php-src/pull/24145) (ASCII fast path in `htmlspecialchars()`, by the author of this report).

`determine_charset()` runs on every call of `htmlspecialchars()`, `htmlentities()`, `html_entity_decode()` and `get_html_translation_table()`. On master it calls `strlen()` and walks the 33 entries of `charset_map`, comparing lengths and then names case-insensitively. The PR checks for `utf-8` in any case first, moves the walk into a non-inlined `lookup_charset()`, and makes the walk compare only entries with the same first letter, without `strlen()`.

## Summary

- **Alone, on master:** `htmlspecialchars()` of 8 bytes takes 9–12% fewer cycles and `html_entity_decode()` of 40 bytes 12–13% fewer; 40-byte `htmlspecialchars()` with a UTF-8 or default charset −8 … +1%, depending on the compiler (−8 … +4% with all charsets). Instructions on these UTF-8 and default-charset calls: 3–11% fewer.
- **On top of #23957**, as the description intends: 18–27% fewer cycles for short UTF-8 strings, default charset or explicit; the description says about 40%.
- **`"MacRoman"` with clang 18:** 87 more instructions per call than without the PR (914 → 1,001 on top of #23957, +35% cycles; 86 more and +3% on master). GCC 13 executes 43 fewer on #23957 (44 on master). `MacRoman` is the last entry of the map; the new walk reads the first letter of every entry, the old one compared the stored length first. [Details](#macroman-with-clang-18).
- **With the other html PRs:** no conflicts in code with #23957, #24145, #24142 (`html_entity_decode()`) or #24283 (UTF-8 decoding in `html.h`), only in `NEWS`/`UPGRADING`. The gains add up: on top of #24145, 4–23% fewer cycles for short UTF-8 strings; on top of #23957 + #24145, 22–30% fewer; all three together take 88–92% fewer cycles than master for 40-byte UTF-8 strings without special characters.
- **Output** is the same as master on 79,011 charset hints with four functions, on 32 builds and under ASan/UBSan; the check catches six deliberate mutations.
- **Unused:** `charset_map[].codeset_len` is no longer read.
- **Not measured:** AMD, ZTS builds; a fix for the clang 18 case.

## Results

Change in CPU cycles per call relative to the base named in each heading (negative = fewer cycles, faster). Intel i7-13700H, one column per compiler, median of five alternating runs; the second column is the base's cost for scale.

### The PR on master

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 |
|---|--:|--:|--:|--:|--:|
| `htmlspecialchars()`, 8 bytes, `"UTF-8"` | 277 | −11% | −11% | −9% | −12% |
| `htmlspecialchars()`, 40 bytes, `"UTF-8"` | 901 | −7% | −8% | +1% | −2% |
| `htmlspecialchars()`, 40 bytes, default charset | 887 | −6% | −7% | +1% | −2% |
| `htmlspecialchars()`, 40 bytes with `&"'<`, default charset | 882 | −5% | −6% | 0% | −3% |
| `htmlspecialchars()`, 40 bytes, `"utf-8"` | 900 | −7% | −8% | 0% | −2% |
| `htmlspecialchars()`, 40 bytes, `"ISO-8859-1"` | 839 | −5% | −4% | +4% | 0% |
| `htmlspecialchars()`, 40 bytes, `"cp1251"` | 913 | −7% | −5% | +3% | −4% |
| `htmlspecialchars()`, 40 bytes, `"MacRoman"` | 889 | −6% | −4% | +3% | −2% |
| `htmlspecialchars()`, 1 KB text, default charset | 19,680 | −5% | −7% | +7% | +1% |
| `htmlentities()`, 40 bytes with `&"'<`, default charset | 777 | −3% | 0% | +1% | −5% |
| `html_entity_decode()`, 40 bytes with entities, default charset | 218 | −13% | −13% | −12% | −12% |
| `get_html_translation_table(HTML_SPECIALCHARS)` | 965 | −1% | −14% | +2% | +6% |

### The PR on top of #23957

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 |
|---|--:|--:|--:|--:|--:|
| `htmlspecialchars()`, 8 bytes, `"UTF-8"` | 122 | −25% | −26% | −22% | −27% |
| `htmlspecialchars()`, 40 bytes, `"UTF-8"` | 113 | −20% | −24% | −24% | −20% |
| `htmlspecialchars()`, 40 bytes, default charset | 102 | −18% | −22% | −27% | −20% |
| `htmlspecialchars()`, 40 bytes with `&"'<`, default charset | 469 | −7% | −7% | −7% | −7% |
| `htmlspecialchars()`, 40 bytes, `"utf-8"` | 112 | −19% | −24% | −24% | −19% |
| `htmlspecialchars()`, 40 bytes, `"ISO-8859-1"` | 112 | −4% | −11% | −6% | −1% |
| `htmlspecialchars()`, 40 bytes, `"cp1251"` | 194 | −15% | −25% | −3% | −10% |
| `htmlspecialchars()`, 40 bytes, `"MacRoman"` | 170 | −14% | −18% | +35% | +3% |
| `htmlspecialchars()`, 1 KB text, default charset | 11,920 | −2% | −2% | −1% | +3% |
| `htmlentities()`, 40 bytes with `&"'<`, default charset | 746 | −3% | −4% | −4% | −3% |
| `html_entity_decode()`, 40 bytes with entities, default charset | 224 | −12% | −15% | −12% | −6% |
| `get_html_translation_table(HTML_SPECIALCHARS)` | 983 | −4% | −11% | +2% | −6% |

### The PR on top of #24145

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 |
|---|--:|--:|--:|--:|--:|
| `htmlspecialchars()`, 8 bytes, `"UTF-8"` | 199 | −17% | −12% | −18% | −23% |
| `htmlspecialchars()`, 40 bytes, `"UTF-8"` | 414 | −10% | −6% | −15% | −17% |
| `htmlspecialchars()`, 40 bytes, default charset | 396 | −9% | −4% | −15% | −19% |
| `htmlspecialchars()`, 40 bytes with `&"'<`, default charset | 399 | −6% | −7% | −14% | −19% |
| `htmlspecialchars()`, 40 bytes, `"utf-8"` | 410 | −9% | −7% | −15% | −17% |
| `htmlspecialchars()`, 40 bytes, `"ISO-8859-1"` | 406 | −6% | 0% | −7% | −9% |
| `htmlspecialchars()`, 40 bytes, `"cp1251"` | 494 | −13% | −9% | −11% | −9% |
| `htmlspecialchars()`, 40 bytes, `"MacRoman"` | 477 | −9% | −7% | +18% | −3% |
| `htmlspecialchars()`, 1 KB text, default charset | 8,095 | −1% | +2% | −3% | −6% |
| `htmlentities()`, 40 bytes with `&"'<`, default charset | 591 | 0% | −3% | −7% | −4% |
| `html_entity_decode()`, 40 bytes with entities, default charset | 221 | −11% | −11% | −16% | −13% |
| `get_html_translation_table(HTML_SPECIALCHARS)` | 1,005 | −9% | −4% | −2% | +5% |

### The PR on top of #23957 + #24145

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 |
|---|--:|--:|--:|--:|--:|
| `htmlspecialchars()`, 8 bytes, `"UTF-8"` | 119 | −23% | −25% | −28% | −30% |
| `htmlspecialchars()`, 40 bytes, `"UTF-8"` | 114 | −22% | −22% | −25% | −23% |
| `htmlspecialchars()`, 40 bytes, default charset | 103 | −24% | −22% | −26% | −25% |
| `htmlspecialchars()`, 40 bytes with `&"'<`, default charset | 265 | −14% | −10% | −16% | −21% |
| `htmlspecialchars()`, 40 bytes, `"utf-8"` | 113 | −22% | −22% | −26% | −23% |
| `htmlspecialchars()`, 40 bytes, `"ISO-8859-1"` | 113 | −5% | −10% | −9% | −11% |
| `htmlspecialchars()`, 40 bytes, `"cp1251"` | 199 | −13% | −24% | −20% | −22% |
| `htmlspecialchars()`, 40 bytes, `"MacRoman"` | 174 | −14% | −21% | −6% | −7% |
| `htmlspecialchars()`, 1 KB text, default charset | 5,444 | −5% | +1% | −2% | −1% |
| `htmlentities()`, 40 bytes with `&"'<`, default charset | 636 | 0% | −1% | −8% | −7% |
| `html_entity_decode()`, 40 bytes with entities, default charset | 218 | −9% | −10% | −17% | −14% |
| `get_html_translation_table(HTML_SPECIALCHARS)` | 994 | −2% | −2% | −12% | +3% |

### All three (#23957 + #24145 + #23961) against master

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 |
|---|--:|--:|--:|--:|--:|
| `htmlspecialchars()`, 8 bytes, `"UTF-8"` | 276 | −66% | −65% | −64% | −72% |
| `htmlspecialchars()`, 40 bytes, `"UTF-8"` | 895 | −90% | −89% | −88% | −90% |
| `htmlspecialchars()`, 40 bytes, default charset | 886 | −91% | −89% | −89% | −92% |
| `htmlspecialchars()`, 40 bytes with `&"'<`, default charset | 871 | −73% | −70% | −79% | −82% |
| `htmlspecialchars()`, 40 bytes, `"utf-8"` | 891 | −90% | −89% | −88% | −90% |
| `htmlspecialchars()`, 40 bytes, `"ISO-8859-1"` | 838 | −87% | −86% | −85% | −88% |
| `htmlspecialchars()`, 40 bytes, `"cp1251"` | 914 | −81% | −82% | −81% | −85% |
| `htmlspecialchars()`, 40 bytes, `"MacRoman"` | 890 | −82% | −83% | −79% | −84% |
| `htmlspecialchars()`, 1 KB text, default charset | 19,526 | −72% | −70% | −91% | −91% |
| `htmlentities()`, 40 bytes with `&"'<`, default charset | 772 | −17% | −10% | −21% | −22% |
| `html_entity_decode()`, 40 bytes with entities, default charset | 220 | −9% | −12% | −15% | −11% |
| `get_html_translation_table(HTML_SPECIALCHARS)` | 930 | +4% | −7% | −6% | +12% |

With spread and instructions: [full tables](#full-tables).

## MacRoman with clang 18

| build | base | `htmlspecialchars()`, 40 bytes, `"MacRoman"`: instructions per call, base → with the PR | cycles |
|---|---|--:|--:|
| clang 18.1 | master | 4,042 → 4,128 | +3% |
| clang 18.1 | #23957 | 914 → 1,001 | +35% |
| clang 18.1 | #24145 | 1,652 → 1,738 | +18% |
| clang 18.1 | #23957 + #24145 | 914 → 1,001 | −6% |
| GCC 13.3 | master | 3,257 → 3,213 | −6% |
| GCC 13.3 | #23957 | 878 → 835 | −14% |

`MacRoman` is the last entry of the map (33 entries on master, 32 with the PR, which removes `utf-8`) and the only one starting with `m`. The new walk loads `codeset[0]` of every entry and lowers it before comparing the first letter; the old walk compared `codeset_len`, stored in the entry, first. With clang 18 this costs 86–87 instructions for a charset at the end of the map; GCC 13, GCC 14 and clang 20 do not show it (instructions −8 … −1% on top of #23957). Storing the lowered first letter in `charset_map`, or comparing `codeset_len` before the name, would avoid loading the name for every entry; I have not measured either.

## Correctness

- [`difftest.php`](difftest.php) calls `htmlspecialchars()`, `htmlentities()`, `html_entity_decode()` and `get_html_translation_table()` with each hint and hashes the results and warnings per section:
  - every alias of `charset_map` in four case forms (132 hints);
  - every prefix, six one-byte suffixes and nine one-byte replacements at every position of every alias and of `UTF-8` spellings (`utf8`, `UTF_8`, `utf-88`, with spaces; 2,991 hints);
  - all one- and two-byte strings (65,792);
  - `null`, `''` and `'utf-8'` under eight `default_charset` and four `internal_encoding` values (96);
  - 10,000 random strings of up to 31 bytes, mostly from charset-name characters, seed 7.
- Identical output ([`difftest-master.txt`](difftest-master.txt)) on master and on 28 builds of #23957, #24145 and the PR, alone and combined (16 of them contain the PR), with all four compilers, and on master + #23961 built with `--enable-debug --enable-address-sanitizer --enable-undefined-sanitizer` (clang 18.1, `USE_ZEND_ALLOC=0`, nothing on stderr): [`difftest-builds.txt`](difftest-builds.txt).
- [`mutate.py`](mutate.py) applies six mutations to the PR one at a time (accept `utf-8` followed by anything, accept `utf_8`, compare the first letter case-sensitively, skip the second character, accept a prefix of a codeset, look up an empty name when there is no default); each one changes the output: [`mutate-output.txt`](mutate-output.txt).
- `ext/standard/tests/strings` under ASan: 677 passed, 0 failed, 64 skipped (741 tests).

## Method

- Machine: Intel i7-13700H, P-core CPU 2, governor `powersave`, turbo on, kernel 7.0.0-34. Compilers GCC 13.3.0, GCC 14.2.0, clang 18.1.3, clang 20.1.2.
- Builds: `bench build`, CLI only (`--disable-all`), with the compiler and linker flags of the official Docker image plus `-g`: `BENCH_CFLAGS='-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64'`, `LDFLAGS='-Wl,-O1 -pie'`, `--enable-werror`. All on master `c65321c70f7`: #23957 merged with `NEWS` from master and the generated `arginfo`/`decl` headers regenerated by `build/gen_stub.php`; #24145 merged as its PR head, or, on top of #23957, as the same change rebased onto #23957's head `c1db7a451b4` (local commit `b9a694ea8b6`; the published [`hsc-runs-on-ng`](https://github.com/ArtUkrainskiy/php-src/commits/hsc-runs-on-ng) holds the same change rebased onto #23957's earlier head); #23961 merged with `NEWS`/`UPGRADING` from the base.
- Metric: CPU cycles and instructions per call from `perf stat`, N calls minus the same process with 0 calls, divided by N ([`pairs-run.sh`](pairs-run.sh), cases in [`cases.php`](cases.php)). Five runs per case, base and change alternating; the value is the median over runs of the change's cycles divided by the median of the base's runs, written as a change in percent. Strings come from a pool of 256 random strings (fixed seed).
- Control: master against master in the same series, −1 … +1% over the twelve cases.
- Raw data: [`intel-docker-20261014.txt`](intel-docker-20261014.txt); groups `g13` … `c20` (the PR on master), suffix `d` (on #23957), `h` (on #24145), `f` (on #23957 + #24145), `all` (all three against master), `aa` (control). Tables: [`speedup-table.py`](speedup-table.py) with [`rows.txt`](rows.txt).

## Full tables

Change in CPU cycles per call (negative = fewer cycles, faster), median of five runs, in brackets the lowest and the highest run; last column: change in instructions, lowest and highest over the four compilers.

### The PR on master

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | instructions |
|---|--:|--:|--:|--:|--:|--:|
| `htmlspecialchars()`, 8 bytes, `"UTF-8"` | 277 | −11% (−12 … −10) | −11% (−11 … −10) | −9% (−10 … −9) | −12% (−14 … −10) | −11% … −9% |
| `htmlspecialchars()`, 40 bytes, `"UTF-8"` | 901 | −7% (−9 … −7) | −8% (−10 … −6) | +1% (0 … +1) | −2% (−3 … −2) | −4% … −3% |
| `htmlspecialchars()`, 40 bytes, default charset | 887 | −6% (−6 … −5) | −7% (−8 … −6) | +1% (0 … +4) | −2% (−2 … −1) | −4% … −3% |
| `htmlspecialchars()`, 40 bytes with `&"'<`, default charset | 882 | −5% (−6 … −1) | −6% (−7 … −6) | 0% (0 … +1) | −3% (−4 … −3) | −4% … −3% |
| `htmlspecialchars()`, 40 bytes, `"utf-8"` | 900 | −7% (−8 … −5) | −8% (−9 … −7) | 0% (−1 … 0) | −2% (−3 … −2) | −4% … −3% |
| `htmlspecialchars()`, 40 bytes, `"ISO-8859-1"` | 839 | −5% (−5 … −4) | −4% (−4 … −4) | +4% (+4 … +5) | 0% (−1 … 0) | −1% |
| `htmlspecialchars()`, 40 bytes, `"cp1251"` | 913 | −7% (−7 … −6) | −5% (−5 … −4) | +3% (+2 … +3) | −4% (−4 … −3) | −4% … 0% |
| `htmlspecialchars()`, 40 bytes, `"MacRoman"` | 889 | −6% (−6 … −5) | −4% (−4 … −4) | +3% (+3 … +4) | −2% (−2 … 0) | −2% … +2% |
| `htmlspecialchars()`, 1 KB text, default charset | 19,680 | −5% (−6 … −5) | −7% (−8 … −5) | +7% (+7 … +7) | +1% (+1 … +2) | 0% |
| `htmlentities()`, 40 bytes with `&"'<`, default charset | 777 | −3% (−4 … −3) | 0% (−1 … +8) | +1% (+1 … +2) | −5% (−6 … −5) | −3% … 0% |
| `html_entity_decode()`, 40 bytes with entities, default charset | 218 | −13% (−13 … −12) | −13% (−14 … −12) | −12% (−13 … −8) | −12% (−13 … −12) | −10% … −9% |
| `get_html_translation_table(HTML_SPECIALCHARS)` | 965 | −1% (−2 … +1) | −14% (−15 … −12) | +2% (+1 … +5) | +6% (+5 … +6) | −4% |

### The PR on top of #23957

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | instructions |
|---|--:|--:|--:|--:|--:|--:|
| `htmlspecialchars()`, 8 bytes, `"UTF-8"` | 122 | −25% (−27 … −25) | −26% (−26 … −25) | −22% (−22 … −21) | −27% (−29 … −27) | −21% … −19% |
| `htmlspecialchars()`, 40 bytes, `"UTF-8"` | 113 | −20% (−21 … −19) | −24% (−25 … −24) | −24% (−24 … −23) | −20% (−21 … −19) | −21% … −18% |
| `htmlspecialchars()`, 40 bytes, default charset | 102 | −18% (−19 … −16) | −22% (−23 … −21) | −27% (−28 … −27) | −20% (−22 … −19) | −22% … −20% |
| `htmlspecialchars()`, 40 bytes with `&"'<`, default charset | 469 | −7% (−7 … −7) | −7% (−7 … −7) | −7% (−7 … −6) | −7% (−8 … −6) | −7% … −6% |
| `htmlspecialchars()`, 40 bytes, `"utf-8"` | 112 | −19% (−20 … −15) | −24% (−24 … −18) | −24% (−24 … −24) | −19% (−19 … −19) | −21% … −18% |
| `htmlspecialchars()`, 40 bytes, `"ISO-8859-1"` | 112 | −4% (−4 … −3) | −11% (−11 … −10) | −6% (−7 … −5) | −1% (−2 … 0) | −7% … −6% |
| `htmlspecialchars()`, 40 bytes, `"cp1251"` | 194 | −15% (−15 … −13) | −25% (−25 … −24) | −3% (−3 … −2) | −10% (−11 … −8) | −13% … 0% |
| `htmlspecialchars()`, 40 bytes, `"MacRoman"` | 170 | −14% (−15 … −14) | −18% (−19 … −18) | +35% (+34 … +37) | +3% (+3 … +5) | −8% … +10% |
| `htmlspecialchars()`, 1 KB text, default charset | 11,920 | −2% (−3 … −2) | −2% (−3 … −1) | −1% (−1 … 0) | +3% (+2 … +7) | 0% |
| `htmlentities()`, 40 bytes with `&"'<`, default charset | 746 | −3% (−4 … −2) | −4% (−4 … −3) | −4% (−4 … −3) | −3% (−3 … −2) | −3% |
| `html_entity_decode()`, 40 bytes with entities, default charset | 224 | −12% (−13 … −10) | −15% (−16 … −14) | −12% (−12 … −11) | −6% (−8 … −5) | −10% … −9% |
| `get_html_translation_table(HTML_SPECIALCHARS)` | 983 | −4% (−5 … −2) | −11% (−13 … −3) | +2% (+1 … +2) | −6% (−7 … 0) | −4% |

### The PR on top of #24145

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | instructions |
|---|--:|--:|--:|--:|--:|--:|
| `htmlspecialchars()`, 8 bytes, `"UTF-8"` | 199 | −17% (−17 … −16) | −12% (−13 … −11) | −18% (−19 … −17) | −23% (−23 … −22) | −16% … −13% |
| `htmlspecialchars()`, 40 bytes, `"UTF-8"` | 414 | −10% (−11 … −9) | −6% (−8 … −4) | −15% (−16 … −14) | −17% (−18 … −16) | −12% … −9% |
| `htmlspecialchars()`, 40 bytes, default charset | 396 | −9% (−9 … −8) | −4% (−5 … −2) | −15% (−15 … −14) | −19% (−19 … −19) | −12% … −9% |
| `htmlspecialchars()`, 40 bytes with `&"'<`, default charset | 399 | −6% (−7 … +1) | −7% (−9 … −5) | −14% (−14 … −14) | −19% (−19 … −18) | −11% … −8% |
| `htmlspecialchars()`, 40 bytes, `"utf-8"` | 410 | −9% (−10 … −7) | −7% (−8 … −4) | −15% (−16 … −14) | −17% (−17 … −17) | −12% … −8% |
| `htmlspecialchars()`, 40 bytes, `"ISO-8859-1"` | 406 | −6% (−8 … −5) | 0% (−4 … +1) | −7% (−8 … −7) | −9% (−10 … −5) | −4% … −3% |
| `htmlspecialchars()`, 40 bytes, `"cp1251"` | 494 | −13% (−14 … −12) | −9% (−10 … −7) | −11% (−11 … −11) | −9% (−10 … −8) | −9% … 0% |
| `htmlspecialchars()`, 40 bytes, `"MacRoman"` | 477 | −9% (−9 … −5) | −7% (−9 … −4) | +18% (+17 … +18) | −3% (−3 … −2) | −6% … +5% |
| `htmlspecialchars()`, 1 KB text, default charset | 8,095 | −1% (−1 … +1) | +2% (−1 … +2) | −3% (−3 … −2) | −6% (−6 … −5) | −1% |
| `htmlentities()`, 40 bytes with `&"'<`, default charset | 591 | 0% (0 … +1) | −3% (−3 … +14) | −7% (−8 … −6) | −4% (−4 … −4) | −4% … −3% |
| `html_entity_decode()`, 40 bytes with entities, default charset | 221 | −11% (−12 … −10) | −11% (−12 … −10) | −16% (−17 … −15) | −13% (−14 … −12) | −10% … −9% |
| `get_html_translation_table(HTML_SPECIALCHARS)` | 1,005 | −9% (−13 … −9) | −4% (−5 … −3) | −2% (−2 … −1) | +5% (+5 … +6) | −4% |

### The PR on top of #23957 + #24145

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | instructions |
|---|--:|--:|--:|--:|--:|--:|
| `htmlspecialchars()`, 8 bytes, `"UTF-8"` | 119 | −23% (−24 … −22) | −25% (−27 … −22) | −28% (−28 … −28) | −30% (−31 … −29) | −21% … −19% |
| `htmlspecialchars()`, 40 bytes, `"UTF-8"` | 114 | −22% (−22 … −21) | −22% (−23 … −22) | −25% (−26 … −24) | −23% (−24 … −22) | −21% … −18% |
| `htmlspecialchars()`, 40 bytes, default charset | 103 | −24% (−24 … −23) | −22% (−22 … −21) | −26% (−27 … −22) | −25% (−25 … −25) | −22% … −20% |
| `htmlspecialchars()`, 40 bytes with `&"'<`, default charset | 265 | −14% (−15 … −14) | −10% (−11 … −10) | −16% (−16 … −14) | −21% (−22 … −19) | −13% … −11% |
| `htmlspecialchars()`, 40 bytes, `"utf-8"` | 113 | −22% (−22 … −20) | −22% (−23 … −20) | −26% (−26 … −23) | −23% (−24 … −22) | −21% … −18% |
| `htmlspecialchars()`, 40 bytes, `"ISO-8859-1"` | 113 | −5% (−5 … −4) | −10% (−11 … −9) | −9% (−10 … −7) | −11% (−12 … −10) | −7% … −6% |
| `htmlspecialchars()`, 40 bytes, `"cp1251"` | 199 | −13% (−14 … −12) | −24% (−25 … −19) | −20% (−20 … −20) | −22% (−22 … −22) | −13% … 0% |
| `htmlspecialchars()`, 40 bytes, `"MacRoman"` | 174 | −14% (−15 … −13) | −21% (−21 … −20) | −6% (−7 … −6) | −7% (−8 … −7) | −8% … +10% |
| `htmlspecialchars()`, 1 KB text, default charset | 5,444 | −5% (−6 … −3) | +1% (+1 … +2) | −2% (−3 … −1) | −1% (−2 … 0) | −2% … −1% |
| `htmlentities()`, 40 bytes with `&"'<`, default charset | 636 | 0% (0 … +1) | −1% (−2 … −1) | −8% (−8 … −7) | −7% (−8 … −4) | −4% … −3% |
| `html_entity_decode()`, 40 bytes with entities, default charset | 218 | −9% (−10 … −8) | −10% (−10 … −10) | −17% (−17 … −16) | −14% (−14 … −13) | −10% … −9% |
| `get_html_translation_table(HTML_SPECIALCHARS)` | 994 | −2% (−6 … +1) | −2% (−4 … +7) | −12% (−13 … −6) | +3% (+2 … +3) | −4% |

### All three against master

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | instructions |
|---|--:|--:|--:|--:|--:|--:|
| `htmlspecialchars()`, 8 bytes, `"UTF-8"` | 276 | −66% (−67 … −66) | −65% (−66 … −65) | −64% (−65 … −64) | −72% (−72 … −69) | −65% … −60% |
| `htmlspecialchars()`, 40 bytes, `"UTF-8"` | 895 | −90% (−90 … −90) | −89% (−89 … −88) | −88% (−88 … −88) | −90% (−90 … −90) | −88% … −83% |
| `htmlspecialchars()`, 40 bytes, default charset | 886 | −91% (−91 … −91) | −89% (−89 … −89) | −89% (−90 … −88) | −92% (−92 … −90) | −89% … −85% |
| `htmlspecialchars()`, 40 bytes with `&"'<`, default charset | 871 | −73% (−74 … −72) | −70% (−70 … −70) | −79% (−79 … −78) | −82% (−83 … −82) | −75% … −72% |
| `htmlspecialchars()`, 40 bytes, `"utf-8"` | 891 | −90% (−90 … −90) | −89% (−89 … −89) | −88% (−88 … −88) | −90% (−90 … −89) | −88% … −83% |
| `htmlspecialchars()`, 40 bytes, `"ISO-8859-1"` | 838 | −87% (−87 … −87) | −86% (−86 … −86) | −85% (−85 … −84) | −88% (−89 … −79) | −85% … −80% |
| `htmlspecialchars()`, 40 bytes, `"cp1251"` | 914 | −81% (−81 … −81) | −82% (−83 … −82) | −81% (−81 … −76) | −85% (−86 … −85) | −80% … −75% |
| `htmlspecialchars()`, 40 bytes, `"MacRoman"` | 890 | −82% (−83 … −82) | −83% (−83 … −82) | −79% (−80 … −75) | −84% (−84 … −83) | −79% … −74% |
| `htmlspecialchars()`, 1 KB text, default charset | 19,526 | −72% (−73 … −72) | −70% (−71 … −70) | −91% (−91 … −91) | −91% (−91 … −91) | −89% … −86% |
| `htmlentities()`, 40 bytes with `&"'<`, default charset | 772 | −17% (−19 … −16) | −10% (−11 … −10) | −21% (−21 … −20) | −22% (−23 … 0) | −21% … −17% |
| `html_entity_decode()`, 40 bytes with entities, default charset | 220 | −9% (−11 … −9) | −12% (−12 … −9) | −15% (−16 … −15) | −11% (−12 … −10) | −10% … −9% |
| `get_html_translation_table(HTML_SPECIALCHARS)` | 930 | +4% (+2 … +4) | −7% (−8 … −5) | −6% (−7 … −6) | +12% (+11 … +12) | −4% |

## Reproduce

Build master and the variants on `c65321c70f7` as in [Method](#method), named `hcs-<compiler>-base` (master), `hcs-<compiler>-c` (+#23961), `hcs-<compiler>-s57` (+#23957), `hcs-<compiler>-d` (+#23957+#23961) and so on, then from this directory:

```sh
B=${BENCH_BUILDS:-../../../php-builds}
for b in g13-base g13-c; do $B/hcs-$b/sapi/cli/php -n difftest.php 10000 7 | diff - difftest-master.txt && echo "$b ok"; done
BENCH_BUILDS=$B PREFIX=hcs- CPU=2 PASSES=5 ./pairs-run.sh out.txt g13:g13-base:g13-c g13d:g13-s57:g13-d aa:g13-base:g13-base
mapfile -t ROWS < rows.txt
./speedup-table.py --full out.txt 'g13:GCC 13.3' "${ROWS[@]}"
```
