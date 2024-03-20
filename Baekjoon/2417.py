import math

i = int(input())
s = math.sqrt(i)
if int(s)**2>=i:
    print(int(s))
else:
    print(int(s)+1)
