<?php
/* Memory of the prepared automaton (malloc'd, object lifetime -> counts in process RSS)
 * and the transient peak during a call. RSS from /proc/self/status (page-granular,
 * approximate). Run one N per process for a clean before/after delta.
 * Usage: php -dextension=strmatch.so memtest.php <N> <S> [seed] */

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
function kb(string $field): int {
    foreach (file('/proc/self/status') as $l) if (strncmp($l, $field.':', strlen($field)+1) === 0) return (int)preg_replace('/\D/','',$l);
    return 0;
}

$N=(int)($argv[1]??5000); $S=(int)($argv[2]??65536); $seed=(int)($argv[3]??1);
$dict=gen_dict($N,$seed);
$text=gen_text($S,$dict,$seed);
$tot_bytes=0; foreach($dict as $w)$tot_bytes+=strlen($w);

$r0=kb('VmRSS');
$m=new Str\Matcher($dict);
$r1=kb('VmRSS');
$auto=$r1-$r0;
printf("automaton RSS: %d KB for N=%d (%d keyword bytes, %d nodes approx) => %.1f bytes/keyword, %.1f bytes/keyword-byte\n",
    $auto, $N, $tot_bytes, 0, $auto*1024.0/$N, $auto*1024.0/$tot_bytes);

$h0=kb('VmHWM');
$res=$m->matchAll($text);
$h1=kb('VmHWM');
printf("matchAll transient peak HWM delta: %d KB (text %d KB, %d matches)\n", $h1-$h0, intdiv($S,1024), count($res));
unset($res);

$map=[]; foreach($dict as $i=>$w)$map[$w]='X';
$rp=new Str\Replacer($map);
$h2=kb('VmHWM');
$out=$rp->replace($text);
$h3=kb('VmHWM');
printf("replace transient peak HWM delta: %d KB (best[] = 4 bytes/subject byte = %d KB expected)\n", $h3-$h2, intdiv($S*4,1024));
