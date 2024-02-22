n = int(input())

dp = [5001] * (n + 1)
bag = [3, 5]

dp [0] = 0
for j in bag:
    for i in range(1, n + 1):
        if dp[i - j] != 5001:
            dp[i] = min(dp[i], dp[i - j] + 1)

if dp[n] == 5001:
    print(-1)
else:
    print(dp[n])