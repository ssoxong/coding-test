import math
import sys
data = sys.stdin.read().split()
index=0
t = data[index]
index+=1

for _ in range(t):
    n = data[index]
    index+=1
    d = [[]]
    x=[0]*(n+1)
    y=[0]*(n+1)

    def dist(i, j):
        distance = math.sqrt((x[j] - x[i])**2 + (y[j] - y[i])**2)
        return distance

    def func(i, j):
        res = d[i][j]
        
        if res>=0: return res
        if i==n: return dist(j, n)
        if j==n: return dist(i, n)
        k = max(i, j)+1
        return min(func(k, j)+dist(i, k), func(i, k)+dist(j, k))
    
    d = [[-1 for _ in range(n+1)]for _ in range(n+1)]

    for i in range(1, n+1):
        x[i], y[i] = data[index],data[index+1]
        index+=2
        
    print(func(1,1))