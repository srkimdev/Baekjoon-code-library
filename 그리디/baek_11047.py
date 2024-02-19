n, k = map(int, input().split())

coin = []
for _ in range(n):
    coin.append(int(input()))

result = 0
divide = 0

while True:
    mn = 1e9
    for i in coin:
        if k // i < mn and k // i != 0:
            mn = k // i
            divide = i

    k = k % divide
    result += mn

    if k == 0:
        print(result)
        break