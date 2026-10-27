<?php
/* ASan/UBSan exercise for the base64_decode() quads change. Fuzzes 40000 iterations x 2 modes
 * = 80k decodes over clean base64, MIME-wrapped, alphabet+noise and pure-random input. Run the
 * ASan+UBSan build with USE_ZEND_ALLOC=0; it prints "done <n>" and must emit no sanitizer output.
 * Seeded (mt_srand) for the input shapes; the decoded content is not checked here (that is the
 * differential's job) — this only exercises memory safety. */
mt_srand(1);
$alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';
$noise=[' ',"\n","\r\n","\t",'=','==','-','_',"\0","\xFF",'*'];
$n=0;
for($it=0;$it<40000;$it++){
  $k=mt_rand(0,3);
  if($k==0){ $s=base64_encode(random_bytes(mt_rand(1,300))); }
  elseif($k==1){ $s=implode("\n",str_split(base64_encode(random_bytes(mt_rand(1,4000))),mt_rand(1,76)))."\n"; }
  elseif($k==2){ $s=''; $m=mt_rand(0,200); for($i=0;$i<$m;$i++){ $s .= (mt_rand(0,4)? $alpha[mt_rand(0,63)] : $noise[mt_rand(0,count($noise)-1)]); } }
  else { $s=random_bytes(mt_rand(1,120)); }
  $n += strlen((string)base64_decode($s,false));
  $n += strlen((string)base64_decode($s,true));
}
echo "done $n\n";
