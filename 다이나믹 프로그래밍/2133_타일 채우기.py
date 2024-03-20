import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)

if n >= 2:
    dp[2] = 3

if n >= 4:
    dp[4] = 11

    for i in range(5, n + 1):
        dp[i] = dp[i - 2] * 3
        if i % 2 == 0:
            for j in range(0, i - 2, 2):
                dp[i] += 2 * dp[j]

            dp[i] += 2

print(dp[n])