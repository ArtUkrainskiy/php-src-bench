# Probe: one repeated text against 64 different texts

Why every cell rotates through a pool of different texts.

A prepared call ran 2,000 times on a 16 KiB text, with 128 random keys and one occurrence in the middle.
Either the same text every call, or 64 different texts of the same kind in turn.
`perf stat` counted the 2,000 calls minus an empty run of the same process; values are medians of 3 passes.
CPU 15 of the machine in [METHOD.md](../METHOD.md).
The probe used an earlier version of the extension, before the hot loop was reworked in the PR.

| Compiler | Call | Branch misses, one text | 64 texts | µs, one text | 64 texts |
|---|---|---:|---:|---:|---:|
| GCC 15.2 | `countMatches()` | 142 | 5,256 | 14.4 | 43.4 |
| GCC 15.2 | `getMatchedKeywords()` | 138 | 5,250 | 13.8 | 43.6 |
| GCC 15.2 | `replace()` | 139 | 5,295 | 14.1 | 45.1 |
| Clang 21.1 | `countMatches()` | 141 | 5,272 | 10.1 | 40.1 |
| Clang 21.1 | `getMatchedKeywords()` | 136 | 5,194 | 10.2 | 40.2 |
| Clang 21.1 | `replace()` | 128 | 4,789 | 9.4 | 36.7 |

On one repeated text the CPU learns the branches: far fewer misses per call, and 3 to 4 times less time.
The CSV also has a third variant, `orig`, the fixed input of an earlier report; it is not shown.
Applications rarely search the same text again and again, so the report uses pools of different texts.
Raw counts: [probe/branch-probe.csv](probe/branch-probe.csv).
