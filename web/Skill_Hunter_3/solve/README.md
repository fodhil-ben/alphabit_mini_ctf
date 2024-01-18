# SKILL HUNTER 3

## Write-up
Basically to solve the challenge you need to upload two files
.htaccess to let custom extension run as php code for example .l33t ( like the example shown on portswigger)
But to bypass the exifimgtype check you need to add in the start of your file header's bytes of one of the imf types you find in the documentation
Here if you add random bytes in the start the file .htaccess will get corrupted a non of your command will work
So you need to search for an img format that does not corrupt if we add its header's bytes in the start of the file
One of the img types that looks so perfect for our problems is xbm
Because the header of the img is a comment
This the first step of the problem
Now we need to bypass the <?
Here you need to use another encoding format like utf16 
But to run it you need to add other commands to your .htaccess file
And then you get the rce 
You print the img in your pc
Using exiftool 
You will find the flag in the comment section
I added the last step just to make it easier to cp the flag

# EXPLOIT
 since the other steps are easy to complete i'll explain only  how to bypass the `<?` . I bypassed this check using two types of encoding format. `utf-7` and `utf-16be` . for `utf-16be` i found a script `solve.py` on the internet that does the job for us .
for the utf-7 i added commands to  `.htaccess` to define server's encoding as we need.
using one of the online tools that convert `utf8` to `utf7` we convert our previous pauload to `utf-7` 
we get our rce! we get our flag!


