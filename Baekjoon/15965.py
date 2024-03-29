check = [0]*8080808
primes = []

def sieve(n):
    for i in range(2, n+1):
        if check[i]: 
            continue
        primes.append(i)
        for j in range(i+i, n+1, i):
            check[j] = 1 

sieve(8000000)
k = int(input())
print(primes[k-1])