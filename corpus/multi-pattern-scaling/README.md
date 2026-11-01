# Dictionary-size series: moderation, search and replacement

This is a controlled extension of the [product corpus](../multi-pattern-product/README.md).
It measures exactly **8, 16, 32, 64, 128, 256 and 512 distinct literal strings**.
Each application task keeps the same documents at every size. The original product
series remains unchanged; its EN/RU/ZH results are separate from this English series.

## Tasks

| Task | Dictionary | Documents | Output |
|---|---|---|---|
| Moderate short comments | Nested literal moderation policies | Eight independent comments, separately absent/start/middle/end variants | Boolean: any occurrence |
| Moderate detailed support messages | The same policies | Three separately authored messages, absent or with a quoted term | Boolean: any occurrence |
| Search support articles | Nested commerce/support glossary | Eight different saved help articles | Distinct keys, count of all overlaps, or all byte locations; separate cases |
| Link support terms | The same glossary mapped to links | One article or one publishing job containing eight different articles | Leftmost-longest replacement, without rescanning inserted links |

Input JSON files contain complete texts, dictionaries, expected outputs and facts.
Sizes, match counts, offsets and dictionary ranks are inspectable per document.
The [inventory](CASES.md) lists every configuration. No input text is padded or
randomly generated to reach a target size.

### Moderation dictionary

[moderation-words.json](moderation-words.json) contains 512 strings derived from
[David Sojevic's profanity list](https://github.com/dsojevic/profanity-list), under
the included [MIT license](LICENSE-profanity-list.txt). Its metadata pins the
source revision, file hash and extraction rule. Eight common canonical forms are
followed by plain literal alternatives, excluding wildcard/regex entries. The
remaining order is deterministic. We do not implement the source library's
exceptions, wildcards, case folding or word boundaries: this series measures
literal byte matching, not the effectiveness of a profanity classifier.

The key sets are nested. The same eight core terms are spread across dictionary
positions at every size, so successful `str_contains()` loops do not always stop
within the first eight entries of a 512-entry dictionary. Dictionary order is
fixed within each case and saved in JSON. The authored negative comments/messages
are checked against the full 512-key policy before selecting the saved clean
examples. Positive texts quote the same terms at every size.

### Support dictionary

[support-terms.json](support-terms.json) contains 512 authored commerce/support
terms. The first 96 preserve the product corpus glossary. Larger dictionaries add
ordinary payment, delivery, returns, account, accessibility and related terms;
there are no serial-number keys or random ASCII fillers. Smaller configurations
are nested prefixes of this saved list.

A growing dictionary may find additional terms in the unchanged articles.
Expected outputs and match counts therefore vary; the input text does not.
This is an application-shaped size experiment, not a pure isolation of keyword
count or a production frequency distribution. Its crossover cannot be assumed
for another dictionary or workload.

## Lifecycles and checks

Both preparation per job and already prepared dictionaries are eligible: every
configuration has a fixed dictionary across its saved jobs. The one-article and
eight-article replacements distinguish actual batching from indefinite reuse.
PCRE callbacks are used for map values; sequential `str_replace()` is excluded
because these links contain matching terms. Original product cases retain the
direct `preg_replace()` comparison for constant replacements.

Two copied product cases are marked `control` and used to keep A/A checks the same
as in the original series. They are excluded from the size tables.

From the repository root:

```sh
python3 corpus/multi-pattern-scaling/generate.py --check
php -n corpus/multi-pattern-product/verify.php --no-extension \
  --corpus corpus/multi-pattern-scaling
```

Run the verifier with the current prototype loaded too, before measuring. The
existing [measurement driver](../../reports/multi-pattern-search/measure.py)
accepts `--corpus` pointing here and uses the same timing/counter protocol.

The `index.json` manifest is the frozen input snapshot from fixture generation. Its
export-time status is preserved to keep the measured input hash reproducible;
current measurement status is in the linked report.
