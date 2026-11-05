
gcc15-strmatch.so:     file format elf64-x86-64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .plt.got:

Disassembly of section .plt.sec:

Disassembly of section .text:

0000000000002fa0 <zim_Str_Matcher_getMatchedKeywords>:
    2fa0:	f3 0f 1e fa          	endbr64
    2fa4:	41 57                	push   %r15
    2fa6:	41 56                	push   %r14
    2fa8:	41 55                	push   %r13
    2faa:	41 54                	push   %r12
    2fac:	55                   	push   %rbp
    2fad:	53                   	push   %rbx
    2fae:	48 83 ec 38          	sub    $0x38,%rsp
    2fb2:	8b 6f 2c             	mov    0x2c(%rdi),%ebp
    2fb5:	83 fd 01             	cmp    $0x1,%ebp
    2fb8:	0f 85 73 f6 ff ff    	jne    2631 <zim_Str_Matcher_getMatchedKeywords.cold+0x27>
    2fbe:	48 89 fb             	mov    %rdi,%rbx
    2fc1:	49 89 f5             	mov    %rsi,%r13
    2fc4:	80 7f 58 06          	cmpb   $0x6,0x58(%rdi)
    2fc8:	0f 85 13 03 00 00    	jne    32e1 <zim_Str_Matcher_getMatchedKeywords+0x341>
    2fce:	4c 8b 77 50          	mov    0x50(%rdi),%r14
    2fd2:	48 8b 6b 20          	mov    0x20(%rbx),%rbp
    2fd6:	e8 c5 f4 ff ff       	call   24a0 <_zend_new_array_0@plt>
    2fdb:	41 c7 45 08 07 03 00 	movl   $0x307,0x8(%r13)
    2fe2:	00 
    2fe3:	8b 7d f8             	mov    -0x8(%rbp),%edi
    2fe6:	49 89 45 00          	mov    %rax,0x0(%r13)
    2fea:	85 ff                	test   %edi,%edi
    2fec:	74 07                	je     2ff5 <zim_Str_Matcher_getMatchedKeywords+0x55>
    2fee:	49 83 7e 10 00       	cmpq   $0x0,0x10(%r14)
    2ff3:	75 13                	jne    3008 <zim_Str_Matcher_getMatchedKeywords+0x68>
    2ff5:	48 83 c4 38          	add    $0x38,%rsp
    2ff9:	5b                   	pop    %rbx
    2ffa:	5d                   	pop    %rbp
    2ffb:	41 5c                	pop    %r12
    2ffd:	41 5d                	pop    %r13
    2fff:	41 5e                	pop    %r14
    3001:	41 5f                	pop    %r15
    3003:	c3                   	ret
    3004:	0f 1f 40 00          	nopl   0x0(%rax)
    3008:	be 01 00 00 00       	mov    $0x1,%esi
    300d:	e8 2e f4 ff ff       	call   2440 <_ecalloc@plt>
    3012:	49 83 7e 10 00       	cmpq   $0x0,0x10(%r14)
    3017:	0f 84 0b 03 00 00    	je     3328 <zim_Str_Matcher_getMatchedKeywords+0x388>
    301d:	4c 89 6c 24 28       	mov    %r13,0x28(%rsp)
    3022:	4d 89 f7             	mov    %r14,%r15
    3025:	31 db                	xor    %ebx,%ebx
    3027:	45 31 db             	xor    %r11d,%r11d
    302a:	45 31 e4             	xor    %r12d,%r12d
    302d:	31 f6                	xor    %esi,%esi
    302f:	31 ff                	xor    %edi,%edi
    3031:	49 89 c6             	mov    %rax,%r14
    3034:	90                   	nop
    3035:	66 66 2e 0f 1f 84 00 	data16 cs nopw 0x0(%rax,%rax,1)
    303c:	00 00 00 00 
    3040:	8b 45 f8             	mov    -0x8(%rbp),%eax
    3043:	48 39 c3             	cmp    %rax,%rbx
    3046:	0f 83 cd 01 00 00    	jae    3219 <zim_Str_Matcher_getMatchedKeywords+0x279>
    304c:	43 0f b6 44 1f 18    	movzbl 0x18(%r15,%r11,1),%eax
    3052:	49 83 c3 01          	add    $0x1,%r11
    3056:	0f b7 8c 45 e4 fd ff 	movzwl -0x21c(%rbp,%rax,2),%ecx
    305d:	ff 
    305e:	66 85 c9             	test   %cx,%cx
    3061:	0f 84 39 02 00 00    	je     32a0 <zim_Str_Matcher_getMatchedKeywords+0x300>
    3067:	44 8b 95 b0 fd ff ff 	mov    -0x250(%rbp),%r10d
    306e:	45 39 d4             	cmp    %r10d,%r12d
    3071:	0f 82 39 02 00 00    	jb     32b0 <zim_Str_Matcher_getMatchedKeywords+0x310>
    3077:	4c 8b ad c8 fd ff ff 	mov    -0x238(%rbp),%r13
    307e:	eb 12                	jmp    3092 <zim_Str_Matcher_getMatchedKeywords+0xf2>
    3080:	0f 87 42 01 00 00    	ja     31c8 <zim_Str_Matcher_getMatchedKeywords+0x228>
    3086:	44 8b 22             	mov    (%rdx),%r12d
    3089:	45 39 d4             	cmp    %r10d,%r12d
    308c:	0f 82 1e 02 00 00    	jb     32b0 <zim_Str_Matcher_getMatchedKeywords+0x310>
    3092:	45 29 d4             	sub    %r10d,%r12d
    3095:	4b 8d 04 64          	lea    (%r12,%r12,2),%rax
    3099:	49 8d 54 85 00       	lea    0x0(%r13,%rax,4),%rdx
    309e:	44 0f b7 42 08       	movzwl 0x8(%rdx),%r8d
    30a3:	41 83 f8 01          	cmp    $0x1,%r8d
    30a7:	75 d7                	jne    3080 <zim_Str_Matcher_getMatchedKeywords+0xe0>
    30a9:	66 3b 4a 0a          	cmp    0xa(%rdx),%cx
    30ad:	75 d7                	jne    3086 <zim_Str_Matcher_getMatchedKeywords+0xe6>
    30af:	44 8b 62 04          	mov    0x4(%rdx),%r12d
    30b3:	45 85 e4             	test   %r12d,%r12d
    30b6:	0f 89 53 01 00 00    	jns    320f <zim_Str_Matcher_getMatchedKeywords+0x26f>
    30bc:	0f 1f 40 00          	nopl   0x0(%rax)
    30c0:	41 81 e4 ff ff ff 7f 	and    $0x7fffffff,%r12d
    30c7:	48 8b 95 c0 fd ff ff 	mov    -0x240(%rbp),%rdx
    30ce:	44 89 e0             	mov    %r12d,%eax
    30d1:	48 8d 04 40          	lea    (%rax,%rax,2),%rax
    30d5:	48 8d 0c 82          	lea    (%rdx,%rax,4),%rcx
    30d9:	49 63 c4             	movslq %r12d,%rax
    30dc:	44 8b 01             	mov    (%rcx),%r8d
    30df:	45 85 c0             	test   %r8d,%r8d
    30e2:	0f 88 e8 01 00 00    	js     32d0 <zim_Str_Matcher_getMatchedKeywords+0x330>
    30e8:	4c 89 7c 24 20       	mov    %r15,0x20(%rsp)
    30ed:	4d 89 f2             	mov    %r14,%r10
    30f0:	49 89 ef             	mov    %rbp,%r15
    30f3:	4d 89 de             	mov    %r11,%r14
    30f6:	44 89 64 24 1c       	mov    %r12d,0x1c(%rsp)
    30fb:	e9 8f 00 00 00       	jmp    318f <zim_Str_Matcher_getMatchedKeywords+0x1ef>
    3100:	4d 8b 47 e8          	mov    -0x18(%r15),%r8
    3104:	41 c6 04 02 01       	movb   $0x1,(%r10,%rax,1)
    3109:	4d 8b 24 c0          	mov    (%r8,%rax,8),%r12
    310d:	4d 89 f0             	mov    %r14,%r8
    3110:	4d 2b 44 24 10       	sub    0x10(%r12),%r8
    3115:	48 81 fb 00 00 00 40 	cmp    $0x40000000,%rbx
    311c:	0f 84 2c f5 ff ff    	je     264e <zim_Str_Matcher_getMatchedKeywords.cold+0x44>
    3122:	48 39 de             	cmp    %rbx,%rsi
    3125:	75 46                	jne    316d <zim_Str_Matcher_getMatchedKeywords+0x1cd>
    3127:	48 85 f6             	test   %rsi,%rsi
    312a:	48 8d 04 36          	lea    (%rsi,%rsi,1),%rax
    312e:	be 10 00 00 00       	mov    $0x10,%esi
    3133:	ba 18 00 00 00       	mov    $0x18,%edx
    3138:	48 0f 45 f0          	cmovne %rax,%rsi
    313c:	31 c9                	xor    %ecx,%ecx
    313e:	4c 89 54 24 10       	mov    %r10,0x10(%rsp)
    3143:	4c 89 44 24 08       	mov    %r8,0x8(%rsp)
    3148:	48 89 34 24          	mov    %rsi,(%rsp)
    314c:	e8 8f f3 ff ff       	call   24e0 <_safe_erealloc@plt>
    3151:	49 8b 97 c0 fd ff ff 	mov    -0x240(%r15),%rdx
    3158:	4c 8b 54 24 10       	mov    0x10(%rsp),%r10
    315d:	4c 8b 44 24 08       	mov    0x8(%rsp),%r8
    3162:	48 8b 34 24          	mov    (%rsp),%rsi
    3166:	48 89 c7             	mov    %rax,%rdi
    3169:	4a 8d 0c 2a          	lea    (%rdx,%r13,1),%rcx
    316d:	48 8d 04 5b          	lea    (%rbx,%rbx,2),%rax
    3171:	48 83 c3 01          	add    $0x1,%rbx
    3175:	4c 89 04 c7          	mov    %r8,(%rdi,%rax,8)
    3179:	4d 8b 44 24 10       	mov    0x10(%r12),%r8
    317e:	89 6c c7 10          	mov    %ebp,0x10(%rdi,%rax,8)
    3182:	4c 89 44 c7 08       	mov    %r8,0x8(%rdi,%rax,8)
    3187:	48 63 41 04          	movslq 0x4(%rcx),%rax
    318b:	85 c0                	test   %eax,%eax
    318d:	78 1d                	js     31ac <zim_Str_Matcher_getMatchedKeywords+0x20c>
    318f:	4c 8d 2c 40          	lea    (%rax,%rax,2),%r13
    3193:	49 c1 e5 02          	shl    $0x2,%r13
    3197:	4a 8d 0c 2a          	lea    (%rdx,%r13,1),%rcx
    319b:	48 63 01             	movslq (%rcx),%rax
    319e:	48 89 c5             	mov    %rax,%rbp
    31a1:	41 80 3c 02 00       	cmpb   $0x0,(%r10,%rax,1)
    31a6:	0f 84 54 ff ff ff    	je     3100 <zim_Str_Matcher_getMatchedKeywords+0x160>
    31ac:	4d 89 f3             	mov    %r14,%r11
    31af:	4c 89 fd             	mov    %r15,%rbp
    31b2:	44 8b 64 24 1c       	mov    0x1c(%rsp),%r12d
    31b7:	4c 8b 7c 24 20       	mov    0x20(%rsp),%r15
    31bc:	4d 89 d6             	mov    %r10,%r14
    31bf:	eb 4e                	jmp    320f <zim_Str_Matcher_getMatchedKeywords+0x26f>
    31c1:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    31c8:	44 8b 62 04          	mov    0x4(%rdx),%r12d
    31cc:	4c 8b 8d a8 fd ff ff 	mov    -0x258(%rbp),%r9
    31d3:	41 83 e8 01          	sub    $0x1,%r8d
    31d7:	4d 01 e0             	add    %r12,%r8
    31da:	4b 8d 04 e1          	lea    (%r9,%r12,8),%rax
    31de:	4f 8d 44 c1 08       	lea    0x8(%r9,%r8,8),%r8
    31e3:	eb 18                	jmp    31fd <zim_Str_Matcher_getMatchedKeywords+0x25d>
    31e5:	66 66 2e 0f 1f 84 00 	data16 cs nopw 0x0(%rax,%rax,1)
    31ec:	00 00 00 00 
    31f0:	48 83 c0 08          	add    $0x8,%rax
    31f4:	49 39 c0             	cmp    %rax,%r8
    31f7:	0f 84 89 fe ff ff    	je     3086 <zim_Str_Matcher_getMatchedKeywords+0xe6>
    31fd:	66 3b 48 04          	cmp    0x4(%rax),%cx
    3201:	75 ed                	jne    31f0 <zim_Str_Matcher_getMatchedKeywords+0x250>
    3203:	44 8b 20             	mov    (%rax),%r12d
    3206:	45 85 e4             	test   %r12d,%r12d
    3209:	0f 88 b1 fe ff ff    	js     30c0 <zim_Str_Matcher_getMatchedKeywords+0x120>
    320f:	4d 3b 5f 10          	cmp    0x10(%r15),%r11
    3213:	0f 82 27 fe ff ff    	jb     3040 <zim_Str_Matcher_getMatchedKeywords+0xa0>
    3219:	48 89 3c 24          	mov    %rdi,(%rsp)
    321d:	4c 89 f7             	mov    %r14,%rdi
    3220:	4c 8b 6c 24 28       	mov    0x28(%rsp),%r13
    3225:	e8 66 f2 ff ff       	call   2490 <_efree@plt>
    322a:	48 83 fb 01          	cmp    $0x1,%rbx
    322e:	4c 8b 04 24          	mov    (%rsp),%r8
    3232:	0f 87 d0 00 00 00    	ja     3308 <zim_Str_Matcher_getMatchedKeywords+0x368>
    3238:	48 85 db             	test   %rbx,%rbx
    323b:	74 3f                	je     327c <zim_Str_Matcher_getMatchedKeywords+0x2dc>
    323d:	4d 8d 70 10          	lea    0x10(%r8),%r14
    3241:	45 31 e4             	xor    %r12d,%r12d
    3244:	4d 89 c7             	mov    %r8,%r15
    3247:	66 0f 1f 84 00 00 00 	nopw   0x0(%rax,%rax,1)
    324e:	00 00 
    3250:	49 63 16             	movslq (%r14),%rdx
    3253:	48 8b 45 e8          	mov    -0x18(%rbp),%rax
    3257:	48 8b 34 d0          	mov    (%rax,%rdx,8),%rsi
    325b:	f6 46 04 40          	testb  $0x40,0x4(%rsi)
    325f:	75 03                	jne    3264 <zim_Str_Matcher_getMatchedKeywords+0x2c4>
    3261:	83 06 01             	addl   $0x1,(%rsi)
    3264:	4c 89 ef             	mov    %r13,%rdi
    3267:	49 83 c4 01          	add    $0x1,%r12
    326b:	49 83 c6 18          	add    $0x18,%r14
    326f:	e8 8c f2 ff ff       	call   2500 <add_next_index_str@plt>
    3274:	49 39 dc             	cmp    %rbx,%r12
    3277:	72 d7                	jb     3250 <zim_Str_Matcher_getMatchedKeywords+0x2b0>
    3279:	4d 89 f8             	mov    %r15,%r8
    327c:	4d 85 c0             	test   %r8,%r8
    327f:	0f 84 70 fd ff ff    	je     2ff5 <zim_Str_Matcher_getMatchedKeywords+0x55>
    3285:	48 83 c4 38          	add    $0x38,%rsp
    3289:	4c 89 c7             	mov    %r8,%rdi
    328c:	5b                   	pop    %rbx
    328d:	5d                   	pop    %rbp
    328e:	41 5c                	pop    %r12
    3290:	41 5d                	pop    %r13
    3292:	41 5e                	pop    %r14
    3294:	41 5f                	pop    %r15
    3296:	e9 f5 f1 ff ff       	jmp    2490 <_efree@plt>
    329b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
    32a0:	45 31 e4             	xor    %r12d,%r12d
    32a3:	e9 67 ff ff ff       	jmp    320f <zim_Str_Matcher_getMatchedKeywords+0x26f>
    32a8:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
    32af:	00 
    32b0:	48 63 85 e0 fd ff ff 	movslq -0x220(%rbp),%rax
    32b7:	48 8b 95 a0 fd ff ff 	mov    -0x260(%rbp),%rdx
    32be:	49 0f af c4          	imul   %r12,%rax
    32c2:	48 01 c8             	add    %rcx,%rax
    32c5:	44 8b 24 82          	mov    (%rdx,%rax,4),%r12d
    32c9:	e9 38 ff ff ff       	jmp    3206 <zim_Str_Matcher_getMatchedKeywords+0x266>
    32ce:	66 90                	xchg   %ax,%ax
    32d0:	48 63 41 04          	movslq 0x4(%rcx),%rax
    32d4:	85 c0                	test   %eax,%eax
    32d6:	0f 89 0c fe ff ff    	jns    30e8 <zim_Str_Matcher_getMatchedKeywords+0x148>
    32dc:	e9 2e ff ff ff       	jmp    320f <zim_Str_Matcher_getMatchedKeywords+0x26f>
    32e1:	4c 8d 67 50          	lea    0x50(%rdi),%r12
    32e5:	be 01 00 00 00       	mov    $0x1,%esi
    32ea:	4c 89 e7             	mov    %r12,%rdi
    32ed:	e8 4e f0 ff ff       	call   2340 <zend_parse_arg_str_slow@plt>
    32f2:	49 89 c6             	mov    %rax,%r14
    32f5:	48 85 c0             	test   %rax,%rax
    32f8:	0f 85 d4 fc ff ff    	jne    2fd2 <zim_Str_Matcher_getMatchedKeywords+0x32>
    32fe:	e9 07 f3 ff ff       	jmp    260a <zim_Str_Matcher_getMatchedKeywords.cold>
    3303:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
    3308:	4c 89 c7             	mov    %r8,%rdi
    330b:	48 8d 0d 3e 0b 00 00 	lea    0xb3e(%rip),%rcx        # 3e50 <ac_hit_compare>
    3312:	ba 18 00 00 00       	mov    $0x18,%edx
    3317:	48 89 de             	mov    %rbx,%rsi
    331a:	e8 b1 ef ff ff       	call   22d0 <qsort@plt>
    331f:	4c 8b 04 24          	mov    (%rsp),%r8
    3323:	e9 15 ff ff ff       	jmp    323d <zim_Str_Matcher_getMatchedKeywords+0x29d>
    3328:	48 83 c4 38          	add    $0x38,%rsp
    332c:	48 89 c7             	mov    %rax,%rdi
    332f:	5b                   	pop    %rbx
    3330:	5d                   	pop    %rbp
    3331:	41 5c                	pop    %r12
    3333:	41 5d                	pop    %r13
    3335:	41 5e                	pop    %r14
    3337:	41 5f                	pop    %r15
    3339:	e9 52 f1 ff ff       	jmp    2490 <_efree@plt>

Disassembly of section .fini:
