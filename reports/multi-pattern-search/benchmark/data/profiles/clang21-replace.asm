
clang21-strmatch.so:     file format elf64-x86-64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .plt.got:

Disassembly of section .text:

0000000000004390 <zim_Str_Replacer_replace>:
    4390:	55                   	push   %rbp
    4391:	41 57                	push   %r15
    4393:	41 56                	push   %r14
    4395:	41 55                	push   %r13
    4397:	41 54                	push   %r12
    4399:	53                   	push   %rbx
    439a:	48 83 ec 78          	sub    $0x78,%rsp
    439e:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    43a5:	00 00 
    43a7:	48 89 44 24 70       	mov    %rax,0x70(%rsp)
    43ac:	8b 4f 2c             	mov    0x2c(%rdi),%ecx
    43af:	8d 41 fd             	lea    -0x3(%rcx),%eax
    43b2:	83 f8 fd             	cmp    $0xfffffffd,%eax
    43b5:	0f 86 14 08 00 00    	jbe    4bcf <zim_Str_Replacer_replace+0x83f>
    43bb:	49 89 fe             	mov    %rdi,%r14
    43be:	48 83 c7 50          	add    $0x50,%rdi
    43c2:	41 80 7e 58 06       	cmpb   $0x6,0x58(%r14)
    43c7:	48 89 74 24 58       	mov    %rsi,0x58(%rsp)
    43cc:	48 89 4c 24 50       	mov    %rcx,0x50(%rsp)
    43d1:	0f 85 12 08 00 00    	jne    4be9 <zim_Str_Replacer_replace+0x859>
    43d7:	4c 8b 17             	mov    (%rdi),%r10
    43da:	4c 89 74 24 38       	mov    %r14,0x38(%rsp)
    43df:	4d 8b 7e 20          	mov    0x20(%r14),%r15
    43e3:	41 83 7f f8 00       	cmpl   $0x0,-0x8(%r15)
    43e8:	0f 84 ca 02 00 00    	je     46b8 <zim_Str_Replacer_replace+0x328>
    43ee:	4d 8b 72 10          	mov    0x10(%r10),%r14
    43f2:	4c 89 54 24 30       	mov    %r10,0x30(%rsp)
    43f7:	4d 8d 62 18          	lea    0x18(%r10),%r12
    43fb:	48 c7 44 24 08 00 00 	movq   $0x0,0x8(%rsp)
    4402:	00 00 
    4404:	48 c7 44 24 20 00 00 	movq   $0x0,0x20(%rsp)
    440b:	00 00 
    440d:	48 c7 44 24 18 00 00 	movq   $0x0,0x18(%rsp)
    4414:	00 00 
    4416:	48 c7 44 24 10 00 00 	movq   $0x0,0x10(%rsp)
    441d:	00 00 
    441f:	45 31 ed             	xor    %r13d,%r13d
    4422:	48 c7 44 24 28 00 00 	movq   $0x0,0x28(%rsp)
    4429:	00 00 
    442b:	48 c7 04 24 00 00 00 	movq   $0x0,(%rsp)
    4432:	00 
    4433:	4c 89 74 24 48       	mov    %r14,0x48(%rsp)
    4438:	31 c0                	xor    %eax,%eax
    443a:	eb 14                	jmp    4450 <zim_Str_Replacer_replace+0xc0>
    443c:	0f 1f 40 00          	nopl   0x0(%rax)
    4440:	45 31 ed             	xor    %r13d,%r13d
    4443:	48 8d 45 01          	lea    0x1(%rbp),%rax
    4447:	45 85 ed             	test   %r13d,%r13d
    444a:	0f 88 f0 00 00 00    	js     4540 <zim_Str_Replacer_replace+0x1b0>
    4450:	4c 89 f3             	mov    %r14,%rbx
    4453:	49 83 ee 01          	sub    $0x1,%r14
    4457:	0f 82 f6 01 00 00    	jb     4653 <zim_Str_Replacer_replace+0x2c3>
    445d:	48 89 c5             	mov    %rax,%rbp
    4460:	43 0f b6 04 34       	movzbl (%r12,%r14,1),%eax
    4465:	41 0f b7 84 47 e4 fd 	movzwl -0x21c(%r15,%rax,2),%eax
    446c:	ff ff 
    446e:	48 85 c0             	test   %rax,%rax
    4471:	74 cd                	je     4440 <zim_Str_Replacer_replace+0xb0>
    4473:	41 8b 8f b0 fd ff ff 	mov    -0x250(%r15),%ecx
    447a:	41 39 cd             	cmp    %ecx,%r13d
    447d:	73 21                	jae    44a0 <zim_Str_Replacer_replace+0x110>
    447f:	44 89 e9             	mov    %r13d,%ecx
    4482:	49 63 97 e0 fd ff ff 	movslq -0x220(%r15),%rdx
    4489:	48 0f af d1          	imul   %rcx,%rdx
    448d:	48 c1 e2 02          	shl    $0x2,%rdx
    4491:	49 03 97 a0 fd ff ff 	add    -0x260(%r15),%rdx
    4498:	44 8b 2c 82          	mov    (%rdx,%rax,4),%r13d
    449c:	eb a5                	jmp    4443 <zim_Str_Replacer_replace+0xb3>
    449e:	66 90                	xchg   %ax,%ax
    44a0:	49 8b 97 c8 fd ff ff 	mov    -0x238(%r15),%rdx
    44a7:	eb 15                	jmp    44be <zim_Str_Replacer_replace+0x12e>
    44a9:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    44b0:	66 3b 46 0a          	cmp    0xa(%rsi),%ax
    44b4:	74 77                	je     452d <zim_Str_Replacer_replace+0x19d>
    44b6:	44 8b 2e             	mov    (%rsi),%r13d
    44b9:	41 39 cd             	cmp    %ecx,%r13d
    44bc:	72 c1                	jb     447f <zim_Str_Replacer_replace+0xef>
    44be:	41 29 cd             	sub    %ecx,%r13d
    44c1:	4a 8d 3c 6d 00 00 00 	lea    0x0(,%r13,2),%rdi
    44c8:	00 
    44c9:	4c 01 ef             	add    %r13,%rdi
    44cc:	48 8d 34 ba          	lea    (%rdx,%rdi,4),%rsi
    44d0:	0f b7 7c ba 08       	movzwl 0x8(%rdx,%rdi,4),%edi
    44d5:	85 ff                	test   %edi,%edi
    44d7:	74 dd                	je     44b6 <zim_Str_Replacer_replace+0x126>
    44d9:	83 ff 01             	cmp    $0x1,%edi
    44dc:	74 d2                	je     44b0 <zim_Str_Replacer_replace+0x120>
    44de:	4d 8b 87 a8 fd ff ff 	mov    -0x258(%r15),%r8
    44e5:	44 8b 4e 04          	mov    0x4(%rsi),%r9d
    44e9:	4f 8d 1c c8          	lea    (%r8,%r9,8),%r11
    44ed:	49 83 c3 04          	add    $0x4,%r11
    44f1:	45 31 d2             	xor    %r10d,%r10d
    44f4:	66 66 66 2e 0f 1f 84 	data16 data16 cs nopw 0x0(%rax,%rax,1)
    44fb:	00 00 00 00 00 
    4500:	66 43 39 04 d3       	cmp    %ax,(%r11,%r10,8)
    4505:	74 19                	je     4520 <zim_Str_Replacer_replace+0x190>
    4507:	49 ff c2             	inc    %r10
    450a:	4c 39 d7             	cmp    %r10,%rdi
    450d:	75 f1                	jne    4500 <zim_Str_Replacer_replace+0x170>
    450f:	eb a5                	jmp    44b6 <zim_Str_Replacer_replace+0x126>
    4511:	66 66 66 66 66 66 2e 	data16 data16 data16 data16 data16 cs nopw 0x0(%rax,%rax,1)
    4518:	0f 1f 84 00 00 00 00 
    451f:	00 
    4520:	4b 8d 04 c8          	lea    (%r8,%r9,8),%rax
    4524:	46 8b 2c d0          	mov    (%rax,%r10,8),%r13d
    4528:	e9 16 ff ff ff       	jmp    4443 <zim_Str_Replacer_replace+0xb3>
    452d:	44 8b 6e 04          	mov    0x4(%rsi),%r13d
    4531:	e9 0d ff ff ff       	jmp    4443 <zim_Str_Replacer_replace+0xb3>
    4536:	66 2e 0f 1f 84 00 00 	cs nopw 0x0(%rax,%rax,1)
    453d:	00 00 00 
    4540:	48 83 7c 24 10 00    	cmpq   $0x0,0x10(%rsp)
    4546:	75 25                	jne    456d <zim_Str_Replacer_replace+0x1dd>
    4548:	48 89 d9             	mov    %rbx,%rcx
    454b:	48 c1 e9 02          	shr    $0x2,%rcx
    454f:	48 83 e1 fc          	and    $0xfffffffffffffffc,%rcx
    4553:	48 81 f9 00 01 00 00 	cmp    $0x100,%rcx
    455a:	b8 00 01 00 00       	mov    $0x100,%eax
    455f:	48 0f 43 c8          	cmovae %rax,%rcx
    4563:	48 89 4c 24 18       	mov    %rcx,0x18(%rsp)
    4568:	48 89 5c 24 10       	mov    %rbx,0x10(%rsp)
    456d:	41 81 e5 ff ff ff 7f 	and    $0x7fffffff,%r13d
    4574:	44 89 ef             	mov    %r13d,%edi
    4577:	48 8b 54 24 20       	mov    0x20(%rsp),%rdx
    457c:	48 39 54 24 28       	cmp    %rdx,0x28(%rsp)
    4581:	0f 85 99 00 00 00    	jne    4620 <zim_Str_Replacer_replace+0x290>
    4587:	48 8b 74 24 18       	mov    0x18(%rsp),%rsi
    458c:	48 39 f2             	cmp    %rsi,%rdx
    458f:	0f 95 c0             	setne  %al
    4592:	48 81 fa 00 01 00 00 	cmp    $0x100,%rdx
    4599:	0f 92 c1             	setb   %cl
    459c:	08 c1                	or     %al,%cl
    459e:	75 30                	jne    45d0 <zim_Str_Replacer_replace+0x240>
    45a0:	48 8b 44 24 10       	mov    0x10(%rsp),%rax
    45a5:	48 c1 e8 06          	shr    $0x6,%rax
    45a9:	48 89 d6             	mov    %rdx,%rsi
    45ac:	48 39 c2             	cmp    %rax,%rdx
    45af:	73 1f                	jae    45d0 <zim_Str_Replacer_replace+0x240>
    45b1:	48 8b 4c 24 10       	mov    0x10(%rsp),%rcx
    45b6:	4c 29 f1             	sub    %r14,%rcx
    45b9:	48 c1 e9 06          	shr    $0x6,%rcx
    45bd:	48 89 d6             	mov    %rdx,%rsi
    45c0:	48 39 ca             	cmp    %rcx,%rdx
    45c3:	77 0b                	ja     45d0 <zim_Str_Replacer_replace+0x240>
    45c5:	48 8d 34 12          	lea    (%rdx,%rdx,1),%rsi
    45c9:	48 39 f0             	cmp    %rsi,%rax
    45cc:	48 0f 42 f0          	cmovb  %rax,%rsi
    45d0:	48 89 7c 24 40       	mov    %rdi,0x40(%rsp)
    45d5:	48 39 f2             	cmp    %rsi,%rdx
    45d8:	0f 84 c0 03 00 00    	je     499e <zim_Str_Replacer_replace+0x60e>
    45de:	48 8d 1c 12          	lea    (%rdx,%rdx,1),%rbx
    45e2:	48 85 d2             	test   %rdx,%rdx
    45e5:	b8 10 00 00 00       	mov    $0x10,%eax
    45ea:	48 0f 44 d8          	cmove  %rax,%rbx
    45ee:	48 39 de             	cmp    %rbx,%rsi
    45f1:	48 89 74 24 18       	mov    %rsi,0x18(%rsp)
    45f6:	48 0f 42 de          	cmovb  %rsi,%rbx
    45fa:	ba 10 00 00 00       	mov    $0x10,%edx
    45ff:	48 8b 3c 24          	mov    (%rsp),%rdi
    4603:	48 89 de             	mov    %rbx,%rsi
    4606:	31 c9                	xor    %ecx,%ecx
    4608:	e8 33 dc ff ff       	call   2240 <_safe_erealloc@plt>
    460d:	48 89 5c 24 20       	mov    %rbx,0x20(%rsp)
    4612:	48 8b 7c 24 40       	mov    0x40(%rsp),%rdi
    4617:	eb 0b                	jmp    4624 <zim_Str_Replacer_replace+0x294>
    4619:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    4620:	48 8b 04 24          	mov    (%rsp),%rax
    4624:	48 8b 54 24 28       	mov    0x28(%rsp),%rdx
    4629:	48 89 d6             	mov    %rdx,%rsi
    462c:	48 c1 e6 04          	shl    $0x4,%rsi
    4630:	4c 89 34 30          	mov    %r14,(%rax,%rsi,1)
    4634:	49 8b 8f d0 fd ff ff 	mov    -0x230(%r15),%rcx
    463b:	8b 0c b9             	mov    (%rcx,%rdi,4),%ecx
    463e:	48 ff c2             	inc    %rdx
    4641:	48 89 54 24 28       	mov    %rdx,0x28(%rsp)
    4646:	48 89 04 24          	mov    %rax,(%rsp)
    464a:	89 4c 30 08          	mov    %ecx,0x8(%rax,%rsi,1)
    464e:	e9 e0 fd ff ff       	jmp    4433 <zim_Str_Replacer_replace+0xa3>
    4653:	4c 8b 54 24 30       	mov    0x30(%rsp),%r10
    4658:	48 8b 7c 24 28       	mov    0x28(%rsp),%rdi
    465d:	48 83 7c 24 10 00    	cmpq   $0x0,0x10(%rsp)
    4663:	4c 8b 6c 24 08       	mov    0x8(%rsp),%r13
    4668:	74 4e                	je     46b8 <zim_Str_Replacer_replace+0x328>
    466a:	0f 57 c0             	xorps  %xmm0,%xmm0
    466d:	0f 29 44 24 60       	movaps %xmm0,0x60(%rsp)
    4672:	4d 85 ed             	test   %r13,%r13
    4675:	0f 85 91 00 00 00    	jne    470c <zim_Str_Replacer_replace+0x37c>
    467b:	48 85 ff             	test   %rdi,%rdi
    467e:	0f 85 88 00 00 00    	jne    470c <zim_Str_Replacer_replace+0x37c>
    4684:	4d 8b 72 10          	mov    0x10(%r10),%r14
    4688:	31 ed                	xor    %ebp,%ebp
    468a:	4c 89 f3             	mov    %r14,%rbx
    468d:	4d 85 f6             	test   %r14,%r14
    4690:	4c 8b 7c 24 38       	mov    0x38(%rsp),%r15
    4695:	0f 84 fa 02 00 00    	je     4995 <zim_Str_Replacer_replace+0x605>
    469b:	48 8d 7c 24 60       	lea    0x60(%rsp),%rdi
    46a0:	48 89 de             	mov    %rbx,%rsi
    46a3:	31 d2                	xor    %edx,%edx
    46a5:	e8 96 da ff ff       	call   2140 <smart_str_ferealloc@plt>
    46aa:	48 8b 44 24 60       	mov    0x60(%rsp),%rax
    46af:	48 8b 48 10          	mov    0x10(%rax),%rcx
    46b3:	e9 23 02 00 00       	jmp    48db <zim_Str_Replacer_replace+0x54b>
    46b8:	48 8b 4c 24 58       	mov    0x58(%rsp),%rcx
    46bd:	4c 89 11             	mov    %r10,(%rcx)
    46c0:	b8 06 00 00 00       	mov    $0x6,%eax
    46c5:	41 f6 42 04 40       	testb  $0x40,0x4(%r10)
    46ca:	75 08                	jne    46d4 <zim_Str_Replacer_replace+0x344>
    46cc:	41 ff 02             	incl   (%r10)
    46cf:	b8 06 01 00 00       	mov    $0x106,%eax
    46d4:	89 41 08             	mov    %eax,0x8(%rcx)
    46d7:	83 7c 24 50 01       	cmpl   $0x1,0x50(%rsp)
    46dc:	48 8b 44 24 38       	mov    0x38(%rsp),%rax
    46e1:	0f 84 8b 02 00 00    	je     4972 <zim_Str_Replacer_replace+0x5e2>
    46e7:	48 8b 58 60          	mov    0x60(%rax),%rbx
    46eb:	48 83 7b 18 00       	cmpq   $0x0,0x18(%rbx)
    46f0:	0f 85 3c 05 00 00    	jne    4c32 <zim_Str_Replacer_replace+0x8a2>
    46f6:	48 8d 7b 08          	lea    0x8(%rbx),%rdi
    46fa:	e8 01 da ff ff       	call   2100 <zval_ptr_safe_dtor@plt>
    46ff:	48 c7 43 08 00 00 00 	movq   $0x0,0x8(%rbx)
    4706:	00 
    4707:	e9 5f 02 00 00       	jmp    496b <zim_Str_Replacer_replace+0x5db>
    470c:	31 c0                	xor    %eax,%eax
    470e:	31 db                	xor    %ebx,%ebx
    4710:	31 c9                	xor    %ecx,%ecx
    4712:	45 31 c0             	xor    %r8d,%r8d
    4715:	4c 89 64 24 18       	mov    %r12,0x18(%rsp)
    471a:	eb 2e                	jmp    474a <zim_Str_Replacer_replace+0x3ba>
    471c:	0f 1f 40 00          	nopl   0x0(%rax)
    4720:	48 ff c1             	inc    %rcx
    4723:	4c 8b 64 24 18       	mov    0x18(%rsp),%r12
    4728:	31 d2                	xor    %edx,%edx
    472a:	48 3b 4c 24 10       	cmp    0x10(%rsp),%rcx
    472f:	0f 92 c2             	setb   %dl
    4732:	31 f6                	xor    %esi,%esi
    4734:	48 85 ff             	test   %rdi,%rdi
    4737:	40 0f 95 c6          	setne  %sil
    473b:	4d 85 ed             	test   %r13,%r13
    473e:	0f 45 f2             	cmovne %edx,%esi
    4741:	40 84 f6             	test   %sil,%sil
    4744:	0f 84 5c 01 00 00    	je     48a6 <zim_Str_Replacer_replace+0x516>
    474a:	4d 85 ed             	test   %r13,%r13
    474d:	74 11                	je     4760 <zim_Str_Replacer_replace+0x3d0>
    474f:	45 8b 64 8d 00       	mov    0x0(%r13,%rcx,4),%r12d
    4754:	45 85 e4             	test   %r12d,%r12d
    4757:	78 c7                	js     4720 <zim_Str_Replacer_replace+0x390>
    4759:	48 89 cd             	mov    %rcx,%rbp
    475c:	eb 20                	jmp    477e <zim_Str_Replacer_replace+0x3ee>
    475e:	66 90                	xchg   %ax,%ax
    4760:	48 ff cf             	dec    %rdi
    4763:	48 89 fa             	mov    %rdi,%rdx
    4766:	48 c1 e2 04          	shl    $0x4,%rdx
    476a:	48 8b 34 24          	mov    (%rsp),%rsi
    476e:	48 8b 2c 16          	mov    (%rsi,%rdx,1),%rbp
    4772:	48 39 cd             	cmp    %rcx,%rbp
    4775:	72 b1                	jb     4728 <zim_Str_Replacer_replace+0x398>
    4777:	48 01 f2             	add    %rsi,%rdx
    477a:	44 8b 62 08          	mov    0x8(%rdx),%r12d
    477e:	4c 89 44 24 20       	mov    %r8,0x20(%rsp)
    4783:	48 89 7c 24 28       	mov    %rdi,0x28(%rsp)
    4788:	49 89 ed             	mov    %rbp,%r13
    478b:	49 29 dd             	sub    %rbx,%r13
    478e:	76 60                	jbe    47f0 <zim_Str_Replacer_replace+0x460>
    4790:	4d 89 ee             	mov    %r13,%r14
    4793:	48 85 c0             	test   %rax,%rax
    4796:	0f 84 ed 00 00 00    	je     4889 <zim_Str_Replacer_replace+0x4f9>
    479c:	48 8b 48 10          	mov    0x10(%rax),%rcx
    47a0:	4e 8d 34 29          	lea    (%rcx,%r13,1),%r14
    47a4:	4c 3b 74 24 68       	cmp    0x68(%rsp),%r14
    47a9:	0f 83 da 00 00 00    	jae    4889 <zim_Str_Replacer_replace+0x4f9>
    47af:	48 03 5c 24 18       	add    0x18(%rsp),%rbx
    47b4:	48 8d 3c 08          	lea    (%rax,%rcx,1),%rdi
    47b8:	48 83 c7 18          	add    $0x18,%rdi
    47bc:	48 89 de             	mov    %rbx,%rsi
    47bf:	4c 89 ea             	mov    %r13,%rdx
    47c2:	e8 49 d9 ff ff       	call   2110 <memcpy@plt>
    47c7:	48 8b 44 24 60       	mov    0x60(%rsp),%rax
    47cc:	4c 89 70 10          	mov    %r14,0x10(%rax)
    47d0:	49 8b 4f f0          	mov    -0x10(%r15),%rcx
    47d4:	4d 63 f4             	movslq %r12d,%r14
    47d7:	4a 8b 34 f1          	mov    (%rcx,%r14,8),%rsi
    47db:	48 8b 56 10          	mov    0x10(%rsi),%rdx
    47df:	48 83 c6 18          	add    $0x18,%rsi
    47e3:	4c 8b 6c 24 08       	mov    0x8(%rsp),%r13
    47e8:	eb 26                	jmp    4810 <zim_Str_Replacer_replace+0x480>
    47ea:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
    47f0:	4d 63 f4             	movslq %r12d,%r14
    47f3:	49 8b 4f f0          	mov    -0x10(%r15),%rcx
    47f7:	4a 8b 34 f1          	mov    (%rcx,%r14,8),%rsi
    47fb:	48 8b 56 10          	mov    0x10(%rsi),%rdx
    47ff:	48 83 c6 18          	add    $0x18,%rsi
    4803:	48 89 d3             	mov    %rdx,%rbx
    4806:	48 85 c0             	test   %rax,%rax
    4809:	4c 8b 6c 24 08       	mov    0x8(%rsp),%r13
    480e:	74 4e                	je     485e <zim_Str_Replacer_replace+0x4ce>
    4810:	48 8b 48 10          	mov    0x10(%rax),%rcx
    4814:	48 8d 1c 11          	lea    (%rcx,%rdx,1),%rbx
    4818:	48 3b 5c 24 68       	cmp    0x68(%rsp),%rbx
    481d:	73 3f                	jae    485e <zim_Str_Replacer_replace+0x4ce>
    481f:	48 8d 3c 08          	lea    (%rax,%rcx,1),%rdi
    4823:	48 83 c7 18          	add    $0x18,%rdi
    4827:	e8 e4 d8 ff ff       	call   2110 <memcpy@plt>
    482c:	48 8b 44 24 60       	mov    0x60(%rsp),%rax
    4831:	48 89 58 10          	mov    %rbx,0x10(%rax)
    4835:	49 8b 4f e8          	mov    -0x18(%r15),%rcx
    4839:	4a 8b 0c f1          	mov    (%rcx,%r14,8),%rcx
    483d:	48 03 69 10          	add    0x10(%rcx),%rbp
    4841:	4c 8b 44 24 20       	mov    0x20(%rsp),%r8
    4846:	49 ff c0             	inc    %r8
    4849:	48 89 e9             	mov    %rbp,%rcx
    484c:	48 89 eb             	mov    %rbp,%rbx
    484f:	4c 8b 64 24 18       	mov    0x18(%rsp),%r12
    4854:	48 8b 7c 24 28       	mov    0x28(%rsp),%rdi
    4859:	e9 ca fe ff ff       	jmp    4728 <zim_Str_Replacer_replace+0x398>
    485e:	48 8d 7c 24 60       	lea    0x60(%rsp),%rdi
    4863:	49 89 f4             	mov    %rsi,%r12
    4866:	48 89 de             	mov    %rbx,%rsi
    4869:	49 89 d5             	mov    %rdx,%r13
    486c:	31 d2                	xor    %edx,%edx
    486e:	e8 cd d8 ff ff       	call   2140 <smart_str_ferealloc@plt>
    4873:	4c 89 ea             	mov    %r13,%rdx
    4876:	4c 8b 6c 24 08       	mov    0x8(%rsp),%r13
    487b:	4c 89 e6             	mov    %r12,%rsi
    487e:	48 8b 44 24 60       	mov    0x60(%rsp),%rax
    4883:	48 8b 48 10          	mov    0x10(%rax),%rcx
    4887:	eb 96                	jmp    481f <zim_Str_Replacer_replace+0x48f>
    4889:	48 8d 7c 24 60       	lea    0x60(%rsp),%rdi
    488e:	4c 89 f6             	mov    %r14,%rsi
    4891:	31 d2                	xor    %edx,%edx
    4893:	e8 a8 d8 ff ff       	call   2140 <smart_str_ferealloc@plt>
    4898:	48 8b 44 24 60       	mov    0x60(%rsp),%rax
    489d:	48 8b 48 10          	mov    0x10(%rax),%rcx
    48a1:	e9 09 ff ff ff       	jmp    47af <zim_Str_Replacer_replace+0x41f>
    48a6:	48 8b 4c 24 30       	mov    0x30(%rsp),%rcx
    48ab:	4c 8b 71 10          	mov    0x10(%rcx),%r14
    48af:	49 29 de             	sub    %rbx,%r14
    48b2:	4c 8b 7c 24 38       	mov    0x38(%rsp),%r15
    48b7:	4c 89 c5             	mov    %r8,%rbp
    48ba:	76 3b                	jbe    48f7 <zim_Str_Replacer_replace+0x567>
    48bc:	49 01 dc             	add    %rbx,%r12
    48bf:	48 85 c0             	test   %rax,%rax
    48c2:	0f 84 a7 03 00 00    	je     4c6f <zim_Str_Replacer_replace+0x8df>
    48c8:	48 8b 48 10          	mov    0x10(%rax),%rcx
    48cc:	4a 8d 1c 31          	lea    (%rcx,%r14,1),%rbx
    48d0:	48 3b 5c 24 68       	cmp    0x68(%rsp),%rbx
    48d5:	0f 83 c0 fd ff ff    	jae    469b <zim_Str_Replacer_replace+0x30b>
    48db:	48 8d 3c 08          	lea    (%rax,%rcx,1),%rdi
    48df:	48 83 c7 18          	add    $0x18,%rdi
    48e3:	4c 89 e6             	mov    %r12,%rsi
    48e6:	4c 89 f2             	mov    %r14,%rdx
    48e9:	e8 22 d8 ff ff       	call   2110 <memcpy@plt>
    48ee:	48 8b 44 24 60       	mov    0x60(%rsp),%rax
    48f3:	48 89 58 10          	mov    %rbx,0x10(%rax)
    48f7:	4d 85 ed             	test   %r13,%r13
    48fa:	48 8b 3c 24          	mov    (%rsp),%rdi
    48fe:	49 0f 45 fd          	cmovne %r13,%rdi
    4902:	e8 f9 d8 ff ff       	call   2200 <_efree@plt>
    4907:	48 8b 44 24 60       	mov    0x60(%rsp),%rax
    490c:	48 85 c0             	test   %rax,%rax
    490f:	74 13                	je     4924 <zim_Str_Replacer_replace+0x594>
    4911:	48 8b 48 10          	mov    0x10(%rax),%rcx
    4915:	c6 44 08 18 00       	movb   $0x0,0x18(%rax,%rcx,1)
    491a:	48 8b 44 24 60       	mov    0x60(%rsp),%rax
    491f:	48 85 c0             	test   %rax,%rax
    4922:	75 0a                	jne    492e <zim_Str_Replacer_replace+0x59e>
    4924:	48 8b 05 9d 36 00 00 	mov    0x369d(%rip),%rax        # 7fc8 <zend_empty_string>
    492b:	48 8b 00             	mov    (%rax),%rax
    492e:	48 8b 54 24 58       	mov    0x58(%rsp),%rdx
    4933:	48 89 02             	mov    %rax,(%rdx)
    4936:	31 c9                	xor    %ecx,%ecx
    4938:	f6 40 04 40          	testb  $0x40,0x4(%rax)
    493c:	0f 94 c1             	sete   %cl
    493f:	c1 e1 08             	shl    $0x8,%ecx
    4942:	83 c9 06             	or     $0x6,%ecx
    4945:	89 4a 08             	mov    %ecx,0x8(%rdx)
    4948:	83 7c 24 50 01       	cmpl   $0x1,0x50(%rsp)
    494d:	74 23                	je     4972 <zim_Str_Replacer_replace+0x5e2>
    494f:	49 8b 5f 60          	mov    0x60(%r15),%rbx
    4953:	48 83 7b 18 00       	cmpq   $0x0,0x18(%rbx)
    4958:	0f 85 fc 02 00 00    	jne    4c5a <zim_Str_Replacer_replace+0x8ca>
    495e:	48 8d 7b 08          	lea    0x8(%rbx),%rdi
    4962:	e8 99 d7 ff ff       	call   2100 <zval_ptr_safe_dtor@plt>
    4967:	48 89 6b 08          	mov    %rbp,0x8(%rbx)
    496b:	c7 43 10 04 00 00 00 	movl   $0x4,0x10(%rbx)
    4972:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    4979:	00 00 
    497b:	48 3b 44 24 70       	cmp    0x70(%rsp),%rax
    4980:	0f 85 e4 02 00 00    	jne    4c6a <zim_Str_Replacer_replace+0x8da>
    4986:	48 83 c4 78          	add    $0x78,%rsp
    498a:	5b                   	pop    %rbx
    498b:	41 5c                	pop    %r12
    498d:	41 5d                	pop    %r13
    498f:	41 5e                	pop    %r14
    4991:	41 5f                	pop    %r15
    4993:	5d                   	pop    %rbp
    4994:	c3                   	ret
    4995:	48 8b 3c 24          	mov    (%rsp),%rdi
    4999:	e9 64 ff ff ff       	jmp    4902 <zim_Str_Replacer_replace+0x572>
    499e:	be 04 00 00 00       	mov    $0x4,%esi
    49a3:	48 8b 7c 24 10       	mov    0x10(%rsp),%rdi
    49a8:	48 89 7c 24 10       	mov    %rdi,0x10(%rsp)
    49ad:	31 d2                	xor    %edx,%edx
    49af:	e8 bc d6 ff ff       	call   2070 <_safe_emalloc@plt>
    49b4:	48 89 44 24 08       	mov    %rax,0x8(%rsp)
    49b9:	48 3b 5c 24 10       	cmp    0x10(%rsp),%rbx
    49be:	73 2d                	jae    49ed <zim_Str_Replacer_replace+0x65d>
    49c0:	48 8b 54 24 48       	mov    0x48(%rsp),%rdx
    49c5:	48 89 d0             	mov    %rdx,%rax
    49c8:	48 29 e8             	sub    %rbp,%rax
    49cb:	48 8b 4c 24 08       	mov    0x8(%rsp),%rcx
    49d0:	48 8d 3c 81          	lea    (%rcx,%rax,4),%rdi
    49d4:	48 29 d5             	sub    %rdx,%rbp
    49d7:	48 03 6c 24 10       	add    0x10(%rsp),%rbp
    49dc:	48 c1 e5 02          	shl    $0x2,%rbp
    49e0:	be ff 00 00 00       	mov    $0xff,%esi
    49e5:	48 89 ea             	mov    %rbp,%rdx
    49e8:	e8 f3 d6 ff ff       	call   20e0 <memset@plt>
    49ed:	48 8b 54 24 20       	mov    0x20(%rsp),%rdx
    49f2:	48 85 d2             	test   %rdx,%rdx
    49f5:	74 14                	je     4a0b <zim_Str_Replacer_replace+0x67b>
    49f7:	89 d0                	mov    %edx,%eax
    49f9:	83 e0 03             	and    $0x3,%eax
    49fc:	48 83 fa 04          	cmp    $0x4,%rdx
    4a00:	73 1a                	jae    4a1c <zim_Str_Replacer_replace+0x68c>
    4a02:	31 c9                	xor    %ecx,%ecx
    4a04:	48 8b 5c 24 08       	mov    0x8(%rsp),%rbx
    4a09:	eb 5c                	jmp    4a67 <zim_Str_Replacer_replace+0x6d7>
    4a0b:	48 83 3c 24 00       	cmpq   $0x0,(%rsp)
    4a10:	48 8b 5c 24 08       	mov    0x8(%rsp),%rbx
    4a15:	75 7d                	jne    4a94 <zim_Str_Replacer_replace+0x704>
    4a17:	e9 81 00 00 00       	jmp    4a9d <zim_Str_Replacer_replace+0x70d>
    4a1c:	48 83 e2 fc          	and    $0xfffffffffffffffc,%rdx
    4a20:	48 8b 0c 24          	mov    (%rsp),%rcx
    4a24:	48 8d 71 38          	lea    0x38(%rcx),%rsi
    4a28:	31 c9                	xor    %ecx,%ecx
    4a2a:	48 8b 5c 24 08       	mov    0x8(%rsp),%rbx
    4a2f:	8b 7e d0             	mov    -0x30(%rsi),%edi
    4a32:	4c 8b 46 c8          	mov    -0x38(%rsi),%r8
    4a36:	42 89 3c 83          	mov    %edi,(%rbx,%r8,4)
    4a3a:	8b 7e e0             	mov    -0x20(%rsi),%edi
    4a3d:	4c 8b 46 d8          	mov    -0x28(%rsi),%r8
    4a41:	42 89 3c 83          	mov    %edi,(%rbx,%r8,4)
    4a45:	8b 7e f0             	mov    -0x10(%rsi),%edi
    4a48:	4c 8b 46 e8          	mov    -0x18(%rsi),%r8
    4a4c:	42 89 3c 83          	mov    %edi,(%rbx,%r8,4)
    4a50:	8b 3e                	mov    (%rsi),%edi
    4a52:	4c 8b 46 f8          	mov    -0x8(%rsi),%r8
    4a56:	42 89 3c 83          	mov    %edi,(%rbx,%r8,4)
    4a5a:	48 83 c1 04          	add    $0x4,%rcx
    4a5e:	48 83 c6 40          	add    $0x40,%rsi
    4a62:	48 39 ca             	cmp    %rcx,%rdx
    4a65:	75 c8                	jne    4a2f <zim_Str_Replacer_replace+0x69f>
    4a67:	48 85 c0             	test   %rax,%rax
    4a6a:	74 28                	je     4a94 <zim_Str_Replacer_replace+0x704>
    4a6c:	48 c1 e1 04          	shl    $0x4,%rcx
    4a70:	48 8b 14 24          	mov    (%rsp),%rdx
    4a74:	48 01 d1             	add    %rdx,%rcx
    4a77:	48 83 c1 08          	add    $0x8,%rcx
    4a7b:	c1 e0 04             	shl    $0x4,%eax
    4a7e:	31 d2                	xor    %edx,%edx
    4a80:	8b 34 11             	mov    (%rcx,%rdx,1),%esi
    4a83:	48 8b 7c 11 f8       	mov    -0x8(%rcx,%rdx,1),%rdi
    4a88:	89 34 bb             	mov    %esi,(%rbx,%rdi,4)
    4a8b:	48 83 c2 10          	add    $0x10,%rdx
    4a8f:	48 39 d0             	cmp    %rdx,%rax
    4a92:	75 ec                	jne    4a80 <zim_Str_Replacer_replace+0x6f0>
    4a94:	48 8b 3c 24          	mov    (%rsp),%rdi
    4a98:	e8 63 d7 ff ff       	call   2200 <_efree@plt>
    4a9d:	49 8b 87 d0 fd ff ff 	mov    -0x230(%r15),%rax
    4aa4:	48 8b 4c 24 40       	mov    0x40(%rsp),%rcx
    4aa9:	8b 04 88             	mov    (%rax,%rcx,4),%eax
    4aac:	42 89 04 b3          	mov    %eax,(%rbx,%r14,4)
    4ab0:	4d 85 f6             	test   %r14,%r14
    4ab3:	0f 84 ff 00 00 00    	je     4bb8 <zim_Str_Replacer_replace+0x828>
    4ab9:	48 c7 04 24 00 00 00 	movq   $0x0,(%rsp)
    4ac0:	00 
    4ac1:	4c 8b 54 24 30       	mov    0x30(%rsp),%r10
    4ac6:	eb 15                	jmp    4add <zim_Str_Replacer_replace+0x74d>
    4ac8:	45 31 ed             	xor    %r13d,%r13d
    4acb:	49 ff ce             	dec    %r14
    4ace:	48 8b 4c 24 08       	mov    0x8(%rsp),%rcx
    4ad3:	42 89 04 b1          	mov    %eax,(%rcx,%r14,4)
    4ad7:	0f 84 d1 00 00 00    	je     4bae <zim_Str_Replacer_replace+0x81e>
    4add:	43 0f b6 44 34 ff    	movzbl -0x1(%r12,%r14,1),%eax
    4ae3:	41 0f b7 8c 47 e4 fd 	movzwl -0x21c(%r15,%rax,2),%ecx
    4aea:	ff ff 
    4aec:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
    4af1:	48 85 c9             	test   %rcx,%rcx
    4af4:	74 d2                	je     4ac8 <zim_Str_Replacer_replace+0x738>
    4af6:	41 8b 97 b0 fd ff ff 	mov    -0x250(%r15),%edx
    4afd:	41 39 d5             	cmp    %edx,%r13d
    4b00:	73 39                	jae    4b3b <zim_Str_Replacer_replace+0x7ab>
    4b02:	44 89 ea             	mov    %r13d,%edx
    4b05:	49 63 b7 e0 fd ff ff 	movslq -0x220(%r15),%rsi
    4b0c:	48 0f af f2          	imul   %rdx,%rsi
    4b10:	48 c1 e6 02          	shl    $0x2,%rsi
    4b14:	49 03 b7 a0 fd ff ff 	add    -0x260(%r15),%rsi
    4b1b:	4c 8d 0c 8e          	lea    (%rsi,%rcx,4),%r9
    4b1f:	45 8b 29             	mov    (%r9),%r13d
    4b22:	45 85 ed             	test   %r13d,%r13d
    4b25:	79 a4                	jns    4acb <zim_Str_Replacer_replace+0x73b>
    4b27:	41 81 e5 ff ff ff 7f 	and    $0x7fffffff,%r13d
    4b2e:	49 8b 87 d0 fd ff ff 	mov    -0x230(%r15),%rax
    4b35:	42 8b 04 a8          	mov    (%rax,%r13,4),%eax
    4b39:	eb 90                	jmp    4acb <zim_Str_Replacer_replace+0x73b>
    4b3b:	49 8b b7 c8 fd ff ff 	mov    -0x238(%r15),%rsi
    4b42:	eb 0e                	jmp    4b52 <zim_Str_Replacer_replace+0x7c2>
    4b44:	66 3b 4f 0a          	cmp    0xa(%rdi),%cx
    4b48:	74 58                	je     4ba2 <zim_Str_Replacer_replace+0x812>
    4b4a:	44 8b 2f             	mov    (%rdi),%r13d
    4b4d:	41 39 d5             	cmp    %edx,%r13d
    4b50:	72 b0                	jb     4b02 <zim_Str_Replacer_replace+0x772>
    4b52:	41 29 d5             	sub    %edx,%r13d
    4b55:	4e 8d 04 6d 00 00 00 	lea    0x0(,%r13,2),%r8
    4b5c:	00 
    4b5d:	4d 01 e8             	add    %r13,%r8
    4b60:	4a 8d 3c 86          	lea    (%rsi,%r8,4),%rdi
    4b64:	46 0f b7 44 86 08    	movzwl 0x8(%rsi,%r8,4),%r8d
    4b6a:	45 85 c0             	test   %r8d,%r8d
    4b6d:	74 db                	je     4b4a <zim_Str_Replacer_replace+0x7ba>
    4b6f:	41 83 f8 01          	cmp    $0x1,%r8d
    4b73:	74 cf                	je     4b44 <zim_Str_Replacer_replace+0x7b4>
    4b75:	44 8b 4f 04          	mov    0x4(%rdi),%r9d
    4b79:	49 c1 e1 03          	shl    $0x3,%r9
    4b7d:	4d 03 8f a8 fd ff ff 	add    -0x258(%r15),%r9
    4b84:	66 66 66 2e 0f 1f 84 	data16 data16 cs nopw 0x0(%rax,%rax,1)
    4b8b:	00 00 00 00 00 
    4b90:	66 41 39 49 04       	cmp    %cx,0x4(%r9)
    4b95:	74 88                	je     4b1f <zim_Str_Replacer_replace+0x78f>
    4b97:	49 83 c1 08          	add    $0x8,%r9
    4b9b:	49 ff c8             	dec    %r8
    4b9e:	75 f0                	jne    4b90 <zim_Str_Replacer_replace+0x800>
    4ba0:	eb a8                	jmp    4b4a <zim_Str_Replacer_replace+0x7ba>
    4ba2:	48 83 c7 04          	add    $0x4,%rdi
    4ba6:	49 89 f9             	mov    %rdi,%r9
    4ba9:	e9 71 ff ff ff       	jmp    4b1f <zim_Str_Replacer_replace+0x78f>
    4bae:	48 8b 7c 24 20       	mov    0x20(%rsp),%rdi
    4bb3:	e9 a5 fa ff ff       	jmp    465d <zim_Str_Replacer_replace+0x2cd>
    4bb8:	48 c7 04 24 00 00 00 	movq   $0x0,(%rsp)
    4bbf:	00 
    4bc0:	48 8b 7c 24 20       	mov    0x20(%rsp),%rdi
    4bc5:	4c 8b 54 24 30       	mov    0x30(%rsp),%r10
    4bca:	e9 8e fa ff ff       	jmp    465d <zim_Str_Replacer_replace+0x2cd>
    4bcf:	bf 01 00 00 00       	mov    $0x1,%edi
    4bd4:	be 02 00 00 00       	mov    $0x2,%esi
    4bd9:	e8 e2 d4 ff ff       	call   20c0 <zend_wrong_parameters_count_error@plt>
    4bde:	31 c9                	xor    %ecx,%ecx
    4be0:	b0 01                	mov    $0x1,%al
    4be2:	45 31 c0             	xor    %r8d,%r8d
    4be5:	31 f6                	xor    %esi,%esi
    4be7:	eb 21                	jmp    4c0a <zim_Str_Replacer_replace+0x87a>
    4be9:	48 89 fb             	mov    %rdi,%rbx
    4bec:	be 01 00 00 00       	mov    $0x1,%esi
    4bf1:	e8 ba d4 ff ff       	call   20b0 <zend_parse_arg_str_slow@plt>
    4bf6:	48 85 c0             	test   %rax,%rax
    4bf9:	75 7c                	jne    4c77 <zim_Str_Replacer_replace+0x8e7>
    4bfb:	b9 04 00 00 00       	mov    $0x4,%ecx
    4c00:	b0 0c                	mov    $0xc,%al
    4c02:	49 89 d8             	mov    %rbx,%r8
    4c05:	be 01 00 00 00       	mov    $0x1,%esi
    4c0a:	64 48 8b 14 25 28 00 	mov    %fs:0x28,%rdx
    4c11:	00 00 
    4c13:	48 3b 54 24 70       	cmp    0x70(%rsp),%rdx
    4c18:	75 50                	jne    4c6a <zim_Str_Replacer_replace+0x8da>
    4c1a:	0f b6 f8             	movzbl %al,%edi
    4c1d:	31 d2                	xor    %edx,%edx
    4c1f:	48 83 c4 78          	add    $0x78,%rsp
    4c23:	5b                   	pop    %rbx
    4c24:	41 5c                	pop    %r12
    4c26:	41 5d                	pop    %r13
    4c28:	41 5e                	pop    %r14
    4c2a:	41 5f                	pop    %r15
    4c2c:	5d                   	pop    %rbp
    4c2d:	e9 be d5 ff ff       	jmp    21f0 <zend_wrong_parameter_error@plt>
    4c32:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    4c39:	00 00 
    4c3b:	48 3b 44 24 70       	cmp    0x70(%rsp),%rax
    4c40:	75 28                	jne    4c6a <zim_Str_Replacer_replace+0x8da>
    4c42:	48 89 df             	mov    %rbx,%rdi
    4c45:	31 f6                	xor    %esi,%esi
    4c47:	48 83 c4 78          	add    $0x78,%rsp
    4c4b:	5b                   	pop    %rbx
    4c4c:	41 5c                	pop    %r12
    4c4e:	41 5d                	pop    %r13
    4c50:	41 5e                	pop    %r14
    4c52:	41 5f                	pop    %r15
    4c54:	5d                   	pop    %rbp
    4c55:	e9 46 d5 ff ff       	jmp    21a0 <zend_try_assign_typed_ref_long@plt>
    4c5a:	48 89 df             	mov    %rbx,%rdi
    4c5d:	48 89 ee             	mov    %rbp,%rsi
    4c60:	e8 3b d5 ff ff       	call   21a0 <zend_try_assign_typed_ref_long@plt>
    4c65:	e9 08 fd ff ff       	jmp    4972 <zim_Str_Replacer_replace+0x5e2>
    4c6a:	e8 21 d4 ff ff       	call   2090 <__stack_chk_fail@plt>
    4c6f:	4c 89 f3             	mov    %r14,%rbx
    4c72:	e9 24 fa ff ff       	jmp    469b <zim_Str_Replacer_replace+0x30b>
    4c77:	49 89 c2             	mov    %rax,%r10
    4c7a:	e9 5b f7 ff ff       	jmp    43da <zim_Str_Replacer_replace+0x4a>

Disassembly of section .fini:
