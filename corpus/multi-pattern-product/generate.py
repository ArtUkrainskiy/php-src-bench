#!/usr/bin/env python3
"""Generate inspectable product jobs and independent byte-based expected results. No timing."""

import argparse
from datetime import datetime, timedelta
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SUITES = {}


def unique(words):
    return list(dict.fromkeys(words))


def occurrences(text, keywords):
    source = text.encode()
    hits = []
    for rank, keyword in enumerate(unique(keywords)):
        needle = keyword.encode()
        offset = 0
        while True:
            offset = source.find(needle, offset)
            if offset < 0:
                break
            hits.append({'offset': offset, 'length': len(needle), 'keyword': keyword, 'rank': rank})
            offset += 1
    return sorted(hits, key=lambda hit: (hit['offset'], hit['length']))


def replace_oracle(text, replacements):
    source = text.encode()
    buckets = {}
    for key, value in replacements.items():
        needle = str(key).encode()
        buckets.setdefault(needle[0], []).append((needle, value.encode()))
    for candidates in buckets.values():
        candidates.sort(key=lambda pair: -len(pair[0]))
    output = bytearray()
    offset = count = consumed = 0
    while offset < len(source):
        for needle, replacement in buckets.get(source[offset], []):
            if source.startswith(needle, offset):
                output.extend(replacement)
                offset += len(needle)
                count += 1
                consumed += len(needle)
                break
        else:
            output.append(source[offset])
            offset += 1
    return output.decode(), count, consumed


def job(identifier, dictionary, *texts):
    return {'id': identifier, 'dictionary': dictionary,
            'documents': [{'id': f'{identifier}-{i + 1}', 'text': text} for i, text in enumerate(texts)]}


def add(suite, identifier, title, operation, description, scope, jobs,
        str_replace=False, synthetic=False, primary=True, constant=False):
    keywords = operation != 'replace'
    methods = {
        'any': ['contains_loop', 'preg_match', 'matcher'],
        'replace': ['strtr', 'preg_replace_callback', 'replacer'],
        'unique': ['strpos_unique', 'preg_each_unique', 'matcher'],
        'count': ['strpos_count', 'preg_each_count', 'matcher'],
        'all': ['strpos_all', 'preg_each_all', 'matcher'],
    }[operation].copy()
    if str_replace:
        methods.append('str_replace')
    if constant:
        methods.append('preg_replace')
    signatures = []
    for item in jobs:
        dictionary = item['dictionary']
        words = dictionary if keywords else list(dictionary)
        assert words and all(isinstance(word, str) and word for word in words)
        assert len(unique(words)) == len(words)
        signatures.append(json.dumps(dictionary, ensure_ascii=False, sort_keys=True))
        if constant:
            values = unique(dictionary.values())
            assert len(values) == 1 and '$' not in values[0] and '\\' not in values[0]
        for document in item['documents']:
            text = document['text']
            hits = occurrences(text, words)
            matched = []
            for hit in hits:
                if hit['keyword'] not in matched:
                    matched.append(hit['keyword'])
            if operation == 'replace':
                output, count, consumed = replace_oracle(text, dictionary)
                expected = {'text': output, 'replacements': count}
                stats = {'selected_matches': count, 'matched_source_bytes': consumed,
                         'output_bytes': len(output.encode())}
            else:
                expected = {'any': bool(hits), 'unique': matched, 'count': len(hits),
                            'all': [{k: hit[k] for k in ['offset', 'length', 'keyword']} for hit in hits]}[operation]
                stats = {}
            document['expected'] = expected
            document['facts'] = {
                'bytes': len(text.encode()), 'occurrences': len(hits),
                'distinct_keywords': len(matched),
                'first_match_offset': hits[0]['offset'] if hits else None,
                'first_matching_dictionary_rank': min((hit['rank'] for hit in hits), default=None),
                **stats,
            }
    values_change = len(set(signatures)) > 1
    modes = [{'id': 'request', 'label': 'Complete request, including dictionary preparation'}]
    if scope != 'one_order':
        modes.append({'id': 'worker', 'label': 'Worker with the same dictionary already prepared'})
    case = {
        'id': identifier, 'title': title, 'kind': 'synthetic' if synthetic else 'product',
        'primary': primary, 'operation': operation, 'description': description,
        'origin': 'Project-authored deterministic workload model; not a production trace.',
        'contract': 'Exact case-sensitive bytes; no word-boundary rules, normalization, or case folding.',
        'lifetime': {'dictionary_scope': scope, 'values_change_between_jobs': values_change,
                     'modes': modes,
                     'pcre_note': 'Pattern keys can remain cached when only replacement values change; report warm and fresh-process compilation separately.'},
        'methods': methods,
        'str_replace_note': ('Longest-first sequential replacement agrees on all saved inputs; this is not a general equivalence.'
                             if str_replace else ('Not applicable to a search operation.' if keywords else
                             'Excluded: no equivalence with this replacement policy is claimed.')),
        'jobs': jobs,
    }
    if scope == 'one_order':
        assert values_change
    else:
        assert not values_change
    SUITES.setdefault(suite, []).append(case)


def moderation():
    seed = json.loads((ROOT / 'moderation-seed.json').read_text())['languages']
    domains = ['unwanted-offer.example.test', 'bulk-followers.example.test',
               'instant-profit.example.test', 'fake-support.example.test']
    wrappers = {
        'en': [lambda t, a, b: t + '. Please review this advertised message. ' + a,
               lambda t, a, b: a + ' The phrase being reported is: ' + t + '. ' + b,
               lambda t, a, b: a + ' I would like to report this advertised phrase: ' + t],
        'ru': [lambda t, a, b: t + '. Пожалуйста, проверьте это рекламное сообщение. ' + a,
               lambda t, a, b: a + ' Мне прислали такую рекламу: ' + t + '. ' + b,
               lambda t, a, b: a + ' Хочу сообщить об этой рекламе: ' + t],
        'zh': [lambda t, a, b: t + '。请查看这条推广内容。' + a,
               lambda t, a, b: a + '我收到的推广内容是：' + t + '。' + b,
               lambda t, a, b: a + '请处理这条推广内容：' + t],
    }
    for language in ['en', 'ru', 'zh']:
        words = seed[language]['terms'] + domains
        messages = seed[language]['messages']
        for state in ['clean', 'start', 'body', 'end']:
            jobs = []
            for i in range(8):
                a, b = messages[i % len(messages)], messages[(i + 3) % len(messages)]
                term = words[(i * 5) % len(words)]
                text = a if state == 'clean' else wrappers[language][['start', 'body', 'end'].index(state)](term, a, b)
                assert bool(occurrences(text, words)) == (state != 'clean')
                jobs.append(job(f'comment-{i + 1}', words, text))
            add('moderation', f'moderation.{language}.{state}',
                f'Flag a short {language.upper()} comment: ' + {'clean': 'no configured phrase', 'start': 'phrase at the start',
                'body': 'phrase inside the message', 'end': 'phrase at the end'}[state],
                'any', 'Literal moderation prefilter with 8 configured terms and 4 fictional domains. '
                'Comments are independent messages, not padding. A quoted phrase may be flagged: this is not semantic spam classification.',
                'community_policy', jobs)


        for state in ['clean', 'reported-phrase']:
            jobs = []
            for i, text in enumerate(seed[language]['posts']):
                term = words[(i * 5) % len(words)]
                if state != 'clean':
                    first, rest = text.split('\n\n', 1)
                    text = wrappers[language][1](term, first, rest)
                assert bool(occurrences(text, words)) == (state != 'clean')
                jobs.append(job(f'detailed-message-{i + 1}', words, text))
            add('moderation', f'moderation.{language}.post-{state}',
                f'Check a detailed {language.upper()} support message: ' + ('no configured phrase' if state == 'clean' else 'a promotional phrase is quoted'),
                'any', 'Three separately authored multi-paragraph return/delivery requests. No repeated filler or target-size padding. '
                'The positive variant quotes a configured phrase within the message.',
                'community_policy', jobs)


ERRORS = ['Fatal error:', 'SQLSTATE[', 'Connection refused', 'TimeoutException',
          'out of memory', 'signature verification failed', 'permission denied', 'upstream unavailable']
EVENTS = [
    ('http.access', 'GET /orders/{n} completed', 'INFO'),
    ('catalog.cache', 'product availability loaded', 'DEBUG'),
    ('payment.authorized', 'payment for order {n} was authorized', 'INFO'),
    ('delivery.updated', 'courier estimate for order {n} was refreshed', 'INFO'),
    ('account.session', 'session for customer {n} was renewed', 'DEBUG'),
    ('mail.queued', 'order {n} confirmation was queued', 'INFO'),
    ('stock.reserved', 'items for order {n} were reserved', 'INFO'),
    ('support.opened', 'support request {n} received an attachment', 'INFO'),
    ('search.completed', 'query returned {n} product results', 'DEBUG'),
    ('worker.finished', 'background job {n} completed', 'INFO'),
    ('upload.accepted', 'image {n} passed validation', 'INFO'),
    ('invoice.created', 'invoice for order {n} was saved', 'INFO'),
]


def logs(batch, count, additions=None):
    additions = additions or {}
    lines = []
    start = datetime(2026, 10, 19, 9, 0, 0) + timedelta(minutes=batch)
    for i in range(count):
        event, message, level = EVENTS[(i * 7 + batch) % len(EVENTS)]
        item = {'time': (start + timedelta(milliseconds=i * 137)).isoformat(timespec='milliseconds') + 'Z',
                'level': level, 'event': event, 'request_id': f'req-{batch:02}-{i:04}',
                'message': message.format(n=1000 + batch * 41 + i),
                'duration_ms': (i * 19 + batch * 7) % 243 + 1}
        if i in additions:
            item.update(additions[i])
        lines.append(json.dumps(item, ensure_ascii=False, separators=(',', ':')))
    return '\n'.join(lines) + '\n'


def error_routing():
    for state, index in [('healthy', None), ('first', 0), ('middle', 8), ('last', 15)]:
        jobs = []
        for i in range(8):
            extra = {} if index is None else {index: {'level': 'ERROR', 'message': ERRORS[i] + ' while processing a queued delivery'}}
            jobs.append(job(f'trace-{i + 1}', ERRORS, logs(i, 16, extra)))
        add('error-routing', 'errors.' + state,
            'Decide whether a request trace needs an alert: ' + ('healthy trace' if index is None else f'error in the {state} record'),
            'any', 'Scan 16 distinct structured log records for eight exact failure markers. No JSON parsing or disk I/O is part of the string operation.',
            'alert_rules', jobs)


ORDER_TEMPLATE = '''<!doctype html>
<html><body><h1>Order {{order.number}} confirmed</h1>
<p>Hello {{customer.name}}, thank you for shopping with {{shop.name}}.</p>
<p>We have reserved your items and will send another message when the parcel leaves the warehouse.</p>
<table><tr><th>Item</th><th>Quantity</th><th>Amount</th></tr>
{{order.items}}</table>
<p>Total paid: <strong>{{order.total}}</strong>. A receipt will be sent to {{customer.email}}.</p>
<p>Your parcel will be delivered to {{delivery.address}}. Current estimate: {{delivery.date}}.</p>
<p>You can check progress at <a href="{{tracking.url}}">your tracking page</a>.</p>
<p>If the address is incorrect, please reply before dispatch. For other questions contact {{support.email}}.</p>
<footer>{{shop.name}} · Thank you for choosing reusable packaging.</footer>
</body></html>'''
ORDER_PLAIN = '''Order {{order.number}} confirmed
Hello {{customer.name}}, your payment of {{order.total}} has been received.
Delivery: {{delivery.address}}
Estimate: {{delivery.date}}
Tracking: {{tracking.url}}
We will email {{customer.email}} after dispatch.
Questions: {{support.email}}
{{shop.name}}'''
CUSTOMERS = [('Maya Chen', 'maya@example.test', '18 Orchard Lane'), ('Alex Rivera', 'alex@example.test', '42 Harbor Road'),
             ('Sam Taylor', 'sam@example.test', '7 Willow Street'), ('Leila Haddad', 'leila@example.test', '29 Market Square'),
             ('Noah Martin', 'noah@example.test', '63 Cedar Avenue'), ('Emma Wilson', 'emma@example.test', '5 Station Road'),
             ('Daniel Kim', 'daniel@example.test', '11 Garden Walk'), ('Sofia Costa', 'sofia@example.test', '32 Bridge Street')]
ITEMS = [('USB-C cable', 2, '$18.00'), ('Desk lamp', 1, '$39.00'), ('Travel adapter', 1, '$24.50'),
         ('Notebook', 3, '$15.00'), ('Water bottle', 1, '$21.00'), ('Laptop sleeve', 1, '$28.00'),
         ('Phone stand', 2, '$16.00'), ('Charging pad', 1, '$32.00')]


def order_emails():
    for pair in [False, True]:
        jobs = []
        for i, (name, email, address) in enumerate(CUSTOMERS):
            item, quantity, total = ITEMS[i]
            mapping = {'{{order.number}}': f'ORD-{4100 + i}', '{{customer.name}}': name,
                       '{{shop.name}}': 'Orchard Supplies', '{{order.items}}': f'<tr><td>{item}</td><td>{quantity}</td><td>{total}</td></tr>',
                       '{{order.total}}': total, '{{customer.email}}': email, '{{delivery.address}}': address,
                       '{{delivery.date}}': f'October {22 + i}, 2026', '{{tracking.url}}': f'https://shop.example.test/track/ORD-{4100 + i}',
                       '{{support.email}}': 'support@example.test'}
            subjects = [ORDER_TEMPLATE] + ([ORDER_PLAIN] if pair else [])
            jobs.append(job(f'order-{4100 + i}', mapping, *subjects))
        add('order-emails', 'order.email-pair' if pair else 'order.email',
            'Render HTML and plain-text confirmation for one order' if pair else 'Render one order confirmation email',
            'replace', 'Ten literal placeholders. Customer, order, item and amount change between jobs. '
            'The prepared replacement map cannot be reused for another order. HTML/plain variants can share one map within an order.',
            'one_order', jobs, str_replace=True)


TENANT = {'{{brand}}': 'Orchard Supplies', '{{support_email}}': 'help@example.test',
          '{{help_url}}': 'https://help.example.test/', '{{company}}': 'Orchard Retail Ltd',
          '{{returns_url}}': 'https://shop.example.test/returns', '{{account_url}}': 'https://shop.example.test/account'}
TENANT_PAGES = [
    '<section><h1>Welcome to {{brand}}</h1><p>Your basket is saved while you browse. Product availability is checked again at checkout.</p><p>Need advice? <a href="{{help_url}}">Visit our help centre</a>.</p></section>',
    '<article><h1>Returns</h1><p>Unused items can be returned in their original packaging. Start your request at {{returns_url}} and include your order number.</p><p>Questions go to {{support_email}}.</p></article>',
    '<aside><h2>Account access</h2><p>Open {{account_url}} to review previous orders and delivery addresses. Password reset links expire after use.</p><p>{{brand}} support: {{support_email}}</p></aside>',
    '<footer><p>Sold by {{company}}. Order history is available in <a href="{{account_url}}">your account</a>.</p><p><a href="{{help_url}}">Help</a> and <a href="{{returns_url}}">returns</a>.</p></footer>',
    'Delivery notice from {{brand}}: we send a tracking link after dispatch. Please keep the packaging until the contents have been checked. Help: {{help_url}}',
    'Your feedback helps {{brand}} improve product instructions. Photos are optional. Do not include payment details in a public review. Contact {{support_email}} for private assistance.',
    '<div class="notice">The current shop operator is {{company}}. For delivery questions use {{support_email}}. Existing orders remain visible at {{account_url}}.</div>',
    'Thank you for choosing {{brand}}. If an item needs to be exchanged, read the instructions at {{returns_url}} before sending the parcel. {{company}}',
]


def tenant_text():
    add('tenant-text', 'tenant.notice', 'Expand fixed tenant labels in one shop notice', 'replace',
        'Six tenant-wide values reused across different notices. No per-customer values are in the map.',
        'tenant_configuration', [job(f'notice-{i + 1}', TENANT, text) for i, text in enumerate(TENANT_PAGES)], str_replace=True)
    add('tenant-text', 'tenant.pages', 'Publish eight different shop pages using one tenant configuration', 'replace',
        'One job is a batch of eight distinct page fragments sharing six tenant values. No paragraph is repeated to reach a target size.',
        'tenant_configuration', [job('page-batch', TENANT, *TENANT_PAGES)], str_replace=True)


PUNCTUATION = {'“': '"', '”': '"', '‘': "'", '’': "'", '–': '-', '—': ' - ', '…': '...', '\u00a0': ' '}
TYPO_TEXT = [
    '“The new charger works well,” Maya wrote. “I’m keeping the old cable as a spare.” The parcel arrived on Tuesday — one day before the estimate.',
    'The product description lists sizes 20–24 cm. Please check the measurement guide before ordering; the colour names in a supplier’s catalogue can differ from ours.',
    'Support replied: “We’ll send the missing clip today.” The replacement part is free — no need to return the complete item.',
    'Delivery costs $5\u00a0per parcel. Orders placed after 16:00 are handled the next business day… the tracking email follows dispatch.',
    'I selected the ‘gift packaging’ option, but I don’t need a printed receipt. Please send the invoice to the email address on my account.',
    'The guide says “connect the blue cable first”. That step was easy — the diagram matches the sockets on the back of the device.',
    'Our supplier’s update changes the model name from “Compact–2” to “Compact 2”. Existing warranty claims are unaffected.',
    'The customer asked, “Can I pick this up on Friday?” We’re checking stock at the pickup point and will confirm the collection time.',
]


def punctuation():
    plain = [text.replace('’', "'").replace('“', '"').replace('”', '"') for text in [
        'The parcel was delivered at 10:35. The customer confirmed that all three items were present.',
        'Please keep this invoice for your records. A copy is available in your account under previous orders.',
        'The new size guide uses centimetres. Measure the outside width before choosing a replacement sleeve.',
        'We moved the pickup date to Friday because the delivery address was changed after checkout.',
    ]]
    add('text-cleanup', 'punctuation.clean', 'Leave ordinary ASCII customer text unchanged', 'replace',
        'Eight typographic literals; the input has no configured character. This models an already-clean imported field.',
        'import_rules', [job(f'plain-{i + 1}', PUNCTUATION, text) for i, text in enumerate(plain)], str_replace=True)
    add('text-cleanup', 'punctuation.mixed', 'Normalize quotes, dashes and spaces in imported customer text', 'replace',
        'Eight exact UTF-8 literals, with only the configured transformations. This is not Unicode normalization.',
        'import_rules', [job(f'text-{i + 1}', PUNCTUATION, text) for i, text in enumerate(TYPO_TEXT)], str_replace=True)
    spaces = {'\u00a0': ' ', '\u202f': ' ', '\u2009': ' ', '\u3000': ' '}
    texts = ['Total: 49\u00a0USD; dispatch within 2\u202fbusiness days.', 'Width 12\u2009cm, height 8\u2009cm. Colour: blue.',
             '配送先：東京都\u3000受取人：山田さん。', 'Invoice amount: 1\u202f250\u00a0EUR. A tax receipt is attached.']
    add('text-cleanup', 'spaces.mixed', 'Replace four special space characters with ordinary spaces', 'replace',
        'Every configured literal has the same replacement. Direct preg_replace is an eligible baseline, without a callback.',
        'import_rules', [job(f'field-{i + 1}', spaces, text) for i, text in enumerate(texts)], str_replace=True, constant=True)


URL_MAP = {
    'http://old.example.test/help/returns': 'https://shop.example.test/returns',
    'http://old.example.test/help': 'https://help.example.test/',
    'http://old.example.test': 'https://shop.example.test',
    'https://cdn-old.example.test/images/': 'https://assets.example.test/img/',
    'https://docs-old.example.test/v1/': 'https://docs.example.test/current/',
    'https://old.example.test/account': 'https://shop.example.test/account',
    'http://old.example.test/search?q=': 'https://shop.example.test/find?query=',
    'https://old.example.test/contact': 'https://help.example.test/contact',
}
URL_PAGES = [
    '<article><h1>Return instructions</h1><p>Please open <a href="http://old.example.test/help/returns">the return form</a> before posting your parcel. Include the order number and keep the postal receipt.</p></article>',
    '<p>For account changes use <a href="https://old.example.test/account">your profile</a>. If the reset email is missing, check the help page at http://old.example.test/help.</p>',
    '<figure><img src="https://cdn-old.example.test/images/cable-front.webp" alt="Cable connector"><figcaption>The connector has a marked top edge.</figcaption></figure>',
    'The integration guide is at https://docs-old.example.test/v1/orders.html. Its examples use a test account and never require a live payment token.',
    '<p>Search the archived catalogue: <a href="http://old.example.test/search?q=desk+lamp">desk lamps</a>. Updated stock appears on the product page.</p>',
    '<p>The receipt footer still points to http://old.example.test. The customer service form is at https://old.example.test/contact.</p>',
    '<p>Packaging photos are stored at https://cdn-old.example.test/images/box-side.jpg. Read http://old.example.test/help/returns if the parcel was damaged.</p>',
    'API documentation: https://docs-old.example.test/v1/refunds.html. Customer accounts remain accessible at https://old.example.test/account.',
]


def link_migration():
    clean = ['<p>The delivery guide is already at https://help.example.test/. Please use the order number when contacting support.</p>',
             '<img src="https://assets.example.test/img/charger.webp" alt="Charging port">']
    for identifier, title, texts in [('clean', 'Check already-migrated content for old literal links', clean),
                                     ('page', 'Rewrite known legacy links in one content page', URL_PAGES)]:
        add('link-migration', 'links.' + identifier, title, 'replace',
            'Eight literal URL rules, including overlapping base/help/returns prefixes. Longest key at the earliest start wins. This is not URL parsing.',
            'migration_rules', [job(f'page-{i + 1}', URL_MAP, text) for i, text in enumerate(texts)], str_replace=True)
    add('link-migration', 'links.batch', 'Migrate eight different content pages with the same URL rules', 'replace',
        'One publishing job updates eight saved pages; the same migration configuration is reused within the job.',
        'migration_rules', [job('publishing-batch', URL_MAP, *URL_PAGES)], str_replace=True)


SERVICES = ['orders', 'payments', 'catalog', 'delivery', 'accounts', 'mail', 'stock', 'support',
            'search', 'exports', 'imports', 'billing', 'reviews', 'images', 'analytics', 'returns',
            'coupons', 'notifications', 'invoices', 'tax', 'warehouse', 'fraud', 'sessions', 'pickup']
SECRETS = {f'fixture_token_{service}_{i + 17:04x}_not_a_real_secret': '[redacted]'
           for i, service in enumerate(SERVICES)}


def secret_redaction():
    keys = list(SECRETS)
    for identifier, count, leaks in [('clean', 32, 0), ('one', 32, 1), ('three', 48, 3), ('incident-batch', 384, 3)]:
        jobs = []
        for i in range(4):
            additions = {}
            for k in range(leaks):
                position = ((k + 1) * count // (leaks + 1) + i) % count
                additions[position] = {'level': 'WARN', 'event': ['debug.header', 'provider.response', 'request.query'][k],
                                       'message': ['upstream request contained authorization data', 'provider echoed a credential',
                                                   'legacy client sent a token in a query'][k],
                                       'debug_value': keys[(i * 7 + k * 5) % len(keys)]}
            jobs.append(job(f'log-sample-{i + 1}', SECRETS, logs(i + 20, count, additions)))
        add('secret-redaction', 'secrets.' + identifier,
            {'clean': 'Mask registered secrets in a log excerpt with no leaked token',
             'one': 'Mask one registered secret in a request log excerpt',
             'three': 'Mask three registered secrets in an incident log excerpt',
             'incident-batch': 'Mask three registered secrets in a larger incident log batch'}[identifier],
            'replace', f'24 fictional registered token values; {count} distinct JSON records per document; '
            f'{leaks} leaked literals. Timestamps, request IDs, events and messages vary. '
            'The method masks only registered exact values, not arbitrary credentials or email addresses.',
            'deployment_secret_registry', jobs, str_replace=True, constant=True)


EMOTICONS = {':))': '😄', ':)': '🙂', ':-)': '🙂', ':(': '🙁', ':-(': '🙁', ';-)': '😉',
             ';)': '😉', ':D': '😃', ':-D': '😃', ':P': '😛', '<3': '❤️', '(^_^)': '😊'}
CHAT = ['Thanks for checking the address :) The courier can leave it with the receptionist.',
        'That fixed the problem :D I can download the invoice now. Thank you!',
        'The colour is perfect <3 I will order the matching cover next week.',
        'I selected the wrong pickup point :( Can it still be changed before dispatch?',
        'Your suggestion worked (^_^) The app remembers my saved filters again.',
        'The gift arrived just in time :)) Please pass my thanks to the packing team.',
        'I kept the tiny instruction card ;-) It has the support address and a QR code.',
        'The replacement clip fits :-) We do not need to return the full stand.']


def chat():
    add('chat-formatting', 'chat.plain', 'Check plain support replies for configured emoticons', 'replace',
        'Twelve literal chat conventions; the ordinary reply has none. No parsing or word-boundary logic is implied.',
        'chat_format_rules', [job(f'reply-{i + 1}', EMOTICONS, text) for i, text in enumerate([
            'Thank you for the update. The delivery address has been corrected.',
            'We have attached a copy of your receipt. Please keep it for your records.',
            'The replacement part will be included in tomorrow\'s dispatch.',
            'Your parcel is ready for collection at the selected pickup point.'])], str_replace=True)
    add('chat-formatting', 'chat.emoticons', 'Render configured emoticons in short customer replies', 'replace',
        'Eight distinct short replies with one literal emoticon each; :)) must take priority over its :) prefix.',
        'chat_format_rules', [job(f'reply-{i + 1}', EMOTICONS, text) for i, text in enumerate(CHAT)], str_replace=True)


TERMS = ['order', 'order number', 'order tracking', 'tracking number', 'delivery', 'delivery address',
         'delivery date', 'shipping', 'shipping address', 'shipping label', 'return', 'return label',
         'return window', 'refund', 'partial refund', 'payment', 'payment method', 'payment failed',
         'invoice', 'invoice number', 'receipt', 'billing', 'billing address', 'discount', 'discount code',
         'gift', 'gift card', 'gift message', 'subscription', 'subscription renewal', 'account',
         'account settings', 'password', 'password reset', 'two-factor authentication', 'verification code',
         'customer', 'customer support', 'support ticket', 'support hours', 'product', 'product page',
         'product variant', 'size guide', 'stock', 'out of stock', 'warranty', 'warranty period',
         'replacement', 'replacement part', 'cancellation', 'cancel order', 'pickup', 'pickup point',
         'courier', 'customs', 'customs charge', 'tax', 'sales tax', 'currency', 'store credit', 'email',
         'email address', 'notification', 'mobile app', 'saved items', 'basket', 'checkout',
         'checkout error', 'browser', 'screen reader', 'accessibility', 'privacy', 'privacy policy',
         'data export', 'data deletion', 'security', 'security key', 'session', 'session expired',
         'attachment', 'file upload', 'photo', 'photo upload', 'delivery instructions', 'warehouse',
         'warehouse delay', 'order status', 'shipping confirmation', 'refund status', 'payment confirmation',
         'business day', 'weekend', 'holiday', 'contact form', 'live chat']
PAGES = [
    'Finding a parcel\n\nUse the order number from your receipt to open order tracking. The tracking number identifies the parcel with the courier, while order status describes our warehouse work. A delivery date is an estimate until the parcel reaches your local depot.\n\nIf the shipping address changed after checkout, contact customer support. Include the old delivery address and the new one in a private support ticket. Do not post an email address in a public review.',
    'Returning one item\n\nA return label can be downloaded from your account. Check the return window before sending the parcel. The shipping label used for the original delivery cannot be reused as a return label.\n\nA partial refund applies when only part of the order is returned. Refund status is updated after the warehouse checks the item. Keep the postal receipt until payment confirmation arrives.',
    'Paying for an order\n\nThe payment method is shown on the invoice. If payment failed, review the billing address and ask your bank whether the transaction was declined. A duplicate authorization is not necessarily a second payment.\n\nA discount code is applied before sales tax. The currency is displayed at checkout. A gift card and store credit can cover part of the balance, with the remaining amount paid by another payment method.',
    'Managing access\n\nUse password reset when you no longer know your password. A verification code confirms a single sign-in attempt. Two-factor authentication can also use a security key, depending on your account settings.\n\nIf a session expired message appears during checkout, sign in again before submitting payment. Review the privacy policy for information about data export and data deletion. Customer support never asks you to post a password in live chat.',
    'Choosing a product\n\nThe product page lists each product variant and its current stock. Use the size guide before adding an item to your basket. An out of stock variant can be added to saved items so you can check it later.\n\nThe warranty period is recorded on the receipt. A replacement part may solve a small fault without replacing the complete product. Include a photo and the invoice number when opening a warranty support ticket.',
    'Collecting a delivery\n\nA pickup point may request the tracking number and proof of identity. The courier sends a notification when the parcel is available. Read the delivery instructions before travelling to collect it.\n\nA warehouse delay can move the delivery date by one business day. A weekend or holiday may affect support hours. For urgent changes use the contact form and include your order number.',
    'Using the mobile site\n\nThe mobile app and browser share your account settings. A screen reader can announce checkout errors and form labels. If a photo upload fails, check the attachment size before trying file upload again.\n\nAccessibility feedback can be sent through the contact form. Do not attach an invoice containing another customer\'s billing address. A support ticket can be reopened if the requested attachment was missing.',
    'Subscriptions and gifts\n\nA subscription renewal produces a new invoice and payment confirmation. You can review the subscription in your account or cancel order dispatch before the displayed cutoff. Cancellation rules are listed in the privacy policy and service terms.\n\nA gift message is printed separately from the receipt. International shipping may require a customs charge. The courier will explain how customs clearance affects the delivery date.',
]


def glossary():
    for operation, title in [('unique', 'List the configured support topics mentioned in a help article'),
                             ('count', 'Count all configured term occurrences in a help article'),
                             ('all', 'Locate all configured term occurrences for a search index')]:
        add('help-index', 'help.' + operation, title, operation,
            'A curated support glossary with nested terms such as order / order number. All substring overlaps count; '
            'a single regex alternation does not enumerate every same-start keyword. The regex baseline searches each literal independently.',
            'glossary_version', [job(f'article-{i + 1}', TERMS, page) for i, page in enumerate(PAGES)], primary=operation == 'unique')
    mapping = {term: '<a href="https://help.example.test/topics/' + term.replace(' ', '-') + '">' + term + '</a>' for term in TERMS}
    add('help-linking', 'help.link-one', 'Link configured support terms in one plain-text help article', 'replace',
        'The fixed glossary is reused across articles. Inserted links contain dictionary terms and must not be searched again; '
        'sequential str_replace is intentionally not equivalent. Input text is owned and HTML escaping is outside this operation.',
        'glossary_version', [job(f'article-{i + 1}', mapping, page) for i, page in enumerate(PAGES)])
    add('help-linking', 'help.link-batch', 'Publish eight different help articles using one link glossary', 'replace',
        'One publishing job applies one fixed term-to-link dictionary to eight distinct articles. '
        'This is exact literal linking, not word-boundary-aware natural-language processing.',
        'glossary_version', [job('article-batch', mapping, *PAGES)])


def controls():
    for orientation in ['prefix', 'suffix']:
        shared = 'same-component-' * 3
        mapping = {(shared + f'{i:04x}' if orientation == 'prefix' else f'{i:04x}' + shared): '[value]' for i in range(64)}
        keys = list(mapping)
        add('synthetic', 'control.' + orientation,
            f'Synthetic control: 64 literals sharing a long {orientation}', 'replace',
            'Dictionary-shape control only; not an application workload. Two selected keys occur in distinct positions.',
            'control', [job('shape', mapping, 'First value: ' + keys[7] + '. This is a saved control input. Last value: ' + keys[51] + '.')],
            synthetic=True, primary=False, constant=True)
    mapping = {'a' * i: 'X' for i in range(1, 17)}
    add('synthetic', 'control.overlaps', 'Synthetic control: nested repeated-byte literals', 'replace',
        'Nested-key control for longest-match selection; intentionally repetitive and excluded from product summaries.',
        'control', [job('overlap', mapping, 'a' * 128 + 'b' + 'a' * 31)], synthetic=True, primary=False, constant=True)
    mapping = {'C++': '$1', 'v1.2': '\\release', '[id]': '~value~', 'a|b': 'kept'}
    add('synthetic', 'control.escaping', 'Correctness control: regex punctuation and literal replacement bytes', 'replace',
        'Escaping check: keys contain regex metacharacters; values contain dollar signs and backslashes. Callback replacement must preserve them literally.',
        'control', [job('escaping', mapping, 'C++ v1.2 [id] a|b; C+ and v1x2 must stay unchanged.')], synthetic=True, primary=False)


def span(low, high):
    return str(low) if low == high else f'{low}–{high}'


def catalogue(entries):
    lines = ['# Complete case inventory', '',
             'Generated from the saved JSON inputs by `generate.py`. No performance results are included.', '',
             'Sizes are UTF-8 bytes per document. Matches are selected non-overlapping replacements for replacement jobs; '
             'for unique-key jobs they count distinct matching keys; for other search jobs they count every occurrence, including nested keywords. '
             'Each range covers all documents in the case. See the JSON `facts` for exact offsets and counts.', '',
             'A request is one saved job. `Documents/request` distinguishes one document from a genuine batch. '
             'The same dictionary may be prepared across requests only where the lifecycle permits it. '
             'Only order-email dictionaries change between jobs.', '']
    for suite in dict.fromkeys(entry['file'] for entry in entries):
        cases = [entry for entry in entries if entry['file'] == suite]
        lines += [f'## [{Path(suite).stem}]({suite})', '',
                  '| Task / case ID | Operation | Keys (key bytes) | Document bytes | Matches | Jobs × documents/request |',
                  '|---|---|---:|---:|---:|---:|']
        for case in cases:
            match_field = {'replace': 'selected', 'unique': 'distinct'}.get(case['operation'], 'occurrences')
            lines.append(f"| {case['title']}<br>`{case['id']}` | {case['operation']} | "
                         f"{span(case['keys_min'], case['keys_max'])} ({span(case['key_bytes_min'], case['key_bytes_max'])}) | "
                         f"{span(case['bytes_min'], case['bytes_max'])} | "
                         f"{span(case[match_field + '_min'], case[match_field + '_max'])} | "
                         f"{case['jobs']} × {case['documents'] // case['jobs']} |")
        lines += ['', 'Dictionary scope: `' + cases[0]['dictionary_scope'] + '`. '
                  + ('Values change per order; prepare a new Replacer for each job.' if cases[0]['dictionary_scope'] == 'one_order'
                     else 'The saved dictionary is identical across jobs; both per-request preparation and worker reuse are eligible.'), '',
                  'Declared methods: ' + ', '.join('`' + method + '`' for method in
                                                   dict.fromkeys(method for case in cases for method in case['methods'])) + '.', '',
                  'Method eligibility and task-specific details are recorded separately for each case in the linked JSON.', '']
    return '\n'.join(lines)


def build():
    moderation()
    error_routing()
    order_emails()
    tenant_text()
    punctuation()
    link_migration()
    secret_redaction()
    chat()
    glossary()
    controls()
    return pack()


def pack():
    files = {}
    entries = []
    for name, cases in SUITES.items():
        value = {'schema': 1, 'suite': name, 'cases': cases}
        text = json.dumps(value, ensure_ascii=False, indent=2) + '\n'
        files[f'suites/{name}.json'] = text
        for case in cases:
            documents = [document for item in case['jobs'] for document in item['documents']]
            dictionary_sizes = [len(item['dictionary']) for item in case['jobs']]
            key_lengths = [len(key.encode()) for item in case['jobs']
                           for key in (list(item['dictionary']) if case['operation'] == 'replace' else item['dictionary'])]
            job_bytes = [sum(document['facts']['bytes'] for document in item['documents']) for item in case['jobs']]
            entries.append({
                'id': case['id'], 'title': case['title'], 'file': f'suites/{name}.json',
                'kind': case['kind'], 'primary': case['primary'], 'operation': case['operation'],
                'dictionary_scope': case['lifetime']['dictionary_scope'], 'jobs': len(case['jobs']),
                'documents': len(documents), 'keys_min': min(dictionary_sizes), 'keys_max': max(dictionary_sizes),
                'key_bytes_min': min(key_lengths), 'key_bytes_max': max(key_lengths),
                'job_bytes_min': min(job_bytes), 'job_bytes_max': max(job_bytes),
                'bytes_min': min(document['facts']['bytes'] for document in documents),
                'bytes_max': max(document['facts']['bytes'] for document in documents),
                'occurrences_min': min(document['facts']['occurrences'] for document in documents),
                'occurrences_max': max(document['facts']['occurrences'] for document in documents),
                'distinct_min': min(document['facts']['distinct_keywords'] for document in documents),
                'distinct_max': max(document['facts']['distinct_keywords'] for document in documents),
                'methods': case['methods'],
                **({'selected_min': min(document['facts']['selected_matches'] for document in documents),
                    'selected_max': max(document['facts']['selected_matches'] for document in documents)}
                   if case['operation'] == 'replace' else {}),
            })
    index = {'schema': 1, 'status': 'Corpus prepared for review; no performance measurements yet.',
             'product_cases': sum(case['kind'] == 'product' for case in entries),
             'synthetic_cases': sum(case['kind'] == 'synthetic' for case in entries),
             'cases': entries, 'suite_sha256': {name: hashlib.sha256(text.encode()).hexdigest() for name, text in files.items()}}
    files['index.json'] = json.dumps(index, ensure_ascii=False, indent=2) + '\n'
    files['CASES.md'] = catalogue(entries)
    return files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    files = build()
    for name, text in files.items():
        path = ROOT / name
        if args.check:
            if not path.exists() or path.read_bytes() != text.encode():
                raise SystemExit('Generated data differs: ' + name)
        else:
            path.write_text(text)
    print(('Corpus regeneration PASS:' if args.check else 'Generated:'),
          sum(len(cases) for cases in SUITES.values()), 'cases in', len(SUITES), 'suites')


if __name__ == '__main__':
    main()
