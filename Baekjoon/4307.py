t = int(input())

for _ in range(t):
    bridge, n = map(int,input().split())
    minA = 0
    maxA = 0

    for _ in range(n):
        ant = int(input())
        minA = max(minA, min(bridge-ant, ant))
        maxA = max(maxA, max(bridge-ant, ant))

    print(minA, maxA)


 