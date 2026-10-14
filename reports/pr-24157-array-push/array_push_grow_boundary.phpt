--TEST--
array_push() appends several values across a table size boundary
--FILE--
<?php
$a = range(1, 7);
var_dump(array_push($a, 8, 9));
var_dump($a === range(1, 9));

$a = range(1, 8);
var_dump(array_push($a, ...range(9, 17)));
var_dump($a === range(1, 17));
?>
--EXPECT--
int(9)
bool(true)
int(17)
bool(true)
