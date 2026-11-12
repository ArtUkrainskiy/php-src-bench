# Edge cases: very small dictionaries and dense matches

- **1 key**: the new class takes 9.5 to 22 times as long as the fastest existing method.
- **4 keys**: 1.9 to 3.4 times as long. `Str\Matcher` and `Str\Replacer` are not meant for dictionaries this small, and the main tables leave them out.
- **Text dense with matches**: the new class is faster in every case, −92…−59%.

**How to read the tables.** "Change" columns: how much the time per call of `Str\Matcher` or `Str\Replacer` differs from the fastest existing method for the same input and mode, in percent. Negative = the new class is faster: −50% is twice as fast, −75% four times, −90% ten times. +100% is twice as slow. † = the processes disagree by more than 5%, the A/A control is off by more than 3%, a process was preempted more than 20 times a second, or the core was not idle; the values are in [data/results.json](data/results.json).

## Fewer than 8 keys

Texts are 4 KiB of English PHP documentation with one key written in.

| Input | Mode | Fastest existing method | Its time, µs | Change, GCC | Change, Clang |
|---|---|---|---:|---:|---:|
| 1 key, `matches()` | Prepared | PCRE alternation | 0.15 | +1707% | +2071% |
| 1 key, `matches()` | One-shot | `str_contains()` | 0.22 | +1368% | +1508%† |
| 1 key, `getMatchedKeywords()` | Prepared | `str_contains()` | 0.17 | +1508%† | +1785%† |
| 1 key, `getMatchedKeywords()` | One-shot | `str_contains()` | 0.24 | +1283% | +1474% |
| 1 key, `countMatches()` | Prepared | `strpos()` loop | 0.52 | +938% | +1108% |
| 1 key, `countMatches()` | One-shot | `strpos()` loop | 0.61 | +868% | +1012% |
| 1 key, `replace()` | Prepared | `preg_replace()`, shared prefixes | 0.34 | +1506% | +1718% |
| 1 key, `replace()` | One-shot | `strtr()` | 0.63 | +847% | +948% |
| 4 keys, `matches()` | Prepared | PCRE alternation | 0.95 | +196% | +245% |
| 4 keys, `matches()` | One-shot | PCRE alternation | 1.54 | +167% | +199% |
| 4 keys, `getMatchedKeywords()` | Prepared | `str_contains()` loop | 2.54 | +119% | +167% |
| 4 keys, `getMatchedKeywords()` | One-shot | `str_contains()` loop | 2.63 | +162% | +207% |
| 4 keys, `countMatches()` | Prepared | `strpos()` loop | 2.96 | +87% | +130% |
| 4 keys, `countMatches()` | One-shot | `substr_count()` loop | 3.05 | +125% | +166% |
| 4 keys, `replace()` | Prepared | PCRE, longest first | 2.05 | +173% | +210% |
| 4 keys, `replace()` | One-shot | PCRE, longest first | 2.79 | +148% | +178% |

## Texts dense with matches

128 frequent English words (ranks 101–228) on English text, so matches are close together.

| Input | Mode | Fastest existing method | Its time, µs | Change, GCC | Change, Clang |
|---|---|---|---:|---:|---:|
| `getMatchedKeywords()`, 4 KiB | Prepared | `str_contains()` loop | 88.8 | −91% | −90% |
| `getMatchedKeywords()`, 4 KiB | One-shot | `str_contains()` loop | 89.2 | −62% | −59% |
| `getMatchedKeywords()`, 64 KiB | Prepared | `str_contains()` loop | 775 | −86% | −84% |
| `getMatchedKeywords()`, 64 KiB | One-shot | `str_contains()` loop | 777 | −82% | −80% |
| `countMatches()`, 4 KiB | Prepared | PCRE, shared prefixes | 85.8 | −92% | −91% |
| `countMatches()`, 4 KiB | One-shot | `substr_count()` loop | 102 | −68% | −66% |
| `countMatches()`, 64 KiB | Prepared | PCRE, shared prefixes | 1,353 | −92% | −91% |
| `countMatches()`, 64 KiB | One-shot | PCRE, shared prefixes | 1,481 | −91% | −90% |
| `matchAll()`, 4 KiB | Prepared | PCRE, shared prefixes | 91.9 | −89% | −87% |
| `matchAll()`, 4 KiB | One-shot | `strpos()` loop | 106 | −66% | −63% |
| `matchAll()`, 64 KiB | Prepared | PCRE, shared prefixes | 1,475 | −89% | −87% |
| `matchAll()`, 64 KiB | One-shot | PCRE, shared prefixes | 1,607 | −88% | −86% |
| `replace()`, 4 KiB | Prepared | PCRE, shared prefixes | 55.5 | −84% | −83% |
| `replace()`, 4 KiB | One-shot | PCRE, longest first | 131 | −76% | −72% |
| `replace()`, 64 KiB | Prepared | PCRE, shared prefixes | 868 | −81% | −79% |
| `replace()`, 64 KiB | One-shot | PCRE, shared prefixes | 988 | −80% | −79% |
