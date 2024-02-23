from collections import deque
import sys

r, c = map(int, input().split())

board = []
for _ in range(r):
    board.append(list(map(str, sys.stdin.readline().rstrip())))

visited = [[0] * c for _ in range(r)]
hedge = [[0] * c for _ in range(r)]
temp = [[0] * c for _ in range(r)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y = 0, 0 #고슴도치 좌표
d_x, d_y = 0, 0 #굴 좌표

def bfs_water():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if visited[nx][ny] == 0 and board[nx][ny] == '.':
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

def bfs_hedgehog(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            temp[nx][ny] = hedge[x][y] + 1

            if (visited[nx][ny] > temp[nx][ny] or visited[nx][ny] == 0) and hedge[nx][ny] == 0 and board[nx][ny] != 'X':
                hedge[nx][ny] = temp[nx][ny]
                queue.append((nx, ny))

# 고슴도치 찾기
for i in range(r):
    for j in range(c):
        if board[i][j] == 'S':
            visited[i][j] = -1
            x, y = i, j
            break

# 굴 찾기
for i in range(r):
    for j in range(c):
        if board[i][j] == 'D':
            d_x, d_y = i, j
            break

# 물 BFS값 입력
queue = deque()
for i in range(r):
    for j in range(c):
        if board[i][j] == '*':
            queue.append((i, j))

bfs_water()
bfs_hedgehog(x, y)

if hedge[d_x][d_y] == 0:
    print('KAKTUS')
else:
    print(hedge[d_x][d_y])


