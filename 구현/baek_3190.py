from pprint import pprint
from collections import deque

n = int(input())
k = int(input()) 

board = [[0] * n for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 8

board[0][0] = 1

l = int(input())

turn = []
for _ in range(l):
    turn.append(list(input().split()))
# turn = [[3, D], [15, L], [17, D]]
directions = ['U', 'R', 'D', 'L'] #위 오 아 왼
dx = [-1, 0, 1, 0] # 위 오 아 왼
dy = [0, 1, 0, -1]

time = 0
current_direction = 'R'
x, y = 0, 0 # 현재 위치
tail_x, tail_y = 0, 0 #꼬리의 좌표
snake = deque()
snake.append([x, y])

while True:
    time += 1
    #방향에 따라 head의 위치를 조정하는 코드
    for direction in directions: # URDL
        if direction == current_direction:
            nx = x + dx[directions.index(direction)]
            ny = y + dy[directions.index(direction)]

    if nx < 0 or ny < 0 or nx >= n or ny >= n: #벽에 부딪히면
        break
    if board[nx][ny] == 1:
        break

    if board[nx][ny] == 8:
        snake.append([nx, ny])
    else:
        snake.append([nx, ny])
        x, y = snake.popleft()
        board[x][y] = 0
    
    board[nx][ny] = 1

    for i in turn: # turn = [[3, D], [15, L], [17, D]]
        if time == int(i[0]): #시간이 맞다면
            if i[1] == 'D':
                current_direction = directions[(directions.index(current_direction) + 1) % 4]
            elif i[1] == 'L':
                current_direction = directions[(directions.index(current_direction) - 1)]

    x, y = nx, ny #현재위치 갱신

print(time)
