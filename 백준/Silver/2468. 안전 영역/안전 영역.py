import sys
input = sys.stdin.readline
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    
    while q:
        a, b = q.popleft()
        
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]

            if(x < n and y < n and x >= 0 and y >= 0):
                if(visited[x][y] == False and graph[x][y] > r):
                    visited[x][y] = True
                    q.append((x, y))

cnts = []

for r in range(max(map(max, graph)) + 1):
    visited = [[False] * n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for k in range(n):
            if(graph[i][k] > r and not visited[i][k]):
                bfs(i, k)
                cnt += 1
    
    cnts.append(cnt)

print(max(cnts))