import sys
input = sys.stdin.readline

n = int(input())

elec = []
for _ in range(n):
    elec.append(list(map(int, input().split())))

elec.sort(key = lambda x : x[1])

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if elec[i][0] > elec[j][0]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
#1, 1, 2, 1, 2, 3, 4, 5

#마지막 전깃줄을 dp테이블 작성같은데?
#본인과 나중꺼에대한 최댓값 갱신
#맥스값을 구한후 전체 전깃줄에서 빼기
