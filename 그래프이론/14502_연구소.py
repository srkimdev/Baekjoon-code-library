from collections import deque
from itertools import combinations
from pprint import pprint

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

combi = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            combi.append([i, j])

combi3 = list(combinations(combi, 3))
total = []
result = 0

for i in combi3: # 리스트안에 튜플로 조합이 들어있음
    visited = [[False] * m for _ in range(n)]
    count = 0
    for j in i:
        x, y = j[0], j[1]
        visited[x][y] = True

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2 and not visited[i][j]:
                bfs(i, j)

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0 and not visited[i][j]:
                count += 1
    result = max(count, result)

print(result)