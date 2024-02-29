import sys
input = sys.stdin.readline

n = int(input())

cow = []
for i in range(n):
    cow.append(list(map(int, input().split())))

cow.sort(key = lambda x : (x[0], x[1]))

now = 0
for k, v in cow:
    if now > k:
        now += v
    else:
        now = k + v
    
    print(now)
