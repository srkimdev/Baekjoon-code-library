n = int(input())

li = list(map(int, input().split()))

new_li = []

m = max(li)

for i in li:
    j = i / m * 100
    new_li.append(j)

print(sum(new_li)/n)