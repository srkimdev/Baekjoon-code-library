n = int(input())

meeting = []
for _ in range(n):
    meeting.append(list(map(int, input().split())))

meeting.sort(key = lambda x : (x[1], x[0]))

last_end = 0
count = 0

for start, end in meeting:
    if last_end <= start: 
        count += 1
        last_end = end

print(count)