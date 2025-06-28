import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    cnt = 1
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    arr.sort()
    best = arr[0][1]
    for i in range(1, n):
        if arr[i][1] < best:
            cnt += 1
            best = arr[i][1]
    print(cnt)