def solution(begin, target, words):
    answer = 0
    # 변환할 수 없음
    if target not in words:
        return answer
    visited = [False for _ in range(len(words))]
    cnt = 0 
    ans = []
    
    def dfs(a,b):
        nonlocal cnt
        if a==b:
            ans.append(cnt)
            return
        
        for i, w in enumerate(words):
            if visited[i]: continue
            
            # 하나만 차이나는 워드로 변경
            diff=0
            for j in range(len(w)):
                if a[j]!=w[j]: diff+=1
                if diff>1: break
            if diff>1: continue
            
            visited[i]=True
            cnt+=1
            dfs(w, b)
            visited[i]=False
            cnt-=1
        
    dfs(begin, target)

    return min(ans)