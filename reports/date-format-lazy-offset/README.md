# date() and DateTimeInterface::format() build the time zone offset only when the format uses it

The change is on branch [`date-format-lazy-offset`](https://github.com/ArtUkrainskiy/php-src/tree/date-format-lazy-offset) of ArtUkrainskiy/php-src, also as a patch: [`date-format-lazy-offset.patch`](date-format-lazy-offset.patch).

`date()` and `DateTimeInterface::format()` turn a date into a string by a format such as `'Y-m-d H:i:s'`. For any date in a time zone, that is every call except `gmdate()`, PHP master works out the time zone offset of that date before it reads the format. Most formats never print it. The change works it out only when the format reaches a character that prints it. Scripts need no change and no setting.

## Summary

- **Formats that don't print the time zone:** fewer CPU cycles per call than master. `format('Y-m-d H:i:s')` takes 39% fewer on GCC 15.2 and 34% fewer on clang 21.1 on Europe/Madrid, and 17% and 9% fewer on UTC. The gain is largest on a time zone identifier with transitions, such as Europe/Madrid or America/New_York, where master also searches the zone's transitions on every call. Over all such formats it's 5–68%, the 68% on `format('Y')` and `format('U')` on Europe/Madrid ([Results](#results)).
- **Formats that print it** (`c`, `DATE_ATOM`, `P`, `O`, `T`): up to 7% more cycles on GCC and up to 12% more on clang, with 0–1% more instructions. On the one clang row I profiled, `format('c')` on +05:30, the extra cycles are in the printf code, which the change doesn't touch but which now sits at another address. That fits code placement, but I didn't confirm it, and I didn't look at GCC. Another build of the same code, without PIE and with aligned functions, gives −5% to +3% on these rows ([Trade-offs](#trade-offs)).
- **Correctness:** the same output as master on over 50,000 calls, on GCC, clang, ZTS and ASan + UBSan. The ext/date tests pass on GCC, clang and ZTS. On ASan one test fails on master too ([Correctness checks](#correctness-checks)).
- **Not checked:** Intel, Windows, a full application, and `date()` with a default zone such as `Europe/Madrid` ([Not tested](#not-tested)).

## What changes and why it is faster

Before: `date_format()` in `ext/date/php_date.c` serves `date()`, `DateTimeInterface::format()` and its procedural alias `date_format()`, among others. For a local time it first builds a `timelib_time_offset`, then walks the format. Building it allocates the structure and an abbreviation string, both freed at the end. For a time zone identifier it also calls `timelib_get_time_zone_info()`, which searches the zone's transitions for the date.

Only these format characters read the offset: `I O P p T Z c r`, and `e` for a zone given as an offset or an abbreviation. For an identifier, `e` prints the zone name.

After: the block that builds the offset is a function, `date_format_offset()`. Each of those characters first calls `date_format_need_offset()`, which, for a local time, builds the offset if it isn't built yet. The offset is freed at the end when it was built. A format without these characters never builds it. An earlier version scanned the format once before the loop instead, and cost more on formats that print the time zone ([Appendix](#appendix-an-earlier-version)).

Why the result is the same: the offset is built by the same code from the same date, before its first use. `gmdate()` passes `localtime = false` and never builds it, before or after. The [correctness checks](#correctness-checks) compare the output with master byte for byte.

## Trade-offs

- **Formats that print the time zone** run 0–1% more instructions than master. Their cycles move by −3% to +12%. Most rows above +3% are marked `layout?`: the cycles changed in every pass, the instructions by less than 0.5%. I looked at one row, `format('c')` on +05:30 on clang ([`data/placement-clang.md`](data/placement-clang.md)). Instructions and branches differ by less than 0.5%, branch and instruction-cache misses are zero on both sides. `date_format()` itself takes 4% of the cycles instead of 7%. Two thirds of the cycles are in `strx_printv()`, the printf engine behind `slprintf()`, which the change doesn't touch. `slprintf()` and the allocator moved by 176 bytes. That fits code placement, but I didn't find the mechanism. I didn't look at the GCC rows.
- **Another build of the same code:** with plain `-O2 -g -falign-functions=64 -falign-loops=32`, without the PIE and stack protector flags of the main series, all formats that print the time zone, on the five zones, are −5% to +3% on clang and −3% to +5% on GCC. 7 passes, load average 9.0 ([`FULL-TABLES.md`](FULL-TABLES.md#aligned-builds)). So the sign of these rows depends on the build. This series changes two things at once, so it doesn't isolate alignment.
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

Noise: master against master on GCC moves single passes by −10% to +7%, with medians within 1%. The clang column has no such control of its own ([Machine and method](#machine-and-method)). [`labels.txt`](labels.txt) maps the case names of `series.json` to these labels.

## Correctness checks

- **Same output as master:** [`difftest-chars.php`](difftest-chars.php) prints every letter from `a` to `Z` as a format, escapes and full formats on 16 dates, and `date()` and `gmdate()` of each. [`difftest-random.php`](difftest-random.php) prints fixed edge formats on 24 dates, and 50,000 random formats of up to 12 characters (seed 1), each on one of those dates picked at random. It also prints `date()` and `gmdate()` of the fixed formats and single characters with three default zones. The dates cover time zone identifiers with and without daylight saving time, offsets in minutes and in seconds (`+05:45:30`), abbreviations, Unix timestamps, and years from `PHP_INT_MIN` to `PHP_INT_MAX`. [`difftest.sh`](difftest.sh) runs both on each build and compares MD5s of stdout and stderr together. Master and the change print the same on GCC, clang, ZTS and ASan + UBSan, and ASan prints nothing ([`data/difftest.txt`](data/difftest.txt)).
- **php-src tests** of `ext/date`: 0 failed on GCC, clang and ZTS ([`tests.sh`](tests.sh), [`data/tests.txt`](data/tests.txt)). On ASan + UBSan `ExtendDateTime.phpt` fails on master and with the change alike. The new test `date_format_escaped_timezone_chars.phpt` prints the nine time zone characters escaped, and `T` unescaped, on an identifier, an offset and an abbreviation. It passes on master too.
- **Do the checks catch bugs?** [`mutants.sh`](mutants.sh) puts four mistakes into the change, one at a time ([`data/mutants-release.txt`](data/mutants-release.txt), [`data/mutants-asan.txt`](data/mutants-asan.txt)). "Caught" means `difftest.sh` sees a different output or a crash. A missing build before `T` or before `e` on an abbreviation, and a free of an offset that wasn't built, are caught by the differential test. On the release build the new test catches the first and the third. Building the offset again at every time zone character gives the same output and leaks memory. Only the ASan build catches it.

## Not tested

- Intel CPUs and other compilers.
- Windows.
- A full application.
- `date()` with a default zone set to an identifier, such as `date.timezone=Europe/Madrid`. Only `format()` was measured on identifiers.
- Different dates in the same loop: each call formats the same date.
- Opcache and JIT: the harness runs `php -n`.

## Machine and method

- AMD Ryzen 9 5950X, kernel 7.0.0-42, governor `performance`, boost on. Measured on CPU 15, on the second CCD. The load average was 3.8 at the start of the main series, from builds and tests that had just finished on other cores ([`data/environment.txt`](data/environment.txt)).
- GCC 15.2 and clang 21.1, builds by `bench build --profile docker`: the flags of the official Docker image (`-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64`, link `-Wl,-O1 -pie`), `--enable-werror`, `--disable-all` with the CLI.
- The number is user-space CPU cycles of the PHP process per call (`perf stat`, minus an empty loop), of the calls in [`date.php`](date.php). Each call formats one `DateTimeImmutable` made before the loop, or one Unix timestamp with `date()`.
- `bench compare`: 15 alternating passes per call and compiler. Each pass runs master and the change back to back. A cell is the median of those per-pass changes. The A/A control runs master against itself at the start and at the end, on GCC 15.2 only. Its medians are within 1% of zero on every row, and single passes range from −10% to +7%. The clang column has no control of its own. A `~` marks a change no larger than the A/A median of its row. `layout?` marks a row where the cycles moved by 3% or more in every pass and the instructions by less than 0.5%.

## Appendix: an earlier version

The first version scanned the whole format for these characters before the loop, and built the offset if it found one. It gave about the same gain on formats without them. On formats with them it ran 0–3% more instructions than master, 2–3% on `P`, `O` and `DATE_ATOM`, and up to 10% more cycles on clang ([`FULL-TABLES.md`](FULL-TABLES.md#earlier-version-scan-before-the-loop), [`earlier-series.json`](earlier-series.json)). That's why the change builds the offset at the first character that needs it instead.

## Reproduce

Steps, about an hour on a 16-core machine: [`REPRODUCE.md`](REPRODUCE.md). The series in this report: [`series.json`](series.json), [`align-series.json`](align-series.json), [`earlier-series.json`](earlier-series.json).
