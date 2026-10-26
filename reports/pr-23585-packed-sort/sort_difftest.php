<?php
/* Differential fuzzer for PR #23585 (packed-array sort). Deterministic: same seed
 * on both binaries. Hashes the sorted array, the internal pointer, and any
 * warnings for sort/rsort/usort across many input shapes and flags. */

$seed  = (int)($argv[1] ?? 1);
$count = (int)($argv[2] ?? 30000);
mt_srand($seed);

$flags = [SORT_REGULAR, SORT_NUMERIC, SORT_STRING, SORT_NATURAL,
          SORT_STRING|SORT_FLAG_CASE, SORT_NATURAL|SORT_FLAG_CASE];

/* element generators chosen to stress ties / type juggling / fallback */
function gen_elem(int $kind) {
    switch ($kind) {
        case 0: return mt_rand(-5, 5);                                  // small ints, many ties
        case 1: return [PHP_INT_MIN, PHP_INT_MAX, 0, -1, 1][mt_rand(0,4)];
        case 2: return mt_rand(-3,3) / 2.0;                             // floats w/ ties
        case 3: return [NAN, INF, -INF, 0.0, -0.0][mt_rand(0,4)];       // special floats
        case 4: return (string)mt_rand(-5,5);                           // numeric strings
        case 5: return ['a','A','b','B','10','9','a10','a9'][mt_rand(0,7)]; // case/natural ties
        case 6: return [9007199254740992, 9007199254740993, 9223372036854775807, 9223372036854775806][mt_rand(0,3)]; // near 2^53 for SORT_NUMERIC stability
        case 7: return mt_rand(0,1) ? true : false;
        case 8: return mt_rand(0,1) ? null : mt_rand(-2,2);
        default: return mt_rand(-5,5);
    }
}
function gen_array(int $kind, int $n): array {
    $a = [];
    for ($i=0;$i<$n;$i++) $a[] = gen_elem($kind);
    // sometimes punch holes (keeps it packed-with-holes)
    if (mt_rand(0,3)===0) { for ($h=0;$h<min(3,$n);$h++){ $k=mt_rand(0,$n-1); unset($a[$k]); } $a=array_values($a); if(mt_rand(0,1)){ $a[]=gen_elem($kind); unset($a[count($a)-1]); } }
    return $a;
}

function warnings_of(callable $fn): array {
    $w=[]; set_error_handler(function($no,$msg) use (&$w){ $w[]="$no:$msg"; return true; });
    try { $fn(); } catch (\Throwable $e) { restore_error_handler(); return ['THROW:'.get_class($e).':'.$e->getMessage()]; }
    restore_error_handler(); return $w;
}

function snapshot(array $a): string {
    // values + keys + internal pointer, serialized stably
    $s = '';
    foreach ($a as $k=>$v) { $s .= $k.'='.serialize_val($v).';'; }
    $ptr = (current($a)===false && key($a)===null) ? 'END' : (key($a).'=>'.serialize_val(current($a)));
    return $s.'|ptr:'.$ptr;
}
function serialize_val($v): string {
    if (is_float($v)) { if (is_nan($v)) return 'NAN'; if (is_infinite($v)) return $v>0?'INF':'-INF'; return 'D'.sprintf('%.17g',$v); }
    if (is_string($v)) return 'S'.$v; if (is_int($v)) return 'I'.$v; if (is_bool($v)) return $v?'T':'F'; if ($v===null) return 'N';
    if (is_array($v)) { $r='A'; foreach($v as $x) $r.=serialize_val($x).','; return $r; }
    return 'O';
}

$acc = hash_init('xxh128');
for ($it=0;$it<$count;$it++){
    $n = [0,1,2,3,5,8,17,64][mt_rand(0,7)];
    $kind = mt_rand(0,8);
    $flag = $flags[mt_rand(0,count($flags)-1)];
    $base = gen_array($kind, $n);

    // sort
    $a=$base; $w=warnings_of(function() use (&$a,$flag){ sort($a,$flag); });
    hash_update($acc, "sort:".snapshot($a)."|w:".implode('/',$w)."\n");
    // rsort
    $a=$base; $w=warnings_of(function() use (&$a,$flag){ rsort($a,$flag); });
    hash_update($acc, "rsort:".snapshot($a)."|w:".implode('/',$w)."\n");
    // usort with a plain comparator
    $a=$base; $w=warnings_of(function() use (&$a){ usort($a, fn($x,$y)=> $x<=>$y); });
    hash_update($acc, "usort:".snapshot($a)."|w:".implode('/',$w)."\n");
    // usort reentrant: callback mutates the array
    $a=$base; $cnt=0;
    $w=warnings_of(function() use (&$a,&$cnt){ usort($a, function($x,$y) use (&$a,&$cnt){ $cnt++; if($cnt===2 && count($a)>1){ $a[]=999; } return $x<=>$y; }); });
    hash_update($acc, "usortRe:".snapshot($a)."|w:".implode('/',$w)."\n");
    // usort reentrant: callback reads internal pointer
    $a=$base;
    $w=warnings_of(function() use (&$a){ usort($a, function($x,$y) use (&$a){ $k=key($a); return $x<=>$y; }); });
    hash_update($acc, "usortPtr:".snapshot($a)."|w:".implode('/',$w)."\n");
}
echo hash_final($acc), "\n";
