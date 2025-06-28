import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    heapq.heappush(heap, int(input()))

cnt = 0

while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    cost = a + b
    cnt += cost
    heapq.heappush(heap, cost)

print(cnt)