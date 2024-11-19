def solution(people, limit):
    people.sort()
    
    cnt = 0
    i, j = 0, len(people)-1

    while(1):
        if i>=j:
            break
        
        if people[i]+people[j]>limit:
            j-=1
            continue

        cnt+=1
        i+=1
        j-=1

    return cnt+(len(people)//2-cnt)*2+len(people)%2

print(solution([100,100,50,20,50,20],	100))