<?php
// Differential test for unserialize() back-references (R:/r:) across var_entries chunks (1018 slots each).
// Prints one sha256 per section over every result: serialize() of the value (keeps the reference
// structure) or "false" plus the warning text.   php -n difftest.php [fuzz-count] [seed]

$fuzzCount = (int) ($argv[1] ?? 3000);
$seed = (int) ($argv[2] ?? 1);
$last = '';
set_error_handler(static function ($no, $str) use (&$last) { $last .= "[$no] $str\n"; return true; });

$sections = [];
$rec = static function (string $name, string $payload) use (&$sections, &$last) {
	$last = '';
	$v = unserialize($payload);
	$out = $v === false && $payload !== 'b:0;' ? "false\n" : serialize($v) . "\n";
	$sections[$name] ??= hash_init('sha256');
	hash_update($sections[$name], $out . $last);
	$sections[$name . ' (count)'] = ($sections[$name . ' (count)'] ?? 0) + 1;
};

// Array of $n ints, then one element per id: R:<id>;  ids are 1-based (root array = 1, values 2..n+1).
$arrayWithRefs = static function (int $n, array $ids, string $kind = 'R'): string {
	$s = 'a:' . ($n + count($ids)) . ':{';
	for ($i = 0; $i < $n; $i++) $s .= "i:$i;i:" . ($i * 7) . ';';
	foreach ($ids as $j => $id) $s .= 'i:' . ($n + $j) . ";$kind:$id;";
	return $s . '}';
};
// Array of $n stdClass objects with one property each (object = 1 id, property = 1 id), then r: refs.
$objectsWithRefs = static function (int $n, array $ids, string $kind = 'r'): string {
	$s = 'a:' . ($n + count($ids)) . ':{';
	for ($i = 0; $i < $n; $i++) $s .= "i:$i;O:8:\"stdClass\":1:{s:1:\"v\";i:$i;}";
	foreach ($ids as $j => $id) $s .= 'i:' . ($n + $j) . ";$kind:$id;";
	return $s . '}';
};

$boundaryIds = static function (int $max): array {
	$ids = [-1, 0, 1, 2, 3];
	foreach ([1018, 2036, 3054, 4072, 5090, 6108, 7126, 8144, 9162] as $b) {
		foreach ([-2, -1, 0, 1, 2, 3] as $d) $ids[] = $b + $d;
	}
	foreach ([-1, 0, 1, 2, 1000, 1018] as $d) $ids[] = $max + $d;
	$ids[] = PHP_INT_MAX;
	return array_values(array_unique($ids));
};

// 1. R: to every id around chunk boundaries, one id per payload, arrays sized around boundaries
foreach ([1, 1016, 1017, 1018, 1019, 2034, 2035, 2036, 5088, 5089, 5090, 5091, 9200] as $n) {
	foreach ($boundaryIds($n + 1) as $id) {
		$rec('R single', $arrayWithRefs($n, [$id]));
	}
}
// 2. many R: in one payload: every valid id of a 5,200-element array, in order and reversed
$rec('R all ids', $arrayWithRefs(5200, range(1, 5201)));
$rec('R all ids', $arrayWithRefs(5200, range(5201, 1, -1)));
// 3. r: (objects) and R: into objects and properties around boundaries
foreach ([509, 510, 1017, 1018, 2600] as $n) {
	foreach ($boundaryIds(2 * $n + 1) as $id) {
		$rec('r objects', $objectsWithRefs($n, [$id], 'r'));
		$rec('R objects', $objectsWithRefs($n, [$id], 'R'));
	}
}
// 4. references inside nested arrays and objects that span chunks
$s = 'a:2:{i:0;a:3000:{';
for ($i = 0; $i < 3000; $i++) $s .= "i:$i;s:" . strlen("x$i") . ":\"x$i\";";
$s .= '}i:1;a:4:{i:0;R:3;i:1;R:1500;i:2;R:3002;i:3;R:2500;}}';
$rec('nested', $s);
// 5. nested unserialize() from __unserialize() during a large outer payload
class Inner { public $p; public function __unserialize(array $d): void { $this->p = unserialize($d['s']); } }
$inner = serialize(array_fill(0, 2000, 'v'));
$s = 'a:1202:{';
for ($i = 0; $i < 1200; $i++) $s .= "i:$i;i:$i;";
$s .= 'i:1200;O:5:"Inner":1:{s:1:"s";s:' . strlen($inner) . ':"' . $inner . '";}i:1201;R:1100;}';
$rec('nested unserialize', $s);
// 6. fuzz: random sizes up to 12,000 values, mixed types, random R:/r: to earlier ids; 10% with one invalid id
mt_srand($seed);
for ($k = 0; $k < $fuzzCount; $k++) {
	$n = mt_rand(0, 3) ? mt_rand(0, 3000) : mt_rand(0, 12000);
	$s = '';
	$count = 0;
	$ids = 1; // last id used: the root array is 1; R: does not take an id, r: does
	$objs = []; // ids of objects, the only valid targets of r:
	$bad = mt_rand(0, 9) === 0 ? mt_rand(0, max(0, $n - 1)) : -1; // 10% of payloads get one invalid reference
	for ($i = 0; $i < $n; $i++) {
		$t = $i === $bad ? 9 : mt_rand(0, 9);
		$key = "i:$count;";
		if ($t < 4 || $ids < 2) { $s .= $key . 'i:' . mt_rand() . ';'; $ids++; }
		elseif ($t < 6) { $v = 'x' . mt_rand(); $s .= $key . 's:' . strlen($v) . ":\"$v\";"; $ids++; }
		elseif ($t < 7) { $s .= $key . 'O:8:"stdClass":1:{s:1:"v";i:1;}'; $objs[] = $ids + 1; $ids += 2; }
		elseif ($t < 8) { $s .= $key . 'a:1:{i:0;d:0.5;}'; $ids += 2; }
		else {
			$r = $objs && mt_rand(0, 1) ? 'r' : 'R';
			$id = $r === 'r' ? $objs[mt_rand(0, count($objs) - 1)] : mt_rand(2, max(2, $ids));
			if ($i === $bad) $id = mt_rand(0, 1) ? mt_rand(-5, 0) : mt_rand($ids + 1, $ids + 3000);
			$s .= $key . "$r:$id;";
			if ($r === 'r') $ids++;
		}
		$count++;
	}
	$rec('fuzz', "a:$count:{" . $s . '}');
}

foreach ($sections as $name => $v) {
	echo str_pad($name, 26), is_int($v) ? $v : hash_final($v), "\n";
}
