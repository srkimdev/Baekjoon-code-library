n = int(input())

for i in range(1, n + 1):
    word = str(i) #198
    hap = 0
    for j in word:
        hap += int(j)
    hap += i 
    if hap == n:
        print(i)
        break
    if i == n:
        print(0)
