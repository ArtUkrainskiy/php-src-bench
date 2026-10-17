<?php
// Mutations of the list assignment from an array literal (php-src PR 24180), on the head build.
// No differential test: destructor order differs from master on purpose; the tests carry the expectations.
$f = 'Zend/zend_compile.c';

return [
    'tests' => ['Zend/tests/list', 'ext/opcache/tests/opt/list_assign_from_array_literal.phpt'],
    'mutations' => [
        'a variable value is not copied before the assignments' => ['file' => $f,
            'from' => "zend_compile_expr(value, values->child[i]->child[0]);\n\t\tif (value->op_type == IS_CV) {",
            'to' => "zend_compile_expr(value, values->child[i]->child[0]);\n\t\tif (0) {"],
        'values assigned to the targets in reverse order' => ['file' => $f,
            'from' => 'zend_emit_assign_znode(target_ast, &value_nodes[i]);',
            'to' => 'zend_emit_assign_znode(target_ast, &value_nodes[count - 1 - i]);'],
        'extra values accepted' => ['file' => $f,
            'from' => 'values->children != targets->children', 'to' => 'values->children < targets->children'],
        'the condition list of a for compiled as unused' => ['file' => $f,
            'from' => '(i + 1 < list->children || !last_result_used)', 'to' => '(true)'],
        'nested list targets accepted' => ['file' => $f,
            'from' => "\n\t\t || target_ast->child[0]->kind == ZEND_AST_ARRAY) {", 'to' => ') {'],
        'keyed values accepted' => ['file' => $f,
            'from' => 'value_ast->kind != ZEND_AST_ARRAY_ELEM || value_ast->child[1] != NULL', 'to' => 'value_ast->kind != ZEND_AST_ARRAY_ELEM'],
    ],
];
