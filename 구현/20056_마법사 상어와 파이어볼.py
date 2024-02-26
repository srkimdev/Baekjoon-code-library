import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
fireball = []
for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    fireball.append([r - 1, c - 1, m, s, d])

graph = [[[] for _ in range(n)] for _ in range(n)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1] #북동남서
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(k):
    while fireball:
        r, c, nm, ns, nd = fireball.pop(0)
        nr = (r + ns * dx[nd]) % n
        nc = (c + ns * dy[nd]) % n
        graph[nr][nc].append([nm, ns, nd])

    for i in range(n):
        for j in range(n):
            if len(graph[i][j]) >= 2:
                nm, ns, cnt_even, cnt_odd, cnt = 0, 0, 0, 0, len(graph[i][j])
                while graph[i][j]:
                    m, s, d = graph[i][j].pop(0)
                    nm += m
                    ns += s

                    if d % 2 == 0:
                        cnt_even += 1
                    else:
                        cnt_odd += 1

                if cnt_even == cnt or cnt_odd == cnt:
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]

                if nm // 5 != 0:
                    for d in nd:
                        fireball.append([i, j, nm // 5, ns // cnt, d])

            elif len(graph[i][j]) == 1:
                fireball.append([i, j] + graph[i][j].pop())

total = 0
for i in fireball:
    total += i[2]
print(total)     