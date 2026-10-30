# Report layout and provenance

This directory evaluates only stock PHP `ef99f4248f1450c39fb86fd7fd6f24c49b8d11eb`
against candidate `ca89fb5fb96399ed730cacb12d948025f83c4e6e`.
There are no alternative candidate implementations or PR-description drafts here.

| Location | Purpose |
|---|---|
| [README.md](README.md) | Main findings, everyday operations, losses and method |
| [REPRODUCE.md](REPRODUCE.md) | Build, corpus, measurement and validation commands |
| [change.patch](change.patch) | Exact source change against the stated stock commit |
| `tables/` | Generated full product tables, controls, confirmations and stress guards |
| `data/amd/` | Final warmed one-second AMD runs, pilot A/A, compiler cycles and finite confirmations |
| `data/intel/` | Quiet Intel original runs, preselected focus, quality rechecks, A/A, early confirmations and fresh cycles |
| `data/stress/` | Same-candidate routing boundaries and repeated-prefix cycle series |
| `data/profiles/` | Same-candidate profiles and disassembly used by the interpretation |
| [data/corpus-manifest.json](data/corpus-manifest.json) | Frozen input sizes, SHA-256 and expressions |
| [data/primary-cases.json](data/primary-cases.json) | The unchanged 76-case primary selection |
| [data/quality.json](data/quality.json) | Idle-wait flags preserved when loose stdout logs were grouped |
| [data/metrics.tsv](data/metrics.tsv) | Absolute values, deltas, quality and selected source for every compiler/case |
| [data/report-manifest.json](data/report-manifest.json) | Hashes of the raw evidence used by the generator |
| [verify/README.md](verify/README.md) | Correctness, sanitizer, mutation and work-budget checks |
| [scripts/build_report.py](scripts/build_report.py) | The single active report/table generator; `--check` verifies its output |
| [scripts/audit.py](scripts/audit.py) | Independent numeric arithmetic, evidence, archives, link and layout checks |
| [scripts/reproduce.py](scripts/reproduce.py) | Native warmed measurement driver with frozen-input checks |

The original AMD per-case JSON files are kept losslessly in
[data/amd/native-parts.tar.gz](data/amd/native-parts.tar.gz).
The two aggregated full-series JSON files keep every case, round and sample.
Archive member names match their `seconds_series.native_parts` entries. No run or
regression is removed by grouping these files. Existing stdout logs are grouped in
[data/run-logs.tar.gz](data/run-logs.tar.gz); profiles remain directly readable.
An aggregate is a convenience view of the native runs, not another experiment.

The [complete AMD confirmation table](tables/confirmations.md) retains all 23 selected
cases. All 39 native A/B or A/A series and eight profiling runs are preserved with
the fixed selection and policy. Original results are never replaced by their repeats.

The primary/full tables use separate elapsed-time and counter tables to keep them
readable. The TSV holds both together. Counters come from separate measurements,
so the tables do not imply simultaneous IPC.

Earlier busy-machine sweeps, alternative implementations, alignment experiments,
compiler-stability research, obsolete exporters, progress files and private drafts
are outside the publication directory. Their preserved history is not an input to
this report. The report generator needs only the files here and the benchmark tool.
