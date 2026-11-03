# Fixed 4 KiB inputs: match position and dictionary size

One operation processes one of four different saved English strings, exactly **4096 bytes** each. All variants cycle equally often. These are controlled authored examples, not production traces. [Saved inputs and expected results](../../corpus/multi-pattern-4k/README.md).

**Time in µs, lower is better.** `Prepared` is one call using an existing candidate object. `One-shot` directly times constructing one candidate object, processing one string and destroying the object together. PHP and PCRE times in these tables come from the same one-operation batch series; their dictionaries, regex strings and callbacks are already prepared and PCRE caches are warm. Input loading is excluded for every method. Prepared timings come from a separate series.

The protocol uses 250 ms warmup per method, 15 time samples (about one second total per method), rotating/reversed order, CPU affinity and an idle SMT sibling. Five N-minus-zero counter passes measure prepared operations. Only the Ryzen 9 5950X was measured. The one-shot timing excludes initial cold-process loading.

PHP comparators: a `str_contains()` loop for `matches()` and `strtr()` for replacement. PCRE comparators: `preg_match()` with one alternation and `preg_replace_callback()` with longest-first literal alternatives, respectively.

## Practical reading

**On both compilers**, one-shot `Matcher::matches()` (no match) and `Replacer::replace()` beat both comparators at **16, 32, 64, 128, 256, 512 keys** on these inputs.

**Eight-key replacement favors PCRE:** with GCC, `preg_replace_callback()` takes **4.958 µs**, against **10.319 µs** for a prepared Replacer and **12.807 µs** including construction and destruction.

These lists require at least a 2% paired-median advantage against each comparator. This is a noise heuristic, not statistical confidence or a universal crossover threshold. Smaller gaps remain visible in the tables. A win with a prepared object does not imply a one-shot win.

## GCC 15.2

### First-match position: Matcher::matches()

128 keys. The four positive variants match dictionary entries **1, 37, 91 and 128** (1-based), in the same order for start/middle/end. Byte offsets are 18 near the start, 2062–2067 in the middle and 4087–4090 near the end; see the saved per-variant facts. The PHP loop follows dictionary order and stops at its first matching key.

| First match: Matcher::matches() | PHP µs | PCRE µs | Prepared µs | One-shot µs |
|---|---:|---:|---:|---:|
| No match | 122.299 | 143.059 | 6.987 | 65.786 |
| Near start (byte 18) | 58.812 | 0.910 | 0.142 | 58.600 |
| Middle (about 2 KiB) | 61.071 | 72.355 | 3.577 | 62.233 |
| Near end (last 9 bytes) | 59.414 | 142.695 | 6.999 | 65.477 |

### Dictionary size: Matcher::matches(), no match

The same four clean strings are used at every dictionary size. All 512 moderation keys are absent. Dictionaries grow by appending entries from the saved policy lexicon.

| Dictionary keys | PHP µs | PCRE µs | Prepared µs | One-shot µs |
|---|---:|---:|---:|---:|
| 8 | 4.553 | 5.505 | 3.797 | 6.058 |
| 16 | 11.983 | 14.894 | 3.713 | 8.823 |
| 32 | 30.082 | 35.404 | 6.731 | 19.303 |
| 64 | 60.096 | 71.473 | 6.779 | 33.926 |
| 128 | 122.468 | 144.862 | 6.980 | 66.434 |
| 256 | 255.464 | 308.410 | 7.128 | 159.231 |
| 512 | 508.844 | 952.189 | 7.534 | 299.693 |

Prepared Matcher wins against both comparators at 8, 16, 32, 64, 128, 256, 512 keys (same 2% heuristic).

### Dictionary size: Replacer::replace(), matching terms

The same four support articles are used at every dictionary size. Keys are the first entries of the support lexicon; values are help URLs. More keys also cause more replacements and larger output. This measures that application workload, not dictionary-size overhead in isolation. [Per-variant replacement counts](../../corpus/multi-pattern-4k/CASES.md).

| Dictionary keys | PHP µs | PCRE µs | Prepared µs | One-shot µs |
|---|---:|---:|---:|---:|
| 8 | 38.703 | 4.958 | 10.319 | 12.807 |
| 16 | 68.425 | 16.226 | 10.556 | 15.548 |
| 32 | 154.142 | 33.721 | 10.910 | 20.137 |
| 64 | 291.588 | 62.292 | 11.275 | 30.190 |
| 128 | 357.375 | 98.391 | 12.023 | 58.151 |
| 256 | 389.199 | 207.114 | 12.451 | 131.305 |
| 512 | 393.089 | 634.562 | 12.618 | 308.186 |

Prepared Replacer wins against both comparators at 16, 32, 64, 128, 256, 512 keys (same 2% heuristic).

### Prepared operations: time and counters

| Case | Method | µs | CPU cycles | Instructions |
|---|---|---:|---:|---:|
| `grid.any.absent.8` | `contains_loop` | 4.513 | 21207.2 | 47297.1 |
| `grid.any.absent.8` | `preg_match` | 5.312 | 24323.3 | 116335.0 |
| `grid.any.absent.8` | `matcher` | 3.797 | 17559.4 | 63704.0 |
| `grid.any.absent.16` | `contains_loop` | 11.895 | 55898.6 | 98934.1 |
| `grid.any.absent.16` | `preg_match` | 14.857 | 68471.4 | 222184.4 |
| `grid.any.absent.16` | `matcher` | 3.713 | 17097.3 | 67205.0 |
| `grid.any.absent.32` | `contains_loop` | 29.940 | 141379.6 | 216740.8 |
| `grid.any.absent.32` | `preg_match` | 35.306 | 162934.4 | 558905.4 |
| `grid.any.absent.32` | `matcher` | 6.731 | 31460.6 | 73562.3 |
| `grid.any.absent.64` | `contains_loop` | 59.933 | 281723.3 | 412139.2 |
| `grid.any.absent.64` | `preg_match` | 71.271 | 327363.6 | 1535960.2 |
| `grid.any.absent.64` | `matcher` | 6.779 | 31635.4 | 73633.3 |
| `grid.any.absent.128` | `contains_loop` | 121.888 | 573696.8 | 803098.3 |
| `grid.any.absent.128` | `preg_match` | 145.072 | 664197.1 | 3081409.7 |
| `grid.any.absent.128` | `matcher` | 6.980 | 32550.2 | 73803.3 |
| `grid.any.absent.256` | `contains_loop` | 254.423 | 1199454.4 | 1652705.9 |
| `grid.any.absent.256` | `preg_match` | 281.298 | 1293372.7 | 6517381.7 |
| `grid.any.absent.256` | `matcher` | 7.128 | 33260.7 | 73933.0 |
| `grid.any.absent.512` | `contains_loop` | 507.294 | 2390718.2 | 3296949.6 |
| `grid.any.absent.512` | `preg_match` | 920.698 | 4672682.9 | 13349518.8 |
| `grid.any.absent.512` | `matcher` | 7.534 | 35158.1 | 74716.9 |
| `grid.replace.mixed.8` | `strtr` | 38.659 | 178631.7 | 701750.0 |
| `grid.replace.mixed.8` | `preg_replace_callback` | 4.935 | 23018.5 | 57699.3 |
| `grid.replace.mixed.8` | `replacer` | 10.319 | 47540.6 | 132419.9 |
| `grid.replace.mixed.16` | `strtr` | 68.552 | 318749.0 | 1060319.3 |
| `grid.replace.mixed.16` | `preg_replace_callback` | 16.182 | 74012.9 | 261505.5 |
| `grid.replace.mixed.16` | `replacer` | 10.556 | 48755.5 | 134706.1 |
| `grid.replace.mixed.32` | `strtr` | 154.193 | 718461.1 | 1906803.2 |
| `grid.replace.mixed.32` | `preg_replace_callback` | 33.560 | 154213.5 | 537767.8 |
| `grid.replace.mixed.32` | `replacer` | 10.910 | 50297.3 | 136799.2 |
| `grid.replace.mixed.64` | `strtr` | 291.305 | 1344340.3 | 3486890.8 |
| `grid.replace.mixed.64` | `preg_replace_callback` | 62.494 | 285514.1 | 1182228.6 |
| `grid.replace.mixed.64` | `replacer` | 11.275 | 52572.4 | 141300.8 |
| `grid.replace.mixed.128` | `strtr` | 356.895 | 1647858.5 | 4256044.2 |
| `grid.replace.mixed.128` | `preg_replace_callback` | 98.828 | 452695.9 | 2094340.7 |
| `grid.replace.mixed.128` | `replacer` | 12.023 | 55260.8 | 144579.5 |
| `grid.replace.mixed.256` | `strtr` | 389.297 | 1795598.9 | 4609652.5 |
| `grid.replace.mixed.256` | `preg_replace_callback` | 208.054 | 952440.6 | 4055697.6 |
| `grid.replace.mixed.256` | `replacer` | 12.451 | 57312.4 | 146949.1 |
| `grid.replace.mixed.512` | `strtr` | 392.678 | 1805281.9 | 4641077.5 |
| `grid.replace.mixed.512` | `preg_replace_callback` | 608.964 | 2957541.3 | 7890928.5 |
| `grid.replace.mixed.512` | `replacer` | 12.618 | 58541.1 | 150079.7 |
| `grid.any.absent.position` | `contains_loop` | 121.967 | 574041.5 | 802859.0 |
| `grid.any.absent.position` | `preg_match` | 142.834 | 655923.3 | 3081410.2 |
| `grid.any.absent.position` | `matcher` | 6.987 | 32596.1 | 73803.4 |
| `grid.any.start.position` | `contains_loop` | 58.729 | 275182.7 | 403997.2 |
| `grid.any.start.position` | `preg_match` | 0.900 | 4131.2 | 17108.5 |
| `grid.any.start.position` | `matcher` | 0.142 | 630.9 | 1853.2 |
| `grid.any.middle.position` | `contains_loop` | 58.813 | 277389.8 | 405649.2 |
| `grid.any.middle.position` | `preg_match` | 72.141 | 331595.9 | 1559647.7 |
| `grid.any.middle.position` | `matcher` | 3.577 | 16694.1 | 37995.8 |
| `grid.any.end.position` | `contains_loop` | 59.128 | 278001.1 | 407838.1 |
| `grid.any.end.position` | `preg_match` | 143.066 | 654224.8 | 3075596.6 |
| `grid.any.end.position` | `matcher` | 6.999 | 32650.8 | 73759.8 |

### A/A controls

| Stage | Scope | Case | Time Δ |
|---|---|---|---:|
| before | Prepared | `grid.any.absent.8` | -0.034% |
| before | Prepared | `grid.any.absent.8` | -0.054% |
| after | Prepared | `grid.any.absent.8` | +0.002% |
| after | Prepared | `grid.any.absent.8` | +0.115% |
| before | One-shot | `grid.any.absent.128` | +0.074% |
| before | One-shot | `grid.replace.mixed.128` | +0.073% |
| after | One-shot | `grid.any.absent.128` | -0.024% |
| after | One-shot | `grid.replace.mixed.128` | +0.014% |

[Prepared samples and counters](data/grid-gcc15.json) · [One-shot samples](data/grid-oneshot-gcc15.json).

## Clang 21.1

### First-match position: Matcher::matches()

128 keys. The four positive variants match dictionary entries **1, 37, 91 and 128** (1-based), in the same order for start/middle/end. Byte offsets are 18 near the start, 2062–2067 in the middle and 4087–4090 near the end; see the saved per-variant facts. The PHP loop follows dictionary order and stops at its first matching key.

| First match: Matcher::matches() | PHP µs | PCRE µs | Prepared µs | One-shot µs |
|---|---:|---:|---:|---:|
| No match | 117.727 | 136.545 | 8.013 | 64.566 |
| Near start (byte 18) | 56.508 | 0.835 | 0.134 | 57.277 |
| Middle (about 2 KiB) | 56.876 | 68.991 | 4.073 | 60.657 |
| Near end (last 9 bytes) | 57.177 | 136.311 | 8.030 | 64.419 |

### Dictionary size: Matcher::matches(), no match

The same four clean strings are used at every dictionary size. All 512 moderation keys are absent. Dictionaries grow by appending entries from the saved policy lexicon.

| Dictionary keys | PHP µs | PCRE µs | Prepared µs | One-shot µs |
|---|---:|---:|---:|---:|
| 8 | 4.624 | 5.550 | 3.614 | 5.888 |
| 16 | 11.582 | 15.171 | 3.845 | 8.815 |
| 32 | 28.800 | 35.012 | 7.793 | 19.796 |
| 64 | 57.558 | 69.648 | 7.814 | 33.641 |
| 128 | 117.866 | 143.756 | 8.005 | 64.657 |
| 256 | 245.572 | 287.860 | 8.175 | 159.038 |
| 512 | 489.278 | 1053.781 | 8.506 | 300.060 |

Prepared Matcher wins against both comparators at 8, 16, 32, 64, 128, 256, 512 keys (same 2% heuristic).

### Dictionary size: Replacer::replace(), matching terms

The same four support articles are used at every dictionary size. Keys are the first entries of the support lexicon; values are help URLs. More keys also cause more replacements and larger output. This measures that application workload, not dictionary-size overhead in isolation. [Per-variant replacement counts](../../corpus/multi-pattern-4k/CASES.md).

| Dictionary keys | PHP µs | PCRE µs | Prepared µs | One-shot µs |
|---|---:|---:|---:|---:|
| 8 | 37.238 | 5.024 | 9.465 | 12.010 |
| 16 | 67.378 | 16.389 | 10.235 | 15.129 |
| 32 | 153.176 | 34.177 | 10.773 | 19.691 |
| 64 | 293.063 | 62.083 | 11.605 | 29.784 |
| 128 | 361.655 | 108.406 | 12.370 | 58.321 |
| 256 | 394.381 | 203.678 | 12.650 | 129.212 |
| 512 | 397.304 | 644.804 | 12.642 | 304.510 |

Prepared Replacer wins against both comparators at 16, 32, 64, 128, 256, 512 keys (same 2% heuristic).

### Prepared operations: time and counters

| Case | Method | µs | CPU cycles | Instructions |
|---|---|---:|---:|---:|
| `grid.any.absent.8` | `contains_loop` | 4.563 | 21267.7 | 47014.3 |
| `grid.any.absent.8` | `preg_match` | 5.333 | 24401.4 | 116341.1 |
| `grid.any.absent.8` | `matcher` | 3.614 | 16595.9 | 72174.0 |
| `grid.any.absent.16` | `contains_loop` | 11.519 | 54090.8 | 95356.8 |
| `grid.any.absent.16` | `preg_match` | 15.140 | 69827.1 | 222190.3 |
| `grid.any.absent.16` | `matcher` | 3.845 | 17658.5 | 76842.0 |
| `grid.any.absent.32` | `contains_loop` | 28.707 | 135216.0 | 205113.6 |
| `grid.any.absent.32` | `preg_match` | 34.924 | 160980.5 | 558911.8 |
| `grid.any.absent.32` | `matcher` | 7.793 | 36304.5 | 85312.4 |
| `grid.any.absent.64` | `contains_loop` | 57.379 | 269490.3 | 389262.8 |
| `grid.any.absent.64` | `preg_match` | 69.601 | 319065.1 | 1535965.1 |
| `grid.any.absent.64` | `matcher` | 7.814 | 36434.0 | 85402.6 |
| `grid.any.absent.128` | `contains_loop` | 117.493 | 552056.6 | 758797.4 |
| `grid.any.absent.128` | `preg_match` | 144.182 | 658811.2 | 3081416.3 |
| `grid.any.absent.128` | `matcher` | 8.005 | 37357.4 | 85615.5 |
| `grid.any.absent.256` | `contains_loop` | 245.170 | 1154649.6 | 1559422.5 |
| `grid.any.absent.256` | `preg_match` | 286.079 | 1314297.5 | 6517394.9 |
| `grid.any.absent.256` | `matcher` | 8.175 | 38099.2 | 85763.7 |
| `grid.any.absent.512` | `contains_loop` | 488.818 | 2300925.5 | 3111362.3 |
| `grid.any.absent.512` | `preg_match` | 1025.131 | 4776830.5 | 13349536.9 |
| `grid.any.absent.512` | `matcher` | 8.506 | 39795.7 | 86716.8 |
| `grid.replace.mixed.8` | `strtr` | 37.295 | 167285.5 | 709881.5 |
| `grid.replace.mixed.8` | `preg_replace_callback` | 5.002 | 23098.2 | 56996.5 |
| `grid.replace.mixed.8` | `replacer` | 9.465 | 43789.5 | 144069.9 |
| `grid.replace.mixed.16` | `strtr` | 67.432 | 313007.0 | 1079106.6 |
| `grid.replace.mixed.16` | `preg_replace_callback` | 16.279 | 74507.0 | 260374.1 |
| `grid.replace.mixed.16` | `replacer` | 10.235 | 47207.3 | 146422.4 |
| `grid.replace.mixed.32` | `strtr` | 153.026 | 707786.8 | 1960960.6 |
| `grid.replace.mixed.32` | `preg_replace_callback` | 34.230 | 156327.4 | 535933.1 |
| `grid.replace.mixed.32` | `replacer` | 10.773 | 49414.7 | 148345.9 |
| `grid.replace.mixed.64` | `strtr` | 292.774 | 1346326.0 | 3586929.0 |
| `grid.replace.mixed.64` | `preg_replace_callback` | 62.108 | 283885.3 | 1179372.1 |
| `grid.replace.mixed.64` | `replacer` | 11.605 | 52980.4 | 152526.9 |
| `grid.replace.mixed.128` | `strtr` | 361.338 | 1664105.5 | 4358800.8 |
| `grid.replace.mixed.128` | `preg_replace_callback` | 107.924 | 495143.8 | 2090269.8 |
| `grid.replace.mixed.128` | `replacer` | 12.370 | 55870.0 | 155545.3 |
| `grid.replace.mixed.256` | `strtr` | 395.778 | 1818912.2 | 4717711.4 |
| `grid.replace.mixed.256` | `preg_replace_callback` | 202.712 | 937512.8 | 4051608.3 |
| `grid.replace.mixed.256` | `replacer` | 12.650 | 58122.7 | 157935.2 |
| `grid.replace.mixed.512` | `strtr` | 397.122 | 1831150.4 | 4749995.9 |
| `grid.replace.mixed.512` | `preg_replace_callback` | 597.225 | 2806800.0 | 7886797.9 |
| `grid.replace.mixed.512` | `replacer` | 12.642 | 58398.5 | 161211.1 |
| `grid.any.absent.position` | `contains_loop` | 117.460 | 552099.3 | 758556.6 |
| `grid.any.absent.position` | `preg_match` | 136.529 | 625683.8 | 3081415.2 |
| `grid.any.absent.position` | `matcher` | 8.013 | 37387.6 | 85615.6 |
| `grid.any.start.position` | `contains_loop` | 56.305 | 264298.3 | 381144.5 |
| `grid.any.start.position` | `preg_match` | 0.849 | 3848.1 | 17116.5 |
| `grid.any.start.position` | `matcher` | 0.134 | 610.4 | 1927.5 |
| `grid.any.middle.position` | `contains_loop` | 56.550 | 265525.0 | 382767.0 |
| `grid.any.middle.position` | `preg_match` | 68.948 | 316127.3 | 1559654.4 |
| `grid.any.middle.position` | `matcher` | 4.073 | 18997.3 | 43965.8 |
| `grid.any.end.position` | `contains_loop` | 56.752 | 266472.7 | 384923.0 |
| `grid.any.end.position` | `preg_match` | 136.209 | 624516.7 | 3075608.1 |
| `grid.any.end.position` | `matcher` | 8.030 | 37388.9 | 85565.3 |

### A/A controls

| Stage | Scope | Case | Time Δ |
|---|---|---|---:|
| before | Prepared | `grid.any.absent.8` | +0.121% |
| before | Prepared | `grid.any.absent.8` | -0.020% |
| after | Prepared | `grid.any.absent.8` | +0.002% |
| after | Prepared | `grid.any.absent.8` | -0.071% |
| before | One-shot | `grid.any.absent.128` | +0.048% |
| before | One-shot | `grid.replace.mixed.128` | -0.022% |
| after | One-shot | `grid.any.absent.128` | -0.014% |
| after | One-shot | `grid.replace.mixed.128` | -0.132% |

[Prepared samples and counters](data/grid-clang21.json) · [One-shot samples](data/grid-oneshot-clang21.json).

[Import audit](data/grid-capture-audit.json) · [Reproduce](REPRODUCE.md#fixed-4-kib-matrix).
