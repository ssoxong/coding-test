t = list(map(int,input().split()))
st = sorted(t)
ts = sorted(t, reverse=True)
if t==st:
    print("ascending")
elif t==ts:
    print("descending")
else:
    print("mixed")