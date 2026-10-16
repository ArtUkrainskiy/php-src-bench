<?php
// Which mbstring functions re-encode UTF-8 for the mobile variants and which return the input bytes.
$s = implode('', ["a", "\u{AE}", "b"]);
foreach (['UTF-8-Mobile#DOCOMO', 'UTF-8-Mobile#KDDI-A', 'UTF-8-Mobile#KDDI-B', 'UTF-8-Mobile#SOFTBANK'] as $enc) {
	echo $enc, "\n";
	printf("  mb_substr(\$s, 1, 1)      %s\n", bin2hex(mb_substr($s, 1, 1, $enc)));
	printf("  mb_str_split(\$s)[1]      %s\n", bin2hex(mb_str_split($s, 1, $enc)[1]));
	printf("  mb_strcut(\$s, 1, 2)      %s\n", bin2hex(mb_strcut($s, 1, 2, $enc)));
	printf("  mb_strstr(\$s, 'b', true) %s\n", bin2hex(mb_strstr($s, 'b', true, $enc)));
	printf("  mb_convert_encoding      %s\n", bin2hex(mb_convert_encoding($s, $enc, $enc)));
	printf("  mb_strlen                %d\n", mb_strlen($s, $enc));
}
