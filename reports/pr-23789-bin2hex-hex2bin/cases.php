<?php
// One bin2hex()/hex2bin() case per process: ns per call (median of 7) and an md5 of the outputs.
//   php cases.php <case|list> [calls]
// With a call count, makes exactly that many calls and prints nothing (for perf stat).
// Short inputs come from a pool of 256 different random strings of the same length (fixed seed),
// so the branch predictor does not see one string repeated.

mt_srand(23789);

function rnd_bytes(int $len): string
{
	$s = '';
	for ($i = 0; $i < $len; $i++) {
		$s .= chr(mt_rand(0, 255));
	}
	return $s;
}

/** Hex text of $len bytes; built by hand, not with bin2hex(), so both builds get the same input. */
function hex_of(string $bin, string $case): string
{
	$digits = $case === 'upper' ? '0123456789ABCDEF' : '0123456789abcdef';
	$s = '';
	for ($i = 0, $n = strlen($bin); $i < $n; $i++) {
		$b = ord($bin[$i]);
		$d = $digits;
		if ($case === 'mixed') {
			$d = mt_rand(0, 1) ? '0123456789ABCDEF' : '0123456789abcdef';
		}
		$s .= $d[$b >> 4] . $d[$b & 15];
	}
	return $s;
}

function pool(int $count, callable $make): array
{
	$p = [];
	for ($i = 0; $i < $count; $i++) {
		$p[] = $make();
	}
	return $p;
}

$cases = [];
foreach ([4, 8, 15, 16, 20, 31, 32, 33, 48, 64, 100, 256, 1024] as $n) {
	$cases["bin2hex-$n"] = ['bin2hex', static fn () => pool(256, static fn () => rnd_bytes($n))];
}
$cases['bin2hex-64k'] = ['bin2hex', static fn () => pool(4, static fn () => rnd_bytes(65536))];
foreach ([4, 8, 15, 16, 20, 31, 32, 33, 48, 64, 100, 256, 1024] as $n) {
	$cases["hex2bin-$n"] = ['hex2bin', static fn () => pool(256, static fn () => hex_of(rnd_bytes($n), 'lower'))];
}
$cases['hex2bin-64k'] = ['hex2bin', static fn () => pool(4, static fn () => hex_of(rnd_bytes(65536), 'lower'))];
$cases['hex2bin-upper-32'] = ['hex2bin', static fn () => pool(256, static fn () => hex_of(rnd_bytes(32), 'upper'))];
$cases['hex2bin-mixed-32'] = ['hex2bin', static fn () => pool(256, static fn () => hex_of(rnd_bytes(32), 'mixed'))];
$cases['hex2bin-mixed-1024'] = ['hex2bin', static fn () => pool(256, static fn () => hex_of(rnd_bytes(1024), 'mixed'))];
// Invalid input: one non-hex byte at a random position; hex2bin() returns false with a warning.
$bad = static function (int $n): string {
	$s = hex_of(rnd_bytes($n), 'lower');
	$s[mt_rand(0, strlen($s) - 1)] = 'g';
	return $s;
};
$cases['hex2bin-invalid-32'] = ['@hex2bin', static fn () => pool(256, static fn () => $bad(32))];
$cases['hex2bin-invalid-1024'] = ['@hex2bin', static fn () => pool(256, static fn () => $bad(1024))];
// Callers of zend_bin2hex() outside bin2hex(): digest formatting.
$cases['md5-32'] = ['md5', static fn () => pool(256, static fn () => rnd_bytes(32))];
$cases['sha1-32'] = ['sha1', static fn () => pool(256, static fn () => rnd_bytes(32))];
$cases['hash-xxh128-32'] = ['xxh128', static fn () => pool(256, static fn () => rnd_bytes(32))];
$cases['hash-sha256-32'] = ['sha256', static fn () => pool(256, static fn () => rnd_bytes(32))];

$name = $argv[1] ?? 'list';
if ($name === 'list') {
	echo implode(' ', array_keys($cases)), "\n";
	exit;
}
[$fn, $make] = $cases[$name];
$pool = $make();
$mask = count($pool) - 1;

$run = match ($fn) {
	'bin2hex' => static function (int $calls) use ($pool, $mask) { for ($i = 0; $i < $calls; $i++) { $r = bin2hex($pool[$i & $mask]); } },
	'hex2bin' => static function (int $calls) use ($pool, $mask) { for ($i = 0; $i < $calls; $i++) { $r = hex2bin($pool[$i & $mask]); } },
	'@hex2bin' => static function (int $calls) use ($pool, $mask) { for ($i = 0; $i < $calls; $i++) { $r = @hex2bin($pool[$i & $mask]); } },
	'md5' => static function (int $calls) use ($pool, $mask) { for ($i = 0; $i < $calls; $i++) { $r = md5($pool[$i & $mask]); } },
	'sha1' => static function (int $calls) use ($pool, $mask) { for ($i = 0; $i < $calls; $i++) { $r = sha1($pool[$i & $mask]); } },
	'xxh128' => static function (int $calls) use ($pool, $mask) { for ($i = 0; $i < $calls; $i++) { $r = hash('xxh128', $pool[$i & $mask]); } },
	'sha256' => static function (int $calls) use ($pool, $mask) { for ($i = 0; $i < $calls; $i++) { $r = hash('sha256', $pool[$i & $mask]); } },
};

if (isset($argv[2])) {
	$run((int) $argv[2]);
	exit;
}

$out = '';
foreach ($pool as $s) {
	$out .= md5(var_export(match ($fn) {
		'bin2hex' => bin2hex($s), 'hex2bin' => hex2bin($s), '@hex2bin' => @hex2bin($s),
		'md5' => md5($s), 'sha1' => sha1($s), 'xxh128' => hash('xxh128', $s), 'sha256' => hash('sha256', $s),
	}, true));
}
$calls = max(1000, (int) (2e6 / max(1, strlen($pool[0]))));
$t = [];
for ($k = 0; $k < 7; $k++) {
	$t0 = hrtime(true);
	$run($calls);
	$t[] = (hrtime(true) - $t0) / $calls;
}
sort($t);
printf("%s %.1f %s\n", $name, $t[3], md5($out));
