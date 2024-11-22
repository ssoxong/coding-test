from itertools import product
def solution(n, m):
    arr = []
    def bt(arr, j):
        # nonlocal arr
        if len(arr)==m:
            print(" ".join(map(str,arr)))
            return
        
        for i in range(j, n+1):
            bt(arr+[i], i)
    bt(arr, 1)


n, k = map(int, input().split())
solution(n, k)