from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

FLAG = "REDACTED"
KEY = os.urandom(16)

iv = os.urandom(16)
cipher = AES.new(KEY, AES.MODE_CBC, iv)
encrypted = cipher.encrypt(pad(FLAG.encode(), 16))
signature = [hex(a ^ b)[2:].zfill(2) for a, b in zip(iv, KEY[::-1])]
signature = "".join(signature)
ciphertext = iv.hex()[4:] + encrypted.hex() + signature
print("ciphertext: ", ciphertext)

# ciphertext: faa2202f72972dee1d815a53887faeee6ffcb7a6868cc71f90845a785d45dda481a8eb4c6c4d78261d5db2132fddf4c8b4bf3c6572e8ab4ce74e1dc4641b603dadc1da1c717df3e0e76811369dc0