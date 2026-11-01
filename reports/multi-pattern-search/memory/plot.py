#!/usr/bin/env python3
"""Optional figure regeneration: install Matplotlib in a separate plotting environment."""
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT.parent / 'data/memory-gcc15.json').read_text())
plt.rcParams.update({'svg.fonttype': 'none', 'svg.hashsalt': 'strmatch-memory', 'font.size': 10})
fig, axes = plt.subplots(1, 2, figsize=(12, 4.7), layout='constrained')
colors = {'glossary-catalog': '#0072B2', 'permuted-control': '#D55E00'}
for family, label in [('glossary-catalog', 'Glossary + catalog'), ('permuted-control', 'Permuted control')]:
    for kind, marker, style in [('Matcher', 'o', '-'), ('Replacer', 's', '--')]:
        rows = [r for r in data['rows'] if r['family'] == family and r['class'] == kind]
        x = [r['size'] for r in rows]
        y = [r['samples'][0]['construction']['object_extra_bytes'] for r in rows]
        kwargs = {'marker': marker, 'linestyle': style, 'color': colors[family], 'markersize': 4,
                  'label': label + ' / ' + kind}
        axes[0].plot(x, [v / 1048576 for v in y], **kwargs)
        axes[1].plot(x, [v / n / 1024 for v, n in zip(y, x)], **kwargs)
axes[0].set(xlabel='Dictionary strings', ylabel='Additional prepared-object memory (MiB)',
            title='Measured allocation above the input array', xlim=(0, 10400), ylim=(0, None))
axes[1].set(xlabel='Dictionary strings (log scale)', ylabel='Additional KiB per dictionary string',
            title='Constant bytes/string would be proportional growth', xscale='log', ylim=(0, None))
for ax in axes:
    ax.grid(True, alpha=0.25)
axes[0].legend(loc='upper left', fontsize=8)
fig.suptitle('Matcher and Replacer memory: 8 to 10,000 strings')
fig.savefig(ROOT / 'growth.svg', metadata={'Date': None, 'Creator': 'Matplotlib ' + matplotlib.__version__,
                                        'Description': 'Five fresh processes; identical GCC/Clang byte counts. Lines join measured sizes only.'})
svg = ROOT / 'growth.svg'
svg.write_text('\n'.join(line.rstrip() for line in svg.read_text().splitlines()) + '\n')
print('Saved memory/growth.svg using Matplotlib ' + matplotlib.__version__)
