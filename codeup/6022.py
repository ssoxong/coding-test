a = input()
for i in range(len(a)):
    print(a[i], end='')
    if i%2!=0:
        print(" ", end='')