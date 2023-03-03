n, m = map(int, input().split())

basket = [i for i in range(1, n+1)] #[1, 2, 3, 4 ,5]

for a in range(m):
    i, j = map(int, input().split())
    basket_sub = basket[i-1:j]
    basket_sub.reverse()
    basket = basket[0:i-1] + basket_sub + basket[j:n]

for b in basket:
    print(b, end = ' ')