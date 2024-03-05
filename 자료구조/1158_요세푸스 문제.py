import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

queue = deque()
for i in range(1, n + 1):
    queue.append(i)
result = []

while queue:
    for _ in range(k - 1):
        queue.append(queue.popleft())

    result.append(queue.popleft())

print(str(result).replace('[', '<').replace(']', '>'))