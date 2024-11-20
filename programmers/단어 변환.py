from collections import deque
def solution(begin, target, words):
    if target not in words: return 0
    
    q = deque([(-1,0)])
    visited = [False]*len(words)
    while(q):
        i, cnt = q.popleft()
        if i!=-1: 
            begin = words[i]
        
        # print(begin)

        if begin==target:
            return cnt

        for j, word in enumerate(words):
            oneDiff = False
            for k in range(len(target)):
                b = begin[k]
                w = word[k]
                # print(b,w)

                if b!=w: 
                    if oneDiff: oneDiff=False; break
                    oneDiff=True

            if oneDiff and not visited[j]:
                # print(begin, word)
                visited[j]=True
                q.append((j,cnt+1))

        if i==-1: continue

print(solution("hit",	"cog"	,["hot", "dot", "dog", "lot", "log", "cog"]))