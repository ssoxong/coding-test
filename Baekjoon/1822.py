na, nb = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

cha = set(a)-set(b)
print(len(cha))
chal = list(cha)
chal.sort()
print(*chal)
