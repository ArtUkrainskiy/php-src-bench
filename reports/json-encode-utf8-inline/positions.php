<?php
// Every byte value at every position of ASCII strings 1..24 bytes long, under a few flag
// sets. Prints one hash per flag set; builds must agree.
$flagSets = [0, JSON_UNESCAPED_SLASHES, JSON_HEX_TAG | JSON_HEX_AMP | JSON_HEX_APOS | JSON_HEX_QUOT,
	JSON_INVALID_UTF8_SUBSTITUTE | JSON_UNESCAPED_UNICODE];
foreach ($flagSets as $f) {
	$h = '';
	for ($len = 1; $len <= 24; $len++) {
		for ($p = 0; $p < $len; $p++) {
			for ($b = 0; $b < 256; $b++) {
				$s = str_repeat('a', $len);
				$s[$p] = chr($b);
				$r = json_encode($s, $f);
				$h = md5($h . ($r === false ? 'F' . json_last_error() : $r));
			}
		}
	}
	echo "flags $f $h\n";
}
