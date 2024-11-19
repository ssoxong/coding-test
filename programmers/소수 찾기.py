from itertools import permutations

def isPrime(n):
    for i in range(2, n//2+1):
        if n%i==0: return False
    return True

def solution(numbers):
    ans = 0
    plist = set()
    for i in range(1, len(str(numbers))+1):
        pp = permutations(list(str(numbers)), i)
        for p in pp:
            while(len(p) and p[0]=='0'):
                p=p[1:]
            if len(p): plist.add(p)
    
    for p in plist:
        sp = "".join(p)
        if sp=="1": continue
        if isPrime(int(sp)): ans+=1
    return ans

print(solution("17"))