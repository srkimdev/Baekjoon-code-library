import sys
input = sys.stdin.readline

r, c = map(int, input().split())
graph = []
for i in range(r):
    graph.append(list(input().strip()))

visited = [[False] * c for _ in range(r)]
dx = [-1, 0, 1]

def dfs(x, y):
    if y == c - 1:
        return True

    for i in range(3):
        nx = x + dx[i]
        ny = y + 1

        if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and graph[nx][ny] == '.':
            visited[nx][ny] = True
            if dfs(nx, ny):
                return True
    return False

route = 0
for i in range(r):
    if dfs(i, 0):
        route += 1

print(route)