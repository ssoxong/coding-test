def gcd(a, b):
    if b:
        return gcd(b, a%b)
    else:
        return a
    
def lcm(a, b):
    return a//gcd(a,b)*b

a, b, l = map(int, input().split())
tmp = lcm(a,b)
if tmp==l:
    print("1")
elif l/tmp-l//tmp==0:
    for i in range(l//tmp, l+1, l//tmp):
        if lcm(i, tmp)==l:
            print(i)
            break
else:
    print("-1")
