<?php
// Interned (literal) keys, plain and needing escaping, repeated across records, through
// arrays, stdClass and declared properties, under several flag sets. Prints one line per
// flag set; builds must agree.
final class KeyCaseRow
{
	public $id = 1;
	public $name = 'x';
	public $created_at = 'y';
}
function rows(): array
{
	$rows = [];
	for ($i = 0; $i < 3; $i++) {
		$rows[] = ['id' => $i, 'a"b' => 1, 'a/b' => 2, '<tag>' => 3, 'amp&' => 4, "it's" => 5, 'é' => 6,
			"\xff" => 7, "\u{2028}" => 8, '' => 9, 'back\\slash' => 10, "tab\t" => 11, 'plain_key_long_enough' => 12];
		$o = new stdClass;
		$o->id = $i;
		$o->{'a"b'} = 1;
		$o->{'é'} = 2;
		$o->{"\xff"} = 3;
		$rows[] = $o;
		$rows[] = new KeyCaseRow;
	}
	return $rows;
}
$flagSets = [0, JSON_UNESCAPED_SLASHES, JSON_UNESCAPED_UNICODE, JSON_HEX_TAG | JSON_HEX_AMP | JSON_HEX_APOS | JSON_HEX_QUOT,
	JSON_INVALID_UTF8_IGNORE, JSON_INVALID_UTF8_SUBSTITUTE, JSON_PARTIAL_OUTPUT_ON_ERROR, JSON_NUMERIC_CHECK, JSON_PRETTY_PRINT,
	JSON_FORCE_OBJECT | JSON_INVALID_UTF8_SUBSTITUTE];
foreach ($flagSets as $f) {
	$r = json_encode(rows(), $f);
	echo "flags $f ", $r === false ? 'false ' . json_last_error() : md5($r), "\n";
}
echo json_encode(rows()[0], JSON_INVALID_UTF8_SUBSTITUTE), "\n";
