import sys
input = sys.stdin.readline

n = int(input())
island = list(map(int, input().split()))
island.sort()
print(sum(island[:-1]))