from collections import deque

def bfs(x, y):
    visited[x][y] = True
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if graph[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

t = int(input())
for _ in range(t):

    n = int(input())

    visited = [[False] * n for _ in range(n)]
    graph = [[0] * n for _ in range(n)]

    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    
    ix, iy = map(int, input().split())
    fx, fy = map(int, input().split())

    bfs(ix, iy)

    print(graph[fx][fy])

