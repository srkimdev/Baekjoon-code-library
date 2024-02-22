from collections import deque
n, m = map(int, input().split())
visited = [False for _ in range(101)]

board = {}
for _ in range(n + m):
    a, b = map(int, input().split())
    board[a] = b

def bfs(x):
    global count
    queue = deque()
    queue.append([x, count])
    visited[x] = True

    while queue:
        x, count = queue.popleft()

        if x == 100:
            return

        for i in range(1, 7):
            nx = x + i

            if nx > 100:
                continue
            if visited[nx]:
                continue

            if nx in board:
                nx = board[nx]
                if not visited[nx]:
                    visited[nx] = True
                    queue.append([nx, count + 1])

            else:
                visited[nx] = True
                queue.append([nx, count + 1])

count = 0
bfs(1)
print(count)
