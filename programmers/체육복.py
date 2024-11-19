def solution(n, lost, reserve):
    cur = [1 for _ in range(n+1)]

    for r in reserve:
        cur[r]+=1
    for l in lost:
        cur[l]-=1
    
    print(cur)

    for i in range(1, len(cur)-1):
        print(cur)
        if cur[i]!=2: continue
        
        if cur[i-1]==0: cur[i-1]=1; cur[i]-=1
        elif cur[i+1]==0: cur[i+1]=1; cur[i]-=1
    
    if cur[-1]==2 and cur[-2]==0: cur[-2]=1

    return len([x for x in cur if x>0])-1

print(solution(5	,[2, 4],	[1, 3, 5]))