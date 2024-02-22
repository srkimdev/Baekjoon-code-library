n = int(input())

a = list(map(int, input().split()))

m = int(input())

arr = list(map(int, input().split()))

a.sort()
result = []

for i in arr:
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if i == a[mid]:
            result.append(1)
            break
        elif i < a[mid]:
            end = mid - 1
        else:
            start = mid + 1
    
    if start > end:
        result.append(0)

for i in result:
    print(i)