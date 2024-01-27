from collections import deque

def bfs(graph, a, b):
    queue = deque()
    queue.append((a, b))
    
    if graph[a][b] == 0:
        return False
    
    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))                            
    return True

t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())

    graph = [[0] * m for _ in range(n)]
    for i in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    result = 0
    for i in range(n):
        for j in range(m):
            if bfs(graph, i, j):
                result += 1

    print(result)
