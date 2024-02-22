number = [int(input()) for i in range(10)]

blank = []
count = 0

for j in number:
    c = j % 42
    blank.append(c)

for k in range(0, 42): #나머지 배열
    if k in blank:
        count += 1

print(count)