extracting the hash of the zip file using : 

```
zip2john vault.zip >hash
```

Performing wordlist attack using rockyou.txt : 

```
john --wordlist=rockyou.txt hash
```

We get the password for the zip file

![image](https://github.com/fodhil-ben/alphabit_mini_ctf/assets/123596322/76139f72-ab67-490b-a508-78fc4c9efa6c)


```
luckyana
```


![flag](https://github.com/fodhil-ben/alphabit_mini_ctf/assets/123596322/6a345185-8d2d-4d53-8316-2c62608b431a)
