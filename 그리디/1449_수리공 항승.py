n, l = map(int, input().split())

location = list(map(int, input().split()))
location.sort()

d = [0] * 2002

count = 0
for i in location:
    if d[i] == 0:
        for j in range(l):
            d[i + j] = 1
        count += 1

print(count)