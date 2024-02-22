from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

arr.sort()

for i in range(len(find)):
    print(count_by_range(arr, find[i], find[i]), end = ' ')
    

        

