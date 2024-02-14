h, w = map(int, input().split())

block = list(map(int, input().split()))

graph = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(len(block)):
        if block[j] != 0:
            graph[i][j] = 1
            block[j] -= 1

result = 0
#graph = [[1, 0, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [0, 0, 0, 1]]
for i in graph: #한층씩 조사
    flag = False
    one = []
    for j in range(len(i)):
        if i[j] == 1:
            one.append(j)
    for k in range(len(one) - 1):
        if one[k + 1] - one[k] > 1:
            result += one[k + 1] - one[k] - 1
    
print(result)