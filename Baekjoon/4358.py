import math

def _round(n):
    n4 = float(f"{n:.4f}")
    n5 = float(f"{n:.5f}")
    if n5-n4>=0.00005:
        return n4+0.0001
    else:
        return n4
    
trees = []

while True:
    try:
        trees.append(input())
    except:
        break

dict = {}
for t in trees:
    if t in dict:
        dict[t]+=1
    else: dict[t]=1

total = len(trees)
sorted_d = sorted(dict)
for k in sorted_d:
    v = dict[k]
    print(k, f"{v/total*100:.4f}")