# Choosing a tool for literal search and replacement

Status: **RFC prototype**, `Str\Matcher` / `Str\Replacer` 0.9-dev.
[Source branch](https://github.com/ArtUkrainskiy/php-src/tree/str-matcher-prototype) · [PHP PR #25122](https://github.com/php/php-src/pull/25122).
Measured on AMD Ryzen 9 5950X with GCC 15.2 and Clang 21.1, 2 November 2026 UTC.
Exact measured revisions and binary hashes are recorded with the samples.

The prototype adds reusable literal dictionaries for case-sensitive byte search
and replacement.
It does not change existing string functions. This report compares equivalent
application tasks with saved input texts, dictionaries and expected output
against native PHP and PCRE, including preparation,
repeated use and memory. **Elapsed time is the primary metric.**

## Which tool fits these tasks?

Here N is the number of distinct literal substrings. In the saved English size
series, preparation determines the result as much as scanning does. Reuse means
multiple jobs on one object within a request, batch or long-running worker;
objects are not automatically shared between FPM requests.

| Task | Build and process one document from an array | Reuse an unchanged dictionary |
|---|---|---|
| Any moderation phrase, short comment without a match | `str_contains()` loop wins at every tested N | Matcher wins at tested 8–512 |
| List distinct matching support terms in an article | Per-term `strpos()` wins at every tested N | Matcher wins at tested 8–512 |
| Link support terms in an article | Replacer has lower medians at 32 and 64; 32 is close. PCRE or `strtr()` wins elsewhere | Replacer wins at tested 16–512; PCRE at 8 |

<!-- SHORT-COSTS -->
At 10,000 saved glossary/catalog entries, the prepared object adds **2.22 MiB for Matcher** or **1.29 MiB for Replacer**, above the input array. Constructor peaks above that same input baseline are 4.58 and 3.19 MiB respectively. [Memory](MEMORY.md) separates retained allocation, construction peak and query scratch space.
<!-- /SHORT-COSTS -->

PCRE compilation caches are warm in both columns. The first column still charges
array-to-pattern conversion; an existing regex string can avoid that work.

For a **batch of eight different articles**, Replacer wins at tested 16–512 even
with construction included. For ordinary order emails and incident-log redaction,
existing tools remain faster. Small substitution maps have mixed results depending
on task and compiler. The detailed tables include these losses.

These are measured configurations, not universal dictionary-size thresholds.
They do not establish a whole-application speedup. FPM throughput and other CPU
architectures were not measured. The memory series covers
8–10,000 strings; preparation has a measurable cost even when reuse is very fast.

<!-- SHORT-PAYBACK -->
For example, a 96-term Matcher listing support topics beat both prepared native and PCRE references by at least 2% in a batch of **5 articles**, on both compilers. This is a sufficient tested size, not the minimum. Other tasks and dictionaries need different reuse.
<!-- /SHORT-PAYBACK -->

[Direct batch tests](AMORTIZATION.md) list every measured sufficient reuse count
and the stronger baseline of already prepared native/PCRE alternatives.



## Reading the measurements

Main-table times are **microseconds per complete job; lower is better**.
For the size series, a job is one comment or article unless explicitly labeled
as an eight-article batch. Eight saved examples are cycled evenly; they are not
all processed in one job. The lowest median per compiler is bold. This is a
median comparison, not a significance test; inspect the per-pass relative changes in the full tables for close cells.

- **Dictionary preparation included:** the original dictionary array already
  exists. Create the object, regex string/callback or parallel arrays as needed,
  process the job, consume/release results and prepared state.
- **Dictionary already prepared:** prepare an unchanged dictionary once, then
  process another job. Reuse may occur within one request, a finite batch or a
  long-running worker. Objects do not automatically survive FPM request boundaries.

PCRE compilation caches are warm in both main modes. Preparation-included PCRE
rows still charge array-to-pattern conversion. An application with an existing
regex string can avoid that conversion. PHP retains compiled regex entries across
requests in a process; ordinary Matcher/Replacer objects have a different lifetime.
[First requests in fresh processes](PCRE-FIRST.md) are separate and exclude PHP startup.

Identical-code A/A control medians are within 0.8%, but do not bound every row's noise. Some close
rankings change in the [order confirmations](CONFIRMATION.md); small gaps should
not drive a choice. The main rotation and corrected repeats are described there.

## Moderation: does any configured substring occur?

Each job checks one short English comment against a literal policy.
The eight comments are **56–84 UTF-8 bytes**, with no matching rule.
`Loop` is early-exit `str_contains()`, `PCRE` is an escaped `preg_match()`
alternation, and Matcher returns the same boolean. All matching is case-sensitive
bytes, without word boundaries or Unicode normalization.

<!-- SCALE-MODERATION -->
### Dictionary preparation included

| Substrings | GCC loop | GCC PCRE | GCC Matcher | Clang loop | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | **0.280** | 0.713 | 2.377 | **0.288** | 0.680 | 2.381 |
| 16 | **0.439** | 1.246 | 5.203 | **0.459** | 1.262 | 5.000 |
| 32 | **0.784** | 2.524 | 12.839 | **0.866** | 2.561 | 12.537 |
| 64 | **1.486** | 4.893 | 26.274 | **1.567** | 5.033 | 25.620 |
| 128 | **3.066** | 9.877 | 58.269 | **3.282** | 10.033 | 56.921 |
| 256 | **6.946** | 19.905 | 152.716 | **7.770** | 20.214 | 149.700 |
| 512 | **16.053** | 49.053 | 295.062 | **17.434** | 50.212 | 293.707 |

### Dictionary already prepared

| Substrings | GCC loop | GCC PCRE | GCC Matcher | Clang loop | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 0.287 | 0.239 | **0.188** | 0.291 | 0.220 | **0.170** |
| 16 | 0.438 | 0.349 | **0.189** | 0.460 | 0.325 | **0.174** |
| 32 | 0.758 | 0.754 | **0.235** | 0.842 | 0.724 | **0.244** |
| 64 | 1.433 | 1.485 | **0.237** | 1.597 | 1.518 | **0.245** |
| 128 | 2.951 | 2.983 | **0.244** | 3.353 | 2.850 | **0.251** |
| 256 | 6.888 | 6.061 | **0.251** | 7.943 | 5.980 | **0.256** |
| 512 | 16.192 | 19.433 | **0.257** | 17.177 | 21.827 | **0.264** |

<!-- /SCALE-MODERATION -->

[Full moderation tables](MODERATION.md) also cover matches at the start, in the
body and near the end, plus 749–817-byte support messages with and without a
quoted matching term. EN/RU/ZH product cases are in [application tables](PRODUCT-CASES.md).
The [policy lexicon](../../corpus/multi-pattern-scaling/moderation-words.json) is
pinned and licensed. Its original exceptions, wildcard rules and case folding
are not part of this literal-substring task.

## Search: which support terms occur?

Each job returns **distinct matching terms**, ordered by first position, from one
help article. Eight saved English articles are **397–465 bytes** each.
`PHP` uses `strpos()` per term; `PCRE` uses a literal pattern per term;
Matcher uses `getMatchedKeywords()`.

The result includes both `order` and `order number` when both match.
A plain regex alternation would miss some same-start terms. The per-term PCRE
reference preserves this behavior; it is not a claim of optimal regex enumeration.

<!-- SCALE-SEARCH -->
### Dictionary preparation included

| Substrings | GCC PHP | GCC PCRE | GCC Matcher | Clang PHP | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | **1.172** | 2.136 | 3.104 | **1.178** | 2.011 | 3.022 |
| 16 | **2.165** | 3.940 | 5.075 | **2.192** | 3.932 | 4.848 |
| 32 | **3.902** | 7.576 | 10.109 | **4.073** | 7.428 | 9.180 |
| 64 | **7.966** | 14.764 | 20.066 | **8.192** | 14.306 | 19.083 |
| 128 | **16.370** | 28.618 | 47.354 | **16.790** | 27.920 | 46.074 |
| 256 | **31.955** | 60.688 | 134.225 | **32.932** | 59.825 | 129.482 |
| 512 | **61.675** | 134.538 | 362.329 | **63.028** | 131.120 | 348.421 |

### Dictionary already prepared

| Substrings | GCC PHP | GCC PCRE | GCC Matcher | Clang PHP | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 1.212 | 1.551 | **0.906** | 1.185 | 1.520 | **0.941** |
| 16 | 2.183 | 2.762 | **1.109** | 2.230 | 2.720 | **1.098** |
| 32 | 3.925 | 5.274 | **1.195** | 3.996 | 5.304 | **1.195** |
| 64 | 7.850 | 9.763 | **1.332** | 8.393 | 9.921 | **1.344** |
| 128 | 16.051 | 18.958 | **1.546** | 16.414 | 18.994 | **1.612** |
| 256 | 31.938 | 39.566 | **1.582** | 32.505 | 40.055 | **1.632** |
| 512 | 61.891 | 93.074 | **1.670** | 62.470 | 93.350 | **1.722** |

<!-- /SCALE-SEARCH -->

[Full search tables](SEARCH.md) also count every overlapping occurrence and return
all byte locations. MatchResult objects retain their natural representation during
timing. Normalization is used only for correctness checks. Larger dictionaries
can yield more results on the same articles.

## Replacement: add support links to an article

The same **397–465-byte** help articles receive glossary links.
`strtr()` and Replacer use earliest-start/longest-key replacement without rescanning
inserted links. `PCRE` is an escaped, longest-first `preg_replace_callback()`
alternation with a map lookup. Sequential `str_replace()` produces different
output here and is excluded; it is included in other tasks where outputs agree.

<!-- SCALE-REPLACEMENT -->
### Dictionary preparation included

| Substrings | GCC strtr | GCC PCRE | GCC Replacer | Clang strtr | Clang PCRE | Clang Replacer |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 4.463 | **2.262** | 3.603 | 4.318 | **2.188** | 3.479 |
| 16 | 7.893 | **5.383** | 6.168 | 7.861 | **5.085** | 5.940 |
| 32 | 16.843 | 10.735 | **10.672** | 16.754 | 10.482 | **10.145** |
| 64 | 31.181 | 23.194 | **20.033** | 31.365 | 22.563 | **19.495** |
| 128 | **38.064** | 47.387 | 46.884 | **38.490** | 47.048 | 45.110 |
| 256 | **41.730** | 113.529 | 115.259 | **42.219** | 107.227 | 112.640 |
| 512 | **42.546** | 264.934 | 292.481 | **43.034** | 265.663 | 288.989 |

### Dictionary already prepared

| Substrings | GCC strtr | GCC PCRE | GCC Replacer | Clang strtr | Clang PCRE | Clang Replacer |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 4.464 | **0.713** | 1.144 | 4.300 | **0.692** | 1.066 |
| 16 | 7.945 | 1.997 | **1.208** | 7.873 | 1.975 | **1.178** |
| 32 | 16.772 | 3.813 | **1.307** | 16.761 | 3.837 | **1.282** |
| 64 | 31.144 | 6.925 | **1.390** | 31.370 | 6.902 | **1.389** |
| 128 | 37.992 | 11.006 | **1.464** | 38.437 | 11.898 | **1.491** |
| 256 | 41.684 | 22.734 | **1.545** | 42.231 | 22.063 | **1.580** |
| 512 | 42.519 | 68.420 | **1.595** | 43.006 | 64.761 | **1.639** |

<!-- /SCALE-REPLACEMENT -->

With preparation included, N=64 has a clear lead in these measurements; N=32 is a
close comparison. This mode charges generic array-to-pattern preparation to PCRE.
It does **not** establish that building a Replacer beats an already available regex
for one article. See direct batches below for that comparison.
[Replacement tables](REPLACEMENT.md) also include the complete eight-article job.

## How many jobs repay preparation?

**≤B is a sufficient measured batch, not an exact minimum.** At that tested size,
building one Matcher/Replacer and processing B jobs took at least 2% less median
time than every measured alternative in that column's group. Native arrays and
regex strings/callbacks are already prepared; PCRE caches are warm. These are
stricter baselines than the preparation-included tables above.

<!-- PAYBACK-TABLE -->
| Task | Strings | GCC native | GCC PCRE | Clang native | Clang PCRE |
|---|---:|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | 12 | ≤285 | ≤690 | ≤719 | — |
| [List the configured support topics mentioned in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | ≤5 | ≤5 | ≤5 | ≤5 |
| [Count all configured term occurrences in a help article](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | ≤6 | ≤3 | ≤6 | ≤3 |
| [Locate all configured term occurrences for a search index](../../corpus/multi-pattern-product/suites/help-index.json) | 96 | ≤5 | ≤1 | ≤5 | ≤1 |
| [Link configured support terms in one plain-text help article](../../corpus/multi-pattern-product/suites/help-linking.json) | 96 | ≤4 | ≤7 | ≤3 | ≤6 |
| [Mask three registered secrets in a larger incident log batch](../../corpus/multi-pattern-product/suites/secret-redaction.json) | 24 | — | — | — | — |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | 512 | ≤24 | ≤18 | ≤23 | ≤17 |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | 512 | ≤11 | ≤7 | ≤10 | ≤6 |
<!-- /PAYBACK-TABLE -->

A dash means no qualifying win at the tested points. Points were selected using
an estimate and need not be consecutive. For example, a large bound for a short
comment does not prove every smaller batch loses. [All tested batch sizes](AMORTIZATION.md)
and [absolute times with paired ranges](PAYBACK-FULL.md) are separate. A 2% median
margin is a reporting rule, not statistical confidence.

## Memory and construction: 8 to 10,000 strings

**KiB (1024 bytes), measured Zend allocations.** Input is the original PHP list or
replacement map including its strings. **+Matcher / +Replacer** is additional
retained object allocation with that input alive. **Peak +** is the constructor's
maximum increase above that baseline, including the final object.
Five fresh processes per configuration and both compilers gave identical byte counts.

<!-- MEMORY-TABLE -->
| Strings | Matcher input | +Matcher | Peak +Matcher | Replacer input | +Replacer | Peak +Replacer |
|---|---:|---:|---:|---:|---:|---:|
| 8 | 0.6 | 3.5 | 5.1 | 1.3 | 3.5 | 7.4 |
| 16 | 1.1 | 5.7 | 8.9 | 2.4 | 6.2 | 12.0 |
| 32 | 2.0 | 10.6 | 19.1 | 4.6 | 13.6 | 25.1 |
| 64 | 3.9 | 29.4 | 41.4 | 9.1 | 24.4 | 45.4 |
| 128 | 7.6 | 46.1 | 86.1 | 21.1 | 43.2 | 91.2 |
| 256 | 18.5 | 83.8 | 151.8 | 38.5 | 70.2 | 154.2 |
| 512 | 33.0 | 187.8 | 307.8 | 73.0 | 140.8 | 296.8 |
| 1000 | 67.6 | 400.8 | 712.8 | 150.1 | 232.8 | 592.8 |
| 2000 | 138.1 | 728.8 | 1352.8 | 307.1 | 368.8 | 884.8 |
| 5000 | 397.4 | 1396.8 | 2624.8 | 897.9 | 760.8 | 2384.8 |
| 10000 | 797.7 | 2272.8 | 4688.8 | 1802.7 | 1324.8 | 3264.8 |
<!-- /MEMORY-TABLE -->

<!-- MEMORY-GROWTH -->
From 1,000 to 10,000 strings in these saved inputs, Matcher: 0.39 to 2.22 MiB (5.67 times); Replacer: 0.23 to 1.29 MiB (5.69 times). The 10,000-string permuted-byte control takes 7.43 MiB for Matcher and 5.68 MiB for Replacer. These are observed endpoints, not a fitted growth law.
<!-- /MEMORY-GROWTH -->

The immutable automaton uses dense transitions near the root and selected fallback
states, compact edges elsewhere, and state arrays sized to actual states.
Runtime automaton arrays have a linear upper bound in **total key bytes** for the
bounded byte alphabet. Retained replacement string bodies are outside that bound.
It is not a fixed number of bytes per dictionary entry. Shared prefixes/suffixes,
alphabet and dense-state selection change the curve. [Memory tables and plot](MEMORY.md)
include a permuted-byte control with the same key lengths.
[Construction tables](PREPARATION.md) separate the first constructor in a fresh
process from repeated build-and-release. Neither is PHP startup or a cold CPU-cache test.
These are Zend allocation counters, not process RSS or allocator-reserved pages.

## Cases where existing tools remain useful

Per-order emails use changing values and require new preparation. The measured
10-placeholder job favors `strtr()`. Incident-log token masking favors direct
`preg_replace()`: one common replacement avoids a callback. A prepared dictionary
is not sufficient by itself to make the new API faster for these tasks.

Small punctuation/chat maps are sensitive to the task and compiler. Close rankings
also move in the order confirmations. The [application tables](PRODUCT-CASES.md)
show every eligible alternative and lifecycle, including URL migrations and
redaction jobs. Do not transfer a glossary-link result to these different outputs.

## Inputs and complete results

- [Saved size corpus](../../corpus/multi-pattern-scaling/README.md): exact nested
  dictionaries, unchanged comments/articles, expected outputs and match positions.
- [Saved application corpus](../../corpus/multi-pattern-product/README.md): moderation
  in EN/RU/ZH, error markers, emails, shop text, punctuation, spaces, URL migration,
  token redaction, chat formatting, support indexing and linking.
- [Application tables](PRODUCT-CASES.md), [all elapsed times](FULL-TIME.md),
  [cycles](FULL-CYCLES.md), [instructions](FULL-INSTRUCTIONS.md),
  [PCRE first requests](PCRE-FIRST.md), [order confirmations](CONFIRMATION.md).

The support glossary is authored application data; moderation uses a pinned external
lexicon. Neither is a production-frequency sample. Two labeled synthetic controls
stay in the full tables. No claims rely on them as everyday workloads.

## Machine, protocol and verification

Only this AMD system was measured. Both compiler series use release PHP 8.7.0-dev
at the same parent revision, with the extension built by that compiler.
The `docker` build profile uses `-fstack-protector-strong -fpic -fpie -O2 -g`,
large-file defines and `-Wl,-O1 -pie`; `--enable-werror` is enabled.
PHP JIT/CLI opcache are off; PCRE 10.44 JIT is on.

CPU 15 is pinned; sibling 31 is observed. Governor is performance, boost on.
Each method/lifecycle has 250 ms warmup and 15 elapsed samples, about one second
of measured work. Five counter passes subtract matching N−0 runs targeting 80 ms.
[Methodology](METHOD.md) describes the sampling and order limitations.

Identical-implementation A/A controls run before and after each series.
The main elapsed A/A medians are within 0.8%; this does not bound noise for every
individual row. Corrected-order and batch controls have their own A/A records.

<!-- AA-TABLE -->
| Series | Compiler | Stage | Control | Time Δ | Cycles Δ | Instructions Δ |
|---|---|---|---|---:|---:|---:|
| Everyday cases | gcc15 | before | Short presence check | +0.025% | +0.036% | -0.000% |
| Everyday cases | gcc15 | before | Large log replacement | +0.033% | -0.069% | -0.000% |
| Everyday cases | gcc15 | after | Short presence check | -0.777% | -0.272% | +0.000% |
| Everyday cases | gcc15 | after | Large log replacement | -0.017% | +0.037% | -0.000% |
| Everyday cases | clang21 | before | Short presence check | -0.147% | +0.027% | +0.000% |
| Everyday cases | clang21 | before | Large log replacement | +0.089% | -0.268% | +0.000% |
| Everyday cases | clang21 | after | Short presence check | +0.067% | -0.261% | +0.000% |
| Everyday cases | clang21 | after | Large log replacement | -0.012% | -0.470% | +0.000% |
| Size series | gcc15 | before | Short presence check | -0.030% | -0.231% | +0.000% |
| Size series | gcc15 | before | Large log replacement | -0.080% | -0.245% | +0.000% |
| Size series | gcc15 | after | Short presence check | -0.074% | -0.111% | -0.000% |
| Size series | gcc15 | after | Large log replacement | -0.014% | +0.295% | -0.000% |
| Size series | clang21 | before | Short presence check | +0.570% | -0.120% | +0.000% |
| Size series | clang21 | before | Large log replacement | +0.043% | +0.360% | -0.000% |
| Size series | clang21 | after | Short presence check | -0.073% | -0.015% | -0.000% |
| Size series | clang21 | after | Large log replacement | -0.010% | -0.228% | -0.000% |
<!-- /AA-TABLE -->

Every timed recipe is checked against saved expected output before timing.
Smoke tests must reject an intentionally wrong presence result. The final source
also passes the 16 PHPT files on GCC, Clang, ASan/UBSan and debug ZTS;
[validation evidence](checks/final-validation.json) records their scope.

Main captures are [GCC](data/gcc15.json), [Clang](data/clang21.json),
[size GCC](data/size-gcc15.json) and [size Clang](data/size-clang21.json).
All 8000 corrected counter samples were recomputed from raw N/zero outputs;
elapsed and first-request samples match raw stdout ([audit](data/capture-audit.json)).
The [supplement audit](data/supplement-capture-audit.json) checks 1168 raw outputs,
original-versus-repeat identity and batch result aggregates. Public metadata uses
path placeholders; measurements are unchanged.

[Reproduce: builds, smoke tests, measurements and import](REPRODUCE.md).
[Main driver](measure.py) · [Timed recipes](harness.php) · [Table renderer](render.py) ·
[Supplemental measurements](supplements/measure.py).

Not measured: other machines/architectures, process RSS, existing alternatives'
memory, framework/FPM throughput, every possible regex formulation, or the exact
minimum profitable batch size. Results describe these saved jobs and configurations.
