
gcc15-strmatch.so:     file format elf64-x86-64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .plt.got:

Disassembly of section .plt.sec:

Disassembly of section .text:

0000000000002de0 <zim_Str_Matcher_countMatches>:
    2de0:	f3 0f 1e fa          	endbr64
    2de4:	41 56                	push   %r14
    2de6:	41 55                	push   %r13
    2de8:	41 54                	push   %r12
    2dea:	55                   	push   %rbp
    2deb:	53                   	push   %rbx
    2dec:	48 83 ec 10          	sub    $0x10,%rsp
    2df0:	8b 6f 2c             	mov    0x2c(%rdi),%ebp
    2df3:	83 fd 01             	cmp    $0x1,%ebp
    2df6:	0f 85 d5 f7 ff ff    	jne    25d1 <zim_Str_Matcher_countMatches.cold+0x25>
    2dfc:	48 89 fb             	mov    %rdi,%rbx
    2dff:	49 89 f3             	mov    %rsi,%r11
    2e02:	80 7f 58 06          	cmpb   $0x6,0x58(%rdi)
    2e06:	0f 85 65 01 00 00    	jne    2f71 <zim_Str_Matcher_countMatches+0x191>
    2e0c:	48 8b 47 50          	mov    0x50(%rdi),%rax
    2e10:	4c 8b 4b 20          	mov    0x20(%rbx),%r9
    2e14:	41 8b 59 f8          	mov    -0x8(%r9),%ebx
    2e18:	85 db                	test   %ebx,%ebx
    2e1a:	0f 84 35 01 00 00    	je     2f55 <zim_Str_Matcher_countMatches+0x175>
    2e20:	48 8b 50 10          	mov    0x10(%rax),%rdx
    2e24:	31 db                	xor    %ebx,%ebx
    2e26:	48 85 d2             	test   %rdx,%rdx
    2e29:	0f 84 e5 00 00 00    	je     2f14 <zim_Str_Matcher_countMatches+0x134>
    2e2f:	4c 8d 50 18          	lea    0x18(%rax),%r10
    2e33:	48 8d 6c 10 18       	lea    0x18(%rax,%rdx,1),%rbp
    2e38:	31 db                	xor    %ebx,%ebx
    2e3a:	31 c0                	xor    %eax,%eax
    2e3c:	0f 1f 40 00          	nopl   0x0(%rax)
    2e40:	41 0f b6 12          	movzbl (%r10),%edx
    2e44:	41 0f b7 8c 51 e4 fd 	movzwl -0x21c(%r9,%rdx,2),%ecx
    2e4b:	ff ff 
    2e4d:	66 85 c9             	test   %cx,%cx
    2e50:	0f 84 da 00 00 00    	je     2f30 <zim_Str_Matcher_countMatches+0x150>
    2e56:	41 8b b9 b0 fd ff ff 	mov    -0x250(%r9),%edi
    2e5d:	39 f8                	cmp    %edi,%eax
    2e5f:	0f 82 d3 00 00 00    	jb     2f38 <zim_Str_Matcher_countMatches+0x158>
    2e65:	4d 8b 81 c8 fd ff ff 	mov    -0x238(%r9),%r8
    2e6c:	eb 0e                	jmp    2e7c <zim_Str_Matcher_countMatches+0x9c>
    2e6e:	66 90                	xchg   %ax,%ax
    2e70:	77 2e                	ja     2ea0 <zim_Str_Matcher_countMatches+0xc0>
    2e72:	8b 02                	mov    (%rdx),%eax
    2e74:	39 f8                	cmp    %edi,%eax
    2e76:	0f 82 bc 00 00 00    	jb     2f38 <zim_Str_Matcher_countMatches+0x158>
    2e7c:	29 f8                	sub    %edi,%eax
    2e7e:	48 8d 04 40          	lea    (%rax,%rax,2),%rax
    2e82:	49 8d 14 80          	lea    (%r8,%rax,4),%rdx
    2e86:	0f b7 72 08          	movzwl 0x8(%rdx),%esi
    2e8a:	83 fe 01             	cmp    $0x1,%esi
    2e8d:	75 e1                	jne    2e70 <zim_Str_Matcher_countMatches+0x90>
    2e8f:	66 3b 4a 0a          	cmp    0xa(%rdx),%cx
    2e93:	75 dd                	jne    2e72 <zim_Str_Matcher_countMatches+0x92>
    2e95:	8b 42 04             	mov    0x4(%rdx),%eax
    2e98:	eb 37                	jmp    2ed1 <zim_Str_Matcher_countMatches+0xf1>
    2e9a:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
    2ea0:	44 8b 72 04          	mov    0x4(%rdx),%r14d
    2ea4:	4d 8b a9 a8 fd ff ff 	mov    -0x258(%r9),%r13
    2eab:	83 ee 01             	sub    $0x1,%esi
    2eae:	4c 01 f6             	add    %r14,%rsi
    2eb1:	4b 8d 44 f5 00       	lea    0x0(%r13,%r14,8),%rax
    2eb6:	49 8d 74 f5 08       	lea    0x8(%r13,%rsi,8),%rsi
    2ebb:	eb 0c                	jmp    2ec9 <zim_Str_Matcher_countMatches+0xe9>
    2ebd:	0f 1f 00             	nopl   (%rax)
    2ec0:	48 83 c0 08          	add    $0x8,%rax
    2ec4:	48 39 c6             	cmp    %rax,%rsi
    2ec7:	74 a9                	je     2e72 <zim_Str_Matcher_countMatches+0x92>
    2ec9:	66 3b 48 04          	cmp    0x4(%rax),%cx
    2ecd:	75 f1                	jne    2ec0 <zim_Str_Matcher_countMatches+0xe0>
    2ecf:	8b 00                	mov    (%rax),%eax
    2ed1:	85 c0                	test   %eax,%eax
    2ed3:	79 32                	jns    2f07 <zim_Str_Matcher_countMatches+0x127>
    2ed5:	25 ff ff ff 7f       	and    $0x7fffffff,%eax
    2eda:	49 8b b1 c0 fd ff ff 	mov    -0x240(%r9),%rsi
    2ee1:	48 b9 ff ff ff ff ff 	movabs $0x7fffffffffffffff,%rcx
    2ee8:	ff ff 7f 
    2eeb:	89 c2                	mov    %eax,%edx
    2eed:	48 29 d9             	sub    %rbx,%rcx
    2ef0:	48 8d 14 52          	lea    (%rdx,%rdx,2),%rdx
    2ef4:	48 8d 14 96          	lea    (%rsi,%rdx,4),%rdx
    2ef8:	8b 52 08             	mov    0x8(%rdx),%edx
    2efb:	48 39 ca             	cmp    %rcx,%rdx
    2efe:	0f 8f ea f6 ff ff    	jg     25ee <zim_Str_Matcher_countMatches.cold+0x42>
    2f04:	48 01 d3             	add    %rdx,%rbx
    2f07:	49 83 c2 01          	add    $0x1,%r10
    2f0b:	4c 39 d5             	cmp    %r10,%rbp
    2f0e:	0f 85 2c ff ff ff    	jne    2e40 <zim_Str_Matcher_countMatches+0x60>
    2f14:	49 89 1b             	mov    %rbx,(%r11)
    2f17:	41 c7 43 08 04 00 00 	movl   $0x4,0x8(%r11)
    2f1e:	00 
    2f1f:	48 83 c4 10          	add    $0x10,%rsp
    2f23:	5b                   	pop    %rbx
    2f24:	5d                   	pop    %rbp
    2f25:	41 5c                	pop    %r12
    2f27:	41 5d                	pop    %r13
    2f29:	41 5e                	pop    %r14
    2f2b:	c3                   	ret
    2f2c:	0f 1f 40 00          	nopl   0x0(%rax)
    2f30:	31 c0                	xor    %eax,%eax
    2f32:	eb d3                	jmp    2f07 <zim_Str_Matcher_countMatches+0x127>
    2f34:	0f 1f 40 00          	nopl   0x0(%rax)
    2f38:	49 63 91 e0 fd ff ff 	movslq -0x220(%r9),%rdx
    2f3f:	48 0f af c2          	imul   %rdx,%rax
    2f43:	49 8b 91 a0 fd ff ff 	mov    -0x260(%r9),%rdx
    2f4a:	48 01 c8             	add    %rcx,%rax
    2f4d:	8b 04 82             	mov    (%rdx,%rax,4),%eax
    2f50:	e9 7c ff ff ff       	jmp    2ed1 <zim_Str_Matcher_countMatches+0xf1>
    2f55:	49 c7 03 00 00 00 00 	movq   $0x0,(%r11)
    2f5c:	41 c7 43 08 04 00 00 	movl   $0x4,0x8(%r11)
    2f63:	00 
    2f64:	48 83 c4 10          	add    $0x10,%rsp
    2f68:	5b                   	pop    %rbx
    2f69:	5d                   	pop    %rbp
    2f6a:	41 5c                	pop    %r12
    2f6c:	41 5d                	pop    %r13
    2f6e:	41 5e                	pop    %r14
    2f70:	c3                   	ret
    2f71:	4c 8d 67 50          	lea    0x50(%rdi),%r12
    2f75:	48 89 74 24 08       	mov    %rsi,0x8(%rsp)
    2f7a:	be 01 00 00 00       	mov    $0x1,%esi
    2f7f:	4c 89 e7             	mov    %r12,%rdi
    2f82:	e8 b9 f3 ff ff       	call   2340 <zend_parse_arg_str_slow@plt>
    2f87:	4c 8b 5c 24 08       	mov    0x8(%rsp),%r11
    2f8c:	48 85 c0             	test   %rax,%rax
    2f8f:	0f 84 17 f6 ff ff    	je     25ac <zim_Str_Matcher_countMatches.cold>
    2f95:	e9 76 fe ff ff       	jmp    2e10 <zim_Str_Matcher_countMatches+0x30>

Disassembly of section .fini:
