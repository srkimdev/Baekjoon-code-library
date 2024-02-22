c = int(input())

for i in range(c):
    count = 0
    score = list(map(int, input().split())) #[7, 100, 95, 90, 80, 70, 60, 50]

    for i in range(1, score[0]+1): #(1, 8)
        if score[i] > (sum(score)-score[0])/score[0]: #77.8
            count += 1

    a = "{:.3f}".format(count / score[0] * 100)
    print(a, end = '')
    print('%')