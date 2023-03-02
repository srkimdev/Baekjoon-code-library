li = [int(input()) for j in range(28)]

absent = []

for i in range(1, 31):
    if i not in li:
        absent.append(i)

print(min(absent))
print(max(absent))