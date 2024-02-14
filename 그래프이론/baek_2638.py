from collections import deque
from pprint import pprint

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    visited[nx][ny] = 2
                    continue
                visited[nx][ny] = 1
                queue.append((nx, ny))

result = 0
time = 0
before_cheeze = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            before_cheeze += 1

while True:
    visited = [[0] * m for _ in range(n)]
    time += 1
    cheeze = 0

    bfs(0, 0)
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 2:
                graph[i][j] = 0
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                cheeze += 1
    
    if cheeze == 0:
        break

    before_cheeze = cheeze
    
print(time)
print(before_cheeze)
    
    