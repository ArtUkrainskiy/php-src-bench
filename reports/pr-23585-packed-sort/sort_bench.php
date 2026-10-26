<?php
/* Perf-measured sort benchmark for PR #23585. Pre-generates BATCH packed arrays
 * of SIZE, then either sorts each once (mode=sort) or does nothing (mode=nop).
 * Run under perf stat; subtract nop from sort to isolate the sort cost.
 * Usage: php -n sort_bench.php <ints|floats|strings> <size> <batch> <sort|rsort|usort> <sort|nop> */
ini_set('memory_limit', '-1'); // strings at 65535 x batch 60 needs > 128 MB just to build the input
$type  = $argv[1] ?? 'ints';
$size  = (int)($argv[2] ?? 64);
$batch = (int)($argv[3] ?? 20000);
$op    = $argv[4] ?? 'sort';
$mode  = $argv[5] ?? 'sort';

mt_srand(717);
$rows = [];
for ($i=0;$i<$batch;$i++){
    $row=[];
    for ($j=0;$j<$size;$j++){
        $v = mt_rand(-1000000,1000000);
        $row[] = $type==='ints' ? $v : ($type==='floats' ? $v/8.0 : (($j%2?'A':'a').$v));
    }
    $rows[]=$row;
}
unset($row);

if ($mode==='nop') { $s=0; foreach($rows as &$r){ $s+=count($r); } unset($r); echo $s,"\n"; return; }

$cmp = fn($x,$y)=>$x<=>$y;
foreach ($rows as &$r){
    switch($op){
        case 'sort':  sort($r, SORT_REGULAR); break;
        case 'rsort': rsort($r, SORT_REGULAR); break;
        case 'usort': usort($r, $cmp); break;
    }
}
unset($r);
echo "done\n";
