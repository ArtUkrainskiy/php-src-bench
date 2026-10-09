# base64_decode(): four characters at a time in the character loop

php-src change: branch `base64-decode-quads`, "ext/standard: Decode base64 four characters at a
time in the character loop", compared with its parent on master,
[`fb6435df56b`](https://github.com/php/php-src/commit/fb6435df56b).

The vector decoders (SSSE3, AVX2, AVX-512, NEON) stop at the first 32-byte block that holds
anything but alphabet characters, and everything after that — as well as every input shorter
than 45 bytes — goes through the character loop in `php_base64_decode_impl()`: one character per
iteration, a `switch` on its position in the group. The change decodes whole groups of four
alphabet characters at once while the input is clean and keeps the one-character step for
whitespace, padding, invalid bytes and the last partial group.

## Summary

| `base64_decode()` input | time | instructions |
|---|---|---|
| 24 bytes (a token) | 2.0× faster | 824 → 522 |
| 44 bytes (a 32-byte key) | 2.5× faster | 1,338 → 684 |
| 136 bytes | 2.3× faster | 1,300 → 718 |
| 1 KB, clean | 1.5× faster | 1,751 → 1,211 |
| 64 KB, clean | same | 46,344 → 45,804 |
| 1 KB in 76-column lines (MIME) | 3.1× faster | 24,425 → 8,438 |
| 64 KB in 76-column lines (MIME) | 3.3× faster | 1,641,721 → 547,715 |
| 64 KB in 64-column lines (PEM) | 3.3× faster | 1,645,586 → 561,240 |
| 64 KB MIME, strict | 3.7× faster | 1,903,638 → 547,742 |
| `base64_encode()` | same | same |

Instruction counts are from `perf stat` and exact; the wall times were taken on a loaded laptop
(load average 4) and are approximate. The suite is
[`results/ideas/base64-suite.php`](../../results/ideas/base64-suite.php) in this repository's
working tree; the raw run is `base64.json` next to this file.

## Verification

- `bench difftest base64 b64-base b64-quads` with seeds 1, 3 and 11, 30,000 inputs each: clean
  base64, MIME and PEM lines, random line lengths, whitespace and invalid bytes anywhere, padding
  in every position, lengths around the group and vector block boundaries, decoded in both modes
  plus `base64_encode()` of the input and of the decoded bytes. Output identical to master.
- The same differential test with the decoder forced onto the SSSE3 and the generic path (a
  throwaway build with an environment switch in the resolver), 20,000 inputs each: identical.
- `ext/standard/tests/url`, `ext/standard/tests/strings/base64*`, `ext/standard/tests/http`:
  77 passed, 0 failed; the new test `base64_decode_whitespace.phpt` passes on master too.

## Why the vector loops were left alone

Resuming the vector loop after a line break instead of finishing in the character loop gives
another 3× on MIME and PEM input; that is a separate change to every vector variant and comes
as a follow-up. Stripping whitespace first and decoding the rest as clean input was measured and
rejected: 1.9× slower than resuming in place on MIME, with a temporary buffer.
