<?php
// Differential fuzz for json_encode() string escaping: random strings around the 16- and
// 32-byte block boundaries, with every escaping and error flag combination. Prints one hash
// per flag set; all builds must print the same lines.
//   php fuzz.php <iterations> <seed>

[$_, $iterations, $seed] = $argv + [null, 20000, 1];
mt_srand((int) $seed);
$pieces = ['a', 'Z', ' ', '0', '"', '\\', '/', '<', '>', '&', "'", "\n", "\r", "\t", "\x00", "\x1f", "\x7f",
	'é', 'ж', '漢', '😀', "\u{2028}", "\u{2029}", "\xC3", "\xE2\x82", "\xF0\x9F", "\xFF", "\x80",
	"\xC0\xAF", "\xC1\xBF", "\xC2\x80", "\xDF\xBF", "\xC2", "\xDF", "\xC2\xC2", "\xD0\xD0\xB6", "\xC2\x7F", "\xC2\xC0",
	"\xE0\xA0\x80", "\xE0\x9F\xBF", "\xED\x9F\xBF", "\xED\xA0\x80", "\xEF\xBF\xBF", "\xE0\x80", "\xEF\xBF", "\xE2\x80\xA8"];
$flagSets = [
	0, JSON_UNESCAPED_SLASHES, JSON_UNESCAPED_UNICODE, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_LINE_TERMINATORS,
	JSON_HEX_TAG | JSON_HEX_AMP | JSON_HEX_APOS | JSON_HEX_QUOT, JSON_INVALID_UTF8_IGNORE, JSON_INVALID_UTF8_SUBSTITUTE,
	JSON_INVALID_UTF8_SUBSTITUTE | JSON_UNESCAPED_UNICODE, JSON_PARTIAL_OUTPUT_ON_ERROR, JSON_NUMERIC_CHECK,
	JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_HEX_TAG,
];
$h = array_fill_keys($flagSets, '');
for ($i = 0; $i < $iterations; $i++) {
	// mostly clean runs with a few special pieces, lengths around block sizes
	$len = [mt_rand(0, 40), mt_rand(14, 18), mt_rand(30, 34), mt_rand(60, 70), mt_rand(0, 300)][mt_rand(0, 4)];
	$s = '';
	while (strlen($s) < $len) {
		$s .= mt_rand(0, 5) ? str_repeat(chr(mt_rand(0x61, 0x7a)), mt_rand(1, 20)) : $pieces[mt_rand(0, count($pieces) - 1)];
	}
	$s = substr($s, 0, $len);
	foreach ($flagSets as $f) {
		$r = json_encode($s, $f);
		$h[$f] = md5($h[$f] . ($r === false ? 'false:' . json_last_error() : $r));
		$r = json_encode(['k' . $s => [$s]], $f);
		$h[$f] = md5($h[$f] . ($r === false ? 'false:' . json_last_error() : $r));
	}
}
foreach ($h as $f => $hash) {
	echo "flags $f $hash\n";
}
