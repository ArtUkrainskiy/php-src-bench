# Compact Sunday shift tables

Proposed change to the substring search used by `strpos()`, `str_replace()` and related functions.

Compare [`strpos-compact-sunday-pr`](https://github.com/ArtUkrainskiy/php-src/tree/strpos-compact-sunday-pr)
with [PHP master](https://github.com/php/php-src/tree/master), both PHP 8.7.0-dev.
[Patch](change.patch) · [Measured build metadata](manifest.json).

The patch reduces the Sunday shift table from 1024 to 256 bytes for 9–31-byte
needles (searched substrings) when at least 1024 input bytes remain from the
current search position. On the Sunday path, needles of 32 bytes or more retain
the wide table. The search algorithm and the inline path for needles below
9 bytes or remaining inputs below 1024 bytes are unchanged. The measured changes include
the cost of the new dispatch and differences in code placement.

On AMD Ryzen 9 5950X with GCC 15 and Clang 21, a 12-term banlist check with no matches takes 4.93–11.84% less time than master; template replacement and counting take 14.42–16.52% less. The two 32-byte early-match controls take 2.99–3.86% more time than master on GCC. These are costs of individual PHP operations, not whole-request speedups.

Searching 4096 `a` bytes for 63 `a` bytes followed by `b` takes 30.70% more time on GCC 15. This 64-byte needle uses the existing wide table. A separate profile records more branch misses with nearly unchanged instructions; the precise cause of the changed branch behavior remains unresolved. [Case and profile](search-controls.md#synthetic-repeated-prefix-regression).

Elapsed results are AMD-only. Intel elapsed measurements failed A/A controls; native ARM, Windows and 32-bit builds were not tested. There is one paired elapsed round per comparison. [Reproduce](reproduce.md) · [Raw measurements](data/native.tar.gz).

## Cases

Inputs are generated application fixtures, not production traffic samples.
All moderation inputs are lower-case UTF-8; searches are case-sensitive literal
substrings, without word-boundary matching or normalization inside timing.
There is one post case for each of English, Russian, Spanish, Arabic, Hindi,
Chinese, Japanese, Korean and mixed emoji. Thread timing cases cover English
and Chinese only.

| Case | Input and measured work | Searched substrings |
|---|---|---|
| Moderation post | About 1 KiB of ordinary comments/messages; check all 12 banlist entries, no match | Local phrases such as `spam`, `casino bonus`, plus advertising-domain fragments; 4–55 UTF-8 bytes across languages |
| Moderation thread | About 64 KiB of messages; the same 12-entry absent search | Same phrases as the corresponding post |
| Split fields | About 4 KiB, 170 varied product fields; `explode()` returns every field | Two consecutive pipe characters or `::`, two bytes |
| Parse HTTP headers | Seven headers and a 64 KiB body; find the terminator after 261 header bytes, then parse the headers; body is not parsed | `\r\n\r\n`, `\r\n` and `: ` |
| Replace template placeholders | 4250-byte order-card/email template; replace 68 slots with four values using `str_replace()` | `{{order.id}}`, `{{user.name}}`, `{{tracking.url}}`, `{{support.email}}`; 12–17 bytes |
| Count template slots | Same template; `substr_count()` finds 17 occurrences | `{{order.id}}`, 12 bytes |
| Search controls | Ordinary ASCII filler; an absent 9-byte substring or a 31/32-byte match at byte offset 7 | Text tokens, plus a 32-byte token made of 31 `a` bytes and `b` |

The split operations are `explode('||', $s)` and `explode('::', $s)`.
Exact input sizes are in the tables. [Measured suite](suite.php) · [31-byte control](early31-suite.php) · [Data-label notes](data-notes.md).

## Results

All deltas are relative to master; negative means lower cost. Elapsed time is
the primary comparison. Time columns show medians in microseconds per complete
operation after empty-loop subtraction.
Cycles and instructions come from a separate series: cycle deltas are the median
of five paired ratios; instruction deltas compare the median absolute counts.

For each case, each build runs at least **3 seconds of warmup**, followed by
**10 approximately one-second samples** in one PHP process. There is one paired round. Counters use
five separate 50 ms-target passes. These are preliminary measurements;
ten samples in one process are not ten independent rounds.

A/A compares the identical master binary before and after the timing series.
We use a minimum 2% threshold, increased to the observed A/A variation if larger:

| Compiler | Before: time Δ | After: time Δ | Noise threshold |
|---|--:|--:|--:|
| GCC 15.2 | +2.32% | +1.37% | 2.32% |
| Clang 21.1 | -0.30% | +0.24% | 2.00% |

Changes at or below this threshold are inconclusive in this run.
The threshold is a reporting rule, not a statistical confidence interval.

Intel elapsed results are excluded: identical-binary A/A reached approximately
−50% and +93%. The GCC 13/14 and Clang 18/20 counter tables are diagnostic only.
There is no valid Intel elapsed-performance conclusion.

Delimiter and HTTP rows check unchanged short-search paths; their timing changes
are not attributed to a new search algorithm. The 32-byte early-match controls
exercise the new dispatcher with the wide table.

[Absolute counters](counters.md) · [Compiler counter tables](cycles.md) · [Raw measurements](data/native.tar.gz) · [Reproduce](reproduce.md).

### GCC 15.2

| Case | Bytes | master µs | compact µs | Time Δ | Cycles Δ | Instr. Δ |
|---|--:|--:|--:|--:|--:|--:|
| English moderation post | 1081 | 2.9496 | 2.6783 | -9.20% | -10.19% | -5.76% |
| Russian moderation post | 1041 | 3.0331 | 2.8469 | -6.14% | -5.18% | -3.43% |
| Spanish moderation post | 1086 | 2.8435 | 2.5977 | -8.65% | -8.85% | -5.77% |
| Arabic moderation post | 1036 | 3.9634 | 3.7680 | -4.93% | -4.79% | -3.99% |
| Hindi moderation post | 1091 | 2.6601 | 2.4853 | -6.57% | -6.95% | -4.96% |
| Chinese moderation post | 1039 | 2.3145 | 2.0789 | -10.18% | -9.91% | -7.75% |
| Japanese moderation post | 1069 | 3.2940 | 3.1229 | -5.20% | -8.56% | -5.32% |
| Korean moderation post | 1098 | 3.1239 | 2.8635 | -8.34% | -7.75% | -5.18% |
| Mixed emoji moderation post | 1097 | 2.6857 | 2.4525 | -8.68% | -9.06% | -6.22% |
| English moderation thread | 65548 | 169.3483 | 157.9180 | -6.75% | -6.99% | -0.13% |
| Chinese moderation thread | 65620 | 149.5828 | 139.0386 | -7.05% | -7.06% | -0.17% |
| Split fields on two pipes | 4123 | 2.5352 | 2.4895 | -1.80% | -0.25% | -0.00% |
| Split fields on `::` | 4099 | 2.5143 | 2.5089 | -0.22% | -0.92% | +0.00% |
| Parse HTTP headers | 65848 | 0.8704 | 0.8702 | -0.02% | +0.89% | +0.00% |
| Replace template placeholders | 4250 | 7.0374 | 5.9181 | -15.91% | -16.10% | -17.63% |
| Count `{{order.id}}` slots | 4250 | 0.9989 | 0.8339 | -16.52% | -15.85% | -18.07% |
| 9-byte search (no match) | 14400 | 3.7974 | 3.4724 | -8.56% | -8.38% | -0.53% |
| 31-byte early match | 14438 | 0.0338 | 0.0297 | -12.30% | -19.15% | -18.72% |
| 32-byte early match (text) | 14439 | 0.0346 | 0.0359 | +3.86% | +2.57% | +0.64% |
| 32-byte early match (repeated a) | 16839 | 0.0399 | 0.0411 | +2.99% | -0.51% | +0.62% |

### Clang 21.1

| Case | Bytes | master µs | compact µs | Time Δ | Cycles Δ | Instr. Δ |
|---|--:|--:|--:|--:|--:|--:|
| English moderation post | 1081 | 2.8060 | 2.5239 | -10.05% | -9.62% | -1.89% |
| Russian moderation post | 1041 | 2.8824 | 2.7330 | -5.19% | -5.16% | -2.32% |
| Spanish moderation post | 1086 | 2.7112 | 2.4345 | -10.21% | -9.86% | -1.89% |
| Arabic moderation post | 1036 | 3.8715 | 3.6589 | -5.49% | -5.71% | -1.28% |
| Hindi moderation post | 1091 | 2.5331 | 2.3453 | -7.41% | -7.00% | -2.70% |
| Chinese moderation post | 1039 | 2.1935 | 1.9339 | -11.84% | -11.45% | -2.61% |
| Japanese moderation post | 1069 | 3.1576 | 2.8807 | -8.77% | -9.26% | -1.73% |
| Korean moderation post | 1098 | 2.9995 | 2.7558 | -8.12% | -8.25% | -1.68% |
| Mixed emoji moderation post | 1097 | 2.5714 | 2.3065 | -10.30% | -10.25% | -2.05% |
| English moderation thread | 65548 | 161.4258 | 148.5095 | -8.00% | -7.99% | -0.04% |
| Chinese moderation thread | 65620 | 143.5457 | 131.7750 | -8.20% | -8.22% | -0.05% |
| Split fields on two pipes | 4123 | 2.7295 | 2.6258 | -3.80% | +0.31% | -0.00% |
| Split fields on `::` | 4099 | 2.6946 | 2.7033 | +0.32% | -0.49% | -0.00% |
| Parse HTTP headers | 65848 | 0.8524 | 0.8262 | -3.07% | -1.81% | +0.00% |
| Replace template placeholders | 4250 | 6.4798 | 5.5455 | -14.42% | -14.44% | -6.37% |
| Count `{{order.id}}` slots | 4250 | 0.9404 | 0.7944 | -15.53% | -15.29% | -6.56% |
| 9-byte search (no match) | 14400 | 3.5678 | 3.1581 | -11.48% | -11.19% | -0.17% |
| 31-byte early match | 14438 | 0.0299 | 0.0266 | -10.92% | -13.73% | -7.45% |
| 32-byte early match (text) | 14439 | 0.0319 | 0.0320 | +0.48% | +1.07% | +2.67% |
| 32-byte early match (repeated a) | 16839 | 0.0373 | 0.0368 | -1.50% | -1.28% | +2.03% |

Long-thread cycle gains accompany less than 0.5% change in instructions. The
[profiles](profiles.md) do not isolate a single cause; code generation and placement also matter.

## Search-shape controls

The [4096-byte search matrix](search-controls.md) measures absent, early, late and repeated-prefix inputs, plus repeated `substr_count()`/`str_replace()` and long-needle controls. There are 21 elapsed cases per compiler, plus a separate GCC 15 repeated-prefix check at 64 bytes. That check takes 30.7851 → 40.2358 µs, +30.70% relative to master. The full 58-case counter sweep includes needle lengths 8–256.

## Measurement and limits

Measured 31 October 2026 on Ryzen 9 5950X, CPU 15, SMT sibling 31, performance
governor, turbo enabled. The core was not reserved for the benchmark. Matched release
builds use the `docker` profile; [flags and commands](reproduce.md).

Native ARM, Windows and 32-bit builds have not been tested.

## Correctness and reproduction

All eight tested release binaries pass 699 PHPT string tests each, with 62 skipped.
The full PHP ASan/UBSan build passes 680 tests, with 81 skipped. No run has failures
or warnings. The added PHPT checks 300 input combinations. GCC and Clang sanitizer
runs each compare the extracted matchers with libc on 20,000 seeded random inputs
and 135,460 input-length combinations with guard pages. The verifier detects both
injected faults with each compiler.

[Verification commands and logs](verify/README.md) · [Build and reproduce](reproduce.md) · [Raw native measurements](data/native.tar.gz) · [Unrounded values](metrics.json) · [Hashes](manifest.json).

Tables are generated by [build-report.py](build-report.py).
[check.py](check.py) verifies the archived measurements and displayed values;
`bench report check reports/compact-sunday` checks the report's links and native tables.
