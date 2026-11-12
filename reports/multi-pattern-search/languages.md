# Text languages

Does the language of the text change the result? Every call was run on seven kinds of text, 4 and 64 KiB long, with two dictionaries of 128 keys.

## Findings

- **Prepared object**: faster in every case but one. English, Spanish and English with emoji: −91…−78%. Russian, Chinese, Japanese and Korean: −76…−48%.
- **The exception is `matches()` with frequent words**: −62…+23% on Russian, Chinese, Japanese and Korean. Both sides stop at the first word found. The fastest existing method takes 0.83–5.61 µs, on 64 KiB as on 4 KiB, so there is little left to win. One-shot this call is slower on every text (+66…+484%): the build costs more than the whole search.
- **One-shot, other calls**: at 64 KiB faster on every text (−90…−37%). At 4 KiB faster on English, Spanish and emoji texts (−70…−14%). On Russian, Chinese, Japanese and Korean at 4 KiB the change is −28…+289%: the build often doesn't pay off at this length.

## Inputs

- **Texts**: windows at random positions of the PHP manual in each language. Korean comes from MDN. English with emoji is the English manual with an emoji after about every 40 bytes.
- **Bytes per character**: the average UTF-8 length of a character in the text. Matching works on bytes.
- **Frequent words**: 128 words of ranks 1001–1128 in the same language; for Chinese and Japanese, sequences of 2 and 3 characters of the same ranks. They occur in the text.
- **PHP names**: 128 ASCII function and method names. The translated manuals keep code examples in English, so the names occur in every corpus except Korean, though not in every window.

**How to read a cell.** `−80% / −75%` is the change in time per call against the fastest existing method: −80% with GCC 15.2, −75% with Clang 21.1. Negative = the new class is faster: −50% is twice as fast, −75% four times, −90% ten times. +100% is twice as slow. † = the processes disagree by more than 5%, the A/A control is off by more than 3%, a process was preempted more than 20 times a second, or the core was not idle; the values are in [data/results.json](data/results.json). The same file has the times in µs and the existing method that was fastest.

## Prepared object

**Frequent words of the same language (128 keys)**

| Text | Bytes per character | Length | `matches()` | `getMatchedKeywords()` | `countMatches()` | `matchAll()` | `replace()` |
|---|---:|---:|---:|---:|---:|---:|---:|
| English | 1.00 | 4 KiB | −84% / −83% | −91% / −89% | −90% / −89% | −90% / −87% | −85% / −86% |
|  |  | 64 KiB | −84% / −83% | −91% / −89% | −91% / −89% | −90% / −87% | −86% / −86% |
| Spanish | 1.01 | 4 KiB | −84% / −83% | −89% / −88% | −89% / −88% | −89% / −87% | −86% / −84% |
|  |  | 64 KiB | −84% / −83% | −90% / −88% | −89% / −88% | −89% / −87% | −86% / −84% |
| Russian | 1.44 | 4 KiB | −56% / −56% | −70% / −69% | −68% / −68% | −69% / −69% | −58% / −58% |
|  |  | 64 KiB | −62%† / −60% | −70% / −69% | −69% / −68% | −70% / −70%† | −59% / −59% |
| Chinese | 1.45 | 4 KiB | −36% / −37% | −74% / −74% | −73% / −72% | −73% / −73% | −52% / −54% |
|  |  | 64 KiB | −39% / −39% | −75% / −75% | −74% / −72% | −73% / −73% | −52% / −54% |
| Japanese | 1.54 | 4 KiB | −12% / −17% | −72% / −71% | −70% / −69% | −70% / −69% | −55% / −56% |
|  |  | 64 KiB | +23% / +18% | −73% / −72% | −70% / −70% | −70% / −69% | −56% / −58%† |
| Korean | 1.53 | 4 KiB | −40% / −40% | −70% / −68% | −68% / −66% | −69% / −67% | −52% / −52% |
|  |  | 64 KiB | −48% / −44% | −69% / −67% | −67% / −64% | −69% / −66% | −50% / −48% |
| English with emoji | 1.11 | 4 KiB | −83% / −81% | −90% / −88% | −89% / −87% | −88% / −86% | −84% / −84% |
|  |  | 64 KiB | −83% / −82% | −90% / −88% | −89%† / −87% | −88% / −86% | −84% / −84% |

**PHP names (128 keys, ASCII)**

| Text | Bytes per character | Length | `matches()` | `getMatchedKeywords()` | `countMatches()` | `matchAll()` | `replace()` |
|---|---:|---:|---:|---:|---:|---:|---:|
| English | 1.00 | 4 KiB | −84% / −82% | −86% / −82% | −85% / −83% | −86% / −82% | −82% / −80% |
|  |  | 64 KiB | −85% / −82% | −86% / −82% | −84% / −83% | −86% / −82% | −82% / −80% |
| Spanish | 1.01 | 4 KiB | −84% / −82% | −86% / −83% | −85% / −83% | −86% / −83% | −83% / −81% |
|  |  | 64 KiB | −85% / −82% | −86% / −82% | −85% / −83% | −86% / −83% | −84% / −82% |
| Russian | 1.44 | 4 KiB | −68% / −67% | −66% / −68% | −69% / −68% | −71% / −68% | −65% / −69% |
|  |  | 64 KiB | −69% / −66% | −69% / −70% | −70% / −69% | −70% / −69% | −65% / −68% |
| Chinese | 1.45 | 4 KiB | −74% / −71% | −74% / −73% | −75% / −73% | −76% / −73% | −70% / −72% |
|  |  | 64 KiB | −74% / −72% | −76% / −74% | −76% / −74% | −76% / −73% | −70% / −71% |
| Japanese | 1.54 | 4 KiB | −73% / −71% | −71% / −72% | −74% / −72% | −75% / −72% | −70% / −72% |
|  |  | 64 KiB | −74% / −72% | −74% / −73% | −75% / −73% | −76% / −75% | −70% / −72% |
| Korean | 1.53 | 4 KiB | −71% / −68% | −70% / −69% | −72% / −70% | −73% / −69% | −66% / −68% |
|  |  | 64 KiB | −71% / −68% | −71% / −70% | −72% / −70% | −73% / −68% | −67% / −70% |
| English with emoji | 1.11 | 4 KiB | −82% / −79% | −84% / −80% | −83% / −80% | −83% / −80% | −79% / −78%† |
|  |  | 64 KiB | −82% / −79% | −83% / −80% | −83% / −80% | −83% / −79% | −80% / −78% |

## One-shot: build and one call

**Frequent words of the same language (128 keys)**

| Text | Bytes per character | Length | `matches()` | `getMatchedKeywords()` | `countMatches()` | `matchAll()` | `replace()` |
|---|---:|---:|---:|---:|---:|---:|---:|
| English | 1.00 | 4 KiB | +107% / +125% | −61% / −57% | −63% / −60% | −62% / −58% | −70% / −69% |
|  |  | 64 KiB | +69% / +85% | −90% / −88% | −89% / −88% | −88% / −86% | −85% / −85% |
| Spanish | 1.01 | 4 KiB | +143% / +163% | −63% / −60% | −64% / −62% | −64% / −61% | −64% / −64% |
|  |  | 64 KiB | +70% / +87% | −88% / −87% | −87% / −86% | −87% / −86% | −84% / −83% |
| Russian | 1.44 | 4 KiB | +174% / +166% | −8.0% / −9.1% | −7.0% / −10% | −8.4% / −9.9% | +4.8% / +2.5% |
|  |  | 64 KiB | +184% / +176% | −72% / −73% | −72% / −73% | −72% / −74% | −67% / −69%† |
| Chinese | 1.45 | 4 KiB | +391% / +371% | +8.8% / +3.6% | +14% / +11% | +7.7% / +2.6%† | +266% / +289%† |
|  |  | 64 KiB | +380% / +366% | −71% / −72% | −71% / −70% | −70% / −71% | −38% / −37% |
| Japanese | 1.54 | 4 KiB | +484% / +469% | −22% / −22% | −21% / −18% | −24% / −24%† | +248% / +256% |
|  |  | 64 KiB | +472% / +459%† | −70%† / −70% | −68% / −68% | −68% / −68% | −41% / −40% |
| Korean | 1.53 | 4 KiB | +214% / +227% | −28% / −25% | −23% / −18% | −27% / −23% | +19% / +25% |
|  |  | 64 KiB | +170% / +187% | −73% / −71% | −71% / −70% | −72% / −71% | −64% / −64% |
| English with emoji | 1.11 | 4 KiB | +106% / +123% | −58% / −54% | −60% / −56% | −59% / −55% | −66% / −64% |
|  |  | 64 KiB | +66% / +82% | −88% / −87% | −87% / −86% | −87% / −85% | −83% / −83% |

**PHP names (128 keys, ASCII)**

| Text | Bytes per character | Length | `matches()` | `getMatchedKeywords()` | `countMatches()` | `matchAll()` | `replace()` |
|---|---:|---:|---:|---:|---:|---:|---:|
| English | 1.00 | 4 KiB | −24% / −20%† | −30% / −24%† | −28% / −24% | −28% / −25% | −35% / −31%† |
|  |  | 64 KiB | −85% / −83% | −86% / −84% | −85% / −84% | −86% / −85% | −83% / −82% |
| Spanish | 1.01 | 4 KiB | −24% / −20% | −30% / −23% | −29% / −25% | −30% / −23% | −35%† / −31% |
|  |  | 64 KiB | −85% / −85% | −86% / −85% | −85% / −85% | −86% / −85% | −84% / −83% |
| Russian | 1.44 | 4 KiB | +56%† / +53% | +49%† / +41% | +51%† / +44%† | +53%† / +42% | +79%† / +74%† |
|  |  | 64 KiB | −67% / −67% | −75%† / −76% | −75% / −75% | −74% / −75% | −71% / −72% |
| Chinese | 1.45 | 4 KiB | +16%† / +16% | +5.2%† / +0.8% | +3.9% / +1.0% | +5.9%† / −0.1%† | +28%† / +31%† |
|  |  | 64 KiB | −72% / −72% | −81% / −81% | −81% / −81% | −81% / −82% | −77% / −78% |
| Japanese | 1.54 | 4 KiB | +24%† / +25%† | +22% / +14%† | +17% / +13%† | +16% / +15% | +34%† / +45% |
|  |  | 64 KiB | −78% / −77% | −80% / −80% | −81% / −81% | −82% / −82% | −77% / −78% |
| Korean | 1.53 | 4 KiB | +26%† / +21% | +24%† / +21% | +21% / +16%† | +22%† / +19% | +42%† / +47%† |
|  |  | 64 KiB | −79%† / −78% | −79% / −79% | −79% / −78% | −79%† / −78% | −76% / −76% |
| English with emoji | 1.11 | 4 KiB | −20% / −14% | −25% / −21% | −25% / −21%† | −25% / −20% | −27% / −20%† |
|  |  | 64 KiB | −85% / −84% | −85% / −83% | −84% / −84% | −85% / −83% | −81% / −81% |
