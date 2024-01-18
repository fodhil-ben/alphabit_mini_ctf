# SQLI
## writeup

bypassing the the AdminBlacklist using other characters that get cleaned using unidecode
check the script `test.py`
for the password field. here the intended input
```
b'/**/IS/**/NOT/**/'C
```
the unintended way is to add `/*` in the end of the admin input


