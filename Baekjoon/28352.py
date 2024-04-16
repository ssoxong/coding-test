n = int(input())
x = 7*24*60*60
ans = 1

for i in range(1, n+1):
    ans*=i
    
print(ans//x)