import sys
input = sys.stdin.readline
n = int(input())

cnt = 0
chess=[0]*n

def promising(y):  
    global chess  
    for i in range(y):
        if chess[i]==chess[y] or abs(y-i)==abs(chess[y]-chess[i]):
            return False
    return True
    
def dfs(y):
    global cnt, n, chess
    if y==n:
        cnt+=1
        return
    
    for i in range(n):
        chess[y]=i
        if not promising(y): continue
        dfs(y+1)

dfs(0)
print(cnt)
