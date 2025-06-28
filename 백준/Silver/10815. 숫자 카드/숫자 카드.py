from bisect import bisect_left

n = int(input())
arr_n = list(map(int, input().split()))
arr_n.sort()
m = int(input())
arr_m = list(map(int, input().split()))
for i in arr_m:
    idx = bisect_left(arr_n, i)
    if idx < len(arr_n) and arr_n[idx] == i:
        print('1', end = ' ')
    else:
        print('0', end = ' ')