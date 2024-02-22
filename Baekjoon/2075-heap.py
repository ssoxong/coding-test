import heapq

import sys
input = sys.stdin.readline
n = int(input())
heap = []

for _ in range(n):
    arr = map(int, input().split())
    for a in arr:
        if len(heap)<n:
            heapq.heappush(heap, a)
        elif heap[0]<a:
            heapq.heappop(heap)
            heapq.heappush(heap, a)

print(heap[0])
