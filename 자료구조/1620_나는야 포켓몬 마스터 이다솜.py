import sys
n, m = map(int, sys.stdin.readline().split())

book = {}

for i in range(1, n + 1):
    a = sys.stdin.readline().rstrip()
    book[i] = a
    book[a] = i

for i in range(m):
    a = sys.stdin.readline().rstrip()
    if a.isdigit():
        print(book[int(a)])
    else:
        print(book[a])