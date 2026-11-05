#!/usr/bin/env python3
"""Build and smoke-check the measured extension snapshot against a release PHP build."""
from pathlib import Path
import argparse,json,subprocess,hashlib,shlex
p=argparse.ArgumentParser();p.add_argument('--php-build',type=Path,required=True);p.add_argument('--compiler',required=True);p.add_argument('--label',choices=['gcc15','clang21'],required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--cpu',type=int,required=True);p.add_argument('--smt-sibling',type=int,required=True);args=p.parse_args();root=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
source=root/'extension/strmatch.c';pin=json.loads((root/'data/source.json').read_text());assert sha(source)==pin['source_sha256']
flags=json.loads((root/'data/build-flags.json').read_text())[args.label]['module_flags'];php_build=args.php_build.resolve();php=php_build/'sapi/cli/php';output=args.output.resolve();output.parent.mkdir(parents=True,exist_ok=True)
cmd=[args.compiler,*flags]
for name in ['','main','TSRM','Zend']:cmd+=['-I'+str(php_build/name)]
cmd += [str(source),'-o',str(output)];print(shlex.join(cmd),flush=True);subprocess.run(cmd,check=True,timeout=120)
code='if (PHP_DEBUG) { fwrite(STDERR, "Release PHP required\\n"); exit(1); } if (!(new Str\\Matcher(["x"]))->matches("x") || (new Str\\Replacer(["x"=>"y"]))->replace("x") !== "y") { exit(2); } echo "Module smoke PASS\\n";'
subprocess.run([str(php),'-n','-d','extension='+str(output),'-r',code],check=True,timeout=10)
config=root/'environment.json';env=json.loads(config.read_text()) if config.exists() else {};env[args.label]={'php':str(php),'module':str(output),'php_sha256':sha(php),'module_sha256':sha(output),'cpu':args.cpu,'smt_sibling':args.smt_sibling};config.write_text(json.dumps(env,indent=2)+'\n');print('Updated environment.json for',args.label,flush=True)
