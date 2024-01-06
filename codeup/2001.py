
pasta = [int(input()) for _ in range(3)]
juice = [int(input()) for _ in range(2)]

print("{:.1f}".format((min(pasta)+min(juice))*1.1))
