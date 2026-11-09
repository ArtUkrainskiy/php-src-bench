# Reproducing the application workloads

The saved corpus needs no downloads. Use a separate checkout or copy and a new
results directory: the scripts write checkpoints and generated tables. A different
machine or binary produces a new series, not additional samples of the laptop run.

## Build and environment

Use a non-debug, NTS PHP CLI with the strmatch module. The measured build uses
the `docker` profile's `-O2` flags. PHP commit, configure options, flags and hashes
are in [data/build.json](data/build.json).
The extension source is [saved with the main report](../benchmark/extension/strmatch.c).
Compile the module with GCC 14 and configured headers from the same PHP commit
as the CLI:

```sh
gcc-14 -shared -fstack-protector-strong -fpic -fpie -O2 -g \
  -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -fPIC -Werror -D_GNU_SOURCE \
  -DCOMPILE_DL_STRMATCH=1 -DZEND_ENABLE_STATIC_TSRMLS_CACHE=1 \
  -I"$APP_PHP_HEADERS" -I"$APP_PHP_HEADERS/main" \
  -I"$APP_PHP_HEADERS/TSRM" -I"$APP_PHP_HEADERS/Zend" \
  ../benchmark/extension/strmatch.c -o "$APP_STRMATCH_MODULE"
```

Set `APP_PHP_HEADERS` to the configured source/header directory and
`APP_STRMATCH_MODULE` to the output module path. Finish building before collecting
performance data.

Create a local environment JSON with your binary/module paths and hashes:

```python
import hashlib, json
from pathlib import Path

build = json.loads(Path('data/build.json').read_text())
build['php'] = '/absolute/path/to/release/php'
build['module'] = '/absolute/path/to/strmatch.so'
for key in ['php', 'module']:
    build[key + '_sha256'] = hashlib.sha256(Path(build[key]).read_bytes()).hexdigest()
# Replace build/runtime metadata too if your CLI, compiler or source differs.
environment = {'platform': 'Linux x86-64', 'compilers': {'gcc14': build}}
Path('environment.local.json').write_text(json.dumps(environment, indent=2) + '\n')
```

Select an otherwise idle physical core and identify its SMT sibling from
`/sys/devices/system/cpu/cpu*/topology/thread_siblings_list`. Set `APP_CPU` and
`APP_SIBLING` accordingly. The recorded laptop affinity is in `data/build.json`;
use the topology of your own machine when selecting affinity.

## Checks, timing and counters

Run from this directory, with `APP_RESULTS` set to a new writable directory:

```sh
python3 run.py check --environment environment.local.json \
  --output "$APP_RESULTS" --compilers gcc14 --cpu "$APP_CPU" --sibling "$APP_SIBLING"

python3 run.py time --environment environment.local.json \
  --output "$APP_RESULTS" --compilers gcc14 --cpu "$APP_CPU" --sibling "$APP_SIBLING" \
  --passes 15 --sample-ms 40 --warmup-ms 100 --attempts 2

taskset -c "$APP_CPU" python3 run.py counters --environment environment.local.json \
  --output "$APP_RESULTS" --compilers gcc14 --cpu "$APP_CPU" --sibling "$APP_SIBLING" \
  --passes 15 --sample-ms 40 --warmup-ms 100 --attempts 2

python3 analyze.py --environment environment.local.json --results "$APP_RESULTS"
```

Pinning the parent starts perf on the same core as PHP. This collector uses Intel hybrid
`cpu_core/cycles/u` and `cpu_core/instructions/u` events. Check availability with
`perf list`; a different PMU requires an explicitly separate collector/series,
with matching event names. Perf permissions must allow user-mode counters.

Every phase verifies binary and subject hashes. Completed points are skipped on
resume. The fingerprint covers corpus, harness, collector, environment and sampling
settings; changes require a new results directory. The analyzer verifies this
identity, measures native memory in fresh processes, and generates tables,
documents and public captures. `--timing-only` renders timing evidence without
waiting for counters.

The saved preflight summary covers four compilers and 4,384 comparisons.
A GCC-14-only check produces 1,096 comparisons.

## Corpus reconstruction and audit

[corpus.json](corpus.json) is authoritative. Each JSON under `inputs/cases/`
contains exact subject contents, the ordered dictionary, expected outputs and
eligible methods. Batch JSONs include every member. All 256 acquired comments
are retained, including subjects outside the measured panel.

`prepare.py` implements acquisition, deterministic selection and independent
expected-output generation. Its `--source-cache` JSON maps source identities to
`content`, `revision` and `url`; the identities are listed in `corpus.json`.
`--download-cache` holds the eight original dataset-server responses named
`civil-<offset>.json`. Later dataset responses may differ. Use the saved subjects
and hashes to repeat measurements or audit the oracle without reacquisition.

All eligible recipes are implemented in [harness.php](harness.php), and their
independent oracle is in [prepare.py](prepare.py). Regex preparation and cache
warmup precede timing; result normalization runs only in check mode.
`memory.php` collects native allocation measurements separately from timing
and hardware counters.
