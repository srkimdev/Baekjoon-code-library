import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

INF = int(1e9)
#벽을 깬 횟수 저장
dp = [[INF] * n for _ in range(n)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    dp[0][0] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            # 방문하지 않은칸에 대해서
            if dp[nx][ny] == INF:
                #흰방 이라면
                if graph[nx][ny] == 1:
                    dp[nx][ny] = dp[x][y]
                    queue.appendleft((nx, ny))
                #벽이 있다면
                else:
                    dp[nx][ny] = min(dp[nx][ny], dp[x][y] + 1)
                    queue.append((nx, ny))

bfs(0, 0)
print(dp[n - 1][n - 1])
