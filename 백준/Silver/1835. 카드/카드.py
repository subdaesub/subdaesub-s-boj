import sys
input = sys.stdin.readline

n = int(input())

arr = []
new = []

for i in range(1, n + 1):
    arr.append(i)

for i in range(1, n + 1):
    for j in range(i):
        tmp = arr[0]
        arr = arr[1:] + [tmp]
    new.append(arr[0])
    arr = arr[1:]

for i in range(n):
    print(new.index(i + 1) + 1, end=' ')