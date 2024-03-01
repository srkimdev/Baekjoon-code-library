import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    command = input().rstrip()

    if 'push' in command:
        stack.append(int(command[5:]))
    elif command == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif command == 'size':
        print(len(stack))
    elif command == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command == 'empty':
        if stack:
            print(0)
        else:
            print(1)