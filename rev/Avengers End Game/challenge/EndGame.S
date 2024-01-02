section .data
    output dq 0x3fbf, 0x3f94, 0x3f90, 0x3f98, 0x3f9f, 0x3f9e, 0x3f97, 0x3f8c, 0x3f85, 0x3fa7, 0x3fd0, 0x3f8b, 0x3fa1, 0x3fb8, 0x3fcd, 0x3f9f, 0x3fae, 0x3fa1, 0x3fb3, 0x3f9b, 0x3fc1, 0x3fa1, 0x3fd0, 0x3fb2, 0x3fa1, 0x3fa7, 0x3fd0, 0x3f8b, 0x3fae, 0x3fa1, 0x3fb4, 0x3fcd, 0x3f9a, 0x3f8c, 0x3fdf, 0x3fdf, 0x3f83
    input resb 38

section .text
    global _start

_start:
    mov rax, 1
    mov rdi, 1
    mov rsi, prompt
    mov rdx, prompt_len
    syscall

    mov rax, 0
    mov rdi, 0
    mov rsi, input
    mov rdx, 38
    syscall

    mov rcx, 0

check:
    cmp byte [input + rcx], 10
    je  end

    movzx rax, byte [input + rcx]
    shl rax, 2
    neg rax
    shr rax, 2
    mov rbx, [output + rcx]
    cmp rax, rbx
    jne  not_equal

    inc rcx
    jmp check

not_equal:
    mov rax, 1
    mov rdi, 1
    mov rsi, no_msg
    mov rdx, no_len
    syscall

    jmp  exit

end:
    mov rax, 1
    mov rdi, 1
    mov rsi, yes_msg
    mov rdx, yes_len
    syscall

exit:
    mov rax, 60
    xor rdi, rdi
    syscall

section .data
    prompt db 'Enter flag: ', 0
    prompt_len equ $ - prompt

    yes_msg db 'Yes', 0
    yes_len equ $ - yes_msg

    no_msg db 'No', 0
    no_len equ $ - no_msg
