#!/usr/bin/env python3
"""Import all four complete shared-input series and verify corrected counters against raw perf output."""
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent


def read(path):return json.loads(path.read_text())
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def path_roots(metadata, run_placeholder='${RUN_DIR}'):
    command=metadata.get('build_command',[])
    roots={}
    includes=[part[2:]for part in command if part.startswith('-I')]
    if includes:roots[includes[0]]='${PHP_BUILD}'
    for part in command:
        if part.endswith('/strmatch.c'):roots[str(Path(part).parent)]='${STRMATCH_SOURCE}'
    if command and '-o' in command:
        output=Path(command[command.index('-o')+1])
        roots[str(output.parent.parent)]=run_placeholder
    return roots


def public(value, roots=None):
    if roots is None:
        roots=path_roots(value.get('metadata',{})if isinstance(value,dict)else{})
    if isinstance(value,str):
        for actual,placeholder in sorted(roots.items(),key=lambda item:-len(item[0])):
            value=value.replace(actual,placeholder)
        return value
    if isinstance(value,list):return [public(v,roots)for v in value]
    if isinstance(value,dict):return {k:('measurement-host' if k=='host' else public(v,roots))for k,v in value.items()}
    return value


def events(text):
    result={}
    for line in text.splitlines():
        fields=line.split(';')
        if len(fields)>2 and fields[2]in ['cycles:u','instructions:u']:
            result[fields[2]]=float(fields[0])
    assert len(result)==2,'Missing raw counter event'
    return result


def capture(directory,corpus,stem,compiler):
    source=directory/f'data-{stem}-{compiler}'
    original=read(source/'results.json')
    meta=original['metadata']
    assert original['status']=='complete'
    assert meta['harness_sha256']==digest(ROOT/'harness.php'),'Stale harness'
    assert meta['driver_sha256']==digest(ROOT/'measure.py'),'Unknown driver'
    assert 'input_dictionary_sharing'in meta['protocol'],'No shared-input policy'
    index_path=ROOT/'../../corpus'/corpus/'index.json'
    index=read(index_path)
    assert meta['corpus_index_sha256']==digest(index_path)
    cases={c['id']:c for filename in index['suite_sha256'] for c in read(index_path.parent/filename)['cases']}
    expected={(c['id'],m['id'])for c in cases.values()for m in c['lifetime']['modes']}
    assert {(r['case'],r['lifecycle'])for r in original['rows']}==expected
    assert len(original['rows'])==len(expected)
    timed={};first=defaultdict(list)
    for path in sorted((source/'raw').glob('*-time.json')):
        config=read(path)
        if set(config['methods'])=={'a','b'}:continue
        timed[(config['case']['id'],config['lifecycle'])]=read(path.with_name(path.stem+'-output.json'))
    for path in sorted((source/'raw').glob('*-first.json')):
        config=read(path);output=read(path.with_name(path.stem+'-output.json'))
        first[(config['case']['id'],config['lifecycle'],config['methods'][0])].append(output['ns'])
    raw=[];grouped=defaultdict(list)
    for path in sorted((source/'raw').glob('*.perf.txt')):
        config=read(path.with_suffix('').with_suffix('.json'))
        row={'sequence':path.stem,'case':config['case']['id'],'lifecycle':config['lifecycle'],
             'method':config['methods'][0],'iterations':config['iterations'],'perf_stat':path.read_text()}
        raw.append(row)
        grouped[(row['case'],row['lifecycle'],row['method'])].append(row)
    pairs={}
    for key,records in grouped.items():
        assert len(records)%2==0
        pairs[key]=[]
        for first_record,second_record in zip(records[::2],records[1::2]):
            by_count={r['iterations']:r for r in [first_record,second_record]}
            assert len(by_count)==2 and 0 in by_count
            count=max(by_count);a=events(by_count[0]['perf_stat']);b=events(by_count[count]['perf_stat'])
            pairs[key].append({'iterations':count,'sample':{name:(b[name]-a[name])/count for name in a}})
    checked=0
    for row in original['rows']:
        case=cases[row['case']]
        assert row['time']==timed[(row['case'],row['lifecycle'])],('Raw elapsed-time mismatch',row['case'])
        for method,values in row['fresh_process_first_request_ns'].items():
            assert values==first[(row['case'],row['lifecycle'],method)],('Raw first-request mismatch',row['case'],method)
        cycle_sink=0
        for job in case['jobs']:
            for document in job['documents']:
                value=document['expected']
                if case['operation']=='replace':cycle_sink+=len(value['text'].encode())
                elif isinstance(value,list):cycle_sink+=len(value)
                else:cycle_sink+=int(value)
        expected_sink=sum(row['time']['iterations'].values())//len(case['jobs'])*cycle_sink*meta['protocol']['passes']
        assert row['time']['sink']==expected_sink,('Repeated-call output-size/count mismatch',row['case'])
        for method in row['methods']:
            assert len(row['time']['ns_per_job'][method])==meta['protocol']['passes']
            assert row['time']['iterations'][method]%len(case['jobs'])==0
            record=row['counters'][method]
            assert len(record['samples'])==meta['protocol']['perf_passes']
            assert record['iterations']%len(case['jobs'])==0
            available=pairs[(row['case'],row['lifecycle'],method)]
            needle=[{'iterations':record['iterations'],'sample':sample}for sample in record['samples']]
            assert any(available[i:i+len(needle)]==needle for i in range(len(available)-len(needle)+1)),('Raw correction mismatch',stem,compiler,row['case'],method)
            checked+=len(needle)
        assert all(len(values)==meta['protocol']['first_requests']for values in row['fresh_process_first_request_ns'].values())
    assert len(original['aa'])==4
    assert all(abs(a['median_ratio']-1)<=0.02 for a in original['aa'])
    exported=public(original)
    exported['metadata']['path_note']='Machine-local paths and hostname are replaced with placeholders; measured samples and hashes are unchanged.'
    output_prefix=''if stem=='product'else'size-'
    files={output_prefix+compiler+'.json':exported,output_prefix+compiler+'-perf.json':raw}
    audit={'series':stem,'compiler':compiler,'source_result_sha256':digest(source/'results.json'),
           'rows':len(original['rows']),'method_lifecycle_cells':sum(len(r['methods'])for r in original['rows']),
           'raw_counter_processes':len(raw),'corrected_counter_samples_verified':checked,
           'output_comparisons':sum(c['comparisons']for c in original['checks'])}
    return files,audit


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('directory',type=Path);args=parser.parse_args()
    files={};audit=[]
    for stem,corpus in [('product','multi-pattern-product'),('size','multi-pattern-scaling')]:
        for cc in ['gcc15','clang21']:
            additions,checks=capture(args.directory,corpus,stem,cc);files.update(additions);audit.append(checks)
    destination=ROOT/'data';destination.mkdir(exist_ok=True)
    for name,value in files.items():(destination/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
    (destination/'capture-audit.json').write_text(json.dumps(audit,indent=2)+'\n')
    print('CAPTURE PASS',len(audit),'complete series,',sum(a['corrected_counter_samples_verified']for a in audit),'raw-verified corrected counter samples')


if __name__=='__main__':main()
