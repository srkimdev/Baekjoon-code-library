n = int(input())
money = list(map(int, input().split()))
m = int(input())

money.sort()
start = 0
end = max(money)

while start <= end:
    total = 0
    mid = (start + end) // 2 #128
    for i in money:
        if i > mid: 
            total += mid
        else:
            total += i #

    if total <= m:
        start = mid + 1 #128
    else:
        end = mid - 1 #127

print(end)