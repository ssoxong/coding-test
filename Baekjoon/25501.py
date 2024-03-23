def recursion(s, l, r):
    global ans
    ans+=1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)


t = int(input())
for _ in range(t):
    s = input()
    ans = 0
    print(isPalindrome(s), ans)