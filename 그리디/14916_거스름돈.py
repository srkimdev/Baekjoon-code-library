import sys
input = sys.stdin.readline

n = int(input())

INF = int(1e9)
dp = [INF] * 100001

dp[2] = 1
dp[4] = 2
dp[5] = 1

for i in range(6, n + 1):
    dp[i] = min(dp[i - 5], dp[i - 2]) + 1

if dp[n] == INF:
    print(-1)
else:
    print(dp[n])


    