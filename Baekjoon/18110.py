n = int(input())
score = []
if n==0: print(0); exit(0)

for _ in range(n):
    score.append(int(input()))

score.sort()

def _round(n):
    if n-int(n)>=0.5:
        return int(n)+1
    return int(n)


e = _round(n*0.15)
score = score[e:n-e]
ans=0
for s in score:
    ans+=s
print(_round(ans/len(score)))
