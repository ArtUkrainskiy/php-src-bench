# Compact Sunday shift table

Proposed php-src change: [php/php-src#25115](https://github.com/php/php-src/pull/25115),
[candidate branch](https://github.com/ArtUkrainskiy/php-src/tree/strpos-compact-sunday-pr).
Measured on 1 November 2026 against unmodified master at the branch base.

## Change and main result

Sunday is the existing forward substring search algorithm. The patch reduces
its table from 256 unsigned integers (1024 bytes on these builds) to 256 bytes
for short needles. It keeps the same
comparisons and shifts. The normal PHP entry path reaches this table for
**9–31-byte needles**, with at least **1024 bytes in the remaining search
span** (from the current search position). Search is byte-based, including
binary strings; this corpus uses UTF-8 text. Shorter searches use
the existing inline path. Needles of 32 bytes or more retain the integer table,
through a new dispatcher and a separate helper.

Less table initialization can reduce the fixed cost of a search. It does not
reduce the number of candidate comparisons or guarantee a faster scan.
The largest shift in the compact path is 32, which fits in a byte.

Across the 108 core application cases, all primary median times decreased on
AMD: **6.1–27.2% with GCC 15 and 4.5–22.0% with Clang 21** relative to each
compiler's master build. Some of those observations are noisy and are marked.
Intel gains depend more on the case and compiler; several long scans remain
close to master. On Intel, seven application cases slowed down in the primary
measurements and in a separate replication:
four Russian moderation cases with Clang 18 (**2.9–3.8% more time** in repeats) and three HTML
case-insensitive replacements with Clang 20 (**3.6–4.1% more time**).
A separate synthetic 64-byte-needle control takes about **31% more time**
with AMD/GCC 15, outside the compact-table range. Causes are not established.
These microbenchmarks do not establish an application-wide throughput gain.
Each warmed loop reuses one fixed input; it does not model a request mix, cold
data or changing documents.

[Full product results](tables/product.md) · [Raw data](data/README.md) · [Reproduce](reproduce.md)

## Reading the summary

EN, RU and ZH mean English, Russian and Chinese. A row times a whole PHP
operation. Moderation checks 12 phrases on a miss, or seven on a hit.
Start/middle/end describe saved match positions; [the case guide](#case-guide)
gives data and needle details.

Each percentage uses its own compiler/machine master. Negative means less
time; positive means slower. **†** flags excessive variation, with a separate
replication rather than a replacement result. A/A compares one unchanged binary
with itself. Fewer CPU instructions do
not by themselves mean faster execution. [Full interpretation and method](#machine-method-and-data).

## Main measurements

The table shows **primary measurements**. Regression replications are listed
separately below; their numbers can differ. The six percentage columns are
**time deltas**, not cycle counts.
¹ The absolute master time is for **AMD/GCC 15 only**, in microseconds; it gives
scale, not a common baseline across compilers. Each percentage uses its own
master. Absolute times for every compiler are in the full tables.

<!-- compact-summary -->
| Case | Master µs¹ | AMD GCC15 | AMD Clang21 | Intel GCC13 | Intel GCC14 | Intel Clang18 | Intel Clang20 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Moderation EN, 4 KiB, absent | 11.0671 | -9.06% | -10.73% | -0.48% | -0.96% | -1.71% | -0.53% |
| Moderation EN, 4 KiB, start | 6.6006 | -8.94% | -10.24%† | +0.01% | -1.35% | -1.86% | +0.16% |
| Moderation EN, 4 KiB, middle | 7.0249 | -8.88% | -10.29% | -0.14% | -0.56% | -1.90% | -0.10% |
| Moderation EN, 4 KiB, end | 7.5198 | -9.18% | -10.68% | +0.14% | -0.59% | -1.64% | -0.21% |
| Moderation RU, 4 KiB, absent | 9.5386 | -9.12% | -10.64% | -0.97% | -0.91% | -1.16% | -1.18% |
| Moderation RU, 4 KiB, start | 5.8293 | -8.65%† | -10.78% | -1.28% | -0.96% | -1.61% | -1.45% |
| Moderation RU, 4 KiB, middle | 6.3119 | -8.92% | -10.93% | -1.07% | -0.55% | -2.84% | -1.24% |
| Moderation RU, 4 KiB, end | 6.8314 | -8.86% | -10.90% | -0.14% | -0.49% | -2.52% | -2.04% |
| Moderation ZH, 4 KiB, absent | 8.7645 | -9.43% | -13.31% | -0.53%† | -0.96% | -1.75% | -0.65% |
| Moderation ZH, 4 KiB, start | 5.1308 | -9.32% | -11.07% | -1.16% | -1.67% | -3.57% | -0.48% |
| Moderation ZH, 4 KiB, middle | 5.4898 | -9.45% | -11.12% | -1.74% | -1.13% | -3.35% | -2.22%† |
| Moderation ZH, 4 KiB, end | 5.8190 | -9.33% | -11.08% | -2.05% | -0.45% | -2.45% | -0.84% |
| Moderation EN, 64 KiB, absent | 175.4803 | -8.48% | -9.58% | +0.44% | +0.02% | -0.54% | -0.50% |
| Moderation RU, 64 KiB, absent | 192.7612 | -6.79% | -9.42% | +0.39% | -0.14% | +4.12% | -2.90% |
| Moderation ZH, 64 KiB, absent | 152.7082 | -7.72% | -9.17% | -0.80% | -0.69% | -0.80% | -2.53% |
| Order ID: strpos, 4 KiB, absent | 0.5959 | -9.86% | -10.68% | -2.44% | -1.01% | -0.43% | -1.52% |
| Order ID: strpos, 4 KiB, start | 0.0263 | -27.18% | -21.67% | -23.46% | -26.57%† | -9.99% | -11.40% |
| Order ID: strpos, 4 KiB, middle | 0.3121 | -9.84% | -10.74% | -3.30% | -2.71% | -3.20% | -2.17% |
| Order ID: strpos, 4 KiB, end | 0.6023 | -9.20% | -10.14% | -1.53% | -1.50% | -1.68% | -1.02% |
| Email: strstr, 4 KiB, middle | 0.3676 | -8.77% | -9.83% | -2.08% | -1.36% | -2.66% | -3.20% |
| Placeholder: substr_count, 17 matches | 0.6714 | -18.90% | -20.71% | -1.89% | -11.38% | -2.03%† | -1.85% |
| Placeholder: str_replace, 17 matches | 1.4390 | -16.94% | -17.88% | -3.49% | -5.44% | -3.14%† | -2.22% |
| HTML receipt: str_ireplace, equal length | 0.5250 | -10.26% | -9.42% | -4.02% | +2.10% | -8.31%† | +3.73% |
| Placeholder: single-key strtr, 17 matches | 1.4394 | -17.29% | -18.37% | -3.00%† | -5.28% | -2.98% | -1.38% |
| MIME receipt: explode, all parts | 0.5208 | -10.18% | -9.21% | -3.16% | -3.33% | -3.34% | -2.61% |
| MIME delivery: stream_get_line | 0.6272 | -7.63% | -7.62% | -1.93% | +0.14% | -0.98%† | -0.57% |
| JSON log: strpos, 68,022 B, absent | 12.3490 | -8.36% | -8.63% | +0.82% | -0.72% | -1.97% | +0.69%† |
| HTML support: strpos, 2,475 B, present | 0.0690 | -16.10%† | -16.09% | -11.34% | -11.63% | -10.00% | -8.22% |
<!-- /compact-summary -->

## Regressions and hypotheses

The following seven product cases slowed down in the primary series and in
all five pairs of a fresh replication. The original and repeated series are
kept separate. [Repeat times and ranges](tables/repeats.md) show their scale.

<!-- compact-regressions -->
| Intel case | Compiler | Primary Δ time | Repeat Δ time |
|---|---|---:|---:|
| `moderation/long/ru/absent` | clang18 | +4.12% | +2.92% |
| `moderation/long/ru/start` | clang18 | +4.72% | +3.82% |
| `moderation/long/ru/middle` | clang18 | +3.63% | +3.77% |
| `moderation/long/ru/end` | clang18 | +3.89% | +3.69% |
| `documents/ireplace/receipt/shorter` | clang20 | +4.27% | +4.09% |
| `documents/ireplace/receipt/equal` | clang20 | +3.73% | +3.64% |
| `documents/ireplace/receipt/longer` | clang20 | +4.32% | +4.06% |
<!-- /compact-regressions -->

For these cases, the primary counter series records fewer instructions but
more cycles. A smaller instruction count does not establish a speedup.
Possible causes include compiler loop scheduling, the dependency chain through
byte-table loads, and changed code placement or branch prediction. These are
**hypotheses**: branch-miss and front-end profiles were not collected for this
corpus, so no specific cause is established.

The synthetic `a…ab` search in 4096 `a` bytes is a separate diagnostic. With a
64-byte needle, AMD/GCC 15 takes about **31% more time**, including in the separate
two-argument `strpos()` check. This needle retains the integer-table algorithm.
The dispatcher, generated helper code and placement are plausible suspects;
this is not evidence that the byte table itself slows that path.
Other boundary controls also show positive deltas, including early matches
outside the compact range. They remain visible in [controls](tables/controls.md)
and [all positive deltas](tables/regressions.md). Small changes without a stable
repeat should not be assigned a mechanism.

## Case guide

The corpus has **108 core application cases, 42 extension cases and 51 controls**
per compiler, plus four correctness-only `strchr()` alias checks.
Every application needle is 9–31 **UTF-8 bytes**, not characters.
All texts, needles, exact lengths, positions, expressions and expected outputs
are saved in [reviewable JSON](corpus/README.md). The benchmark reads them directly;
the optional generator is not part of a measurement. The texts are constructed
fixtures, not captured production traffic.

| Workload | Data and operation |
|---|---|
| Moderation | EN/RU/ZH customer-message text, 4 KiB or 64 KiB base size; `str_contains()` checks up to 12 phrases. Absent means all 12 miss. A hit is the seventh phrase and stops after seven calls. |
| Match position | Absent, near start, middle and end are separate cases. In the position-controlled fixtures, start is byte 1; diagnostic origin cases start at byte 0. Added needle and newline bytes slightly increase the stated base size. |
| Direct search | `strpos()` finds a 16-byte order ID; `str_contains()` a 31-byte warning; `strstr()` a 21-byte email address in about 4 KiB. A separate order-ID suite uses 64 KiB. |
| Count and replace | `substr_count()`, `str_replace()`, `str_ireplace()` and single-key `strtr()` process template placeholders. Position-controlled cases have one hit; repeated cases have 17 hits. Whole-operation time includes copies and allocations. |
| Complete documents | Independently composed posts, HTML receipt/support templates, JSON logs with similar references, and valid MIME messages. Replacement includes shorter/equal/longer values and three-key `str_replace()` arrays. |
| Delimiters | `explode()` splits on a 21-byte message boundary; `stream_get_line()` reads to a saved boundary in a prepared memory stream. Rewind and one read are timed, stream construction is not. |
| Irregular repeats | Saved HTML exports have 3 or 23 occurrences at unequal gaps, for counting, replacement and splitting. |
| Extensions | Five mbstring APIs use EN/RU/ZH with absent/middle matches; three grapheme APIs use ASCII with four match positions. See [caller coverage](coverage.md). |

The summary selects 28 core application rows to cover languages, positions,
long inputs and the main PHP APIs. It is not a list of the fastest cases.
[All product rows](tables/product.md), [extensions](tables/extensions.md),
[controls](tables/controls.md), [replications](tables/repeats.md) and
[all positive primary deltas](tables/regressions.md) are separate tables.
`explode('::', ...)` and `explode('||', ...)` cannot use this compact path and
are not presented as benefit cases. Short 256-byte moderation is a control.

### Detailed interpretation

**Time is the deciding metric.** Each percentage compares the candidate with
that compiler's matching master binary. Negative means less elapsed time;
positive means a slowdown. The percentage is the median of five paired
candidate/master ratios, after subtracting empty-loop cost. It can differ from
the ratio of the two displayed median times. All times are per **whole PHP
operation**, so a moderation row includes several searches.

The observed minimum/maximum in the full tables is not a confidence interval.
**†** marks sample MAD above 5% or process spread above 10%. Such rows were
replicated separately, preserving the primary data; small noisy differences
should not be treated as established gains or regressions. A/A compares the
same unchanged binary with itself and measures run-to-run variation.

## Machine, method and data

Two x86-64 machines were measured: **Ryzen 9 5950X**, GCC 15.2 / Clang 21.1,
CPU 15 with SMT sibling 31, `performance` governor and boost enabled; and
**Core i7-13700H**, GCC 13.3 / GCC 14.2 / Clang 18.1 / Clang 20.1,
P-core CPU 2 with sibling 3, `powersave` governor and turbo enabled, on AC.
No frequency, IRQ or scheduler settings were changed. Idle checks can delay
process starts; this was not a fully isolated operating system.

Release, non-ZTS CLI builds use the repository's `docker` flag profile:
`-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64`,
linked with `-Wl,-O1 -pie`, configured with `--enable-werror`.
This names a build profile; the benchmarks ran on the hosts.
The exact compiler/configure strings, binary hashes and measured source IDs
are in [metadata](data/metadata.json). The captured candidate and the linked
branch revision have identical source trees; their commit metadata differs.

Elapsed time uses **500 ms warmup, five samples of approximately 200 ms per
process, five paired process rounds, AB/BA/AB/BA/AB**. Cycles and instructions
use separate native `bench compare` series with five alternating passes and a
50 ms target. Both subtract a matching empty loop. They are not simultaneous
measurements and must not be combined into a measured IPC value.

Full native counter tables include absolute master cycles, paired ranges,
instruction deltas and per-suite A/A: [AMD](tables/counters-amd.md),
[Intel core](tables/counters-intel.md), [Intel extensions](tables/counters-intel-extensions.md).
Absolute cycles and instructions for both sides are in [CPU counts](tables/cpu.md),
with exact observations in the linked native JSON. Counts per operation are
derived as `(count − empty_count) / iterations`.
[A/A and quality notes](tables/aa.md) identify one mbstring counter-control pair
that ran after an idle timeout. That pair is not a quiet control. The original
is retained, and a separate fresh five-pair A/A validation is provided.

## Verification and limits

[Fixture validation](tools/validate.php) checks exact results against expectations
computed independently in Python, including alias checks. The [verification
record](data/verification.json) identifies the checked binaries and fixture hashes. All 205 fixtures
passed on both binaries for all six compiler/machine configurations, with
matching extension modules where needed. Each measured A/B observation also
has matching input/output hashes. Streams are checked twice on a prepared
resource. [Structural checks](tools/check.py) validate lengths, hashes, positions,
actual PHP search arguments, MIME/log structure and the compact-range rules.
A deliberate wrong-needle mutation was caught by the structural checker.

These fixture checks do not replace PHPT or sanitizer validation. No new
full-PHP sanitizer run or full PHPT suite was run as part of this corpus series.
No ARM64, Windows, 32-bit, ZTS, JIT, FPM request load or framework throughput
was measured. The [caller inventory](coverage.md) distinguishes measured APIs,
conditional internal callers and unchanged mechanisms; session serialization
and deserialization are not optimized by this patch.

[Reproduce and regenerate the tables](reproduce.md).
Raw observations and normalization rules are described in [data](data/README.md).
