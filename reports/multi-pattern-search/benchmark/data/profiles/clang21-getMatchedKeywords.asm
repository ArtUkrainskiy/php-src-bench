
clang21-strmatch.so:     file format elf64-x86-64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .plt.got:

Disassembly of section .text:

0000000000003790 <zim_Str_Matcher_getMatchedKeywords>:
    3790:	55                   	push   %rbp
    3791:	41 57                	push   %r15
    3793:	41 56                	push   %r14
    3795:	41 55                	push   %r13
    3797:	41 54                	push   %r12
    3799:	53                   	push   %rbx
    379a:	48 83 ec 48          	sub    $0x48,%rsp
    379e:	83 7f 2c 01          	cmpl   $0x1,0x2c(%rdi)
    37a2:	0f 85 5d 03 00 00    	jne    3b05 <zim_Str_Matcher_getMatchedKeywords+0x375>
    37a8:	49 89 f5             	mov    %rsi,%r13
    37ab:	48 8d 47 50          	lea    0x50(%rdi),%rax
    37af:	80 7f 58 06          	cmpb   $0x6,0x58(%rdi)
    37b3:	0f 85 67 03 00 00    	jne    3b20 <zim_Str_Matcher_getMatchedKeywords+0x390>
    37b9:	4c 8b 20             	mov    (%rax),%r12
    37bc:	4c 8b 77 20          	mov    0x20(%rdi),%r14
    37c0:	e8 4b ea ff ff       	call   2210 <_zend_new_array_0@plt>
    37c5:	49 89 45 00          	mov    %rax,0x0(%r13)
    37c9:	41 c7 45 08 07 03 00 	movl   $0x307,0x8(%r13)
    37d0:	00 
    37d1:	41 8b 7e f8          	mov    -0x8(%r14),%edi
    37d5:	48 85 ff             	test   %rdi,%rdi
    37d8:	0f 84 18 03 00 00    	je     3af6 <zim_Str_Matcher_getMatchedKeywords+0x366>
    37de:	49 83 7c 24 10 00    	cmpq   $0x0,0x10(%r12)
    37e4:	0f 84 0c 03 00 00    	je     3af6 <zim_Str_Matcher_getMatchedKeywords+0x366>
    37ea:	be 01 00 00 00       	mov    $0x1,%esi
    37ef:	e8 bc e9 ff ff       	call   21b0 <_ecalloc@plt>
    37f4:	49 8b 54 24 10       	mov    0x10(%r12),%rdx
    37f9:	48 85 d2             	test   %rdx,%rdx
    37fc:	0f 84 70 02 00 00    	je     3a72 <zim_Str_Matcher_getMatchedKeywords+0x2e2>
    3802:	48 89 44 24 08       	mov    %rax,0x8(%rsp)
    3807:	45 31 ff             	xor    %r15d,%r15d
    380a:	45 31 d2             	xor    %r10d,%r10d
    380d:	31 c9                	xor    %ecx,%ecx
    380f:	45 31 c9             	xor    %r9d,%r9d
    3812:	31 c0                	xor    %eax,%eax
    3814:	4c 89 6c 24 18       	mov    %r13,0x18(%rsp)
    3819:	4c 89 64 24 10       	mov    %r12,0x10(%rsp)
    381e:	eb 0f                	jmp    382f <zim_Str_Matcher_getMatchedKeywords+0x9f>
    3820:	45 31 d2             	xor    %r10d,%r10d
    3823:	49 ff c7             	inc    %r15
    3826:	49 39 d7             	cmp    %rdx,%r15
    3829:	0f 83 11 02 00 00    	jae    3a40 <zim_Str_Matcher_getMatchedKeywords+0x2b0>
    382f:	41 8b 76 f8          	mov    -0x8(%r14),%esi
    3833:	49 39 f1             	cmp    %rsi,%r9
    3836:	0f 83 04 02 00 00    	jae    3a40 <zim_Str_Matcher_getMatchedKeywords+0x2b0>
    383c:	43 0f b6 74 3c 18    	movzbl 0x18(%r12,%r15,1),%esi
    3842:	41 0f b7 b4 76 e4 fd 	movzwl -0x21c(%r14,%rsi,2),%esi
    3849:	ff ff 
    384b:	48 85 f6             	test   %rsi,%rsi
    384e:	74 d0                	je     3820 <zim_Str_Matcher_getMatchedKeywords+0x90>
    3850:	4c 89 cb             	mov    %r9,%rbx
    3853:	41 8b be b0 fd ff ff 	mov    -0x250(%r14),%edi
    385a:	41 39 fa             	cmp    %edi,%r10d
    385d:	0f 83 4d 01 00 00    	jae    39b0 <zim_Str_Matcher_getMatchedKeywords+0x220>
    3863:	44 89 d7             	mov    %r10d,%edi
    3866:	4d 63 86 e0 fd ff ff 	movslq -0x220(%r14),%r8
    386d:	4c 0f af c7          	imul   %rdi,%r8
    3871:	49 c1 e0 02          	shl    $0x2,%r8
    3875:	4d 03 86 a0 fd ff ff 	add    -0x260(%r14),%r8
    387c:	4d 8d 1c b0          	lea    (%r8,%rsi,4),%r11
    3880:	45 8b 13             	mov    (%r11),%r10d
    3883:	45 85 d2             	test   %r10d,%r10d
    3886:	49 89 d9             	mov    %rbx,%r9
    3889:	79 98                	jns    3823 <zim_Str_Matcher_getMatchedKeywords+0x93>
    388b:	41 81 e2 ff ff ff 7f 	and    $0x7fffffff,%r10d
    3892:	49 8b b6 c0 fd ff ff 	mov    -0x240(%r14),%rsi
    3899:	4f 8d 04 52          	lea    (%r10,%r10,2),%r8
    389d:	42 83 3c 86 00       	cmpl   $0x0,(%rsi,%r8,4)
    38a2:	44 89 d7             	mov    %r10d,%edi
    38a5:	79 0f                	jns    38b6 <zim_Str_Matcher_getMatchedKeywords+0x126>
    38a7:	4a 8d 3c 86          	lea    (%rsi,%r8,4),%rdi
    38ab:	8b 7f 04             	mov    0x4(%rdi),%edi
    38ae:	85 ff                	test   %edi,%edi
    38b0:	0f 88 6d ff ff ff    	js     3823 <zim_Str_Matcher_getMatchedKeywords+0x93>
    38b6:	4c 89 54 24 20       	mov    %r10,0x20(%rsp)
    38bb:	4c 89 7c 24 28       	mov    %r15,0x28(%rsp)
    38c0:	4d 8d 47 01          	lea    0x1(%r15),%r8
    38c4:	4b 8d 14 49          	lea    (%r9,%r9,2),%rdx
    38c8:	4c 8d 3c d5 10 00 00 	lea    0x10(,%rdx,8),%r15
    38cf:	00 
    38d0:	4c 8b 6c 24 08       	mov    0x8(%rsp),%r13
    38d5:	4c 89 44 24 30       	mov    %r8,0x30(%rsp)
    38da:	eb 7c                	jmp    3958 <zim_Str_Matcher_getMatchedKeywords+0x1c8>
    38dc:	0f 1f 40 00          	nopl   0x0(%rax)
    38e0:	4c 8d 2c 09          	lea    (%rcx,%rcx,1),%r13
    38e4:	48 85 c9             	test   %rcx,%rcx
    38e7:	b9 10 00 00 00       	mov    $0x10,%ecx
    38ec:	4c 0f 44 e9          	cmove  %rcx,%r13
    38f0:	ba 18 00 00 00       	mov    $0x18,%edx
    38f5:	48 89 c7             	mov    %rax,%rdi
    38f8:	4c 89 ee             	mov    %r13,%rsi
    38fb:	31 c9                	xor    %ecx,%ecx
    38fd:	4c 89 4c 24 40       	mov    %r9,0x40(%rsp)
    3902:	4c 89 54 24 38       	mov    %r10,0x38(%rsp)
    3907:	e8 34 e9 ff ff       	call   2240 <_safe_erealloc@plt>
    390c:	4c 8b 54 24 38       	mov    0x38(%rsp),%r10
    3911:	4c 8b 44 24 30       	mov    0x30(%rsp),%r8
    3916:	4c 8b 4c 24 40       	mov    0x40(%rsp),%r9
    391b:	49 8b 56 10          	mov    0x10(%r14),%rdx
    391f:	48 8b b3 c0 fd ff ff 	mov    -0x240(%rbx),%rsi
    3926:	4c 89 e9             	mov    %r13,%rcx
    3929:	4c 8b 6c 24 08       	mov    0x8(%rsp),%r13
    392e:	49 89 de             	mov    %rbx,%r14
    3931:	4c 89 c7             	mov    %r8,%rdi
    3934:	4c 29 d7             	sub    %r10,%rdi
    3937:	4a 89 7c 38 f0       	mov    %rdi,-0x10(%rax,%r15,1)
    393c:	4a 89 54 38 f8       	mov    %rdx,-0x8(%rax,%r15,1)
    3941:	46 89 24 38          	mov    %r12d,(%rax,%r15,1)
    3945:	49 ff c1             	inc    %r9
    3948:	8b 7c ae 04          	mov    0x4(%rsi,%rbp,4),%edi
    394c:	49 83 c7 18          	add    $0x18,%r15
    3950:	85 ff                	test   %edi,%edi
    3952:	0f 88 be 00 00 00    	js     3a16 <zim_Str_Matcher_getMatchedKeywords+0x286>
    3958:	89 fa                	mov    %edi,%edx
    395a:	48 8d 2c 52          	lea    (%rdx,%rdx,2),%rbp
    395e:	44 8b 24 ae          	mov    (%rsi,%rbp,4),%r12d
    3962:	49 63 d4             	movslq %r12d,%rdx
    3965:	41 80 7c 15 00 00    	cmpb   $0x0,0x0(%r13,%rdx,1)
    396b:	0f 85 a5 00 00 00    	jne    3a16 <zim_Str_Matcher_getMatchedKeywords+0x286>
    3971:	41 c6 44 15 00 01    	movb   $0x1,0x0(%r13,%rdx,1)
    3977:	49 81 f9 00 00 00 40 	cmp    $0x40000000,%r9
    397e:	0f 84 4d 01 00 00    	je     3ad1 <zim_Str_Matcher_getMatchedKeywords+0x341>
    3984:	49 8b 7e e8          	mov    -0x18(%r14),%rdi
    3988:	4c 89 f3             	mov    %r14,%rbx
    398b:	4c 8b 34 d7          	mov    (%rdi,%rdx,8),%r14
    398f:	4d 8b 56 10          	mov    0x10(%r14),%r10
    3993:	49 39 c9             	cmp    %rcx,%r9
    3996:	0f 84 44 ff ff ff    	je     38e0 <zim_Str_Matcher_getMatchedKeywords+0x150>
    399c:	4c 89 d2             	mov    %r10,%rdx
    399f:	eb 8d                	jmp    392e <zim_Str_Matcher_getMatchedKeywords+0x19e>
    39a1:	66 66 66 66 66 66 2e 	data16 data16 data16 data16 data16 cs nopw 0x0(%rax,%rax,1)
    39a8:	0f 1f 84 00 00 00 00 
    39af:	00 
    39b0:	4d 8b 86 c8 fd ff ff 	mov    -0x238(%r14),%r8
    39b7:	eb 1a                	jmp    39d3 <zim_Str_Matcher_getMatchedKeywords+0x243>
    39b9:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    39c0:	66 41 3b 71 0a       	cmp    0xa(%r9),%si
    39c5:	74 6d                	je     3a34 <zim_Str_Matcher_getMatchedKeywords+0x2a4>
    39c7:	45 8b 11             	mov    (%r9),%r10d
    39ca:	41 39 fa             	cmp    %edi,%r10d
    39cd:	0f 82 90 fe ff ff    	jb     3863 <zim_Str_Matcher_getMatchedKeywords+0xd3>
    39d3:	41 29 fa             	sub    %edi,%r10d
    39d6:	4f 8d 14 52          	lea    (%r10,%r10,2),%r10
    39da:	4f 8d 0c 90          	lea    (%r8,%r10,4),%r9
    39de:	47 0f b7 54 90 08    	movzwl 0x8(%r8,%r10,4),%r10d
    39e4:	45 85 d2             	test   %r10d,%r10d
    39e7:	74 de                	je     39c7 <zim_Str_Matcher_getMatchedKeywords+0x237>
    39e9:	41 83 fa 01          	cmp    $0x1,%r10d
    39ed:	74 d1                	je     39c0 <zim_Str_Matcher_getMatchedKeywords+0x230>
    39ef:	45 8b 59 04          	mov    0x4(%r9),%r11d
    39f3:	49 c1 e3 03          	shl    $0x3,%r11
    39f7:	4d 03 9e a8 fd ff ff 	add    -0x258(%r14),%r11
    39fe:	66 90                	xchg   %ax,%ax
    3a00:	66 41 39 73 04       	cmp    %si,0x4(%r11)
    3a05:	0f 84 75 fe ff ff    	je     3880 <zim_Str_Matcher_getMatchedKeywords+0xf0>
    3a0b:	49 83 c3 08          	add    $0x8,%r11
    3a0f:	49 ff ca             	dec    %r10
    3a12:	75 ec                	jne    3a00 <zim_Str_Matcher_getMatchedKeywords+0x270>
    3a14:	eb b1                	jmp    39c7 <zim_Str_Matcher_getMatchedKeywords+0x237>
    3a16:	4c 8b 64 24 10       	mov    0x10(%rsp),%r12
    3a1b:	49 8b 54 24 10       	mov    0x10(%r12),%rdx
    3a20:	4c 8b 6c 24 18       	mov    0x18(%rsp),%r13
    3a25:	4c 8b 7c 24 28       	mov    0x28(%rsp),%r15
    3a2a:	4c 8b 54 24 20       	mov    0x20(%rsp),%r10
    3a2f:	e9 ef fd ff ff       	jmp    3823 <zim_Str_Matcher_getMatchedKeywords+0x93>
    3a34:	49 83 c1 04          	add    $0x4,%r9
    3a38:	4d 89 cb             	mov    %r9,%r11
    3a3b:	e9 40 fe ff ff       	jmp    3880 <zim_Str_Matcher_getMatchedKeywords+0xf0>
    3a40:	49 89 c7             	mov    %rax,%r15
    3a43:	48 8b 7c 24 08       	mov    0x8(%rsp),%rdi
    3a48:	4c 89 cd             	mov    %r9,%rbp
    3a4b:	e8 b0 e7 ff ff       	call   2200 <_efree@plt>
    3a50:	48 89 ee             	mov    %rbp,%rsi
    3a53:	48 83 fd 02          	cmp    $0x2,%rbp
    3a57:	72 1e                	jb     3a77 <zim_Str_Matcher_getMatchedKeywords+0x2e7>
    3a59:	48 8d 0d 10 01 00 00 	lea    0x110(%rip),%rcx        # 3b70 <ac_hit_compare>
    3a60:	ba 18 00 00 00       	mov    $0x18,%edx
    3a65:	4d 89 fc             	mov    %r15,%r12
    3a68:	4c 89 ff             	mov    %r15,%rdi
    3a6b:	e8 d0 e5 ff ff       	call   2040 <qsort@plt>
    3a70:	eb 12                	jmp    3a84 <zim_Str_Matcher_getMatchedKeywords+0x2f4>
    3a72:	48 89 c7             	mov    %rax,%rdi
    3a75:	eb 47                	jmp    3abe <zim_Str_Matcher_getMatchedKeywords+0x32e>
    3a77:	48 85 f6             	test   %rsi,%rsi
    3a7a:	bd 01 00 00 00       	mov    $0x1,%ebp
    3a7f:	4d 89 fc             	mov    %r15,%r12
    3a82:	74 32                	je     3ab6 <zim_Str_Matcher_getMatchedKeywords+0x326>
    3a84:	49 8d 5c 24 10       	lea    0x10(%r12),%rbx
    3a89:	eb 16                	jmp    3aa1 <zim_Str_Matcher_getMatchedKeywords+0x311>
    3a8b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
    3a90:	4c 89 ef             	mov    %r13,%rdi
    3a93:	e8 c8 e7 ff ff       	call   2260 <add_next_index_str@plt>
    3a98:	48 83 c3 18          	add    $0x18,%rbx
    3a9c:	48 ff cd             	dec    %rbp
    3a9f:	74 1a                	je     3abb <zim_Str_Matcher_getMatchedKeywords+0x32b>
    3aa1:	49 8b 46 e8          	mov    -0x18(%r14),%rax
    3aa5:	48 63 0b             	movslq (%rbx),%rcx
    3aa8:	48 8b 34 c8          	mov    (%rax,%rcx,8),%rsi
    3aac:	f6 46 04 40          	testb  $0x40,0x4(%rsi)
    3ab0:	75 de                	jne    3a90 <zim_Str_Matcher_getMatchedKeywords+0x300>
    3ab2:	ff 06                	incl   (%rsi)
    3ab4:	eb da                	jmp    3a90 <zim_Str_Matcher_getMatchedKeywords+0x300>
    3ab6:	4d 85 e4             	test   %r12,%r12
    3ab9:	74 3b                	je     3af6 <zim_Str_Matcher_getMatchedKeywords+0x366>
    3abb:	4c 89 ff             	mov    %r15,%rdi
    3abe:	48 83 c4 48          	add    $0x48,%rsp
    3ac2:	5b                   	pop    %rbx
    3ac3:	41 5c                	pop    %r12
    3ac5:	41 5d                	pop    %r13
    3ac7:	41 5e                	pop    %r14
    3ac9:	41 5f                	pop    %r15
    3acb:	5d                   	pop    %rbp
    3acc:	e9 2f e7 ff ff       	jmp    2200 <_efree@plt>
    3ad1:	48 8d 35 a5 26 00 00 	lea    0x26a5(%rip),%rsi        # 617d <_fini+0xe91>
    3ad8:	48 89 c3             	mov    %rax,%rbx
    3adb:	31 ff                	xor    %edi,%edi
    3add:	31 c0                	xor    %eax,%eax
    3adf:	e8 8c e7 ff ff       	call   2270 <zend_throw_error@plt>
    3ae4:	4c 89 ef             	mov    %r13,%rdi
    3ae7:	e8 14 e7 ff ff       	call   2200 <_efree@plt>
    3aec:	48 85 db             	test   %rbx,%rbx
    3aef:	74 05                	je     3af6 <zim_Str_Matcher_getMatchedKeywords+0x366>
    3af1:	48 89 df             	mov    %rbx,%rdi
    3af4:	eb c8                	jmp    3abe <zim_Str_Matcher_getMatchedKeywords+0x32e>
    3af6:	48 83 c4 48          	add    $0x48,%rsp
    3afa:	5b                   	pop    %rbx
    3afb:	41 5c                	pop    %r12
    3afd:	41 5d                	pop    %r13
    3aff:	41 5e                	pop    %r14
    3b01:	41 5f                	pop    %r15
    3b03:	5d                   	pop    %rbp
    3b04:	c3                   	ret
    3b05:	bf 01 00 00 00       	mov    $0x1,%edi
    3b0a:	be 01 00 00 00       	mov    $0x1,%esi
    3b0f:	e8 ac e5 ff ff       	call   20c0 <zend_wrong_parameters_count_error@plt>
    3b14:	b0 01                	mov    $0x1,%al
    3b16:	45 31 f6             	xor    %r14d,%r14d
    3b19:	45 31 c0             	xor    %r8d,%r8d
    3b1c:	31 c9                	xor    %ecx,%ecx
    3b1e:	eb 28                	jmp    3b48 <zim_Str_Matcher_getMatchedKeywords+0x3b8>
    3b20:	49 89 ff             	mov    %rdi,%r15
    3b23:	41 be 01 00 00 00    	mov    $0x1,%r14d
    3b29:	48 89 c3             	mov    %rax,%rbx
    3b2c:	48 89 c7             	mov    %rax,%rdi
    3b2f:	be 01 00 00 00       	mov    $0x1,%esi
    3b34:	e8 77 e5 ff ff       	call   20b0 <zend_parse_arg_str_slow@plt>
    3b39:	48 85 c0             	test   %rax,%rax
    3b3c:	75 25                	jne    3b63 <zim_Str_Matcher_getMatchedKeywords+0x3d3>
    3b3e:	b0 0c                	mov    $0xc,%al
    3b40:	b9 04 00 00 00       	mov    $0x4,%ecx
    3b45:	49 89 d8             	mov    %rbx,%r8
    3b48:	0f b6 f8             	movzbl %al,%edi
    3b4b:	44 89 f6             	mov    %r14d,%esi
    3b4e:	31 d2                	xor    %edx,%edx
    3b50:	48 83 c4 48          	add    $0x48,%rsp
    3b54:	5b                   	pop    %rbx
    3b55:	41 5c                	pop    %r12
    3b57:	41 5d                	pop    %r13
    3b59:	41 5e                	pop    %r14
    3b5b:	41 5f                	pop    %r15
    3b5d:	5d                   	pop    %rbp
    3b5e:	e9 8d e6 ff ff       	jmp    21f0 <zend_wrong_parameter_error@plt>
    3b63:	49 89 c4             	mov    %rax,%r12
    3b66:	4c 89 ff             	mov    %r15,%rdi
    3b69:	e9 4e fc ff ff       	jmp    37bc <zim_Str_Matcher_getMatchedKeywords+0x2c>

Disassembly of section .fini:
