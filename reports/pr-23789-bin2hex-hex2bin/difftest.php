<?php
// Differential test for bin2hex()/hex2bin(): prints one sha256 per section over every result,
// to compare a master build with a PR build.   php -n difftest.php [fuzz-count] [seed]
// Results are recorded with var_export(), so false (invalid hex) differs from any string.

$fuzzCount = (int) ($argv[1] ?? 200000);
$seed = (int) ($argv[2] ?? 1);
$warn = 0;
set_error_handler(static function () use (&$warn) { $warn++; return true; });

$sections = [];
$h = static function (string $name) use (&$sections) { $sections[$name] ??= hash_init('sha256'); return $sections[$name]; };
$rec = static function (string $name, $v) use ($h) { hash_update($h($name), var_export($v, true) . "\n"); };

mt_srand(1);
$rnd = static function (int $len): string { $s = ''; for ($i = 0; $i < $len; $i++) $s .= chr(mt_rand(0, 255)); return $s; };
$hexOf = static function (string $bin, bool $mixed = false): string {
	$s = '';
	foreach (str_split($bin) as $c) {
		$d = $mixed && mt_rand(0, 1) ? '0123456789ABCDEF' : '0123456789abcdef';
		$s .= $d[ord($c) >> 4] . $d[ord($c) & 15];
	}
	return $bin === '' ? '' : $s;
};

// 1. bin2hex: every length 0..300, random bytes, 20 strings each
for ($len = 0; $len <= 300; $len++) {
	for ($k = 0; $k < 20; $k++) {
		$rec('bin2hex lengths', bin2hex($rnd($len)));
	}
}
// 2. bin2hex: every byte value at every position of 16, 17, 32, 33, 48 byte strings
foreach ([16, 17, 32, 33, 48] as $len) {
	$base = $rnd($len);
	for ($p = 0; $p < $len; $p++) {
		for ($b = 0; $b < 256; $b++) {
			$s = $base; $s[$p] = chr($b);
			$rec('bin2hex byte x position', bin2hex($s));
		}
	}
}
// 3. hex2bin: every length 0..600 (odd too), valid mixed-case hex
for ($len = 0; $len <= 600; $len++) {
	for ($k = 0; $k < 10; $k++) {
		$hex = substr($hexOf($rnd(intdiv($len + 1, 2)), true), 0, $len);
		$rec('hex2bin lengths', hex2bin($hex));
	}
}
// 4. hex2bin: every byte value at every position of valid hex strings around the 32-character chunk
foreach ([2, 30, 32, 34, 62, 64, 66, 96, 98, 128] as $len) {
	$base = $hexOf($rnd(intdiv($len, 2)), true);
	for ($p = 0; $p < $len; $p++) {
		for ($b = 0; $b < 256; $b++) {
			$s = $base; $s[$p] = chr($b);
			$rec('hex2bin byte x position', hex2bin($s));
		}
	}
}
// 5. hex2bin: all pairs of characters (65536) in the first and the last pair of a 64-character string
$base = $hexOf($rnd(32));
foreach ([0, 30, 31, 62] as $p) {
	for ($a = 0; $a < 256; $a++) {
		for ($b = 0; $b < 256; $b++) {
			$s = $base; $s[$p] = chr($a); $s[$p + 1] = chr($b);
			$rec('hex2bin pairs', hex2bin($s));
		}
	}
}
// 6. fuzz: random lengths up to 2000, mostly valid hex, sometimes one or a few bad bytes
mt_srand($seed);
for ($k = 0; $k < $fuzzCount; $k++) {
	$len = mt_rand(0, 1) ? mt_rand(0, 200) : mt_rand(0, 2000);
	$hex = substr($hexOf($rnd(intdiv($len + 1, 2)), (bool) mt_rand(0, 1)), 0, $len);
	$r = mt_rand(0, 9);
	if ($r < 3 && $len > 0) {
		for ($m = mt_rand(1, 3); $m > 0; $m--) {
			$hex[mt_rand(0, $len - 1)] = chr(mt_rand(0, 255));
		}
	}
	$rec('fuzz hex2bin', hex2bin($hex));
	$rec('fuzz bin2hex', bin2hex($hex));
}

foreach ($sections as $name => $ctx) {
	echo str_pad($name, 26), hash_final($ctx), "\n";
}
echo str_pad('warnings', 26), $warn, "\n";
