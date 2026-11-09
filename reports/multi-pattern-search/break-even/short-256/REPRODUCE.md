# Repeat the 256-byte slice

Use the release GCC 14 CLI and matching module described in the
[parent reproduction instructions](../REPRODUCE.md). Keep the parent report
directory: this slice references its saved backgrounds and formatting helpers.

Set `SHORT_ENV` to the environment JSON, `SHORT_RESULTS` to a new results
directory, and `SHORT_CPU` / `SHORT_SIBLING` to the measured P-core and its SMT
sibling. From this directory:

```sh
python3 -B run256.py smoke --environment "$SHORT_ENV" --output "$SHORT_RESULTS" \
  --cpu "$SHORT_CPU" --sibling "$SHORT_SIBLING"

python3 -B run256.py run --environment "$SHORT_ENV" --output "$SHORT_RESULTS" \
  --cpu "$SHORT_CPU" --sibling "$SHORT_SIBLING"

python3 -B run256.py counters --environment "$SHORT_ENV" --output "$SHORT_RESULTS" \
  --cpu "$SHORT_CPU" --sibling "$SHORT_SIBLING"

python3 -B render.py --results "$SHORT_RESULTS" --environment "$SHORT_ENV"
```

The frozen schedule measures at most 33 short inputs and one 4 KiB counting
control. Every selected input passes exact-output checks before timing. A wrong
expected output must be rejected. The additional counting recipe also has saved
[self-overlap and mutation checks](data/count-baseline-checks.json).

Input, harness, collector, schedule and binary identities are checked. Completed
inputs are skipped on resume; changed settings require a new results directory.
Use a separate checkout or copy to avoid overwriting the published captures and
generated documents. Counter events target an Intel hybrid P-core PMU.
