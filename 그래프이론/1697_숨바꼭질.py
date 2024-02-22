from collections import deque

n, k = map(int, input().split())

visited = [False for _ in range(1000001)]
dx = [-1, 1]

def bfs(x):
    global time
    queue = deque()
    queue.append((x, time))
    visited[x] = True

    while queue:
        x, time = queue.popleft()

        if x == k:
            return

        for i in range(3):
            if i == 2:
                nx = x * 2
            else:
                nx = x + dx[i]

            if 0 <= nx < 100001 and not visited[nx]:
                visited[nx] = True
                queue.append((nx, time + 1))
                
time = 0
bfs(n)
print(time)