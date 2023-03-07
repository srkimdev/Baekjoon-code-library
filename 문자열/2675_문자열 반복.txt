repeat = int(input())

for i in range(repeat):
    r, p = map(str, input().split())
    for j in p: # ABC
        print(int(r) * j, end = '')
    print()
