from collections import deque

n = int(input())

graph = []
for i in range(n):
    graph.append(list(input()))

visited = [[False] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(color, x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if graph[nx][ny] == color and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx, ny))

colors = ['R', 'G', 'B']

count1, count2 = 0, 0

for color in colors:
    for i in range(n):
        for j in range(n):
            if graph[i][j] == color and visited[i][j] == False:
                bfs(color, i, j)
                count1 += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[False] * n for _ in range(n)]

for color in ['R', 'B']:
    for i in range(n):
        for j in range(n):
            if graph[i][j] == color and visited[i][j] == False:
                bfs(color, i, j)
                count2 += 1

print(count1, count2)



