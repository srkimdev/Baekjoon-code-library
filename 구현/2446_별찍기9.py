n = int(input())

for i in range(2*n - 1):
    if i >= n:
        print(' ' * (2 * n -2 - i) + '*' * (2 * (i-n+1)+1))
    else:
        print(' ' * i + '*' * (2 * n - 1 - 2 * i))