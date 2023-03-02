n, x = map(int, input().split())

li = map(int, input().split())

blank = []

for i in li:
    if x > i:
        blank.append(i)

for i in blank:
    print(i, end = ' ')