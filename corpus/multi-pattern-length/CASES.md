# Fixed-length cases

Every case reuses one prepared 128-key dictionary. Only the worker lifecycle is measured. One operation processes one string; four different exact-length variants cycle equally often.

| Case | Operation | Bytes/string | Variants | Keys | Occurrences/string |
|---|---|---:|---:|---:|---|
| `length.any.absent.128` | any | 128 | 4 | 128 | 0 |
| `length.any.start.128` | any | 128 | 4 | 128 | 1 |
| `length.any.middle.128` | any | 128 | 4 | 128 | 1 |
| `length.any.end.128` | any | 128 | 4 | 128 | 1 |
| `length.any.absent.4096` | any | 4096 | 4 | 128 | 0 |
| `length.any.start.4096` | any | 4096 | 4 | 128 | 1 |
| `length.any.middle.4096` | any | 4096 | 4 | 128 | 1 |
| `length.any.end.4096` | any | 4096 | 4 | 128 | 1 |
| `length.any.absent.16384` | any | 16384 | 4 | 128 | 0 |
| `length.any.start.16384` | any | 16384 | 4 | 128 | 1 |
| `length.any.middle.16384` | any | 16384 | 4 | 128 | 1 |
| `length.any.end.16384` | any | 16384 | 4 | 128 | 1 |
| `length.any.absent.65536` | any | 65536 | 4 | 128 | 0 |
| `length.any.start.65536` | any | 65536 | 4 | 128 | 1 |
| `length.any.middle.65536` | any | 65536 | 4 | 128 | 1 |
| `length.any.end.65536` | any | 65536 | 4 | 128 | 1 |
| `length.unique.mixed.512` | unique | 512 | 4 | 128 | 21–29 |
| `length.replace.mixed.512` | replace | 512 | 4 | 128 | 21–29 |
| `length.unique.mixed.4096` | unique | 4096 | 4 | 128 | 194–202 |
| `length.replace.mixed.4096` | replace | 4096 | 4 | 128 | 194–202 |
| `length.unique.mixed.16384` | unique | 16384 | 4 | 128 | 785–787 |
| `length.replace.mixed.16384` | replace | 16384 | 4 | 128 | 785–787 |
| `length.unique.mixed.65536` | unique | 65536 | 4 | 128 | 3153–3157 |
| `length.replace.mixed.65536` | replace | 65536 | 4 | 128 | 3153–3157 |

Search results preserve nested literal matches. Replacements use the longest key at the earliest position without rescanning inserted URLs. Dictionaries, texts and expected outputs are saved in the suite JSON. These are controlled authored examples, not production traces.
