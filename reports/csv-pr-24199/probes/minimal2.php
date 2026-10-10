<?php
mt_srand(3); $d='xy'; $e='xyx'; $eol="\n"; $alpha=['x','y','z'];
$best=null;
for ($i=0;$i<200000;$i++){ $nf=mt_rand(1,2); $row=[]; for($f=0;$f<$nf;$f++){ $s=''; $l=mt_rand(1,5); for($j=0;$j<$l;$j++) $s.=$alpha[mt_rand(0,2)]; $row[]=$s; }
  try { $line=Csv\array_to_row($row,$d,$e,$eol); $back=Csv\row_to_array($line,$d,$e,$eol); if ($back===$row) continue; $res='parsed as '.json_encode($back); }
  catch (Throwable $t){ $res=get_class($t).': '.$t->getMessage(); }
  $len=strlen(implode('',$row)); if ($best===null || $len<$best[0]) $best=[$len,$row,$line,$res]; }
printf("%s -> %s  %s\n", json_encode($best[1]), json_encode($best[2]), $best[3]);
