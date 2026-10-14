<?php
// Differential test for charset resolution in the html functions (determine_charset()).
// For every charset hint: htmlspecialchars(), htmlentities(), html_entity_decode() and
// get_html_translation_table() results plus the warnings, hashed per section.
//   php -n difftest.php [random-count] [seed]

$randomCount = (int) ($argv[1] ?? 10000);
$seed = (int) ($argv[2] ?? 1);
$warn = '';
set_error_handler(static function ($no, $str) use (&$warn) { $warn .= "[$no] $str\n"; return true; });

const ALIASES = ['ISO-8859-1', 'ISO8859-1', 'ISO-8859-15', 'ISO8859-15', 'utf-8', 'cp1252', 'Windows-1252', '1252', 'BIG5', '950',
	'GB2312', '936', 'BIG5-HKSCS', 'Shift_JIS', 'SJIS', '932', 'SJIS-win', 'CP932', 'EUCJP', 'EUC-JP', 'eucJP-win', 'KOI8-R',
	'koi8-ru', 'koi8r', 'cp1251', 'Windows-1251', 'win-1251', 'iso8859-5', 'iso-8859-5', 'cp866', '866', 'ibm866', 'MacRoman'];

$sections = [];
$counts = [];
$probe = static function (string $section, ?string $hint) use (&$sections, &$counts, &$warn) {
	$warn = '';
	$r = [
		htmlspecialchars("<a href='x'>T&amp;é\xE9\xC3\xA9\x80</a>", ENT_QUOTES, $hint),
		htmlspecialchars("ok \xE9", ENT_QUOTES | ENT_SUBSTITUTE, $hint),
		htmlentities("é ü ß \xE9\xFC \xA4 € x", ENT_QUOTES, $hint),
		html_entity_decode('&eacute;&#233;&#x20AC;&euro;&amp;&lt;&nbsp;&copy;&hellip;', ENT_QUOTES | ENT_HTML5, $hint),
		md5(serialize(get_html_translation_table(HTML_ENTITIES, ENT_QUOTES | ENT_HTML5, $hint ?? 'UTF-8'))),
	];
	$sections[$section] ??= hash_init('sha256');
	hash_update($sections[$section], var_export($hint, true) . '|' . bin2hex(serialize($r)) . '|' . $warn . "\n");
	$counts[$section] = ($counts[$section] ?? 0) + 1;
};

// 1. every alias, in several case forms
foreach (ALIASES as $a) {
	foreach ([$a, strtolower($a), strtoupper($a), implode('', array_map(static fn ($c, $i) => $i % 2 ? strtoupper($c) : strtolower($c), str_split($a), array_keys(str_split($a))))] as $h) {
		$probe('aliases', $h);
	}
}
// 2. every prefix, every one-byte suffix, every one-byte replacement of each alias and of "utf-8" spellings
foreach (array_merge(ALIASES, ['UTF-8', 'utf8', 'UTF_8', 'u', 'ut', 'utf', 'utf-', 'utf-88', 'utf-8 ', ' utf-8']) as $a) {
	for ($l = 0; $l <= strlen($a); $l++) $probe('prefixes', substr($a, 0, $l));
	foreach (["\0", ' ', '-', '8', 'x', "\xFF"] as $c) $probe('suffixes', $a . $c);
	for ($p = 0; $p < strlen($a); $p++) {
		foreach (["\0", 'a', 'Z', '-', '_', '9', "\x80", chr(ord($a[$p]) ^ 0x20), chr(ord($a[$p]) + 1)] as $c) {
			$m = $a; $m[$p] = $c; $probe('mutations', $m);
		}
	}
}
// 3. all one- and two-byte strings
for ($a = 0; $a < 256; $a++) {
	$probe('one byte', chr($a));
	for ($b = 0; $b < 256; $b++) $probe('two bytes', chr($a) . chr($b));
}
// 4. empty and null hints under different default_charset / internal_encoding
foreach (['', 'UTF-8', 'utf-8', 'ISO-8859-1', 'cp1251', 'nonsense', 'UTF8', 'Shift_JIS'] as $dc) {
	foreach (['', 'UTF-8', 'koi8-r', 'bogus'] as $ie) {
		ini_set('default_charset', $dc);
		ini_set('internal_encoding', $ie);
		$probe('defaults', null);
		$probe('defaults', '');
		$probe('defaults', 'utf-8');
	}
}
ini_set('default_charset', 'UTF-8');
ini_set('internal_encoding', '');
// 5. random byte strings up to 31 bytes, biased towards hint-like characters
mt_srand($seed);
$alpha = 'utf-8UTF_ISOiso859cpCPwinWINkoiKOIbigBIGsjisSJISeucEUCmacMAC0123456789-_ ';
for ($k = 0; $k < $randomCount; $k++) {
	$len = mt_rand(0, 31);
	$s = '';
	for ($i = 0; $i < $len; $i++) $s .= mt_rand(0, 3) ? $alpha[mt_rand(0, strlen($alpha) - 1)] : chr(mt_rand(0, 255));
	$probe('random', $s);
}

foreach ($sections as $name => $ctx) {
	echo str_pad($name, 12), str_pad((string) $counts[$name], 8, ' ', STR_PAD_LEFT), '  ', hash_final($ctx), "\n";
}
