from collections import deque

ans = []
cnt = 0

def solution(n, k):
    global ans, cnt

    distance = [0]*(100001)
    q = deque()
    q.append(n)

    while q:
        nn = q.popleft()
        if nn==k:
            ans.append(distance[nn])
            break
    
        for nx in (nn-1, nn+1, nn*2):
            if 0<=nx<=100000 and not distance[nx]:
                distance[nx] = distance[nn]+1
                q.append(nx)

    print(min(ans))

if __name__ == "__main__":
    n, k = map(int,input().split())

    solution(n, k)