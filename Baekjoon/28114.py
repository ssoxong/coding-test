first = []
second = {}
for _ in range(3):
    p, y, s = input().split()
    p = int(p)

    first.append(int(y[2:]))
    second[int(p)]=s[:1]

first.sort()
sorted_projects = sorted(second.items(), reverse=True, key=lambda x: x[0])

# 결과 출력
print(''.join(map(str, first)))
print(''.join(status for _, status in sorted_projects))

