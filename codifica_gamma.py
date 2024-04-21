from math import log2,floor
from numpy import  binary_repr
import matplotlib.pyplot as plt

def codifica_gamma(n):
    r=''
    N=floor((log2(n)))
    b=binary_repr(n,width=N+1)
    r=(('0'*N)+b)
    return r

def codifica_binaria(n):
    b=binary_repr(n)
    return b

def lunghezza_media_gamma(n):
    l_m=0
    for i in range(1,n+1):
        s=((2*(floor(log2(i))))+1)
        l_m=l_m+s
    l_m=l_m/n
    return l_m

def lunghezza_media_binaria(n):
    ris=(n*(1+floor(log2(n))))/n
    return ris

def decodifca_gamma(n):
    i=0
    for x in n:
        if x=='0':
            i=i+1
        else:
            aus=n[i:]
            ris=int(aus,2)
            break
    return ris

def print_codifica(d):
    for i in d:
        print("%s : %s "  %(i,d[i]))


n=int(input('Inserisci n '))
g={}
b={}
for i in range(1,n+1):
    g.__setitem__(i,codifica_gamma(i))
    b.__setitem__(i,codifica_binaria(i))

print("Codifica Gamma")
print_codifica(g)
print("Codifica Beta")
print_codifica(b)

num=[]
rapp=[]
for i in range(1,n+1):
    lmg=lunghezza_media_gamma(i)
    num.append(i)
    lmb=lunghezza_media_binaria(i)
    print(lmg)
    print(lmb)
    print(lmg/lmb)
    rapp.append(lmg/lmb)

plt.figure(figsize=(14,10))
plt.plot(num,rapp)
plt.show()

