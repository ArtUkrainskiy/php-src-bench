# Captured observations

Measurements: 1 November 2026. [Report](../README.md).
This directory contains observations and metadata, not generated corpus text.
The reviewable inputs are in [corpus](../corpus/README.md).

| Files | Content |
|---|---|
| `elapsed-amd.json` | 402 A/B comparisons and 24 elapsed-time A/A controls |
| `elapsed-intel.json` | 636 core/control A/B comparisons and 32 elapsed-time A/A controls |
| `elapsed-intel-extensions.json` | 168 extension A/B comparisons and 16 elapsed-time A/A controls |
| `repeats-*.json` | 34 AMD, 36 Intel core and 1 Intel extension comparisons; separate from primary observations |
| `counters/*.json` | 40 native `bench compare` series, plus a separate one-case A/A validation; compatible with `bench table` |
| [metadata.json](metadata.json) | Exact revisions, equal candidate tree IDs, compiler/configure flags, binary/module hashes, fixture hashes and protocols |
| [counter-quality.json](counter-quality.json) | The disturbed A/A pair in Intel mbstring counters; original row remains in its series |
| [verification.json](verification.json) | Runtime checks on the 12 captured binaries and a wrong-needle mutation check; verification only, not a new timing series |
| [provenance.json](provenance.json) | Original capture filenames and SHA-256 before pathname normalization |
| [sha256.json](sha256.json) | SHA-256 of the exported JSON files; checked by the table renderer |

## Elapsed time fields

Each elapsed record keeps `date`, `env`, `config`, `suite`, `builds`, `cases` and
an `event` identifying its compiler, case and control status.
The per-case `sides.A/B` contain five `rounds` arrays, five `loop_ns` values,
iteration counts `n`, and input/output hashes. Each round has five samples.
The build labels map to the exact metadata; A is master and B is the candidate
unless the event explicitly identifies A/A. In an A/A event both labels match.

For side S and process round r:

```
round_time[S,r] = median(rounds[S,r]) - loop_ns[S,r]
reported_time[S] = median(round_time[S,r])
paired_delta[r] = 100 * (round_time[B,r] / round_time[A,r] - 1)
reported_delta = median(paired_delta)
```

Saved time values are nanoseconds per operation; Markdown displays microseconds.
The minimum and maximum are over the five paired deltas.
Noise flags use within-process scaled MAD above 5%, or max/min of process
medians above 1.10, on either side.

## Native counters

These are unchanged numeric observations in the native format. A row is:

```
[group, side, case_id, cycles, instructions, empty_cycles, empty_instructions]
```

Divide `(cycles - empty_cycles)` and `(instructions - empty_instructions)` by
`cases[case_id].n` for the counts per operation. For each group/case, side a and
side b arrays contain the same five paired passes in chronological order.
Compute each b/a ratio before taking its median. Groups `aa` and `aa2` are
master-against-master controls at the start/end of each counter suite.
They differ from the separate elapsed-time A/A controls, which also include
candidate-against-candidate cases.

The disturbed pair is native row 1741 (zero-based) of
[intel-extensions-mbstring.json](counters/intel-extensions-mbstring.json),
not an A/B observation. Exclude that A/A pair from quiet-control claims.
The separate [A/A validation](counters/intel-extensions-aa-validation.json)
does not overwrite or splice into the original series.

## Export and regeneration

[export.py](../tools/export.py) removes repeated build headers from elapsed
records and retains them once in metadata. Private binary, module and suite
paths are normalized to portable labels; no samples, counts, hashes, ordering
or expected outputs are changed. The recorded source hash of the original
extension suite refers to its capture-time loading wrapper, not the portable
suite path substituted for display. Both load the saved corpus. Capture fixture
hashes retain the documentation and checker present during timing. The published
checker adds stricter argument auditing; documentation has been updated. All
corpus JSON, suite entry points and runtime load/functions files still match
the capture hashes. These analysis and documentation changes do not alter a
measured input or PHP expression.

[render.py](../tools/render.py) computes the time tables directly from these
observations and counters. `bench table` renders the native counter blocks.
The exporter and renderer are analysis tools; neither changes the measured C
code, CLI binaries, JSON inputs or the PHP timing harness.
