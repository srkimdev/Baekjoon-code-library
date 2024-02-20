a, b = input().split()

for i in a:
    if i == '6':
        a = a.replace(i, '5')

for i in b:
    if i == '6':
        b = b.replace(i, '5')

print(int(a) + int(b), end = ' ')

for i in a:
    if i == '5':
        a = a.replace(i, '6')

for i in b:
    if i == '5':
        b = b.replace(i, '6')

print(int(a) + int(b))


