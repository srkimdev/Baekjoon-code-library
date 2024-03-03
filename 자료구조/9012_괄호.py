import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    stack = []
    s = input().strip()

    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break

    else:
        if not stack:
            print('YES')
        else:
            print('NO')
    