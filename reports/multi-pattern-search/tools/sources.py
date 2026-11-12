#!/usr/bin/env python3
"""Builds the text corpora and natural dictionaries from pinned upstream checkouts.

    python3 tools/sources.py --doc en=<doc-en> --doc es=<doc-es> --doc ru=<doc-ru> --doc zh=<doc-zh> \
        --doc ja=<doc-ja> --mdn <translated-content> --civil <civil_comments test parquet> \
        --crawlers <crawler-user-agents> --browsers <intoli user-agents>

Reading the Civil Comments parquet file needs pyarrow.

Writes corpus/<lang>.txt, corpus/emoji.txt, dictionaries/*.json and corpus/SOURCES.json (revisions,
licences, SHA-256 of every output). Only the outputs are needed to rerun the benchmark.
"""
import argparse
import collections
import hashlib
import html
import json
import random
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAP = 4 * 1024 * 1024
WORD_PATTERNS = {
    'en': r'[A-Za-z]{3,}', 'es': r'[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]{3,}', 'ru': r'[А-Яа-яЁё]{3,}',
    'ko': r'[가-힣]{2,}', 'zh': None, 'ja': None,
}
EMOJI = ['😀', '😂', '🙂', '😉', '🤔', '👍', '👎', '🎉', '🔥', '✅', '❌', '⚠️', '❤️', '🚀', '📦',
         '👩‍💻', '👨‍👩‍👧', '🏳️‍🌈', '🇺🇦', '🇯🇵', '👍🏽', '☕', '🐘', '🧪']


def sha(data):
    return hashlib.sha256(data).hexdigest()


def revision(path):
    out = subprocess.run(['git', '-C', str(path), 'log', '-1', '--format=%H %cs'], capture_output=True, text=True, check=True)
    return out.stdout.split()


def php_manual_text(doc):
    """Plain text of the PHP manual sources: tags, comments and entities removed; files in sorted order."""
    tag, entity, blank = re.compile(r'<[^>]+>'), re.compile(r'&[A-Za-z0-9_.\-]+;'), re.compile(r'\n[ \t]*\n(?:[ \t]*\n)+')
    chunks, total = [], 0
    for path in sorted(doc.joinpath('reference').rglob('*.xml')) + sorted(doc.joinpath('language').rglob('*.xml')):
        text = path.read_text(errors='replace')
        text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
        text = re.sub(r'<!\[CDATA\[(.*?)\]\]>', r'\1', text, flags=re.S)
        text = blank.sub('\n\n', html.unescape(entity.sub('', tag.sub('', text)))).strip()
        if len(text) < 200:
            continue
        data = (text + '\n\n').encode()
        chunks.append(data)
        total += len(data)
        if total >= CAP:
            break
    return b''.join(chunks)


def mdn_text(root):
    """Plain text of MDN Korean pages: front matter, macros and link targets removed."""
    chunks, total = [], 0
    for path in sorted(root.joinpath('files/ko').rglob('*.md')):
        text = path.read_text(errors='replace')
        text = re.sub(r'\A---\n.*?\n---\n', '', text, flags=re.S)
        text = re.sub(r'\{\{.*?\}\}', '', text, flags=re.S)
        text = re.sub(r'\]\([^)]*\)', ']', text)
        text = re.sub(r'\n{3,}', '\n\n', text).strip()
        if len(text) < 200:
            continue
        data = (text + '\n\n').encode()
        chunks.append(data)
        total += len(data)
        if total >= CAP:
            break
    return b''.join(chunks)


def with_emoji(text, seed='emoji'):
    """English text with an emoji sequence after roughly every 40th byte, at word boundaries."""
    rng = random.Random(seed)
    words = text.decode().split(' ')
    out, since = [], 0
    for word in words:
        out.append(word)
        since += len(word) + 1
        if since >= rng.randint(20, 60):
            out.append(rng.choice(EMOJI))
            since = 0
    return ' '.join(out).encode()[:CAP]


def natural_words(text, lang, count=128, skip=1000):
    """`count` tokens of moderate frequency (ranks skip+1 .. skip+count): words, or CJK n-grams of 2-3 characters."""
    decoded = text.decode()
    if WORD_PATTERNS[lang]:
        counts = collections.Counter(re.findall(WORD_PATTERNS[lang], decoded))
    else:
        counts = collections.Counter()
        for run in re.findall(r'[぀-ヿ一-鿿]+', decoded):
            for n in (2, 3):
                counts.update(run[i:i + n] for i in range(len(run) - n + 1))
    ranked = [word for word, _ in sorted(counts.items(), key=lambda item: (-item[1], item[0]))]
    return ranked[skip:skip + count]


def php_identifiers(doc):
    """Function, method and class names from <refname> in the manual, shuffled with a fixed seed."""
    names = set()
    for path in doc.joinpath('reference').rglob('*.xml'):
        names.update(re.findall(r'<refname>\s*([A-Za-z_][A-Za-z0-9_]*(?:::[A-Za-z_][A-Za-z0-9_]*)?)\s*</refname>', path.read_text(errors='replace')))
    ordered = sorted(names)
    random.Random('php-identifiers').shuffle(ordered)
    return ordered


def manual_pages(doc, cap=CAP):
    """One plain-text document per PHP manual reference page, in sorted order."""
    tag, entity, blank = re.compile(r'<[^>]+>'), re.compile(r'&[A-Za-z0-9_.\-]+;'), re.compile(r'\n[ \t]*\n(?:[ \t]*\n)+')
    pages, total = [], 0
    for path in sorted(doc.joinpath('reference').rglob('*.xml')):
        text = re.sub(r'<!--.*?-->', '', path.read_text(errors='replace'), flags=re.S)
        text = re.sub(r'<!\[CDATA\[(.*?)\]\]>', r'\1', text, flags=re.S)
        text = blank.sub('\n\n', html.unescape(entity.sub('', tag.sub('', text)))).strip()
        if len(text) < 200:
            continue
        pages.append(text)
        total += len(text.encode())
        if total >= cap:
            break
    return pages


def comments(parquet, count=10000):
    """The first `count` comments of the Civil Comments test split, in file order."""
    import pyarrow.parquet
    return pyarrow.parquet.read_table(parquet, columns=['text']).column('text').to_pylist()[:count]


def crawler_patterns(root):
    """Patterns of crawler-user-agents that are plain strings once escaped punctuation is unescaped."""
    patterns = []
    for entry in json.loads(root.joinpath('crawler-user-agents.json').read_text()):
        pattern = entry['pattern']
        if re.search(r'(?<!\\)[\[\]()?*+|^$.{}]', re.sub(r'\\[^A-Za-z0-9]', '', pattern)):
            continue
        patterns.append(re.sub(r'\\([^A-Za-z0-9])', r'\1', pattern))
    return list(dict.fromkeys(patterns))


def user_agents(crawlers, browsers, count=10000, bot_share=0.2):
    """Browser User-Agent strings drawn by their observed weight, mixed with crawler examples."""
    import gzip
    rng = random.Random('user-agents')
    seen = json.load(gzip.open(browsers.joinpath('src/user-agents.json.gz'), 'rt'))
    agents = rng.choices([e['userAgent'] for e in seen], weights=[e['weight'] for e in seen], k=int(count * (1 - bot_share)))
    bots = [i for e in json.loads(crawlers.joinpath('crawler-user-agents.json').read_text()) for i in e.get('instances', [])]
    agents += rng.choices(bots, k=count - len(agents))
    rng.shuffle(agents)
    return agents


def php_functions(doc):
    """Function names containing an underscore, from <refname> in the manual, shuffled with a fixed seed."""
    names = set()
    for path in doc.joinpath('reference').rglob('*.xml'):
        names.update(re.findall(r'<refname>\s*([a-z][a-z0-9]*_[a-z0-9_]+)\s*</refname>', path.read_text(errors='replace')))
    ordered = sorted(names)
    random.Random('php-functions').shuffle(ordered)
    return ordered


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--doc', action='append', required=True, help='<lang>=<php doc checkout>')
    parser.add_argument('--mdn', type=Path, required=True)
    parser.add_argument('--civil', type=Path, required=True)
    parser.add_argument('--crawlers', type=Path, required=True)
    parser.add_argument('--browsers', type=Path, required=True)
    args = parser.parse_args()
    docs = {k: Path(v) for k, v in (item.split('=', 1) for item in args.doc)}
    (ROOT / 'corpus').mkdir(exist_ok=True)
    (ROOT / 'dictionaries').mkdir(exist_ok=True)
    sources, outputs = {}, {}
    texts = {lang: php_manual_text(path) for lang, path in docs.items()}
    for lang, path in docs.items():
        used = [f'corpus/{lang}.txt', f'dictionaries/words-{lang}.json']
        if lang == 'en':
            used += ['corpus/emoji.txt', 'corpus/manual-pages.json', 'dictionaries/words-en-frequent.json',
                     'dictionaries/php-identifiers.json', 'dictionaries/php-functions.json']
        sources[f'doc-{lang}'] = {'url': f'https://github.com/php/doc-{lang}', 'revision': revision(path),
                                   'licence': 'CC BY 3.0', 'used_for': ', '.join(used)}
    texts['ko'] = mdn_text(args.mdn)
    sources['mdn-translated-content'] = {'url': 'https://github.com/mdn/translated-content', 'revision': revision(args.mdn),
                                         'licence': 'CC BY-SA 2.5', 'used_for': 'corpus/ko.txt, dictionaries/words-ko.json'}
    texts['emoji'] = with_emoji(texts['en'])
    for lang, data in texts.items():
        path = ROOT / 'corpus' / f'{lang}.txt'
        path.write_bytes(data)
        outputs[str(path.relative_to(ROOT))] = {'bytes': len(data), 'sha256': sha(data),
                                                 'non_ascii_bytes': round(sum(b >= 0x80 for b in data) / len(data), 3)}
    documents = {'manual-pages': manual_pages(docs['en']), 'comments': comments(args.civil),
                 'user-agents': user_agents(args.crawlers, args.browsers)}
    # data/test-00000-of-00001.parquet at this revision; the same file is test/0000.parquet of refs/convert/parquet.
    sources['civil_comments'] = {'url': 'https://huggingface.co/datasets/google/civil_comments',
                                 'revision': ['f2970eb3a55777454c94069077cc8d9b5866312d', '2024-01-25'],
                                 'file': 'data/test-00000-of-00001.parquet',
                                 'sha256': sha(args.civil.read_bytes()), 'licence': 'CC0 1.0', 'used_for': 'corpus/comments.json'}
    sources['crawler-user-agents'] = {'url': 'https://github.com/monperrus/crawler-user-agents', 'revision': revision(args.crawlers),
                                      'licence': 'MIT', 'used_for': 'dictionaries/crawler-patterns.json, corpus/user-agents.json'}
    sources['intoli-user-agents'] = {'url': 'https://github.com/intoli/user-agents', 'revision': revision(args.browsers),
                                     'licence': 'BSD-2-Clause', 'used_for': 'corpus/user-agents.json'}
    sources['ldnoobw'] = {'url': 'https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words',
                          'revision': ['5faf2ba42d7b1c0977169ec3611df25a3c08eb13', None], 'licence': 'CC BY 4.0',
                          'used_for': 'dictionaries/ldnoobw-en.json (copy in dictionaries/ldnoobw)'}
    for name, items in documents.items():
        path = ROOT / 'corpus' / f'{name}.json'
        data = (json.dumps(items, ensure_ascii=False) + '\n').encode()
        path.write_bytes(data)
        outputs[str(path.relative_to(ROOT))] = {'documents': len(items), 'text_bytes': sum(len(t.encode()) for t in items),
                                                 'sha256': sha(data)}
    banwords = ROOT / 'dictionaries/ldnoobw/en'
    dictionaries = {'php-identifiers': php_identifiers(docs['en']), 'php-functions': php_functions(docs['en']),
                    'crawler-patterns': crawler_patterns(args.crawlers),
                    'ldnoobw-en': [line.strip() for line in banwords.read_text().splitlines() if line.strip()]}
    for lang in ['en', 'es', 'ru', 'zh', 'ja', 'ko']:
        dictionaries[f'words-{lang}'] = natural_words(texts[lang], lang)
    dictionaries['words-en-frequent'] = natural_words(texts['en'], 'en', skip=100)
    for name, keys in dictionaries.items():
        path = ROOT / 'dictionaries' / f'{name}.json'
        data = (json.dumps(keys, ensure_ascii=False, indent=0) + '\n').encode()
        path.write_bytes(data)
        outputs[str(path.relative_to(ROOT))] = {'keys': len(keys), 'sha256': sha(data)}
    (ROOT / 'corpus' / 'SOURCES.json').write_text(json.dumps({'sources': sources, 'outputs': outputs}, ensure_ascii=False, indent=1) + '\n')
    for name, value in outputs.items():
        print(name, value)


if __name__ == '__main__':
    main()
