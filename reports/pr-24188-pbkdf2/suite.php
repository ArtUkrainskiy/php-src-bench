<?php
// hash_pbkdf2() (php-src PR 24188): the input is the algorithm; password and salt are fixed, their
// content does not change the cost. 1 iteration is mostly the fixed part (key preparation,
// allocations), 10 and 1000 iterations the loop the PR changes.
$algos = ['md5', 'sha1', 'sha256', 'sha512', 'sha3-256', 'whirlpool'];
$password = 'correct horse battery staple';
$salt = '0123456789abcdef';
$cases = [];
foreach ([1, 10, 1000] as $iterations) {
    $cases["pbkdf2 x$iterations"] = "hash_pbkdf2(\$s, '$password', '$salt', $iterations)";
}
return ['inputs' => array_combine($algos, $algos), 'cases' => $cases];
