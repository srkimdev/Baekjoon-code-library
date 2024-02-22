n = int(input())

graph = []
for _ in range(n):
    graph.append(list(input()))

dx = [0, 0, 1] #서동남
dy = [-1, 1, 0]
flag = False

#머리찾기
for i in range(n):
    for j in range(n): 
        if graph[i][j] == '*':
            head_x, head_y = i, j
            flag = True
            break
    if flag == True:
        break

#심장찾기
heart_x = head_x + 1
heart_y = head_y
print(heart_x + 1, heart_y + 1)

def dfs(x, y, d):
    global count
    nx = x + dx[d]
    ny = y + dy[d]

    if nx < 0 or ny < 0 or nx >= n or ny >= n:
        return count
    
    if graph[nx][ny] == '*':
        count += 1
        store.append((nx, ny))
        dfs(nx, ny, d)

    return count

store = []
for i in range(3):
    count = 0
    print(dfs(heart_x, heart_y, i), end = ' ') #오른쪽팔

x, y = store.pop()

leftlegx, leftlegy = x + 1, y - 1 #왼쪽 다리 좌표
rightlegx, rightlegy = x + 1, y + 1 #오른쪽 다리 좌표
count = 1
print(dfs(leftlegx, leftlegy, 2), end = ' ')
count = 1
print(dfs(rightlegx, rightlegy, 2))




