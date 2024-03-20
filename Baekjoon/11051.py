n, k = map(int,input().split())
# n!/k!(n-k)!

mul = 1
for i in range(n-k+1, n+1):
    mul*=i

bmul = 1
for i in range(1, k+1):
    bmul*=i

print((int)(mul/bmul)%10007)