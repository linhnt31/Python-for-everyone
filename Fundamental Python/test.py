from collections import deque

digits = [1, 2, 3, 4, 5]
n = len(digits)

res = [deque(digits) for _ in range(n)]

print(deque(map(lambda x: x[1].rotate(-x[0]), enumerate(res))))

print(res)