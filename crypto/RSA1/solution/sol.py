from Crypto.Util.number import inverse, long_to_bytes

n=171982516197433991513379139721115848923
c=84341465200548869340343578848375953199
e=65537

#Factorise the n using factordb or any other tool to get the p and q
p=9695296634545310753
q=17738757531630656891
#RSA being RSA
phi=(p-1)*(q-1)
d=inverse(e,phi)
m=pow(c,d,n)


print(long_to_bytes(m))