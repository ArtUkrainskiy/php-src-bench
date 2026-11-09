# Prepared literal search and replacement

A study of `Str\Matcher` / `Str\Replacer`: when preparing a dictionary pays off compared with existing PHP and PCRE tools. [PR #25122](https://github.com/php/php-src/pull/25122) · [Measured code and builds](benchmark/SOURCE.md). The measured extension source matches [commit 7c7550bcdac](https://github.com/php/php-src/commit/7c7550bcdac2091e5f9c256e3f203f82d7db448f).

Additional studies use GCC 14.2 on an Intel Core i7-13700H, independently of the AMD measurements below:

- [Application workloads](application-workloads/README.md): unchanged open-data texts, literal dictionaries, email substitution and reuse across different documents.
- [Break-even study](break-even/README.md): one-shot calls at different text lengths and prepared calls on 128 B–4 KiB texts with 8, 16, 32 and 48 keys. Replacer performs one replacement per input in this controlled series.

## Methods and comparisons

| Method | What the method returns | Existing PHP method | PCRE method |
|---|---|---|---|
| `Matcher::matches()` | `bool`: whether the text contains at least one key | A `str_contains()` loop with early exit | `preg_match()` |
| `Matcher::getMatchedKeywords()` | An array of unique matched keys, ordered by their first occurrence; ties at the same start are ordered by increasing length | `strpos()` for each key, with ordered results | `preg_match_all()` and selection of unique keys |
| `Matcher::countMatches()` | `int`: the number of all occurrences, including overlaps | Repeated `strpos()` calls, advancing the offset by 1 | `preg_match_all()`, counting occurrences |
| `Matcher::matchAll()` | An array of `MatchResult` objects for all occurrences: key, byte offset and byte length. Overlaps are preserved; results are ordered by offset, then by increasing length | Repeated `strpos()` calls, with ordered results | `preg_match_all()` and ordering of results |
| `Replacer::replace()` | A string with replacements applied from left to right. At the same start, the longest key is selected; processing continues after it. Inserted text is not searched again | `strtr()`; `str_replace()` where the result is equivalent | Longest first: `preg_replace_callback()`; direct `preg_replace()` for a single replacement value |

A key is a string to search for. Searching is case-sensitive and byte-oriented. Matcher includes overlapping occurrences; Replacer selects non-overlapping replacements. To count and enumerate overlaps, PCRE uses lookahead expressions with keys grouped by byte length.

Results have been checked against a reference and are equivalent in content. `matchAll()` returns `MatchResult` objects, while existing methods return arrays. Result creation and release are included in the measurement; converting objects to arrays for verification is not. `str_replace()` and specialized PCRE expressions are included only where they produce an equivalent result.

## Main findings

- On controlled texts with 128 keys and one occurrence, one-shot `getMatchedKeywords()`, `countMatches()` and `matchAll()`, including object construction, are slower than the alternatives at 128 B and 1 KiB. An advantage is observed on the tested texts of 4 KiB and above. The exact break-even point between the tested sizes has not been determined.
- Having a prepared Matcher does not guarantee a speedup: with eight keys, a `strpos()` loop can be faster even on a 64 KiB text. The result depends on both the number of keys and the number of returned results.
- A `str_contains()` loop checks keys in sequence, so its time depends on dictionary order. `Matcher::matches()` reads the text from left to right and stops as soon as it has read the last byte of any matched key; it does not iterate through the dictionary key by key.
- With 32 keys on a 4 KiB text, a prepared Replacer is faster than PCRE, while a one-shot call is slower. On a 16 KiB text with the same 32 keys, the one-shot operation is faster; with 16 keys, the result also depends on key lengths and the compiler. The case below with 16 keys of 11–21 B loses in one-shot use.
- A single key, a recognizable `{{…}}` format and replacing all matched keys with one marker are examples where existing tools are substantially faster than a prepared Replacer.
- On a 1 MiB text with 10000 keys of 8–24 B and 10000 replacements, `Replacer::replace()`, including object construction and destruction, is approximately twice as fast as `strtr()`.
- The findings and tables below describe the saved AMD inputs. The Intel studies above provide separate evidence; results are not pooled across machines. They do not establish a universal key-count threshold or estimate the speedup of PHP applications.

**Prepared object** means calling the method, using the result and releasing it. **One-shot** means object construction, one call, result release and object destruction, measured together. Existing tools use prepared arguments and a warm PCRE cache. This is not a full HTTP request measurement.

AMD Ryzen 9 5950X, Linux x86-64; GCC 15.2 / Clang 21.1. For each compiler, Matcher and Replacer were measured using the same extension module. These are separate runs, not one combined series; exact hashes and parameters are in [SOURCE](benchmark/SOURCE.md).

The tables below show GCC 15.2; Clang 21.1 results for the same inputs are available in the appendices. Parentheses show the median paired change relative to the fastest eligible existing method. Large slowdowns are shown as multiples derived from the same paired ratios. A negative value means less time. Prepared Matcher calls and one-shot calls were measured separately, each alongside existing methods. The table shows the existing method's time from the one-shot measurement. The prepared Matcher percentage therefore cannot be reproduced exactly from the adjacent numbers.

We do not call a difference below 2% a win or a loss; this is a reporting rule, not an estimate of measurement error. † marks a quality issue. The observed time and relative change are shown, with the actual spread and A/A deviation in the quality register.

In the full Clang tables, 11 prepared-object comparisons and 13 one-shot comparisons did not pass the quality checks — out of 135 inputs in each mode. Only one comparison exceeded the A/A threshold. Results marked † retain their observed percentages or multiples; the quality register quantifies the issue. [Reasons and affected inputs](benchmark/QUALITY.md).

## `Matcher::matches()`: no match, or a match near the start, middle or end of the text

A 4 KiB text and a dictionary of 128 keys, each 12 B long. In positive variants, one key occurs; it is key #65 in dictionary order. Its starting byte in the text changes: 8, 2042 or 4076. A separate variant contains no matches.

| Test condition | Best existing method, µs | Prepared object, µs | One-shot, µs |
|---|---|---:|---:|
| [No matches](benchmark/inputs/cases/any/presence.any.bytes4096.keys128.absent.rank65.json) | `preg_match()`<br>100.021 | 3.817 (-96.18%) | 58.107 (-42.02%) |
| [Match: byte 8](benchmark/inputs/cases/any/presence.any.bytes4096.keys128.start.rank65.json) | `preg_match()`<br>0.414 | 0.116 (-71.84%)† | 52.787 (127.4 times slower) |
| [Match: byte 2042](benchmark/inputs/cases/any/presence.any.bytes4096.keys128.middle.rank65.json) | `preg_match()`<br>51.972 | 1.986 (-96.17%) | 54.966 (+5.90%) |
| [Match: byte 4076](benchmark/inputs/cases/any/presence.any.bytes4096.keys128.end.rank65.json) | `str_contains()` loop<br>60.558 | 3.814 (-93.66%) | 57.599 (-4.94%) |

[Other sizes, dictionaries, Clang and raw samples](benchmark/matcher.md). In a separate control with [32 keys and a match with the first dictionary key](benchmark/inputs/cases/any/fixed_rank.any.bytes4096.keys32.end.rank1.json), the PHP loop makes one `str_contains()` call.

## `getMatchedKeywords()`, `countMatches()` and `matchAll()`

The dictionary contains 128 keys, each 12 B long. The main series has one occurrence; rows of the same size use identical texts and ordered dictionaries. `getMatchedKeywords()` returns one unique key, `countMatches()` returns the number 1, and `matchAll()` returns one result with an offset. An additional `matchAll()` row uses 64 KiB with the same dictionary and 64 occurrences of four unique keys.

| Method / exact input | Best existing method, µs | Prepared object, µs | One-shot, µs |
|---|---|---:|---:|
| [Matcher::getMatchedKeywords(); 128 B](benchmark/inputs/cases/unique/results.unique.bytes128.keys128.one.json) | `strpos()` loop<br>3.922 | 0.243 (-93.80%) | 52.676 (13.4 times slower) |
| [Matcher::getMatchedKeywords(); 1 KiB](benchmark/inputs/cases/unique/results.unique.bytes1024.keys128.one.json) | `preg_match_all()`<br>26.284 | 1.144 (-95.65%) | 53.538 (+103.51%) |
| [Matcher::getMatchedKeywords(); 4 KiB](benchmark/inputs/cases/unique/results.unique.bytes4096.keys128.one.json) | `preg_match_all()`<br>102.852 | 4.317 (-95.79%) | 58.478 (-43.01%) |
| [Matcher::getMatchedKeywords(); 64 KiB](benchmark/inputs/cases/unique/results.unique.bytes65536.keys128.one.json) | `preg_match_all()`<br>1613.013 | 189.529 (-88.22%) | 273.373 (-83.05%) |
| [Matcher::countMatches(); 128 B](benchmark/inputs/cases/count/results.count.bytes128.keys128.one.json) | `preg_match_all()`<br>4.265 | 0.219 (-94.85%) | 53.286 (12.5 times slower) |
| [Matcher::countMatches(); 1 KiB](benchmark/inputs/cases/count/results.count.bytes1024.keys128.one.json) | `preg_match_all()`<br>25.706 | 1.236 (-95.19%) | 54.012 (+109.85%) |
| [Matcher::countMatches(); 4 KiB](benchmark/inputs/cases/count/results.count.bytes4096.keys128.one.json) | `preg_match_all()`<br>101.504 | 4.739 (-95.34%) | 66.663 (-34.34%) |
| [Matcher::countMatches(); 64 KiB](benchmark/inputs/cases/count/results.count.bytes65536.keys128.one.json) | `preg_match_all()`<br>1605.462 | 199.793 (-87.51%) | 274.853 (-82.88%) |
| [Matcher::matchAll(); 1 KiB](benchmark/inputs/cases/all/results.all.bytes1024.keys128.one.json) | `preg_match_all()`<br>26.180 | 1.253 (-95.22%) | 53.688 (+104.97%) |
| [Matcher::matchAll(); 4 KiB](benchmark/inputs/cases/all/results.all.bytes4096.keys128.one.json) | `preg_match_all()`<br>102.528 | 4.751 (-95.36%) | 58.780 (-42.75%) |
| [Matcher::matchAll(); 64 KiB](benchmark/inputs/cases/all/results.all.bytes65536.keys128.one.json) | `preg_match_all()`<br>1610.465 | 193.198 (-88.00%) | 278.040 (-82.73%) |
| [Matcher::matchAll(); 64 KiB; occurrences: 64; unique matched keys: 4](benchmark/inputs/cases/all/fixed_density.all.bytes65536.keys128.one-per-kib.json) | `preg_match_all()`<br>1695.893 | 196.443 (-88.42%) | 280.789 (-83.43%) |

[All six lengths, other dictionaries, no matches, repeated occurrences and Clang](benchmark/matcher.md). Total occurrences and unique matched keys are stated separately. The measured Matcher series contains no more than 64 occurrences. Hundreds or thousands of `matchAll()` results were not measured.

## Application examples for Matcher

Two separate natural-language texts (EN) and dictionaries with variable-length keys. Each row is measured separately.

| Method / exact input | Best existing method, µs | Prepared object, µs | One-shot, µs |
|---|---|---:|---:|
| [Matcher::matches(); 1393 B; a dictionary of 128 keys of 3–30 B; no matches](benchmark/inputs/cases/examples/example.posts.en.absent.json) | `str_contains()` loop<br>37.494 | 2.435 (-93.48%) | 73.100 (+95.19%) |
| [Matcher::getMatchedKeywords(); 12828 B; a dictionary of 128 keys of 4–28 B; occurrences: 23; unique matched keys: 12](benchmark/inputs/cases/examples/example.articles.en.unique.json) | `strpos()` loop<br>307.035 | 19.341 (-93.68%) | 95.719 (-68.77%) |

[Texts, dictionaries and results](benchmark/INPUTS.md). On the first input, object construction does not pay off in one call; on the second, it does.

## `Replacer::replace()`: text length and number of replacements

The first rows use one dictionary of 32 keys of 11–21 B; a dictionary of 16 keys in the same length range is shown separately. Each matched key occurs once; its replacement value has the same length as the key. Output size equals input text size. The measured call is `replace($subject)` without the optional output argument `$count`.

| Method / exact input | Best existing method, µs | Prepared object, µs | One-shot, µs |
|---|---|---:|---:|
| [1 KiB; a dictionary of 32 keys; replacements: 0](benchmark/replacer-inputs/natural.b1024.n32.active0.mixed.json) | `preg_replace_callback()`<br>2.214 | 1.365 (-38.15%) | 14.730 (+565.66%) |
| [1 KiB; a dictionary of 32 keys; replacements: 2](benchmark/replacer-inputs/natural.b1024.n32.active2.mixed.json) | `preg_replace_callback()`<br>2.422 | 1.436 (-40.71%) | 14.887 (+514.25%) |
| [4 KiB; a dictionary of 32 keys; replacements: 0](benchmark/replacer-inputs/natural.b4096.n32.active0.mixed.json) | `preg_replace_callback()`<br>8.482 | 5.939 (-29.86%) | 19.350 (+128.73%) |
| [4 KiB; a dictionary of 32 keys; replacements: 16](benchmark/replacer-inputs/natural.b4096.n32.active16.mixed.json) | `preg_replace_callback()`<br>9.380 | 6.247 (-33.42%) | 19.790 (+111.09%) |
| [4 KiB; a dictionary of 32 keys; replacements: 32](benchmark/replacer-inputs/natural.b4096.n32.active32.mixed.json) | `preg_replace_callback()`<br>10.059 | 6.587 (-34.70%) | 20.211 (+101.38%) |
| [16 KiB; a dictionary of 32 keys; replacements: 0](benchmark/replacer-inputs/natural.b16384.n32.active0.mixed.json) | `preg_replace_callback()`<br>62.940 | 25.471 (-59.55%) | 39.979 (-36.48%) |
| [16 KiB; a dictionary of 32 keys; replacements: 32](benchmark/replacer-inputs/natural.b16384.n32.active32.mixed.json) | `preg_replace_callback()`<br>62.564 | 26.422 (-57.84%) | 40.482 (-35.29%) |
| [16 KiB; a dictionary of 16 keys; replacements: 16](benchmark/replacer-inputs/natural.b16384.n16.active16.mixed.json) | `preg_replace_callback()`<br>29.377 | 25.859 (-12.13%) | 32.892 (+11.94%) |

On 4 KiB, increasing replacements from 0 to 32 changes the prepared object's time from 5.939 to 6.587 µs — less than the move to 16 KiB. This is an observation from this series, not a general property of the algorithm.

[Equal and variable key lengths, large dictionaries, changes in output size and Clang](benchmark/replacer.md). PCRE measurements include literal expressions, shared-prefix factoring and groups of up to 512 rules. The table selects the fastest eligible variant; expression and callback preparation is outside the timer.

## Limits of applicability: losses for prepared and one-shot objects

| Method / exact input | Best existing method, µs | Prepared object, µs | One-shot, µs |
|---|---|---:|---:|
| [Matcher::getMatchedKeywords(); 64 KiB; a dictionary of 8 keys; occurrences: 16; unique matched keys: 8<br>both modes lose](benchmark/inputs/cases/unique/results.unique.bytes65536.keys8.sparse.json) | `strpos()` loop<br>30.348 | 158.969 (+423.47%) | 163.313 (+437.99%) |
| [Replacer::replace(); 4 KiB; a dictionary of 1 key; replacements: 5<br>both modes lose](benchmark/replacer-inputs/single.b4096.keybytes8.hits5.json) | `strtr()`<br>0.400 | 4.080 (+921.12%) | 4.462 (11.2 times slower) |
| [Replacer::replace(); 1 MiB; a dictionary of 1000 keys in {{…}} format; replacements: 100<br>both modes lose](benchmark/replacer-inputs/large.b1048576.n1000.active10pct.mixed.json) | `preg_replace_callback()`<br>63.977 | 1148.500 (18.0 times slower) | 1471.567 (23.0 times slower) |
| [Replacer::replace(); 7301 B; a dictionary of 128 keys; replacements: 4<br>the one-shot call loses](benchmark/replacer-inputs/example.links.en.json) | `preg_replace_callback()`<br>47.209 | 9.520 (-79.85%) | 130.398 (+176.24%) |
| [Replacer::replace(); 69643 B; a dictionary of 24 keys; replacements: 3<br>both modes lose](benchmark/replacer-inputs/example.logs.keys24.hits3.json) | `preg_replace()`<br>4.515 | 75.878 (16.8 times slower) | 92.197 (20.4 times slower) |

For `{{…}}` keys, a specialized `preg_replace_callback()` recognizes a fragment using one expression and looks it up in the dictionary. This is an eligible alternative for that format. For the 69643 B text, three occurrences are replaced with one marker, allowing direct `preg_replace()` without a callback. For the 7301 B text, a prepared Replacer is faster, but object construction does not pay off in one call against the measured PCRE method.

## When reuse pays off

Each job constructs one Matcher, processes the same string B times, then destroys the object. The table shows the first tested call count with a win on GCC, including construction and destruction. B=1, 4, 16 and 64 were tested; this is not the exact minimum break-even point.

| Method / exact input | First tested call count with a win | Best existing method: whole job, µs | Matcher: whole job, µs |
|---|---:|---|---:|
| [Matcher::matches(); 128 B; 128 keys; no matches](benchmark/inputs/cases/any/presence.any.bytes128.keys128.absent.rank65.json) | 64 | `preg_match()`<br>190.158 | 60.238 (-68.34%) |
| [Matcher::matches(); 4 KiB; 128 keys; no matches](benchmark/inputs/cases/any/presence.any.bytes4096.keys128.absent.rank65.json) | 1 | `preg_match()`<br>100.021 | 58.107 (-42.02%) |
| [Matcher::matchAll(); 64 KiB; 1024 keys; occurrences: 16](benchmark/inputs/cases/all/results.all.bytes65536.keys1024.sparse.json) | 1 | `strpos()` loop<br>15395.728 | 966.145 (-93.72%) |

For the 128 B text, B=1, 4 and 16 did not show a win; B=64 did. This repeats one text, not a batch of different documents. Replacer reuse was not measured in the AMD series; [the Intel application study](application-workloads/README.md#reuse-one-object-different-texts) measures batches of different texts. [All tested AMD B values, Clang and raw samples](benchmark/REUSE.md).

## Construction and memory

An example where a large dictionary pays off in one call:

| Method / exact input | Best existing method, µs | Prepared object, µs | One-shot, µs |
|---|---|---:|---:|
| [Replacer::replace(); 1 MiB; a dictionary of 10000 keys of 8–24 B; replacements: 10000](benchmark/replacer-inputs/generic.b1048576.n10000.active100pct.mixed.json) | `strtr()`<br>65678.021 | 2262.316 (-96.54%) | 31892.938 (-51.41%) |

Construction is measured without a method call and without object destruction; the constructor is warm. Prepared-object memory is the additional memory beyond the loaded dictionary. Construction peak already includes the object and temporary buffers: these columns should not be added together. This is Zend accounting, not RSS.

| Dictionary | Construction, µs | Additional object memory, KiB | Construction peak above dictionary, KiB |
|---|---:|---:|---:|
| [Matcher; 128 keys of 12 B each](benchmark/inputs/cases/unique/results.unique.bytes4096.keys128.one.json) | 52.138 | 57.750 | 101.750 |
| [Replacer; 32 keys](benchmark/replacer-inputs/natural.b4096.n32.active0.mixed.json) | 13.827 | 19.109 | 34.609 |
| [Replacer; 10000 keys](benchmark/replacer-inputs/generic.b1048576.n10000.active0pct.mixed.json) | 28869.130 | 3202.750 | 9376.812 |

The table does not include input-text memory or temporary allocations during method calls. `matchAll()` creates an object for each occurrence; its call peak was not measured separately. `replace()` peaks are reported in [MEMORY](benchmark/MEMORY.md).

On a 1 MiB text with 10000 keys and 10000 replacements, one-shot `replace()` took 31.893 ms on GCC. Constructing the same dictionary in a separate measurement took 28.869 ms. These are separate measurements, not an exact breakdown of one timing sample. [All memory configurations and temporary allocations during calls](benchmark/MEMORY.md).

In ordinary PHP-FPM, the object does not persist across independent requests. Reuse refers to multiple calls within a request or a long-running application. Changing Replacer keys or values requires a new object. In these measurements, PCRE uses a [warm cache of compiled expressions](https://www.php.net/manual/en/book.pcre.php), which can persist in the worker between requests.

## Method, checks and limitations

The main controlled Matcher series uses artificial 12-byte ASCII keys. Texts are based on saved PHP Manual fragments, with matches placed at specified positions. This does not measure the natural distribution of words and matches in user documents.

In the AMD series, one fixed text and dictionary are processed repeatedly after warmup. Times for different texts are not averaged together. This is a warm working set, not an independent sample of requests. Lengths and occurrence counts are controlled; production workload frequencies are unknown. The linked Intel studies add another CPU and fixed batches of different documents; neither study measures production request throughput or other architectures.

[Method and comparison recipes](benchmark/METHOD.md) · [Code and build hashes](benchmark/SOURCE.md) · [Exact inputs and verification scope](benchmark/INPUTS.md) · [Correctness and sanitizers](benchmark/CHECKS.md) · [Quality control](benchmark/QUALITY.md) · [Cycles and instructions](benchmark/COUNTERS.md) · [Unusual results](benchmark/OBSERVATIONS.md) · [Reproduction](benchmark/REPRODUCE.md) · [Repeated calls](benchmark/REUSE.md).
