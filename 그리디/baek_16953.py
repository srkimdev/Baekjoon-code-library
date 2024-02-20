a, b = map(int, input().split())

count = 1
while a != b:
    temp = b

    if str(b)[-1] == '1':
        b = b // 10
        count += 1

    elif b % 2 == 0:
        b = b // 2 
        count += 1
    
    if temp == b:
        print(-1)
        break
else:
    print(count)