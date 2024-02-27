import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

sensor = list(map(int, input().split()))
sensor.sort()

dist = []
for i in range(n - 1):
    dist.append(sensor[i + 1] - sensor[i])

dist.sort()
print(sum(dist[:n - k]))
