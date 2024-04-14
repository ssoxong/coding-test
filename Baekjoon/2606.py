def graph(start):
    global cnt
    visited[start]=True
    cnt+=1
    for a in nlist[start]:
        if visited[a]:
            continue
        graph(a)

        


cpu = int(input())
n = int(input())
nlist = [[]*(cpu+1) for _ in range(cpu+1)]
visited = [False]*(cpu+1)

for _ in range(n):
    x, y = map(int, input().split())
    nlist[x].append(y)
    nlist[y].append(x)

cnt = 0
graph(1)
print(cnt-1)
