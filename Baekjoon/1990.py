check = [0]*10000001
primes = []

def sieve(b):
    for i in range(2, b+1):
        if check[i]: 
            continue
        primes.append(i)
        for j in range(i+i, b+1, i):
            check[j] = 1 
sieve(10000000)
a, b = map(int,input().split())

for p in primes:
    if p<a: continue
    if p>b: break

    strp = str(p)
    if len(strp)==1 and p>=a:
        print(p)
        continue

    for i in range(len(strp)//2):
        if strp[i]!=strp[-i-1]:
            break
        if i==len(strp)//2-1:
            print(p)

print("-1")
