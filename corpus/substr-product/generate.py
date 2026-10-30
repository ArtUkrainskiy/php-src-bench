#!/usr/bin/env python3
"""Deterministic, application-shaped fixtures. No downloaded/private user data."""
from pathlib import Path
import argparse
import hashlib
import json
import random
import subprocess
import urllib.parse

ROOT = Path(__file__).resolve().parent
BENCH = ROOT.parent.parent
BASE = '9d94059ce881d010d91c0ccaa05ee7e987513e3e'
SEED = 20261030


def php(value):
    if isinstance(value, str):
        return "'" + value.replace('\\', '\\\\').replace("'", "\\'") + "'"
    if isinstance(value, list):
        return '[' + ', '.join(php(v) for v in value) + ']'
    if isinstance(value, int):
        return str(value)
    raise TypeError(type(value))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=ROOT / 'generated')
    parser.add_argument('--bench-root', type=Path, default=BENCH)
    parser.add_argument('--php-src', type=Path)
    parser.add_argument('--catalog', type=Path, help='write the owned, input-free suite catalog')
    parser.add_argument('--owned-only', action='store_true',
                        help='omit supplementary public-document snapshots')
    args = parser.parse_args()
    if args.owned_only and args.catalog:
        parser.error('--catalog requires the full corpus, without --owned-only')
    args.php_src = args.php_src or args.bench_root.parent / 'php-src'
    out = args.out
    (out / 'inputs').mkdir(parents=True, exist_ok=True)
    banks = json.loads((ROOT / 'texts.json').read_text())
    rng = random.Random(SEED)
    inputs = {}
    cases = []

    def save(name, value, recipe, source='owned deterministic product fixture'):
        raw = value.encode('utf-8') if isinstance(value, str) else value
        raw.decode('utf-8')
        if name in inputs:
            raise ValueError('Duplicate input ' + name)
        (out / 'inputs' / (name + '.txt')).write_bytes(raw)
        inputs[name] = {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(),
                        'recipe': recipe, 'source': source}
        return raw

    def add(group, name, input_name, operation, arguments, expected, details):
        s = '$s'
        av = ', '.join(php(v) for v in arguments)
        code = {
            'moderate': lambda: f'substr_product_moderate({s}, {av})',
            'contains': lambda: f'str_contains({s}, {av})',
            'strpos': lambda: f'strpos({s}, {av})',
            'explode': lambda: f'explode({php(arguments[0])}, {s}' +
                (f', {arguments[1]}' if len(arguments) > 1 else '') + ')',
            'count': lambda: f'substr_count({s}, {av})',
            'replace': lambda: f'str_replace({php(arguments[0])}, {php(arguments[1])}, {s})',
            'headers': lambda: f'substr_product_headers({s})',
            'query': lambda: f'substr_product_query({s})',
            'records': lambda: f'substr_product_records({s})',
            'slots': lambda: f'substr_product_slots({s})',
            'log_errors': lambda: f'substr_product_log_errors({s})',
            'tokens': lambda: f'substr_product_token_offsets({s}, {av})',
        }[operation]()
        # Expected strings/results are computed in Python, independently of PHP search.
        cases.append({'name': name, 'id': name + ' @ ' + input_name, 'group': group,
                      'input': input_name, 'operation': operation, 'arguments': arguments,
                      'code': code, 'expected': expected, 'details': details})

    def body(language, target):
        messages = banks[language]['messages']
        paragraphs = []
        length = 0
        while length < target:
            message = rng.choice(messages)
            if len(paragraphs) % 3 == 1:
                message += ' #' + str(rng.randrange(10000, 999999))
            paragraphs.append(message)
            length += len(message.encode('utf-8')) + 2
        return '\n\n'.join(paragraphs)

    sizes = {'comment': 256, 'post': 1024, 'thread': 65536}
    for language, bank in banks.items():
        local = bank['terms']
        terms = [local[0], 'promo-cash.example', 'followers-shop.example',
                 'instant-profit.example', 'claim-bonus.example'] + local[1:]
        for size, target in sizes.items():
            clean = body(language, target)
            assert not any(term in clean for term in terms), language
            for state, text in [('clean', clean), ('early', terms[0] + '! ' + clean),
                                ('late', clean + '\n' + terms[-1])]:
                label = f'moderation-{language}-{size}-{state}'
                raw = save(label, text, f'UTF-8 {language}; {size}; {state}; lower-case text prepared before timing')
                positions = [raw.find(term.encode()) for term in terms]
                expected = next((i for i, p in enumerate(positions) if p >= 0), -1)
                assert expected == {'clean': -1, 'early': 0, 'late': len(terms)-1}[state]
                add('moderation', f'banlist12/{language}/{size}/{state}', label,
                    'moderate', [terms], expected,
                    {'language': language, 'size': size, 'state': state, 'terms': len(terms),
                     'normalization': 'already lower-case; literal substring policy, no word boundaries',
                     'first_hit_byte': positions[expected] if expected >= 0 else -1})
                if state == 'clean':
                    add('literal-word', f'banword/{language}/{size}/absent', label,
                        'contains', [terms[0]], False,
                        {'language': language, 'size': size, 'state': 'absent', 'needle_bytes': len(terms[0].encode())})

    values = ['order-104872', 'confirmed', 'blue-cotton-shirt', 'customer@example.test',
              'warehouse-east', 'priority', '12.50', '2026-10-12', 'item-2048', 'standard-delivery',
              'синяя рубашка', 'доставка завтра', '山田', 'заказ подтверждён']
    separators = {'pipe2': '||', 'colon2': '::', 'crlf': '\r\n', 'comma': ',', 'tab': '\t', 'amp': '&'}
    delimiter_sizes = {'short': 128, '4k': 4096, '64k': 65536, '1m': 1048576}
    for kind, separator in separators.items():
        for size, target in delimiter_sizes.items():
            fields = []
            length = 0
            while length < target:
                field = rng.choice(values) + '-' + str(rng.randrange(1000, 99999))
                fields.append(field)
                length += len(field.encode()) + len(separator)
            text = separator.join(fields)
            label = f'delimiter-{kind}-{size}'
            save(label, text, f'varied product fields separated by {kind}; no quoting/escaping; {size}')
            detail = {'separator': kind, 'size': size, 'fields': len(fields),
                      'profile': 'bulk guard' if size == '1m' else 'regular',
                      'mean_field_bytes': sum(len(field.encode()) for field in fields)/len(fields)}
            add('explode', f'explode/{kind}/{size}', label, 'explode', [separator], fields, detail)
            if kind in ['pipe2', 'colon2', 'crlf'] and size != '1m':
                add('split-first', f'explode-limit2/{kind}/{size}', label,
                    'explode', [separator, 2], text.split(separator, 1), detail)
                add('count-delimiter', f'substr-count/{kind}/{size}', label,
                    'count', [separator], text.count(separator), detail)
                add('replace-delimiter', f'str-replace/{kind}/{size}', label,
                    'replace', [separator, ' / '], text.replace(separator, ' / '), detail)
        label = f'delimiter-{kind}-absent'
        text = body('en', 4096).replace(',', ';')
        assert separator not in text
        save(label, text, f'clean natural text with no {kind} separator')
        add('explode', f'explode/{kind}/absent', label, 'explode', [separator], [text],
            {'separator': kind, 'size': '4k', 'state': 'absent'})

    for size, target in [('small', 256), ('4k', 4096), ('64k', 65536)]:
        rows = []
        length = 0
        while length < target:
            row = ['sku-' + str(rng.randrange(10000, 99999)), rng.choice(values),
                   str(rng.randrange(1, 9)), str(rng.randrange(10, 999)), rng.choice(values)]
            line = '||'.join(row)
            rows.append(row)
            length += len(line.encode()) + 2
        label = 'records-' + size
        save(label, '\r\n'.join('||'.join(row) for row in rows), 'unquoted application record export')
        add('parser-records', 'parse-records/' + size, label, 'records', [], rows,
            {'size': size, 'rows': len(rows), 'columns': 5})

        pairs = [('q', 'wireless headphones'), ('sort', 'created_at'), ('page', '2')]
        query_length = len(urllib.parse.urlencode(pairs))
        while query_length < target:
            pair = ('filter[]', rng.choice(['in stock', 'blue', 'size M', 'under 100', 'delivery today']))
            pairs.append(pair)
            query_length += 1 + len(urllib.parse.urlencode([pair]))
        query = urllib.parse.urlencode(pairs)
        label = 'query-' + size
        save(label, query, 'form-urlencoded query with repeated filters; large case is a size guard')
        add('parser-query', 'parse-query/' + size, label, 'query', [], [list(p) for p in pairs],
            {'size': size, 'pairs': len(pairs), 'profile': 'large guard' if size == '64k' else 'regular'})

    request_line = 'GET /api/orders?status=paid HTTP/1.1'
    headers = [('Host', 'shop.example.test'), ('Accept', 'application/json'),
               ('Accept-Language', 'en,ru;q=0.8'), ('User-Agent', 'ProductApp/4.2'),
               ('X-Request-Id', 'req-4820-9012'), ('Authorization', 'Bearer sample-session-token')]
    for size in ['small', 'cookie4k', 'body64k', 'incomplete']:
        hs = list(headers)
        if size == 'cookie4k':
            hs.append(('Cookie', '; '.join(f'pref_{i}=option_{i}' for i in range(230))))
        else:
            hs.append(('Cookie', 'locale=en; theme=light; cart=4281'))
        head = request_line + '\r\n' + '\r\n'.join(k + ': ' + v for k, v in hs)
        request = head if size == 'incomplete' else head + '\r\n\r\n'
        if size == 'body64k':
            request += body('en', 65536)
        label = 'http-' + size
        save(label, request, 'HTTP request; parser stops at header terminator, body excluded from output')
        add('parser-http', 'parse-http/' + size, label, 'headers', [],
            {} if size == 'incomplete' else {k.lower(): v for k, v in hs},
            {'size': size, 'header_bytes': len(head), 'state': 'incomplete' if size == 'incomplete' else 'complete'})
        needle = '\r\n\r\n'
        pos = request.find(needle)
        add('literal-protocol', 'find-http-end/' + size, label, 'strpos', [needle],
            False if pos < 0 else pos, {'size': size, 'needle': 'CRLFCRLF'})

    for size, target in [('small', 512), ('4k', 4096), ('64k', 65536)]:
        blocks = []
        length = 0
        while length < target:
            block = '<section class="order-card"><h2>order {{order.id}}</h2><p>hello {{user.name}}</p>'
            block += '<p>' + rng.choice(banks['en']['messages']) + '</p>'
            block += '<a href="{{tracking.url}}">track delivery</a><footer>{{support.email}}</footer></section>\n'
            blocks.append(block)
            length += len(block)
        template = ''.join(blocks)
        label = 'template-' + size
        save(label, template, 'transactional email/order cards, four named slots per card')
        slots = ['order.id', 'user.name', 'tracking.url', 'support.email'] * len(blocks)
        add('parser-template', 'scan-template/' + size, label, 'slots', [], slots,
            {'size': size, 'slots': len(slots)})
        needles = ['{{order.id}}', '{{user.name}}', '{{tracking.url}}', '{{support.email}}']
        replacements = ['4820', 'anna', 'https://shop.example.test/track/4820', 'help@example.test']
        rendered = template
        for needle, replacement in zip(needles, replacements):
            rendered = rendered.replace(needle, replacement)
        add('render-template', 'render-template/' + size, label, 'replace', [needles, replacements],
            rendered, {'size': size, 'slots': len(slots)})
        for needle in ['href="', 'data-cookieconsent=']:
            add('literal-html', 'html-contains/' + ('link' if needle == 'href="' else 'optional-widget') + '/' + size,
                label, 'contains', [needle], needle in template, {'size': size, 'needle': needle})

    for size, target in sizes.items():
        lines = []
        length = 0
        while length < target:
            event = rng.choice(['payment_created', 'payment_authorized', 'payment_captured', 'payment_refunded'])
            row = {'time': f'2026-10-12T10:{len(lines)%60:02d}:30Z', 'level': 'info', 'event': event,
                   'request_id': f'req-{rng.randrange(100000,999999)}', 'order_id': rng.randrange(1000,9999),
                   'message': 'payment state updated successfully'}
            line = json.dumps(row, separators=(',', ':'))
            lines.append(line)
            length += len(line) + 1
        for state in ['clean', 'early', 'late']:
            current = list(lines)
            error_index = 0 if state == 'early' else len(lines)-1
            if state != 'clean':
                row = json.loads(current[error_index])
                row.update(level='error', event='payment_failed', message='payment authorization declined')
                current[error_index] = json.dumps(row, separators=(',', ':'))
            text = '\n'.join(current)
            label = f'logs-{size}-{state}'
            save(label, text, 'JSON-lines payment lifecycle log; varied identifiers and event names')
            for needle, alias in [('payment_failed', 'event'), ('"level":"error"', 'level')]:
                add('literal-log', f'log-contains/{alias}/{size}/{state}', label,
                    'contains', [needle], needle in text, {'size': size, 'state': state, 'needle': needle})
            if state != 'early':
                add('parser-log', f'log-filter/{size}/{state}', label, 'log_errors', [],
                    [] if state == 'clean' else [error_index], {'size': size, 'state': state, 'lines': len(lines)})

    source = subprocess.check_output(['git', '-C', str(args.php_src), 'show', BASE + ':ext/standard/string.c'])
    for size, target in [('4k', 4096), ('64k', 65536)]:
        text = source[:target].decode('utf-8', 'ignore')
        label = 'source-' + size
        save(label, text, f'first {target} bytes; complete UTF-8 suffix',
             f'php-src {BASE}:ext/standard/string.c; BSD-3-Clause')
        for needle in ['zend_string', 'TODO', 'deprecated_api_call']:
            raw = text.encode()
            nr = needle.encode()
            positions = []
            offset = 0
            while (position := raw.find(nr, offset)) >= 0:
                positions.append(position)
                offset = position + len(nr)
            add('scan-source', f'source-tokens/{needle}/{size}', label, 'tokens', [needle], positions,
                {'size': size, 'needle': needle, 'matches': len(positions)})

    # Existing public snapshots are copied, never re-downloaded during a run.
    for doc in ([] if args.owned_only else ['html-phpnet', 'md-bootstrap', 'js-jquery.min']):
        path = args.bench_root / 'corpus' / 'real' / (doc + '.txt')
        if not path.exists():
            raise FileNotFoundError(f'{path}: run corpus/real/fetch.sh before generating this corpus')
        data = path.read_bytes()
        for size, target in [('4k', 4096), ('64k', 65536)]:
            text = data[:target].decode('utf-8', 'ignore')
            label = f'real-{doc}-{size}'
            save(label, text, f'prefix up to {target} bytes; never repeat/pad a short document',
                 f'existing corpus/real/{doc}.txt; source/license in corpus/real/README.md; source sha256={hashlib.sha256(data).hexdigest()}')
            needles = {'html-phpnet': ['href="', 'data-cookieconsent='],
                       'md-bootstrap': ['```', 'TODO'],
                       'js-jquery.min': ['function', 'sourceMappingURL=']}[doc]
            for needle in needles:
                add('scan-document', f'document/{doc}/{needle}/{size}', label,
                    'contains', [needle], needle in text, {'size': size, 'needle': needle})

    assert len({c['id'] for c in cases}) == len(cases)
    expected_results = {c['id']: c.pop('expected') for c in cases}
    expected_json = json.dumps(expected_results, ensure_ascii=False, separators=(',', ':')) + '\n'
    (out / 'expected.json').write_text(expected_json)
    manifest = {'format': 1, 'seed': SEED, 'description': 'Unweighted application scenarios; no production frequency claim',
                'languages': list(banks), 'inputs': inputs, 'cases': cases,
                'expected_sha256': hashlib.sha256(expected_json.encode()).hexdigest()}
    (out / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    if args.catalog:
        catalog = {'format': 1, 'cases': [{k: c[k] for k in ['name', 'input', 'code']} for c in cases]}
        args.catalog.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'inputs': len(inputs), 'cases': len(cases),
                      'bytes': sum(x['bytes'] for x in inputs.values()),
                      'groups': {g: sum(c['group'] == g for c in cases) for g in sorted({c['group'] for c in cases})}}, indent=2))


if __name__ == '__main__':
    main()
