import sys
input = sys.stdin.readline

n = int(input())
graph = [[0] * (n + 1)]
total = 0
for _ in range(1, n + 1):
    data = [0] + list(map(int, input().split()))
    total += sum(data)
    graph.append(data)

def area_sum(x, y, d1, d2):
    area = [0] * 5
    temp = [[0] * (n + 1) for _ in range(n + 1)]
    temp[x][y] = 5

    for i in range(1, d1 + 1):
        temp[x + i][y - i] = 5
        temp[x + d2 + i][y + d2 - i] = 5

    for i in range(1, d2 + 1):
        temp[x + i][y + i] = 5
        temp[x + d1 + i][y - d1 + i] = 5

    #1번 구역
    for i in range(1, x + d1):
        for j in range(1, y + 1):
            if temp[i][j] == 5:
                break
            area[0] += graph[i][j]

    # 2번 구역
    for i in range(1, x + d2 + 1):
        for j in range(n, y, -1):
            if temp[i][j] == 5:
                break
            area[1] += graph[i][j]

    # 3번 구역
    for i in range(x + d1, n + 1):
        for j in range(1, y - d1 + d2):
            if temp[i][j] == 5:
                break
            area[2] += graph[i][j]

    #4번 구역
    for i in range(x + d2 + 1, n + 1):
        for j in range(n, y + d2 - d1 - 1, -1):
            if temp[i][j] == 5:
                break
            area[3] += graph[i][j]

    area[4] = total - sum(area)
            
    return max(area) - min(area)

mn = int(1e9)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for d1 in range(1, n + 1):
            for d2 in range(1, n + 1):
                if i < i + d1 + d2 <= n and 1 <= j - d1 < j < j + d2 <= n:
                    mn = min(mn, area_sum(i, j, d1, d2))
print(mn)

