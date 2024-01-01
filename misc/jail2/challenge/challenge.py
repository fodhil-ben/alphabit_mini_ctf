#!/usr/bin/env python3

blackList = ["open", "print", "read"]

inp = input("Enter your inp:\n>>> ")



if any([i in inp for i in blackList]):
    print("No no!, Invalid Input")
    exit()

eval(inp)