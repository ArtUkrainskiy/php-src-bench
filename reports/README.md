# Reports

Results that are cited somewhere, usually in a php-src pull request, with everything needed to
check them: what was compared, the full tables, how the output was verified and the commands to
run it again.

| Report | Subject | php-src PR |
|---|---|---|
| [substr-adaptive-search](substr-adaptive-search/) | Forward substring search: final product report, 233 cases, six compiler/CPU pairs, elapsed time, cycles, instructions and remaining regressions | not opened yet |
| [json-encode-utf8-inline](json-encode-utf8-inline/) | `json_encode()`: decode valid UTF-8 inline | [#24283](https://github.com/php/php-src/pull/24283) |
| [fgetcsv-mblen](fgetcsv-mblen/) | `php_mblen()`: skip `mbrlen()` for ASCII bytes (`fgetcsv()`, `str_getcsv()`, `escapeshell*()`) | [#24207](https://github.com/php/php-src/pull/24207) |
| [deprecation-cost](deprecation-cost/) | What a deprecated call costs, and `#[\Deprecated]` without constructing the attribute | [#24198](https://github.com/php/php-src/pull/24198) |
| [list-assign-from-array-literal](list-assign-from-array-literal/) | `[$a, $b] = [$b, $a]` compiled without the array | [#24180](https://github.com/php/php-src/pull/24180) |
| [htmlspecialchars-ascii-fast-path](htmlspecialchars-ascii-fast-path/) | A fast path for ASCII in `htmlspecialchars()` | [#24145](https://github.com/php/php-src/pull/24145) |
| [htmlspecialchars-vs-23957](htmlspecialchars-vs-23957/) | `htmlspecialchars()`: #23957 and #24145 together | [#23957](https://github.com/php/php-src/pull/23957), [#24145](https://github.com/php/php-src/pull/24145) |
| [csv-pr-24199](csv-pr-24199/) | ext/csv (the `csv_extension` RFC) against the built-in CSV functions | [#24199](https://github.com/php/php-src/pull/24199) (review) |
| [pr-23517-array-shift](pr-23517-array-shift/) | `array_shift()`: one `memmove()` for hole-free packed arrays | [#23517](https://github.com/php/php-src/pull/23517) (review) |
| [pr-22648-array-diff](pr-22648-array-diff/) | `array_diff()` of ints through a bitset | [#22648](https://github.com/php/php-src/pull/22648) (review) |
| [pr-24157-array-push](pr-24157-array-push/) | `array_push()` appending to packed arrays in bulk | [#24157](https://github.com/php/php-src/pull/24157) (review) |
| [pr-23189-var-export](pr-23189-var-export/) | `var_export()` without temporary strings: 32-bit overflow, long-string regression, a one-pass variant | [#23189](https://github.com/php/php-src/pull/23189) (review) |
| [pr-23961-html-charset](pr-23961-html-charset/) | html functions: UTF-8 first when resolving the charset; alone and with #23957 and #24145 | [#23961](https://github.com/php/php-src/pull/23961) (review) |
| [pr-23110-unserialize-var-access](pr-23110-unserialize-var-access/) | `unserialize()`: back-references found by chunk index instead of a list walk; measurements, correctness, a variant without the GCC per-value cost | [#23110](https://github.com/php/php-src/pull/23110) (review) |
| [pr-23789-bin2hex-hex2bin](pr-23789-bin2hex-hex2bin/) | `bin2hex()`/`hex2bin()` with SSE2/NEON: measurements, big-endian AArch64 result, a variant without the short-input cost | [#23789](https://github.com/php/php-src/pull/23789) (review) |
| [pdo-pgsql-stmt-cache](pdo-pgsql-stmt-cache/) | pdo_pgsql: a per-connection cache of prepared statements, measured on Drupal 11.4 | not opened yet |
| [mysqlnd-zts-stats](mysqlnd-zts-stats/) | mysqlnd: relaxed atomics instead of a mutex for statistics in ZTS builds | not opened yet |
| [base64-decode-quads](base64-decode-quads/) | `base64_decode()`: four characters at a time in the character loop | not opened yet |
| [php-benchmark-history](php-benchmark-history/) | php-src's benchmark CI, read as a history | — |

## Adding a report

One directory per change:

```sh
mkdir reports/<name>
./bench run <suite> --a base --b <build> --perf --wait-idle 600   # default rounds, quiet machine
sed "s|$(dirname "$PWD")/|../|g" results/<file>.json > reports/<name>/<suite>.json
./bench show reports/<name>/<suite>.json --md             # the table for README.md
```

The `sed` strips the absolute paths of your machine from the result. `README.md` of a report says:

- which two commits were compared, with links, and what the change is;
- the machine and its state during the run (governor, load, whether warnings were printed);
- a summary by kind of input, including what got slower or did not change;
- the full table of every suite that was run;
- how the output was verified (`bench difftest`, tests, sanitizers);
- the commands to reproduce it.

Build both sides from commits, not from a working tree snapshot, so that the report names
something others can check out. Numbers from other tools, such as php-src's
`benchmark/benchmark.php`, belong in the report too, with a sentence on how they were obtained.
