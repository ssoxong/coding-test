a,b=map(int, input().split())

result=0

result+=abs(a-b)//10
c=abs(a-b)%10

if(c==1 or c==5): result+=1
elif(c==2 or c==4 or c==6 or c==9): result+=2
elif(c==3 or c==7 or c==8): result+=3

print(result)