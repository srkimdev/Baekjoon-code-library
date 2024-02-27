docu = input()
word = input()

count = 0
s = 0

for i in range(len(docu)):
    if i < s:
        continue

    elif docu[i] == word[0]:
        if docu[i:i + len(word)] == word:
            count += 1
            s = i + len(word)
print(count)
        
