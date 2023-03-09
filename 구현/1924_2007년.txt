a, b = map(int, input().split())

thirtyone = [1, 3, 5, 7, 8, 10, 12]
twentyeight = [2]
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

sum = 0

for i in range(1, a):
  if i == 0:
    break
  elif i in thirtyone:
    sum = sum + 31
  elif i in twentyeight:
    sum = sum + 28
  else:
    sum = sum + 30

sum = sum + b

print(day[sum%7])