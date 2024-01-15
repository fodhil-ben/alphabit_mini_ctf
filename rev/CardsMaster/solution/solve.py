from pwn import *
from ctypes import CDLL

libc = CDLL("/lib/x86_64-linux-gnu/libc.so.6")
libc.srand(libc.time(0)+0xfe)

# io = process("./chal")
io = remote("0.0.0.0",1010)

io.recvline()
io.recvline()
io.recvline()
io.recvline()

for i in range(0,1000):
    io.recvline()
    guess = libc.rand()
    guess = str(((guess % 26 + 65) ^ 0xfefe + (guess % 26)))
    io.sendline(guess)
    print(io.recvline())
    

io.interactive()