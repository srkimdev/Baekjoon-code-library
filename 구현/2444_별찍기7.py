n = int(input())

for i in range(2*n - 1):
    if i >= n: 
        print(' ' * (i - n + 1) + '*' * (2*n-1 - 2*(i-n+1)))
    else: 
        print(' ' * (n-1-i) + '*' * (2*i+1))