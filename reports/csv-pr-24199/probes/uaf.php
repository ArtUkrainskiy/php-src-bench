<?php
class S { function __toString(): string { $GLOBALS['gen']->next(); return "s"; } }
function rows() { yield [new S, 'b']; yield ['c','d']; }
$gen = rows();
echo json_encode(Csv\collection_to_buffer($gen)), "\n";
