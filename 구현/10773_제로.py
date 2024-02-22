n = int(input())

b = []

for i in range(n):
  a = int(input())

  if a == 0:
    b.pop()
  else:
    b.append(a)

print(sum(b))
