<?php
// utf8_decode() over every byte pair and every E0..EF triple, alone and inside ASCII.
// Prints one hash; builds must agree.
error_reporting(E_ALL & ~E_DEPRECATED);
$h = '';
for ($a = 0; $a < 256; $a++) {
	$h = md5($h . utf8_decode('ab' . chr($a)));
	for ($b = 0; $b < 256; $b++) {
		$p = chr($a) . chr($b);
		$h = md5($h . utf8_decode($p) . '|' . utf8_decode('x' . $p . 'y'));
		if ($a >= 0xe0 && $a < 0xf0) {
			for ($c = 0; $c < 256; $c++) {
				$h = md5($h . utf8_decode($p . chr($c)) . '|' . utf8_decode('x' . $p . chr($c)));
			}
		}
	}
}
echo "$h\n";
