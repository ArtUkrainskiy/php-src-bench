#!/usr/bin/env python3
"""Count the final hybrid layout from saved byte dictionaries, without measuring PHP."""

import argparse
import json
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def layout(keywords, kind):
    if kind not in ('Matcher', 'Replacer'):
        raise ValueError(kind)
    words = list(dict.fromkeys(word.encode('utf-8') for word in keywords))
    if any(not word for word in words):
        raise ValueError('Empty keywords are not accepted')
    alphabet = set().union(*map(set, words)) if words else set()
    children, depth, failure = [{}], [0], [0]
    for word in words:
        state = 0
        for byte in word if kind == 'Matcher' else reversed(word):
            target = children[state].get(byte)
            if target is None:
                target = len(children)
                children[state][byte] = target
                children.append({})
                depth.append(depth[state] + 1)
                failure.append(0)
            state = target
    queue = deque(children[0].values())
    while queue:
        state = queue.popleft()
        for byte, child in children[state].items():
            fallback = failure[state]
            while fallback and byte not in children[fallback]:
                fallback = failure[fallback]
            failure[child] = children[fallback].get(byte, 0)
            queue.append(child)
    dense = [
        depth[state] <= 3
        or len(edges) >= 8
        or (depth[failure[state]] > 3 and depth[state] - depth[failure[state]] <= 4)
        for state, edges in enumerate(children)
    ]
    states = len(children) if words else 0
    dense_states = sum(dense) if words else 0
    packed_edges = sum(len(edges) for state, edges in enumerate(children) if not dense[state] and len(edges) > 1)
    parts = {
        'dense_transition_bytes': 4 * dense_states * (len(alphabet) + 1),
        'sparse_metadata_bytes': 12 * (states - dense_states),
        'packed_edge_bytes': 8 * packed_edges,
        'output_metadata_bytes': (12 if kind == 'Matcher' else 4) * states,
        'dictionary_pointer_bytes': (8 if kind == 'Matcher' else 16) * len(words),
    }
    return {
        'states': states,
        'dense_states': dense_states,
        'sparse_states': states - dense_states,
        'packed_edges': packed_edges,
        'alphabet_bytes': len(alphabet),
        'keyword_bytes': sum(map(len, words)),
        'requested_array_bytes': sum(parts.values()),
        **parts,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    parser.parse_args()
    index = json.loads((ROOT / 'index.json').read_text())
    checked = 0
    for family in index['families']:
        words = list(json.loads((ROOT / (family + '.json')).read_text())['replacements'])
        facts = json.loads((ROOT / (family + '-expected.json')).read_text())
        for fact in facts:
            for kind in ['Matcher', 'Replacer']:
                result = layout(words[: fact['size']], kind)
                assert result['states'] == fact[kind.lower() + '_states']
                assert result['keyword_bytes'] == fact['keyword_bytes']
                assert result['alphabet_bytes'] == fact['alphabet_bytes']
                assert result['dense_states'] + result['sparse_states'] == result['states']
                checked += 1
    print(f'Hybrid layout facts PASS: {checked} class/dictionary combinations')


if __name__ == '__main__':
    main()
