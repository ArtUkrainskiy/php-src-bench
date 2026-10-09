<?php
class W { public $context; static $data = ''; static $log = [];
  function stream_open($p,$m,$o,&$op){ self::$log[] = "open $m opt=$o"; return true;}
  function stream_write($d){ self::$data .= $d; return strlen($d);}
  function stream_flush(){ self::$log[] = "flush"; return false; }
  function stream_close(){ self::$log[] = "close"; }
  function stream_eof(){ return true; }
  function stream_read($n){ return ''; }
  function stream_stat(){ return []; }
}
stream_wrapper_register('wt', 'W');
try { Csv\collection_to_file("wt://x", [[1]]); echo "no error\n"; } catch (Throwable $e) { echo get_class($e), ": ", $e->getMessage(), "\n"; }
print_r(W::$log); var_dump(W::$data);
$f = fopen("wt://y", "wb"); var_dump($f); fwrite($f, "q"); var_dump(fflush($f)); fclose($f); print_r(W::$log);
// createFromFile with user wrapper, then let object die at shutdown with refcount 2
class R { public $context; static $pos = 0; static $d = "a,b\r\nc,d\r\n";
  function stream_open($p,$m,$o,&$op){ return true;}
  function stream_read($n){ $r = substr(self::$d, self::$pos, $n); self::$pos += strlen($r); return $r; }
  function stream_eof(){ return self::$pos >= strlen(self::$d); }
  function stream_close(){ echo "R close called\n"; }
  function stream_stat(){ return []; }
}
stream_wrapper_register('rt', 'R');
$c = Csv\LazyLaxCollection::createFromFile("rt://x");
foreach ($c as $row) echo json_encode($row), "\n";
$c2 = $c; // refcount 2 -> survives until free_object_storage
echo "end of script\n";
