from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [[] for _ in range(m)]

for _ in range(n):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost))

INF = float('inf')

min_distance = [INF] * m
min_cost = [INF] * m

q = deque()
q.append((0, 0, 0))

min_distance[0] = 0
min_cost[0] = 0

while q:
    node, dist, cost = q.popleft()

    if dist > min_distance[1]:
        continue

    for next_node, edge_cost in graph[node]:
        new_dist = dist + 1
        new_cost = cost + edge_cost


        if new_dist < min_distance[next_node]:
            min_distance[next_node] = new_dist
            min_cost[next_node] = new_cost
            q.append((next_node, new_dist, new_cost))


        elif new_dist == min_distance[next_node] and new_cost < min_cost[next_node]:
            min_cost[next_node] = new_cost
            q.append((next_node, new_dist, new_cost))

print(min_cost[1])