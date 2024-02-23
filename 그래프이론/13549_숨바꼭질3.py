from collections import deque

n, k = map(int, input().split())

INF = 100001
visited = [False] * INF

def bfs(x, time):
    queue = deque()
    queue.append((x, time))
    visited[x] = True

    while queue:
        x, time = queue.popleft()
        if x == k:
            print(time)
            return
            
        for nx in (x * 2, x - 1, x + 1):
            if 0 <= nx < INF and not visited[nx]:
                if nx == x * 2:
                    visited[nx] = True
                    queue.append((nx, time))
                else:
                    visited[nx] = True
                    queue.append((nx, time + 1))

time = 0
bfs(n, time)