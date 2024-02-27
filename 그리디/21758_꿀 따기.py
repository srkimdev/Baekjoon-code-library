import sys
input = sys.stdin.readline

n = int(input())
honey = list(map(int, input().split()))

hap = []
hap.append(honey[0])
for i in range(1, n):
    hap.append(hap[i - 1] + honey[i])

mx = 0
#벌 / 벌 / 물통
for i in range(1, n - 1):
    mx = max(mx, hap[n - 1] - honey[0] - honey[i] + hap[n - 1] - hap[i])

#물통 / 벌 / 벌
for i in range(1, n - 1):
    mx = max(mx, hap[n - 2] + hap[i - 1] - honey[i])
    
#벌 / 물통 / 벌
for i in range(1, n - 1):
    mx = max(mx, hap[n - 2] - honey[0] + honey[i])

print(mx)
