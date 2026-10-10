# ext/csv (php-src PR #24199) against the built-in CSV functions

Review material for [php/php-src#24199](https://github.com/php/php-src/pull/24199), the
`csv_extension` RFC: a port of [girgias/csv](https://gitlab.com/Girgias/csv-php-extension)
0.6.0 plus a new stream mode. Two rounds: the first on PR head
[`38e463a9641`](https://github.com/php/php-src/pull/24199/commits/38e463a9641d347d9ed648f3e308f864852dc30d)
(2026-10-09 morning), the second on
[`121c02fc62d`](https://github.com/php/php-src/pull/24199/commits/121c02fc62da8bed0e53b29541bdecee43892614)
after the author's fixes the same evening. Built with `--enable-csv --enable-werror`; the
built-ins on master
[`0dcfd997990`](https://github.com/php/php-src/commit/0dcfd99799044492f6c61ab67ceb634ea11354bf)
and on the same master with [#24207](https://github.com/php/php-src/pull/24207).

## Findings (as of 121c02fc62d)

1. The RFC's claim that the built-ins "cannot be fixed without breaking compatibility" does not
   hold: `$escape` is fixed by the 8.4 deprecation; the locale dependence goes away for ASCII
   bytes with #24207 (`fgetcsv()` 4,210 → 500 ns per row, the rest is `isspace()` and CJK
   trail-byte protection); multibyte tokens and `str_putcsv()` are additions; `[null]` and the
   dropped space before an enclosure are documented lenient parsing, enclosing fields with
   spaces on output is allowed by RFC 4180 §2.5.
2. On every input that follows RFC 4180 section 2, `fgetcsv(escape: '')` and
   `Csv\buffer_to_collection()` return the same result. They differ only on malformed input:
   since `121c02fc62d` ext/csv rejects all of it (including LF-only files with the default
   dialect), `fgetcsv()` is lenient. Table below, full output in `rfc4180-matrix.txt`.
3. ext/csv at `121c02fc62d`: every defect from the first round is fixed (use-after-free with a
   generator, quadratic rescan, six smaller ones), the rewritten parser passes a 4,000-row
   round-trip fuzz and valgrind, and reads faster than `fgetcsv()` with #24207 (plain file
   468 vs 500 ns per row, buffer 272 vs 505); writing stays 7–20% slower than `fputcsv()`.
4. What remains is a property of the "multibyte delimiters" feature, present in the original
   too: dialects whose tokens overlap with field content don't round-trip
   (`['-', 'z']` with delimiter `--` → `---z` → `["", "-z"]`). RFC v1.1 lists it as an open issue.
5. The PR fixes three real bugs of the original (sparse array loops forever, `row_to_array('')`
   reads past the buffer, enclosure re-matched against its own tail).

## First round: PR head 38e463a9641

Findings at the time, superseded where the follow-up says so: `fgetcsv()` was slower than
ext/csv only because of `php_mblen()`; with #24207 the built-ins read 2–4× faster than that
head; ext/csv accepted `"a"b` and an unterminated quote and parsed LF-only files into one row
silently; two blockers (use-after-free, quadratic rescan).

## Speed (38e463a9641)

`bench.php`, best of 5, ns per row, release builds, i7-13700H. Data from `gen.php`: 20,000
rows; "plain" 10 unquoted fields, "quoted" 10 fields with ~30% needing enclosure (commas,
quotes, newlines), "wide" 50 fields. `escape: ''` everywhere.

| | master | master + #24207 | ext/csv |
|---|---|---|---|
| read a file, plain | `fgetcsv()` 4,210 | 501 | `createFromFile()` 1,695 |
| read a file, quoted | 5,117 | 726 | 1,922 |
| read a file, wide | 20,709 | 2,139 | 8,232 |
| read a buffer, plain | `str_getcsv()` per line 4,186 | 522 | `buffer_to_collection()` 1,018, `createFromBuffer()` 1,007 |
| read a buffer, quoted | 5,057 | 698 | 1,046, 1,091 |
| read a buffer, wide | 20,664 | 2,298 | 4,865 (needs `memory_limit` > 128M), 4,689 |
| write, plain | `fputcsv()` 324 | 324 | `collection_to_buffer()` 362, `collection_to_file()` 367 |
| write, quoted | 426 | 424 | 481, 502 |
| write, wide | 1,605 | 1,590 | 1,834, 1,866 |

Where the time goes (callgrind, plain file, instructions per row): `fgetcsv()` on master
78,751, 83% in `mbrtowc`/gconv/`mblen` (`php_mblen()` once per byte); ext/csv 24,441, 36% in
`memcmp` (once per byte for the delimiter/enclosure/EOL checks) and 37% in its two parse
functions.

## RFC 4180 (matrix regenerated on 121c02fc62d)

`probes/rfc4180.php` feeds the same inputs to `fgetcsv()` with `escape: ''` and to
`Csv\buffer_to_collection()`; `rfc4180-matrix.txt` is the full output. The differences:

| input | `fgetcsv()` | ext/csv |
|---|---|---|
| LF-only `a,b\nc,d\n` | `[[a,b],[c,d]]` | ValueError (was `[[a,"b\nc","d\n"]]` silently before 121c02fc62d) |
| `a"b,c` (quote in an unquoted field) | `[a"b, c]` | ValueError |
| BOM then `"a",b` (Excel "CSV UTF-8") | `[BOM"a", b]`, quotes kept | ValueError |
| `a\"b,c` | literal | ValueError |
| ` "a",b` (space before the quote) | `[a, b]` | ValueError |
| `"a" ,b` (space after the quote) | `[a , b]` | ValueError (was `[a , b]`) |
| `"a"b,c` (junk after the quote) | `[ab, c]` | ValueError (was `[ab, c]`) |
| `"a,b\r\nc,d\r\n` (unterminated) | one field | ValueError (was one field) |
| empty line between rows | `[null]` | ValueError (field count) |
| writer, `['a b','c']` | `"a b",c\n` | `a b,c\r\n` |

Both writers are compliant: section 2.5 allows enclosing any field, and `fputcsv()` writes
CRLF when `$eol` says so. RFC 4180 (Informational) quotes Postel in section 2: be liberal in
what you accept.

## Defects in the PR (38e463a9641, all fixed in 121c02fc62d)

Reproducers in `probes/`.

- **Use-after-free.** `collection_to_buffer()`/`collection_to_file()` iterate the row from
  `get_current_data()` without an addref; a `Stringable` element whose `__toString()` resumes
  the generator frees the row. `probes/uaf.php` under `USE_ZEND_ALLOC=0 valgrind`: invalid read
  in `hashtable_to_rfc4180_string` (csv.c:135), block freed by `zend_array_destroy` in
  `ZEND_YIELD`. Also in girgias/csv 0.6.0.
- **Quadratic rescan.** `createFromFile()` scans the row from its start after every 8 KiB
  read. One enclosed field: 1 MB 0.09 s, 2 MB 0.35 s, 4 MB 1.38 s, 8 MB 5.38 s;
  `buffer_to_collection()` on the 4 MB bytes 0.01 s. An unterminated `"` at the start of a
  large file does not finish.
- `row_to_array("a,b\r\nc,d")` returns `[a, b]`; the rest is dropped without an error.
- A collection element that is a reference is `TypeError: Element 0 of the collection must be
  an array` (no `ZVAL_DEREF`); `[&$row]` works with `foreach`.
- Iteration state lives on the collection, not the iterator: `foreach ($c as $a) foreach ($c
  as $b)` gives 3 pairs instead of 9.
- Stream open errors lose their reason: `php_stream_open_wrapper_ex(..., 0, NULL, NULL)` has
  no `REPORT_ERRORS` and no default context, so a missing file is `Error: Failed to open
  "…" for reading` and `stream_context_set_default()` is ignored.
- The stream is detached from its resource (`res->type = -1`, `zend_list_delete()`) to make it
  private, instead of the `PHP_STREAM_FLAG_NO_FCLOSE` pattern of spl_directory.c. A collection
  alive at shutdown never calls a user wrapper's `stream_close()` (`probes/t5_close.php`:
  `fopen()` does), and a `compress.zlib://` descriptor leaks (acknowledged in csv.c:813).
- `"a"b` → `[ab]` and an unterminated enclosure are accepted silently while `a"b` is a
  ValueError.

## Bugs of the original fixed by the PR

`probes/bugs.php` against a `.so` built from the GitLab tree at [`d312915`](https://gitlab.com/Girgias/csv-php-extension/-/commit/d312915) (0.6.0):
`collection_to_buffer()` with a hole in the array loops forever; `row_to_array('')` returns
`[" "]` (read past the buffer); enclosure `aa` with field `aaa` gives `["aaa\n"]` (the enclosure
is re-matched against its own tail). The PR's "six upstream bugs" — these three are the ones I
could identify; gl14–16 in the tracker were reported by someone else and fixed upstream in July and August.

## Files

- `bench.php <datadir> <case>[:plain|quoted|wide]` — the timings; `gen.php <dir>` makes the data
- `probes/rfc4180.php` — the conformance matrix; `rfc4180-matrix.txt` is its output on the PR build
- `probes/uaf.php`, `probes/bugs.php` — reproducers
- `probes/t1..t6_*.php` — parser edge cases, streams, user wrappers, close at shutdown, legacy comparison

## Follow-up: PR head 121c02fc62d (2026-10-09)

The author's [reply](https://github.com/php/php-src/pull/24199#issuecomment-6087825865) came with a 541-line
change to csv.c. Re-checked on that head, same builds and data:

- Use-after-free: valgrind clean on `probes/uaf.php` and `probes/t2_uaf.php`.
- Rescan: 4 MB quoted field 0.01 s, 8 MB 0.03 s, 32 MB 0.06 s; an unterminated `"` in 8 MB
  raises `ValueError` in 0.01 s.
- Every smaller item fixed as described (`probes/verify_claims.php` equivalent in `t1`–`t6`).
- Parser now rejects everything that doesn't follow RFC 4180 section 2, LF-only files with the
  default dialect included; `rfc4180-matrix.txt` is its output on this head.
- Speed, same `bench.php`, ns per row: read a file plain 468 (`fgetcsv()` + #24207: 500),
  quoted 576 (700), wide 2,003 (2,145); read a buffer plain 272 (`str_getcsv()` + #24207: 505);
  write plain 358 (`fputcsv()` 336).
- `probes/csvfuzz.php`: 4,000 random rows (NUL, CR/LF, `\xC3`, token bytes in the fields) through
  `collection_to_buffer` → `buffer_to_collection` / `createFromBuffer` / `createFromFile` /
  `row_to_array`: 0 mismatches and 0 exceptions in the seven dialects whose tokens don't overlap;
  valgrind clean on 600 of them; multibyte tokens across the 8 KiB read boundary (field lengths
  8180–8200) fine.

What remains, and predates the port (girgias/csv 0.6.0 does the same): dialects whose tokens
overlap with field content don't round-trip, because the writer doesn't enclose a field when a
token appears across the field/delimiter boundary (`probes/minimal.php`, `probes/minimal2.php`):

```
['-', 'z']  delimiter "--" enclosure "aa"  -> "---z\r\n"  -> ["", "-z"]
['x', 'x']  delimiter "xy" enclosure "xyx" -> "xxyx\n"    -> ValueError (was: parsed as ["yx"])
```

In the fuzz: `xy`/`xyx` 365 of 560 cases, `--`/`aa` 43 of 549.
