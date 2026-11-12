# Searching for many keys at once: `Str\Matcher` and `Str\Replacer`

[PR #25122](https://github.com/php/php-src/pull/25122) proposes two classes for `ext/standard`, plus `Str\MatchResult` for results; they aren't in a released PHP yet.
They find or replace many literal keys in one pass over the text:

```php
$matcher = new Str\Matcher(['viagra', 'casino', 'free money']);
$matcher->matches($comment);   // also getMatchedKeywords(), countMatches(), matchAll()
(new Str\Replacer(['str_contains' => '<a href="…">str_contains</a>']))->replace($page);
```

The report compares them with the fastest existing way to do the same: a `str_contains()`/`strpos()` loop, `strtr()`, or a PCRE alternation.

Two modes:

- **Prepared**: a call on an object built earlier, once per worker in a long-running runtime or once before a loop over many texts. Under PHP-FPM an object lives for one request.
- **One-shot**: building the object and one call.

Main results, times with GCC:

- A prepared object with 32 keys or more is 1.9 to 16 times faster per call.
- One call on a short text is slower: on 128 B with 16 random keys the build and call take 4.19–4.58 µs, the fastest existing method 0.46–1.89 µs.
- One call pays for the build on longer texts: at 4 KiB with 128 random keys it changes the time by −67…−29%. On whole manual pages of 4–16 KiB, one auto-linking call with 128 or 512 names changes it by −72…−65%.
- One `replace()` with a large dictionary is slower than `strtr()`: +95…+751% with 1024 random keys on 1–4 KiB, +32…+502% with the 3,345 auto-linking names on pages of 1–16 KiB.
- `matches()` stops at the first match. Its time grows with the position of the match, not with the number of keys. With a match in the middle of 4 KiB a prepared call takes 2.86 µs with 16 keys and 2.96 µs with 1024, the fastest existing method 6.39 and 17.7 µs.
- The ranges above leave out a match in the first 64 bytes. There `matches()` and PCRE stop after a few bytes. Prepared, the new class takes 0.26–0.27 µs at any key count, PCRE 0.12–0.16 µs with 16 keys and 0.68–0.75 µs with 1024: the change is +58…+115% with 16 keys and −70…−61% with 1024. One-shot, the new class still builds its object, 4.43–392 µs. PCRE only builds its pattern string, 1.34–62.4 µs, and keeps the compiled pattern in its cache. One call changes the time by +221…+550%.

Detailed tables by question: [Where to look](#where-to-look).

## How it was compared

Every change compares the new class with the **fastest existing method** for the same call, text, keys and mode: change = new time ÷ its time − 1. Negative = the new class is faster: −50% is twice as fast, −90% ten times. The fastest method is picked per value, after the run, from these:

| Call | Existing methods |
|---|---|
| `matches()` | `str_contains()` loop, `preg_match()` |
| `getMatchedKeywords()` | `str_contains()` loop, `preg_match_all()` |
| `countMatches()` | `strpos()` loop, `substr_count()` loop, `preg_match_all()` |
| `matchAll()` | `strpos()` loop, `preg_match_all()` with offsets |
| `replace()` | `strtr()`, `preg_replace_callback()`, `preg_replace()` when every key has the same replacement |

PCRE is tried as a plain alternation and as one that shares key prefixes (`/cas(?:ino|h)/`). When case is ignored, the loops use `stripos()` or lowercase the text once. The code of every method: [METHOD.md](METHOD.md#existing-methods-in-code).

- Only methods that are right on every text compete. `str_replace()` is left out: it replaces inside text it has already replaced, so its output can differ from `strtr()`. For which keys, how many and every occurrence, PCRE uses a lookahead so that overlapping keys are found. An alternation that consumes matches took 2–25% less time in a probe but misses overlapping keys.
- Existing methods return the same keys, counts and offsets in a simpler form: plain arrays in any order, no `Str\MatchResult` objects. The new class pays for its full result. Results are sorted and compared outside the timer.
- Prepared: the object or the pattern strings exist before the timer. `strtr()` has no prepared form: its time includes processing the whole key array on every call.
- One-shot: the timer also covers building the object or the PCRE pattern string. Compiling the pattern isn't timed: PCRE keeps compiled patterns in its per-process cache.
- Calls go through a pool of different texts instead of repeating one. On one repeated text the new class ran 3–4 times faster, because the CPU learns its branches (an earlier version; the existing methods weren't probed).

[METHOD.md](METHOD.md) has the details, [REPRODUCE.md](REPRODUCE.md) the commands.

## Application scenarios

| Scenario | Texts | Median text | Keys | Texts with a match | Most matches in a text |
|---|---:|---:|---:|---:|---:|
| Moderation | 10,000 | 199 B | 403 | 20.5% | 14 |
| Bot detection | 10,000 | 118 B | 1,469 | 19.2% | 4 |
| Auto-linking | 4,153 | 597 B | 3,345 | 46.4% | 45 |

- **Moderation**: the literal substring check of moderation. [Civil Comments](https://huggingface.co/datasets/google/civil_comments) against the English [LDNOOBW](dictionaries/ldnoobw/ATTRIBUTION.md) list, ignoring ASCII case. No word boundaries, Unicode case folding or judgement of false positives.
- **Bot detection**: the literal patterns of [crawler-user-agents](https://github.com/monperrus/crawler-user-agents) against real User-Agent strings, mixed by the generator: 80% browsers picked by their observed weight in the source data, 20% crawler examples. The 10,000 texts hold 2,069 distinct strings; caching results per string is not modelled.
- **Auto-linking**: PHP manual pages as plain text, markup removed; `replace()` turns every function name that contains `_` into a link. Names without `_`, such as `strlen`, are not in the list. Existing links and identifier boundaries are not handled. With 3,345 names only `strtr()` competes for `replace()`: PCRE can't compile a replacement pattern this large.

Times are GCC, changes are GCC / Clang, both against the fastest existing method for that task and mode ([How it was compared](#how-it-was-compared)). A time is the time of a block of calls over the pool divided by the calls, not the latency of a median text. The last four rows are pages of 4–16 KiB, see [One call on long pages](#one-call-on-long-pages).
Calls to repay the build: 1 when a single call is already faster. Otherwise an estimate: build time ÷ prepared saving per call, with the existing method's one-time work counted as zero, which favours it.

| Task | Prepared, µs: fastest existing / new | Prepared change | One-shot, µs: fastest existing / new | One-shot change | Calls to repay the build, GCC / Clang |
|---|---:|---:|---:|---:|---:|
| Moderation: does a comment contain a listed word? `matches()` | 4.24 / 0.53 | −87% / −87% | 20.4 / 119 | +483% / +417% | 32 / 29 |
| Moderation: which listed words occur? `getMatchedKeywords()` | 8.54 / 0.64 | −93% / −93% | 26 / 119 | +359% / +304% | 16 / 14 |
| Bot detection: is this User-Agent a crawler? `matches()` | 3.15 / 0.27 | −92% / −91% | 32.7 / 1,019 | +3004% / +2873% | 354 / 350 |
| Bot detection: which crawler patterns match? `getMatchedKeywords()` | 3.84 / 0.33 | −91% / −91% | 35.8 / 1,013 | +2730% / +2604% | 289 / 287 |
| Auto-linking, all pages, 3,345 names: link them `replace()` | 363 / 2.99 | −99% / −99% | 345 / 3,169 | +851% / +796% | 9 / 9 |
| Auto-linking, all pages, 3,345 names: every name with its offset `matchAll()` | 27.1 / 2.07 | −93% / −92% | 622 / 1,642 | +164% / +169% | 66 / 63 |
| Auto-linking, all pages, 3,345 names: which names occur? `getMatchedKeywords()` | 27.3 / 2.03 | −93% / −92% | 618 / 1,651 | +167% / +177% | 66 / 63 |
| Auto-linking, 4–16 KiB pages, 128 names: link them `replace()` | 47.2 / 10.6 | −78% / −75% | 181 / 59.4 | −67% / −65% | 1 / 1 |
| Auto-linking, 4–16 KiB pages, 128 names: every name with its offset `matchAll()` | 51 / 9.57 | −81% / −78% | 176 / 49.5 | −72% / −69% | 1 / 1 |
| Auto-linking, 4–16 KiB pages, 512 names: link them `replace()` | 55.6 / 12.6 | −77% / −75% | 1,204 / 353 | −71%† / −70% | 1 / 1 |
| Auto-linking, 4–16 KiB pages, 512 names: every name with its offset `matchAll()` | 72 / 9.88 | −86% / −84% | 678 / 232 | −66%† / −67%† | 1 / 1 |

### One call on long pages

The auto-linking task on whole manual pages, grouped by length. The dictionary is the full list of 3,345 names or a random subset of 128 or 512 of them. The groups hold 726, 231 and 91 pages with a median length of 1.3, 2.6 and 5.6 KiB. Pages under 1 KiB and the 9 over 16 KiB are left out. Pages with at least one name, by group: 128 names 6, 6, 7%; 512 names 20, 24, 27%; 3,345 names 60, 67, 65%.

Build and one call, change against the fastest existing method, GCC / Clang:

| Names | Call | 1–2 KiB | 2–4 KiB | 4–16 KiB |
|---|---|---:|---:|---:|
| 128 | `matchAll()` | +0.5% / +8.9% | −42% / −38%† | −72% / −69% |
|  | `replace()` | +5.5%† / +14% | −35% / −32% | −67% / −65% |
| 512 | `matchAll()` | +38% / +37% | −24% / −25% | −66%† / −67%† |
|  | `replace()` | +6.2% / +6.6% | −39% / −38% | −71%† / −70% |
| 3,345 | `matchAll()` | +60% / +67% | −13% / −9.5% | −62% / −60% |
|  | `replace()` | +502% / +465% | +222% / +197% | +40% / +32% |

With 3,345 names building the object takes most of the time of `replace()`, and `strtr()` stays faster. These cells ran in a separate series with the same builds: [data/pages.json](data/pages.json).

## Results by keys and text length

Change in time per call against the fastest existing method ([How it was compared](#how-it-was-compared)), GCC / Clang. **Bold**: faster by more than 3% with both compilers. † = noisy value (see [METHOD.md](METHOD.md)). The time of every method for every value: [all-methods.md](all-methods.md).
Random keys are random strings of the letters a–p, written into English text. The text has one match in the middle third, or none where the row says so. `matches()` stops at the match, about halfway. The other calls read the whole text.

### Prepared

| Keys | Call | 128 B | 1 KiB | 4 KiB | 16 KiB | 64 KiB |
|---|---|---:|---:|---:|---:|---:|
| 8 | `getMatchedKeywords()` | **−20% / −18%** | −8.3% / +11% | −4.2% / +19% | −4.4% / +20% | −1.9% / +23% |
|  | `countMatches()` | **−32% / −33%** | −18% / −1.7% | −11% / +12% | −9.6% / +13% | −9.2% / +14% |
|  | `matchAll()` | **−30%† / −28%** | −17% / −0.6% | −12% / +11% | −9.4% / +15% | −9.8% / +14% |
|  | `matches()`, no match | **−14% / −11%†** | −13% / +5.4% | −10% / +11% | −7.8% / +15% | −9.1% / +14% |
|  | `matches()`, match in the middle | +16% / +10%† | −9.5% / +3.2% | −14% / +3.8% | −13% / +7.3% | −17% / +2.3% |
|  | `replace()` | **−31% / −31%** | **−26% / −21%** | **−27% / −20%** | **−27% / −20%** | **−25% / −18%** |
| 16 | `getMatchedKeywords()` | **−57% / −55%** | **−56% / −47%** | **−54% / −43%** | **−54% / −43%** | **−55% / −43%** |
|  | `countMatches()` | **−62% / −60%** | **−58% / −50%** | **−56% / −46%** | **−56% / −44%** | **−53% / −41%** |
|  | `matchAll()` | **−58% / −58%** | **−57% / −49%** | **−56% / −45%** | **−56% / −44%** | **−54% / −43%** |
|  | `matches()`, no match | **−49% / −47%** | **−55% / −48%** | **−55% / −45%** | **−55% / −45%** | **−52% / −42%** |
|  | `matches()`, match in the middle | **−26%† / −28%** | **−49% / −44%** | **−55% / −47%** | **−55% / −46%** | **−54% / −44%** |
|  | `replace()` | **−53% / −52%** | **−55% / −50%** | **−54% / −47%** | **−52% / −45%** | **−52% / −45%** |
| 32 | `getMatchedKeywords()` | **−76% / −75%** | **−71% / −68%** | **−70% / −66%** | **−69% / −65%** | **−69% / −64%** |
|  | `countMatches()` | **−73% / −71%** | **−70% / −64%** | **−70% / −62%** | **−67% / −59%** | **−67% / −59%** |
|  | `matchAll()` | **−74% / −73%** | **−71% / −67%** | **−70% / −66%** | **−69% / −64%** | **−68% / −63%** |
|  | `matches()`, no match | **−62% / −62%** | **−68% / −63%** | **−69% / −63%** | **−68% / −61%** | **−67% / −61%** |
|  | `matches()`, match in the middle | **−46% / −51%** | **−64% / −61%** | **−69% / −63%** | **−68% / −62%** | **−67% / −60%** |
|  | `replace()` | **−64% / −65%** | **−68% / −64%** | **−69% / −64%** | **−68% / −63%** | **−67% / −62%** |
| 128 | `getMatchedKeywords()` | **−82% / −82%** | **−80% / −77%** | **−79% / −76%** | **−79% / −76%** | **−78% / −75%** |
|  | `countMatches()` | **−81% / −80%** | **−80% / −75%** | **−80% / −75%** | **−78% / −73%** | **−78% / −73%** |
|  | `matchAll()` | **−81% / −81%** | **−80% / −77%** | **−79% / −76%** | **−79% / −75%** | **−79% / −75%** |
|  | `matches()`, no match | **−73% / −73%** | **−77% / −74%** | **−77% / −74%** | **−77% / −73%** | **−76% / −72%** |
|  | `matches()`, match in the middle | **−61% / −64%** | **−74% / −72%** | **−77% / −74%** | **−78% / −74%** | **−77% / −73%** |
|  | `replace()` | **−73% / −73%** | **−76% / −74%** | **−77% / −74%** | **−77% / −74%** | **−76% / −73%** |
| 1024 | `getMatchedKeywords()` | **−88% / −88%** | **−85% / −83%** | **−85% / −82%** | **−84% / −81%** | **−84% / −81%** |
|  | `countMatches()` | **−87% / −87%** | **−85% / −82%** | **−84% / −81%** | **−84% / −80%** | **−84% / −80%** |
|  | `matchAll()` | **−87% / −87%** | **−85% / −83%** | **−85% / −82%** | **−85% / −82%** | **−84% / −81%** |
|  | `matches()`, no match | **−84% / −83%** | **−83% / −80%** | **−84% / −80%** | **−83% / −79%** | **−83% / −79%** |
|  | `matches()`, match in the middle | **−80%† / −81%** | **−82% / −79%** | **−83% / −80%** | **−84% / −79%** | **−84% / −79%** |
|  | `replace()` | **−83% / −83%** | **−83% / −81%** | **−83% / −80%** | **−83%† / −80%** | **−83% / −80%** |

### One-shot

| Keys | Call | 128 B | 1 KiB | 1.5 KiB | 2 KiB | 3 KiB | 4 KiB | 16 KiB | 64 KiB |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 | `getMatchedKeywords()` | +476% / +483%† | +121% / +144% | — | — | — | +35% / +58% | +6.7% / +30% | +0.9% / +25% |
|  | `countMatches()` | +443% / +434% | +101%† / +117% | — | — | — | +27% / +48% | +0.5% / +23% | −6.4% / +17% |
|  | `matchAll()` | +387% / +401% | +98% / +118% | — | — | — | +25% / +49% | +0.4% / +24% | −6.8% / +16% |
|  | `matches()`, no match | +531% / +524% | +116% / +135% | — | — | — | +27% / +48% | +2.1% / +24% | −6.6% / +16% |
|  | `matches()`, match in the middle | +779% / +772% | +212% / +223% | — | — | — | +54% / +71% | +5.1% / +25% | −12% / +6.7% |
|  | `replace()` | +94% / +101% | +27% / +30%† | — | — | — | −8.5% / −1.2% | **−22% / −15%** | **−23% / −16%** |
| 16 | `getMatchedKeywords()` | +470% / +479% | +58% / +72% | +27% / +39% | +9.0% / +21% | −9.8% / +2.0% | **−20% / −7.3%** | **−45% / −33%** | **−52% / −41%** |
|  | `countMatches()` | +436% / +436% | +54%† / +66% | +23% / +35% | +4.8% / +17% | −14% / −1.5% | **−24% / −12%** | **−47% / −35%** | **−53% / −41%** |
|  | `matchAll()` | +416% / +417%† | +54% / +65% | +22% / +35% | +5.3% / +18% | −14% / −0.8%† | **−24% / −11%†** | **−47% / −35%** | **−53% / −41%** |
|  | `matches()`, no match | +533% / +540% | +59% / +72% | +25% / +38% | +6.8% / +19% | −12% / +0.1% | **−23% / −11%** | **−48% / −36%** | **−53% / −41%** |
|  | `matches()`, match in the middle | +856% / +859% | +159% / +173% | +96% / +111% | +63% / +76% | +25% / +38% | +5.1%† / +17% | **−41% / −29%** | **−54% / −44%** |
|  | `replace()` | +126% / +134% | +14% / +17% | −3.6% / −0.8% | **−15% / −12%** | **−26% / −24%** | **−32% / −28%** | **−48% / −43%** | **−53% / −49%** |
| 32 | `getMatchedKeywords()` | +454% / +451% | +20% / +29% | −9.5%† / −2.1% | **−26% / −18%** | **−42% / −36%** | **−50% / −44%** | **−70% / −65%†** | **−72% / −69%** |
|  | `countMatches()` | +431% / +412% | +16% / +23% | **−12% / −3.8%** | **−26% / −18%** | **−41% / −32%** | **−49% / −42%** | **−69% / −62%** | **−70% / −64%** |
|  | `matchAll()` | +420% / +411% | +17% / +24% | **−13% / −4.9%** | **−27% / −21%** | **−42% / −36%** | **−50% / −44%** | **−70% / −65%** | **−72% / −68%** |
|  | `matches()`, no match | +505%† / +491% | +20% / +28% | −10% / −2.9% | **−25% / −18%** | **−41% / −35%** | **−50% / −43%** | **−69% / −64%** | **−71% / −66%** |
|  | `matches()`, match in the middle | +945% / +948% | +129% / +140% | +69% / +79%† | +35% / +45% | −1.2% / +6.6% | **−19% / −12%** | **−62% / −56%** | **−73% / −67%** |
|  | `replace()` | +159% / +187% | +11% / +20% | **−9.1% / −6.6%†** | **−23% / −21%** | **−38% / −36%** | **−50% / −44%** | **−70% / −65%** | **−71% / −67%** |
| 128 | `getMatchedKeywords()` | +454% / +439% | +8.3% / +12% | **−20% / −16%** | **−34% / −32%** | **−52% / −50%** | **−62% / −59%** | **−84% / −83%** | **−81% / −79%** |
|  | `countMatches()` | +444% / +435% | +12% / +15% | **−16% / −14%** | **−31% / −31%** | **−50% / −48%** | **−60% / −59%** | **−84% / −82%** | **−81% / −78%** |
|  | `matchAll()` | +432% / +426%† | +6.8% / +12% | **−20%† / −16%** | **−34% / −32%** | **−52% / −49%** | **−62% / −60%** | **−84% / −83%** | **−81% / −79%** |
|  | `matches()`, no match | +500% / +473% | +17% / +18% | **−13% / −13%** | **−31% / −31%** | **−49% / −49%** | **−59% / −59%** | **−83% / −83%** | **−80% / −77%** |
|  | `matches()`, match in the middle | +982% / +959% | +100% / +108% | +42% / +47% | +19% / +18% | **−13% / −13%** | **−29% / −29%** | **−76% / −75%** | **−82% / −81%** |
|  | `replace()` | +402% / +403% | +7.2% / +13% | **−18% / −15%** | **−35% / −33%** | **−53% / −51%** | **−63% / −60%** | **−84%† / −83%** | **−80% / −79%** |
| 1024 | `getMatchedKeywords()` | +892% / +847% | +72% / +76% | +19% / +21% | **−7.9% / −5.0%** | **−38% / −35%** | **−52% / −51%** | **−80% / −81%** | **−80% / −81%** |
|  | `countMatches()` | +874% / +845% | +70% / +74% | +19% / +21% | **−8.6% / −6.3%** | **−37% / −35%** | **−52% / −51%** | **−80%† / −81%** | **−80% / −80%** |
|  | `matchAll()` | +856% / +853% | +70% / +74% | +18% / +21% | **−9.0% / −7.5%** | **−36% / −35%** | **−52% / −51%** | **−80% / −81%** | **−81% / −81%** |
|  | `matches()`, no match | +935% / +874% | +71% / +74% | +20% / +23% | **−7.1% / −5.0%** | **−36% / −34%** | **−52% / −51%** | **−80% / −81%** | **−80% / −80%** |
|  | `matches()`, match in the middle | +1805% / +1724% | +234% / +242% | +134% / +138% | +82% / +85% | +26% / +27% | **−6.3% / −4.9%** | **−76% / −76%** | **−80%† / −80%** |
|  | `replace()` | +5012% / +4893% | +658% / +635% | +423% / +411% | +298% / +290% | +169% / +165% | +98% / +95% | **−47% / −47%** | **−81% / −81%** |

PHP names, other match positions and every value in µs: [boundaries.md](boundaries.md), [all-methods.md](all-methods.md).

Other inputs:

- **Fewer than 8 keys**: not the intended use; [edge-cases.md](edge-cases.md) shows the loss.
- **Russian, Chinese, Japanese, Korean**: smaller gains, −76…−48% prepared; `matches()` with frequent words −62…+23%. See [languages.md](languages.md).

## Build time and memory

| Dictionary | Matcher build, µs | Matcher memory, KiB | Replacer build, µs | Replacer memory, KiB |
|---|---:|---:|---:|---:|
| random letters a–p, 8 keys | 2.2 | 4.8 | 2.11 | 4.1 |
| random letters a–p, 128 keys | 30.3 | 50 | 28.7 | 43 |
| random letters a–p, 1024 keys | 385 | 277 | 381 | 221 |
| PHP names, 8019 keys | 7,533 | 2,241 | 16,612 | 4,113 |
| LDNOOBW, 403 keys | 117 | 134 | 124 | 118 |
| crawler patterns, 1469 keys | 1,007 | 881 | 1,103 | 673 |
| PHP functions, 3345 keys | 1,640 | 809 | 3,121 | 1,149 |

GCC; Clang is within 15%. Memory is what the object keeps, without the key strings. More in [construction.md](construction.md).

## Limits

- One AMD Ryzen 9 5950X, one build per compiler: GCC 15.2 and Clang 21.1. The new class is 13% slower with Clang in the median prepared value, 2% one-shot.
- 3 to 5 fresh processes per value. They differ by 1.0% in the median value and by 3.3% or less in 90% of values. Changes within about 3% are noise.
- Calls run back to back with warm caches. Garbage collection was off.
- Not measured: other CPUs, cold caches, the PHP JIT, keys starting with a byte rare in the text (`$`, `<`), which let `strpos()` and PCRE skip faster, userland Aho–Corasick libraries, PCRE compile time and the memory of compiled patterns.

## Where to look

| Question | Page |
|---|---|
| A given key count, text length, call and match position, both modes | [boundaries.md](boundaries.md) |
| Russian, Chinese, Japanese, Korean, emoji in the text | [languages.md](languages.md) |
| 1 or 4 keys; texts dense with matches | [edge-cases.md](edge-cases.md) |
| Build time and memory of every dictionary | [construction.md](construction.md) |
| Moderation, bot detection, auto-linking | [Application scenarios](#application-scenarios) above |
| How a value was measured, what counts as the reference | [METHOD.md](METHOD.md) |
| Why calls don't repeat one text | [data/branch-probe.md](data/branch-probe.md) |
| How many passes and processes are enough | [data/calibration.md](data/calibration.md) |
| Rerun on your machine | [REPRODUCE.md](REPRODUCE.md) |
| Every value against every existing method, in µs | [all-methods.md](all-methods.md) |
| Every value with its times in µs, the winning method, spread and A/A | [data/results.json](data/results.json), [data/pages.json](data/pages.json) |
| Scripts | [tools/](tools) |
