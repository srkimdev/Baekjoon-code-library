import heapq

n = int(input())
card = []
for i in range(n):
    heapq.heappush(card, int(input()))

cost = 0
while len(card) > 1:
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    sm = a + b

    cost += sm
    heapq.heappush(card, sm)

print(cost)