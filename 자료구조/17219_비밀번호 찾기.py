import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dic = {}
for _ in range(n):
    a, b = input().split()
    dic[a] = b

for _ in range(m):
    s = input().strip()
    print(dic[s])