import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 1
answer = 0

while end <= n and start <= end:
    
    total = sum(arr[start:end])

    if total == m:
        answer += 1
        end += 1

    elif total < m:
        end += 1
    
    else:
        start += 1

print(answer)