from math import floor, log2
from numpy import  binary_repr


def codifica_rice(x,k):
    ris=''
    q=floor((x-1)/(2**k))
    c_q='0'*q+'1'
    r=x-((2**k)*q)-1
    c_r=binary_repr(r,k)
    ris=c_q+c_r
    return ris

def decodifica_rice(s,k):
    q=0
    ris=0
    for i in range(len(s)):
        if (s[i]=='0'):
            q+=1
        else:
            r=int(s[i+1:len(s)],2)
            break
    ris=1+r+((2**k)*q)
    return ris

x=int(input("Inserisci x "))
k=int(input("Inserisci k "))

r={}
for i in range(1,x+1):
    c=codifica_rice(i,k)
    r.__setitem__(i,c)

for i in r:
     print("R_%d (%s) --> %s "  %(k,i,r[i]))

for i in r:
     print("%s --> %d "  %(r[i],decodifica_rice(r[i],k)))