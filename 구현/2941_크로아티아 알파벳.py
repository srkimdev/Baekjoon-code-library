word = input()

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0

for i in croatia: 
    count = count + word.count(i)
    word = word.replace(i, ' ')

print(count + len(word.replace(' ', '')))