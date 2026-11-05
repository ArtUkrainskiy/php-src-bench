<?php
set_error_handler(static function($n,$m){throw new ErrorException($m);});
$root=__DIR__; $index=json_decode(file_get_contents($root.'/replacer-index.json'),true,512,JSON_THROW_ON_ERROR);$n=0;
foreach($index['cases'] as $entry){
 $path=$root.'/inputs/'.$entry['file'];if(hash_file('sha256',$path)!==$entry['sha256'])throw new RuntimeException('Hash mismatch');
 $c=json_decode(file_get_contents($path),true,512,JSON_THROW_ON_ERROR)['cases'][0];$job=$c['jobs'][0];$doc=$job['documents'][0];$obj=new Str\Replacer($job['dictionary']);$count=null;$actual=$obj->replace($doc['text'],$count);
 if($actual!==$doc['expected']['text']||$count!==$doc['facts']['selected_matches'])throw new RuntimeException('Mismatch '.$entry['id']);
 if(strtr($doc['text'],$job['dictionary'])!==$actual)throw new RuntimeException('strtr mismatch '.$entry['id']);
 unset($obj,$actual,$c,$job,$doc);$n++;
}
echo json_encode(['status'=>'PASS','cases'=>$n,'php'=>PHP_VERSION,'debug'=>PHP_DEBUG]),"\n";
