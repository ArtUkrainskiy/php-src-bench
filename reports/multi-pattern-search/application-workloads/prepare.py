#!/usr/bin/env python3
"""Freeze open source inputs and independent expected outputs; never time code."""
import argparse
import ast
import concurrent.futures
import hashlib
import json
from pathlib import Path
import re
import time
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parent
SEED = 'strmatch-application-v1'
LOWER = bytes.maketrans(b'ABCDEFGHIJKLMNOPQRSTUVWXYZ', b'abcdefghijklmnopqrstuvwxyz')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def rank(identity):
    return digest((SEED + '\0' + identity).encode())


def fetch(url):
    for attempt in range(3):
        try:
            request = urllib.request.Request(url, headers={'User-Agent': 'php-src-bench-corpus/1'})
            with urllib.request.urlopen(request, timeout=30) as response:
                return response.read()
        except Exception:
            if attempt == 2:
                raise
            time.sleep(1)


def occurrences(subject, keys):
    hits = []
    for key in keys:
        needle = key.encode()
        offset = 0
        while True:
            start = subject.find(needle, offset)
            if start < 0:
                break
            hits.append({'offset': start, 'length': len(needle), 'keyword': key})
            offset = start + 1
    hits.sort(key=lambda h: (h['offset'], h['length']))
    return hits


def replacement(subject, mapping):
    hits = occurrences(subject, list(mapping))
    hits.sort(key=lambda h: (h['offset'], -h['length']))
    cursor, parts, selected = 0, [], []
    for hit in hits:
        start = hit['offset']
        if start < cursor:
            continue
        parts.extend([subject[cursor:start], mapping[hit['keyword']].encode()])
        cursor = start + hit['length']
        selected.append(hit)
    parts.append(subject[cursor:])
    return b''.join(parts).decode(), selected


def profile(subject, keys, hits):
    unique = list(dict.fromkeys(h['keyword'] for h in hits))
    intervals = sorted((h['offset'], h['offset'] + h['length']) for h in hits)
    covered, end = 0, 0
    for left, right in intervals:
        covered += max(0, right - max(left, end))
        end = max(end, right)
    return {'bytes': len(subject), 'keys': len(keys),
            'key_byte_lengths': sorted(set(len(k.encode()) for k in keys)),
            'occurrences': len(hits), 'unique_matched_keys': len(unique),
            'first_offset': hits[0]['offset'] if hits else None,
            'matched_dictionary_ranks': [keys.index(k) + 1 for k in unique],
            'covered_bytes': covered}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-cache', type=Path, required=True)
    parser.add_argument('--download-cache', type=Path, required=True)
    args = parser.parse_args()
    args.download_cache.mkdir(parents=True, exist_ok=True)
    cache = json.loads(args.source_cache.read_text())
    candidates = json.loads((ROOT / 'sources.candidate.json').read_text())
    blobs = {('python/' if s['id'] == 'cpython' else 'emails/') + f['path']: f['git_blob_sha']
             for s in candidates['sources'] if s['id'] in ['cpython', 'groundmail']
             for f in s.get('documents', s.get('candidate_files', []))}
    source_files = []
    for identity, item in sorted(cache.items()):
        data = item['content'].encode()
        if identity in blobs:
            blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
            if blob != blobs[identity]:
                raise RuntimeError('Source blob mismatch: ' + identity)
        path = ROOT / 'sources' / identity
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        source_files.append({'id': identity, 'path': str(path.relative_to(ROOT)),
                             'sha256': digest(data), 'bytes': len(data),
                             'revision': item['revision'], 'url': item['url']})

    # Dataset-server responses are cached and hashed. Re-running does not silently
    # replace the exact acquired records with an updated upstream dataset.
    offsets = [round(i * (97320 - 32) / 7) for i in range(8)]
    def page(offset):
        url = 'https://datasets-server.huggingface.co/rows?' + urllib.parse.urlencode({
            'dataset': 'google/civil_comments', 'config': 'default', 'split': 'test',
            'offset': offset, 'length': 32})
        path = args.download_cache / ('civil-' + str(offset) + '.json')
        if not path.exists():
            path.write_bytes(fetch(url))
        raw = path.read_bytes()
        result = json.loads(raw)
        if len(result['rows']) != 32 or result['num_rows_total'] != 97320:
            raise RuntimeError('Unexpected source population')
        return url, raw, result['rows']
    pages = list(concurrent.futures.ThreadPoolExecutor(max_workers=2).map(page, offsets))
    docs, source_rows, duplicate_rows, unique_hashes = {}, [], [], set()
    for url, raw, rows in pages:
        for row in rows:
            identity = 'comment.' + str(row['row_idx'])
            data = row['row']['text'].encode()
            path = ROOT / 'inputs' / 'comments' / (identity + '.txt')
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
            docs[identity] = {'id': identity, 'path': str(path.relative_to(ROOT)),
                              'sha256': digest(data), 'bytes': len(data), 'source_row': row['row_idx']}
            source_rows.append({'id': identity, 'request': url, 'response_sha256': digest(raw)})
            folded_sha = digest(data.translate(LOWER))
            if folded_sha in unique_hashes:
                duplicate_rows.append(identity)
            else:
                unique_hashes.add(folded_sha)
    comment_ids = list(docs)
    unique_comments = [i for i in comment_ids if i not in duplicate_rows]
    by_size = sorted(unique_comments, key=lambda i: (docs[i]['bytes'], i))
    selected_comments = []
    for q in range(4):
        group = by_size[len(by_size) * q // 4:len(by_size) * (q + 1) // 4]
        selected_comments += sorted(group, key=rank)[:4]
    assert len(selected_comments) == 16
    batch_comments = sorted(unique_comments, key=rank)[:64]
    assert len(batch_comments) == 64
    words = list(dict.fromkeys(line.encode().translate(LOWER).decode()
                               for line in cache['banwords/en']['content'].splitlines() if line))
    mapping_node = next(node.value for node in ast.parse(cache['python/fix_imports.py']['content']).body
                        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'MAPPING' for t in node.targets))
    mapping = ast.literal_eval(mapping_node)
    assert len(mapping) == 48
    dictionaries = {'banwords': {'keys': words, 'policy': 'ascii-insensitive'},
                    'module-renames': {'keys': list(mapping), 'replacements': mapping, 'policy': 'case-sensitive'}}
    document_ids = []
    for source in source_files:
        if source['id'].startswith('python/Doc/'):
            identity = 'document.' + Path(source['id']).stem
            docs[identity] = {'id': identity, **{k: source[k] for k in ['path', 'sha256', 'bytes']}}
            document_ids.append(identity)
    assert len(document_ids) == 16
    document_ids.sort(key=rank)

    cases, inventory = [], []
    def add(identity, family, operation, document, dictionary, modes):
        doc, entry = docs[document], dictionaries[dictionary]
        raw = (ROOT / doc['path']).read_bytes()
        processed = raw.translate(LOWER) if entry['policy'] == 'ascii-insensitive' else raw
        keys = entry['keys']
        hits = occurrences(processed, keys)
        expected = {'any': bool(hits), 'unique': list(dict.fromkeys(h['keyword'] for h in hits)),
                    'count': len(hits), 'all': hits}
        stats = profile(processed, keys, hits)
        methods = ['native']
        if operation == 'replace':
            result, chosen = replacement(raw, entry['replacements'])
            expected['replace'] = result
            stats.update(replacements=len(chosen), output_bytes=len(result.encode()))
            methods += ['strtr', 'preg_literal_callback', 'preg_trie_callback']
            sequential = raw
            for key in sorted(keys, key=lambda k: -len(k.encode())):
                sequential = sequential.replace(key.encode(), entry['replacements'][key].encode())
            if sequential == result.encode():
                methods += ['str_replace']
            if family == 'email':
                methods += ['preg_tokens_callback']
        else:
            methods += ['string_loop', 'preg_literal', 'preg_trie']
            if entry['policy'] == 'ascii-insensitive':
                methods += ['folded_string_loop']
        case = {'id': identity, 'family': family, 'operation': operation, 'documents': [document],
                'dictionary': dictionary, 'policy': entry['policy'], 'modes': modes, 'methods': methods,
                'expected': {document: expected[operation]}, 'input': stats}
        cases.append(case)
        inventory.append({'case': identity, 'document': document, 'dictionary': dictionary,
                          'processed_sha256': digest(processed), **stats})
        return case
    for document in selected_comments:
        for operation in ['any', 'unique']:
            add(document + '.' + operation, 'validation', operation, document, 'banwords', ['prepared', 'oneshot'])
    for document in document_ids:
        for operation in ['unique', 'count', 'all', 'replace']:
            add(document + '.' + operation, 'rewrite' if operation == 'replace' else 'references',
                operation, document, 'module-renames', ['prepared', 'oneshot'])
    for source in source_files:
        if not source['id'].startswith('emails/templates/'):
            continue
        relative = Path(source['id'])
        family = relative.parent.name
        form = relative.suffix[1:]
        identity = 'email.' + family + '.' + form
        docs[identity] = {'id': identity, **{k: source[k] for k in ['path', 'sha256', 'bytes']}, 'template_family': family}
        tokens = list(dict.fromkeys(re.findall(r'\{\{[a-zA-Z0-9_]+\}\}', cache[source['id']]['content'])))
        if not tokens:
            raise RuntimeError('No literal tokens in ' + identity)
        def value(token):
            name = token[2:-2]
            suffix = rank(family + ':' + name)[:12]
            if 'url' in name or 'link' in name:
                return 'https://example.test/' + name.replace('_', '/') + '/' + suffix
            if 'email' in name:
                return 'alex.' + suffix[:4] + '@example.test'
            if 'name' in name:
                return 'Alexandra Morgan' if int(suffix[0], 16) % 2 else 'Sam Lee'
            if 'amount' in name or 'price' in name:
                return '$49.00'
            if 'date' in name or 'time' in name or 'expires' in name:
                return '30 minutes' if 'expires' in name else '2026-11-09 12:30 UTC'
            if 'code' in name:
                return '482917'
            return name.replace('_', ' ').capitalize() + ' ' + suffix[:6]
        dictionary_id = 'payload.' + family + '.' + form
        dictionaries[dictionary_id] = {'keys': tokens, 'replacements': {t: value(t) for t in tokens},
                                       'policy': 'case-sensitive', 'payload_kind': 'documented-fixture-values'}
        add(identity, 'email', 'replace', identity, dictionary_id, ['oneshot'])

    single_count = len(cases)
    def batch(family, operation, members, dictionary):
        # Expected values are computed from each member, not averaged subjects.
        expected, eligible = {}, None
        for member in members:
            temporary = add('__oracle__', family, operation, member, dictionary, ['oneshot'])
            expected[member] = temporary['expected'][member]
            eligible = set(temporary['methods']) if eligible is None else eligible.intersection(temporary['methods'])
            cases.pop()
            inventory.pop()
        cases.append({'id': 'batch.' + family + '.' + operation + '.b' + str(len(members)),
                      'family': family, 'operation': operation, 'documents': members,
                      'dictionary': dictionary, 'policy': dictionaries[dictionary]['policy'],
                      'modes': ['batch'], 'methods': [m for m in temporary['methods'] if m in eligible], 'expected': expected,
                      'batch_size': len(members), 'total_bytes': sum(docs[i]['bytes'] for i in members)})
    for count in [1, 4, 16, 64]:
        for operation in ['any', 'unique']:
            batch('validation', operation, batch_comments[:count], 'banwords')
    for count in [1, 4, 16]:
        for operation in ['unique', 'count', 'all', 'replace']:
            batch('rewrite' if operation == 'replace' else 'references', operation, document_ids[:count], 'module-renames')
    assert single_count == 120 and len(cases) == 140, (single_count, len(cases))
    save(ROOT / 'corpus.json', {'format': 1, 'seed': SEED, 'sources': source_files,
         'documents': docs, 'dictionaries': dictionaries, 'cases': cases,
         'selection': {'comment_windows': offsets, 'selected_comments': selected_comments,
                       'batch_comments': batch_comments, 'duplicate_comment_rows': duplicate_rows,
                       'document_order': document_ids, 'source_rows': source_rows}})
    save(ROOT / 'inventory.json', {'single_document_cases': inventory, 'single_count': single_count,
                                  'batch_count': len(cases) - single_count,
                                  'comment_pool': len(comment_ids), 'unique_processed_comments': len(unique_comments)})
    print(json.dumps({'status': 'corpus-frozen', 'single_cases': single_count,
                      'batch_cases': len(cases) - single_count, 'comments': len(comment_ids),
                      'banwords': len(words), 'source_files': len(source_files)}, indent=2), flush=True)


if __name__ == '__main__':
    main()
