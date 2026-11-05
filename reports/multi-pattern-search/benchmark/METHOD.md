# Method and comparison recipes

One input is one saved text, one ordered dictionary and one operation. One timing result is the median of 15 mean operation times. Different texts are not combined into one measured time.

## Timing and order

AMD Ryzen 9 5950X, Linux x86-64; CPU 15, SMT sibling 31 is monitored. After calibration, each method is warmed up for 100 ms; the target time per sample is 40 ms, with 15 samples in total. Method order changes between rounds. A fixed text and dictionary are repeated: this is a warm working set.

A prepared object is constructed before the timer. A one-shot call includes object construction, the query, consuming and releasing the result, and object destruction. PHP/PCRE arguments are prepared in advance; the PCRE cache of compiled expressions is warm. Search, replacement and the constructor itself are separate series. The constructor is separately warmed up for 250 ms and measured in 15 samples targeting approximately 66.7 ms. Timer overhead is retained and not subtracted; destruction occurs outside its timer.

The percentage reference is the eligible existing method with the lowest unrounded median in that series. The change is `100 × (median_i(Tobject_i / Treference_i) − 1)`. Comparisons are paired by round. For Matcher, prepared and one-shot modes have separate series: the adjacent PHP/PCRE columns show the one-shot series, so the prepared-call percentage cannot be calculated by dividing by those printed times. For the replacement series, both modes are included in the same rounds; the single-key control has separate series. All sample arrays are available in the [data](data/elapsed.json.gz).

An identical-code A/A control checks object timings. The A/A limit is 2%; the maximum deviation of a sample from its median is 5%; SMT sibling load must not exceed 2%. Matcher qualifies the comparison as a whole. Replacer checks the object, its A/A control and the selected alternative; a flag on any of these excludes the percentage. A/A is checked within a process and does not assess variation between independent processes. The first attempt to pass the checks is used regardless of speed. Failed attempts are retained. The 2% threshold for close results is a reporting rule, not a confidence interval.

## Existing methods

- `matches()`: a `str_contains()` loop with early exit and `preg_match()` with literal alternatives. Keys are split into groups of up to 512; checking stops at the first match.
- `getMatchedKeywords()`: `strpos()` for each key, ordering unique results; PCRE collects occurrences and selects unique keys.
- `countMatches()`: repeated `strpos()`, advancing the offset by one byte, or `preg_match_all()`. Overlapping occurrences are included.
- `matchAll()`: repeated `strpos()` or `preg_match_all()`, constructing an ordered result. `Matcher::matchAll()` returns `MatchResult` objects, while existing methods return arrays; creation and release are included.
- PCRE for unique/count/all combines keys of equal length into expressions of up to 512 keys and uses lookahead expressions `(?=...)` to preserve overlaps. Combining and ordering results is included where required by the method.
- `replace()`: `strtr()`, `str_replace()` where applicable to the input, and `preg_replace_callback()` with literal alternatives, shared-prefix factoring and groups of up to 512 rules. Direct `preg_replace()` is also checked for a single replacement value.
- For keys in `{{…}}` format, `~\{\{[^{}]*\}\}~` is checked, followed by dictionary lookup of the matched fragment. Unknown fragments are preserved. This method uses the format constraint and is not applied to arbitrary substrings.

All included methods are checked for equality with the saved result before the timer. Universal equivalence of sequential str_replace(), strtr() and different regex strategies is not claimed. In the large replacement matrix, a preliminary single sample was used to select fast alternatives; it is not used for comparative percentages. Compilation errors or result mismatches identify an ineligible method.

## Input characteristics

The dictionary contains keys to search for. Occurrences are all key matches in the text, including repeats and overlaps. Unique matched keys means how many distinct keys occur at least once. For example, four repetitions of one key mean four occurrences and one unique matched key.

The six Matcher lengths use prefixes of one saved PHP Manual stream. The background of controlled texts comes from saved sources; matches are placed to meet the specified conditions. This is not a production traffic sample. The Matcher length series fixes a dictionary of 128 keys of 12 bytes and one occurrence; lengths are 128 B and 1/4/16/32/64 KiB. Inputs for unique keys, counting and all results are byte-identical across methods. The main replacement controls use keys of 11–21 bytes; with 32 replacements on 4 KiB, 512 bytes (12.5%) are replaced. The main large matrix replaces no more than 15.3% of bytes. Percentages of activated rules mean the number of distinct replaced keys, not the fraction of text bytes.

## Cycles, instructions and memory

Counters use five N/0 pairs: identical loading, preparation and eight warmup calls; the measured work is subtracted and divided by N. N is chosen to target approximately 60 ms of work. Results for different methods do not form a paired hardware-counter percentage. Unavailable or non-positive corrections and pairs with SMT load are flagged; all five pairs are retained. No additional counters were collected for alternatives costing more than 100 ms.

Memory uses Zend accounting, not RSS. Dictionary and object memory, construction peak and call peak have separate baselines. Call peak includes the result. Time and memory alone do not determine full application performance.

The exact method sets and their order are saved in the [configurations and results](data/captures.json.gz). “Best” means the fastest among the saved repeated measurements; global optimality among all possible regex strategies is not claimed. [Preliminary single-sample estimates for the large matrix](data/recipe-screening.json) are kept separate from comparative results. [Summary input selection](data/report-selection.json).
