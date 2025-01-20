def solution(sticker):
    answer = 0
    tans = 0
    visited = []
    n = len(sticker)
    if n<=3: return max(sticker)

    def dp(i):
        nonlocal answer, tans
        visited[i] = 1
        visited[(i-1)%n] = -1
        visited[(i+1)%n] = -1
        tans += sticker[i]
        if 0 not in visited: 
            answer = max(answer, tans)
            tans-=sticker[i]
            return
        
        for j in range(n):
            if visited[j] != 0: continue
            if visited[(j+1)%n]==1 or visited[(j-1)%n]==1: continue
            dp(j)

        tans-=sticker[i]
        visited[i], visited[(i+1)%n], visited[(i-1)%n] = 0, 0, 0
    
    for i in range(len(sticker)):
        tans = 0
        visited = [0 for _ in range(len(sticker))]
        dp(i)
    return answer

print(solution([14, 6, 5, 11, 3, 9, 2, 10]	))