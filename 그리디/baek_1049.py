n, m = map(int, input().split())

six_mn = 1e9
one_mn = 1e9

for _ in range(m):
    a, b = map(int, input().split())
    six_mn = min(six_mn, a)
    one_mn = min(one_mn, b)

if six_mn > one_mn * 6:
    result = one_mn * n

else:
    result = six_mn * (n // 6)

    if (n % 6) * one_mn > six_mn:
        result += six_mn
    else:
        result += (n % 6) * one_mn

print(result)