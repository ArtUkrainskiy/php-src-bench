# Builds, sources and measurement method

Matcher and Replacer use the same strmatch module. The release PHP CLI and module were built separately with GCC 14.2; their source and binary identities are recorded below.

| Component | Exact identity |
|---|---|
| PHP CLI source commit | `3b8e98882e425907921c606496da424c33d12fab` |
| PHP CLI SHA-256 | `39159ae473c652bcfce049760de06e40c6ca06d5dfbe1af5fdf5cda1843f541d` |
| Extension source SHA-256 | `c4cece7e7a4f5952caae5609b9bc607408427c1fe006e47f59d7fdc0cc0946b3` |
| Extension module SHA-256 | `7333c1ef752620bacad96138c4fa969fa4cea63a28eea17a9f882bdefd8f861c` |
| PHP `main/php_config.h` SHA-256 | `32e7126ddfcb28ae02bcf1f70448e640770a2b2256ac3637939561a523264223` |

[Measured C source](../benchmark/extension/strmatch.c). [Build metadata](data/build.json) includes configure options, compiler flags and runtime versions. The module uses headers configured from the CLI's PHP commit. The collector verifies binary hashes before measuring.

Intel Core i7-13700H, Linux x86-64; logical P-core 2, SMT sibling 3. Locale `C`; GC, PHP JIT and OPcache disabled in the timing harness. PCRE JIT is enabled, but individual patterns were not checked for JIT execution.

The collector records sibling load, temperatures and CPU steal. AC was observed connected; power supply and package power were not continuously logged. Affinity pins execution but does not isolate the CPU from other system activity.

## Input snapshots and licenses

| Input | Snapshot and attribution | License / saved evidence |
|---|---|---|
| Civil Comments | [Google dataset](https://huggingface.co/datasets/google/civil_comments); test rows at offsets recorded in corpus.json, acquired 2026-11-09 | Dataset card declares CC0-1.0; the saved text and SHA-256 identify each acquired row |
| English banword dictionary | LDNOOBW / Shutterstock, Inc.; `5faf2ba42d7b1c0977169ec3611df25a3c08eb13` | [CC BY 4.0](sources/banwords/LICENSE); [attribution](sources/banwords/ATTRIBUTION.md) |
| Complete documentation and rename mapping | Python Software Foundation and contributors; `8d21aa21f2cbc6d50aab3f420bb23be1d081dac4` | [Complete CPython license](sources/python/LICENSE), including its historical terms |
| HTML/text email templates | Groundmail; `5240b4a4de917b4d69bf2725b5441e50cb94a682` | [MIT license](sources/emails/LICENSE) |

[corpus.json](corpus.json) records source URLs, Git revisions, byte sizes and SHA-256 hashes. Civil Comments responses did not identify an immutable dataset revision: use the saved row texts and hashes to reproduce these inputs. Later downloads may differ.

[DESIGN](DESIGN.md) specifies selection, dictionary transformations and expected-output checks. Every measured case has a self-contained JSON with its texts, ordered dictionary and expected output.

## Timing and quality checks

Each recipe receives 100 ms warmup and 15 samples targeting 40 ms each. Recipe order rotates and reverses between rounds. A second native object runs the same code as an A/A control. The collector keeps the first attempt passing quality checks, with at most two attempts; if neither passes, it keeps and flags the first. [Thresholds and affected cases](QUALITY.md).

Summary percentages compare the native median with the single reference median shown in the row. Raw captures also retain paired sample ratios. The 2% rule for calling a difference close is a reporting convention, not a confidence interval.

## PCRE recipes

- `literal`: alternatives made from escaped literal keys.
- `prefix`: equivalent alternatives with shared prefixes factored out.
- `tokens`: recognize `{{name}}`, look it up in the replacement map and preserve unknown tokens.

Unique/count/all searches use lookahead and group keys by byte length to retain overlapping and nested matches. Unique/all include deduplication or sorting as required. Replacement alternatives select longest matches first and use callbacks to insert literal values without rescanning them. Pattern construction and compilation are outside timing for every PCRE recipe.

## Hardware counters

Each recipe has five alternating 0/N pairs, with N targeting 30 ms. Subtract the zero-iteration count from the N-iteration count and divide by N to obtain user-mode cycles and instructions per job. Both the collector and PHP are pinned to the P-core. Counter captures and quality checks are separate from elapsed timing.

## Raw evidence

- [Elapsed points and every attempt](data/elapsed.json.gz)
- [Counter pairs](data/counters.json.gz) and [raw perf observations](data/counter-captures.json.gz)
- [Fresh-process native allocation observations](data/memory.json)
- [Correctness summary](data/checks.json) and [display-selection rule](data/summary-selection.json)

Public captures retain samples, diagnostics and collection settings. Local command paths are replaced by placeholders; exact texts are supplied in case JSONs. Timings and counters are unchanged.
