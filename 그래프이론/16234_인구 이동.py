from collections import deque

n, l, r = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
day = 0

def bfs(x, y):
    queue = deque()
    union = []
    union.append((x, y))
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if l <= abs(graph[x][y] - graph[nx][ny]) <= r and visited[nx][ny] == 0: 
                visited[nx][ny] = 1
                queue.append((nx, ny))
                union.append((nx, ny))
    return union

while True:
    flag = 0
    visited = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                union = bfs(i, j)

                if len(union) > 1:
                    flag = 1
                    people = sum(graph[x][y] for x, y in union) // len(union)

                    for x, y in union:
                        graph[x][y] = people

    if flag == 0:
        print(day)
        break

    day += 1