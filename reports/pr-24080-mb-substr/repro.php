<?php
$s = str_repeat("a\u{AE}b", 2);
var_dump(bin2hex(mb_substr($s, 1, 1, 'UTF-8-Mobile#DOCOMO')));
mb_substr($s, -1, null, 'UTF-8-Mobile#DOCOMO'); // counts the length, which marks $s as valid UTF-8
var_dump(bin2hex(mb_substr($s, 1, 1, 'UTF-8-Mobile#DOCOMO')));
