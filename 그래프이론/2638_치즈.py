#2:25

from collections import deque
from pprint import pprint

n, m = map(int, input().split())
cheeze = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
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

            if 0 <= nx < n and 0 <= ny < m and cheeze[nx][ny] == 1:
                visited[nx][ny] = True
                blank[nx][ny] += 1

            elif 0 <= nx < n and 0 <= ny < m and cheeze[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

time = 0     
while True:
    visited = [[False] * m for _ in range(n)]
    blank = [[0] * m for _ in range(n)]

    bfs(0, 0)

    for i in range(n):
        for j in range(m):
            if blank[i][j] >= 2:
                cheeze[i][j] -= blank[i][j]
                if cheeze[i][j] < 0:
                    cheeze[i][j] = 0
    
    time += 1

    if cheeze == [[0] * m for _ in range(n)]:
        print(time)
        break

