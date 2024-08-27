cnt = 0
ans = [0, 0] # white, blue
def solution(a, b, n, arr):
    global cnt
    start = arr[a][b]

    if n==1:
        ans[start]+=1
        return
    _bool = True
    for aa in range(a, a+n):
        for bb in range(b, b+n):
            if arr[aa][bb]!=start: _bool=False; break
    if _bool:
        ans[start]+=1
    else:
        solution(a, b, n//2, arr)
        solution(a, b+n//2, n//2, arr)
        solution(a+n//2, b, n//2, arr)
        solution(a+n//2, b+n//2, n//2, arr)

if __name__=="__main__":
    n = int(input())
    arr = [[]for _ in range(n)]
    for i in range(n):
        arr[i]=list(map(int,input().split()))
    solution(0, 0, n, arr)
    for a in ans:
        print(a)