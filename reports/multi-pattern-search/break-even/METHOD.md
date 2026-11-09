# Finding small inputs where preparation pays

This controlled series narrows the gaps between measured losses and wins. It uses
GCC 14.2 on the Intel Core i7-13700H, with the same release PHP CLI and strmatch
module as [the application series](../application-workloads/SOURCE.md).
Samples from that series are not reused.
The boundary, 256-byte and prepared-grid cohorts use logical P-core 10, with SMT
sibling 11 monitored; the application cohort used core 2 and sibling 3. The
build identities and affinity for each cohort remain in its own `data/build.json`.

## Two questions, not a full matrix

| Search | Fixed inputs | Parameter varied |
|---|---|---|
| One-shot: how short can the text be? | All 48 keys, one text background, fixed match count | Text length, 128 B–64 KiB |
| Prepared: how few keys can suffice? | 4 KiB text, fixed match count, nested ordered dictionaries | 1–48 keys |

Both object lifetimes are measured together on each selected input. They share
the same existing-method samples, so a row needs only one reference time.
One-shot includes construction, operation, result release and destruction;
prepared excludes construction and destruction. Existing arguments, callbacks
and regex patterns are prepared outside timing and PCRE caches are warm.

The schedule starts with the endpoints of each axis. It adds at most three
interior points per method and axis, prioritizing gaps between a non-winning
point and a winning point. If endpoints have the same outcome, interior probes
check for a reversal. The candidate grids and rules are frozen in [plan.json](plan.json).
This is a bounded search, not exhaustive enumeration or proof of monotonicity.

This initial cohort has a hard limit of **64 distinct measured inputs**, each
timed with both object lifetimes. The main report shows its one-shot length
boundaries and three presence controls, alongside the separate
[prepared grid](prepared-grid/METHOD.md) and [256-byte slice](short-256/METHOD.md).
Every observation, including losses, close results and flags, remains in the
detailed tables and raw captures.

## Dictionary and controlled texts

The [dictionary](dictionary.json) is CPython's 48-entry module-name mapping,
retaining its source order and values. Smaller dictionaries are ordered prefixes.
Keys have different lengths, 3–18 bytes; no artificial keys are added.

Two backgrounds are derived from [the saved open sources](../application-workloads/SOURCE.md):

- Primary: distinct ASCII paragraphs from the complete documentation files,
  excluding paragraphs containing any dictionary key.
- Validation: distinct ASCII Civil Comments texts without dictionary keys.

Blocks are joined once with blank lines; none are repeated. `plan.json` records
source identities, block hashes and background hashes. Lengths are prefixes of
these streams. These are controlled derived texts, not unchanged documents or
measurements of natural match frequencies.

`matches()` uses no-match inputs for the axis searches. The other methods use
exactly one `StringIO` occurrence in the middle. It remains dictionary entry #1
at every N; these operations must return all required results rather than stop
after the first matching key. Spaces around the insertion prevent accidental
nested matches. The number of occurrences stays fixed as length changes.
Replacement uses the saved `StringIO` → `io` rule, shortening the output by six
bytes. Output expansion is not varied in this series.

Three additional `matches()` inputs place `markupbase`, dictionary entry #25,
at byte 8, in the middle and eight bytes before the end. They use the primary
scan's first observed winning one-shot length, or 64 KiB if none won; later gap
probes do not change these controls. Each native
search may stop after reading the final byte of a found key; PHP loops may also
stop after a matching dictionary entry, and PCRE has its own search optimizations.

The smallest observed prepared N and one-shot length with a confirmed win for
each method are checked on the second background. A changed winner is reported,
not replaced by a more favorable input. No second full matrix is measured.

## Comparators and correctness

All applicable standard and PCRE recipes are measured: `str_contains()`/`strpos()`
loops, lookahead searches preserving overlaps, `strtr()`, eligible `str_replace()`,
and literal or prefix-factored PCRE. For one key, direct `str_contains()` and
direct unique-key lookup avoid charging an unnecessary PHP dictionary loop.

An independent byte-search oracle constructs expected results. Replacement uses
separate leftmost-longest selection. Every selected input is checked in both
lifetimes before timing; a deliberately wrong expected output must be rejected.
No C implementation changes are part of this study.

## Timing, controls and decisions

Each input has 100 ms warmup per implementation and 15 rotated/reversed rounds
targeting 40 ms per sample. Prepared and one-shot each have a separate A/A object.
The eligible existing recipe with the lowest median is the shared reference.
Displayed changes are ratios of medians; paired ratios and their min/max are saved.

A capture fails if A/A differs by more than 2%, native/control/reference sample
deviation exceeds 5%, SMT sibling load exceeds 2%, or CPU steal is observed.
The primary collector allows two attempts; keep the first passing attempt,
otherwise flag the first. Both lifetimes use the same chosen capture.

After the primary scan, a bounded follow-up can confirm at most six flagged
boundary inputs once more. A confirmation is used only if both modes pass.
Remaining input budget permits at most four further grid-gap probes, reserving
room to check new winners on the second background. The 64-input cap is unchanged.
This follow-up was specified after inspecting primary quality flags, before
collecting its additional samples. Original captures and the separate policy
remain available; no attempt is selected for having the fastest time.
If one slot remains and an upper endpoint is still flagged, that slot can probe
the unmeasured grid point between it and a confirmed loss. A second-text check
is then reported as unperformed if the budget is exhausted.

A confirmed win requires a paired median below 0.98 and every paired ratio below
1. A confirmed loss requires a paired median above 1.02 and every ratio above 1.
Other qualified observations are close. These are decision rules, not confidence
intervals. A flag or close result cannot serve as a confirmed losing endpoint.

Before each input, a half-second check requires at most 20% load on the measured
core and 2% on its sibling. The stricter 2% sibling limit and timing/A/A checks
apply throughout the actual capture. PHP is pinned to one P-core; perf is pinned before it starts. Each
implementation also has five alternating 0/N counter pairs. User-mode cycles and
instructions are corrected by subtraction and reported separately from timing.

## What a boundary means

The report identifies the smallest **tested and confirmed** winning point and
the nearest smaller confirmed loss on that axis. Unmeasured intermediate values
remain unknown. A later reversal or failure on the second background prevents
turning that pair into a general "use it from N" recommendation.

The scope is one real dictionary family, two controlled English backgrounds,
zero or one occurrence, one CPU and GCC 14. It does not establish a universal
minimum for arbitrary dictionaries, dense outputs, Unicode processing or HTTP
requests. The broad application and controlled reports remain separate evidence.
