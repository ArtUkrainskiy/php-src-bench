<?php
use function Csv\{collection_to_buffer, collection_to_file};

class Resumer { function __toString(): string { global $gen; $gen->next(); return str_repeat("x", 64); } }
function g() { yield [new Resumer, str_repeat("a", 64), str_repeat("b", 64), str_repeat("c", 64)]; yield [str_repeat("q", 64), 'r', 's', 't']; }
$gen = g();
try { var_dump(collection_to_buffer($gen)); } catch (Throwable $e) { echo get_class($e), ": ", $e->getMessage(), "\n"; }

class Overwriter { function __toString(): string { global $ai; $ai[0] = str_repeat("z", 64); return str_repeat("y", 64); } }
$ai = new ArrayIterator([[new Overwriter, str_repeat("a", 64), str_repeat("b", 64)]]);
try { var_dump(collection_to_buffer($ai)); } catch (Throwable $e) { echo get_class($e), ": ", $e->getMessage(), "\n"; }

// outer array with refcount 1 reachable through a Stringable holding a reference
class RefHolder { public $ref; function __toString(): string { $this->ref = []; return "w"; } }
$h = new RefHolder; $arr = [[$h, str_repeat("m", 64)]]; $h->ref = &$arr;
try { var_dump(collection_to_buffer($arr)); } catch (Throwable $e) { echo get_class($e), ": ", $e->getMessage(), "\n"; }
echo "done\n";
