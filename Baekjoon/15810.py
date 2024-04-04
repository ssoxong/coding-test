n, m = map(int,input().split())
alist = list(map(int,input().split()))

def get(m):
    res = 0
    for i in range(n):
        res+=(m//alist[i])
    return res

ballon = 0
r = 1e12
while(ballon<r):
    i = (ballon+r)//2
    if get(i)>=m: r=i
    else: ballon=i+1

print(int(r))