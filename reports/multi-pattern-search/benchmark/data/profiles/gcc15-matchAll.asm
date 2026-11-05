
gcc15-strmatch.so:     file format elf64-x86-64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .plt.got:

Disassembly of section .plt.sec:

Disassembly of section .text:

0000000000005520 <zim_Str_Matcher_matchAll>:
    5520:	f3 0f 1e fa          	endbr64
    5524:	41 57                	push   %r15
    5526:	41 56                	push   %r14
    5528:	41 55                	push   %r13
    552a:	41 54                	push   %r12
    552c:	55                   	push   %rbp
    552d:	53                   	push   %rbx
    552e:	48 83 ec 58          	sub    $0x58,%rsp
    5532:	64 4c 8b 24 25 28 00 	mov    %fs:0x28,%r12
    5539:	00 00 
    553b:	4c 89 64 24 48       	mov    %r12,0x48(%rsp)
    5540:	44 8b 67 2c          	mov    0x2c(%rdi),%r12d
    5544:	41 83 fc 01          	cmp    $0x1,%r12d
    5548:	0f 85 1a d4 ff ff    	jne    2968 <zim_Str_Matcher_matchAll.cold+0x81>
    554e:	48 89 fb             	mov    %rdi,%rbx
    5551:	48 89 f5             	mov    %rsi,%rbp
    5554:	80 7f 58 06          	cmpb   $0x6,0x58(%rdi)
    5558:	0f 85 b8 02 00 00    	jne    5816 <zim_Str_Matcher_matchAll+0x2f6>
    555e:	4c 8b 7f 50          	mov    0x50(%rdi),%r15
    5562:	4c 8b 63 20          	mov    0x20(%rbx),%r12
    5566:	e8 35 cf ff ff       	call   24a0 <_zend_new_array_0@plt>
    556b:	c7 45 08 07 03 00 00 	movl   $0x307,0x8(%rbp)
    5572:	45 8b 4c 24 f8       	mov    -0x8(%r12),%r9d
    5577:	48 89 45 00          	mov    %rax,0x0(%rbp)
    557b:	45 85 c9             	test   %r9d,%r9d
    557e:	0f 84 dc 01 00 00    	je     5760 <zim_Str_Matcher_matchAll+0x240>
    5584:	49 83 7f 10 00       	cmpq   $0x0,0x10(%r15)
    5589:	0f 84 d1 01 00 00    	je     5760 <zim_Str_Matcher_matchAll+0x240>
    558f:	31 db                	xor    %ebx,%ebx
    5591:	45 31 d2             	xor    %r10d,%r10d
    5594:	31 ff                	xor    %edi,%edi
    5596:	45 31 ed             	xor    %r13d,%r13d
    5599:	31 f6                	xor    %esi,%esi
    559b:	4d 89 fe             	mov    %r15,%r14
    559e:	66 90                	xchg   %ax,%ax
    55a0:	43 0f b6 44 16 18    	movzbl 0x18(%r14,%r10,1),%eax
    55a6:	49 83 c2 01          	add    $0x1,%r10
    55aa:	41 0f b7 8c 44 e4 fd 	movzwl -0x21c(%r12,%rax,2),%ecx
    55b1:	ff ff 
    55b3:	66 85 c9             	test   %cx,%cx
    55b6:	0f 84 24 02 00 00    	je     57e0 <zim_Str_Matcher_matchAll+0x2c0>
    55bc:	45 8b 8c 24 b0 fd ff 	mov    -0x250(%r12),%r9d
    55c3:	ff 
    55c4:	45 39 cd             	cmp    %r9d,%r13d
    55c7:	0f 82 1b 02 00 00    	jb     57e8 <zim_Str_Matcher_matchAll+0x2c8>
    55cd:	4d 8b 9c 24 c8 fd ff 	mov    -0x238(%r12),%r11
    55d4:	ff 
    55d5:	eb 1b                	jmp    55f2 <zim_Str_Matcher_matchAll+0xd2>
    55d7:	66 0f 1f 84 00 00 00 	nopw   0x0(%rax,%rax,1)
    55de:	00 00 
    55e0:	0f 87 a2 01 00 00    	ja     5788 <zim_Str_Matcher_matchAll+0x268>
    55e6:	44 8b 2a             	mov    (%rdx),%r13d
    55e9:	45 39 cd             	cmp    %r9d,%r13d
    55ec:	0f 82 f6 01 00 00    	jb     57e8 <zim_Str_Matcher_matchAll+0x2c8>
    55f2:	45 29 cd             	sub    %r9d,%r13d
    55f5:	4b 8d 44 6d 00       	lea    0x0(%r13,%r13,2),%rax
    55fa:	49 8d 14 83          	lea    (%r11,%rax,4),%rdx
    55fe:	44 0f b7 42 08       	movzwl 0x8(%rdx),%r8d
    5603:	41 83 f8 01          	cmp    $0x1,%r8d
    5607:	75 d7                	jne    55e0 <zim_Str_Matcher_matchAll+0xc0>
    5609:	66 3b 4a 0a          	cmp    0xa(%rdx),%cx
    560d:	75 d7                	jne    55e6 <zim_Str_Matcher_matchAll+0xc6>
    560f:	44 8b 6a 04          	mov    0x4(%rdx),%r13d
    5613:	45 85 ed             	test   %r13d,%r13d
    5616:	0f 89 b3 01 00 00    	jns    57cf <zim_Str_Matcher_matchAll+0x2af>
    561c:	0f 1f 40 00          	nopl   0x0(%rax)
    5620:	41 81 e5 ff ff ff 7f 	and    $0x7fffffff,%r13d
    5627:	49 8b 94 24 c0 fd ff 	mov    -0x240(%r12),%rdx
    562e:	ff 
    562f:	44 89 e8             	mov    %r13d,%eax
    5632:	48 8d 04 40          	lea    (%rax,%rax,2),%rax
    5636:	48 8d 0c 82          	lea    (%rdx,%rax,4),%rcx
    563a:	49 63 c5             	movslq %r13d,%rax
    563d:	44 8b 01             	mov    (%rcx),%r8d
    5640:	45 85 c0             	test   %r8d,%r8d
    5643:	0f 88 bf 01 00 00    	js     5808 <zim_Str_Matcher_matchAll+0x2e8>
    5649:	48 89 6c 24 28       	mov    %rbp,0x28(%rsp)
    564e:	44 89 6c 24 1c       	mov    %r13d,0x1c(%rsp)
    5653:	4d 89 d5             	mov    %r10,%r13
    5656:	4c 89 74 24 20       	mov    %r14,0x20(%rsp)
    565b:	49 89 f6             	mov    %rsi,%r14
    565e:	66 90                	xchg   %ax,%ax
    5660:	4c 8d 3c 40          	lea    (%rax,%rax,2),%r15
    5664:	49 8b 44 24 e8       	mov    -0x18(%r12),%rax
    5669:	4d 89 e9             	mov    %r13,%r9
    566c:	49 c1 e7 02          	shl    $0x2,%r15
    5670:	4a 8d 0c 3a          	lea    (%rdx,%r15,1),%rcx
    5674:	4c 63 01             	movslq (%rcx),%r8
    5677:	4c 89 c5             	mov    %r8,%rbp
    567a:	4e 8b 04 c0          	mov    (%rax,%r8,8),%r8
    567e:	4d 2b 48 10          	sub    0x10(%r8),%r9
    5682:	48 81 fb 00 00 00 40 	cmp    $0x40000000,%rbx
    5689:	0f 84 94 d2 ff ff    	je     2923 <zim_Str_Matcher_matchAll.cold+0x3c>
    568f:	49 39 de             	cmp    %rbx,%r14
    5692:	75 43                	jne    56d7 <zim_Str_Matcher_matchAll+0x1b7>
    5694:	4d 85 f6             	test   %r14,%r14
    5697:	4b 8d 04 36          	lea    (%r14,%r14,1),%rax
    569b:	41 be 10 00 00 00    	mov    $0x10,%r14d
    56a1:	ba 18 00 00 00       	mov    $0x18,%edx
    56a6:	4c 0f 45 f0          	cmovne %rax,%r14
    56aa:	31 c9                	xor    %ecx,%ecx
    56ac:	4c 89 44 24 10       	mov    %r8,0x10(%rsp)
    56b1:	4c 89 4c 24 08       	mov    %r9,0x8(%rsp)
    56b6:	4c 89 f6             	mov    %r14,%rsi
    56b9:	e8 22 ce ff ff       	call   24e0 <_safe_erealloc@plt>
    56be:	4c 8b 44 24 10       	mov    0x10(%rsp),%r8
    56c3:	4c 8b 4c 24 08       	mov    0x8(%rsp),%r9
    56c8:	49 8b 94 24 c0 fd ff 	mov    -0x240(%r12),%rdx
    56cf:	ff 
    56d0:	48 89 c7             	mov    %rax,%rdi
    56d3:	4a 8d 0c 3a          	lea    (%rdx,%r15,1),%rcx
    56d7:	48 8d 04 5b          	lea    (%rbx,%rbx,2),%rax
    56db:	48 83 c3 01          	add    $0x1,%rbx
    56df:	4c 89 0c c7          	mov    %r9,(%rdi,%rax,8)
    56e3:	4d 8b 40 10          	mov    0x10(%r8),%r8
    56e7:	89 6c c7 10          	mov    %ebp,0x10(%rdi,%rax,8)
    56eb:	4c 89 44 c7 08       	mov    %r8,0x8(%rdi,%rax,8)
    56f0:	48 63 41 04          	movslq 0x4(%rcx),%rax
    56f4:	85 c0                	test   %eax,%eax
    56f6:	0f 89 64 ff ff ff    	jns    5660 <zim_Str_Matcher_matchAll+0x140>
    56fc:	4c 89 f6             	mov    %r14,%rsi
    56ff:	4c 8b 74 24 20       	mov    0x20(%rsp),%r14
    5704:	4d 89 ea             	mov    %r13,%r10
    5707:	48 8b 6c 24 28       	mov    0x28(%rsp),%rbp
    570c:	44 8b 6c 24 1c       	mov    0x1c(%rsp),%r13d
    5711:	4d 3b 56 10          	cmp    0x10(%r14),%r10
    5715:	0f 82 85 fe ff ff    	jb     55a0 <zim_Str_Matcher_matchAll+0x80>
    571b:	49 89 f8             	mov    %rdi,%r8
    571e:	48 83 fb 01          	cmp    $0x1,%rbx
    5722:	0f 87 18 01 00 00    	ja     5840 <zim_Str_Matcher_matchAll+0x320>
    5728:	48 85 db             	test   %rbx,%rbx
    572b:	0f 85 e4 01 00 00    	jne    5915 <zim_Str_Matcher_matchAll+0x3f5>
    5731:	4d 85 c0             	test   %r8,%r8
    5734:	74 2a                	je     5760 <zim_Str_Matcher_matchAll+0x240>
    5736:	48 8b 44 24 48       	mov    0x48(%rsp),%rax
    573b:	64 48 2b 04 25 28 00 	sub    %fs:0x28,%rax
    5742:	00 00 
    5744:	0f 85 15 02 00 00    	jne    595f <zim_Str_Matcher_matchAll+0x43f>
    574a:	48 83 c4 58          	add    $0x58,%rsp
    574e:	4c 89 c7             	mov    %r8,%rdi
    5751:	5b                   	pop    %rbx
    5752:	5d                   	pop    %rbp
    5753:	41 5c                	pop    %r12
    5755:	41 5d                	pop    %r13
    5757:	41 5e                	pop    %r14
    5759:	41 5f                	pop    %r15
    575b:	e9 30 cd ff ff       	jmp    2490 <_efree@plt>
    5760:	48 8b 44 24 48       	mov    0x48(%rsp),%rax
    5765:	64 48 2b 04 25 28 00 	sub    %fs:0x28,%rax
    576c:	00 00 
    576e:	0f 85 e1 01 00 00    	jne    5955 <zim_Str_Matcher_matchAll+0x435>
    5774:	48 83 c4 58          	add    $0x58,%rsp
    5778:	5b                   	pop    %rbx
    5779:	5d                   	pop    %rbp
    577a:	41 5c                	pop    %r12
    577c:	41 5d                	pop    %r13
    577e:	41 5e                	pop    %r14
    5780:	41 5f                	pop    %r15
    5782:	c3                   	ret
    5783:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
    5788:	44 8b 7a 04          	mov    0x4(%rdx),%r15d
    578c:	4d 8b ac 24 a8 fd ff 	mov    -0x258(%r12),%r13
    5793:	ff 
    5794:	41 83 e8 01          	sub    $0x1,%r8d
    5798:	4d 01 f8             	add    %r15,%r8
    579b:	4b 8d 44 fd 00       	lea    0x0(%r13,%r15,8),%rax
    57a0:	4f 8d 44 c5 08       	lea    0x8(%r13,%r8,8),%r8
    57a5:	eb 16                	jmp    57bd <zim_Str_Matcher_matchAll+0x29d>
    57a7:	66 0f 1f 84 00 00 00 	nopw   0x0(%rax,%rax,1)
    57ae:	00 00 
    57b0:	48 83 c0 08          	add    $0x8,%rax
    57b4:	49 39 c0             	cmp    %rax,%r8
    57b7:	0f 84 29 fe ff ff    	je     55e6 <zim_Str_Matcher_matchAll+0xc6>
    57bd:	66 3b 48 04          	cmp    0x4(%rax),%cx
    57c1:	75 ed                	jne    57b0 <zim_Str_Matcher_matchAll+0x290>
    57c3:	44 8b 28             	mov    (%rax),%r13d
    57c6:	45 85 ed             	test   %r13d,%r13d
    57c9:	0f 88 51 fe ff ff    	js     5620 <zim_Str_Matcher_matchAll+0x100>
    57cf:	4d 3b 56 10          	cmp    0x10(%r14),%r10
    57d3:	0f 82 c7 fd ff ff    	jb     55a0 <zim_Str_Matcher_matchAll+0x80>
    57d9:	e9 3d ff ff ff       	jmp    571b <zim_Str_Matcher_matchAll+0x1fb>
    57de:	66 90                	xchg   %ax,%ax
    57e0:	45 31 ed             	xor    %r13d,%r13d
    57e3:	eb ea                	jmp    57cf <zim_Str_Matcher_matchAll+0x2af>
    57e5:	0f 1f 00             	nopl   (%rax)
    57e8:	49 63 84 24 e0 fd ff 	movslq -0x220(%r12),%rax
    57ef:	ff 
    57f0:	49 8b 94 24 a0 fd ff 	mov    -0x260(%r12),%rdx
    57f7:	ff 
    57f8:	49 0f af c5          	imul   %r13,%rax
    57fc:	48 01 c8             	add    %rcx,%rax
    57ff:	44 8b 2c 82          	mov    (%rdx,%rax,4),%r13d
    5803:	eb c1                	jmp    57c6 <zim_Str_Matcher_matchAll+0x2a6>
    5805:	0f 1f 00             	nopl   (%rax)
    5808:	48 63 41 04          	movslq 0x4(%rcx),%rax
    580c:	85 c0                	test   %eax,%eax
    580e:	0f 89 35 fe ff ff    	jns    5649 <zim_Str_Matcher_matchAll+0x129>
    5814:	eb b9                	jmp    57cf <zim_Str_Matcher_matchAll+0x2af>
    5816:	4c 8d 6f 50          	lea    0x50(%rdi),%r13
    581a:	be 01 00 00 00       	mov    $0x1,%esi
    581f:	4c 89 ef             	mov    %r13,%rdi
    5822:	e8 19 cb ff ff       	call   2340 <zend_parse_arg_str_slow@plt>
    5827:	49 89 c7             	mov    %rax,%r15
    582a:	48 85 c0             	test   %rax,%rax
    582d:	0f 85 2f fd ff ff    	jne    5562 <zim_Str_Matcher_matchAll+0x42>
    5833:	e9 af d0 ff ff       	jmp    28e7 <zim_Str_Matcher_matchAll.cold>
    5838:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
    583f:	00 
    5840:	48 8d 0d 09 e6 ff ff 	lea    -0x19f7(%rip),%rcx        # 3e50 <ac_hit_compare>
    5847:	ba 18 00 00 00       	mov    $0x18,%edx
    584c:	48 89 de             	mov    %rbx,%rsi
    584f:	48 89 7c 24 08       	mov    %rdi,0x8(%rsp)
    5854:	e8 77 ca ff ff       	call   22d0 <qsort@plt>
    5859:	4c 8b 44 24 08       	mov    0x8(%rsp),%r8
    585e:	48 8d 44 5b fd       	lea    -0x3(%rbx,%rbx,2),%rax
    5863:	49 83 3c c0 00       	cmpq   $0x0,(%r8,%rax,8)
    5868:	0f 88 b1 00 00 00    	js     591f <zim_Str_Matcher_matchAll+0x3ff>
    586e:	4c 89 44 24 08       	mov    %r8,0x8(%rsp)
    5873:	4d 89 c7             	mov    %r8,%r15
    5876:	45 31 ed             	xor    %r13d,%r13d
    5879:	4c 8d 74 24 30       	lea    0x30(%rsp),%r14
    587e:	66 90                	xchg   %ax,%ax
    5880:	48 8b 35 a9 2a 00 00 	mov    0x2aa9(%rip),%rsi        # 8330 <str_matchresult_ce>
    5887:	4c 89 f7             	mov    %r14,%rdi
    588a:	e8 91 cb ff ff       	call   2420 <object_init_ex@plt>
    588f:	48 8b 44 24 30       	mov    0x30(%rsp),%rax
    5894:	49 8b 37             	mov    (%r15),%rsi
    5897:	8b 0d ab 29 00 00    	mov    0x29ab(%rip),%ecx        # 8248 <result_offset>
    589d:	48 89 34 08          	mov    %rsi,(%rax,%rcx,1)
    58a1:	49 8b 77 08          	mov    0x8(%r15),%rsi
    58a5:	c7 44 08 08 04 00 00 	movl   $0x4,0x8(%rax,%rcx,1)
    58ac:	00 
    58ad:	8b 0d 91 29 00 00    	mov    0x2991(%rip),%ecx        # 8244 <result_length>
    58b3:	48 89 34 08          	mov    %rsi,(%rax,%rcx,1)
    58b7:	c7 44 08 08 04 00 00 	movl   $0x4,0x8(%rax,%rcx,1)
    58be:	00 
    58bf:	8b 0d 7b 29 00 00    	mov    0x297b(%rip),%ecx        # 8240 <result_keyword>
    58c5:	49 63 77 10          	movslq 0x10(%r15),%rsi
    58c9:	48 01 c8             	add    %rcx,%rax
    58cc:	49 8b 4c 24 e8       	mov    -0x18(%r12),%rcx
    58d1:	48 8b 0c f1          	mov    (%rcx,%rsi,8),%rcx
    58d5:	be 06 00 00 00       	mov    $0x6,%esi
    58da:	f6 41 04 40          	testb  $0x40,0x4(%rcx)
    58de:	75 08                	jne    58e8 <zim_Str_Matcher_matchAll+0x3c8>
    58e0:	83 01 01             	addl   $0x1,(%rcx)
    58e3:	be 06 01 00 00       	mov    $0x106,%esi
    58e8:	48 89 08             	mov    %rcx,(%rax)
    58eb:	48 8b 7d 00          	mov    0x0(%rbp),%rdi
    58ef:	49 83 c5 01          	add    $0x1,%r13
    58f3:	49 83 c7 18          	add    $0x18,%r15
    58f7:	89 70 08             	mov    %esi,0x8(%rax)
    58fa:	4c 89 f6             	mov    %r14,%rsi
    58fd:	e8 4e cb ff ff       	call   2450 <zend_hash_next_index_insert@plt>
    5902:	49 39 dd             	cmp    %rbx,%r13
    5905:	0f 82 75 ff ff ff    	jb     5880 <zim_Str_Matcher_matchAll+0x360>
    590b:	4c 8b 44 24 08       	mov    0x8(%rsp),%r8
    5910:	e9 1c fe ff ff       	jmp    5731 <zim_Str_Matcher_matchAll+0x211>
    5915:	48 83 3f 00          	cmpq   $0x0,(%rdi)
    5919:	0f 89 4f ff ff ff    	jns    586e <zim_Str_Matcher_matchAll+0x34e>
    591f:	4c 89 c7             	mov    %r8,%rdi
    5922:	e8 69 cb ff ff       	call   2490 <_efree@plt>
    5927:	48 8b 44 24 48       	mov    0x48(%rsp),%rax
    592c:	64 48 2b 04 25 28 00 	sub    %fs:0x28,%rax
    5933:	00 00 
    5935:	75 23                	jne    595a <zim_Str_Matcher_matchAll+0x43a>
    5937:	48 83 c4 58          	add    $0x58,%rsp
    593b:	48 8d 35 de 07 00 00 	lea    0x7de(%rip),%rsi        # 6120 <_fini+0x7a4>
    5942:	31 ff                	xor    %edi,%edi
    5944:	31 c0                	xor    %eax,%eax
    5946:	5b                   	pop    %rbx
    5947:	5d                   	pop    %rbp
    5948:	41 5c                	pop    %r12
    594a:	41 5d                	pop    %r13
    594c:	41 5e                	pop    %r14
    594e:	41 5f                	pop    %r15
    5950:	e9 bb cb ff ff       	jmp    2510 <zend_throw_error@plt>
    5955:	e8 c6 c9 ff ff       	call   2320 <__stack_chk_fail@plt>
    595a:	e8 c1 c9 ff ff       	call   2320 <__stack_chk_fail@plt>
    595f:	e8 bc c9 ff ff       	call   2320 <__stack_chk_fail@plt>

Disassembly of section .fini:
