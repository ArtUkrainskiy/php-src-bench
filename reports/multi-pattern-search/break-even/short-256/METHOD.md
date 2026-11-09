# 256-byte texts: prepared and one-shot operations

This is a separate fixed-length slice of the [boundary study](../METHOD.md).
It uses the same GCC 14 release CLI, module, timing collector and ordered 48-key
dictionary. Earlier timing samples are not reused or merged.

All texts are exactly **256 bytes**. Initial dictionary sizes are **1, 4, 16, 48**.
One additional grid point per method may narrow a gap between a non-winning and
a confirmed winning result. Both object lifetimes share one baseline capture.

The five operations use the same conditions as the parent study: `matches()`
has no matches; unique/count/all/replace have one middle `StringIO` occurrence.
Its replacement is `io`, so the replacement output is 250 bytes. Three presence
controls instead place dictionary key #25 at byte 8, in the middle and near the
end. The smallest confirmed prepared winning N is checked on the second text.

The maximum is **33 short inputs**: 20 initial, at most 5 refinements, 3 presence
controls and at most 5 second-text checks. One separate 4 KiB count input checks
whether the stronger count recipe changes the parent's conclusion: **34 inputs
in total at most**. The main tables show boundary pairs and an equal-dictionary
comparison, not every measured input.

Inputs, dictionary order, preprocessing, cache policy, exact-output checks, A/A
controls, 15 samples, 40 ms target, 100 ms warmup, two-attempt limit and paired
win/loss decisions match the parent collector. Five alternating 0/N pairs measure
cycles and instructions separately. Sources and licenses are linked from the
[application study](../../application-workloads/SOURCE.md).

The short-text harness adds a stronger count comparator: `substr_count()` for
keys that cannot overlap themselves, with a `strpos()` loop advancing one byte
for the remaining keys. Self-overlap eligibility is prepared outside timing.
Matches between different keys are still counted independently. A single safe
key also has a direct `substr_count()` baseline without a dictionary loop.
These recipes preserve the required overlapping-count semantics; this is not a
comparison against ordinary non-overlapping counting. The parent series did not
measure this additional recipe, so count results from the two series have
different sets of measured comparators.

A confirmed win applies to that input and object lifetime. A small prepared-call
win does not establish that construction pays off. Tests repeat a fixed short
text with warm caches and do not measure whole requests or production traffic.
