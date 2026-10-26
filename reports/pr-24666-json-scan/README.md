# ext/json: speed up scanning and escaping of strings (PR #24666) — review

Review of [PR #24666](https://github.com/php/php-src/pull/24666). The PR vectorizes the JSON string scanner (`json_decode`, `json_validate`) and the string escaper (`json_encode`). This report measures it on real backend JSON of several shapes, plus a synthetic sweep, on an AMD Ryzen 9 5950X with GCC 15.2 and clang 21.1. Measured on 26 October 2026.

## Summary

**Verdict: correct in every case, but a trade-off, not a clear win — big wins on ASCII and on `json_encode` with `JSON_UNESCAPED_UNICODE`, a real, instruction-backed regression on the default `json_encode` and all `json_decode` of non-Latin text, which has no opt-out.** In the tables below a negative percentage is fewer cycles (faster).

- Big win: `json_encode` with `JSON_UNESCAPED_UNICODE` on non-Latin text (−36% to −61%), and text-heavy ASCII (English posts −26% to −37%).
- Regression on non-Latin text in the default paths: `json_decode` +22% to +52% on raw UTF-8 (the escaped document +4% to +14%), default `json_encode` +3% to +8%. `json_decode` has **no mode flag to opt out**. But these are an upper bound (the test text is almost fully non-ASCII); break-even is around 10–15% non-ASCII characters, so mixed real content regresses less.
- Output identical to master (differential fuzzing, mutation-tested), clean under ASan/UBSan. A proposed fast-bail (not in the PR) cuts the decode regression but does not remove it.

Instructions per call are the real added work and do not depend on the machine (decode raw is +19% to +25%, default encode up to +15%). Cycle percentages are specific to this AMD box and will differ on other CPUs, though the direction holds; it also held on an Intel i7-13700H. To regenerate the tables (no build) or rebuild, see Reproduce at the end.

The rows are real dummyjson responses; the localized ones have their free-text fields refilled in each language, keeping the real structure, keys and numbers. Each series also ran master against itself as a control; every control row was within ±1%, so the machine was quiet (details in Method). Watch one row: `json_encode, English users` is +6% cycles but flat instructions, so it is code placement, not added work (see Trade-offs).

<!-- bench-table 20261026-amd-dummy-head.json --labels labels-head.txt --no-control -->
| call | master, CPU cycles per call (GCC 15.2) | GCC 15.2 | clang 21.1 |
|---|--:|--:|--:|
| json_encode, English products (flat) | 2,122,081 | −4% | −4% |
| json_encode, English users (nested) | 2,567,988 | +6% | +4% |
| json_encode, English posts (text) | 486,675 | −26% | −27% |
| json_encode, Russian posts | 2,397,606 | +6% | +3% |
| json_encode, Arabic quotes | 3,930,056 | +8% | +6% |
| json_encode UNESCAPED_UNICODE, Russian comments | 709,388 | −36% | −41% |
| json_encode UNESCAPED_UNICODE, Russian posts | 2,908,962 | −52% | −59% |
| json_encode UNESCAPED_UNICODE, Chinese posts | 2,840,961 | −57% | −61% |
| json_decode, English posts (escaped) | 1,587,349 | −28% | −37% |
| json_decode, Chinese posts (escaped) | 7,775,318 | +14% | +7% |
| json_decode, Russian posts (raw UTF-8) | 1,678,540 | +28% | +22% |
| json_decode, Chinese posts (raw UTF-8) | 1,648,524 | +52% | +44% |
| json_decode, Japanese posts (raw UTF-8) | 1,618,415 | +47% | +41% |
| json_decode, Arabic quotes (raw UTF-8) | 2,969,299 | +25% | +17% |
<!-- /bench-table -->

## What the change does, and where it wins

The scanner skips a run of plain ASCII (everything except `"`, `\`, control bytes and bytes ≥ 0x80) 16 bytes at a time with SSE2 (a CPU instruction set that processes 16 bytes at once) before re-entering the re2c string state (re2c is the lexer generator php-src's JSON scanner is built from). The encoder does the same for bytes that are always copied verbatim (copied unchanged, not escaped), and with `JSON_UNESCAPED_UNICODE` it keeps a well-formed UTF-8 sequence in the pending run instead of decoding and appending it on its own.

The win is real where the input is mostly ASCII, or where whole UTF-8 sequences are copied verbatim:

- `json_encode` `JSON_UNESCAPED_UNICODE` of non-Latin text: −36% to −61% (posts, comments, quotes above).
- `json_encode` and `json_decode` of ASCII-heavy text: posts-en −26% to −37%.

The read is correct. The verbatim UTF-8 validator matches `php_next_utf8_char` byte for byte (C2–DF; E0–EF with code point ≥ 0x800 and no surrogate; F0–F4 within 0x10FFFF), so nothing invalid is ever kept.

## Trade-offs

The skip and the verbatim scan run per character, even when the current byte is already non-ASCII or a special byte, where there is nothing to skip. On text that is not mostly plain ASCII they add work on top of what re2c and the escaper already do.

A synthetic sweep isolates the break-even. This is a worst case: one 20000-character JSON string with a growing share of non-ASCII characters (2-byte Cyrillic `s2`, 3-byte CJK `s3`), no structure to dilute the string scan. `encode` is the default escaping encode, `decode` is `json_decode` of the `JSON_UNESCAPED_UNICODE` document. The big cells (e.g. +454% at 100% non-ASCII) are this synthetic worst case, not real documents.

<!-- bench-table 20261026-amd-jsonratio.json --labels labels-ratio.txt --no-control -->
| call | master, CPU cycles per call (GCC 15.2) | GCC 15.2 | clang 21.1 |
|---|--:|--:|--:|
| json_encode, 0% non-ASCII | 41,508 | −82% | −87% |
| json_encode, 10% non-ASCII | 91,977 | −1% | −17% |
| json_encode, 30% non-ASCII | 225,559 | +24% | +4% |
| json_encode, 100% non-ASCII | 408,514 | +15% | 0% ~ |
| json_decode, 0% non-ASCII | 41,474 | −87% | −94% |
| json_decode, 10% non-ASCII | 43,630 | −17% | −58% |
| json_decode, 15% non-ASCII | 44,701 | +20% | −35% |
| json_decode, 30% non-ASCII | 47,972 | +121% | +24% |
| json_decode, 100% non-ASCII | 62,996 | +454% | +321% |

~: the change is not larger than the A/A control of the same row: not evidence of a difference.
<!-- /bench-table -->

Break-even in cycles is around 10% non-ASCII characters for the default encode and 10–15% for decode on GCC, later on clang. Past that it is a regression, worst at a high density (dense CJK or Cyrillic). On real documents the strings are one part of a larger parse, so the magnitude is smaller than the single-string sweep, but the direction is the same.

By instructions (deterministic, machine-independent) the decode regression is +19% to +25% on the real posts and +68% to +129% on the pure non-ASCII sweep. Cycles grow more than instructions; the microarchitectural cause (code placement or the branch predictor) was not profiled.

Instructions matter here because not every cycle regression is a real work regression. The `json_encode` `users` row is +6% cycles but flat instructions (−3% to +1%), so it is not added work — most likely code placement in the larger binary. The instruction-backed regressions are `json_decode` of non-Latin text (+6% to +12% escaped, +19% to +25% raw) and, more modestly, the default `json_encode` of non-Latin text (up to +15%).

## A possible mitigation (proposed, not in the PR)

[`fix.diff`](fix.diff) adds a scalar fast-bail to the top of both helpers: if the first byte already stops the run, return at once and skip the SSE setup. Output stays identical (same fuzzing). It cuts the decode regression a lot — raw non-Latin from +28%…+52% down to +13%…+15%, escaped from +14% to +5% — but it leaves the default encoder regression and costs about +3% on pure-ASCII encode. A starting point, not a full fix. Built with GCC 15.2 on the same commit as the head, so `fixVhead` isolates the bail.

Column `fixVmaster` is the fix against master (the net effect), `fixVhead` is the fix against the PR head (what the bail recovers).

<!-- bench-table 20261026-amd-dummy-fix2.json --labels labels-fix.txt --no-control -->
| call | master, CPU cycles per call (GCC 15.2 (fixVmaster)) | GCC 15.2 (fixVmaster) | GCC 15.2 (fixVhead) |
|---|--:|--:|--:|
| json_encode, English posts (bail's ASCII cost) | 482,889 | −24% | +3% |
| json_encode, Russian posts (default) | 2,394,335 | +6% | −1% |
| json_encode UNESCAPED_UNICODE, Russian posts | 2,910,166 | −57% | −10% |
| json_decode, Chinese posts (escaped) | 7,762,267 | +5% | −9% |
| json_decode, Russian posts (raw UTF-8) | 1,678,457 | +15% | −11% |
| json_decode, Chinese posts (raw UTF-8) | 1,653,078 | +13% | −26% |
| json_decode, Japanese posts (raw UTF-8) | 1,618,939 | +13% | −24% |
<!-- /bench-table -->

A full fix would avoid paying the per-character scan where there is no ASCII run to skip, which the bail only does for the zero-length case.

## Machine and method

AMD Ryzen 9 5950X, Ubuntu, pinned to CPU 15 (second CCD). GCC 15.2 and clang 21.1. Builds use the flags of the official PHP Docker image (`-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64`, link `-Wl,-O1 -pie`) plus `--enable-werror`, via `bench pr`.

The PR head is `97378f2a680`. `bench pr` builds it merged onto the pinned master `49b2bc4532e`, and the resulting commit `ff0c54aac94` is what the tables name as B. The merge is deterministic (fixed author identity and the head's date), so the hash is the same on any machine while the PR has no new commits.

The number is user-space CPU cycles per call: `perf stat` over N calls minus the same process with 0 calls, divided by N. 15 alternating passes per case; each cell is the median over the passes of the per-pass ratio of B to A. Master is also run against itself at the start and the end as a control; almost every control row is within ±1%, so the machine was quiet. The PR-effect and break-even series (dummy-head, jsonratio) were measured on an idle machine; the fix series (dummy-fix2) ran at load average 2.2, so its spreads are a little wider. The same direction appears on an Intel i7-13700H with GCC 13.3/14.2 and clang 18.1/20.1, measured under load and not published here; the instructions agree.

Inputs are real responses from dummyjson.com (`corpus/dummyjson/`), fetched 26 October 2026: `products` and `users` are field- and nesting-heavy, `posts`, `comments` and `quotes` carry free text. The localized variants refill the free-text fields from the committed per-language corpus (`corpus/<lang>.txt`) at the same character length, keeping the real structure, keys and numbers. That text has no inter-word ASCII (no spaces, for Chinese and Japanese), so the localized fields are close to fully non-ASCII; real localized content mixes in punctuation, digits, spaces and Latin brand names, so the non-Latin rows here are an upper bound on the regression.

Suites: [`jsondummy.php`](jsondummy.php) (real data), [`jsonratio.php`](jsonratio.php) (the break-even sweep). Series: [`20261026-amd-dummy-head.json`](20261026-amd-dummy-head.json), [`20261026-amd-jsonratio.json`](20261026-amd-jsonratio.json), [`20261026-amd-dummy-fix2.json`](20261026-amd-dummy-fix2.json).

## Output verification

- Differential fuzzing against master, [`json_difftest.php`](json_difftest.php): deterministic inputs (same seed on both binaries) covering valid 2/3/4-byte UTF-8, overlongs, surrogates, truncated sequences, code points above U+10FFFF, lone continuation bytes, escape sequences, special bytes, and lengths across the 16-byte SSE boundary. It runs `json_encode` (10 flag sets), `json_decode` (4 flag sets) and `json_validate`, and hashes every result. 50000 iterations, output identical to master across GCC 13.3/14.2/15.2 and clang 18.1/20.1/21.1, and identical for the fix build — see [`fuzz-check.txt`](fuzz-check.txt).
- The check catches a real defect (mutation test). A build with the surrogate exclusion removed from the verbatim UTF-8 validator — so it keeps surrogate bytes verbatim under `JSON_UNESCAPED_UNICODE` where master rejects them — diverges from master within the first iterations.
- The PR's own `string_scan_boundaries.phpt` passes on head and base.
- ASan/UBSan build (`--enable-address-sanitizer --enable-undefined-sanitizer`, `USE_ZEND_ALLOC=0`): the fuzzer runs clean, no leaks; the phpt passes.

## Not tested

- NEON (aarch64) paths.
- Throughput or latency under a server load; these are single-process, single-core cycle counts.
- Emoji-heavy and mixed-script documents beyond the languages above.
- `json_validate` is vectorized by the PR but has no timing row here (it shares the scanner with `json_decode`); it is only in the fuzzer.
- `json_decode` to `stdClass` (without the assoc flag); both suites decode to arrays or scalars.
- Microarchitectural profiling (branch-misses, top-down) for the cycles-above-instructions gap.
- The proposed fast-bail is measured only on GCC 15.2 (it is a direction, not part of the PR).

## Reproduce

The tables regenerate from the committed series, no build needed, from the root of [php-src-bench](https://github.com/ArtUkrainskiy/php-src-bench). The `labels-*.txt` pick the rows shown; add `--full` for the instructions column and per-pass ranges, and drop `--no-control` to also print the master-vs-master control.

```
d=reports/pr-24666-json-scan
./bench table $d/20261026-amd-dummy-head.json --labels $d/labels-head.txt --no-control   # Summary
./bench table $d/20261026-amd-jsonratio.json  --labels $d/labels-ratio.txt --no-control   # sweep
./bench table $d/20261026-amd-dummy-fix2.json --labels $d/labels-fix.txt  --no-control   # fix
```

To rebuild and re-measure, with php-src checked out at `../php-src`. Build names carry your
compiler's major version, so on a GCC 13 / clang 18 box replace every `gcc15`/`clang21` below
with `gcc13`/`clang18` (in the group labels and the `../php-builds/...` paths). Each `bench
compare` takes a few minutes and prints progress per case.

```
# real data: the 5 files used are committed under corpus/dummyjson (fetched 26 Oct 2026).
# fetch.sh re-downloads them live from dummyjson.com; its data is unpinned, so a later
# fetch can shift the small +/- rows. curl is required. Skip this step to reproduce exactly.
sh corpus/dummyjson/fetch.sh

./bench pr 24666 --base 49b2bc4532e --slim --profile docker --cc gcc,clang   # head 97378f2a680 -> ff0c54aac94

# pick an idle, isolated core for --cpu (15 is this box's second-CCD core; on an Intel hybrid
# use a P-core, not an E-core); see `bench check`.
# PR effect on real data (~5 min)
./bench compare jsondummy gcc15=pr24666-base-gcc15:pr24666-head-gcc15 clang21=pr24666-base-clang21:pr24666-head-clang21 --cpu 15 --passes 15
./bench table results/<date>-compare-jsondummy.json --full

# break-even sweep (~5 min)
./bench compare jsonratio gcc15=pr24666-base-gcc15:pr24666-head-gcc15 clang21=pr24666-base-clang21:pr24666-head-clang21 --cpu 15 --passes 15

# correctness: no output means identical to master (builds live in ../php-builds)
cp reports/pr-24666-json-scan/json_difftest.php /tmp
diff <(../php-builds/pr24666-base-gcc15/sapi/cli/php -n /tmp/json_difftest.php 7 50000) \
     <(../php-builds/pr24666-head-gcc15/sapi/cli/php -n /tmp/json_difftest.php 7 50000)

# the proposed mitigation. fix.diff is a working-tree snapshot (the series names it as the
# local commit d66e36d3255 = ff0c54aac94 + fix.diff, not pushed). It applies on the merged
# head (the helpers it patches are added by the PR). Build on the same commit the head used so
# the comparison isolates the bail, with --cc gcc to match base/head's driver.
git -C ../php-src worktree add /tmp/pr24666-fix ff0c54aac94
git -C /tmp/pr24666-fix apply "$PWD/reports/pr-24666-json-scan/fix.diff"
PHP_SRC=/tmp/pr24666-fix ./bench build --slim --cc gcc pr24666-fix2 .
./bench compare jsondummy fixVmaster=pr24666-base-gcc15:pr24666-fix2-gcc15 fixVhead=pr24666-head-gcc15:pr24666-fix2-gcc15 --cpu 15 --passes 15

# cleanup (--force: the worktree has the applied fix.diff)
git -C ../php-src worktree remove --force /tmp/pr24666-fix
./bench gc 'pr24666-*'
```
