m, n = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y):
    # 도착 지점
    if x == m - 1 and y == n - 1:
        return 1
    # 이미 방문한 곳
    if dp[x][y] != -1:
        return dp[x][y]

    # 낮은 값으로 이동하여 방문처리
    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n and board[nx][ny] < board[x][y]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]
            

print(dfs(0, 0))
