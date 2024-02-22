value = []

for i in range(5):
    value.append(int(input()))

value.sort()

print(sum(value) // 5)
print(value[2])