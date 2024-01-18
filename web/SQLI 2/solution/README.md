# SQLI
## writeup

bypassing the the AdminBlacklist using other characters that get cleaned using unidecode
check the script [test.py](./test.py) to test your input if it baypasses the admin blacklist
check the script [solve.py](./solve.py)  that output all possible matches that can give the same result after the unidecode cleaning 


for the password field. here the intended input
```
b'/**/IS/**/NOT/**/'C
```
the unintended way is to add `/*` in the end of the admin input


