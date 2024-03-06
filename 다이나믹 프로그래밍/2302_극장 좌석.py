import sys
from math import prod
input = sys.stdin.readline

n = int(input())
m = int(input())

vip = [0]
for _ in range(m):
    vip.append(int(input()))

dp = [0] * (n + 1)
dp[0], dp[1] = 1, 1

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

result = 1
if m >= 1:
    for i in range(1, len(vip)):
        result *= dp[vip[i] - vip[i - 1] - 1]
    result *= dp[n - vip[-1]]
    print(result)

else:
    print(dp[n])
