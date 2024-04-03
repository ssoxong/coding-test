# 메모리초과
def sieve(b):
    for i in range(2, b+1):
        if check[i]: 
            continue
        for j in range(i*i, b+1, i):
            check[j] = True

n = int(input())
check=[False]*(n+1)
sieve(n)

ans=1
primes=[]
primes.append(2)
for i in range(3, n+1):
    if not check[i]:
        primes.append(i)   

for prime in primes:
    tmp = 1
    while tmp*prime<=n: tmp*=prime
    ans = (ans*tmp)%4294967296

print(ans)