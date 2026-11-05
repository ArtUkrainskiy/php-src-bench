
gcc15-strmatch.so:     file format elf64-x86-64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .plt.got:

Disassembly of section .plt.sec:

Disassembly of section .text:

00000000000033b0 <zim_Str_Replacer_replace>:
    33b0:	f3 0f 1e fa          	endbr64
    33b4:	41 57                	push   %r15
    33b6:	41 56                	push   %r14
    33b8:	41 55                	push   %r13
    33ba:	41 54                	push   %r12
    33bc:	55                   	push   %rbp
    33bd:	53                   	push   %rbx
    33be:	48 83 ec 78          	sub    $0x78,%rsp
    33c2:	48 89 74 24 08       	mov    %rsi,0x8(%rsp)
    33c7:	64 48 8b 2c 25 28 00 	mov    %fs:0x28,%rbp
    33ce:	00 00 
    33d0:	48 89 6c 24 68       	mov    %rbp,0x68(%rsp)
    33d5:	8b 6f 2c             	mov    0x2c(%rdi),%ebp
    33d8:	8d 45 ff             	lea    -0x1(%rbp),%eax
    33db:	83 f8 01             	cmp    $0x1,%eax
    33de:	0f 87 b6 f2 ff ff    	ja     269a <zim_Str_Replacer_replace.cold>
    33e4:	48 89 fb             	mov    %rdi,%rbx
    33e7:	80 7f 58 06          	cmpb   $0x6,0x58(%rdi)
    33eb:	0f 85 9a 05 00 00    	jne    398b <zim_Str_Replacer_replace+0x5db>
    33f1:	4c 8b 77 50          	mov    0x50(%rdi),%r14
    33f5:	31 c0                	xor    %eax,%eax
    33f7:	48 8d 53 60          	lea    0x60(%rbx),%rdx
    33fb:	83 fd 01             	cmp    $0x1,%ebp
    33fe:	4c 8b 63 20          	mov    0x20(%rbx),%r12
    3402:	48 0f 45 c2          	cmovne %rdx,%rax
    3406:	48 89 44 24 10       	mov    %rax,0x10(%rsp)
    340b:	41 8b 44 24 f8       	mov    -0x8(%r12),%eax
    3410:	85 c0                	test   %eax,%eax
    3412:	0f 84 11 01 00 00    	je     3529 <zim_Str_Replacer_replace+0x179>
    3418:	49 8b 6e 10          	mov    0x10(%r14),%rbp
    341c:	48 85 ed             	test   %rbp,%rbp
    341f:	0f 84 04 01 00 00    	je     3529 <zim_Str_Replacer_replace+0x179>
    3425:	45 31 db             	xor    %r11d,%r11d
    3428:	45 31 ed             	xor    %r13d,%r13d
    342b:	31 f6                	xor    %esi,%esi
    342d:	45 31 ff             	xor    %r15d,%r15d
    3430:	45 31 d2             	xor    %r10d,%r10d
    3433:	31 db                	xor    %ebx,%ebx
    3435:	66 66 2e 0f 1f 84 00 	data16 cs nopw 0x0(%rax,%rax,1)
    343c:	00 00 00 00 
    3440:	49 89 e8             	mov    %rbp,%r8
    3443:	48 83 ed 01          	sub    $0x1,%rbp
    3447:	41 0f b6 44 2e 18    	movzbl 0x18(%r14,%rbp,1),%eax
    344d:	41 0f b7 8c 44 e4 fd 	movzwl -0x21c(%r12,%rax,2),%ecx
    3454:	ff ff 
    3456:	66 85 c9             	test   %cx,%cx
    3459:	0f 84 99 01 00 00    	je     35f8 <zim_Str_Replacer_replace+0x248>
    345f:	41 8b bc 24 b0 fd ff 	mov    -0x250(%r12),%edi
    3466:	ff 
    3467:	39 fb                	cmp    %edi,%ebx
    3469:	0f 82 98 01 00 00    	jb     3607 <zim_Str_Replacer_replace+0x257>
    346f:	4c 89 2c 24          	mov    %r13,(%rsp)
    3473:	4d 8b 8c 24 c8 fd ff 	mov    -0x238(%r12),%r9
    347a:	ff 
    347b:	4d 89 fd             	mov    %r15,%r13
    347e:	eb 10                	jmp    3490 <zim_Str_Replacer_replace+0xe0>
    3480:	0f 87 22 01 00 00    	ja     35a8 <zim_Str_Replacer_replace+0x1f8>
    3486:	8b 1a                	mov    (%rdx),%ebx
    3488:	39 fb                	cmp    %edi,%ebx
    348a:	0f 82 70 01 00 00    	jb     3600 <zim_Str_Replacer_replace+0x250>
    3490:	29 fb                	sub    %edi,%ebx
    3492:	48 8d 04 5b          	lea    (%rbx,%rbx,2),%rax
    3496:	49 8d 14 81          	lea    (%r9,%rax,4),%rdx
    349a:	0f b7 5a 08          	movzwl 0x8(%rdx),%ebx
    349e:	83 fb 01             	cmp    $0x1,%ebx
    34a1:	75 dd                	jne    3480 <zim_Str_Replacer_replace+0xd0>
    34a3:	66 3b 4a 0a          	cmp    0xa(%rdx),%cx
    34a7:	75 dd                	jne    3486 <zim_Str_Replacer_replace+0xd6>
    34a9:	4d 89 ef             	mov    %r13,%r15
    34ac:	8b 5a 04             	mov    0x4(%rdx),%ebx
    34af:	4c 8b 2c 24          	mov    (%rsp),%r13
    34b3:	66 90                	xchg   %ax,%ax
    34b5:	66 66 2e 0f 1f 84 00 	data16 cs nopw 0x0(%rax,%rax,1)
    34bc:	00 00 00 00 
    34c0:	85 db                	test   %ebx,%ebx
    34c2:	79 4f                	jns    3513 <zim_Str_Replacer_replace+0x163>
    34c4:	81 e3 ff ff ff 7f    	and    $0x7fffffff,%ebx
    34ca:	4d 85 d2             	test   %r10,%r10
    34cd:	75 1a                	jne    34e9 <zim_Str_Replacer_replace+0x139>
    34cf:	4d 89 c7             	mov    %r8,%r15
    34d2:	b8 00 01 00 00       	mov    $0x100,%eax
    34d7:	4d 89 c2             	mov    %r8,%r10
    34da:	49 c1 ef 04          	shr    $0x4,%r15
    34de:	49 c1 e7 02          	shl    $0x2,%r15
    34e2:	49 39 c7             	cmp    %rax,%r15
    34e5:	4c 0f 47 f8          	cmova  %rax,%r15
    34e9:	4c 39 ee             	cmp    %r13,%rsi
    34ec:	0f 84 3e 01 00 00    	je     3630 <zim_Str_Replacer_replace+0x280>
    34f2:	49 8b 8c 24 d0 fd ff 	mov    -0x230(%r12),%rcx
    34f9:	ff 
    34fa:	89 da                	mov    %ebx,%edx
    34fc:	4c 89 e8             	mov    %r13,%rax
    34ff:	49 83 c5 01          	add    $0x1,%r13
    3503:	48 c1 e0 04          	shl    $0x4,%rax
    3507:	8b 14 91             	mov    (%rcx,%rdx,4),%edx
    350a:	49 89 2c 03          	mov    %rbp,(%r11,%rax,1)
    350e:	41 89 54 03 08       	mov    %edx,0x8(%r11,%rax,1)
    3513:	48 85 ed             	test   %rbp,%rbp
    3516:	0f 85 24 ff ff ff    	jne    3440 <zim_Str_Replacer_replace+0x90>
    351c:	4c 89 14 24          	mov    %r10,(%rsp)
    3520:	4d 85 d2             	test   %r10,%r10
    3523:	0f 85 17 07 00 00    	jne    3c40 <zim_Str_Replacer_replace+0x890>
    3529:	48 8b 44 24 08       	mov    0x8(%rsp),%rax
    352e:	4c 89 30             	mov    %r14,(%rax)
    3531:	b8 06 00 00 00       	mov    $0x6,%eax
    3536:	41 f6 46 04 40       	testb  $0x40,0x4(%r14)
    353b:	74 5b                	je     3598 <zim_Str_Replacer_replace+0x1e8>
    353d:	48 8b 74 24 08       	mov    0x8(%rsp),%rsi
    3542:	89 46 08             	mov    %eax,0x8(%rsi)
    3545:	48 8b 44 24 10       	mov    0x10(%rsp),%rax
    354a:	48 85 c0             	test   %rax,%rax
    354d:	74 26                	je     3575 <zim_Str_Replacer_replace+0x1c5>
    354f:	48 8b 18             	mov    (%rax),%rbx
    3552:	48 83 7b 18 00       	cmpq   $0x0,0x18(%rbx)
    3557:	0f 85 02 04 00 00    	jne    395f <zim_Str_Replacer_replace+0x5af>
    355d:	48 8d 7b 08          	lea    0x8(%rbx),%rdi
    3561:	e8 2a ee ff ff       	call   2390 <zval_ptr_safe_dtor@plt>
    3566:	48 c7 43 08 00 00 00 	movq   $0x0,0x8(%rbx)
    356d:	00 
    356e:	c7 43 10 04 00 00 00 	movl   $0x4,0x10(%rbx)
    3575:	48 8b 44 24 68       	mov    0x68(%rsp),%rax
    357a:	64 48 2b 04 25 28 00 	sub    %fs:0x28,%rax
    3581:	00 00 
    3583:	0f 85 c4 06 00 00    	jne    3c4d <zim_Str_Replacer_replace+0x89d>
    3589:	48 83 c4 78          	add    $0x78,%rsp
    358d:	5b                   	pop    %rbx
    358e:	5d                   	pop    %rbp
    358f:	41 5c                	pop    %r12
    3591:	41 5d                	pop    %r13
    3593:	41 5e                	pop    %r14
    3595:	41 5f                	pop    %r15
    3597:	c3                   	ret
    3598:	41 83 06 01          	addl   $0x1,(%r14)
    359c:	b8 06 01 00 00       	mov    $0x106,%eax
    35a1:	eb 9a                	jmp    353d <zim_Str_Replacer_replace+0x18d>
    35a3:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
    35a8:	44 8b 7a 04          	mov    0x4(%rdx),%r15d
    35ac:	49 8b 84 24 a8 fd ff 	mov    -0x258(%r12),%rax
    35b3:	ff 
    35b4:	83 eb 01             	sub    $0x1,%ebx
    35b7:	4c 01 fb             	add    %r15,%rbx
    35ba:	4a 8d 04 f8          	lea    (%rax,%r15,8),%rax
    35be:	4d 8b bc 24 a8 fd ff 	mov    -0x258(%r12),%r15
    35c5:	ff 
    35c6:	49 8d 5c df 08       	lea    0x8(%r15,%rbx,8),%rbx
    35cb:	eb 10                	jmp    35dd <zim_Str_Replacer_replace+0x22d>
    35cd:	0f 1f 00             	nopl   (%rax)
    35d0:	48 83 c0 08          	add    $0x8,%rax
    35d4:	48 39 c3             	cmp    %rax,%rbx
    35d7:	0f 84 a9 fe ff ff    	je     3486 <zim_Str_Replacer_replace+0xd6>
    35dd:	66 3b 48 04          	cmp    0x4(%rax),%cx
    35e1:	75 ed                	jne    35d0 <zim_Str_Replacer_replace+0x220>
    35e3:	4d 89 ef             	mov    %r13,%r15
    35e6:	8b 18                	mov    (%rax),%ebx
    35e8:	4c 8b 2c 24          	mov    (%rsp),%r13
    35ec:	e9 cf fe ff ff       	jmp    34c0 <zim_Str_Replacer_replace+0x110>
    35f1:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    35f8:	31 db                	xor    %ebx,%ebx
    35fa:	e9 14 ff ff ff       	jmp    3513 <zim_Str_Replacer_replace+0x163>
    35ff:	90                   	nop
    3600:	4d 89 ef             	mov    %r13,%r15
    3603:	4c 8b 2c 24          	mov    (%rsp),%r13
    3607:	49 63 84 24 e0 fd ff 	movslq -0x220(%r12),%rax
    360e:	ff 
    360f:	49 8b 94 24 a0 fd ff 	mov    -0x260(%r12),%rdx
    3616:	ff 
    3617:	48 0f af c3          	imul   %rbx,%rax
    361b:	48 01 c8             	add    %rcx,%rax
    361e:	8b 1c 82             	mov    (%rdx,%rax,4),%ebx
    3621:	e9 9a fe ff ff       	jmp    34c0 <zim_Str_Replacer_replace+0x110>
    3626:	66 2e 0f 1f 84 00 00 	cs nopw 0x0(%rax,%rax,1)
    362d:	00 00 00 
    3630:	4d 39 ef             	cmp    %r13,%r15
    3633:	0f 85 a7 02 00 00    	jne    38e0 <zim_Str_Replacer_replace+0x530>
    3639:	49 81 fd ff 00 00 00 	cmp    $0xff,%r13
    3640:	0f 86 9a 02 00 00    	jbe    38e0 <zim_Str_Replacer_replace+0x530>
    3646:	4c 89 d0             	mov    %r10,%rax
    3649:	48 c1 e8 06          	shr    $0x6,%rax
    364d:	49 39 c5             	cmp    %rax,%r13
    3650:	0f 82 dd 02 00 00    	jb     3933 <zim_Str_Replacer_replace+0x583>
    3656:	31 d2                	xor    %edx,%edx
    3658:	be 04 00 00 00       	mov    $0x4,%esi
    365d:	4c 89 d7             	mov    %r10,%rdi
    3660:	4c 89 5c 24 20       	mov    %r11,0x20(%rsp)
    3665:	4c 89 44 24 18       	mov    %r8,0x18(%rsp)
    366a:	4c 89 14 24          	mov    %r10,(%rsp)
    366e:	e8 8d ec ff ff       	call   2300 <_safe_emalloc@plt>
    3673:	4c 8b 44 24 18       	mov    0x18(%rsp),%r8
    3678:	4c 3b 04 24          	cmp    (%rsp),%r8
    367c:	4c 8b 5c 24 20       	mov    0x20(%rsp),%r11
    3681:	49 89 c7             	mov    %rax,%r15
    3684:	73 28                	jae    36ae <zim_Str_Replacer_replace+0x2fe>
    3686:	48 8b 14 24          	mov    (%rsp),%rdx
    368a:	4b 8d 3c 87          	lea    (%r15,%r8,4),%rdi
    368e:	be ff 00 00 00       	mov    $0xff,%esi
    3693:	4c 89 5c 24 18       	mov    %r11,0x18(%rsp)
    3698:	4c 29 c2             	sub    %r8,%rdx
    369b:	48 c1 e2 02          	shl    $0x2,%rdx
    369f:	e8 cc ec ff ff       	call   2370 <memset@plt>
    36a4:	4c 8b 5c 24 18       	mov    0x18(%rsp),%r11
    36a9:	4d 85 ed             	test   %r13,%r13
    36ac:	74 20                	je     36ce <zim_Str_Replacer_replace+0x31e>
    36ae:	4c 89 ee             	mov    %r13,%rsi
    36b1:	4c 89 d8             	mov    %r11,%rax
    36b4:	48 c1 e6 04          	shl    $0x4,%rsi
    36b8:	4c 01 de             	add    %r11,%rsi
    36bb:	8b 48 08             	mov    0x8(%rax),%ecx
    36be:	48 8b 10             	mov    (%rax),%rdx
    36c1:	48 83 c0 10          	add    $0x10,%rax
    36c5:	41 89 0c 97          	mov    %ecx,(%r15,%rdx,4)
    36c9:	48 39 c6             	cmp    %rax,%rsi
    36cc:	75 ed                	jne    36bb <zim_Str_Replacer_replace+0x30b>
    36ce:	4d 85 db             	test   %r11,%r11
    36d1:	74 08                	je     36db <zim_Str_Replacer_replace+0x32b>
    36d3:	4c 89 df             	mov    %r11,%rdi
    36d6:	e8 b5 ed ff ff       	call   2490 <_efree@plt>
    36db:	49 8b b4 24 d0 fd ff 	mov    -0x230(%r12),%rsi
    36e2:	ff 
    36e3:	89 d8                	mov    %ebx,%eax
    36e5:	8b 04 86             	mov    (%rsi,%rax,4),%eax
    36e8:	41 89 04 af          	mov    %eax,(%r15,%rbp,4)
    36ec:	48 85 ed             	test   %rbp,%rbp
    36ef:	0f 84 9c 00 00 00    	je     3791 <zim_Str_Replacer_replace+0x3e1>
    36f5:	66 66 2e 0f 1f 84 00 	data16 cs nopw 0x0(%rax,%rax,1)
    36fc:	00 00 00 00 
    3700:	48 83 ed 01          	sub    $0x1,%rbp
    3704:	41 0f b6 44 2e 18    	movzbl 0x18(%r14,%rbp,1),%eax
    370a:	41 0f b7 8c 44 e4 fd 	movzwl -0x21c(%r12,%rax,2),%ecx
    3711:	ff ff 
    3713:	66 85 c9             	test   %cx,%cx
    3716:	0f 84 14 03 00 00    	je     3a30 <zim_Str_Replacer_replace+0x680>
    371c:	45 8b 84 24 b0 fd ff 	mov    -0x250(%r12),%r8d
    3723:	ff 
    3724:	44 39 c3             	cmp    %r8d,%ebx
    3727:	0f 82 0f 03 00 00    	jb     3a3c <zim_Str_Replacer_replace+0x68c>
    372d:	4d 8b 8c 24 c8 fd ff 	mov    -0x238(%r12),%r9
    3734:	ff 
    3735:	eb 1a                	jmp    3751 <zim_Str_Replacer_replace+0x3a1>
    3737:	66 0f 1f 84 00 00 00 	nopw   0x0(%rax,%rax,1)
    373e:	00 00 
    3740:	0f 87 aa 02 00 00    	ja     39f0 <zim_Str_Replacer_replace+0x640>
    3746:	8b 1a                	mov    (%rdx),%ebx
    3748:	44 39 c3             	cmp    %r8d,%ebx
    374b:	0f 82 eb 02 00 00    	jb     3a3c <zim_Str_Replacer_replace+0x68c>
    3751:	44 29 c3             	sub    %r8d,%ebx
    3754:	48 8d 04 5b          	lea    (%rbx,%rbx,2),%rax
    3758:	49 8d 14 81          	lea    (%r9,%rax,4),%rdx
    375c:	0f b7 7a 08          	movzwl 0x8(%rdx),%edi
    3760:	83 ff 01             	cmp    $0x1,%edi
    3763:	75 db                	jne    3740 <zim_Str_Replacer_replace+0x390>
    3765:	66 3b 4a 0a          	cmp    0xa(%rdx),%cx
    3769:	75 db                	jne    3746 <zim_Str_Replacer_replace+0x396>
    376b:	8b 5a 04             	mov    0x4(%rdx),%ebx
    376e:	66 90                	xchg   %ax,%ax
    3770:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
    3775:	85 db                	test   %ebx,%ebx
    3777:	79 0b                	jns    3784 <zim_Str_Replacer_replace+0x3d4>
    3779:	81 e3 ff ff ff 7f    	and    $0x7fffffff,%ebx
    377f:	89 d8                	mov    %ebx,%eax
    3781:	8b 04 86             	mov    (%rsi,%rax,4),%eax
    3784:	41 89 04 af          	mov    %eax,(%r15,%rbp,4)
    3788:	48 85 ed             	test   %rbp,%rbp
    378b:	0f 85 6f ff ff ff    	jne    3700 <zim_Str_Replacer_replace+0x350>
    3791:	45 31 db             	xor    %r11d,%r11d
    3794:	66 0f ef c0          	pxor   %xmm0,%xmm0
    3798:	31 ed                	xor    %ebp,%ebp
    379a:	48 8d 44 24 50       	lea    0x50(%rsp),%rax
    379f:	4c 89 74 24 20       	mov    %r14,0x20(%rsp)
    37a4:	48 89 44 24 48       	mov    %rax,0x48(%rsp)
    37a9:	45 31 c0             	xor    %r8d,%r8d
    37ac:	48 89 eb             	mov    %rbp,%rbx
    37af:	4d 89 e6             	mov    %r12,%r14
    37b2:	48 c7 44 24 18 00 00 	movq   $0x0,0x18(%rsp)
    37b9:	00 00 
    37bb:	4c 89 5c 24 28       	mov    %r11,0x28(%rsp)
    37c0:	0f 29 44 24 50       	movaps %xmm0,0x50(%rsp)
    37c5:	e9 a3 00 00 00       	jmp    386d <zim_Str_Replacer_replace+0x4bd>
    37ca:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
    37d0:	49 89 da             	mov    %rbx,%r10
    37d3:	4d 29 c2             	sub    %r8,%r10
    37d6:	48 85 d2             	test   %rdx,%rdx
    37d9:	0f 84 99 03 00 00    	je     3b78 <zim_Str_Replacer_replace+0x7c8>
    37df:	48 8b 42 10          	mov    0x10(%rdx),%rax
    37e3:	4d 8d 24 02          	lea    (%r10,%rax,1),%r12
    37e7:	4c 3b 64 24 58       	cmp    0x58(%rsp),%r12
    37ec:	0f 83 89 03 00 00    	jae    3b7b <zim_Str_Replacer_replace+0x7cb>
    37f2:	48 8d 7c 02 18       	lea    0x18(%rdx,%rax,1),%rdi
    37f7:	48 8b 44 24 20       	mov    0x20(%rsp),%rax
    37fc:	4c 89 d2             	mov    %r10,%rdx
    37ff:	4a 8d 74 00 18       	lea    0x18(%rax,%r8,1),%rsi
    3804:	e8 97 eb ff ff       	call   23a0 <memcpy@plt>
    3809:	49 8b 76 f0          	mov    -0x10(%r14),%rsi
    380d:	48 63 d5             	movslq %ebp,%rdx
    3810:	48 8b 44 24 50       	mov    0x50(%rsp),%rax
    3815:	48 8d 2c d5 00 00 00 	lea    0x0(,%rdx,8),%rbp
    381c:	00 
    381d:	4c 8b 04 d6          	mov    (%rsi,%rdx,8),%r8
    3821:	4c 89 60 10          	mov    %r12,0x10(%rax)
    3825:	49 8b 70 10          	mov    0x10(%r8),%rsi
    3829:	49 83 c0 18          	add    $0x18,%r8
    382d:	49 01 f4             	add    %rsi,%r12
    3830:	4c 3b 64 24 58       	cmp    0x58(%rsp),%r12
    3835:	0f 83 98 00 00 00    	jae    38d3 <zim_Str_Replacer_replace+0x523>
    383b:	48 8b 50 10          	mov    0x10(%rax),%rdx
    383f:	48 8d 7c 10 18       	lea    0x18(%rax,%rdx,1),%rdi
    3844:	48 89 f2             	mov    %rsi,%rdx
    3847:	4c 89 c6             	mov    %r8,%rsi
    384a:	e8 51 eb ff ff       	call   23a0 <memcpy@plt>
    384f:	48 8b 44 24 50       	mov    0x50(%rsp),%rax
    3854:	48 83 44 24 18 01    	addq   $0x1,0x18(%rsp)
    385a:	4c 89 60 10          	mov    %r12,0x10(%rax)
    385e:	49 8b 46 e8          	mov    -0x18(%r14),%rax
    3862:	48 8b 04 28          	mov    (%rax,%rbp,1),%rax
    3866:	48 03 58 10          	add    0x10(%rax),%rbx
    386a:	49 89 d8             	mov    %rbx,%r8
    386d:	4d 85 ff             	test   %r15,%r15
    3870:	0f 84 4a 01 00 00    	je     39c0 <zim_Str_Replacer_replace+0x610>
    3876:	48 3b 1c 24          	cmp    (%rsp),%rbx
    387a:	0f 83 e9 01 00 00    	jae    3a69 <zim_Str_Replacer_replace+0x6b9>
    3880:	41 8b 2c 9f          	mov    (%r15,%rbx,4),%ebp
    3884:	85 ed                	test   %ebp,%ebp
    3886:	0f 88 cf 01 00 00    	js     3a5b <zim_Str_Replacer_replace+0x6ab>
    388c:	48 8b 54 24 50       	mov    0x50(%rsp),%rdx
    3891:	48 89 d0             	mov    %rdx,%rax
    3894:	49 39 d8             	cmp    %rbx,%r8
    3897:	0f 82 33 ff ff ff    	jb     37d0 <zim_Str_Replacer_replace+0x420>
    389d:	49 8b 76 f0          	mov    -0x10(%r14),%rsi
    38a1:	48 63 d5             	movslq %ebp,%rdx
    38a4:	48 8d 2c d5 00 00 00 	lea    0x0(,%rdx,8),%rbp
    38ab:	00 
    38ac:	4c 8b 04 d6          	mov    (%rsi,%rdx,8),%r8
    38b0:	49 8b 70 10          	mov    0x10(%r8),%rsi
    38b4:	49 83 c0 18          	add    $0x18,%r8
    38b8:	48 85 c0             	test   %rax,%rax
    38bb:	0f 84 83 02 00 00    	je     3b44 <zim_Str_Replacer_replace+0x794>
    38c1:	4c 8b 60 10          	mov    0x10(%rax),%r12
    38c5:	49 01 f4             	add    %rsi,%r12
    38c8:	4c 3b 64 24 58       	cmp    0x58(%rsp),%r12
    38cd:	0f 82 68 ff ff ff    	jb     383b <zim_Str_Replacer_replace+0x48b>
    38d3:	48 89 74 24 30       	mov    %rsi,0x30(%rsp)
    38d8:	4c 89 e6             	mov    %r12,%rsi
    38db:	e9 69 02 00 00       	jmp    3b49 <zim_Str_Replacer_replace+0x799>
    38e0:	49 39 f7             	cmp    %rsi,%r15
    38e3:	0f 84 69 03 00 00    	je     3c52 <zim_Str_Replacer_replace+0x8a2>
    38e9:	b8 10 00 00 00       	mov    $0x10,%eax
    38ee:	48 8d 14 36          	lea    (%rsi,%rsi,1),%rdx
    38f2:	49 39 c7             	cmp    %rax,%r15
    38f5:	49 0f 46 c7          	cmovbe %r15,%rax
    38f9:	4c 39 fa             	cmp    %r15,%rdx
    38fc:	49 0f 47 d7          	cmova  %r15,%rdx
    3900:	48 85 f6             	test   %rsi,%rsi
    3903:	48 0f 45 c2          	cmovne %rdx,%rax
    3907:	48 89 c6             	mov    %rax,%rsi
    390a:	4c 89 df             	mov    %r11,%rdi
    390d:	31 c9                	xor    %ecx,%ecx
    390f:	ba 10 00 00 00       	mov    $0x10,%edx
    3914:	4c 89 54 24 18       	mov    %r10,0x18(%rsp)
    3919:	48 89 34 24          	mov    %rsi,(%rsp)
    391d:	e8 be eb ff ff       	call   24e0 <_safe_erealloc@plt>
    3922:	4c 8b 54 24 18       	mov    0x18(%rsp),%r10
    3927:	48 8b 34 24          	mov    (%rsp),%rsi
    392b:	49 89 c3             	mov    %rax,%r11
    392e:	e9 bf fb ff ff       	jmp    34f2 <zim_Str_Replacer_replace+0x142>
    3933:	4c 89 d2             	mov    %r10,%rdx
    3936:	48 29 ea             	sub    %rbp,%rdx
    3939:	48 c1 ea 06          	shr    $0x6,%rdx
    393d:	4c 39 ea             	cmp    %r13,%rdx
    3940:	0f 82 10 fd ff ff    	jb     3656 <zim_Str_Replacer_replace+0x2a6>
    3946:	4c 8d 3c 36          	lea    (%rsi,%rsi,1),%r15
    394a:	49 39 c7             	cmp    %rax,%r15
    394d:	4c 0f 47 f8          	cmova  %rax,%r15
    3951:	49 39 f7             	cmp    %rsi,%r15
    3954:	0f 84 fc fc ff ff    	je     3656 <zim_Str_Replacer_replace+0x2a6>
    395a:	4c 89 fe             	mov    %r15,%rsi
    395d:	eb ab                	jmp    390a <zim_Str_Replacer_replace+0x55a>
    395f:	48 8b 44 24 68       	mov    0x68(%rsp),%rax
    3964:	64 48 2b 04 25 28 00 	sub    %fs:0x28,%rax
    396b:	00 00 
    396d:	0f 85 d5 02 00 00    	jne    3c48 <zim_Str_Replacer_replace+0x898>
    3973:	48 83 c4 78          	add    $0x78,%rsp
    3977:	48 89 df             	mov    %rbx,%rdi
    397a:	31 f6                	xor    %esi,%esi
    397c:	5b                   	pop    %rbx
    397d:	5d                   	pop    %rbp
    397e:	41 5c                	pop    %r12
    3980:	41 5d                	pop    %r13
    3982:	41 5e                	pop    %r14
    3984:	41 5f                	pop    %r15
    3986:	e9 a5 ea ff ff       	jmp    2430 <zend_try_assign_typed_ref_long@plt>
    398b:	4c 8d 67 50          	lea    0x50(%rdi),%r12
    398f:	be 01 00 00 00       	mov    $0x1,%esi
    3994:	4c 89 e7             	mov    %r12,%rdi
    3997:	e8 a4 e9 ff ff       	call   2340 <zend_parse_arg_str_slow@plt>
    399c:	49 89 c6             	mov    %rax,%r14
    399f:	48 85 c0             	test   %rax,%rax
    39a2:	0f 85 4d fa ff ff    	jne    33f5 <zim_Str_Replacer_replace+0x45>
    39a8:	e9 33 ed ff ff       	jmp    26e0 <zim_Str_Replacer_replace.cold+0x46>
    39ad:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
    39b4:	00 
    39b5:	66 66 2e 0f 1f 84 00 	data16 cs nopw 0x0(%rax,%rax,1)
    39bc:	00 00 00 00 
    39c0:	4d 85 ed             	test   %r13,%r13
    39c3:	0f 84 0f 02 00 00    	je     3bd8 <zim_Str_Replacer_replace+0x828>
    39c9:	49 83 ed 01          	sub    $0x1,%r13
    39cd:	4c 89 e8             	mov    %r13,%rax
    39d0:	48 c1 e0 04          	shl    $0x4,%rax
    39d4:	48 03 44 24 28       	add    0x28(%rsp),%rax
    39d9:	48 8b 10             	mov    (%rax),%rdx
    39dc:	48 39 da             	cmp    %rbx,%rdx
    39df:	72 df                	jb     39c0 <zim_Str_Replacer_replace+0x610>
    39e1:	8b 68 08             	mov    0x8(%rax),%ebp
    39e4:	48 89 d3             	mov    %rdx,%rbx
    39e7:	e9 a0 fe ff ff       	jmp    388c <zim_Str_Replacer_replace+0x4dc>
    39ec:	0f 1f 40 00          	nopl   0x0(%rax)
    39f0:	44 8b 5a 04          	mov    0x4(%rdx),%r11d
    39f4:	4d 8b 94 24 a8 fd ff 	mov    -0x258(%r12),%r10
    39fb:	ff 
    39fc:	83 ef 01             	sub    $0x1,%edi
    39ff:	4c 01 df             	add    %r11,%rdi
    3a02:	4b 8d 04 da          	lea    (%r10,%r11,8),%rax
    3a06:	49 8d 7c fa 08       	lea    0x8(%r10,%rdi,8),%rdi
    3a0b:	eb 10                	jmp    3a1d <zim_Str_Replacer_replace+0x66d>
    3a0d:	0f 1f 00             	nopl   (%rax)
    3a10:	48 83 c0 08          	add    $0x8,%rax
    3a14:	48 39 f8             	cmp    %rdi,%rax
    3a17:	0f 84 29 fd ff ff    	je     3746 <zim_Str_Replacer_replace+0x396>
    3a1d:	66 3b 48 04          	cmp    0x4(%rax),%cx
    3a21:	75 ed                	jne    3a10 <zim_Str_Replacer_replace+0x660>
    3a23:	8b 18                	mov    (%rax),%ebx
    3a25:	e9 46 fd ff ff       	jmp    3770 <zim_Str_Replacer_replace+0x3c0>
    3a2a:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
    3a30:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
    3a35:	31 db                	xor    %ebx,%ebx
    3a37:	e9 48 fd ff ff       	jmp    3784 <zim_Str_Replacer_replace+0x3d4>
    3a3c:	49 63 84 24 e0 fd ff 	movslq -0x220(%r12),%rax
    3a43:	ff 
    3a44:	49 8b 94 24 a0 fd ff 	mov    -0x260(%r12),%rdx
    3a4b:	ff 
    3a4c:	48 0f af c3          	imul   %rbx,%rax
    3a50:	48 01 c8             	add    %rcx,%rax
    3a53:	8b 1c 82             	mov    (%rdx,%rax,4),%ebx
    3a56:	e9 15 fd ff ff       	jmp    3770 <zim_Str_Replacer_replace+0x3c0>
    3a5b:	48 83 c3 01          	add    $0x1,%rbx
    3a5f:	48 3b 1c 24          	cmp    (%rsp),%rbx
    3a63:	0f 82 17 fe ff ff    	jb     3880 <zim_Str_Replacer_replace+0x4d0>
    3a69:	4c 8b 74 24 20       	mov    0x20(%rsp),%r14
    3a6e:	4c 8b 5c 24 28       	mov    0x28(%rsp),%r11
    3a73:	49 8b 46 10          	mov    0x10(%r14),%rax
    3a77:	49 39 c0             	cmp    %rax,%r8
    3a7a:	73 53                	jae    3acf <zim_Str_Replacer_replace+0x71f>
    3a7c:	4c 29 c0             	sub    %r8,%rax
    3a7f:	48 89 c3             	mov    %rax,%rbx
    3a82:	48 8b 44 24 50       	mov    0x50(%rsp),%rax
    3a87:	48 85 c0             	test   %rax,%rax
    3a8a:	0f 84 6c 01 00 00    	je     3bfc <zim_Str_Replacer_replace+0x84c>
    3a90:	48 8b 50 10          	mov    0x10(%rax),%rdx
    3a94:	48 8d 2c 13          	lea    (%rbx,%rdx,1),%rbp
    3a98:	48 3b 6c 24 58       	cmp    0x58(%rsp),%rbp
    3a9d:	0f 83 5c 01 00 00    	jae    3bff <zim_Str_Replacer_replace+0x84f>
    3aa3:	48 8d 7c 10 18       	lea    0x18(%rax,%rdx,1),%rdi
    3aa8:	4b 8d 74 06 18       	lea    0x18(%r14,%r8,1),%rsi
    3aad:	48 89 da             	mov    %rbx,%rdx
    3ab0:	4c 89 1c 24          	mov    %r11,(%rsp)
    3ab4:	e8 e7 e8 ff ff       	call   23a0 <memcpy@plt>
    3ab9:	48 8b 44 24 50       	mov    0x50(%rsp),%rax
    3abe:	4d 85 ff             	test   %r15,%r15
    3ac1:	4c 8b 1c 24          	mov    (%rsp),%r11
    3ac5:	48 89 68 10          	mov    %rbp,0x10(%rax)
    3ac9:	0f 84 20 01 00 00    	je     3bef <zim_Str_Replacer_replace+0x83f>
    3acf:	4c 89 ff             	mov    %r15,%rdi
    3ad2:	e8 b9 e9 ff ff       	call   2490 <_efree@plt>
    3ad7:	48 8b 44 24 50       	mov    0x50(%rsp),%rax
    3adc:	48 85 c0             	test   %rax,%rax
    3adf:	0f 84 e4 00 00 00    	je     3bc9 <zim_Str_Replacer_replace+0x819>
    3ae5:	48 8b 50 10          	mov    0x10(%rax),%rdx
    3ae9:	c6 44 10 18 00       	movb   $0x0,0x18(%rax,%rdx,1)
    3aee:	48 8b 74 24 08       	mov    0x8(%rsp),%rsi
    3af3:	48 89 06             	mov    %rax,(%rsi)
    3af6:	f6 40 04 40          	testb  $0x40,0x4(%rax)
    3afa:	0f 85 ac 00 00 00    	jne    3bac <zim_Str_Replacer_replace+0x7fc>
    3b00:	c7 46 08 06 01 00 00 	movl   $0x106,0x8(%rsi)
    3b07:	48 83 7c 24 10 00    	cmpq   $0x0,0x10(%rsp)
    3b0d:	0f 84 62 fa ff ff    	je     3575 <zim_Str_Replacer_replace+0x1c5>
    3b13:	48 8b 44 24 10       	mov    0x10(%rsp),%rax
    3b18:	48 8b 18             	mov    (%rax),%rbx
    3b1b:	48 83 7b 18 00       	cmpq   $0x0,0x18(%rbx)
    3b20:	0f 85 08 01 00 00    	jne    3c2e <zim_Str_Replacer_replace+0x87e>
    3b26:	48 8d 7b 08          	lea    0x8(%rbx),%rdi
    3b2a:	e8 61 e8 ff ff       	call   2390 <zval_ptr_safe_dtor@plt>
    3b2f:	48 8b 44 24 18       	mov    0x18(%rsp),%rax
    3b34:	c7 43 10 04 00 00 00 	movl   $0x4,0x10(%rbx)
    3b3b:	48 89 43 08          	mov    %rax,0x8(%rbx)
    3b3f:	e9 31 fa ff ff       	jmp    3575 <zim_Str_Replacer_replace+0x1c5>
    3b44:	48 89 74 24 30       	mov    %rsi,0x30(%rsp)
    3b49:	48 8b 7c 24 48       	mov    0x48(%rsp),%rdi
    3b4e:	31 d2                	xor    %edx,%edx
    3b50:	4c 89 44 24 40       	mov    %r8,0x40(%rsp)
    3b55:	48 89 74 24 38       	mov    %rsi,0x38(%rsp)
    3b5a:	e8 71 e8 ff ff       	call   23d0 <smart_str_ferealloc@plt>
    3b5f:	4c 8b 64 24 38       	mov    0x38(%rsp),%r12
    3b64:	48 8b 74 24 30       	mov    0x30(%rsp),%rsi
    3b69:	48 8b 44 24 50       	mov    0x50(%rsp),%rax
    3b6e:	4c 8b 44 24 40       	mov    0x40(%rsp),%r8
    3b73:	e9 c3 fc ff ff       	jmp    383b <zim_Str_Replacer_replace+0x48b>
    3b78:	4d 89 d4             	mov    %r10,%r12
    3b7b:	31 d2                	xor    %edx,%edx
    3b7d:	48 8d 7c 24 50       	lea    0x50(%rsp),%rdi
    3b82:	4c 89 e6             	mov    %r12,%rsi
    3b85:	4c 89 44 24 38       	mov    %r8,0x38(%rsp)
    3b8a:	4c 89 54 24 30       	mov    %r10,0x30(%rsp)
    3b8f:	e8 3c e8 ff ff       	call   23d0 <smart_str_ferealloc@plt>
    3b94:	48 8b 54 24 50       	mov    0x50(%rsp),%rdx
    3b99:	4c 8b 44 24 38       	mov    0x38(%rsp),%r8
    3b9e:	4c 8b 54 24 30       	mov    0x30(%rsp),%r10
    3ba3:	48 8b 42 10          	mov    0x10(%rdx),%rax
    3ba7:	e9 46 fc ff ff       	jmp    37f2 <zim_Str_Replacer_replace+0x442>
    3bac:	48 8b 44 24 08       	mov    0x8(%rsp),%rax
    3bb1:	c7 40 08 06 00 00 00 	movl   $0x6,0x8(%rax)
    3bb8:	48 83 7c 24 10 00    	cmpq   $0x0,0x10(%rsp)
    3bbe:	0f 85 4f ff ff ff    	jne    3b13 <zim_Str_Replacer_replace+0x763>
    3bc4:	e9 ac f9 ff ff       	jmp    3575 <zim_Str_Replacer_replace+0x1c5>
    3bc9:	48 8b 05 f8 43 00 00 	mov    0x43f8(%rip),%rax        # 7fc8 <zend_empty_string>
    3bd0:	48 8b 00             	mov    (%rax),%rax
    3bd3:	e9 16 ff ff ff       	jmp    3aee <zim_Str_Replacer_replace+0x73e>
    3bd8:	4c 8b 74 24 20       	mov    0x20(%rsp),%r14
    3bdd:	4c 8b 5c 24 28       	mov    0x28(%rsp),%r11
    3be2:	49 8b 46 10          	mov    0x10(%r14),%rax
    3be6:	49 39 c0             	cmp    %rax,%r8
    3be9:	0f 82 8d fe ff ff    	jb     3a7c <zim_Str_Replacer_replace+0x6cc>
    3bef:	4c 89 df             	mov    %r11,%rdi
    3bf2:	e8 99 e8 ff ff       	call   2490 <_efree@plt>
    3bf7:	e9 db fe ff ff       	jmp    3ad7 <zim_Str_Replacer_replace+0x727>
    3bfc:	48 89 dd             	mov    %rbx,%rbp
    3bff:	31 d2                	xor    %edx,%edx
    3c01:	48 8d 7c 24 50       	lea    0x50(%rsp),%rdi
    3c06:	48 89 ee             	mov    %rbp,%rsi
    3c09:	4c 89 44 24 20       	mov    %r8,0x20(%rsp)
    3c0e:	4c 89 1c 24          	mov    %r11,(%rsp)
    3c12:	e8 b9 e7 ff ff       	call   23d0 <smart_str_ferealloc@plt>
    3c17:	48 8b 44 24 50       	mov    0x50(%rsp),%rax
    3c1c:	4c 8b 44 24 20       	mov    0x20(%rsp),%r8
    3c21:	4c 8b 1c 24          	mov    (%rsp),%r11
    3c25:	48 8b 50 10          	mov    0x10(%rax),%rdx
    3c29:	e9 75 fe ff ff       	jmp    3aa3 <zim_Str_Replacer_replace+0x6f3>
    3c2e:	48 8b 74 24 18       	mov    0x18(%rsp),%rsi
    3c33:	48 89 df             	mov    %rbx,%rdi
    3c36:	e8 f5 e7 ff ff       	call   2430 <zend_try_assign_typed_ref_long@plt>
    3c3b:	e9 35 f9 ff ff       	jmp    3575 <zim_Str_Replacer_replace+0x1c5>
    3c40:	45 31 ff             	xor    %r15d,%r15d
    3c43:	e9 4c fb ff ff       	jmp    3794 <zim_Str_Replacer_replace+0x3e4>
    3c48:	e8 d3 e6 ff ff       	call   2320 <__stack_chk_fail@plt>
    3c4d:	e8 ce e6 ff ff       	call   2320 <__stack_chk_fail@plt>
    3c52:	31 d2                	xor    %edx,%edx
    3c54:	be 04 00 00 00       	mov    $0x4,%esi
    3c59:	4c 89 d7             	mov    %r10,%rdi
    3c5c:	4c 89 5c 24 20       	mov    %r11,0x20(%rsp)
    3c61:	4c 89 44 24 18       	mov    %r8,0x18(%rsp)
    3c66:	4c 89 14 24          	mov    %r10,(%rsp)
    3c6a:	e8 91 e6 ff ff       	call   2300 <_safe_emalloc@plt>
    3c6f:	4c 8b 44 24 18       	mov    0x18(%rsp),%r8
    3c74:	4c 3b 04 24          	cmp    (%rsp),%r8
    3c78:	4c 8b 5c 24 20       	mov    0x20(%rsp),%r11
    3c7d:	49 89 c7             	mov    %rax,%r15
    3c80:	0f 82 00 fa ff ff    	jb     3686 <zim_Str_Replacer_replace+0x2d6>
    3c86:	e9 1e fa ff ff       	jmp    36a9 <zim_Str_Replacer_replace+0x2f9>

Disassembly of section .fini:
