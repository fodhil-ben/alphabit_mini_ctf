#!/usr/bin/python3
from Crypto.Util.number import bytes_to_long, getPrime
from flag import FLAG


p =getPrime(512)
q =getPrime(512)
o =getPrime(512)

n = p * q
e = 65537
m = bytes_to_long(FLAG)
c = pow(m, e, n)

gift = p*o


print(f'{e=}')
print(f'{n=}')
print(f'{c=}')
print(f'{gift=}')
