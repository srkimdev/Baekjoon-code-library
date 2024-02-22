from collections import deque

tooth = [deque(list(map(int, input()))) for _ in range(4)]
k = int(input())

def left_rotate(n, d):
    if n < 0:
        return False
    if tooth[n][2] != tooth[n + 1][6]:
        left_rotate(n - 1, -d) 
        tooth[n].rotate(d)
        
def right_rotate(n, d):
    if n > 3:
        return False
    if tooth[n - 1][2] != tooth[n][6]:
        right_rotate(n + 1, -d)
        tooth[n].rotate(d)

for _ in range(k):
    idx, d = map(int, input().split())
    idx -= 1 #인덱스화

    left_rotate(idx - 1, -d)
    right_rotate(idx + 1, -d)

    tooth[idx].rotate(d)

score = 0
for i in range(len(tooth)):
    if tooth[i][0] == 1:
        score += 2 ** i

print(score)

