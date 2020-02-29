import fibo

print(fibo.createFib(20))
print(dir())

from collections import deque

queue = deque(['小青', '小红', '小皂'])
print(queue)
queue.append('小白')
print(queue.popleft())
print(queue)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print([[row[i] for row in matrix] for i in range(4)])


try:
    b = 0
    a = 1/b
except ZeroDivisionError:
    print("除数不能为0")


