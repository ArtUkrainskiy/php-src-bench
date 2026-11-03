# Memory: preparation, retained objects and queries

All tables use **KiB (1024 bytes)** unless stated otherwise. These are Zend live-allocation counters, not process RSS.

Five fresh processes per class, size, family and compiler: 440 processes. All recorded allocation values match across repeats and GCC 15 / Clang 21. A shared table therefore loses no observed compiler difference.

## Reading the columns

- **Input:** the caller's PHP list or map and its strings, after parsing temporaries are released.
- **+Matcher / +Replacer:** additional live allocation after construction while Input remains alive. Strings are shared by reference.
- **Peak +:** the constructor peak above that same input baseline, after resetting the peak counter. This includes the retained object; do not add the two columns.
- **Standalone:** the object and strings it retains after the input array is released, relative to the baseline before loading the dictionary.

Startup, input-parsing peaks, reserved allocator pages and physical peaks inside realloc are outside these counters. All native automaton buffers use Zend allocation functions and are included.

## Growth and structure

The automaton combines dense transition rows with packed sparse states. It keeps dense rows for shallow states, states with at least eight children, and selected states near their failure target. Other states retain actual trie edges and a failure link. A single-child transition is stored inside its sparse record; it does not need a separate edge allocation.

For a nonempty dictionary, let N be its string count, T its total key bytes, A its distinct key-byte count, S its state count, D its dense-state count and E its separately packed sparse-edge count. On these 64-bit builds the requested runtime arrays occupy:

- **Matcher:** `4D(A+1) + 12(S-D) + 8E + 12S + 8N` bytes.
- **Replacer:** `4D(A+1) + 12(S-D) + 8E + 4S + 16N` bytes.

These budgets exclude the fixed object and byte-map fields, allocator rounding and retained string bodies. They explain the measured object additions; the measured tables remain authoritative. The final state arrays are sized to S. Temporary build arrays can grow geometrically, but their spare capacity is not retained in the immutable runtime automaton.

**String count alone does not determine memory.** Prefix sharing changes Matcher states; suffix sharing matters for reversed Replacer states. Alphabet size and the dense/sparse mix change the cost of each state. Dense-selection thresholds can create steps even without spare runtime capacity. Since `D ≤ S`, `E ≤ S-1`, `S ≤ 1+T` and the byte alphabet is bounded, automaton storage has a linear upper bound in total key bytes. This does not establish smooth or proportional growth in N.

Construction also needs trie records, edges, failure-link workspace and runtime packing. Its measured peak is separate from retained storage. It should not be inferred by adding table columns.

![Memory growth and allocation per dictionary string](memory/growth.svg)

Lines join measured sizes only. The first 512 entries preserve the support glossary; larger dictionaries add authored combinations of product names. They are constructed inputs, not a production vocabulary or a speed experiment at 10,000 strings.

## Saved input families

[Glossary and catalog](memory/glossary-catalog.json) uses the existing glossary, then saved catalog labels. [Permuted control](memory/permuted-control.json) rearranges bytes within each key, preserving lengths, byte multisets, alphabet and replacement values. It is a synthetic topology control, not another product case or a proven worst case. Dictionaries are nested prefixes of the same saved list. Every replacement value is a distinct 37-byte help URL.

## Glossary and constructed catalog

| Strings | Matcher input | +Matcher | Peak +Matcher | Replacer input | +Replacer | Peak +Replacer |
|---|---:|---:|---:|---:|---:|---:|
| 8 | 0.6 | 3.5 | 5.1 | 1.3 | 3.5 | 7.4 |
| 16 | 1.1 | 5.7 | 8.9 | 2.4 | 6.2 | 12.0 |
| 32 | 2.0 | 10.6 | 19.1 | 4.6 | 13.6 | 25.1 |
| 64 | 3.9 | 29.4 | 41.4 | 9.1 | 24.4 | 45.4 |
| 128 | 7.6 | 46.1 | 86.1 | 21.1 | 43.2 | 91.2 |
| 256 | 18.5 | 83.8 | 151.8 | 38.5 | 70.2 | 154.2 |
| 512 | 33.0 | 187.8 | 307.8 | 73.0 | 140.8 | 296.8 |
| 1000 | 67.6 | 400.8 | 712.8 | 150.1 | 232.8 | 592.8 |
| 2000 | 138.1 | 728.8 | 1352.8 | 307.1 | 368.8 | 884.8 |
| 5000 | 397.4 | 1396.8 | 2624.8 | 897.9 | 760.8 | 2384.8 |
| 10000 | 797.7 | 2272.8 | 4688.8 | 1802.7 | 1324.8 | 3264.8 |

| Strings | Matcher standalone | Replacer standalone | Matcher bytes/string | Replacer bytes/string |
|---|---:|---:|---:|---:|
| 8 | 3.9 | 4.4 | 444.0 | 442.0 |
| 16 | 6.4 | 7.9 | 364.0 | 395.0 |
| 32 | 11.9 | 16.9 | 339.0 | 435.0 |
| 64 | 32.0 | 31.0 | 470.5 | 391.0 |
| 128 | 51.2 | 56.3 | 369.0 | 346.0 |
| 256 | 94.1 | 96.6 | 335.0 | 281.0 |
| 512 | 208.7 | 193.7 | 375.5 | 281.5 |
| 1000 | 448.2 | 342.8 | 410.4 | 238.3 |
| 2000 | 830.8 | 595.8 | 373.1 | 188.8 |
| 5000 | 1662.1 | 1338.6 | 286.1 | 155.8 |
| 10000 | 2810.4 | 2487.4 | 232.7 | 135.7 |

Bytes/string uses the object addition, excluding Input.

| Strings | Key bytes | Mean key bytes | Alphabet bytes | Matcher states | Matcher dense | Replacer states | Replacer dense |
|---|---:|---:|---:|---:|---:|---:|---:|
| 8 | 91 | 11.4 | 21 | 64 | 13 | 80 | 17 |
| 16 | 179 | 11.2 | 23 | 118 | 21 | 148 | 32 |
| 32 | 358 | 11.2 | 23 | 228 | 38 | 288 | 55 |
| 64 | 716 | 11.2 | 26 | 477 | 77 | 568 | 92 |
| 128 | 1523 | 11.9 | 28 | 1055 | 137 | 1132 | 153 |
| 256 | 3365 | 13.1 | 29 | 2232 | 215 | 2220 | 211 |
| 512 | 6898 | 13.5 | 44 | 4509 | 417 | 4214 | 334 |
| 1000 | 20078 | 20.1 | 44 | 12823 | 470 | 9203 | 345 |
| 2000 | 47229 | 23.6 | 44 | 25964 | 495 | 16350 | 354 |
| 5000 | 128474 | 25.7 | 44 | 51943 | 495 | 34586 | 548 |
| 10000 | 264053 | 26.4 | 44 | 85439 | 495 | 61722 | 573 |

State/layout facts are calculated from the saved byte strings and the final implementation by [layout.py](memory/layout.py). They are explanatory counts, not public runtime API counters. The array budget below excludes fixed fields and allocator rounding.

| Strings | Class | Dense rows KiB | Sparse KiB | Edges KiB | Outputs KiB | Pointers KiB | Arrays KiB |
|---|---|---:|---:|---:|---:|---:|---:|
| 8 | Matcher | 1.1 | 0.6 | 0.0 | 0.8 | 0.1 | 2.6 |
| 8 | Replacer | 1.5 | 0.7 | 0.0 | 0.3 | 0.1 | 2.7 |
| 128 | Matcher | 15.5 | 10.8 | 0.4 | 12.4 | 1.0 | 40.0 |
| 128 | Replacer | 17.3 | 11.5 | 0.4 | 4.4 | 2.0 | 35.7 |
| 512 | Matcher | 73.3 | 48.0 | 2.6 | 52.8 | 4.0 | 180.7 |
| 512 | Replacer | 58.7 | 45.5 | 3.4 | 16.5 | 8.0 | 132.1 |
| 2000 | Matcher | 87.0 | 298.5 | 15.3 | 304.3 | 15.6 | 720.7 |
| 2000 | Replacer | 62.2 | 187.5 | 19.3 | 63.9 | 31.2 | 364.1 |
| 10000 | Matcher | 87.0 | 995.4 | 100.2 | 1001.2 | 78.1 | 2262.0 |
| 10000 | Replacer | 100.7 | 716.6 | 92.6 | 241.1 | 156.2 | 1307.3 |

### Query peaks

Additional allocations above an already prepared object, subject and expected-result data. Each operation resets the peak; correctness checks occur after the snapshot. Result storage is included.

| Strings | matches() | countMatches() | getMatchedKeywords() | matchAll() | replace() |
|---|---:|---:|---:|---:|---:|
| 8 | 0.0 | 0.0 | 0.6 | 819.0 | 400.0 |
| 16 | 0.0 | 0.0 | 0.6 | 819.0 | 400.0 |
| 32 | 0.0 | 0.0 | 0.6 | 819.0 | 400.0 |
| 64 | 0.0 | 0.0 | 0.6 | 819.0 | 400.0 |
| 128 | 0.0 | 0.0 | 0.6 | 819.0 | 400.0 |
| 256 | 0.0 | 0.0 | 0.7 | 819.0 | 400.0 |
| 512 | 0.0 | 0.0 | 0.9 | 855.6 | 408.0 |
| 1000 | 0.0 | 0.0 | 1.4 | 855.6 | 408.0 |
| 2000 | 0.0 | 0.0 | 2.4 | 855.6 | 408.0 |
| 5000 | 0.0 | 0.0 | 8.4 | 855.6 | 408.0 |
| 10000 | 0.0 | 0.0 | 12.4 | 855.6 | 408.0 |

| Strings | Distinct keys matched | All overlapping hits | Replacements | Output KiB |
|---|---:|---:|---:|---:|
| 8 | 8 | 4682 | 3122 | 142.1 |
| 16 | 8 | 4682 | 3122 | 142.1 |
| 32 | 8 | 4682 | 3122 | 142.1 |
| 64 | 8 | 4682 | 3122 | 142.1 |
| 128 | 8 | 4682 | 3122 | 142.1 |
| 256 | 8 | 4682 | 3122 | 142.1 |
| 512 | 9 | 5072 | 3512 | 151.7 |
| 1000 | 9 | 5072 | 3512 | 151.7 |
| 2000 | 9 | 5072 | 3512 | 151.7 |
| 5000 | 9 | 5072 | 3512 | 151.7 |
| 10000 | 9 | 5072 | 3512 | 151.7 |

## Permuted-byte control

| Strings | Matcher input | +Matcher | Peak +Matcher | Replacer input | +Replacer | Peak +Replacer |
|---|---:|---:|---:|---:|---:|---:|
| 8 | 0.6 | 4.9 | 7.8 | 1.3 | 4.1 | 7.9 |
| 16 | 1.1 | 13.1 | 21.6 | 2.4 | 7.5 | 17.8 |
| 32 | 2.0 | 21.0 | 33.0 | 4.6 | 14.8 | 29.8 |
| 64 | 3.9 | 33.2 | 50.2 | 9.1 | 28.8 | 50.8 |
| 128 | 7.6 | 69.8 | 113.8 | 21.1 | 58.8 | 114.8 |
| 256 | 18.5 | 126.8 | 202.8 | 38.5 | 104.8 | 204.8 |
| 512 | 33.0 | 288.8 | 456.8 | 73.0 | 236.8 | 436.8 |
| 1000 | 67.6 | 664.8 | 1160.8 | 150.1 | 528.8 | 1168.8 |
| 2000 | 138.1 | 1429.2 | 2481.2 | 307.1 | 1101.1 | 2489.1 |
| 5000 | 397.4 | 3676.8 | 6488.8 | 897.9 | 2799.8 | 6531.8 |
| 10000 | 797.7 | 7608.8 | 13352.8 | 1802.7 | 5812.8 | 13420.8 |

| Strings | Matcher standalone | Replacer standalone | Matcher bytes/string | Replacer bytes/string |
|---|---:|---:|---:|---:|
| 8 | 5.4 | 5.1 | 632.0 | 528.0 |
| 16 | 13.9 | 9.2 | 840.0 | 480.0 |
| 32 | 22.3 | 18.1 | 672.0 | 472.0 |
| 64 | 35.8 | 35.3 | 532.0 | 460.0 |
| 128 | 74.8 | 71.8 | 558.0 | 470.0 |
| 256 | 137.2 | 131.1 | 507.1 | 419.0 |
| 512 | 309.7 | 289.7 | 577.5 | 473.5 |
| 1000 | 712.3 | 638.8 | 680.8 | 541.5 |
| 2000 | 1531.3 | 1328.2 | 731.8 | 563.8 |
| 5000 | 3942.1 | 3377.6 | 753.0 | 573.4 |
| 10000 | 8146.5 | 6975.4 | 779.1 | 595.2 |

Bytes/string uses the object addition, excluding Input.

| Strings | Key bytes | Mean key bytes | Alphabet bytes | Matcher states | Matcher dense | Replacer states | Replacer dense |
|---|---:|---:|---:|---:|---:|---:|---:|
| 8 | 91 | 11.4 | 21 | 90 | 23 | 90 | 23 |
| 16 | 179 | 11.2 | 23 | 174 | 43 | 173 | 42 |
| 32 | 358 | 11.2 | 23 | 342 | 80 | 342 | 80 |
| 64 | 716 | 11.2 | 26 | 670 | 146 | 666 | 142 |
| 128 | 1523 | 11.9 | 28 | 1392 | 253 | 1393 | 256 |
| 256 | 3365 | 13.1 | 29 | 3049 | 453 | 3039 | 447 |
| 512 | 6898 | 13.5 | 44 | 6153 | 799 | 6144 | 795 |
| 1000 | 20078 | 20.1 | 44 | 18373 | 1360 | 18370 | 1351 |
| 2000 | 47229 | 23.6 | 44 | 43325 | 2403 | 43319 | 2366 |
| 5000 | 128474 | 25.7 | 44 | 117043 | 5383 | 117083 | 5358 |
| 10000 | 264053 | 26.4 | 44 | 238825 | 11661 | 238778 | 11605 |

State/layout facts are calculated from the saved byte strings and the final implementation by [layout.py](memory/layout.py). They are explanatory counts, not public runtime API counters. The array budget below excludes fixed fields and allocator rounding.

| Strings | Class | Dense rows KiB | Sparse KiB | Edges KiB | Outputs KiB | Pointers KiB | Arrays KiB |
|---|---|---:|---:|---:|---:|---:|---:|
| 8 | Matcher | 2.0 | 0.8 | 0.0 | 1.1 | 0.1 | 3.9 |
| 8 | Replacer | 2.0 | 0.8 | 0.0 | 0.4 | 0.1 | 3.2 |
| 128 | Matcher | 28.7 | 13.3 | 0.0 | 16.3 | 1.0 | 59.3 |
| 128 | Replacer | 29.0 | 13.3 | 0.0 | 5.4 | 2.0 | 49.8 |
| 512 | Matcher | 140.4 | 62.7 | 0.0 | 72.1 | 4.0 | 279.3 |
| 512 | Replacer | 139.7 | 62.7 | 0.0 | 24.0 | 8.0 | 234.4 |
| 2000 | Matcher | 422.4 | 479.6 | 0.5 | 507.7 | 15.6 | 1425.8 |
| 2000 | Replacer | 415.9 | 479.9 | 0.3 | 169.2 | 31.2 | 1096.6 |
| 10000 | Matcher | 2049.8 | 2662.1 | 10.5 | 2798.7 | 78.1 | 7599.2 |
| 10000 | Replacer | 2039.9 | 2662.2 | 11.2 | 932.7 | 156.2 | 5802.3 |

### Query peaks

Additional allocations above an already prepared object, subject and expected-result data. Each operation resets the peak; correctness checks occur after the snapshot. Result storage is included.

| Strings | matches() | countMatches() | getMatchedKeywords() | matchAll() | replace() |
|---|---:|---:|---:|---:|---:|
| 8 | 0.0 | 0.0 | 0.6 | 480.6 | 400.0 |
| 16 | 0.0 | 0.0 | 0.6 | 480.6 | 400.0 |
| 32 | 0.0 | 0.0 | 0.6 | 480.6 | 400.0 |
| 64 | 0.0 | 0.0 | 0.6 | 480.6 | 400.0 |
| 128 | 0.0 | 0.0 | 0.6 | 480.6 | 400.0 |
| 256 | 0.0 | 0.0 | 0.7 | 480.6 | 400.0 |
| 512 | 0.0 | 0.0 | 0.9 | 480.6 | 400.0 |
| 1000 | 0.0 | 0.0 | 1.4 | 480.6 | 400.0 |
| 2000 | 0.0 | 0.0 | 2.4 | 480.6 | 400.0 |
| 5000 | 0.0 | 0.0 | 8.4 | 480.6 | 400.0 |
| 10000 | 0.0 | 0.0 | 12.4 | 480.6 | 400.0 |

| Strings | Distinct keys matched | All overlapping hits | Replacements | Output KiB |
|---|---:|---:|---:|---:|
| 8 | 8 | 3121 | 3121 | 142.1 |
| 16 | 8 | 3121 | 3121 | 142.1 |
| 32 | 8 | 3121 | 3121 | 142.1 |
| 64 | 8 | 3121 | 3121 | 142.1 |
| 128 | 8 | 3121 | 3121 | 142.1 |
| 256 | 8 | 3121 | 3121 | 142.1 |
| 512 | 8 | 3121 | 3121 | 142.1 |
| 1000 | 8 | 3121 | 3121 | 142.1 |
| 2000 | 8 | 3121 | 3121 | 142.1 |
| 5000 | 8 | 3121 | 3121 | 142.1 |
| 10000 | 8 | 3121 | 3121 | 142.1 |

## Query interpretation

Each family has a saved 65,536-byte subject made by repeating a sentence containing its first eight terms. The text stays fixed as N grows; other terms may also match. These repetitive texts measure allocations. They are not additional product-speed benchmarks.

`matches()` and `countMatches()` allocate no additional tracked heap in these runs. `getMatchedKeywords()` needs dictionary-sized scratch storage. `matchAll()` stores a result object per hit. `replace()` has subject-sized candidate storage plus its output. Different hit density, output expansion or subject length changes these peaks.

Constructor and query peaks occur in different operations: do not sum them. No memory comparison with PCRE/native alternatives, other allocators, machines or FPM worker sharing is claimed.

## Data and reproduction

[GCC samples](data/memory-gcc15.json) · [Clang samples](data/memory-clang21.json) · [fixtures](memory/index.json) · [generator](memory/generate.py) · [PHP snapshots](memory/measure.php) · [driver](memory/measure.py). The module/PHP hashes match the main time series. Every fresh process checks the measured methods against saved independent expected results.

After the main series in [Reproduce](REPRODUCE.md), keep its BENCH_BUILDS, RUN_ROOT and BENCH_CPU variables:

```sh
python3 memory/generate.py --check
for tag in gcc15 clang21; do
  python3 memory/measure.py --php-build "$BENCH_BUILDS/runtime-$tag" \
    --module "$RUN_ROOT/data-product-$tag/strmatch.so" \
    --reference-data "$RUN_ROOT/data-product-$tag/results.json" \
    --compiler "$tag" --cpu "$BENCH_CPU" --output "$RUN_ROOT/memory-$tag.json"
done
```

Each compiler ends with `MEMORY COMPLETE: 44 configurations, 220 fresh processes`. One compiler took under a minute here. No timing warmup is needed for allocation snapshots. Existing output files are rejected; failures abort the series.

Copy each complete memory JSON into `data/memory-gcc15.json` or `data/memory-clang21.json` beside the corresponding imported main captures in a separate report checkout. For example, use `cp "$RUN_ROOT/memory-gcc15.json" data/memory-gcc15.json` and likewise for Clang. `python3 memory/render.py` and `python3 memory/render.py --check` update/verify only memory tables. The general renderer requires all supplemental captures to match the newly imported main binaries. `python3 memory/layout.py --check` checks state counts against saved fixtures. The optional `python3 memory/plot.py` uses Matplotlib; no plotting runs inside a measurement.
