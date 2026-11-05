<?php
set_error_handler(static function($n,$m){throw new ErrorException($m);});
$root=__DIR__;$entries=json_decode(file_get_contents($root.'/replacer-index.json'),true,512,JSON_THROW_ON_ERROR)['cases'];$out=[];
foreach($entries as $e){
 $path=$root.'/inputs/'.$e['file'];if(hash_file('sha256',$path)!==$e['sha256'])throw new RuntimeException('hash');
 $case=json_decode(file_get_contents($path),true,512,JSON_THROW_ON_ERROR)['cases'][0];$j=$case['jobs'][0];$d=$j['documents'][0];
 $before=memory_get_usage(false);memory_reset_peak_usage();$obj=new Str\Replacer($j['dictionary']);$object=memory_get_usage(false)-$before;$ctor=memory_get_peak_usage(false)-$before;
 $before=memory_get_usage(false);memory_reset_peak_usage();$result=$obj->replace($d['text']);$held=memory_get_usage(false)-$before;$peak=memory_get_peak_usage(false)-$before;
 if($result!==$d['expected']['text'])throw new RuntimeException('result');
 $out[]=['case'=>$e['id'],'object_extra_bytes'=>$object,'constructor_peak_extra_bytes'=>$ctor,'query_result_extra_bytes'=>$held,'query_peak_extra_bytes'=>$peak];
 unset($obj,$result,$case,$j,$d);
}
echo json_encode(['observations'=>$out]),"\n";
