import matplotlib.pyplot as plt
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
    

n=int(input("Inserisci n "))
fib = [0 for i in range(n)]
num = [i for i in range(1,n+1)]
f={}
l=[]
for i in range(1,n+1):
    c=codifica_fibonacci(i)
    l.append(len(c))
    f.__setitem__(i,c)

for i in f:
     print("%s --> %s "  %(i,f[i]))

