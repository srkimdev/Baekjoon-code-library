n, m = map(int, input().split())

basket = [i+1 for i in range(n)] # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(m):
    i, j, k = map(int, input().split())

    basket = basket[0:i-1] + basket[k-1:j] + basket[i-1:k-1] + basket[j:n]  

for i in basket:
    print(i, end = ' ')