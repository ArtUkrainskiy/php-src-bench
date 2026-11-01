# Choosing a tool for literal search and replacement

Status: **prototype**, `Str\Matcher` / `Str\Replacer` 0.9-dev.
[Prototype branch](https://github.com/ArtUkrainskiy/php-src/tree/str-matcher-prototype).
Machine: AMD Ryzen 9 5950X, GCC 15.2 and Clang 21.1.

[Moderation tables](MODERATION.md) · [Search tables](SEARCH.md) · [Replacement tables](REPLACEMENT.md) · [Exact inputs](../../corpus/multi-pattern-scaling/README.md) · [Reproduce](REPRODUCE.md)

## Practical result

Here N is the number of distinct literal substrings. Reuse is the useful niche
in these saved English tasks. Creating a prepared object
for one comment or article does not beat the fastest measured existing method.
A real eight-article publishing job can amortize Replacer construction.
Moderation returns a boolean; search returns distinct matching terms. Replacement
uses the earliest start and longest key there, without rescanning inserted links.

| Task | Build and process one document from an array | Reuse an unchanged dictionary |
|---|---|---|
| Any moderation phrase, clean short comment | Loop wins at every tested N | Matcher wins at tested 16–512; PCRE at 8 |
| Distinct support terms in an article | Per-term `strpos()` wins at every tested N | Matcher wins at tested 16–512; 8 depends on compiler |
| Link support terms in an article | PCRE wins at 8–64; `strtr()` at 128–512 | Replacer wins at tested 16–512; PCRE at 8 |

For a **batch of eight different articles**, Replacer wins at tested 16–512 even
with construction included. These are measured configurations, not universal
thresholds or the exact minimum profitable batch size. The comparison includes
native PHP and PCRE; literal matching is case-sensitive, without word boundaries.
These are CLI jobs, not measured framework/FPM throughput; memory and other
architectures were not measured. The release-build series use 15 alternating
time samples per method and before/after A/A controls.

## Reading the tables

The controlled dictionary-size series measures **8, 16, 32, 64, 128, 256 and 512 strings** in
three separate tasks: moderation, search results and replacement. Within each
task, documents stay the same and nested dictionary sets grow. Additional everyday product
cases are in [separate application tables](PRODUCT-CASES.md).

**Main-table times are microseconds for one comment or one article; lower is better.**
The eight input examples are cycled evenly, not processed together as one job.
The separately labeled eight-article batch times cover all eight articles.
The lowest median for each compiler is bold; this does not imply statistical
significance. String count and preparation are explicit, rather than embedded
in task names.

- **Dictionary preparation included:** create the required object, pattern string
  or parallel arrays, process the job, consume/release results and prepared state.
  The original dictionary array already exists.
- **Dictionary already prepared:** process another job using an unchanged prepared
  dictionary. This represents reuse inside a request/batch or a long-running
  worker. It does not imply objects survive ordinary FPM request boundaries.

PCRE compilation caches are warm in both main-table modes; pattern construction
is still charged where preparation is included. [First requests in fresh processes](PCRE-FIRST.md)
are measured separately. Prepared-call times alone do not establish how many
calls repay construction.

If the application already has a static regex string, it can skip the array-to-pattern
conversion charged in the preparation-included PCRE rows. PHP also retains compiled
PCRE entries across requests in a process. Matcher objects do not automatically
survive ordinary request boundaries. Keep that distinction when choosing a tool;
these CLI job measurements are not FPM request-throughput measurements.

## 1. Moderation: does any configured substring occur?

Task: check a short English comment against a literal moderation policy.
Each timed call checks one comment. Eight independent examples are cycled; they are **56–84 UTF-8 bytes**, with **no
matching rule**. This is the ordinary clean-message path. `Loop` means early-exit
`str_contains()`; `PCRE` means one escaped `preg_match()` alternation; Matcher
returns the same boolean.

<!-- SCALE-MODERATION -->
### Dictionary preparation included

| Substrings | GCC loop | GCC PCRE | GCC Matcher | Clang loop | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | **0.281** | 0.710 | 1.398 | **0.291** | 0.683 | 1.353 |
| 16 | **0.434** | 1.237 | 3.615 | **0.455** | 1.233 | 3.462 |
| 32 | **0.786** | 2.558 | 10.546 | **0.829** | 2.553 | 9.892 |
| 64 | **1.457** | 4.891 | 21.533 | **1.557** | 4.986 | 20.686 |
| 128 | **2.870** | 9.920 | 47.788 | **3.238** | 10.031 | 44.924 |
| 256 | **6.749** | 19.853 | 90.183 | **7.679** | 20.075 | 86.337 |
| 512 | **16.077** | 48.315 | 165.833 | **17.685** | 50.060 | 158.689 |

### Dictionary already prepared

| Substrings | GCC loop | GCC PCRE | GCC Matcher | Clang loop | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 0.282 | **0.236** | 0.266 | 0.288 | **0.220** | 0.274 |
| 16 | 0.444 | 0.347 | **0.266** | 0.463 | 0.324 | **0.273** |
| 32 | 0.780 | 0.754 | **0.267** | 0.857 | 0.722 | **0.273** |
| 64 | 1.406 | 1.482 | **0.271** | 1.653 | 1.519 | **0.278** |
| 128 | 2.920 | 2.975 | **0.276** | 3.450 | 2.854 | **0.285** |
| 256 | 6.760 | 6.079 | **0.294** | 7.934 | 5.979 | **0.304** |
| 512 | 16.203 | 20.267 | **0.313** | 17.747 | 20.411 | **0.324** |

<!-- /SCALE-MODERATION -->

[All moderation tables](MODERATION.md) separately cover matches at the start,
in the body and near the end, plus detailed support messages of 749–817 bytes
without a match and messages quoting a matching term. Exact dictionary order,
match offsets and dictionary ranks are saved. The [512-string policy source](../../corpus/multi-pattern-scaling/moderation-words.json)
is pinned and licensed; matching is literal bytes, without the source library's
exceptions, wildcard rules, boundaries or case folding.

## 2. Search: which support terms occur?

Task: find the **distinct matching terms**, ordered by first position, in a help
article. Each timed call processes one article. Eight independently written English articles are **397–465 bytes** each.
The summary compares `strpos()` per term (`PHP`), literal `preg_match()` per term
(`PCRE`) and `Matcher::getMatchedKeywords()`.

This differs from a boolean presence check: a result must include both `order`
and `order number` when both match. A single ordinary regex alternation would
not enumerate every same-start term. The per-key PCRE path is a transparent exact
reference, not a claim that it is the fastest possible regex implementation.

<!-- SCALE-SEARCH -->
### Dictionary preparation included

| Substrings | GCC PHP | GCC PCRE | GCC Matcher | Clang PHP | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | **1.187** | 2.150 | 3.255 | **1.189** | 2.046 | 3.422 |
| 16 | **2.199** | 3.987 | 5.439 | **2.187** | 3.781 | 5.296 |
| 32 | **3.921** | 7.649 | 9.600 | **3.987** | 7.374 | 9.325 |
| 64 | **7.860** | 14.446 | 21.477 | **8.496** | 14.395 | 20.576 |
| 128 | **15.972** | 28.768 | 48.688 | **16.221** | 28.268 | 46.148 |
| 256 | **32.171** | 60.273 | 109.206 | **32.944** | 60.012 | 105.422 |
| 512 | **62.523** | 135.378 | 305.941 | **63.270** | 132.057 | 292.269 |

### Dictionary already prepared

| Substrings | GCC PHP | GCC PCRE | GCC Matcher | Clang PHP | Clang PCRE | Clang Matcher |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 1.184 | 1.488 | **1.149** | **1.176** | 1.463 | 1.343 |
| 16 | 2.160 | 2.737 | **1.228** | 2.283 | 2.827 | **1.429** |
| 32 | 3.907 | 5.238 | **1.356** | 3.968 | 5.272 | **1.542** |
| 64 | 7.909 | 9.853 | **1.569** | 8.181 | 9.868 | **1.732** |
| 128 | 15.961 | 19.092 | **1.886** | 16.301 | 19.088 | **2.055** |
| 256 | 31.978 | 39.282 | **1.958** | 32.852 | 38.661 | **2.112** |
| 512 | 62.095 | 92.959 | **2.110** | 62.293 | 93.300 | **2.292** |

<!-- /SCALE-SEARCH -->

[All search tables](SEARCH.md) also measure counting every overlapping occurrence
and returning all byte locations. MatchResult objects are normalized only for
correctness checks, not during timing. As the glossary grows, more terms may
match the unchanged articles; every dictionary and result count is inspectable.

## 3. Replacement: add support links to an article

Task: replace configured glossary terms with links in one help article. Inputs
are the same **397–465-byte** articles as above. `strtr()` and Replacer use the same
earliest-start/longest-key policy without rescanning inserted links. `PCRE` means
escaped, longest-first `preg_replace_callback()` with a map lookup.

Sequential `str_replace()` changes the result by rescanning inserted links and
is excluded from this task. It remains in equivalent everyday product cases.

<!-- SCALE-REPLACEMENT -->
### Dictionary preparation included

| Substrings | GCC strtr | GCC PCRE | GCC Replacer | Clang strtr | Clang PCRE | Clang Replacer |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 4.432 | **2.260** | 3.707 | 4.343 | **2.188** | 3.710 |
| 16 | 7.913 | **5.285** | 6.568 | 7.887 | **5.146** | 6.355 |
| 32 | 16.769 | **10.628** | 11.741 | 16.722 | **10.439** | 11.152 |
| 64 | 31.154 | **23.111** | 24.363 | 31.324 | **22.785** | 23.369 |
| 128 | **37.993** | 47.099 | 52.396 | **38.501** | 47.117 | 49.294 |
| 256 | **41.643** | 116.729 | 105.458 | **42.149** | 108.814 | 101.300 |
| 512 | **42.505** | 273.277 | 280.263 | **43.089** | 260.801 | 267.681 |

### Dictionary already prepared

| Substrings | GCC strtr | GCC PCRE | GCC Replacer | Clang strtr | Clang PCRE | Clang Replacer |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 4.449 | **0.701** | 1.257 | 4.263 | **0.699** | 1.357 |
| 16 | 7.878 | 1.988 | **1.335** | 7.902 | 1.990 | **1.407** |
| 32 | 16.793 | 3.814 | **1.462** | 16.776 | 3.818 | **1.502** |
| 64 | 31.114 | 6.938 | **1.606** | 31.261 | 6.887 | **1.633** |
| 128 | 37.987 | 10.983 | **1.786** | 38.414 | 11.881 | **1.778** |
| 256 | 41.586 | 22.755 | **1.852** | 42.097 | 22.092 | **1.873** |
| 512 | 42.540 | 69.161 | **2.079** | 42.954 | 67.445 | **2.005** |

<!-- /SCALE-REPLACEMENT -->

[All replacement tables](REPLACEMENT.md) also show a publishing job processing
eight different articles with one dictionary. That is a measured finite batch;
it must not be confused with the indefinitely prepared mode.

## What can be concluded about dictionary size?

The table below lists tested sizes where the prototype has a lower paired median
elapsed time than **every measured existing alternative, on both compilers**.
This is a median comparison, not a statistical confidence test; inspect the full
sample ranges for close results.

<!-- SIZE-CHOICE -->
| Task | Preparation included: tested N | Prepared dictionary: tested N |
|---|---|---|
| Moderation, no match | None | 16, 32, 64, 128, 256, 512 |
| Distinct support terms | None | 16, 32, 64, 128, 256, 512 |
| Link one article | None | 16, 32, 64, 128, 256, 512 |
| Link eight articles | 16, 32, 64, 128, 256, 512 | 16, 32, 64, 128, 256, 512 |
<!-- /SIZE-CHOICE -->

These are tested configurations, not universal thresholds. Dictionary lengths,
shared prefixes/suffixes, text, match position, required output and reuse affect
which tool wins. Untested counts between these points remain unknown. The size
series is English; the EN/RU/ZH moderation results are in the everyday
tables and do not establish size thresholds for those other languages.

For ordinary small substitutions, consult the application task before choosing
a prepared engine. In the everyday corpus, replacements with 4–24 keys
lose to the fastest measured existing alternative, including valid reuse modes.
That statement is about those saved tasks, not every possible small dictionary.
Registered-token masking also differs from glossary links: with one common
replacement, direct `preg_replace()` avoids a callback and is particularly strong
in the measured log jobs. Per-order email values change and require rebuilding
Replacer; a global prepared-object result cannot be applied to those requests.

## Inputs and complete measurements

- [Controlled size corpus](../../corpus/multi-pattern-scaling/README.md): unchanged
  English comments/articles, saved nested dictionaries and exact expected output.
- [Everyday corpus](../../corpus/multi-pattern-product/README.md): moderation in
  EN/RU/ZH, error markers, order emails, shop text, punctuation, spaces, URL
  migration, token redaction, chat formatting, support indexing and linking.
- [Everyday application tables](PRODUCT-CASES.md): task names, string counts,
  documents and preparation are separate.
- [Every alternative: time](FULL-TIME.md), [cycles](FULL-CYCLES.md),
  [instructions](FULL-INSTRUCTIONS.md), and [PCRE first requests](PCRE-FIRST.md).
- [Methodology](METHOD.md), [measurement driver](measure.py),
  [timed recipes](harness.php), [table renderer](render.py),
  [raw-data importer and audit](capture.py).

The main glossary has authored commerce/support terms; the moderation dictionary
uses a pinned MIT-licensed external lexicon. Neither set is a random ASCII
scaling filler or a production-frequency sample. Larger glossary configurations
can produce more results, so this is an application-shaped size experiment,
not an isolation of keyword count alone. Input size and result-count tables are
included with each operation's full tables.

## Machine, controls and correctness

<!-- RUN-STATUS -->
Both compilers × both corpora on this AMD machine are complete and use the shared-dictionary input policy.
<!-- /RUN-STATUS -->

Only the AMD system was used. Both compiler series use release PHP 8.7.0-dev at the same
parent revision, with the current extension compiled by that compiler. Runtime
flags use the `docker` profile: `-fstack-protector-strong -fpic -fpie -O2 -g`,
large-file defines and `-Wl,-O1 -pie`; `--enable-werror`. PHP JIT/CLI opcache are
disabled; PCRE 10.44 JIT is enabled. Exact revisions, flags, binary/source hashes
and settings are recorded with the samples.

CPU 15 is pinned; SMT sibling 31 is observed. Governor: performance; boost remains
enabled. Each method/lifecycle gets 250 ms warmup and 15 alternating time samples,
about one second of measured processing. Counters use five passes, subtracting
a matching initialization/warmup run with zero measured jobs. Time is the primary
metric; cycles/instructions provide supporting evidence.

### A/A controls

These identical-implementation controls run before and after each compiler
series. They do not bound every individual row's noise. Everyday and size series are identified separately. One original PCRE sample set
exceeded a 10% max/min spread and was [confirmed by remeasuring the complete case](CONFIRMATION.md); both results are preserved.

<!-- AA-TABLE -->
| Series | Compiler | Stage | Control | Time Δ | Cycles Δ | Instructions Δ |
|---|---|---|---|---:|---:|---:|
| Everyday cases | gcc15 | before | Short presence check | -0.391% | +0.045% | -0.000% |
| Everyday cases | gcc15 | before | Large log replacement | -0.012% | +0.124% | -0.000% |
| Everyday cases | gcc15 | after | Short presence check | -0.284% | +0.069% | +0.000% |
| Everyday cases | gcc15 | after | Large log replacement | +0.007% | -0.009% | -0.000% |
| Everyday cases | clang21 | before | Short presence check | -0.113% | +0.266% | -0.000% |
| Everyday cases | clang21 | before | Large log replacement | -0.017% | -0.029% | -0.000% |
| Everyday cases | clang21 | after | Short presence check | -0.237% | +0.105% | -0.000% |
| Everyday cases | clang21 | after | Large log replacement | -0.013% | +0.007% | -0.000% |
| Size series | gcc15 | before | Short presence check | -0.653% | +0.819% | -0.000% |
| Size series | gcc15 | before | Large log replacement | +0.014% | +0.011% | +0.000% |
| Size series | gcc15 | after | Short presence check | -0.402% | -0.095% | -0.000% |
| Size series | gcc15 | after | Large log replacement | -0.009% | +0.140% | -0.000% |
| Size series | clang21 | before | Short presence check | -0.173% | -0.071% | -0.000% |
| Size series | clang21 | before | Large log replacement | +0.011% | +0.015% | -0.000% |
| Size series | clang21 | after | Short presence check | -0.525% | -0.032% | +0.000% |
| Size series | clang21 | after | Large log replacement | +0.016% | +0.041% | +0.000% |
<!-- /AA-TABLE -->

The exact timed recipes must match saved expected output in every eligible
lifecycle before timing. The smoke check must reject an intentionally wrong
presence result. With shared inputs, the timed recipes also passed 5270 expected-output comparisons
across 250 case/lifecycle configurations under ASan/UBSan ([validation record](checks/asan-shared-input.json)).
No output normalization or fixture parsing is timed.

### Captured data

Everyday samples: [GCC](data/gcc15.json), [Clang](data/clang21.json).
Size-series samples: [GCC](data/size-gcc15.json), [Clang](data/size-clang21.json).
Everyday raw counter output: [GCC](data/gcc15-perf.json), [Clang](data/clang21-perf.json).
Size-series raw counter output: [GCC](data/size-gcc15-perf.json), [Clang](data/size-clang21-perf.json).
All 8000 corrected counter samples were recomputed from the raw N/zero runs;
elapsed samples and first-request samples match their raw outputs ([capture audit](data/capture-audit.json)).
Machine-local paths in public metadata use placeholders; metrics are unchanged.

### Reproduce

[Build, preflight, smoke, full-run and data-import commands](REPRODUCE.md).

Not measured: other machines/architectures, memory on these corpora, framework
throughput, or the exact minimum profitable batch size. No whole-application
speedup is claimed.
