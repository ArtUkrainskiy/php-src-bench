#!/usr/bin/env python3
"""Save deterministic memory inputs; preserve the measured glossary through 512 terms."""
import argparse
import hashlib
import itertools
import json
from pathlib import Path
import random

ROOT = Path(__file__).resolve().parent
SIZES = [8, 16, 32, 64, 128, 256, 512, 1000, 2000, 5000, 10000]


def encoded(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + '\n'


def build():
    glossary = ROOT / '../../../corpus/multi-pattern-scaling/support-terms.json'
    words = json.loads(glossary.read_text())['words']
    assert len(words) == len(set(words)) == 512
    # Constructed catalog labels, not a mined production dictionary.
    adjectives = ('compact portable lightweight adjustable durable insulated folding '
                  'reusable wireless waterproof travel outdoor indoor rechargeable '
                  'ergonomic magnetic stainless ceramic wooden cotton recycled '
                  'premium classic modern flexible washable transparent protective '
                  'stackable decorative thermal breathable reflective modular '
                  'universal digital automatic manual quiet rugged slim sturdy solar').split()
    products = ('backpack bottle camera charger keyboard mouse speaker headset '
                'lamp blanket pillow notebook organizer basket container shelf '
                'mirror towel jacket gloves wallet suitcase umbrella desk chair '
                'tripod adapter cable monitor printer scanner projector timer '
                'scale kettle blender filter cushion').split()
    variants = ['for home', 'for travel', 'for work', 'for children', 'for camping', 'for everyday use']
    catalog = [' '.join(parts) for parts in itertools.product(adjectives, products, variants)]
    random.Random(20261102).shuffle(catalog)
    words = (words + catalog)[:10000]
    assert len(words) == len(set(words)) == 10000
    shuffled = []
    seen = set()
    rng = random.Random(20261103)
    for word in words:
        chars = list(word)
        while True:
            rng.shuffle(chars)
            candidate = ''.join(chars)
            if candidate not in seen and candidate != word:
                break
        shuffled.append(candidate)
        seen.add(candidate)
    files = {}
    index = {'sizes': SIZES, 'families': {}, 'files_sha256': {}}
    for family, keys in [('glossary-catalog', words), ('permuted-control', shuffled)]:
        replacements = {key: f'https://help.example.test/topic/{i:05d}' for i, key in enumerate(keys)}
        sentence = ' | '.join(keys[:8]) + ' | Please contact the support team about your purchase.\n'
        subject = (sentence * (65536 // len(sentence) + 1))[:65536]
        files[family + '.json'] = encoded({'replacements': replacements})
        files[family + '.txt'] = subject
        rows = []
        for size in SIZES:
            selected = keys[:size]
            hits = []
            for key in selected:
                start = 0
                while (offset := subject.find(key, start)) >= 0:
                    hits.append((offset, len(key), key))
                    start = offset + 1
            hits.sort()
            unique = list(dict.fromkeys(hit[2] for hit in hits))
            fragments = []
            end = 0
            replaced = 0
            # Independent leftmost-longest replacement oracle, derived from all hits.
            for offset, length, key in sorted(hits, key=lambda h: (h[0], -h[1])):
                if offset < end:
                    continue
                fragments.extend([subject[end:offset], replacements[key]])
                end = offset + length
                replaced += 1
            fragments.append(subject[end:])
            output = ''.join(fragments)
            signature = ''.join(f'{offset}:{length}:{key}\n' for offset, length, key in hits)
            prefix = {''}
            suffix = {''}
            for key in selected:
                prefix.update(key[:i] for i in range(1, len(key) + 1))
                suffix.update(key[-i:] for i in range(1, len(key) + 1))
            rows.append({
                'size': size, 'keyword_bytes': sum(map(len, selected)),
                'min_length': min(map(len, selected)), 'max_length': max(map(len, selected)),
                'alphabet_bytes': len(set(''.join(selected))),
                'matcher_states': len(prefix), 'replacer_states': len(suffix),
                'subject_bytes': len(subject), 'matches': bool(hits), 'countMatches': len(hits),
                'getMatchedKeywords': unique, 'matchAll_sha256': hashlib.sha256(signature.encode()).hexdigest(),
                'replace_sha256': hashlib.sha256(output.encode()).hexdigest(),
                'replacement_count': replaced, 'output_bytes': len(output),
            })
        files[family + '-expected.json'] = encoded(rows)
        index['families'][family] = {'dictionary': family + '.json', 'subject': family + '.txt',
                                     'expected': family + '-expected.json'}
    index['glossary_sha256'] = hashlib.sha256(glossary.read_bytes()).hexdigest()
    index['generator_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    index['files_sha256'] = {name: hashlib.sha256(text.encode()).hexdigest() for name, text in files.items()}
    files['index.json'] = encoded(index)
    return files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    for name, text in build().items():
        path = ROOT / name
        if args.check:
            if not path.exists() or path.read_text() != text:
                raise SystemExit('Stale memory fixture: ' + name)
        else:
            path.write_text(text)
    print('Memory fixtures PASS: 2 families, 11 sizes, saved dictionaries and 64 KiB inputs')


if __name__ == '__main__':
    main()
