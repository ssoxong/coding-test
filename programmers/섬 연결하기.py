import heapq

parent = []
def find(n):
    if parent[n]!=n:
        parent[n] = find(parent[n])
    return parent[n]

def union(a, b):
    ap = find(a)
    bp = find(b)
    parent[bp] = ap

def solution(n, costs):
    global parent
    graph =[]
    parent = [x for x in range(0, n+1)]

    for s, e, w in costs:
        if s>e: tmp=s; s=e; e=tmp
        heapq.heappush(graph, (w, s, e))

    ans = 0
    cnt = 0
    while cnt<n-1:
        w, s, e = heapq.heappop(graph)

        # 부모 find 후 union
        if find(s)!=find(e):
            union(s, e)
            ans+=w
            cnt+=1
    
    return ans

print(solution(4, [(0, 1, 1), (0, 2, 2), (1, 2, 5), (1, 3, 1), (2, 3, 8)]))
