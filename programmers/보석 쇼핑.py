def solution(gems):
    answer = [0,len(gems)]
    sgem = set(gems)
    gems = gems
    mmap = {gems[0]:1}
    start, end = 0,0

    while(end<len(gems)):
        if len(mmap)==len(sgem):
            if end-start<answer[1]-answer[0]: answer = [start, end]            
            mmap[gems[start]]-=1
            if mmap[gems[start]]==0: del mmap[gems[start]]
            start+=1

        else: 
            end+=1
            if end>=len(gems): continue
            if gems[end] not in mmap: mmap[gems[end]]=0
            mmap[gems[end]]+=1
    return [x+1 for x in answer]

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))