import sys
input = sys.stdin.readline

r, c = map(int, input().split())
maps = []
for _ in range(r):
    maps.append(list(map(str, input().strip())))

visited = [[0] * c for _ in range(r)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 바다 찾기
def find_sea(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            visited[x][y] += 1

        if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] == '.':
            visited[x][y] += 1

# visited에 바다의 개수 기록
for i in range(r):
    for j in range(c):
        if maps[i][j] == 'X':
            find_sea(i, j)

# 바다의 개수가 3개 이상일 경우에는 .으로 바꾸기
for i in range(r):
    for j in range(c):
        if visited[i][j] >= 3:
            maps[i][j] = '.'

INF = int(1e9)
mx, my, lx, ly = 0, 0, INF, INF

# 맵에 있는 X좌표의 최대와 최소값 찾기
for i in range(r):
    for j in range(c):
        if maps[i][j] == 'X':
            mx = max(mx, i)
            my = max(my, j)
            lx = min(lx, i)
            ly = min(ly, j)
            
# 최대, 최소 좌표만큼만 map에서 가져와서 출력
for i in range(lx, mx + 1):
    new_map = ''
    for j in range(ly, my + 1):
        new_map += maps[i][j]
    print(new_map)
        