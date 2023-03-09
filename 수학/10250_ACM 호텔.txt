t = int(input())

for i in range(t):
  h, w, n = map(int, input().split())

  height = n % h 
  room = n // h + 1

  if height == 0:
    height = h
    room = n // h

  if room <= 9:
    print(str(height)+"0"+str(room))

  else:
    print(str(height)+str(room))