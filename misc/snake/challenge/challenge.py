#!/usr/bin/env python3

MAX_LENGTH = 4

print("to solve this challenge you need to think in a pythonic way")

inp1 = input("here is your first try:")


try:
    if len(inp1) > MAX_LENGTH or float(inp1) < 10**12 or inp1=='nan':
        print("You are wrong")
        exit()

    print("\nyou tricked me but i knew that so i will make it even harder for you\n")
    inp2 = input("here is your second try:")
    if len(inp2) > MAX_LENGTH-1 or float(inp2) < 10000000000 or inp2=='nan':
        print("\nYou are wrong")
        exit()
    if  inp1 == inp2:
        print("\nnice try, but i learn from my mistakes!\n")
        exit()
    print("\npython is very tricky and so are you\n")
    with open('./flag.txt', 'rb') as flag:
        print(flag.read())
    
except Exception:
    print("INVALID INPUT !!!")