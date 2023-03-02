blank = []
count = 0

for i in range(0, 9):
    a = int(input())
    blank.append(a)

maximum = max(blank)

for i in blank:
    count += 1
    if maximum == i:
        save = count

print(maximum)
print(save)