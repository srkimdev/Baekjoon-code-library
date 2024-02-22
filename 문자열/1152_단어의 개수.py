sentence = input()

count = 0

for i in sentence + ' ':
    if i == ' ':
        count += 1

if sentence[0] == ' ':
    count -= 1

if sentence[len(sentence)-1] == ' ':
    count -= 1

print(count)