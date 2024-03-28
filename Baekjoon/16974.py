n, x = map(int,input().split())
layer = [0]*51
patty = [0]*51
layer[0] = 1
patty[0] = 1

for i in range(1, 51):
    layer[i] = layer[i-1]*2+3
    patty[i] = patty[i-1]*2+1

def f(n, x):
    if x==1:
        return 0
    elif x<1+layer[n-1]:
        return f(n-1, x-1) # 맨 아래 번 빼주기
    elif x==1+layer[n-1]:
        return patty[n-1]
    elif x==1+layer[n-1]+1:
        return patty[n-1]+1
    elif 1+layer[n-1]+1<x and x<1+layer[n-1]+1+layer[n-1]:
        return patty[n-1]+1+f(n-1, x-layer[n-1]-2)
    elif 1+layer[n-1]+1+layer[n-1]<=x and x<=layer[n]:
        return patty[n]
    
print(f(n,x))