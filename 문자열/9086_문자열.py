number = int(input())

for i in range(number):
    letter = input()
    print(letter[0], end='')
    print(letter[len(letter)-1])