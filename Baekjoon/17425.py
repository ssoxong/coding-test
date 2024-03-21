import sys
input = sys.stdin.readline

# f(a) = a약수 합
# g(a) = a보다 같거나 작은 자연수들의 f(n) 합
MAX = 1000000

t = int(input())

f = [0]*(MAX+1)
g = [0]*(MAX+1)

for i in range(1, MAX+1):
    j=1
    while i*j<=MAX:
        f[i*j]+=i
        j+=1
    
    g[i] = g[i-1]+f[i]

for _ in range(t):
    x = int(input())
    print(g[x])