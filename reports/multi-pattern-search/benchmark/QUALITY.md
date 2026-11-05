# Quality control

† marks a flagged observation; its percentage is not used. A counter flag does not change the status of the independent elapsed-time measurement. Full samples and A/A: [elapsed.json.gz](data/elapsed.json.gz).

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

In the full Clang tables, 11 prepared-object comparisons and 13 one-shot comparisons did not pass the quality checks — out of 135 inputs in each mode. Only one comparison exceeded the A/A threshold. Percentages are omitted for results marked †.
