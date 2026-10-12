<?php
// One json_encode() case per process: ns per call (median of 7) and an md5 of the output,
// to compare builds. With "list" prints the case names.
//   php cases.php <case|list> [calls]
// With a call count, makes exactly that many calls and prints nothing (for perf stat).

function text(int $len, callable $chunk): string
{
	$s = '';
	for ($i = 0; strlen($s) < $len; $i++) {
		$s .= $chunk($i);
	}
	$s = substr($s, 0, $len);
	// do not end in the middle of a UTF-8 character
	while ($s !== '' && !preg_match('//u', $s)) {
		$s = substr($s, 0, -1);
	}
	return $s;
}

final class JsonCaseOrder
{
	public int $id;
	public int $user_id;
	public string $status = 'paid';
	public string $title;
	public int $amount_cents;
	public string $currency = 'RUB';
	public string $created_at = '2026-01-01T00:00:37+00:00';
	public string $updated_at = '2026-01-01T01:00:37+00:00';
	public string $comment;
	public int $flags;

	public function __construct(int $i)
	{
		$this->id = $i;
		$this->user_id = $i * 7;
		$this->title = "Order number $i";
		$this->amount_cents = $i * 1531;
		$this->comment = "note $i";
		$this->flags = $i % 8;
	}
}

function mb_substr_safe(string $s): string
{
	$s = substr($s, 0, 4096);
	while ($s !== '' && !preg_match('//u', $s)) {
		$s = substr($s, 0, -1);
	}
	return $s;
}

$words = static fn ($i) => ['lorem ', 'ipsum ', 'dolor ', 'sit ', 'amet, ', 'consectetur ', 'adipiscing ', 'elit ', "1234 "][$i % 9];

$cases = [
	'ascii-16' => [str_repeat('a', 16), 0],
	'ascii-256' => [text(256, $words), 0],
	'ascii-4k' => [text(4096, $words), 0],
	'ascii-64k' => [text(65536, $words), 0],
	'html-4k' => [text(4096, static fn ($i) => ['<p class="x">', 'Tom &amp; Jerry ', "it's ", 'text text text ', '</p>'][$i % 5]), 0],
	'url-4k' => [text(4096, static fn ($i) => "https://example.com/a/b/c/$i?x=1 "), 0],
	'url-4k-unescaped-slashes' => [text(4096, static fn ($i) => "https://example.com/a/b/c/$i?x=1 "), JSON_UNESCAPED_SLASHES],
	'esc-every-16' => [text(4096, static fn ($i) => 'abcdefghijklmno"'), 0],
	'esc-every-8' => [text(4096, static fn ($i) => 'abcdefg"'), 0],
	'esc-every-byte' => [str_repeat('"', 4096), 0],
	'newlines-every-40' => [text(4096, static fn ($i) => str_repeat('x', 39) . "\n"), 0],
	'cyrillic-4k' => [text(4096, static fn ($i) => ['привет ', 'мир ', 'текст '][$i % 3]), 0],
	'cyrillic-4k-unescaped' => [text(4096, static fn ($i) => ['привет ', 'мир ', 'текст '][$i % 3]), JSON_UNESCAPED_UNICODE],
	'cjk-4k' => [text(4095, static fn ($i) => ['漢字', '中文', '日本語'][$i % 3]), 0],
	'cjk-4k-unescaped' => [text(4095, static fn ($i) => ['漢字', '中文', '日本語'][$i % 3]), JSON_UNESCAPED_UNICODE],
	'french-4k' => [text(4096, static fn ($i) => ['élève ', 'à ', 'été ', 'garçon ', 'Noël ', 'le ', 'chat ', 'mange '][$i % 8]), 0],
	'french-4k-unescaped' => [text(4096, static fn ($i) => ['élève ', 'à ', 'été ', 'garçon ', 'Noël ', 'le ', 'chat ', 'mange '][$i % 8]), JSON_UNESCAPED_UNICODE],
	'ascii-random-utf8-unescaped' => [(static function () {
		mt_srand(42);
		$s = '';
		while (strlen($s) < 4096) {
			$s .= str_repeat('a', mt_rand(0, 60)) . 'é';
		}
		return mb_substr_safe($s);
	})(), JSON_UNESCAPED_UNICODE],
	'ascii-random-utf8' => [(static function () {
		mt_srand(42);
		$s = '';
		while (strlen($s) < 4096) {
			$s .= str_repeat('a', mt_rand(0, 60)) . 'é';
		}
		return mb_substr_safe($s);
	})(), 0],
	'ascii-rare-utf8-unescaped' => [text(4096, static fn ($i) => str_repeat('a', 30) . 'é'), JSON_UNESCAPED_UNICODE],
	'api-1000-records' => [array_map(static fn ($i) => [
		'id' => $i, 'user_id' => $i * 7, 'status' => 'paid', 'title' => "Order number $i", 'amount_cents' => $i * 1531,
		'currency' => 'RUB', 'created_at' => '2026-01-01T00:00:37+00:00', 'updated_at' => '2026-01-01T01:00:37+00:00',
		'comment' => "note $i", 'flags' => $i % 8,
	], range(1, 1000)), 0],
	'objects-1000-records' => [array_map(static fn ($i) => new JsonCaseOrder($i), range(1, 1000)), 0],
	'object-100-keys' => [array_combine(array_map(static fn ($i) => "field_$i", range(1, 100)), range(1, 100)), 0],
];

if ($argv[1] === 'list') {
	echo implode("\n", array_keys($cases)), "\n";
	return;
}
[$value, $flags] = $cases[$argv[1]];

if (isset($argv[2])) {
	for ($i = 0, $n = (int) $argv[2]; $i < $n; $i++) {
		json_encode($value, $flags);
	}
	return;
}

$out = json_encode($value, $flags);
$t = hrtime(true);
for ($n = 0; hrtime(true) - $t < 20_000_000; $n++) {
	json_encode($value, $flags);
}
$iters = max(1, $n);
$times = [];
for ($r = 0; $r < 7; $r++) {
	$t = hrtime(true);
	for ($i = 0; $i < $iters; $i++) {
		json_encode($value, $flags);
	}
	$times[] = (hrtime(true) - $t) / $iters;
}
sort($times);
printf("%s %.1f %d %s\n", $argv[1], $times[3], strlen($out), md5($out));
