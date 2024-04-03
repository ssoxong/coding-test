q, m = map(int,input().split())

fib = [0]*m
fib[0] = 1
fib[1] = 1
nlist = []

for _ in range(q):
    nlist.append(int(input()))

nlist.sort()
nmax = max(nlist)

for i in range(2, nmax+1):
    fib[i%m]=((fib[(i-1)%m]+fib[(i-2)%m])%m)
    if i in nlist:
        print(fib[(i%m)-1])
        nlist.pop(0)
