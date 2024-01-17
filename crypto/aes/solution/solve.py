from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import long_to_bytes
from pwn import xor


def brute_force(iv,enc,sig):
	for i in range(2**8, 2**16):
		my_iv = long_to_bytes(i) + iv
		my_key = xor(my_iv,sig)[::-1]
		try:
			cipher = AES.new(my_key, AES.MODE_CBC, my_iv)
			pt = cipher.decrypt(enc)
			if pt[0:8] == b'Alphabit':
				print(pt.decode())
				break
			else:
				pass
		except:
			pass
	return

ct = bytes.fromhex('faa2202f72972dee1d815a53887faeee6ffcb7a6868cc71f90845a785d45dda481a8eb4c6c4d78261d5db2132fddf4c8b4bf3c6572e8ab4ce74e1dc4641b603dadc1da1c717df3e0e76811369dc0')
iv = ct[0:14]
enc = ct[14:-16]
sig = ct[-16:]

brute_force(iv,enc,sig)
