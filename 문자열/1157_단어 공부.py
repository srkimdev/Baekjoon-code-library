word = input()

alphabet = [chr(i) for i in range(97, 123)] #[a, b, c, ,,, z]

alphabet_count = list(0 for i in range(97, 123)) #[0, 0, ,,, 0]

for i in word.lower(): #mississipi abcdefghijklm
    if i in alphabet: #m
        alphabet_count[ord(i)-97] = alphabet_count[ord(i)-97] + 1

count = 0

for i in alphabet_count:
    if i == max(alphabet_count):
        count += 1

if count >= 2:
    print('?')
else:
    print(alphabet[alphabet_count.index(max(alphabet_count))].upper())