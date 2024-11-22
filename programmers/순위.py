from collections import Counter

def solution(n, results):
    score = [set()for _ in range(n+1)]
    for w, l in results:
        score[w].add(l)
    for i in range(1, n+1):
        for s in score:
            ss=list(s)
            for j in range(len(ss)):
                s.update(score[ss[j]])
                
    cnt = [0]*(n+1)
    
    for i,s in enumerate(score):
        for ss in s:
            cnt[ss]+=1
        cnt[i]+=len(s)

    return cnt.count(n-1)


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	))