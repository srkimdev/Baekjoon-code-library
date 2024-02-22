s = input()
previous = s[0]

one, zero = 0, 0
if s[0] == '1':
    one += 1
else:
    zero += 1

for i in range(1, len(s)):
    if s[i] != previous:
        previous = s[i]

        if s[i] == '0':
            zero += 1
        else:
            one += 1

print(min(one, zero))

