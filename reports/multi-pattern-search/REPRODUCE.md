# Reproduce

You need PHP build tools, Python 3.10 or newer, and about 3 GB of disk for two PHP builds.

## 1. Build PHP with the extension

Build outside this directory, once with each compiler:

```sh
git clone --filter=blob:none https://github.com/php/php-src.git php-src && cd php-src
git fetch origin bb508627af16e029c3c760109461c7596259484c && git checkout FETCH_HEAD
for cc in gcc clang; do
  git worktree add -f ../php-$cc HEAD && (cd ../php-$cc && ./buildconf --force &&
    CC=$cc CFLAGS='-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64' \
    LDFLAGS='-Wl,-O1 -pie' ./configure --disable-all --enable-cli --disable-cgi --disable-phpdbg &&
    make -j"$(nproc)")
done
```

The binaries are `../php-gcc/sapi/cli/php` and `../php-clang/sapi/cli/php`. OPcache and PCRE are built in.
The rest runs from a copy of this directory, so that your data and pages don't overwrite ours: `cp -a . ../mps-repro && cd ../mps-repro`.

## 2. Unpack the inputs

```sh
gunzip -kf corpus/*.gz
python3 tools/cells.py controlled crossover natural languages scenarios counterexamples pages
sha256sum -c data/cells.sha256
```

`data/cells.sha256` was written with `sha256sum cells/*/*.json`.

`cells.py` takes about 5 minutes. Each cell stores corpus offsets and the keys written into every window, and `bench.php` checks the corpus hash before it runs.
To rebuild the corpora and dictionaries from upstream, see the header of [tools/sources.py](tools/sources.py) and the revisions in [corpus/SOURCES.json](corpus/SOURCES.json).

## 3. Check one cell

```sh
INI='-n -d memory_limit=-1 -d opcache.enable_cli=1 -d opcache.file_update_protection=0 -d opcache.jit=disable -d pcre.jit=1'
<gcc build>/sapi/cli/php $INI tools/bench.php cells/scenarios/moderation.any.json verify
```

`verify` runs every existing method on every text of the cell and lists the ones whose results match the native call.

## 4. Run the series

[tools/full-run.sh](tools/full-run.sh) runs everything on CPU 15 and CPU 7, two cores of different CCDs of a Ryzen 9 5950X.
On another machine, pick two cores whose SMT siblings are idle (`lscpu -e`) and pass them as `CPU_A`, `SIB_A`, `CPU_B` and `SIB_B`. The page-length series and the build-time loop below use `CPU_A` and `SIB_A` too. The output directories keep the names `cpu15` and `cpu7`. On Intel hybrid CPUs use performance cores only, and fix the frequency or expect more values marked †.

```sh
bash tools/full-run.sh runs <gcc build>/sapi/cli/php <clang build>/sapi/cli/php
```

It takes about 2.5 hours on the machine above and returns at once; the series is done when `runs/cpu15/done.json` and `runs/cpu7/done.json` exist. The published data came from separate runs of the same cells: the two grids with languages in parallel, then edge cases, then scenarios on CPU 15, with a version of `bench.php` that also timed the replacement methods dropped since; see [METHOD.md](METHOD.md). `data/corecheck.json` also holds the 45 PHP-name cells of 1.5–3 KiB, which an earlier version of `full-run.sh` ran on CPU 15 as well. The compiler labels must stay `gcc15` and `clang21`, the names `render.py` expects.
Rerunning a `run.py` command with the same arguments resumes an interrupted series. Start the next commands only after both `done.json` files exist: they use the same core.

The page-length cells are not in `full-run.sh`. They ran on their own on CPU 15, in under 10 minutes:

```sh
python3 tools/run.py --out runs/pages --cpu ${CPU_A:-15} --sibling ${SIB_A:-31} \
  --php gcc15=<gcc build>/sapi/cli/php --php clang21=<clang build>/sapi/cli/php cells/pages/*.json
```

Build time and memory:

```sh
set -o pipefail
INI='-n -d memory_limit=-1 -d opcache.enable_cli=1 -d opcache.file_update_protection=0 -d opcache.jit=disable -d pcre.jit=1'
php=<gcc build>/sapi/cli/php
for p in 1 2 3; do
  $php $INI tools/construct.php | while read -r name; do
    for cc in gcc15:<gcc build> clang21:<clang build>; do
      taskset -c ${CPU_A:-15} ${cc#*:}/sapi/cli/php $INI tools/construct.php "$name" | sed "s/^{/{\"compiler\":\"${cc%%:*}\",\"process\":$p,/"
    done
  done
done > data/construct.jsonl
```

Each dictionary is built in a fresh process with only that dictionary loaded: with every dictionary in memory at once, some builds took longer. The file should have 276 lines.

## 5. Summarize and render

```sh
python3 tools/summarize.py runs/cpu15 runs/cpu7 --out data/results.json
python3 tools/summarize.py runs/corecheck --out data/corecheck.json
python3 tools/summarize.py runs/pages --out data/pages.json
python3 tools/render.py
```

`render.py` writes every `*.md` page from its `*.md.in` template. Tables and measured values come from the data files. The machine and compiler versions in the text come from `ENVIRONMENT` in `tools/render.py`: set yours there.

## Not reproducible from these tools

[data/branch-probe.md](data/branch-probe.md) and [data/calibration.md](data/calibration.md) were made with earlier scripts and an earlier version of the extension.
Their raw data is in [data/probe](data/probe).
