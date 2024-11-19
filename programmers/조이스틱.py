ans = []
def dfs(s, e, cnt, name, need, N):
    ss = s

    # 이동 count
    go = 0
    if s<e: go = min(e-s, N-e+s)
    elif s>e: go = min(s-e, N-s+e)
     
    s = e

    # 변환 검사
    change = min(ord(name[s])-ord('A'), ord('Z')-ord(name[s])+1)
    
    if len(need)==0:
        ans.append(cnt+go+change)
        return

    # 다른 노드 탐색
    for e in [need[0], need[-1]]:        
        if need[0]==e: dfs(s, e, cnt+go+change, name, need[1:], N)
        else: dfs(s, e, cnt+go+change, name, need[:-1], N)

    return s

def solution(name):
    nlist = list(name)
    need = []
    for i, n in enumerate(nlist):
        if n != 'A': need.append(i)
    s=0
    cnt = 0
    N = len(nlist)

    # 첫번째는 그냥 처리
    if len(nlist)==1:
        return min(ord(name[s])-ord('A'), ord('Z')-ord(name[s])+1)

    if not len(need): return 0

    for e in [need[0], need[-1]]:        
        if need[0]==e: dfs(s, e, cnt, name, need[1:], N)
        else: dfs(s, e, cnt, name, need[:-1], N)

    return min(ans)

print(solution("ABBAAABAAAABB"))
# print(solution("AAAAAA"))
