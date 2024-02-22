n = int(input())
result = 0

i = 1
while True:
    result += i

    if result > n:
        print(i - 1)
        break
    i += 1
