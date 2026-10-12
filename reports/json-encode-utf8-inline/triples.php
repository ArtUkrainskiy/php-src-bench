<?php
// Every three-byte sequence with a lead byte E0..EF, alone and inside ASCII, under each
// UTF-8 related flag set. Prints one hash per flag set; builds must agree.
$flagSets = [0, JSON_UNESCAPED_UNICODE, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_LINE_TERMINATORS,
	JSON_INVALID_UTF8_IGNORE, JSON_INVALID_UTF8_SUBSTITUTE, JSON_INVALID_UTF8_SUBSTITUTE | JSON_UNESCAPED_UNICODE];
foreach ($flagSets as $f) {
	$h = '';
	for ($a = 0xe0; $a < 0xf0; $a++) {
		for ($b = 0; $b < 256; $b++) {
			for ($c = 0; $c < 256; $c++) {
				$t = chr($a) . chr($b) . chr($c);
				$r = json_encode($t, $f);
				$h = md5($h . ($r === false ? 'F' : $r) . ':e' . json_last_error());
				$r = json_encode('x' . $t . 'y', $f);
				$h = md5($h . ($r === false ? 'F' : $r) . ':e' . json_last_error());
			}
		}
	}
	echo "flags $f $h\n";
}
