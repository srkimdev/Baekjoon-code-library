import sys
input = sys.stdin.readline

n, c = map(int, input().split())

home = []
for _ in range(n):
    home.append(int(input()))

home.sort()

start = 1
end = home[-1] - home[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    current = home[0]
    count = 1
    
    for i in range(1, len(home)):
        if home[i] >= current + mid:
            count += 1
            current = home[i]
    
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)


