n, a, b = map(int,input().split())
if(b-n>a-n):
    print("Bus")
elif (b-n==a-n):
    print("Anything")
else:
    print("Subway")