Product substring-search corpus

Generate: python3 corpus/substr-product/generate.py
Without downloaded documents: python3 corpus/substr-product/generate.py --owned-only
Validate: <php> -n corpus/substr-product/verify.php
Measure: bench run substr-product --a <base> --b <candidate> --perf
Missing generated inputs are skipped, like corpus/real. cases.json is the owned suite
catalog, without downloaded document contents. Set SUBSTR_PRODUCT_CORPUS to use another
generated directory. After changing the scenarios, refresh the catalog with:
python3 corpus/substr-product/generate.py --catalog corpus/substr-product/cases.json

This is a deterministic set of application scenarios, not a production traffic trace.
There are no inferred popularity percentages and no application-wide weighted score.
The original synthetic/adversarial substr-search cases are not part of this suite.

Inputs and ground truth

texts.json contains owned, hand-written product/order/support messages in English,
Spanish, Russian, Arabic, Hindi, Chinese, Japanese, Korean and mixed English/emoji.
The same operations, sizes and hit states are used for every language. Longer bodies
combine complete messages in seeded order with varied order identifiers; these are
constructed natural-language fixtures, not captured user posts.

Other constructed fixtures model unquoted field exports, HTTP requests, URL queries,
transactional email templates and JSON-lines payment logs. Public HTML/Markdown/JS
snapshots are reused from corpus/real, with source hashes recorded. C source comes
from the pinned baseline commit. Source/license information is in each input entry
and corpus/real/README.md. Do not commit generated public-document snapshots.

generated/ contains 141 frozen UTF-8 inputs and a manifest of 233 operations.
The --owned-only mode omits the six public-document inputs and their twelve operations;
it preserves every owned input and expression, including all 76 primary cases.
The generator uses Python bytes/string search, split and replacement to produce
expected.json independently of Zend. verify.php checks input hashes and exact results.
Regeneration with the same inputs/seed is checked byte-for-byte. Expected outputs are
kept outside manifest.json so benchmark setup does not parse large result arrays.

Cases

* Moderation: 12 literal terms with short-circuiting, on comment (~256 B), post (~1 KB)
  and long thread (~64 KB). Clean text checks all terms; early hit checks one term;
  late hit checks the last term and finds it at the end. Four example blocked domains
  supplement eight local terms. Text is already normalized to lower case. This models
  literal substring policies; Unicode normalization, case folding, word boundaries,
  tokenization and stemming are deliberately outside the measured operation.
* Single-word misses use the same clean text and isolate the search call from the loop.
* explode: ||, ::, CRLF, comma, tab and ampersand. Varied real-looking fields; short,
  4 KB, 64 KB, 1 MB and no-separator cases. One-character delimiters are controls.
  The 1 MB cases are bulk/export guards, not ordinary request sizes. Also limit=2,
  substr_count and str_replace for the multi-byte delimiters.
* Whole parsers: unquoted || records; form-urlencoded queries, retaining repeated keys;
  HTTP headers (including a large Cookie, body after headers, and incomplete request);
  template-slot scanning; selecting error lines from payment logs. Allocation and PHP
  loops are measured. The record scanner is not a general quoted CSV parser.
* Template rendering uses str_replace with four placeholders. HTML checks look for a
  present href and an absent optional widget attribute.
* Payment log scans cover absent/early/late payment_failed and level:error markers.
  Common prefixes such as payment_created/authorized/captured occur naturally here.
* Source/document scans cover present and absent identifiers, TODO, fenced Markdown,
  JavaScript tokens and optional HTML attributes on existing public snapshots.

Size/position interpretation

Reported bytes are actual input bytes, not necessarily bytes examined: for example,
an HTTP parser stops at the header terminator even with a 64 KB body, and an early
moderation hit stops before later terms. Large queries and 1 MB delimiter files are
explicit guards. Complete messages/records are retained, so nominal sizes may differ
slightly from actual sizes. Short public documents are not repeated to fill 64 KB.

Timing

The reusable suite measures actual PHP calls with their allocations and interpreter
work, using the existing runner. Corpus creation, normalization and ground-truth checks
are outside the timed loop. Inputs are read lazily for the selected cases. No PHP source
or benchmark runner changes are necessary. Bench compares hashes of inputs and results
in addition to verify.php. Never interpret a corpus median as average application speed.
