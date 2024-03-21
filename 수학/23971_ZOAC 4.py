h, w, n, m = map(int, input().split())
count1, count2 = 0, 0

for i in range(0, h, n + 1):
    count1 += 1
for j in range(0, w, m + 1):
    count2 += 1
print(count1 * count2)