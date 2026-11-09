# Prepared objects: length × dictionary size

The fixed primary grid contains 16 subject/dictionary combinations:

- Subject length: 128 B, 256 B, 1 KiB, 4 KiB.
- Dictionary size: 8, 16, 32, 48 keys.
- Operations: presence, unique matched keys, occurrence count, all occurrences,
  and replacement, measured separately.

This gives 80 prepared-call comparisons. Five further inputs can check the
smallest confirmed winning N at 128 bytes on the second background, one per
operation. There are no repeated one-shot measurements.

The dictionary and backgrounds are those of the [boundary study](../METHOD.md).
Dictionaries are ordered prefixes of the real 48-rule mapping. Presence inputs
have no matches. Each other input has one middle `StringIO` occurrence;
replacement uses `StringIO` → `io` and shortens the result by six bytes.
Inputs start explicitly at 128 B / 8 keys. These are controlled derived texts.

The native object and its A/A control are constructed before timing. Each sample
includes the call, result creation, consumption and release. Existing arguments,
callbacks and regex source strings are prepared, and PCRE caches are warm.
There is no constructor or destructor cost in the prepared-call interval.

The harness and comparators match the [256-byte slice](../short-256/METHOD.md),
including overlap-safe `substr_count()`/`strpos()` counting. Native algorithm
source and GCC 14 binaries are unchanged. This cohort has fresh samples and a
prepared-only timing schedule; earlier captures are not pooled with it.

Sampling uses 100 ms warmup and 15 rotated/reversed rounds targeting 40 ms per
implementation. A/A limit is 2%, maximum sample deviation 5%, SMT sibling busy
time 2%, with no CPU steal. Keep the first passing capture of at most two;
otherwise retain the first with a quality flag. A win requires a paired median
below 0.98 and every paired ratio below 1. A loss requires a median above 1.02
and every ratio above 1. Other qualified results are inconclusive.

Each selected input is checked against independent expected outputs before
timing; wrong expected output must be rejected. Five alternating 0/N pairs per
implementation measure user-mode cycles and instructions separately.

The main README lists all tested N at each length with the observed prepared
time and relative change. A win at one N does not guarantee a win at larger N.
Close results and quality flags remain visible with their measured values.
The five rows for 128 B / 8 keys show absolute reference and
prepared-call times. Full captures and the second-background checks remain in
the appendix. This grid does not determine how many calls amortize construction.
