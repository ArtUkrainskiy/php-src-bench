# Inputs and verification scope

Matcher correctness is checked on 601 saved inputs. Time is measured for the 64 inputs used in the summary and appendices. Replacer: 71 inputs with checks of the result and replacement count. The number of inputs describes the controlled set, not the frequency of tasks in applications.

For getMatchedKeywords(), countMatches() and matchAll(), corresponding rows use identical texts and ordered dictionaries. The length series fixes one occurrence and one dictionary of 128 keys. Other profiles state the total occurrence count and the number of unique matched keys.

| Method | Input | JSON |
|---|---|---|
| `Matcher::matches()` | 128 B; dictionary of 8 keys; key lengths 12 B; no matches | [text, dictionary and reference](inputs/cases/any/presence.any.bytes128.keys8.absent.rank5.json) |
| `Matcher::matches()` | 128 B; dictionary of 128 keys; key lengths 12 B; no matches | [text, dictionary and reference](inputs/cases/any/presence.any.bytes128.keys128.absent.rank65.json) |
| `Matcher::matches()` | 1024 B; dictionary of 16 keys; key lengths 12 B; no matches | [text, dictionary and reference](inputs/cases/any/presence.any.bytes1024.keys16.absent.rank9.json) |
| `Matcher::matches()` | 4096 B; dictionary of 128 keys; key lengths 12 B; no matches | [text, dictionary and reference](inputs/cases/any/presence.any.bytes4096.keys128.absent.rank65.json) |
| `Matcher::matches()` | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 8, dictionary key #65 | [text, dictionary and reference](inputs/cases/any/presence.any.bytes4096.keys128.start.rank65.json) |
| `Matcher::matches()` | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 2042, dictionary key #65 | [text, dictionary and reference](inputs/cases/any/presence.any.bytes4096.keys128.middle.rank65.json) |
| `Matcher::matches()` | 4096 B; dictionary of 128 keys; key lengths 12 B; match: byte 4076, dictionary key #65 | [text, dictionary and reference](inputs/cases/any/presence.any.bytes4096.keys128.end.rank65.json) |
| `Matcher::matches()` | 16384 B; dictionary of 256 keys; key lengths 12 B; no matches | [text, dictionary and reference](inputs/cases/any/presence.any.bytes16384.keys256.absent.rank129.json) |
| `Matcher::matches()` | 32768 B; dictionary of 1024 keys; key lengths 12 B; no matches | [text, dictionary and reference](inputs/cases/any/presence.any.bytes32768.keys1024.absent.rank513.json) |
| `Matcher::matches()` | 65536 B; dictionary of 1024 keys; key lengths 12 B; no matches | [text, dictionary and reference](inputs/cases/any/presence.any.bytes65536.keys1024.absent.rank513.json) |
| `Matcher::matches()` | 65536 B; dictionary of 10000 keys; key lengths 12 B; no matches | [text, dictionary and reference](inputs/cases/any/presence.any.bytes65536.keys10000.absent.rank5001.json) |
| `Matcher::matches()` | 4096 B; dictionary of 32 keys; key lengths 12 B; match: byte 4076, dictionary key #1 | [text, dictionary and reference](inputs/cases/any/fixed_rank.any.bytes4096.keys32.end.rank1.json) |
| `Matcher::matches()` | 4096 B; dictionary of 256 keys; key lengths 12 B; match: byte 4076, dictionary key #1 | [text, dictionary and reference](inputs/cases/any/fixed_rank.any.bytes4096.keys256.end.rank1.json) |
| `Matcher::matches()` | 4096 B; dictionary of 10000 keys; key lengths 12 B; match: byte 8, dictionary key #1 | [text, dictionary and reference](inputs/cases/any/fixed_rank.any.bytes4096.keys10000.start.rank1.json) |
| `Matcher::getMatchedKeywords()` | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | [text, dictionary and reference](inputs/cases/unique/results.unique.bytes128.keys128.one.json) |
| `Matcher::getMatchedKeywords()` | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | [text, dictionary and reference](inputs/cases/unique/results.unique.bytes128.keys10000.absent.json) |
| `Matcher::getMatchedKeywords()` | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | [text, dictionary and reference](inputs/cases/unique/results.unique.bytes128.keys10000.one.json) |
| `Matcher::getMatchedKeywords()` | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | [text, dictionary and reference](inputs/cases/unique/results.unique.bytes1024.keys128.one.json) |
| `Matcher::getMatchedKeywords()` | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | [text, dictionary and reference](inputs/cases/unique/results.unique.bytes4096.keys8.one.json) |
| `Matcher::getMatchedKeywords()` | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | [text, dictionary and reference](inputs/cases/unique/results.unique.bytes4096.keys128.absent.json) |
| `Matcher::getMatchedKeywords()` | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | [text, dictionary and reference](inputs/cases/unique/results.unique.bytes4096.keys128.one.json) |
| `Matcher::getMatchedKeywords()` | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | [text, dictionary and reference](inputs/cases/unique/results.unique.bytes4096.keys128.sparse.json) |
| `Matcher::getMatchedKeywords()` | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | [text, dictionary and reference](inputs/cases/unique/results.unique.bytes4096.keys10000.one.json) |
| `Matcher::getMatchedKeywords()` | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | [text, dictionary and reference](inputs/cases/unique/results.unique.bytes16384.keys128.one.json) |
| `Matcher::getMatchedKeywords()` | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | [text, dictionary and reference](inputs/cases/unique/results.unique.bytes32768.keys128.one.json) |
| `Matcher::getMatchedKeywords()` | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 16; unique matched keys: 8 | [text, dictionary and reference](inputs/cases/unique/results.unique.bytes65536.keys8.sparse.json) |
| `Matcher::getMatchedKeywords()` | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | [text, dictionary and reference](inputs/cases/unique/results.unique.bytes65536.keys128.one.json) |
| `Matcher::getMatchedKeywords()` | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | [text, dictionary and reference](inputs/cases/unique/repeat.unique.bytes4096.keys128.sparse-one-key.json) |
| `Matcher::getMatchedKeywords()` | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | [text, dictionary and reference](inputs/cases/unique/fixed_density.unique.bytes65536.keys128.one-per-kib.json) |
| `Matcher::countMatches()` | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | [text, dictionary and reference](inputs/cases/count/results.count.bytes128.keys128.one.json) |
| `Matcher::countMatches()` | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | [text, dictionary and reference](inputs/cases/count/results.count.bytes128.keys10000.absent.json) |
| `Matcher::countMatches()` | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | [text, dictionary and reference](inputs/cases/count/results.count.bytes1024.keys128.one.json) |
| `Matcher::countMatches()` | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | [text, dictionary and reference](inputs/cases/count/results.count.bytes4096.keys8.one.json) |
| `Matcher::countMatches()` | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | [text, dictionary and reference](inputs/cases/count/results.count.bytes4096.keys128.absent.json) |
| `Matcher::countMatches()` | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | [text, dictionary and reference](inputs/cases/count/results.count.bytes4096.keys128.one.json) |
| `Matcher::countMatches()` | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | [text, dictionary and reference](inputs/cases/count/results.count.bytes4096.keys128.sparse.json) |
| `Matcher::countMatches()` | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | [text, dictionary and reference](inputs/cases/count/results.count.bytes4096.keys10000.one.json) |
| `Matcher::countMatches()` | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | [text, dictionary and reference](inputs/cases/count/results.count.bytes16384.keys128.one.json) |
| `Matcher::countMatches()` | 32768 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | [text, dictionary and reference](inputs/cases/count/results.count.bytes32768.keys8.one.json) |
| `Matcher::countMatches()` | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | [text, dictionary and reference](inputs/cases/count/results.count.bytes32768.keys128.one.json) |
| `Matcher::countMatches()` | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | [text, dictionary and reference](inputs/cases/count/results.count.bytes65536.keys8.one.json) |
| `Matcher::countMatches()` | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | [text, dictionary and reference](inputs/cases/count/results.count.bytes65536.keys128.one.json) |
| `Matcher::countMatches()` | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | [text, dictionary and reference](inputs/cases/count/repeat.count.bytes4096.keys128.sparse-one-key.json) |
| `Matcher::countMatches()` | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | [text, dictionary and reference](inputs/cases/count/fixed_density.count.bytes65536.keys128.one-per-kib.json) |
| `Matcher::matchAll()` | 128 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | [text, dictionary and reference](inputs/cases/all/results.all.bytes128.keys128.one.json) |
| `Matcher::matchAll()` | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | [text, dictionary and reference](inputs/cases/all/results.all.bytes128.keys10000.absent.json) |
| `Matcher::matchAll()` | 128 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | [text, dictionary and reference](inputs/cases/all/results.all.bytes128.keys10000.one.json) |
| `Matcher::matchAll()` | 1024 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | [text, dictionary and reference](inputs/cases/all/results.all.bytes1024.keys128.one.json) |
| `Matcher::matchAll()` | 4096 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | [text, dictionary and reference](inputs/cases/all/results.all.bytes4096.keys8.one.json) |
| `Matcher::matchAll()` | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | [text, dictionary and reference](inputs/cases/all/results.all.bytes4096.keys128.absent.json) |
| `Matcher::matchAll()` | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | [text, dictionary and reference](inputs/cases/all/results.all.bytes4096.keys128.one.json) |
| `Matcher::matchAll()` | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 4 | [text, dictionary and reference](inputs/cases/all/results.all.bytes4096.keys128.sparse.json) |
| `Matcher::matchAll()` | 4096 B; dictionary of 10000 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | [text, dictionary and reference](inputs/cases/all/results.all.bytes4096.keys10000.one.json) |
| `Matcher::matchAll()` | 16384 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | [text, dictionary and reference](inputs/cases/all/results.all.bytes16384.keys128.one.json) |
| `Matcher::matchAll()` | 32768 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | [text, dictionary and reference](inputs/cases/all/results.all.bytes32768.keys128.one.json) |
| `Matcher::matchAll()` | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 0; unique matched keys: 0 | [text, dictionary and reference](inputs/cases/all/results.all.bytes65536.keys8.absent.json) |
| `Matcher::matchAll()` | 65536 B; dictionary of 8 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | [text, dictionary and reference](inputs/cases/all/results.all.bytes65536.keys8.one.json) |
| `Matcher::matchAll()` | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 1; unique matched keys: 1 | [text, dictionary and reference](inputs/cases/all/results.all.bytes65536.keys128.one.json) |
| `Matcher::matchAll()` | 65536 B; dictionary of 1024 keys; key lengths 12 B; occurrences: 16; unique matched keys: 16 | [text, dictionary and reference](inputs/cases/all/results.all.bytes65536.keys1024.sparse.json) |
| `Matcher::matchAll()` | 4096 B; dictionary of 128 keys; key lengths 12 B; occurrences: 4; unique matched keys: 1 | [text, dictionary and reference](inputs/cases/all/repeat.all.bytes4096.keys128.sparse-one-key.json) |
| `Matcher::matchAll()` | 65536 B; dictionary of 128 keys; key lengths 12 B; occurrences: 64; unique matched keys: 4 | [text, dictionary and reference](inputs/cases/all/fixed_density.all.bytes65536.keys128.one-per-kib.json) |
| `Matcher::matches()` | 1393 B; dictionary of 128 keys; key lengths 3–30 B; no matches | [text, dictionary and reference](inputs/cases/examples/example.posts.en.absent.json) |
| `Matcher::matches()` | 1337 B; dictionary of 128 keys; key lengths 3–30 B; match: byte 438, dictionary key #1 | [text, dictionary and reference](inputs/cases/examples/example.posts.en.positive.json) |
| `Matcher::getMatchedKeywords()` | 12828 B; dictionary of 128 keys; key lengths 4–28 B; occurrences: 23; unique matched keys: 12 | [text, dictionary and reference](inputs/cases/examples/example.articles.en.unique.json) |
| `Replacer::replace()` | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | [text, dictionary and reference](replacer-inputs/natural.b4096.n16.active0.equal.json) |
| `Replacer::replace()` | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | [text, dictionary and reference](replacer-inputs/natural.b4096.n16.active0.mixed.json) |
| `Replacer::replace()` | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | [text, dictionary and reference](replacer-inputs/natural.b4096.n16.active8.equal.json) |
| `Replacer::replace()` | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | [text, dictionary and reference](replacer-inputs/natural.b4096.n16.active8.mixed.json) |
| `Replacer::replace()` | 4096 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | [text, dictionary and reference](replacer-inputs/natural.b4096.n16.active16.equal.json) |
| `Replacer::replace()` | 4096 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | [text, dictionary and reference](replacer-inputs/natural.b4096.n16.active16.mixed.json) |
| `Replacer::replace()` | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | [text, dictionary and reference](replacer-inputs/natural.b4096.n32.active0.equal.json) |
| `Replacer::replace()` | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | [text, dictionary and reference](replacer-inputs/natural.b4096.n32.active0.mixed.json) |
| `Replacer::replace()` | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | [text, dictionary and reference](replacer-inputs/natural.b4096.n32.active16.equal.json) |
| `Replacer::replace()` | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | [text, dictionary and reference](replacer-inputs/natural.b4096.n32.active16.mixed.json) |
| `Replacer::replace()` | 4096 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | [text, dictionary and reference](replacer-inputs/natural.b4096.n32.active32.equal.json) |
| `Replacer::replace()` | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | [text, dictionary and reference](replacer-inputs/natural.b4096.n32.active32.mixed.json) |
| `Replacer::replace()` | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | [text, dictionary and reference](replacer-inputs/single.b4096.keybytes8.hits1.json) |
| `Replacer::replace()` | 4096 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | [text, dictionary and reference](replacer-inputs/single.b4096.keybytes8.hits5.json) |
| `Replacer::replace()` | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | [text, dictionary and reference](replacer-inputs/single.b4096.keybytes24.hits1.json) |
| `Replacer::replace()` | 4096 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | [text, dictionary and reference](replacer-inputs/single.b4096.keybytes24.hits5.json) |
| `Replacer::replace()` | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 3856 B | [text, dictionary and reference](replacer-inputs/output.b4096.n32.active16.mixed.short.json) |
| `Replacer::replace()` | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 4608 B | [text, dictionary and reference](replacer-inputs/output.b4096.n32.active16.mixed.long.json) |
| `Replacer::replace()` | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 4000 B | [text, dictionary and reference](replacer-inputs/output.b4096.n32.active16.mixed.marker.json) |
| `Replacer::replace()` | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 0 | [text, dictionary and reference](replacer-inputs/natural.b16384.n16.active0.equal.json) |
| `Replacer::replace()` | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 0 | [text, dictionary and reference](replacer-inputs/natural.b16384.n16.active0.mixed.json) |
| `Replacer::replace()` | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 8 | [text, dictionary and reference](replacer-inputs/natural.b16384.n16.active8.equal.json) |
| `Replacer::replace()` | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 8 | [text, dictionary and reference](replacer-inputs/natural.b16384.n16.active8.mixed.json) |
| `Replacer::replace()` | 16384 B; dictionary of 16 keys; key lengths 16 B; replacements: 16 | [text, dictionary and reference](replacer-inputs/natural.b16384.n16.active16.equal.json) |
| `Replacer::replace()` | 16384 B; dictionary of 16 keys; key lengths 11–21 B; replacements: 16 | [text, dictionary and reference](replacer-inputs/natural.b16384.n16.active16.mixed.json) |
| `Replacer::replace()` | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 0 | [text, dictionary and reference](replacer-inputs/natural.b16384.n32.active0.equal.json) |
| `Replacer::replace()` | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 0 | [text, dictionary and reference](replacer-inputs/natural.b16384.n32.active0.mixed.json) |
| `Replacer::replace()` | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 16 | [text, dictionary and reference](replacer-inputs/natural.b16384.n32.active16.equal.json) |
| `Replacer::replace()` | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16 | [text, dictionary and reference](replacer-inputs/natural.b16384.n32.active16.mixed.json) |
| `Replacer::replace()` | 16384 B; dictionary of 32 keys; key lengths 16 B; replacements: 32 | [text, dictionary and reference](replacer-inputs/natural.b16384.n32.active32.equal.json) |
| `Replacer::replace()` | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 32 | [text, dictionary and reference](replacer-inputs/natural.b16384.n32.active32.mixed.json) |
| `Replacer::replace()` | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 1 | [text, dictionary and reference](replacer-inputs/single.b16384.keybytes8.hits1.json) |
| `Replacer::replace()` | 16384 B; dictionary of 1 key; key lengths 8 B; replacements: 5 | [text, dictionary and reference](replacer-inputs/single.b16384.keybytes8.hits5.json) |
| `Replacer::replace()` | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 1 | [text, dictionary and reference](replacer-inputs/single.b16384.keybytes24.hits1.json) |
| `Replacer::replace()` | 16384 B; dictionary of 1 key; key lengths 24 B; replacements: 5 | [text, dictionary and reference](replacer-inputs/single.b16384.keybytes24.hits5.json) |
| `Replacer::replace()` | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16144 B | [text, dictionary and reference](replacer-inputs/output.b16384.n32.active16.mixed.short.json) |
| `Replacer::replace()` | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; output 16896 B | [text, dictionary and reference](replacer-inputs/output.b16384.n32.active16.mixed.long.json) |
| `Replacer::replace()` | 16384 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 16; one replacement value; output 16288 B | [text, dictionary and reference](replacer-inputs/output.b16384.n32.active16.mixed.marker.json) |
| `Replacer::replace()` | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100; keys {{…}} | [text, dictionary and reference](replacer-inputs/large.b1048576.n1000.active10pct.mixed.json) |
| `Replacer::replace()` | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000; keys {{…}} | [text, dictionary and reference](replacer-inputs/large.b1048576.n10000.active10pct.mixed.json) |
| `Replacer::replace()` | 820 B; dictionary of 10 keys; key lengths 13–20 B; replacements: 11; keys {{…}}; output 860 B | [text, dictionary and reference](replacer-inputs/example.order.email.json) |
| `Replacer::replace()` | 7301 B; dictionary of 128 keys; key lengths 4–28 B; replacements: 4; output 7372 B | [text, dictionary and reference](replacer-inputs/example.links.en.json) |
| `Replacer::replace()` | 8607 B; dictionary of 64 keys; key lengths 30–69 B; replacements: 9; output 8454 B | [text, dictionary and reference](replacer-inputs/example.pages.en.original.json) |
| `Replacer::replace()` | 69643 B; dictionary of 24 keys; key lengths 24 B; replacements: 3; one replacement value; output 69601 B | [text, dictionary and reference](replacer-inputs/example.logs.keys24.hits3.json) |
| `Replacer::replace()` | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 0 | [text, dictionary and reference](replacer-inputs/generic.b1048576.n1000.active0pct.equal.json) |
| `Replacer::replace()` | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 10 | [text, dictionary and reference](replacer-inputs/generic.b1048576.n1000.active1pct.equal.json) |
| `Replacer::replace()` | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 100 | [text, dictionary and reference](replacer-inputs/generic.b1048576.n1000.active10pct.equal.json) |
| `Replacer::replace()` | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 500 | [text, dictionary and reference](replacer-inputs/generic.b1048576.n1000.active50pct.equal.json) |
| `Replacer::replace()` | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 750 | [text, dictionary and reference](replacer-inputs/generic.b1048576.n1000.active75pct.equal.json) |
| `Replacer::replace()` | 1048576 B; dictionary of 1000 keys; key lengths 16 B; replacements: 1000 | [text, dictionary and reference](replacer-inputs/generic.b1048576.n1000.active100pct.equal.json) |
| `Replacer::replace()` | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 0 | [text, dictionary and reference](replacer-inputs/generic.b1048576.n1000.active0pct.mixed.json) |
| `Replacer::replace()` | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 10 | [text, dictionary and reference](replacer-inputs/generic.b1048576.n1000.active1pct.mixed.json) |
| `Replacer::replace()` | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 100 | [text, dictionary and reference](replacer-inputs/generic.b1048576.n1000.active10pct.mixed.json) |
| `Replacer::replace()` | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 500 | [text, dictionary and reference](replacer-inputs/generic.b1048576.n1000.active50pct.mixed.json) |
| `Replacer::replace()` | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 750 | [text, dictionary and reference](replacer-inputs/generic.b1048576.n1000.active75pct.mixed.json) |
| `Replacer::replace()` | 1048576 B; dictionary of 1000 keys; key lengths 8–24 B; replacements: 1000 | [text, dictionary and reference](replacer-inputs/generic.b1048576.n1000.active100pct.mixed.json) |
| `Replacer::replace()` | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 0 | [text, dictionary and reference](replacer-inputs/generic.b1048576.n10000.active0pct.equal.json) |
| `Replacer::replace()` | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 100 | [text, dictionary and reference](replacer-inputs/generic.b1048576.n10000.active1pct.equal.json) |
| `Replacer::replace()` | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 1000 | [text, dictionary and reference](replacer-inputs/generic.b1048576.n10000.active10pct.equal.json) |
| `Replacer::replace()` | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 5000 | [text, dictionary and reference](replacer-inputs/generic.b1048576.n10000.active50pct.equal.json) |
| `Replacer::replace()` | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 7500 | [text, dictionary and reference](replacer-inputs/generic.b1048576.n10000.active75pct.equal.json) |
| `Replacer::replace()` | 1048576 B; dictionary of 10000 keys; key lengths 16 B; replacements: 10000 | [text, dictionary and reference](replacer-inputs/generic.b1048576.n10000.active100pct.equal.json) |
| `Replacer::replace()` | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 0 | [text, dictionary and reference](replacer-inputs/generic.b1048576.n10000.active0pct.mixed.json) |
| `Replacer::replace()` | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 100 | [text, dictionary and reference](replacer-inputs/generic.b1048576.n10000.active1pct.mixed.json) |
| `Replacer::replace()` | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 1000 | [text, dictionary and reference](replacer-inputs/generic.b1048576.n10000.active10pct.mixed.json) |
| `Replacer::replace()` | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 5000 | [text, dictionary and reference](replacer-inputs/generic.b1048576.n10000.active50pct.mixed.json) |
| `Replacer::replace()` | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 7500 | [text, dictionary and reference](replacer-inputs/generic.b1048576.n10000.active75pct.mixed.json) |
| `Replacer::replace()` | 1048576 B; dictionary of 10000 keys; key lengths 8–24 B; replacements: 10000 | [text, dictionary and reference](replacer-inputs/generic.b1048576.n10000.active100pct.mixed.json) |
| `Replacer::replace()` | 4096 B; dictionary of 32 keys; key lengths 11–21 B; replacements: 2 | [text, dictionary and reference](replacer-inputs/natural.b4096.n32.active2.mixed.json) |

## Replacer supplement: 1 KiB

The same dictionary of 32 keys as in the mixed-length 4/16 KiB series. Two separate texts with 0 and 2 replacements. Each result is measured separately. [Saved input metadata](data/replacer-1k-inputs.json).

- [natural.b1024.n32.active0.mixed](replacer-inputs/natural.b1024.n32.active0.mixed.json): 1024 B, 32 keys, 0 replacements.
- [natural.b1024.n32.active2.mixed](replacer-inputs/natural.b1024.n32.active2.mixed.json): 1024 B, 32 keys, 2 replacements.
