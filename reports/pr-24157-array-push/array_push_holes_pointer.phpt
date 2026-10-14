--TEST--
array_push() onto a full packed array with holes and the internal pointer past the end
--FILE--
<?php
$a = range(0, 15);
for ($i = 0; $i < 14; $i++) unset($a[$i]);
end($a);
next($a);
var_dump(array_push($a, 16, 17));
var_dump(key($a));
var_dump(array_keys($a));
?>
--EXPECT--
int(4)
NULL
array(4) {
  [0]=>
  int(14)
  [1]=>
  int(15)
  [2]=>
  int(16)
  [3]=>
  int(17)
}
