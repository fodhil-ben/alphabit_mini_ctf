def dungeon(password):
    test = []
    for i in range(len(password)):
        char = password[i]
        attr = ord(char) + 1 if i % 2 == 0 else ord(char) - 1
        test.append(attr)
    return test

def main():

    password = input("Enter your password: ")

    key = dungeon(password)
    target = [113, 120, 117, 103, 49, 109, 96, 99, 118, 109, 104, 100, 112, 109, 96, 50, 121, 111, 109, 47, 115, 96, 117, 104, 49, 109, 96, 48, 116, 94, 109, 50, 52, 50, 52, 115]



    if key == target:
        print("You've escaped the dungeon, well done!")
    else:
        print("You have been trapped Haha!")

if __name__ == "__main__":
    main()
