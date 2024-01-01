def string_to_xor_array(input_string, key_array):
    ord_array = [ord(char) for char in input_string]
    key_length = len(key_array)

    xor_result = [
        char_ord ^ key_array[i % key_length] for i, char_ord in enumerate(ord_array)
    ]

    return xor_result

# Example Usage:
ascii_string = input("give me : ")
xor_key = [42, 79, 51, 33, 16] 
result_array = string_to_xor_array(ascii_string, xor_key)

print(result_array)

# obfuscation https://obfuscator.io/
# deobfuscation https://obf-io.deobfuscate.io/
# Alphabit{Crack3d_Cod3_D00r}
