<?php
// Differential test for var_export(): one sha256 per section over the exported text of every value.
//   php -n difftest.php [fuzz-count] [seed]

$fuzzCount = (int) ($argv[1] ?? 20000);
$seed = (int) ($argv[2] ?? 1);

$sections = [];
$counts = [];
$rec = static function (string $name, $v) use (&$sections, &$counts) {
	$sections[$name] ??= hash_init('sha256');
	hash_update($sections[$name], var_export($v, true) . "\n");
	$counts[$name] = ($counts[$name] ?? 0) + 1;
};

final class P { public $pub; protected $prot; private $priv; public function __construct($a, $b, $c) { $this->pub = $a; $this->prot = $b; $this->priv = $c; } }
enum E: string { case A = "a'b\\c"; }

// 1. every byte, alone and between letters, as a value and as a key
for ($b = 0; $b < 256; $b++) {
	$c = chr($b);
	$rec('byte value', $c);
	$rec('byte value', "x{$c}y");
	$rec('byte key', [$c => 1, "x{$c}y" => 2]);
}
// 2. all strings of length 1..4 over the escaping alphabet {a, ', \, NUL}, as values, keys and dynamic property names
$alpha = ['a', "'", '\\', "\0"];
$all = [''];
for ($len = 1; $len <= 4; $len++) {
	$next = [];
	foreach ($all as $p) if (strlen($p) === $len - 1) foreach ($alpha as $a) $next[] = $p . $a;
	$all = array_merge($all, $next);
}
foreach ($all as $s) {
	$rec('escape value', $s);
	$rec('escape key', [$s => $s]);
	$o = new stdClass();
	if ($s !== '' && $s[0] !== "\0") { $o->{$s} = $s; }
	$rec('escape property', $o);
}
// 3. long strings: runs of quotes, backslashes and NULs, and their mixes, 1 KB to 64 KB
mt_srand(5);
foreach ([1024, 65536] as $n) {
	foreach (["'", '\\', "\0", "a"] as $c) $rec('long', str_repeat($c, $n));
	$s = ''; for ($i = 0; $i < $n; $i++) $s .= $alpha[mt_rand(0, 3)];
	$rec('long', $s);
	$s = ''; for ($i = 0; $i < $n; $i++) $s .= mt_rand(0, 15) ? chr(mt_rand(32, 126)) : $alpha[mt_rand(1, 3)];
	$rec('long', $s);
}
// 4. nesting and indentation, objects with visibility, enums, numeric and mixed keys
$deep = 'leaf';
for ($i = 0; $i < 6; $i++) $deep = [$i => $deep, "k'$i" => [$deep], 'o' => (object) ['p' => $deep]];
$rec('structure', $deep);
$rec('structure', new P("a'", ['b\\' => "\0"], new P(1, 2.5, [true, null])));
$rec('structure', [E::A, 'e' => [E::A]]);
$rec('structure', [1.5, false, null, -0.0, 1e100, NAN, INF, -1 => 'neg', '01' => 'str', '' => 'empty', PHP_INT_MAX => 'max']);
// 5. fuzz: random nested arrays/objects of random strings
mt_srand($seed);
$rs = static function () use ($alpha): string {
	$n = mt_rand(0, 3) ? mt_rand(0, 12) : mt_rand(0, 300);
	$s = '';
	for ($i = 0; $i < $n; $i++) $s .= mt_rand(0, 2) ? chr(mt_rand(0, 255)) : $alpha[mt_rand(0, 3)];
	return $s;
};
$gen = static function (int $depth) use (&$gen, $rs) {
	$t = mt_rand(0, $depth > 3 ? 2 : 5);
	if ($t <= 1) return $rs();
	if ($t === 2) return mt_rand(-1000, 1000);
	$a = [];
	for ($i = mt_rand(0, 6); $i > 0; $i--) {
		$v = $gen($depth + 1);
		if (mt_rand(0, 1)) $a[$rs()] = $v; else $a[] = $v;
	}
	if ($t === 5) { $o = new stdClass(); foreach ($a as $k => $v) { $k = (string) $k; if ($k !== '' && $k[0] !== "\0") $o->{$k} = $v; } return $o; }
	return $a;
};
for ($k = 0; $k < $fuzzCount; $k++) $rec('fuzz', $gen(0));

foreach ($sections as $name => $ctx) echo str_pad($name, 16), str_pad((string) $counts[$name], 8, ' ', STR_PAD_LEFT), '  ', hash_final($ctx), "\n";
