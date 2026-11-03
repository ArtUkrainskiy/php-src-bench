# Fixed 4 KiB inputs: dictionary size and match position

Each operation processes one of four different saved English strings, exactly **4096 bytes** each. Texts and dictionary order are visible in the suite JSON; all variants cycle equally often. These are controlled authored examples, not production traces. The source texts are copied byte-for-byte from the [input-length corpus](../multi-pattern-length/README.md).

- Dictionary-size matrix: **8, 16, 32, 64, 128, 256, 512** keys. Moderation searches four clean strings with no matches, even against all 512 keys. Replacement uses the same four support articles at every size, replacing literal support terms with help URLs. Both dictionaries grow by appending entries from the pinned lexicons; growing the support dictionary also increases matches and output, shown in [CASES.md](CASES.md).
- Position matrix: **128** moderation phrases with no match, a match near the start, middle or end. Each positive variant has one matching key; its 1-based dictionary rank is respectively **1, 37, 91 or 128**, in the same order at each position. This avoids measuring only a first-key hit. Exact byte offsets are saved with the inputs.

Worker timing reuses prepared state. Separate batches of one operation include candidate construction and destruction while native arrays and regex patterns/callbacks are already prepared; PCRE caches are warm. Input loading is excluded throughout.

[generate.py](generate.py) recomputes expected outputs using independent byte search and longest-match replacement. Verify saved files with `python3 generate.py --check`. This matrix leaves earlier corpora unchanged.
