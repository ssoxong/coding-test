def gcd(a, b):
    if b:
        return gcd(b, a%b)
    else:
        return a

sp=[0]*1010101010
def sieve(n):
    for i in range(2, n+1):
        if sp[i]: continue
        sp[i] = i
        for j in range(i+i, n+1, i):
            if not sp[j]:
                sp[j]=i
    

sieve(1000000000)
n = int(input())

xlist = list(map(int,input().split()))

for i in range(1,n+1):
    x=xlist[i-1]
    while x>1:
        print(sp[x], end=" ")
        x//=sp[x]
    print()