import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def backtracking(arr, start, n, m):
    if len(arr)==m:
        print(' '.join(map(str, arr)))
        return
    for i in range(start, n+1):
        if i not in arr:
            arr.append(i)
            backtracking(arr, i+1, n, m)
            arr.pop()

backtracking([], 1, n, m)