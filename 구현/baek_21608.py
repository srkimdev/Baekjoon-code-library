n = int(input())
p = n * n #시간초과 방지

board = [[0] * n for _ in range(n)]
like_room = [[] for _ in range(p + 1)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(p):
    student = list(map(int, input().split()))
    like = student[1:]
    like_room[student[0]] = like

    temp = []
    for i in range(n):
        for j in range(n):
            blank, prefer = 0, 0

            if board[i][j] != 0:
                continue

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                if board[nx][ny] in like:
                    prefer += 1
                if board[nx][ny] == 0:
                    blank += 1
                    
            temp.append((prefer, blank, i, j))
    temp.sort(key = lambda x : (-x[0], -x[1], x[2], x[3]))
    board[temp[0][2]][temp[0][3]] = student[0]

sum_result = 0
for i in range(n):
    for j in range(n):
        result = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] in like_room[board[i][j]]:
                result += 1
        
        if result != 0:
            sum_result += 10 ** (result - 1)
print(sum_result)