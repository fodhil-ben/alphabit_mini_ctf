import base64

# Read the base64 string from the file
with open("flag.txt", "r") as file:
    base64_data = file.read()

# Decode the base64 string
decoded_data = base64.b64decode(base64_data)

# Save the decoded data to a JPG file
with open("decoded_image.jpg", "wb") as f:
    f.write(decoded_data)

print("Image successfully decoded and saved as 'decoded_image.jpg'.")
