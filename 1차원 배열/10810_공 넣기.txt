n, m = map(int, input().split())

basket = []
for i in range(n):
    basket.append(0)

for count in range(m):
    i, j, k = map(int, input().split())
    for y in range(i, j+1):
        basket[y-1] = k

for i in basket:
    print(i, end = ' ')