# Fixed-4-KiB cases

| Case | Keys | First match byte offsets | First matching key ranks (1-based) | Replacements/string |
|---|---:|---|---|---|
| `grid.any.absent.8` | 8 | —, —, —, — | —, —, —, — | — |
| `grid.any.absent.16` | 16 | —, —, —, — | —, —, —, — | — |
| `grid.any.absent.32` | 32 | —, —, —, — | —, —, —, — | — |
| `grid.any.absent.64` | 64 | —, —, —, — | —, —, —, — | — |
| `grid.any.absent.128` | 128 | —, —, —, — | —, —, —, — | — |
| `grid.any.absent.256` | 256 | —, —, —, — | —, —, —, — | — |
| `grid.any.absent.512` | 512 | —, —, —, — | —, —, —, — | — |
| `grid.replace.mixed.8` | 8 | 127, 617, 155, 14 | 1, 1, 1, 1 | 24, 22, 22, 26 |
| `grid.replace.mixed.16` | 16 | 22, 308, 75, 14 | 1, 1, 1, 1 | 40, 35, 40, 40 |
| `grid.replace.mixed.32` | 32 | 22, 203, 18, 14 | 1, 1, 1, 1 | 65, 62, 62, 61 |
| `grid.replace.mixed.64` | 64 | 22, 21, 18, 14 | 1, 1, 1, 1 | 100, 99, 99, 96 |
| `grid.replace.mixed.128` | 128 | 22, 21, 18, 14 | 1, 1, 1, 1 | 144, 138, 141, 141 |
| `grid.replace.mixed.256` | 256 | 22, 21, 18, 14 | 1, 1, 1, 1 | 145, 139, 142, 142 |
| `grid.replace.mixed.512` | 512 | 22, 21, 18, 14 | 1, 1, 1, 1 | 147, 141, 144, 144 |
| `grid.any.absent.position` | 128 | —, —, —, — | —, —, —, — | — |
| `grid.any.start.position` | 128 | 18, 18, 18, 18 | 1, 37, 91, 128 | — |
| `grid.any.middle.position` | 128 | 2064, 2067, 2062, 2063 | 1, 37, 91, 128 | — |
| `grid.any.end.position` | 128 | 4090, 4087, 4090, 4090 | 1, 37, 91, 128 | — |
