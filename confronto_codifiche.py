"""
Confronto tra le codifiche: binaria, gammma, delta e Fibonacci
"""


import matplotlib.pyplot as plt
from math import log2,floor
fib=[]
# Ritorna l'indice del più grande numero di fibonacci < n 
def fibonacci(n):
    fib[0]=1
    fib[1]=2
    i=2
    while (fib[i-1]<=n):
        fib[i]=fib[i-1]+fib[i-2]
        i=i+1
    return (i-2)

def codifica_fibonacci(n):
    i=fibonacci(n)
    ris = ['-' for j in range(i + 2)]
    j=i
    while (n):
        ris[j]='1'
        n=n-fib[j]
        j=j-1
        while (j >= 0 and fib[j] > n):
            ris[j]='0'
            j=j-1
    ris[i+1]='1'
    return "".join(ris)

def lunghezza_cod_bin(n):
     l=[]
     for i in range(1,n+1):
          l.append(((1+floor(log2(i)))))
     return l

def lunghezza_cod_gamma(n):
    l=[]
    for i in range(1,n+1):
          l.append((2*(floor(log2(i))))+1)
    return l

def lunghezza_cod_delta(n):
    l=[]
    for i in range(1,n+1):
          N=floor(log2(i))
          l.append((1+2*(floor(log2(N+1))))+N)
    return l


n=int(input("Inserisci n "))
fib = [0 for i in range(n)]
num = [i for i in range(1,n+1)]
f={}
l_f=[]

for i in range(1,n+1):
    c=codifica_fibonacci(i)
    l_f.append(len(c))
    f.__setitem__(i,c)
"""
for i in f:
     print("%s --> %s "  %(i,f[i]))
"""
l_b=lunghezza_cod_bin(n)
l_g=lunghezza_cod_gamma(n)
l_d=lunghezza_cod_delta(n)

plt.figure(figsize=(14, 10))
plt.plot(num, l_f,'r',label="Codifica di Fibonacci")
plt.plot(num, l_b,'b',label="Codifica Binaria")
plt.plot(num, l_g,'g',label="Codifica Gamma")
plt.plot(num, l_d,'y',label="Codifica Delta")
legend = plt.legend(loc='lower right', shadow=True, fontsize='x-large')
plt.show()

