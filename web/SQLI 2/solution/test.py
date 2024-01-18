from unidecode import unidecode

# Original URL with Unicode characters
url = "àдмìн｡àlphàbìt"
AdminBlacklist = ['a', 'd', 'm', 'i', 'n','.']

if any(char in AdminBlacklist for char in url):
    print("Condition: The condition is true.")
else:
    print("Condition: The condition is false.")


# After unidecode (should be True)
decoded_url = unidecode(url)
print(decoded_url)

# Check if any character in the decoded URL is in the AdminBlacklist
if any(char in AdminBlacklist for char in decoded_url):
    print("Condition after unidecode: The condition is true.")
else:
    print("Condition after unidecode: The condition is false.")
