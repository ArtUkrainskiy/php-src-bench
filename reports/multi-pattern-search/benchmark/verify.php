<?php
set_error_handler(static function($n,$m){throw new ErrorException($m);});
$root=__DIR__; $index=json_decode(file_get_contents($root.'/index.json'),true,512,JSON_THROW_ON_ERROR);$n=0;
foreach($index['cases'] as $entry){
 $path=$root.'/inputs/'.$entry['file'];if(hash_file('sha256',$path)!==$entry['sha256'])throw new RuntimeException('Hash mismatch');
 $c=json_decode(file_get_contents($path),true,512,JSON_THROW_ON_ERROR)['cases'][0];$job=$c['jobs'][0];$doc=$job['documents'][0];$obj=new Str\Matcher($job['dictionary']);
 $method=['any'=>'matches','unique'=>'getMatchedKeywords','count'=>'countMatches','all'=>'matchAll'][$c['operation']];$actual=$obj->$method($doc['text']);
 if($c['operation']==='all')$actual=array_map(static fn($h)=>['offset'=>$h->offset,'length'=>$h->length,'keyword'=>$h->keyword],$actual);
 if($actual!==$doc['expected'])throw new RuntimeException('Mismatch '.$entry['id']);
 unset($obj,$actual,$c,$job,$doc);$n++;
}
echo json_encode(['status'=>'PASS','cases'=>$n,'php'=>PHP_VERSION,'debug'=>PHP_DEBUG]),"\n";
