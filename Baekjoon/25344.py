def gcd(a, b):
    if b:
        return gcd(b, a%b)
    else:
        return a
    
def lcm(a, b):
    return a//gcd(a,b)*b

n = int(input())
ans = list(map(int,input().split()))
t = ans[0]
for i in range(0, n-3):
    t = lcm(t, ans[i+1])

print(t)
