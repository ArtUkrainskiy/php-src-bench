<?php
$mode = $argv[1] ?? 'none'; $n = (int)($argv[2] ?? 100000); $x = null;
if ($mode === 'baseline') { for ($i = 0; $i < $n; $i++) { strlen(''); } }
else { for ($i = 0; $i < $n; $i++) { strlen($x); } }   // "Passing null to parameter #1 ($string) of type string is deprecated"
