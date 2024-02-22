from collections import deque
from pprint import pprint

r, c, t = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(map(int, input().split())))

dx = [0, -1, 0, 1] #동북서남
dy = [1, 0, -1, 0] 
time = 0
robot = 0

def dust_update(x, y):
    count = 0
    for i in range(4):
        nx = x + dx[i] 
        ny = y + dy[i] 
        if nx < 0 or ny < 0 or nx >= r or ny >= c or graph[nx][ny] == -1:
            continue
        change[nx][ny] += graph[x][y] // 5
        count += 1 
    change[x][y] -= (graph[x][y] // 5 * count)

def counter_clock_wise(robot):
    x, y, d = robot, 0, 0
    temp = 0
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if nx > robot or nx < 0 or ny < 0 or ny >= c: 
            d = (d + 1) % 4
            continue
        if nx == robot and ny == 0:
            break
        graph[nx][ny], temp = temp, graph[nx][ny]
        x, y = nx, ny

def clock_wise(robot):
    x, y, d = robot, 0, 0
    temp = 0
    while True:
        nx = x + dx[d]
        ny = y + dy[d]

        if nx < robot or nx >= r or ny < 0 or ny >= c: 
            d = (d + 3) % 4
            continue
        if nx == robot and ny == 0:
            break
        graph[nx][ny], temp = temp, graph[nx][ny]
        x, y = nx, ny

for i in range(r): #공기청정기 위치 찾기
    if graph[i][0] == -1:
        robot = i
        break

while True:
    time += 1
    queue = deque()
    change = [[0] * c for _ in range(r)]

    for i in range(r): #먼지 찾고 큐에 넣기
        for j in range(c):
            if graph[i][j] != 0 and graph[i][j] != -1:
                queue.append((i, j))

    for _ in range(len(queue)): #먼지 업데이트
        x, y = queue.popleft()
        dust_update(x, y)

    for i in range(r): #먼지 업데이트
        for j in range(c):
                graph[i][j] += change[i][j]

    counter_clock_wise(robot)
    clock_wise(robot + 1)

    if time == t:
        break

total = 0
for i in range(r):
    for j in range(c):
        total += graph[i][j]
print(total + 2)