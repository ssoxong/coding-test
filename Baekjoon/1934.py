def gcd(a, b):
    if b:
        return gcd(b, a%b)
    else:
        return a
    
def lcm(a, b):
    return a//gcd(a,b)*b

t = int(input())
for _ in range(t):
    a, b = map(int,input().split())
    print(lcm(a,b))