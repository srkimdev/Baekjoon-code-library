n = int(input())

i = 0
n = n - 1
i += 1

while True:
    if n < 1:
        break
    n = n - 6 * i
    i += 1

print(i)