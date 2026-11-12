#!/usr/bin/env python3
"""Generates benchmark cells. A cell stores its pool as corpus offsets plus the keys written into every
window, so each text is rebuilt byte for byte from the corpus; the generator checks that every window
yields exactly the intended occurrences.

    python3 tools/cells.py <set> [<set>...]     # sets: controlled crossover natural languages scenarios counterexamples pages
"""
import hashlib
import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POOL_BYTES = 2 * 1024 * 1024
MIN_TEXTS = 64


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def occurrences(text, keys):
    hits = []
    for key in keys:
        needle = key.encode()
        at = text.find(needle)
        while at >= 0:
            hits.append((at, key))
            at = text.find(needle, at + 1)
    return sorted(hits)


def random_keys(count, seed, lengths=(4, 16), alphabet='abcdefghijklmnop', avoid=b''):
    """Distinct keys of random letters; no key is a substring of another or of `avoid`."""
    rng = random.Random(seed)
    keys = []
    while len(keys) < count:
        key = ''.join(rng.choice(alphabet) for _ in range(rng.randint(*lengths)))
        if key.encode() in avoid or any(key in old or old in key for old in keys):
            continue
        keys.append(key)
    return keys


def pool(corpus, length, place, keys, seed):
    """Window offsets of `length` bytes; place(rng) gives each window its own [(offset, key)] insertions,
    and the window must contain exactly those occurrences."""
    data = (ROOT / corpus).read_bytes()
    rng = random.Random(seed)
    count = max(MIN_TEXTS, POOL_BYTES // length)
    offsets, inserts, tries = [], [], 0
    while len(offsets) < count:
        tries += 1
        if tries > count * 50:
            raise SystemExit(f'cannot fill pool: {corpus} {length} {len(offsets)}/{count}')
        at = rng.randrange(0, len(data) - length)
        insert = sorted(place(rng))
        window = bytearray(data[at:at + length])
        for offset, key in insert:
            window[offset:offset + len(key)] = key.encode()
        if occurrences(bytes(window), keys) == insert:
            offsets.append(at)
            inserts.append([[o, k] for o, k in insert])
    return {'corpus': corpus, 'corpus_sha256': sha(ROOT / corpus), 'length': length, 'offsets': offsets, 'inserts': inserts}


def natural_pool(corpus, length, keys, seed):
    """Window offsets of `length` bytes at random positions; occurrences are whatever the text contains."""
    data = (ROOT / corpus).read_bytes()
    rng = random.Random(seed)
    count = max(MIN_TEXTS, POOL_BYTES // length)
    offsets = [rng.randrange(0, len(data) - length) for _ in range(count)]
    hits = [len(occurrences(data[at:at + length], keys)) for at in offsets]
    hits.sort()
    return {'corpus': corpus, 'corpus_sha256': sha(ROOT / corpus), 'length': length, 'offsets': offsets, 'insert': [],
            'occurrences': {'min': hits[0], 'median': hits[len(hits) // 2], 'max': hits[-1],
                            'texts_with_matches': sum(1 for h in hits if h)}}


def documents_pool(corpus, keys, fold=False, size=None):
    """Every document of a JSON corpus, in a fixed shuffled order; occurrences are whatever the documents contain.
    `size` = (min, max) keeps only documents of min <= bytes < max."""
    docs = json.loads((ROOT / corpus).read_text())
    order = list(range(len(docs)))
    random.Random(corpus).shuffle(order)
    if size:
        order = [i for i in order if size[0] <= len(docs[i].encode()) < size[1]]
        docs = [docs[i] for i in sorted(order)]
    hits = sorted(len(occurrences((d.lower() if fold else d).encode(), keys)) for d in docs)
    lengths = sorted(len(d.encode()) for d in docs)
    return {'documents': corpus, 'corpus_sha256': sha(ROOT / corpus), 'indices': order,
            'bytes': {'median': lengths[len(lengths) // 2], 'max': lengths[-1], 'total': sum(lengths)},
            'occurrences': {'min': hits[0], 'median': hits[len(hits) // 2], 'max': hits[-1],
                            'texts_with_matches': sum(1 for h in hits if h)}}


def middle(length, key):
    """One occurrence at a random offset in the middle third of the text."""
    return lambda rng: [(rng.randint(length // 3, 2 * length // 3 - len(key)), key)]


def spread(length, keys, ranks):
    """One occurrence per rank, each at a random offset inside its own equal segment of the text."""
    width = length // len(ranks)
    return lambda rng: [(i * width + rng.randint(0, width - len(keys[r])), keys[r]) for i, r in enumerate(ranks)]


def near(start, end, key):
    """One occurrence at a random offset in [start, end)."""
    return lambda rng: [(rng.randint(start, end - 1), key)]


NONE = lambda rng: []


def write(group, cell):
    path = ROOT / 'cells' / group / f"{cell['id']}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(cell, ensure_ascii=False, separators=(',', ':')) + '\n')
    print(group, cell['id'], len(cell['pool'].get('offsets') or cell['pool']['indices']), 'texts')


def dictionary_cell(op, keys):
    return {'mapping': {k: k.upper() for k in keys}} if op == 'replace' else {'keys': keys}


OPS = ['any', 'unique', 'count', 'all', 'replace']
LENGTHS = [128, 1024, 4096, 16384, 65536]


def controlled():
    """Random keys of 4-16 letters a-p, absent from the corpus; occurrences are written into every window."""
    corpus = 'corpus/en.txt'
    family = random_keys(1024, 'controlled-1024', avoid=(ROOT / corpus).read_bytes())
    for n in [8, 16, 32, 128, 1024]:
        keys = family[:n]
        key = keys[n // 2]
        for length in LENGTHS:
            variants = {'one': middle(length, key)}
            if length >= 1024:
                ranks = [min(n - 1, (2 * i + 1) * n // 32) for i in range(16)]
                variants['spread16'] = spread(length, keys, ranks)
            for op in OPS:
                cases = dict(variants)
                if op in ('any', 'replace'):
                    cases['absent'] = NONE
                if op == 'any':
                    cases.pop('spread16', None)
                    if length in (4096, 65536):
                        cases['start'] = near(0, 64, key)
                        cases['end'] = near(length - len(key) - 64, length - len(key) + 1, key)
                for name, insert in cases.items():
                    cell = {'id': f'{op}.n{n}.b{length}.{name}', 'op': op, 'grid': 'controlled', 'condition': name,
                            **dictionary_cell(op, keys)}
                    cell['pool'] = pool(corpus, length, insert, keys, f'controlled.{cell["id"]}')
                    write('controlled', cell)


def crossover():
    """One-shot only, between 1 KiB and 4 KiB: where building the object for one call starts to pay off."""
    corpus = 'corpus/en.txt'
    family = random_keys(1024, 'controlled-1024', avoid=(ROOT / corpus).read_bytes())
    names = json.loads((ROOT / 'dictionaries/php-identifiers.json').read_text())
    for length in [1536, 2048, 3072]:
        for n in [16, 32, 128, 1024]:
            keys = family[:n]
            for op in OPS:
                cases = {'one': middle(length, keys[n // 2])}
                if op in ('any', 'replace'):
                    cases['absent'] = NONE
                for name, insert in cases.items():
                    cell = {'id': f'{op}.n{n}.b{length}.{name}', 'op': op, 'grid': 'crossover', 'modes': ['oneshot'],
                            **dictionary_cell(op, keys)}
                    cell['pool'] = pool(corpus, length, insert, keys, f'crossover.{cell["id"]}')
                    write('crossover', cell)
        for n in [32, 128, 512]:
            keys = names[:n]
            for op in OPS:
                cell = {'id': f'{op}.names{n}.b{length}', 'op': op, 'grid': 'crossover', 'modes': ['oneshot'],
                        **dictionary_cell(op, keys)}
                cell['pool'] = natural_pool(corpus, length, keys, f'crossover.{cell["id"]}')
                write('crossover', cell)


def natural():
    """PHP manual identifiers over the English manual text; occurrences are natural."""
    corpus = 'corpus/en.txt'
    family = json.loads((ROOT / 'dictionaries/php-identifiers.json').read_text())
    for n in [8, 32, 128, 512, 2048]:
        keys = family[:n]
        for length in [128, 1024, 4096, 65536]:
            for op in OPS:
                cell = {'id': f'{op}.n{n}.b{length}', 'op': op, 'grid': 'natural', **dictionary_cell(op, keys)}
                cell['pool'] = natural_pool(corpus, length, keys, f'natural.{cell["id"]}')
                write('natural', cell)


def languages():
    """Each corpus with words of its own language and with PHP identifiers; occurrences are natural."""
    identifiers = json.loads((ROOT / 'dictionaries/php-identifiers.json').read_text())[:128]
    for lang in ['en', 'es', 'ru', 'zh', 'ja', 'ko', 'emoji']:
        words = json.loads((ROOT / f"dictionaries/words-{'en' if lang == 'emoji' else lang}.json").read_text())
        for dictionary, keys in [('words', words), ('identifiers', identifiers)]:
            for length in [4096, 65536]:
                for op in OPS:
                    cell = {'id': f'{lang}.{dictionary}.{op}.b{length}', 'op': op, 'grid': 'languages',
                            'language': lang, 'dictionary': dictionary, **dictionary_cell(op, keys)}
                    cell['pool'] = natural_pool(f'corpus/{lang}.txt', length, keys, f'languages.{cell["id"]}')
                    write('languages', cell)


def scenarios():
    """Product scenarios on real dictionaries and real texts."""
    load = lambda name: json.loads((ROOT / f'dictionaries/{name}.json').read_text())
    moderation = [k.lower() for k in load('ldnoobw-en')]
    for op in ['any', 'unique']:
        cell = {'id': f'moderation.{op}', 'op': op, 'grid': 'scenarios', 'policy': 'ascii-insensitive', 'keys': moderation}
        cell['pool'] = documents_pool('corpus/comments.json', moderation, fold=True)
        write('scenarios', cell)
    bots = load('crawler-patterns')
    for op in ['any', 'unique']:
        cell = {'id': f'bots.{op}', 'op': op, 'grid': 'scenarios', 'keys': bots}
        cell['pool'] = documents_pool('corpus/user-agents.json', bots)
        write('scenarios', cell)
    functions = load('php-functions')
    links = {name: f'<a href="https://www.php.net/function.{name.replace("_", "-")}">{name}</a>' for name in functions}
    for op in ['replace', 'all', 'unique']:
        cell = {'id': f'autolink.{op}', 'op': op, 'grid': 'scenarios'}
        cell.update({'mapping': links} if op == 'replace' else {'keys': functions})
        cell['pool'] = documents_pool('corpus/manual-pages.json', functions)
        write('scenarios', cell)


PAGE_SIZES = [(1024, 2048), (2048, 4096), (4096, 16384)]


def pages():
    """Auto-linking on whole manual pages grouped by length, with the full name list and random subsets of it."""
    functions = json.loads((ROOT / 'dictionaries/php-functions.json').read_text())
    for n in [128, 512, len(functions)]:
        names = functions[:n]
        links = {name: f'<a href="https://www.php.net/function.{name.replace("_", "-")}">{name}</a>' for name in names}
        for low, high in PAGE_SIZES:
            for op in ['replace', 'all']:
                cell = {'id': f'autolink.{op}.n{n}.p{low}', 'op': op, 'grid': 'pages'}
                cell.update({'mapping': links} if op == 'replace' else {'keys': names})
                cell['pool'] = documents_pool('corpus/manual-pages.json', names, size=(low, high))
                write('pages', cell)


def counterexamples():
    """Where existing functions are expected to win: one or four keys, and dense results."""
    corpus = 'corpus/en.txt'
    family = random_keys(1024, 'controlled-1024', avoid=(ROOT / corpus).read_bytes())
    for n in [1, 4]:
        keys = family[:n]
        key = keys[n // 2]
        for op in ['any', 'unique', 'count', 'replace']:
            cell = {'id': f'few.{op}.n{n}.b4096', 'op': op, 'grid': 'counterexamples', **dictionary_cell(op, keys)}
            cell['pool'] = pool(corpus, 4096, middle(4096, key), keys, f'counterexamples.{cell["id"]}')
            write('counterexamples', cell)
    frequent = json.loads((ROOT / 'dictionaries/words-en-frequent.json').read_text())
    for length in [4096, 65536]:
        for op in ['unique', 'count', 'all', 'replace']:
            cell = {'id': f'dense.{op}.b{length}', 'op': op, 'grid': 'counterexamples', **dictionary_cell(op, frequent)}
            cell['pool'] = natural_pool(corpus, length, frequent, f'counterexamples.{cell["id"]}')
            write('counterexamples', cell)


if __name__ == '__main__':
    sets = {'controlled': controlled, 'crossover': crossover, 'natural': natural, 'languages': languages,
            'scenarios': scenarios, 'counterexamples': counterexamples, 'pages': pages}
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for name in sys.argv[1:]:
        sets[name]()
