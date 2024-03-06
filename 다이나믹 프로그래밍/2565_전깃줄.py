import sys
input = sys.stdin.readline

n = int(input())

elec = []
for _ in range(n):
    elec.append(list(map(int, input().split())))

elec.sort(key = lambda x : x[1])

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if elec[i][0] > elec[j][0]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
