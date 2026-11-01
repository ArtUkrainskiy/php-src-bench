#!/usr/bin/env python3
"""Focused application fixtures for the compact Sunday path, without timings."""
import argparse
import hashlib
import json
from pathlib import Path
import random
import sys

sys.dont_write_bytecode = True
from applications import add_application_cases, add_control_cases

ROOT = Path(__file__).resolve().parent
STATES = ['absent', 'start', 'middle', 'end']

def php(value):
    if isinstance(value, str):
        return "'" + value.replace('\\', '\\\\').replace("'", "\\'") + "'"
    if isinstance(value, list):
        return '[' + ', '.join(php(v) for v in value) + ']'
    raise TypeError(value)

def body(messages, size):
    rng = random.Random(25115)
    text = ''
    while len(text.encode()) < size:
        text += rng.choice(messages) + '\n\n'
    raw = text.encode()[:size].decode('utf-8', errors='ignore').encode()
    return (raw + b' ' * (size - len(raw))).decode()

def plant(text, needle, state):
    if state == 'absent':
        return text
    if state == 'start':
        at = 0
    elif state == 'end':
        at = len(text)
    else:
        at = len(text.encode()[:len(text.encode()) // 2].decode('utf-8', errors='ignore'))
        space = text.rfind('\n\n', 0, at)
        if space >= 0 and len(text[space:at].encode()) < min(128, max(8, len(text.encode()) // 25)):
            at = space + 2
    return text[:at] + '\n' + needle + '\n' + text[at:]

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--out', type=Path, default=ROOT.parent / 'corpus')
    p.add_argument('--limit', type=int)
    a = p.parse_args()
    banks = json.loads((ROOT / 'texts.json').read_text())
    assert set(banks) == {'en', 'ru', 'zh'}
    cases, inputs = [], {}
    bases = {lang: body(bank['messages'], 4096) for lang, bank in banks.items()}

    def add(name, api, text, needles, code, expected, panel='api', state=None,
            family='core', setup=None, benchmark=True, extra=None):
        extra = extra or {}
        assert needles and all(1 <= len(n.encode()) <= 256 for n in needles), name
        if panel != 'control':
            assert all(9 <= len(n.encode()) <= 31 for n in needles), name
        raw = text.encode()
        assert len(raw) >= 128
        remaining = len(raw) - extra.get('search_offset_bytes', 0)
        path = ('existing inline control' if remaining < 1024 or max(len(n.encode()) for n in needles) < 9
                else 'wide Sunday control' if min(len(n.encode()) for n in needles) >= 32
                else 'compact Sunday')
        key = name.replace('/', '-')
        inputs[key] = text
        folded = api in ['str_ireplace', 'mb_stripos', 'mb_stristr', 'grapheme_stripos']
        searchable = raw.lower() if folded else raw
        positions = [searchable.find(n.encode().lower() if folded else n.encode()) for n in needles]
        row = dict(name=name, api=api, family=family, panel=panel, state=state,
                   input=key, bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest(),
                   needles=needles, needle_bytes=[len(n.encode()) for n in needles],
                   ascii_folded_fixture=folded,
                   positions=positions, position_unit='UTF-8 bytes', entry_remaining_bytes=remaining,
                   entry_path=path,
                   code=code, expected=expected, benchmark=benchmark,
                   repeated_search_may_enter_inline=api in
                   ['explode', 'substr_count', 'str_replace', 'str_ireplace', 'strtr', 'mb_substr_count'])
        if setup:
            row['setup'] = setup
        row.update(extra)
        cases.append(row)

    for size_name, target in [('short', 256), ('medium', 4096), ('long', 65536)]:
        for lang in ['en', 'ru', 'zh']:
            terms = banks[lang]['terms']
            clean = body(banks[lang]['messages'], target)
            assert len(terms) == 12 and all(9 <= len(n.encode()) <= 31 for n in terms)
            assert not any(n in clean for n in terms)
            hit_index = 6
            for state in STATES:
                text = plant(clean, terms[hit_index], state)
                matches = [i for i, term in enumerate(terms) if term in text]
                assert matches == ([] if state == 'absent' else [hit_index])
                add(f'moderation/{size_name}/{lang}/{state}', 'str_contains', text, terms,
                    f'compact_moderate($s, {php(terms)})',
                    -1 if state == 'absent' else hit_index,
                    panel='control' if size_name == 'short' else 'product', state=state,
                    extra=dict(language=lang, size=size_name,
                               hit_term_index=None if state == 'absent' else hit_index,
                               searches_per_operation=12 if state == 'absent' else hit_index + 1))

    ordinary = bases['en']
    specs = [
        ('strpos', 'order-2026-00142', None),
        ('str_contains', 'your account has been suspended', None),
        ('strstr', 'customer@example.test', None),
        ('strchr', 'customer@example.test', None),
        ('substr_count', '{{tracking.url}}', None),
        ('str_replace', '{{customer.email}}', '[redacted]'),
        ('str_ireplace', '{{customer.email}}', '[redacted]'),
        ('strtr', '{{customer.email}}', '[redacted]'),
        ('explode', '--message-boundary-42', None),
        ('stream_get_line', '--message-boundary-42', None),
    ]
    for api, needle, replacement in specs:
        for state in STATES:
            actual = needle.upper() if api == 'str_ireplace' else needle
            text = plant(ordinary, actual, state)
            raw, n = text.encode(), needle.encode()
            hay = raw.lower() if api == 'str_ireplace' else raw
            pos = hay.find(n)
            setup = None
            if api in ['strpos', 'str_contains', 'strstr', 'strchr', 'substr_count']:
                code = f'{api}($s, {php(needle)})'
                expected = {'strpos': False if pos < 0 else pos,
                            'str_contains': pos >= 0,
                            'strstr': False if pos < 0 else raw[pos:].decode(),
                            'strchr': False if pos < 0 else raw[pos:].decode(),
                            'substr_count': raw.count(n)}[api]
            elif api == 'explode':
                code = f'explode({php(needle)}, $s)'
                expected = [v.decode() for v in raw.split(n)]
            elif api == 'stream_get_line':
                global_key = 'compact_stream_' + str(len(cases))
                setup = f"$GLOBALS['{global_key}'] = fopen('php://memory', 'w+b'); fwrite($GLOBALS['{global_key}'], $s)"
                code = f"compact_read_record($GLOBALS['{global_key}'], strlen($s), {php(needle)})"
                expected = (raw if pos < 0 else raw[:pos]).decode()
            elif api == 'strtr':
                code = f'strtr($s, [{php(needle)} => {php(replacement)}])'
                expected = text.replace(needle, replacement)
            else:
                code = f'{api}({php(needle)}, {php(replacement)}, $s)'
                expected = text if pos < 0 else (raw[:pos] + replacement.encode() + raw[pos+len(n):]).decode()
            add(f'{api}/en/{state}', api, text, [needle], code, expected,
                state=state, setup=setup, benchmark=api != 'strchr',
                extra=dict(language='en', first_hit_byte=pos,
                           alias_of='strstr' if api == 'strchr' else None,
                           ascii_case_fold=api == 'str_ireplace'))

    needle = 'order-2026-00142'
    for state in STATES:
        text = plant(body(banks['en']['messages'], 65536), needle, state)
        pos = text.encode().find(needle.encode())
        add(f'strpos/en/64k/{state}', 'strpos', text, [needle],
            f'strpos($s, {php(needle)})', False if pos < 0 else pos,
            panel='long-text', state=state, extra=dict(language='en', first_hit_byte=pos))

    for api in ['substr_count', 'str_replace', 'str_ireplace', 'strtr', 'explode']:
        needle = '--message-boundary-42' if api == 'explode' else '{{customer.email}}'
        actual = needle.upper() if api == 'str_ireplace' else needle
        text = (ordinary[:180] + '\n' + actual + '\n') * 17 + ordinary[:80]
        if api == 'substr_count':
            code, expected = f'substr_count($s, {php(needle)})', 17
        elif api == 'explode':
            code, expected = f'explode({php(needle)}, $s)', text.split(needle)
        elif api == 'strtr':
            code = f'strtr($s, [{php(needle)} => {php("[redacted]")}])'
            expected = text.replace(actual, '[redacted]')
        else:
            code = f'{api}({php(needle)}, {php("[redacted]")}, $s)'
            expected = text.replace(actual, '[redacted]')
        add(f'{api}/en/repeated', api, text, [needle], code, expected,
            state='repeated', extra=dict(language='en', match_count=17,
                                        ascii_case_fold=api == 'str_ireplace'))

    # Separate extension suites fail clearly when the requested extension is absent.
    for lang in ['en', 'ru', 'zh']:
        for api in ['mb_strpos', 'mb_stripos', 'mb_strstr', 'mb_stristr', 'mb_substr_count']:
            needle = '{{customer.email}}' if api in ['mb_stripos', 'mb_stristr'] else banks[lang]['terms'][1]
            for state in ['absent', 'middle']:
                actual = needle.upper() if api in ['mb_stripos', 'mb_stristr'] else needle
                text = plant(bases[lang], actual, state)
                position = text.lower().find(needle.lower())
                if api in ['mb_strpos', 'mb_stripos']:
                    code, expected = f"{api}($s, {php(needle)}, 0, 'UTF-8')", False if position < 0 else position
                elif api == 'mb_substr_count':
                    code, expected = f"{api}($s, {php(needle)}, 'UTF-8')", text.count(needle)
                else:
                    code = f"{api}($s, {php(needle)}, false, 'UTF-8')"
                    expected = False if position < 0 else text[position:]
                add(f'{api}/{lang}/{state}', api, text, [needle], code, expected,
                    family='mbstring', state=state,
                    extra=dict(language=lang, result_unit=('Unicode codepoint offset' if api in ['mb_strpos', 'mb_stripos'] else 'non-overlapping match count' if api == 'mb_substr_count' else 'UTF-8 substring')))
    for api in ['grapheme_strpos', 'grapheme_stripos', 'grapheme_strstr']:
        needle = 'order-2026-00142'
        for state in STATES:
            actual = needle.upper() if api == 'grapheme_stripos' else needle
            text = plant(ordinary, actual, state)
            pos = text.lower().find(needle)
            expected = (False if pos < 0 else text[pos:]) if api == 'grapheme_strstr' else (False if pos < 0 else pos)
            add(f'{api}/en/{state}', api, text, [needle], f'{api}($s, {php(needle)})',
                expected, family='intl', state=state,
                extra=dict(language='en', ascii_only=True))

    add_application_cases(add, php, plant, banks)
    add_control_cases(add, php, plant, ordinary)

    if a.limit:
        cases = cases[:a.limit]
    output = a.out
    output.mkdir(parents=True, exist_ok=True)
    def group(case):
        if 'suite' in case:
            return case['suite']
        if case['name'].startswith('moderation/'):
            return 'moderation-' + case['size']
        if case['family'] == 'mbstring':
            return 'mbstring'
        if case['family'] == 'intl':
            return 'intl-ascii'
        if case['panel'] == 'long-text':
            return 'search-long'
        if case['api'] in ['strpos', 'str_contains', 'strstr', 'strchr']:
            return 'search'
        if case['api'] in ['str_replace', 'str_ireplace', 'strtr']:
            return 'replace'
        return case['api'].replace('_', '-')
    groups = {}
    for case in cases:
        groups.setdefault(group(case), []).append(case)
    index = dict(format=1, status='corpus candidate; no new timings', suites=[])
    for name, entries in groups.items():
        frozen, names_by_hash = {}, {}
        for case in entries:
            original = case['input']
            digest = case['sha256']
            key = names_by_hash.setdefault(digest, original)
            if key not in frozen:
                frozen[key] = dict(text=inputs[original], bytes=case['bytes'], sha256=digest)
            case['input'] = key
        manifest = dict(format=1, status='corpus candidate; no new timings', suite=name,
                        languages=sorted({c['language'] for c in entries}),
                        needle_range_bytes=[min(n for c in entries for n in c['needle_bytes']),
                                            max(n for c in entries for n in c['needle_bytes'])],
                        inputs=frozen, cases=entries)
        path = output / (name + '.json')
        path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
        index['suites'].append(dict(name=name, file=path.name, family=entries[0]['family'],
            cases=len(entries), benchmark_cases=sum(c['benchmark'] for c in entries),
            inputs=len(frozen), control_only=all(c['panel']=='control' for c in entries),
            sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
    (output / 'index.json').write_text(json.dumps(index, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(dict(cases=len(cases), suites=len(groups),
        core=sum(c['family']=='core' for c in cases),
        mbstring=sum(c['family']=='mbstring' for c in cases),
        intl=sum(c['family']=='intl' for c in cases),
        needle_lengths=sorted({n for c in cases for n in c['needle_bytes']}))))

if __name__ == '__main__':
    main()
