import math

n = int(input())
nlist = list(map(int,input().split()))
m = int(input())

nlist.sort()
if max(nlist)*n<=m:
    print(max(nlist))
    exit(0)

avg = sum(nlist)//n
if avg*n>m:
    avg = m//n

precha = -1
while (avg*n<m):
    print("avg", avg)
    cha = 0
    for n in nlist:
        if n>avg:
            cha+=avg-n
    print("cha", cha)
    if cha==0:
        print(avg)
        break
    else:
        if cha+n>m:
            print(avg)
            break
        else: 
            avg+=1

print("ans", avg)
    
        
        