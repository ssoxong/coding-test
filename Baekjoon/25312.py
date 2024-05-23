n, m = map(int,input().split())
persugar = []
for i in range(n):
    a, b = map(int,input().split())
    persugar.append((a, b/a))
sugar = sorted(persugar, key=lambda x: (-x[1], -x[0]))
for s in sugar:
    if s<=m:
        

