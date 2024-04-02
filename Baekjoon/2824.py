def gcd(a, b):
    while b:
        tmp = a
        a = b
        b = tmp%b
    return a

n1 = int(input())
list1 = list(map(int,input().split()))
n2 = int(input())
list2 = list(map(int,input().split()))

mul1 = 1
mul2 = 1
for l1 in list1:
    mul1*=l1

for l2 in list2:
    mul2*=l2

print(str(gcd(mul1,mul2))[-9:])
