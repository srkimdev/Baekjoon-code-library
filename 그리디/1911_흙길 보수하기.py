import sys
input = sys.stdin.readline

n, l = map(int, input().split())
hole = [list(map(int, input().split())) for _ in range(n)]

hole.sort(key = lambda x: x[0])

cur, count = 0, 0
for start, end in hole:
    if start > end:
        continue
    if cur > start:
        start = cur
    while start < end:
        start += l
        count += 1
    cur = start

print(count)