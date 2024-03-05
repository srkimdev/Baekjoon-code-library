import sys
input = sys.stdin.readline

d, k = map(int, input().split())

for i in range(1, 100000):
    for j in range(i, 100000):
        dp = [0] * (d + 1)
        dp[1] = i
        dp[2] = j

        for l in range(3, d + 1):
            dp[l] = dp[l - 2] + dp[l - 1]
        
        if dp[d] == k:
            print(i)
            print(j)
            exit()
