#!/usr/bin/env python3
"""Save a fixed-4-KiB dictionary-size and match-position matrix with byte-search oracles."""

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LENGTH = ROOT.parent / 'multi-pattern-length'
SCALING = ROOT.parent / 'multi-pattern-scaling'
PRODUCT = ROOT.parent / 'multi-pattern-product'
spec = importlib.util.spec_from_file_location('product', PRODUCT / 'generate.py')
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)


def read(path):
    return json.loads(path.read_text())


def build():
    g.SUITES = {}
    originals = {
        case['id']: case
        for suite in ['moderation', 'support']
        for case in read(LENGTH / f'suites/{suite}.json')['cases']
    }
    words = read(SCALING / 'moderation-words.json')['words']
    terms = read(SCALING / 'support-terms.json')['words']

    def add(suite, identifier, operation, dictionary, source, axis, size, state):
        original = originals[source]
        texts = [job['documents'][0]['text'] for job in original['jobs']]
        assert len(set(texts)) == 4 and all(len(text.encode()) == 4096 for text in texts)
        g.add(
            suite,
            identifier,
            'One 4 KiB string against a fixed dictionary',
            operation,
            'Four saved strings, exactly 4096 bytes each. One call processes one string. '
            'For the dictionary-size axis, the strings stay byte-identical as prefix dictionaries grow; '
            'support match counts and replacement output can change with dictionary size.',
            'fixed_policy',
            [g.job(f'document-{i + 1}', dictionary, text) for i, text in enumerate(texts)],
        )
        case = g.SUITES[suite][-1]
        case['lifetime']['modes'] = [{'id': 'worker', 'label': 'Dictionary already prepared'}]
        case['grid'] = {'axis': axis, 'keys': size, 'bytes': 4096, 'variants': 4, 'match': state, 'source_case': source}
        if operation == 'any':
            assert all(bool(doc['expected']) == (state != 'absent') for job in case['jobs'] for doc in job['documents'])

    for size in [8, 16, 32, 64, 128, 256, 512]:
        add(
            'moderation',
            f'grid.any.absent.{size}',
            'any',
            words[:size],
            'length.any.absent.4096',
            'dictionary',
            size,
            'absent',
        )
        mapping = {term: f'https://help.example.test/topic/{i:05}' for i, term in enumerate(terms[:size])}
        add(
            'replacement',
            f'grid.replace.mixed.{size}',
            'replace',
            mapping,
            'length.replace.mixed.4096',
            'dictionary',
            size,
            'mixed',
        )
    for state in ['absent', 'start', 'middle', 'end']:
        source = f'length.any.{state}.4096'
        add(
            'position',
            f'grid.any.{state}.position',
            'any',
            originals[source]['jobs'][0]['dictionary'],
            source,
            'position',
            128,
            state,
        )
    files = g.pack()
    index = json.loads(files['index.json'])
    index.update(
        status='Saved fixed-4-KiB dictionary-size and position inputs; independent byte-based expected output.',
        source_sha256={
            str(path.relative_to(ROOT.parent)): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in [
                LENGTH / 'suites/moderation.json',
                LENGTH / 'suites/support.json',
                SCALING / 'moderation-words.json',
                SCALING / 'support-terms.json',
                PRODUCT / 'generate.py',
            ]
        },
    )
    files['index.json'] = json.dumps(index, ensure_ascii=False, indent=2) + '\n'
    lines = [
        '# Fixed-4-KiB cases',
        '',
        '| Case | Keys | First match byte offsets | First matching key ranks (1-based) | Replacements/string |',
        '|---|---:|---|---|---|',
    ]
    for cases in g.SUITES.values():
        for case in cases:
            facts = [job['documents'][0]['facts'] for job in case['jobs']]
            offsets = ', '.join('—' if v['first_match_offset'] is None else str(v['first_match_offset']) for v in facts)
            ranks = ', '.join(
                '—' if v['first_matching_dictionary_rank'] is None else str(v['first_matching_dictionary_rank'] + 1)
                for v in facts
            )
            counts = ', '.join(str(v['selected_matches']) for v in facts) if case['operation'] == 'replace' else '—'
            lines.append(f'| `{case["id"]}` | {case["grid"]["keys"]} | {offsets} | {ranks} | {counts} |')
    files['CASES.md'] = '\n'.join(lines) + '\n'
    files['README.md'] = """# Fixed 4 KiB inputs: dictionary size and match position

Each operation processes one of four different saved English strings, exactly **4096 bytes** each. Texts and dictionary order are visible in the suite JSON; all variants cycle equally often. These are controlled authored examples, not production traces. The source texts are copied byte-for-byte from the [input-length corpus](../multi-pattern-length/README.md).

- Dictionary-size matrix: **8, 16, 32, 64, 128, 256, 512** keys. Moderation searches four clean strings with no matches, even against all 512 keys. Replacement uses the same four support articles at every size, replacing literal support terms with help URLs. Both dictionaries grow by appending entries from the pinned lexicons; growing the support dictionary also increases matches and output, shown in [CASES.md](CASES.md).
- Position matrix: **128** moderation phrases with no match, a match near the start, middle or end. Each positive variant has one matching key; its 1-based dictionary rank is respectively **1, 37, 91 or 128**, in the same order at each position. This avoids measuring only a first-key hit. Exact byte offsets are saved with the inputs.

Worker timing reuses prepared state. Separate batches of one operation include candidate construction and destruction while native arrays and regex patterns/callbacks are already prepared; PCRE caches are warm. Input loading is excluded throughout.

[generate.py](generate.py) recomputes expected outputs using independent byte search and longest-match replacement. Verify saved files with `python3 generate.py --check`. This matrix leaves earlier corpora unchanged.
"""
    return files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    for name, content in build().items():
        path = ROOT / name
        if args.check:
            assert path.read_text() == content, name
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
    print('Fixed-4-KiB corpus PASS: 18 cases')


if __name__ == '__main__':
    main()
