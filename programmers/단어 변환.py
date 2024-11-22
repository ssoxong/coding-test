from collections import deque
def solution(begin, target, words):
    if target not in words: return 0

    q = deque([(begin, 0)])
    visited = [0 for _ in range(len(words))]
    while(q):
        cur, cnt = q.popleft()
        if cur==target:
            return cnt
        for i, w in enumerate(words):
            cha = 0
            for a, b in zip(list(cur), list(w)):
                if a!=b: cha+=1
            if cha==1:
                visited[i]=1
                q.append((w, cnt+1))

print(solution("hit",	"cog"	,["hot", "dot", "dog", "lot", "log"]))