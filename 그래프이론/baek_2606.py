from collections import deque

n = int(input())
m = int(input())

graph = [[0] * (n + 1) for i in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def bfs(v):
    queue = deque([v])
    visited[v] = 1

    while queue:
        v = queue.popleft()
        for i in range(1, n + 1):
            if graph[v][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1

bfs(1)
print(visited)
print(sum(visited))
