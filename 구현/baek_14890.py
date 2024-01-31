n, l = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

count = 0

def check_path(now):

    for i in range(len(now)):
        if i == n - 1:
            return True
            
        if now[i] == now[i + 1]:
            continue

        if abs(now[i] - now[i + 1]) > 1:
            return False
        
        if now[i] - now[i + 1] == 1:
            for k in range(l):
                if i + l >= n:
                    return False
                if now[i] == now[i + 1 + k] + 1:
                    fence[i + k + 1] = True
                else:
                    return False
                
        if now[i + 1] - now[i] == 1:
            if fence[i]:
                return False
            for k in range(l):
                if i - l + 1 < 0:
                    return False
                if now[i + 1] == now[i - k] + 1 and not fence[i - k]:
                    fence[i - k] = True
                else:
                    return False
    return True 

#가로확인
for i in range(n):
    fence = [False] * n
    if check_path(graph[i]):
        count += 1
        
#세로확인
for i in range(n):
    fence = [False] * n
    if check_path([graph[j][i] for j in range(n)]):
        count += 1

print(count)


