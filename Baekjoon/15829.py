n = int(input())
str = input()
ans = 0
for i, s in enumerate(str):
    s = ord(s)-ord('a')+1
    ans+=s*(31**i)
print(ans%1234567891)
