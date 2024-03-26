import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())

answer = 0
start, end = 0, n - 1
while start < end:
    temp = arr[start] + arr[end]
    if temp == x:
        answer += 1
        start += 1
    
    elif temp < x:
        start += 1
    
    else:
        end -= 1

print(answer)