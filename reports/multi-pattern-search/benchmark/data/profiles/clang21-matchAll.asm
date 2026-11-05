
clang21-strmatch.so:     file format elf64-x86-64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .plt.got:

Disassembly of section .text:

0000000000003ba0 <zim_Str_Matcher_matchAll>:
    3ba0:	55                   	push   %rbp
    3ba1:	41 57                	push   %r15
    3ba3:	41 56                	push   %r14
    3ba5:	41 55                	push   %r13
    3ba7:	41 54                	push   %r12
    3ba9:	53                   	push   %rbx
    3baa:	48 83 ec 58          	sub    $0x58,%rsp
    3bae:	48 89 74 24 28       	mov    %rsi,0x28(%rsp)
    3bb3:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    3bba:	00 00 
    3bbc:	48 89 44 24 50       	mov    %rax,0x50(%rsp)
    3bc1:	83 7f 2c 01          	cmpl   $0x1,0x2c(%rdi)
    3bc5:	0f 85 e2 03 00 00    	jne    3fad <zim_Str_Matcher_matchAll+0x40d>
    3bcb:	48 8d 47 50          	lea    0x50(%rdi),%rax
    3bcf:	80 7f 58 06          	cmpb   $0x6,0x58(%rdi)
    3bd3:	0f 85 ef 03 00 00    	jne    3fc8 <zim_Str_Matcher_matchAll+0x428>
    3bd9:	48 8b 00             	mov    (%rax),%rax
    3bdc:	48 89 44 24 18       	mov    %rax,0x18(%rsp)
    3be1:	48 8b 5f 20          	mov    0x20(%rdi),%rbx
    3be5:	e8 26 e6 ff ff       	call   2210 <_zend_new_array_0@plt>
    3bea:	48 8b 4c 24 28       	mov    0x28(%rsp),%rcx
    3bef:	48 89 01             	mov    %rax,(%rcx)
    3bf2:	c7 41 08 07 03 00 00 	movl   $0x307,0x8(%rcx)
    3bf9:	48 89 5c 24 08       	mov    %rbx,0x8(%rsp)
    3bfe:	83 7b f8 00          	cmpl   $0x0,-0x8(%rbx)
    3c02:	48 8b 5c 24 18       	mov    0x18(%rsp),%rbx
    3c07:	0f 84 3b 03 00 00    	je     3f48 <zim_Str_Matcher_matchAll+0x3a8>
    3c0d:	48 8b 4b 10          	mov    0x10(%rbx),%rcx
    3c11:	48 85 c9             	test   %rcx,%rcx
    3c14:	0f 84 2e 03 00 00    	je     3f48 <zim_Str_Matcher_matchAll+0x3a8>
    3c1a:	48 c7 44 24 10 00 00 	movq   $0x0,0x10(%rsp)
    3c21:	00 00 
    3c23:	31 f6                	xor    %esi,%esi
    3c25:	31 c0                	xor    %eax,%eax
    3c27:	45 31 e4             	xor    %r12d,%r12d
    3c2a:	31 ff                	xor    %edi,%edi
    3c2c:	4c 8b 4c 24 08       	mov    0x8(%rsp),%r9
    3c31:	eb 22                	jmp    3c55 <zim_Str_Matcher_matchAll+0xb5>
    3c33:	66 66 66 66 2e 0f 1f 	data16 data16 data16 cs nopw 0x0(%rax,%rax,1)
    3c3a:	84 00 00 00 00 00 
    3c40:	48 c7 44 24 10 00 00 	movq   $0x0,0x10(%rsp)
    3c47:	00 00 
    3c49:	48 ff c6             	inc    %rsi
    3c4c:	48 39 ce             	cmp    %rcx,%rsi
    3c4f:	0f 83 f7 01 00 00    	jae    3e4c <zim_Str_Matcher_matchAll+0x2ac>
    3c55:	0f b6 54 33 18       	movzbl 0x18(%rbx,%rsi,1),%edx
    3c5a:	41 0f b7 94 51 e4 fd 	movzwl -0x21c(%r9,%rdx,2),%edx
    3c61:	ff ff 
    3c63:	48 85 d2             	test   %rdx,%rdx
    3c66:	74 d8                	je     3c40 <zim_Str_Matcher_matchAll+0xa0>
    3c68:	48 89 74 24 20       	mov    %rsi,0x20(%rsp)
    3c6d:	41 8b b1 b0 fd ff ff 	mov    -0x250(%r9),%esi
    3c74:	39 74 24 10          	cmp    %esi,0x10(%rsp)
    3c78:	73 36                	jae    3cb0 <zim_Str_Matcher_matchAll+0x110>
    3c7a:	4c 8b 4c 24 10       	mov    0x10(%rsp),%r9
    3c7f:	44 89 ce             	mov    %r9d,%esi
    3c82:	4c 8b 4c 24 08       	mov    0x8(%rsp),%r9
    3c87:	4d 63 81 e0 fd ff ff 	movslq -0x220(%r9),%r8
    3c8e:	4c 0f af c6          	imul   %rsi,%r8
    3c92:	49 c1 e0 02          	shl    $0x2,%r8
    3c96:	4d 03 81 a0 fd ff ff 	add    -0x260(%r9),%r8
    3c9d:	4d 8d 1c 90          	lea    (%r8,%rdx,4),%r11
    3ca1:	e9 8f 00 00 00       	jmp    3d35 <zim_Str_Matcher_matchAll+0x195>
    3ca6:	66 2e 0f 1f 84 00 00 	cs nopw 0x0(%rax,%rax,1)
    3cad:	00 00 00 
    3cb0:	4d 8b 81 c8 fd ff ff 	mov    -0x238(%r9),%r8
    3cb7:	4c 8b 4c 24 10       	mov    0x10(%rsp),%r9
    3cbc:	eb 11                	jmp    3ccf <zim_Str_Matcher_matchAll+0x12f>
    3cbe:	66 90                	xchg   %ax,%ax
    3cc0:	66 41 3b 51 0a       	cmp    0xa(%r9),%dx
    3cc5:	74 5b                	je     3d22 <zim_Str_Matcher_matchAll+0x182>
    3cc7:	45 8b 09             	mov    (%r9),%r9d
    3cca:	41 39 f1             	cmp    %esi,%r9d
    3ccd:	72 b0                	jb     3c7f <zim_Str_Matcher_matchAll+0xdf>
    3ccf:	41 29 f1             	sub    %esi,%r9d
    3cd2:	4f 8d 14 49          	lea    (%r9,%r9,2),%r10
    3cd6:	4f 8d 0c 90          	lea    (%r8,%r10,4),%r9
    3cda:	47 0f b7 54 90 08    	movzwl 0x8(%r8,%r10,4),%r10d
    3ce0:	45 85 d2             	test   %r10d,%r10d
    3ce3:	74 e2                	je     3cc7 <zim_Str_Matcher_matchAll+0x127>
    3ce5:	41 83 fa 01          	cmp    $0x1,%r10d
    3ce9:	74 d5                	je     3cc0 <zim_Str_Matcher_matchAll+0x120>
    3ceb:	45 8b 59 04          	mov    0x4(%r9),%r11d
    3cef:	49 c1 e3 03          	shl    $0x3,%r11
    3cf3:	48 8b 5c 24 08       	mov    0x8(%rsp),%rbx
    3cf8:	4c 03 9b a8 fd ff ff 	add    -0x258(%rbx),%r11
    3cff:	48 8b 5c 24 18       	mov    0x18(%rsp),%rbx
    3d04:	66 66 66 2e 0f 1f 84 	data16 data16 cs nopw 0x0(%rax,%rax,1)
    3d0b:	00 00 00 00 00 
    3d10:	66 41 39 53 04       	cmp    %dx,0x4(%r11)
    3d15:	74 19                	je     3d30 <zim_Str_Matcher_matchAll+0x190>
    3d17:	49 83 c3 08          	add    $0x8,%r11
    3d1b:	49 ff ca             	dec    %r10
    3d1e:	75 f0                	jne    3d10 <zim_Str_Matcher_matchAll+0x170>
    3d20:	eb a5                	jmp    3cc7 <zim_Str_Matcher_matchAll+0x127>
    3d22:	49 83 c1 04          	add    $0x4,%r9
    3d26:	4d 89 cb             	mov    %r9,%r11
    3d29:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    3d30:	4c 8b 4c 24 08       	mov    0x8(%rsp),%r9
    3d35:	45 8b 13             	mov    (%r11),%r10d
    3d38:	45 85 d2             	test   %r10d,%r10d
    3d3b:	48 8b 74 24 20       	mov    0x20(%rsp),%rsi
    3d40:	78 0e                	js     3d50 <zim_Str_Matcher_matchAll+0x1b0>
    3d42:	4c 89 54 24 10       	mov    %r10,0x10(%rsp)
    3d47:	e9 fd fe ff ff       	jmp    3c49 <zim_Str_Matcher_matchAll+0xa9>
    3d4c:	0f 1f 40 00          	nopl   0x0(%rax)
    3d50:	41 81 e2 ff ff ff 7f 	and    $0x7fffffff,%r10d
    3d57:	49 8b 91 c0 fd ff ff 	mov    -0x240(%r9),%rdx
    3d5e:	4f 8d 04 52          	lea    (%r10,%r10,2),%r8
    3d62:	42 83 3c 82 00       	cmpl   $0x0,(%rdx,%r8,4)
    3d67:	4c 89 54 24 10       	mov    %r10,0x10(%rsp)
    3d6c:	44 89 d6             	mov    %r10d,%esi
    3d6f:	79 0f                	jns    3d80 <zim_Str_Matcher_matchAll+0x1e0>
    3d71:	4a 8d 34 82          	lea    (%rdx,%r8,4),%rsi
    3d75:	8b 76 04             	mov    0x4(%rsi),%esi
    3d78:	85 f6                	test   %esi,%esi
    3d7a:	0f 88 c2 00 00 00    	js     3e42 <zim_Str_Matcher_matchAll+0x2a2>
    3d80:	48 8b 4c 24 20       	mov    0x20(%rsp),%rcx
    3d85:	4c 8d 41 01          	lea    0x1(%rcx),%r8
    3d89:	4b 8d 0c 64          	lea    (%r12,%r12,2),%rcx
    3d8d:	48 8d 1c cd 10 00 00 	lea    0x10(,%rcx,8),%rbx
    3d94:	00 
    3d95:	4c 89 44 24 30       	mov    %r8,0x30(%rsp)
    3d9a:	eb 6c                	jmp    3e08 <zim_Str_Matcher_matchAll+0x268>
    3d9c:	0f 1f 40 00          	nopl   0x0(%rax)
    3da0:	4c 89 64 24 38       	mov    %r12,0x38(%rsp)
    3da5:	4c 8d 24 00          	lea    (%rax,%rax,1),%r12
    3da9:	48 85 c0             	test   %rax,%rax
    3dac:	b8 10 00 00 00       	mov    $0x10,%eax
    3db1:	4c 0f 44 e0          	cmove  %rax,%r12
    3db5:	ba 18 00 00 00       	mov    $0x18,%edx
    3dba:	4c 89 e6             	mov    %r12,%rsi
    3dbd:	31 c9                	xor    %ecx,%ecx
    3dbf:	e8 7c e4 ff ff       	call   2240 <_safe_erealloc@plt>
    3dc4:	4c 8b 44 24 30       	mov    0x30(%rsp),%r8
    3dc9:	4c 8b 4c 24 08       	mov    0x8(%rsp),%r9
    3dce:	48 89 c7             	mov    %rax,%rdi
    3dd1:	49 8b 4e 10          	mov    0x10(%r14),%rcx
    3dd5:	49 8b 91 c0 fd ff ff 	mov    -0x240(%r9),%rdx
    3ddc:	4c 89 e0             	mov    %r12,%rax
    3ddf:	4c 8b 64 24 38       	mov    0x38(%rsp),%r12
    3de4:	4c 89 c6             	mov    %r8,%rsi
    3de7:	48 29 ee             	sub    %rbp,%rsi
    3dea:	48 89 74 1f f0       	mov    %rsi,-0x10(%rdi,%rbx,1)
    3def:	48 89 4c 1f f8       	mov    %rcx,-0x8(%rdi,%rbx,1)
    3df4:	44 89 3c 1f          	mov    %r15d,(%rdi,%rbx,1)
    3df8:	49 ff c4             	inc    %r12
    3dfb:	42 8b 74 aa 04       	mov    0x4(%rdx,%r13,4),%esi
    3e00:	48 83 c3 18          	add    $0x18,%rbx
    3e04:	85 f6                	test   %esi,%esi
    3e06:	78 31                	js     3e39 <zim_Str_Matcher_matchAll+0x299>
    3e08:	49 81 fc 00 00 00 40 	cmp    $0x40000000,%r12
    3e0f:	0f 84 56 01 00 00    	je     3f6b <zim_Str_Matcher_matchAll+0x3cb>
    3e15:	89 f1                	mov    %esi,%ecx
    3e17:	4c 8d 2c 49          	lea    (%rcx,%rcx,2),%r13
    3e1b:	4e 63 3c aa          	movslq (%rdx,%r13,4),%r15
    3e1f:	49 8b 49 e8          	mov    -0x18(%r9),%rcx
    3e23:	4e 8b 34 f9          	mov    (%rcx,%r15,8),%r14
    3e27:	49 8b 6e 10          	mov    0x10(%r14),%rbp
    3e2b:	49 39 c4             	cmp    %rax,%r12
    3e2e:	0f 84 6c ff ff ff    	je     3da0 <zim_Str_Matcher_matchAll+0x200>
    3e34:	48 89 e9             	mov    %rbp,%rcx
    3e37:	eb ab                	jmp    3de4 <zim_Str_Matcher_matchAll+0x244>
    3e39:	48 8b 5c 24 18       	mov    0x18(%rsp),%rbx
    3e3e:	48 8b 4b 10          	mov    0x10(%rbx),%rcx
    3e42:	48 8b 74 24 20       	mov    0x20(%rsp),%rsi
    3e47:	e9 fd fd ff ff       	jmp    3c49 <zim_Str_Matcher_matchAll+0xa9>
    3e4c:	49 83 fc 02          	cmp    $0x2,%r12
    3e50:	72 1c                	jb     3e6e <zim_Str_Matcher_matchAll+0x2ce>
    3e52:	48 8d 0d 17 fd ff ff 	lea    -0x2e9(%rip),%rcx        # 3b70 <ac_hit_compare>
    3e59:	ba 18 00 00 00       	mov    $0x18,%edx
    3e5e:	49 89 ff             	mov    %rdi,%r15
    3e61:	4c 89 e6             	mov    %r12,%rsi
    3e64:	e8 d7 e1 ff ff       	call   2040 <qsort@plt>
    3e69:	4c 89 ff             	mov    %r15,%rdi
    3e6c:	eb 09                	jmp    3e77 <zim_Str_Matcher_matchAll+0x2d7>
    3e6e:	4d 85 e4             	test   %r12,%r12
    3e71:	0f 84 c1 00 00 00    	je     3f38 <zim_Str_Matcher_matchAll+0x398>
    3e77:	4b 8d 04 64          	lea    (%r12,%r12,2),%rax
    3e7b:	48 83 7c c7 e8 00    	cmpq   $0x0,-0x18(%rdi,%rax,8)
    3e81:	0f 88 94 01 00 00    	js     401b <zim_Str_Matcher_matchAll+0x47b>
    3e87:	4d 89 e6             	mov    %r12,%r14
    3e8a:	49 89 ff             	mov    %rdi,%r15
    3e8d:	48 8d 5f 10          	lea    0x10(%rdi),%rbx
    3e91:	4c 8d 64 24 40       	lea    0x40(%rsp),%r12
    3e96:	eb 39                	jmp    3ed1 <zim_Str_Matcher_matchAll+0x331>
    3e98:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
    3e9f:	00 
    3ea0:	48 89 14 08          	mov    %rdx,(%rax,%rcx,1)
    3ea4:	31 f6                	xor    %esi,%esi
    3ea6:	f6 42 04 40          	testb  $0x40,0x4(%rdx)
    3eaa:	40 0f 94 c6          	sete   %sil
    3eae:	c1 e6 08             	shl    $0x8,%esi
    3eb1:	83 ce 06             	or     $0x6,%esi
    3eb4:	89 74 08 08          	mov    %esi,0x8(%rax,%rcx,1)
    3eb8:	48 8b 44 24 28       	mov    0x28(%rsp),%rax
    3ebd:	48 8b 38             	mov    (%rax),%rdi
    3ec0:	4c 89 e6             	mov    %r12,%rsi
    3ec3:	e8 f8 e2 ff ff       	call   21c0 <zend_hash_next_index_insert@plt>
    3ec8:	48 83 c3 18          	add    $0x18,%rbx
    3ecc:	49 ff ce             	dec    %r14
    3ecf:	74 6f                	je     3f40 <zim_Str_Matcher_matchAll+0x3a0>
    3ed1:	48 8b 35 18 43 00 00 	mov    0x4318(%rip),%rsi        # 81f0 <str_matchresult_ce>
    3ed8:	4c 89 e7             	mov    %r12,%rdi
    3edb:	e8 b0 e2 ff ff       	call   2190 <object_init_ex@plt>
    3ee0:	48 8b 44 24 40       	mov    0x40(%rsp),%rax
    3ee5:	8b 0d 0d 43 00 00    	mov    0x430d(%rip),%ecx        # 81f8 <result_offset>
    3eeb:	48 8b 53 f0          	mov    -0x10(%rbx),%rdx
    3eef:	48 89 14 08          	mov    %rdx,(%rax,%rcx,1)
    3ef3:	c7 44 08 08 04 00 00 	movl   $0x4,0x8(%rax,%rcx,1)
    3efa:	00 
    3efb:	8b 0d fb 42 00 00    	mov    0x42fb(%rip),%ecx        # 81fc <result_length>
    3f01:	48 8b 53 f8          	mov    -0x8(%rbx),%rdx
    3f05:	48 89 14 08          	mov    %rdx,(%rax,%rcx,1)
    3f09:	c7 44 08 08 04 00 00 	movl   $0x4,0x8(%rax,%rcx,1)
    3f10:	00 
    3f11:	8b 0d e9 42 00 00    	mov    0x42e9(%rip),%ecx        # 8200 <result_keyword>
    3f17:	48 8b 54 24 08       	mov    0x8(%rsp),%rdx
    3f1c:	48 8b 52 e8          	mov    -0x18(%rdx),%rdx
    3f20:	48 63 33             	movslq (%rbx),%rsi
    3f23:	48 8b 14 f2          	mov    (%rdx,%rsi,8),%rdx
    3f27:	f6 42 04 40          	testb  $0x40,0x4(%rdx)
    3f2b:	0f 85 6f ff ff ff    	jne    3ea0 <zim_Str_Matcher_matchAll+0x300>
    3f31:	ff 02                	incl   (%rdx)
    3f33:	e9 68 ff ff ff       	jmp    3ea0 <zim_Str_Matcher_matchAll+0x300>
    3f38:	49 89 ff             	mov    %rdi,%r15
    3f3b:	48 85 ff             	test   %rdi,%rdi
    3f3e:	74 08                	je     3f48 <zim_Str_Matcher_matchAll+0x3a8>
    3f40:	4c 89 ff             	mov    %r15,%rdi
    3f43:	e8 b8 e2 ff ff       	call   2200 <_efree@plt>
    3f48:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    3f4f:	00 00 
    3f51:	48 3b 44 24 50       	cmp    0x50(%rsp),%rax
    3f56:	0f 85 f2 00 00 00    	jne    404e <zim_Str_Matcher_matchAll+0x4ae>
    3f5c:	48 83 c4 58          	add    $0x58,%rsp
    3f60:	5b                   	pop    %rbx
    3f61:	41 5c                	pop    %r12
    3f63:	41 5d                	pop    %r13
    3f65:	41 5e                	pop    %r14
    3f67:	41 5f                	pop    %r15
    3f69:	5d                   	pop    %rbp
    3f6a:	c3                   	ret
    3f6b:	48 8d 35 0b 22 00 00 	lea    0x220b(%rip),%rsi        # 617d <_fini+0xe91>
    3f72:	48 89 fb             	mov    %rdi,%rbx
    3f75:	31 ff                	xor    %edi,%edi
    3f77:	31 c0                	xor    %eax,%eax
    3f79:	e8 f2 e2 ff ff       	call   2270 <zend_throw_error@plt>
    3f7e:	48 85 db             	test   %rbx,%rbx
    3f81:	74 c5                	je     3f48 <zim_Str_Matcher_matchAll+0x3a8>
    3f83:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    3f8a:	00 00 
    3f8c:	48 3b 44 24 50       	cmp    0x50(%rsp),%rax
    3f91:	0f 85 b7 00 00 00    	jne    404e <zim_Str_Matcher_matchAll+0x4ae>
    3f97:	48 89 df             	mov    %rbx,%rdi
    3f9a:	48 83 c4 58          	add    $0x58,%rsp
    3f9e:	5b                   	pop    %rbx
    3f9f:	41 5c                	pop    %r12
    3fa1:	41 5d                	pop    %r13
    3fa3:	41 5e                	pop    %r14
    3fa5:	41 5f                	pop    %r15
    3fa7:	5d                   	pop    %rbp
    3fa8:	e9 53 e2 ff ff       	jmp    2200 <_efree@plt>
    3fad:	bf 01 00 00 00       	mov    $0x1,%edi
    3fb2:	be 01 00 00 00       	mov    $0x1,%esi
    3fb7:	e8 04 e1 ff ff       	call   20c0 <zend_wrong_parameters_count_error@plt>
    3fbc:	b0 01                	mov    $0x1,%al
    3fbe:	45 31 f6             	xor    %r14d,%r14d
    3fc1:	45 31 c0             	xor    %r8d,%r8d
    3fc4:	31 c9                	xor    %ecx,%ecx
    3fc6:	eb 28                	jmp    3ff0 <zim_Str_Matcher_matchAll+0x450>
    3fc8:	49 89 ff             	mov    %rdi,%r15
    3fcb:	41 be 01 00 00 00    	mov    $0x1,%r14d
    3fd1:	48 89 c3             	mov    %rax,%rbx
    3fd4:	48 89 c7             	mov    %rax,%rdi
    3fd7:	be 01 00 00 00       	mov    $0x1,%esi
    3fdc:	e8 cf e0 ff ff       	call   20b0 <zend_parse_arg_str_slow@plt>
    3fe1:	48 85 c0             	test   %rax,%rax
    3fe4:	75 6d                	jne    4053 <zim_Str_Matcher_matchAll+0x4b3>
    3fe6:	b0 0c                	mov    $0xc,%al
    3fe8:	b9 04 00 00 00       	mov    $0x4,%ecx
    3fed:	49 89 d8             	mov    %rbx,%r8
    3ff0:	64 48 8b 14 25 28 00 	mov    %fs:0x28,%rdx
    3ff7:	00 00 
    3ff9:	48 3b 54 24 50       	cmp    0x50(%rsp),%rdx
    3ffe:	75 4e                	jne    404e <zim_Str_Matcher_matchAll+0x4ae>
    4000:	0f b6 f8             	movzbl %al,%edi
    4003:	44 89 f6             	mov    %r14d,%esi
    4006:	31 d2                	xor    %edx,%edx
    4008:	48 83 c4 58          	add    $0x58,%rsp
    400c:	5b                   	pop    %rbx
    400d:	41 5c                	pop    %r12
    400f:	41 5d                	pop    %r13
    4011:	41 5e                	pop    %r14
    4013:	41 5f                	pop    %r15
    4015:	5d                   	pop    %rbp
    4016:	e9 d5 e1 ff ff       	jmp    21f0 <zend_wrong_parameter_error@plt>
    401b:	e8 e0 e1 ff ff       	call   2200 <_efree@plt>
    4020:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    4027:	00 00 
    4029:	48 3b 44 24 50       	cmp    0x50(%rsp),%rax
    402e:	75 1e                	jne    404e <zim_Str_Matcher_matchAll+0x4ae>
    4030:	48 8d 35 37 20 00 00 	lea    0x2037(%rip),%rsi        # 606e <_fini+0xd82>
    4037:	31 ff                	xor    %edi,%edi
    4039:	31 c0                	xor    %eax,%eax
    403b:	48 83 c4 58          	add    $0x58,%rsp
    403f:	5b                   	pop    %rbx
    4040:	41 5c                	pop    %r12
    4042:	41 5d                	pop    %r13
    4044:	41 5e                	pop    %r14
    4046:	41 5f                	pop    %r15
    4048:	5d                   	pop    %rbp
    4049:	e9 22 e2 ff ff       	jmp    2270 <zend_throw_error@plt>
    404e:	e8 3d e0 ff ff       	call   2090 <__stack_chk_fail@plt>
    4053:	48 89 44 24 18       	mov    %rax,0x18(%rsp)
    4058:	4c 89 ff             	mov    %r15,%rdi
    405b:	e9 81 fb ff ff       	jmp    3be1 <zim_Str_Matcher_matchAll+0x41>

Disassembly of section .fini:
