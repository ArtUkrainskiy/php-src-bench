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
`results.json` live in the output directory supplied to the driver. The public
report will be generated from completed results; synthetic controls stay separate.


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

## Data and source identity

The measured source revision is `287aaab7fb729d3a8e91c6fd35224c4359c343e3`.
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
