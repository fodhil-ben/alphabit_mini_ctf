check = ['26', '38', 'b', '72', '5f', '56', '1a', '48', '28', '_', 'd', '1c', '75', '2f', '22', '1d', '_', '37', '59', '1', 'f', 'b', '_', '3e', '2', 'd', '_', '75', '2f', '38', '_', '4', '36', '52', '56', '2']
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
new_recipe = "fvklzt3e8pryho6x4ub2qsgnd0w1im75caj9"
key = "JUrC4gm9JuxG"

def uncook(well_cooked, key):
    decoration = []
    index = 0
    for attribute in well_cooked:
        if attribute == "_":
            decoration.append("_")
        else:
            decoration.append(chr(int(attribute, 16) ^ ord(key[index % len(key)])))
            index += 1
    return decoration

def unprepare(decoration):
    message = []
    for attribute in decoration:
        if attribute == "_":
            message.append("_")
        else:
            index = new_recipe.find(attribute)  
            if index != -1:
                message.append(alphabet[index])
            else:
                message.append(attribute) 
    return ''.join(message)

def main():
    prep = uncook(check, key)
    print(prep)
    dough = unprepare(prep)
    print("The dough is:", dough)

if __name__ == "__main__":
    main()
