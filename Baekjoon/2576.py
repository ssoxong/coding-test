from collections import deque
cnt = 0

def solution(arr):
    global cnt
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()

    # 익지 않은 토마토 개수
    zero=0
    for a in arr:
        zero += a.count(0)
    if zero==0: return  
    
    for y in range(0, len(arr)):
        for x in range(0, len(arr[0])):
            if arr[y][x]!=1: continue
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<len(arr[0]) and 0<=ny<len(arr) and arr[ny][nx]==0:
                    q.append((nx, ny))
                    arr[ny][nx]=2
    
    cnt+=1
    for nx, ny in q:
        arr[ny][nx]=1
    zero-=len(q)

    while True:
        # 익지 않은 토마토 없음
        if zero==0: break  
        # 익을 수 없는 토마토 없음
        if len(q)==0: cnt=-1; break
        
        # 유망한 노드 next_q에 집어넣기
        next_q = deque()
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<len(arr[0]) and 0<=ny<len(arr) and arr[ny][nx]==0:
                    next_q.append((nx, ny))
                    arr[ny][nx]=2
        q = next_q
        # 하루 지남
        cnt+=1

        # 유망한 토마토 전부 익음
        for nx, ny in q:
            arr[ny][nx]=1
        zero-=len(q)


if __name__=="__main__":
    m, n = map(int,input().split())
    arr = [[]for _ in range(n)]
    for i in range(n):
        arr[i]=list(map(int,input().split()))
    solution(arr)
    print(cnt)