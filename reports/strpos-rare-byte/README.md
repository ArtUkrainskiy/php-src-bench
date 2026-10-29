# Faster `zend_memnstr`: anchor the scan on the needle's rarest byte

Status: prototype for a PHP PR, measured 29 October 2026. Branch
[`ArtUkrainskiy:php-src:strpos-rare-byte-scan`](https://github.com/php/php-src/compare/master...ArtUkrainskiy:php-src:strpos-rare-byte-scan)
at commit `6f12f434d1e`, against `php/php-src` master `9d94059ce881`.

`zend_memnstr()` is the substring search behind `strpos()`, `strstr()`, `str_contains()`,
`explode()`, `str_replace()` and `substr_count()`. Today it anchors its `memchr` scan on the
needle's **first** byte and restarts on every hit, and uses a scalar Sunday scan for needles
of 9+ bytes. Both are slow when the leading byte is common in the haystack, or the needle is
long. This change scans for the needle's **rarest** byte instead, and falls back to the
current search when that does not help — so the result is the same and never much slower.

## Summary

This is a **targeted** optimization, not a universal one. Where it applies it is large
(9–23x fewer cycles, and it removes a quadratic Sunday blow-up on long needles); on most
calls it changes nothing.

- **Wins** when the haystack is large (> ~256 bytes), mostly ASCII, and the needle contains
  a byte that is **rare in that haystack** — e.g. searching source, logs, config, HTML or
  JSON for a distinctive token. Intel i7-13700H, GCC 13, cycles per call:
  `zend_string` in 290 KB of C source: 10919 → 1210; the word `example` in 100 KB of text:
  9307 → 402; an absent rare-byte token: 110811 → 6514.
- **Unchanged** (`= base`) for the common cases: 1-byte needles (they already use `memchr`),
  small haystacks, needles of only common bytes, and **UTF-8 / multilingual text** (its high
  bytes are common, so the scan falls back to the current search).
- **Small residual costs** (sub-microsecond): a short needle whose match is found early, or
  whose first byte is already rare, and the `MIN_SPAN` boundary — see Trade-offs.
- It does not beat `preg_match()` everywhere; the bar here is the current `strpos`, not the
  regex engine.

AMD Ryzen 9 5950X (GCC 15) showed the same pattern.

## What changes and why it is faster

`zend_memnstr()` picks the needle byte with the lowest weight in a static byte-frequency
table (`zend_byte_commonness`) and `memchr`s for that, instead of the first byte. When the
first byte is common but the needle has a rarer byte, the scan stops restarting at every
position; for a 9+ byte needle it replaces the scalar Sunday scan with a `memchr` on a rare
byte.

Correctness is unchanged: the rarest byte only decides where `memchr` looks; every candidate
is confirmed with `memcmp`, and the fallbacks run the current algorithm. See Verification.

## Trade-offs

The fallback **limits** regressions rather than removing them. Measured, Intel GCC 13,
cycles per call:

| case | base | this PR | note |
|---|---:|---:|---|
| `ax` in 258 bytes of `x` (anchor dense, at the MIN_SPAN edge) | 77 | 363 | +286 cycles |
| 6-byte needle, match at offset 0 | 66 | 94 | +28 cycles (anchor pick) |
| short needle, rare first byte, absent (`xqzbad` in 48 KB) | 3361 | 3983 | base is already optimal |
| sparse anchor then dense, needle 32, absent | ~base | ~base | per-window density re-check |
| needle 256 all-`a` + `x`, absent in 100 KB `a` | 14.4M | 6527 | base Sunday is quadratic here |
| `z`+`a`*4095 in 1 MiB of `z`, absent | 11976 | 9550 | long needle kept on Sunday |

The residual losses are a short needle whose match is found early or whose first byte is
already rare (the extra work is the rarest-byte scan, tens to a few hundred cycles), and the
density boundary. There is no guaranteed upper bound; the density check and the `MIN_SPAN` /
`MAX_NEEDLE` guards keep the known cases small.

## Where it does and does not help

| call class | effect |
|---|---|
| 1-byte needle (`explode(",")`, `strpos($s,"/")`) | unchanged (uses `memchr`) |
| small haystack (headers, paths, short strings) | unchanged (below `MIN_SPAN`) |
| UTF-8 / multilingual text (comments, names) | `= base` (high bytes are common → fallback) |
| needle of only common bytes (`name`, `error`) | `= base` |
| large ASCII haystack + needle with a rare byte | **win, 9–23x** |
| long needle (9+) with a rare byte | **win** + removes the Sunday quadratic |

Multilingual blocklist scanning — the obvious motivating case — lands in `= base`: a
48 KB en/es/ru/zh/ja/ko/emoji feed searched for `спам` or `垃圾话` is 32655 → 32660 and
56958 → 56872. The gains are on ASCII needles with a rare byte.

## Comparison with preg_match (context)

For needles with a rare byte the search is also competitive with `preg_match()` on literals,
sometimes faster (`zend_string`: 1210 vs PCRE's 2795). Where the needle has no rare byte it
keeps the current behaviour, so PCRE's JIT is ahead on those large-haystack misses
(`__NO_SUCH_MACRO__`: this PR 215046, base 221431, PCRE 42060). This PR does not try to beat
PCRE2; its baseline is the current `strpos`.

## Machine and method

- Intel i7-13700H, core 2 (P-core), `perf stat -e cpu_core/instructions/u` and
  `cpu_core/cycles/u`; PHP 8.7.0-dev built with the official-image flags (`-O2`, stack
  protector, PIE), `--enable-werror`. AMD Ryzen 9 5950X, core 15 (second CCD), GCC 15 and
  clang 21, `cycles:u`.
- Per call = (cycles at K calls − at 0 calls) / K, built once before the loop; median of 5
  passes. Haystacks are the files under `corpus/` (real C source, English docs, a generated
  access log, a generated HTML page, a balanced multilingual feed).
- The byte-frequency table and the thresholds (`MIN_SPAN = 256`, `RARE_GAP = 133`,
  `SAMPLE = 16`, `MAX_NEEDLE = 256`, `COMMON = 64`) are tuned on these machines and inputs;
  they only choose which byte to scan for and when to fall back, never the result.

## Verification

- Differential fuzzing against a naive reference (`verify.php`), ~1.1M cases over ASCII,
  binary and embedded-NUL alphabets, lengths across the thresholds — no mismatches.
- Two `.phpt`: `str_search_edges` (randomized differential over strpos/str_contains/strstr/
  substr_count) and `str_search_fallback` (deterministic cases on each branch: the per-window
  density re-check, the MIN_SPAN boundary, early matches, long needles, all-common needles).
- The `ext/standard` string test suite passes.
- An ASan/UBSan build is clean over the fuzz corpus and both `.phpt`.

## Not tested

- A reproducible per-compiler matrix across all six compilers (this is a two-machine draft
  series; a full `bench compare` matrix is future work).
- Non-x86 builds keep the scalar path unchanged.

## Alternatives explored (not in this PR)

Measured, each with its own trade-off, left for follow-up research:

- A SIMD packed-pair scan (two rare bytes at once) additionally speeds up the all-common-byte
  and UTF-8 misses this PR leaves at `= base`, but needs an SSE2/AVX2 path with its own
  portability and worst-case questions (it regressed long needles and tiny haystacks before
  the scalar fallback was added).
- A Two-Way fallback would bound the worst case at O(n); this PR keeps the current Sunday
  scan there.
- A UTF-8-aware frequency table would let the rare-byte scan help multilingual text; changing
  the table and the algorithm together would make the benchmarks hard to read, so it is
  deferred.

## Reproduce

Corpora: `gen_corpus.py` writes the generated log and HTML; `gen_multilang.py` writes the
multilingual feed; the `code` and `prose` corpora are concatenated from php-src sources and
its docs. All live under `corpus/` at run time (not committed).

```
# from the php-src build tree (branch strpos-rare-byte-scan):
./configure --enable-werror && make -j
PHP="$PWD/sapi/cli/php"
"$PHP" run-tests.php ext/standard/tests/strings/str_search_edges.phpt \
                     ext/standard/tests/strings/str_search_fallback.phpt

# from this report directory, measuring against a base build of master:
"$PHP" verify.php 500000 1                 # correctness vs naive
# one cell, cycles per call (hybrid Intel: cpu_core/cycles/u, taskset to a P-core):
getc() { taskset -c 2 perf stat -x, -e cpu_core/cycles/u -- "$PHP" "$@" 2>&1 >/dev/null | awk -F, '/cycles/{print $1}'; }
hi=$(getc real_bench.php strpos corpus/code.c "$(printf %s zend_string | base64 -w0)" 4000)
lo=$(getc real_bench.php strpos corpus/code.c "$(printf %s zend_string | base64 -w0)" 0)
# per call = (hi - lo) / 4000
```

The scripts (`verify.php`, `needle_bench.php`, `real_bench.php`, the corpus generators) and
the raw series (`report-series.txt`) are in this directory.
