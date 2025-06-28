n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

w, h = 0, 0

for i in range(n):
    flag = False
    for j in range(n - 1):
        if arr[i][j:j + 2] == '..':
            if not flag:
                w += 1
                flag = True
        else:
            flag = False

for i in range(n):
    flag = False
    for j in range(n - 1):
        if arr[j][i] + arr[j + 1][i] == '..':
            if not flag:
                h += 1
                flag = True
        else:
            flag = False

print(w, h)