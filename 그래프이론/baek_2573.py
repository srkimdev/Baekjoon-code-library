from collections import deque
# import sys

# sys.getrecursionlimit(1000)
n, m = map(int, input().split())

ice = []
for i in range(n):
    ice.append(list(map(int, input().split())))

dx = [0, 1, 0, -1] #동남서북
dy = [1, 0, -1, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and ice[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
            
            if 0 <= nx < n and 0 <= ny < m and ice[nx][ny] == 0:
                count[x][y] += 1

year = 0

while True:
    area = 0
    visited = [[False] * m for _ in range(n)]
    count = [[0] * m for _ in range(n)]

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if ice[i][j] > 0 and not visited[i][j]:
                bfs(i, j)

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if count[i][j] > 0:
                ice[i][j] -= count[i][j]
                if ice[i][j] < 0:
                    ice[i][j] = 0

    visited = [[False] * m for _ in range(n)]

    for i in range(1, n - 1):
        for j in range(m):
            if ice[i][j] != 0 and not visited[i][j]:
                bfs(i, j)
                area += 1

    if area == 0:
        print(0)
        exit()

    year += 1
    if area >= 2:
        print(year)
        break
