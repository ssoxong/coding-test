from collections import deque

# deque에 튜플 삽입
dq = deque()

# 튜플 데이터 추가
dq.append(("a", "b"))
dq.append(("b", "x"))

# deque 출력
print(dq)

# 튜플 데이터 접근
while dq:
    item = dq.popleft()
    print(item)  # 튜플 자체 출력
    print(item[0], item[1])  # 튜플 내부 데이터 접근
