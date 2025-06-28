graph = []
cnt = 0
for _ in range(8):
    graph.append(input())
for i in range(8):
    if i % 2 == 0:
        for j in [0, 2, 4, 6]:
            if graph[i][j] == 'F':
                cnt += 1
    else:
        for j in [1, 3, 5, 7]:
            if graph[i][j] == 'F':
                cnt += 1
print(cnt)