flag = "Alphabit{fake_flag}"
c = []
for i in range(0, len(flag)):
    c.append((ord(flag[i]) ^ 0x88) + 0x7)
print(c) 

#c=[208, 235, 255, 231, 240, 241, 232, 259, 250, 215, 191, 257, 222, 192, 258, 222, 258, 191, 222, 194, 195, 258, 248, 252]
