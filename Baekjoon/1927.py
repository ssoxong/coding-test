import heapq
import sys
input = sys.stdin.readline

n = int(input())
q=[]
for _ in range(n):
    x = int(input())
    if x==0:
        if not len(q): print(0)
        else: print(heapq.heappop(q))
    else:
        heapq.heappush(q, x)

