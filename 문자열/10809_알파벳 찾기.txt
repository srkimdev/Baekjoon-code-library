s = input()

alist = list(map(chr, range(97, 123)))
result = []

for i in alist: #c
    if i in s: #baekjoon 
        result.append(s.index(i))
    else:
        result.append(-1)

for j in result:
    print(j, end = ' ')