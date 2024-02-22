from collections import deque

m, n, k = map(int, input().split())

dot = [list(map(int, input().split())) for _ in range(k)]
board = [[0] * n for _ in range(m)]
visited = [[False] * n for _ in range(m)]

for i in dot: #i = [0, 2, 4, 4]
    for j in range(i[1], i[3]):
        for h in range(i[0], i[2]):
            board[j][h] = 1
            visited[j][h] = True

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    global result
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                result += 1
                visited[nx][ny] = True
                queue.append((nx, ny))

    return result

count = 0
area = []
for i in range(m):
    for j in range(n):
        if board[i][j] == 0 and not visited[i][j]:
            result = 1
            area.append(bfs(i, j))
            count += 1

area.sort()
print(count)
for i in area:
    print(i, end = ' ')
