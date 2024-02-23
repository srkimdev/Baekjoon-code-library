from collections import deque

m, n = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# 벽을 깬 횟수 저장
dp = [[-1] * m for _ in range(n)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    dp[0][0] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 방문 안한것에 대해서
            if dp[nx][ny] == -1:
                #벽이 있다면
                if board[nx][ny] == 0:
                    dp[nx][ny] = dp[x][y]
                    queue.appendleft((nx, ny)) #우선적으로 0을 탐색
                else:
                    dp[nx][ny] = dp[x][y] + 1
                    queue.append((nx, ny))

bfs(0, 0)
print(dp[n - 1][m - 1])
