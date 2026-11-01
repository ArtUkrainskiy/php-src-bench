#!/usr/bin/env python3
"""Render operation-specific tables from complete product and dictionary-size series."""
import argparse
import hashlib
import json
from pathlib import Path
import statistics
import subprocess
import sys

ROOT=Path(__file__).resolve().parent
COMPILERS=['gcc15','clang21']
SIZES=[8,16,32,64,128,256,512]
LABELS={'contains_loop':'str_contains() loop','preg_match':'preg_match()',
        'strtr':'strtr()','str_replace':'str_replace()',
        'preg_replace':'preg_replace()','preg_replace_callback':'preg_replace_callback()',
        'strpos_unique':'strpos() per term','strpos_count':'strpos() per term',
        'strpos_all':'strpos() per term','preg_each_unique':'preg_match() per term',
        'preg_each_count':'PCRE lookahead per term','preg_each_all':'PCRE lookahead per term'}
MODE_LABEL={'request':'Dictionary preparation included','worker':'Dictionary already prepared'}
MATCH_LABEL={'absent':'No match','start':'Match at start','middle':'Match in body',
             'end':'Match near end','quoted':'Quoted matching term','mixed':'Mixed matches'}


def load(name,corpus,stem):
    directory=(ROOT/'../../corpus'/corpus).resolve()
    index=json.loads((directory/'index.json').read_text())
    cases={case['id']:{**case,'file':filename} for filename in index['suite_sha256'] for case in json.loads((directory/filename).read_text())['cases']}
    data={cc:json.loads((ROOT/'data'/f'{stem}{cc}.json').read_text()) for cc in COMPILERS}
    digest=hashlib.sha256((directory/'index.json').read_bytes()).hexdigest()
    expected={(c['id'],mode['id']) for c in cases.values() for mode in c['lifetime']['modes']}
    rows={cc:{(r['case'],r['lifecycle']):r for r in d['rows']} for cc,d in data.items()}
    for cc,d in data.items():
        assert d['status']=='complete' and set(rows[cc])==expected
        assert d['metadata']['corpus_index_sha256']==digest
    return {'name':name,'corpus':corpus,'index':index,'cases':cases,'data':data,'rows':rows}


def median(values):return statistics.median(values)
def ext(row):return 'matcher' if 'matcher' in row['methods'] else 'replacer'
def label(method):return LABELS.get(method,method)
def samples(row,method,metric):
    return row['time']['ns_per_job'][method] if metric=='time' else [s[metric] for s in row['counters'][method]['samples']]
def delta(a,b):return [(y/x-1)*100 for x,y in zip(a,b)]
def count(case):return len(case['jobs'][0]['dictionary'])
def case_link(ds,case):
    name={'order.email':'Order confirmation email',
          'order.email-pair':'Order confirmation in HTML and plain text'}.get(case['id'],case['title'])
    return f"[{name}](../../corpus/{ds['corpus']}/{case['file']})"
def span(values):return str(min(values)) if min(values)==max(values) else f'{min(values)}–{max(values)}'


def full(datasets,metric,heading,unit):
    lines=[f'# {heading}','',f'Unit: {unit} per complete job. Lower is better. Δ is the median of paired per-pass changes; min/max are paired changes, not confidence intervals.','',
           'All measured alternatives are listed. Preparation and reuse are separate sections. Natural API result representations are retained; see [method](METHOD.md).','']
    if metric=='time':lines += ['A dagger marks an original sample span above 10%; the [complete-case confirmation](CONFIRMATION.md) preserves both measurements.','']
    for ds in datasets:
        lines += [f"## {ds['name']}",'']
        for kind in dict.fromkeys(c['kind'] for c in ds['cases'].values()):
            lines += [f'### {kind.capitalize()} tasks','']
            for mode in ['request','worker']:
                lines += ['#### '+MODE_LABEL[mode],'']
                for cc in COMPILERS:
                    lines += [f'##### {cc}','', '| Task | Substrings | Existing method | Existing | Prototype | Δ | Min Δ | Max Δ |','|---|---:|---|---:|---:|---:|---:|---:|']
                    for row in ds['data'][cc]['rows']:
                        if row['kind']!=kind or row['lifecycle']!=mode:continue
                        c=ds['cases'][row['case']]
                        for method in row['methods']:
                            if method==ext(row):continue
                            a=samples(row,method,metric);b=samples(row,ext(row),metric);d=delta(a,b)
                            divisor=1000 if metric=='time' else 1;digits=3 if metric=='time' else 1
                            a_mark='†'if metric=='time'and max(a)/min(a)>1.1 else''
                            b_mark='†'if metric=='time'and max(b)/min(b)>1.1 else''
                            task=case_link(ds,c)
                            if c.get('scaling',{}).get('group')=='moderation':
                                task+=' ('+MATCH_LABEL[c['scaling']['match']]+')'
                            lines.append(f'| {task} | {count(c)} | {label(method)} | {median(a)/divisor:.{digits}f}{a_mark} | {median(b)/divisor:.{digits}f}{b_mark} | {median(d):+.1f}% | {min(d):+.1f}% | {max(d):+.1f}% |')
                    lines += ['']
    return '\n'.join(lines)


def product_tables(ds):
    lines=['# Everyday application cases','',
           'All times are microseconds per complete job. String count, documents per job and preparation are shown separately. “Prototype” is Matcher for searches and Replacer for substitutions.','',
           'The existing reference is fixed across compilers; all alternatives and paired changes are in [full time results](FULL-TIME.md). These tasks have different dictionaries and inputs; their keyword counts do not define a size crossover.','']
    for family,operations in [('Presence checks',{'any'}),('Search results',{'unique','count','all'}),('Literal replacement',{'replace'})]:
        lines += [f'## {family}','']
        for mode in ['request','worker']:
            lines += ['### '+MODE_LABEL[mode],'','| Task | Substrings | Documents | Existing method | Existing GCC | Prototype GCC | Existing Clang | Prototype Clang |','|---|---:|---:|---|---:|---:|---:|---:|']
            for c in ds['cases'].values():
                if c['kind']!='product' or c['operation']not in operations or (c['id'],mode)not in ds['rows']['gcc15']:continue
                row=ds['rows']['gcc15'][(c['id'],mode)]
                method={'any':'contains_loop','replace':'strtr','unique':'strpos_unique','count':'strpos_count','all':'strpos_all'}[c['operation']]
                cells=[]
                for cc in COMPILERS:
                    r=ds['rows'][cc][(c['id'],mode)]
                    cells += [f'{median(samples(r,method,"time"))/1000:.3f}',f'{median(samples(r,ext(r),"time"))/1000:.3f}']
                lines.append(f'| {case_link(ds,c)} | {count(c)} | {len(c["jobs"][0]["documents"])} | {label(method)} | '+' | '.join(cells)+' |')
            lines += ['']
    return '\n'.join(lines)


def matrix(ds,ids,methods,names):
    lines=['| Substrings | '+ ' | '.join(f'{cc} {name}' for cc in ['GCC','Clang'] for name in names)+' |', '|---:|'+ '|'.join('---:'for _ in range(6))+'|']
    for n in SIZES:
        cid,mode=ids(n);cells=[]
        for cc in COMPILERS:
            row=ds['rows'][cc][(cid,mode)]
            values=[median(samples(row,method,'time'))/1000 for method in methods]
            for method,value in zip(methods,values):
                cell=f'{value:.3f}'
                cell='**'+cell+'**' if value==min(values) else cell
                cells.append(cell+('†'if max(samples(row,method,'time'))/min(samples(row,method,'time'))>1.1 else''))
        lines.append(f'| {n} | '+' | '.join(cells)+' |')
    return '\n'.join(lines)


def size_section(ds,prefix,methods,names):
    lines=[]
    for mode in ['request','worker']:
        lines += ['### '+MODE_LABEL[mode],'',matrix(ds,lambda n:(prefix+str(n),mode),methods,names),'']
    return '\n'.join(lines)


def size_files(ds):
    common='Times are microseconds per complete job; lower is better. Bold marks the lowest median per compiler, not a significance test. GCC 15.2 and Clang 21.1 on the same AMD system. PCRE compilation caches are warm in these tables; first requests are [separate](PCRE-FIRST.md). Exact input dictionaries and expected outputs are saved in the [corpus](../../corpus/multi-pattern-scaling/README.md).\n\n'
    common+='A dagger marks the one noisy original PCRE cell; its [complete-case confirmation](CONFIRMATION.md) preserves the original and repeat measurements.\n\n'
    moderation='# Moderation: find any configured substring\n\n'+common
    moderation+='`Loop` is early-exit `str_contains()`. `PCRE` is a single escaped `preg_match()` alternation. Matcher returns the same boolean. English texts are fixed across every N.\n\n'
    for length,state,title in [('short','absent','Short comments, no match'),('short','start','Short comments, match at the start'),('short','middle','Short comments, match in the body'),('short','end','Short comments, match near the end'),('message','absent','Detailed support messages, no match'),('message','quoted','Detailed support messages, quoted matching term')]:
        moderation+='## '+title+'\n\n'+size_section(ds,f'scale.moderation.{length}.{state}.',['contains_loop','preg_match','matcher'],['loop','PCRE','Matcher'])+'\n'
    search='# Search: return matching keys, counts or positions\n\n'+common
    search+='The same eight commerce help articles are used at every N. `PHP` searches each literal with `strpos()`. `PCRE` searches each literal separately to preserve nested/overlapping matches; this is an exact reference, not a claim of an optimal regex implementation. The number of matched terms grows with the dictionary and is reported below.\n\n'
    for op,title in [('unique','Distinct matching terms'),('count','Count every overlapping occurrence'),('all','Return every occurrence and byte location')]:
        search+='## '+title+'\n\n'+size_section(ds,f'scale.search.{op}.', ['strpos_'+op,'preg_each_'+op,'matcher'],['PHP','PCRE','Matcher'])+'\n'
    replacement='# Replacement: add links to support terms\n\n'+common
    replacement+='`strtr` is the native map function. `PCRE` is longest-first escaped `preg_replace_callback()`. Replacer has the same leftmost-longest, no-rescan policy. Sequential `str_replace()` would change the result and is excluded.\n\n'
    for batch,title in [(1,'One help article'),(8,'A publishing job with eight different help articles')]:
        replacement+='## '+title+'\n\n'+size_section(ds,f'scale.replace.articles{batch}.',['strtr','preg_replace_callback','replacer'],['strtr','PCRE','Replacer'])+'\n'
    for family,text in [('moderation',moderation),('search',search),('replacement',replacement)]:
        result_label={'moderation':'Literal occurrences','search':'Distinct terms','replacement':'Replacements'}[family]
        text+='## Input sizes and results\n\nString bytes are UTF-8 lengths; total string bytes sum the dictionary literals, not engine memory.\n\n'
        text+='| Substrings | Input | Bytes per substring | Total literal bytes | Bytes per document | '+result_label+' |\n|---:|---|---:|---:|---:|---:|\n'
        for n in SIZES:
            for c in ds['cases'].values():
                s=c.get('scaling',{})
                if s.get('group')!=family or s['needles']!=n:continue
                if family=='search' and s['result']!='unique':continue
                if family=='replacement' and s['documents_per_job']!=1:continue
                docs=[d for j in c['jobs']for d in j['documents']]
                field={'moderation':'occurrences','search':'distinct_keywords','replacement':'selected_matches'}[family]
                counts=[d['facts'][field] for d in docs]
                words=c['jobs'][0]['dictionary']
                lengths=[len(word.encode()) for word in words]
                name=c['title']+(' ('+MATCH_LABEL[s['match']]+')' if family=='moderation' else '')
                text+=f'| {n} | {name} | {span(lengths)} | {sum(lengths)} | {span([d["facts"]["bytes"]for d in docs])} | {span(counts)} |\n'
        if family=='moderation':moderation=text
        elif family=='search':search=text
        else:replacement=text
    main={
        'SCALE-MODERATION':size_section(ds,'scale.moderation.short.absent.',['contains_loop','preg_match','matcher'],['loop','PCRE','Matcher']),
        'SCALE-SEARCH':size_section(ds,'scale.search.unique.',['strpos_unique','preg_each_unique','matcher'],['PHP','PCRE','Matcher']),
        'SCALE-REPLACEMENT':size_section(ds,'scale.replace.articles1.',['strtr','preg_replace_callback','replacer'],['strtr','PCRE','Replacer']),
    }
    return {'MODERATION.md':moderation,'SEARCH.md':search,'REPLACEMENT.md':replacement},main


def controls(datasets):
    lines=['| Series | Compiler | Stage | Control | Time Δ | Cycles Δ | Instructions Δ |','|---|---|---|---|---:|---:|---:|']
    for ds in datasets:
        for cc,d in ds['data'].items():
            for aa in d['aa']:
                fields=[]
                for event in ['cycles:u','instructions:u']:
                    fields.append(f'{median(delta([s[event]for s in aa["counter_a"]],[s[event]for s in aa["counter_b"]])):+.3f}%')
                control='Short presence check' if aa['case']=='moderation.en.clean' else 'Large log replacement'
                lines.append(f'| {ds["name"]} | {cc} | {aa["stage"]} | {control} | {(aa["median_ratio"]-1)*100:+.3f}% | '+' | '.join(fields)+' |')
    return '\n'.join(lines)


def first_requests(datasets):
    lines=['# PCRE first requests and warm-cache requests','',
           'All times are microseconds per complete job. Warm requests still build pattern strings and request-owned state. First requests run in fresh processes, with PHP startup outside the timer. They include first-use effects, preparation, query and release. These are not pure compilation measurements and are not paired with the warm-cache samples.','']
    for ds in datasets:
        lines += [f'## {ds["name"]}','']
        for cc,d in ds['data'].items():
            lines += [f'### {cc}','','| Task | Substrings | PCRE method | Warm median | First median | First min | First max |','|---|---:|---|---:|---:|---:|---:|']
            for row in d['rows']:
                if row['kind']!='product':continue
                c=ds['cases'][row['case']]
                task=case_link(ds,c)
                if c.get('scaling',{}).get('group')=='moderation':task+=' ('+MATCH_LABEL[c['scaling']['match']]+')'
                for method,values in row['fresh_process_first_request_ns'].items():
                    lines.append(f'| {task} | {count(c)} | {label(method)} | {median(samples(row,method,"time"))/1000:.3f} | {median(values)/1000:.3f} | {min(values)/1000:.3f} | {max(values)/1000:.3f} |')
            lines += ['']
    return '\n'.join(lines)


def winners(ds):
    lines=['| Task | Preparation included: tested N | Prepared dictionary: tested N |','|---|---|---|']
    for name,prefix in [('Moderation, no match','scale.moderation.short.absent.'),('Distinct support terms','scale.search.unique.'),('Link one article','scale.replace.articles1.'),('Link eight articles','scale.replace.articles8.')]:
        cells=[]
        for mode in ['request','worker']:
            passed=[]
            for n in SIZES:
                rows=[ds['rows'][cc][(prefix+str(n),mode)]for cc in COMPILERS]
                if all(all(median(delta(samples(r,m,'time'),samples(r,ext(r),'time')))<0 for m in r['methods']if m!=ext(r))for r in rows):passed.append(str(n))
            cells.append(', '.join(passed) if passed else 'None')
        lines.append('| '+name+' | '+' | '.join(cells)+' |')
    return '\n'.join(lines)


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args()
    product=load('Everyday cases','multi-pattern-product','');datasets=[product]
    scale=None
    if all((ROOT/'data'/f'size-{cc}.json').exists()for cc in COMPILERS):
        scale=load('Size series','multi-pattern-scaling','size-');datasets.append(scale)
    files={'FULL-TIME.md':full(datasets,'time','Complete elapsed-time comparisons','µs'),
           'FULL-CYCLES.md':full(datasets,'cycles:u','Complete CPU-cycle comparisons','cycles'),
           'FULL-INSTRUCTIONS.md':full(datasets,'instructions:u','Complete instruction comparisons','instructions'),
           'PCRE-FIRST.md':first_requests(datasets),'PRODUCT-CASES.md':product_tables(product)}
    current_hash=hashlib.sha256((ROOT/'harness.php').read_bytes()).hexdigest()
    refreshed=scale is not None and all(d['metadata']['harness_sha256']==current_hash for ds in datasets for d in ds['data'].values())
    status=('Both compilers × both corpora on this AMD machine are complete and use the shared-dictionary input policy.' if refreshed else
            '**Measurement refresh in progress.** The earlier application tables are being replaced after correcting dictionary sharing. The report is not yet final.')
    blocks={'PRODUCT-TABLE':'See the [separate everyday application tables](PRODUCT-CASES.md).','AA-TABLE':controls(datasets),'RUN-STATUS':status}
    if scale:
        additional,matrices=size_files(scale);files.update(additional);blocks.update(matrices);blocks['SIZE-CHOICE']=winners(scale)
    else:
        for marker in ['SCALE-MODERATION','SCALE-SEARCH','SCALE-REPLACEMENT','SIZE-CHOICE']:
            blocks[marker]='Measurements for 8–512 strings are in progress on the AMD system; no values have been inferred from the earlier product cases.'
        for filename,heading in [('MODERATION.md','Moderation: find any substring'),('SEARCH.md','Search results'),('REPLACEMENT.md','Literal replacement')]:
            files[filename]='# '+heading+'\n\nThe controlled 8–512-string measurements are in progress on the AMD system. Results will be rendered from completed series.\n'
    readme=(ROOT/'README.md').read_text()
    for marker,table in blocks.items():
        start=f'<!-- {marker} -->';end=f'<!-- /{marker} -->'
        if start not in readme:continue
        left,tail=readme.split(start,1);_,right=tail.split(end,1)
        readme=left+start+'\n'+table+'\n'+end+right
    files['README.md']=readme
    for name,text in files.items():
        if not text.endswith('\n'):text+='\n'
        path=ROOT/name
        if args.check:assert path.exists()and path.read_text()==text,'Stale rendering: '+name
        elif not path.exists()or path.read_text()!=text:path.write_text(text)
    print('Rendered tables PASS'if args.check else'Rendered operation-specific tables')
    if (ROOT/'data/memory-gcc15.json').exists() and (ROOT/'data/memory-clang21.json').exists():
        command=[sys.executable,str(ROOT/'memory/render.py')]
        if args.check:command.append('--check')
        subprocess.run(command,check=True)


if __name__=='__main__':main()
