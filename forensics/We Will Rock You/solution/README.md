extracting the hash of the zip file using : 

```
zip2john vault.zip >hash
```

Performing wordlist attack using rockyou.txt : 

```
john --wordlist=rockyou.txt hash
```

We get the password for the zip file

```
luckyana
```