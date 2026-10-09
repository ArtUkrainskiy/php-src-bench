<?php
class R { public $context; static $pos = 0; static $d = "a,b\r\nc,d\r\n";
  function stream_open($p,$m,$o,&$op){ return true;}
  function stream_read($n){ $r = substr(self::$d, self::$pos, $n); self::$pos += strlen($r); return $r; }
  function stream_eof(){ return self::$pos >= strlen(self::$d); }
  function stream_close(){ echo "R close called\n"; }
  function stream_stat(){ return []; }
}
stream_wrapper_register('rt', 'R');
class Holder { public $c; public $self; }
$h = new Holder; $h->self = $h; // cycle: freed only at shutdown
if ($argv[1] === 'csv') { $h->c = Csv\LazyLaxCollection::createFromFile("rt://x"); foreach ($h->c as $r) {} }
else { $h->c = fopen("rt://x", "rb"); fread($h->c, 100); }
echo "end of script\n";
