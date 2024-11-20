cnt = 0

def dfs(i, cur, numbers, t):
    global cnt
    # print(i, cur, op)
    if i==len(numbers): 
        if cur==t: cnt+=1
        return

    dfs(i+1, cur+numbers[i], numbers, t)
    dfs(i+1, cur-numbers[i], numbers, t)

def solution(numbers, target):
    global cnt
    dfs(0, 0, numbers, target)

    return cnt

print(solution([4, 1, 2, 1]	,4))