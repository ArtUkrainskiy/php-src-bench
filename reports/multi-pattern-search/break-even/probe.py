#!/usr/bin/env python3
"""Collect one explicit grid point without changing the frozen timing code."""
import argparse
from pathlib import Path
import study


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--environment', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--cpu', type=int, required=True)
    parser.add_argument('--sibling', type=int, required=True)
    parser.add_argument('--operation', choices=list(study.OPS), required=True)
    parser.add_argument('--keys', type=int, required=True)
    parser.add_argument('--bytes', type=int, required=True)
    parser.add_argument('--background', choices=['technical', 'comments'], default='technical')
    args = parser.parse_args()
    collector = study.Collector(args)
    assert args.keys in collector.plan['dictionary_sizes']
    assert args.bytes in collector.plan['subject_sizes']
    assert (args.output / 'time-done.json').exists()
    case = study.make_case(args.operation, args.keys, args.bytes, args.background)
    study.save(args.output / 'last-gap-probe.json', {
        'case': case['id'], 'reason': 'Last unused input slot: confirmed lower loss but flagged upper endpoint',
        'script_sha256': study.sha(Path(__file__)), 'fingerprint': collector.fingerprint})
    collector.measure(case, 'followup:resolve-unqualified-upper-endpoint')
    study.save(args.output / 'time-done.json', {'inputs': len(collector.selection), 'fingerprint': collector.fingerprint,
                                               'bounded_followup': True})


if __name__ == '__main__':
    main()
