import random

random.seed(1)

# Realistic nginx/apache-style access log.
paths = ['/', '/index.php', '/api/v2/users/%d', '/api/v2/orders/%d?sort=name',
         '/static/js/app.min.js', '/static/css/main.css', '/images/photo-%d.jpg',
         '/wp-admin/admin-ajax.php', '/vendor/autoload.php', '/favicon.ico',
         '/blog/%d/how-to-do-things', '/search?q=widget&page=%d']
uas = ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0 Safari/537.36',
       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/142.0',
       'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) Mobile/15E148 Safari/604.1',
       'curl/8.9.1', 'python-requests/2.32.3']
codes = [200, 200, 200, 200, 301, 302, 304, 404, 500]
log = []
while sum(len(x) for x in log) < 260000:
    ip = '%d.%d.%d.%d' % (random.randint(1, 223), random.randint(0, 255), random.randint(0, 255), random.randint(1, 254))
    p = random.choice(paths)
    if '%d' in p:
        p = p % random.randint(1, 99999)
    line = '%s - - [28/Oct/2026:%02d:%02d:%02d +0000] "GET %s HTTP/1.1" %d %d "https://example.com/ref" "%s"' % (
        ip, random.randint(0, 23), random.randint(0, 59), random.randint(0, 59), p,
        random.choice(codes), random.randint(120, 80000), random.choice(uas))
    log.append(line)
open('corpus/access.log', 'w').write('\n'.join(log) + '\n')

# Realistic-ish HTML page.
words = 'the quick brown fox jumps over a lazy dog widget service price order user name email'.split()
body = []
while sum(len(x) for x in body) < 240000:
    tag = random.choice(['p', 'div', 'span', 'li', 'h2', 'a'])
    cls = random.choice(['content', 'item', 'nav-link', 'btn btn-primary', 'card', 'text-muted'])
    text = ' '.join(random.choice(words) for _ in range(random.randint(3, 20)))
    if tag == 'a':
        body.append('<a href="/page/%d" class="%s">%s</a>' % (random.randint(1, 999), cls, text))
    else:
        body.append('<%s class="%s">%s</%s>' % (tag, cls, text, tag))
html = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<title>Example Store</title>\n<script src="/static/js/app.min.js"></script>\n'
        '<link rel="stylesheet" href="/static/css/main.css">\n</head>\n<body>\n'
        + '\n'.join(body) + '\n</body>\n</html>\n')
open('corpus/page.html', 'w').write(html)

print('access.log', len(open('corpus/access.log').read()))
print('page.html', len(open('corpus/page.html').read()))
