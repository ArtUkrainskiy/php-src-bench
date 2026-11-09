# Reproduce the prepared-only grid

Use the release GCC 14 CLI, module and environment JSON described in the
[boundary reproduction instructions](../REPRODUCE.md). Keep the report tree:
this cohort references the parent's saved backgrounds and formatting helpers.

Set `GRID_ENV`, `GRID_RESULTS`, `GRID_CPU` and `GRID_SIBLING`. Choose a new results
directory and a P-core with its SMT sibling. From this directory:

```sh
python3 -B run_grid.py smoke --environment "$GRID_ENV" --output "$GRID_RESULTS" \
  --cpu "$GRID_CPU" --sibling "$GRID_SIBLING"

python3 -B run_grid.py run --environment "$GRID_ENV" --output "$GRID_RESULTS" \
  --cpu "$GRID_CPU" --sibling "$GRID_SIBLING"

python3 -B run_grid.py counters --environment "$GRID_ENV" --output "$GRID_RESULTS" \
  --cpu "$GRID_CPU" --sibling "$GRID_SIBLING"

python3 -B render.py --results "$GRID_RESULTS" --environment "$GRID_ENV"
```

The source/binary hashes, frozen schedule and complete input grid are checked.
Every selected input passes exact-output checks before timing. Completed inputs
are checkpointed for resume. A separate `pilot` phase times only 128 B / 8 keys
for presence; use another output directory to exclude pilot samples.

The timed objects and A/A objects are already prepared. There are no one-shot
calls in this cohort. Counter events require the Intel hybrid P-core PMU.
Use a separate checkout or copy to avoid overwriting the published evidence.
