#!/usr/bin/env python3
"""Generate a controlled dictionary-size extension without changing the product corpus."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
BASE=ROOT.parent/'multi-pattern-product'
spec=importlib.util.spec_from_file_location('product_generator',BASE/'generate.py')
g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)
SIZES=[8,16,32,64,128,256,512]


def spread_core(words, size):
    keys=words[:size]
    slots={i*(size-1)//7:keys[i] for i in range(8)}
    rest=iter(keys[8:])
    return [slots[i] if i in slots else next(rest) for i in range(size)]


def add(suite, identifier, title, operation, description, jobs, size, **details):
    g.add(suite,identifier,title,operation,description,'fixed_policy',jobs)
    case=g.SUITES[suite][-1]
    case['scaling']={'needles':size,'language':'en',**details}
    return case


def build():
    g.SUITES={}
    words=json.loads((ROOT/'moderation-words.json').read_text())['words']
    terms=json.loads((ROOT/'support-terms.json').read_text())['words']
    assert len(words)==len(set(words))==512
    assert len(terms)==len(set(terms))==512
    seed=json.loads((BASE/'moderation-seed.json').read_text())['languages']['en']
    comments=[text for text in seed['messages'] if not g.occurrences(text,words)]
    posts=[text for text in seed['posts'] if not g.occurrences(text,words)]
    assert len(comments)>=8 and len(posts)>=3,(len(comments),len(posts))
    comments=comments[:8];posts=posts[:3]
    for n in SIZES:
        keys=spread_core(words,n)
        for state in ['absent','start','middle','end']:
            jobs=[]
            for i,text in enumerate(comments):
                term=words[i%8]
                if state=='start':text='"'+term+'" was the reply I received. '+text
                elif state=='middle':text=text+' The reply also said "'+term+'". '+comments[(i+3)%8]
                elif state=='end':text=text+' The word I want to report is "'+term+'".'
                assert bool(g.occurrences(text,keys))==(state!='absent')
                jobs.append(g.job(f'comment-{i+1}',keys,text))
            add('moderation',f'scale.moderation.short.{state}.{n}',
                'Check a short comment','any',
                'Same saved English comments at every size. '+state+' literal match. '
                'Nested rule sets; eight core rules distributed across dictionary ranks. No boundaries or case folding.',
                jobs,n,group='moderation',input='short comment',match=state)
        for state in ['absent','quoted']:
            jobs=[]
            for i,text in enumerate(posts):
                if state=='quoted':
                    first,rest=text.split('\n\n',1)
                    text=first+' The reply contained "'+words[(i*3)%8]+'".\n\n'+rest
                assert bool(g.occurrences(text,keys))==(state!='absent')
                jobs.append(g.job(f'message-{i+1}',keys,text))
            add('moderation',f'scale.moderation.message.{state}.{n}',
                'Check a detailed support message','any',
                'Same three separately authored support messages at every size; '+state+' match. '
                'Nested rule sets; literal bytes only.',jobs,n,group='moderation',input='support message',match=state)
        dictionary=terms[:n]
        for operation,label in [('unique','Find distinct support terms'),('count','Count support-term occurrences'),('all','Locate support-term occurrences')]:
            add('search',f'scale.search.{operation}.{n}',label,operation,
                'Same eight English help articles at every size; nested prefixes of one 512-term commerce glossary. '
                'All overlapping substring occurrences are preserved; result counts are recorded per document.',
                [g.job(f'article-{i+1}',dictionary,text) for i,text in enumerate(g.PAGES)],n,
                group='search',input='help article',match='mixed',result=operation)
        mapping={term:'<a href="https://help.example.test/topics/'+term.replace(' ','-')+'">'+term+'</a>' for term in dictionary}
        for batch in [1,8]:
            jobs=[g.job(f'article-{i+1}',mapping,text) for i,text in enumerate(g.PAGES)] if batch==1 else [g.job('publishing-batch',mapping,*g.PAGES)]
            add('replacement',f'scale.replace.articles{batch}.{n}',
                'Add support links to a help article' if batch==1 else 'Publish eight help articles',
                'replace','Same saved English help articles at every dictionary size; leftmost-longest links without rescanning inserted text. '
                'Sequential str_replace is not equivalent. The map is unchanged between jobs.',
                jobs,n,group='replacement',input='help article',match='mixed',documents_per_job=batch)
    # Ordinary saved inputs used only to keep A/A controls identical to the product series.
    for file,identifier in [('moderation.json','moderation.en.clean'),('secret-redaction.json','secrets.incident-batch')]:
        case=next(c for c in json.loads((BASE/'suites'/file).read_text())['cases'] if c['id']==identifier)
        case['kind']='control';case['primary']=False
        g.SUITES.setdefault('controls',[]).append(case)
    files=g.pack()
    index=json.loads(files['index.json'])
    index['control_cases']=2
    index['sizes']=SIZES
    index['scope']='Controlled English dictionary-size extension; original EN/RU/ZH product series remains separate.'
    files['index.json']=json.dumps(index,ensure_ascii=False,indent=2)+'\n'
    for family in ['moderation','search','replacement']:
        cases=g.SUITES[family]
        configs={}
        for case in cases:
            settings=dict(case['scaling']);settings.pop('needles')
            key=json.dumps(settings,sort_keys=True)
            texts=[d['text'] for j in case['jobs'] for d in j['documents']]
            if key in configs:assert configs[key]==texts,'Text changed across dictionary sizes'
            configs[key]=texts
    return files


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args()
    files=build()
    for name,text in files.items():
        path=ROOT/name
        if args.check:assert path.is_file() and path.read_text()==text,'Changed generated file: '+name
        else:path.parent.mkdir(exist_ok=True,parents=True);path.write_text(text)
    print('Scaling regeneration PASS' if args.check else 'Generated scaling corpus:',sum(len(v) for v in g.SUITES.values()),'cases')


if __name__=='__main__':main()
