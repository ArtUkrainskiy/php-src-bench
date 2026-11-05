# Reproduction

Requires Linux x86-64, Python 3, a release PHP build, perf, GCC 15 or Clang 21. Exact versions, the PHP commit and published binary hashes are in [SOURCE.md](SOURCE.md); configure/CFLAGS/LDFLAGS are in [build-flags.json](data/build-flags.json). The module is built as a shared extension from the attached extension/strmatch.c using the same PHP headers and flags. Binary hashes may differ on another machine; record the hashes of the binaries actually used.

First build PHP from the specified commit. GCC example, starting in the benchmark directory:

```sh
mkdir -p .build
git clone https://github.com/php/php-src.git .build/php-gcc
git -C .build/php-gcc checkout 758c9ac5492848a54f9fd88fac2a54d5e6108c05
cd .build/php-gcc
./buildconf --force
CC=gcc-15 CFLAGS="-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64" LDFLAGS="-Wl,-O1 -pie" ./configure --disable-all --disable-cgi --disable-phpdbg --enable-cli --enable-werror
make -j2
cd ../..
python3 build-module.py --php-build .build/php-gcc --compiler gcc-15 --label gcc15 --output .build/gcc15-strmatch.so --cpu 15 --smt-sibling 31
```

Choose a free core and the correct SMT sibling for your machine. Repeat the build in a separate tree for Clang 21 (`CC=clang-21`, label `clang21`). Build-module uses the measured flags, checks the source SHA-256 and module loading, then writes the actual hashes to environment.json. The PHP build takes minutes and depends on the machine; expect make to finish without errors and `Module smoke PASS`.

After both builds, from the benchmark directory:

```sh
python3 run.py smoke
python3 run.py check
python3 run.py time
python3 memory.py
python3 run.py counters
```

Smoke collects two short samples on both compilers, taking a few seconds; detection of a corrupted reference is also checked. Check covers 601 Matcher inputs. For Replacer, run PHP with the module and verify-replacer.php: 71 inputs. Expect PASS; a mismatch stops the phase.

Time covers 64 Matcher inputs, the single-key Replacer control and the selected reuse jobs, with 15 samples each. Completed comparisons are skipped. Captures, separate attempts, A/A and status.json are saved. Total duration depends on the machine; on the report machine, the main repeat takes tens of minutes, not seconds. Counters collects five N/0 pairs per method. An elapsed-time flag is not hidden by stable instruction counts.

The Replacer matrix of 71 inputs and its measured arrays are in data/elapsed.json.gz; all recipes are described in METHOD.md, and the actual inputs are in replacer-inputs/. To rerun each replacement input, use the same harness.php and its exact saved configuration from data/captures.json.gz. Resolve the configuration’s case_path relative to the benchmark directory and preserve its methods mapping, scope and timing parameters. Warmup, sample count and sample_ns are specified in the method document. Fresh results on another CPU form a separate series.

Cleanup: generated captures/ and memory/ may be removed after saving the results. Source files, inputs/, replacer-inputs/ and published data/ are needed for reproduction.
