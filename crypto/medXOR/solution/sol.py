knownpart = "Alphabit"
c=[68, 87, 117, 83, 100, 89, 108, 79, 126, 124, 98, 100, 124, 11, 112, 100, 118, 11, 105, 77, 54, 100, 52, 79, 90, 8, 115, 8, 107, 100, 114, 10, 113, 83, 53, 78, 113, 100, 113, 83, 54, 100, 110, 94, 124, 70]
key = []
for i in range(0, len(knownpart)):
    key.append(c[i] ^ ord(knownpart[i]))

print(key)

flag = ""
for i, value in enumerate(c):
    flag += chr(value ^ key[i % len(key)])

print(flag)