from collections import Counter

def solution(n, results):
    score = [[0 for _ in range(n+1)]for _ in range(n+1)]
    for a, b in results:
        score[a][b]=1

    for s in score:
        print (s)
    ans=0
    for i in range(1, n+1):
        cnt = score[i].count(1)
        for j in range(1, n+1):
            cnt+=score[j][i]
        
        print(i, cnt)
        if cnt==n-1: ans+=1

    return ans


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	))