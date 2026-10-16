--TEST--
mb_substr() gives the same result for strings already checked as valid UTF-8
--EXTENSIONS--
mbstring
--FILE--
<?php
// 1-, 2-, 3- and 4-byte characters, 400 characters in 1000 bytes
function make() { return str_repeat("a\u{E9}\u{20AC}\u{1F600}", 100); }

foreach ([0, 1, 255, 256, 257, 399, 400, 401, -1, -257] as $from) {
    foreach ([null, 0, 1, 300, -1] as $len) {
        $checked = make();
        mb_check_encoding($checked, 'UTF-8');
        if (mb_substr(make(), $from, $len, 'UTF-8') !== mb_substr($checked, $from, $len, 'UTF-8')) {
            echo "differs: from $from, length ", var_export($len, true), "\n";
        }
    }
}

// The UTF-8-Mobile encodings convert U+00AE to a carrier code point, checked or not
foreach (['UTF-8-Mobile#DOCOMO', 'UTF-8-Mobile#KDDI-A', 'UTF-8-Mobile#SOFTBANK'] as $enc) {
    $s = str_repeat("a\u{AE}b", 2);
    $before = bin2hex(mb_substr($s, 1, 1, $enc));
    mb_check_encoding($s, 'UTF-8');
    var_dump($before, bin2hex(mb_substr($s, 1, 1, $enc)));
}
?>
--EXPECT--
string(6) "ee9cb6"
string(6) "ee9cb6"
string(6) "ee9599"
string(6) "ee9599"
string(6) "ee898f"
string(6) "ee898f"
