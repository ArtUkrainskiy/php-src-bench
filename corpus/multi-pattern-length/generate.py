#!/usr/bin/env python3
"""Save fixed-byte-length application texts and independent expected results. No timing."""

import argparse
import hashlib
import importlib.util
import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PRODUCT = ROOT.parent / 'multi-pattern-product'
SCALING = ROOT.parent / 'multi-pattern-scaling'
spec = importlib.util.spec_from_file_location('product', PRODUCT / 'generate.py')
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)


def fixed_text(bank, length, variant, inserted='', location='absent'):
    rng = random.Random(20261103 + variant * 1009 + length)
    text = ''
    while len(text.encode()) < length + 512:
        paragraphs = list(bank)
        rng.shuffle(paragraphs)
        text += '\n\n'.join(paragraphs) + '\n\n'
    if location == 'start':
        text = 'Reported phrase: "' + inserted + '".\n\n' + text
    elif location == 'middle':
        position = text.rfind(' ', 0, length // 2)
        text = text[:position] + '\n\nReported phrase: "' + inserted + '".\n\n' + text[position + 1 :]
    elif location == 'end':
        tail = '\n\nThe last reply said "' + inserted + '".'
        budget = length - len(tail.encode())
        prefix = text.encode()[:budget].decode('utf-8', errors='ignore')
        prefix = prefix.rsplit(' ', 1)[0]
        text = prefix + ' ' * (budget - len(prefix.encode())) + tail
    if len(text.encode()) > length:
        text = text.encode()[:length].decode('utf-8', errors='ignore')
        if not text[-1:].isspace():
            text = text.rsplit(' ', 1)[0]
    text = text.rstrip()
    padding = length - len(text.encode())
    assert 0 <= padding < 80
    return text + ' ' * padding


def build():
    g.SUITES = {}
    bank = json.loads((ROOT / 'paragraphs.json').read_text())
    words = json.loads((SCALING / 'moderation-words.json').read_text())['words']
    terms = json.loads((SCALING / 'support-terms.json').read_text())['words'][:128]
    policy = words[:128]
    # Spread the eight core rules over dictionary ranks without changing its set.
    positions = {i * 127 // 7: policy[i] for i in range(8)}
    rest = iter(policy[8:])
    policy = [positions[i] if i in positions else next(rest) for i in range(128)]
    core = [words[i] for i in [0, 2, 5, 7]]
    for group, short, texts in [('moderation', 128, bank['clean']), ('support', 512, bank['support'])]:
        for length in [short, 4096, 16384, 65536]:
            states = ['absent', 'start', 'middle', 'end'] if group == 'moderation' else ['mixed']
            for state in states:
                docs, variant_indices = [], []
                for i in range(4):
                    candidate = i
                    while True:
                        text = fixed_text(texts, length, candidate, core[i], state)
                        if text not in docs:
                            docs.append(text)
                            variant_indices.append(candidate)
                            break
                        candidate += 4
                        assert candidate < 10000, 'Cannot create distinct saved inputs'
                assert len(set(docs)) == 4
                if group == 'moderation':
                    assert all(bool(g.occurrences(text, words)) == (state != 'absent') for text in docs)
                    operations = [('any', 'Moderation policy check', policy)]
                else:
                    mapping = {term: f'https://help.example.test/topic/{i:05}' for i, term in enumerate(terms)}
                    operations = [
                        ('unique', 'List distinct support terms', terms),
                        ('replace', 'Replace support terms with help URLs', mapping),
                    ]
                for operation, title, dictionary in operations:
                    identifier = f'length.{operation}.{state}.{length}'
                    g.add(
                        group,
                        identifier,
                        title,
                        operation,
                        f'Exactly {length} UTF-8 bytes per document, 128 literal keys, four saved variants. '
                        'One call processes one document. Variants cycle equally. '
                        'Documents assemble saved authored paragraphs in seeded order, trim to a word boundary '
                        'and use fewer than 80 final ASCII spaces to reach the exact size. '
                        'This is a controlled input-length experiment, not a production trace.',
                        'fixed_policy',
                        [g.job(f'document-{i + 1}', dictionary, text) for i, text in enumerate(docs)],
                    )
                    case = g.SUITES[group][-1]
                    case['lifetime']['modes'] = [{'id': 'worker', 'label': 'Dictionary already prepared'}]
                    case['length_study'] = {
                        'bytes': length,
                        'dictionary_size': 128,
                        'variants': 4,
                        'language': 'en',
                        'match': state,
                        'variant_indices': variant_indices,
                    }
                    assert all(d['facts']['bytes'] == length for j in case['jobs'] for d in j['documents'])
    files = g.pack()
    index = json.loads(files['index.json'])
    index.update(
        status='Saved fixed-length inputs with independently computed expected output.',
        scope='English controlled input-length series, fixed 128-key dictionaries.',
        source_sha256={
            str(p.relative_to(ROOT.parent)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in [
                ROOT / 'paragraphs.json',
                PRODUCT / 'generate.py',
                SCALING / 'moderation-words.json',
                SCALING / 'support-terms.json',
            ]
        },
    )
    files['index.json'] = json.dumps(index, ensure_ascii=False, indent=2) + '\n'
    descriptions = [
        '# Fixed-length cases',
        '',
        (
            'Every case reuses one prepared 128-key dictionary. Only the worker lifecycle is measured. '
            'One operation processes one string; four different exact-length variants cycle equally often.'
        ),
        '',
        '| Case | Operation | Bytes/string | Variants | Keys | Occurrences/string |',
        '|---|---|---:|---:|---:|---|',
    ]
    for group in g.SUITES.values():
        for case in group:
            counts = [document['facts']['occurrences'] for job in case['jobs'] for document in job['documents']]
            extent = str(counts[0]) if len(set(counts)) == 1 else f'{min(counts)}–{max(counts)}'
            descriptions.append(
                f'| `{case["id"]}` | {case["operation"]} | {case["length_study"]["bytes"]} | 4 | 128 | {extent} |'
            )
    descriptions += [
        '',
        (
            'Search results preserve nested literal matches. Replacements use the longest key at '
            'the earliest position without rescanning inserted URLs. Dictionaries, texts and expected '
            'outputs are saved in the suite JSON. These are controlled authored examples, not production traces.'
        ),
        '',
    ]
    files['CASES.md'] = '\n'.join(descriptions)
    return files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    files = build()
    for name, text in files.items():
        path = ROOT / name
        if args.check:
            assert path.exists() and path.read_text() == text, name
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text)
    print('Fixed-length corpus PASS:', sum(len(cases) for cases in g.SUITES.values()), 'cases')


if __name__ == '__main__':
    main()
