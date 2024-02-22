t = int(input())

coin = [25, 10, 5, 1]

for _ in range(t):
    n = int(input())

    for i in coin:
        print(n // i, end = ' ')
        n = n % i
    print()