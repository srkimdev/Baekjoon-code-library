n = int(input())

en = [500, 100, 50, 10, 5, 1]

rest = 1000 - n
result = 0

for i in en:
    result += rest // i
    rest = rest % i

print(result)