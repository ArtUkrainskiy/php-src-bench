# Pure construction and retained memory

**Time: µs for constructing one object from an already loaded dictionary. Memory: KiB added by the retained object above that dictionary.** No search or destruction is included in the construction column. The process is warm. Intervals around `new` include the adjacent `hrtime()` cost; no empty-clock subtraction is applied. Destruction is measured separately and included only in payback.

Constructor times use 250 ms warmup and 15 samples of approximately one second in total. Memory uses five fresh processes; values match across all repeats and both compilers. This is Zend allocation, not process RSS or total process memory. The support glossary/catalog keys and values are the [saved memory dictionary](memory/glossary-catalog.json); moderation is the fixed-length study's 128-phrase policy. Sharing patterns differ even at the same entry count.

## gcc15

| Dictionary | Keys | Matcher new, µs | Matcher added, KiB | Replacer new, µs | Replacer added, KiB |
|---|---:|---:|---:|---:|---:|
| Moderation phrases | 128 | 56.871 | 58.0 | n/a | n/a |
| Support glossary/catalog | 8 | 2.133 | 3.5 | 2.341 | 3.5 |
| Support glossary/catalog | 16 | 3.885 | 5.7 | 4.868 | 6.2 |
| Support glossary/catalog | 32 | 7.994 | 10.6 | 9.401 | 13.6 |
| Support glossary/catalog | 64 | 18.259 | 29.4 | 18.380 | 24.4 |
| Support glossary/catalog | 128 | 44.716 | 46.1 | 43.353 | 43.2 |
| Support glossary/catalog | 256 | 130.375 | 83.8 | 111.629 | 70.2 |
| Support glossary/catalog | 512 | 351.759 | 187.8 | 288.682 | 140.8 |
| Support glossary/catalog | 1000 | 872.781 | 400.8 | 604.971 | 232.8 |
| Support glossary/catalog | 2000 | 1770.989 | 728.8 | 1125.255 | 368.8 |
| Support glossary/catalog | 5000 | 3926.115 | 1396.8 | 3243.375 | 760.8 |
| Support glossary/catalog | 10000 | 10264.009 | 2272.8 | 6931.491 | 1324.8 |

### Destruction cost

| Dictionary | Keys | Class | Destruction, µs |
|---|---:|---|---:|
| support | 8 | Matcher | 0.050 |
| support | 8 | Replacer | 0.058 |
| support | 16 | Matcher | 0.058 |
| support | 16 | Replacer | 0.070 |
| support | 32 | Matcher | 0.087 |
| support | 32 | Replacer | 0.099 |
| support | 64 | Matcher | 0.137 |
| support | 64 | Replacer | 0.168 |
| support | 128 | Matcher | 0.172 |
| support | 128 | Replacer | 0.251 |
| support | 256 | Matcher | 0.272 |
| support | 256 | Replacer | 0.448 |
| support | 512 | Matcher | 0.574 |
| support | 512 | Replacer | 0.917 |
| support | 1000 | Matcher | 1.212 |
| support | 1000 | Replacer | 1.991 |
| support | 2000 | Matcher | 2.306 |
| support | 2000 | Replacer | 3.895 |
| support | 5000 | Matcher | 5.512 |
| support | 5000 | Replacer | 54.130 |
| support | 10000 | Matcher | 101.856 |
| support | 10000 | Replacer | 56.797 |
| moderation | 128 | Matcher | 0.170 |

## clang21

| Dictionary | Keys | Matcher new, µs | Matcher added, KiB | Replacer new, µs | Replacer added, KiB |
|---|---:|---:|---:|---:|---:|
| Moderation phrases | 128 | 55.504 | 58.0 | n/a | n/a |
| Support glossary/catalog | 8 | 2.026 | 3.5 | 2.338 | 3.5 |
| Support glossary/catalog | 16 | 3.693 | 5.7 | 4.664 | 6.2 |
| Support glossary/catalog | 32 | 7.586 | 10.6 | 9.156 | 13.6 |
| Support glossary/catalog | 64 | 17.567 | 29.4 | 17.891 | 24.4 |
| Support glossary/catalog | 128 | 42.825 | 46.1 | 42.773 | 43.2 |
| Support glossary/catalog | 256 | 125.946 | 83.8 | 109.404 | 70.2 |
| Support glossary/catalog | 512 | 344.072 | 187.8 | 285.742 | 140.8 |
| Support glossary/catalog | 1000 | 865.712 | 400.8 | 599.167 | 232.8 |
| Support glossary/catalog | 2000 | 1756.428 | 728.8 | 1112.941 | 368.8 |
| Support glossary/catalog | 5000 | 4033.889 | 1396.8 | 3192.125 | 760.8 |
| Support glossary/catalog | 10000 | 10194.090 | 2272.8 | 6888.769 | 1324.8 |

### Destruction cost

| Dictionary | Keys | Class | Destruction, µs |
|---|---:|---|---:|
| support | 8 | Matcher | 0.054 |
| support | 8 | Replacer | 0.056 |
| support | 16 | Matcher | 0.062 |
| support | 16 | Replacer | 0.067 |
| support | 32 | Matcher | 0.079 |
| support | 32 | Replacer | 0.100 |
| support | 64 | Matcher | 0.134 |
| support | 64 | Replacer | 0.167 |
| support | 128 | Matcher | 0.182 |
| support | 128 | Replacer | 0.263 |
| support | 256 | Matcher | 0.302 |
| support | 256 | Replacer | 0.468 |
| support | 512 | Matcher | 0.544 |
| support | 512 | Replacer | 0.909 |
| support | 1000 | Matcher | 1.246 |
| support | 1000 | Replacer | 1.861 |
| support | 2000 | Matcher | 2.316 |
| support | 2000 | Replacer | 3.811 |
| support | 5000 | Matcher | 5.524 |
| support | 5000 | Replacer | 52.854 |
| support | 10000 | Matcher | 102.083 |
| support | 10000 | Replacer | 56.958 |
| moderation | 128 | Matcher | 0.183 |

Construction peak is a different quantity. [Memory totals](MEMORY.md) show input alone, input plus the ready object, and their common-baseline construction peak. These columns are totals, not amounts to add together. [First constructors and build/release measurements](PREPARATION.md) have different timing scopes and are not substituted into this table.

[GCC samples](data/build-cost-gcc15.json) · [Clang samples](data/build-cost-clang21.json).
