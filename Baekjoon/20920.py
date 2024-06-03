import sys
input = sys.stdin.readline
n, m = map(int,input().rstrip().split())
map = {}

for _ in range(n):
    w = input().rstrip()
    if len(w)<m: continue

    if w in map:
        map[w]+=1
    else:
        map[w] = 1

map = sorted(map.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for m in map:
    print(m[0])
