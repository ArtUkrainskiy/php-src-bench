<?php
// Every byte pair, alone, after ASCII and before ASCII, plus every lone byte at the end,
// under each UTF-8 related flag set. Prints one hash per flag set; builds must agree.
$flagSets = [0, JSON_UNESCAPED_UNICODE, JSON_INVALID_UTF8_IGNORE, JSON_INVALID_UTF8_SUBSTITUTE,
	JSON_INVALID_UTF8_SUBSTITUTE | JSON_UNESCAPED_UNICODE, JSON_PARTIAL_OUTPUT_ON_ERROR];
foreach ($flagSets as $f) {
	$h = '';
	for ($a = 0; $a < 256; $a++) {
		$r = json_encode('abc' . chr($a), $f);
		$h = md5($h . ($r === false ? 'F' . json_last_error() : $r));
		for ($b = 0; $b < 256; $b++) {
			$p = chr($a) . chr($b);
			foreach ([$p, 'x' . $p . 'y', str_repeat('q', 20) . $p] as $s) {
				$r = json_encode($s, $f);
				$h = md5($h . ($r === false ? 'F' . json_last_error() : $r));
			}
		}
	}
	echo "flags $f $h\n";
}
