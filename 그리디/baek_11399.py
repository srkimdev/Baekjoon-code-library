n = int(input())

p = list(map(int, input().split()))
p.sort()

result = 0
for i in range(1, len(p) + 1):
    for j in range(i):
        result += p[j]

print(result)

