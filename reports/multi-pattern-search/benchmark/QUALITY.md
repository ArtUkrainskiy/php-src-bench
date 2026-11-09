# Quality control

† marks a flagged observation. Its observed time and relative change remain visible; measured variability is listed below. A counter flag does not change the status of the independent elapsed-time measurement. Full samples and A/A: [elapsed.json.gz](data/elapsed.json.gz).

| Compiler | Input | Mode | Reason |
|---|---|---|---|
| gcc15 | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 8, dictionary key #65 | prepared | spread:matcher,matcher_aa |
| gcc15 | 4096 B; dictionary of 256 keys; key lengths 12 B; match: byte 4076, dictionary key #1 | prepared | spread:preg_match_chunks |
| clang21 | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | spread:matcher |
| clang21 | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | spread:matcher,matcher_aa |
| clang21 | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | oneshot | spread:matcher |
| clang21 | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | prepared | spread:matcher,matcher_aa |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | prepared | aa-outside-2-percent |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | prepared | aa-outside-2-percent |
| gcc15 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | prepared | spread:preg_replace_callback,preg_trie_callback,preg_chunked_callback,preg_replace,preg_trie_constant,preg_chunked_constant |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | prepared | spread:preg_replace_callback,preg_trie_callback,preg_chunked_callback,preg_replace,preg_trie_constant,preg_chunked_constant,replacer_aa |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | oneshot | spread:replacer,replacer_aa |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | prepared | spread:replacer,replacer_new,replacer_aa,oneshot_aa |
| clang21 | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | oneshot | spread:replacer,replacer_new,replacer_aa,oneshot_aa |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000; keys {{…}} | prepared | aa-outside-2-percent, spread:strtr,preg_chunked_callback,preg_delimited_callback,oneshot_aa |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000; keys {{…}} | oneshot | aa-outside-2-percent, spread:strtr,preg_chunked_callback,preg_delimited_callback,oneshot_aa |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000; keys {{…}} | prepared | aa-outside-2-percent, spread:strtr,preg_chunked_callback,oneshot_aa |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000; keys {{…}} | oneshot | aa-outside-2-percent, spread:strtr,preg_chunked_callback,oneshot_aa |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 100 | oneshot | spread:oneshot_aa |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 100 | oneshot | spread:oneshot_aa |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 500 | oneshot | spread:oneshot_aa |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 500 | oneshot | spread:oneshot_aa |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100 | oneshot | spread:oneshot_aa |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100 | oneshot | spread:oneshot_aa |
| gcc15 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 500 | oneshot | spread:oneshot_aa |
| clang21 | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 500 | oneshot | spread:oneshot_aa |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 100 | prepared | spread:strtr |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 100 | oneshot | spread:strtr |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 100 | prepared | spread:strtr |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 100 | oneshot | spread:strtr |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 1000 | prepared | spread:strtr,replacer_aa |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 1000 | oneshot | spread:strtr,replacer_aa |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 1000 | prepared | spread:strtr,replacer |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 1000 | oneshot | spread:strtr,replacer |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 5000 | prepared | spread:strtr |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 5000 | oneshot | spread:strtr |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 5000 | prepared | spread:strtr |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 5000 | oneshot | spread:strtr |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 7500 | prepared | spread:strtr,replacer |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 7500 | oneshot | spread:strtr,replacer |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 7500 | prepared | spread:strtr,replacer_aa |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 7500 | oneshot | spread:strtr,replacer_aa |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 10000 | prepared | spread:strtr |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 10000 | oneshot | spread:strtr |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 5000 | prepared | spread:replacer,replacer_aa |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 5000 | prepared | spread:replacer,replacer_aa |
| gcc15 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 7500 | prepared | spread:replacer |
| clang21 | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 7500 | prepared | spread:replacer |

## Replacer supplement: 1 KiB

| Compiler | Replacements | Prepared object | One-shot call |
|---|---:|---|---|
| gcc15 | 0 | checks passed | checks passed |
| gcc15 | 2 | checks passed | checks passed |
| clang21 | 0 | checks passed | checks passed |
| clang21 | 2 | checks passed | checks passed |

## Clang summary

In the full Clang tables, 11 prepared-object comparisons and 13 one-shot comparisons did not pass the quality checks — out of 135 inputs in each mode. Only one comparison exceeded the A/A threshold. Results marked † retain their observed percentages or multiples; the quality register quantifies the issue.

## Measured variability

Spread is the maximum absolute sample deviation from its own median. A/A is the measured difference between identical calls. Flagged results retain the observed time and relative change.

| Compiler | Exact input | Mode | A/A | Sample spread by implementation |
|---|---|---|---:|---|
| gcc15 | `presence.any.bytes4096.keys128.start.rank65` | prepared | +0.61% | contains_loop: 0.93%, preg_match_chunks: 1.70%, matcher: 12.53%, matcher_aa: 8.88% |
| gcc15 | `fixed_rank.any.bytes4096.keys256.end.rank1` | prepared | -0.12% | contains_loop: 0.51%, preg_match_chunks: 24.31%, matcher: 0.26%, matcher_aa: 0.33% |
| clang21 | `results.unique.bytes1024.keys128.one` | prepared | +0.16% | strpos_unique: 0.89%, preg_grouped_unique: 0.31%, matcher: 5.58%, matcher_aa: 4.90% |
| clang21 | `results.unique.bytes16384.keys128.one` | oneshot | -0.29% | strpos_unique: 0.60%, preg_grouped_unique: 0.30%, matcher: 10.54%, matcher_aa: 10.71% |
| clang21 | `results.count.bytes65536.keys8.one` | oneshot | -0.13% | strpos_count: 0.73%, preg_grouped_count: 1.21%, matcher: 6.20%, matcher_aa: 0.30% |
| clang21 | `results.all.bytes4096.keys8.one` | prepared | -0.28% | strpos_all: 1.33%, preg_grouped_all: 1.19%, matcher: 5.27%, matcher_aa: 5.28% |
| gcc15 | `single.b16384.keybytes8.hits1` | prepared | -2.15% | replacer_aa: 1.78%, strtr: 1.78%, str_replace: 1.38%, preg_trie_constant: 0.41%, preg_chunked_constant: 0.54%, replacer: 4.44% |
| gcc15 | `single.b16384.keybytes8.hits1` | oneshot | -0.28% | oneshot_aa: 4.02%, strtr: 1.78%, str_replace: 1.38%, preg_trie_constant: 0.41%, preg_chunked_constant: 0.54%, replacer_new: 1.23% |
| gcc15 | `single.b16384.keybytes8.hits5` | prepared | -2.27% | replacer_aa: 1.72%, strtr: 1.94%, str_replace: 1.91%, preg_trie_constant: 0.42%, preg_chunked_constant: 0.54%, replacer: 2.80% |
| gcc15 | `single.b16384.keybytes8.hits5` | oneshot | -0.35% | oneshot_aa: 3.45%, strtr: 1.94%, str_replace: 1.91%, preg_trie_constant: 0.42%, preg_chunked_constant: 0.54%, replacer_new: 1.84% |
| gcc15 | `single.b16384.keybytes24.hits1` | prepared | -0.53% | strtr: 0.48%, str_replace: 1.15%, preg_replace_callback: 8.06%, preg_trie_callback: 7.45%, preg_chunked_callback: 8.13%, replacer: 1.09%, preg_replace: 7.01%, preg_trie_constant: 7.02%, preg_chunked_constant: 7.33%, replacer_aa: 1.95% |
| clang21 | `single.b16384.keybytes24.hits1` | prepared | -0.36% | strtr: 0.74%, str_replace: 1.23%, preg_replace_callback: 8.17%, preg_trie_callback: 7.13%, preg_chunked_callback: 7.82%, replacer: 1.58%, preg_replace: 8.43%, preg_trie_constant: 7.76%, preg_chunked_constant: 7.58%, replacer_aa: 6.87% |
| clang21 | `single.b16384.keybytes24.hits1` | oneshot | -0.26% | strtr: 0.63%, str_replace: 0.93%, preg_replace_callback: 1.03%, preg_trie_callback: 0.75%, preg_chunked_callback: 0.70%, replacer: 7.27%, preg_replace: 0.89%, preg_trie_constant: 0.88%, preg_chunked_constant: 0.77%, replacer_aa: 7.69% |
| clang21 | `single.b16384.keybytes24.hits5` | prepared | -0.26% | replacer_aa: 6.55%, strtr: 0.56%, str_replace: 0.96%, preg_trie_constant: 0.97%, preg_chunked_constant: 0.77%, replacer: 6.56% |
| clang21 | `single.b16384.keybytes24.hits5` | oneshot | -0.06% | oneshot_aa: 6.56%, strtr: 0.56%, str_replace: 0.96%, preg_trie_constant: 0.97%, preg_chunked_constant: 0.77%, replacer_new: 6.49% |
| gcc15 | `large.b1048576.n10000.active10pct.mixed` | prepared | +4.35% | replacer_aa: 4.36%, strtr: 38.51%, preg_chunked_callback: 8.86%, preg_delimited_callback: 5.06%, replacer: 4.49% |
| gcc15 | `large.b1048576.n10000.active10pct.mixed` | oneshot | -0.27% | oneshot_aa: 19.74%, strtr: 38.51%, preg_chunked_callback: 8.86%, preg_delimited_callback: 5.06%, replacer_new: 0.62% |
| clang21 | `large.b1048576.n10000.active10pct.mixed` | prepared | +4.54% | replacer_aa: 4.48%, strtr: 41.02%, preg_chunked_callback: 8.22%, preg_delimited_callback: 4.69%, replacer: 4.42% |
| clang21 | `large.b1048576.n10000.active10pct.mixed` | oneshot | -0.19% | oneshot_aa: 20.01%, strtr: 41.02%, preg_chunked_callback: 8.22%, preg_delimited_callback: 4.69%, replacer_new: 4.03% |
| gcc15 | `generic.b1048576.n1000.active10pct.equal` | prepared | -0.29% | replacer_aa: 0.28%, strtr: 1.10%, preg_trie_callback: 3.70%, replacer: 1.73% |
| gcc15 | `generic.b1048576.n1000.active10pct.equal` | oneshot | -0.15% | oneshot_aa: 6.99%, strtr: 1.10%, preg_trie_callback: 3.70%, replacer_new: 0.47% |
| clang21 | `generic.b1048576.n1000.active10pct.equal` | prepared | -0.26% | replacer_aa: 0.43%, strtr: 0.85%, preg_trie_callback: 3.23%, replacer: 1.88% |
| clang21 | `generic.b1048576.n1000.active10pct.equal` | oneshot | -0.06% | oneshot_aa: 6.50%, strtr: 0.85%, preg_trie_callback: 3.23%, replacer_new: 0.52% |
| gcc15 | `generic.b1048576.n1000.active50pct.equal` | prepared | -0.32% | replacer_aa: 0.28%, strtr: 1.41%, preg_trie_callback: 3.70%, replacer: 1.98% |
| gcc15 | `generic.b1048576.n1000.active50pct.equal` | oneshot | -0.20% | oneshot_aa: 7.62%, strtr: 1.41%, preg_trie_callback: 3.70%, replacer_new: 0.96% |
| clang21 | `generic.b1048576.n1000.active50pct.equal` | prepared | -0.41% | replacer_aa: 0.82%, strtr: 0.87%, preg_trie_callback: 3.26%, replacer: 1.98% |
| clang21 | `generic.b1048576.n1000.active50pct.equal` | oneshot | +0.02% | oneshot_aa: 7.91%, strtr: 0.87%, preg_trie_callback: 3.26%, replacer_new: 1.55% |
| gcc15 | `generic.b1048576.n1000.active10pct.mixed` | prepared | -1.14% | replacer_aa: 0.45%, strtr: 0.53%, preg_trie_callback: 3.47%, replacer: 1.79% |
| gcc15 | `generic.b1048576.n1000.active10pct.mixed` | oneshot | -0.19% | oneshot_aa: 7.05%, strtr: 0.53%, preg_trie_callback: 3.47%, replacer_new: 0.67% |
| clang21 | `generic.b1048576.n1000.active10pct.mixed` | prepared | -0.89% | replacer_aa: 0.29%, strtr: 0.48%, preg_trie_callback: 3.35%, replacer: 1.62% |
| clang21 | `generic.b1048576.n1000.active10pct.mixed` | oneshot | -0.10% | oneshot_aa: 7.28%, strtr: 0.48%, preg_trie_callback: 3.35%, replacer_new: 0.92% |
| gcc15 | `generic.b1048576.n1000.active50pct.mixed` | prepared | -0.12% | replacer_aa: 0.26%, strtr: 0.55%, preg_trie_callback: 3.62%, replacer: 1.82% |
| gcc15 | `generic.b1048576.n1000.active50pct.mixed` | oneshot | +0.06% | oneshot_aa: 7.58%, strtr: 0.55%, preg_trie_callback: 3.62%, replacer_new: 0.79% |
| clang21 | `generic.b1048576.n1000.active50pct.mixed` | prepared | -0.91% | replacer_aa: 0.35%, strtr: 0.57%, preg_trie_callback: 3.36%, replacer: 1.61% |
| clang21 | `generic.b1048576.n1000.active50pct.mixed` | oneshot | -0.09% | oneshot_aa: 8.15%, strtr: 0.57%, preg_trie_callback: 3.36%, replacer_new: 1.06% |
| gcc15 | `generic.b1048576.n10000.active1pct.equal` | prepared | -0.63% | replacer_aa: 4.30%, strtr: 9.07%, preg_chunked_callback: 1.46%, replacer: 4.71% |
| gcc15 | `generic.b1048576.n10000.active1pct.equal` | oneshot | +0.11% | oneshot_aa: 0.82%, strtr: 9.07%, preg_chunked_callback: 1.46%, replacer_new: 1.07% |
| clang21 | `generic.b1048576.n10000.active1pct.equal` | prepared | -0.50% | replacer_aa: 4.35%, strtr: 9.50%, preg_chunked_callback: 1.45%, replacer: 4.39% |
| clang21 | `generic.b1048576.n10000.active1pct.equal` | oneshot | -0.27% | oneshot_aa: 1.06%, strtr: 9.50%, preg_chunked_callback: 1.45%, replacer_new: 0.83% |
| gcc15 | `generic.b1048576.n10000.active10pct.equal` | prepared | -0.18% | replacer_aa: 5.49%, strtr: 9.48%, preg_chunked_callback: 1.78%, replacer: 4.40% |
| gcc15 | `generic.b1048576.n10000.active10pct.equal` | oneshot | -0.40% | oneshot_aa: 1.70%, strtr: 9.48%, preg_chunked_callback: 1.78%, replacer_new: 0.48% |
| clang21 | `generic.b1048576.n10000.active10pct.equal` | prepared | -0.21% | replacer_aa: 4.08%, strtr: 9.98%, preg_chunked_callback: 1.85%, replacer: 5.12% |
| clang21 | `generic.b1048576.n10000.active10pct.equal` | oneshot | -0.42% | oneshot_aa: 2.06%, strtr: 9.98%, preg_chunked_callback: 1.85%, replacer_new: 0.87% |
| gcc15 | `generic.b1048576.n10000.active50pct.equal` | prepared | -0.00% | replacer_aa: 4.58%, strtr: 9.90%, preg_chunked_callback: 2.00%, replacer: 4.93% |
| gcc15 | `generic.b1048576.n10000.active50pct.equal` | oneshot | -0.63% | oneshot_aa: 1.02%, strtr: 9.90%, preg_chunked_callback: 2.00%, replacer_new: 0.95% |
| clang21 | `generic.b1048576.n10000.active50pct.equal` | prepared | -0.12% | replacer_aa: 4.86%, strtr: 10.58%, preg_chunked_callback: 2.10%, replacer: 4.98% |
| clang21 | `generic.b1048576.n10000.active50pct.equal` | oneshot | -0.31% | oneshot_aa: 1.09%, strtr: 10.58%, preg_chunked_callback: 2.10%, replacer_new: 1.08% |
| gcc15 | `generic.b1048576.n10000.active75pct.equal` | prepared | -0.18% | replacer_aa: 5.00%, strtr: 10.26%, preg_chunked_callback: 2.00%, replacer: 5.38% |
| gcc15 | `generic.b1048576.n10000.active75pct.equal` | oneshot | -0.13% | oneshot_aa: 0.90%, strtr: 10.26%, preg_chunked_callback: 2.00%, replacer_new: 0.73% |
| clang21 | `generic.b1048576.n10000.active75pct.equal` | prepared | -0.03% | replacer_aa: 5.10%, strtr: 11.10%, preg_chunked_callback: 2.12%, replacer: 4.97% |
| clang21 | `generic.b1048576.n10000.active75pct.equal` | oneshot | -0.11% | oneshot_aa: 0.94%, strtr: 11.10%, preg_chunked_callback: 2.12%, replacer_new: 0.53% |
| gcc15 | `generic.b1048576.n10000.active100pct.equal` | prepared | -0.55% | replacer_aa: 1.17%, strtr: 5.08%, preg_chunked_callback: 1.08%, replacer: 1.08% |
| gcc15 | `generic.b1048576.n10000.active100pct.equal` | oneshot | -0.92% | oneshot_aa: 1.08%, strtr: 5.08%, preg_chunked_callback: 1.08%, replacer_new: 1.93% |
| gcc15 | `generic.b1048576.n10000.active50pct.mixed` | prepared | -0.22% | replacer_aa: 5.09%, strtr: 0.93%, preg_chunked_callback: 2.16%, replacer: 5.27% |
| gcc15 | `generic.b1048576.n10000.active50pct.mixed` | oneshot | -0.35% | oneshot_aa: 1.11%, strtr: 0.93%, preg_chunked_callback: 2.16%, replacer_new: 0.54% |
| clang21 | `generic.b1048576.n10000.active50pct.mixed` | prepared | -0.34% | replacer_aa: 5.14%, strtr: 0.98%, preg_chunked_callback: 2.08%, replacer: 5.23% |
| clang21 | `generic.b1048576.n10000.active50pct.mixed` | oneshot | -0.24% | oneshot_aa: 1.54%, strtr: 0.98%, preg_chunked_callback: 2.08%, replacer_new: 0.83% |
| gcc15 | `generic.b1048576.n10000.active75pct.mixed` | prepared | -0.22% | replacer_aa: 4.72%, strtr: 0.97%, preg_chunked_callback: 2.01%, replacer: 5.01% |
| gcc15 | `generic.b1048576.n10000.active75pct.mixed` | oneshot | -0.03% | oneshot_aa: 0.63%, strtr: 0.97%, preg_chunked_callback: 2.01%, replacer_new: 0.65% |
| clang21 | `generic.b1048576.n10000.active75pct.mixed` | prepared | -0.10% | replacer_aa: 4.93%, strtr: 0.98%, preg_chunked_callback: 2.09%, replacer: 5.43% |
| clang21 | `generic.b1048576.n10000.active75pct.mixed` | oneshot | -0.23% | oneshot_aa: 0.77%, strtr: 0.98%, preg_chunked_callback: 2.09%, replacer_new: 0.51% |
