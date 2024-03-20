i = int(input())
b = (bin(i)[2:])[::-1]
for index, bb in enumerate(b):
    if bb=='1':
        print(index, end=" ")