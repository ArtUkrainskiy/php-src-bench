<?php
/* Fallback-cost benchmark for PR #23585. The PR scans a packed array for
 * fast-path eligibility before sorting; a disqualifying element forces the old
 * Bucket sort, so the scan is pure overhead. Worst case: a long scalar prefix
 * with the disqualifier at the end.
 * Usage: php -n sort_fallback.php <size> <batch> <disq:obj|nan|ref|none> <pos:last|first> <sort|rsort|usort> <sort|nop> */
ini_set('memory_limit', '-1');
$size  = (int)($argv[1] ?? 65535);
$batch = (int)($argv[2] ?? 2000);
$disq  = $argv[3] ?? 'obj';
$pos   = $argv[4] ?? 'last';
$op    = $argv[5] ?? 'sort';
$mode  = $argv[6] ?? 'sort';

mt_srand(717);
$rows = [];
$refholders = [];
for ($i=0;$i<$batch;$i++){
    $row=[];
    for ($j=0;$j<$size;$j++){ $row[] = mt_rand(-1000000,1000000); }
    if ($disq !== 'none') {
        $k = ($pos==='first') ? 0 : $size-1;
        if ($disq==='obj') { $row[$k] = new stdClass(); }
        elseif ($disq==='nan') { $row[$k] = NAN; }
        elseif ($disq==='ref') { $refholders[$i] = $row[$k]; $row[$k] =& $refholders[$i]; }
    }
    $rows[]=$row;
}
unset($row);

if ($mode==='nop') { $s=0; foreach($rows as &$r){ $s+=count($r); } unset($r); echo $s,"\n"; return; }

$cmp = fn($x,$y)=>$x<=>$y;
foreach ($rows as &$r){
    switch($op){
        case 'sort':  @sort($r, SORT_REGULAR); break;
        case 'rsort': @rsort($r, SORT_REGULAR); break;
        case 'usort': @usort($r, $cmp); break;
    }
}
unset($r);
echo "done\n";
