import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

left = [1] * n
right = [1] * n

for i in range(1, n):
    if arr[i - 1] <= arr[i]:
        left[i] = left[i - 1] + 1

for i in range(n - 2, -1, -1):
    if arr[i + 1] <= arr[i]:
        right[i] = right[i + 1] + 1

max_width = 0
for i in range(n):
    width = left[i] + right[i] - 1
    max_width = max(max_width, width)

print(max_width)