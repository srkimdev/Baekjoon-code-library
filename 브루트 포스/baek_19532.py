value = list(map(int, input().split()))

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (value[0] * i + value[1] * j == value[2]) and (value[3] * i + value[4] * j == value[5]):
            print(i, j)
            break 
            