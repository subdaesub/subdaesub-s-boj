import sys
input = sys.stdin.readline

def mod(list, a, b):
    for i in range(a - 1, b):
        list[i] = list[i]**2 % 2010
    return list

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 1:
        arr = mod(arr, a, b)
    else:
        print(sum(arr[a - 1:b]))