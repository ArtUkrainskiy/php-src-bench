# Frozen application corpus

Status: measured on 1 November 2026; see the [report](../README.md) and [full tables](../tables/product.md).

The JSON status field is retained from fixture creation (before timing);
measurement completion is documented in the report, not that frozen field.

Each linked JSON file contains the full UTF-8 input text, the search needles,
their byte lengths and first match positions, the PHP expression and its expected result.
`inputs` stores a text once per suite; cases refer to its key.
Positions use UTF-8 bytes; an absent match is `-1`.

| Suite | Cases | Timed cases | Input bytes | Needle bytes | Scope |
|---|---:|---:|---:|---:|---|
| [moderation-short](moderation-short.json) | 12 | 12 | 256–282 | 9–31 | inline control |
| [moderation-medium](moderation-medium.json) | 12 | 12 | 4096–4122 | 9–31 | core |
| [moderation-long](moderation-long.json) | 12 | 12 | 65536–65562 | 9–31 | core |
| [search](search.json) | 16 | 12 | 4096–4129 | 16–31 | core |
| [substr-count](substr-count.json) | 5 | 5 | 3480–4114 | 16–18 | core |
| [replace](replace.json) | 15 | 15 | 3480–4116 | 18–18 | core |
| [explode](explode.json) | 5 | 5 | 3531–4119 | 21–21 | core |
| [stream-get-line](stream-get-line.json) | 4 | 4 | 4096–4119 | 21–21 | core |
| [search-long](search-long.json) | 4 | 4 | 65536–65554 | 16–16 | core |
| [mbstring](mbstring.json) | 30 | 30 | 4096–4121 | 12–23 | mbstring |
| [intl-ascii](intl-ascii.json) | 12 | 12 | 4096–4114 | 16–16 | intl |
| [documents-moderation](documents-moderation.json) | 6 | 6 | 1168–2184 | 9–31 | core |
| [documents-search](documents-search.json) | 8 | 8 | 2422–68022 | 16–18 | core |
| [documents-replace](documents-replace.json) | 11 | 11 | 2422–2475 | 16–19 | core |
| [documents-count](documents-count.json) | 2 | 2 | 2422–2475 | 18–18 | core |
| [documents-mail](documents-mail.json) | 6 | 6 | 2878–3764 | 21–23 | core |
| [documents-repeated](documents-repeated.json) | 6 | 6 | 14919–15339 | 18–21 | core |
| [controls-lengths](controls-lengths.json) | 16 | 16 | 4096–4096 | 9–31 | diagnostic control |
| [controls-routing](controls-routing.json) | 19 | 19 | 1023–12299 | 8–256 | diagnostic control |
| [controls-prefix](controls-prefix.json) | 4 | 4 | 4096–4096 | 9–64 | diagnostic control |

Total: 205 cases: 108 core application timed cases, 12 short inline controls, 39 diagnostic controls, 42 optional extension cases and 4 alias correctness checks.

“Timed cases” are included in the completed elapsed-time and counter measurements.
`strchr()` aliases `strstr()` and is checked for correctness without a duplicate timing.
Application needles are 9–31 UTF-8 bytes. Short moderation inputs stay below
1024 bytes and exercise the existing inline path.
`controls-*` are separate synthetic diagnostics, not application benefit rows.
They deliberately include 8-, 32-, 64- and 256-byte needles to check adjacent routes.
`documents-*` preserve complete HTML, MIME messages, JSON log records and
independent posts. They are constructed fixtures, not captured production traffic.
Optional mbstring and intl fixtures passed runtime validation and were measured with matching shared modules.

The generator is optional. Review and measure the saved JSON files directly.
To propose changes, generate into a separate directory and inspect the diff first.
Full text and expected string results may make individual JSON lines long.
