# Measurement protocol

The saved [product corpus](../../corpus/multi-pattern-product/README.md) is loaded
before timing. Each iteration processes one complete saved job. Jobs rotate in a
fixed order, with iteration counts rounded to complete cycles through all jobs.
A publishing batch and an HTML/plain-text email pair remain complete jobs.
The same protocol also measures the [8–512-string extension](../../corpus/multi-pattern-scaling/README.md).

Equal dictionaries repeated in saved job records share one PHP array before
timing. This gives the native functions the same unchanged dictionary throughout
reuse, rather than different parsed copies with different cache footprints.
Different order-specific replacement maps remain separate. Input sharing is
recorded in the captured protocol and applies equally to every implementation.

`measure.py` takes paths, compiler and CPU from command arguments. It builds the
current extension against a release PHP runtime built with the `docker` profile.
The runtime source revision, flags, compiler, binary/module/source hashes, corpus
hash and harness hash are recorded with the results. Native functions and the
extension run in the same PHP process. PHP JIT and CLI opcache are disabled;
PCRE JIT is enabled and its version/settings are recorded.

## Correctness before timing

Every declared method is checked against every saved expected result in both
eligible lifecycles. MatchResult objects are normalized only for this check.
The smoke command also deliberately flips a presence result and must reject it.
The corpus verifier independently checks input facts and replacement counts.

## Lifecycles

- `request`: the input dictionary array already exists. Construct the object,
  literal regex or parallel replacement arrays as needed, process all documents,
  consume/release results, and release request-owned prepared state.
- `worker`: prepare an unchanged dictionary once, then process different saved
  jobs. A changed dictionary makes this mode fail. Per-order email maps therefore
  have no worker row; the two emails of one order share one preparation.

Recipes are compiled before timing to avoid method-dispatch switches inside each
query. Every job uses the same outer closure and document loop. The sink consumes
string lengths, array lengths or scalar results, then releases the result. These
application-loop costs are included in elapsed time. `matchAll()` keeps its natural
MatchResult objects, while the reference implementations build associative arrays;
no normalization is added to the timed extension path. These output representation
costs are part of the API comparison.

PCRE keys are escaped literally. Boolean presence needs no longest-first sorting.
Replacement alternatives are sorted longest first. Callback creation belongs to
preparation. Direct `preg_replace()` is used for eligible constant replacements.
Per-key PCRE patterns for overlapping enumeration are built in preparation, not
inside each query. Sequential `str_replace()` is included only in cases whose
saved outputs agree with that policy.

## Elapsed time

The default protocol uses 250 ms of warmup per method/lifecycle, then calibration
to approximately 1/15 second per sample. Fifteen samples give approximately one
second of measured processing per method/lifecycle. The original starting position uses `pass % method_count`, reversing odd
passes. For even method counts this does not balance all positions: the two-method
A/A order stays unchanged, and four methods visit only alternate position classes. The reported unit is nanoseconds per
complete job; summaries may display microseconds. No empty-loop subtraction is
applied to elapsed time. Paired deltas use samples from the same pass.

The main series intentionally has a warm PCRE compilation cache. Rebuilding a
pattern string does not bypass that cache. For every PCRE method, 15 separate
fresh processes additionally time their first complete request. PHP startup is
outside that timer. This first-request measurement includes preparation, query
and release, plus first-use effects; it is not a pure measurement of compilation.

A known static policy can supply a precomputed regex string and avoid constructing
it from an array for every job. The preparation-included rows measure a generic
dictionary-to-pattern conversion, not every possible application integration.
PHP's compiled PCRE cache is persistent across requests in a process; Matcher
objects are ordinary request-owned objects unless used inside a long-running
worker. Prepared PCRE timings therefore do not require the same object-lifetime
assumptions as a prepared Matcher. FPM request throughput is not measured here.

## Hardware counters and controls

Five counter passes alternate method order. Each pass measures N complete jobs
and a process with the same initialization and warmup but zero measured jobs;
subtract the latter and divide by N. The N/zero order alternates too. N targets
approximately 80 ms. User-space cycles and instructions are recorded with raw
`perf stat` output. These corrected counters include the common job-loop costs.

Before and after each compiler series, identical implementations are measured as
A and B on short presence and larger replacement tasks. An elapsed A/A median
outside 2% stops the run. Counter A/A samples are retained for interpretation.
The selected CPU's SMT sibling is observed for each row; more than 5% activity
stops the run and marks that row for remeasurement. Governor, boost and load are
recorded. A stopped series is not a complete performance result. Wide sample spans
remain in the main capture and trigger the additional confirmation below.

Raw samples, configuration files, hashes, correctness results and incremental
`results.json` live in the output directory supplied to the driver. Published tables are generated from complete captures; synthetic controls stay separate.


## Order confirmations

The main timed recipes are frozen. A separate copy changes only the rotation to
`intdiv(pass, 2) % method_count`, still reversing odd passes. Each consecutive pair
has reversed order; a complete 2×method-count cycle balances all positions.
Fifteen passes are a partial cycle. Selection is the union of all even-method-count
rows, candidate within 5% of the fastest alternative, and any method with sample
max/min above 1.10. This produces 34 GCC and 32 Clang rows. The original capture
is retained. Main hardware-counter order already alternates independently.

Corrected A/A controls run before and after confirmations, constructors and direct
batch tests. Some close pairwise rankings change; this does not isolate a causal
order effect, since process placement and measurement time also change.
The report presents close results as uncertain choices, not reliable wins.
Supplemental time calls explicitly use `memory_limit=1G`; the main time series
uses the `-n` default. Inputs, source, binaries and JIT settings are unchanged.
An observed sibling interval with zero elapsed jiffies is unknown, not proof of
an idle sibling. Positive intervals above 5% stop supplemental calls.

## Preparation and payback

Preparation covers two saved dictionary families and 11 sizes from 8 to 10,000,
for both classes and compilers. The first constructor is measured in five fresh
processes after input parsing; release and PHP startup are outside that timer.
Repeated build-and-release uses 15 samples. CPU and file caches are not cold.
[Construction tables](PREPARATION.md) state the two scopes separately.

A request-minus-worker estimate selects direct batch points. The batch harness
constructs one candidate object, processes B complete jobs, then releases it.
Existing parallel arrays, pattern strings and callbacks are already prepared;
PCRE caches are warm. Every method is checked before timing. A sufficient point
must beat every measured alternative in its native/PCRE group by at least a 2%
paired median margin. This rule does not establish confidence or an exact minimum.
The full model covers 124 dual-lifecycle case records per compiler; direct tests
cover 36 selected cases and 102 case/batch rows per compiler. Corpus plus case ID
forms the key because two control IDs appear in both corpora.

## Capture scopes

Every table uses the same final implementation; the input and timing scopes differ. One table does not replace another merely because its capture date is later.

| Tables | Inputs | What is timed |
|---|---|---|
| PRODUCT-CASES, MODERATION, SEARCH, REPLACEMENT, FULL-* | Application jobs and short-input dictionary-size corpus | Whole saved jobs; preparation-included and reuse sections are separate |
| LENGTH, LENGTH-PAYBACK | Fixed 128-key dictionaries; varying string lengths | One string or the stated reuse batch; full one-operation checks are explicit |
| FIXED-4K | Fixed 4 KiB strings; 8–512 keys or different match positions | Prepared call and directly measured construction + one call + destruction |
| BUILD-MEMORY | Loaded moderation/glossary/catalog dictionaries | Warm `new` only; retained memory added above the input |
| PREPARATION, MEMORY | Glossary/catalog and permuted control | First constructor, repeated build/release, or allocation snapshots; scopes are labeled |
| AMORTIZATION, PAYBACK-FULL, CONFIRMATION | Application and short-input dictionary-size cases | Complete reuse batches or order/noise repeats, not the fixed-length series |

## Data and source identity

The measured source revision is `287aaab7fb729d3a8e91c6fd35224c4359c343e3`.
All captured series have that revision and the same hashes for `strmatch.c`, `php_strmatch.h` and `strmatch_arginfo.h`. The renderer rejects an incomplete series or a different source identity.
Both release runtimes use parent `758c9ac5492848a54f9fd88fac2a54d5e6108c05`.
This is a pinned baseline, not a claim to be the latest master.
Four main series contain 500 case/lifecycle rows. Raw N/zero counter output is
included in the `*-perf.json` files; elapsed samples and correctness results are
in the companion JSON. The main importer verifies 8000 corrected counter samples.
The supplemental importer verifies 1168 raw subprocess outputs, batch sinks and
original-versus-confirmation identity. Memory has five fresh processes for each
of 44 configurations per compiler and its own allocation protocol in [Memory](MEMORY.md).

The published main measurement driver and harness match recorded hashes. The
portable supplemental Python controller changes machine paths/configuration and
removes the original wait-for-main queue, and preserves partial stdout/stderr on timeout. Its four timed PHP helpers are
byte-identical to the capture; their hashes are in the supplemental metadata.
Table rendering, imports and the memory layout model run outside measured windows.
A separate instrumented build cross-checks 32 C layout configurations against
[computed layout statistics](checks/layout.json); it supplies no timing samples.
[Final implementation checks](checks/final-validation.json) record the sixteen PHPT tests on GCC, Clang, ASan/UBSan and ZTS. Deliberately incorrect mutation variants in that file are correctness controls, not benchmark implementations.


## Fixed-length summary series

The main README uses a separate controlled series measured on 3 November 2026. It fixes each dictionary at 128 literal keys. Moderation uses 128/4096/16384/65536-byte texts; support search/replacement uses 512/4096/16384/65536 bytes. Four different saved variants have exactly the same size at each point. Complete cycles give each variant equal weight; one operation processes one string. A sample divides the elapsed time for all calls by their count; the report takes the median of 15 samples. These are not individual-document medians or a batch of four documents.

The English texts reorder saved authored paragraphs with a fixed seed, trim to word boundaries and use fewer than 80 trailing ASCII spaces. Longer texts repeat paragraphs. The policy source and support glossary are unchanged; the support workload is match-rich, while moderation has separate absent/start/middle/end cases. This is an input-length experiment, not a production trace. Result counts and replacement-output sizes change with length and are saved with each exact input. The 64 KiB cases are additional long-input controls.

The source revision and release profiles match the other series. Both compilers use 250 ms warmup, 15 samples totaling about one second per method, and five N−0 counter passes targeting 80 ms. Time orders reverse in pairs and rotate between pairs. The three-method cycle is partially covered by 15 passes. Before/after A/A, output checks, result-size aggregates, hardware-counter corrections and sibling observation are retained. The new harness changes only test-time mutations and corrected time order; the recipes and result consumption match the saved application harness.

Pure construction has its own timer around `new`, with a separate timer for destruction. The process and allocator are warm; the dictionary is already loaded. Adjacent hrtime calls are included and no empty-clock subtraction is applied. Search is excluded. Five separate fresh processes measure the additional retained object allocation and construction peak; getters validate the dictionary after the snapshot. The new memory snapshots are independent of the older family-based memory series. Both use Zend allocation counters, not RSS.

For each alternative, the reuse estimate is `floor((constructor + destructor)/(alternative_query - prepared_query)) + 1`. It uses the median of paired constructor/destructor sums and prepared median query times. Nonpositive query savings have no finite estimate; positive savings below 2% are marked close. That cutoff is a heuristic, not statistical confidence. Direct batches include one call and counts near 75%/125% of estimates, capped at 4096. They include one candidate construction/destruction, while native arrays/regex strings/callbacks are already prepared and PCRE caches are warm. Within this input-length series, direct checks cover absent/mixed cases through 16 KiB; early/middle/end and 64 KiB have estimates only. The separate [fixed 4 KiB matrix](FIXED-4K.md) directly measures one-operation lifetimes at all four match positions. Tested points do not prove the exact minimum or behavior at every larger count.

[Fixed-length full tables](LENGTH.md), [pure construction and retained memory](BUILD-MEMORY.md), [direct reuse checks](LENGTH-PAYBACK.md), and [raw capture audit](data/length-capture-audit.json) describe this series. Application-job and dictionary-size captures use the same implementation, with their own inputs and sampling scopes.

The length series measures only prepared worker calls. The inherited protocol field `first_requests: 15` describes the general driver's request mode; no fresh-process first requests were measured in this worker-only series or the fixed 4 KiB matrix.

## Fixed 4 KiB position and dictionary-size matrix

[FIXED-4K.md](FIXED-4K.md) is a separate capture of 18 saved cases with GCC 15.2 and Clang 21.1. All inputs are exactly 4096 bytes, four different variants cycled equally often. For the seven dictionary sizes (8–512 keys), the text bytes stay identical; dictionaries are growing prefixes of pinned lexicons. Moderation always returns false. In replacement, the number of matches and output size grow with dictionary size; this is an application workload, not an isolated cost-per-key experiment. Per-variant counts and all input bytes are [saved](../../corpus/multi-pattern-4k/README.md).

The four match-position cases keep 128 keys. Positive variants hit 1-based dictionary ranks 1, 37, 91 and 128, consistently at each position. Native loops follow that order. A sample averages full cycles of all four variants; its median across 15 samples is shown. Match-position and size tables use native/PCRE timings from the direct batch series alongside the candidate's full one-shot lifetime; prepared candidate timings come from the separate worker series.

Warmup, time/counter sampling, affinity, source and runtime checks follow the input-length protocol. Before/after one-shot A/A checks cover both object classes; their paired medians must remain within 2%. Lists of winning dictionary sizes require a paired-median saving of at least 2% against each comparator. This cutoff is a noise heuristic, not a confidence interval or a universal threshold. Full raw samples, A/A checks and prepared cycles/instructions are linked from the result tables.
