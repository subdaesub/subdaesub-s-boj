n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

mine = [[0 for _ in range(n + 2)] for _ in range(n + 2)]

for i in range(n):
    for j in range(n):
        if arr[i][j] != '.':
            mine[i + 1][j + 1] = '*'
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    if mine[x][y] != '*':
                        mine[x][y] += int(arr[i][j])


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if mine[i][j] != '*' and mine[i][j] > 9:
            print('M', end = '')
        else:
            print(mine[i][j], end = '')
    print('')