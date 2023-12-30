#!/usr/bin/python3
from Crypto.Util.number import bytes_to_long, getPrime
from flag import FLAG


p =getPrime(1024)
q =getPrime(1024)
n = p * q
e = 3
m = bytes_to_long(FLAG)

c = pow(m, e, n)



print(f'{e=}')
print(f'{n=}')
print(f'{c=}')

