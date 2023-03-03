n, m = map(int, input().split())

basket = [i for i in range(1, n+1)]

for b in range(m):
    i, j = map(int, input().split())
    a = basket[i-1]
    basket[i-1] = basket[j-1] 
    basket[j-1] = a

for b in basket:
    print(b, end = ' ')