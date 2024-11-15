import time

def solution(brown, yellow):
    i=2
    while(1):
        i+=1
        if (brown+yellow)%i!=0: continue
        if (((brown+yellow)//i)-2)*(i-2)!=yellow: continue
        return [(brown+yellow)//i, i]
        
    
print(solution(10,2))