n, l = map(int, input().split())

height = list(map(int, input().split()))
height.sort()

for i in height:
    if l >= i:
        l += 1
    else:
        print(l)
        exit()
print(l)
