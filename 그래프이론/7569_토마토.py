from collections import deque

m, n, h = map(int, input().split())

dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

def bfs():
    while queue:
        z, y, x = queue.popleft()

        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and box[nz][ny][nx] == 0:
                box[nz][ny][nx] = box[z][y][x] + 1
                queue.append((nz, ny, nx))

day = 0
queue = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                queue.append((i, j, k))

bfs()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 0:
                print(-1)
                exit()
            
            elif box[i][j][k] > day:
                day = box[i][j][k]
print(day - 1)
