from pprint import pprint
from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
queue = deque([[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]])

for _ in range(m):
    d, s = map(int, input().split())
    cloud = [[False] * n for _ in range(n)]

    for _ in range(len(queue)):
        x, y = queue.popleft()
        nx = (s * dx[d - 1] + x) % n #-4 
        ny = (s * dy[d - 1] + y) % n #4
        graph[nx][ny] += 1
        cloud[nx][ny] = True
        queue.append([nx, ny])

    for _ in range(len(queue)):
        x, y = queue.popleft()
        for i in range(1, 8, 2):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] != 0:
                graph[x][y] += 1

    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 2 and cloud[i][j] == False:
                graph[i][j] -= 2
                queue.append([i, j])
total = 0
for i in range(n):
    for j in range(n):
        total += graph[i][j]
print(total)
    
