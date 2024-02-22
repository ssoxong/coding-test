import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []
heapq.heapify(heap)
for _ in range(n):
    x = int(input())
    if(x==0):
        if(heap):
            print(-heapq.heappop(heap))
        else:
            print(0)
    else: 
        heapq.heappush(heap, -x)

    