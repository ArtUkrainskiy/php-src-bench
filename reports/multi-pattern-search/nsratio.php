<?php
/* Paired ns/op ratio in ONE process, robust to between-process frequency drift.
 * For R reps, time A then B (K calls each) back to back and record B/A per rep; report
 * median ratio and median absolute ns. Alternate order each rep to cancel ramp.
 * Usage: php -dextension=strmatch.so nsratio.php <pair> <N> <S> <K> <R> [seed]
 *   pair: replace-vs-strtr | matchall-vs-strpos */

function gen_dict(int $n, int $seed): array {
    mt_srand($seed); $w=[]; $seen=[];
    while (count($w) < $n) { $l=mt_rand(4,12); $s=''; for($i=0;$i<$l;$i++)$s.=chr(mt_rand(97,122)); if(isset($seen[$s]))continue; $seen[$s]=1; $w[]=$s; }
    return $w;
}
function gen_text(int $bytes, array $d, int $seed): string {
    mt_srand($seed ^ 0x5a5a); $n=count($d); $o='';
    while (strlen($o) < $bytes) { if(mt_rand(0,99)<8){$o.=$d[mt_rand(0,$n-1)].' ';} else {$l=mt_rand(2,10);for($i=0;$i<$l;$i++)$o.=chr(mt_rand(97,122));$o.=' ';} }
    return substr($o,0,$bytes);
}
function timeit(callable $op, int $K): float { $t0=hrtime(true); $s=0; for($i=0;$i<$K;$i++)$s+=$op(); $t1=hrtime(true); return ($t1-$t0)/$K; }

$pair=$argv[1]??'replace-vs-strtr'; $N=(int)($argv[2]??500); $S=(int)($argv[3]??16384);
$K=(int)($argv[4]??500); $R=(int)($argv[5]??15); $seed=(int)($argv[6]??1);

$dict=gen_dict($N,$seed);
$map=[]; foreach($dict as $i=>$w)$map[$w]='<'.($i%7).'>';
$text=gen_text($S,$dict,$seed);

if ($pair==='replace-vs-strtr') {
    $r=new Str\Replacer($map);
    $A=fn()=>strlen($r->replace($text)); $An='replace';
    $B=fn()=>strlen(strtr($text,$map)); $Bn='strtr';
} elseif ($pair==='matchall-vs-strpos') {
    $m=new Str\Matcher($dict);
    $A=fn()=>count($m->matchAll($text)); $An='matchAll';
    $B=function()use($dict,$text){$c=0;foreach($dict as $w)if(str_contains($text,$w))$c++;return $c;}; $Bn='strpos-loop';
} else { fwrite(STDERR,"unknown pair\n"); exit(2); }

for($i=0;$i<max(1,intdiv($K,5));$i++){ $A(); $B(); } // warm

$ra=[];$rb=[];$ratio=[];
for($k=0;$k<$R;$k++){
    if($k&1){ $b=timeit($B,$K); $a=timeit($A,$K); } else { $a=timeit($A,$K); $b=timeit($B,$K); }
    $ra[]=$a; $rb[]=$b; $ratio[]=$b/$a;
}
sort($ra);sort($rb);sort($ratio);
$md=fn($x)=>$x[intdiv(count($x),2)];
printf("%s N=%d S=%d K=%d R=%d: %s %.1f ns, %s %.1f ns, %s/%s ratio median %.2fx (min %.2f max %.2f)\n",
    $pair,$N,$S,$K,$R,$An,$md($ra),$Bn,$md($rb),$Bn,$An,$md($ratio),$ratio[0],$ratio[count($ratio)-1]);
