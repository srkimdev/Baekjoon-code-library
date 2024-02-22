word = input()

second = 0

for i in word:
    if i <= 'O': #65 66 67 // 68 69 30
        second = second + (ord(i)-ord('A')) // 3 + 3

    elif i <= 'S': #80~83
        second = second + 8
    
    elif i <= 'V': #84~86
        second = second + 9
    else:
        second = second + 10

print(second) 
