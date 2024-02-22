import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def backtracking(arr, n, m):
    if len(arr)==m:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, n+1):
        if i not in arr:
            arr.append(i)
            backtracking(arr, n, m)
            arr.pop()

backtracking([], n, m)