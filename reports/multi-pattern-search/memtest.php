<?php
/* Memory of the prepared automaton and the transient per-call scratch.
 *   automaton: VmRSS delta (resident, page-granular, the figure quoted in the report)
 *     plus the Zend-heap delta (precise; the buffers are emalloc'd). Run one N per
 *     process for a clean before/after delta.
 *   per-call scratch (emalloc'd best[] / hits): memory_get_peak_usage around the call
 *     after memory_reset_peak_usage (PHP 8.2+) — VmHWM is the process lifetime maximum,
 *     so it would not show a call peak below an earlier one, and is not used here.
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

$r0=kb('VmRSS'); $u0=memory_get_usage();
$m=new Str\Matcher($dict);
$r1=kb('VmRSS'); $u1=memory_get_usage();
printf("automaton: RSS +%d KB, Zend heap +%d KB  (N=%d, %d keyword bytes => %.0f B/keyword-byte RSS)\n",
    $r1-$r0, intdiv($u1-$u0,1024), $N, $tot_bytes, ($r1-$r0)*1024.0/max(1,$tot_bytes));

memory_reset_peak_usage();
$base=memory_get_usage();
$res=$m->matchAll($text);
printf("matchAll transient Zend-heap peak: ~%d KB (text %d KB, %d matches)\n",
    intdiv(memory_get_peak_usage()-$base,1024), intdiv($S,1024), count($res));
unset($res);

$map=[]; foreach($dict as $i=>$w)$map[$w]='X';
$rp=new Str\Replacer($map);
memory_reset_peak_usage();
$base=memory_get_usage();
$out=$rp->replace($text);
printf("replace transient Zend-heap peak: ~%d KB (best[] ~ 4 bytes/subject byte = %d KB)\n",
    intdiv(memory_get_peak_usage()-$base,1024), intdiv($S*4,1024));
