def add(a,b,c):
    return (a+b)%c

def mul(a,b,c):
    res = 0
    while b>0:
        if b%2==1:
            res = add(res, a, c)
        b//=2
        a = add(a, a, c)
    return res

def pow(a, b, c):
    res = 1
    while b>0:
        if b%2==1:
            res = mul(res, a, c)
        b//=2
        a = mul(a, a, c)
    return res

a, b, c = map(int,input().split())
print(pow(a,b,c))