import sys
input = sys.stdin.readline

k = int(input())
dp = [[0] * (k + 1) for _ in range(k + 1)]
dp[0][0] = 1 # A의 개수
dp[1][0] = 0 # B의 개수

for i in range(1, k + 1):
    dp[0][i] = dp[1][i - 1]
    dp[1][i] = dp[1][i - 1] + dp[0][i - 1]

print(dp[0][k], dp[1][k])