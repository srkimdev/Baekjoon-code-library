k, n = map(int, input().split())

wire = []
for i in range(k):
    wire.append(int(input()))

start = 1 #start => 1
end = max(wire)

while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in wire: 
        total += (i // mid)
    if total >= n: 
        start = mid + 1
    else: 
        end = mid - 1

print(end)
