import sys
input = sys.stdin.readline
n, m =  map(int, input().split())

day=[31,28,31,30,31,30,31,31,30,31,30,31]
date = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
sum = 0

for i in range(n-1):
    sum+=day[i]
sum+=m

if sum<=7:
    print(date[sum-1])
else:
    print(date[sum%7-1])