t = int(input())

for _ in range(t):

    n = int(input()) 
    
    d1 = [0] * 41
    d2 = [0] * 41

    d1[0], d2[0] = 1, 0
    d1[1], d2[1] = 0, 1

    d1[2], d2[2] = 1, 1
    d1[3], d2[3] = 1, 2

    for i in range(4, n + 1):
        d1[i] = d1[i - 1] + d1[i - 2]
        d2[i] = d2[i - 1] + d2[i - 2]

    print(d1[n], d2[n])