n = int(input())

rope = []
for _ in range(n):
    rope.append(int(input()))

rope.sort()
result = 0
mx = 0
for i in range(len(rope)):
    result = rope[i] * (len(rope) - i)
    if mx < result:
        mx = result

print(mx)
