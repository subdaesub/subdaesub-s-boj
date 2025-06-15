import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

if len(set(arr)) == 1:
    print(min(n, arr[0]))
    sys.exit()
stair = 1
stair_max = 1

i = 1
while i < n:
    if arr[i] > stair:
        stair += 1
        stair_max = max(stair_max, stair)
    else:
        i -= (arr[i] - 1)
        if i <= 0:
            i = 1
        stair = 1
    i += 1
print(stair_max)