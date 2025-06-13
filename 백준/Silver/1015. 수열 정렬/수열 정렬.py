import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
res = [0] * n
rank = 0

cnt = 0

while cnt < n:
    min_val = min(arr)
    for i in range(n):
        if arr[i] == min_val:
            res[i] = rank
            arr[i] = float('inf')
            rank += 1
            cnt += 1

print(*res)