x = int(input())
a = x
i = 0

while True:
    if a <= 0:
        break
    i = i + 1
    a = a - i

pyramid = [k for k in range(1, i)] # 0

rest = x - sum(pyramid) # 1-0 = 1

bunja = [k for k in range(1, i+1)] # 1

if i % 2 == 0: 
    print(bunja[rest-1], end='')
    print('/', end='')
    print(bunja[len(bunja)-rest])
else:
    print(bunja[len(bunja)-rest], end='')
    print('/', end='')
    print(bunja[rest-1], end='')