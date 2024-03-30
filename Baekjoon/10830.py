def mul(a, b):
    n = len(a)
    c=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] = (c[i][j]+a[i][k]*b[k][j])%1000

    return c

def pow(a, b):
    n = len(a)
    res=[[0]*n for _ in range(n)]
    for i in range(n):
        res[i][i] = 1
    while b>0:
        if b%2==1:
            res = mul(res, a)
        b//=2
        a = mul(a, a)
    return res

n, b = map(int,input().split())
a=[[0]*n for _ in range(n)]
for i in range(n):
    a[i] = list(map(int,input().split()))

ans = pow(a, b)
for an in ans:
    print(*an)