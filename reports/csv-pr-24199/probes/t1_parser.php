<?php
function t(string $label, callable $f) {
    echo "== $label: ";
    try { $r = $f(); echo json_encode($r, JSON_UNESCAPED_SLASHES|JSON_INVALID_UTF8_SUBSTITUTE), "\n"; }
    catch (\Throwable $e) { echo get_class($e), ": ", $e->getMessage(), "\n"; }
}
use function Csv\{row_to_array, array_to_row, buffer_to_collection, buffer_to_collection_lax, collection_to_buffer};

t('closing enclosure then garbage "a"b', fn() => row_to_array('"a"b'));
t('closing enclosure then garbage then enclosure "a"b"', fn() => row_to_array('"a"b"'));
t('"a" ,b (space after close)', fn() => row_to_array('"a" ,b'));
t('unterminated "abc', fn() => row_to_array('"abc'));
t('lone "', fn() => row_to_array('"'));
t('a,"', fn() => row_to_array('a,"'));
t('""""', fn() => row_to_array('""""'));
t('"" ', fn() => row_to_array('""'));
t('trailing delimiter a,b,', fn() => row_to_array('a,b,'));
t('trailing EOL a,b\r\n', fn() => row_to_array("a,b\r\n"));
t('data after EOL a,b\r\nc,d', fn() => row_to_array("a,b\r\nc,d"));
t('empty', fn() => row_to_array(""));
t('only EOL', fn() => row_to_array("\r\n"));
t('bare \n in field with CRLF eol', fn() => row_to_array("a\nb,c"));
t('\r alone', fn() => row_to_array("a\rb,c"));
t('delim ,, enclosure ,', fn() => row_to_array('a,,b', ',,', ','));
t('delim , enclosure ,,', fn() => row_to_array('a,,b', ',', ',,'));
t('delim \n eol \n\n roundtrip', function() { $r = array_to_row(['a','b'], "\n", '"', "\n\n"); return [bin2hex($r), row_to_array($r, "\n", '"', "\n\n")]; });
t('eol prefix of delimiter: delim "ab", eol "a"', fn() => row_to_array("xaby", "ab", '"', "a"));
t('enclosure prefix of delimiter: enc "a", delim "ab"', fn() => row_to_array("xaby", "ab", 'a', "\n"));
t('NUL delimiter', fn() => row_to_array("a\0b\0\0c", "\0"));
t('NUL in data', fn() => row_to_array("a\0b,\"c\0d\""));
t('NUL enclosure', fn() => row_to_array("\0a,b\0,c", ",", "\0"));
t('eol with NUL', fn() => row_to_array("a,b\0\nc", ",", '"', "\0\n"));
t('enclosure doubled multibyte XY', fn() => row_to_array("XYaXYXYbXY,c", ",", "XY"));
t('multibyte enclosure tail bytes YX? enc "XY" data XYaXYY', fn() => row_to_array("XYaXYY,c", ",", "XY"));
t('BOM', fn() => row_to_array("\xEF\xBB\xBF\"a\",b"));
t('enclosed field containing EOL', fn() => row_to_array("\"a\r\nb\",c"));
t('buffer: trailing blank line 2 cols strict', fn() => buffer_to_collection("a,b\r\n\r\n"));
t('buffer: trailing blank line 2 cols lax', fn() => buffer_to_collection_lax("a,b\r\n\r\n"));
t('buffer: just CRLF', fn() => buffer_to_collection("\r\n"));
t('buffer: empty', fn() => buffer_to_collection(""));
t('buffer: unterminated enclosure spans rows', fn() => buffer_to_collection("a,\"b\r\nc,d\r\n"));
t('buffer: error on row 2', fn() => buffer_to_collection("a,b\r\nc,d\"e\r\n"));
t('buffer: first row 1 field second 2 fields msg', fn() => buffer_to_collection("a\r\nc,d\r\n"));
t('empty array -> row', fn() => bin2hex(array_to_row([])));
t('[""] -> row', fn() => bin2hex(array_to_row([""])));
t('roundtrip [[]]', fn() => buffer_to_collection(collection_to_buffer([[]])));
t('roundtrip ["", ""]', fn() => row_to_array(array_to_row(["", ""])));
t('roundtrip ["a"] vs [] eol only', fn() => row_to_array(array_to_row([])));
t('writer: field with only \r', fn() => bin2hex(array_to_row(["a\rb"])));
t('writer: field with eol "|" custom', fn() => array_to_row(["a|b", "c"], ",", '"', "|"));
t('writer: enclosure is multi "XY" doubling', fn() => array_to_row(["aXYb"], ",", "XY"));
t('writer: field equal to enclosure', fn() => array_to_row(['"']));
t('writer: null,true,false,int,float', fn() => array_to_row([null, true, false, 1, 1.5, 1e100, -0.0]));
t('writer: nested array', fn() => array_to_row([[1]]));
t('writer: object no toString', fn() => array_to_row([new stdClass]));
t('writer: Stringable', fn() => array_to_row([new class { function __toString(): string { return "x,y"; } }]));
t('writer: Stringable throws', fn() => array_to_row([new class { function __toString(): string { throw new RuntimeException("boom"); } }]));
t('writer: non packed keys ignored', fn() => array_to_row(['z' => 1, 'a' => 2, 5 => 3]));
t('writer: reference element', function() { $x = "r"; $a = [&$x]; return array_to_row($a); });
t('writer: delimiter inside enclosure? delim "ab", enclosure "b"', fn() => array_to_row(["xaby"], "ab", "b"));
t('writer: ValueError empty delim', fn() => array_to_row(["a"], ""));
t('writer: delim==eol', fn() => array_to_row(["a"], "\r\n"));
t('writer: enc==eol', fn() => array_to_row(["a"], ",", "\r\n"));
t('writer: delim==enc', fn() => array_to_row(["a"], ",", ","));
t('collection: non-array element 0', fn() => collection_to_buffer([1]));
t('collection: non-array element 1', fn() => collection_to_buffer([[1], 2]));
t('collection: width mismatch', fn() => collection_to_buffer([[1,2], [3]]));
t('collection: generator yields non-array mid', fn() => collection_to_buffer((function() { yield [1]; yield 2; })()));
t('collection: generator throws mid', fn() => collection_to_buffer((function() { yield [1]; throw new LogicException("mid"); })()));
t('collection: empty generator', fn() => bin2hex(collection_to_buffer((function() { yield from []; })())));
t('collection: IteratorAggregate returning non-traversable', fn() => collection_to_buffer(new class implements IteratorAggregate { function getIterator(): Iterator { throw new DomainException("gi"); } }));
t('collection: LazyLaxCollection passthrough', fn() => collection_to_buffer(Csv\LazyLaxCollection::createFromBuffer("a,b\r\nc,d\r\n")));
t('long field 1M', fn() => strlen(row_to_array(array_to_row([str_repeat('"', 500000)]))[0]));
t('many fields 100k', fn() => count(row_to_array(array_to_row(array_fill(0, 100000, 'x')))));
// deep eq round trip
$cases = [['a','b'], ['"'], ["\r\n"], ["", ""], ["a\"b", "c,d", "e\r\nf"], ["\0", "\0\0"], [" a ", "b "]];
foreach ($cases as $c) { $r = row_to_array(array_to_row($c)); echo (($r === $c) ? "RT ok " : "RT MISMATCH ") . json_encode($c) . " -> " . json_encode($r) . "\n"; }
