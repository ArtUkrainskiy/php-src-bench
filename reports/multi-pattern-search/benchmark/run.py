from pathlib import Path
import json,subprocess,hashlib,time,statistics as st,fcntl,sys,math,datetime
R=Path(__file__).resolve().parent;I=json.loads((R/'index.json').read_text());B=json.loads((R/'environment.json').read_text());H=R/'reports/multi-pattern-search/harness.php';O=R/'captures';O.mkdir(exist_ok=True)
phase=sys.argv[1] if len(sys.argv)>1 else 'smoke';lock=open(str(R/'.measure.lock'),'w');fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
def write(p,x):
 p=Path(p);q=p.with_suffix(p.suffix+'.tmp');q.write_text(json.dumps(x,indent=2)+'\n');q.replace(p)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def cpu():
 v=list(map(int,next(s for s in Path('/proc/stat').read_text().splitlines() if s.startswith('cpu'+str(B['gcc15']['smt_sibling'])+' ')).split()[1:9]));return sum(v),v[3]+v[4]
for cc,b in B.items():
 assert sha(b['module'])==b['module_sha256'];assert sha(b['php'])==b['php_sha256']
assert sha(R/'extension/strmatch.c')=='c4cece7e7a4f5952caae5609b9bc607408427c1fe006e47f59d7fdc0cc0946b3'
def run(e,cc,scope,tag,mode='time',passes=15,iterations=0,methods=None,batch=1,mutation=False):
 b=B[cc];p=R/'inputs'/e['file'];assert sha(p)==e['sha256'];methods=methods or {m:m for m in e['methods']}
 if mode=='time':
  proto='replacer' if e['operation']=='replace' else 'matcher';methods={**methods,proto+'_aa':proto}
 config={'case_path':str(p),'case_sha256':e['sha256'],'scope':scope,'mode':mode,'methods':methods,'batch':batch,'passes':passes,'warmup_ns':100000000 if passes==15 else 10000000,'sample_ns':40000000 if passes==15 else 10000000,'chunk_keys':512,'iterations':iterations,'mutation':mutation};cp=O/f'{tag}.config.json';write(cp,config)
 cmd=['taskset','-c',str(b['cpu']),b['php'],'-n','-d','pcre.jit=1','-d','opcache.enable_cli=0','-d','opcache.jit=0','-d','extension='+b['module'],str(H),str(cp)]
 if mode=='perf':cmd=['perf','stat','-x',';','-e','cycles:u,instructions:u,context-switches,cpu-migrations','--']+cmd
 a=cpu();start=time.monotonic();q=subprocess.run(cmd,capture_output=True,text=True,timeout=120);z=cpu();busy=100*(1-(z[1]-a[1])/max(1,z[0]-a[0]));x={'compiler':cc,'case':e['id'],'scope':scope,'batch':batch,'mode':mode,'returncode':q.returncode,'elapsed_s':time.monotonic()-start,'sibling_busy_percent':busy,'command':cmd,'stdout':q.stdout,'stderr':q.stderr,'case_sha256':e['sha256'],'module_sha256':b['module_sha256'],'php_sha256':b['php_sha256'],'harness_sha256':sha(H),'timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 if q.returncode==0:x['result']=json.loads(q.stdout)
 write(O/f'{tag}.json',x);return x

def summary(x):
 samples=x['result']['ns_per_job'];proto='matcher' if 'matcher' in samples else 'replacer';aa=100*(st.median(b/a for a,b in zip(samples[proto],samples[proto+'_aa']))-1);flags=[]
 if abs(aa)>2:flags.append('aa-outside-2-percent')
 if x['sibling_busy_percent']>2:flags.append('smt-load')
 spread=[m for m,v in samples.items() if max(abs(z/st.median(v)-1) for z in v)>.05]
 if spread:flags.append('spread:'+','.join(spread))
 return {'compiler':x['compiler'],'case':x['case'],'scope':x['scope'],'batch':x['batch'],'samples':samples,'median_us':{m:st.median(v)/1000 for m,v in samples.items()},'aa_percent':aa,'flags':flags,'qualified':not flags,'raw':str(Path(x['command'][-1]).with_suffix('.json').name).replace('.config.json','.json'),'module_sha256':x['module_sha256']}
entries=[e for e in I['cases'] if e['measure']]
if phase not in ['check','smoke','pilot']:
 e=next(e for e in json.loads((R/'replacer-index.json').read_text())['cases'] if e['id']=='single.b16384.keybytes24.hits1');c=json.loads((R/'inputs'/e['file']).read_text())['cases'][0];entries.append({**e,'operation':'replace','methods':c['methods']+['preg_replace','preg_trie_constant','preg_chunked_constant']})
if phase=='check':
 for cc,b in B.items():
  cmd=['taskset','-c',str(b['cpu']),b['php'],'-n','-d','extension='+b['module'],str(R/'verify.php')];q=subprocess.run(cmd,capture_output=True,text=True,timeout=120);write(R/f'check-{cc}.json',{'command':cmd,'module_sha256':b['module_sha256'],'returncode':q.returncode,'stdout':q.stdout,'stderr':q.stderr});assert q.returncode==0,q.stderr;print(cc,q.stdout.strip(),flush=True)
 exit()
if phase=='smoke':
 e=next(e for e in entries if e['id']=='results.count.bytes16384.keys128.one')
 for cc in B:
  for scope in ['prepared','oneshot']:
   x=run(e,cc,scope,f'smoke-{cc}-{scope}',passes=2);assert not x['returncode'],x['stderr'];print(cc,scope,'smoke',x['elapsed_s'],flush=True)
  x=run(e,cc,'prepared',f'mutation-{cc}',mode='check',methods={'matcher':'matcher'},mutation=True);assert x['returncode']!=0
 exit()
if phase=='pilot':entries=[e for e in entries if e['id']=='results.count.bytes16384.keys128.one']
points=[]
for cc in B:
 for e in entries:
  for scope in ['prepared','oneshot']:points.append((cc,e,scope,1))
for cc in ([] if phase=='pilot' else B):
 for id in ['presence.any.bytes128.keys128.absent.rank65','presence.any.bytes4096.keys128.absent.rank65','results.unique.bytes4096.keys128.sparse','results.all.bytes65536.keys1024.sparse']:
  e=next(e for e in entries if e['id']==id)
  for batch in [4,16,64]:points.append((cc,e,'oneshot',batch))
if phase in ['time','pilot']:
 for i,(cc,e,scope,batch) in enumerate(points):
  tag=f'{cc}-{e["id"]}-{scope}-b{batch}';out=O/f'{tag}-summary.json'
  if out.exists():continue
  attempts=[];chosen=None
  for attempt in range(1,3):
   x=run(e,cc,scope,f'{tag}-a{attempt}',batch=batch);assert x['returncode']==0,x['stderr'];v=summary(x);attempts.append(v);chosen=chosen or v
   if v['qualified']:chosen=v;break
  chosen={**chosen,'attempts':[{'raw':v['raw'],'flags':v['flags'],'qualified':v['qualified']} for v in attempts]};write(out,chosen);write(R/'status.json',{'phase':phase,'point':i+1,'points':len(points),'compiler':cc,'case':e['id'],'scope':scope,'batch':batch,'flags':chosen['flags'],'timestamp':time.time()});print(i+1,'/',len(points),cc,e['id'],scope,batch,'flags',chosen['flags'],flush=True)
 write(R/(phase+'-done.json'),{'status':'complete','points':len(points)});exit()
if phase=='counters':
 points=[p for p in points if p[3]==1]
 for i,(cc,e,scope,batch) in enumerate(points):
  tag=f'{cc}-{e["id"]}-{scope}-b1';out=O/f'{tag}-counters.json'
  if out.exists():continue
  timed=json.loads((O/f'{tag}-summary.json').read_text());results={}
  for m in e['methods']:
   median=timed['median_us'][m]
   if median>100000:
    results[m]={'status':'not-captured','reason':'Over 100 ms/call; elapsed observations retained'};continue
   n=max(1,math.ceil(60000/median));pairs=[]
   for rnd in range(5):
    raw={}
    for count in ([0,n] if rnd%2==0 else [n,0]):
     x=run(e,cc,scope,f'perf-{tag}-{m}-r{rnd}-n{count}',mode='perf',iterations=count,methods={m:m});assert not x['returncode'],x['stderr'];values={};available=True
     for l in x['stderr'].splitlines():
      f=l.split(';')
      if len(f)>2 and f[2] in ['cycles:u','instructions:u','context-switches','cpu-migrations']:
       values[f[2]]=float(f[0]);available=available and not (f[2].endswith(':u') and len(f)>4 and f[4] and float(f[4])<99)
     assert all(k in values for k in ['cycles:u','instructions:u']),x['stderr'];raw[count]={'counts':values,'sibling_busy_percent':x['sibling_busy_percent'],'available':available}
    corrected={k:(raw[n]['counts'][k]-raw[0]['counts'][k])/n for k in ['cycles:u','instructions:u']};pairs.append({'per_call':corrected,'raw':raw,'valid':all(z>0 for z in corrected.values()) and all(q['available'] and q['sibling_busy_percent']<=2 for q in raw.values())})
   results[m]={'iterations':n,'pairs':pairs,'median':{k:st.median(p['per_call'][k] for p in pairs) for k in ['cycles:u','instructions:u']}}
  write(out,{'compiler':cc,'case':e['id'],'scope':scope,'module_sha256':B[cc]['module_sha256'],'methods':results});write(R/'counter-status.json',{'point':i+1,'points':len(points),'compiler':cc,'case':e['id'],'scope':scope});print('counters',i+1,'/',len(points),flush=True)
 write(R/'counters-done.json',{'status':'complete','points':len(points)});exit()
raise RuntimeError('Unknown phase')
