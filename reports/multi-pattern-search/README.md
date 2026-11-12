# Searching for many keys at once: `Str\Matcher` and `Str\Replacer`

[PR #25122](https://github.com/php/php-src/pull/25122) proposes two classes for `ext/standard`, plus `Str\MatchResult` for results; they aren't in a released PHP yet.
They find or replace many literal keys in one pass over the text:

```php
$matcher = new Str\Matcher(['viagra', 'casino', 'free money']);
$matcher->matches($comment);   // also getMatchedKeywords(), countMatches(), matchAll()
(new Str\Replacer(['strlen' => '<a href="…">strlen</a>']))->replace($page);
```

The report compares them with the fastest existing way to do the same: a `str_contains()`/`strpos()` loop, `strtr()`, or a PCRE alternation.

Each result is shown in two modes:

- **Prepared**: the time of a call on an object that already exists. The build is paid elsewhere: once per worker in a long-running runtime, once per request before a loop over many texts, or anywhere else the object is reused. Under PHP-FPM an object lives for one request.
- **One-shot**: the time of building the object and making one call with it.

The cost of the build decides between them. On the random-key and PHP-name grids, a prepared object with 32 keys or more is 1.9 to 16 times faster per call, unless a match comes in the first 64 bytes.
Building it for a single check of a short text is slower: on 128 B with 16 random keys the build and call take 4.19–4.58 µs, the fastest existing method 0.46–1.89 µs. In the moderation scenario the build pays off from about 29–32 checks with the same object.
On long texts a single call usually pays for the build: at 64 KiB with 16 random keys or more a one-shot call changes the time by −82…+5.2%. The exception is `matches()` with a match in the first 64 bytes: +221…+550% at 4 and 64 KiB.

Detailed tables by question: [Where to look](#where-to-look).

## Results

Each value is the change in time per call against the fastest existing method for the same call, text, keys and mode. Which methods compete: [How it was compared](#how-it-was-compared); the time of each of them for every value: [all-methods.md](all-methods.md).
Negative = the new class is faster: −50% is twice as fast, −90% ten times. † = noisy value (see [METHOD.md](METHOD.md)).
Random keys are random strings of the letters a–p, written into English text. PHP names are function and method names from the PHP manual, on manual text.
Ranges cover the five calls (`matches()`, `getMatchedKeywords()`, `countMatches()`, `matchAll()`, `replace()`), texts from 128 B to 64 KiB, and both compilers. A match in the first 64 bytes is listed separately below.

| Mode | Keys | Random keys | PHP names |
|---|---|---:|---:|
| Prepared | 32 or more | −90…−46% | −94…−62% |
| Prepared | 16 | −62…+0.7% | not measured |
| Prepared | 8 | −42…+117% | +17…+58% |

### When a single call pays for the build

The smallest measured text on which building the object for one call is already faster than the fastest existing method, on both compilers. Measured lengths: 1, 1.5, 2, 3, 4, 16 and 64 KiB; PHP names have no 16 KiB cell.
Random keys: one match in the middle third or none. The last column adds 16 matches across the text (measured at 1, 4, 16 and 64 KiB) and, for `matches()`, a match in the last 64 bytes (4 and 64 KiB), so it only looks at those lengths. 2048 PHP names were measured at 1, 4 and 64 KiB only.

| Dictionary | Keys | Every call but `matches()` with a match | Every call | Every call, also 16 matches or a match in the last 64 bytes |
|---|---:|---:|---:|---:|
| Random keys | 16 | 4 KiB | 16 KiB | not up to 64 KiB |
| Random keys | 32 | 1.5 KiB* | 4 KiB | 16 KiB |
| Random keys | 128 | 1.5 KiB | 3 KiB | 4 KiB |
| Random keys | 1024 | 16 KiB | 16 KiB | 16 KiB |
| PHP names | 32 | 4 KiB | 4 KiB | — |
| PHP names | 128 | 3 KiB* | 4 KiB | — |
| PHP names | 512 | 4 KiB | 64 KiB | — |
| PHP names | 2048 | 64 KiB | not up to 64 KiB | — |

\* The slowest case at that length is within 3% of the reference, inside the noise.

`matches()` with a match is the hardest case: the existing methods stop at the first match, so they spend less the earlier it comes. With a match in the first 64 bytes a one-shot `matches()` didn't pay at 4 or 64 KiB: +221…+550% with 16 keys or more.
On PHP names the text decides where matches are, so `matches()` is left out of the first column there.

Below that length a one-shot call is slower. One call on a 128 B text, one-shot, GCC, over the five calls and match positions:

| Random keys | Fastest existing method, µs | Build and call, µs |
|---|---:|---:|
| 16 | 0.46–1.89 | 4.19–4.58 |
| 32 | 0.78–3.1 | 8.02–8.39 |
| 128 | 2.85–6.26 | 29.3–31.1 |

One-shot with 128 random keys, change per call (GCC / Clang):

| Call | 1 KiB | 1.5 KiB | 2 KiB | 3 KiB | 4 KiB |
|---|---:|---:|---:|---:|---:|
| `getMatchedKeywords()` | +8.3% / +12% | −20% / −16% | −34% / −32% | −52% / −50% | −62% / −59% |
| `countMatches()` | +12% / +15% | −16% / −14% | −31% / −31% | −50% / −48% | −60% / −59% |
| `matchAll()` | +6.8% / +12% | −20%† / −16% | −34% / −32% | −52% / −49% | −62% / −60% |
| `replace()` | +7.2% / +13% | −18% / −15% | −35% / −33% | −53% / −51% | −63% / −60% |
| `matches()`, no match | +17% / +18% | −13% / −13% | −31% / −31% | −49% / −49% | −59% / −59% |
| `matches()`, match in the middle | +100% / +108% | +42% / +47% | +19% / +18% | −13% / −13% | −29% / −29% |

Every key count, call and match position, for both modes: [boundaries.md](boundaries.md).

### When a single `replace()` call pays for the build

One-shot `Str\Replacer`: build, one `replace()` call and destroy, against the fastest existing method (GCC / Clang).
Random keys have one match in the middle of the text; PHP names occur as they do in the manual.

| Dictionary | 1 KiB | 1.5 KiB | 2 KiB | 3 KiB | 4 KiB | 16 KiB | 64 KiB |
|---|---:|---:|---:|---:|---:|---:|---:|
| 16 random keys | +14% / +17% | −3.6% / −0.8% | −15% / −12% | −26% / −24% | −32% / −28% | −48% / −43% | −53% / −49% |
| 32 random keys | +11% / +20% | −9.1% / −6.6%† | −23% / −21% | −38% / −36% | −50% / −44% | −70% / −65% | −71% / −67% |
| 128 random keys | +7.2% / +13% | −18% / −15% | −35% / −33% | −53% / −51% | −63% / −60% | −84%† / −83% | −80% / −79% |
| 1024 random keys | +658% / +635% | +423% / +411% | +298% / +290% | +169% / +165% | +98% / +95% | −47% / −47% | −81% / −81% |
| 32 PHP names | +62%† / +69% | +29% / +32% | +7.9% / +11% | −17% / −13% | −33% / −26% | — | −74% / −71% |
| 128 PHP names | +86%† / +85%† | +39%† / +42%† | +12%† / +15%† | −15%† / −18%† | −35%† / −30%† | — | −83% / −82% |
| 512 PHP names | +64% / +43%† | +17% / +7.5% | −6.7%† / −13% | −38% / −40%† | −51% / −54%† | — | −77% / −79% |

A single `replace()` pays for the build from 1.5–2 KiB with 16 to 128 random keys (16 keys at 1.5 KiB is within the noise), and from 2–3 KiB of manual text with 32 to 512 PHP names.
With 1024 keys the reference is `strtr()`: on 1–4 KiB with GCC it takes 51.4–198 µs, the build and call of the new class 389–392 µs.

### Applications

| Application | Prepared | One-shot | One-shot against the prepared existing method | Calls on one object to repay the build |
|---|---:|---:|---:|---:|
| Moderation | 8.0–13× faster | 4.0–5.8× slower | 13–28× slower | 29–32 |
| Bot detection | 11–12× faster | 27–31× slower | 262–324× slower | 350–354 |
| Auto-linking | 12–123× faster | 2.6–9.5× slower | 8.4–61× slower | 9–66 |

- **Fewer than 8 keys**: not the intended use; [edge-cases.md](edge-cases.md) shows the loss.
- **"Against the prepared existing method"**: the application keeps the PCRE pattern as a constant, and PCRE has it compiled already, as under PHP-FPM; the new object is still built on every request. For auto-linking `replace()` the existing method is `strtr()`, which has no prepared form: 8.4–8.7× there, 58–61× against PCRE.
- **A match in the first 64 bytes** (`matches()`, 4 and 64 KiB): prepared −70% to +49% with 32 or more keys, +58…+115% with 16 and +94…+155% with 8. One-shot `matches()`: +221…+550% with 16 keys or more.
- **Russian, Chinese, Japanese, Korean**: smaller gains, −76…−48% prepared; `matches()` with frequent words −62…+23%. See [languages.md](languages.md).

One AMD Ryzen 9 5950X, GCC 15.2 and Clang 21.1, 3 to 5 fresh processes per value; the processes of a value differ by 1.0% in the median and by 3.3% or less in 90% of values; changes within about 3% are not told apart. The prepared new class is 13% slower with Clang than with GCC in the median value, one-shot 2%, which moves the boundaries at 8 and 16 keys.
Not measured: other CPUs, cold CPU caches, the PHP JIT, keys starting with a byte rare in the text (`$`, `<`), userland Aho–Corasick libraries, PCRE compile time and the memory of compiled patterns.

## How it was compared

- Only existing methods that are right on every text compete. `str_replace()` is left out: it replaces inside text it has already replaced, so its output can differ from `strtr()`.
- PCRE is tried as a plain alternation and as one that shares key prefixes (`/cas(?:ino|h)/`); the faster one counts. For which keys, how many and every occurrence, PCRE uses a lookahead so that overlapping keys are found. An alternation that consumes matches took 2–25% less time in a probe but misses overlapping keys, so it doesn't compete.
- `strtr()` has no prepared form: its time includes processing the whole key array on every call.
- One-shot includes building the PCRE pattern string, not compiling it: PCRE keeps compiled patterns in its per-process cache.
- Every call gets a different text. On one repeated text the new class ran 3–4 times faster, because the CPU learns its branches (an earlier version; the existing methods weren't probed).

[METHOD.md](METHOD.md) has the details, [REPRODUCE.md](REPRODUCE.md) the commands.

## Application scenarios

| Scenario | Texts | Median text | Keys |
|---|---:|---:|---:|
| Moderation | 10,000 | 199 B | 403 |
| Bot detection | 10,000 | 118 B | 1,469 |
| Auto-linking | 4,153 | 597 B | 3,345 |

- **Moderation**: [Civil Comments](https://huggingface.co/datasets/google/civil_comments) against the English [LDNOOBW](dictionaries/ldnoobw/ATTRIBUTION.md) list, ignoring ASCII case.
- **Bot detection**: User-Agents (80% browsers, 20% crawlers) against the literal patterns of [crawler-user-agents](https://github.com/monperrus/crawler-user-agents).
- **Auto-linking**: PHP manual pages; `replace()` turns every function name into a link. For `replace()` only `strtr()` competes: PCRE can't compile a replacement pattern this large.

Change is GCC / Clang. † = noisy value, details in [data/results.json](data/results.json).

**Prepared**

| Task | Fastest existing method | Its time, µs | New class, µs | Change, GCC / Clang |
|---|---|---:|---:|---:|
| Moderation: does a comment contain a listed word? | PCRE, shared prefixes | 4.24 | 0.53 | −87% / −87% |
| Moderation: which listed words occur? | PCRE, shared prefixes | 8.54 | 0.64 | −93% / −93% |
| Bot detection: is this User-Agent a crawler? | PCRE, shared prefixes | 3.15 | 0.27 | −92% / −91% |
| Bot detection: which crawler patterns match? | PCRE, shared prefixes | 3.84 | 0.33 | −91% / −91% |
| Auto-linking: link PHP function names in a manual page | `strtr()` | 363 | 2.99 | −99% / −99% |
| Auto-linking: every function name with its offset | PCRE, shared prefixes | 27.1 | 2.07 | −93% / −92% |
| Auto-linking: which function names occur? | PCRE, shared prefixes | 27.3 | 2.03 | −93% / −92% |

**One-shot**

| Task | Fastest existing method | Its time, µs | New class, µs | Change, GCC / Clang |
|---|---|---:|---:|---:|
| Moderation: does a comment contain a listed word? | `strtolower()` + `str_contains()` loop | 20.4 | 119 | +483% / +417% |
| Moderation: which listed words occur? | `strtolower()` + `str_contains()` loop | 26 | 119 | +359% / +304% |
| Bot detection: is this User-Agent a crawler? | `str_contains()` loop | 32.7 | 1,019 | +3004% / +2873% |
| Bot detection: which crawler patterns match? | `str_contains()` loop | 35.8 | 1,013 | +2730% / +2604% |
| Auto-linking: link PHP function names in a manual page | `strtr()` | 345 | 3,169 | +851% / +796% |
| Auto-linking: every function name with its offset | `strpos()` loop | 622 | 1,642 | +164% / +169% |
| Auto-linking: which function names occur? | `str_contains()` loop | 618 | 1,651 | +167% / +177% |

Build time and the number of calls on one object that repay it: build ÷ prepared saving per call, from the two modes. The existing method's own one-time work, such as building and compiling its pattern, counts as zero, which favours it.

| Task | Build, GCC, µs | Calls, GCC | Build, Clang, µs | Calls, Clang |
|---|---:|---:|---:|---:|
| Moderation | 118 | 32 | 110 | 29 |
| Bot detection | 1,018 | 354 | 1,009 | 350 |
| Auto-linking, replace | 3,166 | 9 | 3,130 | 9 |
| Auto-linking, offsets | 1,640 | 66 | 1,615 | 63 |

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

- One machine, one build per compiler.
- Random keys use the letters a–p. Keys starting with a rare byte let `strpos()` and PCRE skip faster; not measured.
- Calls run back to back with warm caches. PHP JIT and garbage collection were off.

## Where to look

| Question | Page |
|---|---|
| A given key count, text length, call and match position, both modes | [boundaries.md](boundaries.md) |
| Russian, Chinese, Japanese, Korean, emoji in the text | [languages.md](languages.md) |
| 1 or 4 keys; texts dense with matches | [edge-cases.md](edge-cases.md) |
| Build time and memory of every dictionary | [construction.md](construction.md) |
| Moderation, bot detection, auto-linking | [Application scenarios](#application-scenarios) above |
| How a value was measured, what counts as the reference | [METHOD.md](METHOD.md) |
| Why every call gets a different text | [data/branch-probe.md](data/branch-probe.md) |
| How many passes and processes are enough | [data/calibration.md](data/calibration.md) |
| Rerun on your machine | [REPRODUCE.md](REPRODUCE.md) |
| Every value against every existing method, in µs | [all-methods.md](all-methods.md) |
| Every value with its times in µs, the winning method, spread and A/A | [data/results.json](data/results.json) |
| Scripts | [tools/](tools) |
