from math import prod
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

array = [int(input()) for _ in range(n)]
array.sort()
queue = deque(array)
minus = []
temp = []

result = 0
for _ in range(n):
    x = queue.pop()
    if x <= 0:
        minus.append(x)
    elif x == 1:
        result += x
    else:
        temp.append(x)

    if len(temp) == 2:
        result += prod(temp)
        temp.clear()

if temp:
    result += temp.pop()

minus.sort(reverse = True)
for _ in range(len(minus)):
    x = minus.pop()
    temp.append(x)

    if len(temp) == 2:
        result += prod(temp)
        temp.clear()

if temp:
    result += temp.pop()

print(result)