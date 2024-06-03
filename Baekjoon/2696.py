import heapq

t = int(input())
for _ in range(t):
    m = int(input())
    arr = list(map(int,input().split()))
    minh = []
    maxh = []
    heapq.heappush(minh, arr[0])
    heapq.heappush(maxh, arr[0])
    print(arr[0])

    for a in arr[1:]:
        heapq.heappush(minh, a)
        heapq.heappush(maxh, a)
        print()
    