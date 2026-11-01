# Complete case inventory

Generated from the saved JSON inputs by `generate.py`. No performance results are included.

Sizes are UTF-8 bytes per document. Matches are selected non-overlapping replacements for replacement jobs; for unique-key jobs they count distinct matching keys; for other search jobs they count every occurrence, including nested keywords. Each range covers all documents in the case. See the JSON `facts` for exact offsets and counts.

A request is one saved job. `Documents/request` distinguishes one document from a genuine batch. The same dictionary may be prepared across requests only where the lifecycle permits it. Only order-email dictionaries change between jobs.

## [moderation](suites/moderation.json)

| Task / case ID | Operation | Keys (key bytes) | Document bytes | Matches | Jobs × documents/request |
|---|---|---:|---:|---:|---:|
| Check a short comment<br>`scale.moderation.short.absent.8` | any | 8 (4–8) | 56–84 | 0 | 8 × 1 |
| Check a short comment<br>`scale.moderation.short.start.8` | any | 8 (4–8) | 89–121 | 1–2 | 8 × 1 |
| Check a short comment<br>`scale.moderation.short.middle.8` | any | 8 (4–8) | 152–196 | 1–2 | 8 × 1 |
| Check a short comment<br>`scale.moderation.short.end.8` | any | 8 (4–8) | 93–125 | 1–2 | 8 × 1 |
| Check a detailed support message<br>`scale.moderation.message.absent.8` | any | 8 (4–8) | 749–817 | 0 | 3 × 1 |
| Check a detailed support message<br>`scale.moderation.message.quoted.8` | any | 8 (4–8) | 777–845 | 1 | 3 × 1 |
| Check a short comment<br>`scale.moderation.short.absent.16` | any | 16 (4–13) | 56–84 | 0 | 8 × 1 |
| Check a short comment<br>`scale.moderation.short.start.16` | any | 16 (4–13) | 89–121 | 1–2 | 8 × 1 |
| Check a short comment<br>`scale.moderation.short.middle.16` | any | 16 (4–13) | 152–196 | 1–2 | 8 × 1 |
| Check a short comment<br>`scale.moderation.short.end.16` | any | 16 (4–13) | 93–125 | 1–2 | 8 × 1 |
| Check a detailed support message<br>`scale.moderation.message.absent.16` | any | 16 (4–13) | 749–817 | 0 | 3 × 1 |
| Check a detailed support message<br>`scale.moderation.message.quoted.16` | any | 16 (4–13) | 777–845 | 1 | 3 × 1 |
| Check a short comment<br>`scale.moderation.short.absent.32` | any | 32 (4–23) | 56–84 | 0 | 8 × 1 |
| Check a short comment<br>`scale.moderation.short.start.32` | any | 32 (4–23) | 89–121 | 1–2 | 8 × 1 |
| Check a short comment<br>`scale.moderation.short.middle.32` | any | 32 (4–23) | 152–196 | 1–2 | 8 × 1 |
| Check a short comment<br>`scale.moderation.short.end.32` | any | 32 (4–23) | 93–125 | 1–2 | 8 × 1 |
| Check a detailed support message<br>`scale.moderation.message.absent.32` | any | 32 (4–23) | 749–817 | 0 | 3 × 1 |
| Check a detailed support message<br>`scale.moderation.message.quoted.32` | any | 32 (4–23) | 777–845 | 1 | 3 × 1 |
| Check a short comment<br>`scale.moderation.short.absent.64` | any | 64 (3–23) | 56–84 | 0 | 8 × 1 |
| Check a short comment<br>`scale.moderation.short.start.64` | any | 64 (3–23) | 89–121 | 1–2 | 8 × 1 |
| Check a short comment<br>`scale.moderation.short.middle.64` | any | 64 (3–23) | 152–196 | 1–2 | 8 × 1 |
| Check a short comment<br>`scale.moderation.short.end.64` | any | 64 (3–23) | 93–125 | 1–2 | 8 × 1 |
| Check a detailed support message<br>`scale.moderation.message.absent.64` | any | 64 (3–23) | 749–817 | 0 | 3 × 1 |
| Check a detailed support message<br>`scale.moderation.message.quoted.64` | any | 64 (3–23) | 777–845 | 1 | 3 × 1 |
| Check a short comment<br>`scale.moderation.short.absent.128` | any | 128 (3–30) | 56–84 | 0 | 8 × 1 |
| Check a short comment<br>`scale.moderation.short.start.128` | any | 128 (3–30) | 89–121 | 1–2 | 8 × 1 |
| Check a short comment<br>`scale.moderation.short.middle.128` | any | 128 (3–30) | 152–196 | 1–2 | 8 × 1 |
| Check a short comment<br>`scale.moderation.short.end.128` | any | 128 (3–30) | 93–125 | 1–2 | 8 × 1 |
| Check a detailed support message<br>`scale.moderation.message.absent.128` | any | 128 (3–30) | 749–817 | 0 | 3 × 1 |
| Check a detailed support message<br>`scale.moderation.message.quoted.128` | any | 128 (3–30) | 777–845 | 1 | 3 × 1 |
| Check a short comment<br>`scale.moderation.short.absent.256` | any | 256 (3–30) | 56–84 | 0 | 8 × 1 |
| Check a short comment<br>`scale.moderation.short.start.256` | any | 256 (3–30) | 89–121 | 1–2 | 8 × 1 |
| Check a short comment<br>`scale.moderation.short.middle.256` | any | 256 (3–30) | 152–196 | 1–2 | 8 × 1 |
| Check a short comment<br>`scale.moderation.short.end.256` | any | 256 (3–30) | 93–125 | 1–2 | 8 × 1 |
| Check a detailed support message<br>`scale.moderation.message.absent.256` | any | 256 (3–30) | 749–817 | 0 | 3 × 1 |
| Check a detailed support message<br>`scale.moderation.message.quoted.256` | any | 256 (3–30) | 777–845 | 1 | 3 × 1 |
| Check a short comment<br>`scale.moderation.short.absent.512` | any | 512 (3–30) | 56–84 | 0 | 8 × 1 |
| Check a short comment<br>`scale.moderation.short.start.512` | any | 512 (3–30) | 89–121 | 1–2 | 8 × 1 |
| Check a short comment<br>`scale.moderation.short.middle.512` | any | 512 (3–30) | 152–196 | 1–2 | 8 × 1 |
| Check a short comment<br>`scale.moderation.short.end.512` | any | 512 (3–30) | 93–125 | 1–2 | 8 × 1 |
| Check a detailed support message<br>`scale.moderation.message.absent.512` | any | 512 (3–30) | 749–817 | 0 | 3 × 1 |
| Check a detailed support message<br>`scale.moderation.message.quoted.512` | any | 512 (3–30) | 777–845 | 1 | 3 × 1 |

Dictionary scope: `fixed_policy`. The saved dictionary is identical across jobs; both per-request preparation and worker reuse are eligible.

Declared methods: `contains_loop`, `preg_match`, `matcher`.

Method eligibility and task-specific details are recorded separately for each case in the linked JSON.

## [search](suites/search.json)

| Task / case ID | Operation | Keys (key bytes) | Document bytes | Matches | Jobs × documents/request |
|---|---|---:|---:|---:|---:|
| Find distinct support terms<br>`scale.search.unique.8` | unique | 8 (5–16) | 397–465 | 0–8 | 8 × 1 |
| Count support-term occurrences<br>`scale.search.count.8` | count | 8 (5–16) | 397–465 | 0–11 | 8 × 1 |
| Locate support-term occurrences<br>`scale.search.all.8` | all | 8 (5–16) | 397–465 | 0–11 | 8 × 1 |
| Find distinct support terms<br>`scale.search.unique.16` | unique | 16 (5–16) | 397–465 | 0–10 | 8 × 1 |
| Count support-term occurrences<br>`scale.search.count.16` | count | 16 (5–16) | 397–465 | 0–14 | 8 × 1 |
| Locate support-term occurrences<br>`scale.search.all.16` | all | 16 (5–16) | 397–465 | 0–14 | 8 × 1 |
| Find distinct support terms<br>`scale.search.unique.32` | unique | 32 (4–20) | 397–465 | 3–12 | 8 × 1 |
| Count support-term occurrences<br>`scale.search.count.32` | count | 32 (4–20) | 397–465 | 3–16 | 8 × 1 |
| Locate support-term occurrences<br>`scale.search.all.32` | all | 32 (4–20) | 397–465 | 3–16 | 8 × 1 |
| Find distinct support terms<br>`scale.search.unique.64` | unique | 64 (3–25) | 397–465 | 6–16 | 8 × 1 |
| Count support-term occurrences<br>`scale.search.count.64` | count | 64 (3–25) | 397–465 | 7–19 | 8 × 1 |
| Locate support-term occurrences<br>`scale.search.all.64` | all | 64 (3–25) | 397–465 | 7–19 | 8 × 1 |
| Find distinct support terms<br>`scale.search.unique.128` | unique | 128 (3–25) | 397–465 | 15–21 | 8 × 1 |
| Count support-term occurrences<br>`scale.search.count.128` | count | 128 (3–25) | 397–465 | 18–26 | 8 × 1 |
| Locate support-term occurrences<br>`scale.search.all.128` | all | 128 (3–25) | 397–465 | 18–26 | 8 × 1 |
| Find distinct support terms<br>`scale.search.unique.256` | unique | 256 (3–25) | 397–465 | 15–21 | 8 × 1 |
| Count support-term occurrences<br>`scale.search.count.256` | count | 256 (3–25) | 397–465 | 18–26 | 8 × 1 |
| Locate support-term occurrences<br>`scale.search.all.256` | all | 256 (3–25) | 397–465 | 18–26 | 8 × 1 |
| Find distinct support terms<br>`scale.search.unique.512` | unique | 512 (3–25) | 397–465 | 15–22 | 8 × 1 |
| Count support-term occurrences<br>`scale.search.count.512` | count | 512 (3–25) | 397–465 | 19–27 | 8 × 1 |
| Locate support-term occurrences<br>`scale.search.all.512` | all | 512 (3–25) | 397–465 | 19–27 | 8 × 1 |

Dictionary scope: `fixed_policy`. The saved dictionary is identical across jobs; both per-request preparation and worker reuse are eligible.

Declared methods: `strpos_unique`, `preg_each_unique`, `matcher`, `strpos_count`, `preg_each_count`, `strpos_all`, `preg_each_all`.

Method eligibility and task-specific details are recorded separately for each case in the linked JSON.

## [replacement](suites/replacement.json)

| Task / case ID | Operation | Keys (key bytes) | Document bytes | Matches | Jobs × documents/request |
|---|---|---:|---:|---:|---:|
| Add support links to a help article<br>`scale.replace.articles1.8` | replace | 8 (5–16) | 397–465 | 0–7 | 8 × 1 |
| Publish eight help articles<br>`scale.replace.articles8.8` | replace | 8 (5–16) | 397–465 | 0–7 | 1 × 8 |
| Add support links to a help article<br>`scale.replace.articles1.16` | replace | 16 (5–16) | 397–465 | 0–9 | 8 × 1 |
| Publish eight help articles<br>`scale.replace.articles8.16` | replace | 16 (5–16) | 397–465 | 0–9 | 1 × 8 |
| Add support links to a help article<br>`scale.replace.articles1.32` | replace | 32 (4–20) | 397–465 | 2–11 | 8 × 1 |
| Publish eight help articles<br>`scale.replace.articles8.32` | replace | 32 (4–20) | 397–465 | 2–11 | 1 × 8 |
| Add support links to a help article<br>`scale.replace.articles1.64` | replace | 64 (3–25) | 397–465 | 5–14 | 8 × 1 |
| Publish eight help articles<br>`scale.replace.articles8.64` | replace | 64 (3–25) | 397–465 | 5–14 | 1 × 8 |
| Add support links to a help article<br>`scale.replace.articles1.128` | replace | 128 (3–25) | 397–465 | 13–18 | 8 × 1 |
| Publish eight help articles<br>`scale.replace.articles8.128` | replace | 128 (3–25) | 397–465 | 13–18 | 1 × 8 |
| Add support links to a help article<br>`scale.replace.articles1.256` | replace | 256 (3–25) | 397–465 | 13–18 | 8 × 1 |
| Publish eight help articles<br>`scale.replace.articles8.256` | replace | 256 (3–25) | 397–465 | 13–18 | 1 × 8 |
| Add support links to a help article<br>`scale.replace.articles1.512` | replace | 512 (3–25) | 397–465 | 13–19 | 8 × 1 |
| Publish eight help articles<br>`scale.replace.articles8.512` | replace | 512 (3–25) | 397–465 | 13–19 | 1 × 8 |

Dictionary scope: `fixed_policy`. The saved dictionary is identical across jobs; both per-request preparation and worker reuse are eligible.

Declared methods: `strtr`, `preg_replace_callback`, `replacer`.

Method eligibility and task-specific details are recorded separately for each case in the linked JSON.

## [controls](suites/controls.json)

| Task / case ID | Operation | Keys (key bytes) | Document bytes | Matches | Jobs × documents/request |
|---|---|---:|---:|---:|---:|
| Flag a short EN comment: no configured phrase<br>`moderation.en.clean` | any | 12 (4–27) | 56–84 | 0 | 8 × 1 |
| Mask three registered secrets in a larger incident log batch<br>`secrets.incident-batch` | replace | 24 (40–50) | 64741–64786 | 3 | 4 × 1 |

Dictionary scope: `community_policy`. The saved dictionary is identical across jobs; both per-request preparation and worker reuse are eligible.

Declared methods: `contains_loop`, `preg_match`, `matcher`, `strtr`, `preg_replace_callback`, `replacer`, `str_replace`, `preg_replace`.

Method eligibility and task-specific details are recorded separately for each case in the linked JSON.
