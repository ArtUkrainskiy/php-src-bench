#!/usr/bin/env python3
"""Restore observed deltas on flagged AMD results without rewriting report prose."""
import argparse
import gzip
import json
import re
import statistics as stats
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load(path):
    if path.suffix == '.gz':
        with gzip.open(path, 'rt') as stream:
            return json.load(stream)
    return json.loads(path.read_text())


def native(point):
    return next(k for k in point['samples_ns'] if k in ['matcher', 'replacer', 'replacer_new'])


def delta(point, russian=False):
    samples = point['samples_ns']
    own = native(point)
    reference = min((k for k in samples if not k.startswith(('matcher', 'replacer', 'oneshot'))),
                    key=lambda k: stats.median(samples[k]))
    ratio = stats.median(a / b for a, b in zip(samples[own], samples[reference]))
    if ratio >= 2:
        return (f'в {ratio:.1f} раза медленнее'.replace('.', ',') if russian else f'{ratio:.1f} times slower')
    return f'{100 * (ratio - 1):+.2f}%'


def update_table(path, points, russian=False):
    by = {(p['compiler'], p['case'], p['scope']): p for p in points}
    compiler = 'gcc15'
    result, changed = [], 0
    for line in path.read_text().splitlines():
        heading = line.lstrip('#').strip().lower() if line.startswith('#') else ''
        if heading.startswith('clang'):
            compiler = 'clang21'
        elif heading.startswith('gcc'):
            compiler = 'gcc15'
        cells = [c.strip() for c in line.split('|')[1:-1]] if line.startswith('|') else []
        if len(cells) == 4 and any(re.fullmatch(r'[0-9.]+†', c) for c in cells[2:]):
            values = [re.match(r'([0-9.]+)', c).group(1) for c in cells[2:]]
            candidates = []
            for (cc, case, scope), p in by.items():
                if cc != compiler or scope != 'prepared':
                    continue
                q = by[(cc, case, 'oneshot')]
                if [f'{stats.median(x["samples_ns"][native(x)])/1000:.3f}' for x in [p, q]] == values:
                    candidates.append(case)
            assert len(candidates) == 1, (path, cells, candidates)
            for index, scope in [(2, 'prepared'), (3, 'oneshot')]:
                if re.fullmatch(r'[0-9.]+†', cells[index]):
                    p = by[(compiler, candidates[0], scope)]
                    cells[index] = cells[index][:-1] + ' (' + delta(p, russian) + ')†'
                    changed += 1
            line = '| ' + ' | '.join(cells) + ' |'
        result.append(line)
    path.write_text('\n'.join(result) + '\n')
    return changed


def variability(points, russian=False):
    lines = ['## ' + ('Фактический разброс замеров' if russian else 'Measured variability'), '',
             ('Разброс — максимальное абсолютное отклонение отсчёта от медианы своего способа. A/A — измеренное отличие двух одинаковых вызовов. Отмеченные результаты сохраняют время и наблюдаемую разницу.' if russian else
              'Spread is the maximum absolute sample deviation from its own median. A/A is the measured difference between identical calls. Flagged results retain the observed time and relative change.'), '',
             '| Compiler | Exact input | Mode | A/A | Sample spread by implementation |', '|---|---|---|---:|---|']
    for p in points:
        if not p.get('flags'):
            continue
        samples = {**p.get('control_samples_ns', {}), **p['samples_ns']}
        spread = ', '.join(k + ': ' + f'{100 * max(abs(v / stats.median(a) - 1) for v in a):.2f}%'
                           for k, a in samples.items() if isinstance(a, list) and a)
        lines.append(f"| {p['compiler']} | `{p['case']}` | {p['scope']} | {p['aa_percent']:+.2f}% | {spread} |")
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--russian-report', type=Path)
    args = parser.parse_args()
    points = load(ROOT / 'data/elapsed.json.gz')['points']
    for root, russian in [(ROOT.parent, False)] + ([(args.russian_report, True)] if args.russian_report else []):
        files = ['README.ru.md', 'benchmark/matcher.ru.md', 'benchmark/replacer.ru.md'] if russian else ['README.md', 'benchmark/matcher.md', 'benchmark/replacer.md']
        for name in files:
            path = root / name
            print(name, update_table(path, points, russian), 'restored deltas')
        quality = root / ('benchmark/QUALITY.ru.md' if russian else 'benchmark/QUALITY.md')
        text = quality.read_text()
        heading = '## Фактический разброс замеров' if russian else '## Measured variability'
        text = text.split(heading)[0].rstrip() + '\n\n' + variability(points, russian)
        quality.write_text(text)
    reuse = load(ROOT / 'data/reuse.json')
    for name in ['REUSE.md', 'REUSE.ru.md']:
        path = (args.russian_report / 'benchmark' / name) if name.endswith('.ru.md') and args.russian_report else ROOT / name
        if not path.exists():
            continue
        text = path.read_text()
        for p in reuse:
            if p['qualified']:
                continue
            reference = min((m for m in p['samples'] if not m.startswith('matcher')), key=lambda m: p['median_us'][m])
            ratio = stats.median(a / b for a, b in zip(p['samples']['matcher'], p['samples'][reference]))
            old = f"{p['median_us']['matcher']:.3f}† | † |"
            text = text.replace(old, f"{p['median_us']['matcher']:.3f}† | {100*(ratio-1):+.2f}%† |")
        path.write_text(text)


if __name__ == '__main__':
    main()
