import sys
input = sys.stdin.readline

n, m = map(int, input().split())

price = []
for _ in range(m):
    price.append(int(input()))

mx = 0
if n > m:
    price.sort()
    for i in range(m):
        if price[i] * (m - i) > mx:
            mx = price[i] * (m - i)
            what = price[i]
else:
    price.sort(reverse = True)
    price = price[:n]
    price.sort()
    for i in range(n):
        if price[i] * (n - i) > mx:
            mx = price[i] * (n - i)
            what = price[i]

print(what, mx)