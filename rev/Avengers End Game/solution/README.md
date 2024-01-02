# Agent of Shield 2
## Writeup

- there is a check function
```
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
```
- it shifts left the input by 2
- then perform a negation which is a bitwise NOT and incrementation
- finally it shift it right by 2

## solving script :

```
enc=[0x3fbf, 0x3f94, 0x3f90, 0x3f98, 0x3f9f, 0x3f9e, 0x3f97, 0x3f8c, 0x3f85, 0x3fa7, 0x3fd0, 0x3f8b, 0x3fa1, 0x3fb8, 0x3fcd, 0x3f9f, 0x3fae, 0x3fa1, 0x3fb3, 0x3f9b, 0x3fc1, 0x3fa1, 0x3fd0, 0x3fb2, 0x3fa1, 0x3fa7, 0x3fd0, 0x3f8b, 0x3fae, 0x3fa1, 0x3fb4, 0x3fcd, 0x3f9a, 0x3f8c, 0x3fdf, 0x3fdf, 0x3f83]



for x in enc :
    print(chr((0xFFFF-((x<<2)-1))>>2),end="")
    
```

## Flag

> Alphabit{Y0u_H3aR_Me?_0N_Y0uR_L3ft!!}

