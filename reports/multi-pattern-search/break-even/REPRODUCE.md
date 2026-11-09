# Reproduce the boundary search

Use a release GCC 14 PHP CLI and matching strmatch module. [Build instructions
and environment JSON format](../application-workloads/REPRODUCE.md) are shared
with the application study. Exact identities for this run are in
`data/build.json` after collection. No new extension source changes are required.

Set `BOUNDARY_ENV` to your environment JSON, `BOUNDARY_RESULTS` to a new results
directory, and `BOUNDARY_CPU` / `BOUNDARY_SIBLING` to a P-core and its SMT sibling.
The counter events require an Intel hybrid P-core PMU. From this directory:

```sh
python3 -B study.py smoke --environment "$BOUNDARY_ENV" --output "$BOUNDARY_RESULTS" \
  --cpu "$BOUNDARY_CPU" --sibling "$BOUNDARY_SIBLING"

python3 -B study.py run --environment "$BOUNDARY_ENV" --output "$BOUNDARY_RESULTS" \
  --cpu "$BOUNDARY_CPU" --sibling "$BOUNDARY_SIBLING"

python3 -B followup.py --environment "$BOUNDARY_ENV" --output "$BOUNDARY_RESULTS" \
  --cpu "$BOUNDARY_CPU" --sibling "$BOUNDARY_SIBLING"

python3 -B study.py counters --environment "$BOUNDARY_ENV" --output "$BOUNDARY_RESULTS" \
  --cpu "$BOUNDARY_CPU" --sibling "$BOUNDARY_SIBLING"

python3 -B report.py --results "$BOUNDARY_RESULTS" --environment "$BOUNDARY_ENV"
```

The collector pins PHP and starts perf on the same core. It verifies binary and
background hashes. Its fingerprint includes the frozen plan, generator/collector,
harness and environment. Completed inputs are checkpointed and skipped on resume;
changed settings require a new output directory. A smoke check collects no timing
samples. An optional `study.py pilot` measures one small input; give it a separate
output directory so its samples do not enter the main series.

The adaptive rules and 64-input limit are in [METHOD.md](METHOD.md). Every
requested input is logged with its selection reason before timing. The generated
report exports exact inputs, all timing attempts, counter pairs and quality
decisions. The renderer writes local documents and data; use a separate copy when
reproducing so the published evidence is not overwritten.

`followup.py` confirms at most six flagged boundary inputs once more and uses
remaining budget for at most four grid-gap probes and their second-text checks.
The overall limit remains 64 distinct inputs. Original captures are retained;
the follow-up policy and its script hash are saved before this phase.

The recorded series used its last spare slot for Replacer with 32 keys on 4 KiB.
To replay that decision, run the following before counters, only if the point is
missing and an input slot remains. Another machine's adaptive search may choose
different points or already exhaust the budget.

```sh
python3 -B probe.py --environment "$BOUNDARY_ENV" --output "$BOUNDARY_RESULTS" \
  --cpu "$BOUNDARY_CPU" --sibling "$BOUNDARY_SIBLING" \
  --operation replace --keys 32 --bytes 4096
```
