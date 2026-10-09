<?php
// 1. sparse collection (hole after unset)
$a = [['a','b'],['c','d'],['e','f']]; unset($a[1]);
echo "sparse: "; echo json_encode(Csv\collection_to_buffer($a)), "\n";
// 2. row_to_array('')
echo "empty row: "; var_dump(Csv\row_to_array(''));
// 3. multibyte enclosure doubled
$enc = 'ab';
$row = Csv\array_to_row(['x"ab"y', 'z'], ',', $enc);
echo "mb enclosure row: ", json_encode($row), " -> ", json_encode(Csv\row_to_array($row, ',', $enc)), "\n";
// 4. iterator throwing
function gen() { yield ['a']; throw new Exception('boom'); }
try { Csv\collection_to_buffer(gen()); } catch (Exception $e) { echo "iterator exc: ", $e->getMessage(), "\n"; }
echo "done\n";
