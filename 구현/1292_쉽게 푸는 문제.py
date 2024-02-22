a, b = map(int, input().split())
sequence = []

for i in range(1, b):
    for j in range(i):
        sequence.append(i)
        
print(sum(sequence[a-1:b]))
