# Code and builds

All published search and replacement values refer to one snapshot of the extension source code. For each compiler, Matcher and Replacer were measured using the same PHP CLI and extension module listed below. These are separate series of runs; quality-control rules are described in the method document. Identity is established by the attached file and the hashes of the measured modules.

| Component | Identity |
|---|---|
| Extension source code | [strmatch.c](extension/strmatch.c), SHA-256 `c4cece7e7a4f5952caae5609b9bc607408427c1fe006e47f59d7fdc0cc0946b3` |
| Implementation in PR #25122 | [7c7550bcdac](https://github.com/php/php-src/commit/7c7550bcdac2091e5f9c256e3f203f82d7db448f) |
| PHP source code | commit `758c9ac5492848a54f9fd88fac2a54d5e6108c05` |
| gcc15: PHP CLI SHA-256 | `950c71e1d7b072975c4f0d37cbf5aa719b45c14433d21a2c67c0c7581673f2c0` |
| gcc15: extension module SHA-256 | `b630e6bac6d03ffabe5499f929a7e7427b667979a39a5f25781d35d0f8a79960` |
| clang21: PHP CLI SHA-256 | `edc570aa6b5c1babbeaed1364a558cab2fb0f7088d705b6e493cc1a8a1e9bb1f` |
| clang21: extension module SHA-256 | `54b6a6e39e85a13d99d84f67fc5ac67e64489958def494f6ae9e225c257b3839` |

AMD Ryzen 9 5950X, Linux x86-64; GCC 15.2 and Clang 21.1. Release, docker profile: `-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64`; the module is built with `-Werror`. PHP CLI without OPcache/PHP JIT; PCRE JIT is enabled and supported. JIT use by each individual expression was not confirmed.

Search and replacement protocol: 100 ms warmup, 15 samples targeting 40 ms per method after calibration. Search and replacement series have separate quality-control records; their results are not combined into one ratio. [Exact method](METHOD.md).
