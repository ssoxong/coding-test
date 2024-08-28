ans = 0
for i in range(3):
    s = input()
    try:
        ss = int(s)
        ans = ss+3-i
    except:
        pass

if ans%3==0 and ans%5==0:
    print("FizzBuzz")
elif ans%3==0 and not ans%5==0:
    print("Fizz")
elif not ans%3==0 and ans%5==0:
    print("Buzz")
else:
    print(ans)
