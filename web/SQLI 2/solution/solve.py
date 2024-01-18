from unidecode import unidecode

def find_matching_chars():
    for i in range(0, 0x10FFFF):
        try:
            char = chr(i)
            result = unidecode(char)
            if result == ".": #here for example we search for all chars that matches the dot
                print(f"Original: {char}, Unidecoded: {result}")
        except ValueError:
            # Skip invalid Unicode values
            pass

# Run the test
find_matching_chars()
