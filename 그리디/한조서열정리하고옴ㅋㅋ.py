import sys
input = sys.stdin.readline
n = int(input())

mountain = list(map(int, input().split()))
count, mx = 0, 0
now = mountain[0]

for i in range(1, n):
    if now > mountain[i]:
        count += 1
        if i == n - 1:
            mx = max(count, mx)

    elif now < mountain[i]:
        mx = max(count, mx)
        count = 0
        now = mountain[i]

print(mx)
