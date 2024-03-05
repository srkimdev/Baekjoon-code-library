import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    k = int(input())

    dp = [0] * (k + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, k + 1):
            dp[i] += dp[i - coin]
    
    print(dp[k])
    
