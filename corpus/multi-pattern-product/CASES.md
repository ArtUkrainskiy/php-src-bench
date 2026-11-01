# Complete case inventory

Generated from the saved JSON inputs by `generate.py`. No performance results are included.

Sizes are UTF-8 bytes per document. Matches are selected non-overlapping replacements for replacement jobs; for unique-key jobs they count distinct matching keys; for other search jobs they count every occurrence, including nested keywords. Each range covers all documents in the case. See the JSON `facts` for exact offsets and counts.

A request is one saved job. `Documents/request` distinguishes one document from a genuine batch. The same dictionary may be prepared across requests only where the lifecycle permits it. Only order-email dictionaries change between jobs.

## [moderation](suites/moderation.json)

| Task / case ID | Operation | Keys (key bytes) | Document bytes | Matches | Jobs × documents/request |
|---|---|---:|---:|---:|---:|
| Flag a short EN comment: no configured phrase<br>`moderation.en.clean` | any | 12 (4–27) | 56–84 | 0 | 8 × 1 |
| Flag a short EN comment: phrase at the start<br>`moderation.en.start` | any | 12 (4–27) | 101–148 | 1 | 8 × 1 |
| Flag a short EN comment: phrase inside the message<br>`moderation.en.body` | any | 12 (4–27) | 160–212 | 1 | 8 × 1 |
| Flag a short EN comment: phrase at the end<br>`moderation.en.end` | any | 12 (4–27) | 108–155 | 1 | 8 × 1 |
| Check a detailed EN support message: no configured phrase<br>`moderation.en.post-clean` | any | 12 (4–27) | 749–817 | 0 | 3 × 1 |
| Check a detailed EN support message: a promotional phrase is quoted<br>`moderation.en.post-reported-phrase` | any | 12 (4–27) | 807–852 | 1 | 3 × 1 |
| Flag a short RU comment: no configured phrase<br>`moderation.ru.clean` | any | 12 (8–41) | 111–160 | 0 | 8 × 1 |
| Flag a short RU comment: phrase at the start<br>`moderation.ru.start` | any | 12 (8–41) | 208–290 | 1 | 8 × 1 |
| Flag a short RU comment: phrase inside the message<br>`moderation.ru.body` | any | 12 (8–41) | 314–382 | 1 | 8 × 1 |
| Flag a short RU comment: phrase at the end<br>`moderation.ru.end` | any | 12 (8–41) | 176–258 | 1 | 8 × 1 |
| Check a detailed RU support message: no configured phrase<br>`moderation.ru.post-clean` | any | 12 (8–41) | 1191–1451 | 0 | 3 × 1 |
| Check a detailed RU support message: a promotional phrase is quoted<br>`moderation.ru.post-reported-phrase` | any | 12 (8–41) | 1270–1511 | 1 | 3 × 1 |
| Flag a short ZH comment: no configured phrase<br>`moderation.zh.clean` | any | 12 (6–27) | 42–78 | 0 | 8 × 1 |
| Flag a short ZH comment: phrase at the start<br>`moderation.zh.start` | any | 12 (6–27) | 87–136 | 1 | 8 × 1 |
| Flag a short ZH comment: phrase inside the message<br>`moderation.zh.body` | any | 12 (6–27) | 147–204 | 1 | 8 × 1 |
| Flag a short ZH comment: phrase at the end<br>`moderation.zh.end` | any | 12 (6–27) | 84–133 | 1 | 8 × 1 |
| Check a detailed ZH support message: no configured phrase<br>`moderation.zh.post-clean` | any | 12 (6–27) | 691–796 | 0 | 3 × 1 |
| Check a detailed ZH support message: a promotional phrase is quoted<br>`moderation.zh.post-reported-phrase` | any | 12 (6–27) | 734–839 | 1 | 3 × 1 |

Dictionary scope: `community_policy`. The saved dictionary is identical across jobs; both per-request preparation and worker reuse are eligible.

Declared methods: `contains_loop`, `preg_match`, `matcher`.

Method eligibility and task-specific details are recorded separately for each case in the linked JSON.

## [error-routing](suites/error-routing.json)

| Task / case ID | Operation | Keys (key bytes) | Document bytes | Matches | Jobs × documents/request |
|---|---|---:|---:|---:|---:|
| Decide whether a request trace needs an alert: healthy trace<br>`errors.healthy` | any | 8 (9–29) | 2679–2704 | 0 | 8 × 1 |
| Decide whether a request trace needs an alert: error in the first record<br>`errors.first` | any | 8 (9–29) | 2686–2718 | 1 | 8 × 1 |
| Decide whether a request trace needs an alert: error in the middle record<br>`errors.middle` | any | 8 (9–29) | 2697–2724 | 1 | 8 × 1 |
| Decide whether a request trace needs an alert: error in the last record<br>`errors.last` | any | 8 (9–29) | 2704–2722 | 1 | 8 × 1 |

Dictionary scope: `alert_rules`. The saved dictionary is identical across jobs; both per-request preparation and worker reuse are eligible.

Declared methods: `contains_loop`, `preg_match`, `matcher`.

Method eligibility and task-specific details are recorded separately for each case in the linked JSON.

## [order-emails](suites/order-emails.json)

| Task / case ID | Operation | Keys (key bytes) | Document bytes | Matches | Jobs × documents/request |
|---|---|---:|---:|---:|---:|
| Render one order confirmation email<br>`order.email` | replace | 10 (13–20) | 820 | 11 | 8 × 1 |
| Render HTML and plain-text confirmation for one order<br>`order.email-pair` | replace | 10 (13–20) | 286–820 | 9–11 | 8 × 2 |

Dictionary scope: `one_order`. Values change per order; prepare a new Replacer for each job.

Declared methods: `strtr`, `preg_replace_callback`, `replacer`, `str_replace`.

Method eligibility and task-specific details are recorded separately for each case in the linked JSON.

## [tenant-text](suites/tenant-text.json)

| Task / case ID | Operation | Keys (key bytes) | Document bytes | Matches | Jobs × documents/request |
|---|---|---:|---:|---:|---:|
| Expand fixed tenant labels in one shop notice<br>`tenant.notice` | replace | 6 (9–17) | 147–213 | 2–4 | 8 × 1 |
| Publish eight different shop pages using one tenant configuration<br>`tenant.pages` | replace | 6 (9–17) | 147–213 | 2–4 | 1 × 8 |

Dictionary scope: `tenant_configuration`. The saved dictionary is identical across jobs; both per-request preparation and worker reuse are eligible.

Declared methods: `strtr`, `preg_replace_callback`, `replacer`, `str_replace`.

Method eligibility and task-specific details are recorded separately for each case in the linked JSON.

## [text-cleanup](suites/text-cleanup.json)

| Task / case ID | Operation | Keys (key bytes) | Document bytes | Matches | Jobs × documents/request |
|---|---|---:|---:|---:|---:|
| Leave ordinary ASCII customer text unchanged<br>`punctuation.clean` | replace | 8 (2–3) | 91–101 | 0 | 4 × 1 |
| Normalize quotes, dashes and spaces in imported customer text<br>`punctuation.mixed` | replace | 8 (2–3) | 129–166 | 2–6 | 8 × 1 |
| Replace four special space characters with ordinary spaces<br>`spaces.mixed` | replace | 4 (2–3) | 43–56 | 1–2 | 4 × 1 |

Dictionary scope: `import_rules`. The saved dictionary is identical across jobs; both per-request preparation and worker reuse are eligible.

Declared methods: `strtr`, `preg_replace_callback`, `replacer`, `str_replace`, `preg_replace`.

Method eligibility and task-specific details are recorded separately for each case in the linked JSON.

## [link-migration](suites/link-migration.json)

| Task / case ID | Operation | Keys (key bytes) | Document bytes | Matches | Jobs × documents/request |
|---|---|---:|---:|---:|---:|
| Check already-migrated content for old literal links<br>`links.clean` | replace | 8 (23–36) | 76–120 | 0 | 2 × 1 |
| Rewrite known legacy links in one content page<br>`links.page` | replace | 8 (23–36) | 132–214 | 1–2 | 8 × 1 |
| Migrate eight different content pages with the same URL rules<br>`links.batch` | replace | 8 (23–36) | 132–214 | 1–2 | 1 × 8 |

Dictionary scope: `migration_rules`. The saved dictionary is identical across jobs; both per-request preparation and worker reuse are eligible.

Declared methods: `strtr`, `preg_replace_callback`, `replacer`, `str_replace`.

Method eligibility and task-specific details are recorded separately for each case in the linked JSON.

## [secret-redaction](suites/secret-redaction.json)

| Task / case ID | Operation | Keys (key bytes) | Document bytes | Matches | Jobs × documents/request |
|---|---|---:|---:|---:|---:|
| Mask registered secrets in a log excerpt with no leaked token<br>`secrets.clean` | replace | 24 (40–50) | 5367–5388 | 0 | 4 × 1 |
| Mask one registered secret in a request log excerpt<br>`secrets.one` | replace | 24 (40–50) | 5442–5468 | 1 | 4 × 1 |
| Mask three registered secrets in an incident log excerpt<br>`secrets.three` | replace | 24 (40–50) | 8245–8293 | 3 | 4 × 1 |
| Mask three registered secrets in a larger incident log batch<br>`secrets.incident-batch` | replace | 24 (40–50) | 64741–64786 | 3 | 4 × 1 |

Dictionary scope: `deployment_secret_registry`. The saved dictionary is identical across jobs; both per-request preparation and worker reuse are eligible.

Declared methods: `strtr`, `preg_replace_callback`, `replacer`, `str_replace`, `preg_replace`.

Method eligibility and task-specific details are recorded separately for each case in the linked JSON.

## [chat-formatting](suites/chat-formatting.json)

| Task / case ID | Operation | Keys (key bytes) | Document bytes | Matches | Jobs × documents/request |
|---|---|---:|---:|---:|---:|
| Check plain support replies for configured emoticons<br>`chat.plain` | replace | 12 (2–5) | 61–73 | 0 | 4 × 1 |
| Render configured emoticons in short customer replies<br>`chat.emoticons` | replace | 12 (2–5) | 67–82 | 1 | 8 × 1 |

Dictionary scope: `chat_format_rules`. The saved dictionary is identical across jobs; both per-request preparation and worker reuse are eligible.

Declared methods: `strtr`, `preg_replace_callback`, `replacer`, `str_replace`.

Method eligibility and task-specific details are recorded separately for each case in the linked JSON.

## [help-index](suites/help-index.json)

| Task / case ID | Operation | Keys (key bytes) | Document bytes | Matches | Jobs × documents/request |
|---|---|---:|---:|---:|---:|
| List the configured support topics mentioned in a help article<br>`help.unique` | unique | 96 (3–25) | 397–465 | 14–19 | 8 × 1 |
| Count all configured term occurrences in a help article<br>`help.count` | count | 96 (3–25) | 397–465 | 18–22 | 8 × 1 |
| Locate all configured term occurrences for a search index<br>`help.all` | all | 96 (3–25) | 397–465 | 18–22 | 8 × 1 |

Dictionary scope: `glossary_version`. The saved dictionary is identical across jobs; both per-request preparation and worker reuse are eligible.

Declared methods: `strpos_unique`, `preg_each_unique`, `matcher`, `strpos_count`, `preg_each_count`, `strpos_all`, `preg_each_all`.

Method eligibility and task-specific details are recorded separately for each case in the linked JSON.

## [help-linking](suites/help-linking.json)

| Task / case ID | Operation | Keys (key bytes) | Document bytes | Matches | Jobs × documents/request |
|---|---|---:|---:|---:|---:|
| Link configured support terms in one plain-text help article<br>`help.link-one` | replace | 96 (3–25) | 397–465 | 12–16 | 8 × 1 |
| Publish eight different help articles using one link glossary<br>`help.link-batch` | replace | 96 (3–25) | 397–465 | 12–16 | 1 × 8 |

Dictionary scope: `glossary_version`. The saved dictionary is identical across jobs; both per-request preparation and worker reuse are eligible.

Declared methods: `strtr`, `preg_replace_callback`, `replacer`.

Method eligibility and task-specific details are recorded separately for each case in the linked JSON.

## [synthetic](suites/synthetic.json)

| Task / case ID | Operation | Keys (key bytes) | Document bytes | Matches | Jobs × documents/request |
|---|---|---:|---:|---:|---:|
| Synthetic control: 64 literals sharing a long prefix<br>`control.prefix` | replace | 64 (49) | 157 | 2 | 1 × 1 |
| Synthetic control: 64 literals sharing a long suffix<br>`control.suffix` | replace | 64 (49) | 157 | 2 | 1 × 1 |
| Synthetic control: nested repeated-byte literals<br>`control.overlaps` | replace | 16 (1–16) | 160 | 10 | 1 × 1 |
| Correctness control: regex punctuation and literal replacement bytes<br>`control.escaping` | replace | 4 (3–4) | 51 | 4 | 1 × 1 |

Dictionary scope: `control`. The saved dictionary is identical across jobs; both per-request preparation and worker reuse are eligible.

Declared methods: `strtr`, `preg_replace_callback`, `replacer`, `preg_replace`.

Method eligibility and task-specific details are recorded separately for each case in the linked JSON.
