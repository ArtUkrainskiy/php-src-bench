# Forward substring search: product benchmarks

This report measures a change to `zend_memnstr_ex()`, the forward matcher used by PHP string functions. The change reduces Sunday setup costs for medium needles and limits expensive verification on long scans. The corpus covers everyday moderation, separators, parsers, templates and logs.

Compared: change [`ca89fb5fb96`](https://github.com/ArtUkrainskiy/php-src/commit/ca89fb5fb96399ed730cacb12d948025f83c4e6e) ([branch](https://github.com/ArtUkrainskiy/php-src/tree/strpos-adaptive-pr), [patch](change.patch)) versus stock PHP [`ef99f4248f1`](https://github.com/php/php-src/commit/ef99f4248f1450c39fb86fd7fd6f24c49b8d11eb). Measured on 30 October 2026 with the same two commits and corpus on all six compiler/CPU combinations.

Review follow-up: [`8c6759c6826`](https://github.com/ArtUkrainskiy/php-src/commit/8c6759c6826e59aeaf14db2696c503f5334f81ad) corrects PHPT coverage and removes folding comments without changing the matcher algorithm. [Supplementary route, gram4-ablation and scalar measurements](review/README.md) are separate from the frozen product series below.

**Elapsed time of the complete PHP operation is the primary criterion.** Negative deltas mean lower cost; every delta is relative to stock. Cycles and instructions are diagnostic evidence, not substitutes for elapsed time. There is no application-wide average or assumed traffic distribution.

## Reading the case names

For example, `banlist12/en/post/clean` checks twelve case-sensitive literal substrings against a 1,081-byte English post, with no match. The list contains eight locale-specific words/phrases and four example blocked domains, such as `spam`, `casino bonus` and `promo-cash.example`. Searches use `str_contains()` and stop at the first matching term. `banword` measures only one search.

`comment`, `post` and `thread` target about 256 B, 1 KiB and 64 KiB respectively. They are UTF-8 strings assembled from hand-written order, delivery and support messages in seeded order, with varied identifiers. Complete messages are retained, so actual byte sizes vary; the main time tables show them. A `thread` is one long text input. Sizes count bytes, not characters. Text is already lower-case; normalization and word-boundary processing are outside timing.

`clean` means no listed term occurs, so all twelve searches run. `early` places the first term at byte zero and stops after one search. `late` appends the last term at the end, so all twelve searches run. Languages: `en` English, `es` Spanish, `ru` Russian, `ar` Arabic, `hi` Hindi, `zh` Chinese, `ja` Japanese, `ko` Korean; `emoji` mixes English and emoji.

| Case family | Data and search |
|---|---|
| `explode`, `explode-limit2`, `substr-count`, `str-replace` | Varied product fields with identifiers, including mixed UTF-8 values. `pipe2` = `\|\|`, `colon2` = `::`, `crlf` = CRLF, `comma` = `,`, `tab` = tab, `amp` = `&`. Split, split once, count or replace the delimiter; no quoting/escaping. |
| `parse-records` | Unquoted five-column records: split CRLF rows, then double-pipe fields. |
| `parse-query` | Form-urlencoded query with repeated `filter[]` keys: split `&` and `=`, then URL-decode keys and values. |
| `parse-http`, `find-http-end` | Constructed HTTP request: search CRLFCRLF; the parser also splits headers at CRLF and `: `. `cookie4k` has a long cookie; `incomplete` has no header terminator. |
| `scan-template`, `render-template` | Order-card HTML with `{{order.id}}`, `{{user.name}}`, `{{tracking.url}}`, `{{support.email}}`: collect slots or replace all four distinct names. |
| `log-contains`, `log-filter` | JSON-lines payment logs with varied request/order IDs and similar event prefixes. Search `payment_failed` or `"level":"error"`, or split lines and collect error-line indexes. Here early/late means the first/last record; clean has neither error marker. |
| `html-contains`, `source-tokens`, `document` | Search `href="` / `data-cookieconsent=`, C identifiers such as `zend_string`, Markdown fences/comment markers, or JavaScript `function` / `sourceMappingURL=`. Source/document scans are supplementary; source and snapshot hashes are in the manifest. |

`short` targets 128 B; `4k`, `64k`, `1m` target 4 KiB, 64 KiB, 1 MiB. `small` depends on the family. One MiB exports and large queries are size guards. `absent` means the searched literal/delimiter is missing.

Input bytes are not necessarily bytes scanned: `parse-http/body64k` has 65,848 bytes, but its parser stops after the 265-byte header prefix. The `render-template/4k` fixture has 4,250 bytes and 68 placeholder occurrences across its four distinct names. Parser/template timings include PHP loops, result construction and allocations.

## Summary

| CPU / compiler | Clean posts, Δ time | 4 KiB template, Δ time |
|---|---:|---:|
| AMD / GCC 15.2 | −10.35% … −4.93% | −14.70% |
| AMD / Clang 21.1 | −11.64% … −3.95% | −14.48% |
| Intel / GCC 13.3 | −6.69% … −2.48% | −15.66% |
| Intel / GCC 14.2 | −5.77% … −1.88% | −13.08% |
| Intel / Clang 18.1 | −7.98% … +0.18% | −8.48% |
| Intel / Clang 20.1 | −6.97% … −1.78% | −0.42% |

The post ranges cover medians across all nine languages, not uncertainty bounds; row quality and controls remain below and in the full tables. Moderation checks twelve literals in already normalized text. Short comments and one-/two-byte separators mostly retain their existing work. They have no general speedup guarantee. The template case replaces four distinct placeholder names with allocations, not a complete page request.

There are real losses: the independent AMD repeat retained GCC slowdowns around 1.66–2.48% in three parser cases. The original Clang `explode("||")` 4 KiB result was +3.24%, versus +0.20% in its single independent repeat; neither result is deleted. Quiet Intel retains roughly +4.4% and +5.4% on long English and Chinese text with Clang 20. A universal 3% regression bound and greater cross-compiler stability are not supported.

## Everyday elapsed times

The main tables use the complete final AMD one-second series, without replacing rows by favourable repeats. They include all nine clean-post languages plus short/early controls, long texts, separators, parsers, templates and logs.

### AMD / GCC 15.2

| Case | Bytes | Stock, µs | Change, µs | Δ time | Δ cycles¹ | Δ instr. | Result |
|---|--:|--:|--:|--:|--:|--:|---|
| banlist12/en/post/clean | 1,081 | 2.9548 | 2.6760 | −9.43% | −10.08% | −5.77% | Faster |
| banlist12/ru/post/clean | 1,041 | 3.0461 | 2.8732 | −5.68% | −5.66% | −3.39% | Faster |
| banlist12/es/post/clean | 1,086 | 2.8571 | 2.5900 | −9.35% | −9.52% | −5.77% | Faster |
| banlist12/ar/post/clean | 1,036 | 3.9494 | 3.7548 | −4.93% | −5.17% | −4.01% | Faster |
| banlist12/hi/post/clean | 1,091 | 2.6588 | 2.4771 | −6.83% | −7.09% | −4.93% | Faster |
| banlist12/zh/post/clean | 1,039 | 2.3121 | 2.0728 | −10.35% | −10.45% | −7.76% | Faster |
| banlist12/ja/post/clean | 1,069 | 3.2846 | 3.0208 | −8.03% | −8.91% | −5.33% | Faster |
| banlist12/ko/post/clean | 1,098 | 3.1002 | 2.8682 | −7.48% | −7.60% | −5.19% | Faster |
| banlist12/emoji/post/clean | 1,097 | 2.6880 | 2.4388 | −9.27% | −9.60% | −6.22% | Faster |
| banlist12/en/comment/clean | 300 | 0.4995 | 0.5034 | +0.79% | +1.25% | −0.00% | Unclear |
| banlist12/en/post/early | 1,087 | 0.0326 | 0.0338 | +3.76% | −2.42% | +0.00% | Unclear |
| banlist12/hi/post/early | 1,108 | 0.0454 | 0.0374 | −17.58% | −14.89% | −16.76% | Faster |
| banlist12/en/thread/clean | 65,548 | 170.6972 | 158.9640 | −6.87% | −7.18% | −0.13% | Faster |
| banlist12/ru/thread/clean | 65,638 | 222.3682 | 217.5858 | −2.15% | −2.20% | −0.07% | Faster |
| banlist12/zh/thread/clean | 65,620 | 149.5724 | 141.4225 | −5.45% | −5.98% | −0.17% | Faster |
| explode/pipe2/4k | 4,123 | 2.5081 | 2.5085 | +0.02% | +1.37% | +0.00% | Unclear |
| explode/colon2/4k | 4,099 | 2.5272 | 2.4989 | −1.12% | −0.21% | −0.00% | Unclear |
| explode/comma/4k | 4,111 | 2.1888 | 2.1952 | +0.29% | −0.32% | −0.00% | Unclear |
| explode/crlf/4k | 4,098 | 2.4607 | 2.4325 | −1.15% | −0.04% | +0.00% | Unclear |
| parse-records/4k | 4,151 | 9.4418 | 9.5843 | +1.51% | −0.75% | +0.00% | Slower |
| parse-query/4k | 4,096 | 26.0120 | 26.2823 | +1.04% | +0.46% | +0.00% | Slower |
| parse-http/small | 265 | 0.8447 | 0.8538 | +1.07% | +1.70% | +0.00% | Unclear |
| parse-http/body64k | 65,848 | 0.8381 | 0.8595 | +2.54% | +1.60% | +0.00% | Slower |
| scan-template/4k | 4,250 | 4.5714 | 4.5635 | −0.17% | +0.26% | +0.00% | Unclear |
| render-template/4k | 4,250 | 7.0283 | 5.9951 | −14.70% | −14.66% | −17.65% | Faster |
| log-contains/event/thread/clean | 65,600 | 13.3864 | 12.3392 | −7.82% | −7.78% | −0.12% | Faster |
| log-filter/thread/clean | 65,600 | 42.0660 | 41.9510 | −0.27% | +0.85% | −0.00% | Unclear |

### AMD / Clang 21.1

| Case | Bytes | Stock, µs | Change, µs | Δ time | Δ cycles¹ | Δ instr. | Result |
|---|--:|--:|--:|--:|--:|--:|---|
| banlist12/en/post/clean | 1,081 | 2.8101 | 2.5401 | −9.61% | −10.14% | −1.94% | Faster |
| banlist12/ru/post/clean | 1,041 | 2.8605 | 2.7476 | −3.95% | −4.14% | −2.27% | Faster |
| banlist12/es/post/clean | 1,086 | 2.7114 | 2.4480 | −9.72% | −9.88% | −1.93% | Faster |
| banlist12/ar/post/clean | 1,036 | 3.8592 | 3.6704 | −4.89% | −4.93% | −1.31% | Faster |
| banlist12/hi/post/clean | 1,091 | 2.4691 | 2.3515 | −4.76% | −4.41% | −2.68% | Faster |
| banlist12/zh/post/clean | 1,039 | 2.1799 | 1.9261 | −11.64% | −12.09% | −2.67% | Faster |
| banlist12/ja/post/clean | 1,069 | 3.1152 | 2.8773 | −7.64% | −8.11% | −1.78% | Faster |
| banlist12/ko/post/clean | 1,098 | 2.9588 | 2.7281 | −7.80% | −7.53% | −1.72% | Faster |
| banlist12/emoji/post/clean | 1,097 | 2.5483 | 2.2975 | −9.84% | −9.16% | −2.10% | Faster |
| banlist12/en/comment/clean | 300 | 0.5138 | 0.5104 | −0.66% | +0.23% | +0.00% | Unclear |
| banlist12/en/post/early | 1,087 | 0.0304 | 0.0304 | +0.09% | −1.04% | +0.00% | Unclear |
| banlist12/hi/post/early | 1,108 | 0.0418 | 0.0357 | −14.56% | −12.93% | −5.95% | Faster |
| banlist12/en/thread/clean | 65,548 | 161.8209 | 149.1975 | −7.80% | −8.06% | −0.04% | Faster |
| banlist12/ru/thread/clean | 65,638 | 217.9945 | 205.6730 | −5.65% | −5.73% | +3.70% | Faster |
| banlist12/zh/thread/clean | 65,620 | 144.1783 | 131.6223 | −8.71% | −8.80% | −0.06% | Faster |
| explode/pipe2/4k | 4,123 | 2.7138 | 2.8019 | +3.24% | −0.15% | −0.00% | Slower |
| explode/colon2/4k | 4,099 | 2.7902 | 2.7557 | −1.23% | +0.39% | +0.00% | Unclear |
| explode/comma/4k | 4,111 | 2.2465 | 2.2148 | −1.41% | +0.62% | +0.00% | Unclear |
| explode/crlf/4k | 4,098 | 2.6348 | 2.6547 | +0.76% | −0.79% | +0.00% | Unclear |
| parse-records/4k | 4,151 | 9.9516 | 10.0725 | +1.22% | +0.62% | +0.00% | Unclear |
| parse-query/4k | 4,096 | 27.2458 | 27.5487 | +1.11% | +0.33% | −0.00% | Unclear |
| parse-http/small | 265 | 0.8478 | 0.8275 | −2.39% | −1.66% | +0.00% | Faster |
| parse-http/body64k | 65,848 | 0.8440 | 0.8262 | −2.10% | −2.49% | +0.00% | Faster |
| scan-template/4k | 4,250 | 4.3505 | 4.3489 | −0.04% | +0.10% | −0.00% | Unclear |
| render-template/4k | 4,250 | 6.5323 | 5.5867 | −14.48% | −14.26% | −6.53% | Faster |
| log-contains/event/thread/clean | 65,600 | 12.4447 | 11.4881 | −7.69% | −7.73% | −0.04% | Faster |
| log-filter/thread/clean | 65,600 | 43.1143 | 42.9586 | −0.36% | +0.13% | −0.00% | Unclear |

¹ Cycles were measured separately: five paired passes × 50 ms on AMD, three × 50 ms in the fresh quiet Intel series. Binary hashes match the elapsed-time builds. Instruction deltas here are from the elapsed-time series. These columns do not yield exact simultaneous IPC. A dash means no matching completed cycle row.

Faster/Slower requires separated round medians and at least a 1% difference. Unclear means overlap or a small difference, not proof of equality. Noise includes sample spread over 5%, round drift over 10%, or an idle-wait timeout. Spread is `1.4826 × MAD / median`, not a confidence interval.

## Regressions and independent controls

A finite confirmation stage selected every noisy row and every usable slower row from the full AMD series: 23 cases, 47 runs including same-binary A/A and profiles. Selection did not depend on obtaining a favourable result. Each selected case has one new A/B run; there are no recursive retries. Three remain noisy. The original slower rows and all their controls are shown here.

| Case | Compiler | Original Δ time | Repeat Δ time | Stock A/A | Change A/A | Result |
|---|---|---:|---:|---:|---:|---|
| parse-records/4k | GCC 15.2 | +1.51% | +0.84% | +0.22% | +0.16% | Unclear |
| parse-query/4k | GCC 15.2 | +1.04% | +0.44% | −0.66% | +0.42% | Unclear |
| parse-http/body64k | GCC 15.2 | +2.54% | +2.24% | +0.94% | +0.13% | Slower |
| explode-limit2/colon2/short | GCC 15.2 | +2.08% | +1.32% | −0.50% | −0.36% ⚠ | Unclear |
| parse-query/small | GCC 15.2 | +1.41% | +1.66% | −0.10% | −0.27% | Slower |
| parse-query/64k | GCC 15.2 | +1.01% | +0.77% | −0.18% | −0.45% | Unclear |
| parse-http/cookie4k | GCC 15.2 | +1.31% | +2.48% | +0.40% | −0.25% | Slower |
| explode/pipe2/4k | Clang 21.1 | +3.24% | +0.20% | −0.18% | +1.41% | Unclear |

⚠ marks a noisy A/A control. Small positive parser deltas present in both runs are retained even if the repeat is Unclear. A/A is specific to the measured case/build; it is not a universal error bar for every compiler or CPU.

## Compiler cycle matrix and A/A

Generated by `bench compare` / `bench table --full --compact-header`, with every available compiler and same-row A/A below each table. Absolute stock cycles use the compiler named above the table. Each percentage compares the change with that column's own stock build. The cycle A/A uses GCC 15 on AMD and GCC 13 on Intel. [All 76 rows and pass ranges](tables/cycles.md) are retained.

### AMD

<!-- bench-table data/amd/cycles-reference.json --full --compact-header --base-name Stock --labels data/cycle-labels.txt -->
Absolute cycles/call: Stock with GCC 15.2.

| call | Stock cycles | GCC 15.2 | clang 21.1 | Δ instr. |
|---|--:|--:|--:|--:|
| banlist12/en/post/clean | 13,958 | −10% (−11 … −10) | −10% (−10 … −10) | −6% … −2% |
| banlist12/ru/post/clean | 14,319 | −6% (−6 … −1) | −4% (−4 … −4) | −3% … −2% |
| banlist12/es/post/clean | 13,467 | −10% (−10 … −9) | −10% (−10 … −9) | −6% … −2% |
| banlist12/ar/post/clean | 18,605 | −5% (−5 … +17) | −5% (−5 … −5) | −4% … −1% |
| banlist12/hi/post/clean | 12,483 | −7% (−10 … −6) | −4% (−5 … −3) | −5% … −3% |
| banlist12/zh/post/clean | 10,923 | −10% (−11 … −10) | −12% (−12 … −11) | −8% … −3% |
| banlist12/ja/post/clean | 15,437 | −9% (−9 … −9) | −8% (−8 … −8) | −5% … −2% |
| banlist12/ko/post/clean | 14,561 | −8% (−8 … −7) | −8% (−9 … −7) | −5% … −2% |
| banlist12/emoji/post/clean | 12,684 | −10% (−10 … −9) | −9% (−10 … −4) | −6% … −2% |
| explode/pipe2/4k | 11,540 | +1% (−1 … +3) | 0% (−5 … +6) ~ | 0% |
| explode/colon2/4k | 11,638 | 0% (0 … +1) ~ | 0% (−1 … +2) ~ | 0% |
| parse-records/4k | 43,247 | −1% (−1 … 0) | +1% (0 … +3) | 0% |
| parse-query/4k | 117,786 | 0% (0 … +2) | 0% (−1 … +1) | 0% |
| parse-http/small | 3,793 | +2% (+1 … +3) | −2% (−3 … −1) | 0% |
| parse-http/body64k | 3,799 | +2% (0 … +3) | −2% (−17 … −1) | 0% |
| render-template/4k | 32,819 | −15% (−15 … −14) | −14% (−16 … −14) | −18% … −7% |
| log-contains/event/thread/clean | 63,244 | −8% (−8 … −8) layout? | −8% (−8 … −7) layout? | 0% |

Control: Stock against itself.

Absolute cycles/call: Stock with GCC 15.2.

| call | Stock cycles | A/A start | A/A end |
|---|--:|--:|--:|
| banlist12/en/post/clean | 14,020 | 0% (0 … 0) | −1% (−1 … +1) |
| banlist12/ru/post/clean | 14,354 | 0% (−1 … +1) | 0% (0 … 0) |
| banlist12/es/post/clean | 13,453 | 0% (−1 … 0) | 0% (−1 … 0) |
| banlist12/ar/post/clean | 18,573 | 0% (0 … +1) | 0% (0 … +1) |
| banlist12/hi/post/clean | 12,475 | 0% (0 … 0) | 0% (0 … +5) |
| banlist12/zh/post/clean | 10,925 | 0% (0 … +3) | 0% (−1 … 0) |
| banlist12/ja/post/clean | 15,422 | 0% (0 … 0) | 0% (0 … 0) |
| banlist12/ko/post/clean | 14,549 | 0% (−1 … 0) | 0% (−1 … +1) |
| banlist12/emoji/post/clean | 12,655 | 0% (0 … +1) | 0% (0 … 0) |
| explode/pipe2/4k | 11,535 | +1% (−1 … +3) | 0% (−1 … +2) |
| explode/colon2/4k | 11,550 | +1% (−2 … +1) | 0% (−2 … 0) |
| parse-records/4k | 43,389 | −1% (−1 … +1) | −1% (−1 … +1) |
| parse-query/4k | 118,637 | 0% (−5 … +3) | 0% (−1 … 0) |
| parse-http/small | 3,792 | +1% (−2 … +2) | +1% (0 … +1) |
| parse-http/body64k | 3,775 | +1% (0 … +1) | 0% (−1 … +2) |
| render-template/4k | 32,757 | 0% (−1 … +1) | 0% (−1 … 0) |
| log-contains/event/thread/clean | 63,165 | 0% (0 … 0) | 0% (0 … +1) |

~: the change is not larger than the A/A control of the same row: not evidence of a difference.

layout?: in every pass the cycles changed in the same direction, by 3% or more in the median, the instructions by less than 0.5%: the work is the same, so look for the cause (code placement, branch prediction) with `bench why` before reporting the row.
<!-- /bench-table -->

### INTEL

<!-- bench-table data/intel/control-cycles.json --full --compact-header --base-name Stock --labels data/cycle-labels.txt -->
Absolute cycles/call: Stock with GCC 13.3.

| call | Stock cycles | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | Δ instr. |
|---|--:|--:|--:|--:|--:|--:|
| banlist12/en/post/clean | 13,299 | −7% (−9 … −6) | −2% (−3 … −2) | 0% (0 … 0) ~ | −6% (−7 … −6) | −10% … −6% |
| banlist12/ru/post/clean | 13,675 | −3% (−4 … −2) | −3% (−3 … −2) | −3% (−3 … −2) | −2% (−3 … −2) | −9% … −3% |
| banlist12/es/post/clean | 12,473 | −4% (−5 … −3) | −5% (−8 … −3) | −6% (−6 … −5) | −2% (−3 … −2) | −10% … −6% |
| banlist12/ar/post/clean | 18,645 | −3% (−3 … −2) | −2% (−3 … −2) | −2% (−7 … −1) | −2% (−2 … −2) | −6% … −4% |
| banlist12/hi/post/clean | 11,869 | −3% (−3 … −3) | −3% (−4 … −1) | −4% (−4 … −4) | −2% (−2 … +4) | −11% … −5% |
| banlist12/zh/post/clean | 9,943 | −6% (−6 … −6) | −4% (−6 … −4) | −8% (−8 … −8) | −3% (−3 … −3) | −11% … −8% |
| banlist12/ja/post/clean | 14,955 | −3% (−4 … −3) | −4% (−6 … −2) | −5% (−5 … −5) | −3% (−3 … −3) | −8% … −5% |
| banlist12/ko/post/clean | 14,533 | −5% (−5 … −4) | −2% (−3 … 0) | −3% (−4 … −3) | −2% (−2 … −1) | −8% … −5% |
| banlist12/emoji/post/clean | 11,949 | −2% (−2 … −2) | −3% (−3 … −2) | −6% (−7 … −6) | −3% (−4 … −3) | −10% … −6% |
| explode/pipe2/4k | 9,489 | +1% (−2 … +1) ~ | −2% (−3 … +3) ~ | −1% (−2 … 0) ~ | −4% (−4 … 0) layout? | 0% |
| explode/colon2/4k | 9,238 | 0% (−5 … +4) ~ | +1% (−4 … +4) ~ | 0% (−2 … +1) ~ | +1% (0 … +1) ~ | 0% |
| parse-records/4k | 36,772 | −1% (−2 … 0) ~ | +2% (0 … +3) | +1% (0 … +2) ~ | −1% (−2 … +1) ~ | 0% |
| parse-query/4k | 96,493 | 0% (−1 … +1) ~ | 0% (−1 … +1) | 0% (−3 … 0) ~ | +1% (0 … +2) | 0% |
| parse-http/small | 3,084 | +1% (+1 … +3) | −1% (−1 … −1) | −1% (−2 … 0) | +1% (0 … +2) | 0% |
| parse-http/body64k | 3,101 | +1% (0 … +2) | 0% (−2 … +2) | +1% (−4 … +3) | +1% (+1 … +1) | 0% |
| render-template/4k | 28,885 | −16% (−17 … −16) | −11% (−14 … −11) | −8% (−9 … −6) | −3% (−5 … −3) | −18% … −12% |
| log-contains/event/thread/clean | 72,698 | −11% (−13 … +9) | −2% (−4 … +2) | +7% (−2 … +8) | −1% (−5 … +6) | −9% … 0% |

Control: Stock against itself.

Absolute cycles/call: Stock with GCC 13.3.

| call | Stock cycles | A/A start | A/A end |
|---|--:|--:|--:|
| banlist12/en/post/clean | 13,214 | +1% (0 … +1) | 0% (0 … 0) |
| banlist12/ru/post/clean | 13,645 | 0% (0 … +2) | 0% (−1 … 0) |
| banlist12/es/post/clean | 12,546 | 0% (0 … 0) | 0% (0 … +1) |
| banlist12/ar/post/clean | 18,657 | 0% (−1 … 0) | 0% (0 … 0) |
| banlist12/hi/post/clean | 11,845 | +1% (−2 … +2) | 0% (0 … +1) |
| banlist12/zh/post/clean | 9,912 | +1% (0 … +1) | 0% (0 … 0) |
| banlist12/ja/post/clean | 14,991 | −1% (−1 … −1) | 0% (0 … 0) |
| banlist12/ko/post/clean | 14,484 | 0% (−2 … 0) | 0% (0 … +1) |
| banlist12/emoji/post/clean | 11,947 | 0% (−1 … +1) | 0% (0 … 0) |
| explode/pipe2/4k | 9,505 | +3% (−3 … +4) | +1% (−1 … +5) |
| explode/colon2/4k | 9,197 | 0% (0 … +4) | −2% (−3 … 0) |
| parse-records/4k | 36,892 | 0% (−1 … 0) | +1% (0 … +2) |
| parse-query/4k | 95,247 | 0% (0 … 0) | 0% (−1 … +1) |
| parse-http/small | 3,101 | 0% (−2 … 0) | 0% (0 … 0) |
| parse-http/body64k | 3,100 | 0% (−1 … +1) | 0% (−3 … 0) |
| render-template/4k | 29,108 | 0% (−1 … 0) | +1% (+1 … +1) |
| log-contains/event/thread/clean | 64,437 | −1% (−1 … +1) | 0% (0 … +1) |

~: the change is not larger than the A/A control of the same row: not evidence of a difference.

layout?: in every pass the cycles changed in the same direction, by 3% or more in the median, the instructions by less than 0.5%: the work is the same, so look for the cause (code placement, branch prediction) with `bench why` before reporting the row.
<!-- /bench-table -->

## Machine and method

AMD Ryzen 9 5950X, GCC 15.2 / Clang 21.1: pinned physical core, `performance` governor, turbo enabled. Intel i7-13700H, GCC 13.3 / GCC 14.2 / Clang 18.1 / Clang 20.1: pinned P-core, AC power, `powersave` governor, turbo enabled. No frequency-setting changes are made to reproduce the report. The compiler matrix compares matched pairs within a machine; it is not an absolute AMD-versus-Intel ranking.

All timing pairs are non-debug, non-ZTS CLI release builds using the `docker` profile, `--disable-all --disable-cgi --disable-phpdbg --enable-cli --enable-werror`, CFLAGS `-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64`, LDFLAGS `-Wl,-O1 -pie`. Compiler, configure options and flags match within each pair. Full generated flags, binary fingerprints, environment and warnings remain in the raw series. Extra-alignment builds are historical diagnostics only.

AMD: 233 cases per compiler, four paired rounds × one approximately 1000 ms sample, warmup at least 1000 ms, perf instructions. Each case runs in its own PHP processes; compilers alternate after each case. Calibration chooses the iteration count; timing the batch avoids a timer call per operation. The median empty-loop cost is subtracted. Case preparation and result checking are outside the timed loop.

Quiet Intel: the initial 233-case sweep uses four rounds × seven samples × 10 ms. A preselected 22-case focus and quality rechecks use 50 ms. The selection policy is quality recheck, then preselected focus, then original full run; the original 233 rows are always retained. The source and sample window of each chosen row are recorded. Earlier busy-laptop elapsed times are historical and unusable for speed claims.

Cycle cost is `(counted process − empty-loop process) / iterations`, measured sequentially with alternating A/B order. The delta is the median of paired B/A pass ratios; absolute costs are separate side medians, so their ratio can differ slightly from the published paired delta. Elapsed deltas are directly `(median ca89 / median stock − 1) × 100%`. Instructions in elapsed runs are separate perf counts.

The [A/A window-duration pilot and all final confirmations](tables/confirmations.md) preserve both short and one-second controls. Longer windows did not universally reduce A/A drift. The final method also changes grouping from a whole filtered suite to one case per PHP process, so differences between old and new series cannot be assigned to warmup or duration alone.

## Code

The header memchr/verify path for remaining haystacks below 1024 bytes or needles below 9 bytes is unchanged. Needles of 9–31 bytes use a 256-byte uint8 Sunday table instead of the original 1 KiB unsigned-int table. Needles of at least 32 bytes retain wide-table Sunday below 8192 input bytes. On larger buffers, sixteen deep failed verifications trigger a work-versus-progress check; with at least 4096 bytes remaining, expensive scans may switch to an SSE2 pair filter, sampled four-byte filter and portable Two-Way. Full-verification budgets cover the remaining scan. The patch changes one C file and adds five PHPT files. No public API is added.

Unchanged instruction counts do not erase elapsed regressions. Profiles of the two confirmed GCC HTTP cases show L1 instruction-cache misses increasing from about 0.02 to 2.41 and 1.90 per call; the affected PHP entry-point addresses and sizes are unchanged. This is consistent with placement/cache effects, not proof of a unique cause. Long Russian/Hindi Clang scans can improve while executing more instructions. [Earlier profiles and disassembly](tables/profiles.md) and [new profiles](data/amd/final-confirmation/gcc15-case066-why.log) are retained. A general explanation for every layout-sensitive row has not been established.

## Algorithm references

- **Sunday / Quick Search.** Daniel M. Sunday, [A very fast substring search algorithm](https://doi.org/10.1145/79173.79184), 1990. PHP already uses this shift rule. The short-needle path keeps the same search and stores its shifts in bytes.
- **Two-Way.** Maxime Crochemore and Dominique Perrin, [Two-way string-matching](https://doi.org/10.1145/116825.116845), 1991. `zend_memnstr_twoway()` uses critical factorization and remembers periodic matches across shifts.
- **SIMD pair filtering.** The [packed-pair implementation in Rust memchr 2.7.6](https://github.com/BurntSushi/memchr/blob/2.7.6/src/arch/all/packedpair/mod.rs) is a related implementation reference for choosing two needle positions using background byte frequencies. Here SSE2 checks both positions at sixteen candidate starts, then verifies each hit completely.
- **Four-byte filtering, related work.** Simone Faro and M. Oğuzhan Külekci, [Fast Packed String Matching for Short Patterns](https://arxiv.org/abs/1209.6449), 2012 preprint, section 3.2 (EPSM_a). The related primitive intersects shifted byte-equality masks. `zend_memnstr_gram4()` applies it to a selected internal four-byte anchor, with overlapping windows, selectivity sampling and a verification budget.

The dispatch thresholds, byte-frequency weights, sampling rules and verification budgets are implementation choices evaluated by these PHP measurements. The references describe the search mechanisms; the measured gains, losses and applicability come from this corpus. The work-count checks are fixture audits rather than a formal proof of the complete hybrid.

## Corpus and scope

The [owned product corpus](data/corpus-manifest.json) has 141 frozen inputs and 233 operations, including a preselected 76-case primary set. The [manifest](data/corpus-manifest.json) records exact byte sizes, SHA-256 and recipes. Nine language variants cover comments, posts and approximately 64 KiB threads with absent/early/late matches. Normalization, word boundaries and case folding are outside timing. Fields, queries, HTTP, separators, templates and payment logs include PHP loops and allocations. A 64 KiB HTTP body does not imply a full-body scan: parsing stops at the header terminator.

The messages are constructed deterministic fixtures, not captured production traffic. No popularity weights are inferred. Public document snapshots are supplementary and retain source hashes; fetching current pages cannot reproduce the exact old snapshots. Their content is not committed. Source-text fixtures are pinned separately from the runtime base commit. One MiB exports, 64 KiB queries, the 112-case boundary grid and six repeated-prefix cases are size/stress guards, not typical request frequencies.

## Tests

- All 233 product and 112 boundary outputs agree across six compiler builds; Python ground truth independently generates exact expected search/split/replacement values. Raw runner hashes use MD5 of PHP serialized values; manifest SHA-256 covers input bytes. These are different checks.
- Core/string PHPT: release 6237 passed, 243 skipped, one expected failure; debug/ZTS 6236 passed, 244 skipped, one expected failure. No unexpected failures or warnings. String-only tests on each of the six compiler builds: 703 passed, 62 skipped.
- Exact extracted matching functions under ASan/UBSan: 100000 randomized inputs and 135460 guarded configurations for SSE2 and forced scalar, both passed. Four functional mutations are rejected. Work-count fixtures reject the tested disabled budgets/window reset; they are not a formal all-input complexity proof.
- [Validation records](data/validation.json), [sources and commands](verify/README.md). Benchmark framework self-tests were rerun after measurement and [passed](verify/framework-tests.txt). Native ARM and 32-bit runs remain untested; scalar on x86 does not replace them.

## Full evidence

- [All 76 primary cases on six compilers: absolute elapsed time, cycles, instructions and deltas](tables/primary.md).
- [All 233 original rows on six compilers](tables/all-product.md), [every observed elapsed increase over 1%](tables/increases.md), [TSV](data/metrics.tsv).
- [All cycle passes and A/A](tables/cycles.md), [elapsed A/A controls](tables/controls.md).
- [Boundary grid](tables/boundaries.md) and [repeated-prefix stress cases](tables/stress.md), separate from everyday cases.
- [All finite AMD confirmations](tables/confirmations.md), [quiet Intel early-match confirmations](tables/early.md), [data and file roles](LAYOUT.md).

## Not measured

Cold requests, complete FPM requests, framework throughput and production traffic weights; native ARM/32-bit performance; Go/Rust or cold-versus-cached PCRE. No universal cross-compiler stability or maximum-regression claim is made. All timing rows, including noisy and unresolved layout-sensitive rows, are published; such rows are not proof of an algorithmic gain.

## Reproduce

[Commands for rebuilding, rerunning and regenerating the report](REPRODUCE.md). The report regenerates from published raw data without private `results/` paths. `scripts/build_report.py --check` checks generated text/metrics and data invariants; `bench report check reports/substr-adaptive-search` checks native cycle blocks, links, placeholders and portable paths.
