# grapheme_strlen() and related functions check for ASCII 8 bytes at a time

The change is on branch [`grapheme-ascii-check-words`](https://github.com/ArtUkrainskiy/php-src/tree/grapheme-ascii-check-words) of ArtUkrainskiy/php-src, also as a patch: [`grapheme-ascii-check.patch`](grapheme-ascii-check.patch).

`grapheme_strlen()`, `grapheme_substr()`, `grapheme_strpos()` and five other functions of ext/intl count user-visible characters (grapheme clusters). When a string is ASCII without a CR LF pair, each byte is one grapheme, and these functions can work on bytes without ICU. To find out, they first call `grapheme_ascii_check()` on the string. On master it reads the string one byte at a time. The change reads 8 bytes at a time. Scripts need no change and no setting.

## Summary

- **ASCII strings of 9 bytes and more:** fewer CPU cycles per call than master in every measured function. On 2 KB, `grapheme_strlen()` takes 79% fewer on GCC 15.2 and 80% fewer on clang 21.1, the other functions except `grapheme_extract()` 69–79% fewer. On 80 bytes they take 40–67% fewer, on 16 bytes 10–28%, on 9 bytes 6–25%. `grapheme_extract($s, 8)` checks only 9 bytes and takes 5–14% fewer on all of them ([Results](#results)).
- **ASCII strings of 1–8 bytes, the same string in every call:** −10% to +12% against master, −10 to +8 cycles per call. Calls with a needle on 1 byte cost the most, up to 12% more. `grapheme_substr()` on GCC is 5–10% faster ([Trade-offs](#trade-offs)).
- **ASCII strings of mixed lengths, 1–24 bytes in a random order:** `grapheme_strlen()` takes 28–33% fewer cycles, `grapheme_substr()` 7–8%, `grapheme_strpos()` 12–13%.
- **Text with non-ASCII characters or CR LF:** these strings take the ICU path, as on master, and the change is within 3% of master. Two cases gain: `grapheme_extract($s, 8)` checks only the first 9 bytes, so it takes 5–14% fewer cycles whenever they are ASCII. With one "é" at the end of 2 KB of ASCII, `grapheme_substr()` takes 19% fewer.
- **Correctness:** the same output as master on 26,470 strings in every function that calls the check, on GCC, clang, ZTS and ASan + UBSan. A new test catches all six mistakes put into the code. On ASCII strings over 2 GiB `grapheme_strlen()` and `grapheme_strstr()` now return the right result instead of an error, and the other functions answer as on master. ([Correctness checks](#correctness-checks)).
- **Not checked:** Intel, Windows, big-endian, a full application ([Not tested](#not-tested)).

## What changes and why it is faster

Before: `grapheme_ascii_check()` in `ext/intl/grapheme/grapheme_util.cpp` walked the string one byte at a time. For each byte it checked for a value above 0x7f and for a CR LF pair. It also read one byte after the length: the NUL at the end of a string, or the next byte of the string for `grapheme_extract()`. It kept the length in an `int`.

The functions that call it are `grapheme_strlen()`, `grapheme_substr()`, `grapheme_strpos()`, `grapheme_stripos()`, `grapheme_strrpos()`, `grapheme_strripos()`, `grapheme_strstr()` and `grapheme_extract()`. Most of them check the whole string, also for `grapheme_substr($s, 0, 8)`. `grapheme_extract()` checks only `size + 1` bytes.

After: while at least 9 bytes are left, it loads 8 bytes at `p` and 8 bytes at `p + 1` as two 64-bit words.
- A byte above 0x7f sets a bit of `0x8080808080808080` in the first word.
- Byte `i` of the first word is `p[i]`, byte `i` of the second is `p[i + 1]`. So `(first ^ 0x0d0d…) | (second ^ 0x0a0a…)` has a zero byte exactly where a CR is followed by an LF. The standard zero-byte test finds it. It doesn't depend on byte order.

The rest, 0–8 bytes, is checked one byte at a time, without reading the byte after the length. The function returns the length as `zend_long` without keeping it in an `int`. `grapheme_strpos()`, `grapheme_stripos()`, `grapheme_strrpos()`, `grapheme_strripos()` and `grapheme_substr()` use `int32_t` offsets on their ASCII path, so they now skip the check for strings longer than `INT32_MAX` bytes and go to ICU.

Why the result is the same: inside the checked bytes both versions return −1 when a byte is above 0x7f or a CR is followed by an LF, else the length. Master also returned −1 when the last checked byte was a CR and the byte after the length an LF. That never changed a result: the only caller that checks fewer bytes than its string is `grapheme_extract()`, and that CR is outside the `size` bytes it returns. Above 2³¹ bytes master's `int` held a wrong length. For 2–4 GiB it was negative. `grapheme_extract()` compares the result with −1, so it still took the ASCII path. The other functions went to ICU, which can't take such strings. With the change, `grapheme_strlen()` and `grapheme_strstr()` take the ASCII path there and return the right result. The five functions with `int32_t` offsets go to ICU as before. The [correctness checks](#correctness-checks) compare every function with master, and a mutation that reads the byte after the length again gives the same output.

## Trade-offs

- **ASCII of 1–8 bytes, one string repeated:** the change adds 3 to 34 instructions per call. In cycles it's −10 to +8 per call, on calls of 33–153 cycles on master. The biggest increases are on 1 byte with a needle: `grapheme_strpos($s, 'zz')` +12% on GCC and +11% on clang, `grapheme_strpos($s, 'x')` +12% and +8%, `grapheme_strstr()` +9% and +10%. `grapheme_strstr()` checks the needle whenever the haystack is ASCII, and the others when the needle isn't found in an ASCII haystack. So these calls pay for two short checks. On GCC `grapheme_substr()` is 5–10% faster from 1 to 8 bytes. I didn't profile these rows further.
- **Code size:** `grapheme_ascii_check()` is 213 bytes on GCC instead of 60, and 223 on clang instead of 56. It saves 1 register on GCC and 3 on clang on entry, master's saves none ([`data/disassembly.txt`](data/disassembly.txt)).
- **Earlier versions:** the first one searched for CR with `memchr()`. In its series `grapheme_strlen()` and `grapheme_strpos()` of 5 bytes cost 21–31% more than master. The second one looked for a CR in each word and then checked that word byte by byte. On clang it cost 7–16% more on 5 bytes. On 2 KB of plain ASCII both were faster than the final version: `grapheme_strlen()` −87% to −91% and −83%, against −79% to −80%. With a lone CR every 80 bytes they were slower ([Appendix](#appendix-earlier-versions)).

## Results

Change in CPU cycles per call against master (negative = fewer cycles, faster). Each compiler is compared with master built by the same compiler. The strings: ASCII English text of 1 byte to 2 KB; 1024 ASCII strings of 1–24 bytes, one per call in a fixed random order; 2 KB of ASCII with a lone CR or CR LF every 80 bytes, or with one "é" at the start or the end; 80 bytes of Spanish and Chinese. The range over the passes, the change in instructions, all 111 calls (also 2, 4, 8 and 10 bytes, `grapheme_strstr()`, `grapheme_strrpos()`, Russian, Japanese, Korean, emoji) and the master-against-master control are in [`FULL-TABLES.md`](FULL-TABLES.md).

<!-- bench-table series.json --labels labels.txt --no-control -->
| call | master, CPU cycles per call (GCC 15.2 (gcc15)) | GCC 15.2 (gcc15) | clang 21.1 (clang21) | clang 21.1 (clang21-aa) |
|---|--:|--:|--:|--:|
| `grapheme_strlen()`, ASCII 1 B | 36 | +9% | +4% | +3% |
| `grapheme_strlen()`, ASCII 3 B | 40 | +3% | −4% | 0% |
| `grapheme_strlen()`, ASCII 5 B | 44 | −2% | −5% | 0% |
| `grapheme_strlen()`, ASCII 9 B | 52 | −23% | −25% | −6% |
| `grapheme_strlen()`, ASCII 16 B | 69 | −28% | −27% | 0% ~ |
| `grapheme_strlen()`, ASCII 80 B | 211 | −67% | −64% | 0% |
| `grapheme_strlen()`, ASCII 2 KB | 4,157 | −79% | −80% | 0% ~ |
| `grapheme_strlen()`, ASCII 2 KB, a lone CR every 80 B | 4,157 | −79% | −82% | 0% |
| `grapheme_strlen()`, ASCII 2 KB, CR LF every 80 B | 125,899 | +1% | +1% | 0% ~ |
| `grapheme_strlen()`, ASCII 2 KB, "é" at the start | 125,225 | +1% | +1% | 0% ~ |
| `grapheme_strlen()`, ASCII 2 KB, "é" at the end | 129,355 | −2% | −1% | +1% |
| `grapheme_strlen()`, Spanish 80 B | 5,847 | −1% | +1% | 0% ~ |
| `grapheme_strlen()`, Chinese 80 B | 3,067 | −2% | +1% | 0% ~ |
| `grapheme_strlen()`, ASCII, mixed lengths 1–24 B | 100 | −28% | −33% | 0% ~ |
| `grapheme_substr($s, 0, 8)`, ASCII, mixed lengths 1–24 B | 159 | −8% | −7% | 0% ~ |
| `grapheme_strpos($s, 'zz')`, ASCII, mixed lengths 1–24 B | 145 | −12% | −13% | 0% ~ |
| `grapheme_substr($s, 0, 8)`, ASCII 5 B | 103 | −9% | −2% | −2% |
| `grapheme_substr($s, 0, 8)`, ASCII 80 B | 258 | −53% | −53% | 0% |
| `grapheme_substr($s, 0, 8)`, ASCII 2 KB, "é" at the end | 17,422 | −19% | −19% | 0% |
| `grapheme_strpos($s, 'zz')`, ASCII 5 B | 78 | +3% | +7% | 0% |
| `grapheme_strpos($s, 'zz')`, ASCII 80 B | 262 | −54% | −54% | −1% |
| `grapheme_strpos($s, 'zz')`, ASCII 2 KB | 4,725 | −69% | −70% | 0% ~ |
| `grapheme_strpos($s, 'x')`, ASCII 1 B | 66 | +12% | +8% | 0% |
| `grapheme_strpos($s, 'x')`, ASCII 80 B | 231 | −60% | −60% | 0% ~ |
| `grapheme_stripos($s, 'Z')`, ASCII 5 B | 153 | +1% | 0% | −1% |
| `grapheme_extract($s, 8)`, ASCII 5 B | 110 | +1% | 0% | −1% |
| `grapheme_extract($s, 8)`, ASCII 2 KB | 115 | −5% | −13% | 0% |

~: within noise, the change is no larger than the difference between master and master on the same row.
<!-- /bench-table -->

Noise: the last column runs clang master against itself, as its own group after the clang group. Its medians are from −6% to +3%. The GCC control runs master against itself at the start and the end of the series: medians from −6% to +1%. The `~` mark comes from the GCC control and is put on every column. [`labels.txt`](labels.txt) maps the case names of `series.json` to these labels.

`grapheme_extract($s, 8)` checks 9 bytes, so it gains the same 5–14% from 9 bytes to 2 KB. With CR LF every 80 bytes, `grapheme_strlen()` and the others take the ICU path, which costs 13,000–221,000 cycles here. The check is a small part of it.

## Correctness checks

- **Same output as master:** [`difftest.php`](difftest.php) calls the eight functions, and `grapheme_stristr()`, on 26,470 strings and prints one MD5 per function:
  - every string of up to 6 characters from `a`, CR, LF, "é" and the invalid byte `\xFF`;
  - ASCII of 0–40 bytes with CR, LF, CR LF, "é", `\x80`, `\x7F`, NUL or `\xFF` inserted at every position, so around every 8-byte boundary;
  - texts in six languages and with CR LF lines.

  `grapheme_extract()` runs on 20,195 of these strings, with every size, the three extract types and up to 13 start offsets. [`difftest.sh`](difftest.sh) runs it on each build and compares the MD5 of stdout and stderr together. Master and the change print the same on GCC, clang, ZTS and ASan + UBSan, and ASan prints nothing ([`data/difftest.txt`](data/difftest.txt)). [`data/builds.txt`](data/builds.txt) lists the commit and the SHA-1 of each binary.
- **php-src tests** of `ext/intl`: 0 failed on GCC, clang and ZTS ([`tests.sh`](tests.sh), [`data/tests.txt`](data/tests.txt)). On ASan + UBSan seven `oom_*.phpt` tests fail on master and with the change alike: they test the memory limit, and ASan runs with `USE_ZEND_ALLOC=0`. The new test `grapheme_ascii_check_positions.phpt` puts a non-ASCII character, CR, LF, CR LF or a lone CR before CR LF at every position of 17 ASCII bytes, and runs `grapheme_extract()` with CR LF right after the checked bytes. It passes on master too ([`data/new-test-on-master.txt`](data/new-test-on-master.txt)).
- **Do the checks catch bugs?** [`mutants.sh`](mutants.sh) puts seven mistakes into the change, one at a time ([`data/mutants.txt`](data/mutants.txt)). The differential test and the new test each catch all six real bugs: CR LF not checked in the words or in the tail, the second word read at `p`, a mask that misses one byte, a byte 0x80 taken as ASCII in the tail, the last byte not checked. Without the new test, the grapheme tests of php-src catch one of them, the unchecked last byte ([`data/mutants-without-new-test.txt`](data/mutants-without-new-test.txt)). The last mutation reads the byte after the length, as master did. Both checks miss it, as they should: it gives the same results.
- **Strings over 2 GiB:** [`large-string.php`](large-string.php) calls the eight functions on 2³¹ + 8 ASCII bytes. On master every call returns false, NULL or an error, except `grapheme_extract($s, 2 ** 31 - 1)`. With the change `grapheme_strlen()` returns the length and `grapheme_strstr($s, 'a', true)` an empty string, as they do for a short string. The other calls return the same as on master, and neither build crashes. The intl error after a call is the last one set: the ASCII paths don't reset it ([`data/large-string.txt`](data/large-string.txt)).

## Not tested

- Intel CPUs and other compilers.
- Windows and big-endian CPUs: the zero-byte test doesn't depend on byte order, but I didn't run it there.
- Strings over 4 GiB. Master's `int` could hold a small positive length there. With the change the five functions with `int32_t` offsets send them to ICU.
- Other ICU versions than 78.2.
- Strings outside the CPU cache: every input of the series is 2 KB or less.
- `grapheme_strripos()` in the series. Its check is the same as in `grapheme_strrpos()`.
- A full application.
- Opcache and JIT: the harness runs `php -n`.

## Machine and method

- AMD Ryzen 9 5950X, kernel 7.0.0-42, governor `performance`, boost on. Measured on CPU 15, on the second CCD. Load average 2.6 at the start of the series, CPU 15 and its sibling 31 idle.
- GCC 15.2 and clang 21.1, builds by `bench build --profile docker`: the flags of the official Docker image (`-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64`, link `-Wl,-O1 -pie`), `--enable-werror`, `--disable-all` with the CLI and `--enable-intl`, ICU 78.2. ext/intl is C++: the image passes the same flags in `CPPFLAGS`, and so do these builds, with `CXX` matching `CC`. Without that, master builds C++ without `-O2` ([GH-25688](https://github.com/php/php-src/issues/25688)).
- The number is user-space CPU cycles of the PHP process per call (`perf stat`, minus an empty loop), of the calls in [`grapheme.php`](grapheme.php).
- `bench compare`: 15 alternating passes per call and compiler. Each pass runs master and the change back to back. A cell is the median of those per-pass changes. A `~` marks a change no larger than the master-against-master median of its row.
- The series names commit `5595f170c35`. The final commit differs from it only in the commit message, and its binaries have the same SHA-1 ([`data/builds.txt`](data/builds.txt)).

## Appendix: earlier versions

Two earlier versions, each measured in its own series on the same machine with the same master builds. They ran an earlier, smaller suite, [`earlier-grapheme.php`](earlier-grapheme.php): 56 calls on ASCII of 5, 10, 80 bytes and 2 KB and the same texts with CR, CR LF, "é" and six languages ([`FULL-TABLES.md`](FULL-TABLES.md#earlier-versions)). Only their speed was compared. The correctness checks ran on the final change only.
- [`earlier-memchr.diff`](earlier-memchr.diff), [`memchr-series.json`](memchr-series.json): the 8-byte loop for bytes above 0x7f, then `memchr()` for each CR.
- [`earlier-inword.diff`](earlier-inword.diff), [`inword-series.json`](inword-series.json): a word with a CR is checked byte by byte inside the loop.

## Reproduce

Steps, about 75 minutes on a 16-core machine: [`REPRODUCE.md`](REPRODUCE.md).
