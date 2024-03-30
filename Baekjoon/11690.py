def gcd(a, b):
    if b:
        return gcd(b, a%b)
    else:
        return a


nmax = 101010
check = [0]*nmax

for i in range(2, nmax):
    if check[i]: continue
    # prime.append(i)
    for j in range(i+i, nmax, i):
        check[j] = 1

klist = [0]*nmax
t = int(input())
for i in range(t):
    n = int(input())

    for k in range(1, n+1):
        tmp = k
        cnt=0
        if klist[k]: continue

        for j in range(1,k+1):
            if gcd(tmp, k-j)==1:
                tmp = tmp*(k-j)

                cnt+=1
                if cnt==k:
                    break
        klist[k] = max(tmp, klist[k-1])

    print(klist[n]%pow(2,32))