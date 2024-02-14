n, k = map(int, input().split())

belt = []

belt = list(map(int, input().split())) #내구도 저장
robot = [False] * 2 * n
level = 0 #단계

while True:
    belt = belt[-1:] + belt[:-1]
    robot = robot[-1:] + robot[:-1]
    level += 1

    if robot[n - 1] == True: #컨베이어 벨트 돌 때
        robot[n - 1] = False

    for i in range(n - 2, -1, -1):
        if robot[i] == True and not robot[i + 1] and belt[i + 1] >= 1:
            robot[i + 1] = robot[i]
            robot[i] = False
            belt[i + 1] -= 1
        else:
            continue

    if robot[n - 1] == True: #로봇이 움직일 때
        robot[n - 1] = False

    if belt[0] > 0: #내구도가 0이상이면 로봇 올려놓기
        robot[0] = True
        belt[0] -= 1

    count = belt.count(0)
    
    if count >= k:
        break

print(level)