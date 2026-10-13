<?php
// Four-byte sequences with a lead byte F0..FF: every second and third byte, the fourth byte
// from the continuation boundaries, alone, inside ASCII and truncated. One hash per flag set;
// builds must agree.
$flagSets = [0, JSON_UNESCAPED_UNICODE, JSON_INVALID_UTF8_SUBSTITUTE | JSON_UNESCAPED_UNICODE];
$fourth = [0x00, 0x7f, 0x80, 0x81, 0xbf, 0xc0, 0xff];
foreach ($flagSets as $f) {
	$h = '';
	$add = static function (string $t) use (&$h, $f) {
		$r = json_encode($t, $f);
		$h = md5($h . ($r === false ? 'F' : $r) . ':e' . json_last_error());
	};
	for ($a = 0xf0; $a <= 0xff; $a++) {
		for ($b = 0; $b < 256; $b++) {
			$add(chr($a) . chr($b));
			for ($c = 0; $c < 256; $c++) {
				$p = chr($a) . chr($b) . chr($c);
				$add($p);
				$add('x' . $p);
				foreach ($fourth as $d) {
					$t = $p . chr($d);
					$add($t);
					$add('x' . $t . 'y');
				}
			}
		}
	}
	echo "flags $f $h\n";
}
