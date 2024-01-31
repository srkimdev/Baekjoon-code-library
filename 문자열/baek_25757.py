n, game = input().split()

d = {}

participant = []
for i in range(int(n)):
    participant.append(input())

for i in participant:
    d[i] = d.get(i, 0) + 1

if game == 'Y':
    play = 1
elif game == 'F':
    play = 2
elif game == 'O':
    play = 3

print(len(d) // play)
