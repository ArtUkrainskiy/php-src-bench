# Product corpus for Str\Matcher and Str\Replacer

This corpus models ordinary application tasks that use a fixed set of literal strings. It is intended to show when a prepared dictionary is useful and what preparation costs, alongside existing PHP functions and PCRE. It does not assume that Replacer should replace `strtr()`.

**Inputs and correctness verified.** The completed measurements are in the [report](../../reports/multi-pattern-search/README.md). There are 43 product scenarios in 10 suites and 4 separate synthetic/correctness controls. The saved jobs contain 292 document instances across 263 jobs. Variants deliberately reuse some documents to compare operations and match positions; these are not 292 independent production samples.

## Representative tasks

The table selects 26 product scenarios; the [complete inventory](CASES.md) lists all 47 scenarios. Each task links to the actual saved inputs, dictionaries and expected results. Sizes are UTF-8 bytes per document, not character counts. A request processes all documents in one saved job.

For replacement tasks, **matches** means selected, non-overlapping replacements. For unique-key tasks, it means distinct matching keys; for other search tasks it means all literal occurrences, including nested terms. The JSON also records distinct keys, the first match offset, dictionary rank, replaced source bytes and output size where applicable.

| Task | Keys | Document bytes | Matches | Documents/request |
|---|---:|---:|---:|---:|
| [Flag a short EN comment: no configured phrase](suites/moderation.json) | 12 | 56–84 | 0 | 1 |
| [Flag a short EN comment: phrase at the start](suites/moderation.json) | 12 | 101–148 | 1 | 1 |
| [Flag a short EN comment: phrase inside the message](suites/moderation.json) | 12 | 160–212 | 1 | 1 |
| [Flag a short EN comment: phrase at the end](suites/moderation.json) | 12 | 108–155 | 1 | 1 |
| [Flag a short RU comment: no configured phrase](suites/moderation.json) | 12 | 111–160 | 0 | 1 |
| [Flag a short RU comment: phrase inside the message](suites/moderation.json) | 12 | 314–382 | 1 | 1 |
| [Flag a short ZH comment: no configured phrase](suites/moderation.json) | 12 | 42–78 | 0 | 1 |
| [Flag a short ZH comment: phrase inside the message](suites/moderation.json) | 12 | 147–204 | 1 | 1 |
| [Check a detailed EN support message: a promotional phrase is quoted](suites/moderation.json) | 12 | 807–852 | 1 | 1 |
| [Check a detailed RU support message: a promotional phrase is quoted](suites/moderation.json) | 12 | 1270–1511 | 1 | 1 |
| [Check a detailed ZH support message: a promotional phrase is quoted](suites/moderation.json) | 12 | 734–839 | 1 | 1 |
| [Decide whether a request trace needs an alert: healthy trace](suites/error-routing.json) | 8 | 2679–2704 | 0 | 1 |
| [Decide whether a request trace needs an alert: error in the last record](suites/error-routing.json) | 8 | 2704–2722 | 1 | 1 |
| [Render one order confirmation email](suites/order-emails.json) | 10 | 820 | 11 | 1 |
| [Render HTML and plain-text confirmation for one order](suites/order-emails.json) | 10 | 286–820 | 9–11 | 2 |
| [Publish eight different shop pages using one tenant configuration](suites/tenant-text.json) | 6 | 147–213 | 2–4 | 8 |
| [Normalize quotes, dashes and spaces in imported customer text](suites/text-cleanup.json) | 8 | 129–166 | 2–6 | 1 |
| [Replace four special space characters with ordinary spaces](suites/text-cleanup.json) | 4 | 43–56 | 1–2 | 1 |
| [Migrate eight different content pages with the same URL rules](suites/link-migration.json) | 8 | 132–214 | 1–2 | 8 |
| [Mask registered secrets in a log excerpt with no leaked token](suites/secret-redaction.json) | 24 | 5367–5388 | 0 | 1 |
| [Mask one registered secret in a request log excerpt](suites/secret-redaction.json) | 24 | 5442–5468 | 1 | 1 |
| [Mask three registered secrets in an incident log excerpt](suites/secret-redaction.json) | 24 | 8245–8293 | 3 | 1 |
| [Mask three registered secrets in a larger incident log batch](suites/secret-redaction.json) | 24 | 64741–64786 | 3 | 1 |
| [Render configured emoticons in short customer replies](suites/chat-formatting.json) | 12 | 67–82 | 1 | 1 |
| [List the configured support topics mentioned in a help article](suites/help-index.json) | 96 | 397–465 | 14–19 | 1 |
| [Publish eight different help articles using one link glossary](suites/help-linking.json) | 96 | 397–465 | 12–16 | 8 |

All early, middle, late and absent variants remain in the full inventory. Synthetic controls are excluded from this table.

## What the suites contain

| Suite | Scenarios | Input and operation |
|---|---:|---|
| [Moderation](suites/moderation.json) | 18 | EN/RU/ZH comments and separately authored multi-paragraph support messages. Twelve configured terms/domains; absent or quoted at different positions. Literal prefilter, not semantic moderation. |
| [Error routing](suites/error-routing.json) | 4 | Sixteen different NDJSON trace records and eight known failure markers. No marker or one marker in the first, middle or final record. |
| [Order emails](suites/order-emails.json) | 2 | Ten order-specific placeholders, either one HTML email or HTML plus plain text. Eight orders with different values. |
| [Tenant text](suites/tenant-text.json) | 2 | Six tenant-wide substitutions across eight distinct notices/page fragments, individually or in a publishing batch. |
| [Text cleanup](suites/text-cleanup.json) | 3 | Eight literal punctuation substitutions or four Unicode spaces mapped to ASCII space. Clean and affected input; not general Unicode normalization. |
| [Link migration](suites/link-migration.json) | 3 | Eight old URL rules, including overlapping prefixes; already migrated pages, affected pages and a publishing batch. No URL parsing. |
| [Secret redaction](suites/secret-redaction.json) | 4 | Twenty-four registered fake tokens. Varied NDJSON records with zero, one or three leaks in approximately 5, 8 or 65 KB. Exact known-token masking, not arbitrary email/credential detection. |
| [Chat formatting](suites/chat-formatting.json) | 2 | Twelve literal emoticons in short customer replies, with and without matches. Longest-match selection matters for `:))` and `:)`. |
| [Help indexing](suites/help-index.json) | 3 | Ninety-six support terms in eight separately written FAQ articles. Unique topics, overlapping occurrence counts and all byte locations are separate tasks. |
| [Help linking](suites/help-linking.json) | 2 | The same glossary maps terms to links, in one article or eight distinct articles. Inserted links must not be searched again. |
| [Synthetic controls](suites/synthetic.json) | 4 | Long common prefixes, long common suffixes, nested repeated-byte keys and regex/replacement escaping. Kept separate from product conclusions. |

## Equivalent alternatives

| Task | Alternatives |
|---|---|
| Any configured literal present | Early-exit `str_contains()` loop, one escaped `preg_match()` alternation, `Matcher::matches()` |
| Different replacement per key | `strtr()`, escaped longest-first `preg_replace_callback()` with a map lookup, `Replacer::replace()` |
| Same replacement for every key | Also direct `preg_replace()` without a callback; used for spaces, known-token redaction and eligible controls |
| Unique matching keys | First `strpos()` per key, first literal `preg_match()` per key, `Matcher::getMatchedKeywords()` |
| All overlapping occurrences/counts | Repeated `strpos()` per key, PCRE lookahead per key, `Matcher::matchAll()` / `countMatches()` |

`str_replace()` is included only in cases where a longest-first sequential pass agrees on every saved input. It is excluded from help autolinking: rescanning inserted links changes the result. Agreement on these saved inputs is not a claim of general equivalence.

Keys are escaped for PCRE; replacements containing `$` or backslashes are returned through a callback. Direct `preg_replace()` is restricted here to one plain literal replacement. For nested glossary terms, a single ordinary regex alternation would discard same-start matches, so the overlap-preserving baseline searches each literal independently. That baseline is a transparent reference, not a claim that it is the fastest possible PCRE implementation.

Everything uses exact case-sensitive byte matching. There is no `/u`, case folding, word-boundary logic, normalization, parsing, I/O or HTML escaping in the measured operation. Offset units are bytes in every implementation.

## Dictionary lifetime and measurements

Each JSON case records its dictionary scope and eligible lifecycle modes:

- **Complete request:** prepare the dictionary/pattern, process all documents in that job, and release request-owned prepared state. Report elapsed time per request and the number of documents processed.
- **Worker reuse:** retain the same prepared dictionary across different documents/jobs. Only cases with an identical dictionary across jobs permit this mode. Report processing time separately from preparation and retained memory.
- **Order emails:** replacement values change for every order. A Replacer must be rebuilt per order. The HTML/plain-text pair legitimately shares one object within that order; it cannot share that object across unrelated orders. PCRE can still reuse its compiled pattern when only replacement values change.

The report distinguishes an already cached PCRE pattern from compilation in a fresh process, with JIT configuration recorded. Reconstructing a pattern string does not make its compiled form cold. Pattern construction and sorting belong to preparation; they must not silently be charged to only one implementation.

The primary comparison is elapsed time for an equivalent complete task, with cycles/instructions as supporting data. Preparation time, memory, one-document use and genuine batch/worker reuse must remain visible. Synthetic results and small regressions must be reported separately, without pooling all methods/lifecycles into an unexplained percentage or declaring a universal winner.

## Inspect and validate

The suite JSON files are the actual inputs. Every job contains its literal `dictionary` and a list of `documents`, each with `text`, `expected` and `facts`. No text is generated on the fly by the timed loop. Load JSON and validate outputs before timing; parsing, correctness checks and fixture generation are outside the measured task.

The data are project-authored application models, not captured production traffic. Short moderation seeds come from the repository's existing substring corpus; [moderation-seed.json](moderation-seed.json) records the source hash and separately identifies the newly authored detailed posts. Log records are deterministically authored from varied event types, timestamps and request IDs; they are not a repeated line padded to a target byte count. Names, domains and tokens are fictional.

```sh
python3 corpus/multi-pattern-product/generate.py --check
php -n corpus/multi-pattern-product/verify.php --no-extension
"$PHP_BUILD/sapi/cli/php" -n -d "extension=$SMOKE_OUTPUT/strmatch.so" \
  corpus/multi-pattern-product/verify.php
```

Run these commands from the repository root. Set `PHP_BUILD` and `SMOKE_OUTPUT`
using the report’s reproduction recipe. For the size corpus add
`--corpus corpus/multi-pattern-scaling`. Without the explicit module load the
verifier checks only the native/PCRE alternatives. To edit fixtures, change the generator/seed, run `generate.py`, inspect the resulting JSON diff, then validate again. `index.json` records suite hashes and an inventory; `generate.py --check` checks deterministic regeneration byte for byte. Expected results use an independent Python byte-based search/replacement oracle. The PHP verifier checks the results, input facts and replacement counts against native PHP, PCRE and the current prototype.

[workloads.php](workloads.php) contains correctness adapters, **not a timed harness**. For example, it normalizes MatchResult objects for comparison and constructs per-key PCRE patterns in some adapters. The timed harness has separate recipes and keeps those verification costs outside timing.

The corpus covers small and medium dictionaries (4–96 keys) and ordinary bounded texts. It does not establish behavior for huge dictionaries, arbitrary regexes, Unicode-aware linguistic processing, streaming or untrusted HTML. Additional scaling tests would be separate controls rather than evidence about the frequency of these product tasks.

The `index.json` manifest is the frozen input snapshot from fixture generation. Its
export-time status is preserved to keep the measured input hash reproducible;
current measurement status is in the linked report.
