from math import log2,floor,log
from numpy import  binary_repr
import matplotlib.pyplot as plt

def codifica_gamma(n):
    N=floor((log2(n)))
    b=binary_repr(n,width=N+1)
    r=('0'*N)+b
    return r

def codifica_delta(n):
    ris=''
    N=floor(log2(n))
    g=codifica_gamma(N+1)
    b=binary_repr(n)
    ris=((g)+b[1:])
    return ris

def decodifica_delta(x):
    x=str(x)
    ris=[]
    l=0
    for i in x:
        if i=='0':
            l=l+1
        else:
            n=int(x[(l): (l+1+l)],2)
            ris=int('1'+x[(l+l+1): l+l+1+n-1],2)
            break
    return ris

def lunghezza_media_delta(n):
    l_m=0
    s=0
    for i in range(1,n):
        N=floor(log2(i))
        s=(1+2*(floor(log2(N+1))))+N
        l_m+=s
    return l_m/n

n=int(input("Inserisci n "))
d={}
for i in range(1,n+1):
    d.__setitem__(i,codifica_delta(i))

for i in d:
     print("%s --> %s "  %(i,d[i]))

for i in d:
     print("%s --> %d "  %(d[i],decodifica_delta(d[i])))

lmg=[]
num=[]
for i in range(1,n+1):
    num.append(i)
    lmg.append(lunghezza_media_delta(i))

plt.figure(figsize=(14,10))
plt.plot(num,lmg)
plt.show()
