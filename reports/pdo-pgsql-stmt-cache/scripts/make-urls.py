# URL list of logged-in editors that makes as many distinct SQL texts as possible: every listing takes random
# exposed filters, sorts and deep pages (Drupal writes LIMIT and OFFSET into the SQL text).
#   python3 make-urls.py <count> <seed> > urls.csv
import random
import sys

count, seed = int(sys.argv[1]), int(sys.argv[2])
rnd = random.Random(seed)
NODES, TERMS, USERS = 3000, 200, 121  # site.txt; users: admin, 100 generated, 20 editors
CONTENT_PAGES = 60  # /admin/content shows 50 nodes per page; the front page (/node) 10, so 300 pages
LETTERS = 'abcdefghijklmnoprstuvw'


def word():
    return ''.join(rnd.choice(LETTERS) for _ in range(rnd.randint(2, 5)))


def admin_content():
    q = []
    if rnd.random() < 0.6:
        q.append('title=' + word()[: rnd.randint(1, 3)])
    if rnd.random() < 0.5:
        q.append('type=' + rnd.choice(['article', 'page']))
    if rnd.random() < 0.4:
        q.append('status=' + rnd.choice(['1', '2']))
    if rnd.random() < 0.3:
        q.append('langcode=' + rnd.choice(['en', 'und', 'zxx']))
    q.append('order=' + rnd.choice(['title', 'type', 'name', 'status', 'changed']))
    q.append('sort=' + rnd.choice(['asc', 'desc']))
    q.append(f'page={rnd.randint(0, CONTENT_PAGES - 1)}')
    return '/admin/content?' + '&'.join(q)


def search():
    keys = '+'.join(word() for _ in range(rnd.randint(1, 3)))
    return f'/search/node?keys={keys}&page={rnd.randint(0, 2)}'


MIX = [
    (30, admin_content),
    (15, lambda: f'/node/{rnd.randint(1, NODES)}'),
    (10, lambda: f'/node/{rnd.randint(1, NODES)}/edit'),
    (10, lambda: f'/taxonomy/term/{rnd.randint(1, TERMS)}?page={rnd.randint(0, 3)}'),
    (10, search),
    (10, lambda: f'/node?page={rnd.randint(0, 299)}'),
    (5, lambda: f'/user/{rnd.randint(1, USERS)}'),
    (5, lambda: '/'),
    (5, lambda: '/admin/content'),
]
weights = [w for w, _ in MIX]
print('path')
for _ in range(count):
    print(rnd.choices(MIX, weights)[0][1]())
