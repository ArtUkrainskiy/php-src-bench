# Unusual results

These observations refer to the final measured module. Result correctness has been checked. Counters and profiles show machine-code execution; no causal conclusion is drawn without a separate change/control.

## Search on the same 16384 B text

128 keys of 12 bytes, one occurrence. The text and ordered dictionary are identical for the three methods.

| Compiler | Method | Prepared call, µs | Cycles/call | Instructions/call | Branch misses/call |
|---|---|---:|---:|---:|---:|
| gcc15 | `Matcher::getMatchedKeywords()` | 17.329 | 78694.8 | 265198.0 | 93.1 |
| gcc15 | `Matcher::countMatches()` | 38.156 | 176595.3 | 215486.0 | 3963.9 |
| gcc15 | `Matcher::matchAll()` | 18.663 | 85642.2 | 216206.0 | 63.9 |
| clang21 | `Matcher::getMatchedKeywords()` | 13.377 | 153772.7 | 278474.0 | 3711.1 |
| clang21 | `Matcher::countMatches()` | 33.806 | 157529.7 | 213930.0 | 3905.6 |
| clang21 | `Matcher::matchAll()` | 14.162 | 64796.6 | 266598.0 | 49.0 |

countMatches() produces a simpler result, but its loop can be slower than the other methods on the same input. Profiling used the final module. On GCC, diagnostic countMatches() shows more branch misses with fewer instructions than getMatchedKeywords(). A causal link to the slowdown has not been established. Diagnostic pairs were collected in separate processes and are not counters from the same rounds as the elapsed-time measurements. On Clang, diagnostic getMatchedKeywords() cycles do not agree with the ratio of the main timings. The reason for the difference between runs has not been established. [Main-series counters](COUNTERS.md).

## One 24 B key, a 16384 B text

One replacement. The input is identical on both compilers. Separate series are shown; † marks measurements that did not pass the quality checks, even when the A/A median is within 2%.

| Compiler | Prepared Replacer, µs | One-shot, µs | Prepared A/A, % | One-shot A/A, % |
|---|---:|---:|---:|---:|
| gcc15 | 47.385† | 48.116 | -0.530 | -0.177 |
| clang21 | 12.073† | 12.799† | -0.357 | -0.258 |

The compiler difference alone does not establish the cause. Disassembly and sampled profiles are saved in the [diagnostic data](data/profiles/README.md). The single-key input remains a limit on the applicability of the general-purpose automaton; no special path was added in this study.
