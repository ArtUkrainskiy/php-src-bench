<?php
// difftest.php <seed> <count>: one line per case with the md5 of every result, for diffing builds.
// Covers every caller of mb_get_substr() and mb_find_strpos() on unflagged and flagged (valid UTF-8) strings.
$seed = (int)($argv[1] ?? 1);
$count = (int)($argv[2] ?? 1000);
mt_srand($seed);

$encodings = ['UTF-8', 'UTF-8-Mobile#DOCOMO', 'UTF-8-Mobile#KDDI-A', 'UTF-8-Mobile#KDDI-B', 'UTF-8-Mobile#SOFTBANK'];
$otherEncodings = ['SJIS', 'UTF-16LE', 'ISO-8859-1', 'EUC-JP'];

// Code point pools: ASCII, 2/3/4-byte, the mobile vendors' private-use emoji, symbols they map, emoji sequences.
$pools = [
	[0x20, 0x7E], [0x00, 0x1F], [0xA0, 0x24F], [0x400, 0x4FF], [0x800, 0xFFF],
	[0x3040, 0x30FF], [0x4E00, 0x4FFF], [0xE001, 0xE05A], [0xE468, 0xE5DF], [0xE63E, 0xE757],
	[0xEA80, 0xEB88], [0xF000, 0xF8FF], [0xFF00, 0xFFFD], [0x1F300, 0x1F64F], [0x1F1E6, 0x1F1FF],
	[0x10000, 0x10FFFF],
];
$specials = ["\u{A9}", "\u{AE}", "\u{2122}", "#\u{20E3}", "1\u{20E3}", "\u{1F1EF}\u{1F1F5}", "\u{1F1FA}\u{1F1F8}",
	"\u{2600}", "\u{2601}", "\u{2614}", "\u{FFFD}", "e\u{301}", "\u{200D}", "\u{FEFF}"];

function cp(int $c): string { return mb_chr($c, 'UTF-8') ?: '?'; }

function gen_valid(array $pools, array $specials): string {
	$shape = mt_rand(0, 9);
	$n = match (true) {
		$shape < 4 => mt_rand(0, 40),
		$shape < 7 => mt_rand(200, 600),
		$shape < 9 => [255, 256, 257, 511, 512, 513, 768, 1024, 1025][mt_rand(0, 8)],
		default => mt_rand(1000, 3000),
	};
	$ascii = mt_rand(0, 3) === 0 ? 95 : mt_rand(0, 100);
	$s = '';
	for ($i = 0; $i < $n; $i++) {
		$r = mt_rand(0, 99);
		if ($r < $ascii) {
			$s .= chr(mt_rand(0x20, 0x7E));
		} elseif ($r < $ascii + 3) {
			$s .= $specials[mt_rand(0, count($specials) - 1)];
		} else {
			$p = $pools[mt_rand(0, count($pools) - 1)];
			$c = mt_rand($p[0], $p[1]);
			if ($c >= 0xD800 && $c <= 0xDFFF) $c = 0x41;
			$s .= cp($c);
		}
	}
	return $s;
}

function gen(array $pools, array $specials): string {
	$s = gen_valid($pools, $specials);
	if ($s !== '' && mt_rand(0, 9) === 0) {
		// invalid: a stray continuation, a truncated sequence or an overlong form
		$bad = ["\x80", "\xBF", "\xC3", "\xE3\x81", "\xF0\x9F\x98", "\xC0\xAF", "\xED\xA0\x80", "\xFF"][mt_rand(0, 7)];
		$pos = mt_rand(0, strlen($s));
		$s = substr($s, 0, $pos) . $bad . substr($s, $pos);
	}
	return $s;
}

function fresh(string $s): string { return strrev(strrev($s)); }

function h($v): string {
	return md5(serialize($v));
}

function call(callable $f) {
	try {
		return $f();
	} catch (Throwable $e) {
		return get_class($e) . ': ' . $e->getMessage();
	}
}

function offsets(int $len): array {
	$o = [0, 1, -1, $len, $len - 1, $len + 1, -$len, -$len - 1, 255, 256, 257, 512, 513, -256, -257, PHP_INT_MAX, -PHP_INT_MAX];
	for ($i = 0; $i < 4; $i++) $o[] = mt_rand(-$len - 2, $len + 2);
	$pick = [];
	for ($i = 0; $i < 6; $i++) $pick[] = $o[mt_rand(0, count($o) - 1)];
	return $pick;
}

for ($case = 0; $case < $count; $case++) {
	$s = gen($pools, $specials);
	$len = mb_strlen($s, 'UTF-8');
	$offs = offsets($len);
	$lens = [null, 0, 1, 2, 255, 256, 257, -1, -2, -256, PHP_INT_MAX, mt_rand(0, $len + 2), -mt_rand(0, $len + 2)];
	$needle = '';
	if ($s !== '') {
		$a = mt_rand(0, max(0, $len - 1));
		$needle = mb_substr($s, $a, mt_rand(1, 4), 'UTF-8');
	}
	if (mt_rand(0, 4) === 0) $needle = ['a', "\u{AE}", "\u{E63E}", "\u{3042}", "\u{1F600}", 'xyz'][mt_rand(0, 5)];
	$marker = ['...', "\u{2026}", '', "\u{AE}"][mt_rand(0, 3)];

	foreach ($encodings as $enc) {
		foreach ([false, true] as $flag) {
			$res = [];
			$mk = function () use ($s, $flag, $enc) {
				$x = fresh($s);
				if ($flag) mb_check_encoding($x, 'UTF-8');
				return $x;
			};
			foreach ($offs as $o) {
				foreach ($lens as $l) {
					$res[] = call(fn() => mb_substr($mk(), $o, $l, $enc));
				}
				$res[] = call(fn() => mb_strpos($mk(), $needle, $o, $enc));
				$res[] = call(fn() => mb_strrpos($mk(), $needle, $o, $enc));
				$res[] = call(fn() => mb_stripos($mk(), $needle, $o, $enc));
				$res[] = call(fn() => mb_strripos($mk(), $needle, $o, $enc));
				$res[] = call(fn() => mb_strimwidth($mk(), $o, mt_rand(0, 300), $marker, $enc));
			}
			foreach ([false, true] as $before) {
				$res[] = call(fn() => mb_strstr($mk(), $needle, $before, $enc));
				$res[] = call(fn() => mb_strrchr($mk(), $needle, $before, $enc));
				$res[] = call(fn() => mb_stristr($mk(), $needle, $before, $enc));
				$res[] = call(fn() => mb_strrichr($mk(), $needle, $before, $enc));
			}
			$res[] = call(fn() => mb_ucfirst($mk(), $enc));
			$res[] = call(fn() => mb_lcfirst($mk(), $enc));
			$res[] = call(fn() => mb_trim($mk(), null, $enc));
			$res[] = call(fn() => mb_ltrim($mk(), " a\u{AE}", $enc));
			$res[] = call(fn() => mb_rtrim($mk(), " a\u{AE}", $enc));
			$res[] = call(fn() => mb_str_pad($mk(), mt_rand(0, $len + 20), "\u{AE}x\u{1F600}", [STR_PAD_LEFT, STR_PAD_RIGHT, STR_PAD_BOTH][mt_rand(0, 2)], $enc));
			$res[] = call(fn() => mb_strlen($mk(), $enc));
			echo "$case $enc ", $flag ? 'flag' : 'plain', ' ', h($res), "\n";
		}
	}
	foreach ($otherEncodings as $enc) {
		$x = mb_convert_encoding($s, $enc, 'UTF-8');
		$n = mb_convert_encoding($needle, $enc, 'UTF-8');
		$res = [];
		foreach ($offs as $o) {
			$res[] = call(fn() => mb_strpos($x, $n, $o, $enc));
			$res[] = call(fn() => mb_stripos($x, $n, $o, $enc));
			$res[] = call(fn() => mb_strrpos($x, $n, $o, $enc));
			$res[] = call(fn() => mb_substr($x, $o, $lens[mt_rand(0, count($lens) - 1)], $enc));
		}
		echo "$case $enc other ", h($res), "\n";
	}
}
