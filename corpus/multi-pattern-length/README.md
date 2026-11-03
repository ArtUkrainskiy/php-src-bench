# Fixed-length search and replacement inputs

This series holds each dictionary at **128 distinct literal keys** and changes the input length. Inputs are saved JSON, not generated inside a timed operation.

| Task | Exact bytes per string | Match state |
|---|---|---|
| Moderation | 128, 4096, 16384, 65536 | No match, near start, middle, near end |
| List distinct support terms | 512, 4096, 16384, 65536 | Matching terms |
| Replace support terms with help URLs | 512, 4096, 16384, 65536 | Matching terms |

Each case contains four **different** strings of the same exact length. Timed loops cycle through them equally often. One operation processes one string; 15 samples report time per operation. Every variant is visible in [moderation.json](suites/moderation.json) or [support.json](suites/support.json), alongside exact expected results, match positions, output sizes and dictionary order.

The texts combine [authored paragraphs](paragraphs.json) already present in the product corpus. A fixed seed permutes paragraph order; the generator trims to a word boundary and pads fewer than 80 final ASCII spaces to reach the exact byte length. Long inputs repeat paragraphs. This is a controlled size experiment, not a production trace or corpus frequency sample. 64 KiB is an additional long-input control.

The policy is a prefix of the pinned [moderation lexicon](../multi-pattern-scaling/moderation-words.json), with the first eight rules spread over dictionary ranks. Support terms are a prefix of [support-terms.json](../multi-pattern-scaling/support-terms.json). Their replacements are fixed help URLs. Matching is case-sensitive bytes, without word boundaries or Unicode normalization.

[generate.py](generate.py) computes independent byte-search and replacement expected results. Recheck saved inputs with `python3 generate.py --check`. The existing product and dictionary-size corpora are unchanged.
