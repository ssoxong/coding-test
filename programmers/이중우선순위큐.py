import heapq

def solution(operations):
    h = []
    for o in operations:
        so = o.split()
        if so[0] == 'I':
            heapq.heappush(h, int(so[1]))
        elif o == "D 1":
            if not len(h): continue
            h = heapq.nlargest(len(h), h)[1:]
            heapq.heapify(h)
        else:
            if not len(h): continue
            heapq.heappop(h)

    if not len(h): heapq.heappush(h, 0)
    h.sort()
    return [h[-1], h[0]]

print(solution(["I -45","I -45","I -45", "D 1", "D -1"]))