def solution(begin, target, words):
    if target not in words: return 0
    visited = [0 for _ in range(len(words))]
    ans = []
    
    def dfs(cur, cnt):
        nonlocal target, words, visited
        if cur==target: 
            ans.append(cnt)
            return

        for i, w in enumerate(words):
            cha=0
            for a, b in zip(list(cur), list(w)):
                if a!=b: cha+=1
                if cha>1: break
            if cha==1 and not visited[i]:
                visited[i]=1
                dfs(w, cnt+1)
                visited[i]=0

    dfs(begin, 0)
    return min(ans)
        

print(solution("hit",	"cog"	,["hot", "dot", "dog", "lot", "log", "cog"]))