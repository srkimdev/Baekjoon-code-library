n = int(input())
arr = [[0 for j in range(100)] for i in range(100)]
count = 0

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1

for i in range(100):
    for j in range(100):
        if(arr[i][j] == 1):
            count += 1

print(count)