n = int(input())
cost = [0] + list(map(int, input().split()))

d = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, i + 1):
        d[i] = max(d[i], d[i - j] + cost[j])

print(d[n])