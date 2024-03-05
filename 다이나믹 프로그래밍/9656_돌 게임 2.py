import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)
dp[1] = 'SK'

for i in range(2, n + 1):
    if i % 2 == 0:
        dp[i] = 'CY'
    else:
        dp[i] = 'SK'

if dp[n] == 'CY':
    print('SK')
else:
    print('CY')
