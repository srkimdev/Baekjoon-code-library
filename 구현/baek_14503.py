from pprint import pprint

n, m = map(int, input().split())
x, y, d = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = 1

while True:
    all_clean = True
    graph[x][y] = 2 #현재구역 청소

    for _ in range(4): # 0, 1, 2, 3
        d = (d + 3) % 4
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            all_clean = False
            graph[nx][ny] == 2
            x, y = nx, ny
            count += 1
            break
    
    if all_clean:
        nx = x + dx[d - 2]
        ny = y + dy[d - 2]
        x, y = nx, ny
        if 0 <= nx < n and 0 <= ny < m and graph[x][y] == 1:
            break
print(count)