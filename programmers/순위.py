from collections import Counter

def solution(n, results):
    score = [[0 for _ in range(n+1)]for _ in range(n+1)]
    for a, b in results:
        score[a][b]=1
        score[b][a]=-1

    answer = 0
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if score[i][j]!=0: continue
                if score[i][k]==1 and score[k][j]==1:
                    score[i][j] = 1
                if score[i][k]==-1 and score[k][j]==-1:
                    score[i][j] = -1
    for s in score:
        if Counter(s)[0]==2:
            answer+=1

    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	))