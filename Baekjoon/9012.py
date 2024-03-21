import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    ans = 0

    s = input()
    for i in range(len(s)):
        if s[i]=='(':
            ans+=1
        elif s[i]==')':
            ans-=1

        if ans<0:
            break
    
    if ans!=0:
        print("NO")
    else:
        print("YES")