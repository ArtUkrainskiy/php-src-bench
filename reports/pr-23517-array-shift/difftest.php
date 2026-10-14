<?php
// Differential test for array_shift(): sequences of shifts, unsets, appends, references, objects,
// copies and foreach on packed (and some hash) arrays. Records every return value, the array after
// each step (keys, values, reference structure via serialize) and destructor order.
//   php -n difftest.php [fuzz-count] [seed]

$fuzzCount = (int) ($argv[1] ?? 20000);
$seed = (int) ($argv[2] ?? 1);

$log = [];
final class D { public function __construct(public int $id) {} public function __destruct() { $GLOBALS['log'][] = "~{$this->id}"; } }

$sections = [];
$counts = [];
$rec = static function (string $name, string $s) use (&$sections, &$counts) {
	$sections[$name] ??= hash_init('sha256');
	hash_update($sections[$name], $s . "\n");
	$counts[$name] = ($counts[$name] ?? 0) + 1;
};
$state = static fn (array $a): string => serialize($a) . '|' . json_encode(array_keys($a));

// 1. drain packed arrays of every size 0..40, with an append after every shift
for ($n = 0; $n <= 40; $n++) {
	$a = $n ? range(100, 99 + $n) : [];
	$out = [];
	while ($a) { $out[] = array_shift($a); $a[] = 'x'; array_pop($a); }
	$a[] = 'end';
	$rec('drain', json_encode($out) . $state($a));
}
// 2. holes at every position (unset one or two slots), then shifts and appends
for ($n = 1; $n <= 12; $n++) {
	for ($h = 0; $h < $n; $h++) {
		foreach ([[$h], [$h, ($h + 2) % $n]] as $holes) {
			$a = range(0, $n - 1);
			foreach ($holes as $x) unset($a[$x]);
			$s = '';
			for ($k = 0; $k < 3; $k++) { $s .= var_export(array_shift($a), true) . ';' . $state($a) . ';'; $a[] = "n$k"; $s .= $state($a) . ';'; }
			$rec('holes', $s);
		}
	}
}
// 3. references in the tail, shared objects, destructor order, copies
for ($n = 1; $n <= 8; $n++) {
	$x = 'X'; $y = 'Y';
	$a = [];
	for ($i = 0; $i < $n; $i++) {
		if ($i % 3 === 1) $a[] = &$x; elseif ($i % 3 === 2) $a[] = new D($i); else $a[] = $i;
	}
	$copy = $a;
	$log = [];
	$v = array_shift($a);
	$x = 'X2';
	$s = var_export(is_object($v) ? 'obj' . $v->id : $v, true) . ';' . $state($a) . ';' . $state($copy);
	unset($v, $a);
	$s .= ';' . implode(',', $log);
	$log = [];
	unset($copy);
	$rec('refs objects', $s . ';' . implode(',', $log));
}
// 4. array_shift inside foreach (by value and by reference), and with an external iterator position
for ($n = 1; $n <= 8; $n++) {
	$a = range(0, $n - 1);
	$s = '';
	foreach ($a as $k => $v) { $s .= "$k=$v,"; if ($k === 0) $s .= 'S' . array_shift($a) . ','; }
	$s .= $state($a) . ';';
	$a = range(0, $n - 1);
	foreach ($a as $k => &$v) { $s .= "$k=$v,"; if ($v % 2 === 0 && $a) $s .= 'S' . array_shift($a) . ','; }
	unset($v);
	$rec('foreach', $s . $state($a));
}
// 5. self references and nested arrays
$a = [1, 2, 3];
$a[] = &$a;
$v = array_shift($a);
$rec('self', var_export($v, true) . ';' . count($a) . ';' . count($a[2]));
$a = [[1, [2]], [3], 4];
$rec('self', serialize(array_shift($a)) . ';' . $state($a));
// 6. fuzz: random operation sequences on packed arrays, sometimes turned into hash arrays
mt_srand($seed);
for ($k = 0; $k < $fuzzCount; $k++) {
	$n = mt_rand(0, 3) ? mt_rand(0, 20) : mt_rand(0, 300);
	$a = $n ? range(1, $n) : []; // range(1, 0) is [1, 0]
	$x = 'r';
	$s = '';
	for ($op = mt_rand(1, 12); $op > 0; $op--) {
		switch (mt_rand(0, 9)) {
			case 0: case 1: case 2: case 3: $s .= var_export(array_shift($a), true) . ';'; break;
			case 4: if ($a) unset($a[array_rand($a)]); break;
			case 5: $a[] = mt_rand(); break;
			case 6: $a[] = &$x; break;
			case 7: $b = $a; $s .= var_export(array_shift($b), true) . ':' . count($b) . ';'; break;
			case 8: if (mt_rand(0, 4) === 0) $a['k' . mt_rand()] = 1; break;
			case 9: array_unshift($a, 'u'); break;
		}
	}
	$x = 'r2';
	$rec('fuzz', $s . $state($a));
}

foreach ($sections as $name => $ctx) echo str_pad($name, 14), str_pad((string) $counts[$name], 8, ' ', STR_PAD_LEFT), '  ', hash_final($ctx), "\n";
