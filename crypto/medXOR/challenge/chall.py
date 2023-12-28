import random
flag = "Alphabit{fake_flag}"
key = [random.randint(0,99),random.randint(0,99)]
c = []
for i in range(0 , len(flag)):
    c.append((ord(flag[i]) ^ key[i % len(key)]))
print(c)


# [68, 87, 117, 83, 100, 89, 108, 79, 126, 124, 98, 100, 124, 11, 112, 100, 118, 11, 105, 77, 54, 100, 52, 79, 90, 8, 115, 8, 107, 100, 114, 10, 113, 83, 53, 78, 113, 100, 113, 83, 54, 100, 110, 94, 124, 70]