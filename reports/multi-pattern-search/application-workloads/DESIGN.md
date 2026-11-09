# Corpus, selection and measurement boundaries

The corpus was fixed before primary timing. [corpus.json](corpus.json) records
every source, subject, ordered dictionary, expected output and batch member.
[SOURCE](SOURCE.md) provides licenses, revisions and build identities.
`sources.candidate.json` retains the acquisition audit; it is not the final inventory.

## Short texts: presence and unique matched keys

The source is Civil Comments, with the complete English LDNOOBW dictionary:
403 unique entries, 2–27 bytes per key. The task is ASCII-insensitive literal
substring detection, not word-boundary matching or toxicity classification.

The acquired pool contains 256 comments: eight evenly spaced windows of 32 rows
from the 97,320-row test split. Offsets are saved in the corpus. Original text,
source row IDs and SHA-256 hashes are retained. Toxicity labels were not used.

Selection is deterministic, using seed `strmatch-application-v1` and the SHA-256
of the seed, a NUL byte and the row identity:

- Sort distinct comments by byte length, with identity as the tie-breaker.
- Divide them into four equal groups; select the four lowest hashes per group.
- For batches, select the 64 lowest hashes from the full distinct pool.

This gives 16 individual subjects, all included among the 64 batch subjects.
Duplicates are checked after ASCII folding; the duplicate ledger is saved.
Selection does not depend on matches or timing. Texts are not padded and matches
are not inserted. The dictionary retains source order after ASCII folding and
deduplication; it is not reordered for a particular subject.

Matcher receives `strtolower($subject)` inside the timed operation. Standard PHP
uses a `stripos()` loop or `strtolower()` plus `strpos()`; PCRE uses `/i` without
`/u`, in locale `C`. Each implementation is checked against an explicit
ASCII-folding oracle. These checks do not establish Unicode case-insensitivity.

## Complete texts: search and literal rewriting

Sixteen complete CPython 2.7 documentation files retain their original
reStructuredText bytes. The dictionary is the existing 48-entry `MAPPING` from
`Lib/lib2to3/fixes/fix_imports.py`, extracted without executing the fixer.
Keys are 3–18 ASCII bytes; mapping order and replacement values are preserved.
The corpus lists every file and its source identity.

Each text is measured separately for unique matched keys, total overlapping
occurrences, all occurrences with byte offsets, and literal replacement. All four
operations use the same subject and dictionary. No occurrences are added.

Search is case-sensitive. Replacement selects the leftmost non-overlapping
occurrence, preferring the longest key at a shared start, and does not rescan
inserted values. This historical mapping supplies real rules; it does not make
literal rewriting a semantic migration tool. Keys can match inside prose and
identifiers.

## Email templates: replacement values change between messages

Groundmail supplies 12 template families, each in HTML and plain text: 24 inputs.
The original files are unchanged. Related HTML/text versions and shared styling
are correlations, not independent application sources.

Literal keys are the templates' existing `{{name}}` placeholders. Replacement
values are deterministic fixtures saved in each case; some are generated from
variable names. Values arrive ready for substitution. Escaping and delivery are
outside the measured operation.

HTML and text versions have separate measurements. Only one-shot Replacer is
measured: changing values requires a new object, even when placeholder names
stay the same. A prepared call with unchanged values would measure another task.

## Equivalent PHP and PCRE implementations

| Operation | Standard PHP | PCRE |
|---|---|---|
| Presence | `stripos()` loop; folded `strpos()` loop | Literal alternatives, with and without shared-prefix factoring |
| Unique keys | First occurrence per key, then ordering | Lookahead groups, deduplication and ordering |
| Count | Repeated `strpos()`, advancing one byte after each start | Lookahead groups and summed counts |
| All occurrences | Repeated `strpos()` and ordered arrays | Lookahead groups and ordered arrays |
| Replacement | `strtr()`; eligible `str_replace()` | Longest-first literal alternatives, with and without prefix factoring |
| Placeholders | `strtr()`; eligible `str_replace()` | Literal alternatives and a token recognizer with dictionary lookup |

Lookahead groups contain keys of equal byte length, preserving overlapping and
nested occurrences. ASCII-insensitive searches return canonical dictionary
entries. Replacement callbacks insert values literally; the token recipe also
preserves unknown placeholders. [harness.php](harness.php) contains every recipe.

The independent Python oracle searches each key separately, advancing one byte
after each hit, and independently selects leftmost-longest replacements. Every included
implementation must match the expected content and order. `MatchResult` objects
are converted to arrays only during checks, outside timing. Sequential
`str_replace()` is eligible only when it produces the oracle's output. Batch
eligibility requires equivalence on every member.

## What the timer includes

| Mode | Measured interval |
|---|---|
| Prepared | Required per-subject preprocessing, method call, result consumption and release |
| One-shot | Object construction, the same operation and result release, then object destruction |
| Batch | Construction once, operations on all B distinct subjects, release after each, then destruction |

Existing functions receive prebuilt arguments, callbacks and regex source strings
and use warm compiled-pattern caches. Their own processing and result creation
are timed. File/network I/O, JSON loading, regex preparation and correctness
normalization are excluded. `replace($subject)` omits the optional count argument.

Batches use prefixes of one saved deterministic order. Comment batches contain
1, 4, 16 or 64 distinct subjects; document batches contain 1, 4 or 16. Every batch
is measured directly, including B=1. Reported values are batch totals, not the
sum of separate constructor and query measurements.

## Task and comparison counts

| Input set | Tasks | Object lifetimes | Timing comparisons |
|---|---:|---|---:|
| 16 comments × 2 operations | 32 | Prepared and one-shot | 64 |
| 16 complete texts × 3 search operations | 48 | Prepared and one-shot | 96 |
| 16 complete texts × replacement | 16 | Prepared and one-shot | 32 |
| 24 email inputs | 24 | One-shot | 24 |
| Different-document batches | 20 | Construction once per batch | 20 |
| Total | 140 | | 236 |

Performance samples use GCC 14.2 on the Intel Core i7-13700H laptop. Four release
builds passed correctness checks before the GCC-14-only measurement decision;
they are not four performance series. The initial GCC 13 pilot and AMD samples
are excluded.

Each comparison contains the native operation, eligible alternatives and an A/A
control. Sampling, retries, hardware counters and quality thresholds are in
[SOURCE](SOURCE.md) and [QUALITY](QUALITY.md). Fresh-process allocator measurements
separate retained object memory, constructor peak and method peak; inputs are
excluded and peaks must not be added.

## Interpretation

The summary uses one displayed reference time from the one-shot series for both
object columns. Relative changes use that reference median. Full paired sample
statistics and every implementation remain available separately.

These tests repeat fixed subjects or fixed batches with warm caches. They do not
sample production request frequencies, measure whole applications, or establish
universal thresholds. Different natural texts vary in more than length, so a
performance difference between them does not isolate the effect of text size.
