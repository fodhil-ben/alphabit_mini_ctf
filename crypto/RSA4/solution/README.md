# RSA4
## writeup

we have:
p = prime
q = prime
o = prime

n = p*q
gift = p*o

we can get the p by calculating gcd(p, q)


solve script 
```py
from Crypto.Util.number import long_to_bytes
from gmpy2 import gcd

e=65537
n=134469406812033733897401857410542103280146691020462277000869447640185537464707383420976879672337509054113033173733041506954098124591342076590525978274979143787579788004661351905490854564675096234289043962325001210662588294560908587537356252037416675413752744103173726168117570229992262527280887444508249906913
c=101872894649087716557950016259410540800794869861526066595739835261774690967864382382402154107141261653565798387686460618311377696975711699746917230641629111298062470599653636444459598909299622105243754752138706761799838395999485607933284261177448559555621574605178659056079054743135971612744922505744855014897
gift=129129402526132742033929530189717596626664966270684176548234257105367888389134698161765830799305751660769424463360633393363735895241681118825922371712082751311209914382336454662824669286121955899676196555948965260048169119228784940794544138421077847835259343558582047571946591478788487692286863280473719308673
p = gcd(gift, n)

q = n//p

phi = (p-1)*(q-1)

d = pow(e, -1, phi)

flag = pow(c, d, n)

print(long_to_bytes(flag))
```