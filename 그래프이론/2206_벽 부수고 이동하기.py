from collections import deque

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input())))

#visited[x][y][0]은 벽파괴 가능, visited[x][y][1]은 벽파괴 불가능
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))

    while queue:
        x, y, z = queue.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if board[nx][ny] == 1 and z == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append((nx, ny, 1))

            elif board[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))

    return - 1
print(bfs(0, 0, 0))
