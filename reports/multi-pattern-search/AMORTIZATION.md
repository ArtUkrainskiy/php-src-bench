# How many jobs repay preparation?

**≤B means a sufficient measured batch, not an exact minimum.** At that batch size the candidate's paired median time was at least 2% lower than every measured alternative in that column's group. A dash means no such point in the tested batches. It does not mean payback is impossible for every other input or batch size.

A job is the complete saved task. Most selected jobs contain one comment or article; the incident-log job contains one log document with 384 JSON records. See the corpus for each job. Dictionary strings and jobs per object are different counts.

Matcher/Replacer is constructed once per batch and released at its end. Native parallel arrays and regex strings/callbacks are already prepared, and PCRE compilation caches are warm. This deliberately compares the candidate against prepared existing tools. No PHP startup or input loading is timed. In contrast, the main preparation-included tables also charge array-to-regex or parallel-array preparation.

Native means every measured non-PCRE alternative for that task; PCRE means every measured regex alternative. Overlapping enumeration uses a pattern per term, rather than an ordinary alternation that would miss nested terms. All alternatives keep their natural result representation.

## Everyday jobs

| Task | Strings | GCC native | GCC PCRE | Clang native | Clang PCRE | GCC tested jobs | Clang tested jobs |
|---|---:|---:|---:|---:|---:|---|---|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | ≤285 | ≤690 | ≤719 | — | 1, 285, 345, 690 | 1, 719, 865, 1024 |
| [Flag a short RU comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | ≤53 | ≤66 | ≤58 | ≤72 | 1, 53, 66 | 1, 58, 72 |
| [Flag a short ZH comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | ≤102 | ≤125 | ≤90 | ≤111 | 1, 102, 125 | 1, 90, 111 |
| [Flag a short EN comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | ≤241 | ≤584 | ≤406 | ≤980 | 1, 241, 292, 584 | 1, 406, 490, 980 |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | — | — | — | — | 1, 8 | 1, 8 |
| [Flag a short EN comment: phrase at the end](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | — | — | — | — | 1, 8 | 1, 8 |
| [Check a detailed EN support message: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | — | — | — | — | 1, 8 | 1, 8 |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | ≤6 | ≤3 | ≤6 | ≤3 | 1, 3, 6 | 1, 3, 6 |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | ≤5 | ≤5 | ≤5 | ≤5 | 1, 2, 5 | 1, 2, 5 |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | ≤5 | ≤1 | ≤5 | ≤1 | 1, 2, 5 | 1, 2, 5 |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | ≤4 | ≤7 | ≤3 | ≤6 | 1, 4, 7 | 1, 3, 6 |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | 8 | — | — | — | ≤8 | 1, 8 | 1, 8 |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | 12 | — | — | — | — | 1, 8 | 1, 8 |
| [Mask registered secrets in a log excerpt with no leaked token](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | — | — | — | — | 1, 8 | 1, 8 |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | — | — | — | — | 1, 8 | 1, 8 |

## Controlled dictionary sizes

| Task | Strings | GCC native | GCC PCRE | Clang native | Clang PCRE | GCC tested jobs | Clang tested jobs |
|---|---:|---:|---:|---:|---:|---|---|
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 8 | ≤42 | ≤42 | ≤44 | ≤55 | 1, 42, 53 | 1, 44, 55 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 16 | ≤31 | ≤40 | ≤32 | ≤41 | 1, 31, 40 | 1, 32, 41 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 32 | ≤24 | ≤31 | ≤25 | ≤33 | 1, 24, 31 | 1, 25, 33 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 64 | ≤28 | ≤28 | ≤25 | ≤25 | 1, 21, 28 | 1, 19, 25 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 128 | ≤21 | ≤28 | ≤21 | ≤28 | 1, 21, 28 | 1, 21, 28 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 256 | ≤26 | ≤34 | ≤26 | ≤34 | 1, 26, 34 | 1, 26, 34 |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 512 | ≤24 | ≤18 | ≤23 | ≤17 | 1, 18, 24 | 1, 17, 23 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 8 | ≤11 | ≤7 | ≤12 | ≤8 | 1, 7, 11 | 1, 8, 12 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 16 | ≤6 | ≤3 | ≤6 | ≤3 | 1, 3, 6 | 1, 3, 6 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 32 | ≤6 | ≤3 | ≤5 | ≤2 | 1, 3, 6 | 1, 2, 5 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 64 | ≤5 | ≤5 | ≤5 | ≤5 | 1, 2, 5 | 1, 2, 5 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 128 | ≤6 | ≤3 | ≤3 | ≤3 | 1, 3, 6 | 1, 3, 6 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 256 | ≤7 | ≤4 | ≤7 | ≤4 | 1, 4, 7 | 1, 4, 7 |
| [Find distinct support terms](../../corpus/multi-pattern-scaling/suites/search.json) | 512 | ≤9 | ≤5 | ≤9 | ≤5 | 1, 5, 9 | 1, 5, 9 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 8 | ≤1 | — | ≤1 | — | 1, 8 | 1, 8 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 16 | ≤1 | ≤10 | ≤1 | ≤9 | 1, 6, 10 | 1, 5, 9 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 32 | ≤1 | ≤6 | ≤1 | ≤6 | 1, 3, 6 | 1, 3, 6 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 64 | ≤1 | ≤6 | ≤1 | ≤6 | 1, 3, 6 | 1, 3, 6 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 128 | ≤4 | ≤7 | ≤4 | ≤7 | 1, 4, 7 | 1, 4, 7 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 256 | ≤5 | ≤9 | ≤5 | ≤9 | 1, 5, 9 | 1, 5, 9 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | ≤11 | ≤7 | ≤10 | ≤6 | 1, 7, 11 | 1, 6, 10 |

## Estimated versus directly tested

The model uses the main case's request-minus-worker difference as an estimate P of preparation and release. If Q is the prepared candidate time and A the prepared alternative time, it solves `P + B×Q < B×A`. The reported model value is `floor(P/(A-Q)) + 1` only when the gap is positive. It is not the fresh-process constructor measurement and includes differences between request/worker wrappers.

Small differences produce unstable, sometimes very large estimates. A gap below 2% is marked small; a nonpositive estimated P is marked unstable. The model selects batch control points. The tables above use actual batches with a 2% median margin, without claiming statistical significance or an unmeasured minimum. The tested sizes need not be consecutive.

[All direct batch times and paired ranges](PAYBACK-FULL.md) · [GCC model](data/payback-model-gcc15.json) · [Clang model](data/payback-model-clang21.json). The model covers all 124 case records permitting both lifecycles per compiler, including labeled controls; 36 product/size cases receive direct batch checks.

## Controls and reproduction

Fifteen samples, 250 ms warmup and approximately one second of measured work per method. Orders are reversed in pairs; the start rotates between pairs. A complete 2×method-count cycle balances positions; 15 samples are a partial cycle. A/A controls before/after each compiler must stay within 2%. The selected CPU and its SMT sibling are monitored; zero-jiffy activity intervals are unknown, not zero-load observations.

See [Reproduce](REPRODUCE.md#additional-measurements) for the timed PHP files and portable controller. All methods are checked against saved expected output before each batch measurement. The importer also checks repeated-call result aggregates and raw stdout. These CLI jobs are not FPM throughput or a guarantee for every vocabulary.
