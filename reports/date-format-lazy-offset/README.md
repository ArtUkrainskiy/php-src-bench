# date() and DateTimeInterface::format() build the time zone offset only when the format uses it

The change is on branch [`date-format-lazy-offset`](https://github.com/ArtUkrainskiy/php-src/tree/date-format-lazy-offset) of ArtUkrainskiy/php-src, also as a patch: [`date-format-lazy-offset.patch`](date-format-lazy-offset.patch).

`date()` and `DateTimeInterface::format()` turn a date into a string by a format such as `'Y-m-d H:i:s'`. For a date in a local time zone (every `date()` and `format()` call, but not `gmdate()`), PHP master works out the time zone offset of that date before it reads the format. Many common formats, such as `'Y-m-d H:i:s'`, never print it. The change works it out only when the format reaches a character that prints it. Scripts need no change and no setting.

## Summary

- **Formats that don't use the offset:** fewer CPU cycles per call than master. `format('Y-m-d H:i:s')` takes 39% fewer on GCC 15.2 and 34% fewer on clang 21.1 on Europe/Madrid, and 17% and 9% fewer on UTC. On GCC the change saves about the same number of cycles whatever the format: 484–507 per call on Europe/Madrid, 148–184 on UTC. The saving is largest on a time zone identifier with transitions, such as Europe/Madrid or America/New_York, where master also searches the zone's transitions on every call. Over all such formats it's 5–68% ([Results](#results)).
- **Paths that call it often:** `json_encode()` and `serialize()` of 100 `DateTimeImmutable` objects in Europe/Madrid take 18–23% fewer cycles, since PHP formats each date to build its properties. With `date.timezone` set to Europe/Madrid, `date('Y-m-d H:i:s')` takes 25% fewer on GCC and 21% fewer on clang ([More paths](#more-paths)).
- **Formats that use the offset, and `gmdate()`:** 0–1% more instructions than master. Their cycles move by −7% to +7% on GCC and −3% to +12% on clang. With `-falign-functions=64 -falign-loops=32` added to the same flags, they move by −2% to +8% on GCC and −5% to +5% on clang. The slower rows are not the same in the two builds. So these rows depend strongly on where the code sits, but I didn't find the exact cause ([Trade-offs](#trade-offs)).
- **Correctness:** the same output as master on over 50,000 calls, on GCC, clang, ZTS and ASan + UBSan. The ext/date tests pass on GCC, clang and ZTS. On ASan one test fails on master too ([Correctness checks](#correctness-checks)).
- **Not checked:** Intel, Windows, a full application ([Not tested](#not-tested)).

## What changes and why it is faster

Before: `date_format()` in `ext/date/php_date.c` serves `date()`, `DateTimeInterface::format()` and its procedural alias `date_format()`, among others. For a local time it first builds a `timelib_time_offset`, then walks the format. Building it allocates the structure and an abbreviation string, both freed at the end. For a time zone identifier it also calls `timelib_get_time_zone_info()`, which searches the zone's transitions for the date.

Only these format characters read the offset: `I O P p T Z c r`, and `e` for a zone given as an offset or an abbreviation. For an identifier, `e` prints the zone name.

After: the block that builds the offset is a function, `date_format_offset()`. Each of those characters first calls `date_format_need_offset()`, which, for a local time, builds the offset if it isn't built yet. The offset is freed at the end when it was built. A format without these characters never builds it. An earlier version scanned the format once before the loop instead, and cost more on formats that print the time zone ([Appendix](#appendix-an-earlier-version)).

Why the result is the same: the offset is built by the same code from the same date, before its first use. `gmdate()` passes `localtime = false` and never builds it, before or after. The [correctness checks](#correctness-checks) compare the output with master byte for byte.

## Trade-offs

- **Formats that use the offset, and `gmdate()`,** run 0–1% more instructions than master. Their cycles move by −7% to +12% depending on the compiler and the build (ranges above, rows in [Results](#results), [More paths](#more-paths) and [`FULL-TABLES.md`](FULL-TABLES.md)). Most rows above +3% are marked `layout?`: the cycles moved in every pass, the instructions by less than 0.5%. The clearest case is `gmdate('Y-m-d H:i:s')`: its path through `date_format()` calls none of the new code, only the final check reads `offset` instead of `localtime`, yet it is +8% on clang and −3% on GCC in the main build, and −2% on clang and +4% on GCC in the aligned one.
- **One row in detail:** `format('c')` on +05:30, clang, main build ([`data/placement-clang.md`](data/placement-clang.md)). Instructions and branches differ by less than 0.5%, and branch and instruction-cache misses round to zero on both sides. `date_format()` itself takes 4% of the cycles instead of 7%. Two thirds of the cycles are in `strx_printv()`, the printf engine behind `slprintf()`, which the change doesn't touch. `slprintf()` and the functions next to it moved by 176 bytes. I didn't look at the GCC rows in this way.
- **Code size:** `date_format()` is 107 bytes smaller in the clang build, 2,983 bytes instead of 3,090.

## Results

Change in CPU cycles per call against master (negative = fewer cycles, faster). Each compiler is compared with master built by the same compiler. The rows name the zone of the `DateTimeImmutable`: an identifier (UTC, Europe/Madrid, America/New_York), an offset (+05:30) or an abbreviation (EST). `date()` runs with the default zone, UTC. The first nine rows print no time zone, the last six do. The range over the passes, the change in instructions, all 58 calls and the master-against-master control are in [`FULL-TABLES.md`](FULL-TABLES.md).

<!-- bench-table series.json --labels labels.txt --no-control -->
| call | master, CPU cycles per call (GCC 15.2) | GCC 15.2 | clang 21.1 |
|---|--:|--:|--:|
| `format('Y')`, UTC | 416 | −42% | −26% |
| `format('Y')`, Europe/Madrid | 746 | −68% | −63% |
| `format('Y-m-d H:i:s')`, UTC | 1,039 | −17% | −9% |
| `format('Y-m-d H:i:s')`, Europe/Madrid | 1,258 | −39% | −34% |
| `format('Y-m-d H:i:s')`, +05:30 | 1,080 | −20% | −18% |
| `format('Y-m-d H:i:s')`, EST | 985 | −12% | −8% |
| `format('Y-m-d\TH:i:s.u')`, America/New_York | 1,398 | −34% | −29% |
| `date('Y-m-d')`, UTC | 866 | −17% | −10% |
| `date('Y-m-d H:i:s')`, UTC | 1,277 | −12% | −5% |
| `format('c')`, UTC | 812 | +1% | +8% layout? |
| `format('c')`, Europe/Madrid | 1,125 | +2% | +5% layout? |
| `format('c')`, +05:30 | 832 | +6% layout? | +12% layout? |
| `format('Y-m-d\TH:i:sP')`, Europe/Madrid | 1,468 | −1% | +7% layout? |
| `format('D, d M Y H:i:s O')`, +05:30 | 1,390 | 0% ~ | +6% layout? |
| `date(DATE_ATOM)`, UTC | 1,433 | −2% | +3% |

~: within noise, the change is no larger than the difference between master and master on the same row.

layout?: in every pass the cycles changed in the same direction, by 3% or more in the median, the instructions by less than 0.5%: the work is the same, so look for the cause (code placement, branch prediction) with `bench why` before reporting the row.
<!-- /bench-table -->

Noise: master against master on GCC moves single passes by −10% to +7%, with medians within 1%. The clang column of this series has no such control of its own, the series in [More paths](#more-paths) has one ([Machine and method](#machine-and-method)). [`labels.txt`](labels.txt) maps the case names of `series.json` to these labels.

## More paths

A second series covers paths around the change ([`date-extra.php`](date-extra.php), [`extra-series.json`](extra-series.json)): `json_encode()` and `serialize()` of an array of 100 dates one day apart, `date()` with Europe/Madrid as the default zone, `gmdate()`, and formats with `p`, `e` or several characters that use the offset. Same builds, 15 passes. The last column runs clang master against itself as its own control.

<!-- bench-table extra-series.json --labels extra-labels.txt --no-control -->
| call | master, CPU cycles per call (GCC 15.2 (gcc15)) | GCC 15.2 (gcc15) | clang 21.1 (clang21) | clang 21.1 (clang21-aa) |
|---|--:|--:|--:|--:|
| `json_encode()` of 100 dates, UTC | 182,579 | −9% | −1% | 0% ~ |
| `json_encode()` of 100 dates, Europe/Madrid | 218,476 | −22% | −20% | 0% |
| `serialize()` of 100 dates, UTC | 194,702 | −9% | −1% | 0% |
| `serialize()` of 100 dates, Europe/Madrid | 232,803 | −23% | −18% | 0% ~ |
| `date('Y-m-d')`, default zone Europe/Madrid | 1,541 | −31% | −28% | 0% ~ |
| `date('Y-m-d H:i:s')`, default zone Europe/Madrid | 1,947 | −25% | −21% | 0% ~ |
| `date(DATE_ATOM)`, default zone Europe/Madrid | 2,111 | −1% | +3% layout? | 0% ~ |
| `format('e')`, Europe/Madrid | 687 | −69% | −68% | 0% ~ |
| `format('e')`, EST | 291 | +1% | −2% | 0% |
| `gmdate('Y-m-d H:i:s')` | 892 | −3% | +8% layout? | 0% ~ |
| `gmdate('c')` | 639 | 0% ~ | +11% layout? | 0% ~ |
| `gmdate('D, d M Y H:i:s \G\M\T')` | 1,039 | −2% | +3% | 0% ~ |
| `format('p')`, +05:30 | 525 | +2% | +6% layout? | 0% ~ |
| `format('Y-m-d H:i:s T (P)')`, Europe/Madrid | 1,664 | −1% | +7% layout? | 0% |
| `format('P T e I Z')`, +05:30 | 1,000 | −2% | +6% | 0% |

~: within noise, the change is no larger than the difference between master and master on the same row.

layout?: in every pass the cycles changed in the same direction, by 3% or more in the median, the instructions by less than 0.5%: the work is the same, so look for the cause (code placement, branch prediction) with `bench why` before reporting the row.
<!-- /bench-table -->

`json_encode()`, `serialize()`, `var_export()` and `(array)` of a date object format it with `'x-m-d H:i:s.u'`, which doesn't use the offset. The aligned builds of this series are in [`FULL-TABLES.md`](FULL-TABLES.md#more-paths-aligned-builds).

## Correctness checks

- **Same output as master:** [`difftest-chars.php`](difftest-chars.php) prints every letter from `a` to `Z` as a format, escapes and full formats on 16 dates, and `date()` and `gmdate()` of each. [`difftest-random.php`](difftest-random.php) prints fixed edge formats on 24 dates, and 50,000 random formats of up to 12 characters (seed 1), each on one of those dates picked at random. It also prints `date()` and `gmdate()` of the fixed formats and single characters with three default zones. The dates cover time zone identifiers with and without daylight saving time, offsets in minutes and in seconds (`+05:45:30`), abbreviations, Unix timestamps, and years from `PHP_INT_MIN` to `PHP_INT_MAX`. [`difftest.sh`](difftest.sh) runs both on each build and compares MD5s of stdout and stderr together. Master and the change print the same on GCC, clang, ZTS and ASan + UBSan, and ASan prints nothing ([`data/difftest.txt`](data/difftest.txt)).
- **php-src tests** of `ext/date`: 0 failed on GCC, clang and ZTS ([`tests.sh`](tests.sh), [`data/tests.txt`](data/tests.txt)). On ASan + UBSan `ExtendDateTime.phpt` fails on master and with the change alike. The new test `date_format_escaped_timezone_chars.phpt` prints the characters that use the offset escaped, then unescaped and several in one format, on UTC, Europe/Madrid, an offset and an abbreviation, and the same with `gmdate()`. It passes on master too.
- **Do the checks catch bugs?** [`mutants.sh`](mutants.sh) puts four mistakes into the change, one at a time ([`data/mutants-release.txt`](data/mutants-release.txt), [`data/mutants-asan.txt`](data/mutants-asan.txt)). "Caught" means `difftest.sh` sees a different output or a crash. A missing build before `T` or before `e` on an abbreviation, and a free of an offset that wasn't built, are caught by the differential test. The new test catches the first three on its own. Building the offset again at every time zone character gives the same output and leaks memory. Only the ASan build catches it.

## Not tested

- Intel CPUs and other compilers.
- Windows.
- A full application.
- Different dates in the same loop: each call formats the same date, except the 100 dates of the serialization rows.
- Opcache and JIT: the harness runs `php -n`.

## Machine and method

- AMD Ryzen 9 5950X, kernel 7.0.0-42, governor `performance`, boost on. Measured on CPU 15, on the second CCD. The load average was 3.8 at the start of the main series, from builds and tests that had just finished on other cores ([`data/environment.txt`](data/environment.txt)).
- GCC 15.2 and clang 21.1, builds by `bench build --profile docker`: the flags of the official Docker image (`-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64`, link `-Wl,-O1 -pie`), `--enable-werror`, `--disable-all` with the CLI.
- The number is user-space CPU cycles of the PHP process per call (`perf stat`, minus an empty loop), of the calls in [`date.php`](date.php) and [`date-extra.php`](date-extra.php). Each call formats one `DateTimeImmutable` made before the loop, or one Unix timestamp with `date()`.
- `bench compare`: 15 alternating passes per call and compiler. Each pass runs master and the change back to back. A cell is the median of those per-pass changes. The A/A control runs master against itself at the start and at the end, on GCC 15.2. In the main series its medians are within 1% of zero on every row, and single passes range from −10% to +7%. The main series has no control for clang. The second series has one: clang master against itself in every pass, medians within 1% of zero. A `~` marks a change no larger than the A/A median of its row. `layout?` marks a row where the cycles moved by 3% or more in every pass and the instructions by less than 0.5%.

## Appendix: an earlier version

The first version scanned the whole format for these characters before the loop, and built the offset if it found one. It gave about the same gain on formats without them. On formats with them it ran 0–3% more instructions than master, 2–3% on `P`, `O` and `DATE_ATOM`, and up to 10% more cycles on clang ([`FULL-TABLES.md`](FULL-TABLES.md#earlier-version-scan-before-the-loop), [`earlier-series.json`](earlier-series.json)). That's why the change builds the offset at the first character that needs it instead.

## Reproduce

Steps, about 70 minutes on a 16-core machine: [`REPRODUCE.md`](REPRODUCE.md). The series in this report: [`series.json`](series.json), [`align-series.json`](align-series.json), [`extra-series.json`](extra-series.json), [`extra-align-series.json`](extra-align-series.json), [`earlier-series.json`](earlier-series.json).
