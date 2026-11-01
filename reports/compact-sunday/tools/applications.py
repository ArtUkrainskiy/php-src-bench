"""Construct complete application documents and separate routing/stress controls."""
import html
import json
import random


def document_inputs():
    products = [
        ('USB-C travel charger', '45 W, two ports', '29.90'),
        ('Braided charging cable', '2 m, graphite', '12.50'),
        ('Laptop stand', 'Adjustable aluminium', '34.00'),
        ('Compact keyboard', 'UK layout, wireless', '59.00'),
        ('Notebook refill', 'A5, dotted pages', '6.40'),
        ('Desk organiser', 'Oak finish, three trays', '24.90'),
        ('Insulated bottle', '500 ml, navy', '18.00'),
        ('Protective sleeve', '14 inch, water resistant', '21.00'),
    ]
    items = ''.join(f'<tr><td>{html.escape(name)}</td><td>{detail}</td>'
                    f'<td>1</td><td>GBP {price}</td></tr>\n'
                    for name, detail, price in products)
    receipt = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Your order receipt</title></head>
<body><header><a href="https://shop.example.test/">North Street Supplies</a></header>
<main><h1>Thank you, {{customer.name}}</h1>
<p>We have received order {{order.reference}}. A confirmation will be sent to
{{customer.email}}. Please keep this receipt until your delivery is complete.</p>
<section><h2>Delivery details</h2><address>{{customer.address}}</address>
<p>Telephone: {{customer.phone}}. The courier will contact you before delivery.</p>
<p>Delivery is scheduled for {{delivery.date}}. Follow the parcel at
<a href="{{tracking.url}}">the tracking page</a>.</p></section>
<section><h2>Items</h2><table><thead><tr><th>Product</th><th>Details</th>
<th>Quantity</th><th>Price</th></tr></thead><tbody>
''' + items + '''</tbody></table><p>Delivery: GBP 4.95. VAT is included in the listed prices.</p></section>
<section><h2>Changes and cancellations</h2>
<p>Before dispatch, you can update delivery instructions in your account.
Changes to the delivery address may require a new shipping quote. If an item
has already left the warehouse, contact support before placing a replacement order.</p>
<p>For returns, keep the original accessories and include the order reference.
Refunds are sent to the original payment method after the returned parcel is checked.</p></section>
<footer><p>Questions? Write to {{support.email}} from {{customer.email}},
or use the contact form in your account. Never send card details by email.</p>
<p>North Street Supplies, 18 Market Road. This is an order confirmation,
not a subscription message. Please check your receipt for incorrect quantities.</p></footer>
</main></body></html>'''
    articles = [
        ('Delivery address', 'Open the order details page and choose Edit delivery instructions. '
         'Once a parcel is dispatched, the courier decides whether an address correction is possible.'),
        ('Missing item', 'Compare the contents with the packing list. Some orders arrive in separate '
         'parcels. Send a photograph of the label if the tracking page marks every parcel delivered.'),
        ('Payment pending', 'A pending card authorisation can appear before the final charge. '
         'Check the order status before paying again; your bank may take several days to release a hold.'),
        ('Invoice download', 'Invoices are available from the billing section after dispatch. '
         'Check the company name and tax address before requesting a corrected document.'),
        ('Return collection', 'Choose a collection date when creating the return request. '
         'Pack fragile accessories separately and keep the collection receipt until the refund arrives.'),
        ('Replacement parts', 'Include the model number, a description of the missing part and '
         'a clear photograph. Support will confirm compatibility before sending a replacement.'),
        ('Account access', 'Use the password reset page if you cannot sign in. We will never ask '
         'for your current password, a payment PIN or remote access to your computer.'),
        ('Warranty details', 'Keep the invoice and the serial number. Normal wear and accidental '
         'damage may need a separate assessment; explain when the problem first appeared.'),
    ]
    support = '''<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>Help with your order</title></head><body><header><h1>Customer help</h1></header>
<main><p>Hello {{customer.name}}, this page contains guidance for order {{order.reference}}.</p>
<p>Your contact email is {{customer.email}}. Check {{customer.phone}} and
{{customer.address}} before submitting a delivery enquiry.</p>
''' + '\n'.join(f'<section id="help-{i}"><h2>{title}</h2><p>{text}</p></section>'
                 for i, (title, text) in enumerate(articles)) + '''
<aside><h2>Still need help?</h2><p>Send your question to {{support.email}},
include {{order.reference}}, and tell us which steps you have already tried.
A copy of the response will be sent to {{customer.email}}.</p>
<a href="{{tracking.url}}">Track this order</a></aside></main>
<footer>Help centre · Privacy · Accessibility · Contact preferences</footer></body></html>'''

    def log(records):
        lines = []
        for i in range(records):
            order = 100 + i + (i >= 42)
            entry = dict(time=f'2026-10-28T{8+i//3600:02d}:{i//60%60:02d}:{i%60:02d}Z',
                         level='warning' if i % 19 == 0 else 'info',
                         request_id=f'req-{i+73000:08d}', method='GET' if i % 3 else 'POST',
                         path=['/account/orders', '/api/checkout', '/support/tickets'][i % 3],
                         order_id=f'order-2026-{order:05d}', status=202 if i % 7 == 0 else 200,
                         duration_ms=3 + (i * 17) % 83,
                         message=['Order status loaded', 'Payment confirmation queued',
                                  'Delivery preferences saved', 'Invoice download requested'][i % 4])
            lines.append(json.dumps(entry, ensure_ascii=False, separators=(',', ':')))
        return '\n'.join(lines) + '\n'

    boundary = 'message-boundary-42'
    def mail(subject, content, attachment):
        parts = ['Content-Type: text/plain; charset=UTF-8\r\n\r\n' + content,
                 'Content-Type: text/html; charset=UTF-8\r\n\r\n' + receipt]
        if attachment:
            parts.append('Content-Type: application/json\r\n'
                         'Content-Disposition: attachment; filename="delivery.json"\r\n\r\n' +
                         json.dumps(dict(order='order-2026-00142', items=products, status='dispatched'), indent=2))
        parts = [part.replace('\r\n', '\n').replace('\n', '\r\n') for part in parts]
        return ('From: orders@example.test\r\nTo: customer@example.test\r\n'
                f'Subject: {subject}\r\nMIME-Version: 1.0\r\n'
                f'Content-Type: multipart/mixed; boundary="{boundary}"\r\n\r\n' +
                ''.join(f'--{boundary}\r\n{part}\r\n' for part in parts) +
                f'--{boundary}--\r\n')

    return dict(receipt=receipt, support=support, log_short=log(20), log_long=log(320),
                mail_receipt=mail('Your order receipt', 'Your payment has been received.\r\n'
                                  'Please check the item list and keep the receipt for your records.', False),
                mail_delivery=mail('Delivery documents', 'Your parcel is ready for collection.\r\n'
                                   'The attached document lists the items and delivery status.', True)), articles


def add_application_cases(add, php, plant, banks):
    documents, articles = document_inputs()

    posts = {
        'en': '\n\n'.join(title + '\n' + text for title, text in articles),
        'ru': '''Хочу описать, как прошёл наш переезд и обустройство рабочего места.
Мы заранее составили список вещей, которые понадобятся в первую неделю: лампа,
удлинитель, подставка для ноутбука и несколько коробок для документов. Часть заказа
привезли в субботу, а оставшиеся позиции приехали отдельной посылкой в понедельник.

Сборка стола оказалась проще, чем мы ожидали. В инструкции хорошо показаны крепления,
но рисунок последнего шага слишком мелкий. Пришлось открыть электронную версию на
планшете. Один винт остался запасным; сначала мы решили, что пропустили деталь,
а потом нашли пояснение в конце списка комплектации.

Теперь ноутбук стоит на уровне глаз, клавиатура лежит отдельно, а провода убраны
под стол. На видеозвонках стало удобнее смотреть в камеру. Лампу поставили слева,
чтобы свет не отражался в экране. Вечером яркости хватает даже на минимальном режиме.

Из замечаний: поверхность подставки быстро собирает отпечатки, а у кабеля довольно
жёсткая оплётка. Это не мешает работе, но для поездок я выбрал бы вариант помягче.
Упаковку пока сохранили на случай обмена. Через месяц дополню отзыв и расскажу,
не разболтались ли шарниры и как покрытие переносит обычную уборку.''',
        'zh': '''周末我们终于整理好了家里的小书房，想记录一下这次布置的过程。
房间不大，原来的桌子靠着窗户，下午使用电脑时屏幕反光很明显。
我们先量了墙面的宽度和插座的位置，再决定把书桌转到另一边。

这次买了台灯、笔记本支架、收纳盒和一条较长的电源线。
包裹分两天送到，每个箱子里都有单独的装箱清单。
安装支架时，说明书最后一张图有点小，我们用手机放大后才看清楚。
多出来的一颗螺丝是备用件，配件表里有注明。

桌面整理之后，开会时摄像头的位置自然多了，也不用一直低头看屏幕。
台灯放在左边，晚上阅读纸质资料时没有明显的阴影。
收纳盒主要放充电器和转接头，常用的东西终于不用到处找了。

目前发现的缺点是支架表面容易留下指纹，电源线比想象中硬一些。
如果经常带着出门，可能需要更轻便的款式。
我们打算先用一个月，再看看转轴是否松动，以及桌面清洁起来是否方便。
这篇记录只代表目前的使用情况，后面有新发现会继续补充。''',
    }
    for lang, clean in posts.items():
        terms = banks[lang]['terms']
        assert len(clean.encode()) >= 1024 and not any(n in clean for n in terms)
        for state in ['absent', 'middle']:
            text = plant(clean, terms[6], state)
            add(f'documents/moderation/{lang}/{state}', 'str_contains', text, terms,
                f'compact_moderate($s, {php(terms)})', -1 if state == 'absent' else 6,
                panel='product', state=state,
                extra=dict(suite='documents-moderation', language=lang,
                           hit_term_index=None if state == 'absent' else 6,
                           searches_per_operation=12 if state == 'absent' else 7,
                           fixture_kind='independent constructed post; no repeated padding'))

    def app(name, api, text, needles, code, expected, suite, state='document', **metadata):
        add(name, api, text, needles, code, expected, panel='product', state=state,
            extra=dict(suite=suite, language='en', fixture_kind='constructed complete document', **metadata))

    for key in ['receipt', 'support', 'log_short', 'log_long']:
        needle = 'order-2026-00142' if key.startswith('log') else '{{customer.email}}'
        for state in ['absent', 'present']:
            text = documents[key]
            if key.startswith('log'):
                if state == 'present':
                    records = [json.loads(line) for line in text.splitlines()]
                    records[len(records)//2]['order_id'] = needle
                    text = '\n'.join(json.dumps(r, separators=(',', ':')) for r in records) + '\n'
            elif state == 'absent':
                text = text.replace(needle, '{{customer.phone}}')
            position = text.find(needle)
            app(f'documents/search/{key}/{state}', 'strpos', text, [needle],
                f'strpos($s, {php(needle)})', False if position < 0 else position,
                'documents-search', state='absent' if state == 'absent' else 'document',
                document=key, similar_prefixes=True)

    replacements = dict(shorter='[redacted]', equal='reader@example.org',
                        longer='confirmed-customer@example.test')
    needle = '{{customer.email}}'
    assert len(replacements['equal']) == len(needle)
    for key in ['receipt', 'support']:
        for mode, replacement in replacements.items():
            text = documents[key]
            app(f'documents/replace/{key}/{mode}', 'str_replace', text, [needle],
                f'str_replace({php(needle)}, {php(replacement)}, $s)', text.replace(needle, replacement),
                'documents-replace', document=key, replacement_kind=mode,
                replacement_bytes=len(replacement), match_count=text.count(needle))
        terms = [needle, '{{order.reference}}', '{{tracking.url}}']
        values = ['reader@example.org', 'order-2026-00142', 'https://tracking.example.test/parcel/42']
        expected = documents[key]
        for term, value in zip(terms, values):
            expected = expected.replace(term, value)
        app(f'documents/replace/{key}/array', 'str_replace', documents[key], terms,
            f'str_replace({php(terms)}, {php(values)}, $s)', expected, 'documents-replace',
            document=key, replacement_kind='three sequential search/replacement pairs')
        app(f'documents/count/{key}', 'substr_count', documents[key], [needle],
            f'substr_count($s, {php(needle)})', documents[key].count(needle),
            'documents-count', document=key, match_count=documents[key].count(needle))
    for mode, replacement in replacements.items():
        text = documents['receipt'].replace(needle, '{{CUSTOMER.EMAIL}}', 1)
        expected = text.replace('{{CUSTOMER.EMAIL}}', replacement).replace(needle, replacement)
        app(f'documents/ireplace/receipt/{mode}', 'str_ireplace', text, [needle],
            f'str_ireplace({php(needle)}, {php(replacement)}, $s)', expected, 'documents-replace',
            document='receipt', replacement_kind=mode, replacement_bytes=len(replacement),
            mixed_case=True)

    delimiter = '--message-boundary-42'
    for key in ['mail_receipt', 'mail_delivery']:
        text = documents[key]
        for limit in [None, 2]:
            code = f'explode({php(delimiter)}, $s' + (', 2)' if limit else ')')
            app(f'documents/explode/{key}/' + ('limit2' if limit else 'all'), 'explode', text,
                [delimiter], code, text.split(delimiter, 1) if limit else text.split(delimiter),
                'documents-mail', document=key, split_limit=limit)
        closing = delimiter + '--'
        global_key = 'compact_' + key
        setup = f"$GLOBALS['{global_key}'] = fopen('php://memory', 'w+b'); fwrite($GLOBALS['{global_key}'], $s)"
        add(f'documents/stream/{key}/closing', 'stream_get_line', text, [closing],
            f"compact_read_record($GLOBALS['{global_key}'], strlen($s), {php(closing)})",
            text[:text.index(closing)], panel='product', state='document', setup=setup,
            extra=dict(suite='documents-mail', language='en', document=key,
                       fixture_kind='constructed complete MIME message'))

    # Unequal section sizes and deterministic irregular match positions.
    for count in [3, 23]:
        chosen = set(random.Random(25115 + count).sample(range(48), count))
        sections = []
        marker = '<!-- record-break -->'
        for i in range(48):
            title, content = articles[(i * 5) % len(articles)]
            detail = ' Please include the courier reference and the collection date.' if i % 3 else ''
            contact = needle if i in chosen else '{{customer.phone}}'
            sections.append(f'<section id="ticket-{700+i}"><h2>{title}: request {700+i}</h2>'
                            f'<p>{content}{detail}</p><p>Reply to {contact}.</p></section>' +
                            (marker if i in chosen else ''))
        text = '<!doctype html><html lang="en"><body>' + '\n'.join(sections) + '</body></html>'
        for api in ['substr_count', 'str_replace', 'explode']:
            n = marker if api == 'explode' else needle
            code = (f'substr_count($s, {php(n)})' if api == 'substr_count' else
                    f'str_replace({php(n)}, {php("[redacted]")}, $s)' if api == 'str_replace' else
                    f'explode({php(n)}, $s)')
            expected = count if api == 'substr_count' else text.replace(n, '[redacted]') if api == 'str_replace' else text.split(n)
            app(f'documents/repeated/{api}/{count}', api, text, [n], code, expected,
                'documents-repeated', state='repeated', match_count=count,
                spacing='irregular; different section lengths', document=f'help-export-{count}')


def add_control_cases(add, php, plant, ordinary):
    def search(name, length, size, state, suite, prefix=False, offset=0):
        needle = ('a' * (length - 1) + 'b') if prefix else 'invoice-order-reference-2026-status-code'[:length]
        if len(needle) < length:
            needle += 'Z' * (length - len(needle))
        text = ('a' * size) if prefix else (ordinary * (size // len(ordinary) + 1))[:size]
        if state == 'origin':
            text = text[:offset] + needle + text[offset+len(needle):]
        elif state in ['middle', 'end']:
            at = size // 2 if state == 'middle' else size - len(needle) - 1
            text = text[:at] + needle + text[at+len(needle):]
        position = text.find(needle, offset)
        add(name, 'strpos', text, [needle], f'strpos($s, {php(needle)}, {offset})',
            False if position < 0 else position, panel='control', state=state,
            extra=dict(suite=suite, language='en', search_offset_bytes=offset,
                       fixture_kind='synthetic diagnostic; not application benefit'))

    for length in [9, 16, 24, 31]:
        for state in ['absent', 'origin', 'middle', 'end']:
            search(f'controls/length-{length}/{state}', length, 4096, state, 'controls-lengths')
    for size in [1023, 1024, 1025]:
        for state in ['absent', 'origin']:
            search(f'controls/haystack-{size}/{state}', 16, size, state, 'controls-routing')
    for length in [8, 9, 31, 32]:
        for state in ['absent', 'origin']:
            search(f'controls/needle-{length}/{state}', length, 4096, state, 'controls-routing')
    for length in [64, 256]:
        search(f'controls/needle-{length}/absent', length, 4096, 'absent', 'controls-routing')
    for remaining in [1023, 1024]:
        search(f'controls/remaining-{remaining}/absent', 16, 3072, 'absent',
               'controls-routing', offset=3072-remaining)
    for length in [9, 16, 31, 64]:
        search(f'controls/prefix-{length}/absent', length, 4096, 'absent', 'controls-prefix', prefix=True)

    needle = '--message-boundary-42'
    at = 8192 - len(needle)//2
    text = (ordinary * 3)[:at] + needle + ordinary
    setup = "$GLOBALS['compact_buffer_seam'] = fopen('php://memory', 'w+b'); fwrite($GLOBALS['compact_buffer_seam'], $s)"
    add('controls/stream/buffer-seam', 'stream_get_line', text, [needle],
        f"compact_read_record($GLOBALS['compact_buffer_seam'], strlen($s), {php(needle)})",
        text[:at], panel='control', state='document', setup=setup,
        extra=dict(suite='controls-routing', language='en', boundary_byte=8192,
                   fixture_kind='delimiter across default stream chunk boundary'))
