#!/usr/bin/env python3
"""Audit frozen inputs and case metadata without running PHP or measuring time."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
from email import policy
from email.parser import Parser

ROOT = Path(__file__).resolve().parent.parent


def parts(text, delimiter=','):
    """Split the literal PHP expressions used by these fixtures, outside nesting/quotes."""
    result, start, depth, quoted, i = [], 0, 0, False, 0
    while i < len(text):
        char = text[i]
        if quoted:
            if char == '\\':
                i += 2
                continue
            if char == "'":
                quoted = False
        elif char == "'":
            quoted = True
        elif char in '[(':
            depth += 1
        elif char in '])':
            depth -= 1
            assert depth >= 0, text
        elif depth == 0 and text.startswith(delimiter, i):
            result.append(text[start:i].strip())
            i += len(delimiter)
            start = i
            continue
        i += 1
    assert not quoted and depth == 0, text
    result.append(text[start:].strip())
    return result


def literal(text):
    assert len(text) >= 2 and text[0] == text[-1] == "'", text
    return re.sub(r"\\(['\\])", r'\1', text[1:-1])


def expression_needles(case):
    match = re.fullmatch(r'([a-z_]+)\((.*)\)', case['code'], re.S)
    assert match, case['name']
    function, arguments = match.groups()
    args = parts(arguments)
    aliases = {'compact_moderate': 'str_contains', 'compact_read_record': 'stream_get_line'}
    assert aliases.get(function, function) == case['api'], case['name']
    haystack_argument = 2 if function in ['str_replace', 'str_ireplace'] else 1 if function == 'explode' else 0
    if function == 'compact_read_record':
        assert args[1] == 'strlen($s)', case['name']
        assert f'fwrite({args[0]}, $s)' in case['setup'], case['name']
    else:
        assert args[haystack_argument] == '$s', case['name']
    if function in ['str_replace', 'str_ireplace', 'explode']:
        needle = args[0]
    elif function == 'compact_read_record':
        needle = args[2]
    elif function == 'strtr':
        assert args[1][0] == '[' and args[1][-1] == ']'
        keys = [literal(parts(entry, '=>')[0]) for entry in parts(args[1][1:-1])]
        assert len(keys) == 1, 'Only the single-key strtr path belongs in this corpus'
        return keys
    else:
        assert function in ['compact_moderate', 'strpos', 'str_contains', 'strstr', 'strchr',
            'substr_count', 'mb_strpos', 'mb_stripos', 'mb_strstr', 'mb_stristr',
            'mb_substr_count', 'grapheme_strpos', 'grapheme_stripos', 'grapheme_strstr'], function
        needle = args[1]
    if function == 'strpos':
        offset = int(args[2]) if len(args) > 2 else 0
        assert 0 <= offset <= case['bytes'] and offset == case.get('search_offset_bytes', 0), case['name']
    if needle.startswith('['):
        assert needle.endswith(']')
        return [literal(value) for value in parts(needle[1:-1])]
    return [literal(needle)]


def audit(root):
    index = json.loads((root / 'index.json').read_text())
    assert index['format'] == 1
    seen, rows, moderation = set(), [], {}
    for suite in index['suites']:
        path = root / suite['file']
        assert path.parent == root and path.suffix == '.json'
        assert hashlib.sha256(path.read_bytes()).hexdigest() == suite['sha256'], path
        data = json.loads(path.read_text())
        assert data['suite'] == suite['name']
        assert len(data['cases']) == suite['cases']
        assert len(data['inputs']) == suite['inputs']
        assert sum(c['benchmark'] for c in data['cases']) == suite['benchmark_cases']
        used, sizes, lengths = set(), [], []
        for key, value in data['inputs'].items():
            raw = value['text'].encode('utf-8')
            assert len(raw) == value['bytes'], key
            assert hashlib.sha256(raw).hexdigest() == value['sha256'], key
        for case in data['cases']:
            name = case['name']
            assert name not in seen, name
            seen.add(name)
            used.add(case['input'])
            value = data['inputs'][case['input']]
            raw = value['text'].encode('utf-8')
            remaining = len(raw) - case.get('search_offset_bytes', 0)
            assert case['bytes'] == len(raw) and remaining == case['entry_remaining_bytes'], name
            assert case['sha256'] == value['sha256'], name
            ns = [n.encode('utf-8') for n in case['needles']]
            assert expression_needles(case) == case['needles'], name
            diagnostic = case['panel'] == 'control' and data['suite'].startswith('controls-')
            assert ns and all(1 <= len(n) <= 256 for n in ns), name
            if not diagnostic:
                assert all(9 <= len(n) <= 31 for n in ns), name
            assert [len(n) for n in ns] == case['needle_bytes'], name
            hay = raw.lower() if case['ascii_folded_fixture'] else raw
            positions = [hay.find(n.lower() if case['ascii_folded_fixture'] else n) for n in ns]
            assert positions == case['positions'], name
            assert case['position_unit'] == 'UTF-8 bytes', name
            compact = remaining >= 1024 and min(map(len, ns)) >= 9 and max(map(len, ns)) <= 31
            route = ('existing inline control' if remaining < 1024 or max(map(len, ns)) < 9 else
                     'wide Sunday control' if min(map(len, ns)) >= 32 else 'compact Sunday')
            assert case['entry_path'] == route, name
            assert case['family'] == suite['family'], name
            if case.get('document', '').startswith('log_'):
                records = [json.loads(line) for line in value['text'].splitlines()]
                assert len(records) >= 20 and all(isinstance(r, dict) for r in records), name
                assert len({r['request_id'] for r in records}) == len(records), name
                assert len({r['order_id'] for r in records}) == len(records), name
                assert all(r['order_id'].startswith('order-2026-') for r in records), name
            if case.get('document', '').startswith('mail_'):
                message = Parser(policy=policy.default).parsestr(value['text'])
                assert message.is_multipart() and message.get_boundary() == 'message-boundary-42', name
                assert not message.defects, name
                leaves = [p for p in message.walk() if not p.is_multipart()]
                assert len(leaves) >= 2 and all(not p.defects for p in leaves), name
                assert {'text/plain', 'text/html'} <= {p.get_content_type() for p in leaves}, name
                for part in leaves:
                    if part.get_content_type() == 'application/json':
                        assert isinstance(json.loads(part.get_payload(decode=True)), dict), name
            if 'replacement_bytes' in case:
                comparison = (case['replacement_bytes'] > len(ns[0])) - (case['replacement_bytes'] < len(ns[0]))
                assert comparison == {'shorter': -1, 'equal': 0, 'longer': 1}[case['replacement_kind']], name
            if 'match_count' in case:
                count = hay.count(ns[0].lower() if case['ascii_folded_fixture'] else ns[0])
                assert count == case['match_count'], name
            if case.get('spacing'):
                occurrences, at = [], 0
                while True:
                    at = hay.find(ns[0], at)
                    if at < 0:
                        break
                    occurrences.append(at)
                    at += len(ns[0])
                assert len({b-a for a,b in zip(occurrences, occurrences[1:])}) > 1, name
            if case['state'] == 'absent':
                assert all(p == -1 for p in positions), name
            elif case['state'] == 'origin':
                assert positions == [case.get('search_offset_bytes', 0)], name
            elif case['state'] in ['start', 'middle', 'end']:
                hits = [(p, len(n)) for p, n in zip(positions, ns) if p >= 0]
                assert len(hits) == 1, name
                position, length = hits[0]
                if case['state'] == 'start':
                    assert position == 1, name
                elif case['state'] == 'end':
                    assert position + length == len(raw) - 1, name
                else:
                    assert .40 <= position / len(raw) <= .60, (name, position)
            if name.startswith('moderation/'):
                key = case['size'], case['language']
                moderation.setdefault(key, []).append(case)
                hit = case['state'] != 'absent'
                assert case['searches_per_operation'] == (7 if hit else 12), name
                assert case['expected'] == (6 if hit else -1), name
                assert case['hit_term_index'] == (6 if hit else None), name
                assert compact == (case['size'] != 'short'), name
            if case['api'] == 'strchr':
                assert not case['benchmark'] and case['alias_of'] == 'strstr', name
            sizes.append(len(raw))
            lengths.extend(case['needle_bytes'])
        assert used == set(data['inputs']), suite['name']
        assert suite['control_only'] == all(c['panel'] == 'control' for c in data['cases'])
        rows.append((suite, sizes, lengths))
    assert len(moderation) == 9
    for key, cases in moderation.items():
        assert {c['state'] for c in cases} == {'absent', 'start', 'middle', 'end'}, key
        assert len({tuple(c['needles']) for c in cases}) == 1, key
    return index, rows


def write_index(root, rows):
    text = '''# Frozen application corpus

Status: review candidate; no elapsed-time or counter measurements for these inputs.

Each linked JSON file contains the full UTF-8 input text, the search needles,
their byte lengths and first match positions, the PHP expression and its expected result.
`inputs` stores a text once per suite; cases refer to its key.
Positions use UTF-8 bytes; an absent match is `-1`.

| Suite | Cases | Timed candidates | Input bytes | Needle bytes | Scope |
|---|---:|---:|---:|---:|---|
'''
    for suite, sizes, lengths in rows:
        scope = ('inline control' if max(sizes) < 1024 else 'diagnostic control') if suite['control_only'] else suite['family']
        text += (f"| [{suite['name']}]({suite['file']}) | {suite['cases']} | "
                 f"{suite['benchmark_cases']} | {min(sizes)}–{max(sizes)} | "
                 f"{min(lengths)}–{max(lengths)} | {scope} |\n")
    application = sum(s['benchmark_cases'] for s, _, _ in rows if s['family'] == 'core' and not s['control_only'])
    inline = sum(s['benchmark_cases'] for s, _, _ in rows if s['name'] == 'moderation-short')
    diagnostic = sum(s['benchmark_cases'] for s, _, _ in rows if s['name'].startswith('controls-'))
    optional = sum(s['benchmark_cases'] for s, _, _ in rows if s['family'] != 'core')
    correctness = sum(s['cases'] - s['benchmark_cases'] for s, _, _ in rows)
    text += (f'\nTotal: {sum(s["cases"] for s, _, _ in rows)} cases: '
             f'{application} core application timing candidates, {inline} short inline controls, '
             f'{diagnostic} diagnostic controls, {optional} optional extension candidates '
             f'and {correctness} alias correctness checks.\n')
    text += '''
“Timed candidates” means cases selected for a future benchmark, not completed measurements.
`strchr()` aliases `strstr()` and is checked for correctness without a duplicate timing.
Application needles are 9–31 UTF-8 bytes. Short moderation inputs stay below
1024 bytes and exercise the existing inline path.
`controls-*` are separate synthetic diagnostics, not application benefit rows.
They deliberately include 8-, 32-, 64- and 256-byte needles to check adjacent routes.
`documents-*` preserve complete HTML, MIME messages, JSON log records and
independent posts. They are constructed fixtures, not captured production traffic.
Optional mbstring and intl fixtures require separate builds and runtime validation.

The generator is optional. Review and measure the saved JSON files directly.
To propose changes, generate into a separate directory and inspect the diff first.
Full text and expected string results may make individual JSON lines long.
'''
    (root / 'README.md').write_text(text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('corpus', nargs='?', type=Path, default=ROOT / 'corpus')
    parser.add_argument('--write-index', action='store_true')
    args = parser.parse_args()
    index, rows = audit(args.corpus)
    if args.write_index:
        write_index(args.corpus, rows)
    families = Counter()
    for suite, _, _ in rows:
        families[suite['family']] += suite['cases']
    print(json.dumps(dict(suites=len(rows), cases=sum(families.values()), families=families,
                          status='structural audit passed; no timings')))
