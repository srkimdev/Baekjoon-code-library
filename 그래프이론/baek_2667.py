from collections import deque

def bfs(graph, a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(bfs(graph, i, j))

result.sort()
print(len(result))
for i in result:
    print(i)