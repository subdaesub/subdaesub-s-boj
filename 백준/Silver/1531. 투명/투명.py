pic =[[0 for _ in range(0, 100)] for _ in range(0, 100)]
n, m = map(int, input().split())
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1 - 1, x2):
        for k in range(y1 - 1,y2):
            pic[j][k] += 1
cnt = 0
for i in range(0, 100):
    for j in range(0, 100):
        if pic[i][j] > m:
            cnt += 1
print(cnt)