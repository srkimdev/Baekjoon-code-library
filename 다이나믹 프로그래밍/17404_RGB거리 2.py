import sys
input = sys.stdin.readline

n = int(input())
INF = int(1e9)
ans = INF

house = []
for _ in range(n):
    house.append(list(map(int, input().split())))

for i in range(3):
    dp = [[0] * 3 for _ in range(n)]
    dp[0] = [INF, INF, INF]
    dp[0][i] = house[0][i]
    
    for j in range(1, n):
        dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + house[j][0]
        dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + house[j][1]
        dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + house[j][2]

    dp[n - 1][i] = INF
    ans = min(ans, min(dp[n - 1]))

print(ans)
    