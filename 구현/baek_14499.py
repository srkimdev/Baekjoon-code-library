from pprint import pprint

n, m, x, y, k = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

move = list(map(int, input().split()))

def turn(direction):
    if direction == 1:
        dice[0], dice[1], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[1]
    elif direction == 2:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[5], dice[1], dice[0]
    elif direction == 3:
        dice[0], dice[1], dice[2], dice[3] = dice[2], dice[3], dice[1], dice[0]
    else:
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[2], dice[0], dice[1]

dice = [0, 0, 0, 0, 0, 0] #위 아래 앞 뒤 왼 오
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in move: #1234
    nx = x + dx[i - 1]
    ny = y + dy[i - 1]

    if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue

    turn(i)

    if board[nx][ny] == 0:
        board[nx][ny] = dice[1]
    elif board[nx][ny] != 0:
        dice[1] = board[nx][ny]
        board[nx][ny] = 0
    
    x, y = nx, ny
    print(dice[0])
    


    
