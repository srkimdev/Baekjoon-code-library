import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = set()
b = set()
result = []

for _ in range(n):
    a.add(input().strip())
for _ in range(m):
    b.add(input().strip())

for i in a:
    if i in b:
        result.append(i)

result.sort()
print(len(result))
for i in result:
    print(i)

