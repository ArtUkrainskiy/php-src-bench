# Correctness checks

| Build | Set | Cases | Result |
|---|---|---:|---|
| gcc15 | Matcher: all four methods | 601 | PASS |
| clang21 | Matcher: all four methods | 601 | PASS |
| gcc15 | replacer69 | 69 | PASS |
| clang21 | replacer69 | 69 | PASS |
| gcc15-asan-ubsan | verify.php | 601 | PASS |
| gcc15-asan-ubsan | verify-replacer.php | 69 | PASS |
| gcc15 | PHPT | 16 | PASS |
| clang21 | PHPT | 16 | PASS |

601 is the size of the Matcher verification set; 69 is the size of the Replacer set. These are different sets; the counts do not denote the number of measured comparisons. All 601 Matcher inputs were checked on GCC, Clang and under ASan/UBSan; Replacer is also compared with strtr() and the saved replacement count. Before each timing run, the harness checks the output of the measured method. Corrupting the reference in a trial run caused a failure on both compilers.

[Machine-readable check results](data/checks.json) · [Code identity](SOURCE.md).

Logs: [PHPT GCC](data/check-logs/phpt-gcc15.log), [PHPT Clang](data/check-logs/phpt-clang21.log), [ASan/UBSan Matcher](data/check-logs/verify.php.asan.log), [Replacer](data/check-logs/verify-replacer.php.asan.log). Paths in the log copies are normalized.

[Check results with a corrupted reference](data/mutations.json).

Two additional 1 KiB Replacer inputs were checked: the result, replacement count and agreement with `strtr()` — PASS on GCC 15.2, Clang 21.1 and ASan/UBSan. [Check records](data/replacer-1k-checks.json). They supplement the original 69 inputs; Replacer now has 71 inputs in total.
