N = int(input())

count = 0

li = map(int, input().split())

v = int(input())

for i in li:
    if v == i:
        count += 1

print(count)