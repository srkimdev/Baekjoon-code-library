from collections import deque

n = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []
max_height = 0
for _ in range(n):
    graph.append(list(map(int, input().split())))
    max_height = max(max_height, max(graph[-1]))

def bfs(a, b, height):
    queue = deque()
    queue.append((a, b))
    visited[a][b] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > height and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))

result = 0
for height in range(max_height):
    visited = [[0] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > height and visited[i][j] == 0:
                bfs(i, j, height)
                count += 1
    result = max(result, count)
print(result)