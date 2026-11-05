
clang21-strmatch.so:     file format elf64-x86-64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .plt.got:

Disassembly of section .text:

0000000000003590 <zim_Str_Matcher_countMatches>:
    3590:	41 57                	push   %r15
    3592:	41 56                	push   %r14
    3594:	41 54                	push   %r12
    3596:	53                   	push   %rbx
    3597:	50                   	push   %rax
    3598:	83 7f 2c 01          	cmpl   $0x1,0x2c(%rdi)
    359c:	0f 85 7d 01 00 00    	jne    371f <zim_Str_Matcher_countMatches+0x18f>
    35a2:	48 8d 47 50          	lea    0x50(%rdi),%rax
    35a6:	80 7f 58 06          	cmpb   $0x6,0x58(%rdi)
    35aa:	0f 85 89 01 00 00    	jne    3739 <zim_Str_Matcher_countMatches+0x1a9>
    35b0:	48 8b 00             	mov    (%rax),%rax
    35b3:	48 8b 4f 20          	mov    0x20(%rdi),%rcx
    35b7:	83 79 f8 00          	cmpl   $0x0,-0x8(%rcx)
    35bb:	0f 84 22 01 00 00    	je     36e3 <zim_Str_Matcher_countMatches+0x153>
    35c1:	48 8b 50 10          	mov    0x10(%rax),%rdx
    35c5:	45 31 d2             	xor    %r10d,%r10d
    35c8:	48 85 d2             	test   %rdx,%rdx
    35cb:	0f 84 1b 01 00 00    	je     36ec <zim_Str_Matcher_countMatches+0x15c>
    35d1:	49 b8 ff ff ff ff ff 	movabs $0x7fffffffffffffff,%r8
    35d8:	ff ff 7f 
    35db:	45 31 c9             	xor    %r9d,%r9d
    35de:	31 ff                	xor    %edi,%edi
    35e0:	eb 1d                	jmp    35ff <zim_Str_Matcher_countMatches+0x6f>
    35e2:	66 66 66 66 66 2e 0f 	data16 data16 data16 data16 cs nopw 0x0(%rax,%rax,1)
    35e9:	1f 84 00 00 00 00 00 
    35f0:	45 31 d2             	xor    %r10d,%r10d
    35f3:	49 ff c1             	inc    %r9
    35f6:	49 39 d1             	cmp    %rdx,%r9
    35f9:	0f 84 ef 00 00 00    	je     36ee <zim_Str_Matcher_countMatches+0x15e>
    35ff:	46 0f b6 5c 08 18    	movzbl 0x18(%rax,%r9,1),%r11d
    3605:	46 0f b7 9c 59 e4 fd 	movzwl -0x21c(%rcx,%r11,2),%r11d
    360c:	ff ff 
    360e:	4d 85 db             	test   %r11,%r11
    3611:	74 dd                	je     35f0 <zim_Str_Matcher_countMatches+0x60>
    3613:	8b 99 b0 fd ff ff    	mov    -0x250(%rcx),%ebx
    3619:	41 39 da             	cmp    %ebx,%r10d
    361c:	73 52                	jae    3670 <zim_Str_Matcher_countMatches+0xe0>
    361e:	45 89 d2             	mov    %r10d,%r10d
    3621:	48 63 99 e0 fd ff ff 	movslq -0x220(%rcx),%rbx
    3628:	49 0f af da          	imul   %r10,%rbx
    362c:	48 c1 e3 02          	shl    $0x2,%rbx
    3630:	48 03 99 a0 fd ff ff 	add    -0x260(%rcx),%rbx
    3637:	4e 8d 24 9b          	lea    (%rbx,%r11,4),%r12
    363b:	45 8b 14 24          	mov    (%r12),%r10d
    363f:	45 85 d2             	test   %r10d,%r10d
    3642:	79 af                	jns    35f3 <zim_Str_Matcher_countMatches+0x63>
    3644:	41 81 e2 ff ff ff 7f 	and    $0x7fffffff,%r10d
    364b:	4c 8b 99 c0 fd ff ff 	mov    -0x240(%rcx),%r11
    3652:	4b 8d 1c 52          	lea    (%r10,%r10,2),%rbx
    3656:	45 8b 5c 9b 08       	mov    0x8(%r11,%rbx,4),%r11d
    365b:	48 89 fb             	mov    %rdi,%rbx
    365e:	4c 31 c3             	xor    %r8,%rbx
    3661:	4c 39 db             	cmp    %r11,%rbx
    3664:	0f 82 9a 00 00 00    	jb     3704 <zim_Str_Matcher_countMatches+0x174>
    366a:	4c 01 df             	add    %r11,%rdi
    366d:	eb 84                	jmp    35f3 <zim_Str_Matcher_countMatches+0x63>
    366f:	90                   	nop
    3670:	4c 8b b1 c8 fd ff ff 	mov    -0x238(%rcx),%r14
    3677:	eb 16                	jmp    368f <zim_Str_Matcher_countMatches+0xff>
    3679:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    3680:	66 45 3b 5a 0a       	cmp    0xa(%r10),%r11w
    3685:	74 50                	je     36d7 <zim_Str_Matcher_countMatches+0x147>
    3687:	45 8b 12             	mov    (%r10),%r10d
    368a:	41 39 da             	cmp    %ebx,%r10d
    368d:	72 8f                	jb     361e <zim_Str_Matcher_countMatches+0x8e>
    368f:	41 29 da             	sub    %ebx,%r10d
    3692:	4f 8d 3c 52          	lea    (%r10,%r10,2),%r15
    3696:	4f 8d 14 be          	lea    (%r14,%r15,4),%r10
    369a:	47 0f b7 7c be 08    	movzwl 0x8(%r14,%r15,4),%r15d
    36a0:	45 85 ff             	test   %r15d,%r15d
    36a3:	74 e2                	je     3687 <zim_Str_Matcher_countMatches+0xf7>
    36a5:	41 83 ff 01          	cmp    $0x1,%r15d
    36a9:	74 d5                	je     3680 <zim_Str_Matcher_countMatches+0xf0>
    36ab:	45 8b 62 04          	mov    0x4(%r10),%r12d
    36af:	49 c1 e4 03          	shl    $0x3,%r12
    36b3:	4c 03 a1 a8 fd ff ff 	add    -0x258(%rcx),%r12
    36ba:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
    36c0:	66 45 39 5c 24 04    	cmp    %r11w,0x4(%r12)
    36c6:	0f 84 6f ff ff ff    	je     363b <zim_Str_Matcher_countMatches+0xab>
    36cc:	49 83 c4 08          	add    $0x8,%r12
    36d0:	49 ff cf             	dec    %r15
    36d3:	75 eb                	jne    36c0 <zim_Str_Matcher_countMatches+0x130>
    36d5:	eb b0                	jmp    3687 <zim_Str_Matcher_countMatches+0xf7>
    36d7:	49 83 c2 04          	add    $0x4,%r10
    36db:	4d 89 d4             	mov    %r10,%r12
    36de:	e9 58 ff ff ff       	jmp    363b <zim_Str_Matcher_countMatches+0xab>
    36e3:	48 c7 06 00 00 00 00 	movq   $0x0,(%rsi)
    36ea:	eb 05                	jmp    36f1 <zim_Str_Matcher_countMatches+0x161>
    36ec:	31 ff                	xor    %edi,%edi
    36ee:	48 89 3e             	mov    %rdi,(%rsi)
    36f1:	c7 46 08 04 00 00 00 	movl   $0x4,0x8(%rsi)
    36f8:	48 83 c4 08          	add    $0x8,%rsp
    36fc:	5b                   	pop    %rbx
    36fd:	41 5c                	pop    %r12
    36ff:	41 5e                	pop    %r14
    3701:	41 5f                	pop    %r15
    3703:	c3                   	ret
    3704:	48 8d 35 43 29 00 00 	lea    0x2943(%rip),%rsi        # 604e <_fini+0xd62>
    370b:	31 ff                	xor    %edi,%edi
    370d:	31 c0                	xor    %eax,%eax
    370f:	48 83 c4 08          	add    $0x8,%rsp
    3713:	5b                   	pop    %rbx
    3714:	41 5c                	pop    %r12
    3716:	41 5e                	pop    %r14
    3718:	41 5f                	pop    %r15
    371a:	e9 51 eb ff ff       	jmp    2270 <zend_throw_error@plt>
    371f:	bf 01 00 00 00       	mov    $0x1,%edi
    3724:	be 01 00 00 00       	mov    $0x1,%esi
    3729:	e8 92 e9 ff ff       	call   20c0 <zend_wrong_parameters_count_error@plt>
    372e:	b0 01                	mov    $0x1,%al
    3730:	31 db                	xor    %ebx,%ebx
    3732:	45 31 c0             	xor    %r8d,%r8d
    3735:	31 c9                	xor    %ecx,%ecx
    3737:	eb 2a                	jmp    3763 <zim_Str_Matcher_countMatches+0x1d3>
    3739:	49 89 ff             	mov    %rdi,%r15
    373c:	49 89 f4             	mov    %rsi,%r12
    373f:	bb 01 00 00 00       	mov    $0x1,%ebx
    3744:	49 89 c6             	mov    %rax,%r14
    3747:	48 89 c7             	mov    %rax,%rdi
    374a:	be 01 00 00 00       	mov    $0x1,%esi
    374f:	e8 5c e9 ff ff       	call   20b0 <zend_parse_arg_str_slow@plt>
    3754:	48 85 c0             	test   %rax,%rax
    3757:	75 21                	jne    377a <zim_Str_Matcher_countMatches+0x1ea>
    3759:	b9 04 00 00 00       	mov    $0x4,%ecx
    375e:	b0 0c                	mov    $0xc,%al
    3760:	4d 89 f0             	mov    %r14,%r8
    3763:	0f b6 f8             	movzbl %al,%edi
    3766:	89 de                	mov    %ebx,%esi
    3768:	31 d2                	xor    %edx,%edx
    376a:	48 83 c4 08          	add    $0x8,%rsp
    376e:	5b                   	pop    %rbx
    376f:	41 5c                	pop    %r12
    3771:	41 5e                	pop    %r14
    3773:	41 5f                	pop    %r15
    3775:	e9 76 ea ff ff       	jmp    21f0 <zend_wrong_parameter_error@plt>
    377a:	4c 89 e6             	mov    %r12,%rsi
    377d:	4c 89 ff             	mov    %r15,%rdi
    3780:	e9 2e fe ff ff       	jmp    35b3 <zim_Str_Matcher_countMatches+0x23>

Disassembly of section .fini:
