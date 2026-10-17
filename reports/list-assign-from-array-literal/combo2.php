<?php
// Combinatorial sweep: 2 targets x 2 values, each from a set of kinds, with observable side effects.
// MASTER=<php> HEAD=<php> WORK=<empty dir> php combo2.php: each program is a file in WORK, run by
// HEAD in the four modes of modes.sh (they must agree) and by MASTER without opcache (listed).
$prelude = <<<'PHP'
final class D { public function __construct(public $n) {} public function __destruct() { echo "~{$this->n} "; } public function __toString(): string { return $this->n; } }
final class AA implements ArrayAccess { public $d = []; function offsetExists($o): bool { return isset($this->d[$o]); } function offsetGet($o): mixed { echo "get($o) "; return $this->d[$o] ?? null; } function offsetSet($o, $v): void { echo "set($o) "; } function offsetUnset($o): void {} }
final class STO implements ArrayAccess { public $d = []; function offsetExists($o): bool { return isset($this->d[$o]); } function offsetGet($o): mixed { echo "get($o) "; return $this->d[$o] ?? null; } function offsetSet($o, $v): void { echo "store($o) "; $this->d[$o] = $v; } function offsetUnset($o): void {} }
final class MG { public $d = []; function __set($n, $v) { echo "__set($n) "; } function __get($n) { echo "__get($n) "; return $this->d[$n] ?? null; } }
final class HK { public $hd { set { echo "hook-discard "; } get => null; } public $hs { set { echo "hook-store "; $this->hs = $value; } } }
final class TY { public int $i = 0; public string $s = ''; public ?D $d = null; public static $st; }
$aa = new AA; $as = new STO; $mg = new MG; $hk = new HK; $ty = new TY; $arr = []; $str = 'abc'; $cv = new D('cv'); $old = new D('old');
$plain = new D('plain'); $same = null;
PHP;
$targets = [
    'cv' => '$t1', 'cv-same' => '$same', 'cv-old' => '$old', 'prop' => '$ty->d', 'typed-int' => '$ty->i', 'typed-str' => '$ty->s',
    'aa-discard' => '$aa["k"]', 'aa-store' => '$as["k"]', 'magic' => '$mg->m', 'hook-discard' => '$hk->hd', 'hook-store' => '$hk->hs',
    'static' => 'TY::$st', 'dim' => '$arr[]', 'stroff' => '$str[0]', 'nested' => '[$n1]',
];
$values = ['new' => 'new D("v%d")', 'cv' => '$cv', 'nested' => '[new D("n%d")]', 'int' => '%d'];
$M = getenv('MASTER'); $P = getenv('HEAD'); $dir = getenv('WORK');
$modes = ['plain', 'opt', 'tracing', 'function'];
function run($bin, $file, $mode) {
    $p = proc_open([__DIR__ . '/modes.sh', $bin, $file, $mode], [1 => ['pipe', 'w'], 2 => ['pipe', 'w']], $pipes);
    $out = stream_get_contents($pipes[1]) . stream_get_contents($pipes[2]);
    proc_close($p);
    return preg_replace('/ in \S+ on line \d+/', '', $out);
}
$n = 0; $modeDiffs = 0; $masterDiffs = 0; $byKind = []; $modeList = [];
foreach ($targets as $tk1 => $t1) foreach ($targets as $tk2 => $t2) {
    if ($tk1 === 'cv-same' && $tk2 !== 'cv-same') continue;
    if ($tk1 === 'cv-same') { $t1 = '$same'; }
    if ($tk2 === 'cv-same') { $t2 = $t1; if ($tk1 === 'nested') $t2 = '[$n1]'; }
    foreach ($values as $vk1 => $v1) foreach ($values as $vk2 => $v2) {
        $stmt = "[$t1, $t2] = [" . sprintf($v1, 1) . ", " . sprintf($v2, 2) . "];";
        $code = "<?php\n" . $prelude . "\ntry { $stmt echo '|after '; } catch (Throwable \$e) { echo '!', get_class(\$e), ' '; } echo '|end'; unset(\$t1, \$same, \$old, \$n1, \$arr, \$str, \$ty, \$hk, \$as, \$aa, \$mg, \$cv, \$plain); echo \"\\n\";\n";
        $file = "$dir/c$n.php"; file_put_contents($file, $code); $n++;
        $outs = [];
        foreach ($modes as $m) { $outs[$m] = run($P, $file, $m); }
        foreach ($modes as $m) if ($outs[$m] !== $outs['plain']) { $modeDiffs++; $modeList[] = [$m, $stmt, trim($outs['plain']), trim($outs[$m])]; }
        $om = run($M, $file, 'plain');
        if ($om !== $outs['plain']) { $masterDiffs++; $byKind["$tk1,$tk2"][] = ["$vk1,$vk2", $stmt, trim($om), trim($outs['plain'])]; }
    }
}
echo "programs=$n head-mode-diffs=$modeDiffs master-diffs=$masterDiffs\n";
foreach (array_slice($modeList, 0, 10) as [$m, $stmt, $a, $b]) { echo "MODE $m: $stmt\n  plain: $a\n  $m: $b\n"; }
foreach ($byKind as $k => $list) {
    echo "== targets $k: ", count($list), " diffs\n";
    foreach ($list as [$vk, $stmt, $om, $op]) { echo "  [$vk] $stmt\n    master: $om\n    head  : $op\n"; }
}
