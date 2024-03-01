import sys
from collections import deque
input = sys.stdin.readline

queue = deque()
n = int(input())

for _ in range(n):
    command = input().strip()

    if 'push' in command:
        queue.append(command[5:])
    elif command == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif command == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
