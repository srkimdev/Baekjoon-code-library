import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

max_dp = arr
min_dp = arr

for _ in range(n - 1):
    temp = list(map(int, input().split()))
    
    max_dp = [max(max_dp[0], max_dp[1]) + temp[0], max(max_dp) + temp[1], max(max_dp[1], max_dp[2]) + temp[2]]
    min_dp = [min(min_dp[0], min_dp[1]) + temp[0], min(min_dp) + temp[1], min(min_dp[1], min_dp[2]) + temp[2]]

print(max(max_dp), min(min_dp))

