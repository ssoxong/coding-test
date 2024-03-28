n, k = map(int,input().split())
# n!/k!(n-k)!

c=[[0]*1010 for _ in range(1010)]
c[0][0]=1

for i in range(1, n+1):
    c[i][0]=1
    for j in range(1, i+1):
        c[i][j] = c[i-1][j]+c[i-1][j-1]
        if c[i][j]>=10007:
            c[i][j] -= 10007

print(c[n][k])