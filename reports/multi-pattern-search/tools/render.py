#!/usr/bin/env python3
"""Renders the report pages from data/results.json, data/pages.json, data/construct.jsonl and the cell files.

    python3 tools/render.py

Every *.md.in template is written to *.md with {{NAME}} placeholders filled by this script.
Every table and most measured values in the text come from the data. The templates also state a few
fixed facts of the setup (sizes, sources, the 3% noise floor).
"""
import json
import math
import re
import statistics as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from summarize import AA_LIMIT, SPREAD_LIMIT, universal  # noqa: E402
from cells import PAGE_SIZES  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
COMPILERS = [('gcc15', 'GCC 15.2'), ('clang21', 'Clang 21.1')]
MODES = [('prepared', 'Prepared'), ('oneshot', 'One-shot')]
OPS = {'any': '`matches()`', 'unique': '`getMatchedKeywords()`', 'count': '`countMatches()`',
       'all': '`matchAll()`', 'replace': '`replace()`'}
EXISTING = {'any': 'Does any key occur?', 'unique': 'Which keys occur?', 'count': 'How many occurrences?',
            'all': 'Every occurrence with its offset', 'replace': 'Replace every occurrence'}
METHODS = {
    'folded_strpos_loop': '`strtolower()` + `str_contains()` loop',
    'contains_loop': '`str_contains()` loop', 'substring_count_loop': '`substr_count()` loop',
    'single_contains': '`str_contains()`', 'single_unique': '`str_contains()`',
    'strtr': '`strtr()`', 'pcre_longest': 'PCRE, longest first', 'pcre_prefix': 'PCRE, shared prefixes',
    'pcre_literal': 'PCRE alternation', 'pcre_prefix_constant': '`preg_replace()`, shared prefixes',
}
LENGTHS = [128, 1024, 4096, 16384, 65536]
CONTROLLED_N = [8, 16, 32, 128, 1024]
NATURAL_N = [8, 32, 128, 512, 2048]
NATURAL_LENGTHS = [128, 1024, 4096, 65536]
PLACEMENTS = {'one': 'one occurrence in the middle third', 'spread16': '16 occurrences across the text',
              'absent': 'no occurrence', 'start': 'one occurrence in the first 64 bytes',
              'end': 'one occurrence in the last 64 bytes'}
LANGUAGES = {'en': 'English', 'es': 'Spanish', 'ru': 'Russian', 'zh': 'Chinese', 'ja': 'Japanese', 'ko': 'Korean',
             'emoji': 'English with emoji'}
# Marks in tables: spread between processes above MARK_SPREAD %, or A/A above MARK_AA %.
MARK_SPREAD, MARK_AA = 5.0, 3.0


def method_name(method, cell):
    """Label of an existing method; strpos_loop runs str_contains(), strpos() or stripos() by operation."""
    base = re.sub(r'_(512|1024)$', '', method)
    chunk = re.search(r'_(512|1024)$', method)
    if base == 'strpos_loop':
        caseless = cell.get('policy') == 'ascii-insensitive'
        function = 'stripos' if caseless else ('str_contains' if cell['op'] in ('any', 'unique') else 'strpos')
        name = f'`{function}()` loop'
    else:
        name = METHODS.get(base, method)
    return name + (f' in chunks of {chunk.group(1)}' if chunk else '')


def size(n):
    return f'{n // 1024} KiB' if n >= 1024 and n % 1024 == 0 else f'{n} B'


def num(value):
    """Signed change: whole percent from 10 up, one decimal below."""
    text = f'{value:+.0f}' if abs(value) >= 9.95 else f'{value:+.1f}'
    return text.replace('-', '−')


def micro(value):
    if value >= 1000:
        return f'{value:,.0f}'
    return f'{value:.3g}' if value >= 1 else f'{value:.2f}'


def table(head, rows, numeric_from=1):
    align = ['---'] * numeric_from + ['---:'] * (len(head) - numeric_from)
    lines = ['| ' + ' | '.join(head) + ' |', '|' + '|'.join(align) + '|']
    lines += ['| ' + ' | '.join(str(v) for v in row) + ' |' for row in rows]
    return '\n'.join(lines)


class Data:
    def __init__(self):
        records = json.loads((ROOT / 'data/results.json').read_text())
        self.results = {(r['cell'], r['compiler'], r['mode']): r for r in records}
        # The page-length series ran separately; it is kept apart so it doesn't enter the run-wide statistics.
        pages = json.loads((ROOT / 'data/pages.json').read_text())
        self.pages = {(r['cell'], r['compiler'], r['mode']): r for r in pages}
        self.cells = {}
        for path in (ROOT / 'cells').glob('*/*.json'):
            self.cells[f'{path.parent.name}/{path.stem}'] = json.loads(path.read_text())
        self.construct = []
        path = ROOT / 'data/construct.jsonl'
        if path.exists():
            self.construct = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
        self.sources = json.loads((ROOT / 'corpus/SOURCES.json').read_text())

    def get(self, cell, compiler, mode):
        """A record of the main series or, failing that, of the page-length series. Run-wide statistics
        iterate self.results directly."""
        key = (cell, compiler, mode)
        return self.results.get(key) or self.pages.get(key)

    def marked(self, r):
        return r['spread_percent'] > MARK_SPREAD or abs(r['aa_max_percent']) > MARK_AA or bool({'preempted', 'load'} & set(r['flags']))

    def change(self, cell, compiler, mode, unit='%'):
        r = self.get(cell, compiler, mode)
        if r is None:
            return '—'
        return num(r['change_percent']) + unit + ('†' if self.marked(r) else '')

    def pair(self, cell, mode):
        """'GCC / Clang' change, as used in the grid tables."""
        if self.get(cell, 'gcc15', mode) is None:
            return ''
        return f"{self.change(cell, 'gcc15', mode)} / {self.change(cell, 'clang21', mode)}"

    def changes(self, cells, modes=('prepared', 'oneshot'), compilers=('gcc15', 'clang21')):
        return [r['change_percent'] for c in cells for m in modes for cc in compilers
                if (r := self.get(c, cc, m)) is not None]

    def span(self, cells, modes, compilers=('gcc15', 'clang21')):
        values = self.changes(cells, modes, compilers)
        lo, hi = min(values), max(values)
        return f'{num(lo)}%' if round(lo) == round(hi) else f'{num(lo)}…{num(hi)}%'


MARK_TEXT = (f'† = the processes disagree by more than {MARK_SPREAD:.0f}%, the A/A control is off by more than '
             f'{MARK_AA:.0f}%, a process was preempted more than 20 times a second, or the core was not idle; '
             'the values are in [data/results.json](data/results.json).')
SCALE = 'Negative = the new class is faster: −50% is twice as fast, −75% four times, −90% ten times. +100% is twice as slow.'
LEGEND = ('**How to read the tables.** "Change" columns: how much the time per call of `Str\\Matcher` or `Str\\Replacer` '
          'differs from the fastest existing method for the same input and mode, in percent. ' + SCALE + ' ' + MARK_TEXT)
GRID_LEGEND = ('**How to read a cell.** `−80% / −75%` is the change in time per call against the fastest existing method: '
               '−80% with GCC 15.2, −75% with Clang 21.1. ' + SCALE + ' '
               + MARK_TEXT.replace('(data/results.json)', '({root}data/results.json)')
               + ' The same file has the times in µs and the existing method that was fastest.')


SCENARIOS = [
    ('Moderation: does a comment contain a listed word?', 'scenarios/moderation.any'),
    ('Moderation: which listed words occur?', 'scenarios/moderation.unique'),
    ('Bot detection: is this User-Agent a crawler?', 'scenarios/bots.any'),
    ('Bot detection: which crawler patterns match?', 'scenarios/bots.unique'),
    ('Auto-linking, all pages, 3,345 names: link them', 'scenarios/autolink.replace'),
    ('Auto-linking, all pages, 3,345 names: every name with its offset', 'scenarios/autolink.all'),
    ('Auto-linking, all pages, 3,345 names: which names occur?', 'scenarios/autolink.unique'),
]


PAGE_SCENARIOS = [
    ('Auto-linking, 4–16 KiB pages, 128 names: link them', 'pages/autolink.replace.n128.p4096'),
    ('Auto-linking, 4–16 KiB pages, 128 names: every name with its offset', 'pages/autolink.all.n128.p4096'),
    ('Auto-linking, 4–16 KiB pages, 512 names: link them', 'pages/autolink.replace.n512.p4096'),
    ('Auto-linking, 4–16 KiB pages, 512 names: every name with its offset', 'pages/autolink.all.n512.p4096'),
]


def repay_calls(data, cell, compiler):
    """Calls on one object after which the build is repaid: 1 when a single call is already faster.
    Otherwise build / (existing prepared time - native prepared time), rounded up, where build = one-shot
    minus prepared time of the new class; the existing method's own one-time work counts as zero."""
    prepared, oneshot = data.get(cell, compiler, 'prepared'), data.get(cell, compiler, 'oneshot')
    if oneshot['ratio'] < 1:
        return '1'
    build = oneshot['native_us'] - prepared['native_us']
    gain = prepared['reference_us'] - prepared['native_us']
    return f'{math.ceil(build / gain)}' if gain > 0 else 'never'


def scenario_table(data):
    """Every scenario task in both modes: GCC times of the fastest existing method and the new class,
    the change 'GCC / Clang', and the calls that repay the build 'GCC / Clang'."""
    rows = []
    for label, cell in SCENARIOS + PAGE_SCENARIOS:
        row = [f"{label} {OPS[data.cells[cell]['op']]}"]
        for mode, _ in MODES:
            r = data.get(cell, 'gcc15', mode)
            row += [f"{micro(r['reference_us'])} / {micro(r['native_us'])}", data.pair(cell, mode)]
        row.append(' / '.join(repay_calls(data, cell, cc) for cc, _ in COMPILERS))
        rows.append(row)
    return table(['Task', 'Prepared, µs: existing / new', 'Prepared change', 'One-shot, µs: existing / new',
                  'One-shot change', 'Calls to repay the build, GCC / Clang'], rows)


def scenario_inputs(data):
    out = []
    for name, cell in [('Moderation', 'scenarios/moderation.any'), ('Bot detection', 'scenarios/bots.any'),
                       ('Auto-linking', 'scenarios/autolink.replace')]:
        c = data.cells[cell]
        keys = len(c['keys'] if 'keys' in c else c['mapping'])
        texts, hits = len(c['pool']['indices']), c['pool']['occurrences']['texts_with_matches']
        out.append([name, f'{texts:,}', size(c['pool']['bytes']['median']), f'{keys:,}', f'{100 * hits / texts:.1f}%',
                    f"{c['pool']['occurrences']['max']}"])
    return table(['Scenario', 'Texts', 'Median text', 'Keys', 'Texts with a match', 'Most matches in a text'], out, 1)


def distinct_documents(cell):
    pool = cell['pool']
    return len(set(json.loads((ROOT / pool['documents']).read_text())))


PAGE_NAMES = [128, 512, 3345]


def page_label(low, high):
    return f'{low // 1024}–{high // 1024} KiB'


def page_cell(op, n, low):
    return f'pages/autolink.{op}.n{n}.p{low}'


def page_change(data, cell, mode='oneshot'):
    out = []
    for cc, _ in COMPILERS:
        r = data.pages[(cell, cc, mode)]
        out.append(num(r['change_percent']) + '%' + ('†' if data.marked(r) else ''))
    return ' / '.join(out)


def page_values(data):
    v = {}
    groups = [data.cells[page_cell('all', 3345, low)]['pool'] for low, _ in PAGE_SIZES]
    v['PAGES_INPUTS'] = (f"The groups hold {', '.join(str(len(g['indices'])) for g in groups[:-1])} and "
                         f"{len(groups[-1]['indices'])} pages with a median length of "
                         f"{', '.join(format(g['bytes']['median'] / 1024, '.1f') for g in groups[:-1])} and "
                         f"{groups[-1]['bytes']['median'] / 1024:.1f} KiB.")
    heads = ['Names', 'Call'] + [page_label(lo, hi) for lo, hi in PAGE_SIZES]
    rows = []
    for n in PAGE_NAMES:
        for op in ('all', 'replace'):
            first = f'{n:,}' if op == 'all' else ''
            rows.append([first, OPS[op]] + [page_change(data, page_cell(op, n, lo)) for lo, _ in PAGE_SIZES])
    v['PAGES_TABLE'] = table(heads, rows, 2)
    longest = PAGE_SIZES[-1][0]
    span = lambda recs: (lambda xs: f'{num(min(xs))}…{num(max(xs))}%')([r['change_percent'] for r in recs])  # noqa: E731
    pick = lambda pred: [r for (c, _, m), r in data.pages.items() if m == 'oneshot' and pred(c)]  # noqa: E731
    v['PAGES_LONG_SMALL'] = span(pick(lambda c: c.endswith(f'.p{longest}') and '.n3345.' not in c))
    v['PAGES_REPLACE_3345'] = span(pick(lambda c: '.replace.n3345.' in c))
    hits = []
    for n in PAGE_NAMES:
        shares = [100 * c['pool']['occurrences']['texts_with_matches'] / len(c['pool']['indices'])
                  for c in (data.cells[page_cell('all', n, lo)] for lo, _ in PAGE_SIZES)]
        hits.append(f"{n:,} names {', '.join(f'{x:.0f}' for x in shares)}%")
    v['PAGES_HITS'] = 'Pages with at least one name, by group: ' + '; '.join(hits) + '.'
    v['PAGES_LONGEST'] = page_label(*PAGE_SIZES[-1])
    return v


def grid(data, prefix, ns, lengths, placement, mode):
    rows = []
    for n in ns:
        row = [n]
        for b in lengths:
            row.append(data.pair(f'{prefix}.n{n}.b{b}' + (f'.{placement}' if placement else ''), mode))
        rows.append(row)
    return table(['Keys'] + [size(b) for b in lengths], rows)




def oneshot_cell(n, b, op, placement):
    group = 'crossover' if b in (1536, 2048, 3072) else 'controlled'
    return f'{group}/{op}.n{n}.b{b}.{placement}'


NOISE = 3.0  # changes within this many percent are not told apart


def bold_pair(data, cell, mode):
    """'GCC / Clang' change, bold when both compilers are faster by more than NOISE %; '—' if not measured."""
    if data.get(cell, 'gcc15', mode) is None:
        return '—'
    text = data.pair(cell, mode)
    return f'**{text}**' if max(data.changes([cell], [mode])) < -NOISE else text


GRID_CALLS = [('unique', 'one', OPS['unique']), ('count', 'one', OPS['count']), ('all', 'one', OPS['all']),
              ('any', 'absent', OPS['any'] + ', no match'), ('any', 'one', OPS['any'] + ', match in the middle'),
              ('replace', 'one', OPS['replace'])]
GRID_LENGTHS = {'prepared': [128, 1024, 4096, 16384, 65536],
                'oneshot': [128, 1024, 1536, 2048, 3072, 4096, 16384, 65536]}


def mode_grid(data, mode):
    """Random keys x text length for one mode, one row per call: 'GCC / Clang' change against the fastest
    existing method. The text has one match in the middle third, or none for matches() where the row says so."""
    rows = []
    for n in CONTROLLED_N:
        for i, (op, placement, label) in enumerate(GRID_CALLS):
            rows.append([n if i == 0 else '', label]
                        + [bold_pair(data, oneshot_cell(n, b, op, placement), mode) for b in GRID_LENGTHS[mode]])
    heads = ['Keys', 'Call'] + [size(b) if b % 1024 == 0 or b < 1024 else f'{b / 1024:g} KiB' for b in GRID_LENGTHS[mode]]
    return table(heads, rows, 2)


def controlled_tables(data, mode):
    parts = []
    for op, placements in [('any', ['one', 'absent', 'start', 'end']), ('unique', ['one', 'spread16']),
                           ('count', ['one', 'spread16']), ('all', ['one', 'spread16']),
                           ('replace', ['one', 'absent', 'spread16'])]:
        for placement in placements:
            lengths = [b for b in LENGTHS if f'controlled/{op}.n8.b{b}.{placement}' in data.cells]
            parts.append(f'**{OPS[op]}, {PLACEMENTS[placement]}**\n\n'
                         + grid(data, f'controlled/{op}', CONTROLLED_N, lengths, placement, mode))
    return '\n\n'.join(parts)


def natural_tables(data, mode):
    return '\n\n'.join(f'**{OPS[op]}**\n\n' + grid(data, f'natural/{op}', NATURAL_N, NATURAL_LENGTHS, None, mode)
                       for op in OPS)


def bytes_per_char(lang):
    text = (ROOT / f'corpus/{lang}.txt').read_bytes()
    return len(text) / len(text.decode())


def language_tables(data, mode):
    parts = []
    for dictionary, title in [('words', 'Frequent words of the same language (128 keys)'),
                              ('identifiers', 'PHP names (128 keys, ASCII)')]:
        rows = []
        for lang, name in LANGUAGES.items():
            for b in (4096, 65536):
                rows.append([name if b == 4096 else '', f'{bytes_per_char(lang):.2f}' if b == 4096 else '', size(b)]
                            + [data.pair(f'languages/{lang}.{dictionary}.{op}.b{b}', mode) for op in OPS])
        parts.append(f'**{title}**\n\n' + table(['Text', 'Bytes per character', 'Length'] + list(OPS.values()),
                                                rows, numeric_from=1))
    return '\n\n'.join(parts)


def counterexample_tables(data):
    rows = []
    for cell, label in [('few.{op}.n1.b4096', '1 key'), ('few.{op}.n4.b4096', '4 keys')]:
        for op in OPS:
            c = f'counterexamples/{cell.format(op=op)}'
            for mode, mode_name in MODES:
                r = data.get(c, 'gcc15', mode)
                if r is not None:
                    rows.append([f'{label}, {OPS[op]}', mode_name, method_name(r['reference'], data.cells[c]), micro(r['reference_us']),
                                 data.change(c, 'gcc15', mode), data.change(c, 'clang21', mode)])
    few = table(['Input', 'Mode', 'Fastest existing method', 'Its time, µs', 'Change, GCC', 'Change, Clang'], rows, 3)
    rows = []
    for op in ['unique', 'count', 'all', 'replace']:
        for b in (4096, 65536):
            c = f'counterexamples/dense.{op}.b{b}'
            for mode, mode_name in MODES:
                r = data.get(c, 'gcc15', mode)
                if r is not None:
                    rows.append([f'{OPS[op]}, {size(b)}', mode_name, method_name(r['reference'], data.cells[c]), micro(r['reference_us']),
                                 data.change(c, 'gcc15', mode), data.change(c, 'clang21', mode)])
    dense = table(['Input', 'Mode', 'Fastest existing method', 'Its time, µs', 'Change, GCC', 'Change, Clang'], rows, 3)
    return few, dense


def construct_rows(data):
    groups = {}
    for r in data.construct:
        groups.setdefault((r['dictionary'], r['class'], r['compiler']), []).append(r)
    out = {}
    for (dictionary, cls, cc), rs in groups.items():
        out[(dictionary, cls, cc)] = {'us': st.median(r['construct_us'] for r in rs),
                                      'retained': st.median(r['retained_bytes'] for r in rs),
                                      'peak': st.median(r['peak_bytes'] for r in rs),
                                      'keys': rs[0]['keys'], 'key_bytes': rs[0]['key_bytes']}
    return out


def kib(n):
    return f'{n / 1024:,.0f}' if n >= 10 * 1024 else f'{n / 1024:.1f}'


def construct_short(data, names):
    rows = construct_rows(data)
    out = []
    for d in dict.fromkeys(r['dictionary'] for r in data.construct):
        if d not in names:
            continue
        m, r = rows[(d, 'matcher', 'gcc15')], rows[(d, 'replacer', 'gcc15')]
        label = d.replace('random a-p', 'random letters a–p').replace('PHP identifiers', 'PHP names')
        out.append([label, micro(m['us']), kib(m['retained']), micro(r['us']), kib(r['retained'])])
    return table(['Dictionary', 'Matcher build, µs', 'Matcher memory, KiB', 'Replacer build, µs',
                  'Replacer memory, KiB'], out)


def construct_table(data, names=None, memory=False):
    rows = construct_rows(data)
    dictionaries = list(dict.fromkeys(r['dictionary'] for r in data.construct))
    if names:
        dictionaries = [d for d in dictionaries if d in names]
    out = []
    for d in dictionaries:
        m, r = rows.get((d, 'matcher', 'gcc15')), rows.get((d, 'replacer', 'gcc15'))
        mc, rc = rows.get((d, 'matcher', 'clang21')), rows.get((d, 'replacer', 'clang21'))
        if not m:
            continue
        label = (d.replace('random a-p', 'random letters a–p').replace('nested a..a', 'nested a, aa, …')
                 .replace('PHP identifiers', 'PHP names'))
        if memory:
            out.append([label, kib(m['key_bytes']), kib(m['retained']), kib(m['peak']), kib(r['retained']), kib(r['peak'])])
        else:
            out.append([label, kib(m['key_bytes']), micro(m['us']), micro(mc['us']), micro(r['us']), micro(rc['us'])])
    if memory:
        return table(['Dictionary', 'Keys, KiB', 'Matcher kept, KiB', 'Matcher peak, KiB', 'Replacer kept, KiB',
                      'Replacer peak, KiB'], out)
    return table(['Dictionary', 'Keys, KiB', 'Matcher, GCC', 'Matcher, Clang', 'Replacer, GCC', 'Replacer, Clang'], out)


SLOW_DICTIONARIES = ('nested a..a', '64-byte common prefix', 'random bytes')


def page_summaries(data):
    """Findings at the top of languages.md, edge-cases.md and construction.md."""
    v = {}
    lang = lambda langs, dictionaries, ops, sizes: [  # noqa: E731
        f'languages/{lg}.{d}.{op}.b{b}' for lg in langs for d in dictionaries for op in ops for b in sizes]
    latin, other, ops = ('en', 'es', 'emoji'), ('ru', 'zh', 'ja', 'ko'), list(OPS)
    both, sizes = ('words', 'identifiers'), (4096, 65536)
    v['LANG_PREP_LATIN'] = data.span(lang(latin, both, ops, sizes), ['prepared'])
    rest = [c for c in lang(other, both, ops, sizes) if '.words.any.' not in c]
    v['LANG_PREP_OTHER'] = data.span(rest, ['prepared'])
    v['LANG_ANY_WORDS_PREP'] = data.span(lang(other, ['words'], ['any'], sizes), ['prepared'])
    us = [r['reference_us'] for c in lang(other, ['words'], ['any'], sizes) for cc, _ in COMPILERS
          if (r := data.get(c, cc, 'prepared'))]
    v['LANG_ANY_WORDS_US'] = f'{micro(min(us))}–{micro(max(us))}'
    v['LANG_ANY_WORDS_ONESHOT'] = data.span(lang(LANGUAGES, ['words'], ['any'], sizes), ['oneshot'])
    no_any_words = lambda cells: [c for c in cells if '.words.any.' not in c]  # noqa: E731
    v['LANG_ONESHOT_64K'] = data.span(no_any_words(lang(LANGUAGES, both, ops, [65536])), ['oneshot'])
    v['LANG_ONESHOT_4K_LATIN'] = data.span(no_any_words(lang(latin, both, ops, [4096])), ['oneshot'])
    v['LANG_ONESHOT_4K_OTHER'] = data.span(no_any_words(lang(other, both, ops, [4096])), ['oneshot'])

    def times(cells):
        values = data.changes(cells, ['prepared', 'oneshot'])
        lo, hi = (1 + f(values) / 100 for f in (min, max))
        return f'{lo:.1f} to {hi:.0f}' if hi >= 10 else f'{lo:.1f} to {hi:.1f}'
    v['FEW_1_TIMES'] = times([c for c in data.cells if c.startswith('counterexamples/few.') and '.n1.' in c])
    v['FEW_4_TIMES'] = times([c for c in data.cells if c.startswith('counterexamples/few.') and '.n4.' in c])
    v['DENSE_SPAN'] = data.span([c for c in data.cells if c.startswith('counterexamples/dense.')], ['prepared', 'oneshot'])

    rows = construct_rows(data)
    ordinary = [d for (d, cls, cc) in rows if cls == 'matcher' and cc == 'gcc15' and not d.startswith(SLOW_DICTIONARIES)]
    per_kib = [rows[(d, 'matcher', 'gcc15')]['us'] / (rows[(d, 'matcher', 'gcc15')]['key_bytes'] / 1024) for d in ordinary]
    v['BUILD_PER_KIB'] = f'{min(per_kib):.0f}–{max(per_kib):.0f}'
    slow = [x['us'] / (x['key_bytes'] / 1024) for (d, cls, cc), x in rows.items() if d.startswith(SLOW_DICTIONARIES) and cc == 'gcc15']
    v['BUILD_PER_KIB_MAX'] = f'{max(slow):.0f}'
    names = [d for d in ordinary if d.startswith(('PHP identifiers', 'PHP functions'))
             and int(re.search(r'(\d+) keys', d).group(1)) >= 512]
    ratio = [rows[(d, 'replacer', 'gcc15')]['us'] / rows[(d, 'matcher', 'gcc15')]['us'] for d in names]
    v['REPLACER_NAMES_RATIO'] = f'{min(ratio):.1f}–{max(ratio):.1f}'
    simple = [d for d in ordinary if d.startswith(('random a-p', 'words'))]
    ratio = [rows[(d, 'replacer', cc)]['us'] / rows[(d, 'matcher', cc)]['us'] for d in simple for cc, _ in COMPILERS]
    v['REPLACER_SIMPLE_GAP'] = f'{100 * max(abs(x - 1) for x in ratio):.0f}'
    return v


def sources_table(data):
    rows = []
    for name, s in data.sources['sources'].items():
        rev = s.get('revision') or [s.get('file', '')]
        ref = f"`{rev[0][:12]}`" if rev and rev[0] and re.fullmatch(r'[0-9a-f]{40}', rev[0]) else f"`{rev[0]}`"
        rows.append([f"[{name}]({s['url']})", ref, s['licence'], s['used_for']])
    return '\n'.join('| ' + ' | '.join(r) + ' |' for r in rows)


def flag_summary(data):
    records = list(data.results.values())
    marked = [r for r in records if data.marked(r)]
    spreads = sorted(r['spread_percent'] for r in records)
    return {
        'RECORDS': str(len(records)),
        'MARKED': str(len(marked)),
        'SPREAD_MEDIAN': f'{spreads[len(spreads) // 2]:.1f}',
        'SPREAD_P90': f'{spreads[int(0.9 * len(spreads))]:.1f}',
        'RECHECKED': str(sum(1 for r in records if r['processes'] > 3)),
        'FAST_PASS_MEDIAN': f"{st.median(r['calls_per_pass'] * min(r['native_us'], r['reference_us']) for r in records) / 1000:.0f}",
        'UNRECHECKED': str(sum(1 for r in records if r['spread_percent'] > SPREAD_LIMIT and r['processes'] == 3)),
        'AA_OVER': str(sum(1 for r in records if abs(r['aa_max_percent']) > AA_LIMIT)),
    }


COMMIT = 'bb508627af16e029c3c760109461c7596259484c'
ENVIRONMENT = {
    'PR_URL': 'https://github.com/php/php-src/pull/25122',
    'COMMIT_SHORT': COMMIT[:10],
    'COMMIT_URL': f'https://github.com/php/php-src/commit/{COMMIT}',
    'AA_LIMIT': f'{AA_LIMIT:g}', 'SPREAD_LIMIT': f'{SPREAD_LIMIT:g}', 'PROCESSES': '3', 'RECHECK': '2',
    'MACHINE': 'AMD Ryzen 9 5950X (Zen 3, two 8-core CCDs), Ubuntu 26.04, Linux 7.0',
    'GCC': '15.2.0', 'CLANG': '21.1.8',
    'CFLAGS': '-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64',
}
GROUP_NAMES = {'controlled': 'random-key grid', 'natural': 'PHP-name grid', 'languages': 'languages',
               'scenarios': 'scenarios', 'counterexamples': 'edge cases', 'crossover': 'one-shot cells at 1.5–3 KiB'}


def core_split(data):
    """Which group ran on which core, and how far the cross-core repeat of random-key inputs moved."""
    cores = {}
    for r in data.results.values():
        cores.setdefault(r['cpu'], set()).add(r['cell'].split('/')[0])
    parts = [f"CPU {cpu}: {', '.join(GROUP_NAMES[g] for g in GROUP_NAMES if g in groups)}"
             for cpu, groups in sorted(cores.items())]
    check = json.loads((ROOT / 'data/corecheck.json').read_text())
    cross = [r for r in check if data.get(r['cell'], r['compiler'], r['mode'])['cpu'] != r['cpu']]
    rel = sorted(100 * abs(r['ratio'] / data.get(r['cell'], r['compiler'], r['mode'])['ratio'] - 1) for r in cross)
    groups = {}
    for r in cross:
        groups.setdefault(r['cell'].split('/')[0], set()).add(r['cell'])
    label = {'controlled': 'random-key', 'crossover': 'PHP-name 1.5–3 KiB', 'scenarios': 'scenario'}
    repeated = ', '.join(f'{len(cells)} {label[g]}' for g, cells in sorted(groups.items()))
    return (f"{'; '.join(parts)}. The two cores are on different CCDs. The random-key grid and the PHP-name grid "
            'with languages ran at the same time; edge cases and scenarios ran later alone, and the 1.5–3 KiB cells '
            f'later on both cores. Repeated on the other core ([data/corecheck.json](data/corecheck.json)): {repeated} '
            'inputs; the tables use the core listed above. Between the cores the native/reference ratio moved by '
            f'{rel[len(rel) // 2]:.1f}% in the median and {rel[-1]:.1f}% at most.')


def branch_probe_table():
    import csv
    rows = list(csv.DictReader((ROOT / 'data/probe/branch-probe.csv').open()))
    by = {(r['cc'], r['op'], r['texts'], r['pass'], r['calls']): r for r in rows}
    groups = {}
    for (cc, op, texts, p, calls), r in by.items():
        if calls == '0' or texts == 'orig':
            continue
        zero, n = by[(cc, op, texts, p, '0')], int(calls)
        groups.setdefault((cc, op, texts), []).append(
            ((int(r['branch_misses']) - int(zero['branch_misses'])) / n, float(r['ns_per_call']) / 1000))
    global PROBE_GROUPS
    PROBE_GROUPS = groups
    out = []
    for cc, name in COMPILERS:
        for op in ('count', 'unique', 'replace'):
            one, many = groups[(cc, op, '1')], groups[(cc, op, '64')]
            out.append([name, OPS[op], f'{st.median(m for m, _ in one):,.0f}', f'{st.median(m for m, _ in many):,.0f}',
                        f'{st.median(t for _, t in one):.1f}', f'{st.median(t for _, t in many):.1f}'])
    return table(['Compiler', 'Call', 'Branch misses, one text', '64 texts', 'µs, one text', '64 texts'], out, 2)


PROBE_GROUPS = {}


def probe_range(texts):
    values = [st.median(t for _, t in v) for (cc, op, t), v in PROBE_GROUPS.items() if t == texts]
    return f'{min(values):.1f}–{max(values):.1f}'


def calibration_table():
    lines = (ROOT / 'data/probe/calibration-summary.txt').read_text().splitlines()
    out = []
    for line in lines:
        f = line.split()
        if len(f) == 9 and f[0].isdigit():
            out.append(f)
    return table(['Pass, ms', 'Passes', 'Processes', 'Time per method, ms', 'Ratio spread, median %', 'p90 %',
                  'max %', 'Max |A/A|, %', 'Native spread p90, %'], out, 0)


KINDS = [('controlled', 'Random keys'), ('natural', 'PHP names'), ('crossover', 'Crossover lengths'),
         ('languages', 'Text languages'), ('scenarios', 'Application scenarios'), ('counterexamples', 'Edge cases'),
         ('pages', 'Manual pages by length')]


def input_label(kind, cell_id):
    """Human label of a cell from its id: keys, text length, match position or language."""
    if kind == 'scenarios':
        return 'all texts of the scenario'
    parts = []
    for token in cell_id.split('.'):
        if token in OPS:
            continue
        if m := re.fullmatch(r'n(\d+)', token):
            parts.append(f'{m.group(1)} keys' if kind not in ('natural', 'pages') else f'{m.group(1)} PHP names')
        elif m := re.fullmatch(r'names(\d+)', token):
            parts.append(f'{m.group(1)} PHP names')
        elif m := re.fullmatch(r'b(\d+)', token):
            parts.append(size(int(m.group(1))))
        elif m := re.fullmatch(r'p(\d+)', token):
            parts.append('pages of ' + page_label(*next(s for s in PAGE_SIZES if s[0] == int(m.group(1)))))
        elif token == 'autolink':
            continue
        elif token in PLACEMENTS:
            parts.append(PLACEMENTS[token])
        else:
            parts.append(LANGUAGES.get(token, {'words': 'frequent words', 'identifiers': 'PHP names',
                                               'dense': 'dense matches', 'few': 'few keys'}.get(token, token)))
    return ', '.join(parts)


def sort_key(cell_id):
    numbers = [int(x) for x in re.findall(r'(?:^|\.)(?:n|names|b|p)(\d+)', cell_id)]
    return (re.sub(r'\d+', '', cell_id), numbers)


def method_cell(r, method):
    if method in r['methods_us']:
        text = micro(r['methods_us'][method])
        return f'**{text}**' if method == r['reference'] else text
    if method in r['untimed']:
        return f'≈{micro(r["untimed"][method])}'
    if method in r['excluded']:
        return 'too large' if 'too large' in r['excluded'][method] else 'wrong result'
    return '—'


def keys_of(kind, cid):
    m = re.search(r'(?:^|\.)(?:n|names)(\d+)(?:\.|$)', cid)
    return int(m.group(1)) if m and kind in ('controlled', 'natural', 'crossover', 'pages') else None


def all_methods(data):
    """Every value with the time of every existing method: per data set, call, mode and key count."""
    scenario_titles = {cell.split('/')[1]: title for title, cell in SCENARIOS}
    out = []
    for kind, title in KINDS:
        out.append(f'## {title}')
        ids = sorted({c.split('/', 1)[1] for c in data.cells if c.startswith(kind + '/')}, key=sort_key)
        ops = sorted({data.cells[f'{kind}/{cid}']['op'] for cid in ids}, key=list(OPS).index)
        for op in ops:
            op_ids = [cid for cid in ids if data.cells[f'{kind}/{cid}']['op'] == op]
            if kind == 'scenarios':
                parts = [(scenario_titles.get(cid, cid), [cid]) for cid in op_ids]
            else:
                out.append(f'### {OPS[op]}')
                counts = sorted({keys_of(kind, cid) for cid in op_ids}, key=lambda n: n or 0)
                parts = [(None, [cid for cid in op_ids if keys_of(kind, cid) == n]) for n in counts]
            for heading, cids in parts:
                if heading:
                    out.append(f'### {heading}')
                for mode, mode_title in MODES:
                    recs = [(cid, label, data.get(f'{kind}/{cid}', cc, mode)) for cid in cids for cc, label in COMPILERS]
                    recs = [x for x in recs if x[2] is not None]
                    if not recs:
                        continue
                    methods = []
                    for _, _, r in recs:
                        for m in [*r['methods_us'], *r['untimed'], *r['excluded']]:
                            if m not in methods and universal(f'{kind}/{cids[0]}', m):
                                methods.append(m)
                    methods.sort(key=lambda m: (m.startswith('pcre'), m))
                    meta = data.cells[f'{kind}/{cids[0]}']
                    names = [method_name(m, meta) for m in methods]
                    names = [n + (', second copy' if n in names[:i] else '') + ', µs' for i, n in enumerate(names)]
                    heads = ['Input', 'Compiler', 'New class, µs'] + names
                    heads.append('Change against the fastest')
                    rows = [[input_label(kind, cid), label.split()[0], micro(r['native_us'])]
                            + [method_cell(r, m) for m in methods]
                            + [data.change(f'{kind}/{cid}', r['compiler'], mode)] for cid, label, r in recs]
                    n = keys_of(kind, cids[0])
                    what = f'{n} {"PHP names" if kind in ("natural", "pages") or "names" in cids[0] else "keys"}, ' if n else ''
                    out.append(f'**{what}{mode_title.lower()}**')
                    out.append(table(heads, rows, 2))
    return '\n\n'.join(out)




def placeholders(data):
    v = {**ENVIRONMENT, 'BRANCH_PROBE_TABLE': branch_probe_table(), 'CALIBRATION_TABLE': calibration_table(),
         'LEGEND': LEGEND, 'GRID_LEGEND': GRID_LEGEND.format(root=''), 'MARK_SPREAD': f'{MARK_SPREAD:.0f}',
         'MARK_AA': f'{MARK_AA:.0f}', 'PROBE_ONE_US': probe_range('1'), 'PROBE_MANY_US': probe_range('64')}
    v['SCENARIOS_TABLE'] = scenario_table(data)
    v['SCENARIO_INPUTS'] = scenario_inputs(data)
    v['BOTS_DISTINCT'] = f"{distinct_documents(data.cells['scenarios/bots.any']):,}"
    v.update(page_values(data))
    for mode, _ in MODES:
        key = mode.upper()
        v[f'CONTROLLED_{key}'] = controlled_tables(data, mode)
        v[f'NATURAL_{key}'] = natural_tables(data, mode)
        v[f'LANGUAGES_{key}'] = language_tables(data, mode)
    v['PREPARED_GRID'] = mode_grid(data, 'prepared')
    v['ONESHOT_GRID'] = mode_grid(data, 'oneshot')
    v['FEW_TABLE'], v['DENSE_TABLE'] = counterexample_tables(data)
    v['CONSTRUCT_TABLE'] = construct_table(data)
    v['CONSTRUCT_MEMORY'] = construct_table(data, memory=True)
    v.update(page_summaries(data))
    v['CONSTRUCT_SHORT'] = construct_short(data, {'random a-p, 8 keys', 'random a-p, 128 keys', 'random a-p, 1024 keys',
                                                  'LDNOOBW, 403 keys', 'crawler patterns, 1469 keys',
                                                  'PHP functions, 3345 keys', 'PHP identifiers, 8019 keys'})
    v['SOURCES_TABLE'] = sources_table(data)
    v.update(flag_summary(data))
    v['CORE_SPLIT'] = core_split(data)
    check = json.loads((ROOT / 'data/corecheck.json').read_text())
    v['CROSS_MAX'] = f"{max(100 * abs(r['ratio'] / data.get(r['cell'], r['compiler'], r['mode'])['ratio'] - 1) for r in check):.1f}"
    pairs = [(r, data.get(c, 'clang21', m)) for (c, cc, m), r in data.results.items() if cc == 'gcc15']
    for mode in ('prepared', 'oneshot'):
        v[f'CLANG_GAP_{mode.upper()}'] = f"{100 * st.median(c['native_us'] / g['native_us'] - 1 for g, c in pairs if g['mode'] == mode):.0f}"
    v['LOAD_COUNT'] = str(sum(1 for r in data.results.values() if 'load' in r['flags']))
    v['UNTIMED_MIN'] = f"{min(min(r['untimed'].values()) / r['reference_us'] for r in data.results.values() if r['untimed']):.2f}"

    controlled = [c for c in data.cells if c.startswith('controlled/')]
    natural = [c for c in data.cells if c.startswith('natural/')]
    n_of = lambda c: int(re.search(r'\.n(\d+)\.', c).group(1))  # noqa: E731
    b_of = lambda c: int(re.search(r'\.b(\d+)', c).group(1))  # noqa: E731
    not_start = [c for c in controlled if not c.endswith('.start')]
    start = [c for c in controlled if c.endswith('.start')]
    v['PREPARED_32_PLUS'] = data.span([c for c in not_start if n_of(c) >= 32], ['prepared'])
    r32 = [r['ratio'] for c in not_start + natural if n_of(c) >= 32 for cc, _ in COMPILERS
           if (r := data.get(c, cc, 'prepared'))]
    v['PREPARED_32_TIMES'] = f'{1 / max(r32):.1f} to {1 / min(r32):.0f}'
    v['PREPARED_16'] = data.span([c for c in not_start if n_of(c) == 16], ['prepared'])
    v['START_16'] = data.span([c for c in start if n_of(c) == 16], ['prepared'])
    v['PREPARED_8_ALL'] = data.span([c for c in not_start if n_of(c) == 8], ['prepared'])
    rows = construct_rows(data)
    v['CLANG_BUILD_GAP'] = f"{100 * max(abs(rows[(d, c, 'clang21')]['us'] / x['us'] - 1) for (d, c, cc), x in rows.items() if cc == 'gcc15'):.0f}"
    scen = [r['ratio'] for (c, _, m), r in data.results.items() if c.startswith('scenarios/') and m == 'prepared']
    v['ONESHOT_4K_128'] = data.span([c for c in not_start if n_of(c) == 128 and b_of(c) == 4096], ['oneshot'])
    mid = lambda n: data.get(f'controlled/any.n{n}.b4096.one', 'gcc15', 'prepared')  # noqa: E731
    v['ANY_MID_16_US'], v['ANY_MID_1024_US'] = micro(mid(16)['native_us']), micro(mid(1024)['native_us'])
    v['PREPARED_NATURAL_32_PLUS'] = data.span([c for c in natural if n_of(c) >= 32], ['prepared'])
    st32 = data.changes([c for c in start if n_of(c) >= 32], ['prepared'])
    v['START_32_PLUS_LO'], v['START_32_PLUS_HI'] = f'{num(min(st32))}%', f'{num(max(st32))}%'
    v['ONESHOT_START_16'] = data.span([c for c in start if n_of(c) >= 16], ['oneshot'])
    v['START_1024'] = data.span([c for c in start if n_of(c) == 1024], ['prepared'])
    rng = lambda xs: f'{micro(min(xs))}–{micro(max(xs))}'  # noqa: E731
    pcre_start = lambda n: [data.get(c, 'gcc15', 'prepared')['reference_us'] for c in start if n_of(c) == n]  # noqa: E731
    v['START_PCRE_LOW_US'] = rng(pcre_start(16))
    v['START_PCRE_HIGH_US'] = rng(pcre_start(1024))
    v['REF_MID_16_US'] = micro(data.get('controlled/any.n16.b4096.one', 'gcc15', 'prepared')['reference_us'])
    v['REF_MID_1024_US'] = micro(data.get('controlled/any.n1024.b4096.one', 'gcc15', 'prepared')['reference_us'])
    v['REPLACE_1024_SHORT'] = data.span([oneshot_cell(1024, b, 'replace', p) for b in GRID_LENGTHS['oneshot'] if 1024 <= b <= 4096
                                         for p in ('one', 'absent', 'spread16')
                                         if oneshot_cell(1024, b, 'replace', p) in data.cells], ['oneshot'])
    gcc_start = lambda mode, key: [data.get(c, 'gcc15', mode)[key] for c in start if n_of(c) >= 16]  # noqa: E731
    v['START_NATIVE_16_US'] = rng(gcc_start('prepared', 'native_us'))
    v['START_ONESHOT_NATIVE_US'] = rng(gcc_start('oneshot', 'native_us'))
    v['START_ONESHOT_PCRE_US'] = rng(gcc_start('oneshot', 'reference_us'))
    recs = [data.get(c, 'gcc15', 'oneshot') for c in controlled if n_of(c) == 16 and b_of(c) == 128]
    span = lambda xs: f'{micro(min(xs))}–{micro(max(xs))}'  # noqa: E731
    v['ONESHOT_128B_16_REF'] = span([r['reference_us'] for r in recs])
    v['ONESHOT_128B_16_NATIVE'] = span([r['native_us'] for r in recs])
    v['ALL_METHODS'] = all_methods(data)
    raw = [r['change_without_noop_percent'] for c in not_start if n_of(c) >= 32 for cc, _ in COMPILERS
           if (r := data.get(c, cc, 'prepared'))]
    v['PREPARED_32_PLUS_RAW'] = f'{num(min(raw))}…{num(max(raw))}%'
    return v


def render():
    data = Data()
    values = placeholders(data)
    for template in sorted([*ROOT.glob('*.md.in'), *ROOT.glob('data/*.md.in')]):
        text = template.read_text()
        for name in set(re.findall(r'\{\{([A-Z0-9_]+)\}\}', text)):
            if name in values:
                text = text.replace('{{' + name + '}}', values[name])
        missing = re.findall(r'\{\{([A-Z0-9_]+)\}\}', text)
        if missing:
            print(f'{template.relative_to(ROOT)}: unfilled {sorted(set(missing))}')
        template.with_suffix('').write_text(text)


if __name__ == '__main__':
    render()
