# 2:35

import sys
from collections import deque
input = sys.stdin.readline

n, q = map(int, input().split())

len_graph = 2 ** n
graph = []
for _ in range(len_graph):
    graph.append(list(map(int, input().split())))

L = list(map(int, input().split()))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def rotate(graph, len_graph, l):
    
    new_graph = [[0] * (len_graph) for _ in range(len_graph)]

    r_size = 2 ** l
    for x in range(0, len_graph, r_size):
        for y in range(0, len_graph, r_size):
            for i in range(r_size):
                for j in range(r_size):
                    new_graph[x + j][y + r_size - i - 1] = graph[x + i][y + j]
    graph = new_graph
    return graph

def melt_ice(x, y, ice_count):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= len_graph or ny < 0 or ny >= len_graph:
            ice_count += 1

        if 0 <= nx < len_graph and 0 <= ny < len_graph and graph[nx][ny] == 0:
            ice_count += 1

    return ice_count

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    area = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len_graph and 0 <= ny < len_graph and not visited[nx][ny] and graph[nx][ny] > 0:
                area += 1
                visited[nx][ny] = True
                queue.append((nx, ny))
    return area

melting_list = []
for l in L:
    visited = [[0] * len_graph for _ in range(len_graph)]
    graph = rotate(graph, len_graph, l)

    for i in range(len_graph):
        for j in range(len_graph):
            ice_count = 0
            if graph[i][j] > 0:
                if melt_ice(i, j, ice_count) >= 2:
                    melting_list.append([i, j])

    for x, y in melting_list:
        graph[x][y] -= 1
        if graph[x][y] < 0:
            graph[x][y] = 0

    melting_list.clear()

result = 0
for i in range(len_graph):
    result += sum(graph[i])

visited = [[False] * len_graph for _ in range(len_graph)]

area = 0
for i in range(len_graph):
    for j in range(len_graph):
        if graph[i][j] > 0 and not visited[i][j]:
            area = max(area, bfs(i, j))

print(result)
print(area)



