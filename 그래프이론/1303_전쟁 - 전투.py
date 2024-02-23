from collections import deque

n, m = map(int, input().split())

people = []
for _ in range(m):
    people.append(list(map(str, input())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y, color):
    global man
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and people[nx][ny] == color:
                visited[nx][ny] = True
                man += 1
                queue.append((nx, ny))

visited = [[False] * n for _ in range(m)]
army, enemy = 0, 0

for i in range(m):
    for j in range(n):
        man = 1
        if people[i][j] == 'W' and not visited[i][j]:
            bfs(i, j, 'W')
            army += man ** 2

        elif people[i][j] == 'B' and not visited[i][j]:
            bfs(i, j, 'B')
            enemy += man ** 2

print(army, enemy)