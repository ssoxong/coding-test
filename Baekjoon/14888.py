import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int,input().split()))
op = list(map(int,input().split()))

maximum, minimum = -1e9, 1e9

def dfs(depth, total, plus, minus, multiple, divide):
    global maximum, minimum
    if depth==N:
        maximum = max(maximum, total)
        minimum = min(minimum, total)
        return
    if plus:
        dfs(depth+1, total+num[depth], plus-1, minus, multiple, divide)
    if minus:
        dfs(depth+1, total-num[depth], plus, minus-1, multiple, divide)
    if multiple:
        dfs(depth+1, total*num[depth], plus, minus, multiple-1, divide)  
    if divide:
        dfs(depth+1, int(total/num[depth]), plus, minus, multiple, divide-1)          

dfs(1, num[0], op[0], op[1], op[2], op[3])

print(maximum)
print(minimum)