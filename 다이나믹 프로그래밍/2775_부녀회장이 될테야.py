t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())

    people = [i for i in range(1, n + 1)]

    for i in range(k):
        new = []
        for j in range(n):
            new.append(sum(people[:j + 1]))
        people = new
    print(people[-1])