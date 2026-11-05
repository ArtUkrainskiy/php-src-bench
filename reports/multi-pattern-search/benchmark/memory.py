from pathlib import Path
import subprocess,json,hashlib,statistics as st,fcntl
R=Path(__file__).resolve().parent;O=R/'memory';O.mkdir(exist_ok=True);I=json.loads((R/'index.json').read_text());B=json.loads((R/'environment.json').read_text());by={e['id']:e for e in I['cases']};lock=open(str(R/'.measure.lock'),'w');fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
ids=['results.unique.bytes4096.keys128.one','presence.any.bytes128.keys8.absent.rank5','presence.any.bytes4096.keys128.absent.rank65','example.articles.en.unique','presence.any.bytes65536.keys1024.absent.rank513','presence.any.bytes65536.keys10000.absent.rank5001'];records=[]
reps=json.loads((R/'replacer-index.json').read_text())['cases'];seen=set();repmaps=[]
for e in reps:
 c=json.loads((R/'inputs'/e['file']).read_text())['cases'][0];d=c['jobs'][0]['dictionary'];h=hashlib.sha256((json.dumps(d,ensure_ascii=False)+'\n').encode()).hexdigest()
 if h not in seen:seen.add(h);repmaps.append(e)
for cc,b in B.items():
 for e in [by[id] for id in ids]+repmaps:
  id=e['id']
  cls='Str\\Replacer' if e in repmaps else 'Str\\Matcher';c=json.loads((R/'inputs'/e['file']).read_text())['cases'][0];d=c['jobs'][0]['dictionary'];raw=(json.dumps(d,ensure_ascii=False)+'\n').encode();sha=hashlib.sha256(raw).hexdigest();dp=O/(sha+'.json');dp.write_bytes(raw);record={'compiler':cc,'class':cls,'case':id,'dictionary_sha256':sha,'module_sha256':b['module_sha256'],'observations':[]}
  for mode in ['constructor_time']+['construction_memory']*5:
   conf={'mode':mode,'class':cls,'dictionary_path':str(dp),'dictionary_file_sha256':sha};cp=O/f'{cc}-{id}-{mode}.config.json';cp.write_text(json.dumps(conf));cmd=['taskset','-c',str(b['cpu']),b['php'],'-n','-d','extension='+b['module'],str(R/'memory_time.php'),str(cp)];q=subprocess.run(cmd,capture_output=True,text=True,timeout=30);assert not q.returncode,q.stderr
   result=json.loads(q.stdout)
   if mode=='constructor_time':record['constructor']=result['result']
   else:record['observations'].append(result['result'])
  records.append(record);(O/'results.json').write_text(json.dumps(records,indent=2)+'\n');print('memory',cc,id,flush=True)

for cc,b in B.items():
 cmd=['taskset','-c',str(b['cpu']),b['php'],'-n','-d','extension='+b['module'],str(R/'replace-memory.php')];q=subprocess.run(cmd,capture_output=True,text=True,timeout=120);assert not q.returncode,q.stderr;(O/('replace-query-'+cc+'.json')).write_text(q.stdout);print('query memory',cc,str(len(reps))+' cases',flush=True)
(R/'memory-done.json').write_text(json.dumps({'status':'complete','records':len(records)})+'\n')
