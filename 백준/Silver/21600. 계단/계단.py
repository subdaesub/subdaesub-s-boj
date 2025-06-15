import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
left = 1
left_max = 1

i = 1
while i < n:
    if arr[i] > left:
        left += 1
        left_max = max(left_max, left)
    else:
        i -= (arr[i] - 1)
        if i <= 0:
            i = 1
        left_max = max(left_max, left)
        left = 1
    i += 1
print(left_max)