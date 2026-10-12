<?php
// utf8_decode() ns per call on 4 KiB of text. php udecode-bench.php <latin1|cyrillic|ascii> [calls]
error_reporting(E_ALL & ~E_DEPRECATED);
$chunks = ['latin1' => ['élève ', 'à ', 'été ', 'garçon ', 'Noël '], 'cyrillic' => ['привет ', 'мир '], 'ascii' => ['lorem ', 'ipsum ']][$argv[1]];
$s = '';
for ($i = 0; strlen($s) < 4096; $i++) { $s .= $chunks[$i % count($chunks)]; }
if (isset($argv[2])) { for ($i = 0; $i < (int) $argv[2]; $i++) { utf8_decode($s); } return; }
echo md5(utf8_decode($s)), "\n";
