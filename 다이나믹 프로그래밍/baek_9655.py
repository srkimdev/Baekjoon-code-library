n = int(input())

d = [0] * (n + 1)

for i in range(1, n + 1):
    if i % 2 == 0:
        d[i] = 'CY'
    else:
        d[i] = 'SK'
print(d[n])