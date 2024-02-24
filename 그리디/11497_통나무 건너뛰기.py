import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    wood = list(map(int, input().split()))
    wood.sort(reverse = True)

    arrange = deque()
    for i in range(n):
        if i % 2 == 0:
            arrange.append(wood[i])
        else:
            arrange.appendleft(wood[i])

    mx = 0
    for i in range(1, n):
        if abs(arrange[i]- arrange[i - 1]) > mx:
            mx = abs(arrange[i]- arrange[i - 1])
    
    print(mx)