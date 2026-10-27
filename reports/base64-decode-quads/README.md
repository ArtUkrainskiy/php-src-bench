# base64_decode(): four characters at a time in the character loop

Status: open for a PR, not in any release.

php-src change: branch `base64-decode-quads`, "ext/standard: Decode base64 four characters at a
time in the character loop", one commit on master
[`100e8f353ea`](https://github.com/php/php-src/commit/100e8f353ea).

The vector decoders (SSSE3, AVX2, AVX-512, NEON) stop at the first 32-byte block that holds
anything but alphabet characters, and everything after that — as well as every input shorter
than 45 bytes — goes through the character loop in `php_base64_decode_impl()`: one character per
iteration, a `switch` on its position in the group. The change decodes whole groups of four
alphabet characters at once while the input is clean and keeps the one-character step for
whitespace, padding, invalid bytes and the last partial group. Output is unchanged.

## Summary

Instructions per call (`perf stat`, deterministic); the range spans six compilers — GCC 13/14
and clang 18/20 on an Intel i7-13700H, GCC 15 and clang 21 on an AMD Ryzen 9 5950X. The AMD
cycles column is the min…max of GCC 15 and clang 21 on a quiet host. Negative = faster.

| `base64_decode()` input | instructions/call | AMD cycles |
|---|---:|---:|
| 24 B (a token) | −41…−46% | −37…−58% |
| 44 B (a 32-byte key) | −45…−50% | −45…−64% |
| 136 B | −47…−51% | −46…−63% |
| 1 KB, clean | −29…−31% | −22…−42% |
| 64 KB, clean | −1% (flat) | flat |
| 1 KB in 76-column lines (MIME) | −67…−70% | −63…−80% |
| 64 KB in 76-column lines (MIME) | −69…−71% | −64…−81% |
| 64 KB in 64-column lines (PEM) | −68…−71% | −64…−81% |
| 64 KB MIME, strict | −73…−76% | −68…−79% |

`base64_encode()` is not touched. The clean 64 KB row is flat because that input stays in the
vector loop, which is unchanged; the win is on short input and on input with line breaks, which
hands the bytes after the first break to the character loop. Base64 with line breaks is what
mail (RFC 2045), PEM, SAML and the Java/Python MIME encoders produce. clang gains the most, its
old character loop was the slowest.

Raw data: `intel-instructions.txt` (per compiler, all cases), `amd-cycles.txt` (AMD cycles and
instructions); inputs built by `base64_cases.php`.

## Verification

- `bench difftest base64 <base> <head>` seed 1, 30,000 inputs each, on all six compilers
  (GCC 13/14, clang 18/20, GCC 15, clang 21): clean base64, MIME and PEM lines, random line
  lengths, whitespace and invalid bytes anywhere, padding in every position, lengths around the
  group and vector block boundaries, both modes, plus `base64_encode()` of input and decoded
  bytes. Output identical to master.
- The same differential with the decoder forced onto the SSSE3 and the generic path (a throwaway
  build with an environment switch), 20,000 inputs: identical.
- ASan + UBSan build of the change: the differential and the test suite run clean, no sanitizer
  report.
- `ext/standard/tests/url`, `.../strings/base64*`, `.../http`: pass; the new
  `base64_decode_whitespace.phpt` (a line break at every position of inputs up to 100 bytes, both
  modes) passes on master too.

## Why the vector loops were left alone

Resuming the vector loop after a line break instead of finishing in the character loop gives
another ~3× on MIME and PEM input; that is a separate change to every vector variant and comes
as a follow-up. Stripping whitespace first and decoding the rest as clean input was measured and
rejected: slower than resuming in place on MIME, and it needs a temporary buffer.
